# oracle — External Observer Feedback Learning Controller

Type: Living document  
Status: Draft -> Active  
Last updated: 2026-01-27  
Owner: baf

## 0. Purpose
Use oracle as a small, all-Python substrate that:
* forces "think like the interpreter" execution (guards -> action -> invariants -> alternatives)
* produces machine-readable evidence (JSONL + Mermaid)
* enables an external observer (LLM) to propose the next bounded action (B–A–B loop)
* stays usable across TELUQ courses with different plants (pseudocode, SQL, algorithms, C++, math)

## 1. Scope and boundaries

In scope:
* Python-only controller surface (contracts + evidence + tests)
* Multiple plants (Python / SQL / C++ / math / pseudocode projection)
* External observer outputs as contracts (Proposal)

Out of scope (hard boundaries):
* Remote shell / agentic "do anything" execution
* LLM outputting arbitrary code as the primary deliverable
* Push-based automation (everything is pull-based: files in/out + local processes)

## 2. Core model

### 2.1 Plants (what changes)
A plant is the thing being executed/controlled:
* Python algorithm (sorting, trees, graph search)
* SQL engine (DuckDB / Postgres)
* C++ binary (compiled and executed)
* Symbolic math (algebraic simplification/solving)
* Pseudocode deliverable (rendered from a verified reference implementation)

### 2.2 Controller surface (what stays constant)

Artifacts (Python-only):
* trace.jsonl
* flow.mmd
* proposal.json
* tests

Contracts (Pydantic):
* `Lens`, `Span`, `Step`, `RunCapsule`
* `Proposal`

Mechanical evaluation:
* pytest + hypothesis for invariants (GEN/SELECT/EVAL behaviors)

Surfacing:
* marimo dashboard for trace + Mermaid rendering

Core learning tools (oracle_tools):
* budgeted runs and deterministic reproduction
* Mermaid renderers for predictive flow and calltree
* tooling that turns trace evidence into interpretable structure

## 3. Shared "observer language" (artifacts + contracts)

### 3.1 Step (plant transition)
Each step records:
* state_before (small snapshot of key locals/state)
* guards (named predicates -> booleans)
* action_taken (what transition occurred)
* invariants (named checks -> pass/fail)
* state_after
* why_safe (why it didn’t break)
* why_transitioned (why plan/phase changed)
* alternatives (other possible outcomes + trigger conditions)
* span_id / parent_span_id (call stack / recursion)

### 3.2 Outputs (evidence)
* trace.jsonl: append-only, diffable execution evidence
* Mermaid: flowchart TD derived from steps/spans (renderable in marimo)
* Hypothesis counterexample (on failure): minimal failing input

## 4. External Observer: two domains

### 4.1 Domain 1 — Controller (B–A–B feedback loop)
Goal: transform evidence into the next bounded action.

B (Observe): ingest
* trace.jsonl (RunCapsule/Span/Step)
* test results + failing invariant(s)
* Hypothesis minimal counterexample (if any)

A (Act): propose a single change
* a Proposal: one micro-action, success criteria, rollback, bounded scope

B (Observe again): verify
* rerun tests, compare new trace, confirm invariants improve

Output contract:
* proposal.json (Pydantic)

Rule: Domain 1 output must be small, testable, rollbackable.

### 4.2 Domain 2 — Interactive (Explain / Why / What-else)
Goal: answer "why did this happen?" in human terms.
Uses the same artifacts (trace + Mermaid), but outputs:
* narrative explanations
* clarifying questions
* "what else could happen" alternatives

## 5. How oracle is structured (monorepo with worktrees)

The repo is a monorepo structured with worktrees:
* `packages/oracle_api` provides the stable evidence substrate.
* `packages/oracle_tools` provides core learning tools.
* `courses/<course>` contains course-specific work and deliverables.

The external observer produces `proposal.json` against evidence; execution and
changes happen in the relevant course or package worktree.

## 6. TELUQ course leverage map

### 6.1 INF1220 — Pseudocode / foundations
Challenge: deliverables are often pseudocode, not Python.

Approach:
* Implement the algorithm in Python with ctrlr steps.
* Prove invariants with pytest/hypothesis.
* Render pseudocode as a projection of the verified implementation.

Observer Domain 1 does:
* detects missing invariants ("why_safe" incomplete)
* suggests clearer guard naming + alternatives
* proposes smallest edits to align code <-> pseudocode mapping

Progression artifacts:
* trace.jsonl + Mermaid flow
* tests demonstrating correctness
* derived pseudocode output

### 6.2 INF1250 — Databases / SQL
Plant: DuckDB (default) and optionally Postgres.

Approach:
* treat each query as a plant transition: connect -> DDL -> explain -> execute -> check
* validate row shapes and outputs (Pydantic models)
* Hypothesis generates small tables and shrinks failing datasets

Example invariants:
* expected rowcount bounds
* key uniqueness
* join cardinality constraints
* result schema matches model

Observer Domain 1 does:
* proposes missing checks (e.g., nullability validation)
* proposes minimal dataset reproducing incorrect logic
* proposes next query/constraint to isolate the issue

Artifacts:
* trace with query steps
* Mermaid flow (sequence-level)
* tests replaying failing datasets

### 6.3 INF1425 — Data structures / algorithms / graphs / performance
Plant: Python implementations + classic sorts.

Approach:
* instrument operations as transitions (push/pop, rotate, rehash, BFS/DFS visit, relax edge)
* Hypothesis generates sequences of ops + shrinks failures
* add explicit counters (comparisons/swaps/visits) to state for performance reasoning

Observer Domain 1 does:
* identifies first invariant break and guard flip
* proposes one fix (guard, invariant, or state snapshot)
* improves "alternatives" coverage

Artifacts:
* trace + Mermaid (flow/calltree)
* property tests
* counterexample inputs

### 6.4 INF2005 — C++ intro (outlier)
Plant: C++ binary; controller surface remains Python-only.

Approach:
* Python harness transitions: BUILD (compile), RUN (execute), EVAL (compare outputs vs Python reference)
* differential testing: Python = oracle
* Hypothesis generates inputs + shrinks failures

Example invariants:
* compile exit code == 0
* run exit code == 0
* output parseable and equals reference

Observer Domain 1 does:
* diagnoses build vs run vs eval failures
* proposes smallest next action (parsing, bounds, flags for learning runs, isolate failing case)

Artifacts:
* build/run/eval trace
* minimal failing input
* equivalence proof restored after fix

### 6.5 MQT1001 — Math / constraints (optional)
Plant: algebraic transformation/solving.

Approach:
* represent each rewrite/solve operation as a step
* invariants: semantic equivalence or solution validity
* Hypothesis generates small expressions to find counterexamples (when feasible)

Observer does:
* proposes missing domain assumptions
* flags non-equivalence steps
* suggests alternative transforms

## 7. marimo workflow augmentation (the interpreter dashboard)
Use marimo to:
* load trace.jsonl
* show a step table (filter by phase, invariant failures)
* render Mermaid via mo.mermaid()
* provide a stepper UI (select step index -> show before/after)
* run tests and display first failing counterexample

## 8. Minimum viable evidence routine

Daily (10 minutes)
* log: course + objective + evidence link/path
* attach: one trace + one Mermaid + one test run output

Weekly (20 minutes)
* summarize improvements + next smallest step
* external observer may generate:
  * weekly delta summary from traces + outcomes
  * next bounded action proposal aligned to syllabus objective

## 9. Operational safety / boundaries (non-negotiable)
* No remote shell patterns.
* Pull-based integration only (files in/out, local processes).
* LLM outputs must be contracts (Proposal, optional PacketStub), not arbitrary code.

## 10. Minimal checklist per new TELUQ topic
For any new topic (algorithm/query/math/C++):
* Define plant state and guards.
* Define invariants ("not breaking").
* Emit steps at transitions.
* Add Hypothesis property tests.
* Render Mermaid.
* Run observer Domain 1 to propose next bounded improvement.

## 11. Suggested directory layout (convention)

```
packages/
  oracle_api/
    src/oracle_api/...
    tests/...
  oracle_tools/
    src/oracle_tools/...
    tests/...
courses/
  <course>/
    ...
integration/
docs/
pyproject.toml
uv.lock
```

## 12. Revision log
* 2026-01-27: Initial living document formatted from draft spec.

## 13. Open backlog (next candidates)
* Define the Proposal schema (minimal fields + validation rules).
* Specify a trace schema version and forward-compat policy.
* Standardize "state snapshot" sizing rules (what is legal to capture by default).
* Decide the minimum Mermaid projections: (a) flow, (b) calltree, (c) phase transitions.

```mermaid
flowchart TD
  A[Observe evidence\n(trace + tests + counterexample)] --> B[Propose 1 bounded action\nproposal.json]
  B --> C[Execute + rerun tests\n(new trace)]
  C --> D{Invariants improved?}
  D -- yes --> E[Promote + record delta]
  D -- no --> A
```
