---
name: robs-design
description: "Use when designing software architecture or new features: producing technical design documents with model definitions, service code, API contracts, migration strategies, and testing plans. Works alongside OpenSpec proposals or stands alone for feature design. This is NOT the `design.md` UI design system format (colors, typography, components) — this is purely for engineering architecture documentation."
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

Every `design.md` is a comprehensive technical document that an implementer can follow without guessing. It includes full model definitions, complete service code, API contracts, migration order, testing strategy, documentation plan, and risk analysis. The implementer should never need to ask "what does this look like?"

## Document structure

Write the document in this exact order. Omit sections that don't apply.

1. **`# Design: <name>`** — Title line with change name and brief scope
2. **`## Context`** — Current state, existing conventions, what this builds on
3. **`## Goals / Non-Goals`** — Two subsections: `**Goals:**` (bulleted) and `**Non-Goals:**` (bulleted)
4. **`## Decisions`** — Numbered decisions (D1, D2, ...) with full code
5. **`## Data Storage`** — Full model/entity definitions for every new or changed persistence structure
6. **`## Data Structures`** — Input and output schema definitions
7. **`## Interfaces`** — All user-facing interfaces: REST APIs, CLI commands, MCP tools, TUI screens, GUI components
8. **`## Implementation Detail`** — Full service code, background tasks, CLI, settings
9. **`## Migrations`** — Creation order, dependencies, compatibility notes
10. **`## Testing Philosophy`** — Prose sections (not bullets) per test area
11. **`## Documentation Plan`** — Prose sections (not tables) per doc file
12. **`## Risks / Trade-offs`** — Prose sections with **Risk:** and **Mitigation:** paragraphs

### Context example

```markdown
## Context

The project has infrastructure scaffolding (FastAPI, async SQLAlchemy 2.0, Celery, Docker Compose) but zero domain functionality. No models, no routes, no business logic. This design establishes the first complete data flow.

The architecture follows the existing template's conventions: async SQLAlchemy with `mapped_column`, Pydantic v2 settings, Typer CLI with `@syncify`, and the router pattern for FastAPI.
```

### Goals / Non-Goals example

```markdown
## Goals / Non-Goals

**Goals:**

- 7 domain models with migration
- URL normalization for source uniqueness
- Global article deduplication by URL
- Feed fetching service using `feedparser` + `httpx`
- REST API: CRUD for sources, list/detail for articles
- CLI commands: `fetch` and `seed`
- Settings: `default_fetch_interval`, `feed_fetch_timeout`

**Non-Goals:**

- User authentication, reactions, or preferences (Phase 2)
- AI summaries, embeddings, breaking news (Phase 3)
- Per-source fetch intervals — global default only
- Translation logic (structural placeholder only)
- Frontend, MCP server (future phases)
```

## Decision format

Each decision is a numbered subsection: `### D1: <name>`, `### D2: <name>`, etc.

Every decision must include:

1. **Decision statement** — What was chosen and why, in prose
2. **Code** — Full, working code. Not pseudocode. Not stubs. Include file path comments (`# package/module/file.py`)
3. **Alternatives considered** — `**Alternative considered:**` followed by what was rejected and why
4. **Rationale** — Inline prose explaining the choice
5. **Trade-offs** — Note any downsides, deferred work, or future migration needs

Decisions are separated by `---` (horizontal rule).

### Decision example — with code

````markdown
### D1: URL normalization with `yarl`

**Decision:** Source URLs are normalized before storage and uniqueness checks using `yarl.URL`. Normalization: lowercase scheme and host, strip trailing path slashes, remove default ports (`:80` for HTTP, `:443` for HTTPS), drop query and fragment.

```python
# package/services/feed.py
from yarl import URL


def normalize_url(raw: str) -> str:
    """Normalize a feed URL for consistent storage and deduplication."""
    url = URL(raw)
    if (url.scheme == "http" and url.port == 80) or (url.scheme == "https" and url.port == 443):
        url = url.with_port(None)
    path = url.path.rstrip("/") or "/"
    return str(url.with_path(path).with_query(None).with_fragment(None))
```
````

`yarl` is chosen over `urllib.parse` because it provides an immutable URL object with clean manipulation methods and handles edge cases (Unicode domains, IPv6 literals) that manual parsing would miss.

**Alternative considered:** `urllib.parse.urlparse` (stdlib). Rejected — requires manual reassembly, more error-prone for edge cases.

### Decision example — architecture (no code)

```markdown
### D2: In-memory state only for Phase 1

**Choice:** Player state is a Python dataclass held in memory for the duration of a session. It is not persisted between sessions.

**Alternatives considered:**

- Database persistence from day one: locks us into a schema before we understand the full shape of state.
- JSON file storage: commits to a serialization format prematurely.

**Rationale:** We cannot design the DB schema without knowing the full shape of state first. Building the in-memory model first validates the data model before committing it to migrations.
```

## Code-level detail requirements

### Data Storage models

Write the complete class/structure with every field:

- Identity: `id` as `Mapped[UUID]` with `primary_key=True, default=uuid4` (or equivalent)
- References: all foreign key / reference columns with appropriate cascade behavior
- Timestamps: `created_at` / `updated_at` with `DateTime(timezone=True)`
- Constraints: `UniqueConstraint` in `__table_args__` when composite uniqueness is needed
- Docstrings: explaining purpose and any future-expansion notes

Do not defer FK constraints to "later" unless the referenced table genuinely doesn't exist yet. If a FK target doesn't exist, create the column as a plain nullable `UUID` with a `comment` noting the future FK.

**See [references/sqlalchemy-models.md](references/sqlalchemy-models.md) for relational model examples.**
**See [references/in-memory-models.md](references/in-memory-models.md) for dataclass and in-memory examples.**

### Data Structures

Write complete input and output schemas. Separate input from output — never reuse the same model for both. Include `Field(...)` with `description` and `default`/`optional` annotations.

```python
# package/schemas/source.py
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID


class SourceCreate(BaseModel):
    url: str = Field(
        description="Feed URL. Will be normalized before storage.",
        examples=["https://feeds.example.com/rss"],
    )
    name: str | None = Field(
        default=None,
        description="Optional display name. Derived from feed on first fetch if omitted.",
    )


class SourceRead(BaseModel):
    id: UUID = Field(description="Unique identifier.")
    url: str = Field(description="Normalized URL.")
    name: str | None = Field(description="Display name.")
    is_default: bool = Field(description="Whether this is a built-in default source.")
    added_at: datetime = Field(description="When the source was added.")
    last_fetched_at: datetime | None = Field(
        default=None,
        description="When the source was last successfully fetched.",
    )
```

For complex discriminated unions (condition trees, step types, event types), use Pydantic's `Annotated[Union[...], Field(discriminator="type")]` pattern.

**See [references/pydantic-schemas.md](references/pydantic-schemas.md) for schema patterns and discriminated unions.**

### Service classes

Write the complete class with all methods:

- Constructor with configuration from settings
- Core business logic methods (upsert, fetch, parse, etc.)
- Helper methods (`_extract_*`, `_parse_*`, `_detect_*`)
- Custom exception classes
- Error handling and logging

Include the full method body — not just signatures. Every public method gets a docstring. Use `logger.getLogger(__name__)` for logging.

### Background tasks

Use a `_syncify` pattern to bridge async service code from sync task runners. Never scatter `asyncio.run()` through task bodies — define a `_syncify` wrapper and thin sync helpers for cache/DB operations.

Structure: `_syncify` function + sync cache/DB wrappers + `async def _impl(...)` + `@celery.task` decorated sync entry point that calls `_syncify(_impl)`.

**See [references/celery-tasks.md](references/celery-tasks.md) for full task patterns.**

### CLI commands

Show the full command function with the sync bridge decorator (`@syncify`).

**See [references/typer-cli.md](references/typer-cli.md) for CLI command patterns.**

### Settings

Show the exact `Field(...)` definitions with `default` and `description`:

```python
# package/conf/settings.py
default_fetch_interval: int = Field(
    default=30,
    description="Interval in minutes between automatic fetches.",
)
feed_fetch_timeout: int = Field(
    default=30,
    description="Timeout in seconds for individual HTTP requests.",
)
```

### Interfaces

Document every user-facing interface. Use tables or structured lists for each interface area. Include error responses.

The Interfaces section covers all applicable types — use the table/list format appropriate to each:

- **REST APIs** — Method, path, request, response, description + error response table
- **CLI commands** — Command name, arguments, description, exit codes
- **MCP tools** — Tool name, parameters, return type, description
- **TUI screens** — Screen name, options, navigation
- **GUI components** — Component name, properties, events

```markdown
### REST API — Sources

| Method | Path            | Request        | Response       | Description         |
| ------ | --------------- | -------------- | -------------- | ------------------- |
| `GET`  | `/sources`      | —              | `SourceRead[]` | List all sources    |
| `POST` | `/sources`      | `SourceCreate` | `SourceRead`   | Create a new source |
| `GET`  | `/sources/{id}` | —              | `SourceRead`   | Get source by ID    |

### CLI Commands

| Command | Arguments | Description                    |
| ------- | --------- | ------------------------------ |
| `fetch` | —         | Trigger a fetch of all sources |
| `seed`  | —         | Seed default sources           |

### MCP Tools

| Tool           | Parameters | Returns        | Description      |
| -------------- | ---------- | -------------- | ---------------- |
| `list_sources` | —          | `SourceRead[]` | List all sources |
```

**See [references/fastapi-routes.md](references/fastapi-routes.md) for REST endpoint patterns.**
**See [references/typer-cli.md](references/typer-cli.md) for CLI command patterns.**

### Accessibility

Every user-facing interface requires an accessibility section. Use `## Accessibility` as a top-level section after `## Interfaces`. Cover each interface type with actionable requirements, not aspirational language.

```markdown
## Accessibility

### Visual Design

- **Color contrast:** All text meets WCAG 2.1 AA minimum contrast ratios (4.5:1 for normal text, 3:1 for large text and UI components). Verify with automated tools during development.
- **Color as the only indicator:** No information conveyed by color alone. Status indicators include icons, text labels, or patterns in addition to color.
- **Focus indicators:** All interactive elements have visible focus indicators with sufficient contrast against their background. Do not remove or style `outline: none` without providing an alternative.
- **Motion and animation:** Respect `prefers-reduced-motion`. Disable non-essential animations when the user's OS preference is set. Provide static fallbacks.

### Screen Reader Support

- **Semantic HTML:** Use native elements (`<button>`, `<nav>`, `<main>`, `<header>`) over generic `<div>` wrappers. Apply ARIA roles only when native semantics are insufficient.
- **Labels and descriptions:** Every interactive element has an accessible name. Use `aria-label`, `aria-labelledby`, or visible labels — never rely on placeholder text alone.
- **Live regions:** Dynamic content updates (notifications, data loading, errors) use `aria-live` regions with appropriate politeness (`polite` for updates, `assertive` for errors).
- **Status messages:** Form validation, success confirmations, and error states are announced to screen readers via `role="alert"` or `aria-live` regions.

### Keyboard Navigation

- **Complete keyboard access:** Every interactive function is operable using keyboard alone. No keyboard traps — users can tab forward and backward through all elements.
- **Logical tab order:** Tab order follows visual reading order. Use DOM order rather than `tabindex` positive values. Skip links provide navigation past repeated content.
- **Custom keyboard shortcuts:** If shortcuts exist, they are documented, configurable, and do not conflict with browser or screen reader shortcuts. Provide visual indicators of active shortcuts.

### TUI-Specific Requirements

- **Terminal color support:** Use ANSI color codes that work on both light and dark terminal backgrounds. Do not assume a specific terminal theme.
- **Braille display compatibility:** Ensure text output does not rely on Unicode graphics characters (block elements, drawings) for conveying information. Provide fallback text.
- **Resize behavior:** The interface degrades gracefully when the terminal is resized. Content reflows or truncates without breaking layout.

### CLI-Specific Requirements

- **Help text:** Every command and flag has descriptive help text accessible via `--help`. Output is parseable and readable without color.
- **Error messages:** Errors include actionable guidance, not just codes. Messages are descriptive enough for users who cannot see color-coded output.
- **Structured output:** Support `--json` or similar flags for machine-readable output, enabling integration with assistive tools.

### Forms and Input

- **Field association:** Labels are programmatically associated with inputs via `for`/`id` pairing. Group related fields with `fieldset` and `legend`.
- **Error identification:** Errors identify the specific field, describe the problem in plain language, and suggest corrections. Use `aria-invalid` and `aria-describedby` for programmatic association.
- **Autofill support:** Use appropriate `autocomplete` attributes to assist password managers and form-filling tools.
```

**Checklist for every interface:**

- Does it work with keyboard-only navigation?
- Is all information accessible without color?
- Are dynamic updates announced to assistive technology?
- Does it respect `prefers-reduced-motion`?
- Are error messages descriptive and actionable?

## Prose formatting rules

### Risks / Trade-offs

Use subsection headers, not tables. Each risk gets its own `### <name>` section with two bold-labeled paragraphs:

```markdown
## Risks / Trade-offs

### Large feeds overwhelming the worker

**Risk:** Feeds with 1000+ entries can hold the lock for a long time, blocking the next scheduled cycle and delaying all other sources.

**Mitigation:** `feed_fetch_timeout` limits the HTTP fetch time. If needed in the future, chunked processing or per-entry timeouts can be added.

### Partial processing on crash

**Risk:** `session.commit()` is called after all entries are processed. If the task crashes mid-feed, the transaction rolls back — no partial data, but all work on that feed is lost.

**Mitigation:** The next fetch retry processes the full feed again. Guarantees consistency — no orphaned or half-processed records.
```

### Testing Philosophy

Use subsection headers, not bullet lists. Each test area gets its own `### <area>` section with a prose paragraph:

```markdown
## Testing Philosophy

### URL normalization

Verify each normalization rule independently: lowercase scheme and host, trailing slash removal, default port stripping, query and fragment removal. Test edge cases including IPv6 literals, Unicode domains, and malformed URLs.

### Upsert behavior

Fetch the same feed twice and verify that the record is updated (title, published_at, fetched_at) rather than duplicated, and that content is updated in place. Confirm the unique constraint prevents duplicates.

### Background task behavior

Mock the service to verify that the periodic task iterates all sources, handles per-source failures without stopping the cycle, and respects the lock for overlap prevention. Verify the manual task handles missing IDs.
```

### Documentation Plan

Use subsection headers, not tables. Each doc file gets its own `### <file path>` section with an audience line and full paragraph:

```markdown
## Documentation Plan

### `docs/dev/api.md`

**Audience:** Developers

Document all new endpoints: sources CRUD, article listing and detail, pagination parameters, error responses, and the paginated response shape. Include the request/response models and example curl commands.

### `docs/dev/celery.md`

**Audience:** Developers

Document the periodic task (scheduling, lock for overlap prevention) and manual task. Cover the `_syncify` bridge pattern for running async service code from sync task runners. Include the lock key format and TTL behavior.
```

## Architecture review and changes

**Before writing the design, always check if `docs/dev/architecture.md` exists in the project.** If it does, read it in full. The existing architecture document is your primary source of truth for how the system is currently structured — understanding it is essential before making any design decisions. Note existing conventions, patterns, component boundaries, and technology choices.

After reviewing, include a dedicated subsection in the design documenting any changes needed to the architecture file:

```markdown
### `docs/dev/architecture.md` changes

List every section of the architecture document that needs to be updated, added, or removed. Include the exact prose or diagrams that should be inserted.

Examples:

- New component added to the high-level diagram
- New data flow between existing services
- Changed deployment topology
- Updated technology choices or conventions
```

If the file does not exist, note this explicitly: "No `docs/dev/architecture.md` exists in the project."

## Structural discipline

- **No fake or placeholder population code.** If a table is a structural placeholder for a future phase, the model exists but the service does NOT write to it. Document this explicitly: "Structural placeholder for future use. Not populated in this phase."

- **Build for the future, not just now.** If a column will be needed later, include it. If a constraint will need to support 1:N later, design it that way now (e.g., `UniqueConstraint(article_id, language)` instead of `unique=True` on `article_id`).

- **Every decision needs alternatives.** If there was only one choice, say so: "No meaningful alternative — this is the standard approach."

- **Code must be implementer-ready.** The implementer should be able to copy-paste with minimal adjustment. File paths, imports, type hints, docstrings — all present.

- **Separate input from output schemas.** Never reuse the same model for both creation and reading. `SourceCreate` ≠ `SourceRead`.

- **The implementer can work from the design alone.** No cross-referencing to the proposal, no guessing at shapes, no wondering about error codes. Everything needed is in the design.

## Advanced features

Library-specific reference files — load these when writing the corresponding sections of your design:

- **SQLAlchemy models**: [references/sqlalchemy-models.md](references/sqlalchemy-models.md)
- **Pydantic schemas**: [references/pydantic-schemas.md](references/pydantic-schemas.md)
- **FastAPI routes**: [references/fastapi-routes.md](references/fastapi-routes.md)
- **Typer CLI**: [references/typer-cli.md](references/typer-cli.md)
- **Celery tasks**: [references/celery-tasks.md](references/celery-tasks.md)
- **In-memory models**: [references/in-memory-models.md](references/in-memory-models.md)
- **Discriminated unions**: [references/discriminated-unions.md](references/discriminated-unions.md)
