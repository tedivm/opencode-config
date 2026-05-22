# opencode Configuration

Personal opencode CLI configuration directory (`~/.config/opencode`).

## Setup

```bash
make install    # installs snip (output compression tool)
npm install     # installs @opencode-ai/plugin dependency
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

| Skill                   | Purpose                                             |
| ----------------------- | --------------------------------------------------- |
| `bootstrapping-plan`    | Design new projects via iterative exploration       |
| `create-command`        | Create/modify opencode custom commands              |
| `create-python-project` | Scaffold Python projects from cookiecutter template |
| `create-skill`          | Generate new agent skills                           |
| `customize-opencode`    | Edit opencode's own configuration files             |
| `exploring-code`        | Deep codebase exploration via subagent              |
| `gh-cli`                | All GitHub CLI operations (PRs, issues, actions)    |
| `init-openspec`         | Initialize OpenSpec in a project                    |
| `parsing-json`          | JSON parsing/transforming with `jq`                 |
| `quality-checks`        | Iterative test/fix loops until clean                |
| `robs-design`           | Rob's system design standard, used with openspec    |
| `robs-theme`            | Rob's color and font preferences                    |
| `searching-files`       | File content search with `rg` (ripgrep)             |

## Environment Files

- `.llm_host` — vLLM server base URL
- `.openai_api_key` — API key for vLLM provider
- `.context7-api-key` — Context7 MCP API key
