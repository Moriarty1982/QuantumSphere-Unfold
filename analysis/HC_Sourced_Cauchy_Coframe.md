# Sourced Cauchy Data: Full Coframe Rank Is Not Yet Curvature

Date: 2026-10-17. Status: a local analytic Maxwell--Dirac comparison, exact polynomial Cauchy/Taylor checks, and a coframe flatness result. Not a native C7 solution, a gravitational field equation, or a continuation of the previous curved Hopf-flux sector. Main TeX/PDF unchanged.

This follows the [full-triad geometry/readout audit](HC_Gauge_Invariant_Geometry_Readouts.md). Its stationary single-polarization solution had real coframe rank at most one. The following construction shows that this **rank defect is ansatz-dependent**, without mistaking a full-rank replacement ansatz for the missing same-induced-frame solution.

## 1. Declare the Changed Comparison

Use flat reference coordinates `(t,x,y,z)`, eta=diag(-1,1,1,1), the already used ordinary-adjoint real symmetric Dirac comparison, and three internal probe channels. Retain the prepared Hermitian matrix

\[
 M=\begin{pmatrix}3/5&0&4\\0&3/5&7/10\\4&7/10&3/5\end{pmatrix}.
\]

These are dimensionless comparison coefficients, not identified masses, observer-frame values or entries of native M16. Let `P=I3`, eliminate the hard-dependent `H=Lambda=0` before variation, and gauge only the common U(1):

\[
 B_\mu=ia_\mu I_3,\qquad a_0=0,\qquad
 \kappa_g=g_{\rm full}^2/3=16/75.
\]

The factor three follows from `Tr_3(f I3)^dagger(f I3)=3|f|^2`, as in the [separated-factor source equation](HC_Triadic_Gauge_Factorization.md). The matter source is the channel sum, not an average. This is a smaller varied gauge algebra, not the full U(3) equation with its off-diagonal sources suppressed.

Write `Psi` as an internal-by-spin matrix, beta=diag(1,1,-1,-1), and alpha_i for the previous Hermitian Dirac velocity matrices. Define

\[
 \rho=\langle\Psi,\Psi\rangle,\quad
 j_i=\langle\Psi,\Psi\alpha_i^T\rangle,\quad
 \mathcal E_i=f_{0i}=\partial_ta_i.
\]

All currents here are real channel-summed classical bilinears. The flat-reference equations are

\[
 \partial_t\Psi=-\sum_i(\partial_i\Psi+ia_i\Psi)\alpha_i^T
                  -iM\Psi\beta^T=:L(a)\Psi,
                                                        \tag{1}
\]
\[
 \partial_t a_i=\mathcal E_i,\qquad
 \partial_t\mathcal E_i=\Delta a_i-\partial_i(\partial_ka_k)-\kappa_g j_i,
 \qquad \partial_i\mathcal E_i=\kappa_g\rho.              \tag{2}
\]

They have the same sign convention as `partial^mu f_mu,nu=kappa_g j_nu`, with lowered `j_0=-rho`. The reference spin connection is zero. No external compensating charge or hand-chosen time derivative is inserted. The global S2/Hopf topology and its flux condition have been changed, not solved away; this example addresses the local rank question only.

## 2. Analytic Initial Data Satisfying Gauss

For `r^2=x^2+y^2+z^2`, prescribe

\[
 \Psi(0,\mathbf x)=
 \begin{pmatrix}1&0&z/2&-(x+iy)/2\\0&0&0&0\\0&0&0&0\end{pmatrix},
 \qquad a_i(0,\mathbf x)=0,
\]
\[
 \mathcal E_i(0,\mathbf x)
 =\kappa_g x_i\left(\frac13+\frac{r^2}{20}\right).        \tag{3}
\]

Direct contraction and differentiation give

\[
 j^a(0,\mathbf x)=(1+r^2/4,-x,-y,z),\qquad
 \operatorname{div}\boldsymbol{\mathcal E}
 =\kappa_g(1+r^2/4)=\kappa_g\rho.
\]

Thus (3) satisfies the nonzero charge constraint exactly. A vanishing initial potential does **not** mean a vanishing electromagnetic field: its time derivative is nonzero away from the spatial origin. The current is future timelike on `r<2` because

\[
 \rho^2-|\mathbf j|^2=(1-r^2/4)^2>0.
\]

The mixing matrix is retained dynamically. The third channel appears at first time order, and the initially empty second channel has coefficient `Psi_2(t,x)=-7t^2 s/5+O(t^3)`, with `s` the initial first-channel spinor. This is not a stationary eigenchannel or an incoherent mixture. Polynomial spatial data are used locally; they are not claimed to have finite energy over all of R3.

## 3. Why Actual Local Solutions Exist

After splitting Psi into real and imaginary parts, (1)--(2) are real-analytic polynomial equations. To use an analytic existence theorem with the derivative orders displayed correctly, prolong them to

\[
 a_{tt}=\Delta a-\nabla\operatorname{div}a-\kappa_g\mathbf j(\Psi),
\]
\[
 \Psi_{tt}=L(a)\Psi_t-i\sum_i a_{i,t}\Psi\alpha_i^T.      \tag{4}
\]

Every unknown is now solved for its second time derivative; other derivatives have total order at most two and time order less than two. Take initial `a_t` from (3) and `Psi_t=L(a_0)Psi_0`. The standard higher-order Cauchy--Kovalevskaya theorem therefore supplies a unique local analytic solution. This application uses the normal-form hypotheses of [Tsogtgerel Gantumur, *The Cauchy-Kovalevskaya Theorem*, Theorem 33](https://www.math.mcgill.ca/gantumur/math580f14/analytic.pdf), with complex spinor components treated as real variables.

For the first-order Dirac residual `R=Psi_t-L(a)Psi`, equation (4) gives `R_t=0`. Since `R(0,x)=0`, the prolonged solution solves (1). Hermitian M and a real common potential give `rho_t+div j=0`. Consequently

\[
 \partial_t(\operatorname{div}\boldsymbol{\mathcal E}-\kappa_g\rho)
 =-\kappa_g(\operatorname{div}\mathbf j+\rho_t)=0,
\]

so Gauss propagates too. This proves local analytic existence for the **declared comparison**; it gives neither a global solution nor a numerical lifetime or stability bound. The finite cubic Taylor polynomial checked by the script is a jet of that solution, not itself an exact solution for nonzero time.

## 4. The Original Real Coframe Can Have Full Rank

Keep the full real bilinear functional, with no cross selector, imaginary-part substitution or added background in its definition:

\[
 E^a{}_{\mu}=\operatorname{Re}\langle\Psi,
                  (\partial_\mu+ia_\mu)\Psi(K^a)^T\rangle,
 \quad K^0=I,\quad K^i=\alpha_i.
\]

Use the time derivative fixed by (1). At `t=0` it gives, with `m=M_11=3/5`,

\[
 E=\begin{pmatrix}
 1/2&x/4&y/4&z/4\\
 -x/4+my&-1/2&0&0\\
 -y/4-mx&0&-1/2&0\\
 z/4&0&0&1/2
 \end{pmatrix},\qquad
 \det E=\frac1{16}\left(1-\frac{r^2}{4}\right).           \tag{5}
\]

The determinant is strictly positive on `r<2`. Continuity of the analytic solution preserves full rank in a spacetime neighborhood of each initial point in that ball. At the origin, `E=(1/2)diag(1,-1,-1,1)` and `g[E]=eta/4`. Two spatial sign reversals preserve the coframe orientation and the reference time orientation at this point. This is an on-shell local-reference rank construction, not an arbitrary off-shell point-jet fit.

## 5. The Resulting Metric Is Nevertheless Locally Flat

The K matrices are constant Hermitian matrices and the common internal transport is anti-Hermitian and commutes with them. Therefore, **for any smooth probe in this flat-reference comparison**, even without using (1),

\[
 E^a{}_{\mu}=\frac12\partial_\mu j^a.                    \tag{6}
\]

The gauge term is purely imaginary in this contraction. The same algebraic identity holds for any factorized internal anti-Hermitian connection commuting with the constant K matrices; that broader identity does not assert a solution of a broader gauge-source equation. Wherever (5), or its evolved counterpart, is invertible, the inverse function theorem makes `Y^a=j^a/2` local coordinates. Equation (6) then reads `E^a=dY^a`, so

\[
 g[E]=\eta_{ab}\,dY^a dY^b,\qquad \operatorname{Riem}[g[E]]=0.
\]

This is exact local flatness, not an inference from small numerical curvature. The code separately reconstructs the torsion-free spin connection and curvature from the full coframe two-jet at the origin, obtaining spin norm zero and curvature norm about `5.2e-15`. Nonzero gauge curvature away from the origin does not change (6). More common internal phase shifts cannot create the missing non-holonomic geometry in this setting.

Rank does not establish an Einstein solution either. At the origin the reference probe stress in the declared real action is `T_00=3/5`, the electromagnetic field is zero there, and the induced Einstein tensor is zero. Simply using that reference stress as an induced Einstein source would therefore fail. A common-action induced stress law has not been derived, and no gravitational equation or cancellation source has been satisfied by showing rank four.

## 6. The Same-Induced-Frame Obstruction Remains

Now replace the flat reference coordinate gamma matrices by those of the induced inverse coframe, keeping this same probe and its derivatives. The coframe is holonomic, so its own torsion-free spin connection is zero. At the origin, direct substitution yields

\[
 R_{\rm reference}=0,\qquad
 R_{\rm induced}=(4ic+Mc)\otimes(1,0,0,0),\quad c=(1,0,0)^T,
\]
\[
 \|R_{\rm induced}\|^2=16+\|Mc\|^2=32.36,
 \qquad\operatorname{Im}(\bar\Psi R_{\rm induced})=4.     \tag{7}
\]

Thus the [previous same-frame trace obstruction](HC_Bilinear_Geometry_Bridge.md) is reproduced, not evaded. There is also a geometric check: the induced coordinate current is `J^mu=(E^-1)^mu_a j^a`. In the Y chart, `J^a=2Y^a`, hence its induced divergence is eight. Reference conservation and induced conservation are not interchangeable when their tetrads differ.

**Outcome.** Spatial spin/current structure can remove the former rank-one defect while keeping a self-sourced gauge equation. It does not, by itself, produce curved geometry or identify the probe's reference equation with the induced one. A next curved construction must specify a consistent reference/induced action relation and independently justified non-holonomic transport or HC structure, while rechecking the trace/current constraints. No such native structure, physical coefficient or gravitational completion is inferred here.

## Reproduction

The subsequent [probe-law/source and curved-geometry audit](HC_Probe_Law_Revision_Audit.md) checks whether a later source actually replaces the standing probe equation. It derives the variable-weight real-action law, constructs a curved same-coframe/spin triple kept off shell, and proves a conditional homothetic-current obstruction extending to locally phase-blind composite actions. A surviving orthogonal spectral projector can carry internal curvature without supplying the missing real coframe/current contribution. No native equation is silently updated.

- [Calculation](HC_Sourced_Cauchy_Coframe.py), [saved results](HC_Sourced_Cauchy_Coframe.json), and [tests](../scripts/qsc_audit/tests/test_hc_sourced_cauchy_coframe.py).
- Run `python -B analysis/HC_Sourced_Cauchy_Coframe.py --output analysis/HC_Sourced_Cauchy_Coframe.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_sourced_cauchy_coframe.py`.

Thirty-six regression checks cover the exact evolution/Gauss/continuity coefficients, channel mixing, gauge backreaction, determinant and current identities, holonomic two-jets, curvature and the same-induced-frame negative controls. Exact symbolic checks use the already installed SymPy, alongside the existing NumPy geometry routines. No package installation, main-text replacement, PDF rebuild or release activation is introduced.
