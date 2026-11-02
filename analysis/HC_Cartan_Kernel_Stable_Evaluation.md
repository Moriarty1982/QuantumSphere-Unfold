# Stable retained-origin evaluation from exact kernel parameters

## Purpose and scope

The cubic spinor reprepare supplied an exact free/pivot representation preserving
the retained origin equations, but its rounded binary64 fourth-spinor array
failed the old numerical tolerance. This audit separates input rounding from
arithmetic cancellation and implements a stable retained-equation update.

This is an affine update anchored to the inherited 1114-vector, not a fresh
high-precision evaluation of all nonlinear parent equations. It adds no new
Taylor order, regional solution, uniform error certificate or physical
identification. Main TeX/PDF remain unchanged.

## Reconstruction, not precision promotion

The existing certificate stores the rational 4-by-24 readout A, four dependent
pivot columns, 20 free columns, a rational pivot map and 35 sets of free
degree-four monomial coordinates. This audit checks:

- the free/pivot columns partition all 24 coordinates;
- A_pivot P + A_free = 0 exactly;
- the readout agrees with the actual frozen origin inputs;
- each reconstructed monomial and its fourth-derivative update lie in ker A.

Fourth derivatives are formed from those reconstructed parameters using exact
factorials and the rational radius r=1/16384. No rounded dependent pivot is
promoted to an exact input. Exact rational contraction gives zero for all 320
retained C3 updates.

Only C3 depends on this fourth-spinor change in the retained 1114-vector. For
each triple and constitutive coordinate, the update is the corresponding
readout of the symmetric fourth derivative. All other retained rows are
unchanged. This is the same structural dependence checked in the prior audit.

## Independent precision paths

Private mpmath contexts with 40 and 80 decimal digits reconstruct the pivots
again at their own precision. Two paths are compared:

1. Contract A with the fourth-derivative increment directly.
2. Contract A with the new and old fourth derivatives separately, then subtract.

Neither path manually substitutes zero. The results are:

| Quantity | 40 digits | 80 digits |
| --- | ---: | ---: |
| Direct parametric C3 update norm | 1.07e-32 | 7.03e-73 |
| Direct/incremental discrepancy | 3.41e-35 | 4.42e-75 |
| Anchored 1114 residual norm | 4.87113987858253e-10 | 4.87113987858253e-10 |

The anchor is the previously evaluated binary64 residual vector. Its original
error has not been independently bounded or recomputed at high precision here.
The stable update preserves that reference value; it does not create a new
independent 1114-row solution or certify that the anchor is an exact zero.

## Why the rounded input cannot be rescued by more digits

The former candidate was assembled as rounded new fourth-derivative coordinates.
Treating those stored binary64 numbers as exact rational inputs yields a nonzero
C3 update of norm 7.99e-8. Thus the input itself has already left the exact kernel.

Both the 40- and 80-digit evaluations of those rounded inputs reproduce this
same nonzero update. Their anchored residual is about 7.99e-8. Merely increasing
working precision after dependent pivots have been rounded cannot recover the
missing relation.

The full raw binary64 re-evaluation still gives about 1.28e-7. Its update differs
from the exact linear update of the rounded inputs by about 1.08e-7, exposing
an additional arithmetic-cancellation effect. These norm values are not additive
error budgets. The failed raw recheck remains a valid negative control.

## Usage boundary

For retained-origin checks, use the exact free/pivot representation and a
high-precision or exact linear update. Do not export only rounded dependent
coefficients and then treat them as an equivalent authoritative representation.

This zero-update property is origin-specific. The readout depends on the
background spinor. Away from the origin, evaluate the actual modified fields
and residuals; copying the origin anchor or forcing the update to zero would
hide the remaining quartic field errors.

The next-order cubic/quartic and regularity calculations remain separate. No
previous regional majorant is refreshed by stabilizing this origin update.

## Reproduce and controls

Run `python -B analysis/HC_Cartan_Kernel_Stable_Evaluation.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_kernel_stable_evaluation`.
The adjacent JSON stores fingerprints, library versions, both precision paths
and the exact rounded-input failure. Two independent precision contexts run
with two bounded local workers without changing global mpmath settings.

Tests also perturb a non-kernel fourth-spinor direction and compare the linear
update with the actual full parent evaluator. This checks that the method does
not erase arbitrary residual changes just because the intended update is zero.
