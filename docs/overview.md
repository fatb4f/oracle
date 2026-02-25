# Oracle Overview

`oracle` is the canonical OTEL-native package for Evidence-First DSA work in
this monorepo.

## Core idea

Build and debug DSAs by emitting structured evidence first:

- step and run spans
- guard and invariant outcomes
- explanation events
- provenance (`code.filepath`/`code.lineno` or notebook/cell provenance)

Code and pseudocode follow from evidence.

## Canonical package

Primary package: `oracle`

Capabilities:

- OTEL runtime helpers for run/span/step/event emission
- schema-aligned evidence keys and provenance fields
- adapter surfaces for workflow tools
- materializers that reconstruct ordered steps and outcomes

## Workflow surfaces

- VS Code + Codex-IDE: coding, debugging, and test runs
- Marimo + ACP: notebook execution and evidence surfacing

Both surfaces use one OTEL config model and one schema contract.

## EOFL relationship

EOFL is a closed-loop governance model for this workflow:

- Feedback artifacts: traces, tests, invariants, explanations
- Feedforward surfaces: VS Code + Codex-IDE, Marimo + ACP

The Evidence-First DSA workflow is canonical; EOFL governs and improves it.

## Package status

- `oracle`: active and canonical
- `oracle_api`: deprecated, migration-only
- `oracle_tools`: deprecated, migration-only
