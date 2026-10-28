# A shared flat reference with a relational clock and causal test signals

Date: 2026-10-27. Conditional analytical model and exact rank obstruction. This is not a native SRT derivation, a coupled gravitational solution, or OP5 closure.

## 1. Declared geometric input

Use the proposed symmetric two-probe readout with constant Hermitian K^a and D=partial:

 E^a_mu=Re(A^dagger K^a partial_mu B+B^dagger K^a partial_mu A)/2
       =partial_mu Y^a,  Y^a=Re(A^dagger K^a B)/2.

Assume det(dY) is nonzero on a patch. Then g=eta_ab dY^a dY^b is flat on that patch, eta=diag(-1,1,1,1). This assumes the Lorentz form and nondegeneracy; it does not derive them. No particular native background is claimed. The earlier HC_Background_Coframe_Origin example supplies a conditional rank-four cross-readout but evolves its source fields with a separately specified reference Dirac operator; its causal cone must not silently be identified with g.

Use units c=hbar=1 below. Y0 is the time coordinate of this flat comparison. Independent scalar phases applied to only one probe need not preserve E; a common scalar phase does preserve the symmetric E under these hypotheses.

## 2. An operational comparison clock

Place a test clock at fixed spatial Y. Its proper time is tau=Y0. Take a coherent two-level internal state

 |psi(tau)>=(exp(-i E1 tau)|1>+exp(-i E2 tau)|2>)/sqrt(2), E2!=E1.

The interference observable O=|1><2|+|2><1| has expectation cos((E2-E1)tau). Its period is T=2pi/|E2-E1|. A diagonal mixture or a detector with no off-diagonal sensitivity would not read this clock. The two levels and their coherent measurement coupling are additional model inputs, not extracted native M16 eigenmodes.

For inertial motion Y1=vY0, |v|<1, tau=sqrt(1-v^2)Y0. The same proper-time clock has coordinate-time period T/sqrt(1-v^2). This follows from the assumed flat metric, not from a newly proved calibration law. A shift of both levels by C leaves the observed clock unchanged.

## 3. Signals use this SAME geometry

Take a scalar test signal with S_phi=-1/2 integral sqrt|g| g^{mu nu} partial_mu phi partial_nu phi. In Y coordinates its equation is (-partial_0^2+sum_i partial_i^2)phi=0. Every smooth profile phi=f(Y1-Y0) is an exact right-moving plane-front solution. Its wavefront has null normal d(Y1-Y0). A smooth profile supported for Y1-Y0<0 provides a front moving at unit speed; compact transverse localization would require a full wave packet, not this plane example.

Locally a conventional symmetric-hyperbolic Dirac test field can use Gamma^mu=e_a^mu Gamma^a, where e is the inverse of THIS coframe. Its principal null cone then agrees with g. This is a declared coupling prescription, not proof that the source probes A,B obey that same equation. In a different coordinate chart transform the operator and volume as well as the metric.

Emitter and receiver at rest with Y1=0 and Y1=L exchange such a light signal in elapsed proper time L (restore L/c in physical units). With the clock above, the travel interval is |E2-E1|L/(2pi) clock cycles. This dimensionless observable is invariant under a consistent change of length/time units Y->aY and energy units E->E/a. A physical scale change relative to fixed couplings is a different operation.

## 4. Source self-consistency: exact plane-wave obstruction

Suppose A=a exp(-ik_A.x), B=b exp(-ik_B.x) with constant spinors and constant real phase covectors. Then Z^a=A^dagger K^a B=z^a exp(-i q.x), q=k_B-k_A. Consequently

 E^a_mu=(1/2) q_mu Im(z^a exp(-i q.x)).

This is an outer product, hence rank(E)<=1 everywhere. Two single plane-wave probes cannot produce a nondegenerate four-dimensional symmetric derivative coframe, regardless of how their masses or relative phase are chosen.

More generally, take N single plane-wave modes and a constant linear combination of their symmetric cross-readouts. Every row covector lies in span{k_j-k_1: j=2,...,N}, so rank(E)<=min(4,N-1). For three modes rank is at most two. Five modes are necessary within this restricted ansatz, not sufficient. Nonconstant amplitudes, multiwave packets, connections or variable weights evade the assumptions; this is not a no-go for a triadic theory with structured fields.

A simple test clock built from two homogeneous modes is therefore compatible with a GIVEN flat geometry but cannot itself furnish its four independent coframe directions in this ansatz. The earlier polynomial-background construction is a legitimate richer candidate to examine, but must pass the common-dynamics test.

## 5. What is achieved and what is not

The common flat reference supports a consistent relational clock, null test signal and operational travel-time comparison once a rank-four readout and common metric couplings are assumed. The source generation of that reference remains unsolved here; the simplest two/three-plane-wave realization is excluded exactly. The clock/signal fields are test systems: their gravitational backreaction is not solved and they are not silently identified with A,B. Native projector/gauge equations, time orientation selection and scale calibration remain open.

For OP5, flatness and a phase-neutral clock do not set the vacuum coefficient. A common energy shift is invisible to the isolated clock, but a volume term in an independently varied gravitational action can still affect geometry. Next required calculation: put the richer source probes, their coframe constraint and test-field coupling into one declared action, vary all source fields, and verify both their evolution and the coframe equation. Do not replace this by changing gamma matrices after solving the original reference equation.

Verification: OP5_Flat_Reference_Check.py checks a nontrivial coordinate pullback, exact null propagation, plane-wave rank algebra and the clock/offset formulas. These checks support the analytical identities above and do not certify native existence.
