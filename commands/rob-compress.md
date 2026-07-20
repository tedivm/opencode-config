---
description: Compress the conversation intelligently
---

# Compression

Compress the current conversation to free up context. Summarize related sections together while preserving important messages.

## Rules

- **IDs are stable.** Compressing a range replaces those messages with a `(bN)` placeholder but leaves all other message IDs unchanged. You can compress in any order or batch multiple ranges in one call.
- **Group related messages.** Wrap adjacent messages that cover the same topic into a single batch. - **Remove Waste.** Only compress single, isolated messages when they are pure noise or are very large with unnecessary content.
- **Leave important messages alone.** Do not compress:
  - User messages that state requirements, give approval, or set constraints
  - Error messages or tool outputs you may need to reference
  - The most recent messages, as they provide context for the current conversations
- **Use the `compress` tool.** Call it with a `topic` and one or more `content` entries (each with `startId`, `endId`, `summary`). Batch multiple independent ranges in a single call as long as their boundaries do not overlap.

## Summary Instructions

- **Make summaries exhaustive.** Each summary must be technically complete and replace the original content faithfully enough that nothing essential is lost. It should include items such as (but not limited to):
  - Demands made by the user
  - Decisions made
  - Decisions left unmade
  - File paths and function signatures
  - Constraints discovered
  - Key findings
  - Third party sources referenced
  - Compromises that occurred
- **Be lean.** Strip failed attempts, verbose tool output, and back-and-forth exploration. Keep the signal, discard the noise.

## Process

1. Scan the full conversation and identify sections that are "done" — research concluded, implementation verified, dead-end noise.
2. Group adjacent, related messages into batches. Note each batch's `startId` and `endId`.
3. For each batch, write a dense technical summary capturing everything important.
4. Call `compress` with all ranges in a single call, or sequentially if you need to refine summaries between calls.
5. Report what you compressed and what you left intact.
