---
name: rendering-mermaid
description: Use when rendering mermaid diagrams to PNG, SVG, or PDF images. Handles both .mmd files and inline mermaid code blocks in markdown files. Don't use for creating mermaid syntax or GraphViz/DOT diagrams.
license: MIT
compatibility: Requires Node.js and npx. SVG pretty-printing requires xmllint (libxml2).
metadata:
  source: https://github.com/tedivm/opencode-config
  author: Robert Hafner
---

## Quick start

Render a `.mmd` file to PNG, SVG, or PDF using `@mermaid-js/mermaid-cli`. The bundled config and CSS files ensure consistent styling and remove known bugs across outputs.

## Prerequisites

- **Node.js / npx** — required for `@mermaid-js/mermaid-cli`
- **xmllint** — required for SVG pretty-printing (`brew install libxml2` on macOS)
- **Puppeteer dependencies** — `@mermaid-js/mermaid-cli` uses Puppeteer under the hood. On macOS, install Chromium: `npx puppeteer browsers install chrome`

## Width Guidelines

Default widths by diagram complexity:

| Diagram Type           | Width     | Example                        |
| ---------------------- | --------- | ------------------------------ |
| Simple (1-3 nodes)     | `-w 1200` | Small flowchart                |
| Medium (4-10 nodes)    | `-w 2000` | Standard sequence diagram      |
| Large (11-20 nodes)    | `-w 3000` | Full ERD, complex architecture |
| Very large (20+ nodes) | `-w 4000` | Complete database schema       |

Adjust based on readability — text should be clearly legible without zooming.

## Assets

Use the bundled files in `assets/`:

- `assets/config.json` — mermaid configuration (neutral theme, arial font, deterministic IDs)
- `assets/png.css` — CSS override for proper SVG sizing in PNG output

## Workflow

### Single file render

1. **Determine the skill's base path** — resolve the absolute path to this skill directory
2. **Set the asset paths** relative to the skill base:
   - Config: `<skill_base>/assets/config.json`
   - CSS: `<skill_base>/assets/png.css`
3. **Render using npx** — no local install needed:

```bash
# PNG (adjust -w based on diagram complexity — see Width Guidelines)
npx -p @mermaid-js/mermaid-cli mmdc \
  -w 2000 -b transparent \
  --cssFile <skill_base>/assets/png.css \
  --configFile <skill_base>/assets/config.json \
  -e png -i input.mmd -o output.mmd.png

# SVG (with pretty-print)
TMP=$(mktemp -d)
npx -p @mermaid-js/mermaid-cli mmdc \
  -w 2000 -b transparent \
  --cssFile <skill_base>/assets/png.css \
  --configFile <skill_base>/assets/config.json \
  -e svg -i input.mmd -o $TMP/diagram.svg
xmllint --format $TMP/diagram.svg > output.mmd.svg
rm -rf $TMP

# PDF
npx -p @mermaid-js/mermaid-cli mmdc \
  -w 2000 -b transparent \
  --cssFile <skill_base>/assets/png.css \
  --configFile <skill_base>/assets/config.json \
  -e pdf -i input.mmd -o output.mmd.pdf
```

### Batch render (multiple files)

For rendering many `.mmd` files in a project, set up the same options as variables and loop. Use dynamic width based on line count:

```bash
MMD_BASE="-b transparent --cssFile <skill_base>/assets/png.css --configFile <skill_base>/assets/config.json"

for f in $(find . -name "*.mmd" -not -path "*/build/*"); do
  # Auto-select width based on diagram size (line count as proxy for complexity)
  LINES=$(wc -l < "$f")
  if [ "$LINES" -gt 300 ]; then
    WIDTH=4000
  elif [ "$LINES" -gt 150 ]; then
    WIDTH=3000
  elif [ "$LINES" -gt 50 ]; then
    WIDTH=2000
  else
    WIDTH=1200
  fi
  npx -p @mermaid-js/mermaid-cli mmdc -w $WIDTH $MMD_BASE -e png -i "$f" -o "${f}.png"
done
```

### Rendering from inline mermaid in markdown

When a mermaid diagram is embedded in a markdown file (e.g., README.md) inside a ` ```mermaid ... ``` ` code block:

1. **Extract the diagram content** — copy everything in the mermaid code block
2. **Write to a temp file:**
   ```bash
   TMP_MMD=$(mktemp /tmp/diagram_XXXXXX.mmd)
   ```
3. **Paste the extracted mermaid content into `$TMP_MMD`**
4. **Auto-select width based on diagram complexity:**
   ```bash
   LINES=$(wc -l < $TMP_MMD)
   if [ "$LINES" -gt 300 ]; then WIDTH=4000
   elif [ "$LINES" -gt 150 ]; then WIDTH=3000
   elif [ "$LINES" -gt 50 ]; then WIDTH=2000
   else WIDTH=1200; fi
   ```
5. **Render from the temp file:**
   ```bash
   npx -p @mermaid-js/mermaid-cli mmdc \
     -w $WIDTH -b transparent \
     --cssFile <skill_base>/assets/png.css \
     --configFile <skill_base>/assets/config.json \
     -e png -i $TMP_MMD -o output.png
   ```
6. **Clean up:**
   ```bash
   rm $TMP_MMD
   ```

If the markdown file contains multiple mermaid diagrams, give each a descriptive temp filename and output name (e.g., `architecture.mmd` → `architecture.png`, `user_flow.mmd` → `user_flow.png`).

### Output naming convention

Append the format extension to the original filename:

- `diagram.mmd` → `diagram.mmd.png`, `diagram.mmd.svg`, `diagram.mmd.pdf`

## Configuration

The default `assets/config.json` uses:

- `theme: "neutral"` — works well on both light and dark backgrounds
- `fontFamily: "arial"` — consistent cross-platform rendering
- `deterministicIds: true` — stable SVG element IDs across renders

To change the theme, edit `assets/config.json` or override with `-t <theme>` on the command line (options: `default`, `dark`, `forest`, `neutral`).

## Width Guidance

Use line count as a proxy for diagram complexity to auto-select width:

| Lines   | Complexity                               | Width |
| ------- | ---------------------------------------- | ----- |
| < 50    | Simple (flowchart, sequence)             | 1200  |
| 50–150  | Medium (class diagram, state machine)    | 2000  |
| 150–300 | Large (ERD, architecture)                | 3000  |
| > 300   | Very large (full schema, complex system) | 4000+ |

For very large diagrams (10+ tables/nodes), start at 4000px and increase if text is unreadable.

## Troubleshooting

- **Puppeteer/Chromium errors** — run `npx puppeteer browsers install chrome` to install the browser dependency
- **xmllint not found** — install with `brew install libxml2` (macOS) or `apt install libxml2-utils` (Linux)
- **Diagram too small** — see Width Guidance table; increase `-w` value (e.g., `-w 4000` for large schemas)
- **Font rendering differs** — ensure the target font is installed on the system running the render
