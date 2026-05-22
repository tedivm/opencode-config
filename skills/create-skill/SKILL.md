---
name: create-skill
description: Use when asked to create, generate, or scaffold a new Agent Skill. Don't use for modifying existing skills or writing general documentation.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Determine the skill name

- Use gerund form when possible: `processing-pdfs`, `analyzing-data`, `testing-code`
- Name must match `^[a-z0-9]+(-[a-z0-9]+)*$` (1-64 chars, lowercase, hyphens as separators only, no leading/trailing/consecutive hyphens)
- Name must exactly match the parent directory name
- Avoid vague names (`helper`, `utils`, `tools`) and reserved words (`anthropic`, `claude`)

## Create the directory

Always place skills in `./.agents/skills/<name>/`:

```bash
mkdir -p ./.agents/skills/<name>/
```

## Write frontmatter

Required fields:

- `name` — must match directory name
- `description` — 1-1024 chars, written in **third person**, specific enough for correct activation

Optional fields:

- `license` — license name or reference to a bundled license file
- `compatibility` — 1-500 chars, environment requirements
- `metadata` — arbitrary string-to-string key-value map (use `author` for the author name)

### Source metadata

Always add a `source` field under `metadata` pointing to the repository URL. Resolve it dynamically — do not hardcode:

1. Run `git remote get-url origin` to get the remote URL
2. Convert `ssh` format (`git@github.com:user/repo.git`) to `https` (`https://github.com/user/repo`)
3. Strip `.git` suffix if present
4. Add `metadata:\n  source: <url>` to the frontmatter

### Author and license

Determine author and license dynamically:

1. Run `whoami` to check the current username
2. If the username is `tedivm`:
   - Set `license: MIT`
   - Set `metadata.author: Robert Hafner`
3. Otherwise, ask the user for their name and preferred license, then add them to the frontmatter

### Description best practices

- **Be concise.** Aim for a single sentence. Every token competes with conversation context.
- **Use imperative, action-oriented language:** "Use when extracting text from PDFs" not "Extracts text and tables from PDF files, fills forms, and merges documents."
- **Lead with the trigger context** ("Use when...") rather than a feature list
- **Include negative triggers** when helpful: "Don't use for Vue, Svelte, or vanilla CSS projects"
- **Include key terms** the user is likely to mention

**Good:** "Use when extracting text from PDFs, filling forms, or merging documents."
**Bad:** "Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."

## Write the SKILL.md body

### Core principles

- **Concise is key.** Assume the agent is already smart. Only add context it doesn't already have. Every token competes with conversation history.
- **Keep SKILL.md under 500 lines.** Offload details to `references/` files.
- **Write in third-person imperative:** "Extract the text..." not "I will extract..." or "You should extract..."
- **Use consistent terminology.** Pick one term per concept and use it throughout.
- **Use step-by-step numbering** for procedural instructions. Map out decision trees clearly.

### Set appropriate degrees of freedom

Match specificity to the task's fragility:

- **High freedom** (text instructions only): multiple valid approaches, context-dependent decisions
- **Medium freedom** (pseudocode or parameterized scripts): preferred pattern exists, some variation acceptable
- **Low freedom** (exact scripts, no parameters): fragile operations, consistency critical, specific sequence required

Don't offer too many options. Provide a default with an escape hatch:

```
Use pdfplumber for text extraction.
For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
```

### Recommended body structure

```
## Quick start
[Brief overview with the most common use case]

## Workflow
[Step-by-step numbered instructions]

## Advanced features
[Links to reference files for less common features]
```

### Progressive disclosure patterns

Use one of these patterns to organize content:

**Pattern 1: High-level guide with references**

```
## Quick start
[Core instructions inline]

## Advanced features
**Form filling**: See [FORMS.md](FORMS.md)
**API reference**: See [REFERENCE.md](REFERENCE.md)
```

**Pattern 2: Domain-specific organization**

```
## Available domains
**Finance**: Revenue, billing → See [reference/finance.md](reference/finance.md)
**Sales**: Pipeline, accounts → See [reference/sales.md](reference/sales.md)
```

**Pattern 3: Conditional workflow**

```
## Document modification
**Creating new content?** → Follow "Creation workflow" below
**Editing existing content?** → Follow "Editing workflow" below
```

### Workflow patterns

For complex multi-step tasks, provide a checklist the agent can track:

```
Copy this checklist and check off items as you complete them:

```

Task Progress:

- [ ] Step 1: Analyze the form (run analyze_form.py)
- [ ] Step 2: Create field mapping (edit fields.json)
- [ ] Step 3: Validate mapping (run validate_fields.py)
- [ ] Step 4: Fill the form (run fill_form.py)
- [ ] Step 5: Verify output (run verify_output.py)

```

```

### Feedback loops

For quality-critical tasks, implement validate-fix-repeat cycles:

```
1. Make your edits
2. Validate: python scripts/validate.py input/
3. If validation fails, fix and re-run
4. Only proceed when validation passes
5. Rebuild: python scripts/build.py input/ output/
```

### Examples pattern

For output-dependent skills, provide input/output pairs:

```
## Commit message format

**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication

Follow this style: type(scope): brief description.
```

### Template pattern

For strict output requirements, provide exact templates:

```
## Report structure
ALWAYS use this exact template:

# [Title]
## Executive summary
[One paragraph]
## Key findings
- Finding with data
```

For flexible guidance, provide a default and allow adaptation.

## Add supporting files

### Directory structure

```
skill-name/
├── SKILL.md              # Required: metadata + core instructions (<500 lines)
├── scripts/              # Executable code as tiny CLIs
├── references/           # Supplementary context (schemas, cheatsheets)
└── assets/               # Templates or static files
```

### References

- Keep files **one level deep** from SKILL.md. Never nest references within references.
- For reference files over 100 lines, include a table of contents at the top.
- Use forward slashes in all paths, regardless of OS: `reference/guide.md`
- Name files descriptively: `form_validation_rules.md`, not `doc2.md`

### Scripts

Many skills are wrappers around existing CLI tools (`gh`, `rsync`, `jq`, `git`, etc.). Before writing instructions, research the CLI thoroughly:

- Use Context7, web search, or other available tools to look up the CLI's documentation
- Run the CLI's own help commands (`<tool> --help`, `<tool> <subcommand> --help`) to discover available flags, subcommands, and usage patterns
- Verify current behavior — don't rely on memory or outdated knowledge
- Note platform-specific differences and document them

Don't bundle or reimplement these CLIs — assume they're available and provide installation instructions in a separate file.

- Put dependency installation instructions in `references/installation_guide.md`
- List each required tool and the command to install it (`brew install jq`, `pip install pdfplumber`, etc.)
- Prefer bash scripts for portability — they run everywhere without additional runtimes
- Keep bundled scripts tiny and single-purpose; larger scripts (Python, Node, etc.) are out of scope for this skill
- Handle edge cases gracefully with descriptive error messages — solve, don't punt to the agent
- Document all parameters and justify any constants (no magic numbers)
- Make execution intent clear: "Run `analyze_form.py`" (execute) vs "See `analyze_form.py`" (read as reference)

### Assets

- Templates, JSON schemas, diagrams, lookup tables
- Provide concrete templates instead of verbose descriptions of output format

### Don't create

- `README.md`, `CHANGELOG.md`, or other human-facing documentation
- Redundant instructions for tasks the agent already handles reliably
- Time-sensitive information (use an "Old patterns" collapsible section instead)

## Verify the skill

### Discovery validation

Test the description in isolation with an LLM:

1. Generate 3 prompts that should trigger the skill
2. Generate 3 similar prompts that should NOT trigger it
3. Critique the description for breadth — is it too vague or too narrow?

### Logic validation

Simulate execution: feed the full SKILL.md to an LLM and ask it to walk through a representative task step by step, flagging any ambiguities or missing steps.

### Edge case testing

Ask an LLM to attack the skill's logic: what happens on failure, unsupported configurations, missing dependencies?

### Final checklist

- [ ] `SKILL.md` is spelled in all caps
- [ ] Frontmatter has `name` and `description`
- [ ] `name` matches directory name
- [ ] `metadata.source` contains the resolved repository HTTPS URL
- [ ] `license` is set (MIT for `tedivm`)
- [ ] `metadata.author` is set (Robert Hafner for `tedivm`)
- [ ] Description is third-person, specific, includes trigger keywords
- [ ] SKILL.md body is under 500 lines
- [ ] File references are one level deep with forward slashes
- [ ] Consistent terminology throughout
- [ ] No time-sensitive information
- [ ] No duplicate skill names across all locations
- [ ] No Windows-style paths
