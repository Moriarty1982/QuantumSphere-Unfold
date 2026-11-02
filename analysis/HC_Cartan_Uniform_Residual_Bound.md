# Whole-ball residual bound: a negative sharpness control

## Fixed problem and new calculation

The prior quartic extension and derivative control tested a shared polynomial
field at finitely many coordinates. This audit constructs a conservative
whole-ball enclosure of all 80 residual components of that same rounded field:
16 constitutive constraints, 24 real probe rows, 16 coframe rows and 24 curls.
The first 12 curls coincide with the mixed rows in the 68-equation parent;
the last 12 are the additional spatial curls. No field coefficients, sources,
couplings or assumptions are fitted or changed.

Scope remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison, not the native HC/C7 theory or a physical coupling identification.
The main TeX/PDF remain unchanged. The exact retained-origin kernel certificate
is not replaced by rounded dependent coordinates or by this enclosure.

## Construction

The existing Frobenius tensor-ball arithmetic supplies value/variation bounds
for multilinear contractions. Each value ball is lifted to a first jet carrying
four coordinate derivative balls. The product rule propagates those derivatives
through the actual connection construction. In particular,

    d(E^-1) = -E^-1 (dE) E^-1,
    d(H^-1) = -H^-1 (dH) H^-1.

The old corrected field balls are extended to include all second coframe,
first spinor and first multiplier derivatives. Their polynomial majorants
include both the earlier spinor reprepare and the later quartic correction.
The known coframe/determinant/Cartan-Hessian inverse bounds supply the inverse
value balls. No finite-difference residual derivatives are used in the enclosure.

The resulting connection, its first derivatives, the real symmetric probe
operator, the independent coframe Euler derivative and all six curl pairs are
evaluated directly in ball arithmetic. At zero input radii, their centers are
checked against the independent original 80-row evaluator at the origin,
displaced points and perturbed off-shell jets. Matching errors are about 1e-13
on the saved field. The off-shell control prevents success from depending only
on already-fitted nearly-zero equations.

These are real-arithmetic enclosure formulas evaluated with ordinary floating
point numbers. Arithmetic roundoff is not enclosed. In particular a zero-radius
control does not assert exact equality of independently rounded evaluations.
This is not an interval-certified bound.

## Result: finite but not useful for the desired fifth-order estimate

Let r = 1/16384 be the residual sampling radius and let
R = 2.3283064365e-10 be the refreshed augmented-chart radius.

| Radius | Whole-ball residual upper estimate | Example sampled residual norms |
| --- | ---: | ---: |
| r | 2.496e6 | 9.61e-8, 2.78e-7 |
| r/2 | 1.228e6 | 3.00e-9, 8.69e-9 |
| R | 9.255 | 6.88e-14, 8.65e-14 |
| R/2 | 4.627 | 5.69e-14, 6.67e-14 |

The estimate encloses the samples but is many orders too loose to establish
the observed small residual uniformly. At R its largest block contributions
are curls (about 9.199) and coframe equations (about 1.017); individual block
norms are combined quadratically, not added as independent physical effects.

For small radii the bound decreases by a factor near two under halving, not
32. This is a limitation of the natural enclosure, not evidence that the actual
field has lost the previously observed fifth-order decay. Independent balls
discard correlations and cancellations: even the expression X-X has radius
twice that of X under ordinary ball subtraction. Applying this arithmetic to
the unreduced field expressions cannot preserve all cancellations between
homogeneous residual coefficients.

Therefore this calculation is a retained negative control. It must not be
reported as a sharp fifth-order remainder estimate or as a successful regional
completion. A positive normal-chart inverse estimate does not fix this loss of
residual sharpness, and is not an inverse of the full regional PDE operator.

## The estimate actually needed

For a C^5 residual map F on a convex coordinate ball of radius L, write its
degree-four Taylor polynomial with normalized coefficients

    C_alpha = L^|alpha| (partial^alpha F)(0) / alpha!.

Set epsilon_k = sum_{|alpha|=k} ||C_alpha||. If

    M5 >= L^5 sup_{||z|| <= L} ||D^5 F(z)||_op / 120,

then for 0 <= s <= 1 and ||x|| <= s L,

    ||F(x)|| <= sum_{k=0}^4 epsilon_k s^k + M5 s^5.

To see the remainder factor, apply one-variable Taylor's integral formula to
g(t)=F(t x). Its fifth derivative is D^5 F(t x)[x,x,x,x,x], and the integral
of (1-t)^4/4! over [0,1] is 1/120. The polynomial terms are bounded by their
coefficient norms since each |x_i/L| <= s. This derivation is conditional on
actual bounds for those derivatives and coefficients, not a computation of M5.

The earlier numerical homogeneous fits do not certify all epsilon_k as zero.
In particular the origin residual and the extraction/rounding uncertainty
cannot be discarded. A hypothetical extrapolation of a 1e-7 fifth-order error
at r to R would give roughly 8e-35; the actual binary64 evaluations at R are
instead near their 1e-13 numerical floor. That scale comparison is illustrative,
not an inferred uniform remainder bound or proof of an exact nonzero residual.

The next useful refinement must preserve the normalized Taylor coefficients
and bound only the remaining tail, with inverse/coframe operations controlled
on the same domain. Outward-rounded errors and low-order coefficient errors
must also be included before promoting it to a certificate. More collocation
points, a larger fixed ball majorant, or another apparent radial slope do not
substitute for these quantities. Even a small residual certificate would still
need PDE compatibility and a suitable functional inverse to imply closeness
to an exact regional solution.

## Reproduce and tests

Run `python -B analysis/HC_Cartan_Uniform_Residual_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_uniform_residual_bound`.
Two bounded local workers evaluate independent radii. The adjacent JSON stores
fingerprints, block estimates, zero-radius and sampled controls, and explicit
failure/scope flags. Tests cover the complex product rule, full tensor norms,
field enclosure, original-equation agreement and the dependency-loss control.
No convergence, fifth-order uniform bound or distance-to-solution certificate
is claimed.
