# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context window, context rot, compaction, structured note-taking, just-in-time retrieval and sub-agents. Use for: any decision about what the assistant keeps in context.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25, merging, the 200,000-token rule for skipping retrieval, and measured failure rates. Use for: how the assistant finds the right page in a long manual.
- [Documentation: Memory tool (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  The client-side file-based memory tool, its commands and its security guidance. Use for: what the assistant saves between sessions and how to build the storage handler safely.

## Wisdom (Communities)

None chosen yet; a community for agent builders is to be added in a later lesson.

## Gaps

- A high-trust community where the learner can test agent designs.
- A source on workflows versus agents and on multi-agent systems (later objectives).
