---
name: browser-workbench-bridge
description: Use when NOVA should analyze browser developer surfaces, service workers, storage, manifests, WASM, console/network telemetry, or browser-hosted workbench capabilities.
---

# Browser Workbench Bridge

## Purpose

Map browser runtime capability into NOVA without pretending the browser grants unrestricted backend access. The browser can host apps, service workers, storage, manifests, WASM, sockets, and telemetry under origin and permission boundaries.

## Required Inputs

- Browser origin
- Console or network trace
- Manifest or service worker status
- Storage report
- User-facing product goal

## Workflow

1. Record origin and permission boundary.
2. Classify available surfaces: service worker, local/session storage, IndexedDB, cache, manifest, WASM, sockets, media, reporting.
3. Identify what can become a browser workbench feature.
4. Identify what requires a server, extension, native app, or authenticated API.
5. Produce a workbench plan and risk report.

## Proof Gates

- Origin captured
- Storage boundary captured
- Service worker status captured
- No cross-origin bypass claim

## Refusal Boundary

Do not recommend bypassing browser security, MIME checks, CORS, origin policy, auth, or platform terms.
