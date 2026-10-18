# Recomputed Regularity for the Compatible Shifted Jet

Date: 2026-10-19. Local, uncommitted work after baseline 5eb266f.
The OP register and issue 16 were read, not updated. Added neutral
commuting-spinor odd-cross comparison only. Main TeX/PDF unchanged.

## Inputs and Purpose

The [compatible tangential lift](HC_Cartan_Compatible_Tangential_Lift.md)
changed all classes of higher jets while retaining the six source values
and shifted lower point. Bounds for the original completion cannot be
inherited. This module checks the candidate's fingerprints, reconstructs
its full symmetric tensors and recomputes the coefficient norms and
estimates using the established temporal/geometric and Cartan formulas.

All fourth spinor derivatives are decoded per quartet as 12 real then
12 imaginary entries. Full tensor norms include every symmetric
permutation. An unweighted unique-coordinate norm is not substituted.

The object being bounded is the candidate's explicit quartic Taylor
field, with cubic multiplier. Its algebraic Cartan connection is solved
pointwise. Bounds on this field do not assert that it satisfies the
remaining field equations throughout the ball.

## Reused Analytic Inequalities, New Coefficients

For coordinate radius r=||x||_2 and full derivative-tensor norms, set

    d = ||E2|| r^2/2 + ||E3|| r^3/6 + ||E4|| r^4/24,
    p = ||psi1|| r + ||psi2|| r^2/2 + ||psi3|| r^3/6 + ||psi4|| r^4/24,
    ell = ||lambda1[...,0]|| r + ||lambda2[...,0]|| r^2/2
          + ||lambda3[...,0]|| r^3/6.

Then ||E-I||_2<=d, ||psi-psi0||<=p, and the last coordinate column of
lambda changes by at most ell. For d<1, E is invertible, its volume is
between (1-d)^4 and (1+d)^4, and ||E^-1||_2<=1/(1-d). The previous
[temporal derivation](HC_Cartan_Joint_Neighborhood.md) bounds the temporal
probe-weight change by

    k = 4d + 6d^2 + 4d^3 + d^4 + (1+d)^4 sqrt(2)d/(1-d) + ell/sqrt(2).

With original temporal eigenvalue mu, use m=mu-k>0. The constitutive/probe
Schur-block change is bounded by

    dt = ((2||psi0||p+p^2)/m + ||psi0||^2 k/(m mu))/2.

Its smallest singular value is therefore bounded below by tau0-dt.
Metric estimates also retain positive spatial metric and timelike
coordinate-time margins.

For the algebraic Cartan Hessian, the
[congruence derivation](HC_Cartan_Joint_Cartan_Regularity.md) gives

    H(E) = |det E| T(E).T H(I) T(E),
    sigma_min(H(E)) >= sigma_min(H(I)) (1-d)^4/(1+d)^2.

These are uniform analytic inequalities evaluated with the new numerical
norms. Floating-point norm and margin evaluations are not outward-rounded
interval certificates.

## New Bounds

The dyadic selection is rerun independently for each block. The temporal
selection is r=1/16384, and the Cartan perturbation selection is r=1/64.
Use their minimum as a common coefficient-domain radius:

    r_common = 1/16384 = 0.00006103515625.

| Common-ball bound | Value |
| --- | ---: |
| Coframe change upper bound d | 2.9893e-9 |
| Spinor change upper bound p | 0.00115157 |
| Temporal multiplier-column change | 9.2894e-5 |
| Temporal probe eigenvalue lower bound | 0.96800847 |
| Constitutive/probe Schur singular-value lower bound | 0.02557689 |
| Schur inverse-norm upper bound | 39.09779 |
| Spatial metric eigenvalue lower bound | 0.9999999940 |
| Coordinate-time timelike margin | 0.9999999940 |
| Cartan Hessian singular-value lower bound | 0.9999999821 |
| Cartan inverse-norm upper bound | 1.0000000180 |

At its separately selected larger radius 1/64, the Cartan congruence
bound is still 0.92025223 and its inverse bound is 1.08665861. Temporal
regularity is not asserted there.

The dyadic radii happen to equal those previously selected for the
original jet, but the tensor coefficients and margins differ and were
recomputed. These are sufficient conservative choices, not maximal
radii: for example, the temporal estimate at twice the common radius
still has positive margins but misses the selection rule's requirement
to retain at least half the original Schur singular margin. No physical
length unit has been identified for these comparison coordinates.

## Independent Checks and Remaining Defects

Seventeen sample points cover the origin, positive/negative coordinate
axes and seeded directions. At every point the code compares full-tensor
Taylor contraction with the existing unique-coordinate homogeneous-jet
constructor. Coframe, spinor, multiplier and connection agree within
test tolerances; their saved connection discrepancies are zero in this
run. The Cartan congruence discrepancies are below 1.6e-16. These checks
support the implementation but do not replace the uniform inequalities.

The origin still has all 1114 residuals at 4.87e-10. Across the common-ball
samples, maxima are about 1.32e-11 for the constitutive constraint,
8.46e-8 for the probe residual, and 3.85e-15 for the algebraically solved
Cartan residual. The nonzero off-origin probe residual is retained,
not reclassified as a solution because it is small.

The 68-by-56 normal map is rechecked at the shifted origin: rank 40,
smallest retained singular value 0.10594420, particular inverse norm
9.43893144. This is not a uniform rank result for that full operator
throughout the ball. Positivity of a temporal subblock and invertibility
of the algebraic Cartan block do not establish full PDE hyperbolicity,
gauge/source evolution, or regional Cauchy existence.

## Next Question and Handoff

The finite candidate now has recomputed regular coefficient-domain
estimates. The [general normal-chart follow-up](HC_Cartan_General_Normal_Chart.md)
formulates the general-coframe 68-by-56 operator and checks rank 40 at
13 points, together with an augmented coordinate chart. A quantitative
uniform rank/inverse bound and compatibility propagation remain open.
Separately, a regional solution
would require propagation/evolution or a justified completion of the
higher hierarchy, not only bounds on this finite Taylor polynomial.
No regional solution has been obtained here. No native HC/C7, frame, mass,
Planck scale, global closure or stability claim is added.

## Reproduction

Run `python -B analysis/HC_Cartan_Compatible_Lift_Regularity.py --output
analysis/HC_Cartan_Compatible_Lift_Regularity.json` from the repository
root. No large matrices are rebuilt for this short bound refresh.

29 focused tests passed: 10 new compatible-lift regularity tests, 11
compatible-tangential-lift tests, and 8 original Cartan-regularity tests.
They check the new norms, symmetric multiplicities, selected radii,
sample inequalities, independent constructors, origin normal rank and
guards against claiming a regional solution from finite bounds. They
do not prove that regional solutions do not exist. The full repository suite
was not rerun for this isolated sidecar.
