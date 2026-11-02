# Joint Exterior Curl Bound

## Scope

This calculation improves the residual enclosure for the existing neutral
commuting-spinor odd-cross Einstein-Cartan comparison. It does not alter the
fields, release any fixed parameters or identify a native HC/C7 operator.
Main TeX/PDF and published payloads remain unchanged.

The [previous Ricci calculation](HC_Cartan_Pair_Antisymmetric_Ricci_Bound.md)
leaves curl uncertainty as the largest block. Most of that uncertainty comes
from separately bounding six antisymmetric pairs of connection derivatives.
The new calculation applies their joint linear map before taking norms.

## Exact Exterior Operator

Let J_rs,ab = partial_r omega_s,ab. The six-pair operator D acts as

```text
(D J)_(r,s),ab = J_rs,ab - J_sr,ab,  r < s,
pair order = (01, 02, 03, 12, 13, 23).
```

Its six rows have disjoint supports of two entries, +1 and -1. Consequently

```text
D D^T = 2 I_6,
||D tensor I_16||_2 = sqrt(2).
```

The first identity is checked in exact integer arithmetic. A tensor with only
J_01,00=1 and J_10,00=-1 attains the induced norm. No antisymmetry of the input
J is required. This rank-six linear map is not a source-gate identification.

The implementation uses the dyadic upper value 1.4142135623730951, whose exact
rational square is checked to be at least two. All component norms are positive
Euclidean Frobenius norms, not indefinite spacetime contractions.

## Derivative Errors And Variable Spinors Remain

The existing connection evaluator provides four separately controlled models of
partial_r omega. If their tails are t_r, stacking them gives an error bounded
by sqrt(sum_r t_r^2). Thus the exterior derivative tail is bounded by

```text
sqrt(2) sqrt(sum_r t_r^2).
```

This is a deterministic vector-norm inequality. It does not require statistical
independence of the errors. These derivative models were built from the known
field polynomial and product/inverse derivative identities. No derivative of
an unknown value remainder is taken.

The differentiated term of the Hermitian curl identity is evaluated jointly:

```text
(1/2) Im[psi^dagger Q response(D J) psi].
```

The preceding centered readout evaluator retains its fixed center map and all
three variable-spinor cross terms. The direct spinor derivative, connection
value and coframe derivative terms are also retained. Their six-pair tail is
combined with the joint differentiated-readout tail by the triangle inequality;
no cross-family cancellation is assumed. Approximation tails and discarded
high-degree products remain present.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous curl tail | 0.233297677 | 0.007269481 |
| Joint differentiated-readout tail | 0.130653064 | 0.004072800 |
| Other curl terms tail | 0.007353421 | 0.000226285 |
| New curl tail | 0.138006485 | 0.004299086 |
| Previous combined 80-row upper estimate | 0.296850549 | 0.009249676 |
| New combined 80-row upper estimate | 0.229648062 | 0.007154950 |

The first 56 rows, including the improved coframe enclosure, are unchanged.
The retained curl coefficients differ from the predecessor by about 8.09e-15
in Frobenius norm from regrouping roundoff. Nonzero degree-three/four defects
are retained rather than refitted or set to zero. Coframe uncertainty is now
the largest block, with tail 0.175082474 at the larger radius.

## Verification And Limits

Nine focused tests cover the exact Gram identity, norm saturation, pair order,
input validation, separately bounded derivative errors, variable/zero-center
spinors, polynomial agreement with the predecessor, nonzero off-shell curl
agreement with the original evaluator, input fingerprints, unchanged first
56 rows and nonzero low-order defects. Axis, cube-corner and interior samples
are checked against the original full equations; they are controls, not proof
of a whole-cube estimate. The two radii are recomputed with two local workers.

Only the fixed operator constants have exact arithmetic certificates. The
surrounding nonlinear calculation remains binary64 without complete outward
rounding. The estimate is still much larger than sampled residuals; crossing
one is not an existence threshold. Exact low-order closure, regional
compatibility, convergence and distance to a solution remain unproved.

The executable and saved JSON report share this note's filename stem.
