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
2. **Ask about execution context** — ask the user if the command should run as a subtask or with a specific agent. Only include `subtask` or `agent` in the frontmatter if they confirm.
3. **Create the file** — name it `<command-name>.md` (lowercase, hyphens allowed)
4. **Write frontmatter** — set `description` (required). Only add `agent`, `model`, or `subtask` if the user specifically requested them.
5. **Write the template** — the body content becomes the prompt sent to the LLM
6. **Test** — run `/command-name` in the TUI

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

```
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

**Arguments** — use `$ARGUMENTS` for all args, or `$1`, `$2`, `$3` for positional:

```
---
description: Create a new component
---
## Overview

Create a new React component named $ARGUMENTS with TypeScript support.

## Phases

1. Determine the component type and props based on $ARGUMENTS
2. Create the component file with proper TypeScript types
3. Add basic structure and default exports
```

Run: `/component Button`

```
---
description: Create a new file with content
---
## Overview

Create a file named $1 in the directory $2 with the following content: $3

## Phases

1. Verify the directory $2 exists
2. Create the file $1 inside $2
3. Populate it with the provided content
```

Run: `/create-file config.json src "{ \"key\": \"value\" }"`

**Shell output** — use `!`command`` to inject bash output into the prompt.

**File references** — use `@filepath` to include file contents in the prompt.

## Notes

- Custom commands override built-in commands if names match
- Use the markdown file approach for simplicity; JSON config for programmatic setups
