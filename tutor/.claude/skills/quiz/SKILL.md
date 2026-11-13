---
name: quiz
description: Write a quiz and its answer key for the learner in this workspace, built in two parts - definition questions first, then application questions - on any topic; use it whenever the learner asks for a quiz or to be tested.
argument-hint: "Which objective, and how many questions?"
---

# Quiz

You write quizzes and their answer keys for the learner in this workspace.
Do the job yourself, in this conversation and in one pass, and finish with your message to the learner.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## Read first

The current directory is the workspace root, and every path below is relative to it.
Never write anything under `.claude/`, and never edit `PREFERENCES.md` or `FORMATS.md`.

1. `FORMATS.md`, the exact shape of a quiz file and a key file; follow it down to file names, numbering and JSON keys.
2. `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`, so the quiz fits this learner and their reason for learning.
3. The lessons in `lessons/` on the objective, and the earlier files in `quizzes/`, `keys/` and `grades/`, for what was taught and which misconceptions this learner has shown.
4. When no lesson covers the objective, search the web for a high-trust source on exactly that objective, read it, and build the quiz from it; say in your message that the quiz is ahead of the lessons.

## The shape of the quiz: definitions first, then application

The learner learns best by first checking that they can name and define each new part, and then using those parts on a case.
So every quiz has two parts, in this order:

1. **Definition questions.**
   Each one asks what one key term or component of the objective is, or what it does, in plain words.
   One term per item, the terms the objective cannot be understood without, taken from the lesson or the source.
   These are meant to be quick for a learner who read the lesson: recall, not a puzzle.
   Good shapes: an `mcq` "Which of these best defines X?" whose distractors are the definitions of neighbouring terms or a common misreading, or a `short` "In one phrase, what does X do?".
2. **Application questions.**
   Each one gives a concrete case, a scenario, a design choice, a small calculation, and asks the learner to use the defined ideas on it.
   Build each on terms the definition part already asked about, so the quiz goes from knowing the parts to using them.
   Make the cases ones this learner relates to, as `PREFERENCES.md` describes, and tie them to the mission where you can.
   Let difficulty rise gently through this part; one item may stretch the learner, and none needs knowledge they were never given.

How many of each: this learner wants longer quizzes, so a quiz has ten items, q1 to q5 definition questions and q6 to q10 application questions.
When the request asks for fewer than ten items, still write ten, and say in your message that the quiz is longer than asked because the learner prefers ten questions, half definitions and half application.
When the request asks for more than ten, use that number, with the first half (rounded down) definition questions and the rest application questions.

Give each part a clear start in the stems the learner sees: the first definition stem may begin "Definitions:" and the first application stem "Applying it:", but the stems must still each read as one complete question.

## Writing the items

- Every item serves the requested objective and carries its id.
- One question per item, complete on its own: a learner who knows the idea can answer it without the lesson open.
- Plain, exact wording: no double negatives, no "all of the above" or "none of the above", no trick wording.
- Give every number, unit and condition the answer depends on.
- No item gives away another item's answer; in particular, an application stem must not restate a definition that an earlier item asks for.
- Do not repeat the lesson's own practice questions.
- Types: `mcq` when the wrong answers are predictable misconceptions; `numeric` when a quantity is involved (state the unit in the stem and in `unit`); `short` when the learner should produce the idea in a word, a phrase or one sentence.
  Mix the types where the objective allows.

For `mcq` options:

- Three to five options, usually four, with ids `a`, `b`, `c`, `d`.
- Each distractor is plausible to someone holding the misconception it encodes; no joke options.
- Options of similar length, grammar and detail, so the longest or most careful option is not a giveaway.
- Vary the position of the correct option across items.
- Exactly one option is correct; check that no distractor is also defensible.

## Writing the key

Follow `FORMATS.md` for the key's shape, with the same number as the quiz.

- `answer`: the option id, the number in the item's unit, or the shortest complete reference answer for a `short` item.
- `accepted`: for a `short` item, other wordings that are just as correct.
- `tolerance`: for a `numeric` item, the absolute tolerance the stem's precision implies.
- `rationale`: why the answer is right, and, in a second sentence, why the most tempting wrong answer is wrong, so that feedback on a wrong pick can name the learner's actual error.
- `distractors`: each wrong option that encodes a misconception, mapped to that misconception's id; reuse ids the workspace already has.

## Steps

1. Pin down the objective, its id and the number of items, by the rule above.
2. Find the objective's core in its lessons or source, and list the key terms for the definition part.
3. Take the next number in `quizzes/`; the key gets the same number in `keys/`.
4. Write the quiz to `quizzes/NNNN.json` and its key to `keys/NNNN.json`, exactly as `FORMATS.md` shows.
5. Check: answer every item yourself from its stem alone, without the key, and rewrite any item where you hesitate or a careful expert could argue for a second answer.
   Check that the definition items come first, that the quiz file holds no answers, and that every item carries the objective's id.
6. Finish with a short message: the quiz's path, that it opens with definition questions and then applies them, and that it is ready when the learner is.
   Never put an answer in the message.

## Giving a quiz in the chat

When the learner wants to take a quiz in a live session, show its title and each item's stem and options, never anything from `keys/`.
Collect their answers, write them exactly as given to the next `submissions/sN.json` as `FORMATS.md` shows, and tell them it is ready to grade.
