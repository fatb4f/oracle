# Evidence-First DSA Workflow

This is the canonical workflow for DSA work in `oracle`. EOFL is the closed-loop
feedback system that governs and improves this workflow.

## Purpose

Build DSAs by making evidence (trace, invariants, tests) the primary artifact,
and let code/pseudocode follow from that evidence.

## Core Artifacts

* Trace: step-level state transitions
* Invariants: small, named checks that must hold at each step
* Tests: minimal cases that exercise edge conditions
* Explanation: short “why safe / why transitioned” notes

## Workflow (repeat per DSA)

1. Define the model
   * State variables (e.g., `head`, `tail`, `size`)
   * Operations (e.g., `enqueue`, `dequeue`)
   * 1–3 invariants
2. Write minimal implementation
   * Only enough code to execute one operation
3. Trace a single operation
   * Capture state before/after and guard conditions
4. Add one test
   * Edge case or boundary case
5. Check invariants
   * If any fail, fix the first failing invariant or guard
6. Extend by one operation
   * Repeat steps 3–5 for the next op
7. Summarize
   * One paragraph: what changed, what remained safe, and why

## Definition of Done (per DSA)

* All operations have a trace
* Invariants are explicitly stated and never violated
* At least one boundary test per operation
* A short explanation of correctness and failure modes
