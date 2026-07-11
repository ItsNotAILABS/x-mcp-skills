# Production Readiness Guide

## Marketable Product Name

NOVA External AI Connector Control Plane

## One-Line Offer

Use Caffeine, Grok Build, MCP/MTP servers, and future AI workers without losing proof, scope, artifact lineage, or deployment truth.

## User Promise

A builder can choose an AI worker, submit a scoped task, watch the run, import the artifact, verify the result, and decide whether it is safe to promote.

## Minimum Product Views

- Connector catalog
- Tool discovery viewer
- Task request composer
- Run status timeline
- Artifact import ledger
- Verification and promotion panel

## Production Gates

- Connector registry exists.
- Every connector declares auth mode.
- Every run declares operator scope.
- Every task has a stable id.
- Every imported artifact has a hash.
- Every verification report names pass/fail/gap.
- Every deployment claim is tied to proof.

## First Demo Script

1. Open connector catalog.
2. Choose Caffeine MTP/MCP.
3. Show required operator inputs.
4. Submit a mock build request.
5. Import a mock artifact hash.
6. Show verification report.
7. Promote or reject.

## Marketing Angles

- Multi-AI coding governance.
- AI worker orchestration for production teams.
- Proof-ledger layer for AI-generated code.
- Connector control plane for Caffeine, Grok Build, and MCP/MTP servers.

## Near-Term Build Tasks

- Add schema validation tests for `connector-registry.json`.
- Add a simple dashboard mock.
- Add a sample run folder with discovery, request, import, and verification JSON.
- Add an MCP-compatible server skeleton.
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
