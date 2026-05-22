---
name: gh-cli
description: "All actions on GitHub must use this skill. Covers pull requests, issues, repositories, releases, GitHub Actions, searches, and API requests via the `gh` CLI."
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick Start

Verify authentication first:

```
gh auth status
```

All other `gh` commands support `-R OWNER/REPO` to target a specific repository. When omitted, the current directory's repo is used.

## Pull Requests

### Create

```
gh pr create --title "TITLE" --body "BODY"
```

- `--fill` — autofill title and body from commit messages
- `--fill-first` — use only the first commit
- `--fill-verbose` — use full commit msg + body
- `--draft` — create as draft
- `--base BRANCH` — set target branch
- `--head USER:BRANCH` — specify head from fork
- `-a @me` — self-assign
- `-l LABEL` — add labels (repeatable)
- `-r HANDLE` — request reviewers (repeatable)
- `-F file` — read body from file
- `--web` — open browser to create

Reference issues with `Closes #N` or `Fixes #N` in the body for auto-closure.

### View and List

```
gh pr list [--state open|closed|all] [--label NAME] [--reviewer ME]
gh pr view <NUMBER|URL|BRANCH>
gh pr status  # relevant PRs across repos
```

### Review

```
gh pr review --approve
gh pr review -r -b "Request changes because..."
gh pr review --comment -b "Comment only"
```

### Merge

```
gh pr merge --squash --delete-branch
gh pr merge --rebase --delete-branch
gh pr merge --merge --delete-branch
gh pr merge --auto  # auto-merge after checks pass
```

Use `--admin` to bypass merge queue requirements. Use `--match-head-commit SHA` for safety.

### Other

```
gh pr checkout <NUMBER>
gh pr diff <NUMBER>
gh pr checks <NUMBER>
gh pr update-branch <NUMBER>
gh pr close <NUMBER>
gh pr reopen <NUMBER>
gh pr edit <NUMBER> --title "..." --body "..."
gh pr lock <NUMBER>
gh pr unlock <NUMBER>
```

## Issues

### Create

```
gh issue create --title "TITLE" --body "BODY"
```

- `-l LABEL` — add labels (repeatable)
- `-a HANDLE` — assign (use `@me` or `@copilot`)
- `-m MILESTONE` — add to milestone
- `-T TEMPLATE` — use issue template
- `-F file` — read body from file
- `-e` — open editor for title and body
- `--web` — open browser

### View and List

```
gh issue list [--state open|closed|all] [--label NAME] [--assignee HANDLE]
gh issue view <NUMBER|URL>
gh issue status  # relevant issues across repos
```

### Manage

```
gh issue edit <NUMBER> --title "..." --label "..."
gh issue comment <NUMBER> -b "COMMENT"
gh issue close <NUMBER>
gh issue reopen <NUMBER>
gh issue lock <NUMBER>
gh issue unlock <NUMBER>
gh issue pin <NUMBER>
gh issue unpin <NUMBER>
gh issue transfer <NUMBER> OWNER/REPO
gh issue delete <NUMBER>
```

## Repositories

```
gh repo clone OWNER/REPO
gh repo fork OWNER/REPO
gh repo create [--private|--public]
gh repo list [--visibility public|private|all]
gh repo view [--web]
gh repo set-default OWNER/REPO
gh repo rename <NAME>
gh repo archive
gh repo unarchive
gh repo sync
gh repo delete OWNER/REPO  # destructive, confirm carefully
```

## GitHub Actions

```
gh run list
gh run view <RUN_ID>
gh run watch <RUN_ID>
gh run cancel <RUN_ID>
gh run rerun <RUN_ID>
gh run download <RUN_ID>
gh run delete <RUN_ID>

gh workflow list
gh workflow view <NAME>
```

## Releases

```
gh release create TAG --title "TITLE" --notes "NOTES"
gh release list
gh release view TAG
gh release upload TAG FILE
gh release download TAG --output FILE
gh release edit TAG
gh release delete TAG
gh release delete-asset TAG ASSET
gh release verify TAG
```

## Search

```
gh search issues "QUERY"
gh search prs "QUERY"
gh search repos "QUERY"
gh search code "QUERY"
gh search commits "QUERY"
```

Use `--` before queries with hyphens to avoid flag parsing issues:

```
gh search issues -- "is:open -label:bug"
```

## API Requests

For anything not covered by built-in commands:

```
gh api repos/{owner}/{repo}/releases
gh api repos/{owner}/{repo}/issues --jq '.[].title'
```

- `-X METHOD` — HTTP method (default GET, auto POST with params)
- `-f key=value` — string parameter
- `-F key=value` — typed parameter (auto-converts true/false/null/numbers, `@file` reads from file)
- `--jq 'QUERY'` — filter output with jq
- `--paginate` — fetch all pages
- `--slurp` — wrap paginated results into single array
- `--input file` — send file as request body
- `-H 'Key: Value'` — custom header
- `{owner}`, `{repo}`, `{branch}` — auto-resolved placeholders

### Nested parameters

```
gh api endpoint -F 'key[sub]=val' -F 'arr[]=a' -F 'arr[]=b'
```

### GraphQL

```
gh api graphql -f query='query { viewer { name } }' -F var='value'
```

## Output Formatting

Append to any command producing JSON:

```
--jq '.field'          # jq filter
--json FIELD,FIELD     # specific fields as JSON
```

## Common Workflows

### Create PR from current branch

```
gh pr create --fill --reviewer HANDLE
```

### Review and approve current branch PR

```
gh pr review --approve
```

### Squash merge and cleanup

```
gh pr merge --squash --delete-branch
```

### Check CI before merging

```
gh pr checks
```

### Full PR lifecycle

1. Push branch: `git push -u origin BRANCH`
2. Create PR: `gh pr create --fill`
3. Check CI: `gh pr checks`
4. Review: `gh pr review --approve`
5. Merge: `gh pr merge --squash --delete-branch`
