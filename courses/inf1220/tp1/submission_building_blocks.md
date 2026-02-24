# TP1 Submission Building Blocks

## 1) Sum>100 algorithm (O-01)

- Problem contract: input type, output type, threshold rule (`> 100`)
- Preconditions/assumptions: positive numbers, empty array behavior
- State model: `sum`, iterator/index
- Control flow: loop + early termination condition
- Edge-case handling: empty, exactly 100, first-element >100, very large array
- Complexity note: best/worst case with early stop

## 2) Language-agnostic pseudocode quality (O-02)

- Standard header: Inputs / Variables / Output
- Primitive ops: assignment, arithmetic, comparison, boolean logic
- Atomic constructs: `IF/ELSE`, `FOR/WHILE`, `RETURN`
- Naming clarity: semantic variable names
- Formatting consistency: indentation, block delimiters, one style only
- Syntax hygiene: no Python/Java-specific tokens

## 3) Line-by-line trace (O-03)

- Test case selection: one case that triggers early stop, one that does not
- Trace schema: `line | state_before | action | state_after`
- State completeness: all mutated variables included
- Decision checkpoints: branch condition outcomes shown explicitly
- Termination proof: exact line and reason for return/exit
- Final result check: trace result matches algorithm output

## 4) FizzBuzz logical error + correction (O-04)

- Original logic restatement: branch order and conditions
- Defect localization: which condition makes another unreachable
- Root-cause explanation: why control flow is wrong
- Corrected pseudocode: reordered conditions (combined case first)
- Sanity examples: at least one value per branch class
- Invariant/guard statement: each input maps to exactly one correct output

## 5) Original vs corrected comparison (O-05)

- Shared input set: same values run on both versions
- Side-by-side execution table: original output vs corrected output
- Divergence points: where behavior first differs
- Iteration/branch behavior summary: condition-hit differences
- Logical conclusion: why corrected version satisfies spec
- Concise takeaway: one paragraph final comparison statement
