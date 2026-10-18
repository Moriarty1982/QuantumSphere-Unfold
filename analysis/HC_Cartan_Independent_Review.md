# Independent Review of the Regular Cartan Jet Calculations

Date: 2026-10-18. Scope: independent critical review, not another continuation calculation. All statements below concern only the **explicitly added neutral odd-cross Einstein-Cartan comparison with commuting spinors**, fixed M and Q, c=1 and u=0. Neither a numerical point jet nor this review establishes a Cauchy solution, native HC physics or a physical scale.

Reviewed sources: `analysis/HC_Cartan_Regular_Gravity.py`, `analysis/HC_Cartan_Regular_Gravity.md`, `analysis/HC_Cartan_Spatial_Propagation.py`, `analysis/HC_Cartan_Spatial_Propagation.md`, `analysis/HC_Cartan_Cauchy_Rank.py` and `analysis/HC_Cartan_Cauchy_Rank.md`, against `analysis/HC_Cross_Cartan_Parent.py`. File/line references below are within `analysis/` and refer to the inspected workspace state.

## Findings, by Severity

**No blocking mathematical or implementation error found in the reviewed scope.** In particular, the checks below did not reveal a wrong Lorentz/coordinate sign, a missing nonzero-multiplier reaction, or an invalid identification of the ten exhibited leading directions as gauge. This is a targeted review, not an exhaustive proof or an interval certificate.

The following are limitations and validation gaps, not demonstrated defects requiring a change to the shared calculation:

1. **Important scope boundary: metric curvature is not Cartan curvature.** `HC_Cartan_Regular_Gravity.py:202` constructs the Levi-Civita bundle of the bilinear coframe from C, dC and d2C; `HC_Cartan_Regular_Gravity.py:207` compares it with the independent E metric's Levi-Civita curvature. The statement at `HC_Cartan_Regular_Gravity.md:110` is correct as written, but must not be expanded into equality with the independent, sourced Lorentz-connection curvature. At the saved regular jet, the torsion component norm is approximately 15.9904531, the upper-index curvature difference `R(omega)-R(omega_LC(E))` has component norm approximately 28.0271904, and their scalar contractions are approximately 15.5046397 versus 1.82288570. These Euclidean component norms are chart-dependent diagnostics, not invariant physical scales. No fix to the current metric-curvature statement is needed; retain this distinction in later integration or summaries.

2. **Residuals computed from a solved algebraic equation are not independent action checks.** `HC_Cartan_Spatial_Propagation.py:269` solves Hk=-s+L^T lambda; the reported `Cartan` residual at `HC_Cartan_Spatial_Propagation.py:285` reuses exactly that H, s and L. Its small value verifies the linear solve, not the correctness of the parent variation by itself. Likewise, equality of the two metric curvatures follows necessarily once their coframes agree through second order; it is not an additional dynamical prediction independent of F=dF=d2F=0. The direct-parent and raw-map checks below provide separate support, and the present notes already limit the curvature claim to a point. Future tests should preserve that separation rather than counting these reconstructed quantities as new independent field equations.

3. **The six-dimensional normal quotient is conditional, not a physical degree count.** `HC_Cartan_Regular_Gravity.py:124` and `HC_Cartan_Regular_Gravity.py:244` exhibit ten independent leading normal gauge vectors inside the particular normal kernel. `HC_Cartan_Regular_Gravity.md:123` appropriately does not classify the remaining six as physical or necessarily nongauge. The vectors do not, by themselves, give a gauge fixing, a reduced principal symbol, or propagation of every constraint. The complete gauge-induced higher changes were independently checked below. Maintain this qualification when advancing the hierarchy.

## Action and Variation Checks

The reference was the actual real density in `HC_Cross_Cartan_Parent.py:152`, its independent coframe Euler expression at `HC_Cross_Cartan_Parent.py:159`, the original spin maps at `HC_Cross_Cartan_Parent.py:93`, and the kinetic weights at `HC_Cross_Cartan_Parent.py:136`. The existing test count was not used as mathematical evidence.

### Nonzero-Multiplier Connection Reaction

At the declared normal point, dE=0 implies H_,r=0, but not H_,rs=0. Differentiating the actual eliminated connection equation gives

```text
H k_,rs = -s_,rs + L_,rs^T lambda
          + L_,r^T lambda_,s + L_,s^T lambda_,r
          + L^T lambda_,rs - H_,rs k.
```

All these terms are retained in `HC_Cartan_Regular_Gravity.py:48` through `HC_Cartan_Regular_Gravity.py:64`. The first derivative retains L_,r^T lambda in `HC_Cartan_Spatial_Propagation.py:40` through `HC_Cartan_Spatial_Propagation.py:45`, and in `HC_Cartan_Cauchy_Rank.py:88` through `HC_Cartan_Cauchy_Rank.py:93`. The first probe derivative also retains the multiplier-dependent weight, its first/second derivatives and the connection-adjoint terms in `HC_Cartan_Spatial_Propagation.py:169` through `HC_Cartan_Spatial_Propagation.py:184`.

A directional second-connection difference was rebuilt using **the original** `spin_maps`, `contorsion_hessian` and LC `bundle`, not the optimized `fast_cartan_data`, `source_forms` or the analytic connection-jet routine. For unrelated random higher jets, seed 74025, and direction proportional to (.4,-.2,.7,.3), its errors against the analytic second derivative were:

| Difference step | Component-norm error |
| --- | --- |
| 4e-4 | 7.34e-6 |
| 2e-4 | 1.83e-6 |
| 1e-4 | 6.64e-7 |

The first halving shows the expected central-difference behavior; the smallest step starts to encounter roundoff. This supports the implemented nonzero-lambda formula and its index ordering, but is not an all-directions exact proof.

### Direct Local Lorentz and Coordinate Covariance

An unrelated off-shell field value was generated with seed 74023: generic E near I, generic complex Psi/dPsi, generic connection/curvature and a nonzero multiplier with all columns present. The direct density was used with c=.7 and u=.09 solely as an independent off-shell covariance check; the saved comparison data and their c=1/u=0 values were not changed.

For J^T eta+eta J=0, the checked infinitesimal transformations were

```text
delta E = J E,       delta Psi = S_J Psi,
delta d_mu Psi = S_J d_mu Psi + (d_mu S_J) Psi,
delta lambda = -J^T lambda,
delta omega_mu = eta J eta omega_mu - omega_mu J - eta d_mu J,
delta R_mu,nu = J R_mu,nu + R_mu,nu J^T,
S_J = -(eta J)_ab Gamma^a Gamma^b / 4.
```

Both J and its four first derivatives were nonzero. The centered directional derivative of the **direct parent density** under this local transformation was approximately 3.84e-7, 3.73e-9 and 2.66e-9 at steps 1e-4, 1e-5 and 1e-6. No fitted solution or Noether-row helper entered that check.

A separate variation of E at fixed independent omega and curvature gave errors approximately 2.73e-7, 2.76e-9 and 4.47e-10 against the direct coframe Euler formula. Thus the reference is the independent parent variation, not a silent LC-restricted variation.

For an infinitesimal coordinate Jacobian f^nu_mu, the transformations E -> E+E f and

```text
delta lambda = (tr f) lambda - lambda f^T
```

together with the covector/two-form transformations of dPsi, omega and R gave the expected scalar-density derivative `(tr f) L`. The difference from this prediction was approximately 4.65e-10, 1.99e-10 and -6.75e-11 at the same steps. This independently supports the vector-density convention required by the four coordinate rows.

## The 24 Lorentz and Four Coordinate Relations

With the independent Cartan equation eliminated, the undifferentiated Lorentz identity is

```text
FE:(J E) + 2 Re[(S_J Psi)^dagger R] + F:(J^T lambda) = 0,
F = C-E,   F_lambda = -F.
```

At E=I, dE=0 and F=R=FE=0, differentiating it leaves exactly the signed relation in `HC_Cartan_Regular_Gravity.md:76` and the 24 rows assembled at `HC_Cartan_Regular_Gravity.py:151`. Terms differentiating its coefficients vanish because their accompanying point Euler expressions vanish. This is a conditional on-shell first-derivative identity, not a general off-shell identity containing only the displayed differentiated terms.

For diffeomorphisms, the coefficient of d_mu xi^nu is

```text
I^mu_nu = FE_a^mu E^a_nu
          - F_lambda^a_nu lambda_a^mu
          + delta^mu_nu (F_lambda:lambda).
```

At the same on-shell normal point, its divergence yields

```text
sum_mu d_mu FE_nu^mu
  + sum_a,mu lambda_a^mu (d_mu F^a_nu - d_nu F^a_mu) = 0.
```

This agrees with `HC_Cartan_Regular_Gravity.md:86` and `HC_Cartan_Regular_Gravity.py:158`. Dropping the multiplier-curl term on arbitrary lower data would be wrong. Its disappearance at the prepared point is justified by the separately prepared curl condition. It is not a torsion-free Bianchi assumption.

Using unrelated random higher coordinates, seed 74024, without refitting them, the component norms of the three row blocks applied to the full equation vector were:

| Relation block | Rows / evaluated rank | Residual norm |
| --- | --- | --- |
| First-constraint curls | 24 / 24 | 3.27e-14 |
| Differentiated Lorentz identity | 24 / 24 | 9.28e-14 |
| Coordinate identity | 4 / 4 | 5.04e-14 |
| Combined | 52 / 52 | All three blocks above |

These checks do not independently certify the full 384-by-1200 rank or prove constant rank on a neighborhood. The 24 curl rows use the prepared lower G=0 and are compatibility relations at this point, not 24 further off-shell Noether symmetries.

## Complete Gauge-Jet Check

The ten normal vectors in `HC_Cartan_Regular_Gravity.py:124` have only an E_,00 component because the normal unknown vector does not contain Psi2/lambda2/Psi3. The omitted components are nevertheless essential to the corresponding full transformations.

For a local Lorentz parameter J t^2/2, the full retained jet changes include

```text
delta E_,00 = J,
delta Psi_,00 = S_J Psi,
delta lambda_,00 = -J^T lambda,
delta Psi_,rst = delta_r0 delta_s0 S_J Psi_,t
               + delta_r0 delta_t0 S_J Psi_,s
               + delta_s0 delta_t0 S_J Psi_,r.
```

For xi^a=v^a t^3/6, with f^nu_mu=v^nu delta_mu0, they include

```text
delta E^a_0,00 = v^a,
delta Psi_,000 = v^r Psi_,r,
delta lambda_,00 = v^0 lambda - lambda f^T.
```

The saved regular higher jet was transformed using these full changes, without re-solving any equation or modifying M, Q or the lower field values. The change of the complete retained 384-component equation vector was approximately 1.59e-12 for a random Lorentz generator and 1.74e-12 for a random coordinate generator. This supports the claimed ten leading gauge directions more directly than normal-matrix annihilation alone. It does not classify the other six normal directions or supply a full gauge reduction.

## Remaining Checks and Interpretation

- The exact temporal Pfaffian formula in `HC_Cartan_Cauchy_Rank.py:71` was checked on 20 unrelated complex spinors and positive temporal multiplier columns, seed 74025; maximum absolute discrepancy from the direct Hermitian-inverse formula was 5.55e-16. This is a pointwise probe-block check, not a gravitational evolution result.
- The first-constraint principal-map argument at `HC_Cartan_Spatial_Propagation.md:67` correctly assumes surjectivity of its four real functionals. Cancellation of symmetric second spinor derivatives yields exactly the 24 curl obstructions with the remaining lower data frozen. That sufficiency concerns only dF, not the full field equations.
- Direct finite differences and action covariance reduce circular-validation risk, but share gamma conventions and lower source data with the implementation. An independent symbolic derivation or separate implementation would strengthen the audit further.
- No independent exact/interval rank certificate, constant-rank neighborhood, surface-data construction, full constraint propagation, convergence, or native action identification was established. No physical interpretation of the remaining kernel was inferred.
- No source correction is proposed on the evidence found. Preserve the current limits in later write-ups. The focused follow-up below now retains complete gauge-transformation/direct-action regression tests; leading-vector tests alone do not exercise every necessary companion jet.

## Reproducible Focused Tests

The follow-up stores eight tests in `scripts/qsc_audit/tests/test_hc_cartan_independent_covariance.py`. Setup reads the saved regular JSON coordinates and evaluates them directly. It does **not** construct the 1200-column higher-jet coefficient matrix or call the continuation solver. All changed jets are private copies; the saved point, M, Q, c=1 and u=0 are preserved. Generic off-shell density variations use c=.7/u=.09 only in their unrelated covariance fixture, as in the initial review.

The eight tests retain:

1. Direct parent local Lorentz covariance with nonzero parameter derivatives, and an omission control for the derivative contribution to dPsi.
2. Direct parent coordinate density covariance, and an omission control for the multiplier's density weight.
3. Direct independent-coframe variation at fixed connection and curvature, including central-difference convergence.
4. Complete Lorentz companion jets for all six elementary generators, with a failed leading-E-only control.
5. Complete coordinate companion jets for all four elementary directions, with a failed leading-E-only control.
6. A second-connection difference built from raw parent `spin_maps`, `contorsion_hessian` and the LC bundle, bypassing the optimized Cartan maps.
7. Pointwise bilinear/E metric-curvature agreement together with demonstrably nonzero torsion and different Cartan curvature/scalar; no identification of the two connections.
8. All 52 conditional relations on three unfitted random higher jets, independently contracted in tensor form and compared with the row-matrix implementation. The evaluated 24/24/4 block ranks and combined rank 52 are retained, without a full equation-matrix rank solve.

Reproduction:

```text
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_independent_covariance.py -v
```

Result on 2026-10-18: **8 tests passed**, reported test time approximately 1.93 seconds. No global suite was run. These regressions preserve the review's conditional scope; they are not an exact rank certificate, Cauchy/existence result, or native-physics validation.

## Execution and Changed Paths

Read-only source inspection used `rg` and PowerShell file reads. Three targeted numerical batches ran with `python -B -c`, using seeds 74023, 74024 and 74025. They covered direct action variations/covariance, all 52 conditional row relations on arbitrary higher jets, complete Lorentz/coordinate jet transformations, raw-parent connection second differences, the generic temporal Pfaffian, and the distinction between Cartan and metric curvature. No full test suite or continuation solver was rerun.

The initial review created only `analysis/HC_Cartan_Independent_Review.md`. Its narrowly scoped follow-up added `scripts/qsc_audit/tests/test_hc_cartan_independent_covariance.py` and updated this note. No shared calculation, saved input, coupling, existing test module, main TeX/PDF, release file or package environment was changed. No Git index/history operation, commit, push or message to another chat was performed.
