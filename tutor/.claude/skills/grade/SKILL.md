---
name: grade
description: Grade the learner's submission to a quiz in this workspace - a verdict, a misconception id and feedback for every item, where the feedback on a wrong or partial answer first explains why the learner's own answer is wrong and then what is right; use it whenever the learner asks for a submission to be graded or hands in a complete set of quiz answers.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You grade the learner's answers to a quiz and write feedback that helps them learn.
You grade in this conversation, have the `grade-reviewer` subagent review the draft with a fresh context, revise, and only then write the final grades file; finish with your message to the learner.

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
3. The quiz in `quizzes/`, its key in `keys/`, the submission in `submissions/`, and the lesson in `lessons/` the quiz is on, if there is one.

## Verdicts

- Judge what the response means, not how it is worded: `correct` when it means what the key's answer means, even if oddly worded, misspelled, or reached by a valid route the key did not expect; the key's `accepted` list gives examples, not the only correct wordings.
- `partial` when part of it is right: the right method with a slip or the wrong unit, one half of a two-part idea, or the right answer with a stated reason or an added claim that is wrong.
- `wrong` when it misses the idea, contradicts it, or is blank.
- For `mcq`, compare the chosen option with the key; match written-out option text to its option.
- For `numeric`, the number is right within the key's tolerance (1% of the answer when the key gives none), after converting any unit the learner stated.
- If you are sure the key itself is wrong, grade against what is actually correct, and say so in the summary.

## Misconceptions

- Name a misconception id when the response shows that misconception: for `mcq`, the key's `distractors` entry for the chosen option; for other items, the misconception the answer or its reasoning shows, from ids the workspace already uses (keys, `NOTES.md`, learning records).
- Use `null` for a correct response, a slip, a blank, or a wrong answer that shows no known misconception; never invent an id.

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

1. Grade every item in the quiz, in order, including unanswered ones: verdict, misconception, feedback.
2. **Draft.** Write the grades to `drafts/grades-NNNN-sN.json`, in exactly the shape `FORMATS.md` gives for a grades file.
   Never write a draft into `grades/`: that folder gets each file once, at the end.
   Check the draft yourself first: every item's feedback opens with its verdict word ("Correct.", "Wrong." or "Partial."), runs 3 to 5 sentences, and every wrong or partial item carries an example from the fields `PREFERENCES.md` names.
3. **Review, at most two passes.** A pass is one review and the revision after it.
   - Start the `grade-reviewer` subagent with the Agent tool.
     Its task message names the draft's path, the quiz, its key, the submission, and the lesson in `lessons/` on the quiz's objective if there is one, or says there is none, and tells it to read `PREFERENCES.md` first.
     Do not pass it your reasoning or your own opinion of the draft; it reads the draft fresh.
   - Wait for its report before you do anything else; do not revise or finish while it is still running.
   - Fix every item in the report's "Must fix" line, using its replacement text unless you can write better text that meets the same check, and any other finding you agree with, by rewriting the draft in place.
     A verdict you keep against the reviewer's, and any other finding you leave, gets its reason in the record.
   - If "Must fix" was "none", the loop ends after this pass.
     Otherwise run a second pass on the revised draft, with the same kind of task message.
     After the second pass, fix what it found and stop: there is never a third review.
4. **Check the last revision yourself**, since no reviewer sees it: the verdict word first, 3 to 5 sentences per item, and every file the feedback names exists under that name.
5. **Write the final file once.** Write `grades/NNNN-sN.json` with your file-writing tool, as a complete file, exactly as `FORMATS.md` shows, named after the quiz and the submission; do not copy it with a shell command.
   Leave the draft in `drafts/` as it is after the last revision.
6. **Record the loop** in `review-records/NNNN-sN-grade.md`: how many passes ran; for each pass, the items the reviewer flagged, with the check (such as P8 blunt verdict first) and a few words of its finding; what you changed in each item; and any finding you left, with the reason.
7. Write a learning record when the grades are evidence, real understanding of something non-trivial or a misconception to work on, in the format in `FORMATS.md`, and update `NOTES.md` with what the learner knows and does not yet know.
8. Finish in the chat with the summary and the one next step.
