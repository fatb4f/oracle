# Basic Usage

## Layout

Recommended paths inside `oracle`:

```
packages/
  oracle_api/
    src/oracle_api/...
    tests/...
  oracle_tools/
    src/oracle_tools/...
    tests/...
courses/
  inf2220/...
  inf1250/...
integration/
docs/
pyproject.toml
uv.lock
```

Dependency rule:

* `oracle_tools` may import `oracle_api`
* `oracle_api` must not import `oracle_tools`

Notes:

* `oracle_tools` contains no variable content.
* No xtrlv2 references, folders, wrappers, packet specs, state, or evidence are stored in this repo.
* **Worktree** = a checkout location tied to a branch.
* `courses/<course>/...` = a content subtree **inside** a worktree checkout.

## Worktrees

Suggested branch names:

```
WT        Branch
main      main
api       work/api
tools     work/tools
inf2220   course/inf2220
inf1250   course/inf1250
```

Bootstrap:

```bash
git clone git@github.com:<owner>/oracle.git oracle-main
cd oracle-main
git checkout main

git worktree add ../oracle-api     -b work/api main
git worktree add ../oracle-tools   -b work/tools main
git worktree add ../oracle-inf2220 -b course/inf2220 main
git worktree add ../oracle-inf1250 -b course/inf1250 main
```

Operational rule:

* Develop only in `oracle-{api,tools,inf2220,inf1250}`; merge only via PR into `main`.

Minimal CI path policy (gatekeeper-friendly):

* `packages/oracle_api/**` → run API tests
* `packages/oracle_tools/**` → run tools tests
* `courses/**` → run content validation (as defined)
* always run `integration/**` smoke if either package changes

## Tooling Additions (Hypothesis + snoop + birdseye)

Additions that complement the current stack:

1. Branch coverage (forces "did we hit both outcomes?")
Use `coverage.py` branch coverage via `pytest-cov` to verify conditional branches were exercised.
Typical usage:
```bash
pytest --cov=src --cov-branch
```
Why it complements the stack:
Hypothesis finds edge cases; branch coverage confirms those cases push execution through both sides of important conditionals.

2. Hypothesis Ghostwriter (bootstrap properties fast)
Hypothesis can generate starter property tests for a function via `hypothesis.extra.ghostwriter`, including a CLI.
Typical usage:
```bash
hypothesis write your_module:your_function
```
Why it complements the stack:
Reduces blank-page overhead for each new DSA exercise; you then refine invariants.

3. Hypothesis Stateful testing (operation sequences)
For mutable DSAs (stack/queue/heap/union-find/hash map), use `RuleBasedStateMachine` to model operations and check invariants after each step.
Why it complements the stack:
Finds bugs that only appear after specific sequences of pushes/pops/inserts/deletes/rebalances.

4. VizTracer (timeline + call-stack trace)
VizTracer traces execution (function entry/exit) and visualizes it in a Perfetto-based UI, producing JSON/HTML reports.
Why it complements the stack:
Great for recursion, divide-and-conquer, and "where is time going?" questions. Pairs well with Mermaid: VizTracer gives you the actual call structure; Mermaid captures the simplified story.

5. Hunter (filtered tracing, attachable)
Hunter is a flexible tracing toolkit with strong filtering and an attach-to-process workflow.
Why it complements the stack:
Use it when you want targeted tracing without the noise or overhead of full profilers.
