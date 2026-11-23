# Random Forest Regression Resources

## Knowledge

- [Wikipedia: Random forest](https://en.wikipedia.org/wiki/Random_forest)
  Compact summary of the algorithm; states that regression output is the average of the trees and that deep trees have low bias and high variance. Use for: quick definitions and the bias-variance statement.
- [scikit-learn user guide: ensembles](https://scikit-learn.org/stable/modules/ensemble.html)
  Official documentation on bootstrap samples, feature subsets, bagging and forests. Use for: how the algorithm maps to code.
- [scikit-learn: RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
  Parameter reference; max_features defaults to 1.0, equivalent to bagged trees. Use for: parameter meanings and defaults.
- [The Elements of Statistical Learning, chapter 15 (hosted PDF excerpt)](https://www.math.mcgill.ca/yyang/resources/doc/randomforest.pdf)
  Textbook treatment: variance of an average of correlated trees and the role of the number of candidate features. Use for: the variance formula and its derivation. Note: automated fetches returned HTTP 403, so open it in a browser.
- [Liu and Mazumder, "Randomization Can Reduce Both Bias and Variance" (arXiv preprint)](https://arxiv.org/html/2402.12668v4)
  Recent preprint arguing forests can reduce bias relative to bagging. Use for: nuance beyond the standard variance-only account; not needed for the exam.

## Wisdom (Communities)

- Cross Validated, the statistics question site on Stack Exchange
  Moderated Q&A. Use for: checking explanations of bias, variance and ensemble methods. (No link recorded: not opened this session.)

## Gaps

- A freely fetchable copy of the Elements of Statistical Learning chapter on random forests.
