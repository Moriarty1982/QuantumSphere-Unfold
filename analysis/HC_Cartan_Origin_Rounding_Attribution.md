# Origin rounding attribution without a residual anchor

## Scope

This audit examines the failed raw origin check for the latest cubic-kernel
and quartic-refreshed candidate in the added neutral commuting-spinor odd-cross
Einstein-Cartan comparison. It changes no field coefficients, parent report,
main TeX/PDF or published payload. It is not a native HC/C7 identification.

Unlike the earlier anchored kernel-update control, the current C3 residual
is assembled directly from its source and principal terms. No previously
computed residual vector is added as an anchor. The important restriction is
that the nonlinear source terms are recomputed in binary64 and then frozen;
their own numerical error has not been eliminated or certified.

## Direct frozen-source assembly

The retained parent evaluator has the form

    C3 = S0 + S1 + P(A, p4),

where S0 is the lower-jet nonlinear source, S1 the highest coframe/multiplier
connection contribution, and P the symmetric fourth-spinor readout. Both
source arrays are evaluated afresh, and each stored binary64 value is then
interpreted as an exact rational. Their norms are about 1.04134e6 and
6.28811e5: the final small residual is produced by severe cancellation.

The exact readout A is independently reconstructed from the frozen origin
spinor, selector and weights, and compared with the kernel certificate.
The baseline p4 coordinates are likewise treated as their exact stored values.
The kernel update is reconstructed from its rational free/pivot parameters,
including the exact factorial/radius derivative conversion, before adding it
to the baseline. Direct exact contraction gives:

| Reassembled diagnostic | Norm |
|---|---:|
| Baseline C3 from freshly frozen sources | 4.77396e-10 |
| C3 including the exact parametric kernel update | 4.77396e-10 |
| Raw binary64 candidate C3 | 1.39723e-7 |

The baseline and updated C3 vectors are exactly equal as rational arrays, not
merely close in norm. This directly verifies preservation of the frozen source
residual without importing an old residual anchor. It does not show that this
residual is zero or that the frozen nonlinear sources are accurate to 1e-10.

The other 794 retained origin rows are bitwise unchanged by the fourth-spinor
update. Combining those unchanged binary64 rows with the directly reassembled
C3 gives a **hybrid frozen-source** 1114-row norm about 4.88828e-10, versus
1.39723e-7 in the raw candidate evaluation. This is not a fresh high-precision
nonlinear evaluation of all 1114 equations.

## Exact vector error decomposition

Four evaluations use the same frozen sources:

1. Exact readout and exact parametric p4.
2. Exact readout and the actually assembled rounded p4.
3. The stored binary64 readout and rounded p4, but exact rational arithmetic.
4. The actual binary64 parent result.

Successive differences separate input rounding, readout-matrix rounding and
floating arithmetic. Their vector sum equals the complete raw-minus-parametric
error exactly, row by row. The input contribution is further split between
rounding monomial coefficients and scaling/adding them into physical fourth
derivatives.

| Contribution | Vector norm |
|---|---:|
| Rounding of monomial coefficients | 5.56370e-8 |
| Physical fourth-derivative assembly | 8.14639e-8 |
| Combined input rounding | 1.00816e-7 |
| Readout-matrix rounding | exactly 0 for these inputs |
| Dot-product and summation arithmetic | 9.55093e-8 |
| Total raw-minus-parametric discrepancy | 1.39752e-7 |

These norms are **not additive**. Only the signed vectors add. The matrix
contribution is zero for this particular frozen readout; it is not assumed
zero in the attribution helper or claimed universally.

## Independent precision and negative controls

Two private mpmath contexts at 40 and 80 digits directly contract the total
principal terms and add the frozen sources. Both reproduce C3 norm
4.773958330761969853277e-10. Their parametric-minus-baseline discrepancies are
about 5.71e-33 and 3.96e-73 respectively, without forcing either update to zero.

Using the already rounded inputs instead reproduces about 1.00784e-7 at both
precisions. More working digits do not restore a relation lost from the
inputs. A deliberately nonkernel fourth-spinor perturbation changes C3 by
about 1.79702e-6, confirming that reassembly does not erase arbitrary changes.
Tests also alter a source entry and verify that the residual changes with it.

## What is resolved and what remains

The apparent 1e-7 growth relative to the frozen-source baseline is fully
attributed to representational and arithmetic effects in the principal
readout. The exact parametric kernel update does not cause such growth.
The remaining nonzero baseline cannot yet be assigned to mathematical
incompatibility or rounding in the nonlinear sources.

A stronger next check must evaluate those nonlinear source terms, and
eventually the other 794 equations, independently at higher precision while
retaining exact dependent coordinates. Replacing frozen binary64 values with
high-precision numbers after the fact is not that check. No interval bound,
exact origin closure, regional solution or convergence claim follows here.

## Reproduction

Run `python -B analysis/HC_Cartan_Origin_Rounding_Attribution.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_origin_rounding_attribution`.
The JSON includes source fingerprints, all exact rational attribution vectors,
both precision paths, negative controls and explicit proof boundaries. The
independent precision checks use two local workers with separate contexts.
