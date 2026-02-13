# Oracle Controller (standby)

This repo defines **stable contracts and helpers** for controlled development loops.
At present, EOFL is **on standby** and the active workflow relies on **external observation**:

- VS Code + Codex IDE for repo inspection and bounded change proposals
- marimo + ACP for interactive analysis and notebook-driven exploration
- standard Python debugging/tests in VS Code

This document describes what the repository provides **today**, without assuming any in-repo operator.

---

## Repository structure (current)

- `packages/oracle_api/`  
  Stable API: contracts and primitives that can be used by any operator or workflow.

- `packages/oracle_tools/`  
  Developer tooling: local helpers (budgeting, Mermaid rendering) and optional dev/test tooling.

- `courses/<course_id>/`  
  Variable course content (e.g., `inf2220`, `inf1250`) managed in dedicated worktrees.

- `main` (gatekeeper)  
  Merge-only trunk. Development happens in worktrees (api/tools/course) and lands via PR.

---

## Playbook-entities (process API)

The workflow is expressed in stable “playbook-entities”. These are **workflow artifacts** first; code support is intentionally minimal while EOFL is on standby.

### Mapping to repo concerns

- **Target** → the selected worktree + allowed paths + verification commands (workflow-level)
- **PlanCard** → issue/PR intent + success criteria + scope + stop rules
- **Observation** → findings recorded in issue/PR text (optionally also in trace step payloads)
- **Proposal** → bounded diff suggestion (may be applied manually or by an external operator)
- **EvidenceRef** → external run ids / logs / coverage pointers referenced from PR/issue text
- **Decision** → continue/stop/rescope captured in the PR/issue thread

### Minimal structure guidance

If you need machine-readable structure but want to keep `oracle_api` stable:

- store workflow/controller fields under `Step.data` (or equivalent) using a documented key set
- version the key set (e.g. `eofl.v1.*`) so evolution is explicit

---

## Minimal "EOFL" environment (observer-first)

EOFL is not enforced in-repo. The “minimal EOFL environment” is the combination of tools that provides **observation**, **bounded proposals**, and **verification**.

### Required
1. **VS Code**
   - Python extension configured for the repo environment
   - Codex IDE extension installed and authenticated

2. **Python runtime**
   - reproducible install path (uv/venv)
   - a small set of verification commands (at minimum: `pytest`)

3. **marimo + ACP**
   - notebooks for analysis/exploration
   - ACP agent connection configured for read-only or bounded-edit sessions

### Operating rules
- Default to **observe**; avoid unbounded edits.
- Any applied change must have: **declared scope**, **verification run**, and **EvidenceRef** pointer.
- Evidence/state is **operator-owned** and stored externally; the repo only links to it.

---

## What is stable in code (today)

### `oracle_api`
Provide stable primitives for:
- structured trace concepts (run/span/step)
- deterministic seeding helpers when needed
- control primitives that do **not** assume a specific operator

### `oracle_tools`
Provide developer-side helpers for:
- budgeting/guardrails utilities
- rendering/visualization helpers (e.g. Mermaid)
- optional test/observability tooling installed via extras

`oracle_tools` should remain safe to omit in minimal/CI contexts.

---

## Next increments (small, compatible)

- Add `oracle_tools` extras for the analysis stack (hypothesis/snoop/birdseye/hunter/viztracer/coverage)
- Add a short “Quickstart (observer loop)” page that matches `docs/eofl-oracle.md`
- When ready, formalize a minimal `Proposal` contract in `oracle_api` (versioned)
