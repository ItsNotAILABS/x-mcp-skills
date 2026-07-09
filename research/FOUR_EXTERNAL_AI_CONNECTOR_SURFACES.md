# Four External AI Connector Surfaces

## Thesis

NOVA should not treat external AI tools as replacements for its intelligence substrate. Caffeine CLI, Caffeine MTP/MCP, Grok Build, and generic agent servers are four worker surfaces. Their value is not that they become NOVA; their value is that NOVA can route work into them, recover artifacts, verify outputs, and preserve the proof chain.

## Surface 1: Caffeine CLI

Caffeine CLI is the local build and check surface. It should be used when a project needs Caffeine conventions, local setup, and preview validation.

Primary actions:

- authenticate
- diagnose environment
- install dependencies
- check project
- preview build
- hand off to web publish when required

Proof gates:

- auth status captured
- doctor output captured
- check output captured
- preview build output captured
- no unsupported deploy claim

## Surface 2: Caffeine MTP/MCP Server

Caffeine MTP/MCP is the remote tool-discovery and build-request surface. Until the exact contract is supplied, NOVA treats it as a configurable agent server.

Primary actions:

- register server URL
- discover tools/resources/prompts
- submit build request
- poll status
- import artifact
- hash artifact

Proof gates:

- server origin recorded
- auth scope recorded
- tool schema captured
- task id captured
- artifact hash captured

## Surface 3: Grok Build

Grok Build is the external coding-agent worker surface. It can plan, patch, review, run tools, and possibly coordinate MCP servers, but NOVA must capture the plan, approval boundary, diff, and verification.

Primary actions:

- request plan
- approve scoped files
- run patch
- capture diff
- run tests
- import verification

Proof gates:

- plan captured
- approval boundary recorded
- diff captured
- tests captured
- external model boundary noted

## Surface 4: Generic Agent Server

Generic agent servers let NOVA connect to future AI workers without rebuilding the whole connector stack.

Primary actions:

- discover schema
- submit task
- poll status
- download artifact
- verify artifact
- register result

Proof gates:

- schema captured
- task id recorded
- timeout policy recorded
- retry policy recorded
- artifact hash captured

## Architecture Law

External tools may execute, but NOVA owns:

- routing
- proof ledger
- artifact import
- connector registry
- customer-facing truth line
- deployment readiness claims

## Product Path

The first product form is a Connector Control Plane:

1. Choose worker surface.
2. Register auth and scope.
3. Submit task.
4. Watch live status.
5. Import artifact.
6. Verify and package.
7. Promote or reject.

## Market Readiness

This can be marketed as the connector layer for teams that want to use multiple AI coding tools without losing governance, proof, or deploy discipline.
