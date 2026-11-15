# Loop and tool calling mostly solid; M6 and M4 still open

On the spaced attempt at quiz 0001 (s2) Riley correctly identified the agent loop (q1), what the model outputs when it calls a tool (q2), and what the program does with a tool result (q5).
Two misconceptions remain: M6, that an agent left running will eventually succeed without a stopping condition (q3), and M4, that the model runs the tools itself (stated in the reasoning for q4, though the count of 4 was right).
Riley also relied on the tool name alone to explain how the model picks a tool (q6).

**Evidence:** quiz 0001, submission s2, items q3, q4 and q6.

**Implications:** Before moving to context and memory, revisit stopping conditions (step limits) and that the program, not the model, runs tools. The s1 attempt is still ungraded.
