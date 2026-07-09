---
name: antigravity-terminal-bridge
description: Use when NOVA should route local terminal, Antigravity-style workspace, dev server, debugging, or deployment-prep workflows through a governed command/proof boundary.
---

# Antigravity Terminal Bridge

## Purpose

Treat terminals as talk-back substrates. Commands produce stdout, stderr, exit codes, file deltas, process state, URLs, and logs. NOVA records those signals before claiming success.

## Required Inputs

- Workspace state
- Intended command or command family
- Dev server or deployment target
- Risk level
- Operator approval for destructive actions

## Workflow

1. Classify command intent: read, write, test, server, deploy, network, or destructive.
2. Require approval for destructive or credential-bearing commands.
3. Capture command, exit code, logs, and runtime URL.
4. Convert output into a proof event or failure report.
5. Hand off to CI, proof, or launch bot as needed.

## Proof Gates

- Command captured
- Exit code captured
- Runtime URL or artifact captured when applicable
- Unsafe command review completed

## Refusal Boundary

Do not run destructive commands, secret exfiltration, privilege escalation, or unbounded code execution through this bridge.
