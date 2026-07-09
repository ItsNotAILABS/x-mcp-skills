#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "connector-registry.json"


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data.get("schema") == "nova.external_connector_registry.v1", "invalid schema"
    connectors = data.get("connectors")
    assert isinstance(connectors, list) and connectors, "connectors must be a non-empty list"
    seen: set[str] = set()
    for connector in connectors:
        connector_id = connector.get("id")
        assert connector_id and connector_id not in seen, f"duplicate or missing id: {connector_id}"
        seen.add(connector_id)
        path = connector.get("path")
        assert path and (ROOT / path).exists(), f"missing skill file for {connector_id}: {path}"
        assert connector.get("surfaces"), f"missing surfaces for {connector_id}"
        assert connector.get("proof_gates"), f"missing proof gates for {connector_id}"
    print(f"validated {len(connectors)} connectors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
