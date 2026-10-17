# Triadic Probe Channels Are Not Gauge Indices

Date: 2026-10-17. Status: source-grounded architectural audit, an intertwiner criterion, and a local coherent three-channel hard-dependent comparison on the already prescribed curved product metric. The actual native gauge representation, C7 embedding and physical coefficients remain uncomputed. Main TeX/PDF unchanged.

This follows [triadic Gauss compatibility](HC_Triadic_Gauss_Compatibility.md). It does **not** invalidate the previous full-matrix-source obstruction: it identifies precisely when that source equation is stronger than the equation obtained by varying the actual gauge algebra.

## 1. What the Paper Says About the Indices

Four source passages are relevant:

1. `sources/research/parts/v470/10_sphaera_and_physics.tex`, the concrete Einstein-limit route immediately before `prop:bilinear-einstein-reconstruction`, calls the entire `(Psi_1,Psi_2,Psi_perp)` a **closed triadic probe field**, with bilinears computed inside C7. This favors allowing the third component within the closed probe architecture. Orthogonality to two probe channels does not mean orthogonality to C7.
2. `sources/research/parts/v470/12_structural_core.tex`, `thm:theorem-level-shadow-bidirectional-probe-lensing`, treats ART/QFT readouts and the third coupling channel on a common closure-stable carrier. Its stronger universal lensing law remains deferred.
3. The gauge section, `sec:gauge` and `thm:octonion-SU3`, assigns the color triplet to the octonionic factor and says the SU(3) generators act on color indices, not quaternion indices.
4. `sources/research/parts/native-operator-link.tex` explicitly distinguishes the three **probe channels** from the three **generation coordinates**. Neither is automatically a color triplet.

These are statements of the paper's architecture, not independent proofs that its field equations or physical identifications hold. They motivate a separated-factor test. They do not give the projector's matrix entries, the channel charge assignments, or an identification of the entire resonance connection with the Standard Model connection. In particular, a further genuinely gauged resonance/channel algebra would still require its own source equations.

The words `generation` in the preceding finite six-dimensional comparison name an auxiliary three-dimensional factor; they do not identify the native triadic channels with generations. Here that factor is explicitly read as **probe-channel space**.

## 2. The Relevant Ward Gate Is Representation-Dependent

The full matrix identity from the same ordinary-adjoint real probe action remains

\[
 D_\mu J^\mu=-i[\Omega,S],\qquad S=\Psi\beta^T\Psi^\dagger.
\]

For an actually gauged Hermitian generator T_a, cyclicity gives

\[
 D_\mu j_a^\mu=-i\operatorname{Tr}([T_a,\Omega]S).
                                                        \tag{1}
\]

This is the local gauge-covariant identity; connection commutators supply the usual mixing of generator components. Consequently, `[Omega,S]=0` is sufficient but is **not necessary** for a smaller algebra whose generators commute with Omega. Nonzero internal channel torque can be invisible to every *gauged* charge without violating gauge-current conservation. This is not loss of total probability, decoherence or an added compensating bath.

For a direct sum of channel representations, a fixed off-diagonal coupling must satisfy the intertwiner condition

\[
 T_i^a\Omega_{ij}=\Omega_{ij}T_j^a.                        \tag{2}
\]

For scalar U(1) charges and the nonzero prepared links `1<->perp`, `2<->perp`, this requires `q_1=q_perp=q_2`. The comparison matrix gives

\[
 \|[\operatorname{diag}(q_i),\Omega_\triangle]\|_F^2
 =2\{16(q_1-q_\perp)^2+.49(q_2-q_\perp)^2\}.
\]

Charges `(1,1,1)` pass; `(1,1,0)` give norm `5.7428216061`. A fixed neutral/charged mixing cannot simply be declared gauge invariant. Inequivalent representations need an allowed intertwiner, a suitably transforming additional field, or vanishing coupling. No native charges or extra charged fields are assigned here.

## 3. Trace Normalization Must Be Kept

Use the declared internal carrier

\[
 V=\mathbb C^2_{g}\otimes\mathbb C^3_{\rm channel},\quad
 P=P_{\rm Hopf}\otimes I_3,\quad
 B^u=B_g\otimes I_3,\quad
 \Omega=I_2\otimes\Omega_\triangle.
\]

This auxiliary U(2) gauge factor is **not** an identification of the native chiral electroweak representation or of its couplings. It provides a direct finite example of the separated-index possibility. An independent color factor would commute with the channel matrix for the same tensor-algebra reason.

Let `j_g=Tr_channel J`. With the unnormalized full-carrier curvature trace used in this comparison,

\[
 \operatorname{Tr}_6(F^\dagger F)=3\operatorname{Tr}_2(F_g^\dagger F_g).
\]

The matter source is a channel *sum*, not a channel average. Varying only `B_g tensor I3` in the same real symmetric probe plus dagger-curvature action therefore yields

\[
 D_g^\mu G_{g,\mu\nu}=i\frac{g_{\rm full}^2}{3}j_{g,\nu}.
                                                        \tag{3}
\]

Equivalently, the Hilbert--Schmidt projection onto the varied gauge algebra is

\[
 \Pi_g(X)=\frac13\operatorname{Tr}_{\rm channel}(X)\otimes I_3,
\]

and the *projected* full-carrier connection equation vanishes. This projection is derived from the field space, not chosen to erase a residual. The unprojected equation remains different and nonzero on the new example. With a canonically normalized two-dimensional gauge trace one would instead call `g_full/sqrt(3)` the coupling; the code retains the full trace and displays the factor three explicitly. No physical gauge normalization is derived from these numbers.

## 4. A Coherent Branch Without Single-Eigenmode Selection

Keep the same prescribed metric `-dt^2+R^2(dtheta^2+sin^2(theta)dphi^2)+dz^2`, its Levi--Civita spin connection and the same local Hopf spinor V_N. Let

\[
 B_g=B_{\rm geom}+ia(z)P_{\rm Hopf}\,dt,
\]
\[
 \Psi=(V_N\otimes\chi)e^{-i\omega t-i\phi/2},\qquad
 \chi_i=(0,U_i(z),0,iV_i(z)),\quad U_i,V_i\in\mathbb R.
\]

Use the prepared real symmetric triad with diagonal .6 and links 4,.7, explicitly not native M16. The hard-dependent comparison eliminates H_C=Lambda=0 before variation. The retained `eta(I-P)n` load has zero curvature because `D_g P_Hopf=0` and n is constant and closed; it annihilates the closed probe.

The full matrix current contains

\[
 J^t=P_{\rm Hopf}\otimes(UU^T+VV^T),\quad
 J^z=iP_{\rm Hopf}\otimes(UV^T-VU^T),
\]

but its gauged partial trace is simply `j_g^t=(|U|^2+|V|^2)P_Hopf`, `j_g^z=0`. Independent angular spin transport still cancels as in the preceding branch. The Dirac equation and **all** projected connection components reduce to

\[
 U'=[(\omega-a)I+\Omega_\triangle]V,\quad
 V'=[\Omega_\triangle-(\omega-a)I]U,
\]
\[
 a''=-\frac{g_{\rm full}^2}{3}(|U|^2+|V|^2).               \tag{4}
\]

The remaining projected spatial equation holds: its longitudinal current is zero and the electrostatic matrices commute. The nonzero unprojected channel current is not discarded from (1); it remains present in the full matrix Ward check. The same single coherent probe supplies the projected gauge source. It is not replaced by an incoherent ensemble.

For initial `(U,V,a,a')=((.5,0,0),(.1,0,0),0,.03)`, omega=.9 and g_full=.8, the first jets include `U_perp'=.4` and `V_perp'=2`. Coupling then populates the second channel as well. At z=.02 the channel densities are approximately

\[
 (.2640537667,\ 8.2385944\,10^{-8},\ .0016831342).
\]

All three **resonance eigenmode** densities are nonzero, approximately `(.12090203,.00779635,.13703861)`. Thus this is not the previous single-eigenmode branch in another basis. The signed spectrum of the given finite matrix is unchanged, including its negative eigenvalue; no physical-mass or positive-spectrum interpretation is inferred.

## 5. Local Existence and Independent Checks

For the eight-coordinate state `(U_1,U_2,U_perp,V_1,V_2,V_perp,a,a')`, use a box of coordinate radius .1 around the stated initial data. Absolute component bounds for (4) are

\[
 (.72,.23,1.03,.64,.11,2.51,.13,.0938666667).
\]

The Jacobian infinity norm is bounded by 6.4 on the whole box. For `|z|<=.03`, the Picard displacement is at most `.0753<.1` and the contraction bound is `.192<1`. The polynomial vector field therefore has a unique local analytic solution in that box. These analytic inequalities, not numerical sampling alone, support the existence statement. The tests additionally check all 256 corners, the Taylor coefficients and the installed independent mpmath solver. This is not a proof-assistant or outward-rounded interval certificate, physical length interval or global solution.

The reduced real action, up to the common sphere factor and the z-independent angular term, is

\[
 L_z=(\omega-a)(|U|^2+|V|^2)+U\cdot V'-V\cdot U'
     -U^T\Omega U+V^T\Omega V+\frac{3a'^2}{2g_{\rm full}^2}.
\]

Its spatial first integral is

\[
 I_z=-(\omega-a)(|U|^2+|V|^2)+U^T\Omega U-V^T\Omega V
       +\frac{3a'^2}{2g_{\rm full}^2}=-.087890625.
\]

It is not a temporal energy or stability theorem. Independent full probe-action and curvature-action variations verify the partial-trace source and factor three. At `(t,theta,phi,z)=(.4,.9,.4,.02)`:

- Full spin-covariant Dirac residual: `3.9e-16`.
- Projected sourced connection residual: `1.2e-10`.
- Projected current-divergence residual: `1.2e-12`.
- Full matrix Ward residual: `1.5e-9` using centered coordinate differences.

The full matrix torque norm is about `1.39539`, while its gauge projection vanishes. The deliberately retained **unprojected** connection residual is `0.13886`: the new example does not solve the stronger full-U(6) equation. No independent soft-HC equation, metric equation or omitted normal connection variation is asserted solved. The real-action/source choice is still a comparison rather than a repair silently applied to the printed complex action.

## Outcome

There is textual support for treating the third probe channel inside a common closed architecture and for separating gauge, channel and generation indices. With **identical channel representations**, this permits a coherent local sourced branch without demanding the full scalar matrix commute with the triadic resonance. It replaces an overly broad full-matrix test by the equation derived from a specified smaller gauge field space, not by a new compensating force.

The next native data needed are the maps `P_i` and `T_i^a` on the three probe channels, the actual triadic intertwiners, and the separation (or additional gauging) of the resonance algebra. The source passages do not compute those data. A common carrier alone does not prove identical charges or the tensor-product ansatz. Hard/soft action consistency, the native M16/scale/readout, a nondegenerate bilinear metric, global spin/finite-energy data and metric backreaction remain separate obligations.

## Reproduction

- [Calculation](HC_Triadic_Gauge_Factorization.py) and [saved results](HC_Triadic_Gauge_Factorization.json).
- Run `python -B analysis/HC_Triadic_Gauge_Factorization.py --output analysis/HC_Triadic_Gauge_Factorization.json`.
- Run `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_triadic_gauge_factorization.py`.

Twenty-eight focused checks include source passages, charge intertwiners, orthogonal gauge projections, full-trace/action variations, Picard bounds, independent ODE agreement, coherent mode populations, matrix jets and all projected curved equations. No main-TeX edit, PDF rebuild, package installation, release activation or Git operation is introduced.

The following [intertwiner classification](HC_Triadic_Intertwiner_Classification.md) proves when connected fixed links force equivalent channel representations. A finite root/commutant calculation distinguishes the additional fixed-label hypothesis, anisotropic or singular links, and scalar versus matrix cycle phases. It also transports this coherent solution through different local channel bases with all connection, resonance and gauge-embedding terms retained. None of the classification's fixed readout projectors is silently identified with a native readout map or C7.
