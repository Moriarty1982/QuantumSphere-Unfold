# Differentiated Gravity on the Regular Cartan Branch

Date: 2026-10-18. Status: derived Cartan/Noether compatibility identities and a numerical finite-jet completion in the **added neutral odd-cross Einstein-Cartan comparison**. Not a full constraint hierarchy, evolved solution, Cauchy/existence theorem, native gravity or physical scale. Main TeX/PDF unchanged.

This follows the [first spatial-integrability audit](HC_Cartan_Spatial_Propagation.md). That audit completed all point equations and first coframe-constraint/probe derivatives, but not differentiated gravity or second coframe constraints. Here both are retained simultaneously, on the same regular nonzero-multiplier point. The successful completion is supported by derived row identities, rather than a projected residual alone.

## 1. Keep the New Lower Point, Not Its Arbitrary Higher Completion

Keep E=I, dE=0, the prepared Psi value and first derivatives, symmetric E2, lambda value and first derivatives, M, Q, c=1 and u=0. In particular the temporal multiplier column remains `(.01,.02,-.03,.04)`; its regular probe block and positive temporal weights are unchanged. These assumptions specify the same comparison action, not a newly identified native HC action.

The unknowns for this step are:

- Symmetric Psi2: 240 real coordinates.
- Symmetric lambda2: 160 real coordinates.
- Symmetric E3: 320 real coordinates.
- Symmetric Psi3: 480 real coordinates.

There are 1,200 real unknowns, with all mixed derivatives commuting. The retained equations are 64 first coframe constraints F_,r, 96 real first probe equations R_,r, 64 first independent coframe Euler equations FE_,r, and 160 second coframe constraints F_,rs counted over symmetric r,s. This is a **384-component unprojected system**. All original point Euler equations remain satisfied by the unchanged lower point.

The preceding particular Psi2/lambda2 completion cannot simply be kept: allowing only E3/Psi3 leaves a best residual about `6122.412` in the 384-by-800 control. Its first gravitational derivative was already about `3563.680` before that attempted repair. This excludes extending those particular frozen higher data in this way, not other data or the model.

## 2. The Nonzero-Multiplier Cartan Reaction

Use the same independent connection equation, with its source and multiplier coupling retained:

\[
 H(E)k=-s(E,\Psi)+L(\Psi)^T\lambda.                              \tag{1}
\]

At dE=0, H_,r=0 but H_,rs is generally nonzero. Twice differentiating gives

\[
 \begin{split}
 H k_{,rs}={}&-s_{,rs}+L_{,rs}^T\lambda
       +L_{,r}^T\lambda_{,s}+L_{,s}^T\lambda_{,r}\\
       &+L^T\lambda_{,rs}-H_{,rs}k.
 \end{split}                                                       \tag{2}
\]

The term L_,rs^T lambda vanished on the former lambda=0 branch. It cannot be dropped here: its component norm in the new completion is about `41.475`. The Hessian/volume reaction H_,rs k and the E2 contribution to s_,rs also remain. Formula (2) reduces to the previous connection-jet implementation when lambda's value is zero, as a regression check.

Add the second derivative of the LC connection to k_,rs to obtain the complete connection derivative. At this normal point that LC contribution is linear in E3. Curvature derivatives include both the connection derivative and the differentiated omega-commutator term. Neither torsion nor its reaction is silently set to zero.

The independent coframe Euler equation at the normal point has form

\[
 FE=L_D I+X^T+{\cal G}(R(\omega))+\lambda,
\]

where X is the unweighted kinetic bilinear and G the independent Palatini coframe derivative. Thus

\[
 FE_{,r}=L_{D,r}I+X_{,r}^T+{\cal G}(R_{,r})+\lambda_{,r}.        \tag{3}
\]

This is not the LC-restricted chain variation and is not a replacement by a background Einstein equation. The full real probe derivative retains the variable kinetic density and connection-adjoint terms from the prior audit.

## 3. Why the Rank Is 332: Derived Identities

Let F=C-E, R the complex probe Euler expression, and FE the real coframe Euler density. At the retained on-shell point, the eliminated Cartan equation holds along with F=R=FE=0. Three sources of linear row relations then apply to the higher-jet equations.

**First-constraint curls, 24 rows.** Commuting second spinor derivatives cancel from

\[
 F^a{}_{s,r}-F^a{}_{r,s}=G^a{}_{rs}.
\]

The fixed lower point was prepared with G=0. These 24 antisymmetric combinations are therefore compatibility relations on the 64 first constraint equations. This is the same derived gate as before, not an extra field law.

**Differentiated local Lorentz identity, 24 rows.** Let J obey J^T eta+eta J=0, and let

\[
 S_J=-\tfrac14(\eta J)_{ab}\Gamma^a\Gamma^b.
\]

Local Lorentz variations are delta E=J E, delta Psi=S_J Psi and delta lambda=-J^T lambda. With the independent Cartan equation eliminated, differentiating the action identity at the on-shell point gives, for each r and each of six J,

\[
 FE_{,r}:J
 +2\operatorname{Re}\bigl((S_J\Psi)^\dagger R_{,r}\bigr)
 +F_{,r}:(J^T\lambda)=0.                                        \tag{4}
\]

These are 24 explicit combinations of first gravity, probe and coframe-constraint equations. They are checked on arbitrary higher jets, not only the fitted solution.

**Coordinate Noether identity, four rows.** Treat lambda as the contravariant coordinate vector density appearing in lambda:(E-C). More explicitly, write the coframe Euler density as FE_a^mu=delta S/delta E^a_mu, with a lower frame index. The coefficient of partial_mu xi^nu in the coordinate variation is

\[
 I^\mu{}_\nu
 =FE_a{}^\mu E^a{}_\nu-F_\lambda{}^a{}_\nu\lambda_a{}^\mu
   +\delta^\mu_\nu F_\lambda:\lambda,\qquad F_\lambda=-F.
\]

At the on-shell normal point its divergence gives the Euler-density form

\[
 \sum_\mu FE_\nu{}^\mu{}_{,\mu}
 +\sum_{a,\mu}\lambda_a{}^\mu
       \bigl(F^a{}_{\nu,\mu}-F^a{}_{\mu,\nu}\bigr)=0.             \tag{5}
\]

This is not an assumption of torsion-free Einstein divergence. The full sourced Cartan identity has already been used. In the current prepared data G=0, so the ordinary divergence in this density formula vanishes as a consequence.

Together these give an explicit 52-by-384 row-relation matrix. At this point its evaluated rank is 52. Its product with the higher-equation coefficient matrix has norm about `2.45e-13`, and with the affine source about `1.07e-13`. The evaluated 384-by-1200 equation matrix has rank **332=384-52**: no further row obstruction is detected at this order. This accounts structurally for the successful affine completion. The identities are derived algebraically; the evaluated ranks and compatibility residuals are numerical, not interval-certified universal rank theorems.

## 4. Joint Regular-Branch Completion and Curvature

Re-solving Psi2/lambda2 together with E3/Psi3 gives full residual about `5.69e-11`. The first gravity component norm is about `2.03e-11`; the full symmetric second-constraint tensor norm, counting both mixed entries, is about `6.18e-11`. First constraint and probe derivatives remain below `1e-10`. All 1,200 coordinates are saved.

Because F, dF and d2F vanish to numerical precision, the bilinear cross coframe and independent E have the same metric curvature at the point. This is **recomputed on the regular branch**, not inherited from the former zero-multiplier construction. The analytic curvature difference is about `9.70e-11`; an independent field-difference reconstruction agrees to about `3.57e-4` at step 2e-5. The independent E metric's unscaled LC scalar is about `1.82289`. That number is in arbitrary comparison coordinates and is not a physical curvature prediction or determination of a Planck scale.

The same data give analytic-versus-field-difference errors about `9.23e-5` for the second connection jet, `3.06e-4` for the second constraint and `8.68e-5` for the first coframe Euler derivative. The latter uses nested differences of the full independent parent expression. These checks have finite-difference/roundoff error; none is an interval certificate. The separate source-response and EH-Hessian second variations are also checked.

## 5. Ten Leading Gauge Directions and Six Still Unresolved

The prior 68-by-56 normal system still has rank 40 and kernel dimension 16. Ten kernel directions can now be exhibited as leading parts of actual gauge transformations:

- Four coordinate directions: xi^a=v^a t^3/6 produces delta E^a_0,00=v^a at the point.
- Six Lorentz directions: a Lorentz parameter J t^2/2 produces delta E_,00=J.

These transformations preserve E, dE, the spinor value/first derivatives and lambda value/first derivatives at the point. Their accompanying higher spinor/multiplier changes are part of the full gauge transformation; the displayed basis lists only its leading normal components. The ten 56-component vectors are independent and are annihilated by the normal matrix.

After these **ten exhibited leading gauge directions**, the normal quotient still has dimension six, and the kernel projection onto spatial multiplier velocities has rank six. They are not declared six physical particles, instabilities or necessarily nongauge modes. This does not establish complete gauge fixing or exclude additional constraint/gauge structure. In the present calculation these lower velocities were held at the already prepared values; differentiated equations constrain the next jets, not a unique full time evolution of those remaining directions.

## 6. Limits and Next Step

The Taylor fields remain off shell away from the origin. For radii `.002,.001,.0005` along the tested direction, coframe-constraint norms are approximately `1.62e-4,2.02e-5,2.53e-6`, with cubic decay. Probe and coframe Euler residuals decay quadratically, but remain nonzero. The full algebraic Cartan equation remains sourced and satisfied along those fields.

The result is a regular finite-jet extension retaining differentiated gravity, second coframe constraints and all original point equations, with its rank explained by derived identities. It is not a proof of closure of the constraint hierarchy. Next include third coframe constraints and second probe/gravitational equations, identify the remaining multiplier/gauge consistency conditions and maintain constant-rank control. Cauchy data on an open surface, propagation, convergence/existence, global boundary conditions, native action/gauge/HC/C7 identification and physical normalization remain open.

## Reproduction

- [Calculation](HC_Cartan_Regular_Gravity.py), [saved audit and coordinates](HC_Cartan_Regular_Gravity.json), [42 tests](../scripts/qsc_audit/tests/test_hc_cartan_regular_gravity.py).
- `python -B analysis/HC_Cartan_Regular_Gravity.py --output analysis/HC_Cartan_Regular_Gravity.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_regular_gravity.py`

The shared Taylor-field helper now accepts optional cubic E/Psi jets; its previous quadratic default is unchanged and remains covered by the prior spatial tests. Tests retain the zero-multiplier limit, nonzero-value Cartan reaction, independent source/field differences, explicit row identities on arbitrary jets, full unprojected residuals, leading gauge directions, pointwise curvature matching and nonzero off-shell remainders. No package installation, main-TeX/PDF rebuild, release modification or Git operation is introduced.
