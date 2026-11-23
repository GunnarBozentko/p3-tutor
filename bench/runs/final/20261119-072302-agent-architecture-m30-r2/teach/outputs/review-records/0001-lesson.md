# Review record: lesson 0001 (O3, context and memory)

**Passes:** 2.

**Pass 1** (length estimate 4,250 words, ratio 0.94)
- L2 section times added to 40 minutes, not 30. Fixed.
- T3 retrieval arithmetic contradicted itself (chunks resent). Fixed, with the 71 times figure. Figure 2 bars were not to scale. Fixed.
- Q13 worked example, misconception box, retrieval check and token practice mirrored quiz items. Changed the scenarios and numbers.
- Also applied: soccer mapping, prompt caching and system of record definitions, history-loop code, cost sentence, compaction example, paragraph splits.
- Left: the optional "after tool result clearing, Anthropic calls it a form of compaction" rewording; the lesson treats them as two techniques, which is accurate enough.

**Pass 2** (length estimate 4,590 words, ratio 1.02)
- L2 section times matched the sum but not the reading load. Retimed to 2/4/5/3/4/5/5/1/1.
- T3 cost framing counted input only. Reworded.
- A10 notes grow with every visit. Added a numeric paragraph.
- Q13 practice and retrieval cost mirrored the quiz again. Changed numbers and the worked-example note.
- T5 compaction paraphrase replaced with the post's recall-first advice.
- Left: a retrieval code sample (`search_manuals`) was suggested; the length was already at 1.02, and the cosine code sample covers the learner's wish for code there.

**Preference reviewer Must fix:** 1, 2, 3, 6, 7, 9, 11, 13, 16, 17.
Changes: concrete opening for the limits section, derivation of the quadratic cost with a numeric check, definitions at first use (token, input and output tokens, recall, attention budget, chunk, embedding, keyword search, cosine, sub-agents), cookbook analogy, statistics link (Pearson correlation) and compaction as summary statistics, bulleted arithmetic, "Correct."/"Incorrect." feedback in the script, formal footer, removed the filler sentence about sources.

**Reference checker Must fix:** three weakly supported claims in the Anthropic post (retrieval in advance, Pokémon tallies and maps, "pointers"); the key was not opened because of the keys guard.
Changes: "pointers" became "identifiers, such as file paths or stored queries". The other two were left: the earlier full read of the post found the embedding-based pre-inference retrieval and just-in-time statements, and the Pokémon tallies and maps.

**Editor:** C1: Figure 3 activity said "three boxes" and the figure has five (now "the boxes"); worked-example step 3 note wording made to match step 5. C2: footer quiz pointer made specific. Left: the lead names three homes while the figure adds a fourth, a tool reading a system of record; scope difference, not a contradiction.
