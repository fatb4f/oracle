# Configuration and Settings

This document defines the local setup for development and learning work in the
`oracle` monorepo.

## 1) Python venv

Create and activate a virtual environment inside each worktree you use.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install project dependencies from the repo root:

```bash
python -m pip install -e packages/oracle_api
python -m pip install -e packages/oracle_tools
```

If you need extras later (tests, hypothesis, etc.), add them here once they are
defined in `pyproject.toml`.

## 2) VS Code + Extensions

Required:
* VS Code
* Codex-IDE extension

Recommended:
* Python extension
* Pylance

Settings (workspace or user):
* Default interpreter: the `.venv` inside the worktree you are actively using
* Terminal activates venv automatically

## 3) Marimo + ACP

Install Marimo in the active venv:

```bash
python -m pip install marimo
```

Use the `codex-cli` ACP extension when running Marimo so the notebook is aware
of the Codex workflow.

## 4) Codex for Marimo and VS Code

* VS Code uses Codex-IDE for interactive coding + debugging.
* Marimo uses `codex-cli` `acp-ext` for notebook workflows and evidence capture.

Keep these roles stable:
* VS Code is the primary debugger and test runner.
* Marimo is the evidence surfacing and explanation surface.

## 5) API + Debug Tools

The API and tooling packages are installed in editable mode:

```bash
python -m pip install -e packages/oracle_api
python -m pip install -e packages/oracle_tools
```

Core tooling for "think like the interpreter":
* ctrlr contracts and trace runtime (oracle_api)
* budgeting/seeded runs + Mermaid renderers (oracle_tools)

Optional debugging tools (install only if needed):
* `pytest`
* `hypothesis`
* `snoop`
* `birdseye`

Add these to the venv when you are ready to use them:

```bash
python -m pip install pytest hypothesis snoop birdseye
```
