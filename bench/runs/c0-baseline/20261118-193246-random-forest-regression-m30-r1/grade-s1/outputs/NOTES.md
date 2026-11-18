# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

## Quiz 0001 (s1), graded
- Correct: split rule (most squared-error reduction), leaf prediction is the mean of its training targets.
- Partial: says a fully grown tree "overfits/memorizes" but does not give the variance reason. This links to the confusion about why averaging trees helps.
- Open misconception M2: expects a tree to extrapolate a trend past the training range (q4). In fact it predicts the flat leaf mean of the edge region.
