---
name: create-command
description: Use when creating or modifying custom opencode commands in the `commands/` directory. Covers markdown command files, frontmatter options (description, agent, model, subtask), prompt templates with $ARGUMENTS, shell output injection, and file references.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Create a markdown file in `.opencode/commands/` (per-project, default). Only use `~/.config/opencode/commands/` (global) if explicitly requested. The filename (without `.md`) becomes the command name.

```
---
description: Run tests with coverage
---
Run the full test suite with coverage report and show any failures. Focus on the failing tests and suggest fixes.
```

The command runs as `/test` in the TUI.

## Workflow

1. **Determine scope** — default to per-project (`.opencode/commands/`). Use global (`~/.config/opencode/commands/`) only if explicitly requested.
2. **Assess command type** — determine what kind of command this is and load the matching reference files. See [Command types](#command-types) below.
3. **Decide execution context** — review and research-heavy commands should default to `subtask: true`. Simple actions don't need it. If unsure, ask the user.
4. **Create the file** — name it `<command-name>.md`. Use the `system-action` pattern: lowercase, hyphen-separated, named for what it does (e.g., `gha-upgrade`, `openspec-review`, `robs-design-review`).
5. **Write frontmatter** — set `description` (required). Add `agent`, `model`, or `subtask` as determined above.
6. **Write the template** — the body content becomes the prompt sent to the LLM. See [Prompt structure](#prompt-structure) below.
7. **Hand off to the user** — the user tests the command with `/command-name` and tells you what to refine. Iterate based on their feedback.

## Command types

Commands fall into these categories. A single command often combines multiple types — load every matching reference.

### Subagent

The command runs as a subagent and its final message is the only thing the parent agent receives.

**Make it a subagent when:** the task is heavy, multi-step, or benefits from isolated execution. Examples: comprehensive reviews, deep research, multi-phase analysis.

**How to set it up:** add `subtask: true` to the frontmatter. If the command benefits from a specialized agent (e.g., `scout` for research, `explore` for codebase analysis), add an `agent` field too. Load [references/subagent-output.md](references/subagent-output.md) and add its guidance to the command template. If you're specifying an `agent`, also load [references/agent-selection.md](references/agent-selection.md) to pick the right one.

### Review / Analysis

The command evaluates, audits, or reviews something and produces categorized findings.

**Make it a review command when:** the user wants to assess existing work — design documents, code, architecture, security posture, documentation quality.

**How to set it up:** set `subtask: true` in the frontmatter. Load [references/review-commands.md](references/review-commands.md) and incorporate its patterns. This adds a perspective section (framing the agent's role), a Category + Impact classification system for findings, and guidance on prose-vs-arguments for discovery-based tasks.

### Research-heavy

The command verifies information against external sources — live documentation, APIs, package registries, URLs.

**Make it a research-heavy command when:** accuracy matters and the agent's training data can't be trusted. Examples: validating third-party APIs, checking if models or packages exist, verifying installation instructions, researching best practices.

**How to set it up:** set `subtask: true` in the frontmatter. Load [references/research-methodology.md](references/research-methodology.md) and add its "search first" guidance to the command template. This establishes the methodology before the agent starts working.

### Simple action

The command does a straightforward task with a clear outcome.

**Use this when:** the task is a single action — run tests, create a file, generate code, execute a script. No special output guidance or research methodology is needed. Just write the phases and checklist.

**Multiple types are common.** A design review command is typically all three: subagent (runs as subtask), review (produces categorized findings), and research-heavy (validates APIs against live docs). Load all matching references and combine their guidance into the command template.

## Frontmatter options

| Field         | Required | Description                                                                 |
| ------------- | -------- | --------------------------------------------------------------------------- |
| `description` | Yes      | Shown in TUI command list                                                   |
| `agent`       | No       | Which agent handles the command (triggers subagent if it's a subagent type) |
| `model`       | No       | Override default model for this command                                     |
| `subtask`     | No       | Set `true` to force subagent invocation regardless of agent mode            |

## Prompt structure

Use markdown headings and lists to structure command templates. Organize prompts into clear sections:

- **Overview** — one or two sentences describing what the command does
- **Constraints** — bullet list of rules to follow
- **Context** — background info, injected shell output, or file references
- **Phases** — numbered steps
- **Checklist** — validation items

```markdown
---
description: Review recent changes
---

## Overview

Review the most recent git commits and suggest improvements to code quality, naming, and potential bugs.

## Constraints

- Focus on substantive issues, not stylistic nitpicks
- Flag security concerns immediately
- Do not suggest changes to generated or vendor files

## Context

Recent commits:
!`git log --oneline -10`

## Phases

1. Read the diff of each commit and identify the scope of changes
2. Check for bugs, edge cases, and security issues
3. Evaluate naming, structure, and code organization
4. Compile findings into a prioritized list

## Checklist

- [ ] All commits reviewed
- [ ] Security concerns flagged
- [ ] Suggestions are actionable and specific
- [ ] Output is organized by priority
```

## Template features

**Prose instructions** — write the command as prose that tells the agent what to do. The agent will figure out the details from context, conversation history, or by searching the project. This is the default and preferred approach for all commands.

```markdown
---
description: Create a new component
---

## Overview

Create a new React component with TypeScript support. The component name and requirements will be provided in the conversation.

## Phases

1. Determine the component type and props from the user's request
2. Create the component file with proper TypeScript types
3. Add basic structure and default exports
```

**Prose over arguments.** Arguments (`$ARGUMENTS`, `$1`, `$2`) are rarely used correctly and add friction. Write commands as prose instructions — the agent has access to the conversation context and will pick up what it needs. If the command needs specific inputs, phrase it as instructions: "the user will provide X" or "look for Y in the project."

**Shell output** — use `!`command`` to inject bash output into the prompt.

**File references** — use `@filepath` to include file contents in the prompt.

## Notes

- Custom commands override built-in commands if names match
- Use the markdown file approach for simplicity; JSON config for programmatic setups

## Advanced features

Reference files — see [Command types](#command-types) for when to load each:

- **Subagent output patterns**: [references/subagent-output.md](references/subagent-output.md)
- **Agent selection**: [references/agent-selection.md](references/agent-selection.md)
- **Research methodology**: [references/research-methodology.md](references/research-methodology.md)
- **Review and analysis commands**: [references/review-commands.md](references/review-commands.md)
