# Lower and spatial repair with fixed normal coordinates

## Scope and changed contract

The previous attribution kept all lower jets fixed. It reduced the first-stage
obstruction by changing higher prescribed data, but a remainder of roughly
3e-7--6e-7 came from lower residuals and constitutive curls.

This calculation deliberately changes lower derivative data at each of the two
displaced samples. It keeps the field values E, psi, lambda and the first coframe
derivative dE fixed, along with all action couplings and 16 selected normal
coordinate values. It does not overwrite the frozen-data control, origin joint
candidate, or any earlier report.

Only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison
is involved. Main TeX/PDF and the published payload are unchanged. These are
independent pointwise jets, not a regional solution or native HC/C7 identification.

## Lower repair

The real lower derivative vector v has 320 entries:

- 160 symmetric E2 coordinates;
- 96 real coordinates for the full complex psi1 tensor;
- 64 lambda1 coordinates.

Let S select the usual 56 normal entries, and W be the existing 16 fixed
coordinate rows. Corrections are restricted to

\[
 \delta v=Zy,\qquad WSZ=0,\qquad Z^\top Z=I_{304}.
\]

The fixed coordinates include the ten previously selected gauge coordinates
and six source coordinates. This preserves their numerical coordinate values,
not an independently established physical gauge/source classification.

The residual is the primary 68-vector plus the 12 spatial curls J_ij, for a total
of 80 rows. At fixed E, dE, psi and lambda its dependence on v is at most
quadratic. Symmetric directional differences of size 16 therefore compute its
Jacobian without a small difference step; an independent smaller-step control
checks the polynomial behavior.

One full Newton correction suffices in both samples. The restricted 80-by-304
Jacobian has numerical rank 74, consistent with six Lorentz identities. This
observation is not a general exact-rank proof.

## First higher repair

After changing lower data, the entire 272-by-720 higher response is recomputed,
rather than reused from the unrepaired point. The generic finite-jet
compatibility tool eliminates higher variables and checks the 52 known rows
with their actual identity-source terms retained.

The recomputed higher matrix has numerical rank 220; the known row space still
matches its left kernel. The identity-source norm drops to about 6e-14--7e-14.
The remaining projected numerical norm is about 1e-10--2e-10, comparable to
the directional derivative evaluation error. No exact zero is inferred from
these floating-point calculations.

## Results

With r=1/16384 in the previous Taylor coordinates:

| Diagnostic | (r,0,0,0) | (0,r,0,0) |
| --- | ---: | ---: |
| Initial lower 80-row norm | 8.15e-7 | 4.27e-7 |
| Repaired lower 80-row norm | 6.41e-14 | 3.24e-14 |
| Lower correction coordinate norm | 5.41e-7 | 1.17e-7 |
| Fixed normal coordinate drift | 3.31e-17 | 3.45e-17 |
| All 24 constitutive curls | 6.32e-14 | 3.09e-14 |
| First derivative norm before higher correction | 0.04361 | 0.02607 |
| First derivative norm after higher correction, step 1e-4 | 5.81e-10 | 6.26e-10 |
| Same corrected jet, step 5e-5 | 2.00e-9 | 2.75e-9 |

The higher correction norms are about 0.04581 and 0.03630. The direct unprojected
first derivatives agree with the affine higher prediction to about 6e-10.
The smaller difference step increases roundoff sensitivity; the two evaluations
support numerical residuals below 3e-9, not a certified convergence order or a
sub-1e-9 rigorous error bound.

## What this resolves

The earlier first-stage obstruction can be removed numerically at these
individual points by repairing lower/spatial compatibility, without changing
the selected normal coordinate values or base field values. The remaining
higher compatibility is then at the observed numerical differentiation floor.
No new unexplained first-stage source is required in these examples.

## What remains

The repaired psi1, lambda1 and E2 at different coordinates are not yet proved to
be derivatives of one common field. Mixed partials are imposed within each
individual symmetric E2/higher tensor, but that is not regional integrability.

The next problem is a compatible spatial germ or regional construction whose
derivatives realize these conditions simultaneously. The full 1114-row higher
completion and regularity estimates must be checked afresh for any such new
germ. This calculation evaluates only the lower/spatial and first-prolongation
stages; it does not establish constraint propagation or all-order completion.

## Reproduce

Run `python -B analysis/HC_Cartan_Lower_Spatial_Repair.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_lower_spatial_repair`.
The adjacent JSON stores input fingerprints, fitted lower coordinates and higher
increments so the actual equations can be re-evaluated independently. Two local
workers handle the separate points, using injected cache/SVD services and the
repository copy of the generic compatibility helper.
