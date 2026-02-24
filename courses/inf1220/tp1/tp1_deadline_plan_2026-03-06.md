# INF1220 TP1 Submission Plan (Deadline: March 6, 2026)

Submission target: **Friday, March 6, 2026 (America/Montreal)**.

## Rules (non-negotiable)

- One focused block per day: **60-90 min**, no multitasking.
- Ship something every block: trace, pseudocode draft, correction note, or final text.
- Stop after block, mark checkboxes, and define next first task.

## Definition of Done (TP1)

- [ ] **O-01**: Early-termination sum-over-100 pseudocode + edge cases.
- [ ] **O-02**: Language-agnostic pseudocode formatting is clean and consistent.
- [ ] **O-03**: Line-by-line trace with variable values.
- [ ] **O-04**: FizzBuzz logical error diagnosed and corrected.
- [ ] **O-05**: Original vs corrected behavior comparison summary.
- [ ] Final proofreading and submission-ready package.

References:
- `courses/inf1220/tp1/objectives/objectives.normalized.json`
- `courses/inf1220/tp1/m1/inf1220_tp1_drill_bank_m1.md`
- `courses/inf1220/tp1/dsa_debugging_checklist.md`

## Layered Build (Required Structures)

End objective is built in this exact order:

1. `primitives`
2. `atomics`
3. `data structures`
4. `algorithms`

### Layer 1: Primitives

Scope:
- variables, constants, assignment
- arithmetic (`+`, `%`)
- comparisons (`>`, `==`)
- boolean operators (`AND`, `OR`, `NOT`)

TP1 mapping:
- O-01 threshold logic (`sum > 100`)
- O-04 divisibility checks for FizzBuzz variant

Done checks:
- [ ] Primitive operations used in pseudocode are explicit and consistent.
- [ ] No language-specific syntax leaks (Python/Java style).

### Layer 2: Atomics

Scope:
- sequence/iteration (`FOR`, loop index, bounds)
- selection (`IF / ELSE IF / ELSE`)
- accumulation (`sum <- sum + value`)
- early termination (`RETURN` inside loop)

TP1 mapping:
- O-01 efficient early-stop algorithm
- O-03 traceable control-flow steps
- O-04 bug root cause usually in atomic branching order

Done checks:
- [ ] Early termination occurs at first valid point.
- [ ] Branch order is logically correct and testable.

### Layer 3: Data Structures

Scope:
- one-dimensional array/list input
- scalar state (`sum`, `i`, `n`, output flag/value)
- trace table as explicit execution structure

TP1 mapping:
- O-01 array edge cases (empty, short, large)
- O-03 variable-state trace
- O-05 side-by-side execution comparison table

Done checks:
- [ ] Input/output and all state variables are declared.
- [ ] Trace table captures state_before/action/state_after.

### Layer 4: Algorithms

Scope:
- final algorithm A: `sum_exceeds_100` with early exit
- final algorithm B: corrected FizzBuzz logic
- comparison method: original vs corrected behavior summary

TP1 mapping:
- O-01 algorithm design + edge handling
- O-02 final pseudocode quality
- O-04 correction
- O-05 comparative analysis

Done checks:
- [ ] Both algorithms pass self-test cases.
- [ ] Comparison explains behavioral difference, not only output difference.

## Dated Execution Plan

### Feb 24, 2026
- [ ] Create/update working notes file (`courses/inf1220/tp1/m1/m1-notes`).
- [ ] Lock **Layer 1 (primitives)** vocabulary and notation.

### Feb 25, 2026
- [ ] Build **Layer 2 (atomics)** for O-01 (loop, branch, early return).
- [ ] Rewrite in strict language-agnostic style (O-02 pass 1).

### Feb 26, 2026
- [ ] Build **Layer 3 (data structures)** trace table for O-01 (O-03 pass 1).
- [ ] Validate variable transitions and stopping condition.

### Feb 27, 2026
- [ ] Build **Layer 4 (algorithms)** draft A: O-01 final version.
- [ ] Solve O-04 (identify bug in given FizzBuzz variant).

### Feb 28, 2026
- [ ] Build **Layer 4 (algorithms)** draft B: corrected FizzBuzz.
- [ ] Execute original vs corrected pseudocode on same inputs.

### Mar 1, 2026
- [ ] Draft O-05 behavior comparison summary (first complete pass).
- [ ] Run self-check against O-01..O-05 checklist.

### Mar 2, 2026
- [ ] Tighten wording and structure (clarity, concision, correctness).
- [ ] Re-run at least one full trace from scratch.

### Mar 3, 2026
- [ ] Dry-run submission version (no placeholders, no TODOs).
- [ ] Fix formatting and notation consistency.

### Mar 4, 2026
- [ ] Final technical review pass.
- [ ] Prepare final submission artifact(s).

### Mar 5, 2026
- [ ] Final proofreading pass only.
- [ ] Freeze content; no major rewrites.

### Mar 6, 2026 (Submission Day)
- [ ] Final sanity check.
- [ ] Submit.
- [ ] Record submitted version metadata in `m1-notes`.

## Fallback if you miss a day

- Do not “catch up everything.”
- Resume the next day with only:
  - one priority task due soonest,
  - one minimum artifact.
- Keep momentum over perfection.
