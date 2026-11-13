# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: to add ask about definiton and application questions to the learner after the teach skill
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: Without it the quiz had 6 questions with them mostly being applide questions. With it there are not 5 definiton and 5 application questions. The structure made the quiz a bit easier, but there are more questions now.
- Kept in final: TODO

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: to guide and help the user with quiz questions but not give the answer away. 
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: The refusals were kind and soft at first, but now they are straight to the point. It also uses soccer and everyday analogies which is good. 
- Kept in final: TODO

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: give a lesson to the learner
- With and without: none yet; teach ships with c0-baseline and no c1-skills round changed it, so its SKILL.md in configs/c1-skills/ is the same as in configs/c0-baseline/
- Review: The skill was unchanged in c1 so the only differences come from my preferneces which ask for math and coding examples as well as analogies, which it does well.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: grades quizzes and gives feedback on the answers
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: Does a good job explaining why a question was incorrect, and explains why the correct answer is right. A drawback is that the responses are a little lengthy.
- Kept in final: TODO
