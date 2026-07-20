---
description: Review drift between OpenSpec specs and the actual codebase
agent: general
subtask: true
---

# OpenSpec Spec Drift Review

## Overview

Review the accepted specs in `openspec/specs/` against the actual codebase. Find drift in both directions: places where the code doesn't match the specs, and places where the specs are missing features that exist in the system.

## Guidance

### Research

**Your memory is unreliable. Always search first.**

You need to thoroughly explore both the specs directory and the codebase. Use glob and grep extensively to map the codebase structure, find relevant implementations, and cross-reference them against spec requirements.

### Subagent Output

You are running as a subagent. Your final message is the only output the primary agent receives. It must be self-contained and actionable.

**What the primary agent needs:**

- Findings detailed enough to act on — specific spec requirements vs actual code behavior, or code features with no spec coverage.
- Your recommendation on each finding — should the code be fixed, or should the spec be updated? Don't just present facts; offer a clear assessment.
- File paths and line references so the agent can navigate to the relevant code or spec sections.
- Enough context in each finding that the agent doesn't need to re-read your entire thought process.

**What the primary agent does not need:**

- Discarded alternatives or ideas you explored and ruled out.
- Exhaustive step-by-step narration of your research process.
- Repetition or padding.

Be concise but thorough. Each finding should stand on its own.

## User Request

The user may have additional requirements, such as focusing the review on specific spec files or domains.

```markdown
$ARGUMENTS
```

If there is nothing in the quote block above then there are no special requests.

## Review

### 0. Setup

1. List all spec files in `openspec/specs/`. Read each spec file in full.
2. Read the project's `AGENTS.md` for conventions and project structure.
3. Explore the codebase structure — identify key directories, entry points, and domain boundaries.

**If no specs exist, report this immediately and stop.**

### 1. Code-to-Spec Drift

For each spec requirement, verify the actual code matches the specified behavior. Work through each spec file systematically:

- **Map requirements to code.** For each requirement and scenario in a spec, find the corresponding code. Use grep to search for relevant function names, route handlers, model definitions, API endpoints, and UI components.
- **Verify behavior matches.** Read the actual implementation. Does it do what the spec says? Check for:
  - Missing functionality the spec requires
  - Different behavior (e.g., spec says 30-min timeout, code uses 15-min)
  - Missing error handling the spec mandates
  - Missing validation the spec requires
  - Different data structures or API contracts
  - Missing edge case handling the spec's scenarios describe
- **Check completeness.** Are all requirements in the spec actually implemented? Or are some still aspirational?

### 2. Spec-to-Code Drift

For each significant feature, module, or behavior in the codebase, verify there is spec coverage:

- **Map code to specs.** As you explore the codebase, note features, behaviors, APIs, and data models that exist in code but have no corresponding spec requirement.
- **Identify uncovered areas.** Look for:
  - Implemented features with no spec documentation
  - API endpoints not described in any spec
  - Data models or database tables without spec definitions
  - Error handling or edge case behavior not captured in scenarios
  - Configuration or environment-dependent behavior not specified
  - Recently added features (check git history for recent additions) that haven't been spec'd
- **Check for stale specs.** Are there specs describing behavior that no longer exists in the code? Features that were removed but not de-specified?

### 3. Cross-Spec Consistency

Check for consistency issues across the specs themselves:

- **Conflicting requirements.** Do different specs describe the same behavior differently?
- **Overlapping scope.** Do multiple specs claim ownership of the same domain?
- **Missing cross-references.** Do specs that depend on each other lack references?
- **Inconsistent terminology.** Are the same concepts named differently across specs?

### 4. Spec Quality

Evaluate the specs themselves for quality issues:

- **Missing scenarios.** Are requirements stated without concrete, testable scenarios?
- **Vague language.** Are requirements written in ambiguous terms that could mean multiple things?
- **Missing RFC 2119 keywords.** Do requirements lack SHALL/MUST/SHOULD/MAY strength indicators?
- **Implementation leakage.** Do specs contain implementation details that should be in design documents?
- **Missing Purpose sections.** Do specs lack high-level domain descriptions?

## Perspective

You are a steward of the project, not just a reviewer of specs. Your job is to protect the project's long-term health. Spec drift is a real risk — specs that don't match code create a false source of truth that misleads both humans and AI agents. A finding that the specs are systematically outdated is as valuable as finding a single bug.

## Return Format

A numbered list of findings, each with:

- **Direction:** Which way the drift flows — `Code-Missing` (code doesn't match spec), `Spec-Missing` (code has features not in specs), `Stale-Spec` (spec describes removed behavior), `Conflict` (specs contradict each other), `Quality` (spec writing issues)
- **Impact:** How much this matters:
  - `Critical` — behavior that affects users, security, or data integrity; specs that actively mislead
  - `High` — significant feature gap or behavioral mismatch; missing coverage for core functionality
  - `Medium` — meaningful drift in edge cases, error paths, or secondary features
  - `Low` — minor wording issues, missing scenarios for trivial behavior
- The spec file and section it relates to (e.g., `specs/auth/spec.md — Requirement: Session Expiration`)
- The code file and location it relates to (e.g., `src/middleware/session.ts:23`)
- What the drift is
- Why it matters
- Your recommendation — fix the code, update the spec, or both
- Suggested fix (if applicable)

Group by Direction, then order by Impact within each group. Lead with Critical and High impact findings regardless of direction.

**Example:**

```markdown
## Spec Drift Review

### Code-Missing

**1. Code-Missing — Critical**

- **Spec:** `specs/auth/spec.md` — Requirement: Session Expiration (30-min timeout)
- **Code:** `src/middleware/session.ts:23` — uses 15-min timeout
- **Issue:** The spec mandates a 30-minute idle timeout, but the implementation uses 15 minutes. Users will experience unexpected logouts.
- **Why it matters:** This directly impacts user experience. The spec is the agreed-upon contract — the code should match.
- **Recommendation:** Update the code to match the spec's 30-minute requirement unless there's a documented reason for the change. If 15 minutes is the intentional new standard, update the spec.
- **Fix:** Change `SESSION_TIMEOUT_MS = 15 * 60 * 1000` to `30 * 60 * 1000` in `src/middleware/session.ts`.

### Spec-Missing

**2. Spec-Missing — High**

- **Spec:** No coverage in `specs/`
- **Code:** `src/services/webhook.ts` — webhook delivery with retry logic
- **Issue:** The webhook service (delivery, retry backoff, failure handling) has no spec coverage. This is a user-facing integration surface that should be specified.
- **Why it matters:** Without specs, future changes to webhook behavior have no guardrails. AI agents working on related features won't know the expected behavior.
- **Recommendation:** Create a `specs/webhooks/spec.md` that covers delivery guarantees, retry behavior, error handling, and the webhook event schema.
- **Fix:** Draft spec covering the existing webhook implementation as the baseline.

### Stale-Spec

**3. Stale-Spec — Medium**

- **Spec:** `specs/payments/spec.md` — Requirement: PayPal Processing
- **Code:** No PayPal-related code found in `src/`
- **Issue:** The spec describes PayPal as a supported payment method, but no PayPal integration exists in the codebase. This appears to be aspirational or legacy.
- **Why it matters:** This creates false expectations. Anyone reading the spec will assume PayPal works.
- **Recommendation:** If PayPal is planned, keep the spec but add a note that it's aspirational. If PayPal was removed, remove or mark the requirement as REMOVED.
- **Fix:** Remove the PayPal requirement or update it to reflect its aspirational status.
```

## Checklist

- [ ] All spec files in `openspec/specs/` read and analyzed
- [ ] Each spec requirement cross-referenced against actual code
- [ ] Each significant code feature checked for spec coverage
- [ ] Cross-spec consistency verified — no conflicting requirements
- [ ] Spec quality evaluated — scenarios, RFC 2119 keywords, Purpose sections
- [ ] Code-to-spec drift identified (code doesn't match spec)
- [ ] Spec-to-code drift identified (code has unspec'd features)
- [ ] Stale specs identified (specs describe removed behavior)
- [ ] Findings grouped by Direction, ordered by Impact
- [ ] Each finding includes file paths and a clear recommendation
- [ ] Overall health assessment provided — are specs a reliable source of truth?
