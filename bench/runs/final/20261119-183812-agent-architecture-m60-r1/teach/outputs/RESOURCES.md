# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot and the attention budget; covers compaction, structured note-taking, sub-agents, and just-in-time versus up-front retrieval. Use for: what to keep in context, what to save outside it, how an agent finds the right page.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How a context window grows turn by turn, what counts toward it, what happens at the limit, compaction and context editing. Use for: the mechanics of context between steps.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A file-based memory that the application runs on the model's request, so it persists between sessions. Use for: how notes saved between sessions work in code.

## Wisdom (Communities)

- Local: the senior design team's own design reviews
  Use for: defending a context and memory design with a reason, and testing it against real makerspace questions.

## Gaps

- No verified, well-moderated online community for agent builders has been found yet; add one when a trusted link is seen.
