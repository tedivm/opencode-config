# Prism.js Syntax Highlighting Theme

This document defines the Prism.js integration and custom token coloring for Rob's Style Guide.

## Integration

Prism.js is not included by default. All styling is custom CSS driven by design token CSS variables — no Prism base theme is used.

**Preferred:** Download the Prism core file and any language component files you need, place them in your project, and load them with local `<script>` tags.

**CDN alternative** (acceptable for quick prototypes or when self-hosting isn't practical):

### Scripts

- **Base:** `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js`
- **Language components** (loaded individually as needed):
  - `prism-json.min.js`, `prism-yaml.min.js`, `prism-json5.min.js`
  - `prism-javascript.min.js`, `prism-python.min.js`, `prism-go.min.js`
  - `prism-bash.min.js`, `prism-hcl.min.js`, `prism-markup.min.js`, `prism-diff.min.js`

### Inline Style Stripping

Prism injects inline `style` attributes on `<pre>` elements that override CSS variables. Strip them after every highlight pass:

```js
for (const pre of document.querySelectorAll("pre")) {
  pre.removeAttribute("style");
}
```

On theme toggle, re-run `Prism.highlightAll()` then strip styles again.

## Complete Prism CSS (Vanilla)

```css
code[class*="language-"],
pre[class*="language-"] {
  color: var(--code-fg);
  background: var(--code) !important;
  font-family: "Source Code Pro", "Roboto Mono", monospace;
  font-size: 0.85rem;
  text-align: left;
  white-space: pre;
  word-spacing: normal;
  word-break: normal;
  word-wrap: normal;
  line-height: 1.5;
  tab-size: 4;
  hyphens: none;
}

pre[class*="language-"] {
  border: 1px solid var(--surface);
  border-radius: 5px;
  padding: 1rem;
  margin: 0.5rem 0;
  overflow-x: auto;
}

pre code {
  background: none;
  padding: 0;
  color: inherit;
}

/* Comments: muted */
.token.comment,
.token.cdata {
  color: var(--muted) !important;
}

/* Strings, numbers, booleans, prolog: success (green) */
.token.prolog,
.token.doctype,
.token.string,
.token.char,
.token.attr-value,
.token.number,
.token.boolean {
  color: var(--success) !important;
}

/* Keywords, functions: pink (primary) */
.token.keyword,
.token.module,
.token.control,
.token.function,
.token.function-name,
.token.function-variable {
  color: var(--primary) !important;
}

/* Operators, punctuation, URL, deleted: error (red) */
.token.operator,
.token.punctuation,
.token.url,
.token.deleted {
  color: var(--error) !important;
}

/* Properties / variables: secondary (purple) */
.token.property,
.token.variable,
.token.symbol {
  color: var(--secondary) !important;
}

/* Tags: primary */
.token.tag {
  color: var(--primary) !important;
}

/* Attributes: secondary (name) */
.token.attr-name {
  color: var(--secondary) !important;
}

/* Built-in constants: cyan (accent) */
.token.constant,
.token.class-name,
.token.builtin {
  color: var(--accent) !important;
}

/* Selectors / at-rules: primary */
.token.selector,
.token.atrule {
  color: var(--primary) !important;
}

/* Namespace: secondary */
.token.namespace {
  color: var(--secondary) !important;
}

/* Entity: warning (amber) */
.token.entity {
  color: var(--warning) !important;
}

/* Regex: warning (amber) */
.token.regex {
  color: var(--warning) !important;
}

/* Importance: warning */
.token.important {
  color: var(--warning) !important;
}

/* Diff */
.token.inserted {
  color: var(--success) !important;
}
```

## Svelte Version

The Svelte implementation uses `:global()` wrappers on all token selectors and maps some CSS variable names to Svelte-specific equivalents:

- `var(--muted)` becomes `var(--muted-foreground)`
- `var(--error)` becomes `var(--destructive)`

```css
:global(.token.comment),
:global(.token.cdata) {
  color: var(--muted-foreground) !important;
}

:global(.token.prolog),
:global(.token.doctype),
:global(.token.string),
:global(.token.char),
:global(.token.attr-value),
:global(.token.number),
:global(.token.boolean) {
  color: var(--success) !important;
}

/* ... same pattern for remaining tokens ... */
```

### Svelte-Specific Integration Notes

- Load Prism scripts dynamically in `onMount()`
- Render pre-built HTML code snippets using `{@html ex.code}`
- Call `tick()` before `Prism.highlightAll()` to ensure the DOM is ready
- After `Prism.highlightAll()`, strip `style` attributes from all `<pre>` elements
- On theme toggle, re-run `Prism.highlightAll()` and strip styles again

## Token-to-Color Mapping

| Color              | Value     | Token Types                                                                                 |
| ------------------ | --------- | ------------------------------------------------------------------------------------------- |
| Primary (pink)     | `#de38a8` | keyword, module, control, function, function-name, function-variable, tag, selector, atrule |
| Secondary (purple) | `#b96dff` | property, variable, symbol, attr-name, namespace                                            |
| Accent (cyan)      | `#01cdfe` | constant, class-name, builtin                                                               |
| Success (green)    | `#50c878` | prolog, doctype, string, char, attr-value, number, boolean, inserted                        |
| Warning (amber)    | `#ffbe32` | regex, entity, important                                                                    |
| Error (red)        | `#ff5050` | operator, punctuation, url, deleted                                                         |
| Muted              | `#b4b4b4` | comment, cdata                                                                              |

## Token Table Styling

Use this CSS for the Prism showcase page's token reference table:

```css
.token-table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0 1.5rem;
  font-size: 0.85rem;
}

.token-table th,
.token-table td {
  text-align: left;
  padding: 8px 12px;
  border-bottom: 1px solid color-mix(in srgb, var(--border) 40%, transparent);
}

.token-table th {
  color: var(--secondary);
  font-weight: 600;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.token-table td {
  vertical-align: middle;
}

.token-table .swatch {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 3px;
}

.token-table .token-list {
  font-family: "Source Code Pro", "Roboto Mono", monospace;
  font-size: 0.8rem;
  color: var(--muted);
  line-height: 1.6;
}
```
