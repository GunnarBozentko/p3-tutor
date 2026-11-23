# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

Misconception (shown again in a later session): believes each leaf of a regression tree fits its own regression line. In fact each leaf predicts a constant, the mean of its training targets. Linked to the earlier gap of expecting smooth, extrapolating trends. Next: show a forest as an average of 100 step functions, not lines.
