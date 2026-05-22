---
name: bootstrapping-plan
description: Use when bootstrapping the design of a brand new project — producing a plan.md through iterative exploration. Don't use for modifying existing plans, implementing features, or working with established codebases.
license: MIT
metadata:
  author: Robert Hafner
  source: https://github.com/tedivm/opencode-config
---

## Quick start

When a user wants to design a new project from scratch, guide them through an iterative exploration that produces a `plan.md` in `./tmp/`. The plan captures vision, architecture, feature requirements, data model, technology stack, implementation phases, and open questions.

## Workflow

1. **Read the existing codebase skeleton** — Understand existing structure, dependencies, Docker setup, and template conventions. This grounds the plan in reality.

2. **Initial exploration** — Read the user's requirements (bullet points, feature list). Identify vague areas that need clarification.

3. **Think through architecture** — Visualize the system. Identify tension points, unclear requirements, and key design decisions. Present an ASCII/mermaid diagram.

4. **Ask focused questions** — Surface ambiguities. Group related questions. Present options where relevant. Wait for answers before proceeding.

5. **Draft the plan** — Create `./tmp/plan.md` with all sections (see template below).

6. **Iterate** — As the user corrects, refines, or adds to the plan, update it in place. Each iteration should improve accuracy without losing previous work.

## Plan Structure

The plan.md must contain these sections in order:

### 1. Vision

One paragraph describing what the project is and what it does.

### 2. Core Architecture

Mermaid diagram showing all interfaces, service layers, and data stores. Rules:

- All interfaces (web frontend, API, CLI, MCP, workers) are peers — none sits in front of another
- Python-native interfaces (FastMCP, CLI, Celery) bypass the REST layer and call the service layer directly
- Web frontends talk through the REST API
- Service layer is the single source of truth for data access
- Use `graph LR` with `subgraph` groupings for External, Application, Compute, Data

### 3. Feature Requirements

Numbered sections for each major feature area. Each section:

- Bullet points of specific behaviors
- Clear scope boundaries
- Notes on what's TBD vs decided

### 4. Data Model (Conceptual)

Mermaid ER diagram with:

- All entities with their fields
- UUID primary keys (not integers)
- Relationships between entities
- Content stored separately from metadata when performance matters
- Use `erDiagram` syntax

### 5. Technology Stack

Bullet list of technologies with their roles. Mark TBD items clearly.

### 6. Implementation Phases

Numbered phases in logical order. Each phase: name + brief description.

### 7. Open Questions

Unresolved decisions that need answers before implementation begins.

## Iteration Patterns

As the user refines the plan, expect these common corrections:

- **Architecture corrections** — Interfaces that should be peers, not gateways
- **Diagram format** — ASCII to mermaid, or mermaid syntax fixes
- **Data model additions** — New entities, relationships, fields
- **Key type decisions** — UUIDs vs integers (default to UUIDs)
- **Separation concerns** — Content vs metadata, caching vs storage
- **Feature scope** — Adding/removing capabilities

Each correction is a surgical edit to the plan — don't rewrite sections that haven't changed.

## Key Principles

- **Explore, don't implement** — This is design time. No code, no features, just planning.
- **Visual first** — Diagrams reveal problems text hides. Use mermaid for all diagrams.
- **Iterative refinement** — The first draft is intentionally incomplete. Expect 5-15 rounds of corrections.
- **Ground in reality** — Reference the actual codebase template, existing dependencies, and conventions.
- **Capture everything** — The plan is the source of truth for what gets built. Ambiguity here becomes technical debt there.
