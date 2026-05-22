---
name: create-python-project
description: Use when creating a new Python project from Rob's Awesome Python Template (cookiecutter). Don't use for adding Python to existing projects, installing packages, or working with established codebases.
compatibility: Requires `uv` installed
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Generate new Python projects using `uvx cookiecutter`. The template handles all setup automatically via post-generation hooks.

## Prerequisites

Verify `uv` is installed:

```bash
which uv
```

If missing, read `references/installation_guide.md` and provide the user with the installation instructions. Do not install anything yourself — instruct the user to run the commands.

## Defaults

Set these defaults before asking the user anything:

| Parameter                     | Default |
| ----------------------------- | ------- |
| `python_version`              | `3.13`  |
| `include_github_actions`      | `y`     |
| `include_agents_instructions` | `y`     |

If `whoami` returns `tedivm`, also set:

| Parameter     | Value           |
| ------------- | --------------- |
| `author_name` | `Robert Hafner` |
| `license`     | `MIT license`   |
| `github_org`  | `tedivm`        |

## Workflow

1. **Determine project type.** Ask the user what kind of project they are building. Use their answer to pre-select features (see below).

2. **Pre-select features based on project type.**

   **Web app:** Enable `fastapi`, `sqlalchemy`, `jinja2`, `aiocache`, `docker`, `requirements_files` automatically. Ask if they need background tasks — if so, discuss the choice:
   - **Celery** — distributed task queue with Redis broker. Best for I/O-bound work, periodic/scheduled jobs, or tasks that need to scale across multiple workers.
   - **QuasiQueue** — multiprocessing library that bypasses the GIL. Best for CPU-bound work that needs true parallelism on a single machine.
     Set the chosen one to `y`.

   **Library:** Enable `publish_to_pypi`.

   **CLI tool:** Enable `include_cli`.

   **Minimal/other:** Leave optional features at `n` unless the user requests them.

   **Implicit dependencies:** If `fastapi`, `sqlalchemy`, `jinja2`, or `celery` are enabled, also set `include_docker=y` and `include_requirements_files=y`.

3. **Gather remaining details.** Ask the user for any values not yet determined:
   - `package_name` — always ask (required, must match `^[_a-zA-Z][_a-zA-Z0-9]+$`)
   - `short_description` — always ask
   - `author_name` — ask unless already set by user identity
   - `license` — ask unless already set by user identity
   - `github_org` — ask unless already set by user identity
   - `include_cli` — ask if not already determined
   - `publish_to_pypi` — ask if not already determined

4. **Confirm the configuration.** Present the final set of options to the user before generating.

5. **Run cookiecutter non-interactively.** Execute from the desired parent directory using `uvx` with `--no-input` and all parameters passed as extra context arguments:

```bash
uvx cookiecutter --no-input --overwrite-if-exists --accept-hooks yes \
  gh:tedivm/robs_awesome_python_template \
  package_name="<name>" \
  author_name="<author>" \
  short_description="<description>" \
  python_version="<version>" \
  github_org="<org>" \
  license="<license>" \
  include_cli="<y or n>" \
  include_fastapi="<y or n>" \
  include_sqlalchemy="<y or n>" \
  include_quasiqueue="<y or n>" \
  include_jinja2="<y or n>" \
  include_aiocache="<y or n>" \
  include_celery="<y or n>" \
  include_docker="<y or n>" \
  include_github_actions="<y or n>" \
  include_requirements_files="<y or n>" \
  include_agents_instructions="<y or n>" \
  publish_to_pypi="<y or n>"
```

`--no-input` forces cookiecutter to use `cookiecutter.json` defaults plus the extra context arguments, skipping all prompts and automatically refreshing cached templates.

6. **Verify the result.** The post-generation hook runs `make all`, `make lock`, and various code quality fixes automatically. Confirm the project directory was created and contains the expected structure.

7. **Initialize git.** Run `git init` inside the new project directory.

## Common issues

- **`uv` not found:** The template's `pre_gen_project.py` exits with an error if `uv` is missing. Direct the user to `references/installation_guide.md`.
- **Invalid package name:** Must match `^[_a-zA-Z][_a-zA-Z0-9]+$`. No hyphens or spaces.
- **Re-run after fixing errors:** Use the same `uvx cookiecutter --no-input ...` command with the same arguments to regenerate.
