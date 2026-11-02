# Fresh high-precision nonlinear C3 source evaluation

## Scope and input contract

This audit recomputes the nonlinear sources of the 320 third constitutive
derivatives in the added neutral commuting-spinor odd-cross Einstein-Cartan
comparison. It does not refit any coefficient, replace historical reports,
change the main TeX/PDF or identify native HC/C7 physics.

The lower fitted field jets are interpreted as their actual stored binary64
values. This defines the numerical point being tested; it does not create more
accurate fitted input coordinates. The updated fourth-spinor kernel parameters
are instead reconstructed from their authoritative rational free/pivot form
before arithmetic. No rounded dependent pivots are promoted to exact inputs.

The preceding rounding-attribution audit promoted already evaluated binary64
nonlinear sources to rationals. Here those source values are not used in the
high-precision calculation. They are retained only as comparison controls.

## Independent series method

Each worker owns a private mpmath context at 40 or 80 decimal digits. Degree-three
matrix series represent the original point fields along x=t y. Matrix products,
inverses and determinant coefficients are computed before rounding. Inverses
use the coefficient recurrence of E(t) A(t)=I; determinant coefficients use
d(det E)/dt=(det E) trace(E^-1 E').

The Levi-Civita connection is reconstructed from the metric and Christoffel
formula. The Cartan correction uses the previously verified coframe/source
factorization and exact flat Hessian inverse. Spin lifting and the full
constitutive expression

    C_a,mu = Im[psi^dagger Q W_a D_mu psi] - E_a,mu

are then evaluated by matrix-series arithmetic. No third-derivative source
formula from the historical evaluator is reused, and no finite differences
or small-step cancellation are used to extract the derivatives.

The 20 integer cubic multiindices supply univariate directions. Their
degree-three coefficient evaluation matrix is inverted rationally and checked
against the identity. Interpolation recovers all multivariate coefficients;
factorials convert them to the parent's unique symmetric derivative packing.
This reconstruction is exact as a coefficient map, not an interval certificate
for the floating high-precision matrix arithmetic around it.

Two source families are evaluated separately: the full lower-jet nonlinear
source S0 with the new highest jets zero, and the leading highest
coframe/multiplier contribution S1 with lower factors at the frozen origin.
The original fourth-spinor principal contribution and the exact kernel update
are added afterward. An extra direction (1,-1,2,0), outside the reconstruction
nodes, checks this split against the unsplit full field-series expression.

## Fresh results

Both 40- and 80-digit calculations give

    ||C3|| = 4.12772957146786736026198e-10.

This is the norm of the unscaled third coordinate derivatives in unique-triple
packing. It is not directly comparable to the earlier radius-scaled cubic
Taylor coefficient norms. Those earlier neighborhood diagnostics also used
the rounded polynomial representative, whereas the principal origin term here
uses the exact kernel parameters.

The freshly computed source vector differs from the previously frozen
binary64 source vector by about 4.00883e-10. The former reassembled norm
4.77396e-10 was therefore not an accuracy certificate for those nonlinear
sources. Norm differences are not additive error components.

| Control | 40 digits | 80 digits |
|---|---:|---:|
| Fresh C3 norm | 4.12773e-10 | 4.12773e-10 |
| Parametric-minus-baseline principal update norm | 5.70610e-33 | 3.96244e-73 |
| Held-out full-series split discrepancy | 1.33915e-32 | 1.71865e-72 |
| Fresh sources with already rounded p4 inputs | 1.00802e-7 | 1.00802e-7 |

The saved C3 vectors at the two precisions differ by about 5.70715e-33.
The separately serialized large source vectors differ at about 1e-29, partly
because their decimal output is deliberately truncated. Both precision paths
recompute all nonlinear products from the input jets, not from saved sources.
The constant constitutive residual is approximately 6.06672e-15, also nonzero.

## What a fourth-spinor-only repair can and cannot do

The exact frozen 4-by-24 spinor readout has rank four. Its fully symmetric
fourth-jet image occupies 35 quartets times four readout components, or 140
directions among the 320 C3 rows. The remaining 180 directions are fixed
compatibility conditions when all other jets are held fixed.

Averaging rows associated with the same quartet is the orthogonal image
projector in the unweighted unique-triple coordinate norm. The fresh C3
vector splits into:

| Conditional component | Norm |
|---|---:|
| Image accessible if all fourth-spinor coordinates were freed | 2.71566e-10 |
| Complement unchanged by fourth-spinor-only changes | 3.10859e-10 |

The squared norms add to the full squared norm up to approximately 1.24e-60
at 40 digits and 2.29e-100 at 80 digits. This projection is diagnostic only:
no previously fixed kernel constraints or field data have been released.
Even unrestricted fourth-spinor freedom would not remove the complement for
these fixed other inputs; the allowed kernel-only updates cannot alter C3
at all at the origin.

## Interpretation and next gap

The former 1e-7 increase was attributable to rounded principal inputs and
arithmetic. But a nonzero C3 residual near 4.13e-10 remains when the nonlinear
sources themselves are independently recomputed at higher precision. For
the stored numerical point, it is not eliminated by merely improving the
last dot product. It may reflect approximate fitted coordinates and does
not establish a structural obstruction for the full nonlinear model.

A further correction must examine the coupled finite-jet system under its
actual allowed-coordinate and prescribed-data restrictions. Changing higher
coframe or multiplier jets also affects R2 and FE2; a C3-only fit is not a
completion of the retained equations. The other 794 origin equations have
not been independently recomputed at high precision in this audit.

No interval-certified error bound, exact zero, high-precision solve of all
1114 equations, regional compatibility or convergent PDE solution is claimed.

## Reproduction and tests

Run `python -B analysis/HC_Cartan_High_Precision_C3_Source.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_high_precision_c3_source`.
The JSON stores all source and residual vectors at both precisions, exact
input provenance, projection diagnostics and the rounded-input negative
control. Tests cover exact input conversion, reshape integrity, matrix-series
inverse/determinant recurrences, exact reconstruction, projector controls,
the independent origin value and all 320 parent source components at binary64
comparison accuracy. Independent precision runs use two local workers and
separate arithmetic contexts; no global precision is changed.
