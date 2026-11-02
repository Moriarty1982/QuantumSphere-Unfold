# Scalar chart integrated inside the full OP5 comparison

30 October 2026. Bounded point0 tests at field-jet orders4 and5. This is a full-field finite-jet fit with an exact scalar coordinate prescription, not postprocessing and not a proof of an all-order full-field construction.

## State map and derivative propagation

scalar_chart_model.py exposes ChartModel. Its inputs are23 real nonpivot Taylor functions per multiindex. Their coefficients are actual derivatives divided by the multiindex factorial. The pivot real A0 coefficient series is constructed as the positive square root of target8/h minus the signed nonpivot quadratic form. The target uses the original exact local h branch through the requested field-jet order, constructed at70-digit precision and converted to float64 for the field fit.

The Torch recurrence runs inside the residual evaluation and is differentiable with respect to all nonpivot coefficients. The reconstructed full24-real coefficient series is converted to twelve complex spinor coefficients before the existing full TaylorModel evaluates covariant derivatives, coframe, inverse coframe, kinetic operator and mass term. Thus derivatives of the pivot, including its explicit h/background dependence, enter the same equations. No background, coupling or spin connection is altered.

Nonpivot value and first derivatives are held exactly fixed to fifth-window-result.json. The pivot value and first derivatives are recomputed by the scalar chart; their changes relative to the saved germ are4.44e-16 and1.24e-14 in coefficient norm. This is explicitly not a claim that every low coefficient is bitwise unchanged. The scalar correction is within the prior floating residual scale.

## Reduced highest operator

At fixed central state, the chart tangent M from23 nonpivot real components to24 full components has identity rows at the nonpivot coordinates and pivot row

M_(pivot,i)=-D_i u_i/u_pivot.

For highest Taylor coefficients, every nonlinear square-root term involving two nonconstant coefficients has lower degree. Consequently the coefficient of each highest nonpivot variable is this same central M, with all target/highest background terms retained in the source. The reduced operator is A_reduced=A_full blockdiag(M), using the full nonlinear first-order principal matrix that includes coframe feedback.

The full nonpivot highest derivatives are eliminated through the complete reduced left kernel, lower nonpivot degrees2..order-1 are fitted jointly with all retained full residual blocks, and the highest nonpivot derivatives are recovered. The full24-component residual and scalar series are recomputed after recovery. The scalar map is never applied as a separate post-fit modification.

## Executed bounded results

Commands: `python scalar_chart_fit.py --order 4 --point 0 --maxsteps 10` and `python scalar_chart_fit.py --order 5 --point 0 --maxsteps 15`.

Both use the same fifth-window seed independently. The fifth-order test is NOT a strict prolongation of the separately returned fourth-order candidate. No untested points or higher orders are included.

| test | reduced highest matrix | rank at1e-8/1e-9/1e-11 | final projected objective | max sampled top-column error |
|---|---|---:|---:|---:|
| order4 | 480x805 | 424 at all cutoffs | 3.90e-13 | 4.29e-14 |
| order5 | 840x1288 | 735 at all cutoffs | 2.62e-12 | 2.94e-13 |

The highest-operator column check perturbs four selected highest nonpivot variables and re-evaluates the fully reconstructed chart residual. It corroborates the central-tangent construction in those columns, not exhaustively for all possible inputs. The scalar map and source convention are also derived above.

Actual derivative norms of the full residual F:

| derivative degree | order4 test | order5 test |
|---|---:|---:|
| 0 | 3.70e-14 | 3.70e-14 |
| 1 | 7.58e-14 | 4.27e-13 |
| 2 | 2.45e-13 | 7.56e-13 |
| 3 | 6.03e-12 | 2.85e-12 |
| 4 | not tested | 2.06e-10 |

Actual derivative norms of scalar g:

| derivative degree | order4 test | order5 test |
|---|---:|---:|
| 0 | 0 in float evaluation | 0 in float evaluation |
| 1 | 4.48e-16 | 4.48e-16 |
| 2 | 6.03e-15 | 5.76e-15 |
| 3 | 2.38e-14 | 2.02e-14 |
| 4 | 1.71e-13 | 2.79e-13 |
| 5 | not tested | 4.03e-12 |

The order4 projected objective needed one lower correction of norm2.30e-9; order5 needed one of norm9.39e-9. The seed had already satisfied scalar derivatives through degree4, so the fourth test mainly checks implementation consistency. At fifth order the scalar g-degree5 condition was not previously imposed. The large postnormalization failure can be repaired by recovering all highest nonpivot derivatives jointly in the chart: only the pivot was changed in the earlier failed postprocessing test, whereas the integrated fit allows its required companion highest changes.

## Guard, geometry and norm cost

Both central charts have pivot1.8321702629071053, radicand3.356847872281091, coframe determinant13.63456067914196 and inverse metric g00=-0.468002000654795. These are pointwise guards only. No uniform neighborhood regularity or hyperbolicity estimate is established.

The order5 full fifth-derivative norm is31064.20, higher than the original window's19526.87. Recovering minimum-norm nonpivot coefficients does not minimize the norm of the full24 reconstructed components. Therefore the norm increase is an explicit cost of this chosen coordinate/solver solution, not evidence of an unavoidable physical scale or divergence. The order5 lower full jet norms are approximately25.94,141.14,1205.49 at degrees2,3,4. The reconstruction does not establish coefficient stabilization or a compatible infinite sequence.

## Scope and reproducibility

scalar_chart_fit_order4_point0.json and scalar_chart_fit_order5_point0.json record inputs, hashes, unchanged-input checks, software, singular values, cutoff tests, fit history, full coefficients and scalar/full residual norms. Inputs remained unchanged in both runs. No source-of-truth repository files or old results were modified. No model physics assumptions were changed.

The scalar equation is structurally built in to all retained orders, but the reported full-field zeros are finite float64 approximations. This demonstrates that integrating the scalar chart is compatible with a bounded full-field fit at the tested point and orders, unlike scalar-only postprocessing. It does not prove native action identification, global chart validity, all-order formal compatibility, analytic convergence, regional existence, a common solution through other points or OP5 closure.
