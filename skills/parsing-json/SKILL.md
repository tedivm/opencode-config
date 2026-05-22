---
name: parsing-json
description: "Use when parsing, querying, transforming, or extracting data from JSON files, API responses, or JSON streams. Always use the `jq` CLI for all JSON operations. Do not use for YAML, XML, CSV, or plain-text parsing. Don't use for building JSON from scratch in Python, Node, or other languages when `jq` can handle it."
compatibility: Requires `jq` 1.6+ installed
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

All JSON processing must use `jq`. Never write custom scripts in Python, Node,
Ruby, `sed`, `awk`, or `grep` for JSON manipulation. `jq` handles every common
pattern cleanly.

```bash
# Pretty-print / validate
jq . file.json

# Extract a field
jq -r '.users[0].name' file.json

# Filter array elements
jq '.items[] | select(.active)' file.json

# Extract to CSV
jq -r '[.id, .name, .email] | @csv' file.json
```

Pipe data from `curl` or other commands directly into `jq`:

```bash
# Fetch and parse API response
curl -s 'https://api.example.com/users' | jq '.[] | {name, email}'

# Extract a single value
curl -s 'https://api.example.com/status' | jq -r '.version'

# Filter and count
curl -s 'https://api.example.com/items' | jq '[.[] | select(.active)] | length'

# Build shell commands from JSON
curl -s 'https://api.example.com/files' | jq -r '.[] | "wget \(.url)"'

# Chain with other tools
curl -s 'https://api.example.com/data' | jq -c '.[]' | while read -r line; do
  echo "$line"
done
```

## Golden rules

1. **Always use `jq`.** If the task involves reading, querying, transforming,
   or writing JSON, use `jq`. No exceptions for Python, Node, `sed`, `awk`,
   or custom scripts.

2. **Quote jq filters with single quotes.** Prevents shell interpolation
   conflicts: `jq '.field'` not `jq .field`.

3. **Use `-r` (raw output) for plain text.** Without `-r`, strings are
   quoted in output. Use `-r` when piping to other commands, writing to
   files, or generating non-JSON output.

4. **Use `-c` (compact) for machine-readable output.** Piping JSON to
   another `jq` call or another JSON consumer? Use `-c`.

5. **Use `--arg` for injecting shell variables.** Never use string
   interpolation to inject values into jq filters.

   ```bash
   # Correct
   jq --arg id "$ID" 'select(.id == $id)' file.json

   # Wrong — breaks on special characters, injection-prone
   jq "select(.id == \"$ID\")" file.json
   ```

6. **Use `--argjson` for passing JSON values.** When the variable is
   already valid JSON (numbers, booleans, arrays, objects).

   ```bash
   jq --argjson config "$CONFIG_JSON" '. + $config' file.json
   ```

## Advanced patterns

### Shell variable injection (never interpolate)

```bash
# Pass strings safely
jq --arg id "$ID" --arg env "$ENV" 'select(.id == $id and .env == $env)' file.json

# Pass JSON values (numbers, booleans, arrays, objects)
jq --argjson limit "$LIMIT" --argjson flags "$FLAGS_JSON" '.items[:$limit] | map(. + $flags)' file.json

# Read external JSON file as variable
jq --slurpfile config config.json '. + $config[0]' file.json

# Read raw text file as variable
jq --rawfile readme README.md '.docs = $readme' file.json
```

### Aggregations and reductions

```bash
# Group and count
jq 'group_by(.status) | map({status: .[0].status, count: length})' file.json

# Group and aggregate
jq 'group_by(.category) | map({category: .[0].category, total: (map(.price) | add)})' file.json

# Conditional reduce — accumulate state across elements
jq 'reduce .[] as $item (0; if $item.active then . + 1 else . end)' file.json
```

### Object/array transformations

```bash
# Deep merge (preserves nested keys from right operand)
jq -s '.[0] * .[1]' base.json overrides.json

# Rename keys across objects
jq '[.[] | .newKey = .oldKey | del(.oldKey)]' file.json

# Pivot rows to object keyed by field
jq 'reduce .[] as $item ({}; .[$item.id] = $item)' file.json

# Flatten nested arrays
jq '[.[][]]' file.json

# Deduplicate by key
jq 'unique_by(.id)' file.json
```

### String extraction and generation

```bash
# Extract values as shell-compatible commands
jq -r '.[] | "curl -s \(.url)"' file.json

# Regex capture groups to object
jq -r '.[] | .path | capture("(?<dir>/[^/]+)/(?<file>[^/]+)")' file.json

# Format as CSV/TSV with header
jq -r '"id,name,email"; (.[] | [.id, .name, .email] | @csv)' file.json

# Base64 encode/decode
jq -r '.data | @base64' file.json
echo "data" | jq -Rr '@base64d'
```

### Streaming large files

```bash
# Process incrementally without loading entire file into memory
jq --stream 'select(.[0] == "items" and .[1] | test("^item"))' large.json

# Process ndjson (one JSON object per line) — naturally streaming
jq -c 'select(.active)' file.ndjson
```

### Error handling and robustness

```bash
# Graceful fallback on missing keys
jq -r '.user.name // "unknown"' file.json

# Suppress errors on invalid paths
jq -r 'try .data.results[].id catch empty' file.json

# Validate and exit on failure
jq -e '.' file.json || echo "Invalid JSON"
```

### Multi-file workflows

```bash
# Slurp multiple files into array
jq -s '.' file1.json file2.json

# Glob and aggregate
jq -s '[.[][] | select(.active)] | length' data/*.json

# Merge with reduce
jq -s 'reduce .[] as $item ({}; . * $item)' templates/*.json
```

## Advanced features

**Installing jq**: See [references/installation.md](references/installation.md)
