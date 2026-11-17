---
name: learner-wording
description: The wording rules for every piece of text the learner reads - lesson prose, grade feedback and summaries, and chat messages - no misconception ids or file paths, sentences under about 30 words, new terms defined at first use, and feedback that opens with its verdict. The grade and teach skills apply it before they write anything the learner reads.
user-invocable: false
---

# Learner-facing wording

These rules cover every piece of text the learner reads: the visible prose of a lesson, each item's `feedback` and the `summary` in a grades file, and every message to the learner in the chat.
They do not cover what only the tutor and the scripts read: JSON keys and fields such as `misconception`, `objective` or `id`, HTML attributes such as `href` and meta tags, review records, learning records and `NOTES.md`.

Apply them as you write, then check the text against each rule before the file is final or the message is sent.

## 1. No misconception ids

Never put a misconception id (`M1`, `M4`, ...) in text the learner reads; the learner has never seen the list those ids come from.
Name the misconception itself in plain words instead.

- Not: "Work on misconception M4 next."
- But: "Work next on the belief that a p-value is the chance the null hypothesis is true; it is the chance of data this extreme if the null were true."

The id still goes in the grades file's `misconception` field, which the learner does not read.

## 2. No file paths

Never put a file path, a folder name or a file name (`lessons/0002-hypothesis-tests.html`, `learning-records/`, `keys/0001.json`, `NOTES.md`) in text the learner reads.
Point to things by what they are called and what is in them.

- Not: "Revisit `lessons/0002-hypothesis-tests.html`, section 3."
- But: "Revisit the section on reading a p-value in your lesson on hypothesis tests."

A lesson may still link to a page or an asset in an `href`; the link text the learner sees follows this rule.

## 3. Sentences under about 30 words

Keep every sentence under about 30 words.
A sentence that runs longer usually holds two ideas: split it at the "and", "because" or "which" that joins them.

- Not (43 words): "You chose b, which reads the p-value as the probability that the null hypothesis is true, and that reading is tempting because both are probabilities about the null, but the p-value assumes the null is true and measures how surprising the data are."
- But: "You chose b, reading the p-value as the probability that the null is true. That reading is tempting, because both are probabilities about the null. In fact the p-value assumes the null and measures how surprising the data are."

Splitting a sentence never drops its content: the explanation of the learner's error stays whole.

## 4. Define each new term at first use

The first time a term appears that the learner may not have met, define it in a clause in the same sentence or the next one.
Use `NOTES.md`, the learning records and `GLOSSARY.md` to judge what the learner already knows; a term they have used correctly needs no definition.

- "The test uses the standard error, the spread you would expect in the sample mean from sample to sample."

## 5. Feedback opens with its verdict

Each item's feedback in a grades file opens with its verdict as the first word: "Correct.", "Wrong." or "Partial.", then the reason.
Nothing comes before the verdict: no restating of the answer, no praise.

## The check

Before a file the learner reads is final, or a message is sent, go through it once for each rule:

1. Search the text for `M` followed by a digit; replace each id with the misconception in words.
2. Search it for `/`, `.json`, `.html` and `.md`; replace each path or file name with what the thing is called.
3. Count the words of any sentence that looks long; split each one over about 30.
4. Find each term the learner may not know; define it at its first use.
5. In grades, check that every item's feedback starts with its verdict word.
