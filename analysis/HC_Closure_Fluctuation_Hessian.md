# Closed-sector fluctuations: what actually enters a determinant?

Date: 2026-10-17. Status: exact Taylor identities for the printed minimal closure functional, followed by a fully evaluated finite **comparison** Hessian. This is not a native path integral, a physical particle count or a new main-paper result.

The [induced-gravity calculation](HC_Induced_Gravity_Heat_Kernel.md) showed how additional mass-matched scalar determinants could cancel the flat vacuum coefficient without cancelling the Einstein term. This continuation asks whether the actual connection/projector/HC package already supplies such ordinary bosonic partners. The answer is not established by its field labels. A concrete quadratic reduction exposes the missing choices.

## 1. Native data and a closed background

The [retained field package](../sources/research/parts/v470/10_sphaera_and_physics.tex), `thm:variational-form` and `thm:closed-master-system`, supplies

\[
 B_\mu=iA_\mu+\kappa Hn_\mu+\eta(I-P)n_\mu,\qquad
 F_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu+[B_\mu,B_\nu],
\]

\[
 \Lambda[M,P]=\rho[M,P]^\dagger[M,P]
              +\sigma\mathfrak R_C^\dagger\mathfrak R_C,\qquad
 \mathfrak R_C=(I-P)MP+PM(I-P),
\]

and the matching penalty `lambda_H ||H-Lambda||^2`. Here `rho,sigma>=0` are closure coefficients, not a vacuum density. `M` denotes the Millennium-side operator, **not** the earlier three-channel Dirac mass matrix. This calculation uses an orthogonal projector and a finite positive Hilbert-Schmidt realization; no actual native representation is identified with the finite example.

Take constant `P0,M0` with `[M0,P0]=0`, constant fixed axis `n`, empty probe background, `A0=H0=0`. Then `Lambda0=0` and `B0=eta Q0 n` is flat, where `Q0=I-P0`. This is a source-free reference for the displayed bosonic terms, not a solved full gravitational background. A nonzero probe, a nonflat connection or a varying axis requires additional Hessian terms.

An empty Grassmann probe background gives no quadratic boson/fermion mixing: couplings such as `delta A bar(psi) psi` and `delta H bar(psi) psi` start at cubic order. The Gaussian fermion operator still needs its physical adjoint, closure constraint, mass operator and integration measure. It is not fixed by counting the bosonic coordinates below.

## 2. The HC first variation is zero

Write `P=P0+epsilon pi+...` and `M=M0+epsilon m+...`. Differentiating `P^2=P` gives

\[
 P_0\pi+\pi P_0=\pi,\qquad
 P_0\pi P_0=Q_0\pi Q_0=0.
\]

For Hermitian projector variations, `pi` is off diagonal between the two subspaces. Its real dimension is `t=2r(N-r)`, not `N^2`.

At the closed background both factors being squared in `Lambda` vanish. Therefore, irrespective of first-order `m,pi`,

\[
 \delta\Lambda=0,\qquad
 \Lambda=\epsilon^2\Lambda_2+O(\epsilon^3),\quad
 \Lambda_2=\rho C_1^\dagger C_1+\sigma R_1^\dagger R_1,
\]

\[
 C_1=[m,P_0]+[M_0,\pi],
\]

\[
 R_1=Q_0mP_0+P_0mQ_0+M_0\pi+\pi M_0
                   -2\pi M_0P_0-2P_0M_0\pi.
\]

`Lambda2` is the coefficient of `epsilon^2`, not the second derivative (which is twice that coefficient).

Two different fluctuation theories follow:

- **Independent soft HC field:** set `H=epsilon h+...`. The quadratic penalty is `epsilon^2 lambda_H ||h||^2`. There is no `h/pi` mixing from this penalty at Gaussian order. Such mixing starts at higher orders through `Lambda2`.
- **Dependent hard HC expression:** impose `H=Lambda[M,P]` before varying/integrating. Then `delta H=0`, the matching penalty vanishes identically, and `h` is not an independent Gaussian field. With a flat curvature background its HC connection contribution also does not enter `F1`.

One must not impose the second prescription and simultaneously count the first prescription's HC determinants. If the independent HC field is moreover restricted to be positive semidefinite, `H0=0` is the boundary of a cone, not the interior of an unconstrained Hermitian Gaussian integration domain. That measure needs its own treatment.

No independent HC Gaussian field does **not** mean every composite HC quantum effect vanishes. If only `H=Lambda` is imposed while off-closure projector/operator fluctuations remain in the integral, `H` starts as the composite `epsilon^2 Lambda2`; its expectation or higher-order insertions can be nonzero and require a constrained propagator and composite-operator renormalization. If exact `[M,P]=0` is imposed on every integrated configuration as well, the minimal `Lambda` vanishes identically on that domain. These are different integration prescriptions.

## 3. Exact closure also restricts the projector tangent

The hard constraint `[M,P]=0` gives `C1=0`. If `M0` is fixed and Hermitian, diagonalize its two closed blocks, with eigenvalues `a_i,d_j`. The off-diagonal tangent satisfies

\[
 (a_i-d_j)\pi_{ij}=0.
\]

Separated block spectra exclude every such tangent. Degeneracies across the blocks can retain tangents, so this is not a universal projector-freezing theorem. Allowing `m` can compensate `[M0,pi]`, but no additional spacetime kinetic action for `m` has been supplied here. Joint infinitesimal unitary conjugation, `m=i[X,M0]`, `pi=i[X,P0]`, gives `C1=0` automatically; a change of representation is not by itself a new physical mode.

For `M0=diag(0.4,1.3)`, `P0=diag(1,0)`, the two real projector tangents are both excluded by fixed-`M` hard closure. The soft comparison below deliberately retains them **off shell** to inspect the fluctuation operator. It is not the already constrained native spectrum.

## 4. A full constant-background comparison Hessian

The printed Lorentzian curvature action has `Tr(F F)`, without a dagger. Its ordinary-Hermitian real-form ambiguity was diagnosed in the [null-axis action analysis](HC_Null_Axis_Action_Check.md). We do not silently turn that expression into a positive Euclidean path integral.

For an explicitly different, calculable comparison, take

\[
 S_{E,B}=\int d^4x\left[\frac14\operatorname{Tr}F_{\mu\nu}^\dagger F_{\mu\nu}
                  +\lambda_H\|H-\Lambda\|^2\right],
\]

with ordinary Hermitian `A,H,P`, finite `U(N)` covariance, constant **real Euclidean** `n`, and independent unconstrained `H`. This real axis is not an admissible Wick rotation derived from the native real Lorentz-null axis. `M` must transform as a spurion if it is to preserve the full unitary covariance. A fixed noncentral `M` restricts the actual symmetry group; the quadratic curvature/matching identities below can have more symmetry than the complete constrained theory.

Keep the background `eta Q0 n`; dropping it would lose necessary lower-derivative connection/projector terms. At linear order set

\[
 u=\kappa h-\eta\pi,\quad C=i[Q_0,\,\cdot\,],\quad
 f_{\mu\nu}=\partial_\mu a_\nu-\partial_\nu a_\mu,
\]

\[
 d_\mu=\partial_\mu u-\eta C a_\mu,\qquad
 X_{\mu\nu}=n_\nu d_\mu-n_\mu d_\nu,\qquad
 F_1=i f+X.
\]

For real fields, `f,X` are Hermitian; the traced real cross term between `i f` and `X` vanishes in the dagger norm. In Fourier variables `partial_mu -> i k_mu`, with a trace-orthonormal Hermitian color basis and an orthonormal projector-tangent basis, this gives

\[
 S^{(2)}=\frac12 z^\dagger\mathcal H(k)z,
\]

\[
 \boxed{\mathcal H=F^\dagger F+X^\dagger X
              +2\lambda_H\Pi_h+\zeta^{-1}G^\dagger G},\qquad
 Gz=i k^\mu a_\mu.
\]

`F,X,G` here denote their finite linear maps, and `Pi_h` selects the HC coordinates. The last term is Lorenz gauge fixing, `zeta>0`. This retains **all** constant-background terms of the stated comparison, not just a diagonal principal ansatz. At `N=2,r=1`, it is a `22 x 22` matrix: sixteen connection, four HC and two projector coordinates. None is yet a physical on-shell mode count.

The curvature-only quadratic gauge directions are

\[
 \delta a_\mu=-i k_\mu e,\qquad \delta h=0,\qquad\delta\pi=C e.
\]

They give `f=X=0` and are exact null directions of the ungauge-fixed Hessian. Their gauge-condition variation is `delta G=k^2 e`, hence the comparison's complex Faddeev-Popov ghost operator is `k^2 I`. The omitted `-eta C a_mu` term is essential for this identity. With hard fixed-`M` closure, only gauge variations preserving that additional data are admissible.

An independent check evaluates the full nonlinear curvature and the exact minimal matching target along exact unitary projector paths, with noncommuting projector derivatives retained by a block matrix exponential. For complex Fourier amplitudes, the real-field phase average obeys `4 <S(epsilon)>/epsilon^2 -> z^dagger H z`. The example errors at `epsilon=(0.04,0.02,0.01)` are `(3.41750e-4,8.54399e-5,2.13601e-5)`, showing quadratic convergence. The quadratic gauge-null error is `5.46e-16`.

## 5. Gauge fixing does not supply an elliptic four-dimensional HC spectrum

The load derivative has the scalar factor

\[
 q(k)=|n|^2|k|^2-(n\cdot k)^2.
\]

It vanishes for every momentum parallel to `n`. At generic nonparallel momentum, the example's gauge-fixed Hessian has rank 22, but its principal part has rank 20: `h,pi` enter its highest derivatives only through `u`. At parallel momentum the **full** gauge-fixed Hessian has rank 20, leaving the two projector directions null. Positive `lambda_H` does not supply a projector derivative along the axis. Changing `zeta` does not remove these null directions.

There is a stronger independent-HC test that does not rely on projector counting. Take a central HC fluctuation `h proportional to I`. It commutes with all background color matrices and is orthogonal to the projector tangents. Its eigenvalue is

\[
 \kappa^2 q(k)+2\lambda_H.
\]

For arbitrarily large momentum parallel to the axis, it remains `2 lambda_H`. More generally its eigenvalue is independent of the parallel component for **every fixed transverse momentum**, not just on a measure-zero ray. The four-dimensional heat trace therefore factorizes into a transverse heat integral and `int dk_parallel exp(-2s lambda_H)`, which diverges for every positive `s` before any usual small-`s` heat asymptotics. The algebraic penalty is not an ultraviolet regulator for the missing derivative direction. A constrained or auxiliary-field reduction could change which determinants should be formed; that is precisely why this raw Hessian cannot yet be treated as ordinary four-dimensional scalar partners.

For illustration only, freezing the connection and selecting one tangent component gives the `h,pi` block

\[
 \begin{pmatrix}\kappa^2q+2\lambda_H&-\kappa\eta q\\
 -\kappa\eta q&\eta^2q\end{pmatrix}.
\]

Its determinant is `2 lambda_H eta^2 q`, not the product of two independent relativistic scalar propagators. Eliminating `h` gives `eta^2 q (2 lambda_H)/(kappa^2 q+2 lambda_H)`, approaching a constant at large transverse `q`. This is a subblock identity, not elimination of the full coupled constrained system or a separate native particle law.

The Lorentzian null-axis principal tensor examined earlier is also degenerate, but it is a different signature problem. Neither the real Euclidean comparison nor its failure establishes a universal no-go for every background, allowed real form or extended native quantization.

## 6. Ordinary gauge bosons are not interchangeable with scalar partners

Even the standard free Maxwell sector requires the gauge determinant. In four Euclidean dimensions, Lorenz/Feynman gauge gives

\[
 \Gamma_{E,\rm Maxwell}=\tfrac12\operatorname{Tr}\log\Delta_1
                      -\operatorname{Tr}\log\Delta_0,
\]

where the second term is the complex FP ghost. Thus the heat trace is the vector trace minus **two** real scalar traces. On a curved torsion-free metric, `Delta1=-nabla^2 I+Ric` and `Delta0=-nabla^2`. Their combined coefficients are

\[
 a_0=4-2=2,\qquad
 a_2=(4/6-1)R-2R/6=-2R/3.
\]

These coefficients agree with [Visser, Table 1, massless spin 1](https://arxiv.org/html/gr-qc/0204062v1). This is a standard free-field negative control, not the determinant of the native resonance/HC connection.

One massless Dirac plus two massless Maxwell fields therefore has zero flat vacuum weight, `4-2(2)=0`, but

\[
 A=\frac{I}{32\pi^2}\left(\frac13-2\frac23\right)
   =-\frac{I}{32\pi^2}<0.
\]

So simply replacing the previous four scalar partners by two gauge bosons reverses the desired Einstein sign. For massive native Dirac modes, massless gauge modes do not even give exact proper-time mass matching. Other field content, backgrounds, masses or nonminimal terms can change this result; it is not an exclusion of gauge-mediated gravity in general.

## 7. Result and next gate

We now have a concrete quadratic operator, checked against an independently varied finite action, together with exact native minimal-closure Taylor identities. They show why the earlier twelve-scalar comparison cannot yet be assigned to the native bosonic fields:

- Hard HC matching removes the independent HC Gaussian variation on the closed background.
- Hard fixed-`M` closure can also remove projector tangents when block spectra are separated.
- Keeping independent soft fields instead gives a constrained, anisotropic coupled operator, not the assumed scalar heat kernels.
- Gauge fixing and ghosts must accompany the connection; field-component counts do not fix the Einstein sign.

The missing decision is not another free numerical coefficient. It is the native action/real-form/integration prescription: which variables fluctuate, which constraints are solved or enforced in the measure, which background is allowed, and which operator actually possesses a controlled spectral or causal determinant. Only after that can the `W0/B2` vacuum conditions be evaluated natively. No new kinetic term, twelve-scalar extension or physical Newton prediction is adopted here.

## Reproduction

The subsequent [hard-closure transport analysis](HC_Hard_Closure_Transport.md) follows the dependent-HC reading and derives the missing full-master invariance conditions. A compatible moving-projector connection gives an exact reduced probe dictionary and a local source-free family with the same projector but different internal curvatures. Its orientation curvature starts at quartic action order around constant P. It supplies neither an independent HC determinant nor the native metric/measure/connection-selection law.

Run `python -B analysis/HC_Closure_Fluctuation_Hessian.py --output analysis/HC_Closure_Fluctuation_Hessian.json`. The finite example is not an evaluated `C7/M16` representation. Thirty-eight tests in `scripts/qsc_audit/tests/test_hc_closure_fluctuation_hessian.py` cover the constrained Taylor expansion, nonlinear action check, gauge/ghost identities, principal and full ranks, central-HC heat obstruction and ordinary-gauge negative control. The main TeX, open OP5 note and PDF remain unchanged.
