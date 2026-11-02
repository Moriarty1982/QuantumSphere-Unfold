# Quartic derivative and normal-chart controls

## Question and fixed inputs

The quartic residual extension leaves a nonzero first prolongation. This audit
asks whether it scales as the derivative of the remaining fifth-order residual,
and refreshes the fixed-coordinate augmented normal-chart majorant for the
changed shared polynomial. No coefficients, sources, couplings or prescribed
data are re-fitted.

This remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison, not a native HC/C7 identification. The main TeX/PDF are unchanged.
The retained-origin rational kernel certificate remains authoritative; the
rounded-input origin failure and the anchored nature of the stable evaluation
are not removed by these neighborhood checks.

## Derivative calculation

Let F denote the 68 general field equations. If the leading remainder is
homogeneous of degree five, its first derivative is homogeneous of degree four:

    F(t x) ~ t^5 F(x),    DF(t x) ~ t^4 DF(x),    x . DF(x) ~ 5 F(x).

These are leading-order diagnostics here, not exact identities of the full
nonlinear field. The first prolongation comprises four derivatives of all 68
equations, hence 272 rows; it does not include derivatives of the additional
12 spatial-curl rows used by the preceding 80-row fit.

Two calculations use the same shared polynomial:

1. Differentiate the equations along its holonomic jet using the existing
   first-prolongation evaluator, at field-space steps 1e-4 and 5e-5.
2. Evaluate F on the actual polynomial at neighboring coordinates and take
   five-point coordinate derivatives. Steps rho/8 and rho/16, where
   rho = r times the radial fraction, are extrapolated to remove their leading
   fourth-order stencil error.

The second calculation does not use the supplied higher jets to differentiate
F. It therefore independently checks the shared-field/higher-jet construction.
Two bounded local workers evaluate independent directions.

## Results at three radial fractions

Here r = 1/16384. Listed values are norms of the actual 272-row prolongation,
not of a projected compatibility fit.

| Direction y | At r y | At r y / 2 | At r y / 4 |
| --- | ---: | ---: | ---: |
| (1,0,0,0) | 9.076e-3 | 5.670e-4 | 3.543e-5 |
| (0,1,0,0) | 5.805e-3 | 3.627e-4 | 2.267e-5 |
| (0,0,1,0) | 3.951e-3 | 2.470e-4 | 1.544e-5 |
| (0.3,0.2,0.1,0.4) | 3.172e-4 | 1.982e-5 | 1.238e-6 |
| (0.2,-0.3,0.1,0.4) | 7.292e-4 | 4.558e-5 | 2.849e-6 |

Successive ratios are approximately 16. Before the quartic correction, the
same calculation decays by approximately 8, consistent with differentiating
the then-leading quartic remainder. Thus the nonzero first prolongation is
consistent with the remaining truncation order at these samples, rather than
evidence by itself of an additional incompatible leading order.

Halving the holonomic field-space derivative step changes the result by
1.6e-9--3.2e-9. The extrapolated coordinate derivative differs by about
2.5e-8--1.7e-7. Its relative accuracy deteriorates at the smallest mixed-direction
residual, reaching about 13 percent there: coordinate subtraction is entering
its numerical noise floor, not furnishing an arbitrarily accurate derivative.

At radial fraction one, the Euler degree-five remainder has norm
1.8e-11--1.6e-10 for the axes and about 2.1e-12--2.2e-12 for the mixed directions.
These values are much smaller than the degree-four alternative. At smaller
fractions, residuals approaching 1e-12 cannot support equally strong relative
Euler accuracy. No exact fifth-order vanishing certificate is inferred.

## Refreshed normal-chart bound

The old bound cannot simply be inherited after changing polynomial coefficients.
The audit adds triangle majorants for every old and new correction to the
original finite-germ field balls. For a block polynomial

    P(x) = a sum_alpha c_alpha (x/r)^alpha,

each ordered derivative component is bounded by the sum of the nonnegative
derivative monomial weights at |x_i| = R times ||c_alpha||. Taking the Euclidean
norm over ordered derivative tuples preserves full-tensor multiplicities.
The resulting cube bound also covers the Euclidean ball ||x|| <= R.

Coframe, first coframe derivative, spinor, spatial spinor derivative and
multiplier balls all include the corrections. Inverse coframe, determinant and
inverse Cartan-Hessian bounds are then recomputed from the total coframe
deviation, before applying the existing direct normal-coefficient formula.
These are real-arithmetic majorant formulas evaluated in binary64, not
outward-rounded intervals. The field coefficients used are the stored rounded
polynomial representation, not an independent exact reconstruction of every
neighborhood value.

The refreshed augmented normal chart retains the following estimates:

| Quantity | Value |
| --- | ---: |
| Selected coordinate radius R | 2.3283064365e-10 |
| Center augmented minimum singular value | 0.10594420 |
| Matrix-change majorant | 0.04934813 |
| Augmented minimum singular lower estimate | 0.05659606 |
| Augmented inverse norm upper estimate | 17.6691 |

The selected radius agrees numerically with the earlier estimate because all
new corrections vanish to high order there. They were included, not ignored.
At r their added bounds are about 3.77e-13 for E, 1.76e-8 for dE, 3.74e-8 for
psi, 1.45e-3 for dpsi and 1.77e-8 for lambda. At R the largest relevant added
bound is only about 2.22e-20, for dpsi.

R is 262144 times smaller than r. At r the normal matrix-change majorant is
about 12994 and does not resolve the chart. This failure is a conservative
bound failure, not proof of chart singularity there. Positive estimates at R
do not extend automatically to the much larger residual-sampling region.
Nor do they prove exact normal rank 40, constraint propagation, hyperbolicity
or uniform regional PDE compatibility.

## Reproduce and next gap

Run `python -B analysis/HC_Cartan_Quartic_Derivative_Control.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_quartic_derivative_control`.
The adjacent JSON stores source fingerprints, derivative step controls, Euler
checks, the full radius-selection sequence and normal-chart sample checks.
Tests independently cover mixed polynomial derivatives, stencil extrapolation,
majorant multiplicities/enclosure and actual saved prolongation witnesses.

The next proof gap is a controlled extension or remainder/convergence argument,
not explaining a mysterious new first-derivative obstruction at these samples.
Neither one further polynomial fit nor a positive augmented inverse alone would
close that gap. No regional solution, all-order convergence, physical length
scale or new physical coupling identification is established.
