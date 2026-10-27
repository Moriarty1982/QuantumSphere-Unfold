# OP5: Null transport versus operational signal locality

Date: 2026-10-27. Analytic diagnostic, not a native propagation theorem.

## Source correction

sources/research/parts/v470/10_sphaera_and_physics.tex, section Fractal Self-Traversal Along the Light Axis, defines L_n by a null condition and states KC(L_n)=L_(n-1). Its subsequent v4.9.0 status annotation explicitly says "transport open". The preceding theorem must not be treated as a completed transport proof. The global null/light-axis lemma in 15_hc_repair_and_transport.tex gives structural identification, not an explicit spacetime domain-of-dependence estimate. The readout separation lemma there also requires an explicit bridge between structural forcing, cascade identification and physical reading.

## Exact negative control

Let u and v be independent smooth solutions of (partial_t+c partial_x)u=0 and the same equation for v, with c>0. For a fixed L>0 define a purported readout

    y(t,x)=u(t,x)+v(t,x+L).

Then (partial_t+c partial_x)y=0 exactly: translation commutes with both derivatives. Thus the readout preserves the propagation equation and its characteristic direction. Nevertheless the map itself is nonlocal: y(0,0) depends on v(0,L). A compact perturbation of v near L alters this nominal output near 0 at the same time.

This is not a proposed physical faster-than-light device. It proves that preserving the null characteristic structure does not by itself establish an operationally local detector map. For an actual signal claim one must specify how the perturbation is prepared, where the detector is physically coupled, and the causal implementation of the readout. A purely mathematical nonlocal summary is not a local measurement.

## Sufficient causal composition condition

Fix a common operational spacetime, future orientation and causal relation J+. For linear response kernels, require every evolution, inter-layer transition and readout kernel K_j(x,y) to vanish unless x is in J+(y). Assuming the compositions exist, their composed kernel has the same support property: a nonzero contribution requires a chain y -> z_1 -> ... -> x, and transitivity of J+ implies x in J+(y). A point-local readout is a special case.

If distinct frames/layers carry different metrics, it is additionally necessary to supply their event maps and prove that each allowed causal link maps into the same matter-observable causal relation. Separate null sets are insufficient. The condition must include the tachyon-labelled sector; its name alone establishes neither a signal channel nor its exclusion. Infinite cascades additionally require existence and support control of the limit; finite compositions alone do not prove convergence.

This is a conditional sufficient criterion, not a derivation of these assumptions from MM/HC. A scale index n has no velocity until spatial and temporal calibration maps are provided. The numerical value of c is not derived here.

## Consequence for OP5

The information layer can be structurally prior without providing an instantaneous channel or a preferred zero of gravitational energy. Two missing bridges remain distinct: (1) causal local readout from information structure to spacetime signals; (2) a variational energy/stress readout into geometry. Proving (1) constrains admissible frame mixtures but does not determine an additive vacuum term in (2).

Next native target: extract the actual cascade map, its spacetime/event interpretation, and the matter detector coupling; check causal support for direct and intermediate-layer routes before identifying the structural null axis with a universal signal boundary.

## Follow-through: where the probe cone enters the current equations

The legacy field-equation block of 10_sphaera_and_physics.tex defines

    (i Gamma^mu D_mu-Omega)Psi=0,
    D_mu=partial_mu+i A_mu+kappa H_C n_mu+eta(1-P)n_mu,
    Omega=m0 I+alpha P M16 P+beta gY T+gamma H_C.

16_master_model.tex repeats this structure in its minimal MM/HC field equation. Under the explicit assumption that A,H_C,P,M16,T are local multiplication coefficients independent of derivatives of the evolving probe, the principal symbol of this probe equation is, up to an irrelevant scalar factor,

    Q(x,xi)=Gamma^mu(x) xi_mu.

If a Lorentzian Clifford relation {Gamma^mu,Gamma^nu}=2g^{mu nu}I has been supplied, direct multiplication yields

    Q(x,xi)^2=[g^{mu nu}xi_mu xi_nu]I.

For g^{-1}(xi,xi) nonzero this explicitly supplies the inverse Q/g^{-1}(xi,xi). For zero norm Q is nilpotent and singular. Hence the unreduced finite-dimensional probe characteristic covectors are precisely null. This is an algebraic conditional result, not yet a well-posedness or full coupled signal-support theorem.

Consequences:
- Algebraic mass, M16, triadic and HC terms cannot change this probe principal cone while Gamma is fixed. They affect lower-order dynamics.
- The displayed n_mu occurs in a multiplication term. Its being called a null/light direction does not itself generate the principal cone.
- The cone comes through the Clifford/coframe structure. A derivation of c from the information cascade must derive that structure and its operational calibration, rather than merely reuse it.
- A smooth local invertible field relabeling Psi=U chi conjugates Q to U^-1 Q U. The derivative of U gives lower-order terms. Thus such a basis/frame relabeling preserves characteristic singularity. A projection or nonlocal readout is not covered by this argument.
- A spacetime-dependent constrained projector needs a preserved constraint and a consistent restricted evolution. Compressing Gamma by P without proving this is not justified.
- If eliminated fields depend on derivatives of Psi, or Gamma/coframe is composite, the complete linearized coupled principal system must be recomputed. This probe calculation does not settle its cones or constraints.

A neutral information origin and a universal cone are therefore compatible hypotheses, but not established consequences of the current probe equation. For OP5 this also separates two tasks: fixing a causal cone cannot alone fix a derivative-free absolute vacuum term. Such a term may still affect the background geometry through the full coupled equations.

## Coframe audit and an exact scale ambiguity

The concrete Einstein-limit reconstruction in 10_sphaera_and_physics.tex explicitly defines E^a_mu=Re(barPsi Gamma^a D_mu Psi) using a fixed Clifford frame, assumes maximal rank, and sets g=E^T eta E with eta=diag(-1,1,1,1). This reconstructs metric components conditional on a chosen Lorentzian internal form; it does not derive the signature from the cascade. The subsequent effective action and derivative expansion are additional assumptions. Earlier quaternion/Minkowski passages also carry a revision annotation replacing the original reading by signature (1,6), natural norm and Reading B; the old paragraph cannot settle the physical slice selection.

Even a proved common null cone would leave the following exact ambiguity. For any smooth positive a(x), define E'=a E and g'=a^2 g. For every tangent vector v,

    g'(v,v)=a^2 g(v,v).

Consequently null vectors and causal sign classes are identical; the inverse metric yields the same characteristic covectors. But proper intervals scale by a, and in four dimensions sqrt|det g'|=a^4 sqrt|det g|. For constant a, R(g')=a^-2 R(g), so the Einstein-Hilbert density scales by a^2 while a fixed vacuum coefficient times the volume density scales by a^4. This follows directly from the inverse metric and determinant scaling; no physical symmetry of the full action is asserted. For variable a, curvature contains additional derivative terms.

Thus causal/null data alone cannot determine an absolute length/time normalization or the volume weight of a vacuum contribution. A coordinate/unit relabeling must be distinguished from a physical rescaling relative to fixed measuring systems and couplings. The family is a diagnostic of what cone data fail to distinguish, not a family of solutions of the native equations. Native coframe equations may fix or exclude members and must be solved to decide.

An information-to-matter bridge therefore needs at least (i) selection of the physical Lorentzian slice, (ii) a local causal map, (iii) an operational scale/clock calibration and (iv) a common action selecting the state and gravitational response. The repeated null-axis pattern is a candidate for (ii)'s geometry, not a replacement for (iii) or (iv). The apparent connection between fractal scale structure and OP5 should be tested at the scale-selection step, rather than assuming the photon null selects an absolute energy zero.

## Clock/scale dependency audit: concrete inherited failures

Read directly in sources/research/parts/v470/10_sphaera_and_physics.tex:

1. At line 1729 the GUE self-determination theorem is explicitly archived. Its replacement text says the claimed selection mu=gamma_L is unconfirmed, the minimum is at mu=1, and the claim is contradicted on zeros 1--2000. This note reports the manuscript's status; it does not independently rerun that numerical experiment.
2. At line 2001 the legacy probe section still says the clock scale is fixed by gamma_L* and cites that archived theorem. That citation no longer supplies a valid derivation of the clock scale. It does not prove no alternative scale derivation exists elsewhere.
3. At line 1815 the revision identifies the constants section's old photon frame as reference frame R, a pure doublet with |b|=1. The photon proper is separately identified by b=0. The old frame names must not be equated in the vacuum argument.
4. The photon-frame Planck-length revision near line 1875 says that under the counting reading both countings use the same Planck length; the gamma_L^(-3/2) conversion is unsupported by that reading. The alternatives cannot be combined silently.
5. The k(c)=0 proof at line 1855 starts with ict and names c as causal propagation speed. This addresses invariance under the declared transformations, not emergence of a finite maximal operational signal speed from the cascade.
6. The cosmological-constant corollary at line 1891 calls the photon-frame term zero while displaying a nonzero finite vacuum-density ratio gamma_L^5. If these are the same vacuum quantity in the same two frames, zero divided by nonzero cannot equal gamma_L^5. A distinction between net cosmological term and bare/cutoff density could avoid that immediate contradiction, but requires explicit definitions and a derived relation; it cannot be supplied silently by the reader.
7. r81 in 36_frame_typed_endpoint.tex explicitly says one may choose epsilon_M^len=l_P/L_ref in a Planck-compatible normalization. This is a normalization input, not by itself a scale-selection equation.

Consequence: do not initialize further OP5 work with a derived gamma_L clock, a neutral photon-reference identity, or a gamma_L-rescaled Planck cutoff unless their distinct hypotheses are restored and justified. Keep the clock calibration, reference frame R, actual photon sector and absolute vacuum coefficient separate. A dimensionless frame ratio alone also cannot supply an absolute dimensionful unit without a calibration; the meaningful physical target is a predicted dimensionless relation to a specified clock/rod or gravitational scale.

## Surviving clock rule: window selection, not a period calibration

34_mm_hc_and_c5_development.tex around line 6386 explicitly defines E_clk^win=max(0,G_req-C_gamma(tau_v)) and says timing is used only to decide whether a local relay window is available. Around line 7680 the example uses G_req=4/5 and C_gamma=1, producing zero window residual. 35_guarded_solve_chain.tex line 41 and 36_frame_typed_endpoint.tex line 331 retain local selector preservation under Delta_gamma<1/5; no global clock theorem is claimed.

An exact identification test: for any positive a, relabel tau'=a tau and define C'_gamma(tau')=C_gamma(tau'/a). At corresponding events tau'_v=a tau_v the window value and residual are exactly unchanged. Thus this isolated window criterion cannot distinguish a clock period from an a-times-longer period. This is an invariance of the criterion under jointly relabelled input/profile, not proof of a symmetry of every native equation, nor permission to change a separately fixed clock profile.

To break the ambiguity relative to another physical clock requires additional data/equations, e.g. a dynamically selected periodic state with phase phi, and a derived relation dphi/dtau_M=omega(state,couplings), where tau_M itself has an independently specified operational meaning. If a second clock exists, a dimensionless frequency ratio is a meaningful prediction. Multiplying all time units is only convention and need not be physically fixed.

Similarly a cascade step count n supplies no propagation speed without spatial and temporal readouts. For positive elapsed times Delta tau_n and distances d_n, a candidate bound d_n<=c Delta tau_n on each link implies sum d_n<=c sum Delta tau_n for a finite path (and endpoint distance no larger than path length). Null-set preservation alone supplies neither positive elapsed times nor these inequalities. A geometric zoom family d_n=d0 r^n and Delta tau_n=tau0 r^n has constant ratio d0/tau0 for every r; it illustrates compatibility of repeated scale structure and finite speed but does not select that ratio, prove the native maps, or justify an infinite cascade limit.

Scope correction: the manuscript separately calls OP5_eff closed in a detector/local sense and OP5_exact open. Current energy/frame work concerns the unresolved physical/global identification; it does not revoke the local detector result or equate its residual Phi5 with vacuum density without a bridge.

## Relational clock candidate and the energy-offset obstruction

12_structural_core.tex around lines 1622--1640 explicitly supplies ART/QFT trace differences Delta X and relative phase Delta phi, inside a hypothesis-grade two-probe interface. These are regime probes, not automatically the matter/photon/tachyon frames. The cascade itself is described as having no preferred time direction in the legacy passage at 10_sphaera_and_physics.tex line 945; that passage is not a proved causal dynamics. No elapsed time per cascade step is supplied by that assertion.

Conditional construction: suppose a physical Hermitian evolution generator H has been derived on two modes, with H|j>=E_j|j>, and prepare a coherent superposition of both. Under ordinary unitary evolution the relative amplitude phase changes by -(E_2-E_1)t/hbar. If an accessible observable has nonzero off-diagonal matrix element in this basis, its expectation can oscillate with period 2pi hbar/|E_2-E_1|. A mixture diagonal in the same basis or a detector diagonal in that basis supplies no such beat. A common phase convention and a physical interference coupling are required. This does not identify the structural M16 with H, nor derive E_j, hbar or operational t; it establishes a candidate comparison mechanism only.

For H=lambda I on a closed isolated sector, rho(t)=rho(0), and every fixed observable expectation is constant. A scalar action on the compensated sector therefore cannot by itself give an internal readable clock even if it is later identified with a Hamiltonian. Comparison to another sector can reveal relative phase. The manuscript's conditional scalar-action claim is not independently proved here and its hypotheses must not be elevated to established native dynamics.

Exact offset test: H'=H+C I gives U'(t)=exp(-iCt/hbar)U(t) for constant real C. Therefore rho'(t)=rho(t), all fixed-observable probabilities coincide, energy gaps and beat periods coincide. Adding further coherently coupled modes does not remove this invariance under a shift of the full generator by C I. A shift of only one channel is not this test and may be observable. A time-dependent scalar offset likewise supplies only a common phase in this fixed-background unitary setting.

Hence a relational clock can address relative frame/scale calibration while being incapable on its own of selecting a common absolute energy offset. This is not a claim that a vacuum term in a metric-dependent action is unobservable: its metric variation can gravitate, and changing it need not preserve the background. That common matter/geometry variation remains the essential OP5 bridge.

Next discriminating native calculation: specify the two physical probe modes and accessible interference observable; derive their generator from the native action; calculate the relative frequency and cross-bilinear coframe together; then test a common vacuum shift in the FULL varied action. Do not infer that a relational beat clock or a repeated null pattern already fixes gravitational vacuum energy.

## Common-phase test of the two oriented geometry readouts

Assume fixed Hermitian K^a (the chosen adjoint has been included in K), and D_mu=partial_mu+B_mu with B a fixed linear multiplication operator commuting with a common scalar phase. Write A and Q for the two probes and

    Z^a=A^dagger K^a Q,
    E_AQ^a_mu=Re(A^dagger K^a D_mu Q),
    E_QA^a_mu=Re(Q^dagger K^a D_mu A).

For A'=exp(i chi)A and Q'=exp(i chi)Q with real smooth chi, direct differentiation gives

    E'_AQ=E_AQ-(partial_mu chi) Im Z^a,
    E'_QA=E_QA+(partial_mu chi) Im Z^a.

Thus E_s=(E_AQ+E_QA)/2 is invariant, while E_a=(E_AQ-E_QA)/2 shifts by -(partial_mu chi)Im Z^a. This refutes the unrestricted assertion that any cross-bilinear is blind to a common phase at fixed connection. The smallest algebraic example is one-component K=1,A=1,Q=i: initial derivatives vanish, Z=i, and a varying common phase gives E'_AQ=-partial chi and E'_QA=+partial chi. This checks the transformation law, not a rank-four physical solution.

If a gauge connection is also transformed to cancel i partial chi, both oriented readouts are covariant/invariant in the appropriate common representation. This is a different operation from holding B fixed; a common energy shift is not automatically a gauge transformation of the full gravitational action.

For B=0 and constant K, E_s^a_mu=(1/2)partial_mu Re Z^a. Define Y^a=Re Z^a/2. On any rank-four patch E_s=dY, so g=eta_ab dY^a dY^b is locally Minkowski in Y coordinates. This candidate cancels the common phase but cannot realize curved gravity on that patch. Nonzero connections contribute (1/2)Re[A^dagger(KB+B^dagger K)Q]; metric-compatible cancellation in this precise K-weighted sense would again leave the exact coframe. General connections, varying weights and additional channels require their full terms and equations.

Vacuum shift distinction: for an independently varied metric, S_vac=-C integral sqrt|g| gives delta S_vac=(C/2) integral sqrt|g| g_mu_nu delta g^{mu nu}. A common phase cancellation of E does not remove this variation. In contrast, if g is constrained from the outset to the exact pullback eta_ab dY^a dY^b on a fixed-orientation nondegenerate patch, its volume density is |det dY| and its integral varies only by a boundary term under compactly supported Y variations. That restricted insensitivity comes with a locally flat metric and a restricted variation space; it is not unrestricted Einstein vacuum screening. Do not mix these two variational problems.

Result: bidirectional symmetrization is a concrete phase-neutral comparison candidate under the declared assumptions. Its elementary derivative-only realization is too restrictive for curved gravity. The open task is a derived non-exact, nondegenerate coframe and common action, preserving justified phase/gauge invariances without discarding the metric/constraint reactions. No native frame selection, vacuum value or OP5 closure follows yet.
