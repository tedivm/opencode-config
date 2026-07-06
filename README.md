# opencode Configuration

Personal opencode CLI configuration directory (`~/.config/opencode`).

## Setup

```bash
make install    # installs snip (output compression tool)
```

## Configuration

**opencode.json** — Core settings:

- **Provider:** vLLM (local model serving via OpenAI-compatible API)
- **Model:** `qwen3.6-27b` (200k context, 40k output)
- **MCP Server:** Context7 (documentation lookup, API key in `.context7-api-key`)
- **Plugin:** `@tarquinen/opencode-dcp` (conversation state management)
- **Features:** LSP enabled, formatter enabled

**AGENTS.md** — Agent behavior guidelines (personality, restrictions, tool usage conventions)

**dcp.jsonc** — Conversation persistence configuration

## Skills

Custom agent skills in `skills/`:

| Skill                    | Purpose                                                          |
| ------------------------ | ---------------------------------------------------------------- |
| `bootstrapping-plan`     | Design new projects via iterative exploration                    |
| `converting-to-markdown` | Convert files to Markdown via Microsoft's markitdown             |
| `create-command`         | Create/modify opencode custom commands                           |
| `create-python-project`  | Scaffold Python projects from cookiecutter template              |
| `create-skill`           | Generate new agent skills                                        |
| `customize-opencode`     | Edit opencode's own configuration files                          |
| `document-architecture`  | Create comprehensive architecture documents                      |
| `exploring-code`         | Deep codebase exploration via subagent                           |
| `gh-cli`                 | All GitHub CLI operations (PRs, issues, actions)                 |
| `github-actions`         | GitHub Actions workflow security and best practices              |
| `init-openspec`          | Initialize OpenSpec in a project                                 |
| `making-prs`             | Create PRs with quality checks and conventional commits          |
| `parsing-json`           | JSON parsing/transforming with `jq`                              |
| `playwright-cli`         | Browser automation and Playwright tests                          |
| `quality-checks`         | Iterative test/fix loops until clean                             |
| `rendering-mermaid`      | Render mermaid diagrams to PNG, SVG, or PDF                      |
| `robs-design`            | Rob's system design standard, used with openspec                 |
| `robs-theme`             | Rob's Style Guide design system (colors, typography, components) |

## Commands

Custom commands in `commands/`:

| Command                   | Purpose                                                       |
| ------------------------- | ------------------------------------------------------------- |
| `gha-upgrade`             | Update all GitHub Action versions to their latest releases    |
| `openspec-proposal-drift` | Review drift in an OpenSpec proposal against archived changes |
| `openspec-review`         | Review OpenSpec proposals and changes                         |
| `openspec-spec-drift`     | Review drift between OpenSpec specs and the codebase          |
| `repo-critique`           | Critique a repository for code quality and architecture       |
| `robs-design-review`      | Review a robs-design document for architectural soundness     |

## Environment Files

- `.llm_host` — vLLM server base URL
- `.openai_api_key` — API key for vLLM provider
- `.context7-api-key` — Context7 MCP API key
