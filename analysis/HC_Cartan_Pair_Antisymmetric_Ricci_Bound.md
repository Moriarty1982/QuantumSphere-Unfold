# Pair-Antisymmetric Ricci Bound

## Scope

This is a sharper enclosure for the existing neutral commuting-spinor,
odd-cross Einstein-Cartan comparison. It changes neither the fields nor the
equations. It does not identify a native HC/C7 gravitational operator.
Main TeX/PDF and published payloads remain unchanged.

The preceding [centered readout calculation](HC_Cartan_Background_Readout_Bound.md)
leaves the Ricci pullback as the largest coframe uncertainty. This calculation
uses only the two antisymmetries already satisfied by curvature of the real
Lorentz connection: antisymmetry in the coordinate pair and in the Lorentz pair.
It does not assume Ricci symmetry, interchange of the pairs, a torsion-free
connection, a Bianchi reduction or any field equation.

## Exact Linear Bound

All norms here are positive Euclidean Frobenius norms of the stored tensor
components, not indefinite Lorentz contractions. Let

```text
P R = (R_mn ab - R_nm ab - R_mn ba + R_nm ba)/4,
L(R)_ac = sum_b R_ab cb.
```

The two commuting antisymmetrizers make P an orthogonal projector of rank 36.
At the identity inverse-coframe center used by the actual calculation, the
restricted Ricci operator is L P. With i = vec(I_4), exact rational arithmetic
gives

```text
(L P)(L P)^T = (1/2) I_16 + (1/4) i i^T.
```

Since i has squared norm four, the eigenvalues are 3/2 once and 1/2 fifteen
times. Thus the exact induced norm is sqrt(3/2), replacing the unrestricted
norm two. The direction (L P)^T i attains the norm, so this is sharp for the
stated linear map. Its output need not be a symmetric matrix.

The implementation uses the dyadic upper value 1.2247448713915892. Integer
arithmetic checks that its exact rational square is at least 3/2. This certifies
that one constant, not the complete floating-point nonlinear calculation.

## No Variable Terms Removed

Writing the inverse coframe as A = I + dA, the pullback remains

```text
Ricci(A,R) = L(R)
  + contract(dA, I, R)
  + contract(I, dA, R)
  + contract(dA, dA, R).
```

Every cross term, inverse tail and discarded high-degree product remains in the
Taylor enclosure. For nonidentity centers the implementation falls back to the
predecessor's unrestricted centered bound; it does not reuse sqrt(3/2).

The actual curvature satisfies R=P R. If p is its polynomial approximation with
error at most t, then

```text
||R - P p|| = ||P(R-p)|| <= t.
```

This justifies projecting the approximate polynomial while retaining its entire
tail. It does not justify projecting an arbitrary physical tensor or declaring
its error zero. Production coefficient projection changes have Frobenius norm
about 2.45e-16 and 1.22e-16 at the two radii; they are recorded explicitly.
The implementation's restricted pullback requires the caller to affirm actual
pair antisymmetry. The coframe path obtains it from the existing Lorentz
curvature construction.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous Ricci-frame tail | 0.280456622 | 0.008743302 |
| New Ricci-frame tail | 0.171743908 | 0.005354157 |
| Previous coframe tail | 0.283795190 | 0.008846777 |
| New coframe tail | 0.175082474 | 0.005457632 |
| Previous combined 80-row upper estimate | 0.371491704 | 0.011577401 |
| New combined 80-row upper estimate | 0.296850549 | 0.009249676 |

The other 64 rows, including the latest curl enclosure, are unchanged. The
retained coframe coefficients differ by about 3.33e-15 from regrouping and
projection roundoff. Degree-three/four defects are still nonzero; none is fitted
again or set to zero. Original-equation sample checks at an axis, two cube
corners and an interior point lie below the enclosures but do not prove them.

## Verification And Remaining Gap

Nine focused tests cover the exact projector, Gram matrix, spectrum and
saturating input; the exact dyadic upper constant; explicit antisymmetry
requirements; retention of approximation uncertainty and all variable inverse
terms; arbitrary off-shell coframe data with nonsymmetric Ricci; the nonidentity
fallback; input fingerprints; the unchanged 64 rows; and the scope boundary.

The JSON report and executable share this filename stem. The two radius cases
are recomputed with two local workers. The result is still a binary64 majorant
without outward rounding of all operations, and remains much larger than the
sampled residual. A bound below one is not an existence criterion. Exact
low-order closure, regional compatibility, convergence and distance to an exact
solution remain unproved.
