# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/research/effective-context-engineering-for-ai-agents)
  Defines context engineering, context rot, compaction, structured note-taking and just-in-time retrieval. Use for: what belongs in an agent's context and how to keep it small over long tasks.
- [Docs: Memory tool (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Official description of a file-based memory that persists between sessions and is executed by your own program. Use for: how notes-as-memory work in practice.
- [Article: "Managing context on the Claude Developer Platform" (Anthropic)](https://www.anthropic.com/news/context-management)
  Introduces context editing (clearing stale tool results) and the memory tool, with Anthropic's reported results. Use for: when to clear versus save.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  Explains chunking, embeddings, BM25, hybrid search and adding context to chunks, with Anthropic's measured retrieval failure rates. Use for: how the assistant should find the right page in a long manual.

## Wisdom (Communities)

- No community has been vetted yet for this topic. Candidate to check in a later session: the Anthropic developer community and the learner's own senior-design review panel.

## Gaps

- An independent (non-vendor) textbook-level source on retrieval evaluation, for judging how well the manual search works.
