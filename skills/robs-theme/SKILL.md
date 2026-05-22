---
name: robs-theme
description: "Use when working on *.tdvm.net and *.tedivm.com services, or when asked to apply `rob's` or `my` style. Applies Rob's personal design system: dark purple palette with pink/cyan/purple accents, specific typography hierarchy, and component patterns (cards, badges, alerts, buttons). Don't use for generic styling or other projects."
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Apply the design system from `https://tedivm.github.io/robs-style-guide/` to any of Rob's services. Use the color tokens, typography rules, and component patterns below consistently.

## Color tokens

| Token      | Hex       | Usage                         |
| ---------- | --------- | ----------------------------- |
| Background | `#1a1025` | Page background               |
| Surface    | `#2d1b4e` | Cards, elevated surfaces      |
| Input      | `#0f0a1a` | Code blocks, form inputs      |
| Border     | `#3d2b5a` | Dividers, borders             |
| Primary    | `#ff71ce` | Pink accent, headings, alerts |
| Secondary  | `#01cdfe` | Cyan accent, links, code text |
| Tertiary   | `#b96dff` | Purple accent, headings       |
| Body text  | `#dcdcdc` | Paragraphs, labels            |
| Muted      | `#b4b4b4` | Secondary text                |
| Dim        | `#999`    | Tertiary text                 |
| Success    | `#50c878` | Positive feedback             |
| Warning    | `#ffbe32` | Cautionary messages           |
| Error      | `#ff5050` | Errors, critical issues       |

## Typography

- **Body font:** `Source Serif 4` (primary) / `Roboto Slab` (fallback). Both weights 400 and 700.
- **Monospace:** `Source Code Pro` (primary) / `Roboto Mono` (fallback). Both weights 400 and 700.
- **Line height:** `1.6` on body, `1.5` on code blocks
- **Max width:** `900px`, centered with `margin: 0 auto`

### Heading hierarchy

| Level | Size      | Color     | Extra styling                                                |
| ----- | --------- | --------- | ------------------------------------------------------------ |
| H1    | `1.8rem`  | `#ff71ce` | `text-shadow: 0 0 20px rgba(255,113,206,0.4)`                |
| H2    | `1.3rem`  | `#01cdfe` | `border-bottom: 1px solid #3d2b5a`, `padding-bottom: 0.4rem` |
| H3    | `1.1rem`  | `#b96dff` | —                                                            |
| H4    | `1rem`    | `#dcdcdc` | —                                                            |
| H5    | `0.9rem`  | `#b96dff` | `text-transform: uppercase`, `letter-spacing: 0.05em`        |
| H6    | `0.85rem` | `#888`    | `text-transform: uppercase`, `letter-spacing: 0.05em`        |

### Text color utilities

| Class           | Color     |
| --------------- | --------- |
| `.text-pink`    | `#ff71ce` |
| `.text-cyan`    | `#01cdfe` |
| `.text-purple`  | `#b96dff` |
| `.text-success` | `#50c878` |
| `.text-warn`    | `#ffbe32` |
| `.text-error`   | `#ff5050` |

### Text utility classes

| Class        | Effect                                                           |
| ------------ | ---------------------------------------------------------------- |
| `.muted`     | `color: #b4b4b4`                                                 |
| `.dim`       | `color: #999`                                                    |
| `.text-sm`   | `font-size: 0.85rem`                                             |
| `.text-xs`   | `font-size: 0.75rem`                                             |
| `.font-bold` | `font-weight: 700`                                               |
| `.font-mono` | `font-family: 'Source Code Pro', 'Roboto Mono', monospace`       |
| `.uppercase` | `text-transform: uppercase`, `letter-spacing: 0.05em`            |
| `.truncate`  | `overflow: hidden; text-overflow: ellipsis; white-space: nowrap` |

## Inline elements

### Links

- Color: `#01cdfe`, no underline
- Hover: `text-decoration: underline`

### Inline code

- `font-family: 'Source Code Pro', 'Roboto Mono', monospace`
- `background: #2d1b4e`, `color: #01cdfe`
- `padding: 2px 6px`, `border-radius: 3px`, `font-size: 0.9em`

### URL-style code (`.url`)

- `font-family: monospace`, `background: #2d1b4e`, `color: #01cdfe`
- `padding: 0.2rem 0.5rem`, `border-radius: 3px`

### Keyboard shortcuts (`.kbd`)

- `background: #2d1b4e`, `border: 1px solid #3d2b5a`, `border-radius: 3px`
- `padding: 0.1rem 0.4rem`, `font-family: monospace`, `font-size: 0.75rem`, `color: #dcdcdc`

### Tooltips (`.tooltip`)

- `border-bottom: 1px dotted #01cdfe`, `cursor: help`
- Uses `data-tip` attribute for content
- On `:hover::after`: `background: #0f0a1a`, `color: #dcdcdc`, `padding: 0.4rem 0.6rem`, `border-radius: 3px`, `font-size: 0.75rem`, `border: 1px solid #2d1b4e`, positioned above with `left: 50%; transform: translateX(-50%)`

## Code blocks

- `background: #0f0a1a`, `color: #e0e0e0`
- `padding: 1rem`, `border-radius: 5px`, `border: 1px solid #2d1b4e`
- `font-size: 0.85rem`, `line-height: 1.5`, `overflow-x: auto`
- Inner `code` resets: `background: none`, `padding: 0`, `color: inherit`

## Badges

- Base: `display: inline-block`, `padding: 2px 8px`, `border-radius: 12px`, `font-size: 0.75em`, `font-weight: 600`
- Semi-transparent backgrounds with matching text color:

| Class            | Background               | Color     |
| ---------------- | ------------------------ | --------- |
| `.badge-app`     | `rgba(255,113,206,0.15)` | `#ff71ce` |
| `.badge-ai`      | `rgba(1,205,254,0.15)`   | `#01cdfe` |
| `.badge-infra`   | `rgba(185,109,255,0.15)` | `#b96dff` |
| `.badge-success` | `rgba(80,200,120,0.15)`  | `#50c878` |
| `.badge-warn`    | `rgba(255,190,50,0.15)`  | `#ffbe32` |
| `.badge-error`   | `rgba(255,80,80,0.15)`   | `#ff5050` |

## Tags (`.tag`)

- `display: inline-block`, `padding: 0.15rem 0.5rem`, `background: #2d1b4e`
- `border-radius: 3px`, `font-size: 0.75rem`, `color: #888`, `margin: 0.1rem`

## Status indicators

- `.status-dot`: `8px` circle (`width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 0.4rem`)
- `.status-online`: `background: #50c878`
- `.status-offline`: `background: #ff5050`
- `.status-warn`: `background: #ffbe32`

## Buttons

- Base `.btn`: `display: inline-block`, `border-radius: 4px`, `font-size: 0.85rem`, `font-weight: 600`, `text-decoration: none`, `border: 1px solid transparent`, `cursor: pointer`
- Sizes: `.btn-sm` (`padding: 0.25rem 0.6rem; font-size: 0.75rem`), default (`padding: 0.5rem 1rem`), `.btn-lg` (`padding: 0.75rem 1.5rem; font-size: 1rem`)

| Class            | Background               | Color     | Border    | Hover background               |
| ---------------- | ------------------------ | --------- | --------- | ------------------------------ |
| `.btn-primary`   | `rgba(255,113,206,0.15)` | `#ff71ce` | `#ff71ce` | `rgba(255,113,206,0.3)`        |
| `.btn-secondary` | `rgba(1,205,254,0.15)`   | `#01cdfe` | `#01cdfe` | `rgba(1,205,254,0.3)`          |
| `.btn-subtle`    | `transparent`            | `#888`    | `#3d2b5a` | color `#dcdcdc`, border `#888` |

## Alerts (`.instructions`)

- Base: `background: #2d1b4e`, `padding: 1rem`, `border-radius: 5px`, `border-left: 3px solid`
- Variants (left border color):

| Class                     | Border color |
| ------------------------- | ------------ |
| `.instructions` (default) | `#ff71ce`    |
| `.instructions-info`      | `#01cdfe`    |
| `.instructions-success`   | `#50c878`    |
| `.instructions-warn`      | `#ffbe32`    |
| `.instructions-error`     | `#ff5050`    |

## Blockquote

- `border-left: 3px solid #ff71ce`, `background: #2d1b4e`
- `padding: 1rem`, `border-radius: 5px`, `color: #dcdcdc`, `font-style: italic`

## Cards

- `.card`: `background: #2d1b4e`, `padding: 1rem`, `border-radius: 5px`, `border: 1px solid #3d2b5a`
- `.card-header`: `font-weight: 600`, `margin-bottom: 0.5rem`
- `.card-body`: `font-size: 0.9rem`, `color: #dcdcdc`

## Progress bars

- `.progress`: `background: #2d1b4e`, `border-radius: 4px`, `height: 8px`, `overflow: hidden`
- `.progress-bar`: `height: 100%`, `border-radius: 4px`, set width via inline `style="width: X%"`
- Color variants: `.progress-pink` (`#ff71ce`), `.progress-cyan` (`#01cdfe`), `.progress-purple` (`#b96dff`), `.progress-success` (`#50c878`)

## Forms

- Inputs (`text`, `password`), `textarea`, `select`: `background: #0f0a1a`, `border: 1px solid #2d1b4e`, `color: #dcdcdc`, `padding: 0.5rem 0.75rem`, `border-radius: 4px`, `font-family: inherit`, `font-size: 0.85rem`, `width: 100%`, `max-width: 400px`
- Focus: `outline: none`, `border-color: #ff71ce`
- Textarea: `min-height: 80px`, `resize: vertical`
- Labels: `display: block`, `margin: 0.5rem 0 0.25rem`, `color: #888`, `font-size: 0.85rem`

## Tables

- `width: 100%`, `border-collapse: collapse`
- `th`, `td`: `text-align: left`, `padding: 10px 14px`, `border-bottom: 1px solid #2d1b4e`
- `th`: `color: #888`, `font-weight: 600`, `font-size: 0.8em`, `text-transform: uppercase`, `letter-spacing: 0.05em`

## Layout utilities

| Class        | Effect                                            |
| ------------ | ------------------------------------------------- |
| `.grid`      | `display: grid; gap: 1rem`                        |
| `.grid-2`    | `grid-template-columns: 1fr 1fr`                  |
| `.grid-3`    | `grid-template-columns: 1fr 1fr 1fr`              |
| `.flex`      | `display: flex; gap: 0.5rem; align-items: center` |
| `.flex-wrap` | `flex-wrap: wrap`                                 |

## Tool cards

- `.tool`: `padding: 0.5rem 0`, `border-bottom: 1px solid #2d1b4e`
- `.tool-name`: `font-weight: bold`, `font-family: monospace`, `color: #ff71ce`
- `.tool-desc`: `color: #dcdcdc`, `font-size: 0.9rem`

## Config sections

- `.config-section`: `margin: 1.5rem 0`
- `.config-path`: `font-size: 0.85rem`, `color: #666`, `font-family: monospace`, `margin-bottom: 0.3rem`

## Avatar (`.avatar`)

- `width: 32px`, `height: 32px`, `border-radius: 50%`, `background: #3d2b5a`, `display: inline-block`

## Horizontal rule

- `border: none`, `border-top: 1px solid #3d2b5a`, `margin: 1.5rem 0`

## Base reset

- `* { margin: 0; padding: 0; box-sizing: border-box; }`
- `body`: `max-width: 900px`, `margin: 0 auto`, `padding: 2rem`, `background: #1a1025`, `color: #dcdcdc`, `line-height: 1.6`
- `p`: `margin: 0.5rem 0`
- `ul`, `ol`: `margin: 0.5rem 0`, `padding-left: 1.5rem`
- `li`: `margin: 0.25rem 0`

## Self-hosting fonts

Always self-host fonts as static files rather than loading from Google Fonts CDN.

1. Fetch the current font CSS from Google Fonts (note: both 400 and 700 weights are loaded):

```bash
curl -s -H "User-Agent: Mozilla/5.0" \
  "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;700&family=Roboto+Slab:wght@400;700&family=Source+Code+Pro:wght@400;700&family=Roboto+Mono:wght@400;700&display=swap"
```

2. Extract the `src: url(...)` value from each `@font-face` block. Download each file to `static/fonts/`:

```bash
mkdir -p static/fonts

curl -o static/fonts/source-serif-4-400-normal.<ext> "<url-from-step-1>"
curl -o static/fonts/source-serif-4-700-bold.<ext>   "<url-from-step-1>"
curl -o static/fonts/roboto-slab-400-normal.<ext>    "<url-from-step-1>"
curl -o static/fonts/roboto-slab-700-bold.<ext>      "<url-from-step-1>"
curl -o static/fonts/source-code-pro-400-normal.<ext> "<url-from-step-1>"
curl -o static/fonts/source-code-pro-700-bold.<ext>  "<url-from-step-1>"
curl -o static/fonts/roboto-mono-400-normal.<ext>    "<url-from-step-1>"
curl -o static/fonts/roboto-mono-700-bold.<ext>      "<url-from-step-1>"
```

Use the same file extension as the downloaded file (woff2 or ttf).

3. Add `@font-face` declarations to your CSS — match the `format()` to the file extension (`woff2` → `format('woff2')`, `ttf` → `format('truetype')`):

```css
@font-face {
  font-family: "Source Serif 4";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url("/fonts/source-serif-4-400-normal.woff2") format("woff2");
}

@font-face {
  font-family: "Source Serif 4";
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url("/fonts/source-serif-4-700-bold.woff2") format("woff2");
}

@font-face {
  font-family: "Roboto Slab";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url("/fonts/roboto-slab-400-normal.woff2") format("woff2");
}

@font-face {
  font-family: "Roboto Slab";
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url("/fonts/roboto-slab-700-bold.woff2") format("woff2");
}

@font-face {
  font-family: "Source Code Pro";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url("/fonts/source-code-pro-400-normal.woff2") format("woff2");
}

@font-face {
  font-family: "Source Code Pro";
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url("/fonts/source-code-pro-700-bold.woff2") format("woff2");
}

@font-face {
  font-family: "Roboto Mono";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url("/fonts/roboto-mono-400-normal.woff2") format("woff2");
}

@font-face {
  font-family: "Roboto Mono";
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url("/fonts/roboto-mono-700-bold.woff2") format("woff2");
}
```

4. Apply font stacks:

```css
body {
  font-family: "Source Serif 4", "Roboto Slab", serif;
}
code,
pre {
  font-family: "Source Code Pro", "Roboto Mono", monospace;
}
```

## Application workflow

1. Identify the component or page element being styled
2. Map it to the nearest pattern above
3. Apply corresponding color tokens, typography rules, and CSS classes
4. Verify against the live style guide at `styleguide.brain.tdvm.net` for edge cases
