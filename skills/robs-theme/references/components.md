# Components Reference

Complete component implementations for Rob's Style Guide. Each component includes vanilla HTML/CSS and Svelte 5 variants.

## Table of Contents

1. [Buttons](#buttons)
2. [Badges](#badges)
3. [Tags](#tags)
4. [Cards](#cards)
5. [Alert / Instructions](#alert-instructions)
6. [Progress Bars](#progress-bars)
7. [Status Dots](#status-dots)
8. [Forms](#forms)
9. [Tables](#tables)
10. [Horizontal Rules](#horizontal-rules)
11. [Layout Utilities](#layout-utilities)
12. [Swatch / Color](#swatch-color)
13. [Toolbar](#toolbar)
14. [Glossary](#glossary)
15. [Config Sections](#config-sections)
16. [Avatar](#avatar)
17. [Spinners](#spinners)
18. [Pulse Dots](#pulse-dots)
19. [Skeleton Shimmer](#skeleton-shimmer)
20. [Dot Loader](#dot-loader)
21. [Bar Loader](#bar-loader)
22. [Vertical Bar Loader](#vertical-bar-loader)

---

## Buttons

### Variants

| Variant       | Description                                         |
| ------------- | --------------------------------------------------- |
| `primary`     | Pink background with pink border                    |
| `secondary`   | Purple background with purple border                |
| `subtle`      | Transparent with border color                       |
| `destructive` | Red/error background with red border                |
| `outline`     | Transparent with border, turns pink on hover        |
| `ghost`       | Transparent, no border, surface background on hover |
| `link`        | Transparent, primary color text                     |
| `gradient`    | Gradient background with gradient border            |

### Sizes

| Size      | Class                                           |
| --------- | ----------------------------------------------- |
| `sm`      | `btn-sm` (0.25rem 0.6rem padding, 0.75rem font) |
| `default` | `btn` (0.5rem 1rem padding, 0.85rem font)       |
| `lg`      | `btn-lg` (0.75rem 1.5rem padding, 1rem font)    |

### Vanilla CSS

```css
.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-family: "Source Serif 4", "Roboto Slab", serif;
  font-size: 0.85rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  border: 1px solid transparent;
}

.btn-primary {
  background: var(--primary-15);
  color: var(--primary);
  border-color: var(--primary);
}
.btn-primary:hover {
  background: var(--primary-30);
}
.btn-secondary {
  background: var(--secondary-15);
  color: var(--secondary);
  border-color: var(--secondary);
}
.btn-secondary:hover {
  background: var(--secondary-30);
}
.btn-tertiary {
  background: var(--accent-15);
  color: var(--accent);
  border-color: var(--accent);
}
.btn-tertiary:hover {
  background: var(--accent-30);
}
.btn-subtle {
  background: transparent;
  color: var(--muted);
  border-color: var(--border);
}
.btn-subtle:hover {
  color: var(--fg);
  border-color: var(--muted);
}
.btn-destructive {
  background: var(--error-15);
  color: var(--error);
  border-color: var(--error);
}
.btn-destructive:hover {
  background: var(--error-30);
}
.btn-outline {
  background: transparent;
  color: var(--fg);
  border-color: var(--border);
}
.btn-outline:hover {
  color: var(--primary);
  border-color: var(--primary);
}
.btn-ghost {
  background: transparent;
  color: var(--fg);
  border: none;
}
.btn-ghost:hover {
  background: var(--surface);
}
.btn-link {
  background: transparent;
  color: var(--primary);
  border: none;
}
.btn-link:hover {
  opacity: 0.85;
}
.btn-gradient {
  border: 1px solid transparent;
  background:
    var(--gradient) padding-box,
    var(--gradient-reverse) border-box;
  color: var(--text-on-gradient);
}
.btn-gradient:hover {
  background:
    linear-gradient(
        90deg,
        var(--primary-30),
        var(--secondary-30),
        var(--accent-30)
      )
      padding-box,
    var(--gradient-reverse) border-box;
}
.btn-sm {
  padding: 0.25rem 0.6rem;
  font-size: 0.75rem;
}
.btn-lg {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}
.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.45rem;
  line-height: 0;
}
```

### Svelte `Button.svelte`

```svelte
<script>
  let { variant = 'primary', size = 'default', onclick, icon = false, class: extraClass = '' } = $props();

  function getClasses() {
    let v = 'btn-' + variant;
    let s = size !== 'default' ? 'btn-' + size : '';
    let i = icon ? 'btn-icon' : '';
    return [v, s, i, extraClass].filter(Boolean).join(' ');
  }
</script>

<button class="btn {getClasses()}" {onclick}>
  <slot />
</button>

<style>
  /* Button styles are in theme.css */
</style>
```

### Usage

```svelte
<Button variant="primary" size="sm" onclick={fn}>Click</Button>
```

---

## Badges

### Variants

| Variant                 | Description                     |
| ----------------------- | ------------------------------- |
| `app` / `primary`       | Pink color                      |
| `ai` / `secondary`      | Purple color                    |
| `infra` / `accent`      | Cyan color                      |
| `success`               | Green color                     |
| `warn` / `warning`      | Yellow color                    |
| `error` / `destructive` | Red color                       |
| `gradient`              | Gradient border with white text |

### Vanilla CSS

```css
.badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.75em;
  font-weight: 600;
}
.badge-app {
  background: var(--primary-15);
  color: var(--primary);
}
.badge-ai {
  background: var(--secondary-15);
  color: var(--secondary);
}
.badge-infra {
  background: var(--accent-15);
  color: var(--accent);
}
.badge-success {
  background: var(--success-15);
  color: var(--success);
}
.badge-warn {
  background: var(--warning-15);
  color: var(--warning);
}
.badge-error {
  background: var(--error-15);
  color: var(--error);
}
.badge-gradient {
  border: 1px solid transparent;
  background:
    var(--gradient) padding-box,
    var(--gradient-reverse) border-box;
  color: var(--text-on-gradient);
}
```

### Svelte `Badge.svelte`

```svelte
<script>
  let { variant = 'primary' } = $props();

  function getClasses() {
    return 'badge badge-' + variant;
  }
</script>

<span class={getClasses()}>
  <slot />
</span>

<style>
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 0.75em;
    font-weight: 600;
  }

  .badge-primary {
    background: var(--primary-15);
    color: var(--primary);
  }

  .badge-secondary {
    background: var(--accent-15);
    color: var(--secondary);
  }

  .badge-accent {
    background: var(--secondary-15);
    color: var(--accent);
  }

  .badge-destructive {
    background: var(--destructive-15);
    color: var(--destructive);
  }

  .badge-success {
    background: var(--success-15);
    color: var(--success);
  }

  .badge-warning {
    background: var(--warning-15);
    color: var(--warning);
  }

  .badge-gradient {
    border: 1px solid transparent;
    background: var(--gradient) padding-box, var(--gradient-reverse) border-box;
    color: var(--text-on-gradient);
  }
</style>
```

---

## Tags

### Vanilla CSS

```css
.tag {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  background: var(--surface);
  border-radius: 3px;
  font-size: 0.75rem;
  color: var(--muted);
  margin: 0.1rem;
}
```

---

## Cards

### Vanilla CSS

```css
.card {
  background: var(--surface);
  padding: 1rem;
  border-radius: 5px;
  border: 1px solid var(--border);
  transition: border-color 0.2s;
}

.card:hover {
  border-color: var(--primary);
}
.card a.card-link {
  text-decoration: none;
}
.card a.card-link:hover {
  text-decoration: none;
}
.card-header {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--accent);
  font-size: 1.1rem;
}
.card-body {
  font-size: 0.9rem;
  color: var(--surface-fg);
}
.card-meta {
  font-size: 0.8rem;
  color: var(--muted);
  margin-top: 0.5rem;
  font-family: "Source Code Pro", monospace;
}
```

### Svelte `Card.svelte`

```svelte
<script>
</script>

<div class="card">
  <div class="card-header-wrapper"><slot name="header" /></div>
  <slot name="body" />
</div>

<style>
  .card {
    background: var(--card);
    color: var(--card-foreground);
    padding: 1rem;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    margin-bottom: 0.5rem;
  }

  .card:hover {
    border-color: var(--primary);
  }

  .card-header-wrapper {
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--accent);
    font-size: 1.1rem;
  }
</style>
```

---

## Alert / Instructions

### Vanilla CSS

```css
.instructions {
  background: var(--surface);
  padding: 1rem;
  border-radius: 5px;
  margin: 0.5rem 0;
  border-left: 3px solid var(--primary);
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
  border-left-color: var(--error);
}
```

### Svelte `Alert.svelte`

```svelte
<script>
  let { variant = 'default' } = $props();

  function getStyles() {
    const c = variant === 'default' ? 'var(--primary)'
      : variant === 'secondary' ? 'var(--secondary)'
      : variant === 'destructive' ? 'var(--destructive)'
      : variant === 'success' ? 'var(--success)'
      : variant === 'warning' ? 'var(--warning)'
      : 'var(--primary)';
    return 'background: var(--muted); border-left: 3px solid ' + c + ';';
  }
</script>

<div class="alert" style={getStyles()}>
  <slot />
</div>

<style>
  .alert {
    padding: 1rem;
    border-radius: var(--radius);
    margin: 0.5rem 0;
    font-size: 0.9rem;
  }
</style>
```

---

## Progress Bars

### Vanilla CSS

```css
.progress {
  background: var(--surface);
  border-radius: 4px;
  height: 8px;
  overflow: hidden;
  margin: 0.5rem 0;
}
.progress-bar {
  height: 100%;
  border-radius: 4px;
}
.progress-pink {
  background: var(--primary);
}
.progress-cyan {
  background: var(--accent);
}
.progress-purple {
  background: var(--secondary);
}
.progress-success {
  background: var(--success);
}
.progress-bar.gradient {
  background: var(--gradient);
}
.progress-bar.gradient-reverse {
  background: var(--gradient-reverse);
}
```

### Svelte `Progress.svelte`

```svelte
<script>
  let { value = 0, color = 'primary' } = $props();

  function getStyles() {
    const c = color === 'primary' ? 'var(--primary)'
      : color === 'secondary' ? 'var(--secondary)'
      : color === 'accent' ? 'var(--accent)'
      : color === 'success' ? 'var(--success)'
      : 'var(--primary)';
    return 'background: ' + c + '; width: ' + value + '%;';
  }
</script>

<div class="progress">
  <div class="bar" style={getStyles()}></div>
</div>

<style>
  .progress {
    background: var(--muted);
    border-radius: 4px;
    height: 8px;
    overflow: hidden;
    margin: 0.5rem 0;
  }
  .bar {
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s;
  }
</style>
```

### Svelte `GradientProgress.svelte`

```svelte
<script>
  let { value = 0, reverse = false } = $props();
</script>

<div class="progress">
  <div class="bar {reverse ? 'bar-reverse' : ''}" style="width: {value}%;"></div>
</div>

<style>
  .progress {
    background: var(--muted);
    border-radius: 4px;
    height: 8px;
    overflow: hidden;
    margin: 0.5rem 0;
  }
  .bar {
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s;
    background: var(--gradient);
  }
  .bar-reverse {
    background: var(--gradient-reverse);
  }
</style>
```

---

## Status Dots

### Vanilla CSS

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
  background: var(--error);
}
.status-warn {
  background: var(--warning);
}
```

---

## Forms

### Vanilla CSS

```css
input[type="text"],
input[type="password"],
textarea,
select {
  background: var(--code);
  border: 1px solid var(--surface);
  color: var(--fg);
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  font-family: inherit;
  font-size: 0.85rem;
  width: 100%;
  max-width: 400px;
}

input[type="text"]:focus,
input[type="password"]:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: var(--primary);
}

textarea {
  min-height: 80px;
  resize: vertical;
}
label {
  display: block;
  margin: 0.5rem 0 0.25rem;
  color: var(--muted);
  font-size: 0.85rem;
}
```

---

## Tables

### Vanilla CSS

```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
}
th,
td {
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid color-mix(in srgb, var(--border) 40%, transparent);
}
th {
  color: var(--muted);
  font-weight: 600;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

---

## Horizontal Rules

### Vanilla CSS

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

---

## Layout Utilities

### Grid

```css
.grid {
  display: grid;
  gap: 1rem;
}
.grid-2 {
  grid-template-columns: 1fr 1fr;
}
.grid-3 {
  grid-template-columns: 1fr 1fr 1fr;
}
```

### Flex

```css
.flex {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
.flex-wrap {
  flex-wrap: wrap;
}
```

---

## Swatch / Color

### Vanilla CSS

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

---

## Toolbar

### Vanilla CSS

```css
.toolbar {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}
.back-link {
  font-size: 0.85rem;
  color: var(--muted);
  text-decoration: none;
}
.back-link:hover {
  text-decoration: underline;
}
```

---

## Glossary

### Vanilla CSS

```css
.glossary {
  margin: 0.5rem 0;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--surface);
}
.glossary-term {
  font-weight: bold;
  font-family: monospace;
  color: var(--primary);
}
.glossary-desc {
  color: var(--fg);
  font-size: 0.9rem;
}
```

---

## Config Sections

### Vanilla CSS

```css
.config-section {
  margin: 1.5rem 0;
}
.config-path {
  font-size: 0.85rem;
  color: var(--dim);
  font-family: monospace;
  margin-bottom: 0.3rem;
}
```

---

## Avatar

### Vanilla CSS

```css
.avatar {
  display: inline-block;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--border);
  vertical-align: middle;
}
```

---

## Spinners

### Variants

| Variant   | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `default` | Solid conic gradient (primary → secondary → accent) with glow |
| `track`   | Ring variant with masked center for a track effect            |

### Sizes

| Size      | Class                                    |
| --------- | ---------------------------------------- |
| `sm`      | `spinner-sm` / `spinner-track-sm` (24px) |
| `default` | `spinner` / `spinner-track` (40px)       |
| `lg`      | `spinner-lg` / `spinner-track-lg` (56px) |

### Vanilla CSS

```css
.spinner {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: conic-gradient(
    from 0deg,
    var(--primary),
    var(--secondary),
    var(--accent),
    var(--primary)
  );
  animation: spinner-rotate 4s linear infinite;
  box-shadow:
    0 0 12px color-mix(in srgb, var(--primary) 40%, transparent),
    0 0 24px color-mix(in srgb, var(--secondary) 25%, transparent);
}
.spinner-sm {
  width: 24px;
  height: 24px;
}
.spinner-lg {
  width: 56px;
  height: 56px;
}

.spinner-track {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: conic-gradient(
    from 0deg,
    var(--surface),
    var(--surface),
    var(--surface),
    var(--surface)
  );
  position: relative;
}
.spinner-track::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(
    from 0deg,
    var(--primary),
    var(--secondary),
    var(--accent),
    var(--primary)
  );
  animation: spinner-rotate 4s linear infinite;
  z-index: 1;
}
.spinner-track::after {
  content: "";
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: var(--bg);
  z-index: 2;
}
.spinner-track-sm {
  width: 24px;
  height: 24px;
}
.spinner-track-lg {
  width: 56px;
  height: 56px;
}

@keyframes spinner-rotate {
  to {
    transform: rotate(360deg);
  }
}
```

### HTML Usage

```html
<!-- Solid spinner -->
<div class="spinner"></div>
<div class="spinner spinner-sm"></div>
<div class="spinner spinner-lg"></div>

<!-- Track spinner -->
<div class="spinner-track"></div>
<div class="spinner-track spinner-track-sm"></div>
<div class="spinner-track spinner-track-lg"></div>
```

---

## Pulse Dots

### Variants

| Variant   | Description                          |
| --------- | ------------------------------------ |
| `pink`    | `pulse-dot-pink` (primary color)     |
| `cyan`    | `pulse-dot-cyan` (accent color)      |
| `purple`  | `pulse-dot-purple` (secondary color) |
| `success` | `pulse-dot-success` (green)          |
| `warn`    | `pulse-dot-warn` (amber)             |
| `error`   | `pulse-dot-error` (red)              |

### Sizes

| Size      | Class                 |
| --------- | --------------------- |
| `sm`      | `pulse-dot-sm` (8px)  |
| `default` | `pulse-dot` (12px)    |
| `lg`      | `pulse-dot-lg` (16px) |

### Vanilla CSS

```css
.pulse-dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  position: relative;
}
.pulse-dot::before {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 2px solid currentColor;
  animation: pulse-ring 1.5s ease-out infinite;
  opacity: 0;
}
.pulse-dot::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: currentColor;
}
.pulse-dot-pink {
  color: var(--primary);
}
.pulse-dot-cyan {
  color: var(--accent);
}
.pulse-dot-purple {
  color: var(--secondary);
}
.pulse-dot-success {
  color: var(--success);
}
.pulse-dot-warn {
  color: var(--warning);
}
.pulse-dot-error {
  color: var(--error);
}
.pulse-dot-sm {
  width: 8px;
  height: 8px;
}
.pulse-dot-sm::before {
  inset: -3px;
  border-width: 1.5px;
}
.pulse-dot-lg {
  width: 16px;
  height: 16px;
}
.pulse-dot-lg::before {
  inset: -6px;
  border-width: 2.5px;
}

@keyframes pulse-ring {
  0% {
    transform: scale(0.8);
    opacity: 1;
  }
  100% {
    transform: scale(1.8);
    opacity: 0;
  }
}
```

### HTML Usage

```html
<!-- Color variants -->
<div class="pulse-dot pulse-dot-pink"></div>
<div class="pulse-dot pulse-dot-cyan"></div>

<!-- Sizes -->
<div class="pulse-dot pulse-dot-pink pulse-dot-sm"></div>
<div class="pulse-dot pulse-dot-pink"></div>
<div class="pulse-dot pulse-dot-pink pulse-dot-lg"></div>

<!-- Inline usage -->
<span
  >Processing<span
    class="pulse-dot pulse-dot-cyan pulse-dot-sm"
    style="margin-left: 0.4rem; vertical-align: middle;"
  ></span
></span>
```

---

## Skeleton Shimmer

### Variants

| Variant           | Description                        |
| ----------------- | ---------------------------------- |
| `skeleton-line`   | Horizontal line placeholder        |
| `skeleton-avatar` | Circular avatar placeholder (32px) |
| `skeleton-card`   | Card-shaped skeleton container     |

### Sizes

| Size      | Class                            |
| --------- | -------------------------------- |
| `sm`      | `skeleton-line-sm` (8px height)  |
| `default` | `skeleton-line` (12px height)    |
| `lg`      | `skeleton-line-lg` (16px height) |

### Width Utilities

| Class   | Width |
| ------- | ----- |
| `w-100` | 100%  |
| `w-75`  | 75%   |
| `w-50`  | 50%   |
| `w-25`  | 25%   |

### Vanilla CSS

```css
.skeleton {
  background: var(--surface);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}
.skeleton::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    color-mix(in srgb, var(--border) 40%, transparent),
    transparent
  );
  animation: shimmer 1.5s ease-in-out infinite;
}
.skeleton-line {
  height: 12px;
  margin: 0.5rem 0;
  border-radius: 4px;
}
.skeleton-line-sm {
  height: 8px;
}
.skeleton-line-lg {
  height: 16px;
}
.skeleton-line.w-100 {
  width: 100%;
}
.skeleton-line.w-75 {
  width: 75%;
}
.skeleton-line.w-50 {
  width: 50%;
}
.skeleton-line.w-25 {
  width: 25%;
}
.skeleton-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}
.skeleton-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 5px;
  padding: 1rem;
}
.skeleton-card .skeleton-line:first-child {
  width: 60%;
  height: 14px;
}

@keyframes shimmer {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}
```

### HTML Usage

```html
<!-- Lines -->
<div class="skeleton skeleton-line w-100"></div>
<div class="skeleton skeleton-line skeleton-line-sm w-75"></div>
<div class="skeleton skeleton-line skeleton-line-lg w-50"></div>

<!-- Card layout -->
<div class="skeleton-card">
  <div class="skeleton skeleton-line"></div>
  <div class="skeleton skeleton-line skeleton-line-sm w-100"></div>
  <div class="skeleton skeleton-line skeleton-line-sm w-75"></div>
</div>

<!-- With avatar -->
<div style="display: flex; gap: 0.75rem; align-items: flex-start;">
  <div class="skeleton skeleton-avatar"></div>
  <div style="flex: 1;">
    <div class="skeleton skeleton-line w-50"></div>
    <div class="skeleton skeleton-line skeleton-line-sm w-75"></div>
  </div>
</div>
```

---

## Dot Loader

### Variants

| Variant   | Description                                     |
| --------- | ----------------------------------------------- |
| `default` | Gradient (primary → secondary → accent)         |
| `solid`   | `dot-loader-solid` (all dots use fg color)      |
| `pink`    | `dot-loader-pink` (primary with fading opacity) |

### Sizes

| Size      | Class                       |
| --------- | --------------------------- |
| `sm`      | `dot-loader-sm` (6px dots)  |
| `default` | `dot-loader` (8px dots)     |
| `lg`      | `dot-loader-lg` (12px dots) |

### Vanilla CSS

```css
.dot-loader {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.dot-loader span {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  animation: dot-bounce 1.6s ease-in-out infinite;
}
.dot-loader span:nth-child(1) {
  background: var(--primary);
  animation-delay: 0s;
}
.dot-loader span:nth-child(2) {
  background: var(--secondary);
  animation-delay: 0.2s;
}
.dot-loader span:nth-child(3) {
  background: var(--accent);
  animation-delay: 0.4s;
}
.dot-loader-sm span {
  width: 6px;
  height: 6px;
}
.dot-loader-lg span {
  width: 12px;
  height: 12px;
}
.dot-loader-solid span {
  background: var(--fg);
}
.dot-loader-pink span {
  background: var(--primary);
}
.dot-loader-pink span:nth-child(2) {
  background: color-mix(in srgb, var(--primary) 70%, transparent);
}
.dot-loader-pink span:nth-child(3) {
  background: color-mix(in srgb, var(--primary) 40%, transparent);
}

@keyframes dot-bounce {
  0%,
  80%,
  100% {
    transform: translateY(0);
    opacity: 0.4;
  }
  40% {
    transform: translateY(-8px);
    opacity: 1;
  }
}
```

### HTML Usage

```html
<!-- Gradient (default) -->
<div class="dot-loader"><span></span><span></span><span></span></div>

<!-- Solid -->
<div class="dot-loader dot-loader-solid">
  <span></span><span></span><span></span>
</div>

<!-- Single color -->
<div class="dot-loader dot-loader-pink">
  <span></span><span></span><span></span>
</div>

<!-- Sizes -->
<div class="dot-loader dot-loader-sm">
  <span></span><span></span><span></span>
</div>
<div class="dot-loader"><span></span><span></span><span></span></div>
<div class="dot-loader dot-loader-lg">
  <span></span><span></span><span></span>
</div>

<!-- Inline -->
<span
  >Loading
  <div class="dot-loader" style="margin-left: 0.4rem; vertical-align: middle;">
    <span></span><span></span><span></span></div
></span>
```

---

## Bar Loader

### Sizes

| Size      | Class                            |
| --------- | -------------------------------- |
| `sm`      | `bar-loader-sm` (32px, 3px bars) |
| `default` | `bar-loader` (48px, 4px bars)    |
| `lg`      | `bar-loader-lg` (64px, 6px bars) |

Five-bar gradient: primary → primary/secondary blend → secondary → secondary/accent blend → accent. Stagger: 0s → 0.15s → 0.3s → 0.45s → 0.6s.

### Vanilla CSS

```css
.bar-loader {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  width: 48px;
}
.bar-loader span {
  width: 80%;
  height: 4px;
  border-radius: 2px;
  animation: bar-slide 3s ease-in-out infinite;
}
.bar-loader span:nth-child(1) {
  background: var(--primary);
  animation-delay: 0s;
}
.bar-loader span:nth-child(2) {
  background: color-mix(in srgb, var(--primary), var(--secondary));
  animation-delay: 0.15s;
}
.bar-loader span:nth-child(3) {
  background: var(--secondary);
  animation-delay: 0.3s;
}
.bar-loader span:nth-child(4) {
  background: color-mix(in srgb, var(--secondary), var(--accent));
  animation-delay: 0.45s;
}
.bar-loader span:nth-child(5) {
  background: var(--accent);
  animation-delay: 0.6s;
}
.bar-loader-sm {
  width: 32px;
}
.bar-loader-sm span {
  height: 3px;
}
.bar-loader-lg {
  width: 64px;
}
.bar-loader-lg span {
  height: 6px;
  border-radius: 3px;
}

@keyframes bar-slide {
  0%,
  100% {
    transform: scaleX(0.3);
    opacity: 0.4;
  }
  50% {
    transform: scaleX(1);
    opacity: 1;
  }
}
```

### HTML Usage

```html
<div class="bar-loader">
  <span></span><span></span><span></span><span></span><span></span>
</div>
<div class="bar-loader bar-loader-sm">
  <span></span><span></span><span></span><span></span><span></span>
</div>
<div class="bar-loader bar-loader-lg">
  <span></span><span></span><span></span><span></span><span></span>
</div>
```

---

## Vertical Bar Loader

### Sizes

| Size      | Class                                     |
| --------- | ----------------------------------------- |
| `sm`      | `bar-loader-vertical-sm` (32px, 3px bars) |
| `default` | `bar-loader-vertical` (48px, 4px bars)    |
| `lg`      | `bar-loader-vertical-lg` (64px, 6px bars) |

Same five-bar gradient as Bar Loader but vertical bars side-by-side with scaleY animation. Stagger: 0s → 0.15s → 0.3s → 0.45s → 0.6s.

### Vanilla CSS

```css
.bar-loader-vertical {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 4px;
  height: 48px;
}
.bar-loader-vertical span {
  width: 4px;
  height: 80%;
  border-radius: 2px;
  animation: bar-slide-vertical 3s ease-in-out infinite;
}
.bar-loader-vertical span:nth-child(1) {
  background: var(--primary);
  animation-delay: 0s;
}
.bar-loader-vertical span:nth-child(2) {
  background: color-mix(in srgb, var(--primary), var(--secondary));
  animation-delay: 0.15s;
}
.bar-loader-vertical span:nth-child(3) {
  background: var(--secondary);
  animation-delay: 0.3s;
}
.bar-loader-vertical span:nth-child(4) {
  background: color-mix(in srgb, var(--secondary), var(--accent));
  animation-delay: 0.45s;
}
.bar-loader-vertical span:nth-child(5) {
  background: var(--accent);
  animation-delay: 0.6s;
}
.bar-loader-vertical-sm {
  height: 32px;
}
.bar-loader-vertical-sm span {
  width: 3px;
}
.bar-loader-vertical-lg {
  height: 64px;
}
.bar-loader-vertical-lg span {
  width: 6px;
  border-radius: 3px;
}

@keyframes bar-slide-vertical {
  0%,
  100% {
    transform: scaleY(0.3);
    opacity: 0.4;
  }
  50% {
    transform: scaleY(1);
    opacity: 1;
  }
}
```

### HTML Usage

```html
<div class="bar-loader-vertical">
  <span></span><span></span><span></span><span></span><span></span>
</div>
<div class="bar-loader-vertical bar-loader-vertical-sm">
  <span></span><span></span><span></span><span></span><span></span>
</div>
<div class="bar-loader-vertical bar-loader-vertical-lg">
  <span></span><span></span><span></span><span></span><span></span>
</div>
```
