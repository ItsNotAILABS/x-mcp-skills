---
name: chatgpt-app-oauth-bridge
description: Use when NOVA should design bounded ChatGPT app/tool OAuth flows, OpenAI sign-in surfaces, or user-authorized product integrations without credential capture or hidden API assumptions.
---

# ChatGPT App OAuth Bridge

## Purpose

Design product flows where users can authorize a NOVA app/tool surface through official OAuth-style permissions. This bridge is for strategy and integration design; it does not scrape, capture, or misuse personal ChatGPT sessions.

## Required Inputs

- Product surface
- Auth provider and intended OAuth flow
- Permission scopes
- User journey
- Compliance or terms constraints

## Workflow

1. Identify the official auth path.
2. Define permission scopes and user consent screens.
3. Separate product intelligence from LLM session behavior.
4. Record compliance and data-handling notes.
5. Return a safe integration plan and open questions.

## Proof Gates

- Official auth path identified
- Permission scope recorded
- Terms review marked
- No credential capture

## Refusal Boundary

Do not design credential harvesting, session hijacking, browser bypasses, hidden API abuse, or flows that misrepresent who pays for compute.
