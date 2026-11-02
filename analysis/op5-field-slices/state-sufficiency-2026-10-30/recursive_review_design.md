# Recursive Taylor calibrator: independent design notes

30 October 2026. Reusable finite-order feasibility diagnostics, no regional existence or physical identification.

## Factorial contract

Use coefficients c_alpha=(partial^alpha psi)/alpha!, alpha!=product_mu(alpha_mu!). Products are ordinary truncated convolutions with no binomial factors. A coordinate derivative maps c_(alpha+e_mu) to (alpha_mu+1)c_(alpha+e_mu). Convert saved symmetric actual derivatives to coefficients by dividing by the MULTIINDEX factorial, not the total-degree factorial. For example mixed xy Hessian has coefficient H_xy, whereas xx has H_xx/2. Cubic xxy has coefficient T_xxy/2, not T_xxy/6.

For normalized residual coefficient F_alpha, the highest coefficient c_(alpha+e_mu) has coefficient (alpha_mu+1) times the principal block partial F/partial J_mu. If top variables are actual derivatives instead, the same entry is the principal block divided by alpha!. The principal block must include the coframe's derivative dependence; using only the frozen kinetic matrix would miss known null directions.

For a matrix polynomial E with invertible E0, inverse coefficients satisfy V0=E0^-1, V_alpha=-V0 sum_(0<beta<=alpha) E_beta V_(alpha-beta). Matrix order matters. The summed lower V terms are already known in degree order. This produces E*V=I through the truncation order; verifying both E*V and V*E is a useful algebra regression.

Residual norms of normalized coefficients are not the same as norms of packed actual derivatives. Comparisons across orders or with historical reports must multiply each coefficient by its multiindex factorial before taking an actual-derivative norm. Report the convention and objective weights.

## Frozen fourth-order necessary control

The successful previous third jets have small g,dg,d²g but a large d³g. Independent recursive_review_fourth_gate.py evaluates it from original h through its third derivatives and saved psi,J,H,T. Explicit d³q formula is independently checked against the multivariate Leibniz/binomial formula to below 3.4e-14.

| point | norm packed d³g | norm d²g | d³g / norm ell |
|---|---:|---:|---:|
| 0 | 137.93976275 | 2.65e-11 | 97.59070674 |
| 1 | 133.70282611 | 3.07e-11 | 94.70663755 |
| 2 | 138.54553223 | 2.46e-11 | 97.97634888 |

Thus keeping all previous three jets frozen should fail fourth completion strongly. Releasing lower H/T jointly is essential. As before, the exact scalar attribution includes derivatives of ell multiplying lower residuals; do not interpret raw ratios as strict bounds at numerical floor. These scalar gates do not account automatically for every symmetric obstruction.

## Independent evaluator checks planned

Compare the generic residual coefficients through degree2 with the successful saved cubic jets using explicit product-rule or directional-polynomial derivatives, not another import of the optimizer's Taylor evaluator. Verify background factorial conversion separately. Add elementary polynomial product, derivative and matrix-inverse benchmarks with noncommuting matrices. For degree3 use a manufactured cubic/quartic polynomial field and direct evaluation at small directional displacements or an independent univariate formal-series calculation. A finite-difference comparison needs a range of step sizes because third differences can be cancellation dominated.

## Actual module review and executed independent check

Reviewed recursive_calibrator.py after the fourth-order three-point result was available. The multivariate convolution, Hermitian-real coframe, background coefficients, derivative shifts, per-coefficient real/imaginary packing and Neumann inverse ordering are correct on inspection. The Neumann construction is (I+E0^-1(E-E0))^-1 E0^-1, so its multiplication order is correct even for noncommuting matrices. The highest operator is built from the full derivative of the original nonlinear first-order residual with respect to first jets; its multiplicities alpha_mu+1 match normalized coefficient variables. Lower derivative degrees2..order-1 are varied, while value and first jets remain fixed. This is not a fixed-H or fixed-T calculation.

Executed recursive_review_coefficients.py without rerunning optimization. This is a distinct NumPy formal-series implementation along six real directions per point (four coordinate directions and two mixed directions). It recomputes the original symbolic normalized background, forms ordinary scalar/vector/matrix coefficient sums, and uses the recurrence inverse rather than the parent's Neumann inverse. It reconstructs F through degree3 and compares it against the directional polynomial obtained from the generic multivariate evaluator. It also checks both E*inverse and inverse*E, and perturbs selected top-coefficient columns to verify the generic highest operator. This is bounded direction/column coverage, not exhaustive validation of every conceivable input.

| point | maximum F coefficient discrepancy, degrees0..3 | maximum inverse identity error | maximum sampled top-operator error |
|---|---:|---:|---:|
| 0 | 2.97e-13 | 5.23e-13 | 7.08e-14 |
| 1 | 1.91e-13 | 4.36e-13 | 8.39e-14 |
| 2 | 3.83e-13 | 5.20e-13 | 7.15e-14 |

Full multivariate scalar-product convolution independently evaluates every normalized coefficient of g through degree3, then restores actual derivatives with multiindex factorials:

| point | norm g | norm dg | norm d²g | norm d³g |
|---|---:|---:|---:|---:|
| 0 | 8.88e-16 | 3.27e-14 | 8.66e-14 | 1.24e-12 |
| 1 | 8.88e-16 | 3.18e-15 | 4.28e-14 | 8.43e-13 |
| 2 | 4.44e-16 | 3.47e-15 | 7.73e-14 | 6.54e-13 |

The former frozen-third-jet scalar obstruction of norm about 134–139 is removed after joint adjustment of second and third jets. Fourth actual derivative norms are about 888–913, compared with third norms about 88–90 and second norms about 26. These norms are in the declared packed coordinate convention; their growth is neither a physical constant nor proof of convergence/divergence of an infinite jet expansion. A finite fourth-order Taylor polynomial always exists for the fitted jets but is not an exact regional solution of the nonlinear equations.

## Verdict

The generic fourth-order implementation passes this bounded independent arithmetic/convention review. The saved numerical three-point result is corroborated through an independent formal-series implementation and complete scalar third-derivative gate. No blocking bug was found. There is no claim of fifth-order completion, recursive convergence, uniform regional existence, a common field through all three points, native action identification or OP5 closure.

Reproduction: `python recursive_review_coefficients.py` and `python recursive_review_fourth_gate.py` in the task artifact directory. These scripts read existing saved results and do not run optimization or alter repository files. Their JSON records include input hashes. The generic evaluator is imported only for the comparison target and sampled operator perturbation; the independently computed series uses original model matrices/backgrounds and NumPy sums.
