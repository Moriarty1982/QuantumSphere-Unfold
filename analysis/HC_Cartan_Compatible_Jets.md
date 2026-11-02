# Compatible Local Taylor Data for the Odd-Cross Cartan Parent

Date: 2026-10-17. Status: a numerical, finite-order local construction in the **same explicitly added neutral comparison parent** as [the Cartan/coframe analysis](HC_Cross_Cartan_Parent.md). It is not Cauchy data on a whole surface, a local-existence proof, an evolved spacetime solution, an adopted native equation, or an interval-certified construction. Main TeX/PDF unchanged.

The previous curved fixed-reference example failed even the necessary connection/constraint equations on its unchanged jet. Here the state and its derivatives are allowed to change. The matrix M, selector Q and action are not changed to obtain a fit. This yields pointwise data satisfying all four Euler equations and the first derivative of the coframe constraint. Higher-order propagation remains unproved.

## 1. Retain the Parent, Choose a Normal-Point Branch

Use the independent E, Lorentz connection omega, commuting three-channel probe Psi, and multiplier density lambda of the preceding note:

\[
 S=\int d^4x\{v(cR(E,\omega)/2-u)+\mathcal L_D
                      +\lambda_a{}^\mu(E^a{}_{\mu}-C^a{}_{\mu})\},
 \qquad C^a{}_{\mu}=\operatorname{Im}(\Psi^\dagger QK^aD_\mu\Psi).
\]

Keep the prepared matrix with diagonal .6 and mediator links 4,.7, and Q=i(E12-E21)/2. For this example set c=1 and u=0 in the arbitrary comparison normalization. Neither c nor any mass, coupling or Planck scale is fitted or predicted. There is no added charged gauge sector, native HC/C7 realization or quantum ground-state identification.

At the chosen point take

\[
 E=I,\quad\partial E=0,\quad\lambda=0,\quad
 \sum_\mu\partial_\mu\lambda_a{}^\mu=0.                                  \tag{1}
\]

The last condition is an additional **choice of data**, not a discarded field equation or gauge condition. Individual derivatives of lambda are allowed and turn out nonzero. A normal value and first jet of E do not require its second jet or metric curvature to vanish. The full connection need not vanish there: torsion is retained.

At lambda=0 the algebraic Cartan equation gives

\[
 k=-H_1^{-1}s_0,\qquad\omega=\omega_{LC}(E)+k.                           \tag{2}
\]

This is evaluated from the same probe used in C and in its equation. It is not an independent prescribed gravitational connection.

## 2. Derive the State Normalization Before Solving Derivatives

For this point branch the Hermitian temporal kinetic density is I_12. Direct evaluation also checks the connection/density defect in the real probe equation; it is not silently dropped. With E=C, contracting the coframe equation gives

\[
 \sum_\mu\operatorname{Im}(\Psi^\dagger QK^\mu D_\mu\Psi)=4.
\]

The real part of the Q-weighted probe equation therefore requires

\[
 b_Q:=\operatorname{Re}(\Psi^\dagger(QM\otimes\beta)\Psi)=-4.             \tag{3}
\]

The real quantity is the expectation of `({Q,M}/2) tensor beta`; Q and M do not commute. It is not a positive particle-mass observable. A negative value does not introduce an imaginary mass or determine a new physical particle mass.

Choose a deterministic generic free spinor seed with b_Q<0 and multiply its amplitude by `sqrt(-4/b_Q)`. This is **state preparation required by the selected constitutive normalization**, not a predicted vacuum amplitude or physical mass fit. The declared dimensionless normalization of E=C remains an extra assumption.

For fixed Psi and (2), solve simultaneously for its four covariant derivatives D_mu Psi. Their 96 real components obey 16 real coframe equations and 24 real probe equations. On this seed the 40-by-96 matrix has rank 39. Its exact left-null identity is (3); an unnormalized seed fails the combined system. After (3) there are 57 free real derivative components.

The resulting rank-four coframe is reconstructed with the **same full connection and coordinate gammas** as the probe equation. This is not the old procedure of solving a reference equation and then substituting a different induced connection.

In the preceding note's eliminated connection equation, these data obey `b=Lk=-d` at c=1 and lambda=0. Thus they satisfy its original Schur-image condition already at this stage. The next compatibility problem below is stronger: it adds the geometric Euler equation and the differentiated constraint.

## 3. Retain the Next Compatibility Equations Too

The raw least-norm first derivatives are not enough. To test their next compatibility, retain unknown symmetric second derivatives of E and Psi, together with the first derivative of lambda:

- 160 real E second-derivative components.
- 240 real Psi second-derivative components.
- 64 real lambda first-derivative components.

The mixed derivatives are symmetric; ordered mixed partials are not fitted independently. Differentiate (2), including the multiplier reaction from the full eliminated equation:

\[
 \partial_r\omega=\partial_r\omega_{LC}
          +H_1^{-1}\{-\partial_r s_0+L^T\partial_r\lambda\}.             \tag{4}
\]

At (1), derivatives of H_1 times k and derivatives of L times lambda vanish. The source derivative is the actual quadratic-spinor derivative, not an independently selected curvature source.

Impose the 64 components of `partial_r(C-E)=0`, all 16 components of the independent coframe Euler equation, and the four selected divergence conditions in (1). For fixed first derivatives this gives an 84-by-464 linear system, of rank 68 on this example. Its 16 left-null equations must be obeyed; a least-squares vector with a nonzero residual is not accepted.

Use the 57 still-free first-derivative components from the previous step to meet those compatibility conditions. A damped numerical Newton correction reduces their norm from `8.09484` through `1.24410`, `.0535786`, `.000804368`, `1.76e-7` to `2.01e-14`. Then solve the **whole** second-jet system again. The chosen minimum-norm data and Newton path are numerical preparation choices, not a derived physical selection principle or a uniqueness result.

For the completed local data, direct residual norms are:

| Equation | Displayed-coordinate residual norm |
| --- | ---: |
| Coframe constraint E=C | `9.6e-15` |
| Complete real probe equation | `2.3e-14` |
| Algebraic Cartan equation | below `1e-13` |
| All independent coframe Euler components | `3.6e-14` |
| First derivative of E=C, all directions | `2.2e-13` |
| Selected multiplier divergence | `9.6e-15` |

These are finite numerical checks, not certified exact zeros or physical error bars. The point's Q-weighted axial square is `3.97288>0`, within the spacelike domain of the previous compatibility criterion. The first-order obstruction was not evaded by moving into an unexamined null-axial case.

The **independent coframe's** metric has signature (-+++) and nonzero LC curvature; its Ricci scalar is about `3.51772` in the arbitrary comparison units. This is not a physical curvature prediction. In particular, matching C and E through their first jets does **not** yet identify their second jets or prove that the cross-readout metric has that curvature. The second differentiated coframe constraint is a further gate.

## 4. Check Actual Fields, Not Just Matrix Residuals

The report saves all complex probe jets, real coframe second jets and multiplier first jets. Form actual smooth fields near zero:

\[
 E(x)=I+\tfrac12 E_{,rs}x^rx^s,\qquad
 \Psi(x)=\Psi_0+\Psi_{,r}x^r+\tfrac12\Psi_{,rs}x^rx^s,\qquad
 \lambda(x)=\lambda_{,r}x^r.
\]

At each nearby point, recompute the LC connection and solve the same algebraic Cartan equation including lambda. Thus the auxiliary connection equation is satisfied there by construction. The full real probe residual retains the varying kinetic density and volume derivatives.

Independent finite differences of this actual connection check (4) to `1.9e-9`. Using that independently differentiated connection in the coframe equation gives origin residual about `7.3e-10`, consistent with differentiation error and the analytic-jet result above.

Away from zero the other equations are **not** solved. Along one fixed normalized direction, halving the displacement from `.002` to `.001` to `.0005` gives coframe-constraint norms `.000509944`, `.000127462`, `.0000318623`: a quadratic remainder. Probe residuals are `.101561`, `.0508042`, `.0254080`: a linear remainder. These controls deliberately expose the missing higher-order equations. A smooth Taylor extension of jets is not an on-shell evolution.

## 5. A Positive Temporal Domain, Without a Stability Claim

The temporal probe form is I_12 at zero. For these polynomial E and lambda fields let

\[
 B_E=\|E''\|_F,\quad B_\lambda=\|\lambda'_{r,a}{}^0\|_F,
 \quad r=\|x\|_2,\quad\delta=\tfrac12 B_E r^2<1.
\]

Then `norm(E-I)<=delta`, the smallest volume factor is at least `(1-delta)^4`, and the inverse-coframe temporal perturbation is bounded by `sqrt(2) delta/(1-delta)`. Since norm(Q)=1/2, the multiplier correction is bounded by `r B_lambda/sqrt(2)`. Where the first factor is positive, this gives

\[
 \lambda_{min}(\mathbb K^0)\ge
 (1-\delta)^4\left(1-\frac{\sqrt2\delta}{1-\delta}\right)
                  -\frac{rB_\lambda}{\sqrt2}.                          \tag{5}
\]

The conservative ball selected by the script has radius `.150707` and lower bound `.34825`. Both are in unscaled comparison coordinates, not a physical length or energy. Sampling several directions independently checks the bound and full-rank coframe. This concerns the probe kinetic form on these off-shell fields, **not** stability, positive total energy, a quantum ground state or well-posedness of the full constrained system.

## Outcome and Next Gate

The previous fixed example's obstruction is not universal at this finite order: after changing its state and derivative data, the **same assumed parent** admits numerically compatible point jets with nondegenerate coframe, positive temporal probe form, all four Euler equations at the point and first constraint prolongation. The actual normal equations, multiplier gradients and sourced connection have been retained.

Next one must enforce the second derivative of E=C and differentiated probe/coframe equations, or construct full constraint-satisfying data on a spacelike surface and prove propagation. A finite jet does not establish formal integrability, analytic local existence or a global solution. Native adjoint, gauge/HC/C7/readout identification, actual physical normalization, boundary conditions, quantum interpretation and the action's assumed Einstein term remain separate obligations. No new result is adopted in the main paper.

## Reproduction

Next-order follow-through: [joint Cartan prolongation](HC_Cartan_Prolongation.md) derives a scalar compatibility gate that the **frozen** data above fail. Retaining the same state value, first Psi derivatives, M, Q and parent, it re-solves the free second/multiplier jets together with third jets. Forty checks numerically satisfy second constraint derivatives and first probe/coframe derivatives, establishing cross/E metric curvature matching at the point and improving the explicit off-shell remainders. This does not establish propagation, analytic existence or an evolved/native solution; the earlier limited results above remain unchanged.

- [Calculation](HC_Cartan_Compatible_Jets.py), [saved numerical jets and diagnostics](HC_Cartan_Compatible_Jets.json), [38 focused tests](../scripts/qsc_audit/tests/test_hc_cartan_compatible_jets.py).
- `python -B analysis/HC_Cartan_Compatible_Jets.py --output analysis/HC_Cartan_Compatible_Jets.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_compatible_jets.py`

The tests cover the weighted-mass compatibility identity, unnormalized and raw-gradient negative controls, retained normal equations and symmetric jets, direct field/connection/curvature checks, temporal positivity, saved arrays and the explicit off-shell remainder. No package installation, TeX/PDF rebuild, release change or Git operation is introduced.
