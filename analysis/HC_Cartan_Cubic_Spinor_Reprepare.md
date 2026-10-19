# Cubic spinor reprepare and exact retained-origin representation

## What changes

The preceding frozen-spinor control leaves a cubic remainder about 2.97e-7 even
when the normal coordinate corrections are free. This stage permits a degree-four
spinor correction, while restricting it to preserve the already imposed origin
equations. Coframe degree-five and multiplier degree-four corrections remain
available. The selected normal coordinate corrections are kept zero at cubic
order, across the full homogeneous polynomial rather than just at a few nodes.

The former fourth spinor derivative values themselves are not retained. Their
contribution to the inherited equations is what is preserved. No earlier report
is overwritten. Main TeX/PDF and published payload remain unchanged. The model
is only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison.

## Structural kernel

Write a degree-four correction as

\[
 \delta\psi=r\sum_{|\alpha|=4}p_\alpha (x/r)^\alpha,
 \qquad p_\alpha\in\mathbb R^{24}.
\]

At the origin define the real readout map A of size 4-by-24 by

\[
 (A u)_a=\operatorname{Im}\sum_{v,i}
 \overline{\psi_{0,v i}}\bigl[(Q u)W_a^\top\bigr]_{v i}.
\]

Here u is interpreted as a complex 3-by-4 spinor, with all 12 real components
followed by all 12 imaginary components. The frozen map has exact rational rank
four. Requiring A p_alpha=0 for every degree-four monomial leaves 20 free real
components per monomial, or 700 in total.

This condition makes the leading constitutive readout variation vanish as a
polynomial. In particular,

\[
 \delta C_{,rst,a\mu}(0)=A_a\,
 \delta\psi_{,rst\mu}(0)=0.
\]

Only these C3 rows of the retained 1114-vector depend on the fourth spinor jet;
the highest-response matrix has exactly zero fourth-spinor columns in all other
rows. Its C3 symbol agrees with the readout construction. E5 and lambda4 do not
change the retained lower coframe/multiplier derivatives. Thus this kernel
preserves the retained residual expressions, not a claim that the old residuals
were exact zeros or that every old highest derivative value was preserved.

## Coupled cubic calculation

The 1456 coframe/multiplier coefficients and 700 retained-kernel spinor coordinates
are solved together. The coupled matrix has numerical rank 1296. Its cubic
remainder is about 5.82e-12 on the coarser estimate, and 7.92e-11 on the finer
estimate, compared with baseline estimate variation 8.13e-11. This supports
cancellation to the observed extraction floor, not an exact proof that every
cubic residual coefficient vanishes.

Independent cubic checks include two axis and two mixed-sign/mixed-component
directions. Their discrepancies from the response prediction are below 2e-12.
Selected normal coordinate cubic drift is about 7.1e-20.

## The numerical preservation warning

The fourth spinor coordinate change has norm about 7.48e8 in the present jet
coordinates. This is not a physical energy or a dimensionless perturbation bound.
It creates a serious precision issue in direct binary64 evaluation:

- inherited origin 1114 norm: 4.87e-10;
- rounded new origin 1114 norm: 1.28e-7;
- direct rounded recheck therefore fails a 1e-8 threshold.

Two floating correction steps alone do not restore the old evaluation accuracy.
This failure is retained in the JSON and tests. Passing the regression suite
does not mean the rounded new origin evaluator passed that threshold.

To retain the constraint exactly, the authoritative update is stored parametrically.
Treat the frozen binary64 psi, selector and weights as exact rational numbers.
Choose four independent columns of A as dependent pivots and store the other
20 components as rational free parameters. The dependent values are

\[
 p_{\mathrm{pivot}}=-A_{\mathrm{pivot}}^{-1}
 A_{\mathrm{free}}p_{\mathrm{free}}.
\]

The report stores A, the rational pivot map and all 35 sets of free parameters.
Exact arithmetic verifies all 35 products A p_alpha are zero. This is an exact
certificate for the retained-update kernel under the stated frozen-input
interpretation, not an exact certificate for the cubic PDE fit or the whole
physical model.

The rounded coefficient vector is a convenience for neighborhood diagnostics;
it is not interchangeable with the exact parametric representation for the
retained-origin claim. A higher-precision implementation should reconstruct
dependent pivots from the rational data rather than promoting rounded pivot
values to exact inputs.

## Radial checks

Actual lower-equation norms of the shared corrected polynomial are:

| Direction | at r | at r/2 | at r/4 |
| --- | ---: | ---: | ---: |
| (1,0,0,0) | 1.99e-7 | 1.24e-8 | 7.78e-10 |
| (0,1,0,0) | 7.54e-8 | 4.72e-9 | 2.95e-10 |
| (0.3,0.2,0.1,0.4) | 5.77e-9 | 3.61e-10 | 2.25e-11 |
| (0.2,-0.3,0.1,0.4) | 8.49e-9 | 5.31e-10 | 3.32e-11 |

Halving the coordinate scale reduces these errors by approximately 16, consistent
with a next quartic residual rather than the prior cubic behavior. These sampled
ratios are not a uniform remainder bound or a regional existence theorem.

## Remaining work

The next order requires its own coupled compatibility calculation. The changed
fourth spinor jet also requires fresh regularity/majorant estimates; old bounds
must not be carried over unchanged. Stable exact/high-precision evaluation of
the retained-origin representation remains distinct from the binary64 controls.
No all-order extension, regional constraint propagation, native HC/C7 identification
or physical source classification has been established.

## Reproduce

Run `python -B analysis/HC_Cartan_Cubic_Spinor_Reprepare.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_cubic_spinor_reprepare`.
NumPy and SymPy versions are recorded. The adjacent JSON stores numeric polynomial
coefficients, the exact rational kernel certificate, the failed rounded origin
recheck, and independent radial controls. Earlier frozen-data failures remain
available in the separate cubic gate report.
