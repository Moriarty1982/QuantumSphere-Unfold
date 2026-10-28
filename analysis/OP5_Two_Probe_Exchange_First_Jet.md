# Two-probe Hermitian exchange: exact first-jet compatibility

2026-10-27. New conditional local compatibility result, not a neighborhood solution of the self-induced equations.

Use the conventions of OP5_Two_Complex_Probes.md. Couple two classical spinors by the real Dirac action with Hermitian internal matrix

 M=[[0,-i g],[i g,0]]=g sigma_y,
 i Gamma^mu partial_mu (A,B)^T=M(A,B)^T.

Hermiticity makes the summed phase current conserved; it does not require conservation of the cross observable used for the geometric readout. The spectrum is +/-g; no positive-energy vacuum, native mass interpretation or stability is asserted. The imaginary entries are relative coupling phases, not imaginary mass eigenvalues. g=8 below is a chosen dimensionless normalization, not a prediction.

At x=0 prescribe

 A=e1, B=0, partial_i A=0,
 partial_x B=2 alpha_x e1, partial_y B=2 alpha_y e1,
 partial_z B=2 alpha_z e1.

The evolution equations imply partial_t A=0 and partial_t B=(g-6)e1. The symmetric cross coframe at that point is therefore

 E=diag((g-6)/2,1,1,1).

For g=8, E=I. The induced inverse coframe and reference operator coincide there. Both full four-component probe equations vanish: the B equation has i Gamma^mu partial_mu B=8i e1=M_BA A, while the A equation has both sides zero. All sixteen coframe equations hold. This is an exact first-jet witness lifting the earlier FREE same-frame contradiction.

Why: for cross current Z^mu=bar A Gamma^mu B, the coupled equations give

 partial_mu Z^mu=g(bar A A-bar B B).

Thus the symmetric coframe trace at an identity frame is (g/2)(bar A A-bar B B). At the chosen point it equals g/2=4, rather than zero. Internal exchange supplies precisely the missing trace. Derivation uses the adjoint coupled equation as well as the B equation. The total phase current remains conserved. The source changes sign when the two population bilinears are exchanged, so no fixed-sign general statement is claimed.

A frozen extension is NOT a solution: keeping A=e1 and B=2(t,0,z,x+iy)^T everywhere gives E=I and solves the B equation for g=8, but the A equation becomes 0=-8i B, false away from B=0. This negative control prevents promotion of the first jet to a common spacetime solution. Letting A evolve repairs its equation but changes the coframe, so all equations must then be solved together.

The standard reference linear PDE with these initial data has its own evolution, but that fact does not prove existence for the nonlinear self-induced system. If the geometry is a constrained composite in a common action, varying that action also gives source/constraint reactions; the displayed coupled Dirac equations alone have not been proved to include those reactions. The next unresolved obligation is joint evolution and coframe consistency beyond first order, followed by full variational consistency. No OP5 closure or universal c derivation.
