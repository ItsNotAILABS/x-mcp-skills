# Connector Control Plane Working Paper

## Executive Abstract

AI coding organizations are moving toward tool pluralism. A team may use Caffeine for app generation, Grok Build for terminal coding, Codex for repository work, local agents for deployment, and MCP/MTP servers for tool access. The failure mode is fragmentation: each tool can produce output, but no system preserves authority, proof, artifact lineage, deployment truth, or customer-safe claims across the whole chain.

The NOVA External AI Connector Control Plane solves that by treating external AI systems as worker surfaces. Caffeine CLI, Caffeine MTP/MCP, Grok Build, and generic agent servers can execute work, but NOVA owns route selection, operator scope, proof gates, artifact import, and promotion logic.

## Problem

Most AI coding tools optimize for immediate code production. They do not consistently answer:

- Which worker was authorized?
- Which tools were allowed?
- What task was submitted?
- What artifact came back?
- What changed?
- What tests ran?
- What claim is safe to make to customers?

Without those answers, a multi-AI workflow becomes impressive but fragile.

## Platform Thesis

The winning product is not another isolated AI coding chat. The winning product is a control plane that lets companies use many AI workers while preserving governance, proof, and deployability.

NOVA's position:

- external AIs execute as worker surfaces
- NOVA routes and governs
- artifacts return with hashes
- proof gates decide promotion
- customer-facing claims stay tied to evidence

## Four Connector Surfaces

### Caffeine CLI

Use when a local project should follow Caffeine conventions and be prepared for Caffeine preview.

Core sequence:

1. install CLI
2. authenticate
3. run doctor
4. install dependencies
5. check project
6. preview build
7. hand off web publish if required

Critical proof gate: do not claim live deployment from CLI unless verified by the current Caffeine contract.

### Caffeine MTP/MCP

Use when Caffeine exposes a tool server that can receive tasks and return artifacts.

Core sequence:

1. register server origin
2. bind auth scope
3. discover tools/resources/prompts
4. submit build task
5. poll status
6. import artifact
7. hash artifact

Critical proof gate: tool schema must be captured before execution.

### Grok Build

Use when Grok should act as a parallel coding worker, reviewer, patcher, or MCP-enabled terminal agent.

Core sequence:

1. request plan
2. record approval boundary
3. allow scoped patch
4. capture diff
5. run tests
6. import verification

Critical proof gate: diff and test output must be captured.

### Generic Agent Server

Use when a new agent server appears before NOVA has a custom adapter.

Core sequence:

1. discover schema
2. submit task
3. poll task
4. download artifact
5. verify hash
6. register result

Critical proof gate: timeout and retry policy must be explicit.

## Product Architecture

The Connector Control Plane should expose:

- connector catalog
- credential/scope panel
- tool discovery viewer
- task composer
- run status timeline
- artifact import ledger
- verification report
- promotion decision

## Customer Value

For builders:

- stop copying outputs between AI tools manually
- keep a trace of what happened
- prove what changed
- reuse the best worker for each job

For companies:

- allow multiple AI tools without losing governance
- preserve deploy readiness
- support audit and compliance
- control customer-facing claims

## Release Readiness Criteria

The first marketable version is ready when it can:

1. register at least one CLI connector and one server connector
2. store connector registry JSON
3. produce task request JSON
4. import artifact hash
5. generate verification report
6. present a readable dashboard or README-driven operator flow

## Conclusion

The connector control plane is the missing infrastructure between AI coding tools and production deployment. NOVA should own this layer because it already treats work as route, proof, artifact, and consequence rather than disconnected generation.
# External AI Connector Control Plane: Working Paper

## Abstract

The NOVA External AI Connector Control Plane is a governance layer for using external AI systems as bounded worker surfaces. Caffeine, Grok Build, Claude, Cursor, Antigravity, local CLIs, browser workbenches, and future MCP/MTP servers can contribute planning, code, review, deployment, or artifact generation without becoming the source of truth.

The central thesis is simple: the LLM or external tool should not overshadow the platform. The platform intelligence lives in registry law, task routing, permissions, proof gates, artifact import, and consequence memory.

## 1. Problem

Modern AI development stacks are increasingly fragmented. A builder may use one tool for coding, another for design, another for research, another for deployment, and another for local terminal work. Without a control plane, this becomes prompt drift and artifact chaos.

The problem is not lack of intelligence. The problem is lack of governed interoperability.

## 2. Connector Model

A connector is a bounded worker surface with these properties:

- `id`: stable connector identifier.
- `surface`: CLI, MCP, MTP, IDE, browser, API, desktop, or local runtime.
- `authority`: what the connector may do.
- `inputs`: accepted request forms.
- `outputs`: expected artifacts.
- `proof`: required evidence before import.
- `limits`: what must remain outside the connector's authority.

## 3. Triple Adapter Pattern

Each connector should expose three faces:

1. **Human Face**: clear operator instructions and launch flow.
2. **Agent Face**: machine-readable skill, registry entry, and task contract.
3. **Runtime Face**: executable or callable adapter surface such as CLI, MCP server, webhook, or API.

This prevents docs, agents, and code from drifting into three separate products.

## 4. Task Lifecycle

1. Operator or agent submits a task request.
2. NOVA selects a connector through registry and policy.
3. Connector receives bounded instructions.
4. External worker returns artifacts, diff, logs, or analysis.
5. NOVA validates the result.
6. Proof is recorded.
7. Approved artifacts are imported into the product runtime or repo.

## 5. Trust Boundary

External AIs are not the crown authority. They are high-capability workers behind a Translatio boundary. The boundary prevents direct uncontrolled writes into trunk logic and forces evidence through import gates.

Trust is earned through:

- explicit task scope
- tool allowlists
- artifact hashes
- validation reports
- replayable receipts
- operator-readable failure states

## 6. Product Strategy

This repo becomes the connector skill catalog for NOVA Build. It should allow teams to connect external AI workers without rewriting governance logic for each tool.

The market value is not another integration list. The value is turning many AI tools into one controlled business-building organism.

## 7. Next Work

- Add live discovery adapters for Caffeine MTP and generic MCP servers.
- Add connector task receipts and replay storage.
- Add CI validation for connector registry shape.
- Add an operator CLI for `discover`, `plan`, `invoke`, `import`, and `prove`.
- Add browser dashboard cards for connector readiness.
