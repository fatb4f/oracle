# Python Profile Template

Import this profile template into VS Code and use it with the deterministic
launcher script.

## Extension set

- `ms-python.python` (required)
- `ms-python.vscode-pylance` (recommended)
- `ms-python.vscode-python-envs` (optional)
- `openai.chatgpt` (Codex IDE extension)

## Settings baseline

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests/integration"],
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  },
  "search.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  }
}
```

## Import path in VS Code

Use: `Profiles: Import Profile...` and apply these settings/extensions to a
profile named `Oracle Python`.
