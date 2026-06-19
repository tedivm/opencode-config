# Svelte Theme CSS

Shadcn-style CSS variables and component styles for Svelte 5.

## Table of Contents

1. [Setup](#setup)
2. [CSS Variables](#css-variables)
3. [Body Styles](#body-styles)
4. [Component Styles](#component-styles)

---

## Setup

In Svelte, the theme CSS is imported at the root of the app:

```js
// src/main.js or src/App.svelte
import "./theme.css";
```

The `theme.css` file defines CSS variables on `:root` (dark mode default) and `.light` (light mode override).

## CSS Variables

See [SKILL.md](../SKILL.md#css-variables) for the complete variable definitions.

```css
:root {
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
}
```

## Body Styles

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
  background: var(--background);
  color: var(--foreground);
  line-height: 1.6;
  transition:
    background 0.2s,
    color 0.2s;
}
```

## Component Styles

In Svelte, component styles are typically scoped within each `.svelte` file using `<style>` blocks. The shared patterns are:

### Headings (in App.svelte or shared styles)

```css
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
  color: var(--foreground);
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
  color: var(--muted-foreground);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Text Utilities

```css
p {
  margin: 0.5rem 0;
}

.muted {
  color: var(--muted-foreground);
}
.dim {
  color: var(--muted-foreground);
}

.text-primary {
  color: var(--primary);
}
.text-secondary {
  color: var(--secondary);
}
.text-accent {
  color: var(--accent);
}
.text-success {
  color: var(--success);
}
.text-warning {
  color: var(--warning);
}
.text-destructive {
  color: var(--destructive);
}

.text-sm {
  font-size: 0.85rem;
}
.text-xs {
  font-size: 0.75rem;
}
.font-mono {
  font-family: "Source Code Pro", monospace;
}
.font-bold {
  font-weight: 700;
}
.uppercase {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.subtitle {
  color: var(--foreground);
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}
```

### Links

```css
a {
  color: var(--accent);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
```

### Inline Elements

```css
code {
  font-family: "Source Code Pro", monospace;
  background: var(--input);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
  color: var(--accent);
}

pre {
  background: var(--input);
  color: var(--foreground);
  padding: 1rem;
  border-radius: 5px;
  overflow-x: auto;
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0.5rem 0;
  border: 1px solid var(--border);
}

pre code {
  background: none;
  padding: 0;
  color: inherit;
}

.url {
  font-family: "Source Code Pro", monospace;
  background: var(--card);
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  color: var(--accent);
}

.kbd {
  display: inline-block;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 3px;
  padding: 0.1rem 0.4rem;
  font-family: "Source Code Pro", monospace;
  font-size: 0.75rem;
  color: var(--foreground);
}

.tooltip {
  position: relative;
  border-bottom: 1px dotted var(--secondary);
  cursor: help;
}

.tooltip:hover::after {
  content: attr(data-tip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--input);
  color: var(--foreground);
  padding: 0.4rem 0.6rem;
  border-radius: 3px;
  font-size: 0.75rem;
  white-space: nowrap;
  border: 1px solid var(--border);
  z-index: 1;
}

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

### Blockquote

```css
blockquote {
  position: relative;
  border-left: 3px solid transparent;
  background: var(--card);
  padding: 1rem;
  margin: 0.5rem 0;
  border-radius: 5px;
  color: var(--card-foreground);
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
```

### Lists

```css
ul,
ol {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}
li {
  margin: 0.25rem 0;
}
```

### Horizontal Rule

```css
hr {
  border: none;
  height: 1px;
  margin: 1.5rem 0;
  background: var(--gradient);
  filter: drop-shadow(
      0 0 6px color-mix(in srgb, var(--primary) 70%, transparent)
    )
    drop-shadow(0 0 16px color-mix(in srgb, var(--secondary) 40%, transparent));
}

hr.reverse {
  background: var(--gradient-reverse);
  filter: drop-shadow(
      0 0 6px color-mix(in srgb, var(--accent) 70%, transparent)
    )
    drop-shadow(0 0 16px color-mix(in srgb, var(--secondary) 40%, transparent));
}
```

### Tables

```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
}

table th,
table td {
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid color-mix(in srgb, var(--border) 40%, transparent);
}

table th {
  color: var(--muted-foreground);
  font-weight: 600;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Tags

```css
.tag {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  background: var(--card);
  border-radius: 3px;
  font-size: 0.75rem;
  color: var(--muted-foreground);
  margin: 0.1rem;
}
```

### Status Indicators

```css
.status-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 0.4rem;
}

.status-online {
  background: var(--success);
}
.status-offline {
  background: var(--destructive);
}
.status-warn {
  background: var(--warning);
}
```

### Alert Boxes

```css
.instructions {
  background: var(--card);
  padding: 1rem;
  border-radius: 5px;
  margin: 0.5rem 0;
  border-left: 3px solid var(--primary);
  font-size: 0.9rem;
}

.instructions-info {
  border-left-color: var(--secondary);
}
.instructions-success {
  border-left-color: var(--success);
}
.instructions-warn {
  border-left-color: var(--warning);
}
.instructions-error {
  border-left-color: var(--destructive);
}
```

### Forms

```css
label {
  display: block;
  margin-bottom: 0.25rem;
  color: var(--muted-foreground);
  font-size: 0.85rem;
}

.input {
  background: var(--input);
  border: 1px solid var(--border);
  color: var(--foreground);
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius);
  font-family: inherit;
  font-size: 0.85rem;
  width: 100%;
  max-width: 400px;
}

.input:focus {
  outline: none;
  border-color: var(--ring);
}

.textarea {
  background: var(--input);
  border: 1px solid var(--border);
  color: var(--foreground);
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius);
  font-family: inherit;
  font-size: 0.85rem;
  width: 100%;
  max-width: 400px;
  min-height: 80px;
  resize: vertical;
}
```

### Utility Layouts

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.back-link {
  font-size: 0.85rem;
  color: var(--muted-foreground);
  text-decoration: none;
}

.back-link:hover {
  text-decoration: underline;
}

.flex-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.space-y {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
```

### Font Specimen

```css
.font-specimen {
  font-size: 1.1rem;
  letter-spacing: 0.05em;
  margin: 0.25rem 0;
  color: var(--foreground);
}
```

### Glossary

```css
.glossary {
  margin: 0.5rem 0;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--card);
}

.glossary-term {
  font-weight: bold;
  font-family: "Source Code Pro", monospace;
  color: var(--primary);
}

.glossary-desc {
  color: var(--foreground);
  font-size: 0.9rem;
}
```

### Config Sections

```css
.config-section {
  margin: 1.5rem 0;
}
.config-path {
  font-size: 0.85rem;
  color: var(--muted-foreground);
  font-family: "Source Code Pro", monospace;
  margin-bottom: 0.3rem;
}
```

### Swatches

```css
.swatch {
  display: inline-block;
  width: 28px;
  height: 28px;
  border-radius: 4px;
  vertical-align: middle;
  margin-right: 6px;
  border: 1px solid var(--border);
}

.color-cell {
  display: flex;
  align-items: center;
  gap: 6px;
}
.color-hex {
  font-family: "Source Code Pro", monospace;
  font-size: 0.85rem;
}
```
