# Open misconception: the model runs the tools itself

On quiz 0001 (submission s1) Riley answered that the model opens the booking system and runs the tools itself, and counted one model call for a three-tool request.
Riley also wrote that the model remembers its tool choices from earlier sessions.
Riley does see that an agent is a loop, that a step limit stops a stuck loop, and that the model picks tools from names and descriptions.

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6 (wrong or partial); q1 and q3 correct.

**Implications:** Before the context and memory lesson, rework who does what at each step: the model writes a request as text, the program runs the tool and sends the result back, and each step is a separate model call. The model keeps nothing between calls; memory is saved and resent by the program. Submission s2 is a later attempt to compare against.
