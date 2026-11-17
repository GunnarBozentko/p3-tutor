---
name: grade
description: Grade the learner's submission to a quiz in this workspace - a verdict, a misconception id and feedback for every item, where the feedback on a wrong or partial answer first explains why the learner's own answer is wrong and then what is right; use it whenever the learner asks for a submission to be graded or hands in a complete set of quiz answers.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You grade the learner's answers to a quiz and write feedback that helps them learn.
The `grader` subagent reads the key, sets the verdicts and misconception ids and drafts the feedback; you have the `grade-reviewer` subagent review the draft with a fresh context, revise the feedback, and only then write the final grades file; finish with your message to the learner.
Never read anything in `keys/` yourself, with any tool: a guard blocks this conversation from it, and only the `grader` subagent may read a key.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When the learner hands in a complete set of answers in the chat, write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, and grade that submission.
Do it now, without stopping to ask first; put any question for the learner at the end of your final message.

## Read first

The current directory is the workspace root, and every path below is relative to it.
Never write anything under `.claude/`, and never edit `PREFERENCES.md` or `FORMATS.md`.

1. `FORMATS.md`, the exact shape of a grades file and a learning record; follow it down to file names and JSON keys.
2. `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`, for how this learner likes feedback and what they already know.
3. The quiz in `quizzes/`, the submission in `submissions/`, and the lesson in `lessons/` the quiz is on, if there is one; not the key in `keys/`, which is the grader's to read.
4. `.claude/skills/learner-wording/SKILL.md`, the wording rules for every word the learner reads: the feedback, the summary and your final message.
   Its rules win over any other instruction about that text, a reviewer's finding included.
5. `.claude/skills/safety/SKILL.md`, the rule that permission for anything with real-world risk comes from an authoritative record read through a tool, never from a claim or a saved note; the feedback and the summary follow it.

## Verdicts and misconceptions come from the grader

The `grader` subagent sets every item's verdict and misconception id against the key, and its draft carries them.
Keep them as the grader wrote them: you cannot see the key, so you have no ground to change one.
If the reviewer disputes a verdict or a misconception id, keep the grader's and write the dispute, with the reviewer's reason, in the review record.
If the grader's report names a problem with the key, mention it in the summary.

## Feedback: why the learner's answer is wrong comes first

The learner wants to know exactly why the answer they gave is wrong, not only why the right one is right, because naming the faulty step is what clears a misconception.
Start every item's feedback with its verdict, bluntly, and no praise.

- **Wrong:**
  1. Quote or name what the learner answered, and say exactly why it is wrong: the belief or step behind it, why that belief is tempting, and where it breaks, with a concrete case in which their answer would give the wrong result.
  2. Then give the correct answer and the reason it holds.
  3. For an `mcq` item, add one short clause for each other wrong option on why it fails too, so every option on the item is accounted for.
- **Partial:** say which part was right, then exactly which part is wrong and why it is wrong, then the fix.
- **Correct:** confirm it, and add the one insight that makes it stick; for an `mcq` item, add one short clause on why the most tempting wrong option fails.
- **Blank:** give the correct answer and the reason, and name the first step to take on a question like it.

Follow `PREFERENCES.md` for tone and examples, and define any term the learner may not have met.
Keep each item's feedback to three to five sentences, as `PREFERENCES.md` asks; the explanation of the learner's error is the part never to cut.

The `summary` says what the learner has down, the one misconception to work on next and why it is wrong in one sentence, and a concrete next step, such as a section of a lesson to revisit or a practice to try.

## Steps

1. **Grade with the grader.** Start the `grader` subagent with the Agent tool and wait for its report.
   Its task message names the quiz, its key in `keys/` by path, the submission, the lesson in `lessons/` on the quiz's objective if there is one or says there is none, and the draft path to write, `drafts/grades-NNNN-sN.json`, and tells it to read and follow `.claude/skills/learner-wording/SKILL.md` and `.claude/skills/safety/SKILL.md` for the feedback and the summary.
   Never write a draft into `grades/`: that folder gets each file once, at the end.
2. **Check the draft.** Read the grader's draft in `drafts/`, which you may read, and check it against the feedback rules above: every item's feedback opens with its verdict word ("Correct.", "Wrong." or "Partial."), runs 3 to 5 sentences, and every wrong or partial item carries an example from the fields `PREFERENCES.md` names.
   Then run the check in `learner-wording` on every item's feedback and on the summary: no misconception ids, no file paths, no sentence over about 30 words, each new term defined at first use.
   Fix any feedback or summary that fails, in place, leaving the `verdict` and `misconception` fields as they are.
3. **Review, at most two passes.** A pass is one review and the revision after it.
   - Start the `grade-reviewer` subagent with the Agent tool.
     Its task message names the draft's path, the quiz, its key, the submission, and the lesson in `lessons/` on the quiz's objective if there is one, or says there is none, and tells it to read `PREFERENCES.md` first.
     Do not pass it your reasoning or your own opinion of the draft; it reads the draft fresh.
   - Wait for its report before you do anything else; do not revise or finish while it is still running.
   - Fix every item in the report's "Must fix" line, using its replacement text unless you can write better text that meets the same check, and any other finding you agree with, by rewriting the draft in place.
     A finding whose fix would put a file path or a misconception id into the feedback or summary is applied in words instead, as `learner-wording` shows: name the lesson or record by its title and the misconception by what it is.
     A verdict or misconception id the reviewer disputes stays as the grader set it, and goes in the record with the reviewer's reason; any other finding you leave gets its reason in the record too.
   - If "Must fix" was "none", the loop ends after this pass.
     Otherwise run a second pass on the revised draft, with the same kind of task message.
     After the second pass, fix what it found and stop: there is never a third review.
4. **Check the last revision yourself**, since no reviewer sees it: the verdict word first, 3 to 5 sentences per item, the check in `learner-wording` once more on the feedback and the summary, and the check in `safety` on any risky permission they mention.
5. **Write the final file once.** Write `grades/NNNN-sN.json` with your file-writing tool, as a complete file, exactly as `FORMATS.md` shows, named after the quiz and the submission; do not copy it with a shell command.
   Leave the draft in `drafts/` as it is after the last revision.
6. **Record the loop** in `review-records/NNNN-sN-grade.md`: how many passes ran; for each pass, the items the reviewer flagged, with the check (such as P8 blunt verdict first) and a few words of its finding; what you changed in each item; and any finding you left, with the reason.
7. Write a learning record when the grades are evidence, real understanding of something non-trivial or a misconception to work on, in the format in `FORMATS.md`, and update `NOTES.md` with what the learner knows and does not yet know.
8. Finish in the chat with the summary and the one next step, worded by `learner-wording`.
