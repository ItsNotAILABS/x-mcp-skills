# Production Readiness: NOVA External AI Connectors

## Product Name

**NOVA External AI Connector Control Plane**

## One-Line Offer

Connect external AI systems as governed worker surfaces so teams can route work to Caffeine, Grok Build, Claude, Cursor, Antigravity, CLIs, and MCP servers without losing permission boundaries, proof, or artifact control.

## Readiness Levels

| Level | Name | Gate |
| --- | --- | --- |
| L0 | Described | Connector idea exists |
| L1 | Registered | Connector is in `connector-registry.json` |
| L2 | Documented | Skill and operator instructions exist |
| L3 | Callable | CLI, API, webhook, MCP, or MTP call path exists |
| L4 | Proved | Artifacts, logs, validation, and receipt exist |
| L5 | Productized | Dashboard, CI, auth, and support docs exist |

## Current Status

- Caffeine CLI and MTP/MCP-style bridge: L2, pending live endpoint credentials and discovery output for L3.
- Grok Build bridge: L2, pending live callable workflow for L3.
- Generic external AI connector pattern: L2, pending shared runtime adapter.

## Production Gates

- Registry validates.
- Each connector has scope, surface, authority, inputs, outputs, and proof requirements.
- External execution is never marked complete without returned evidence.
- Artifact import records source, time, hash, and validation status.
- Human operator can understand what was allowed, what ran, what changed, and what remains unverified.

## Launch Workflow

1. Register connector.
2. Validate registry.
3. Discover tools/resources/prompts if the connector is MCP/MTP.
4. Submit bounded request.
5. Capture returned artifact and execution metadata.
6. Validate output.
7. Import into NOVA only after proof gate passes.

## Next Engineering Tasks

- Add `connectorctl` CLI.
- Add JSON Schema for `connector-registry.json`.
- Add CI validation.
- Add live MCP discovery examples.
- Add OAuth/auth strategy notes for external surfaces.
- Add operator dashboard for connector status and artifact import.
