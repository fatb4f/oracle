# INF1220 — DSA + Debugging Parallel Track (Checklist)

Use this in parallel with TP1. Each item is a bounded micro‑step and should
produce a small evidence artifact (trace, invariant, or correction note).

## Phase 0 — Setup (once)

- Create a DSA workspace note file (e.g., `courses/inf1220/tp1/dsa_notes.md`).
- Define a trace table template: `step | op | state_before | action | state_after | invariant`.
- Decide a naming convention for invariants (e.g., `inv_size`, `inv_order`).

## Phase 1 — Linear DSAs

- Stack: define ops (`push`, `pop`, `peek`) + 2 invariants.
- Stack: trace `push, push, pop` with full state updates.
- Queue: define ops (`enqueue`, `dequeue`, `peek`) + 2 invariants.
- Queue: trace `enqueue, enqueue, dequeue`.
- Deque (optional): define ops + invariants.

## Phase 2 — Array‑Based Queue (circular buffer)

- Define indices (`head`, `tail`, `size`) + empty/full conditions.
- Write invariants for wrap‑around arithmetic.
- Trace a wrap‑around sequence (enqueue until wrap, then dequeue).
- Debug off‑by‑one: explain one potential bug and its fix.

## Phase 3 — Linked Structures

- Singly linked list: define nodes + ops (insert front, delete front, search).
- Invariants: acyclic, size matches node count.
- Trace pointer updates for one insert and one delete.
- Debugging drill: explain a broken link scenario and fix it.

## Phase 4 — Trees

- BST insert: define invariant (left < node < right).
- Trace one insert sequence (3 nodes).
- BST search: trace path for hit and miss.
- Debugging drill: show how a wrong comparison breaks the invariant.

## Phase 5 — Heaps

- Heap insert: define invariants (heap property + shape).
- Trace sift‑up (array representation).
- Extract‑min: trace sift‑down.
- Debugging drill: show a case where one swap is missing.

## Phase 6 — Graph Basics (optional)

- BFS: define visited invariant (monotone).
- Trace queue evolution on a small graph.
- DFS: trace stack/recursion and visited set.
- Debugging drill: show how missing “visited” causes repetition.

## Debugging Loop (per DSA)

- State 1–3 invariants.
- Run 1 minimal test case.
- Capture 1 short trace (3–5 steps).
- Fix first failing invariant or guard.
- Re‑trace and record the correction.

## Evidence Artifacts (minimum)

- One trace table per structure.
- One invariant list per structure.
- One “bug + fix” note per structure.
