# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

## Tutor working notes

- Lesson 1 (O2) written: variance of an average of correlated trees, floor rho*sigma^2, bias-variance numbers, scikit-learn code. Quiz 0002 is ready; not yet taken. Nothing is known yet about whether the confusion above is resolved.
- Misconception ids used in quiz 0002 keys: M1 more trees always keep improving without limit; M2 averaging helps even when trees are identical or randomness is removed; M3 averaging works by removing bias.
- Learner wants: blunt feedback, no praise, formal tone, bullets for multi-step work, terms defined at first use, code, soccer analogies, 3 to 5 sentence paragraphs.
- Scikit-learn's RandomForestRegressor default is max_features=1.0 (plain bagging); the original algorithm uses a feature subset. Teach both distinctly.
- Learner has not stated community preferences.
