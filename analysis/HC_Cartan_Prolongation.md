# Next-Order Cartan Jets and Pointwise Cross-Metric Curvature Matching

Date: 2026-10-17. Status: a numerical higher-order continuation of the **same added neutral odd-cross Einstein-Cartan comparison**, not an evolved/native solution, a Cauchy existence theorem or an interval-certified construction. Main TeX/PDF unchanged.

This follows [compatible local Taylor data](HC_Cartan_Compatible_Jets.md). That note satisfied all point Euler equations and the first coframe-constraint derivative. It explicitly did not establish their next derivatives or identify the cross-readout curvature. Here those next equations are retained together. The old lower jet cannot simply be frozen: a newly differentiated scalar compatibility condition fails on it. Re-solving its free higher data repairs that obstruction and achieves the next prolongation numerically.

## 1. An Exact Scalar Gate Before Any Higher-Jet Fit

Use the preceding parent, ordinary adjoint, constant internal Q, common spin connection, and fixed Hermitian M. No internal charged connection, varying selector, nonunitary HC transport or new term is inserted. The real-action residual uses the same Hermitian kinetic density weights and their full connection/density defect as before.

For an internal Hermitian weight W define

\[
 C[W]^a{}_{\mu}=\operatorname{Im}(\Psi^\dagger WK^aD_\mu\Psi),\qquad
 b_Q=\operatorname{Re}(\Psi^\dagger(QM\otimes\beta)\Psi).
\]

Q commutes with the kinetic weights and their Hermitian defect in this particular neutral, fixed-selector comparison. Taking the real part of the Q-weighted complete probe equation gives the off-shell identity

\[
 \operatorname{Re}(\Psi^\dagger Q\mathfrak F_\Psi)
 =-v\,e_a{}^\mu C[Q]^a{}_{\mu}-v b_Q-\lambda_a{}^\mu C[Q^2]^a{}_{\mu}.   \tag{1}
\]

The defect contribution is purely imaginary under this contraction. This is an **algebraic weighted-equation identity**, not a conserved Q charge: Q and M do not commute. Native transport or selector laws outside these hypotheses need their own extra terms.

On the constraint E=C[Q], the on-shell scalar condition becomes

\[
 \mathcal A:=v(4+b_Q)+\lambda:C[Q^2]=0.                                \tag{2}
\]

At the prepared normal point `E=I, partial E=0, lambda=0`, the old `b_Q=-4` condition is its value equation. Its first derivative also requires

\[
 G_r:=\partial_r b_Q+\lambda_{a,r}{}^\mu C[Q^2]^a{}_{\mu}=0.             \tag{3}
\]

The previous saved data instead give approximately

\[
 G=(3.70443,\;3.73982,\;5.86315,\;-5.50068).
\]

Neither a third E/Psi derivative nor a second lambda derivative appears in (3). Therefore **higher derivatives alone cannot extend that entire frozen lower jet** into a solution. This is exactly the sort of additional gate that the preceding note left open; it does not invalidate its narrower pointwise checks.

The state value and first Psi derivatives can be retained. The second E/Psi derivatives and first lambda derivatives must be allowed to change while preserving all earlier equations.

## 2. Differentiate the Same Eliminated Connection

The Cartan equation is `H(E) k=-s0(E,Psi)+L(Psi)^T lambda`, with c=1 and u=0 as previously. E=I, first E jet zero and lambda zero are retained at the point. Its second derivative is

\[
 k_{,rs}=H_0^{-1}\bigl[-s_{0,rs}
       +L_{,r}^T\lambda_{,s}+L_{,s}^T\lambda_{,r}
       +L_0^T\lambda_{,rs}-H_{,rs}k_0\bigr].                           \tag{4}
\]

The terms involving first H derivatives vanish at this normal point, but **H_,rs does not**. It depends on E_,rs. The source second derivative likewise includes the coframe response and both probe-derivative bilinears. Freezing H or treating the curvature as independent prescribed data would miss these reactions.

The script derives H's coframe derivative from the full EH quadratic curvature tensor, checks it by independent variations, and retains all mixed source/selector terms in (4). The LC connection second jet is linear in E's third jet here because the first E jet vanishes. Add it to (4), rather than substituting an unrelated torsion-free curvature.

## 3. Solve the Lower and Higher Equations Together

Keep the previous M, Q, c, u, Psi value and first Psi derivatives unchanged. Unknown real Taylor coordinates are:

| Jet | Real coordinates |
| --- | ---: |
| Symmetric second E derivatives | 160 |
| Symmetric second Psi derivatives | 240 |
| First lambda derivatives | 64 |
| Symmetric second lambda derivatives | 160 |
| Fully symmetric third E derivatives | 320 |
| Fully symmetric third Psi derivatives | 480 |
| Total | 1,424 |

All mixed partials are holonomic. Ordered copies are not fitted separately. At this normal point, the following equations are jointly affine in those coordinates:

- 64 first derivatives of E-C and 16 coframe Euler equations.
- The four previously chosen zero-divergence conditions on lambda's first jet. These remain a branch choice, not a gauge or a missing normal equation.
- 96 real first derivatives of the **complete real** probe equation, including density/connection-defect derivatives.
- 160 symmetric second derivatives of E-C.
- 64 first derivatives of the coframe Euler equation.

The resulting **404-by-1,424** matrix has evaluated rank 360. The script checks that the equation map is genuinely affine and solves the unprojected system, not just a selected block. The numerical joint residual norm is `6.91e-12`; corresponding full tensor norms are approximately

| Condition | Residual norm |
| --- | ---: |
| E-C at the point | `9.1e-15` |
| Complete probe equation at the point | `5.3e-14` |
| First E-C derivative | `1.9e-12` |
| Second E-C derivative | `7.2e-12` |
| First probe-equation derivative | `4.9e-13` |
| Coframe Euler equation | `3.1e-13` |
| First coframe-Euler derivative | `2.3e-12` |

The repaired G vector in (3) has norm below `4e-13`. The Cartan equation and its derivatives through this order are supplied by the same differentiated auxiliary solution. Values above are numerical diagnostics in chosen unscaled coordinates, not certified zeros, invariant physical errors, a uniqueness result or empirical evidence.

The earlier file is preserved unchanged, and its SHA-256 is recorded in the new report. New jet coordinates are saved separately. The least-norm numerical preparation is not a physical selection principle; there remain many free jet directions. No mass eigenvalue, coupling, frame angle or Planck scale is fitted.

The report's coordinate-block ranges are zero-based and half-open. Within symmetric jets, derivative indices follow lexicographic combinations with replacement; complex coordinates list all real parts before all imaginary parts, as specified by the calculation's unpacker.

## 4. The Curvature Gap Is Closed at This Point and Order

For smooth invertible coframes, the exact implication

\[
 j_p^2(E-C)=0\ \Longrightarrow\
 j_p^2(E^T\eta E-C^T\eta C)=0
 \ \Longrightarrow\ R[g(E)]_p=R[g(C)]_p                               \tag{5}
\]

follows by the product rule and the dependence of LC curvature on the metric's second jet. Thus matching only the frame value is insufficient, but matching through the second jet suffices **at that point**. The implication is algebraic; its premise here is numerically, not interval-certifiably, achieved.

Independent checks build actual cubic E/Psi and quadratic lambda fields, recompute the LC connection, and solve the full Cartan equation at every sampled point. Finite differences of their reconstructed C check its second jet with component error about `1.42e-4` at difference step `2e-5`. Independent cross-metric and E-metric Riemann tensors differ by about `1.93e-4` in displayed components, consistent with the finite-difference accuracy. Their LC scalar curvatures are `-10.9528387` and `-10.9528256` in unscaled comparison units.

This is a **nonflat common metric jet**, not a physical curvature prediction. The scalar differs from the earlier independently chosen E jet because the free data have now been changed to meet stronger equations. It is not a determined cosmological constant, a Planck normalization, a Schwarzschild solution or a derivation of the Einstein action. The EH term was assumed in the comparison from the outset. The full connection is torsionful; (5) compares the LC curvatures of the two metric readouts, not a claim that the torsion vanishes.

Independent four-direction field differences also check the first probe and coframe-Euler derivatives. Their norm discrepancies are about `2.23e-7` and `7.37e-5`, respectively; the latter includes the numerical connection-curvature differentiation. These are distinct from the much smaller analytic-jet equation residuals.

## 5. Improved Remainders Are Still Remainders

The actual Taylor fields are not assumed on shell away from zero. Along the same normalized direction, halving radius gives:

| Radius | Norm E-C | Probe residual | Coframe Euler residual |
| --- | ---: | ---: | ---: |
| .002 | `2.59351e-6` | `2.27864e-4` | `1.11333e-3` |
| .001 | `3.24275e-7` | `5.70114e-5` | `2.78406e-4` |
| .0005 | `4.05397e-8` | `1.42586e-5` | `6.96105e-5` |

The coframe constraint now has a cubic remainder, while the probe and geometric equations have quadratic remainders. Previously they were quadratic and linear, respectively. The auxiliary Cartan equation remains solved by construction, to numerical precision. In particular, this table explicitly rules out labeling the Taylor fields as a solved spacetime.

The positive temporal probe domain survives, with the bounds updated for cubic E and quadratic lambda. Set

\[
 \delta(r)=\tfrac12\|E''\|_F r^2+\tfrac16\|E'''\|_F r^3,\qquad
 L(r)=\|\lambda'_{r,a}{}^0\|_F r+\tfrac12\|\lambda''_{rs,a}{}^0\|_F r^2.
\]

The previous inverse-coframe estimate gives

\[
 \lambda_{min}(\mathbb K^0)\ge
 (1-\delta)^4\left(1-\frac{\sqrt2\delta}{1-\delta}\right)-L(r)/\sqrt2.
\]

The selected conservative ball has radius `.03125`, coframe perturbation bound `.01766`, and temporal eigenvalue lower bound `.6977`. These are arbitrary comparison coordinates, not a physical length. This is a probe kinetic bound on these off-shell fields, not total-energy positivity, full constrained hyperbolicity, a quantum vacuum or stability proof.

## Outcome and Next Gate

The same assumed parent admits a further numerical jet prolongation after its free lower data are re-solved. The new gate (3) is met, all old normal equations are retained, and the cross metric's curvature now agrees with the independent metric **at the point and checked order**. No additional interaction or scale fit was used.

The next question is formal compatibility/constraint propagation, including third derivatives of E-C and second derivatives of the probe/coframe equations. A finite sequence of successful jets does not imply that all orders are compatible, that a formal series converges, or that full constraint-satisfying Cauchy-surface data exist. Native adjoint, gauge/readout/HC/C7 identification, physical normalization, quantum interpretation and global/boundary conditions remain open. The main paper is not updated with an existence or gravity claim.

## Reproduction

Propagation follow-through: the [temporal Cauchy-rank audit](HC_Cartan_Cauchy_Rank.md) finds that these lambda=0 data lie on a rank-degenerate temporal branch despite positive probe weights. Their frozen second scalar gate is nonzero, so the saved jet is not automatically extendable beyond its checked order. An exact Pfaffian criterion and 38 tests identify a regular nonzero-multiplier control and reprepare all point equations there; this is not yet higher-order coframe matching, spatial constraint propagation or a Cauchy solution on that new branch. The finite results above and their numerical input remain unchanged.

- [Calculation](HC_Cartan_Prolongation.py), [saved diagnostics and 1,424 jet coordinates](HC_Cartan_Prolongation.json), [40 focused tests](../scripts/qsc_audit/tests/test_hc_cartan_prolongation.py).
- `python -B analysis/HC_Cartan_Prolongation.py --output analysis/HC_Cartan_Prolongation.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_prolongation.py`

Checks include the frozen-jet obstruction and off-shell scalar identity, source/Hessian variations, holonomic jets, the complete affine system, retained lower equations, independent differentiated fields and curvature, positivity, saved-coordinate reproduction and the explicitly nonzero remainder. No package installation, TeX/PDF rebuild, release change or Git operation is introduced.
