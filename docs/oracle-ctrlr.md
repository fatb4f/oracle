# Oracle Tool Stack and Evidence-First Workflow

This document describes the tooling stack (formerly “ctrlr”) and how it maps to
the current oracle layout. The EOFL loop is decoupled from the stack and is
defined separately in `docs/eofl-oracle.md`.

## 1) Core Pieces (oracle_api)

`oracle_api` is the stable substrate for evidence-first work:
* Contracts (dataclass models): `Lens`, `Span`, `Step`, `RunCapsule`
* Trace runtime: `run(...)`, `span(...)`, `step(...)` -> `trace.jsonl`
* Control gates: `require(...)`, `ensure(...)`, `invariant(...)`

Purpose: a stable “observer language” for algorithms and their transitions.

## 2) Toolstack (oracle_tools + extras)

`oracle_tools` provides core learning tools:
* budgeted runs and deterministic reproduction
* Mermaid renderers for predictive flow and calltree
* tooling that turns trace evidence into interpretable structure

Optional extras are used as **playbook sequences** built from the
Evidence‑First DSA Workflow:
* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

## 3) Canonical Workflow

The canonical workflow is the Evidence‑First DSA Workflow:
* `docs/evidence_first_dsa_workflow.md`

INF1220-specific usage is a direct application of that workflow to
pseudocode-first deliverables.

## 4) Example (DSA + evidence-first)

Example: stack operations in a course worktree.

1. Define the model
   * State: `items`, `size`
   * Ops: `push`, `pop`
   * Invariants: `inv_size == len(items)`
2. Implement `push` and `pop` minimally.
3. Trace `push, push, pop` with `state_before`/`state_after`.
4. Add one boundary test (pop on empty).
5. Fix the first invariant failure (if any).
6. Summarize in one paragraph: what changed and why it’s safe.

This workflow produces evidence artifacts first, then code/pseudocode follows.
