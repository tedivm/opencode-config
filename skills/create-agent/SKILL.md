---
name: create-agent
description: Use when creating, configuring, or modifying opencode agents. Covers Markdown agent definitions, frontmatter options (description, mode, hidden, color), primary vs subagent types, and detailed prompt structure. Don't use for skills, commands, or general config — this is specifically for agents.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Write a Markdown file in `.opencode/agents/` (per-project, default) or `~/.config/opencode/agents/` (global). The filename without `.md` becomes the agent name.

Do not use `opencode agent create` — it is an interactive wizard that produces inferior results compared to writing the file directly.

## Workflow

1. **Determine scope** — default to per-project (`.opencode/agents/`). Use global (`~/.config/opencode/agents/`) only if explicitly requested.
2. **Determine mode** — `primary` (direct user interaction, Tab-cycled, default), `subagent` (invoked by other agents or @-mention), or `all` (both). Default to `primary`.
3. **Write the description** — this is **required** and drives auto-invocation. Make it specific and action-oriented. See [Description guidance](#description-guidance).
4. **Add subagent output guidance** — if the mode is `subagent` or `all`, include a `## Subagent Output` section. See [Subagent Output](#subagent-output).
5. **Set permissions** — omit by default to inherit inherited settings. Only add restrictions when the user explicitly requests them. Load [references/permissions.md](references/permissions.md) for permission keys, glob patterns, and common profiles.
6. **Write the prompt** — inline in the Markdown body after the frontmatter. This is the core of the agent. See [Prompt structure](#prompt-structure).
7. **Create the file** — `<agent-name>.md` in the chosen directory.
8. **Hand off** — user tests and provides feedback for iteration.

## Markdown format

```markdown
---
description: <one sentence describing what this agent does>
mode: primary
---

# Persona

<2-4 paragraphs establishing identity, voice, expertise, approach>

## Goals

<Overview sentence of what the agent is oriented toward>

### <Goal Category>

<Brief intro sentence>

- Specific item to look for or do
- Another specific item
- Use bullet lists, not paragraphs

#### <Sub-Topic>

- More specific items under this category

### <Another Goal Category>

<Brief intro sentence>

- Specific item
- Specific item

## Constraints

### <Constraint Name>

- Hard rule or boundary
- Another hard rule

### <Another Constraint>

- Hard rule
- Hard rule

## Flows

### <Flow Name>

The user asks you to <action>.

1. Step one — what to do and what tools to use
2. Step two
3. Step three
4. Present findings to the user
```

## Prompt structure

Agent prompts are long, detailed, and specific. A well-written agent prompt is typically 150-350 lines. Structure it as four sections (five for subagents — see [Subagent Output](#subagent-output)):

### Persona

Establish who the agent is, its voice, its expertise, and its approach. This is not a single sentence — it's 2-4 paragraphs that paint a complete picture of the agent's identity.

Be specific about:

- **Role and seniority** — is this a senior architect, a meticulous reviewer, a pragmatic developer?
- **Voice and tone** — is it direct, diplomatic, scathing, encouraging?
- **Expertise areas** — what domains, languages, or patterns does it specialize in?
- **Approach** — how does it think? What's its methodology? What mental models does it use?

The persona should feel like stepping into a specific role, not reading a job description.

### Goals

What the agent is oriented toward. Use `###` subheaders for each goal category and `####` for sub-topics. Use bullet lists, not paragraphs — lists are scannable, paragraphs are not.

Structure:

- `###` for each major goal area (Correctness, Security, Maintainability, etc.)
- A brief intro sentence under each `###` header
- Bullet lists of specific things to look for, check, flag
- `####` for sub-topics when a category has multiple aspects (Boilerplate Reduction, File Size, Testability under Refactoring)

Each bullet should be specific and actionable: "Off-by-one errors in array indexing" not "Check for bugs."

### Constraints

Hard rules. What the agent won't do, won't tolerate, or must always do. Use `###` subheaders for each constraint, followed by bullet lists.

Constraints keep the agent focused and prevent it from drifting into generic behavior. "You do not implement" is more effective than "Try not to write code."

### Flows

Common interaction patterns the agent will encounter. Each flow describes:

- **What the user asks** — the trigger phrase or scenario
- **What the agent does** — numbered steps with specific tools and commands
- **What the agent produces** — the output format and delivery method

Flows can be composable — a Document Issues flow might run after any other flow. Include flows when the agent has repeatable, multi-step interaction patterns.

Always frame flows as examples, not an exhaustive list. Add an intro line like: "These are examples of common interaction patterns, not an exhaustive list. Use them as templates for custom flows or tasks that arise. Adapt the steps to fit the specific context — the structure is the guide, not the constraint."

### Subagent Output

For agents with `mode: subagent` or `mode: all`, add a `## Subagent Output` section at the end of the prompt. A subagent does extensive work — research, exploration, evaluation — but the parent agent only sees the final message. Without explicit output guidance, subagents tend to include their working process and discarded alternatives, omit recommendations and source URLs, or write narrative prose instead of structured findings.

Add this section to the agent's prompt:

```markdown
## Subagent Output

You are running as a subagent. Your final message is the only output the primary agent receives. It must be self-contained and actionable.

**What the primary agent needs:**

- Findings detailed enough to act on — specific issues, why they matter, and suggested fixes.
- Your recommendation on each finding — based on your research, what should actually be done? Don't just present facts; offer a clear assessment and preferred path forward. If there are genuine trade-offs requiring a decision, present the viable options with your assessment of each so the parent agent or human can choose.
- References to the documentation, URLs, and sources you used so the agent can dig deeper if needed.
- Enough context in each finding that the agent doesn't need to re-read your entire thought process.

**What the primary agent does not need:**

- Discarded alternatives or ideas you explored and ruled out. The whole point of a subagent is that the primary agent doesn't need to see your working.
- Exhaustive step-by-step narration of your research process.
- Repetition or padding.

Be concise but thorough. Each finding should stand on its own. Include source URLs alongside findings so the agent can verify or explore further independently.
```

Customize the "what the primary agent needs" list to match the agent's domain:

- **Review agents:** findings with category, impact, recommendation, sources
- **Research agents:** summarized findings with source URLs for deeper investigation
- **Planning agents:** ordered steps with dependencies, risks, and decision points
- **Analysis agents:** structured data, patterns found, anomalies flagged

## Description guidance

The description is the single most important field — it determines when the agent gets auto-invoked. Write it differently depending on the agent's mode.

### Primary agents (written for humans)

Primary agents appear in @-autocomplete and are selected by users. Descriptions should convey personality and expertise so the human knows what to expect.

- **Be specific about the persona** — "Critical code reviewer focused on quality and maintainability" not "Helps with code"
- **Include trigger keywords** the user is likely to mention
- **Keep it to one sentence** — every token competes with conversation context
- **Use action-oriented language** — "Performs security audits" not "Security audit tool"

**Good examples:**

- `Critical code reviewer focused on quality, security, and maintainability`
- `Performs security audits and identifies vulnerabilities`
- `Strategic planner for complex technical decisions`

**Bad examples:**

- `Helpful assistant` (no persona)
- `Reviews the auth module` (too task-specific)
- `Does code review` (no personality or focus)

### Subagents (written for the agent)

Subagents are auto-invoked by the primary agent based on context. Descriptions should follow the same methodology as skill descriptions — third-person, imperative, trigger-focused.

- **Lead with the trigger context** — "Use when..." rather than a feature list
- **Use imperative, action-oriented language** — "Use when verifying information against external sources" not "Research agent for..."
- **Include negative triggers** when helpful — "Don't use for code implementation or simple lookups"
- **Include key terms** the primary agent is likely to mention
- **Keep it to one sentence** — every token competes with conversation context

**Good examples:**

- `Use when verifying information against external sources, comparing libraries or frameworks, investigating bugs, or looking up current API documentation. Don't use for code implementation or reviews.`
- `Use when creating, generating, or scaffolding a new Agent Skill. Don't use for modifying existing skills.`

**Bad examples:**

- `Research agent for library comparisons and bug investigation` (no trigger context, reads like a label)
- `Helps with research` (too vague, no activation signal)

## Configuration options

| Option        | Required | Description                                                     |
| ------------- | -------- | --------------------------------------------------------------- |
| `description` | Yes      | What the agent does and when to use it. Drives auto-invocation. |
| `mode`        | No       | `primary`, `subagent`, or `all`. Defaults to `primary`.         |
| `permission`  | No       | Fine-grained tool access control.                               |
| `hidden`      | No       | `true` to hide from @-autocomplete.                             |
| `disable`     | No       | `true` to disable the agent.                                    |
| `color`       | No       | Hex color or theme name (`primary`, `accent`, `success`, etc).  |

Model, temperature, top_p, and steps are advanced options — only set them when explicitly requested. See [Advanced features](#advanced-features).

## Permissions

Default is permissive — inherit the general agent's permissions. Only add `permission:` to the frontmatter when the user explicitly requests restrictions. Load [references/permissions.md](references/permissions.md) for permission keys, glob patterns, common profiles, and task permissions.

## Complete example

See [references/example-reviewer.md](references/example-reviewer.md) for a full, production-quality agent prompt (400+ lines). It demonstrates:

- **Persona depth** — voice, expertise, mental models, approach
- **Goal specificity** — `###` categories, `####` sub-topics, bullet lists of concrete things to check
- **Constraint hardness** — clear boundaries on what the agent will and won't do
- **Flow design** — numbered-step interaction patterns for PR review, OpenSpec review, change review, issue documentation, dependency audit, architecture review, security audit

## Advanced features

### Model override

Only set `model` when explicitly requested. Use `provider/model-id` format (e.g., `anthropic/claude-sonnet-4-20250514`). Useful for using a faster model for planning or a more capable model for implementation.

```yaml
model: anthropic/claude-sonnet-4-20250514
```

### Temperature

Only set `temperature` when explicitly requested. Use `0.1` for deterministic tasks (analysis, review), `0.3-0.5` for general dev, `0.6+` for creative work.

```yaml
temperature: 0.1
```

### Top P

Alternative to temperature for controlling response diversity. Range `0.0-1.0`.

```yaml
top_p: 0.9
```

### Steps limit

Control max agentic iterations before forcing a summary response. Useful for cost control.

```yaml
steps: 5
```

### Provider-specific options

Any unrecognized options pass through to the model provider (e.g., `reasoningEffort: "high"` for OpenAI reasoning models).

## Notes

- The filename (without `.md`) becomes the agent identifier
- Hidden agents (`hidden: true`) still work via the Task tool but do not appear in @-autocomplete
- Built-in agents (Build, Plan, General, Explore, Scout) can be customized or disabled
