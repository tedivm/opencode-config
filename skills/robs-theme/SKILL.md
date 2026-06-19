---
name: robs-theme-implementation
description: Use when implementing, extending, or adapting Rob's Style Guide design system in any framework (vanilla HTML, Svelte, React, etc.). Covers theming, colors, typography, components, Prism.js syntax highlighting, and Tabler Icons. Don't use for generic styling, Tailwind projects, or unrelated design systems.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/robs-style-guide
---

## Overview

Rob's Style Guide is a dark purple design system with pink/purple/cyan accents, dual-mode (dark/light) support, and a consistent visual language. Vanilla HTML is the source of truth.

### Quick Start

The fastest way to adopt the theme is to copy the complete [vanilla `theme.css`](https://tedivm.github.io/robs-style-guide/vanilla/theme.css) into your project and reference it from your HTML. It contains all variables, typography, components, and layout utilities in a single file. Use the rest of this skill for customization, framework adaptation, or deeper understanding.

---

## Color Tokens

### Global (same in both modes)

| Name               | Hex       | Usage                               |
| ------------------ | --------- | ----------------------------------- |
| Primary (pink)     | `#de38a8` | h1, primary buttons, gradient start |
| Secondary (purple) | `#b96dff` | h2, links, secondary buttons        |
| Accent (cyan)      | `#01cdfe` | h3, accent elements                 |
| Success (green)    | `#50c878` | Success states, online              |
| Warning (amber)    | `#ffbe32` | Warning states, degraded            |
| Error (red)        | `#ff5050` | Error states, destructive           |

### Mode-dependent

| Layer           | Dark      | Light     |
| --------------- | --------- | --------- |
| Background      | `#1a1025` | `#fef5f7` |
| Surface / Cards | `#2d1b4e` | `#fce4ec` |
| Code / Inputs   | `#0f0a1a` | `#fce4ec` |
| Borders         | `#3d2b5a` | `#e4b8c8` |
| Body text       | `#dcdcdc` | `#2a1525` |
| Muted text      | `#b4b4b4` | `#8a6578` |
| Dim text        | `#999`    | `#a88a9a` |
| Code text       | `#e0e0e0` | `#4c1161` |
| Surface text    | `#dcdcdc` | `#2a1525` |

### Derived (transparency variants)

These are `color-mix` expressions that compute at runtime from the base color tokens. The resolved hex values are shown for reference.

| Variable                                             | Resolved                    | Usage                            |
| ---------------------------------------------------- | --------------------------- | -------------------------------- |
| `--primary-15`                                       | `rgba(222, 56, 168, 0.15)`  | Button/badge backgrounds         |
| `--primary-30`                                       | `rgba(222, 56, 168, 0.30)`  | Button hover states              |
| `--secondary-15`                                     | `rgba(185, 109, 255, 0.15)` | Button/badge backgrounds         |
| `--secondary-30`                                     | `rgba(185, 109, 255, 0.30)` | Button hover states              |
| `--accent-15`                                        | `rgba(1, 205, 254, 0.15)`   | Button/badge backgrounds         |
| `--accent-30`                                        | `rgba(1, 205, 254, 0.30)`   | Button hover states              |
| `--success-15`                                       | `rgba(80, 200, 120, 0.15)`  | Success button/badge backgrounds |
| `--success-30`                                       | `rgba(80, 200, 120, 0.30)`  | Success hover states             |
| `--warning-15`                                       | `rgba(255, 190, 50, 0.15)`  | Warning button/badge backgrounds |
| `--warning-30`                                       | `rgba(255, 190, 50, 0.30)`  | Warning hover states             |
| `--error-15` (vanilla) / `--destructive-15` (Svelte) | `rgba(255, 80, 80, 0.15)`   | Error/destructive backgrounds    |
| `--error-30` (vanilla) / `--destructive-30` (Svelte) | `rgba(255, 80, 80, 0.30)`   | Error/destructive hover          |

### Utility

| Variable             | Value                     | Usage                        |
| -------------------- | ------------------------- | ---------------------------- |
| `--sun-glow`         | `#ffe033`                 | Sun icon in dark mode        |
| `--sun-glow-70`      | `rgba(255, 224, 51, 0.7)` | Sun icon glow (outer)        |
| `--sun-glow-40`      | `rgba(255, 224, 51, 0.4)` | Sun icon glow (inner)        |
| `--text-on-gradient` | `#ffffff`                 | Text on gradient backgrounds |

### Gradient Variables

| Variable              | Direction | Colors               | Used on                                           |
| --------------------- | --------- | -------------------- | ------------------------------------------------- |
| `--gradient`          | 90deg →   | Pink → Purple → Cyan | h2 underline, hr, btn/badge gradient, progress    |
| `--gradient-reverse`  | 90deg →   | Cyan → Purple → Pink | hr.reverse, gradient border-box, progress reverse |
| `--gradient-vertical` | 180deg ↓  | Pink → Purple → Cyan | blockquote::before                                |

---

## CSS Variables

### `:root` (dark mode — default)

```css
:root {
  --bg: #1a1025;
  --fg: #dcdcdc;
  --surface: #2d1b4e;
  --surface-fg: #dcdcdc;
  --code: #0f0a1a;
  --code-fg: #e0e0e0;
  --border: #3d2b5a;
  --primary: #de38a8;
  --secondary: #b96dff;
  --accent: #01cdfe;
  --muted: #b4b4b4;
  --dim: #999;
  --success: #50c878;
  --warning: #ffbe32;
  --error: #ff5050;
  --gradient: linear-gradient(
    90deg,
    var(--primary),
    var(--secondary),
    var(--accent)
  );
  --gradient-reverse: linear-gradient(
    90deg,
    var(--accent),
    var(--secondary),
    var(--primary)
  );
  --gradient-vertical: linear-gradient(
    180deg,
    var(--primary),
    var(--secondary),
    var(--accent)
  );

  --primary-15: color-mix(in srgb, var(--primary) 15%, transparent);
  --primary-30: color-mix(in srgb, var(--primary) 30%, transparent);
  --secondary-15: color-mix(in srgb, var(--secondary) 15%, transparent);
  --secondary-30: color-mix(in srgb, var(--secondary) 30%, transparent);
  --accent-15: color-mix(in srgb, var(--accent) 15%, transparent);
  --accent-30: color-mix(in srgb, var(--accent) 30%, transparent);
  --error-15: color-mix(in srgb, var(--error) 15%, transparent);
  --error-30: color-mix(in srgb, var(--error) 30%, transparent);
  --success-15: color-mix(in srgb, var(--success) 15%, transparent);
  --success-30: color-mix(in srgb, var(--success) 30%, transparent);
  --warning-15: color-mix(in srgb, var(--warning) 15%, transparent);
  --warning-30: color-mix(in srgb, var(--warning) 30%, transparent);

  --sun-glow: #ffe033;
  --sun-glow-70: rgba(255, 224, 51, 0.7);
  --sun-glow-40: rgba(255, 224, 51, 0.4);
  --text-on-gradient: #ffffff;
}
```

### `.light` (light mode override)

Global colors and gradient variables carry through automatically — they reference color tokens that change in `.light`.

```css
.light {
  --bg: #fef5f7;
  --fg: #2a1525;
  --surface: #fce4ec;
  --surface-fg: #2a1525;
  --code: #fce4ec;
  --code-fg: #4c1161;
  --border: #e4b8c8;
  --primary: #de38a8;
  --secondary: #b96dff;
  --accent: #01cdfe;
  --muted: #8a6578;
  --dim: #a88a9a;
}
```

**Svelte naming** (shadcn-style `--background`, `--foreground`, `--card`, `--input`): used in `svelte/src/theme.css`. See [references/svelte-theme-css.md](references/svelte-theme-css.md).

---

## Typography

### Fonts

| Role      | Primary                          | Fallback                 |
| --------- | -------------------------------- | ------------------------ |
| Body      | `Source Serif 4` (400, 600, 700) | `Roboto Slab` (400, 700) |
| Monospace | `Source Code Pro` (400, 700)     | `Roboto Mono` (400, 700) |

**Preferred:** Download the font files and serve them locally using `@font-face`. This avoids external dependencies, improves load times, and works offline.

**CDN alternative** (acceptable for quick prototypes or when self-hosting isn't practical):

```html
<link
  href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto+Slab:wght@400;700&family=Source+Code+Pro:wght@400;700&family=Source+Serif+4:wght@400;600;700&display=swap"
  rel="stylesheet"
/>
```

### Body and Headings

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Source Serif 4", "Roboto Slab", serif;
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.6;
  transition:
    background 0.2s,
    color 0.2s;
}

h1 {
  font-size: 1.8rem;
  margin: 2rem 0 0.75rem;
  color: var(--primary);
  text-shadow:
    0 0 20px color-mix(in srgb, var(--primary) 60%, transparent),
    0 0 40px color-mix(in srgb, var(--primary) 35%, transparent),
    0 0 60px color-mix(in srgb, var(--primary) 20%, transparent);
}

h2 {
  font-size: 1.3rem;
  margin: 2rem 0 0.75rem;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid;
  border-image: var(--gradient) 1;
  color: var(--secondary);
  text-shadow:
    0 0 20px color-mix(in srgb, var(--secondary) 50%, transparent),
    0 0 40px color-mix(in srgb, var(--secondary) 30%, transparent),
    0 0 60px color-mix(in srgb, var(--secondary) 15%, transparent);
  position: relative;
}

h2::after {
  content: "";
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gradient);
  filter: blur(6px);
  opacity: 0.7;
}

.light h1 {
  text-shadow:
    0 0 20px color-mix(in srgb, var(--primary) 25%, transparent),
    0 0 40px color-mix(in srgb, var(--primary) 12%, transparent);
}

.light h2 {
  text-shadow:
    0 0 20px color-mix(in srgb, var(--secondary) 25%, transparent),
    0 0 40px color-mix(in srgb, var(--secondary) 12%, transparent);
}

h3 {
  font-size: 1.1rem;
  margin: 1.5rem 0 0.5rem;
  color: var(--accent);
}
h4 {
  font-size: 1rem;
  margin: 1.2rem 0 0.4rem;
  color: var(--fg);
}
h5 {
  font-size: 0.9rem;
  margin: 1rem 0 0.3rem;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
h6 {
  font-size: 0.85rem;
  margin: 1rem 0 0.3rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Text Utilities

```css
p {
  margin: 0.5rem 0;
}
.subtitle {
  color: var(--fg);
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}
.muted {
  color: var(--muted);
}
.dim {
  color: var(--dim);
}

.text-pink {
  color: var(--primary);
}
.text-cyan {
  color: var(--accent);
}
.text-purple {
  color: var(--secondary);
}
.text-success {
  color: var(--success);
}
.text-warn {
  color: var(--warning);
}
.text-error {
  color: var(--error);
}

.text-sm {
  font-size: 0.85rem;
}
.text-xs {
  font-size: 0.75rem;
}

.font-mono {
  font-family: "Source Code Pro", "Roboto Mono", monospace;
}
.font-bold {
  font-weight: 700;
}
.uppercase {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

a {
  color: var(--accent);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
```

### Code and Blockquote

```css
code {
  font-family: "Source Code Pro", "Roboto Mono", monospace;
  background: var(--code);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
  color: var(--accent);
}

pre {
  background: var(--code);
  color: var(--code-fg);
  padding: 1rem;
  border-radius: 5px;
  overflow-x: auto;
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0.5rem 0;
  border: 1px solid var(--surface);
}
pre code {
  background: none;
  padding: 0;
  color: inherit;
}

blockquote {
  position: relative;
  border-left: 3px solid transparent;
  background: var(--surface);
  padding: 1rem;
  margin: 0.5rem 0;
  border-radius: 5px;
  color: var(--surface-fg);
  font-style: italic;
}
blockquote::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--gradient-vertical);
}

ul,
ol {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}
li {
  margin: 0.25rem 0;
}
```

---

## Components

All component CSS is in [assets/components.css](assets/components.css) (sourced from `docs/vanilla/theme.css`):

| Component               | Variants                                                                                                                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Button**              | `.btn-primary`, `.btn-secondary`, `.btn-tertiary`, `.btn-subtle`, `.btn-destructive`, `.btn-outline`, `.btn-ghost`, `.btn-link`, `.btn-gradient`, `.btn-sm`, `.btn-lg`, `.btn-icon` |
| **Badge**               | `.badge-app`, `.badge-ai`, `.badge-infra`, `.badge-success`, `.badge-warn`, `.badge-error`, `.badge-gradient`                                                                       |
| **Tag**                 | `.tag`                                                                                                                                                                              |
| **Card**                | `.card`, `.card-header`, `.card-body`, `.card-meta`, `.card-link`                                                                                                                   |
| **Alert**               | `.instructions` + `-info`, `-success`, `-warn`, `-error`                                                                                                                            |
| **Progress**            | `.progress`, `.progress-bar` + color variants + `.gradient`, `.gradient-reverse`                                                                                                    |
| **Status**              | `.status-dot` + `.status-online`, `.status-offline`, `.status-warn`                                                                                                                 |
| **Forms**               | `input`, `textarea`, `select`, `label`                                                                                                                                              |
| **Table**               | `table`, `th`, `td`                                                                                                                                                                 |
| **Inline**              | `.tooltip`, `.kbd`, `.url`                                                                                                                                                          |
| **HR**                  | `hr` + `.reverse`                                                                                                                                                                   |
| **Theme toggle**        | `.theme-toggle` + `.light .theme-toggle`                                                                                                                                            |
| **Color table**         | `.color-toggle`, `tr[data-derived]`, `.derived-name`                                                                                                                                |
| **Spinner**             | `.spinner`, `.spinner-sm`, `.spinner-lg`, `.spinner-track`, `.spinner-track-sm`, `.spinner-track-lg`                                                                                |
| **Pulse dot**           | `.pulse-dot` + `.pulse-dot-pink`, `-cyan`, `-purple`, `-success`, `-warn`, `-error` + `.pulse-dot-sm`, `.pulse-dot-lg`                                                              |
| **Skeleton**            | `.skeleton`, `.skeleton-line`, `.skeleton-line-sm`, `.skeleton-line-lg`, `.skeleton-avatar`, `.skeleton-card` + width utilities `w-100`, `w-75`, `w-50`, `w-25`                     |
| **Dot loader**          | `.dot-loader` + `.dot-loader-sm`, `.dot-loader-lg`, `.dot-loader-solid`, `.dot-loader-pink`                                                                                         |
| **Bar loader**          | `.bar-loader` + `.bar-loader-sm`, `.bar-loader-lg` (5 bars: primary → blend → secondary → blend → accent)                                                                           |
| **Vertical bar loader** | `.bar-loader-vertical` + `.bar-loader-vertical-sm`, `.bar-loader-vertical-lg` (same 5-bar gradient, scaleY animation)                                                               |

Svelte component code (Button, Badge, Card, etc.): [references/components.md](references/components.md)

---

## Layout Utilities

Grid, flex, toolbar, swatch, avatar, glossary: [assets/layout.css](assets/layout.css)

| Utility                                         | Description                            |
| ----------------------------------------------- | -------------------------------------- |
| `.grid`, `.grid-2`, `.grid-3`                   | CSS grid with 1rem gap                 |
| `.flex`, `.flex-wrap`                           | Flexbox with 0.5rem gap                |
| `.toolbar`                                      | Flex row, 1rem gap, 2rem bottom margin |
| `.back-link`                                    | Muted link, underlines on hover        |
| `.swatch`, `.color-cell`, `.color-hex`          | Color palette display                  |
| `.font-specimen`                                | Font showcase text                     |
| `.avatar`                                       | 32px circular placeholder              |
| `.glossary`, `.glossary-term`, `.glossary-desc` | Glossary listing                       |
| `.config-section`, `.config-path`               | Config display                         |

---

## Theme Toggle

### Vanilla JavaScript

Dark mode is the default. The `.light` class on `<html>` switches to light mode. Uses SVG icons — sun in dark mode, moon in light mode.

```js
var sunSvg =
  '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>';
var moonSvg =
  '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>';
var toggle = document.getElementById("theme-toggle");
var isLight = window.matchMedia("(prefers-color-scheme: light)").matches;
if (isLight) {
  document.documentElement.classList.add("light");
  toggle.innerHTML = moonSvg;
  toggle.title = "Toggle Dark Mode";
}
toggle.addEventListener("click", function () {
  isLight = !isLight;
  document.documentElement.classList.toggle("light", isLight);
  toggle.innerHTML = isLight ? moonSvg : sunSvg;
  toggle.title = isLight ? "Toggle Dark Mode" : "Toggle Light Mode";
});
```

Svelte version with Prism re-highlight: [references/theme-toggle-js.md](references/theme-toggle-js.md)

---

## Code Highlighting (Prism.js)

The theme uses Prism.js for syntax highlighting with custom token colors that match the design system. **Prism is not included by default** — it requires explicit setup before any code highlighting will work.

**Before implementing code highlighting, read [references/prism-theme.md](references/prism-theme.md) first.** It covers:

- Downloading and self-hosting Prism.js core + language bundles (preferred) or loading from CDN (acceptable for quick prototypes)
- The custom CSS token color mappings that match the theme palette
- Initializing Prism on page load (`Prism.highlightAll()`)
- Re-highlighting code after a theme toggle (required so tokens adapt to dark/light)
- Language selection and which bundles to load

The complete Prism CSS token styles are available in [assets/prism.css](assets/prism.css).

Without these steps, `<pre><code>` blocks will render with the base styles from [assets/typography.css](assets/typography.css) but will have no syntax coloring.

---

## Key Conventions

- Vanilla is the **source of truth** for all styling
- Dark mode is the **default** in both vanilla and Svelte (`:root` = dark); light mode is an override (`.light` class)
- Max content width: `900px`, centered with `margin: 0 auto`
- Line height: `1.6` on body, `1.5` on code blocks
- Gradient direction is always `90deg` (left to right) unless specified otherwise
- `border-image` is used for h2 underlines, not `border-bottom`
- `h2::after` adds a blurred glow beneath the border-image line
- Badge backgrounds use `rgba(color, 0.15)` for the tinted effect
- Gradient buttons and badges use the `padding-box` / `border-box` trick for gradient borders
- The `.light` override only needs mode-dependent variables; global colors and gradient variables carry through automatically
- Prefer self-hosting fonts, JavaScript, and other third-party resources; CDN is acceptable for quick prototypes or when self-hosting isn't practical

---

## Assets

- [assets/variables.css](assets/variables.css) — `:root` + `.light` color tokens and gradient variables
- [assets/typography.css](assets/typography.css) — Reset, body, headings, text, code, blockquote, lists
- [assets/components.css](assets/components.css) — Buttons, badges, cards, alerts, progress, forms, tables, inline elements, hr, theme toggle, color table
- [assets/layout.css](assets/layout.css) — Grid, flex, toolbar, swatch, avatar, glossary
- [assets/prism.css](assets/prism.css) — Prism.js token color mappings for syntax highlighting

## References

- [references/svelte-theme-css.md](references/svelte-theme-css.md) — Svelte shadcn-style variables and component styles
- [references/components.md](references/components.md) — Svelte component code (Button, Badge, Card, Alert, Progress)
- [references/prism-theme.md](references/prism-theme.md) — Prism.js token mappings and integration
- [references/icons.md](references/icons.md) — Tabler Icons usage patterns
- [references/theme-toggle-js.md](references/theme-toggle-js.md) — Svelte theme toggle with Prism re-highlight
- [references/page-templates.md](references/page-templates.md) — Full HTML and Svelte page scaffolds
