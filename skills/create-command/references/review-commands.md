# Review Commands

Use these patterns when creating commands whose primary purpose is review, analysis, or evaluation — design reviews, code reviews, architecture assessments, security audits, etc.

## Perspective section

Review commands benefit from framing the agent's role beyond just reviewing the immediate artifact. Add a `## Perspective` section that defines the agent's scope of concern:

```markdown
## Perspective

You are a steward of the project, not just a reviewer of this [document/change]. Your job is to protect the project's long-term health. A finding may be outside the [document's/change's] stated scope but still highly valuable to the project — flag it. An architectural change that simplifies [operations/maintenance/safety] is worth surfacing even if the proposal doesn't address it.
```

Customize the bracketed text to match the command's domain.

## Category and Impact classification

Instead of a single severity level, use two dimensions:

```markdown
## Return Format

A numbered list of findings, each with:

- **Category:** What kind of finding this is — e.g., `Bug` (incorrect API, broken approach), `Architectural Change` (fundamental approach shift), `Improvement` (better pattern, missing best practice), `Completeness` (missing section, gap in coverage), `Security`, `Performance`, `Operational` (deployment, monitoring, maintenance)
- **Impact:** How much this benefits the overall system long-term, not just this proposal:
  - `Critical` — prevents system failure, data loss, or security breach; or unlocks a capability that fundamentally improves the project's trajectory
  - `High` — significant lasting benefit to the project; prevents major future rework; materially improves maintainability, reliability, or developer experience
  - `Medium` — meaningful improvement worth doing; reduces friction, clarifies ambiguity, or hardens a weak point
  - `Low` — nice to have; low cost to defer or skip without lasting consequences
- The section or decision it relates to
- What the issue is
- Why it matters
- Your recommendation — what should be done, with source URLs for verification
- Suggested fix (if applicable)

Group by Category, then order by Impact within each category. Lead with Critical and High impact findings regardless of category.
```

Customize the Category list to match the command's domain. The Impact levels can stay as-is.

## Example output

Include a concrete example of what good output looks like. This dramatically improves consistency across different models:

**Example:**

```markdown
### Critical

**1. Category — Impact**

- **Section:** Where the finding relates
- **Issue:** What's wrong
- **Why it matters:** Long-term consequence
- **Recommendation:** What to do, with trade-offs if applicable
- **Fix:** Specific change (if applicable)
- **Sources:** URLs for verification
```

## Prose over arguments for review commands

Review and analysis commands often work better as prose instructions where the agent discovers relevant files itself, rather than using `$1`, `$ARGUMENTS`, or `@filepath` references. This gives the agent flexibility to find the right artifacts:

```markdown
Find the [target] document. Look for [pattern] in the current project. If multiple exist, review the most recently modified one. **If no [target] is found, report this immediately and stop.**
```

## When to use this

Load this reference when the command:

- Reviews designs, proposals, or specifications
- Evaluates code quality, architecture, or security
- Assesses completeness or correctness of documentation
- Produces findings that need categorization and prioritization
