# Projector Readout Bound

## Scope And Search Result

This calculation sharpens the fixed readout constants in the 24 curl equations
of the existing neutral commuting-spinor odd-cross Einstein-Cartan comparison.
It changes neither the fields nor the equations and makes no native HC/C7
identification. Main TeX/PDF and published payloads remain unchanged.

An exploratory direct composition of the Cartan embedding, fixed-spinor
readout and exterior derivative did not improve the existing Gram row-sum
constant. Its smaller floating-point spectral norm was not substituted for
that certified upper constant. Inspection instead exposed a stronger exact
identity in the original four-output readout maps. The implementation uses
that identity only after checking it in rational arithmetic.

## Exact Fixed-Map Norm

For a real fixed readout matrix M with four output components, form

```text
G = M M^T,
kappa = trace(G)/3.
```

All five maps used by the curl calculation satisfy exactly

```text
G^2 = kappa G.
```

Because G is a positive semidefinite symmetric matrix, every eigenvalue is zero
or kappa. If kappa is positive, its trace shows that three eigenvalues equal
kappa and one is zero. Thus

```text
||M||_2 = sqrt(kappa).
```

For a zero map the norm is zero without dividing by kappa. The implementation
accepts rational matrices, checks the identity rather than assuming it, and
uses the previous Gram absolute-row-sum bound for nonprojector matrices. The
square-root upper constant is computed by the existing integer/dyadic routine,
with an exact rational check that its square is at least kappa.

The primary psi/psi map has kappa about 94.99945714. Its upper constant decreases
from about 11.65908595 to 9.74676650. The four fixed dp_r/psi maps also pass the
exact identity check and receive their own sharper constants. The fixed maps
are built from the unchanged binary64 origin data, treated as exact rational
inputs for these particular certificates.

## Variable Readouts Remain

Only the fixed-center map constant changes. For left/right spinors written as
their centers plus deviations, every left-deviation, right-deviation and joint
deviation term remains. This includes a zero-center readout with nonzero
variable contributions. No field component or low-order defect is projected
away. The null direction of one frozen output map need not remain fixed as the
spinors vary; it is not a global physical kernel, source-gate identification or
terminality result.

The joint exterior-derivative construction, improved implicit connection and
physical derivative error controls remain unchanged. No unknown value tail is
differentiated. Full cache keys include all fixed spinor/selector input bytes,
not only a compressed fingerprint.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous curl tail | 0.007877813 | 0.000243714 |
| New curl tail | 0.006705108 | 0.000207354 |
| Previous combined 80-row upper estimate | 0.010420118 | 0.000322793 |
| New combined 80-row upper estimate | 0.009564382 | 0.000296301 |

At the larger radius the curl tail comprises about 0.004875459 differentiated
readout and 0.001829649 other curl terms. All stored 80-row coefficient arrays
are bitwise unchanged. The other 56 components and their enclosures remain
unchanged. Nonzero degree-three/four defects are retained. Curl uncertainty
still dominates, closely followed by the constraint block.

## Verification And Limits

Eight focused tests cover exact scaled-projector and zero maps; nonprojector
fallback and rational-input validation; complete cache keys and unchanged
parent entries; variable/zero-center cross terms; nonzero off-shell curl
agreement with the independent original evaluator; all five rational Gram
identities and exact upper constants; bitwise coefficient preservation;
unchanged other 56 enclosures; original-equation samples; and proof boundaries.
The two radii are recomputed with two local workers.

Only the fixed-map constants carry exact arithmetic certificates. The full
nonlinear calculation remains binary64 without complete outward rounding.
Samples are controls, not proof of a whole-region estimate. Exact low-order
closure, regional PDE compatibility, convergence, native identification and
distance to a solution remain unproved. Numerical thresholds such as one or
0.01 are not existence criteria.

The executable and saved JSON report share this note's filename stem.
