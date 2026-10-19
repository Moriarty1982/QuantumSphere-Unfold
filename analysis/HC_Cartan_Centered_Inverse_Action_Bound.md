# Centered Inverse Action Bound

## Scope

This calculation improves the same neutral commuting-spinor odd-cross
Einstein-Cartan comparison, not native HC/C7 identification. It changes neither
the fields nor the equations and does not refit any coefficients. Main
TeX/PDF and published payloads remain unchanged.

After the [Hermitian constraint enclosure](HC_Cartan_Hermitian_Constraint_Bound.md),
connection uncertainty still dominates curl/coframe bounds. The implicit solve
H k=f was multiplying its vector remainders by the Frobenius norm of the fixed
inverse center, about 4.242640687. Its induced norm is at most one. This step
uses a checked fixed-matrix bound before multiplying uncertain vector models.

## Centered Matrix/Vector Product

For a matrix model A and vector model b, write

```text
A = A0 + dA,
A b = A0 b + dA b.
```

The first term is evaluated as one fixed linear map, with tail bounded by the
induced norm of A0 times the entire vector tail. The second term uses the
existing Taylor product arithmetic, retaining every variable matrix cross term,
matrix tail and discarded high-degree product. The actual stored A0 is used in
all coefficients, not a rounded or projected replacement.

The new product is applied both to k=H^-1 f and to its existing physical
derivative identity

```text
dk = H^-1 [df - (dH) k].
```

The inverse value itself retains the earlier Neumann model and its complete
remainder. This is not a new inverse certificate or a differentiation of an
unknown value tail.

## Fixed-Matrix Certificate

The center is treated as an exact rational matrix corresponding to its stored
binary64 entries. A nearby half-integer reference R is constructed only for
bounding its norm. For G=R^T R the code checks exactly

```text
G^2 - (5/4) G + (1/4) I = 0.
```

Since G is positive semidefinite and symmetric, its spectrum is contained in
{1/4, 1}, hence ||R||_2 <= 1. The full center discrepancy E=A0-R is included:

```text
||A0||_2 <= 1 + ||E||_F,
||E||_F^2 = sum_ij E_ij^2.
```

The error square is computed in rational arithmetic. Its square-root bound and
the final sum are rounded upward with exact rational comparisons. If the
reference polynomial does not hold, the code falls back to the exact Gram
absolute-row-sum bound of the actual center. No reference identity is assumed
for an arbitrary matrix.

In both production radius cases the 24-by-24 center is already exactly equal
to R: the recorded discrepancy square is zero and the certified upper norm is
one. The helper also has a test with a nonzero reference discrepancy, ensuring
that the error is not silently dropped. Reference rounding never changes the
matrix used in the Taylor calculation. Cache keys contain shape and all center
bytes, not a compressed fingerprint alone.

## Recomputed Results

| Quantity | Radius 1/16384 | Radius 1/32768 |
| --- | ---: | ---: |
| Previous constraint tail | 0.000119442 | 0.000003707 |
| New constraint tail | 0.000041522 | 0.000001274 |
| Previous probe tail | 0.000292595 | 0.000009082 |
| New probe tail | 0.000098280 | 0.000003013 |
| Previous coframe tail | 0.003432194 | 0.000106443 |
| New coframe tail | 0.001004658 | 0.000030933 |
| Previous curl tail | 0.006705108 | 0.000207354 |
| New curl tail | 0.002154855 | 0.000066429 |
| Previous combined 80-row upper estimate | 0.007539119 | 0.000233285 |
| New combined 80-row upper estimate | 0.002379942 | 0.000073351 |

All four blocks are recomputed with the same improved connection and the latest
previously checked readout formulas. Connection value uncertainty at the larger
radius decreases from about 2.31e-5 to 7.17e-6; its derivative uncertainties
decrease to about 7.52e-5 through 8.72e-5. Independent original-equation and
connection-jet samples remain inside the respective enclosures.

The retained 80-row coefficient difference is about 3.57e-19 in Frobenius norm,
arising from regrouping. Nonzero degree-three/four defects remain. A smaller
bound is not a smaller actual residual of the unchanged fields.

## Verification And Remaining Gap

Eight focused tests cover the reference polynomial and nonzero discrepancy;
exact upward sums; nonreference fallback and invalid inputs; the fixed identity
action without a Frobenius factor; variable matrix/vector cross terms,
discarded products and uncertain inputs; off-shell agreement with independent
original connection jets; exact production certificates; fingerprints; scope;
retained low-order defects; and original-equation sample checks. The two radius
cases use two local workers, each with a local fixed-matrix cache.

Only fixed-center matrix constants carry exact arithmetic certificates. This
does not validate the numerical inverse itself by interval arithmetic. The
complete nonlinear enclosure remains binary64 without full outward rounding.
Samples are controls, not whole-region proof. Exact low-order closure, regional
PDE compatibility, convergence, native identification and distance to an exact
solution remain unproved.

The executable and saved JSON report share this note's filename stem.
