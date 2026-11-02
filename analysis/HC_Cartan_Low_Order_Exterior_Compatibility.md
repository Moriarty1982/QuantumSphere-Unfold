# Low-order exterior compatibility of the Cartan residual

## Scope

This audit diagnoses the fixed polynomial field of the neutral commuting-spinor
odd-cross Einstein-Cartan comparison. It does not fit new coefficients, alter
the field, change an enclosure or identify native HC/C7 physics. Main TeX/PDF
remain unchanged. The latest centered-source report and all its inputs are
fingerprinted before the retained coefficient arrays are used.

## The curl defects are not independent

Let C_a=C_a,mu dx^mu be the constitutive residual, not an assumed zero field.
The unchanged 24 curl rows are its ordinary exterior derivative,

    F_a = d_x C_a,             d_x F_a = 0.

For y=x/r and homogeneous coefficients this gives

    F^(n) = (1/r) d_y C^(n+1).

The audit differentiates the saved constitutive coefficient polynomials,
without differentiating unknown tails. Available C coefficients through degree
four permit comparison with F through degree three. At r=1/16384:

| Curl degree | Curl coefficient Frobenius norm | Difference from (1/r)d_y C |
|---|---:|---:|
| 0 | 6.28713e-14 | 9.64590e-14 |
| 1 | 2.54145e-15 | 1.36876e-15 |
| 2 | 2.23333e-18 | 4.09694e-16 |
| 3 | 9.77447e-11 | 1.02375e-15 |

Thus the resolved cubic curl defect is reproduced by the derivative of the
constitutive degree-four defect. At the lowest levels discrepancies are as
large as the computed coefficients; they are not evidence of exact nonzero
physical obstructions. The coefficient Frobenius norms here differ from the
sum-of-monomial norm bounds used by the enclosure reports.

## Exact quartic compatibility dimensions

A homogeneous two-form of degree four in four variables has 35 monomials
times six components, or 210 coordinates per constitutive component. Use the
radial vector Y=sum_mu y^mu partial_mu and contraction i_Y. The homogeneous
polynomial homotopy identity is

    d_y i_Y F + i_Y d_y F = (4+2) F = 6 F.

This is checked on every basis coefficient by integer matrices, not sampled
directions. With N=d_y i_Y and M=i_Y d_y the checks give

    N+M=6 I,       N^2=6 N,       d_y N=0,       trace(N)/6=140.

Consequently N/6 is a projector onto the closed two-forms. It is not assumed
orthogonal. Its trace gives exact rank 140; the complementary rank is 70.
For all four constitutive components there are **840 quartic curl coordinates,
560 closed directions and 280 independent compatibility conditions**.
These are ranks of the polynomial exterior complex, not ranks of the full
field-equation symbol or a physical source gate.

## A formal potential, not a field correction

For the stored quartic curl F4 define

    C5_formal = (r/6) i_Y F4,
    F4 = (1/r) d_y C5_formal + (1/6) i_Y d_y F4.

The saved r=1/16384 coefficients give:

| Quantity | Frobenius norm |
|---|---:|
| F4 | 1.20434e-10 |
| d_y F4 | 9.09436e-19 |
| Homotopy obstruction i_Y d_y F4 / 6 | 2.77858e-19 |
| C5_formal | 2.21214e-15 |
| Floating reconstruction discrepancy | 9.35556e-27 |

The quartic defect is nearly closed at the observed arithmetic scale; its
nonzero floating obstruction is retained. It is not certified to vanish and
does not certify exact incompatibility either. The homotopy decomposition is
algebraically valid even for nonclosed input, so its tiny reconstruction error
alone is not evidence that the obstruction is zero.

If a curl-free compatibility condition held exactly, -C5_formal would be a
formal constitutive correction whose exterior derivative cancels F4. But C is
not a free field: it is determined by the coframe, spinor, multipliers and
Cartan solution. Realizing that correction through permitted field coefficients
while preserving all other equations is an additional unsolved lifting problem.
The formal potential has not been installed as a field correction. Its size
is not a distance-to-solution estimate. Potentials also have gradient freedom.

## Why the next order cannot fix this one

The 80-row residual uses at most second coframe derivatives, first spinor
derivatives and first multiplier derivatives. The second spinor derivatives
cancel in the exterior constitutive identity. Around the present nonsingular
coframe/Cartan centers the remaining algebraic inverse operations are analytic.

Adding homogeneous E7, psi6 and lambda6 corrections therefore first changes
the residual at degree at least min(7-2,6-1,6-1)=5. No combination of these new
coefficients can remove an already nonzero degree-four coefficient while
keeping lower field data fixed. An indefinite sequence of higher-order fits
does not repair earlier approximate fits retrospectively.

The next repair should revisit the existing degree-four response system
(E6, psi5, lambda5), retain its coordinate and exact-origin-kernel restrictions,
and use directly computed Taylor coefficients instead of a finite-difference
quartic target. The earlier fit's conditioning and extraction floor must be
handled explicitly. The formal potential only identifies a necessary target;
it does not replace this constrained field solve. Cubic defects likewise need
their own earlier-order repair. Regional compatibility and convergence remain
separate after any successful finite-order correction.

## Controls and reproduction

Run `python -B analysis/HC_Cartan_Low_Order_Exterior_Compatibility.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_low_order_exterior_compatibility`.
Tests check d-squared=0, integer homotopy identities across multiple degrees
and form orders, the exact projector dimension, closed and deliberately
nonclosed inputs, correction-order counting, fingerprints and radius scaling.
The JSON retains the formal potential and unaltered quartic curl coefficients.
The two radii are analyzed with two local workers. No new fit or publication
change is performed; floating residual diagnostics are not interval certificates
or a regional existence theorem.
