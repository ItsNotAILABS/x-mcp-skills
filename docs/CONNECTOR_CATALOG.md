# NOVA External AI Connector Catalog

This catalog lists the first external AI worker surfaces governed by the NOVA External AI Connector Control Plane.

## Build and Code Surfaces

| Connector | Surface | Use It For |
| --- | --- | --- |
| Caffeine CLI and MTP Bridge | CLI / MTP / MCP | Build, preview, check, package, and return app artifacts |
| Grok Build Bridge | API / MCP / headless agent | Planning, patching, review, and external build analysis |
| Claude Code Bridge | CLI / repo agent | Repo analysis, patch suggestions, code review |
| Cursor IDE Bridge | IDE | Workspace edits, code navigation, developer workflow |
| Antigravity Terminal Bridge | Local runtime | Terminal execution, dev servers, debugging, deployment prep |

## Runtime and Browser Surfaces

| Connector | Surface | Use It For |
| --- | --- | --- |
| Browser Workbench and Service Worker Bridge | Browser | Service workers, manifests, storage, WASM, console/network telemetry |
| Generic MCP Gateway | MCP | Discover arbitrary MCP tools, resources, prompts, auth, and risk |
| ChatGPT App OAuth Bridge | Browser / OAuth | User-authorized app/tool flows and permission strategy |

## Recommended GitHub Topics

`mcp`, `model-context-protocol`, `ai-connectors`, `ai-agents`, `developer-tools`, `workflow-automation`, `caffeine`, `grok-build`, `claude-code`, `cursor`, `browser-workbench`, `service-worker`, `nova`, `external-ai`.

## Primary Search Phrases

- external AI connector platform
- MCP connector registry
- AI worker surface control plane
- Caffeine MCP bridge
- Grok Build connector
- Claude Code bridge
- Cursor IDE AI workflow
- browser workbench AI platform
- service worker AI workbench
- AI artifact proof gate

## Import Rule

No connector output should enter NOVA as trusted production work until the artifact, diff, log, or receipt is captured and validated.
