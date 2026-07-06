# Subagent Output Patterns

Load this when creating commands that run as subagents (`subtask: true` or with an `agent` field). Subagent commands have different output requirements than inline commands — the final message is the only thing the parent agent receives.

## Why subagent output needs guidance

A subagent does extensive work — research, exploration, evaluation — but the parent agent only sees the final message. Without explicit output guidance, subagents tend to:

- Include their working process and discarded alternatives (noise)
- Omit recommendations and source URLs (parent can't act)
- Write narrative prose instead of structured findings (hard to parse)

## Subagent Output section

Add a `## Guidance` section with a `### Subagent Output` subsection:

```markdown
## Guidance

### Subagent Output

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

## User Request section

Every subagent command must include a `## User Request` section that uses `$ARGUMENTS` to accept user input. This is the only way to pass additional context into the subagent. Without it, the subagent cannot receive user-specific guidance.

````markdown
## User Request

Describe what the user might provide here — additional requirements, specific targets, scope constraints.

```markdown
$ARGUMENTS
```
````

If there is nothing in the quote block above then there are no special requests.

`````

Customize the introductory prose to match your command's domain. The ````markdown` fence around `$ARGUMENTS` presents the user's input as a clearly delimited block the agent can parse.

## Customizing for your command

Adapt the "what the primary agent needs" list to match your command's output:

- **Review commands:** findings with category, impact, recommendation, sources
- **Research commands:** summarized findings with source URLs for deeper investigation
- **Planning commands:** ordered steps with dependencies, risks, and decision points
- **Analysis commands:** structured data, patterns found, anomalies flagged
`````
