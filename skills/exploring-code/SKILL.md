---
name: exploring-code
description: Use when doing a thorough exploration of an existing codebase. Guides a subagent through reading documentation, reviewing tests, analyzing architecture, and producing a comprehensive overview. Don't use for quick lookups or single-file questions.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Launch a subagent to explore the target codebase. The subagent follows a structured workflow: documentation first, then tests, then source code. It returns a dense overview covering architecture, key modules, patterns, and potential concerns.

## Workflow

1. **Identify the target** — Confirm the root directory and scope with the user. If exploring the current workspace, use its root.

2. **Launch the subagent** — Use the `task` tool with `subagent_type: explore` and a prompt that includes the full exploration checklist below. Set `description` to something like "Explore codebase structure and architecture."

3. **The subagent executes this checklist:**

```
## Exploration Checklist

### Phase 1: Documentation and Entry Points
- [ ] Read README.md (or primary README) for project overview, setup instructions, and high-level architecture
- [ ] Read any additional documentation: CONTRIBUTING.md, ARCHITECTURE.md, docs/, guides/, etc.
- [ ] Check package.json / Cargo.toml / go.mod / pyproject.toml / Cargo.lock for dependencies and their roles
- [ ] Identify the project language, framework, and build system

### Phase 2: Project Structure
- [ ] Map the top-level directory structure
- [ ] Identify key directories: src/, lib/, core/, api/, components/, tests/, scripts/, config/
- [ ] Note the file organization pattern (by feature, by layer, by type)
- [ ] Identify entry points: main files, CLI entry points, server startup files, index files

### Phase 3: Tests
- [ ] Find test directories and test file patterns
- [ ] Read test structure to understand what is tested and testing conventions
- [ ] Note test frameworks used and any test utilities or fixtures
- [ ] Identify gaps: areas with no test coverage

### Phase 4: Source Code Deep Dive
- [ ] Read entry points and bootstrap code
- [ ] Trace the main execution flow from entry point through key modules
- [ ] Identify core abstractions, interfaces, and data models
- [ ] Map dependencies between modules (what imports what)
- [ ] Note architectural patterns used (MVC, layered, event-driven, microservices, etc.)
- [ ] Identify configuration systems and how settings are loaded
- [ ] Note error handling patterns and logging approaches

### Phase 5: Integration Points
- [ ] Identify external dependencies: APIs, databases, message queues, file systems
- [ ] Find configuration files: .env examples, config files, deployment configs
- [ ] Check for CI/CD pipelines: GitHub Actions, Makefiles, build scripts
- [ ] Note deployment patterns and infrastructure requirements

### Phase 6: Synthesis
- [ ] Produce a comprehensive overview as a direct message back to the primary agent (do NOT save any document to disk):
  - Project purpose and what it does
  - High-level architecture diagram (text-based)
  - Key modules and their responsibilities
  - Data flow and execution paths
  - Technology stack and notable dependencies
  - Testing strategy and coverage notes
  - Code organization patterns and conventions
  - Potential concerns, technical debt, or areas needing attention
```

4. **Receive and relay the report** — The subagent returns a comprehensive overview as its final output message. Present it directly to the user. Offer to dive deeper into any specific area.

## Prompt template for subagent

Use this as the prompt when launching the explore subagent:

```
Thoroughly explore the codebase at [WORKSPACE_ROOT]. Follow this structured approach:

1. START with documentation: README, CONTRIBUTING, any docs/ directory, package config files
2. MAP the directory structure: identify key directories, entry points, organization patterns
3. REVIEW tests: find test files, understand testing approach, note coverage gaps
4. DEEP DIVE into source: trace execution flow, identify core abstractions, map module dependencies, note architectural patterns
5. IDENTIFY integration points: external APIs, databases, config systems, CI/CD
6. SYNTHESIZE everything into a comprehensive overview

Return a dense, well-structured report as your final output message — do NOT save any document to disk. Cover: project purpose, architecture, key modules, data flow, tech stack, testing, conventions, and any concerns or technical debt. Be specific — name files, functions, and patterns you find.
```

## Tips

- Set an appropriate timeout for the subagent (codes can be large). Use the `timeout` parameter on the task tool if needed.
- If the codebase is very large, scope the exploration: ask the user which areas matter most, or have the subagent focus on specific directories.
- For monorepos, have the subagent explore each package separately and synthesize the results.
- If the subagent hits token limits on a massive codebase, break the exploration into phases across multiple subagent invocations.
