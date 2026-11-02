# Triadic Resonance and Gauss Compatibility

Date: 2026-10-17. Status: a conditional matrix-current compatibility theorem, a constraint-propagation counterexample, and a local hard-dependent massive eigenmode lift on the already prescribed curved product geometry. The prepared finite triadic resonance is **not** the native Millennium matrix, and no physical mass or native C7 solution is identified. Main TeX/PDF unchanged.

This follows the [massive HC continuation](HC_Massive_Soft_Closure.md) and uses the matrix Ward identity already prepared in the [real-probe/current analysis](HC_Real_Probe_Current_Closure.md). Its new step is to connect that identity to propagation of the *remaining spatial connection equation*, then check the prepared noncentral triad on the same sourced curved branch.

## 1. What the Native Text Actually Fixes

In `sources/research/parts/v470/10_sphaera_and_physics.tex`:

- `prop:closure-equation` prescribes `H_C=Lambda[M16,P]`.
- `thm:closed-master-system` includes that equality and exact residue closure, which makes the minimal H_C vanish.
- `thm:variational-form`, however, lists H_C as a field with a **finite** penalty `lambda_H ||H_C-Lambda||^2` and states an exact Euler-equation equivalence. The finite penalty does not by itself establish the algebraic equality: kinetic and probe-source variations also enter.
- The subsequent compensator interpretation calls it an energetic penalty, not an independent interaction. This supports examining the dependent reading; it is not a derivation of the asserted variational equivalence.

The present lift therefore explicitly uses the **hard-dependent comparison domain**, eliminating H_C=Lambda=0 before variation. It does not impose the independent soft-HC equation as well. The main text's domain/action issue remains unresolved, not hidden by selecting a convenient branch.

## 2. Fixed Noncentral Resonance Adds a Matrix Condition

Use the same ordinary spin adjoint and real symmetric probe action, with a Hermitian internal resonance Omega. Let

\[
 j^\mu=\Psi(K^\mu)^T\Psi^\dagger,\qquad
 S=\Psi\beta^T\Psi^\dagger,\qquad B^u=iA.
\]

The Dirac equation and its adjoint give the already prepared identity

\[
 D^u_\mu j^\mu=-i[\Omega,S].                 \tag{1}
\]

This is internal matrix-charge exchange, not disappearance of total probability: its ordinary trace is zero. The scalar resonance of the previous branch made the commutator vanish automatically.

For a *full unitary matrix* source equation without further adjoint-field currents,

\[
 D_u^\mu G_{\mu\nu}=ig^2j_\nu,
\]

the double covariant divergence of its left side vanishes. Antisymmetry of G and the curvature commutator identity give this on the prescribed torsion-free metric; the Ricci contractions vanish as well. Thus (1) requires

\[
 [\Omega,S]=0.                              \tag{2}
\]

This is **not** a no-go for every native triadic coupling. A smaller gauge algebra sees only its projected current. Alternatively, dynamical resonance/projector/compensator fields may carry a compensating adjoint current. That current and its divergence must be obtained from the same typed action. The paper's displayed scalar trace-gradient currents do not yet specify this matrix balance. Merely assigning a transformation law to a fixed background is not an equation supplying its missing reaction.

A fixed noncentral resonance also limits the actual local gauge symmetry to its stabilizer unless it is supplied with an appropriate covariant background/dynamical-field treatment. Solving full matrix connection equations in the comparison does not by itself construct a gauge-invariant native U(6) theory.

## 3. Explicit Propagation Test

Keep three real generation amplitudes U(z), V(z), a real symmetric matrix A(z), and

\[
 \psi=e^{-i\omega t}(0,U,0,iV),\qquad
 B^u_t=iA,\qquad B^u_z=0.
\]

The same angular polarization can subsequently be lifted onto the sphere. Here define

\[
 \rho=UU^T+VV^T,\quad S=UU^T-VV^T,\quad
 W=UV^T-VU^T.
\]

Independent spinor bilinears give `j^t=rho`, `j^z=iW`, with no angular current. Dirac plus the temporal connection equation give

\[
 U'=(\omega I-A+\Omega)V,\quad
 V'=(\Omega-\omega I+A)U,\quad
 A''=-g^2\rho.                              \tag{3}
\]

The **spatial** connection equation is a separate constraint,

\[
 C:=[A,A']-g^2W=0.                          \tag{4}
\]

It is not legitimate to stop after solving (3). Direct differentiation gives

\[
 W'=-[A,\rho]-[\Omega,S],\qquad
 C'=[A,A'']-g^2W'=g^2[\Omega,S].            \tag{5}
\]

Equations (2) and (5) describe the same compatibility gate. Conversely, if the torque vanishes **throughout an interval** and C vanishes initially, (5) preserves (4) along (3). Vanishing torque at just one point need not be preserved by arbitrary gauge data; a dedicated negative control checks that distinction.

For the prepared comparison

\[
 \Omega_\triangle=
 \begin{pmatrix}.6&0&4\\0&.6&.7\\4&.7&.6\end{pmatrix},
\]

take `U=(.5,0,0)`, `V=(.1,0,0)`, `A=0`, `A'=.03 I`. Initially C=0 and the matrix Dirac equation is satisfied by the first jets (3), but

\[
 \|[\Omega_\triangle,S]\|_F=1.3576450199,\qquad
 \|C'\|_F=0.8688928127.
\]

So a naive three-component extension leaves the constraint surface immediately. Its ordinary trace current is nevertheless conserved. Applying the same unitary basis change to Omega and S changes neither commutator norm nor this conclusion.

## 4. A Compatible State with the Third Component Retained

Let `r=sqrt(16.49)`. The eigenvalues of the **given** finite matrix are `.6-r`, `.6`, `.6+r`; no absolute-value replacement of the negative eigenvalue is performed. Select the positive upper branch

\[
 m_+=.6+r=4.6607881008,\qquad
 e_+=\frac1{\sqrt2}(4/r,\ .7/r,\ 1)^T,\qquad q=e_+e_+^T.
\]

This vector has squared component weights approximately `(0.48514251,0.01485749,0.5)`. Both prepared couplings and the third component enter. It is nonetheless **one eigenmode**, not three independently populated mass eigenstates or a demonstration of generic flavor conversion, frame tunnelling or a derived physical spectrum.

Choose `U=u e_+`, `V=v e_+`, `A=a q`. All matrices stay in the same commuting algebra, so W=C=[Omega,S]=0 identically. System (3) then reduces exactly to the previous hard massive equations with `m=m_+`:

\[
 u'=(\omega-a+m_+)v,\quad
 v'=(m_+-\omega+a)u,\quad a''=-g^2(u^2+v^2).
\]

On the already assumed `R1,1 x S2_R` product geometry use

\[
 P=P_{\rm Hopf}\otimes I_3,\quad
 B^u=B_{\rm geom}\otimes I_3+i a P_{\rm Hopf}\otimes q\,dt,
\]
\[
 \Psi=(V_N\otimes e_+)e^{-i\omega t-i\phi/2}(0,u,0,iv),
 \qquad \Omega=I_2\otimes\Omega_\triangle.
\]

The six-dimensional comparison projector has rank three. The full connection retains `eta(I-P)n`, but `D^u P=0`, H_C=0 and constant closed n make its extra curvature and its action on the probe vanish. The angular spin connection is retained. The geometric curvature is source-free; the longitudinal curvature balances the same probe's nonzero charge. All these matrices also commute with the fixed resonance, so the solution lies in its stabilizer algebra.

The new eigenvalue is not covered by the previous m=.6 existence box. For reference initial data `(u,v,a,a')=(.5,.1,0,.03)`, omega=.9 and g=.8, a separate box of radius .1 gives component bounds

\[
 (1.1321576202,\ 2.3164728605,\ .13,\ .256),
\]

and Jacobian infinity-norm bound `5.8607881009`. On `|z|<=.03`, the Picard map stays within the box (displacement at most `.06949419<.1`) and is a contraction (at most `.17582365<1`). Thus there is a unique local analytic comparison solution in that box. These are explicit analytic bounds, not a proof-assistant or outward-rounded interval-arithmetic certificate. They do not assert a physical length or a global continuation.

Independent full-matrix checks at `(t,theta,phi,z)=(.4,.9,.4,.02)` give approximately:

- Spin-covariant massive Dirac residual: `1.1e-15`.
- All sourced connection components: `2.3e-10` (centered coordinate differences).
- Matrix-current/Ward residual: `3.5e-12`.

The algebraic reduction and Picard argument establish the conditional local result; small finite residuals are consistency checks, not its replacement. No independent soft-HC equation, global finite-energy boundary condition or metric equation is claimed solved. This comparison's source phase and real/dagger action choices remain distinct from the untyped printed complex equation.

## 5. A Separate Sector Gate: Where Is the Third Component?

The lift admits the full C3 generation carrier in P. This is an assumption, **not** a result identifying the native C7 sector. The main text calls the third triadic component orthogonal but does not thereby establish whether it is outside C7. The earlier [hard-transport analysis](HC_Hard_Closure_Transport.md) requires `Q Omega P=0` for preservation of *all* admitted probes, separately from (2).

If instead the third component is excluded by `P_vis=diag(1,1,0)`, the prepared comparison gives

\[
 Q_{\rm vis}\Omega_\triangle P_{\rm vis}
 =\begin{pmatrix}0&0&0\\0&0&0\\4&.7&0\end{pmatrix},
 \qquad \|Q_{\rm vis}\Omega_\triangle P_{\rm vis}\|_F=\sqrt{16.49}.
\]

The selected positive eigenmode then has **one half of its norm outside** the admitted sector and is not a closed probe. The single dark vector `(-.7,4,0)/sqrt(16.49)` is an eigenvector with eigenvalue .6 and zero third component. Its one-dimensional projector commutes with the resonance. This protects that one state, not the entire two-component P_vis: global projector invariance still fails.

No inference about the actual minimal `Lambda[M16,P]` is made by replacing M16 with this prepared resonance matrix. The two tests are independent: a scalar M16 may preserve P while a separate triadic T leaks out of it. A native identification must therefore pass *both* the sector test `Q Omega P=0` and the properly typed source/Ward test. The present positive-eigenmode lift passes them only on its declared larger carrier.

## 6. What This Adds and What Remains

The hard massive branch survives the prepared triadic resonance in a common eigenmode on the prescribed curved background. Generic coherent states cannot be imported without checking the additional matrix-charge balance. Exact M16/P closure alone does not establish (2): block preservation across P is different from commutation with S **inside** the closed sector.

Three structurally possible next routes are now distinguishable: evaluate the actual native state in (2); identify a smaller gauge algebra and its projected currents; or derive the additional dynamical matrix current that balances the torque. For a fixed Hermitian Omega, projection onto its stabilizer kills `[Omega,S]` while retaining within-degenerate-eigenspace coherence. This is a change/specification of the gauge algebra, not an automatic repair of the full-source equations. The native carrier, M16/T coefficients and field domain must decide which route is justified.

The product metric, Hopf carrier, finite triad, gauge normalization and local spin patch remain declared comparison data. Neither a self-sourced spacetime metric, physical masses, temporal stability nor an OP5 closure certificate follows.

## Reproduction

- [Calculation](HC_Triadic_Gauss_Compatibility.py) and [saved results](HC_Triadic_Gauss_Compatibility.json).
- Run `python -B analysis/HC_Triadic_Gauss_Compatibility.py --output analysis/HC_Triadic_Gauss_Compatibility.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_triadic_gauss_compatibility.py`.

Thirty focused tests check independent bilinears/Ward signs, Gauss propagation, trace-only and basis-change failures, stabilizer degeneracies, eigenmode and sector support, the new Picard box and Taylor defect, all matrix/spin jets and sourced curved equations at multiple radii. No main-TeX edit, PDF rebuild, release activation or Git operation is introduced.

The subsequent [gauge-factorization analysis](HC_Triadic_Gauge_Factorization.md) follows the source's distinction between probe channels, generations and color indices. It finds textual support for a closed whole triad and derives the intertwiner/projected-Ward criterion for a separate gauge factor. A coherent multi-eigenmode comparison then solves the smaller, action-derived gauge system with the full trace multiplicity retained; it deliberately does not solve the unprojected full-matrix equation above. Identical native channel representations and the C7 embedding remain unproved.
