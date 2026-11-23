# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on context, context rot, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: any decision about what the assistant keeps in its context.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of the window, how tokens accumulate over turns and what happens when it fills. Use for: cost and limit questions.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side, file-based memory across sessions, with the handler's security duties. Use for: designing notes saved between visits.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://Huggingface.co/papers/2307.03172)
  Peer-reviewed study of how position in a long input affects accuracy. Use for: arguing against stuffing whole manuals into the context.

## Wisdom (Communities)

- [r/LLMDevs (listing)](https://thehiveindex.com/communities/r-llmdevs/)
  Developer community discussing RAG and agents; self-promotion is common, so read critically. Use for: asking how others split context, notes and retrieval.

## Gaps

- A high-trust, vendor-neutral source on retrieval quality (chunking, embeddings, precision and recall) has not been found yet.
