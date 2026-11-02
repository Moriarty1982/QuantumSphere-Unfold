# Independent fifth-order review

30 October 2026. Review of finite-order numerical compatibility under the unchanged OP5 comparison model. No optimization is run by the reviewer.

## Verification contract

The fifth-order spinor jet produces residual Taylor coefficients through degree4. Coefficients are actual multivariate derivatives divided by the multiindex factorial. The independent script fifth_review_coefficients.py reconstructs exact original background coefficients through degree4, restricts the full multivariate spinor polynomial to six real directions per point, differentiates the spinor in each coordinate before restriction, and computes the nonlinear residual by separate NumPy univariate coefficient sums and inverse-matrix recurrence. It compares this result with the generic Torch evaluator only after the independent series has been formed. Both inverse multiplication orders and selected highest-operator columns are also checked.

The script independently evaluates every scalar g coefficient through degree4 with a full multivariate convolution, restores actual derivatives, and reports one norm per derivative degree. This avoids inferring the complete scalar gate from six directional checks alone. The directional residual validation remains bounded coverage; it does not prove equality of every possible input polynomial or all coefficient combinations.

## Sequence and growth interpretation

The prior order4 result is the comparison baseline for degrees2,3,4. Report both normalized coefficient change and actual derivative change, as well as relative normalized change. Psi and all first derivatives should remain exactly fixed. Fifth actual derivatives, normalized fifth coefficients and lower-degree coefficient norms must be distinguished.

If lower coefficients change at order5, the result is a new feasible finite jet sharing psi/first derivatives, not a strict prolongation of the previously fixed fourth jet. Establishing a consistent infinite formal jet would require preserving each lower coefficient eventually or showing a suitable compatible limit. Establishing regional existence would require additional convergence/regularity arguments. Growth of unweighted derivative norms across the first few orders supplies neither a convergence radius nor a physical scale.

## Status

Completed against the three-point fifth-order result. No shared model module, old results or repository files were modified by this review.

## Executed result

All three fifth-order result rows were complete before the review run. Input fingerprints are in fifth-review-coefficients-result.json, including the model module, source model, fourth baseline, fifth result and reviewer script. The recorded inputs were unchanged during the calculation. No fitting was rerun.

| point | maximum independent F-coefficient discrepancy, degrees0..4 | maximum inverse identity error | maximum sampled highest-operator error |
|---|---:|---:|---:|
| 0 | 9.83e-13 | 1.35e-12 | 2.39e-13 |
| 1 | 8.35e-13 | 1.84e-12 | 2.76e-13 |
| 2 | 6.86e-13 | 7.72e-13 | 1.98e-13 |

The independent univariate recurrence therefore corroborates the generic evaluator through residual degree4 at the tested directions. The parent's actual-derivative fourth-residual norms are 8.41e-11, 5.05e-10 and 9.61e-11, respectively. The second point stopped at the declared coefficient-objective tolerance and is less accurate; it should not be reported as machine-zero or silently refitted in a review.

Independent full multivariate scalar convolution gives:

| point | norm g | norm dg | norm d²g | norm d³g | norm d⁴g |
|---|---:|---:|---:|---:|---:|
| 0 | 8.88e-16 | 3.27e-14 | 9.13e-14 | 6.24e-13 | 9.66e-12 |
| 1 | 8.88e-16 | 3.18e-15 | 1.94e-12 | 7.62e-12 | 1.25e-10 |
| 2 | 4.44e-16 | 3.62e-15 | 6.59e-14 | 6.23e-13 | 1.18e-11 |

These scalar norms corroborate fourth-order constraint preservation at the observed numerical accuracy. They do not certify exact zero.

## Movement from the fourth-order candidate

Psi and all first derivatives are unchanged exactly in the saved coefficients. Higher lower-order coefficients are NOT frozen:

| point | relative normalized change degree2 | degree3 | degree4 |
|---|---:|---:|---:|
| 0 | 50.38% | 66.88% | 37.02% |
| 1 | 44.43% | 62.98% | 35.23% |
| 2 | 52.51% | 68.74% | 37.73% |

The actual derivative changes at degrees2/3/4 are respectively (13.89,84.10,580.72), (12.32,82.88,521.47), (14.31,84.15,602.41). Thus this is a new feasible fifth jet sharing the same value and first derivatives, not a strict extension of the prior fixed fourth jet. No stabilization of lower coefficients is demonstrated by this step.

Final normalized coefficient norms at degrees2/3/4/5 are approximately (21.62,52.94,159.87,721.20), (21.55,54.20,163.89,733.41), (21.53,52.14,157.47,715.24). Actual fifth-derivative norms range from 13,629 to 15,776. Factorial normalization reduces the apparent numerical growth but does not remove it. These values alone give no convergence radius, uniform bound or physical scale.

## Verdict and limitations

Implementation and finite assertion independently corroborated in the stated six-direction and selected-column range, with complete scalar coefficient checks through degree4. No blocking arithmetic/convention bug found. The fifth-order result is positive finite numerical feasibility under the fixed comparison, at the reported tolerance. It is not an infinite formal solution, a convergent recursive construction, a regional field solution, a native physical identification or OP5 closure.

Reproduce by running `python fifth_review_coefficients.py` from the repository working directory (or another location where the module can locate the repository). The reviewer writes only fifth_review_coefficients.py, fifth-review-coefficients-result.json and this fifth_review.md in the task workspace.
