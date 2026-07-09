---
name: caffeine-mtp-bridge
description: Use when NOVA needs to connect to Caffeine CLI or a Caffeine MTP/MCP-style server for build requests, tool discovery, artifact import, or Caffeine app handoff.
---

# Caffeine MTP Bridge

## Purpose

Connect NOVA to Caffeine as an external worker surface while keeping NOVA in charge of route, proof, artifact import, and operator scope.

## Supported Surfaces

- Caffeine CLI: `@caffeineai/cli` / `caffeine`
- Caffeine MTP/MCP-style server: operator-provided URL and auth/tool schema
- Caffeine web publish handoff: never claim local CLI deploy unless the tool contract proves it

## CLI Workflow

Use this when the local project should be prepared for Caffeine.

```bash
npm install -g @caffeineai/cli
caffeine auth login
caffeine auth status
caffeine doctor --fix
caffeine install
caffeine check --fix
caffeine preview --build
```

## MTP/MCP Server Workflow

Use this when Alfredo provides a Caffeine server URL or tool contract.

1. Register server URL and auth mode.
2. Discover tools/resources/prompts.
3. Record tool schema in `tool-discovery.json`.
4. Submit build request.
5. Poll task status.
6. Import artifact with hash into NOVA.
7. Record `artifact-import-manifest.json` and verification result.

## Required Operator Inputs

- Server URL, if using MTP/MCP.
- Auth mode: browser session, device login, local-only, or scoped token.
- Project path or repository target.
- Whether publish is manual web handoff or available through a verified tool.

## Proof Gates

- Auth status captured.
- Tool list captured for MTP/MCP.
- Build/check output captured.
- Artifact hash captured.
- No fake deploy claim.
- Origin and credential boundary recorded.

## NOVA Boundary Law

Caffeine can build as an external surface. NOVA owns route, proof ledger, artifact import, and deployment truth line.
