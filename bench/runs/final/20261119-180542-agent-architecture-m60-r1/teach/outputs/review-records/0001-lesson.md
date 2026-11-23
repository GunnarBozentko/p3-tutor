# Review record: lesson 0001, context and memory in an agent (O3, 60 minutes)

## Lesson review loop: 2 passes
- Pass 1: length estimate about 6,250 words (ratio 0.69).
  - L1 length: all sections thin, especially warm-up, S3, practice, summary.
  - L2 times: stated times summed to 69, not 60.
  - T3 numbers: one wrong total in the three-chunk practice (11,450 should be 13,450).
  - T4 growth: "square of steps" claim contradicted the lesson's own numbers; clearing example removed a result the final answer needed.
  - P6: formula without numbers.
  - Q13: the worked run duplicated quiz 0001 q4's request and tool order; warm-up recall repeated quiz 0001 q2 and q5.
  - Changed: added worked examples and practice (fixed-part estimate, compaction, helper, clearing, notes cost, rare-word weighting, priced request); times reset to 3/8/10/8/9/10/9/3; run changed to a 3D printer request with five calls and all numbers recomputed; growth paragraph rewritten with a proof; warm-up replaced; analogy fixed; terms defined at first use.
- Pass 2: length estimate about 7,400 words (ratio 0.82).
  - T3: price rounding ($0.056, $0.065); paste-versus-retrieve comparison compared unlike runs (pasting needs no search step; ratio now 17.5, practice 21).
  - T4: notes code overwrote earlier notes; dropped-result check needed an API caveat.
  - Q13: the notes check and the "remember a failed booking" check overlapped quiz items.
  - Changed: all of the above fixed; added compute practice in S1, S3, S4 and the practice section; notes code merges old notes; checks replaced with new scenarios.
- Left: the reviewer's optional "Statistics view" addition was kept; the suggested memory-tool link with `/en/` was left as seen in search results and fetched by the checker.

## Preference reviewer
- Must fix: 1, 2, 3, 4, 6, 10, 12, 15, 16, 17.
- Changed: example before definition in sections 1, 2, 3 and 5; proof of the growth formula; terms defined at first use; everyday analogies (help line, barista); paragraphs split and steps turned into bullets; feedback wording "Correct." and "Incorrect."; formal footer; code snippet for cosine ranking; IDF and recall at k notes.

## Reference checker
- Must fix: none.
- Changed (optional items): reranking definition softened to the source's wording; token-counting link moved to the platform address it redirects to.

## Lesson editor
- C1: figure 3 caption said a tool loads notes; changed to say the program loads notes at session start and manual chunks come through a search tool.
- C2: footer now names the quiz's objective.
- Left: the mission box says the assistant must "know" training status between visits; kept as motivation, since the lesson teaches that the status comes from a tool.
