# NOVA External AI Connector Control Plane

NOVA connector skills for external AI worker surfaces.

![NOVA External AI Connector Control Plane](assets/connector-control-plane.svg)

## Product Thesis

Teams are going to use many AI coding workers: Caffeine, Grok Build, Codex, local agents, MCP/MTP servers, and whatever comes next. The problem is not whether those tools can produce output. The problem is preserving scope, proof, artifact lineage, deployment truth, and customer-safe claims across all of them.

This repo is the connector skill and registry layer for that control plane.

## MDFUC Role

`x-mcp-skills` owns MCP and external AI connector skills inside the Medina Development Federation Unified Catalog.

It reports to:

- `ItsNotAILABS/nexus` for repo-family registry.
- `ItsNotAILABS/nova-intelligence` for runtime contracts.
- `ItsNotAILABS/PhantomSDK` for SDK packaging and connector clients.

## Current Connectors

- `skills/caffeine-mtp-bridge/SKILL.md` — Caffeine CLI and Caffeine MTP/MCP-style server bridge.
- `skills/grok-build-bridge/SKILL.md` — Grok Build bridge for external planning, patching, review, MCP usage, and artifact handoff.
- `connector-registry.json` — machine-readable registry for connector discovery.
- `platform/external-ai-connector-platform.json` — product/platform manifest.

## Research + Product Docs

- `research/FOUR_EXTERNAL_AI_CONNECTOR_SURFACES.md` — deep connector surface paper.
- `docs/CONNECTOR_CONTROL_PLANE_WORKING_PAPER.md` — production working paper.
- `docs/PRODUCTION_READINESS.md` — market and demo readiness guide.
- `assets/connector-control-plane.svg` — architecture image.

## Operating Law

External AIs are worker surfaces. NOVA keeps routing authority, proof gates, artifact import, and deployment truth line.

## First Use

For Caffeine CLI:

```bash
npm install -g @caffeineai/cli
caffeine auth login
caffeine doctor --fix
caffeine install
caffeine check --fix
caffeine preview --build
```

For Caffeine MTP/MCP:

1. Provide server URL and auth mode.
2. Discover tools/resources/prompts.
3. Capture `tool-discovery.json`.
4. Submit build request.
5. Import artifact hash into NOVA.

For Grok Build:

1. Register repo path and allowed tools.
2. Capture a plan before edits.
3. Record approval boundary.
4. Capture diff and verification output.
5. Import artifacts into NOVA.

## Validation

```bash
python tools/validate_connector_registry.py
```

## Market-Ready Offer

Use Caffeine, Grok Build, MCP/MTP servers, and future AI workers without losing proof, scope, artifact lineage, or deployment truth.

## Next Build

The next production slice is a small MCP-compatible server that exposes:

- `connectors.list`
- `connectors.plan_run`
- `connectors.import_artifact`
- `connectors.verify_run`
