# Full 80-row Taylor residual bound

## Fixed problem

This extends the constitutive Taylor-tail calculation to all 80 equations of
the same saved, quartic-corrected polynomial field. The order is constraint
(16), real probe (24), coframe Euler (16), then six constitutive curl pairs (24).
The first three curl pairs are the mixed rows in the 68-row parent, and the
last three are the additional spatial conditions.

No field coefficients, couplings or source values are fitted or changed. The
calculation remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison, not a native HC/C7 identification. Main TeX/PDF are unchanged.

## Derivatives are modeled, not inferred from an unknown tail

The predecessor stores 70 multivariate coefficients through degree four and a
whole-cube tail bound. That value-tail bound alone cannot be differentiated.
Here the first and second coframe derivatives and first spinor/multiplier
derivatives are assembled directly from the original known field polynomial.
In particular, degree-six coframe terms contribute degree-four second
derivatives, even though their value terms were already above the retained
degree. They must not be dropped before differentiation.

Each tensor is lifted to a value model and four separately controlled physical
coordinate derivative models. Multilinear contractions use the product rule.
The derivative of an inverse is evaluated as -A^-1 (dA) A^-1 using its resolved
Neumann value model and the separately modeled derivative. The volume derivative
uses det(E) tr(E^-1 dE). Derivatives are with respect to physical coordinates x,
not the normalized coordinates y=x/L; the field assembly retains those factors.

This constructs the connection, its first derivatives and kinetic weights.
The real symmetric probe equation, independent coframe Euler equation and all
curl rows then follow the original formulas. Polynomial coefficients are
combined before taking norms; discarded products and Neumann tails are retained.
The 16-row constraint coefficients and tail agree exactly with the predecessor's
saved numerical result, so the extension does not replace that calculation.

## Whole-cube estimates

Let r=1/16384. The following estimates cover |x_i|<=L and therefore also the
Euclidean ball ||x||<=L. Constants and low-order defects are included, not
silently assumed zero.

| Block | At L=r | At L=r/2 |
| --- | ---: | ---: |
| Constraint, 16 rows | 0.0270219 | 0.000838376 |
| Probe, 24 real rows | 0.0480457 | 0.00149082 |
| Coframe Euler, 16 rows | 2.16745 | 0.0674980 |
| Constitutive curls, 24 rows | 10.2408 | 0.319199 |
| Combined 80-row estimate | 10.4678 | 0.326262 |

The combined tail is the root-sum-square of the block tails, not their sum.
Retained coefficients are also included in the combined estimate. At r the
whole-vector norms of coefficient families of degrees zero through four are
bounded numerically by

    (4.46e-14, 3.97e-15, 5.69e-18, 3.63e-10, 5.61e-10).

The total estimate improves from the previous natural enclosure of about
2.496e6 to 10.4678 on the common ball, over 200000-fold. Each block's recomputed
tail decreases by approximately a factor 32 under radius halving. These are
two-radius observations, not a proof of an exact scaling law at every radius.
The nonzero degree-three and degree-four coefficients also mean that the full
numerical residual must not be reported as exactly homogeneous of degree five.

Curl tails dominate this estimate, followed by the coframe block. This is a
statement about the present majorant and expression decomposition, not a newly
identified physical obstruction or independently evolving mode.

## Independent controls and remaining conservatism

The actual 80 equations are evaluated at the axis, mixed directions and cube
corners. At r, sampled norms range from about 4.59e-9 to 8.90e-6. All lie below
the tail estimate, which is still many orders larger. The cube corners have
Euclidean distance 2r; their evaluation does not inherit a larger augmented
normal-chart theorem. The new inverse models resolve algebraic evaluation
throughout the cube, not regional PDE compatibility there.

Independent constant-field Taylor models at the origin and a cube corner have
zero truncation tail and agree with the original evaluator to about 1e-13.
An off-shell perturbed-jet test exercises all blocks without relying on their
previous fit. Direct reconstruction tests include the full second-derivative
axes, spinor packing, first multiplier derivatives and cube corners. Rescaling
the coordinate radius rescales every stored coefficient by its multiindex
degree as expected.

All calculations are binary64 evaluations of real-arithmetic majorant formulas.
Floating-point operation errors are not enclosed by outward rounding. Zero-tail
controls are numerical formula checks, not exact equality certificates.
The inherited retained-origin rational kernel certificate remains authoritative
for its separate precision-sensitive update.

No exact low-order vanishing, uniform normal-rank upper bound, compatibility
propagation, regional existence, convergence of an all-order construction or
distance to an exact PDE solution is established. A norm bound below one at
L=r/2 has no special physical or existence significance by itself. The next
useful improvement is to sharpen the dominant curl/coframe tail bounds while
retaining coefficient correlations and to enclose rounding errors.

## Reproduce

Run `python -B analysis/HC_Cartan_Full_Taylor_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_full_taylor_bound`.
Two bounded local workers evaluate the two radii. The JSON stores fingerprints,
all 70-by-80 coefficient arrays, block and total bounds, Neumann ratios and
actual-equation controls. Historical scripts and their fingerprints are not
rewritten by this extension.
