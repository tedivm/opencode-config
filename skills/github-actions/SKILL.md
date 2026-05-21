---
name: github-actions
description: "Use when creating, modifying, or reviewing GitHub Actions workflow files. Covers workflow syntax, action selection, dependabot configuration, and CI/CD best practices."
---

## Quick start

All GitHub Actions workflows must follow these rules. Apply them every time a workflow file is created or modified.

## Hard rules

1. **Always set `fail-fast: false`.** Add `fail-fast: false` to every `strategy` block so a failure in one matrix job does not cancel the others. All jobs should run to completion regardless of failures.

2. **Always use the latest versions of actions.** Before referencing any action, look up its latest release tag and resolve it to a commit SHA using `gh`. Run both commands for each action:

   ```bash
   # Step 1: Get the latest release tag
   gh api repos/{owner}/{repo}/releases/latest --jq '.tag_name'
   # Example: gh api repos/actions/checkout/releases/latest --jq '.tag_name'
   # Output: v6.0.2

   # Step 2: Resolve the tag to a commit SHA
   gh api repos/{owner}/{repo}/git/ref/tags/{tag} --jq '.object.sha'
   # Example: gh api repos/actions/checkout/git/ref/tags/v6.0.2 --jq '.object.sha'
   # Output: de0fac2e4500dabe0009e67214ff5f5447ce83dd
   ```

   Pin to a full commit SHA, never a branch or mutable tag like `v3` or `main`.

   **Do not skip this step.** Action versions change frequently. Using outdated versions introduces security and compatibility risks.

3. **Always add Dependabot for GitHub Actions.** If `.github/dependabot.yml` does not exist or lacks a GitHub Actions ecosystem entry, create or update it:

   ```yaml
   version: 2
   updates:
     - package-ecosystem: "github-actions"
       directory: "/"
       schedule:
         interval: "monthly"
   ```

   This ensures action versions stay current automatically.

4. **Only use trusted actions.** Restrict third-party actions to:
   - Official GitHub actions (`actions/checkout`, `actions/upload-artifact`, etc.)
   - Actions from well-known companies with established track records (e.g., `docker/`, `google-github-actions/`, `aws-actions/`)
   - Well-known open source projects or authors with established reputations
   - Actions from the project's own repository

5. **Always use language setup actions.** Never assume a runner has the required language runtime or tooling installed. Use the official setup actions before any build, test, or install steps. Look up the latest version of each action using `gh` before referencing it:
   - Node.js: `actions/setup-node`
   - Python: `astral-sh/setup-uv` (preferred) or `actions/setup-python`
   - Go: `actions/setup-go`
   - Ruby: `actions/setup-ruby`
   - Java: `actions/setup-java`
   - Rust: `actions-rs/toolchain`
   - PHP: `shivammathur/setup-php`

   Pin the version explicitly using the project's version file (`.node-version`, `.python-version`, `go.mod`, `Gemfile`, etc.) or a hardcoded version.

   Never use obscure personal repositories, unmaintained forks, or actions without clear ownership and active maintenance.

## Workflow structure

Use this structure for new workflows:

```yaml
name: Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@<sha>
      - uses: astral-sh/setup-uv@<sha>
        with:
          python-version: ${{ matrix.python-version }}
          enable-cache: true
      - run: uv sync
      - run: uv run pytest
```

## Best practices

- Set minimal `permissions` at the workflow level, not per-job
- Use `ubuntu-latest` as the default runner unless a specific OS is required
- Cache dependencies using `actions/cache` or `actions/setup-*` built-in caching
- Use `concurrency` groups to prevent duplicate runs on the same branch when needed
- Name steps descriptively for easier log reading
- Group related output with `::group::` and `::endgroup::` annotations

## Common actions (verify versions before referencing them)

| Action                                                                           | Purpose                           |
| -------------------------------------------------------------------------------- | --------------------------------- |
| `actions/checkout`                                                               | Check out repository code         |
| `actions/setup-node` / `setup-python` / `setup-go` / `setup-ruby` / `setup-java` | Language runtime setup            |
| `actions-rs/toolchain`                                                           | Rust toolchain setup              |
| `shivammathur/setup-php`                                                         | PHP setup                         |
| `actions/upload-artifact` / `download-artifact`                                  | Job artifact sharing              |
| `actions/cache`                                                                  | Dependency caching                |
| `docker/build-push-action`                                                       | Docker image builds               |
| `docker/login-action`                                                            | Container registry authentication |

## Workflow

1. Determine the trigger events and branches
2. Look up the latest version of every action using `gh`
3. Draft the workflow with minimal permissions and `fail-fast: false` on matrix jobs
4. Check for `.github/dependabot.yml` — add a GitHub Actions ecosystem entry if missing
5. Validate the syntax with `actionlint` or `yq eval '.' .github/workflows/<file>.yaml`
