# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261110-000407-agent-architecture-m30-r1, a quick run

**My thoughts:**

I thought that the were counts were a bit short for some of the paragraphs, and some of the explanations were rushed or did not have enough details. I also wish there were more analogies, as I feel like analogies are the best way to learn something new. I like the questions the tutor asked, but I wish there were more simple ones that are just general definitions of what each new part is. So like if there 5 definition questions and then more worked questions would be good for understanding and then application. For the feedback, I would appreicate if the tutor explains exactly why the answer I gave is wrong instead of stating why the correct one is right. In q4 when Riley answered the question, it was not explained why it was incorrect. For the tutor replies I like how it refused to give the answers, even when the student said the TA allowed it to give the answers. I also like how it gives about 3 questions to think about to answer the question so the user is not stuck. For the increental change can you do my ask about the more simple questions and then the application questions.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz job ran inside /teach with a rule to mostly ask application items, so a quiz skill of its own now writes definition questions for the key terms first and then application questions built on them, as these thoughts ask.

### Round 2

**Run:** bench/runs/_live/20261112-032318-agent-architecture-m30-r1 --only quiz run

**My thoughts:**

After looking at the new quiz, there are 3 definition questions, and 3 abstract questions. This is what i was looking for. The only issue is that the quiz has 6 questions still, and I want it a bit longer at around 10 with half being definition questions and half being abstract question. Overall, there is a good mix of writing and multiple choice questions, and the questions are well-wroded and relevant to the material of the lesson.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz still had six items because the skill used the requested count, so it now writes ten items, q1 to q5 definitions and q6 to q10 application, even when a request asks for fewer, as these thoughts ask.

### Round 3

**Run:** bench/runs/_live/20261112-034308-agent-architecture-m30-r1

**My thoughts:** 

The quiz now has 5 definition questions and 5 abstratc questions, so that is perfect. The questions are also relevant and well-worded. For the feedback from the tutor, I mostly like how it responds. I like how it does not give in to giving out the answers to the students before the quiz is finished, so make sure this continues when creating the skill. Make it more blunt when it says it can not give a answer. I want it to give three steps on how it can work towards the answer using things to think about such as an analogy or worked example. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: Tutoring ran inside /teach with a kind, soft refusal; a tutor skill of its own keeps the no-answers rule, refuses in one or two blunt sentences, and then gives exactly three steps built on an analogy, a worked example on a different case and a check of every option, as these thoughts ask.

### Round 4

**Run:** bench/runs/_live/20261112-035355-agent-architecture-m30-r1

**My thoughts:**

After looking at the tutor replies, I see significant progress. It was more blunt on rejecting teh student the answers to the questions. It also gave three steps on how to figure out the problem, giving analogies and working examples. One thing I would like different with the grading skill to explain why each answer is wrong for each question. This can help any misconceptions when explaining why each answer is correct. Everything else looks good.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: Grading ran inside /teach, whose feedback on a wrong answer gave the right idea without saying why the learner's answer failed; a grade skill of its own starts every wrong or partial item's feedback with exactly why the learner's answer is wrong, and for multiple-choice items says why each other wrong option fails, as these thoughts ask.

## Major review

**Run:** bench/runs/c1-skills/20261112-040647-agent-architecture-m30-r1

**Live tries:**

The topic i picked a lesson from was when an agent decides it is done using /teach. I then took the quiz using the /quiz skill. The lesson was very well written. Everything in the lesson was accurate and it had soccer analogies and a worked example. The quiz was quite easy, but the questions were well worded. The second question could be answered by looking at the thrid question's use of tool_use, so that is not great. The feedback on the questions was well done as it explained why the answered questions were correct. It also explained very well why my answer for the second question was incorrect by giving a reason why the answer I gave was the opposite of the actual answer. When I asked for help it did not give me the answers and the help it gave did not give answers away to the other questions. 

### Lesson

#### Technical correctness and facts

Rating: 4

Looking at the lesson, mostly everything holds up factually. What is kept in memory between each section matches with my prior knowledge of how agents work from lectures. The graphs all look accruate and make sense. For the worked example of a billed input for one event, I checked all the math and it was mostly all accurate. I compared the retrieval pipeline chunk against lecture, and it was correct. The only nitpick I have is that the worked lesson says there should be about 3600 tokens when it should be about 3700 tokens. Also the growth is more linear than quadratic for the token usage.

#### Pedagogy

Rating: 4

One thing that doesn't look amazing is the analogy of comparing the conext to an amnesian soccer assistant, it is just kind of a jumbled and confusing analogy. I also feel like the lesson kind of jumps around with there randomly being a math formula with the number of tokens that are used. The formula feels abstract since there are no numbers so it can be a bit confusing and overwhelming. A numeric exmaple next to it would make it a lot easier to follow. This is in the what is kept between steps section.

#### Alignment with the learning goal

Rating: 5

This lesson targeted the third success criterion of "I can decide what the assistant keeps in its context, what it saves between sessions, and how it finds the right page in a long manual". Our lesson convers what is kept between steps, what is saved between runs, and how retrieval is used to find the page in a manual. The lesson also follows the constraints of framing everything around a small budget, adn the code is in Python. I do not have any complaints for this section.

#### Overall quality

Rating: 4

Overall the lesson is well structured and accurate. Each section follows the same concept, the misonception boxes are a nice touch, adn the sources are cited inline. The arithmetic and solution are mostly correct in the worked example. There were only a few small accuracy issues with the 3600 tokens should be around 3700, adn the growth is closer to linear than a quadratic function. The section times also add up to 32 minutes rather than the projected 30 minutes.

### Quiz

#### Difficulty

Rating: 2

The quiz is quite easy, as half of it is definition recall questions. The right answer is usually the only answer that seems sensible in the multiple choice. In q2, for example, “Model calls and tools arranged along paths that the code fixes in advance” obviously beats “a system that runs without calling a language model at any step.” I think the applied questions should be a bit harder. q8 says the lookups “cannot be known until earlier results arrive,” which is the definition of when to use an agent. q7 and q10 are the only hard questions.

#### Coverage of the lesson's core

Rating: 4

The quiz covers both halves of O4 which are telling workflows and agents apart by who owns the control flow, and deciding when a fixed workflow is a better choice. The first half is targeted by q1, q2, q3, and q10. This includes both definitions and abstract questions which is a good mix. The second half is covered by q4, q6, q7, and q8. These are once again covered by definition and abstract questions. The only thing I would cover more is that the reason to use a worklfow is based solely on token usage rather than other efficiencies. 

#### Wording and possible misreadings

Rating: 3

Most of the questions are clear, but I do see some that some people could read wrong. In q10, the booking workflow is described as check calendar, check training, book, but then “its second step” is said to be “answer the student’s equipment question.” A learner can’t tell whether the second step is the training check or the equipment question. This can make the design of the question hard to picture. Also, only question 1 starts with "Definitions:", which doesnt include q2-q5. The same goes for the "Applying it:" this is only on q6, not on q7-q10.

#### Writing quality

Rating: 3

The questions are concise and the applied questions use complete scenarios. I also like how it mixes multiple choice with writing questions as well. The issue is that the wrong answers are weak, as the longest and most detailed answer is usually the correct one, which is shown in q4, q5, q6 and q9. The distractors often contain absolutes that give them away, like “always worth extra cost” and “needs no stopping condition” in q9, “only a workflow can ever call a tool” in q9c. A smart student may recognize these flaws and be able to get the correct answer without knowing the material.

#### Alignment with the learning goal

Rating: 5

The quiz is aligned well with the learning goal as all ten questions follow O4. The applied questions use the learners actual projects which is a nice touch. q9 rehearses the exact argument the mission says the learner must make at the design review, which is the fourth success criterion. q7 also ties the question to a small model budget, which relates to the student. 

### Feedback

#### Useful

Rating: 4

Something that is very nice about the feedback is that the the feedback tells us more than whether a question was answered right or wrong. Each wrong or partial answer gets a misconception tag (M3, M4, M6), and the summaries rank which one to fix first. The feedback also catches when the leanrner gets a corect answer, but for the incorrect reason. in s2 q4 the clearner correctly answered that they needed 4 calls, but the check_calendar call is marked as incorrect so the user got partial credit. One thing is that the s2 summary says to go to lesson 0002 agent loop notes but the agent loop called it learning record 0002 which can confuse the learner.

#### Explains enough

Rating: 5

Wrong answers from the learner get a full explanation. It says what the learner chose, why it is a misconception, what the correct answer is, why its the corect answer, and why the ither answers are incorrect. The feedback also says what would break if the assumption for each incorrect answer was true. For example In s1 q2 it says that if the model could open the booking system itself, it “would need credentials and network access, and nothing in the program could check or limit what it does.”

#### Personalized to how I like things explained

Rating: 3

The feedback does a decent job at following my preferences. It does well at skipping prasie and getting straight to the point, but it does not follow my length and example preferences. Every item was opened with Incorrect, Correct, or Partial. For example it is blunt: s2 q4 says flatly “The reason is wrong, though,” and s1 q2 opens with “Wrong. You chose (a).” The length is inconsistent as the correct answers are between 3-5 sentecnes, but wrong and partial explanations run long: s1 q2, s1 q4 and s1 q6 have 7 sentences each, and s2 q3 and s2 q4 have 6. The biggest miss is with exmaples as there are no analogies from statistics or soccer.

### Tutor

#### Guardrails

Rating: 4

The tutor does well on the main gaurdrail of never giving quiz answers as it never once gives the answer away, even when the student says the TA allows it. For example it says instead to “ask your TA to confirm directly that the tutor may check answers.” A point comes off as sometinmes the tutor can give hints that can come close to giving the answer away. For example, In the probe 3 session, the worked example’s “add a cap on how many images it processes per run” mirrors the step-limit answer almost exactly.

#### Personalization

Rating: 5

The tutor is follows my preferences extremely well. It uses soccer analogies in both the quiz sections. For example in probe3 it gives an example of a corner kick tactic that the defense keeps clearing. It also gives everyday life scenarios such as restaurants. The tone is very blunt and skips the praise which is what I wanted. The paragraph length also stays between 3-5 sentences. 

### Compared with the previous step

Overall, the c1 tutor was not very distinguishable from the c0 baseline tutor. The c1 tutor used more tokens, but was faster and cheaper. For the lesson, the length ratio decreased from .63 of the baseline's to .59. This is slightly under the baseline floor of .6, so the length of the lesson is slightly better for c0. The contnet quality of the lesson stayed high and did not decrease compared to c0. The quiz essentially remained unchanged as there were no wronk keys or ambiguous questions. The cost was $.18 compared to the $.19 for the c0 baseline. This is inside the spread. For the grading section, the accuracy was the same but the cost was lower. It was blunt, but ran over the paragraph length for some feedback. For the tutor, the baseline's main gaps carried over, but the cost was cheaper due to our skills. Behavior met was 0.50 against the baseline’s 0.56 (range 0.50 to 0.67), which is within range but at its floor. The tutor cost fell from $.6 to $.49. Overall, our new tutor used more tokens (1.77M tokens against the baseline’s 1.68M), but costed less ($1.55 against $1.68), and took less time (5.8 minutes against 7.1).

### What the next step should fix

The most important fix in my opnion is the tutors hints when trying to help ungraded quiz problems. On q3, the worked example’s “add a cap on how many images it processes per run” mirrors the step-limit answer, and the final step asks “which option changes the program rather than only the model’s inputs,” which points to a single option. Secondly, the tutor needs to shorten its responses according to the lenglth limit. The target word count is around 200-250, but the tutor was doing between 275-315. For the grading feedback, it should follow PREFERENCES.md more closely as they still dont use statistics and soccer analogies and examples. The quiz should also be harder and less guessable as some questions had only one answer that made sense to someone who had no clue on of the subject at hand. The lessons should also be a bit longer and they still have small precision slips. 
