---
name: cursor-ide-bridge
description: Use when NOVA should coordinate Cursor or VS Code-compatible IDE-assisted edits, navigation, review, and developer workflows under proof gates.
---

# Cursor IDE Bridge

## Purpose

Make Cursor a governed IDE worker surface. It can help edit and navigate code, but NOVA owns the branch, proof, tests, and import decision.

## Required Inputs

- Workspace path
- Selected files or ownership boundary
- Task brief
- Operator approval
- Expected verification command

## Workflow

1. Define allowed file scope.
2. Request plan or edit from Cursor within the workspace boundary.
3. Capture changed file list, tests, and notes.
4. Return artifacts to NOVA as a review-ready branch or patch.
5. Record unresolved risks before promotion.

## Proof Gates

- File list captured
- Operator approval recorded
- Tests recorded
- Review-ready branch or patch produced

## Refusal Boundary

Do not allow direct production deployment, secret edits, or broad workspace rewrites without explicit review.
