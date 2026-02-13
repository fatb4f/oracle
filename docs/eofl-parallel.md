# Parallel External Observers — Consolidated Living Document (v0)

Type: Living document  
Status: Draft -> Active  
Last updated: 2026-01-31  
Owner: baf

## 0. Purpose
Run two external observers in parallel—one for work/learning correctness and
one for cognitive-load legality/safety—with a mechanical coordinator that
intersects their outputs. This system:
* keeps the LLM as proposer/summarizer, never the authority
* uses machine-readable evidence (JSONL + Mermaid + tests)
* produces one bounded next action per tick
* blocks illegal work by deterministic rules (legality windows, uncertain=FAIL, monotone mode)
* integrates with Codex packet execution as a bounded actuator

## 1. Scope and boundaries

### 1.1 In scope
* Python-only controller surface: contracts + evidence + tests
* Multiple plants (what changes): Python / SQL / C++ / math / pseudocode projection
* Two LLM observer domains, running in parallel
* Coordinator that merges/vetoes/degrades outputs deterministically
* Pull-based integration only (files in/out + local processes)

### 1.2 Out of scope (hard boundaries)
* Remote shell / agentic "do anything" execution
* LLM outputting arbitrary code as primary deliverable
* Push-based automation (no autonomous triggering)

## 2. System model

### 2.1 Plants (what changes)
A plant is the system being executed/controlled:
* Python algorithm (sorting, trees, graphs)
* SQL engine (DuckDB default; Postgres optional)
* C++ binary (build/run/eval via Python harness)
* Symbolic math (rewrite/solve steps)
* Pseudocode deliverable (projection of a verified reference implementation)

### 2.2 Controller surfaces (what stays constant)
Evidence artifacts:
* `trace.jsonl` (append-only)
* `flow.mmd` / other Mermaid projections
* `tests.txt` (captured output)
* `proposal.json` (bounded action contract)
* optional `next_packet.contract.json` (Codex packet stub)

Contracts (Pydantic):
* `RunCapsule`, `Span`, `Step`, `Lens`
* `Proposal`, `PacketStub`
* (Neuro) `PreflightSnapshot`, `ActiveBlock`, `OTestResults`, `TickDecision`

Mechanical evaluation:
* pytest + hypothesis for invariants and shrinking counterexamples

Surfacing:
* marimo dashboard (trace viewer + Mermaid renderer + test results)

## 3. Roles, authority, and parallel observers

### 3.1 Authority boundary (non-negotiable)
LLM = proposer + summarizer (never the authority).  
Authority resides in tools/controllers enforcing:
* schema validation
* block legality and boundaries
* policy evaluation
* append-only logging
* execution constraints (Codex packets)

### 3.2 Observer A — Cognitive Supervisor (Neuroctrl / HPS+ELS)
Purpose: decide legality and safe intensity right now.

Inputs: `preflight_snapshot`, `active_block`, `otest_results`, window flags,
last end pointer.

Output: 5-line deterministic decision (+ optional JSON).

### 3.3 Observer B — Learning / Work Observer (ctrlr Domain 1)
Purpose: produce the best next bounded action to improve the work artifact and
its evidence.

Inputs: `trace.jsonl` (+ Mermaid), tests output, failing invariant(s),
counterexample (if any).

Output: `Proposal` (one micro-action; success/rollback/bounded scope).

Optional: `PacketStub` (Codex contract skeleton).

### 3.4 Interactive explanation (ctrlr Domain 2)
Purpose: "why did this happen?" / "what else could happen?"  
Uses the same artifacts but outputs human explanation only. It does not change
deterministic decision-making.

## 4. Shared observer language (evidence)

### 4.1 Step (plant transition)
Each `Step` records:
* `state_before` (small snapshot)
* `guards` (named predicates -> booleans)
* `action_taken`
* `invariants` (named checks -> pass/fail)
* `state_after`
* `why_safe`
* `why_transitioned`
* `alternatives` (other outcomes + triggers)
* `span_id` / `parent_span_id`

### 4.2 Outputs (evidence)
* `trace.jsonl`: append-only, diffable evidence
* Mermaid: flow/calltree/phase projections derived mechanically
* Hypothesis counterexample: minimal failing input on failure

## 5. Neuroctrl deterministic policy (Observer A)

### 5.1 Role contract (LLM constraints)
The LLM:
* proposes one next micro-step (<=1 minute to start)
* emits one paste-ready log line
* recommends mode/band changes (never overrides tooling)

The LLM does not:
* bypass legality windows
* propose multiple options
* propose work during reset phases

### 5.2 Minimal inputs expected
Missing essential fields trigger safe fallbacks.

* `preflight_snapshot`: `{ mode, band, timer_phase }`
* `active_block` (or null): `{ pattern_class: SYL|CTX, boundary, illegal_moves, exit_condition }`
* `otest_results` (or "not run this tick")
* window flags: `{ is_context_block, is_deferred_window }`
* `last_end_pointer` (optional)

### 5.3 Mandatory output format (5 lines)
* Decision: `CONTINUE | DOWNGRADE | RESET_SHORT | RESET_LONG | CLOSE_BLOCK | NOTES_ONLY | DENY_ILLEGAL`
* Why: single reason
* Next step: one imperative action, <=1 minute to start
* Log line: paste-ready
* Fallback: one line

### 5.4 Deterministic decision rules (priority order)

Rule 0 — Missing essentials -> `NOTES_ONLY`  
If `active_block` missing/invalid or legality unknown:
* Decision: NOTES_ONLY
* Next step: write 1 note + define/validate block (or run preflight)

Rule 1 — Legality windows (CTX gating)  
If `pattern_class=CTX` and not (`is_context_block` OR `is_deferred_window`) -> `DENY_ILLEGAL`.  
If "<=1 CTX block/day" signal is missing -> unknown -> deny.

Rule 2 — Mode monotonicity  
Never recommend upgrading within same session/day.

Rule 3 — O-tests: uncertain = FAIL  
Not run this tick -> unknown -> FAIL -> worsen band by 1 step.  
Any ambiguous result -> FAIL.  
Band progression: `OK -> RISING -> NEAR_LIMIT`.

Rule 4 — Mode/band -> required decision mapping

```
mode   band        decision
GREEN  OK          CONTINUE
GREEN  RISING      RESET_SHORT then CONTINUE (recommend YELLOW if repeated)
GREEN  NEAR_LIMIT  DOWNGRADE -> YELLOW + RESET_LONG
YELLOW OK          CONTINUE (single micro-step, no expansion)
YELLOW RISING      RESET_LONG
YELLOW NEAR_LIMIT  DOWNGRADE -> RED + CLOSE_BLOCK
RED    any         CLOSE_BLOCK or NOTES_ONLY
```

Rule 5 — Timer-phase enforcement  
If `timer_phase` is RESET_SHORT or RESET_LONG, the LLM must not propose work.
It outputs the reset decision and reset protocol step.

### 5.5 Micro-step policy (allowed types only)
* Extract 1 fact
* Write 1 artifact line
* Run 1 mechanical check
* Define 1 boundary

## 6. ctrlr Domain 1 policy (Observer B)

### 6.1 B–A–B loop
B (Observe): ingest evidence
* `trace.jsonl` (RunCapsule/Span/Step)
* tests output; failing invariants
* Hypothesis minimal counterexample (if any)

A (Act): propose a single change
* `Proposal`: one micro-action; success criteria; rollback; bounded scope

B (Observe again): verify
* rerun tests; compare trace; confirm invariant improvements

### 6.2 Domain 1 output constraints
* exactly one bounded action
* must be testable and rollbackable
* if evidence is missing, the action becomes an evidence step:
  * add 1 invariant
  * emit 1 step
  * capture 1 counterexample
  * run 1 mechanical check

## 7. Coordinator (mechanical) — intersection + veto rules

### 7.1 Purpose
Merge Observer A (neuro legality/intensity) and Observer B (work proposal) into
one executable outcome.

### 7.2 Coordinator outcomes
* `EXECUTE_PACKET`
* `DEFER`
* `RESET`
* `NOTES_ONLY`
* `CLOSE_BLOCK`

### 7.3 Deterministic merge rules (veto-first)
* If neuro decision is `DENY_ILLEGAL` -> DEFER
* If neuro decision is `RESET_SHORT` or `RESET_LONG` -> RESET
* If neuro decision is `CLOSE_BLOCK` -> CLOSE_BLOCK
* If neuro decision is `NOTES_ONLY` -> NOTES_ONLY
* If neuro decision is `DOWNGRADE` -> DEGRADE proposal then EXECUTE (only if still legal)
* If neuro decision is `CONTINUE` -> EXECUTE (if compliant)

### 7.4 Degrade policy (when needed)
If proposal exceeds constraints (scope/budget/boundary), shrink to the nearest
legal micro-step:
* extract 1 requirement
* write 1 invariant
* run 1 mechanical check
* define 1 boundary line

## 8. Codex integration (repo-work plant)

### 8.1 Plant A — `repo_work_codex`
* executes bounded packets in `.codex/.worktrees/<packet_id>`
* writes evidence under `.codex/out/<packet_id>/`
* commits one change per packet

### 8.2 Plant B — `external_observer`
* reads evidence
* produces `proposal.json` and optional `next_packet.contract.json`

Key benefit: the LLM proposes; Codex executes under strict constraints.

## 9. Course leverage map (plants)

### 9.1 INF1220 — Pseudocode / foundations
* Implement in Python with ctrlr steps
* Prove invariants with pytest/hypothesis
* Render pseudocode as projection of verified code
* Outputs: trace + Mermaid + tests + derived pseudocode

### 9.2 INF1250 — SQL / databases
* Plant: DuckDB default, Postgres optional
* Transitions: connect -> DDL -> explain -> execute -> check
* Invariants: rowcount bounds, key uniqueness, schema matches model, join cardinality constraints
* Hypothesis: small table generation + shrinking failing datasets

### 9.3 INF1425 — Data structures / graphs / performance
* Instrument ops transitions (push/pop/rehash/visit/relax)
* Hypothesis generates op sequences
* Add counters (comparisons/swaps/visits) for performance reasoning

### 9.4 INF2005 — C++ intro (harness)
* Python harness transitions: ACK BUILD -> RUN -> EVAL
* Differential testing: Python reference = oracle
* Invariants: compile/run exit codes, output parseable, output equals reference

### 9.5 MQT1001 — math (optional)
* Each rewrite/solve step is a `Step`
* Invariants: semantic equivalence / solution validity

## 10. marimo workflow augmentation
Use marimo to:
* load `trace.jsonl`
* show step table (filter by phase/invariant failures)
* render Mermaid via `mo.mermaid()`
* stepper UI (select step index -> show before/after)
* run tests and show first failing counterexample

## 11. Minimum viable evidence routine

Daily (10 min)
* log: course + objective + evidence path
* attach: 1 trace + 1 Mermaid + 1 test output

Weekly (20 min)
* summarize improvements + next smallest step
* external observer may generate:
  * weekly delta summary from traces/outcomes
  * next bounded action proposal aligned to syllabus objective

## 12. Operational safety (non-negotiable)
* No remote shell patterns
* Pull-based integration only
* LLM outputs must be contracts (`Proposal`, optional `PacketStub`), not arbitrary code

## 13. Minimal checklist per new topic
For any new topic (algorithm/query/math/C++):
* Define plant state + guards
* Define invariants ("not breaking")
* Emit steps at transitions
* Add Hypothesis property tests
* Render Mermaid
* Run both observers in parallel
* Coordinator yields one legal action (execute/defer/reset/notes-only)

## 14. Suggested directory layout (convention)

```
ctrlr/                           # library
plants/<plant_id>/               # plant implementations/adapters
evidence/<run_id>/trace.jsonl
evidence/<run_id>/flow.mmd
evidence/<run_id>/tests.txt
proposals/<proposal_id>.json
packets/<packet_id>/next_packet.contract.json   # optional
marimo/ctrlr_dashboard.py
neuroctrl/
ledger/events.jsonl
ledger/snapshots/<ts>_snapshot.json
deferred.md
schedule.yaml
```

## 15. Reference Mermaid (B–A–B loop)

```mermaid
flowchart TD
  A[Observe evidence\n(trace + tests + counterexample)] --> B[Propose 1 bounded action\nproposal.json]
  B --> C[Execute + rerun tests\n(new trace)]
  C --> D{Invariants improved?}
  D -- yes --> E[Promote + record delta]
  D -- no --> A
```

## 16. Open backlog (next candidates)
* Define schema set (minimal fields + validation rules)
  * `Proposal.schema.json`
  * `PacketStub.schema.json`
  * `TickSnapshot.schema.json`
  * `TickDecision.schema.json`
* trace schema versioning + forward-compat policy
* standardize state snapshot sizing rules (what is legal to capture by default)
* redaction rules if needed
* Mermaid projection standards (flow, calltree, phase transitions)
* Coordinator implementation (deterministic merge + degrade logic)
* Mechanical gates:
  * "uncertain = FAIL" enforcement on missing O-tests
  * CTX gating with explicit window signals and "<=1 CTX/day" tracking

## 17. Revision log
* 2026-01-27: ctrlr living document drafted/activated
* 2026-01-31: consolidated parallel observers + coordinator into one living document; made deterministic rules canonical
