# Exact local scalar parametrization and all-order scope

30 October 2026. Route B: solve one scalar compatibility identity by a state-coordinate chart. This is not a native action, a new physical hypothesis, a gauge symmetry, or a solution of the remaining OP5 field equations.

## Exact chart

Write the twelve complex spinor components as 24 real components u=(Re psi, Im psi). With Zbeta=diag(1,-1,0) tensor beta, beta=diag(1,1,-1,-1), the real diagonal is

D=(1,1,-1,-1,-1,-1,1,1,0,0,0,0), repeated for the imaginary components.

The scalar identity is g=4-h q/2, q=sum_i D_i u_i². On the original h>0 branch, g=0 is equivalent to q=8/h. Select the positive-sign pivot u0=Re A0. On the chart u0>0, define

R(x,u_nonpivot)=8/h(x)-sum_(i!=0) D_i u_i²,

u0=+sqrt(R).

The chart guard is R>0. This is locally equivalent to the original scalar equation together with u0>0, because substituting the square root gives q=8/h and solving q=8/h for a positive u0 gives exactly the same square root. The derivative of q-8/h with respect to u0 is 2u0, which is nonzero in the chart. There are 23 remaining real state-coordinate functions; the scalar condition removes one real coordinate, not one independently derived physical degree of freedom.

At u0=0 this particular chart fails. Since h>0 implies q=8/h>0, at least one positive-sign real coordinate must be nonzero. Choosing that coordinate as pivot and its local sign supplies another chart. This covers the positive-q scalar hypersurface locally, without asserting a preferred physical pivot or frame.

## All-order statement and derivative constraint

For arbitrary analytic nonpivot functions, if h is analytic and positive and R at the central point is positive, the formula defines an analytic pivot on a sufficiently small neighborhood. Explicitly,

sqrt(R)=sqrt(R0) sum_(n>=0) binom(1/2,n)((R-R0)/R0)^n

converges wherever |R-R0|<R0 in the analytic chart. Thus this scalar subproblem has an explicit local all-order construction, not merely separately fitted zeros at several orders. No numerical radius or common neighborhood for the full field system has been certified.

The pivot derivatives are not free. For example,

partial_mu u0 = [partial_mu(8/h)-2 sum_(i!=0) D_i u_i partial_mu u_i]/(2u0).

At every higher order the differentiated scalar equation similarly determines the highest pivot derivative linearly from lower pivot derivatives, h derivatives and the nonpivot jets. A future full PDE fit must construct these derivatives inside its evaluator. Normalizing only the central state, or replacing a fitted pivot afterward, omits the required chain rule and generally breaks the remaining equations.

This chart fixes q and all its h-linked derivatives. It does not fix the other spinor directions, a unique coframe, metric, orientation, full currents, spin connection, action, constraint propagation or regional field evolution. All those remain governed by their own equations. The eight real C-species directions with D_i=0 remain unconstrained by this scalar equation alone.

## Reusable implementation and exact original background branch

scalar_parametrization.py implements normalized multivariate formal series, reciprocal and positive-square-root recurrences. For the original h=gamma/Delta, gamma=(1-r²/t²)^-1/2 and Delta=cos(asin(t/2)), the real local branch |t|<2, r²<t², t!=0 gives

h^-1=sqrt(1-r²/t²) sqrt(1-t²/4).

The implementation builds this exact background expression by formal series operations, avoiding high-order symbolic expansion. The square-root recurrence is b0=sqrt(a0), b_alpha=[a_alpha-sum_(beta,gamma>0,beta+gamma=alpha) b_beta b_gamma]/(2b0). Products use ordinary convolution because coefficients are partial^alpha/alpha!, with the multiindex factorial. This yields a unique formal pivot at every order when the central guard holds.

Reproduce: `python scalar_parametrization.py --input fifth-window-result.json --order 7 --digits 70`. The supplied nonpivot fifth jets are used as polynomial coefficients; absent nonpivot degrees6 and7 are set to zero for this demonstration. Those choices are not derived from the full field equations. Output scalar_parametrization_order7_result.json records coefficients, input hashes, chart guards and pre/post residuals. All inputs were unchanged during the run.

## Executed seventh-order demonstration

All three germs have central radicands about3.32–3.37, positive pivot values about1.82–1.84 and implicit derivative2u0 about3.64–3.67. The other central background guards are 1-r²/t² about0.638–0.645 and 1-t²/4 about0.747–0.755. At70-digit working precision, every scalar g coefficient through degree7 is below3.3e-67; the independent defining square and q-target identities are also checked in the truncation. This is arithmetic verification of the constructed scalar chart, not a certified high-precision full-PDE zero.

Pivot actual-derivative change norms relative to the saved fifth-window jets are:

| point | degree0 | degree1 | degree2 | degree3 | degree4 | degree5 |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 3.80e-16 | 1.24e-14 | 3.51e-14 | 7.96e-11 | 7.56e-10 | 9448.57 |
| 1 | 2.61e-16 | 7.38e-16 | 1.69e-14 | 8.76e-12 | 8.36e-11 | 9728.54 |
| 2 | 1.55e-16 | 1.67e-15 | 3.05e-14 | 2.89e-12 | 2.87e-11 | 7707.84 |

Degrees0..4 change only at the scale of the previous scalar violations. Degree5 changes are substantial because the prior fifth-jet calculation imposed F through derivative degree4, which controls g through degree4 but not g degree5. This is precisely the next scalar gate; it was not already satisfied. With zero nonpivot degrees6/7, pivot actual sixth derivatives have norms about43,500–69,000 and seventh derivatives about371,000–458,000. These are one chosen scalar completion, not a bound or a physical scale.

## Direct full-field countercheck: normalization is not a repair by itself

scalar_parametrization_field_check.py feeds the normalized coefficients back into the previously reviewed full nonlinear comparison. It does not fit or modify the model. At the central points the coframe changes by less than3.4e-15, as expected from the tiny value/first-jet corrections. However the raw fourth derivative block of F becomes approximately18,920,19,235,12,823. The old full-field fifth-jet solution is therefore NOT preserved after scalar-only normalization. Scalar g is identically satisfied while other equations are badly violated at that order.

This countercheck is intentional. It demonstrates why the chart must be integrated as a coordinate parametrization of the full residual before optimizing the remaining23 functions. The normalization is not a permissible postprocessing claim that OP5 is solved. Its full-field impact is saved in scalar_parametrization_field_check_result.json.

## Strongest safe result and remaining work

The scalar compatibility equation has an explicit exact local analytic parametrization and a reproducible all-order formal recursion on its guarded chart. This removes the scalar gate as an independent equation only if all induced pivot derivatives are included. It does not remove the other compatibility equations or guarantee that the remaining PDE admits a solution. Next work is to substitute this chart into the full comparison, retain its original couplings/domain and evaluate the reduced residual with all chain-rule/background terms. Any highest-jet elimination must then be recomputed for the reduced state coordinates. No native action, regional solution, global common chart or OP5 closure is established here.
