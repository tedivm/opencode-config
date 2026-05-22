---
name: searching-files
description: Use when searching for or replacing text, patterns, or content across files in a codebase. Use `rg` (ripgrep) for all file content searches and replacements. Don't use for finding files by name or path patterns (use `glob` instead).
compatibility: Requires ripgrep 14+. Install: brew install ripgrep (macOS), apt install ripgrep (Linux), cargo install ripgrep (any).
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Use `rg` for all recursive file content searches. It respects `.gitignore`, skips hidden files and binaries by default.

```
rg "pattern"
rg "pattern" src/
rg -t json "pattern"
```

## Common patterns

**Search for text:**

```
rg "functionName"
```

**Search with context (N lines before/after):**

```
rg -C3 "pattern"
```

**Search specific file types:**

```
rg -t ts "pattern"
rg -t py -t js "pattern"
```

**Search by file glob:**

```
rg "pattern" -g "*.config.*"
```

**Case-insensitive search:**

```
rg -i "pattern"
```

**Whole-word match:**

```
rg -w "pattern"
```

**List files containing match (no content):**

```
rg -l "pattern"
```

**Count matches per file:**

```
rg -c "pattern"
```

**Search binary files:**

```
rg -a "pattern"
```

**Search hidden files:**

```
rg "pattern" --hidden
```

**Ignore `.gitignore` rules:**

```
rg "pattern" --no-ignore
```

**Multiple patterns (OR):**

```
rg -e "foo" -e "bar"
```

**PCRE2 regex (lookahead, backreferences):**

```
rg --pcre2 "(?<=prefix)pattern"
```

## Replacing text

`rg -r` previews replacements without modifying files. Use it to verify changes before applying.

**Preview a simple replacement:**

```
rg "oldFunction" -r "newFunction"
```

**Preview replacement limited to file types:**

```
rg "oldFunction" -r "newFunction" -t ts -t tsx
```

**Preview replacement with whole-word match:**

```
rg -w "config" -r "settings"
```

**Preview replacement with regex capture groups:**

```
rg "(foo)(bar)" -r "$2$1"
```

**Preview replacement with named capture groups:**

```
rg "(?<key>\w+)=(?<value>\w+)" -r "$value=$key"
```

**Preview replacement in specific files by glob:**

```
rg "deprecated" -r "removed" -g "*.js"
```

**Preview replacement with context:**

```
rg "old" -r "new" -C2
```

**Pipe to a file to review all changes:**

```
rg "old" -r "new" > changes.txt
```

**To actually apply replacements, use `sed`, a text editor, or an IDE refactoring tool — `rg` only previews.**

## Workflow

1. Start broad: `rg "keyword"` to find occurrences
2. Narrow with file type: `rg -t ts "keyword"` or glob: `rg "keyword" -g "*.ts"`
3. Add context if needed: `rg -C2 "keyword"`
4. For just file paths: `rg -l "keyword"`

## Advanced features

**Fixing false negatives (file was skipped):**
Run `rg "pattern" --debug` to see why files were skipped.

**Search in non-git directories:**
Use `--no-require-git` to respect `.gitignore` outside of git repos.

**Output formatting:**

- `--json` for machine-readable output
- `--vimgrep` for editor integrations
- `--heading` for grouped output by file
- `--with-filename` to always show filenames

**Replacement preview (does not modify files):**

```
rg "old" -r "new"
```

**File listing (what would be searched):**

```
rg --files
```

## References

**Installation**: See [references/installation_guide.md](references/installation_guide.md)
**File types**: Run `rg --type-list` to see all built-in types
**Regex**: Uses Rust regex by default; add `--pcre2` for lookaround/backreferences
