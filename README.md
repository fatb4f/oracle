# Oracle monorepo

`oracle` is the primary OTEL-native package for Evidence-First DSA workflows.

Start here:
* `docs/README.md` for canonical documentation navigation.
* `docs/overview.md` for architecture and package status.
* `docs/setup_and_workflow.md` for setup, environment, and dev flow.
* `docs/otel_migration/README.md` for migration plan and compatibility contract.

Deprecated:
* `oracle_api` and `oracle_tools` remain in-repo only for migration compatibility
  and are not the primary setup/import path.

## MVP bootstrap

Use UV for a reproducible local toolchain (including Marimo and adapter test deps):

```bash
./scripts/mvp_bootstrap.sh
```

Run integration suites:

```bash
./scripts/mvp_tests.sh
```

Install VS Code extension recommendations (Python + Codex IDE extension):

```bash
./scripts/install_vscode_extensions.sh
```

Launch VS Code with deterministic local state (`--user-data-dir`,
`--extensions-dir`, `--profile`):

```bash
./scripts/vscode_deterministic.sh .
```

Launch Marimo:

```bash
./scripts/marimo_deterministic.sh
```
