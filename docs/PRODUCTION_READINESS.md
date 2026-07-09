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
