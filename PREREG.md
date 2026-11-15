# Pre-registration: the length study

This file is for 598E students, for whom the length study is the required rider, and for 498E students who chose it as their stretch.
Everyone else can ignore it or delete it.

A pre-registration is a claim you write down, with the analysis that will judge it, before you can see the answer.
Its value is that the claim can be wrong in a way anyone can check, and that you cannot bend it afterwards to fit the numbers.
A clear "no difference as large as the one I cared about" scores as well as a confirmation, so you have no reason to hedge.

**Git history is how I will know the order.**
Fill in sections 1 to 4 and commit this file before the first of the eighteen length-study runs.
`uv run p3 check --final` reads `git log` and confirms that the commit came first.
After that commit, do not edit sections 1 to 4.
If something must change, add a dated entry in section 6 and leave the original as it was.
Section 5 you write at the end, after the runs and the comparisons.

Each section that needs your words ends with a marker line.
Replace that line with your answer; `uv run p3 check --final` fails while one is left.

The design is fixed: two configs, three lengths, three teach-only runs in each cell, on the shared topic.

| | 10 minutes | 30 minutes | 60 minutes |
|---|---|---|---|
| `c1-skills` | 3 runs | 3 runs | 3 runs |
| `final` | 3 runs | 3 runs | 3 runs |

```
uv run p3 bench --config c1-skills --only teach --minutes 10 --repeats 3
uv run p3 bench --config c1-skills --only teach --minutes 30 --repeats 3
uv run p3 bench --config c1-skills --only teach --minutes 60 --repeats 3
uv run p3 bench --config final --only teach --minutes 10 --repeats 3
uv run p3 bench --config final --only teach --minutes 30 --repeats 3
uv run p3 bench --config final --only teach --minutes 60 --repeats 3
```

After the runs, one blind comparison per length, each pairing only the study's teach-only runs at that length, three pairs each:

```
uv run p3 compare c1-skills final --job teach --teach-only --minutes 10
uv run p3 compare c1-skills final --job teach --teach-only --minutes 30
uv run p3 compare c1-skills final --job teach --teach-only --minutes 60
```

`--teach-only` matters at 30 minutes, where the ladder's full runs of `c1-skills` and `final` hold a 30-minute lesson too; it keeps them out, so every length is paired the same way.
These three sessions are your second blind comparison of the project, beside `c0-baseline` against `final`, and you make no other on top.
The numbers for every cell come from one command:

```
uv run p3 report --configs c1-skills,final --teach-only
```

---

## 1. Hypothesis

One or two sentences: as the requested length grows from 10 to 60 minutes, which config loses more quality, in which measure, and why you expect it.
For example: "The single-agent `c1-skills` loses more than `final` as lessons get longer, because one context writing a 60-minute lesson drifts from the plan, so its `teach_facts_correct` falls further from 10 to 60 minutes, and `final` wins more of the blind pairs at 60 minutes than at 10."
It should be something you could be wrong about.

My hypothesis is that as the requested length grows from 10 to 60 minutes, the c1-skills agent will lose more quality on the length-ratio measurement compared to the multiagent final. This is because the single agent will write the lesson in a single context window and has no step to check the lessons length. The lesson-review agent looks over the lesson at the end to see if the length is enough. Quality loss means length-ratio is decreasing. 

---

## 2. The smallest difference that matters

Choose one primary measure now, so you cannot pick the better one afterwards, and say how large a difference in it would matter to a learner, and why that size.
Call it Δ (delta).

Know what three runs per cell can show before you choose.
There are three blind teach pairs at each length, and even 3 of 3 for one config has a two-sided sign-test p-value of 0.25, so no single length can settle a preference on its own.
Across all three lengths there are nine pairs: 8 of 9 gives a p-value of about 0.04, and 7 of 9 about 0.18.
An objective measure, such as `teach_facts_correct` or the judge's level fit, gives three numbers per cell, and you can see a difference only when it is larger than the spread between the three runs.
So choose a Δ that is large enough to matter and large enough for three runs to see.

My primary measure is the drop in teach_length_ratio. It is calculated by subtracting the mean ratio of the three 60 minute runs from the mean ratio of the three 10 minute runs. This is compared to the c1-skill's drop, minus the finals drop.

The delta I will use is .2, so if the c1-skills drop minus finals drop is greater than .2 then I will determine the difference as meaningful.

I chose this size because at 60 minutes, a .2 difference would result in a lesson that is 12 minutes shorter than the expected hour length. For shorter lessons it would be difficult to notice the missing material as it would only be 2 minutes missing of the time out of the 10 minutes projected. 0.20 also seems to be above the noise from runs we have seen in the past, so it should be a significant enough difference to determine if there is a real change. My three runs at 30 minutes were 0.657, 0.594 and 0.626 for length ratio, and they have a sample standard deviation of about 0.03. My primary measure combines these means for each section, so its standard error is about 0.03 times the square root of 4/3 which is about 0.036, which puts 0.2 about 5.5 standard errors away. If the noise and variation in the runs doubled at 60 minutes, the standard error would be about 0.058, and 0.2 would still be about 3.5 standard errors away.
---

## 3. The measures

Name each measure you will report, and how you will compute it.
At least these:

- **Your primary measure** from section 2, per cell, as the mean and the range of the three runs.
- **The blind comparison** of `c1-skills` against `final` at each length, one session per length, never across lengths, and `final`'s share of the non-tie picks at each.
- **Length accuracy:** `teach_length_ratio` per cell, the lesson's estimated reading time against the minutes requested.
  It is a rough estimate at 150 words a minute, and a "60-minute" lesson that is really 35 confounds every other measure, so say now what you will do with a cell whose lessons miss their length.
- **Cost against length:** tokens per minute of lesson for each config, and whether `final`'s overhead grows in step with length or faster.
  Say whether you divide by the minutes requested or by the estimated minutes.

For the primary measure, I will report the mean and the range of the teach_length_ratio for each of the three runs. I will then compute the drop which is the mean at 10 minutes minus the mean at 60 minutes. Then the c1-skills drop minus the final's drop will be computed.

For the blind comparison, I will run compare c1-skills against final at each length. At each length I will report final’s share of the non-tie picks. I will pool across all three lengths and report final’s value with a two-sided sign-test p-value.

For the length accuracy, I will compute the teach_length_ratio by doing the words / 150, and then this value divided by the expected minutes. If teach_length_ratio falls outside of .6 to 1.5 I will flag it and note wit hthe blind comparison that this lesson was not the requested length. It will still count in my primary measure.

For cost vs length, I will report the mean tokens and dollars per run, as well as the tokens per minute for the lessons. I will then divide the tokens by the estimated minutes so some lessons dont accidentally look cheaper than they really are. To see whether the cost for final grows at the same pace as length, I will compute finals extra tokens against c1-skills. I will do this at each length, and then I will compare the cost for 10 30 and 60 minutes. If finals extra tokens per minute stay constant then its overhead is growing at the same rate as length. If it rises as lessons get longer, the overhead is growing faster.

---

## 4. The analysis, and what each result will mean

The comparison is the change from 10 to 60 minutes in your primary measure, for each config, read against the spread of the three runs.
Write the rule now.
This is the default rule, and you can tighten it, but do not loosen it after you see your numbers.

| The result | I will say |
|---|---|
| the two configs' changes differ by Δ or more in the direction I predicted, and the three runs' ranges at 60 minutes do not overlap | supported |
| they differ by Δ or more in the other direction, and the ranges at 60 minutes do not overlap | contradicted: the opposite holds on these runs |
| they differ by less than Δ | no difference as large as Δ on these runs, with the ranges reported |
| anything else | inconclusive with three runs per cell, and I say so |

Then name the threats to validity you will report (lecture 22): blinding failures (your could-tell share at each length), judge bias toward longer outputs (lecture 24), the rough length estimate, and three runs per cell.
Say which one worries you most for your hypothesis.

I confirm the default rules, with one tweak to the supported and contradicted rules. My new rule is that the two configs' changes differ by Δ or more in the direction I predicted, and the ranges of the two configs' drops from 10 to 60 minutes do not overlap. Each drop's range  is its lowest 10-minute run minus its highest 60-minute run to its highest 10-minute run minus its lowest 60-minute run.

There are 4 validity threats. The first is blinding failures, which I will meausure by using the could-tell at each length. The second is judge bias towards longer outputs which can affect the blind comparison as the judge might prefer a longer lesson solely due to it being longer. The third is the rough length estimate where 150 words corresponds to a minute, and lessons with more graphs and tables may read as too short when really they arent. The fourth is three runs percell, where having only 3 runs does not give a big sample, and it could be quite noisy, espeically if we get an outlier. The threat that worries me the most is the rough length estimate, as my primary measure is based on how long the lesson is estimated to be. 

---

## 5. Outcome (write this after the fact)

What did each measure show, cell by cell?
Which row of the table in section 4 is it?
Did the lessons meet their lengths, and what did the cost per minute of lesson do?
What would you do next, and what would you want a reader to take from this?

TODO: your outcome.

---

## 6. Amendments

Dated entries only, one per change, each saying what changed and why.
Leave this section as it is if nothing changed.
