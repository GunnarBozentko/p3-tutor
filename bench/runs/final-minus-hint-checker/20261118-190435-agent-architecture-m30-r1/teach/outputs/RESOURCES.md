# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering, Sep 29, 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, compaction, tool-result clearing, structured note-taking, just-in-time retrieval. Use for: deciding what an agent keeps in context, saves, or retrieves.
- [Docs: "Context windows" (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how input grows turn by turn, prompt caching and the too-long error. Use for: token and cost arithmetic.

## Wisdom (Communities)

- Local: the senior design team's design review.
  Use for: testing where each fact in the makerspace assistant belongs.

## Gaps

- A trusted source on retrieval quality (chunking, embeddings, evaluating search) is still missing.
