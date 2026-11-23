# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

Misconception (2026-11-18): believes adding more trees to a random forest makes it overfit the training data, and plans to keep 10 trees for that reason. Correct: more trees lower the variance of the averaged prediction and do not increase overfitting; tree depth and leaf size control overfitting per tree. Follow up with the variance of an average of correlated trees, Var = rho*sigma^2 + (1-rho)*sigma^2/B.
