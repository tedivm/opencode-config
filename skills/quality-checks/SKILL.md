---
name: quality-checks
description: Use when asked to "fix things", "qa", "run tests and fix things", "test until clean", or similar requests to iteratively run quality checks and fix failures until everything passes. Don't use for single-purpose tasks like running only tests or only linting without fixes.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Discover project tooling, run all quality checks, fix failures, and repeat until everything passes.

## Workflow

1. Check for task definitions in `AGENTS.md`, `Makefile`, `justfile`, or `package.json` scripts
2. Identify commands for: tests, linting, formatting, documentation builds, and other chores
3. Run all checks and capture results
4. If any check fails, fix the issues
5. Re-run formatting/chores, then the full test suite
6. Repeat steps 4-5 until all checks pass
7. Report final status

## Constraints

- Prefer project-defined tooling (AGENTS.md, Makefile, justfile, package.json) over guessing
- On subsequent runs, reuse previously discovered commands instead of re-researching
- Always re-run the full suite after each fix — do not assume partial re-checks are sufficient
- Report all failures with file paths and line numbers before fixing

## Checklist

- [ ] Test suite executed
- [ ] Lint/format checks completed
- [ ] Documentation/chores run (if applicable)
- [ ] All failures fixed
- [ ] Final pass confirms everything green
