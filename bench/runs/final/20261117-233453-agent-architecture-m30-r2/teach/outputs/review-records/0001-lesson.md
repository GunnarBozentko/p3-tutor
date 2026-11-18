# Review record: lesson 0001, context and memory in an agent (O3, 30 minutes)

## Lesson-reviewer passes: 2
- Pass 1 length estimate: about 3,400 words, ratio 0.76 (too short).
  - L1 length: every section under 150 words per minute. Added worked traces, clearing and compaction examples, failure rates as counts, a cost example, a second warm-up recall and a summary bullet.
  - T4: Figure 1 bars not to scale; the worked placement example contradicted the 200,000-token rule. Redrew bars at 0.06 per token and added the reconciling text.
  - T5: memory-handler code failed on the first `/memories` call; "simplest form" not in the source; footer named a quiz not yet written. Fixed the code, reworded, wrote quiz 0002.
  - P7: soccer analogy did not map one to one. Rewrote it.
  - A10: retrieval as memory was thin. Added a paragraph (a worked example came in pass 2).
- Pass 2 length estimate: about 5,000 words, ratio 1.1.
  - L1: Window section over 150 words per minute. Left in place (see below).
  - T4: "grows by a fixed amount" was false for the lesson's own increments. Reworded.
  - T5: unstated window size; 2.9% should say contextual BM25; caching figure. Added all three.
  - P9: two broken paragraph tags that my own pass-1 edits caused; undefined "attention". Fixed both.
  - A10: retrieval-as-memory worked example. Added.
  - Q13: quiz items 3, 4 and 5 overlapped lesson practice. Rewrote the lesson's welder check and the quiz items 3 to 5.
- Findings left, with reasons:
  - Moving the cost worked example out of the Window section and removing the memory-handler code: left, because `PREFERENCES.md` asks for code and worked examples and the total stays inside the 0.6 to 1.5 band.
  - Splitting the Window section in two: left, because the section times already sum to 30.

## Preference reviewer
- Must fix: 1, 2, 3, 6, 9, 11, 12, 13, 14.
- Changed: example before definition in the warm-up, window, sessions and retrieval openings; a proof of the arithmetic-series shortcut; definitions for attention, session, handler, client-side, authoritative record, chunk, index, prompt, recall and sub-agents; two everyday analogies; the soccer paragraph and long list items into bullets; the retrieval pipeline and the three placement questions into lists; the script's feedback now says "Correct." or "Incorrect." and gives the fix; formal rewording of the misconception boxes and footer; filler removed.

## Reference checker
- Must fix: the 400 tokens-a-page figure was cited to the source but is the lesson's own arithmetic; Claude Code attribution and the absolute failure rates were only partly confirmed by the quote retrieved.
- Changed: the 400 figure is now stated as arithmetic from 200,000 / 500. The other two were left: the fetch of the same article earlier in the session reported the Claude Code compaction example and the 5.7%, 3.7%, 2.9% and 1.9% rates.

## Lesson editor
- C1: none. C2: footer wording now names quiz 0002 and its objective. Left: none.

## Quiz
- Quiz 0002 (five items: two multiple choice on mechanisms, two numeric, one risky-permission item). Rewritten once after the second review found overlap with lesson practice.
