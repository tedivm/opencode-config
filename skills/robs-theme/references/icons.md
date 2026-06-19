# Tabler Icons Reference

## Library Overview

|            |                                        |
| ---------- | -------------------------------------- |
| Name       | Tabler Icons                           |
| License    | MIT                                    |
| Repository | https://github.com/tabler/tabler-icons |
| Icon count | 6146+ (outline + filled)               |
| Format     | SVG (inline), icon font (optional)     |
| Grid       | 24×24, 2px stroke default              |
| Website    | https://tabler.io/icons                |

## Props / API

| Prop     | Type   | Default   | Description                                    |
| -------- | ------ | --------- | ---------------------------------------------- |
| `size`   | number | 24        | Icon size in pixels (12, 16, 24, 32, 48)       |
| `stroke` | number | 2         | Stroke width (0.5 to 3)                        |
| `color`  | string | —         | CSS color or variable (e.g., `var(--primary)`) |
| `type`   | string | "outline" | Icon variant: "outline" or "filled"            |

## Vanilla HTML Usage

### Option 1: Inline SVG

Copy SVG markup directly from tabler.io/icons. Icons inherit `currentColor` so they pick up the parent text color automatically. To use theme colors, set `stroke="var(--primary)"` on the SVG element.

```html
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
  <path d="M12 8v4" />
  <path d="M12 16h.01" />
</svg>
```

### Option 2: Iconfont (self-hosted or CDN)

Download the webfont CSS and font files from the `@tabler/icons-webfont` package and serve them locally.

**CDN alternative** (acceptable for quick prototypes):

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css"
/>
<i class="ti ti-alert-circle"></i>
```

## Svelte 5 Usage

```bash
npm install @tabler/icons-svelte-runes
```

```svelte
<script>
  import IconHeart from '@tabler/icons-svelte-runes/icons/heart';
</script>

<IconHeart size={24} stroke={2} />
```

Import pattern: `@tabler/icons-svelte-runes/icons/{kebab-case-name}`

Icon component names use PascalCase: `IconInfoCircle`, `IconArrowRight`, etc.

## CSS for Icon Showcase Pages

Use these classes when building icon showcase or documentation pages.

```css
.icon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.icon-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 0.75rem;
  background: var(--surface);
  border-radius: 5px;
  border: 1px solid var(--border);
}

.icon-cell svg {
  color: var(--fg);
}

.icon-cell .icon-name {
  font-family: "Source Code Pro", "Roboto Mono", monospace;
  font-size: 0.7rem;
  color: var(--muted);
  text-align: center;
  word-break: break-all;
}

.icon-sizes {
  display: flex;
  align-items: flex-end;
  gap: 1.5rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.icon-size-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
}

.icon-size-cell span {
  font-size: 0.7rem;
  color: var(--muted);
  font-family: "Source Code Pro", monospace;
}

.icon-weights {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.icon-weight-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
}

.icon-weight-cell span {
  font-size: 0.7rem;
  color: var(--muted);
  font-family: "Source Code Pro", monospace;
}

.icon-colors {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.icon-color-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
}

.icon-color-cell span {
  font-size: 0.7rem;
  color: var(--muted);
  font-family: "Source Code Pro", monospace;
}

.icon-stroke {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.icon-stroke-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
}

.icon-stroke-cell span {
  font-size: 0.7rem;
  color: var(--muted);
  font-family: "Source Code Pro", monospace;
}
```

## Common Icon Names

### UI & Navigation

home, pencil, mail, package, search, circle-plus, info-circle, circle-x

### Actions & Status

arrow-right, user, alert-circle, circle-check, alert-triangle, bell, settings
