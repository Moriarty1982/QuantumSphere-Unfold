# Common polynomial germ: holonomic jets, failed regional control

## Purpose and contract

The preceding repair solved lower and first-prolongation equations at separate
points, with independently chosen derivative tensors. This experiment instead
uses derivatives of one polynomial correction. It tests whether lower-equation
collocation alone is sufficient to continue the solution between those points.

This is a different experiment, not an overwrite or interpolation of the saved
independent repaired jets. Base field values outside the origin may now change;
the selected 16 normal coordinate values are imposed only at the three training
points. Action couplings and the original finite jet at the origin are retained.

Only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison
is used. Main TeX/PDF and the published payload are unchanged. There is no
regional field-equation solution or native HC/C7 identification here.

## One shared polynomial

Let r=1/16384 and y=x/r. The correction is

\[
 \delta E=r^2\sum_{|\alpha|=5} e_\alpha y^\alpha,\qquad
 \delta\psi=r\sum_{|\alpha|=5} p_\alpha y^\alpha,\qquad
 \delta\lambda=r\sum_{|\alpha|=4} l_\alpha y^\alpha.
\]

There are 56 degree-five and 35 degree-four four-variable monomials, giving
2800 real coefficients: 896 coframe, 1344 spinor and 560 multiplier entries.
The powers of r condition the derivative scales; r is a Taylor coordinate
scale, not a physical length or a uniform validity radius.

All derivatives are obtained analytically from this single coefficient vector,
not independently fitted tensor entries. Mixed derivatives therefore commute
within the correction. The original Taylor field plus the correction is a
single smooth polynomial field, wherever its coframe is usable.

At x=0 the correction and its derivatives through order four for E and psi,
and order three for lambda, vanish exactly by polynomial degree. Those are the
orders entering the existing origin 1114-row finite-jet calculation. Its input
jet is preserved; no new higher-order or regional completion follows from that.

## Lower collocation

At each training point impose the 80 primary/spatial-curl rows and 16 fixed
normal coordinate values. The training coordinates are

\[
 (r,0,0,0),\quad(0,r,0,0),\quad(r/2,r/2,0,0).
\]

The shared 288-by-2800 Jacobian has numerical rank 270. One full Newton step
reduces the combined residual from 9.72e-7 to 1.40e-13. The three actual lower
residual norms are 6.15e-14, 8.20e-14 and 9.47e-14; selected normal coordinate
drifts are below 3e-21. The fixed coordinates are not a physical source/gauge
classification, nor are their values asserted to be fixed throughout a region.

The largest sampled base spinor/multiplier changes are around 7e-12 and 5e-12;
coframe-value changes are around 1e-17. Such coframe-value changes can be below
machine resolution when added to the identity. Derivative tensors are computed
from the polynomial formula, not recovered by subtracting those tiny field values.

## Held-out checks: the limitation is real

The following coordinates were not used in the fit:

| Coordinate | Baseline lower norm | Corrected lower norm |
| --- | ---: | ---: |
| (r/2,0,0,0) | 1.02e-7 | 2.75e-7 |
| (0,r/2,0,0) | 5.33e-8 | 1.14e-7 |
| (r/sqrt(2),r/sqrt(2),0,0) | 8.87e-7 | 1.42e-6 |
| (0,0,r,0) | 1.82e-7 | 1.82e-7 |

The first three controls get worse; the off-plane control is essentially
unchanged. These are actual unprojected equations, not a surrogate fit loss.
They rule out interpreting this collocation result as a regional PDE solution.
They do not exclude other polynomial coefficients or a different construction.

The first 272 differentiated equations were deliberately not fitted. Their
norms at the three training points are 0.17159, 0.11465 and 0.05166, despite
the small values of the lower equations there. The earlier separate-point
first-prolongation residuals below 3e-9 must not be attached to this new polynomial.

## Interpretation and next step

The kinematic problem of producing a shared differentiable ansatz is addressed,
but the differential field equations are not closed. Zeros of a residual at
isolated nodes do not control its derivatives or values between the nodes.

Baseline lower norms approximately scale by 1/8 when halving either axis
coordinate, suggesting a leading cubic residual in this diagnostic. This is an
inference from the sampled ratios, not a complete symbolic Taylor expansion.
The fitted node cancellations have not removed that leading residual globally.

A useful next step is to determine the first nonvanishing Taylor coefficients
of the residual and solve their coupled conditions, or explicitly include
derivative equations in the common-field fit. Merely increasing the number of
lower-equation nodes would still need held-out and derivative controls. Any
successful finite step remains subject to higher-order compatibility, regularity
and regional existence requirements.

## Reproduce

Run `python -B analysis/HC_Cartan_Common_Polynomial_Germ.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_common_polynomial_germ`.
The adjacent JSON stores the single coefficient vector and all controls.
The generic compatibility helper and injected cache/SVD services are reused;
two local workers compute independent training Jacobians. Tests independently
verify monomial derivatives, field packing, mixed-derivative consistency, origin
jet preservation and the saved failed held-out controls.
