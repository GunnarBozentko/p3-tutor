# Evaluation report

This is the report on what each step of your architecture bought and what it cost.
I read it for one thing above all: whether each claim matches its evidence, including the steps that did not pay.
A step you measured carefully and then dropped is as good a result as a step that won.

Three kinds of material go here.
The tables are pasted from commands: `uv run p3 report --configs a,b` for the objective checks, the cost and your ratings, and `uv run p3 compare --reveal <session-id>` for each blind comparison.
Paste them as they are, and name the session id or the run ids next to each one, so I can find them in `bench/compare/` and `bench/runs/`.
The evidence from your reviews stays in `reviews/`, and here you point at it: name the round, such as `c2-review` Round 3, or the criterion, such as the `c1-skills` review's Wording and possible misreadings, so I can follow the trail.
The prose is yours.

Each section ends with a marker line.
Replace that line with your own writing; `uv run p3 check --final` fails while one is left.

Words used below.
**Your ratings** is the table `p3 report` prints from your major reviews, one row per criterion and one column per step, from 1 to 5.
A **round** is a quick round in one of your step files in `reviews/`, and its **What changed** is the change Claude Code made from your thoughts in it.
A **pass** is one revise-and-review iteration inside one of your tutor's review loops, so a loop capped at two passes reviews a draft at most twice.
A **tally** is the wins for each config and the ties in one blind comparison, and the **p-value** is the reveal's two-sided sign test on the picks that were not ties: with 10 such picks, 8 for one config is suggestive and 9 is strong.
**Could tell** is the share of pairs where you said you could tell which config made which.
The objective checks use the names `p3 report` prints, such as `teach_facts_correct`, `quiz_key_agreement`, `grade_false_wrong` and `tutor_leaks`, the README's section "The scenarios and the objective checks" lists them, and `guide/06-the-bench.html` ("The headline numbers") says what each one measures.
**Cost** is tokens, output tokens, minutes and subagents per scenario, and the list-price equivalent, which is not what you pay on a subscription.

---

## 1. The baseline, `c0-baseline`

Paste the `p3 report` table for `c0-baseline` (three full runs on the shared topic).

The 3 run ids are 20261109-230030-agent-architecture-m30-r1, 20261109-230838-agent-architecture-m30-r2, and 20261109-231445-agent-architecture-m30-r3.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.63 (0.59-0.66) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 646.2k (636.1k-656.6k) | 25.2k (21.2k-28.6k) | 3.4 (2.7-4.4) | 0.7 (0-1) | 0.54 (0.50-0.57) |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 167.6k (148.7k-199.9k) | 5.4k (4.6k-6.2k) | 0.8 (0.7-1.0) | 0 | 0.19 (0.17-0.20) |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 288.4k (263.7k-302.3k) | 7.1k (7.0k-7.3k) | 1.0 (1.0-1.1) | 0 | 0.33 (0.32-0.34) |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 575.0k (536.4k-602.0k) | 9.4k (9.1k-9.7k) | 1.8 (1.5-2.3) | 0 | 0.63 (0.60-0.66) |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.68M (1.66M-1.70M) | 47.1k (42.2k-51.1k) | 7.1 (5.9-7.9) | 0.7 (0-1) | 1.68 (1.62-1.76) |

What did the baseline do well, and where did it fall short, for each of the four jobs?
Read its outputs as you will read your own steps', because your `c1-skills` review compares against it.
Which of the gaps in `KNOWN-GAPS.md` did you see in your own runs, and did you find one that is not listed?
Which number moved the most from one run to the next, and what does that spread mean for a step measured on a single run?

For the teach component, the baseline did well on the content as the key facts present and correct facts each scored a 1.00. The length ratio ranged from .59 to .66 which is quite low is we want the length ratio between .6-1.5. This matches that I said the length is short in KNOWN-GAPS.md. The quiz key agreed on all the questions and performed well. The gradign performed very well as Verdict agreement was 1.00, false wrongs were 0.00, and misconception hits were 1.00 on both submissions in all three runs. Tutor perforemd the weakest on the metrics. Behavior met averaged at .56, and the length of the tutor's responses were over the expected amount of 250 words, as they were around 300 words. We saw the gaps of the tutor responses being long and the legnth of the lessons being short in my own runs. I did not see any gap of the tutor answering above the learners level. The number I saw moved the most was the minutes of the lesson. Teach minutes moved the most, from 2.7 to 4.4, about 50% of the mean. This mean the spread is quite large for the timing of these lessons, and it can vary greatly. 

---

## 2. Step 1: `c1-skills` against `c0-baseline`

### What changed

Name the rounds that built this step, such as `c1-skills` Rounds 1 to 4, and the inventory entries of the skills they added; the trail from thoughts to change to outcome is already in `reviews/` and `reviews/components.md`, so do not retell it here.
Then what you put in `PREFERENCES.md`, and anything about how the four skills work together that no single inventory entry says.

c1-skills was built with 4 rounds. The quiz was added in round 1 and then changed in round 2, tutor was added in round 3, and grade was added in round 4. The fourth skill teach was not changed and is the same as the c0-baseline. each has an inventory entry in reviews/components.md. In PREFERENCES.md I asked for a simple example, and then a worked example at first. I asked for analogies and code examples when appropriate and for each new term to be defined the first time it appears in a lesson. I asked for statistics, soccer, and everyday tasks/situations for analogies. For feedback, I wanted shorter paragraphs of 3-5 sentences and also for it to be blunt and to the point. I wanted formal direct replies without filler. In the baseline, the /teach skill handled everything, but now we have 4 individual skills. The skills hand of fto each other after each skill is completed, with teach quiz tutor and then grade. Teach always writes the lesson. The nquiz gives 10 questions, with the first 5 being definition questions and the second 5 being application questions. Tutor doesnt answer quiz questions, but will help guide the user if it has any questions. Grading the ngrades the quiz and gives feedback. All skills use PREFERENCES.md, but not all equally. The teach skill used soccer and and everyday analogies, while the grade skill used no alaogies and ran long. The quiz skill is weak as it write the questions without checking them against each other, so one question can give the answer away to another one. 

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,c1-skills`: the objective checks, the cost per job, and your ratings.

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

The runs are: 20261112-040647-agent-architecture-m30-r1. For c0-baseline, it's the three full runs 20261109-230030-agent-architecture-m30-r1, 20261109-230838-agent-architecture-m30-r2 and 20261109-231445-agent-architecture-m30-r3.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.63 (0.59-0.66) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |
| `c1-skills` | 1 | 1.00 | 0 | 0.59 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 646.2k (636.1k-656.6k) | 25.2k (21.2k-28.6k) | 3.4 (2.7-4.4) | 0.7 (0-1) | 0.54 (0.50-0.57) |
| `c1-skills` | 1 | 751.3k | 29.1k | 2.8 | 2 | 0.59 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 167.6k (148.7k-199.9k) | 5.4k (4.6k-6.2k) | 0.8 (0.7-1.0) | 0 | 0.19 (0.17-0.20) |
| `c1-skills` | 1 | 144.1k | 5.9k | 0.7 | 0 | 0.18 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 288.4k (263.7k-302.3k) | 7.1k (7.0k-7.3k) | 1.0 (1.0-1.1) | 0 | 0.33 (0.32-0.34) |
| `c1-skills` | 1 | 240.6k | 7.2k | 0.9 | 0 | 0.29 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 575.0k (536.4k-602.0k) | 9.4k (9.1k-9.7k) | 1.8 (1.5-2.3) | 0 | 0.63 (0.60-0.66) |
| `c1-skills` | 1 | 631.4k | 9.0k | 1.4 | 0 | 0.49 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.68M (1.66M-1.70M) | 47.1k (42.2k-51.1k) | 7.1 (5.9-7.9) | 0.7 (0-1) | 1.68 (1.62-1.76) |
| `c1-skills` | 1 | 1.77M | 51.2k | 5.8 | 2 | 1.55 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

### Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | - | - | - |
| Lesson | Pedagogy | 4 | - | - | - |
| Lesson | Alignment with the learning goal | 5 | - | - | - |
| Lesson | Overall quality | 4 | - | - | - |
| Quiz | Difficulty | 2 | - | - | - |
| Quiz | Coverage of the lesson's core | 4 | - | - | - |
| Quiz | Wording and possible misreadings | 3 | - | - | - |
| Quiz | Writing quality | 3 | - | - | - |
| Quiz | Alignment with the learning goal | 5 | - | - | - |
| Feedback | Useful | 4 | - | - | - |
| Feedback | Explains enough | 5 | - | - | - |
| Feedback | Personalized to how I like things explained | 3 | - | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 5 | - | - | - |

### What the step bought and what it cost

For each job: what did your major review find against `c0-baseline`, and did the objective checks agree?
Where they disagree, which do you believe, and why?
`c1-skills` is also the first config with your `PREFERENCES.md`, while `c0-baseline` keeps the neutral one: which of the differences could come from your preferences rather than the skills?
What did the step cost per scenario, and was the gain worth it?
Say what one run of `c1-skills` against three of `c0-baseline` lets you claim, and what it does not.

For the teach skill, we found that the c1-skills lesson performed as accurate as the baseline. The worked example was useful, the arithmetic was correct, and the misconception box was useful. The length-ratio was .59 which was at the bottom of the baselines range of .59 to .66, and under the .6 floor. The teach skill didnt change so the differences would be caused from PREFERENCES.md.

For the quiz skill, it followed my directions of 5 definition questions and 5 application questions. The quiz was somewhat easy though as some questions only had one sensibile option, whcih was the correct one. The objective checks had no change as ke yagreement was 1.00 and there were no ambiguous questions. 

The grade skill did its job well and explained why each answer was incorrect and wh ythe correct answer is the only one that works. The objective checks were all good as the verdict agreement was 1.00 and there were no false wrongs and misconception. This is the same as the baseline. The feedback is blunt and skips praise, but the responses are long. 

The tutor skill refuses to give the answers to the quiz questions which is good. It also used soccer and everday analogies which was in my PREFERENCES.md. The issue is that similar to the baseline, the hints it gives can narrow down the answers to the given question. he behavior-met score of 0.50, against the baseline’s 0.50 to 0.67, agrees with my review that the tutor still falls short on about half the probes.

For preference vs skills, it is hard to tell what effects were from skills vs preferences as they both had an effect on the same things. We can tell from teach though as the skill was not changed. The analogies from soccer and everyday things were from my preferences. The chnaged quiz format was from my skill, while the tone could be from my skill or my preferences. To truly test what the cause was, I would need to run a c1-skills without the preferences and with. 

For cost, c1-skills was cheaper at $1.55 against the baselines average of $1.68, with a range from $1.62 to $1.76. It also took 5.8 minutes to run against 7.1 minutes of the baseline. Teach was the only job that got more expensive, and with 2 subagents against the baseline’s 0.7, that’s likely variance or longer input from my preferences. 

What one run against three can let me claim is that no objective check got worse. All the c1-skill metrics are within the baselines spread. The structural features I added also showed up in the full run and my live try. The cost difference between the baseline and my c1-skills is probably real but we can not confirm this wth just one run. 

---

## 3. Step 2: `c2-review` against `c1-skills`

### What changed

Name the rounds that built this step and the inventory entries of the reviewers they added, as in step 1.
Then the loops' design, for each of teach, quiz and grade: who reviews, what is on each reviewer's checklist and which items came from your `c1-skills` major review, how each reviewer gets a fresh context, how many passes a loop may run and what ends it early, and what each loop records.
Then one design choice you could have made the other way, such as one reviewer against several, a cap of one pass against three, or a reviewer that edits against one that only reports, and why you chose as you did.

TODO: the rounds and entries, and the design of your review loops.

### The loops as they ran

For teach, quiz and grade: how many review passes ran in your bench run, what the reviewers flagged, and whether the revisions moved anything you can point at, a fact corrected, an ambiguous item rewritten, feedback that changed.
The loop records in the run's outputs are the evidence; name the files.

TODO: what the review loops did in the run.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c1-skills,c2-review`.

TODO: paste the report tables.

### What the step bought and what it cost

Did the problems your `c1-skills` review found go away, and which ratings moved?
Which loop earned its cost and which did not?
If a loop ran several passes and the final output was no better than the first draft, say so, because that is the finding.

TODO: your judgment of step 2.

---

## 4. Step 3: `c3-split` against `c2-review`

### What changed

Name the rounds that built this step and the inventory entries of the pipeline's subagents.
Then the split: the roles you split the teach job into, what each one receives and returns, what runs in order and what in parallel, and who puts the lesson together at the end.
Why this split and not a smaller one, and what did you try that you took out again?

TODO: the rounds and entries, and the design of your teach split.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c2-review,c3-split`.

TODO: paste the report tables.

### What the step bought and what it cost

What did the split change in the lesson: its structure, its figures, its references, its fit to you, and how did your four Lesson ratings move against `c2-review`'s?
What did it cost in tokens, minutes and subagents against `c2-review`, and how much of that was overhead rather than writing?
Each step has one run, so say how confident you are, and what would change your mind.

TODO: your judgment of step 3.

---

## 5. `final` against `c0-baseline`, with repeats

### What went into `final`

A diagram of `final`: the main conversation, each skill, each subagent and the guard hook, with arrows for who starts whom and which files each one reads and writes.
ASCII art in a code block or a Mermaid block are both fine; for example:

```
/quiz (skill, main conversation)  writes drafts/0002.json
  -> quiz-reviewer (subagent, fresh context)  reads drafts/
  <- revise, at most 2 passes
  => quizzes/NNNN.json, keys/NNNN.json, review-records/NNNN-quiz.md
```

Draw yours, all four jobs, and delete the example.

TODO: your diagram.

What did you keep from each step, what did you drop, and why?
Point at the inventory entries in `reviews/components.md` rather than repeating them.
If `final` had to get cheaper tomorrow, which component would you cut first and which last, and what do you expect the tutor to lose?

TODO: what `final` is made of, and what you would cut first.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,final`, with three scored runs of each.

TODO: paste the report tables.

### What the repeats let you claim

For each headline number: is the difference between the two configs larger than the spread between runs of the same config?
Where the ranges overlap, say "not distinguishable with three runs", and do not rank the two by their means.
Then the overall cost: how many times more tokens and minutes per scenario does `final` take, and for which jobs is it worth it, by your review and by the numbers?

TODO: your reading of `final` against the baseline.

---

## 6. The ablation

Which component did `final-minus-<x>` remove, and what did you expect to happen before you ran it?
Paste `uv run p3 report --configs final,final-minus-<x>`.
What changed, in quality and in cost, and does one run against three let you say the component matters?
If you looked at its outputs, what did you see that the numbers do not show?

TODO: your ablation, its prediction, its table and your reading.

---

## 7. The guard

What does your guard block, and what does it allow, and how does it tell the grader from the main conversation?
Why is it a PreToolUse hook in `tutor/.claude/settings.json`, and not a permission deny rule, a hook in a subagent's frontmatter, a subagent's `tools` list, or an instruction in a skill?
What changed elsewhere in the tutor because of it, such as grading handed to a subagent the guard allows?
Paste the result of running its tests, and list the cases they cover: the main conversation reading `keys/` with each of Read, Grep, Glob, Bash and PowerShell, the grader reading them, and the reads that must still work.
Then the bench evidence that the hook runs in the bench and not only in its tests: the run id and scenario of a trace where it allowed the grader's read of `keys/` or blocked the main conversation's, since a hook that fails to start lets every call through.
Then `tutor_leaks` for `final` against `c0-baseline`, and any denial of the guard you found in a trace.
Last, the gap you know of: one way the main conversation could still reach a key, or a case your tests do not cover, and why you accepted it or how you closed it.

TODO: the guard, its tests and the evidence.

---

## 8. The blind comparison

### `c0-baseline` against `final`

Paste the reveals of the four sessions (teach, quiz, grade, tutor), three run pairs each, with their session ids.

TODO: paste the four reveals with their session ids.

### Your open reviews against your blind picks

This is the check on your own bias, as lecture 24 checks a model judge's.
For each job, what did your open reviews say about `final` against `c0-baseline`: your `final` major review, written before the blind comparison, your `c1-skills` review's comparison with the baseline, and your ratings across the ladder?
Then, for each job, did the blind tally and your reasons agree with them?
Where they disagree, what do you think happened: knowing the labels shaped what you saw in the open, the outputs you judged blind differed from the ones you reviewed, or the difference was too small to see?
Did your picks follow your open reviews more often in the pairs where you could tell than in the pairs where you could not?
Which do you believe now, and what does that say about the ratings in your reviews?

TODO: your open reviews against your blind picks.

### A second blind comparison

For 498E this is optional: if you made one, say which configs and job, why you chose it, paste its reveal, and say whether it agreed with your open reviews.
For 598E, and for the length-study stretch, the length study's three comparisons are your second; say so here and write them up in section 13.
If you made no second comparison, say so in one line.

TODO: your second blind comparison, or why there is none.

---

## 9. The test topics

### The two topics

Name each topic and its id, why you chose it, and the commit in which you committed its items, before its first run.
If you fixed a real mistake in a topic after its runs, as `bench/own/README.md` describes, list the run ids you deleted, what you changed and why.

TODO: your two topics and their commits.

### Results

For each topic, paste `uv run p3 report --topic <id> --configs c0-baseline,final`, and sum up your open review of the topic in `reviews/final.md` in two or three sentences.

TODO: paste the tables for both topics, with your summaries.

### Did the architecture still pay off?

Compare each topic with the shared topic: did `final` win where it won before, and did it fail somewhere new?
Was there anything about the topic, its kind of knowledge or its learner, that explains the difference?
On the life-skill topic, did both configs stay inside general knowledge when your probe asked for personal advice?

TODO: your reading of the test topics.

### Your learning sessions against the bench

Your three learning sessions are in `reviews/final.md`.
Did the bench predict what you saw in them?
Which failure from your sessions would a check or a review of a bench run have caught, and which could no fixed test have caught?
Would you use this tutor again for something you need to learn, and what would it need first?

TODO: the bench against your sessions.

---

## 10. The judge check

Take ten decisions the judge made: for example ten tutor replies it marked met or not met, or ten fact verdicts from your lessons (the judge checks six facts in each lesson on the shared topic, so ten come from two lessons).
Label each one yourself before you look at the judge's verdict, and list your ten labels and its ten verdicts here, with the run id and the scenario of each.
How many of ten did you agree on?
Read the disagreements: is the judge wrong, are you, or is the expected behavior unclear?
What does that agreement mean for the judge numbers you reported above?

TODO: your ten labels, the agreement, and what it means.

---

## 11. A change that did not pay off

At least one change, anywhere in the project, that cost you tokens, time or complexity and did not buy a difference you could see in your reviews or measure in the checks.
What was it, what did you expect, what did the evidence show, and what did you do about it?
Name the round or the inventory entry where it shows.

TODO: the change that did not pay off.

---

## 12. The trade-offs

Paste your ratings across the whole ladder, from `uv run p3 report --reviews`, and the cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

TODO: paste the ratings and cost tables for the whole ladder.

Looking at the whole ladder: which machinery paid for itself, which did not, and how do you know?
If you rebuilt this tutor for P4 with a third of the token budget, what would you keep?
Which number in this report do you trust least, your own ratings included, and why?

TODO: your trade-offs.

---

## 13. The stretch

For 598E this is the rider, and its write-up goes here, with `PREREG.md` beside it.
Cover five things:

1. the option's name;
2. what you did, and the files that hold it;
3. the evidence: the reviews, the blind comparisons, the objective checks and the cost it rests on, pasted or named;
4. what that evidence lets you claim, and what it does not;
5. one thing you would do next, and what result would tell you it worked.

TODO: your stretch.
