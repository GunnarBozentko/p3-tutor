# Misconception: more trees make a random forest overfit

The learner said they would keep 10 trees because more trees "would just make it overfit". This is wrong: adding trees averages away variance and the error plateaus, so tree count is not an overfitting knob. It ties to their open gap on why averaging many trees beats one deep tree.

**Evidence:** chat message of 2026-11-18.
**Implications:** Teach why averaging decorrelated trees cuts variance, and that depth, leaf size and max features control overfitting. Re-check with a short question later.
