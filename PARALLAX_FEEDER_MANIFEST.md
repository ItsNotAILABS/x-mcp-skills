# PARALLAX Feeder Manifest

This repository feeds the PARALLAX authority repo:

```text
ItsNotAILABS/PARALLAX-Exchange-Clearinghouse
```

## Lane

```text
external_ai_connector_control
```

## What this repo may feed

- MCP skill manifest pointers,
- external AI connector policy summaries,
- tool invocation constraints,
- skill receipt schemas,
- operator approval requirements,
- connector boundary rules.

## What this repo must not feed

- API keys,
- tool secrets,
- connector credentials,
- unapproved autonomous external execution,
- silent mutations,
- unbounded tool dispatch.

## PARALLAX target surfaces

- AI Execution,
- Control Tower,
- Cloudflare Edge Gateway,
- Federation Registry,
- Proof Room.

## Promotion rule

A skill, connector, or external AI tool artifact from this repo becomes PARALLAX authority only after:

1. source commit or artifact hash is recorded,
2. read/write/mutation boundary is assigned,
3. operator approval requirement is declared,
4. proof or receipt expectation is mapped,
5. explicit integration PR is opened in `PARALLAX-Exchange-Clearinghouse`.

## Current boundary

This feeder may support PARALLAX connector intelligence, but it must not expose secrets or enable uncontrolled external tool execution.
