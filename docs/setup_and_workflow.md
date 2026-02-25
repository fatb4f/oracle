# Setup and Workflow

This guide defines local setup and day-to-day execution for development and
learning work in the `oracle` monorepo.

## Repository layout

Primary paths:

```text
src/oracle/...
tests/integration/
docs/
courses/
pyproject.toml
```

Legacy migration paths (deprecated, non-primary):

```text
packages/oracle_api/
packages/oracle_tools/
```

## Dependency rules

- New runtime, adapters, and materializers import from `oracle`.
- New docs and examples use `oracle` as the canonical package.
- References to `oracle_api` and `oracle_tools` are allowed only as explicit
  deprecation or migration context.

## Python environment

Create and activate a virtual environment in the active worktree:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the runtime package from repo root:

```bash
python -m pip install -e .
```

Optional OTEL exporter extras:

```bash
python -m pip install -e ".[otel]"
```

## VS Code and Marimo

Required:

- VS Code
- Codex-IDE extension

Recommended:

- Python extension
- Pylance

Practical defaults:

- Use the `.venv` in the active worktree as interpreter.
- Run tests/debugging from the selected worktree.
- Use Marimo for exploratory and instructional evidence views.
- Keep stable runtime/adapter/materializer code in `src/oracle`.

Install Marimo:

```bash
python -m pip install marimo
```

Use `codex-cli` ACP extension with Marimo for notebook-aware workflows.

### Deterministic editor/app state (`conf.d/`)

Repo-local deterministic defaults live in:

- `conf.d/vscode/env.sh`
- `conf.d/marimo/env.sh`

Use these launchers:

```bash
./scripts/vscode_deterministic.sh .
./scripts/marimo_deterministic.sh
```

VS Code profile template reference:

- `conf.d/vscode/python.profile-template.md`

This setup isolates state under `.state/` and avoids cross-project editor/app
contamination.

## OTEL runtime configuration

Configure exporters with environment variables:

```bash
export OTEL_TRACES_EXPORTER=console
export OTEL_SERVICE_NAME=oracle
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=dev,service.namespace=oracle
```

OTLP example:

```bash
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

## Worktrees and branch flow

Suggested worktrees:

```text
WT         Branch
main       main
runtime    work/oracle-runtime
course     course/<course-id>
```

Bootstrap example:

```bash
git clone git@github.com:<owner>/oracle.git oracle-main
cd oracle-main
git checkout main

git worktree add ../oracle-runtime -b work/oracle-runtime main
git worktree add ../oracle-course  -b course/inf2220 main
```

Operational rule:

- Do day-to-day work in non-`main` worktrees.
- Merge to `main` through PRs.

## Evidence-First DSA workflow

This is the canonical DSA workflow.

### Purpose

Build DSAs by making evidence (trace, invariants, tests) the primary artifact,
then let code and pseudocode follow from that evidence.

### Core artifacts

- Trace: step-level state transitions
- Invariants: named checks that must hold at each step
- Tests: minimal cases that exercise edge conditions
- Explanation: short safety and transition rationale

### Loop (repeat per DSA)

1. Define model state, operations, and 1-3 invariants.
2. Write minimal implementation for one operation.
3. Trace one operation with before/after state and guards.
4. Add one boundary or edge test.
5. Check invariants and fix first failing guard/invariant.
6. Extend by one operation and repeat.
7. Summarize what changed and why it remained safe.

### Definition of done

- All operations have traces.
- Invariants are explicit and never violated.
- Each operation has at least one boundary test.
- Correctness and failure modes are summarized.

## Standard tool stack

- `pytest`, `hypothesis`
- `snoop`, `birdseye`
- `hunter`, `viztracer`
- `coverage`, `pytest-cov`
