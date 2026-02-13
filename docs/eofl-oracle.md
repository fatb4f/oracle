# EOFL Oracle (minimal)

EOFL is a closed-loop feedback system for learning. It is defined here only in
terms of **feedback** and **feedforward**, and how they connect to the workflow.

## Feedback

Evidence artifacts:
* trace
* tests
* invariants
* explanations

## Feedforward

IDE + ACP extension for reasoning and clarification with the operator:
* VS Code + Codex-IDE
* marimo + ACP

## Relationship to the workflow

The Evidence-First DSA Workflow is the canonical workflow. EOFL governs it by
closing the loop using evidence (feedback) and operator-facing tooling
(feedforward).

Tooling like snoop/birdseye/hypothesis is expressed as **playbook sequences**
built from the Evidence-First DSA Workflow, not as standalone EOFL doctrine.
