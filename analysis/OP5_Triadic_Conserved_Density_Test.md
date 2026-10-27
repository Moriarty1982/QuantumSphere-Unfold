# Triadic spin balance: conserved-density test and required exchange law

2026-10-27. Conditional homogeneous probe test for the previous torsion geometry. No full native action solution.

## Original bilinear assignment fails conserved density

The previous assignment A=sqrt(2t)u_up, B=sqrt(2t)u_up, C=2sqrt(t)u_down has selected cross current Re(A^dagger B)=2t and zero total axial spin. But its total phase-current density is 8t and all spatial current components vanish. For a real symmetrized Dirac action with global common U(1) symmetry, independent metric-compatible connection and phase-invariant coframe constraint, the Ward current satisfies partial_mu(v J^mu)=0. In the witness E=I, v=1, this assignment has partial_t J0=8, not zero. Hermitian internal exchange cannot repair the total-density violation without spatial flux or additional specified charge-carrying sources. Torsion is not by itself permission to discard the density-form Ward identity.

## A constant-density triad can retain spin balance

Let N>0 be fixed and use homogeneous positive-beta probes with real amplitudes

 A=sqrt(N/2)cos(theta(t)) u_up,
 B=sqrt(N/2)sin(theta(t)) u_up,
 C=sqrt(N/2)u_down.

Then total density=N, spatial current=0 and total axial spin=0 for every theta. The selected A/B cross time component is

 j_S0=(N/4)sin(2theta).

To realize the specific geometric target j_S0=2t, choose on 0<t<N/8

 theta(t)=(1/2)arcsin(8t/N),
 theta_dot=(4/N)/sqrt(1-(8t/N)^2).

This is an inverse construction of a required trajectory, NOT a dynamically selected law. The bound j_S0<=N/4 follows from the amplitude norm and shows that this fixed-N homogeneous realization cannot extend to arbitrary positive t. The derivative diverges at the endpoint for this chosen branch; no continuation is claimed there.

A Hermitian effective rest Hamiltonian with A/B block theta_dot sigma_y and zero third-channel generator produces the real rotation exactly, up to any common phase. This establishes algebraic compatibility with unitary exchange and conserved density. Its time-dependent coupling has been solved for, not extracted from native M16 or T, and it is not yet the fully varied geometric Dirac equation. A common positive rest energy may be added without altering bilinears, but it contributes to stress and cannot be ignored in a full solution.

## Fixed-coupling negative control

If the exchange strength is a fixed g and theta=gt, then j_S0=(N/4)sin(2gt). Matching its initial slope to 2 requires g=4/N. The target is then

 j_S0=2t-(64/(3N^2))t^3+O(t^5),

not 2t on an interval. For spatially homogeneous j, E0=(1/2) d j_S0 under the chosen compatible connection; in the earlier E0=dt, omega^0_i=dxi/t witness, this would give E0=cos(8t/N)dt and also change the spatial coframe relation unless omega is re-solved. The fixed-connection geometric witness therefore cannot simply be retained with this altered clock.

## Interpretation

The naive amplitude-growing triad is ruled out by the total-current equation. A conserved-density spin-balanced triad exists and can match the target for a finite interval, but only with a prescribed exchange profile in this inverse construction. This narrows the dynamical question to whether the native common action generates that profile or a different self-consistent geometry/current pair. Energy/stress, the connection equation, multiplier reaction and native projector representation remain uncomputed for this trajectory. OP5 remains open.
