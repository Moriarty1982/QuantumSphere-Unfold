# First Spatial Integrability on the Regular Cartan Branch

Date: 2026-10-18. Status: analytic first-constraint compatibility criterion, numerical regular-point re-preparation and first constraint/probe prolongation in the **added neutral odd-cross Einstein-Cartan comparison**. Not a constraint-propagation theorem, Cauchy-surface construction, evolved solution, native identification or physical scale. Main TeX/PDF unchanged.

This continues the [temporal Cauchy-rank audit](HC_Cartan_Cauchy_Rank.md). A regular temporal probe block did not establish spatial-constraint compatibility. Here a curl of the existing coframe constraint supplies a concrete next gate. The earlier regular point fails it, but re-solving its free first spinor derivatives along with its geometric/multiplier derivatives gives a compatible first differential extension. The remaining normal system is still underdetermined.

## 1. A Derived Gate, Not an Additional Field Law

Keep the same real parent, M, Q, Einstein coefficient c=1 and vacuum coefficient u=0. The spin connection remains independent in the parent and is eliminated from **its own sourced Cartan equation**. At the normal point impose E=I and dE=0, as before. Put

\[
 F^a{}_{\mu}=C^a{}_{\mu}-E^a{}_{\mu},\qquad
 C^a{}_{\mu}=\operatorname{Im}(\Psi^\dagger A_a D_\mu\Psi),\qquad
 A_a=Q\otimes K^a.
\]

Define the 24 curl components, with r<s,

\[
 G^a{}_{rs}=\partial_r F^a{}_s-\partial_s F^a{}_r.                 \tag{1}
\]

If F vanishes on a neighborhood, G must vanish there. Spatial pairs i<j are necessary integrability conditions for surface data; the mixed pairs 0,i test a first time-extension condition. They are **differential consequences of F=0**, not added forces, new coupling assumptions or independently postulated equations. At the selected point dE=0, the subtracted exterior derivative of E vanishes. This coordinate statement does not set the Lorentz-connection torsion to zero.

Write p_r=partial_r Psi, p_rs=partial_r partial_s Psi and B_mu for the common spin connection lifted to the three channels. Direct differentiation gives

\[
 \begin{split}
 \partial_r C^a{}_s={}&\operatorname{Im}\bigl[
 p_r^\dagger A_a(p_s+B_s\Psi)\\
 &+\Psi^\dagger A_a(p_{rs}+B_{s,r}\Psi+B_s p_r)\bigr].
 \end{split}                                                        \tag{2}
\]

Because partial derivatives commute and p_rs=p_sr, all second spinor derivatives cancel from (1):

\[
 \begin{split}
 G^a{}_{rs}=\operatorname{Im}\bigl[&
 p_r^\dagger A_a(p_s+B_s\Psi)-p_s^\dagger A_a(p_r+B_r\Psi)\\
 &+\Psi^\dagger A_a\bigl((B_{s,r}-B_{r,s})\Psi+B_s p_r-B_r p_s\bigr)
 \bigr].
 \end{split}                                                        \tag{3}
\]

Thus arbitrary higher spinor jets cannot fix a nonzero G while these lower data remain frozen. The sourced connection derivative depends on p_r, E2 and d lambda, which can change G. It is not held at its old zero-multiplier value.

For the auxiliary contorsion coefficients, retain

\[
 Hk=-s+L^T\lambda,\qquad
 Hk_{,r}=-s_{,r}+L_{,r}^T\lambda+L^T\lambda_{,r}.                 \tag{4}
\]

The H_,r term vanishes at this normal point because dE=0, not because H is globally constant. Add the derivative of the LC connection to k_,r to obtain the full connection derivative. Independent field differences check this elimination and the product rule in (3).

## 2. Why These Are Exactly the First Constraint Obstructions Here

On one real 24-component spinor variation define the four-function map

\[
 {\cal B}_\Psi(v)^a=\operatorname{Im}(\Psi^\dagger A_a v).
\]

Its evaluated rank is four at the unchanged spinor value. The second-derivative contribution to partial_r F^a_s is simply B_Psi(p_rs). Since p_rs is symmetric in r,s, its image consists of all symmetric derivative-index tensors with four coframe components, of dimension 4*10=40. There are 64 first constraint equations, leaving exactly the 24 antisymmetric conditions (1).

For this surjective principal map, **G=0 is necessary and sufficient to complete all first derivatives of F at the point**, with E2, d lambda and p_r fixed. Indeed, let V^a_rs be (2) with p_rs=0, and choose any real right inverse B_Psi^+. The constructive symmetric choice

\[
 p_{rs}=-{\cal B}_\Psi^+\bigl((V_{rs}+V_{sr})/2\bigr)             \tag{5}
\]

removes the symmetric part. Its remaining constraint derivative is the antisymmetric part, with Euclidean component norm ||G||/sqrt(2), counting each r<s once in G. This is a pointwise principal-map statement; it is not sufficiency for the full field system or for a neighborhood. In particular the zero spinor fails the rank assumption.

## 3. What the Previously Regular Point Fails

The saved point satisfies all original point Euler equations to numerical precision, and its temporal probe block is positive and invertible. Nevertheless, its full curl norm is `66.14005` (mixed-pair norm `48.85929`). The best symmetric second-spinor/multiplier completion of the 64 first constraint and 96 real first probe equations has residual `46.76808`, consistent with the unavoidable antisymmetric part.

An attempt to change only E2 and d lambda, while keeping the first spinor jet fixed and retaining every point equation, also fails: the 80-by-224 affine system has rank 28 and minimum unprojected residual `7.93436`. This is a failed repair of these frozen data, not an exclusion of other first jets or of the model. No unsuccessful least-squares fit is relabeled a solution.

## 4. Six Additional Normal Restrictions, Not a Closed Evolution System

Retain the earlier 56 normal unknowns: E_,00 (16), Psi_,0 (24 real) and lambda_,0 (16), with the other jets fixed. Appending G_0i=0 to the original 56 point equations gives a 68-by-56 affine system. On the regular branch its evaluated rank is 40, compared with 34 before the added curls.

More precisely, write the old normal system as N x+b=0 and let Z span its 22-dimensional kernel. Write the twelve mixed curls as V x+g=0. A particular solution x_* gives

\[
 VZ z=-(Vx_*+g).                                                  \tag{6}
\]

Here rank(VZ)=6. Its six-dimensional left kernel supplies **six further compatibility conditions on the frozen lower/spatial data**; the remaining six independent equations restrict normal directions. They do not independently determine twelve new velocities. The prior regular point fails these compatibility projections and the full appended normal system has best residual `2.83665`.

On the newly prepared compatible data below, that residual is about `1.13e-13`. The normal kernel still has dimension 16; its projection onto the temporal derivatives of the spatial multiplier columns has rank six, rather than the earlier twelve. These null directions have not all been classified as gauge or physical freedoms. The calculation does not establish a fully reduced principal symbol, hyperbolicity or uniform estimates.

## 5. Re-Solve the Free First Jet on the Same Regular Branch

Keep the same spinor **value**, multiplier **value**, M, Q, c and u. The temporal multiplier column remains `(.01,.02,-.03,.04)`, with the other multiplier columns zero. Accordingly the smallest temporal probe eigenvalue remains `.96807418` and the smallest T singular value remains `.0339230`. The first spinor derivatives are allowed to change: this is new initial-jet preparation, not evolution of the old data.

Solve the 56 original point equations and all 24 curls using 320 real unknowns: first Psi (96), symmetric E2 (160) and d lambda (64). At fixed Psi and lambda values this map has an exact affine-plus-quadratic form. Its only quadratic part is

\[
 2\operatorname{Im}(p_r^\dagger A_a p_s)
\]

in the curl rows; the exact quadratic Jacobian is checked by independent differences. A minimum-norm Newton step with residual-decreasing backtracking reduces the **full unprojected** residual from `66.14005` to `3.64e-14` in six accepted steps. The evaluated Jacobian has rank 74. This is a numerical preparation, not a uniqueness or interval-certified existence result.

For this new point, solve the 64 first constraint equations together with the 96 real first probe equations for symmetric Psi2 (240 real) and lambda2 (160). The 160-by-400 affine map has rank 136; its residual is `3.04e-12`. Both spatial and mixed first constraint derivatives are included, not only a projected subset. The complete real probe equation includes variable kinetic weights, density/connection-adjoint terms and the nonzero Cartan reaction. All 320 lower and 400 higher coordinates are saved for reproduction.

The first derivative of the coframe Euler equation and the second derivative of F have **not** been completed on this new branch. Earlier higher-order results on the zero-multiplier branch cannot be transferred to it.

## 6. Independent Differences and Remaining Work

Quadratic Taylor fields constructed from the new jets retain the full algebraic Cartan equation away from the origin. At difference step 2e-5, analytic-versus-independent derivative errors are about `8.86e-6` for F, `5.75e-6` for the probe equation and `4.54e-7` for the connection. Halving the step exhibits the expected second-order difference convergence.

The fields themselves remain off shell away from the origin. Along the tested direction, at radii `.002,.001,.0005`, the F norms are approximately `.01355,.003393,.0008490` and probe norms `.01304,.003253,.0008124`: nonzero quadratic remainders. Their elimination would need more than the checks performed here. No physical length or energy unit is attached to these comparison coordinates.

The concrete progress is a derived first spatial-integrability criterion and a regular first differential completion satisfying it with all point equations retained. Next retain the differentiated gravitational equations, determine the remaining multiplier/gauge consistency conditions and check whether the constraint hierarchy closes on a constant-rank branch. Actual Cauchy data on an open surface, a propagation theorem, local/global existence, curvature matching on this new branch and native action/HC/C7/physical scale identification remain open.

The next [regular gravitational prolongation](HC_Cartan_Regular_Gravity.md) retains the nonzero multiplier-value reaction in the second Cartan derivative. It jointly completes first gravity and second coframe constraints after re-solving the free second/higher jets, explains the evaluated rank 332 by 52 curl/Lorentz/coordinate identities and recomputes pointwise curvature matching. Ten leading normal gauge directions are exhibited, while a six-dimensional normal quotient remains unresolved. This is not a closed constraint hierarchy or evolved/native solution.

## Reproduction

- [Calculation](HC_Cartan_Spatial_Propagation.py), [saved audit and coordinates](HC_Cartan_Spatial_Propagation.json), [38 tests](../scripts/qsc_audit/tests/test_hc_cartan_spatial_propagation.py).
- `python -B analysis/HC_Cartan_Spatial_Propagation.py --output analysis/HC_Cartan_Spatial_Propagation.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_spatial_propagation.py`

Tests cover curl cancellation, the exact symmetric principal-map criterion and its rank exception, failed frozen-data controls, normal compatibility projections, the nonlinear preparation, all retained point/first equations, holonomic jets, independent source/field differences and explicit off-shell remainders. No package installation, TeX/PDF rebuild or release change is introduced.
