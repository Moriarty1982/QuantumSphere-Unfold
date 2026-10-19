# Six sources from the first primary prolongation

## Scope

This calculation concerns only the added neutral commuting-spinor odd-cross
Einstein--Cartan comparison. It is a numerical finite-jet result, not native HC/C7
identification, a regional existence theorem, physical frame identification or
an interval certificate. Main TeX/PDF and published payload are unchanged.

## Structural reduction

Let the primary 68 equations be

\[
 F_0=(C,\operatorname{Re}R,\operatorname{Im}R,F_E,J_{0i}),
 \qquad J_{0i,a}=\partial_0 C_{ai}-\partial_i C_{a0}.
\]

Their first prolongation consists of 272 rows, ordered by derivative direction:

\[
 \partial_r F_0=(C_{,r},\operatorname{Re}R_{,r},
 \operatorname{Im}R_{,r},F_{E,r},
 C_{,r0,ai}-C_{,ri,a0}),\qquad r=0,1,2,3.
\]

These are a constant linear extraction from the existing 384 C1/R1/FE1/C2
rows. Symmetry cancels the third spinor derivatives in the differentiated curl;
the numerical norm of their entire response is 1.95e-13. A separate central
difference check of the general-coframe primary equations verifies this extraction.

Keep the same six lower source coordinates q and the same lower background.
Divide higher increments into normal unknowns z_N and prescribed data z_T.
There are 224 normal unknowns: 96 psi2, 64 lambda2 and 64 E3 coordinates.
The inherited joint affinity gives

\[
 0=b+Bq+A_Nz_N+A_Tz_T.
\]

If L has orthonormal columns spanning the full left kernel of A_N, solvability
requires

\[
 Gq=-L^\top(b+A_Tz_T),\qquad G=L^\top B.
\]

At the prepared point, A_N has numerical rank 160, leaving 112 left directions.
The source gate G has rank six, with singular values approximately

\[
 (1.98065,1.27943,0.50328,0.48935,0.27270,0.13460).
\]

Consequently, for compatible prescribed data the source is uniquely determined by

\[
 q=-G^+L^\top(b+A_Tz_T).
\]

Uniqueness is conditional: the other projected compatibility conditions must
also vanish. Arbitrary prescribed data need not admit a source or normal lift.
The left kernel must be computed with a full left singular basis: A_N is tall,
and an economy-only basis would omit 48 left directions.

## Numerical controls

- Compatible candidate: all 272 residuals have norm 1.61e-11.
- Recovered q differs from (0.01,-0.005,0.003,0.002,0.004,-0.001) by 2.82e-12.
- Projected compatibility remainder: 4.23e-12.
- Direct joint-affinity checks: at most 2.72e-11.
- Using only the 68 time-derivative rows gives source-gate rank zero after
  eliminating normal higher unknowns. Spatial derivative conditions are essential
  to this identification; time-only evolution does not determine q at this order.

The computation reuses the fingerprinted matrix cache and does not refit or
replace the compatible 1114-row candidate. Reconstructing a solution of this
smaller system alone would not ensure the other higher equations.

## Relation to the six remaining mixed gates

The six source coordinates belong to the right kernel of the primary normal
matrix. The six extra mixed compatibility gates belong to its left kernel.
Equal dimensions do not identify these spaces. This result determines the former
through the entire first prolongation, rather than claiming a direct six-by-six
inverse between those two objects.

The next task is to transport the source rule to a general-coframe neighborhood,
keep its remaining compatibility conditions, and test whether differentiated
constraints close without external forcing. This pointwise calculation does not
remove the nonzero forcing seen in the previous Taylor-field diagnostic.

## Reproduce

Run `python -B analysis/HC_Cartan_First_Compatibility_Source_Gate.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_first_compatibility_source_gate`.
The adjacent JSON records input fingerprints and numerical results.
