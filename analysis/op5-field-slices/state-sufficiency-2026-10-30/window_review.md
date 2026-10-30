# Independent fixed-second-jet-window fifth-order review

30 October 2026. Bounded review of fifth_window_fit.py with no optimizer rerun. Frozen spinor second derivatives are not thereby identified with physical Riemann curvature.

## Variable and equation window

Spinor coefficient degrees0,1,2 are fixed to the successful fourth-order seed. Degrees3 and4 (480+840 real variables) are free. Degree5 is eliminated through the complete highest-operator left kernel and recovered. The retained objective includes F degree2 and degree3 (240+480 components), plus all105 projected F-degree4 source conditions. F degrees0 and1 depend only on the frozen coefficients and therefore remain at the seed residual levels. The objective covers every lower residual degree that can change in this window.

The highest matrix depends only on psi and first derivatives, so keeping its left kernel fixed is valid. F degree4 is at most quadratic in variable degree3 coefficients: their first derivatives start at degree2, and 2+2=4. It is affine in degree4 coefficients, whose first derivatives start at degree3. Products of variable degree3 and degree4 contributions start at degree5 and do not enter the retained residual. Thus the degree4 linear coefficient matrix is independent of both variable blocks under the frozen0..2 assumption, whereas the degree3 dependence is nonlinear/quadratic. Failure of this bounded nonlinear fit would not prove incompatibility.

An optional economy reduction would eliminate degree4 from the 825-row objective by a second complete left-kernel calculation and optimize degree3 only. That would require explicit source reconstruction and full residual checks; it is a possible alternative, not an executed result in this review.

## Independent verification contract

window_review_coefficients.py reconstructs original symbolic background coefficients through degree4 and implements separate NumPy directional formal-series residual evaluation with recurrence matrix inversion. It checks six directions per point, both inverse multiplication orders, selected highest-operator columns, all multivariate scalar g coefficients through degree4, and exact equality of every frozen degree0..2 coefficient with the seed. It records movement of degrees3 and4 and coefficient/raw derivative norms. No optimization is performed.

The completed three-point result has now been checked. No shared source, previous result or repository file was modified by this review.

## Executed independent checks

Ran window_review_coefficients.py after all three result rows were complete. Fingerprints are recorded in window_review_coefficients-result.json and the inputs remained unchanged during the check. This imports the generic evaluator only as a comparison target; the independent NumPy formal series uses original symbolic backgrounds, separate convolution sums and a recurrence inverse rather than the generic Neumann inverse. It performs no fit.

| point | maximum F coefficient difference, degrees0..4 | maximum inverse identity error | maximum sampled highest-operator error |
|---|---:|---:|---:|
| 0 | 1.81e-12 | 2.01e-12 | 5.11e-13 |
| 1 | 1.01e-12 | 1.68e-12 | 3.71e-13 |
| 2 | 1.28e-12 | 3.76e-12 | 2.40e-13 |

These discrepancies are substantially below the observed final full-residual tolerance. The maximum raw residual block is about 4.35e-10 at the centre, 1.04e-10 at the edge and 1.25e-10 at the inner point. These are numerical approximate jets, not certified exact solutions.

Independent full multivariate scalar convolution gives:

| point | norm g | norm dg | norm d²g | norm d³g | norm d⁴g |
|---|---:|---:|---:|---:|---:|
| 0 | 8.88e-16 | 3.27e-14 | 8.66e-14 | 2.10e-10 | 1.96e-9 |
| 1 | 8.88e-16 | 3.18e-15 | 4.47e-14 | 2.29e-11 | 2.12e-10 |
| 2 | 4.44e-16 | 3.62e-15 | 7.73e-14 | 7.69e-12 | 7.40e-11 |

Thus the scalar conditions are small at the observed tolerance but not all below 1e-10. In particular the centre fourth scalar derivative is about 2e-9. Derivatives of ell multiplying lower F residuals appear in the differentiated scalar identity, so its higher scalar norm need not equal ell times the highest F block alone. No exact-zero or raw lower-bound attribution is made at this numerical floor.

## Frozen coefficients, movement and cost

Every degree0,1,2 coefficient was asserted exactly equal to the fourth-order seed; all assertions passed. Relative normalized degree3 changes are 81.80%,75.86%,82.20%; degree4 changes are 69.05%,56.94%,63.72%. Their actual derivative changes at degrees3/4 are (111.81,1022.00), (104.97,792.72), (108.81,919.98).

The fifth actual-derivative norms are 19526.87,21333.00,17058.17, with normalized fifth-coefficient norms 841.99,793.44,782.92. These are larger than the unrestricted fifth fit's actual fifth norms of about13629–15776. Keeping H fixed therefore has a measurable cost in this chosen solution, without proving a minimum-norm bound or physical cost. The coordinate/norm conventions remain essential.

## Verdict

The implementation and finite numerical result are independently corroborated in the stated directional/column range, with complete scalar and frozen-coefficient checks. No blocking arithmetic/convention issue was found. Unlike the failed fixed0..3 control, this window admits approximate fifth-order jets while preserving the complete old second jet. Accordingly the earlier unrestricted fit's second-jet changes were not necessary for this tested step.

This does not preserve the old third/fourth jets, establish coefficient stabilization across further orders, or identify whether the new third jet will itself admit a fixed-lower sixth completion. The result is not an exact no-go theorem, an infinite formal solution, a regional field solution, an invariant physical geometry or OP5 closure. If a later nonlinear fit fails, the failure must not be promoted to incompatibility without an additional exhaustive or analytic argument.

Reproduction: `python window_review_coefficients.py` from the repository working directory. Reviewer artifacts are only window_review_coefficients.py, window_review_coefficients-result.json and this window_review.md in the task workspace.
