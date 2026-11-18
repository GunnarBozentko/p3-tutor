# Trees predict flat leaf means; the variance reason is still thin

Quiz 0001 (s1) confirmed the learner knows the squared-error split rule and that a leaf predicts the mean of its training targets. Misconception M2 is still open: they expect a tree to continue a trend beyond the training range, as linear regression does. They also named overfitting for a fully grown tree without explaining the high variance behind it, which matters for why averaging trees helps in a random forest.

**Evidence:** quiz 0001, submission s1, items q1, q2 (correct), q3 (partial), q4 (wrong, M2).
**Implications:** Revisit step-function predictions and flat extrapolation before the forest lesson. Ask the learner to explain overfitting through variance, meaning how the tree changes with a different sample.
