# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

Misconception (shown 2026-11-18): believes adding more trees to a random forest makes it overfit, so they plan to keep 10 trees. Truth: more trees do not cause overfitting; they lower variance and the error levels off. Overfitting is controlled by tree depth / min leaf size / max features, not tree count. Check that this landed next session.

