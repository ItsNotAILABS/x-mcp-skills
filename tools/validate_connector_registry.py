#!/usr/bin/env python3
"""Validate NOVA external AI connector registry files.

Standard-library only, so it can run in a clean repo, CI job, or local agent
workspace without installing dependencies.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "connector-registry.json"

REQUIRED_FIELDS = {"id", "name", "surface", "authority", "inputs", "outputs", "proof_gates"}
VALID_SURFACES = {"cli", "mcp", "mtp", "api", "webhook", "ide", "browser", "desktop", "local-runtime"}


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def connector_items(registry: dict[str, Any]) -> list[dict[str, Any]]:
    if isinstance(registry.get("connectors"), list):
        return registry["connectors"]
    if isinstance(registry.get("external_ai_connectors"), list):
        return registry["external_ai_connectors"]
    raise AssertionError("Registry must contain `connectors` or `external_ai_connectors` array")


def validate(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        connectors = connector_items(registry)
    except AssertionError as exc:
        return [str(exc)]

    if not connectors:
        return ["Connector registry cannot be empty"]

    seen: set[str] = set()
    for index, connector in enumerate(connectors):
        label = f"connectors[{index}]"
        if not isinstance(connector, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_FIELDS - set(connector))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")

        connector_id = connector.get("id")
        if not isinstance(connector_id, str) or not connector_id.strip():
            errors.append(f"{label}.id must be a non-empty string")
        elif connector_id in seen:
            errors.append(f"duplicate connector id: {connector_id}")
        else:
            seen.add(connector_id)

        surface = connector.get("surface")
        if isinstance(surface, str) and surface not in VALID_SURFACES:
            errors.append(f"{label}.surface must be one of {sorted(VALID_SURFACES)}")

        for list_field in ("inputs", "outputs", "proof_gates"):
            value = connector.get(list_field)
            if not isinstance(value, list) or not value:
                errors.append(f"{label}.{list_field} must be a non-empty array")
            elif not all(isinstance(item, str) and item.strip() for item in value):
                errors.append(f"{label}.{list_field} must contain only non-empty strings")

    return errors


def main() -> int:
    registry = load_json(REGISTRY_PATH)
    errors = validate(registry)
    if errors:
        print("NOVA connector registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    count = len(connector_items(registry))
    print(f"NOVA connector registry validation passed: {count} connectors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
