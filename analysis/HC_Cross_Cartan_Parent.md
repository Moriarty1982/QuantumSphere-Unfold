# Odd-Cross Parent: Coframe, Cartan Equation and a Compatibility Obstruction

Date: 2026-10-17. Status: conditional first-order neutral Einstein-Cartan comparison; independent variations and an exact compatibility criterion, evaluated on the previous curved reference example. **No common field solution, native action correction or physical scale is obtained.** Main TeX/PDF unchanged.

This continues [exchange-odd cross geometry](HC_Antisymmetric_Cross_Geometry.md). The question is whether its new constitutive candidate can satisfy its constraint and the connection equation together, not just whether its readout is curved. The answer for the unchanged prepared reference jet in the comparison below is negative. A different probe branch or a different action is not excluded.

## 1. Declare the Independent Fields First

Use independent invertible real coframe E, real Lorentz connection omega, three complex **commuting** probe spinors Psi, and real multiplier **density** lambda. The lower connection omega_mu,ab is antisymmetric in a,b. Keep the previously prepared Hermitian matrix M (diagonal .6, links 4 and .7) and the additional readout Q=i(E12-E21)/2. Neither is an evaluated native C7/M16 or a physical mass assignment. The selected sector is neutral; no internal gauge equation is solved or discarded as though it had vanished on charged data.

Write v=abs(det E), e=E^{-1}, eta=diag(-1,1,1,1), K^a=beta Gamma^a and

\[
 B_\mu=-\tfrac14\omega_{\mu,ab}\Gamma^a\Gamma^b,
 \quad D_\mu\Psi=\partial_\mu\Psi+B_\mu\Psi,
 \quad C^a{}_{\mu}=\operatorname{Im}(\Psi^\dagger QK^aD_\mu\Psi).
\]

The new, explicitly assumed parent is

\[
 S=\int d^4x\left\{v(cR(E,\omega)/2-u)+\mathcal L_D
                   +\lambda_a{}^\mu(E^a{}_{\mu}-C^a{}_{\mu})\right\},       \tag{1}
\]
\[
 \mathcal L_D=-v\operatorname{Im}(\Psi^\dagger e_a{}^\mu K^aD_\mu\Psi)
                -v\operatorname{Re}(\Psi^\dagger(M\otimes\beta)\Psi).
\]

c is an arbitrary nonzero Einstein coefficient, not a derived Newton constant; u is a vacuum density. Ordinary Palatini curvature is used, with no Holst, torsion-squared, HC, selector or extra matter action added. Those changes would alter the equations below. In particular, assuming (1) is not a derivation of Einstein gravity from the native model.

Because omega is independent here, C has no direct E dependence. After imposing omega=omega_LC(E), it does depend on E and its derivatives. These are different choices of field space.

## 2. All Four Euler Equations Are Retained

The multiplier equation is E=C. The independent coframe equation is

\[
 \mathfrak F_{E,a}{}^\mu
 =\frac{\partial}{\partial E^a{}_{\mu}}
       \{v(cR/2-u)+\mathcal L_D\}+\lambda_a{}^\mu=0,                    \tag{2}
\]

at fixed omega, its first derivative, Psi and lambda. This derivative is not an already symmetrized torsion-free Dirac stress. The code differentiates the inverse coframe and volume explicitly and checks (2) independently against the density. Its scale contraction retains degrees 2 for the EH term, 4 for the vacuum/mass terms, 3 for the Dirac kinetic term, and 1 for lambda:E. C is degree zero under this **fixed-omega coframe variation**.

The probe equation uses the Hermitian density weights

\[
 \mathbb K^\mu=v\,e_a{}^\mu(I_3\otimes K^a)
                  +\lambda_a{}^\mu(Q\otimes K^a),\qquad
 W=v(M\otimes\beta).
\]

With B acting also on channel space, its complete real-action residual is

\[
 \mathfrak F_\Psi=i\mathbb K^\mu D_\mu\Psi-W\Psi
 +\frac i2\left[\partial_\mu\mathbb K^\mu
        -B_\mu^\dagger\mathbb K^\mu-\mathbb K^\mu B_\mu\right]\Psi=0.    \tag{3}
\]

Derivatives of lambda, inverse coframe and v cannot be omitted. Equation (3) retains the previous phase-current identity

\[
 \partial_\mu\{vJ_D^\mu+\lambda_a{}^\mu q^a\}=0,
 \qquad q^a=\Psi^\dagger QK^a\Psi.
\]

The remaining equation is the **independent connection equation**. Put omega=omega_LC(E)+k, with 24 real lower antisymmetric coefficients k. Up to a boundary divergence, the EH density splits into its LC density plus k^T(c H_1)k/2. H_1 is real symmetric and invertible on a nondegenerate coframe. It is not a positive energy matrix; this algebraic connection sector does not establish stability or extra propagating gravity modes.

For fixed E and Psi define the real 16-by-24 response L and Dirac source s0 by

\[
 C=C_0+Lk,\qquad C_0=C[\Psi,\omega_{LC}],\qquad
 s_0=\partial\mathcal L_D/\partial k.
\]

Then the connection and constraint equations are exactly

\[
 cH_1k+s_0-L^T\lambda=0,\qquad Lk=b,\quad b=E-C_0.                  \tag{4}
\]

The script checks the full integrated Palatini variation, including derivative-of-connection terms, rather than varying only its quadratic part with a frozen erroneous reference. It checks probe, multiplier and coframe variations of the same parent too. Test directions are independent, periodic and off shell.

## 3. Why Imposing Zero Torsion Is Already Restrictive

Define total and Q-weighted axial currents in the same frame,

\[
 A^a=\Psi^\dagger K^a\Gamma_5\Psi,\qquad
 a^a=A_Q^a=\Psi^\dagger QK^a\Gamma_5\Psi,
 \quad\Gamma_5=i\Gamma^0\Gamma^1\Gamma^2\Gamma^3.
\]

The Clifford anticommutator reduces the real Dirac connection response to these axial bilinears. At k=0, each coordinate column of the spin equation requires a relation of the form `v e_column wedge A + lambda_column wedge a=0`, with frame indices consistently lowered. Wedging with a removes lambda. If A and a are independent, **all four inverse-coframe columns would have to lie in their two-dimensional span**, contrary to full rank. Thus no multiplier can give a torsion-free solution of this independent-connection parent on such data.

The prepared reference point has independent A and a. Minimizing its spin residual over all 16 multiplier entries leaves norm `6.34317e-7` versus source norm `2.15459e-5` in the chosen component normalization. The independence argument, not a rounding-sized residual, supplies the conditional structural exclusion. This is not a no-go for the LC-restricted action, which has no independent spin equation.

This distinction has a standard precedent: [James T. Wheeler, *Sources of torsion in Poincare gauge gravity*, sections 3 and 4.3](https://arxiv.org/html/2303.14921v2) explicitly distinguishes coframe/connection choices of independent variables and derives the axial spin source of the minimally coupled Dirac field. That supports the variational method, not the new Sphaera readout or any physical interpretation of this comparison.

## 4. Allowing Torsion Does Not Automatically Repair This Jet

Eliminate k in (4), but **do not discard the null equations**:

\[
 S\lambda=cb+d,\qquad S=LH_1^{-1}L^T,\quad d=LH_1^{-1}s_0.             \tag{5}
\]

For the nonzero spacelike a case relevant here, L has rank 12, but S has rank **9**, not 12 or 16. A direct canonical derivation uses E=I and a=(0,0,0,a3). With l=lambda, S l is `a3^2/8` times

\[
 \begin{pmatrix}
 -l_{00}+l_{11}+l_{22}&l_{01}-l_{10}&l_{02}-l_{20}&l_{03}\\
 -l_{01}+l_{10}&l_{00}-l_{11}+l_{22}&-l_{12}-l_{21}&-l_{13}\\
 -l_{02}+l_{20}&-l_{12}-l_{21}&l_{00}+l_{11}-l_{22}&-l_{23}\\
 0&0&0&0
 \end{pmatrix}.                                                       \tag{6}
\]

The 3-by-3 diagonal map is invertible, the three transverse mixed entries are independent, and so are the three last-column entries. Hence rank nine. The four last-row conditions and three transverse antisymmetry conditions describe its image. This elementary matrix calculation, not a numerical rank guess, fixes the rank in this spacelike case. The implementation checks every coefficient of (6) against the gamma-matrix/Palatini calculation. Null weighted axial currents are not covered by this canonical argument.

In a general frame set P=I-a(a^T eta)/(a^T eta a) and write a coordinate coframe target X as X_frame=X E^{-1}. The image conditions are

\[
 a^T\eta X_{frame}=0,\qquad
 \operatorname{antisym}(P^T\eta X_{frame}P)=0.                          \tag{7}
\]

The same Clifford contraction gives the exact, separately checked identity

\[
 d E^{-1}=-\tfrac18\{(a^T\eta A)I-A(a^T\eta)\}.                        \tag{8}
\]

It satisfies both (7), so d is in the image of S for spacelike a. Therefore, for every nonzero c, (5) requires **b itself** to satisfy (7). Changing the Einstein coefficient cannot remove a transverse incompatibility. The independent vacuum density u does not enter the connection equation and cannot fix it either.

At the already prepared point `(.1,.02,-.03,.01)`, retaining its E, first E jet, Psi and first Psi jet:

- `a^T eta a = 5.93746e-7 > 0`, so the spacelike criterion applies.
- b passes the four row conditions but fails the transverse symmetry condition; the displayed-frame antisymmetric component norm is `.155247`.
- For a numerical orthonormal basis N of ker S, `norm(N^T b)=.001371903`, whereas `norm(N^T d)=3.75e-21`.
- The 40-by-40 saddle system has rank 33 and seven null conditions. Its least-squares residual at c=1 is `.00134825`; the resulting vector is **not a solution**.

These component norms are not physical invariant error magnitudes. The exact range criterion is established algebraically; its nonzero evaluation on the analytic reference example is numerical, not interval-certified. Independent gamma, curvature and action checks make it a resolved diagnostic obstruction, not a proof-assistant certificate. A constructed compatible right-hand-side control is solved by the same linear solver; it is not claimed to be a field solution.

Consequently even solving the probe and metric differential equations later cannot rescue **these unchanged local data** within (1): necessary connection/constraint equations already fail. One must change the probe/coframe data or the specified action, not fit a gravitational scale to this point.

## 5. The Metrically Fixed Connection Has a Different Coframe Equation

For the alternative parent restricted from the start to omega_LC(E), the correct chain rule is

\[
 \mathfrak F_E^{LC}=\mathfrak F_E
                  +(D_E\omega_{LC})^*\mathfrak F_\omega.               \tag{9}
\]

The star is the differential adjoint after integration by parts. It includes the constraint reaction `-(D_E C)^*lambda` and the Dirac connection reaction. One must not impose `F_omega=0` separately after having removed omega as an independent variable. Conversely, using (2) unchanged while assuming a metric-dependent spin connection omits (9)'s second term.

An independent periodic test varies the full LC-substituted action. The coframe derivative plus the spin-chain contribution agrees to `2.7e-9`; omitting that contribution changes this test variation by about `.000496813`. These numbers are off-shell variational checks, not a solution, damping coefficient or physical observable. The LC-restricted branch is therefore still open, with its correct normal equation now specified.

## Outcome and Next Gate

All independent equations of one explicitly chosen parent have been derived, and their variations checked. The previous curved readout example fails a sharper test than its old unchanged-probe residual: the independent connection and coframe constraint cannot be completed simultaneously on its fixed jet, even allowing torsion or rescaling c.

The next constructive task is **new Cauchy data satisfying (7)** for the first-order parent, or a solve of (3), E=C and (9) for the genuinely LC-restricted parent. It is not enough to solve a projected subsystem, drop the multiplier derivatives or reuse the old fixed-reference probe solution. Full temporal positivity, constraint propagation, metric/probe evolution, gauge/readout and native HC/C7 identification, physical normalization and global data remain necessary. None of these comparison choices is inserted as a proved result in the main paper.

## Reproduction

Constructive follow-through: [compatible local Taylor data](HC_Cartan_Compatible_Jets.md) now changes the state and its free derivatives while retaining this parent, M and Q. Its 38 checks find numerical point jets satisfying all four Euler equations and the first coframe-constraint derivative, with positive temporal probe weights. This is not Cauchy-surface data, higher-order constraint propagation or an evolved solution; the original fixed-reference obstruction above remains unchanged.

- [Calculation](HC_Cross_Cartan_Parent.py), [saved report](HC_Cross_Cartan_Parent.json) and [40 focused tests](../scripts/qsc_audit/tests/test_hc_cross_cartan_parent.py).
- `python -B analysis/HC_Cross_Cartan_Parent.py --output analysis/HC_Cross_Cartan_Parent.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cross_cartan_parent.py`

No packages installed, no TeX/PDF replacement, no release changes, and no Git operation are introduced.
