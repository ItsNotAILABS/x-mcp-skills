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
