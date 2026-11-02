# Isometric Curvature Bound

## Scope

This is a sharper residual enclosure for the existing neutral commuting-spinor
odd-cross Einstein-Cartan comparison. It changes neither fields nor equations,
introduces no new physical assumption, and does not identify a native HC/C7
operator. Main TeX/PDF and published payloads remain unchanged.

After the [joint exterior curl bound](HC_Cartan_Joint_Exterior_Curl_Bound.md),
coframe uncertainty dominates. Its Ricci contribution inherits a loose curvature
tail, largely from generic bounds on multiplication by the fixed signature
matrix. This calculation replaces those factors by their exact induced norms.

## Exact Signature Isometry

The fixed frame signature used by the existing evaluator is

```text
eta = diag(-1, 1, 1, 1),
eta^T eta = I_4.
```

For the positive Euclidean Frobenius norm of stored components, multiplying any
tensor axis by eta only changes signs. It therefore has exact induced norm one,
and preserves every coefficient norm and remainder bound. Acting on two axes
also has norm one since (eta tensor eta)^T(eta tensor eta)=I_16.

This statement is about component-error bounds. It does not assert that an
indefinite Lorentz contraction is a positive norm, and it does not apply to an
arbitrary varying metric. The implementation validates that the matrix is
exactly diagonal with entries plus or minus one, rejecting other matrices.

## Unchanged Curvature Formula

With Omega_m,ab the lower-index connection and J_mn,ab=partial_m Omega_n,ab,
the previous construction is retained:

```text
B_m = eta Omega_m,
R_comm,mn = (B_m B_n - B_n B_m) eta,
R_der,mn = eta (J_mn - J_nm) eta,
R = R_comm + R_der.
```

All connection-value tails, controlled physical derivative tails and discarded
high-degree products remain. In particular, the commutator remains a full
nonlinear product, not a frozen or linearized approximation. No derivative of
an unknown value remainder is taken.

The older generic Frobenius estimate assigns norm two to each eta action. In
the derivative term, its two actions thus contributed a factor four where one
is exact. The coordinate antisymmetrization still contributes its valid norm
two. If t_J bounds the stacked first-derivative tensor, the new derivative
curvature tail is 2 t_J rather than 8 t_J.

Signed-axis actions also improve the nonlinear commutator bound, retaining its
quadratic uncertainty term. The existing pair-antisymmetric Ricci enclosure,
all variable inverse corrections and the centered matter readout are then
applied without changes.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous total curvature tail | 0.140228306 | 0.004371651 |
| New derivative curvature tail | 0.031653062 | 0.000987291 |
| New commutator curvature tail | 0.003403993 | 0.000105621 |
| New total curvature tail | 0.035057054 | 0.001092913 |
| Previous coframe tail | 0.175082474 | 0.005457632 |
| New coframe tail | 0.046274514 | 0.001442014 |
| Previous combined 80-row upper estimate | 0.229648062 | 0.007154950 |
| New combined 80-row upper estimate | 0.155646041 | 0.004846335 |

The retained curvature coefficients agree exactly with the predecessor; the
complete stored 80-row coefficient arrays are also bitwise unchanged in this
evaluation. Constraint, probe and curl enclosures are
unchanged, including the curl tail 0.138006485 at the larger radius. Nonzero
degree-three/four defects are retained. No coefficient is fitted again or
replaced by zero. Curl uncertainty is now the largest block again.

## Verification And Remaining Gap

Nine focused tests check exact signature Gram identities, complex coefficient
norm and tail preservation, validation failures, predecessor coefficient
agreement, discarded high-degree products, uncertain connection values and
derivatives, nonzero off-shell coframe agreement with the original equations,
input fingerprints, unchanged other 64 rows and scope restrictions. Original
full-equation samples at an axis, cube corners and an interior point remain
below the enclosures. They are controls, not a whole-cube proof. The two radii
are recomputed with two local workers.

Only the fixed linear constants are certified by exact arithmetic. The full
nonlinear majorant remains binary64 without outward rounding of all operations
and is still much larger than sampled residuals. A bound below one is not an
existence threshold. Exact low-order closure, regional compatibility,
convergence and distance to an exact solution remain unproved.

The executable and saved JSON report share this note's filename stem.
