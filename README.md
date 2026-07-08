# x-mcp-skills

NOVA connector skills for external AI worker surfaces.

## Current Connectors

- `skills/caffeine-mtp-bridge/SKILL.md` — Caffeine CLI and Caffeine MTP/MCP-style server bridge.
- `skills/grok-build-bridge/SKILL.md` — Grok Build bridge for external planning, patching, review, MCP usage, and artifact handoff.
- `connector-registry.json` — machine-readable registry for connector discovery.

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
