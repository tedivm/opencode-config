---
description: Update all GitHub Action versions to their latest releases
subtask: true
---

## Overview

Scan all GitHub Action workflow files, find every action used, check their latest releases via `gh`, and update them while preserving the project's version pinning conventions.

## Constraints

- **Never** update actions pinned to a full SHA commit hash unless you can confirm a newer SHA from the same tag branch
- Preserve the **pinning convention** of each action — if it's pinned to major, minor, patch, or SHA, update to the matching granularity
- Do not change action configuration arguments, only the version reference
- If a workflow file contains multiple actions, update all applicable ones in a single edit
- Skip any action whose owner is the same as the current repository owner (internal actions)

## Version Update Rules

Extract the granularity of the current version reference, then match it to the latest release:

| Current reference | Pinning level | Update to                                              |
| ----------------- | ------------- | ------------------------------------------------------ |
| `@v6`             | Major only    | `@v7` (latest major)                                   |
| `@v6.5`           | Major.minor   | `@v7.2` (latest major.minor)                           |
| `@v6.5.3`         | Full semver   | `@v7.2.1` (latest major.minor.patch)                   |
| `@abc1234...`     | SHA commit    | `@def5678...` (resolve the same tag to its newest SHA) |

If the action already uses the latest version at its pinning level, skip it and note it as up-to-date.

## Phases

1. **Discover workflows** — list all `.yml` and `.yaml` files in `.github/workflows/`
2. **Extract all actions** — grep each workflow for `uses: owner/repo@version` patterns. Collect a deduplicated list of unique `owner/repo` pairs.
3. **Filter out internal actions** — remove any action where the owner matches the current repo owner.
4. **Fetch latest releases** — for each remaining `owner/repo`, run:
   ```
   gh release list --repo owner/repo --limit 1 --json tagName
   ```
   Extract the latest tag (strip leading `v` if present for comparison).
5. **Determine the update target** — for each action usage in each workflow file:
   - Read the current version reference
   - Classify its pinning level (major, minor, patch, SHA)
   - Compute the new version from the latest release matching that granularity
   - If pinned to SHA, resolve the latest tag to its SHA:
     ```
     gh api repos/owner/repo/commits/SHA --jq '.sha'
     ```
     Or use `git ls-remote` equivalent via `gh api repos/owner/repo/refs/tags/TAG`
6. **Apply updates** — edit each workflow file, replacing old version references with new ones. Only modify lines where the version actually changes.
7. **Summary** — produce a table of what was updated, what was skipped (already current), and any actions that failed to resolve.

## Checklist

- [ ] All workflow files in `.github/workflows/` scanned
- [ ] Internal repo actions excluded
- [ ] Every action's latest release fetched via `gh`
- [ ] Pinning convention preserved for every update
- [ ] SHA-pinned actions resolved to the SHA of the latest tag
- [ ] Only lines with actual version changes are edited
- [ ] Summary table produced showing all changes
