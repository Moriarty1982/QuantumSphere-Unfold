# Joint Second-Probe/Gravity and Third-Constraint Completion

This is a pointwise finite-jet result for the explicitly added neutral odd-cross
Einstein-Cartan comparison. It does not change the native paper's action or
identify HC/C7, physical frames, coupling values or scales. Main TeX/PDF and
published release files are not changed by this calculation.

## Why the Earlier Failure Was Repairable

The earlier [frozen diagnostic](HC_Cartan_Third_Constraint_Diagnostic.md) found
45 C3 compatibility directions outside the image of all newly appended highest
derivatives. It correctly ruled out that particular frozen continuation
numerically. It did not rule out changing the earlier higher data.

The [analytic C3 re-preparation](HC_Cartan_Third_Constraint_Reprepare.md) exposes
the 45 conditions and repairs them by changing lambda2/E3/psi3 while fixing
psi2 and all lower-point data. That C3-only repair is retained as a separate
714-component intermediate check. The present result additionally imposes the
full next probe and independent gravitational Euler equations simultaneously.

## Fixed and Variable Data

Fixed exactly: psi, psi1, psi2, E=I, E1=0, E2, lambda0, lambda1, Q, M, the
Einstein coefficient 1 and vacuum 0. The original 56 point equations remain
satisfied. Q and M are still the declared comparison matrices, not fitted
physical couplings. No mass, gravitational constant or unit calibration is
inferred from the result.

The 1840 real solve coordinates are:

| Block | Coordinates | Status |
| --- | ---: | --- |
| lambda2 | 160 | Earlier higher data re-prepared |
| E3 | 320 | Earlier higher data re-prepared |
| psi3 | 480 | Earlier higher data re-prepared |
| E4 | 560 | New highest coframe data |
| lambda3 | 320 | New highest multiplier data |

The 840 real psi4 coordinates are recovered after solving; their 140-dimensional
constraint image is removed by an orthogonal quotient during the solve. The
remaining 700 spinor principal null directions are set to zero by the chosen
minimum-norm right inverse, not identified as physical gauge freedom.

## Equations and Derivation

The prior 394 equations are retained in full. New equations are the full
complex R2 (240 real unique-pair components), independent-coframe Euler FE2
(160 real unique-pair components), and C3 (320 real unique-triple components).
R2 is NOT replaced by its scalar contraction. FE2 is NOT replaced by a metric
LC Einstein equation, and the sourced Cartan curvature is not identified with
the metric LC curvature.

The [analytic R2 derivation](HC_Cartan_Second_Probe_Affine.md) differentiates
the full real variable-weight operator, including its defect Z and every
weight/connection derivative. The new lambda3 principal contribution is
`(i/2) sum_mu,a lambda3[r,s,mu,a,mu] Q_WEIGHT[a] psi`.

The [analytic FE2 derivation](HC_Cartan_Second_Gravity_Affine.md) differentiates
the independent Palatini coframe variation, retaining the E2-volume/inverse
response multiplying the undifferentiated matter and curvature. Curvature2
contains all differentiated connection-product terms and the curl of omega3.
The analytic C3 source includes the nonzero multiplier-value Cartan reaction
and the quadratic normal-frame LC contribution. All derivatives are actual
derivatives, not factorial-normalized Taylor coefficients.

With psi2 and the lower point fixed, each expression is affine in the allowed
variables. After eliminating psi4, the solve has 394+240+160+180=974 rows and
1840 columns. Its numerical rank is 681, with relative SVD cutoff 1e-10.
The smallest retained singular value is about 0.08506; the next is about
3.32e-13 (largest about 898.811), giving a substantial numerical gap.
This is a numerical rank statement; its full symbolic dependency/Noether
classification is not supplied here. Free coordinates are not counted as new
physical degrees of freedom.

The coefficient matrix is sampled from the analytic affine evaluator using
64-unit coordinate increments to reduce source-subtraction roundoff. The new
highest response columns use explicit analytic principal maps. A random affine
control has residual about 6.48e-11. The same SVD inverse is used for residual
refinement, reducing the projected-system residual from about 1.37e-8 to
3.96e-10. No nonlinear optimizer, changed couplings or discarded rows are used.

## Full Unprojected Check

After recovering psi4, every equation is independently re-evaluated from the
saved coordinates without the solver's projection or coefficient matrix.

| Equation block | Recomputed component norm |
| --- | ---: |
| Prior 394 components | 4.784e-11 |
| R2, full symmetric derivative tensor | 2.933e-11 |
| FE2, full symmetric derivative tensor | 1.077e-10 |
| C3, unique sorted derivative triples | 5.275e-10 |
| All 1114 packed real components | 5.377e-10 |

The R2/FE2 full symmetric norms count mixed pairs twice, while the total packed
residual uses each unique derivative pair once. These are declared coordinate
component norms, not invariant physical scales or measured errors.

The earlier higher-coordinate change has norm about 32761.679 and the new
E4/lambda3 coordinates about 26622.924 in these same uncalibrated coordinates.
The small residual must not be mistaken for small field coefficients or a
large domain of validity. The previous neighborhood bound cannot be inherited.

## Independent Controls

The scalar Hessian remains solved, but is no longer used as a substitute for
the full R2 vector. R2 is checked against independently displaced fields with
nonzero lambda3 and against the differentiated off-shell identity. FE2 has
independent parent-Euler polynomial and actual Cartan-field controls, including
nonzero highest jets and the required frame-curvature response. Their numerical
stencil tolerances are documented in the separate derivation notes.

For the final joint coordinates, the actual quartic/cubic Taylor fields are
also inserted into the full algebraically eliminated Cartan constraint, not a
polynomial omega approximation. Along one fixed normalized coordinate direction,
the constraint norms are 6.259e-6, 4.051e-7 and 2.576e-8 for steps .002, .001 and
.0005. Successive ratios near 16 agree with the expected fourth-order remainder
after satisfying C through its third derivative. This is a sampled consistency
control, not a uniform bound or a proof that the fields solve the PDE nearby.

## What Has and Has Not Been Achieved

The previously frozen obstruction is repaired at the next full tested derivative
stage, using unchanged couplings and unchanged lower point/psi2. The older
negative controls and intermediate C3-only completion remain available; no
previous source-of-truth JSON is overwritten.

Still open: the next derivative hierarchy, constraint propagation from surface
data, formal integrability/convergence, a local-existence theorem, an updated
neighborhood estimate including E4/lambda3/psi4, and native/physical identification.
There is no claim that a finite jet proves a gravitational mechanism, a tunnel
between frames, or a new spacetime solution.

## Reproduction

```text
python -B analysis/HC_Cartan_Next_Joint_Completion.py --output analysis/HC_Cartan_Next_Joint_Completion.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_next_joint_completion.py
```

The JSON records normalized source fingerprints, SVD values, all older and new
jet coordinates, refinement controls and the entire unprojected residual.
The parent owns the joint solver and C3 derivation. Parallel independent work
verified the LC cubic formula and supplied separate analytic R2/FE2 derivations
with focused tests. Agent agreement is not treated as a mathematical proof.

Verification: all 1,992 audit checkout tests and 34 separate OP5 checks passed
(2,026 total), including ten joint-integration checks. Six audit tests are
pre-existing unrelated uncommitted metadata-hygiene work, so the research-scope
count excluding them is 2,020. The unchanged full-monolith preservation check
and whitespace check also pass. No commit, push or PDF build was performed.
