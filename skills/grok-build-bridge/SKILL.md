---
name: grok-build-bridge
description: Use when NOVA should route work to Grok Build as an external coding worker for planning, patching, review, MCP tool use, or headless/scripted agent runs.
---

# Grok Build Bridge

## Purpose

Use Grok Build as an external build/review worker while NOVA preserves the coordinating substrate, proof gates, and artifact handoff.

## Supported Surfaces

- Interactive Grok terminal session.
- Headless/scriptable Grok run.
- MCP server/tool configuration.
- AGENTS.md, skills, and hooks where the project supports them.

## Workflow

1. Install and authenticate Grok Build in the operator environment.
2. Register repo path and allowed tools.
3. Ask Grok for a plan before edits.
4. Capture approval boundary.
5. Let Grok patch only the scoped files.
6. Capture diff as `grok-diff.patch`.
7. Run tests/checks.
8. Import plan, diff, and verification into NOVA.

## Required Operator Inputs

- Repo path or GitHub repository.
- Approval mode: plan-only, patch, review, or deploy-support.
- Allowed MCP servers/tools.
- Test commands and package commands.

## Proof Gates

- Grok plan captured.
- Approval boundary recorded.
- Diff captured.
- Tests captured.
- External model boundary noted.
- NOVA handoff record written.

## NOVA Boundary Law

Grok Build may act as a strong worker, reviewer, or parallel builder. It does not replace NOVA source law, proof ledger, or deployment truth line.
