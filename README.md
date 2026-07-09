# NOVA External AI Connector Control Plane

![Status](https://img.shields.io/badge/status-draft%20platform-blue)
![MCP](https://img.shields.io/badge/MCP-connector%20contracts-0b7285)
![Connectors](https://img.shields.io/badge/external%20connectors-8-6f42c1)
![Proof](https://img.shields.io/badge/proof-artifact%20import-2f9e44)
![Registry](https://img.shields.io/badge/registry-validated-success)

![NOVA External AI Connector Control Plane](assets/connector-control-plane.svg)

NOVA External AI Connector Control Plane turns Caffeine, Grok Build, Claude Code, Cursor, Antigravity, local CLIs, IDEs, browser workbenches, ChatGPT app/OAuth surfaces, and MCP/MTP servers into governed worker surfaces.

The external AI does not become the platform. NOVA keeps the registry, routing authority, permission boundary, proof gate, artifact import, and deployment truth line.

## Search Keywords

External AI connector platform, MCP connector registry, AI worker surface control plane, Caffeine MCP bridge, Grok Build connector, Claude Code bridge, Cursor IDE AI workflow, browser workbench AI platform, service worker AI workbench, AI artifact proof gate, NOVA Build connectors.

## MDFUC Role

`x-mcp-skills` owns MCP and external AI connector skills inside the Medina Development Federation Unified Catalog.

It reports to:

- `ItsNotAILABS/nexus` for repo-family registry.
- `ItsNotAILABS/nova-intelligence` for runtime contracts.
- `ItsNotAILABS/PhantomSDK` for SDK packaging and connector clients.

## Current Connectors

| Connector | Surface | Purpose |
| --- | --- | --- |
| Caffeine CLI and MTP Bridge | CLI / MTP / MCP | Build, preview, check, and package bounded app work |
| Grok Build Bridge | API / MCP / headless agent | Plan, patch, review, and return artifacts through proof gates |
| Claude Code Bridge | CLI / repo agent | Repo analysis, code review, patch suggestions |
| Cursor IDE Bridge | IDE | Workspace edits, navigation, developer workflow |
| Antigravity Terminal Bridge | Local runtime | Terminal execution, dev servers, debugging, deployment prep |
| Browser Workbench Bridge | Browser | Service workers, storage, manifests, WASM, console/network telemetry |
| Generic MCP Gateway | MCP | Normalize arbitrary MCP servers into NOVA connector contracts |
| ChatGPT App OAuth Bridge | Browser / OAuth | User-authorized app/tool integration strategy without credential capture |

See [docs/CONNECTOR_CATALOG.md](docs/CONNECTOR_CATALOG.md) for the full connector catalog.

## Repository Map

- `connector-registry.json` — machine-readable connector contract with authority, inputs, outputs, and proof gates.
- `mcp/external-ai-connectors.mcp.json` — MCP-style resource/tool contract for connector discovery and import.
- `skills/` — connector skills for each external AI worker surface.
- `mdfuc.surface.json` — repo-family role and proof gates.
- `tools/validate_connector_registry.py` — dependency-free validation gate.
- `docs/CONNECTOR_CATALOG.md` — connector catalog, search phrases, topics, and use cases.
- `docs/CONNECTOR_CONTROL_PLANE_WORKING_PAPER.md` — working paper for the architecture.
- `docs/PRODUCTION_READINESS.md` — readiness levels and launch gates.

## Quick Start

Validate the connector registry:

```bash
python tools/validate_connector_registry.py
```

For Caffeine CLI:

```bash
npm install -g @caffeineai/cli
caffeine auth login
caffeine doctor --fix
caffeine install
caffeine check --fix
caffeine preview --build
```

For any MCP/MTP connector:

1. Provide server URL and auth mode.
2. Discover tools, resources, and prompts.
3. Capture the tool discovery response and hash.
4. Submit a bounded task request.
5. Import artifact hash into NOVA only after validation.

For IDE or terminal connectors:

1. Register workspace path and allowed files.
2. Capture a plan before edits.
3. Record approval boundary.
4. Capture diff, command output, tests, and verification notes.
5. Import artifacts into NOVA.

## MCP Tool Contract

The manifest in `mcp/external-ai-connectors.mcp.json` defines:

- `external_ai_connectors.list`
- `external_ai_connectors.describe`
- `external_ai_connectors.route_plan`
- `external_ai_connectors.import_artifact`

## Operating Law

- External AIs are worker surfaces, not crown authority.
- NOVA owns routing, proof gates, artifact import, and deployment truth line.
- No connector can claim completion without returned evidence.
- Direct trunk mutation requires explicit operator approval and proof.
- The LLM should help the product, not overshadow the product.

## GitHub Discoverability

Recommended repository topics:

`mcp`, `model-context-protocol`, `ai-connectors`, `ai-agents`, `developer-tools`, `workflow-automation`, `caffeine`, `grok-build`, `claude-code`, `cursor`, `browser-workbench`, `service-worker`, `nova`, `external-ai`.

## Readiness

Current status:

- Eight connector contracts are registered and documented.
- Registry validation is available.
- MCP-style connector manifest is present.
- Live callable adapters require operator-provided credentials, endpoints, and exact tool contracts.

Next build: add `connectorctl`, CI validation, live MCP discovery capture, and a dashboard for connector readiness and artifact import.
