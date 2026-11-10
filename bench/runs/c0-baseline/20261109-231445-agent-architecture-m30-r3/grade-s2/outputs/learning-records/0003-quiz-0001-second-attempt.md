# Riley knows the loop and what a tool result is for, but still thinks the model runs tools and that a loop needs no limit

On the second attempt at quiz 0001, Riley correctly chose the loop as what makes an agent (q1), saw that the model only writes a tool request (q2), and explained that the program feeds the tool result back as the next input so the model can decide what to do (q5).
Two beliefs are still open: the model "runs one tool itself each time" (M4, shown in the reasoning for q4, which had the right count of 4), and a stuck agent will "eventually fix the bug" with no stopping condition (M6, q3).
Riley also says a tool is chosen "by the name", not from the full description (q6, partial).

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5, q6. Submission s1 is not yet graded.

**Implications:** Before context and memory, revisit who runs a tool (the program) and why a loop needs a step limit, tying both to the makerspace assistant's cost. Practice writing a full tool description.
