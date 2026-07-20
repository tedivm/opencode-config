# Permission strategy

Load this when the user explicitly requests restricted permissions for an agent. Default is permissive — inherit the general agent's permissions unless told otherwise.

## Permission keys

Each key accepts `allow`, `ask`, or `deny`.

| Key                  | Tools it gates                    |
| -------------------- | --------------------------------- |
| `read`               | `read`                            |
| `edit`               | `write`, `edit`, `apply_patch`    |
| `bash`               | `bash`                            |
| `task`               | `task` (subagent invocation)      |
| `external_directory` | File ops outside project worktree |
| `webfetch`           | `webfetch`                        |
| `websearch`          | `websearch`                       |
| `skill`              | `skill`                           |
| `question`           | `question`                        |

`read`, `edit`, `glob`, `grep`, `list`, `bash`, `task`, `external_directory`, `lsp`, and `skill` support fine-grained glob patterns.

## Fine-grained patterns

```yaml
permission:
  bash:
    "*": ask
    "git status *": allow
    "grep *": allow
```

Last matching rule wins — put wildcards first, specifics after.

## Common permission profiles

- **Read-only agent**: `edit: deny`, `bash: deny`
- **Review agent**: `edit: deny`, `bash: { "git diff": allow, "git log*": allow }`
- **Full dev agent**: `edit: allow`, `bash: allow`
- **Research agent**: `edit: deny`, `bash: deny`, `webfetch: allow`, `websearch: allow`

## Task permissions

Control which subagents a primary agent can invoke:

```yaml
permission:
  task:
    "*": deny
    "orchestrator-*": allow
    "code-reviewer": ask
```

When set to `deny`, the subagent is removed from the Task tool description entirely.
