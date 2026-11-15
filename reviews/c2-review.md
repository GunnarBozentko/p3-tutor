# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261112-040647-agent-architecture-m30-r1

**My thoughts:**

I want the first reviewer to check the quiz. The reviewer should read the draft the way a learner would, with a fresh context, and flag any item that can be answered from wording alone. In c1 some of the questions would completely give the answer away like q6 says the steps run “always in that order” with no judgment needed, and q8 says the lookups “cannot be known until earlier results arrive.” Also the correct option is often the longest one, so make the wrong answers longer or the correct shorter. The reviewer should also check questions against each other as sometimes one question can help answer another question accidentally. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The thoughts asked for a fresh-context reviewer that flags items answerable from wording alone (stems that state the answer, the longest option being right, absolutes in wrong options) and items that help answer each other, so a quiz-reviewer now blind-reads each draft in drafts/ as a test-wise guesser before opening the key, and the quiz skill revises at most twice, writes quizzes/ and keys/ once, and records the loop in review-records/NNNN-quiz.md.

### Round 2

**Run:** bench/runs/_live/20261114-022428-agent-architecture-m30-r1/

**My thoughts:**

The quiz reviewer does not fix most of what I asked for. The correct option does not stand out by length anymore as most of the answers in the question have a similar length. Besides that, not much changed. some of the questions still give each other away such as q6's question answers q5. Some of the questions still telegraph their answer as "set in advance" is used in the question and answer for q6. Also, incorrect answer still have direct giveaway s htey are not correct.

**What changed:**

- Kind: other
- Files: tutor/.claude/agents/quiz-reviewer.md
- Why: The thoughts said the reviewer still let through cross-item leaks (q6 answering q5), a stem and answer sharing "set in advance", and wrong options that rule themselves out, so the reviewer now builds a leak table comparing items by meaning before it opens the key, flags any phrase the stem shares only with the correct option, counts every option a non-expert can cross out as a finding, and must give exact replacement text for each finding instead of "reword it".

### Round 3

**Run:** bench/runs/_live/20261114-023958-agent-architecture-m30-r1/

**My thoughts:**

This quiz is the best version so far, and it is harder like I intended it to be. Three of the applied questions target common misconceptions, instead of reciting definition questions. q9 has a good trap in option b: a multi-step request (two calendar lookups and a comparison) that is still a fixed workflow. Its correct answer, the peeling prints in option d, is the shortest option rather than the longest. A problem that remains is that the longest option is the correct one in questions q2, q6, and q8. q2 and q3 are workflow questions that give away q4. The quiz lost a numeric cost question which matters because I am trying ito keep cost per request within a small budget an important part of the quiz. 

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The thoughts named the longest option still being correct in q2, q6 and q8, q2 and q3 giving away q4, and the lost numeric cost question, and the review record showed the quiz skill itself kept the leak "with a reason" and swapped the numeric item for an mcq, so the skill now requires a word count where the correct option is never the longest alone, forbids leaving any giveaway or leak unfixed, keeps a numeric item on the mission's cost per request (adding judgment instead of dropping it), and checks all three itself after the last revision.

### Round 4

**Run:** bench/runs/_live/20261114-025740-agent-architecture-m30-r1/

**My thoughts:**

For the reviewer all of the feedback is now within 3-5 sentences. Wrong items do not start wit ha blunt verdict though. The quiz looks good and the longest answers arent the correct one now. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: The thoughts said the feedback now keeps to 3 to 5 sentences but wrong items do not open with a blunt verdict ("You chose a:", "You answered 1"), so a grade-reviewer now reads each draft in drafts/ against PREFERENCES.md with a checklist from my c1 feedback review (verdict word first, 3 to 5 sentences, statistics or soccer examples, references named as they are in the workspace) and gives replacement text, and the grade skill revises at most twice, writes grades/ once, and records the loop in review-records/NNNN-sN-grade.md.

### Round 5

**Run:** bench/runs/_live/20261114-031153-agent-architecture-m30-r1/

**My thoughts:**

This round fixed both things I asked for. Every question now opens with correct, incorrect, or partial, and every question has an example with an analogy from my preferences. Some sentences are now long and dense to fit the analogy in, for example the q2 sentence about the structured request. The reviewer did not fix the legnth and it actually made it worse with a length ratio of 0.55. The precision slips are gone form the lesson though which is good. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The thoughts said the length got worse, at a ratio of 0.55, and that comes from the lesson, which had no reviewer, so a lesson-reviewer now estimates each section's words against 150 per requested minute and names the examples and practice to add, and also fact-checks numbers and growth claims, flags formulas without numbers and confusing analogies, and checks alignment, as my c1 lesson review asked; the teach skill drafts in drafts/, revises at most twice, writes lessons/ once, and records the loop in review-records/NNNN-lesson.md.

## Major review

**Run:** bench/runs/c2-review/20261114-190245-agent-architecture-m30-r1

**Live tries:**

The lecture had good length with a ratio of 1.02. It follows PREFERENCES.md closely as it compares tool choice to soccer and the lesson facts match claude's notes. The quiz also did well with keeping my 10 question format. There was a soccer live-score agent (q7) and a fit_regression tool (q10), which fit my preferences. The feedback was also precise. It started with Correct, Incorrect, or Partial. It explained well why my answer was wrong and why the correct answers were correct. I do not see anything striking that I would change. 

### Lesson

#### Technical correctness and facts

Rating: 5

All of the math calculation check out, for example the grwoth formula matches the inputs put into it and gets the correct answer. The bar chart's heights are accurate and it fixes the statement that the growth is more linear than quadratic. The cosine values are also estiamnted accurately. 

#### Pedagogy

Rating: 4

The lesson follows the PREFERENCES.md file quite closely. There is a general idea and then a concrete example, soccer and everyday terminology and analogies, and new terms are bold the first time they appear. Keyword search is still missing from the retrieval section, so the lesson never explains why an exact error code needs keyword matching rather than embeddings. Some paragraphs still run past 5 sentences and can be a bit lengthy. 

#### Alignment with the learning goal

Rating: 5

The lesson now directyl matches the third success criterion. It covers what the agent keeps in context, saves between sessions, and how it could find the wanted page in a manual. The cost per request is kept in the loop the entire lesson and the code is simple for someone who has no experience with calling a model. 

#### Overall quality

Rating: 5

This is definitely the strongest lesson so far, and the lenght ratio is also the best compared to previous lessons with a ratio of .81. The section times add up to 30 minutes now and the precision slips are absent. There are also several new worked exmaples that work really well like the cosine estimations and the database table. We are missing a keyword search still though. 

### Quiz

#### Difficulty

Rating: 4

This is significantly harder than the c1 section. The aplied problems need reasoning instead of just definitions. q9 asks you to choose the right design for each request type before computing the cost, so a learner who gives both types the same design gets the wrong total. Questions 6 gives the answer away by saying moves 2 and 3 never are triggered by a model decision. 

#### Coverage of the lesson's core

Rating: 4

The quiz does a good job at covering both halves of O4. To tell workflows and agents apart, it defines both (q1, q2), asks what control flow decides (q3), and asks what the model’s job is in a workflow (q5). One of the main losses in this quiz is that there are no questions on routing and prompt-chaining which c1 tested. 

#### Wording and possible misreadings

Rating: 3

Most of the questions are clear but there are a couple that can be confusing. q7 asks for “answering correctly at the lowest cost per request,” and a learner might wonder whether the agent capped at 6 lookups really costs less than the 3-lookup chain. Also questions 6 and 8 have some issues as students could be confused on the agents wrong calendar or the "given that budget" phrase. 

#### Writing quality

Rating: 4

Overall teh questions are well written. The yuse the learners own project with the laser cutting which is good. Lots of the c1-skill giveaway questions are gone. In q6 and q7 the longest answer is not the correct one, which is also a plus. One issue is that q2’s option a also answers q3’s short question (“decides at each point what happens next... and when to stop”).

#### Alignment with the learning goal

Rating: 5

All of the questions are tagged in O4. Q8 is involved with the agents are more capable  argument. The questions also help answer the design of a fixed worklfow for booking and an agent for lookup and troubleshooting. The question format follows my preferences exactly. 

### Feedback

#### Useful

Rating: 5

The feedback is more useful than the c1 skills feedback. Each wrong and partial answer is brought up with a misconception and addresses the learner why that is incorrect. It accurately gives why the correct answer is correct. The s1 summary now credits the right items (“q1 (the loop), q3 (the step limit) and the tool-description part of q6”), which fixes the c1-skills mislabel that credited q5 for choosing tools. The next steps do very well at giving a concrete plan for the learner.

#### Explains enough

Rating: 5

The feedback tells each student why their answer is incorrect and why it is a tempting answer. It then exaplins why the correct answer is the way it is and why something would break if the incorrect answer was actually reality. For example, In s1 q6, a renamed tool “would still be chosen by habit, the way a player keeps running an old set play.” New terms are also defined in parenthesis whcih is great.

#### Personalized to how I like things explained

Rating: 4

Overall the feedback follows PREFERENCES.md quite well. There are multiple statistical and soccer analogies within the feedback. There is code feedback in the s2 next step (for step in range(max_steps)). The length of the feedback are now 4-5 sentences which is within my 3-5 range. It fdoes seem to overuse the soccer analogies though, as I told it to use it when applicable. Every s1 item has a soccer analogy (a team talk, a commentator, a manager at a stoppage, a scout, an old set play), and some are strained, such as s1 q1.

### Compared with the previous step

C2-review performed better on all 3 skills than compared to c1-skills. For the lesson, the lenght is way better and the precision slips are gone. It also uses more analogies and does worked examples and shows each step. The quiz improved the most. Difficulty rose from 2 to 4 as all the application questions required reasoning now. The writing quality also rose as the longest answer does not dominate whether it is correct or not anymore. The feedback greatly improved as well. Explanations of wrong answers ran from 6 to 7 sentences with no analogies, and now they are within 4-5 sentences with analogies which is great. There were good analogies with p-value comaprisons and soccer terminology. 

### What the next step should fix

The next thing that should be fixed is making sure the quiz problems are checked against each other. There were still sometimes leaks that would happen where a later answer would help with a previous question. q2’s option a answers q3’s short question. Also the lesson should cover keyword search in the retireval section. 
