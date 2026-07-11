---
name: generic-mcp-gateway
description: Use when NOVA should discover, normalize, and govern arbitrary MCP servers through tool/resource/prompt discovery, auth boundaries, and proof-gated task invocation.
---

# Generic MCP Gateway

## Purpose

Turn unknown MCP servers into governed NOVA connector contracts. The gateway discovers tools, resources, prompts, transport, and auth boundaries before invocation.

## Required Inputs

- Server URL or local transport
- Auth mode
- Discovery response
- Desired task
- Permission boundary

## Workflow

1. Capture server identity and transport.
2. Discover tools, resources, and prompts.
3. Normalize discovery into connector registry fields.
4. Score permission and execution risk.
5. Invoke only allowlisted tools with proof capture.

## Proof Gates

- Server identity captured
- Auth boundary captured
- Tool list hash captured
- Permission review completed

## Refusal Boundary

Do not invoke unknown tools with broad filesystem, network, credential, or execution authority without explicit review.
