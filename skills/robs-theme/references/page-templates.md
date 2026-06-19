# Page Templates

Page templates for Rob's Style Guide. Use these as starting points when creating new pages in any implementation system.

## Common Patterns

All pages share these structural elements:

- **`<h1>`** — page title rendered in primary pink color
- **`.subtitle`** — paragraph immediately below the title with page description
- **`.toolbar`** — div containing the theme toggle button and navigation links
- **`.back-link`** — link for navigation back to parent or home page
- **Theme toggle** — script at the bottom of the body (vanilla) or in `onMount` (Svelte)

## Vanilla HTML Page

Main style guide page template. Zero dependencies, no build tools required.

**Fonts:** Download the font files and serve them locally using `@font-face`. For quick prototypes, you can use the Google Fonts CDN instead.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width"
      ="device-width,"
      initial-scale="1.0"
    />
    <title>Page Title</title>
    <!-- Self-hosted fonts (preferred) or use Google Fonts CDN: -->
    <!-- <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto+Slab:wght@400;700&family=Source+Code+Pro:wght@400;700&family=Source+Serif+4:wght@400;600;700&display=swap" rel="stylesheet"> -->
    <link rel="stylesheet" href="./theme.css" />
  </head>
  <body>
    <h1>Page Title</h1>
    <p class="subtitle">Page description</p>

    <div class="toolbar">
      <button class="theme-toggle" id="theme-toggle" title="Toggle Light Mode">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2" />
          <path d="M12 20v2" />
          <path d="m4.93 4.93 1.41 1.41" />
          <path d="m17.66 17.66 1.41 1.41" />
          <path d="M2 12h2" />
          <path d="M20 12h2" />
          <path d="m6.34 17.66-1.41 1.41" />
          <path d="m19.07 4.93-1.41 1.41" />
        </svg>
      </button>
      <a href="../" class="back-link">← Home</a>
    </div>

    <!-- Content here -->

    <script>
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
    </script>
  </body>
</html>
```

## Vanilla Prism Page

Code highlighting page with Prism.js. **Download Prism locally** (preferred) or use CDN for quick prototypes. Includes re-highlighting on theme toggle.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width"
      ="device-width,"
      initial-scale="1.0"
    />
    <title>Code Highlighting</title>
    <!-- Self-hosted fonts (preferred) or use Google Fonts CDN: -->
    <!-- <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto+Slab:wght@400;700&family=Source+Code+Pro:wght@400;700&family=Source+Serif+4:wght@400;600;700&display=swap" rel="stylesheet"> -->
    <link rel="stylesheet" href="./theme.css" />
    <style>
      /* Prism custom CSS here (see prism-theme.md) */
    </style>
  </head>
  <body>
    <h1>Code Highlighting</h1>
    <p class="subtitle">Description</p>

    <div class="toolbar">
      <button class="theme-toggle" id="theme-toggle" title="Toggle Light Mode">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2" />
          <path d="M12 20v2" />
          <path d="m4.93 4.93 1.41 1.41" />
          <path d="m17.66 17.66 1.41 1.41" />
          <path d="M2 12h2" />
          <path d="M20 12h2" />
          <path d="m6.34 17.66-1.41 1.41" />
          <path d="m19.07 4.93-1.41 1.41" />
        </svg>
      </button>
      <a href="./index.html" class="back-link">← Back</a>
    </div>

    <!-- Code blocks with class="language-xxx" -->

    <!-- Self-hosted Prism (preferred): -->
    <!-- <script src="./prism/prism.min.js"></script> -->
    <!-- <script src="./prism/components/prism-json.min.js"></script> -->
    <!-- CDN alternative: -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
    <!-- ... other language components ... -->
    <script>
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

        // Re-highlight on theme toggle since CSS variables change
        if (typeof Prism !== "undefined") {
          setTimeout(Prism.highlightAll, 50);
        }
      });
      if (typeof Prism !== "undefined") {
        Prism.highlightAll();
      }
    </script>
  </body>
</html>
```

## Landing Page

Entry point that links to each implementation system. Uses card grid layout with badges.

**Fonts:** Download and self-host (preferred) or use Google Fonts CDN for quick prototypes.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width"
      ="device-width,"
      initial-scale="1.0"
    />
    <title>Rob's Style Guide</title>
    <!-- Self-hosted fonts (preferred) or use Google Fonts CDN: -->
    <!-- <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Roboto+Slab:wght@400;700&family=Source+Code+Pro:wght@400;700&family=Source+Serif+4:wght@400;600;700&display=swap" rel="stylesheet"> -->
    <link rel="stylesheet" href="./vanilla/theme.css" />
  </head>
  <body>
    <h1>Rob's Style Guide</h1>
    <p class="subtitle">
      Shared design system across implementation frameworks
    </p>

    <div class="toolbar">
      <button class="theme-toggle" id="theme-toggle" title="Toggle Light Mode">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle cx="12" cy="12" r="4" />
          <path d="M12 2v2" />
          <path d="M12 20v2" />
          <path d="m4.93 4.93 1.41 1.41" />
          <path d="m17.66 17.66 1.41 1.41" />
          <path d="M2 12h2" />
          <path d="M20 12h2" />
          <path d="m6.34 17.66-1.41 1.41" />
          <path d="m19.07 4.93-1.41 1.41" />
        </svg>
      </button>
    </div>

    <h2>Systems</h2>
    <div class="grid grid-2">
      <div class="card">
        <a class="card-link" href="./vanilla/index.html">
          <div class="card-header">System Name</div>
          <div class="card-body">Description.</div>
          <div class="card-meta"><span class="badge badge-app">Tag</span></div>
        </a>
      </div>
    </div>

    <script>
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
    </script>
  </body>
</html>
```

## Svelte Page (App.svelte)

Svelte 5 runes-based page component. Uses `onMount` for theme detection and inline styles scoped to the component.

```svelte
<script>
  import './theme.css';
  import { onMount } from 'svelte';
  import { IconSun, IconMoon } from '@tabler/icons-svelte';
  let dark = $state(true);

  function toggle() {
    dark = !dark;
    document.documentElement.classList.toggle('light', !dark);
  }

  onMount(() => {
    if (window.matchMedia('(prefers-color-scheme: light)').matches) {
      dark = false;
      document.documentElement.classList.add('light');
    }
  });
</script>

<div class="container">
  <h1>Page Title</h1>
  <p class="subtitle">Description</p>

  <div class="toolbar">
    <button class="theme-toggle" onclick={toggle} title={dark ? 'Toggle Light Mode' : 'Toggle Dark Mode'}>
      {#if dark}
        <IconSun size={18} />
      {:else}
        <IconMoon size={18} />
      {/if}
    </button>
    <a href="../" class="back-link">← Home</a>
  </div>

  <!-- Content here -->
</div>

<style>
  .container { max-width: 900px; }

  .theme-toggle {
    background: var(--accent-15);
    color: var(--accent);
    border: 1px solid var(--accent);
    border-radius: var(--radius);
    padding: 0.4rem;
    cursor: pointer;
    font-family: inherit;
    font-size: 0.85rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .theme-toggle:hover {
    background: var(--accent-30);
  }
  .theme-toggle svg {
    filter: drop-shadow(0 0 6px color-mix(in srgb, var(--accent) 70%, transparent)) drop-shadow(0 0 14px color-mix(in srgb, var(--accent) 40%, transparent));
  }

  :global(.light) .theme-toggle {
    background: var(--secondary-15);
    color: var(--secondary);
    border-color: var(--secondary);
  }
  :global(.light) .theme-toggle:hover {
    background: var(--secondary-30);
  }
  :global(.light) .theme-toggle svg {
    filter: drop-shadow(0 0 6px color-mix(in srgb, var(--secondary) 70%, transparent)) drop-shadow(0 0 14px color-mix(in srgb, var(--secondary) 40%, transparent));
  }

  /* ... styles from the skill references ... */
</style>
```
