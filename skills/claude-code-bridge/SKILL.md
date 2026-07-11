---
name: claude-code-bridge
description: Use when NOVA should route bounded repository analysis, code review, or patch suggestions through Claude Code while preserving NOVA proof, import, and branch authority.
---

# Claude Code Bridge

## Purpose

Treat Claude Code as an external repo worker, not as source authority. NOVA sends bounded tasks and imports only reviewed artifacts.

## Required Inputs

- Repository or workspace scope
- Allowed files or directories
- Task brief
- Review mode: analysis, patch suggestion, implementation, or verification
- Operator approval boundary

## Workflow

1. Record repository scope and allowed paths.
2. Ask Claude Code for plan or patch within the boundary.
3. Capture returned analysis, diff, tests, and risk notes.
4. Route artifacts through NOVA proof/import review.
5. Do not mark work complete until local repo proof exists.

## Proof Gates

- Scope recorded
- Diff captured
- Review notes captured
- Test or verification command captured
- NOVA import approval recorded

## Refusal Boundary

Do not route secrets, private credentials, destructive repo commands, or direct trunk mutation through this bridge.
