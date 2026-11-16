# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context window as a finite resource, context rot, compaction, tool-result clearing, note-taking, sub-agents, just-in-time retrieval. Use for: anything about what goes in an agent's context and how to keep it small.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
  A client-side, file-based memory under /memories that the model reads and writes through tool calls. Use for: a concrete design for saving notes between sessions.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://arxiv.org/abs/2307.03172)
  Evidence that accuracy is highest for information at the start or end of a long input and drops in the middle. Use for: arguing against stuffing whole documents into the context.

## Wisdom (Communities)

## Gaps

- No community has been chosen yet for testing agent designs; add one when the learner wants it.
