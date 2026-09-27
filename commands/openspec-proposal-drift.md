---
description: Review drift in an OpenSpec proposal against archived changes
agent: general
subagent: true
---

# OpenSpec Proposal Drift Review

## Overview

Review an OpenSpec proposal for drift — identify how the codebase and specs have evolved since the proposal was last updated, and report what in the proposal may be outdated as a result.

## Guidance

### Research

**Your memory is unreliable. Always search first.**

Use glob and grep to find the proposal, read its metadata, discover archived changes, and analyze what has changed since the proposal was written.

### Subagent Output

You are running as a subagent. Your final message is the only output the primary agent receives. It must be self-contained and actionable.

**What the primary agent needs:**

- Findings detailed enough to act on — specific drift issues, why they matter, and what should be updated in the proposal.
- Your recommendation on each finding — what parts of the proposal need refreshing, what can stay as-is.
- Enough context in each finding that the agent doesn't need to re-read your entire thought process.

**What the primary agent does not need:**

- Discarded alternatives or ideas you explored and ruled out.
- Exhaustive step-by-step narration of your research process.
- Repetition or padding.

Be concise but thorough. Each finding should stand on its own.

## User Request

The user may specify a particular proposal to review or additional scope constraints.

```markdown
$ARGUMENTS
```

If there is nothing in the quote block above then there are no special requests.

## Review

### 0. Setup

1. Locate the proposal to review:
   - **If the User Request above specifies a target change**, use it as the change name and look for `openspec/changes/<that-name>/proposal.md`.
   - **If the User Request is empty**, search `openspec/changes/*/proposal.md` and pick the most recently modified one.
   - **If no proposal is found, report this immediately and stop.**
2. Note the proposal's last modification time using `stat` or `ls -l` on the proposal file.
3. Read the full proposal document.
4. Read the proposal's associated artifacts: `design.md`, `tasks.md`, and any delta specs in `specs/`.

### 1. Discover Archived Changes

1. List all entries in `openspec/changes/archive/` — these are completed changes sorted by date.
2. Identify which archived changes have timestamps **after** the proposal's last modification time. These represent work that happened while the proposal was sitting idle.
3. For each relevant archived change, read its proposal, design, delta specs, and any other artifacts to understand what changed.

### 2. Analyze Drift

Compare the proposal against the post-proposal archived changes and identify drift in these dimensions:

**Context and Assumptions:**

- Does the proposal's Context section still accurately describe the current state of the system?
- Have any of its assumptions about existing code, APIs, or infrastructure been invalidated by subsequent changes?
- Are there new capabilities or constraints that the proposal doesn't account for?

**Scope and Overlap:**

- Does any archived change partially or fully overlap with what this proposal intends to do?
- Has related work already moved the goalposts — making parts of the proposal redundant, unnecessary, or requiring adjustment?
- Are there conflicts between what this proposal plans and what has already been implemented?

**Design and Technical Approach:**

- Has the project's architectural patterns, conventions, or preferred libraries changed since the proposal was written?
- Are there new dependencies, removed dependencies, or version changes that affect the proposed approach?
- Does the project's error handling, logging, or configuration style differ from what the proposal assumes?

**Spec Deltas:**

- Do the proposal's delta specs still make sense given the current state of `openspec/specs/`?
- Have any requirements the proposal plans to add already been added by another change?
- Have any requirements the proposal plans to modify already been modified by another change?
- Have any requirements the proposal plans to remove already been removed or superseded?

**Task Relevance:**

- Are the proposed tasks still valid, or have some already been completed by other changes?
- Do the tasks reference files, functions, or modules that no longer exist or have moved?

### 3. Freshness Assessment

Provide an overall assessment of how stale the proposal is:

- **Current** — minimal drift, proposal is still a solid starting point
- **Partially Stale** — some sections need updates, particularly context or scope
- **Significantly Stale** — major portions need rewriting; the proposal's foundation may be invalid
- **Obsolete** — the proposal's goals have been met or superseded by other work

## Perspective

You are a steward of the project, not just a reviewer of this proposal. Your job is to protect the project's long-term health. Drift isn't just about whether the proposal is technically accurate — it's about whether investing effort in this proposal still makes sense given the project's trajectory. Flag proposals that are chasing a problem that's already been solved or that conflict with the direction the project has taken.

## Return Format

A numbered list of findings, each with:

- **Category:** What kind of drift this is — `Context Drift` (outdated assumptions about current state), `Scope Overlap` (work already done by another change), `Design Drift` (technical approach no longer fits project conventions), `Spec Drift` (delta specs conflict with current specs), `Task Drift` (tasks reference stale code), `Obsolete` (goals already achieved)
- **Impact:** How much this affects the proposal's viability:
  - `Critical` — the proposal's core assumptions are invalid; the proposal needs a fundamental rewrite or should be abandoned
  - `High` — significant portions need updating; the proposal can be salvaged but requires substantial effort
  - `Medium` — targeted updates needed; specific sections are stale but the overall approach holds
  - `Low` — minor tweaks needed; cosmetic or formatting updates
- The section or artifact it relates to (e.g., "Context", "D2", "specs/auth/spec.md", "tasks.md §3")
- What the drift is
- What changed (reference the archived change name and date)
- Your recommendation — what to update, whether to proceed, or whether to abandon

Group by Category, then order by Impact within each category. Lead with Critical and High impact findings.

**Example:**

```text
## Proposal Drift Review: add-search

**Proposal:** openspec/changes/add-search/proposal.md
**Last Modified:** 2025-06-15
**Archived Changes Since:** 3 (add-analytics, refactor-auth, add-file-uploads)
**Overall Freshness:** Partially Stale

### Critical

**1. Scope Overlap — Critical**

- **Section:** Intent, D1 (Search Indexing)
- **Drift:** The proposal plans to add full-text search with Meilisearch. The archived change `2025-07-01-add-analytics` already integrated Meilisearch for analytics event indexing, establishing the project's Meilisearch conventions, connection patterns, and Docker setup.
- **Changed by:** `add-analytics` (archived 2025-07-01)
- **Recommendation:** Remove the Meilisearch infrastructure setup from this proposal's scope. Leverage the existing infrastructure and follow the established patterns from `add-analytics`. Update D1 to reference the existing connection module.

### Medium

**2. Context Drift — Medium**

- **Section:** Context
- **Drift:** Proposal states the project uses Express middleware for routing. The `refactor-auth` change (archived 2025-06-28) migrated routing to a new router pattern with centralized route registration.
- **Changed by:** `refactor-auth` (archived 2025-06-28)
- **Recommendation:** Update the Context section to reflect the new router pattern. Adjust any design decisions that reference the old middleware-style routing.
```

## Checklist

- [ ] Proposal identified and last modification time noted
- [ ] All archived changes after the proposal's modification time discovered
- [ ] Each relevant archived change's artifacts read and understood
- [ ] Context and assumptions checked against current state
- [ ] Scope overlap with completed work identified
- [ ] Design approach checked against current project conventions
- [ ] Delta specs compared against current `openspec/specs/`
- [ ] Tasks checked for stale file references
- [ ] Overall freshness assessment provided
- [ ] Findings grouped by Category, ordered by Impact
- [ ] Each finding includes the responsible archived change and recommendation
