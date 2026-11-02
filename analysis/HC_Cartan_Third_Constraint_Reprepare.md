# Affine Re-preparation of the Third Constraint

Scope: the added neutral odd-cross Einstein-Cartan comparison only. The main
TeX paper, release, physical couplings, frame interpretation and scales do not
change. A finite jet is not an evolved solution or a local-existence theorem.

## What Changes

The frozen 394-completion had an unreachable third-constraint residual about
26799.511 even after fitting new psi4, E4 and lambda3. The appropriate repair
is not another freely appended derivative. Earlier higher data must change.

The stronger result here is that psi2 need NOT change for this particular gate.
With the lower point and psi2 fixed, C3 is affine in lambda2, E3, psi3, E4,
lambda3 and psi4. The terms quadratic in psi2 become a fixed source. All Q, M,
Einstein and vacuum coefficients are retained.

## Analytic Derivatives

The algebraic Cartan equation is differentiated three times with its nonzero
multiplier value intact. With H1=0 at this normal point:

    H k3 = -s3 + L3^T lambda0
            + sum_cyclic(L2^T lambda1 + L1^T lambda2)
            - H3 k0 - sum_cyclic(H2 k1),

when the new lambda3 is zero in the source. Its highest response is added
separately. The source includes the differentiated volume/inverse coframe,
the spinor bilinears and their cross terms. In particular, the E2/source1 and
E3/source0 contributions are not omitted.

For a Hermitian form B commuting with any inserted internal Q,

    d3(psi^dagger B psi) = 2 Re(psi^dagger B psi3)
                          + 2 Re sum_cyclic(psi1^dagger B psi2).

The LC contribution omega3 at E=I,E1=0,E4=0 is quadratic in E2 and independent
of E3. It follows directly by differentiating
`omega_mu = ETA (E Gamma_mu - E_,mu) inverse(E)`. The fourth metric derivative
contains all six products of two E2 factors; repeated indices retain their
multiplicity. The implementation includes the inverse-frame corrections.
An independent parallel derivation verified this formula with multivariate
Taylor multiplication/inversion, without using finite differences.

The third constraint then uses all eight product-rule terms in
`d3 Im(pair(psi,Dpsi,Q)) - E3`, with covariant derivatives through D3.
Its analytic source differs from the previous independent Richardson source
by about 0.00227544 in a norm about 260390.585, consistent with the recorded
finite-difference stability indicator. The new matrix uses the analytic source,
not the finite-difference values.

## The 45 Conditions Are Now Explicit

The fully symmetric spinor image is represented by 140 columns. Including the
880 new E4/lambda3 coordinates gives a 320-by-1020 image representation of
numerical rank 275. Its orthonormal left nullspace has 45 columns. Projecting
C3 onto that space eliminates ALL the new highest jets, not merely psi4.

Stacking the prior 394 equations with those 45 conditions produces an affine
439-by-960 system in changes of the earlier lambda2/E3/psi3 coordinates. Its
numerical rank is 232; the old-394 block has rank 187 on this restricted slice.
Thus the new conditions contribute all 45 additional ranks here. The matrix is
not said to have 439 independent equations. A random affine identity control
has residual about 7.12e-11.

After solving this system, E4/lambda3 and then psi4 are recovered, and every
component is re-evaluated without the projection:

| Check | Component norm |
| --- | ---: |
| Previous 394 equations | 1.412e-9 |
| All 714 packed components (394 plus 320 C3) | 1.449e-7 |
| Largest absolute component | 2.790e-8 |

The JSON retains the new earlier coordinates, all highest derivatives, the full
residuals, singular values and the original failed control. These are numerical
results, not exact symbolic certificates. The old 394-completion is not overwritten.

## Limits

This C3-only repair does NOT impose the full R2 or FE2 equations. Those must be
assembled jointly because they constrain the same multiplier and connection
derivatives. The companion `HC_Cartan_Next_Joint_Completion` follows that question
separately; a C3-only completion must not be mistaken for its result.

The earlier Taylor-neighborhood estimate must not be inherited unchanged: both
older higher data and new fourth/cubic coefficients have changed. No claim
about a spacetime neighborhood, constraint propagation, formal integrability,
native HC/C7 or a physical frame/scale is established here.

## Reproduction

```text
python -B analysis/HC_Cartan_Third_Constraint_Reprepare.py --output analysis/HC_Cartan_Third_Constraint_Reprepare.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_third_constraint_reprepare.py
```

Eleven focused checks cover derivative symmetries, multiplicities, source
agreement, the Cartan third equation, the cokernel, exact preservation of psi2,
the old failed control and recomputation of the full 714 components.
