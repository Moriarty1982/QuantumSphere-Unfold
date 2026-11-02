# Fifth-order calibration with an exactly frozen second jet

30 October 2026. Same declared comparison and fourth-order seed as previous tests. No new coupling, physical equation or background. No repository files changed in this turn.

## Contract

Keep all coefficients of degrees0,1,2 of the successful fourth-order seed exactly fixed: field value, first derivatives and every symmetric second derivative. Vary only degrees3 and4, then eliminate/recover all symmetric fifth derivatives with the same highest operator as the unrestricted fifth test. The objective contains all variable lower equations (F coefficients of degrees2 and3) plus the complete105-row highest left compatibility gate. F degrees0 and1 are fixed and independently retained in the final full check. No derivative of a coordinate/coframe fixing is added.

Reproduction: `python fifth_window_fit.py` from the repository root with the artifact directory as script location. At most18 outer iterations and10 damping trials per iteration; normalized objective stop1e-9, three fixed points, float64. The complete unprojected residual is checked after highest-jet recovery at relative SVD cutoffs1e-8,1e-9,1e-11.

## Result

The fits take8,6,8 accepted steps. All degrees0..2 match the fourth-order seed bit for bit. Full symmetric raw derivative residuals are:

| point | F | dF | d²F | d³F | d⁴F |
|---|---:|---:|---:|---:|---:|
| centre | 3.06e-14 | 3.93e-14 | 2.41e-10 | 4.35e-10 | 1.20e-10 |
| edge | 2.03e-15 | 2.93e-14 | 2.78e-11 | 4.80e-11 | 1.04e-10 |
| inner | 2.64e-15 | 3.78e-14 | 8.61e-12 | 1.59e-11 | 1.24e-10 |

The rank of the highest840x1344 matrix is735 under all three cutoffs. These are approximate numerical roots under the stated objective tolerance, not certified exact solutions.

## Verification

The separate NumPy directional formal-series evaluator, recurrence inverse, original background derivatives and scalar checks corroborate the result. Six directions per point agree through residual degree4 within1.9e-12; sampled highest-operator columns agree within5.2e-13. Frozen coefficients0..2 are explicitly checked for exact equality.

The separately calculated scalar d³g norms are2.10e-10,2.29e-11,7.69e-12 and d⁴g norms1.96e-9,2.12e-10,7.40e-11. Their scale is not identical to the unweighted residual norm: differentiated identities contain derivatives of the multiplier times lower residuals. Do not promote these data to exact scalar zeros or quote a universal1e-10 bound for every derived quantity. Input hashes are unchanged.

## Cost of preserving the second jet

Normalized degree3 coefficient changes are81.8%,75.9%,82.2%; degree4 changes69.1%,56.9%,63.7%. Raw fifth-derivative norms are19526.9,21333.0,17058.2, larger than the preceding unrestricted fifth fit. This is a redistribution of the adjustment burden, not evidence that higher coefficients converge. The raw second-jet norms stay exactly at25.94,26.44,25.59 from the fourth-order seed. Derivative norms are in the retained unscaled coordinates and are not physical scales.

## Selection rule supported by this step

For this fifth-order test, first try the narrowest moving window: adjust degree4 and recover5 while freezing0..3. That earlier linear feasibility control failed numerically with stable rank. Widen one level: adjust3,4 and recover5 while freezing0..2. This succeeds at all three points. Releasing degree2, as the original unrestricted fifth fit did, is therefore not necessary for this particular step.

This validates one adaptive-window decision, not an all-order rule: start with the highest lower level, widen downward only as needed, keep all retained residuals in the objective, and independently check the final full equations. For a nonlinear fit, bounded solver failure alone must remain inconclusive rather than being treated as an impossibility proof. Success on a wider window does not establish that every coefficient inside it needed to move, only that this allowed window sufficed.

The fixed second jet can be shared by successful finite jets at orders4 and5. It has not been shown that it can remain fixed at every higher order. The old complete fourth jet is still not preserved, because degrees3,4 change. Next discriminating work is to test preservation of the third jet at the next order, or derive compatibility/selection conditions that justify such preservation. Growth bounds, stabilization of an entire sequence, a common regional field, native action and OP5 closure remain open.

Artifacts: fifth_window_fit.py, fifth-window-result.json; window_review_coefficients.py, window_review_coefficients-result.json, window_review.md; fifth-window-manifest.json and input snapshots. Earlier unrestricted successes and the failed frozen0..3 control remain unchanged.
