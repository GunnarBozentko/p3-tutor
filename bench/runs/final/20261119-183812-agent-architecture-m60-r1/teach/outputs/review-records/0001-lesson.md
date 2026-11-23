# Review record: lesson 0001, context and memory (O3, 60 minutes)

## Lesson-reviewer loop: 2 passes
- Pass 1: length estimate about 7,300 words (ratio 0.81). Flagged: context window (T3 ratio "3.5 times" wrong, note token count 120 vs 20; P8 phantom "safety section", forward retrieval reference), kept between steps and sessions and retrieval (P9 long paragraphs), worked example, rehearsal, summary (L1 thin practice), warm-up (L1; Q13 Recall 2 restated quiz 0001 answer; footer pointed to a quiz that did not exist yet).
- Changes after pass 1: corrected the ratio to 2.62 and the note size; fixed the two phantom references; replaced Recall 2; hedged the token rule; split long paragraphs into bullets; added a second faded practice (order of tool calls), a budget check and a model answer in the summary; renamed a mislabeled list item; added "not to scale" to Figure 2; replaced "faculty advisor" with the team.
- Pass 2: length estimate about 8,200 words (ratio 0.91). Must fix: Q13, the numeric case reused quiz 0001's tool names and order and gave away its call count. Recommended: Part C wording, Part B assumption, move Recall 3, quiz footer.
- Changes after pass 2: renamed the third tool to check_material_stock; fixed Part C wording and added the Part B assumption; added the 120-token note assumption; replaced Recall 3 with a question that does not teach tokens; split the stale-notes paragraph.
- Left: the reviewer's suggestion to cut the order-of-tool-calls section or the chunk-size subsection (kept; the time labels add up to 60 and the words are within range). The optional whiteboard-copy remark (not needed).

## Preference reviewer
Must fix: 1, 3, 4, 5, 6, 7, 11, 13, 15. Changes: concrete example added at the start of three sections; a derivation of the cost formula with a numeric check; first-use definitions added for retrieval step, tool definitions, system prompt, input tokens, prefix, compaction, stub, pruned, handler, index, metadata; "Three questions" fix; a numpy top-k code sample; an everyday desk, notebook and library analogy; long paragraphs turned into bullets; three-step retrieval method as a list; formal footer.

## Reference checker
Must fix: sub-agent "tens of thousands" claim (my own fetch of the article reported it, so kept); "badly described tool wastes context" (reworded to the article's point about guidance on tools); minor wording on "safest lightest touch" (now "one of the safest lightest touch forms") and the hybrid strategy (now "describes a hybrid strategy"). All workspace references found.

## Lesson editor
- C1: the opening example and the cost-case base now agree (4,550 tokens); the Priya note after the session is "Prefers afternoon slots", consistent with the table.
- C2: footer quiz pointer now names quiz 0002; the forward pointer to stale notes now names the right subsection; "note-taking" now points to the next section.
- Left: no record number cited for the agent loop; the lesson lists clearing, compaction and sub-agents while the source's three are compaction, note-taking and sub-agents.
