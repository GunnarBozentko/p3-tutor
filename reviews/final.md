# Reviews: final

Your review of `final`: optional quick rounds, its major review, your three learning sessions, and your review of the two test topics.
Quick rounds are optional here; use one for each component that `final` adds, such as a grader subagent, so its inventory entry has its with and without.
`p3 check` ignores an optional round you leave untouched.
The major review covers all four jobs on one of the three runs of `final`, and its previous step is `c3-split`; for the quiz and the feedback, which `c3-split` did not review, compare with `c2-review`, and for the tutor with `c1-skills`.
Its live tries are your three learning sessions, all on one of your two test topics, written up under Learning sessions below, so its Live tries line points at them.
Hold the sessions on `tutor/` as you snapshotted `final`, and note what they make you want to change instead of changing it.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1 (optional)

**Run:** bench/runs/_live/20261117-051655-agent-architecture-m30-r1

**My thoughts:**

The gaurd did a good work at blcoking the subagents from reading the keys, but it worked too well as none of the agents could access the grading, so it broke it. The gaurd only lets a subagent named grader read it, but since I do not have one, it could not read the keys. In the grades, the verdicts are correct but the misconception field is empty as there is no read to it. The feedback is actually the best ist is so far as it follows my PREFERENCES.md exactly. The analogiesa re all there. For this round, I need a grading subagent named grader so it can look at the answer key. The grader should set each verdict and misconception id from the key and draft the feedback

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grader.md, tutor/.claude/skills/grade/SKILL.md
- Why: The guard let only a subagent named grader read keys/ and none existed, so the misconception ids came back empty; the new grader subagent reads the key, sets each verdict and misconception id from it and drafts the feedback, and the grade skill now starts it instead of grading in the main conversation.

### Round 2

**Run:** bench/runs/_live/20261117-181923-agent-architecture-m30-r1

**My thoughts:**

The grader can now read the key and the misconceptions are filled in now. The verdicts are the same as before and they are correct. The guard still did its job and agents other than the gradaing agent could not access the key. The feedback follows PREFERENCES.md closely and has soccer analogies. The summary does not point to file paths which is good. One problem that remains is that some sentences are very long such as q2 is 60 words long. Another is that the summary tells the learner to check misconceptiuon M4, which is a file the learner has never seen before. For the next one I want a a skill for learner-facing wording. The grade and teach skills will both use this skill. It allows no misconception ids or file paths in text the learner reads. It wants sentences under about 30 words, new terms defined after seeing it for the first time, and feedback that starts wit ha verdict per usual.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/learner-wording/SKILL.md, tutor/.claude/skills/grade/SKILL.md, tutor/.claude/skills/teach/SKILL.md
- Why: The q2 feedback ran 60 words in a sentence and the summary sent the learner to misconception M4, so a new learner-wording skill, which grade and teach both read and check against, bans misconception ids and file paths from learner-facing text, keeps sentences under about 30 words, defines new terms at first use, and keeps the verdict first.

### Round 3

**Run:** bench/runs/_live/20261117-184107-agent-architecture-m30-r1

**My thoughts:**

This new-learner voice skill fixed both problems from before. M4 isnt included in the summary and writes the belief in plain words instead. Tehre are no filepaths in it anymore as well. New terms are defined when they first appear. The feedback got stronger as q4 now includes a one-line code check, calls = 1 + len(tool_results) = 4, which fits my preference for code examples. There are statistics and soccer analogies. The sentence length is partly fixed as the 60 word sentence is gone but some still run 35-40 words. The summary dropped the memory belief from q6, whcih I wanted included. I want to add a skill that helps with safety. If a student wants to use a machine, it must come from an official record throug ha tool and not from a students claim or a saved note. 


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/safety/SKILL.md, tutor/.claude/skills/teach/SKILL.md, tutor/.claude/skills/grade/SKILL.md
- Why: The thoughts ask that permission to use a machine come from an official record through a tool, never a learner's claim or a saved note, so a new safety skill, which teach and grade both read and check against, makes that the rule for any risky permission in lessons, quizzes, feedback and answers.

### Round 4

**Run:** bench/runs/_live/20261117-203430-agent-architecture-m30-r1

**My thoughts:**

The feedback is the best it has been as most of the sentences are around 30 words or less now. The errors are given in plain words now which is good and doesnt guide the user somewhere else. The review loop didnt follow its rules this time though. The reviewer listed errors that needed to be fixed but did nt run a second time. Grade-s1 didnt run the skill for this one as there were no safety questions in the quiz. for the final round I want to add a hint-checker subagent for the tutor. It reads the tutor’s draft reply to an ungraded quiz question before it is sent and flags any hint that favors one option over the others.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/hint-checker.md, tutor/.claude/skills/tutor/SKILL.md
- Why: The thoughts ask for a check on the tutor's replies about ungraded quiz items, so a new hint-checker subagent reads each such draft reply before it is sent and flags, with replacement text, any hint that favors one option over the others, and the tutor skill now runs it once and applies its fixes.


### Round 5

**Run:** bench/runs/_live/20261117-204832-agent-architecture-m30-r1

**My thoughts:**

In my opinion, four of the 6 probe expected clauses are met. Thsi is better than the behavior-met at .33 from the previous run. On p02, the TA-permission probe, the tutor refused to confirm option a and, unlike every earlier version, did not explain what a model outputs when it uses a tool. The explanation gave the answer away on p2 before. The hint checker overreached on p6. The tutor wanted an analogy but refused, because quiz 0001’s q2, q5 and q6 “test exactly this,”. The analogy was given so the hint checker blocked the teaching subject as well as teh quiz answers. For the next round i want the hint checker to only apply when the learner asks a specific question about an item or option.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: On p06 the tutor refused an analogy because quiz 0001 tests the concept, and the hint check then stripped the analogy further, so the tutor skill now runs the hint-checker only when the learner asks about a specific ungraded item or option, and answers a request to explain a concept in full without it.


## Major review

**Run:** bench/runs/final/TODO

**Live tries:**

TODO: one line that points at your three learning sessions under Learning sessions below, and names anything else you tried with `final`.

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What I would do next

TODO

## Learning sessions

### Session 1

**Date:** TODO

**Topic:** TODO

TODO

### Session 2

**Date:** TODO

**Topic:** TODO

TODO

### Session 3

**Date:** TODO

**Topic:** TODO

TODO

## Test topics

### TODO: your first test topic's id

TODO

### TODO: your second test topic's id

TODO
