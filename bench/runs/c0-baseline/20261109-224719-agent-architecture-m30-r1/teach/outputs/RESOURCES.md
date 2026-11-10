# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, compaction, note-taking, just-in-time retrieval and sub-agents. Use for: deciding what the assistant keeps in context.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How turns and tool results accumulate, window size, context rot, cost. Use for: token and cost reasoning.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file-based memory and its safety duties. Use for: designing what is saved between sessions.
- [Article: "LLM Powered Autonomous Agents" by Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent)
  Planning, memory and tool use as agent components. Use for: the short-term vs long-term memory framing. (Only seen in search results so far; not read in full.)

## Wisdom (Communities)

No community chosen yet; the learner's makerspace staff and design-review audience are the nearest real-world test.

## Gaps

- A high-trust, beginner-level source on embeddings and retrieval chunking for small document sets.
