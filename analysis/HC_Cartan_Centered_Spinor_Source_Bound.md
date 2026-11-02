# Centered spinor sources in the Cartan comparison

## Scope and unchanged problem

This calculation remains in the added neutral commuting-spinor odd-cross
Einstein-Cartan comparison. No native HC/C7 identification, new physical
coupling, source adjustment or low-order refit is made. Main TeX/PDF are
unchanged. The source support and curved inverse factorization are inherited
from the preceding fingerprinted sidecars.

## Why not reduce the exterior factor again?

The six-pair antisymmetrization D of a four-by-four derivative array obeys
D D^T=2 I6, so its Euclidean operator norm sqrt(2) is already exact on that
unrestricted domain. Another arbitrary reduction would not be justified.
An improvement would require extra structure or correlation, not a smaller
constant for the same free map. This sidecar instead exploits the quadratic
spinor source before the subsequent curl readout.

## Algebraic decomposition

For either channel selector Q or I3, write the flat source as

    B_l,a(z) = Re[z^dagger K_l,a z],
    K_l,a = selector tensor Fflat_l,a.

The selector is checked to be exactly Hermitian. Replacing Fflat by its
Hermitian part leaves the real quadratic form unchanged. Set H=(K+K^dagger)/2,
z=z0+delta. Then the exact real-algebra identity is

    B(z) = B(z0) + 2 Re[z0^dagger H delta] + delta^dagger H delta.

No quadratic term is discarded. In particular, z0=0 does not make B zero
away from the center. The fixed real linear map L sends
[Re(delta), Im(delta)] to the 24 source components, ordered (l,a).
Its row is [2 Re(z0^dagger H), -2 Im(z0^dagger H)].

The frozen coefficients are computed as Gaussian rationals from the actual
stored binary64 inputs. With G=L L^T, the exact rational absolute-row bound
max_i sum_j |G_ij| bounds ||L||_2^2. An integer-arithmetic upward dyadic square
root supplies a fixed-map upper constant. Realification preserves the
complex Euclidean norm, so its tail has factor one, not sqrt(2).

The remaining quadratic deviation is evaluated with all field products,
discarded polynomial terms and input tails. The complete multiplier channel,
coframe factors and reciprocal volume remain in the source-cancelled solve.

## A useful negative result for derivatives

Applying the centered representation indiscriminately to derivatives makes
their majorants slightly worse at both radii. These candidate bounds are
saved explicitly rather than reported as an improvement. At r=1/16384,
the four candidate connection derivative tails are approximately

    [1.41107e-5, 1.02394e-5, 1.36371e-5, 1.38740e-5],

against the previous

    [1.40073e-5, 1.00900e-5, 1.34635e-5, 1.38683e-5].

The adopted connection value uses the improved centered source; all four
physical derivative models are retained in full from the parent, including
their coefficients and tails. A smaller tail is never attached to another
model's coefficient array. These are separate enclosures of the same actual
connection and its physical derivatives; no unknown value-tail derivative
is inferred. Independent original-connection checks cover both parts.

## Recomputed results

| Combined 80-row whole-cube estimate | r=1/16384 | r=1/32768 |
|---|---:|---:|
| Previous source-cancelled model | 0.001064593063 | 0.00003293248451 |
| Centered value, retained derivative models | 0.001020926221 | 0.00003157720855 |

This is about a further 4.1 percent reduction at each radius. The connection
value tail decreases from 3.35865e-6 to 2.76004e-6 at the larger radius.
The curl tail decreases from 0.000987209 to 0.000956832 and remains dominant.
The other three blocks also improve. Retained combined coefficients differ
from the parent by about 3.11e-14 in Frobenius norm through floating-point
regrouping. Nonzero degree-three and degree-four defects remain explicit.

Tests cover non-Hermitian flat forms (with their real quadratic part), both
Hermitian selectors, arbitrary off-shell spinors and derivatives, nonzero
quadratic deviations at zero center, uncertain-input perturbations, exact
Gram row bounds, complete cache keys, original connection jets, and original
80-row residual samples on axes, corners and an interior point.

## Proof boundary and reproduction

The fixed rational norm calculation is not an outward-rounded certificate
for rational-to-float conversion, the nonlinear enclosures or the full PDE.
Sample agreement is a control, not a regional proof. These estimates remain
far larger than sampled residuals; no exact closure, regional compatibility,
convergence, existence, distance-to-solution bound or physical identification
has been established.

Run `python -B analysis/HC_Cartan_Centered_Spinor_Source_Bound.py`, then
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_centered_spinor_source_bound`.
The saved JSON includes source fingerprints, all retained coefficients,
both fixed source maps, rejected derivative candidate tails and original
equation controls. Independent radius calculations use two local workers
with separate caches. Historical modules remain unchanged.
