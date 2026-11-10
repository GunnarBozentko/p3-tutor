# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context window, context rot, compaction, note-taking, just-in-time retrieval, sub-agents. Use for: what to keep in context and what to save.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering, Sept 2024)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25, reranking, and the "under about 200,000 tokens, just include it all" advice. Use for: how to find the right page in a long manual.

## Wisdom (Communities)

- Local: the makerspace staff and your design team.
  Use for: the real list of questions students ask, which decides what to retrieve.

## Gaps

- A beginner-level source on calling a model from Python with tool definitions.
- Independent (non-vendor) evidence on retrieval quality for small manual sets.
