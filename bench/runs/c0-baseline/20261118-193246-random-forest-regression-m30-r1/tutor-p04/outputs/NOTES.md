# Notes

What the leaerner already knows is how a decision tree works, and how to write it in code. They can answer the bias-varaince tradeoff for this model.

They do not know about the ensemble method of random forest regression, and how it makes it predictions. He gets confused on why averageing many trees gives a better prediction than one deep tree. 

Session 2 (tutor): asked for Breiman's strength/correlation bound. I gave the classification derivation (Chebyshev on the margin) and the regression version (PE(forest) <= rho_bar * PE(tree)), and flagged that the strength bound is classification-only while their mission is regression. Related to their open confusion about why averaging helps; the regression bound answers it directly. Wants derivations with math; follow up with a lesson if they ask.
