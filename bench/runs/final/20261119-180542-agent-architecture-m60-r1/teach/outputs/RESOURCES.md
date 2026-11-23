# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Attention budget, context rot, just-in-time retrieval, compaction, tool result clearing, structured note-taking, helper agents. Use for: what to keep in context and how to trim it.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how it grows in a tool loop, context rot, compaction and context editing. Use for: exact definitions and the mechanics of the window.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/agents-and-tools/tool-use/memory-tool)
  File-based memory that persists between sessions, with storage run by the application. Use for: designing what the assistant saves between visits.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  Chunking, keyword plus embedding search, reranking and measured retrieval failures. Use for: finding the right page in a long manual.
- [Docs: Token counting (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
  How to count tokens before sending a request. Use for: budgeting cost per request.

## Wisdom (Communities)

- Local: Colorado School of Mines instructors and the makerspace staff
  Use for: checking which manual pages students most often miss and which questions to test the assistant with.

## Gaps

- A high-trust source on how many tokens an English word takes; the lesson uses the rule of thumb of about 0.75 words per token, from general knowledge, and recommends the counting tool for exact numbers.
- A moderated community for agent builders; none vetted yet.
