# Research Methodology

Load this when creating commands that require external verification — fetching library documentation, validating APIs, checking package existence, or any task where the agent's memory is unreliable.

## Why research methodology matters

Agents trained on stale data will confidently produce wrong answers about current APIs, package names, documentation URLs, and best practices. Commands that depend on accuracy need explicit instructions to search first, not guess.

## Research section

Add a `## Guidance` section with a `### Research` subsection:

```markdown
## Guidance

### Research

**Your memory is unreliable. Always search first.**

You will need to do extensive research during this task — fetching library documentation, verifying APIs, searching for alternative approaches, checking package registries, validating URLs. Do not rely on what you "remember" about any library, API, or tool. Your training data is stale and often wrong.

**Use your web search and web fetch tools aggressively:**

- Before making any claim about how a library works, fetch its current documentation.
- Before saying a model or package exists, search for it and verify.
- Before evaluating whether an approach is best practice, search for how the community actually does it.
- When you encounter an API name, class, or function you haven't seen recently, fetch the docs — don't guess.
- If a search or fetch fails, try different queries or URLs. Do not fall back on memory.

**The rule of zero retries from memory:** if your first attempt to verify something fails, search again with a different query. Do not guess what the answer might be.

Every phase below requires live research. Treat this like a code audit where you have a browser open — you wouldn't claim to know an API from memory, so don't do it here.
```

## When to use vs. skip

**Use this when:**
- The command validates APIs, libraries, models, or packages against live documentation
- The command researches alternatives or best practices
- Accuracy matters more than speed

**Skip this when:**
- The command works entirely within the project's own codebase
- The command is creative or generative (writing code, designing features)
- The command's output doesn't depend on external facts
