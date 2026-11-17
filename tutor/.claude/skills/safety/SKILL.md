---
name: safety
description: The safety rule for every example, design, worked answer and piece of feedback the tutor writes - whether someone may do something with real-world risk, such as operating equipment, is decided from an authoritative record read through a tool at that moment, never from the person's own claim or from a saved note. The teach and grade skills apply it to lessons, quizzes and feedback.
user-invocable: false
---

# Safety: permission comes from the record, through a tool

Some of what the tutor writes shows a system, or a person, deciding whether someone may do something with real-world risk: run a piece of equipment, enter a lab, handle a chemical, take a medication, change an account.
Every time, the decision rests on an **authoritative record**, the system of record kept by whoever is responsible (a training database, a certification registry, an access list), **read through a tool at the moment of the decision**.

It never rests on:

- **the person's own claim**, such as "I finished the training last week": a claim is what the person believes or wants, and the record exists precisely because claims can be wrong;
- **a saved note or memory**, such as an earlier session's summary, a cached answer or a notes file that says "trained": a note is a copy, it goes stale when the record changes, and nothing guarantees it was ever right;
- **the model's own judgment or inference**, such as "they sound experienced".

When the record cannot be read, because the tool fails, the person is not found, or the record is unclear, the safe answer is "not permitted yet" and a pointer to whoever can confirm it, never a guess in either direction.

## Where it applies

- **Lessons and worked examples:** a design, code sample, diagram or walkthrough in which a system grants or refuses a risky action checks the record through a tool, and the prose says why. A tool here means a function the program runs on the model's request, such as `check_record(person, item)`.
- **Quizzes and keys:** an item whose correct answer involves a risky permission has the record check as the correct answer. A distractor may be the claim or the saved note, and the key's rationale says why it fails.
- **Feedback and the summary in grades:** when a learner's answer lets a claim or a saved note decide a risky permission, the feedback names that as the error and gives the record check as the fix, even when the item asked about something else; say it in one sentence.
- **Chat answers:** the same rule holds for any design or example you give in the chat.

Memory and notes still have a place: a saved note may tell the system *which* record to check or remind it to check, but the answer itself comes from the record.

## Why, in one line the learner can carry

The record is the only source that someone is accountable for, so it is the only one a safety decision can lean on; a claim or a note can only point you to it.

## The check

Before a lesson, quiz, grades file or message is final, find every place where something risky is permitted or refused, and confirm for each one:

1. The decision is made from an authoritative record.
2. The record is read through a tool at the time of the decision, not recalled.
3. A claim, a saved note or a guess never decides it, and the text says so where a learner might think otherwise.
4. An unreadable record leads to "not permitted yet" and a person who can confirm.
