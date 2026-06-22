# Choosing a Subagent

Load this when creating a command that uses an `agent` field. The built-in subagents have different capabilities — picking the right one matters for what the command can do.

## Built-in subagents

### `explore`

Fast, read-only agent for exploring codebases. Cannot modify files.

**Use it when:** the command reads, searches, or analyzes existing code — finding files by pattern, searching for keywords, answering questions about the codebase.

**Typical commands:** code reviews, architecture analysis, dependency mapping, finding usages.

### `general`

General-purpose agent with full tool access (except todo). Can make file changes, run commands, and execute multi-step tasks.

**Use it when:** the command needs to do heavy multi-step work that may involve writing files, running commands, or combining research with action. Also the best choice for commands that need both local code exploration and external research.

**Typical commands:** complex refactoring tasks, multi-file updates, design reviews that verify third-party APIs, dependency audits, best practice research.

### `scout` — removed

This agent no longer exists in OpenCode. Do not use it. If you see older examples or configs referencing `scout`, replace them with `explore`.

## How to set it up

Add the `agent` field to your command's frontmatter:

```markdown
---
description: Review a design document for API accuracy
agent: general
subtask: true
---
```

## Picking between explore and general

- **`explore`** — read-only, cannot modify files. Can fetch external docs, run commands, and use tools. Great for research-heavy work: design reviews, API validation, best practice research, anything that reads and analyzes but shouldn't write.
- **`general`** — full tool access, can modify files. Use when the command needs to write, edit, or create files as part of its work.

The dividing line is write access. If the command should only read and report, use `explore`. If it needs to make changes, use `general`.

## When not to specify an agent

If the command is a simple action (run tests, create a file, generate code) and doesn't benefit from a specialized agent, omit the `agent` field entirely. The primary agent will handle it directly or invoke a subagent as needed.
