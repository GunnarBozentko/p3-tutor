# The agent loop holds from memory, with two gaps

Four days after the agent-loop session, Riley answered from memory that an agent is defined by the loop, that the model outputs only a tool request, and that the result is fed back as the next input.
Two gaps remain: Riley believes an agent left running will eventually fix a repeated failure, and says the model runs the tools itself while counting model calls correctly.

**Evidence:** quiz 0001, submission s2: q1, q2 and q5 correct; q3 wrong; q4 partial; q6 partial (chose tools by name only).

**Implications:** Revisit the need for a step limit and the program, not the model, running tools. Teach that the model chooses a tool from its description, not only its name, before context and memory.
