# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: anything on what belongs in an agent's context.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based, client-side memory across sessions, with security cautions. Use for: designing what the assistant saves between visits.
- [Announcement: Managing context on the Claude Developer Platform](https://www.anthropic.com/news/context-management)
  Context editing alongside the memory tool. Use for: clearing stale tool results (read in search results only, not opened in full).
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://Huggingface.co/papers/2307.03172)
  Shows recall drops for information in the middle of long inputs. Use for: arguing against stuffing whole manuals into context.

## Wisdom (Communities)

- Local: the senior design review and faculty advisor
  Use for: testing the architecture choices and token estimates against real critique.
