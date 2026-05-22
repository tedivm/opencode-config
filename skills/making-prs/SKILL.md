---
name: making-prs
description: "Use when creating a pull request, preparing changes for review, or pushing work to GitHub. Handles quality checks, branch management, conventional commits, openspec archival, and PR creation end-to-end."
---

## Quick start

Run quality checks, verify openspec status, create a feature branch, commit with conventional format, and open a PR.

## Workflow

### 1. Run Quality Checks

Load and execute the `quality-checks` skill to ensure all tests, lints, and formatting pass before proceeding. Do not skip this step.

If quality checks fail, fix everything until the full suite passes green. Only continue to step 2 once all checks pass.

### 2. Check OpenSpec Proposal Status

If the project uses OpenSpec (check for `.openspec/` directory or `openspec.json`):

1. Run `openspec list --json` to find active changes.
2. Identify the change relevant to the current work (match by name or title).
3. Check if the change has been archived:
   - If `openspec list` shows the change as active (not archived), ask the user: _"The OpenSpec proposal [name] is still active. Should I archive it before creating the PR?"_
   - If the user says yes, look for an openspec archive skill (e.g., `openspec-archive`) and load it to handle the archival. If no archive skill exists, fall back to running `openspec archive <change-name> --yes`.
   - If the user says no, proceed without archiving.
4. If no active changes exist or the change is already archived, proceed.

### 3. Branch Management

1. Get the default branch: `git symbolic-ref refs/remotes/origin/HEAD` or check `git remote show origin` for the HEAD branch.
2. Get the current branch: `git branch --show-current`.
3. If the current branch **is** the default branch:
   - Generate a descriptive branch name from the changes using `git diff --stat --cached` or `git status --short`.
   - Use conventional prefix format: `feat/...`, `fix/...`, `chore/...`, `refactor/...`, `docs/...`.
   - Create and checkout the new branch: `git checkout -b <branch-name>`.
4. If already on a non-default branch, proceed.

### 4. Stage and Commit

1. Stage all changes: `git add -A`.
2. Determine the conventional commit type by analyzing the changes:
   - `feat` — new functionality
   - `fix` — bug fixes
   - `refactor` — code restructuring without behavior changes
   - `chore` — maintenance, deps, config
   - `docs` — documentation only
   - `test` — adding or modifying tests
   - `style` — formatting, missing semicolons, etc
   - `perf` — performance improvements

   **Functional markdown:** `AGENTS.md` files and skills (`.opencode/skills/` or `skills/`) are markdown but function as agent instructions. Changes to them alter agent behavior — classify them as `feat` (new behavior), `fix` (corrected behavior), or `refactor` (restructured guidance), never `chore` or `docs`.

3. Write a conventional commit message:
   - Format: `<type>(<scope>): <description>`
   - Scope is optional but encouraged (use the main module, feature, or file changed).
   - Description is a concise, imperative summary (under 72 chars).
   - If changes are substantial, add a body paragraph explaining _what_ changed and _why_.

**Examples:**

```
feat(auth): add JWT-based session management
fix(payments): retry failed transactions with exponential backoff
chore(deps): bump redis client to v4.2
refactor(parser): extract tokenization into standalone module
```

4. Commit: `git commit -m "<title>" [-m "<body>"]`.

### 5. Push and Create PR

1. Push the branch: `git push -u origin <branch-name>`.
2. Generate a PR title and body:
   - **Title:** Clear, concise summary of the change (match conventional commit style).
   - **Body summary (first paragraph):** High-level overview of what changed and why.
   - **Body details (following sections):**
     - What changed (bullet points of key modifications)
     - What reviewers should focus on (specific areas needing attention, tricky logic, potential edge cases)
     - Testing notes (how to verify, any manual testing required)
   - Reference the OpenSpec change if applicable: `Implements [change-name]` or link to the spec.
3. Create the PR using `gh-cli` skill:
   ```
   gh pr create --title "TITLE" --body "BODY"
   ```
4. Present the PR URL to the user.

### 6. Post-Merge Cleanup

When the user confirms the PR has been merged:

1. Switch back to the default branch: `git checkout <default-branch>`.
2. Pull the latest changes: `git pull origin <default-branch>`.
3. Confirm the merge is local.

## Constraints

- Never commit directly to the default branch.
- Always run quality checks before committing.
- Always verify openspec status if the project uses it.
- Use conventional commit format for all commit messages.
- PR bodies should focus on _what changed_ and _what reviewers should focus on_, not a line-by-line diff.
