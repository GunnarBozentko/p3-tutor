# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, context rot, compaction, note-taking, just-in-time retrieval, sub-agents. Use for: deciding what the assistant keeps in context, saves, or retrieves.
- [Documentation: "Context windows" (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, errors at the limit, context rot, compaction, tool result clearing. Use for: exact behavior and current limits of the window.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://arxiv.org/abs/2307.03172)
  Shows that models use information at the start and end of a long input better than the middle. Use for: arguing against loading long text into context.

## Wisdom (Communities)

- Local: the senior design team and design reviews.
  Use for: testing where each piece of information should live.

## Gaps

- A high-trust source on retrieval design (chunk size, hybrid search) and a moderated community for agent builders have not been found yet.
