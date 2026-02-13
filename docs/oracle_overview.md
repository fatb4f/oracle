# ctrlr Overview

This document consolidates the ctrlr concepts, workflow, and repo usage for
`oracle`. It replaces older, divergent guidance and keeps the focus on DSAs,
coding, and debugging with a stable evidence model.

## Core Idea

ctrlr is a minimal Python substrate that emits interpreter-level evidence. The
goal is to "think like the interpreter": observe state changes, control flow,
and invariants in a form that is replayable, diffable, and explainable.

## Repository Roles

### oracle_api (stable substrate)
The canonical evidence model and runtime:
* Contracts: `Lens`, `Span`, `Step`, `RunCapsule`
* Trace runtime: `run`, `span`, `step` -> `trace.jsonl`
* Control gates: `require`, `ensure`, `invariant`

### oracle_tools (core learning tools)
These are not optional debugging aids. They are core to learning how to think
like the interpreter:
* Budgeted runs and deterministic reproduction (`budget`, `seeded`)
* Mermaid renderers for predictive flow and calltree
* Any tooling that turns trace evidence into interpretable structure

### courses (applied learning)
Each course worktree is where DSAs are implemented, instrumented, tested, and
explained. The output is course deliverables backed by evidence.

## Stable Workflow (What Will Not Change)

* **Marimo with ACP Codex** for interactive exploration and trace surfacing.
* **VS Code with Codex-IDE** for daily coding and debugging.
* Focus: DSAs, a lot of coding, and a lot of debugging.

The workflow details will evolve, but these tools and the evidence-first model
are stable.

## External-Observer Loop (Core Emphasis)

The external observer is a structured feedback loop that uses the *same evidence
artifacts* you generate:

Observe -> Orient -> Decide -> Act -> Record -> Review -> Update

What to provide to the observer:
* `trace.jsonl` (or a filtered excerpt)
* failing invariant or test output
* the smallest reproducible input

What to request back:
* a single bounded proposal
* explicit success criteria
* a rollback plan

The loop is only as good as the evidence. Keep it small, precise, and replayable.

## How to Use oracle_api and oracle_tools from a Course Worktree

The course worktree is the consumer. It imports the stable APIs and tools from
`packages/` and keeps all variable content under `courses/`.

Recommended flow:
1. Implement DSA in the course worktree (`courses/<course>/...`).
2. Instrument with `oracle_api` steps/spans and gates.
3. Use `oracle_tools` to:
   * bound runs (`budget`, `seeded`)
   * render flows/calltrees (Mermaid)
4. Verify with tests (pytest + hypothesis as needed).
5. Write pseudocode that mirrors the trace steps and guard names.

## Pseudocode Mapping Discipline

* Keep variable names identical between Python and pseudocode (or use a strict,
  deterministic map).
* Each pseudocode block should correspond to a span or step boundary.
* Use trace evidence to justify:
  * why a branch was taken
  * which invariant kept the algorithm safe

## Evidence Artifacts (Minimum Set)

Per DSA/topic:
* `trace.jsonl`
* Mermaid flow + calltree
* pytest output
* optional minimal counterexample

These artifacts are the shared language between you, tests, and the observer.
