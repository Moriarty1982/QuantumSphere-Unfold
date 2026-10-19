# Quartic residual extension

## Scope

This audit continues the cubic spinor reprepare and stable retained-origin
evaluation for the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison. It is not a native HC/C7 identification or a regional PDE theorem.
The main TeX and PDF are unchanged.

## Shared correction and preserved orders

One shared polynomial adds homogeneous degree-six coframe, degree-five spinor
and degree-five multiplier corrections. With y = x/r and r = 1/16384, their
amplitudes are respectively r^2, r and r. There are 3584 real coefficients:
16 times 84 coframe coefficients and 40 times 56 spinor/multiplier coefficients.

The field equations use second coframe derivatives and first spinor/multiplier
derivatives. These additions therefore first affect their degree-four residual.
They leave the previously treated cubic coefficients and all retained origin
jet orders unchanged by degree. Higher derivatives at displaced points are
derived from the same polynomial, not fitted independently.

The inherited rational free/pivot representation remains authoritative for the
earlier fourth-spinor kernel update. This extension does not repair or suppress
the failed rounded-input origin recheck. Neighborhood calculations use rounded
approximations; the stable origin anchor is not a new full high-precision solve.

## Coefficient extraction and solve

For a directional residual f(t), use

    D4(h) = [f(2h) - 4f(h) + 6f(0) - 4f(-h) + f(-2h)] / (24 h^4).

This extracts the quartic coefficient exactly for polynomials through degree
five. Richardson combinations (4 D4(h/2) - D4(h))/3 cancel the leading degree-six
contamination. Coarse and fine estimates use h = 1, 1/2, 1/4. Extraction points
can reach 2r; old uniform radius estimates are not silently reused.

All 35 degree-four multiindices supply directional coefficient equations.
The augmented matrix has 3360 rows: 2800 residual rows and 560 rows preserving
16 selected normal coordinates. These are coordinate constraints, not a newly
established physical classification. The degree-four Vandermonde condition
estimate is about 329.

| Quantity | Numerical value |
| --- | ---: |
| Augmented matrix | 3360 by 3584 |
| Numerical rank | 2454 |
| Singular-value cutoff | 3.37e-8 |
| Smallest retained singular value | 1.88e-7 |
| First omitted singular value | 1.78e-13 |
| Retained condition estimate | 1.79e9 |
| Baseline quartic sample norm | 3.66e-7 |
| Coarse fitted remainder | 1.35e-12 |
| Extraction step-change norm | 4.42e-11 |
| Fine-estimate remainder of coarse fit | 4.42e-11 |
| Fixed-coordinate quartic drift | 7.64e-20 |

The fit reaches the observed extraction floor, not a certified exact zero.
Refitting the finer right-hand side with the same inverse changes the coefficient
vector by 1.20e-6 against norm 7.60e-5, about 1.6 percent. Its fitted remainder is
2.13e-11. The large retained condition estimate limits conclusions about precise
coefficients or uniqueness; numerical rank is not an exact-rank certificate.

## Actual-equation checks

At five additional directions, the script evaluates the actual modified fields
and all 80 lower/spatial residuals. Quartic-response prediction discrepancies
range from about 4e-13 to 6.4e-11, comparable to extraction uncertainty. Observed
changes in extracted cubic coefficients are at most 1.1e-11.

| Direction y | Residual at r y | At r y / 2 | At r y / 4 |
| --- | ---: | ---: | ---: |
| (1,0,0,0) | 9.61e-8 | 3.00e-9 | 9.38e-11 |
| (0,1,0,0) | 6.62e-8 | 2.07e-9 | 6.46e-11 |
| (0,0,1,0) | 6.57e-8 | 2.05e-9 | 6.41e-11 |
| (0.3,0.2,0.1,0.4) | 1.77e-9 | 5.54e-11 | 1.72e-12 |
| (0.2,-0.3,0.1,0.4) | 4.59e-9 | 1.44e-10 | 4.49e-12 |

The approximate factor 32 under radius halving is consistent with a leading
fifth-order residual at these samples. It is not a uniform remainder estimate.
The finer-fit field produces similar sampled residuals, generally within one
percent. The separately evaluated 272 first-prolongation rows remain nonzero,
with norms as large as about 0.0091. No exact field solution is obtained.

## Reproduction and remaining gap

Run `python -B analysis/HC_Cartan_Quartic_Residual_Extension.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_quartic_residual_extension`.
The adjacent JSON records source fingerprints, coefficients, both extraction
estimates, sensitivity checks and actual-equation witnesses. Independent sample
evaluations use two bounded local workers; matrix preparation uses the existing
numerical services and compact cached solve results.

Tests cover extraction, shared field/higher derivatives, order preservation,
saved-witness reproduction, sensitivity and explicit scope boundaries. Future
work must control conditioning and coefficient growth, refresh regularity bounds
for the changed polynomial and establish integrable regional closure. A finite
sequence of successful coefficient fits alone establishes neither convergence
nor regional existence. No interval or outward-rounded error certificate is
claimed.
