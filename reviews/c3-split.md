# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261115-194017-agent-architecture-m30-r1/

**My thoughts:**

This is the best lesson so far. The length-ratio is about .87 and has no precision or calculation slips. It finally has the keyword search in the retrieval section. The warm-ups token estimated and it is checked later as well. It also follows my PREFERENCES.md file clsoely. One issue I see is that there is a contradiction for who writes notes as Section 4 says notes are “small, exact and written by the agent,” but section 3 says the model “gets the record to read but no tool to write it.” The footer also says quiz 0002 which tests on O4 and not this lesson. I think both of these problems come from checking. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-editor.md, tutor/.claude/skills/teach/SKILL.md
- Why: The notes contradiction came from a second-pass fix to section 3 that nothing checked afterwards, and the footer named quiz 0002 before that quiz existed, so a fresh-context lesson-editor now reads the reviewed draft after the quiz is written, makes every section state each fact the same way and every pointer match a real file, and only then is the lesson written.

### Round 2

**Run:** bench/runs/_live/20261116-003607-agent-architecture-m30-r1/

**My thoughts:**

The notes contradiction is now resolved. The issue is that it did this by having the model write the training status with save_note. This  reversed the earlier safety point, which is not good. Also it "fixed" the footer by claiming quiz 0002 covers O3, but it actually covers O4. The checker needs to consult references with the actual files without blindly stating that it is correct. Keep this checker, and add a separate checker that opens the actual files and makes sure the sources are found and correct.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/reference-checker.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson-editor stays, and a separate reference-checker now opens every workspace file the lesson names and fetches every source it cites, quoting what each actually says, before the editor runs, so a reference is judged by the file and not by the lesson's own description of it.

### Round 3

**Run:** bench/runs/_live/20261116-010244-agent-architecture-m30-r1/

**My thoughts:**

This is now the strongest lesson so far. That safety regression from before is gone as the training status is in the database that a tool uses at a request. The references all look checked now as the header now reads Lesson 0001 and cites records by their actual title. The contradiction baout notes is still gone. Also the footer is actullay good as quiz 0002 is on O3, so the footer is correct. The only thing is that there is no soccer example or analogy anymore, but there is still a statistics example. A new subagent that I would like is a preference reviewer, which checks if the lesson follows the PREFERENCES.md file. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/preference-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The soccer analogies were cut in a review pass and never replaced, so a preference-reviewer now checks the draft against every wish in PREFERENCES.md, one by one, after the lesson-reviewer loop, and requires a missing field such as soccer to come back as a working analogy rather than be dropped.

## Major review

**Run:** bench/runs/c3-split/20261116-015134-agent-architecture-m30-r1

**Live tries:**

For the live tries I asked for a 15 minute lesson on how agents divide to work on a task. The length is 1.15, which is the longest we have seen. The section times add up to 15 minutes. The facts in the lesson come straight from anthropics article and site it accordingly. All of the calculations are correct. It also used my preferences better. One example is a proof that shows parallel time can never be slower than sequentual time which I really liked. The soccer analogy does well and is not confusing. One flaw is that a definition is missing a space after the colon (“at the same time):”Breaking”.

### Lesson

#### Technical correctness and facts

Rating: 4

All of the numbers are correct. For example, the call example totals 2,100 + 3,600 + 5,100 + 6,600 = 17,400, and the formula n·S + r·n(n−1)/2 is proven to be correct. The figures are also drawn to scale. which is great. The lost in the middle claim is correct and backed up by sources. The only reason a point is taken off is because the worked example puts traning status in a saved note. This is bad because a studnets claim can become a fact if nobody validates it. A database read by a tool will help solve this issue. 

#### Pedagogy

Rating: 4

This lesson follows my PREFERENCES.md extremely closely. All of the sections have a concrete example which is very nice. There are math proofs and statistical explanations throughout the lesson. There is also an example in python and an everyday life analogy. There is a point off for the same reason in c1 as the socceranalogy is a little confusing and forced with the coach who gets amnesia. 

#### Alignment with the learning goal

Rating: 5

The lesson aligns with O3 perfectly. What is kept between steps, what is saved between sessions, and how a correct page is found in a manual is in sections 3, 4, and 5 of the lesson plan. The worked example includes the makerspace scenario which is involved with the leartners background. Also, the cost budget is considered throughout. 

#### Overall quality

Rating: 5

This lesson is very well done and has a length ratio of close to 0.89. This is the closest the length ratio has been to one. The section times add up to 30 minutes and all of the examples and facts in the lesson are correct. It also does a very good job at following preferences and the footer at the bottom points to the correct quiz. The only bad thing was the step back on safety wit hthe saved note example.

### Compared with the previous step

c3 performs better than c2 on length, preferences, and lesson coverage. It did mess up on the safety points, so the score of 5 from x2 dropped to a 4 for technical correctness. Length rose from .78 to .89. The keyword search is now present in c3. The lesson also adds more material that fits me with worked and concrete examples and proofs. One thing that got worse was that in the earlier c3 rounds they kept training status in a database read by a tool as safety procesdures should come from an official record. In the new lesson, the safety is a saved note, which is not offical. The analogiesa re also slightly weaker in this c3 as the amnesiac coach is a confusing analogy for me that I stated in c1. The split model was a lot more expensive and took more time. Teaching cost went to $2.45 for c3 compared to $1.69 for c2, which is a 1.45x increase. It also took 12.4 minutes compared to 8.2. I think this increase was worth it for length and and coverage but not reliability.

### What the next step should fix

The most important next step is that the safety rule should come from an official safety document than a saved note. There should be a checker to make sure this rule is never breached. Secondly, the analogies need to be clear and consistent. One thing it could do would be to use the same analogy throughout the lesson. The amnesiac soccer coach seems like a stretch and can be hard to picture and seems weird. A checker could also be used to verify links and not just quiz preferences. I would keep the lesson reviewer as the length went from .55 to .78 in c2. I would keep the reference checker as it fixed the false footer and corrected the lesson number. I would drop the lesson editor as it fixed the notes contradiction but brought in the safety issue. I would keep the preference reviewer as it brought more analogies and kept worked examples. I would keep the quiz and grade reviewers from c2 as well.
