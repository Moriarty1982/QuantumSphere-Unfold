# Resonance exchange closes the counterflow current gates

2026-10-27. Follow-up to OP5_Counterflow_Source_Coframe_Gate.md. Exact necessary-condition compatibility within the inverse-specified comparison model, not an on-shell solution or native OP5 closure.

## Keep the previously fitted spatial connection

Use c=cos(theta), d=sin(theta), Delta=cos(2theta)>0, theta=asin(8t/N)/2, theta_dot=4/(N Delta), n=N/(2 gamma). The previous internal connection along the local transverse spin direction has third-mode coefficients

p=3c/(2tv Delta), q=-3d/(2tv Delta).

It supplies the correct C-sector source and zero expectation correction to every coframe component. It does not by itself satisfy the separate A/B balances.

## Put the remaining exchange in Omega, not A_0

Let Y be sigma_y on the A/B flavor block and zero on C. Add a Hermitian scalar-in-spinor-space resonance term

Omega_AB=h_m Y, h_m=16 gamma/(N Delta).

Its Hamiltonian contribution is beta_D h_m Y, where beta_D is the Dirac matrix, NOT the real coefficient called beta in the manuscript's Omega formula. This distinction is essential. The term is a comparison realization of a possible triadic resonance slot, not a derivation of the native T operator.

Because A and B share the same boost, A^dagger beta_D B=ncd. Thus the resonance source contributions to the individual phase currents are

R_A=-2h_m ncd, R_B=+2h_m ncd, R_C=0.

The total sources now equal the required divergences:

3N c^2/(2t Delta)-2h_m ncd = -Ncd theta_dot+3N c^2/(2t),
-3N d^2/(2t Delta)+2h_m ncd = +Ncd theta_dot+3N d^2/(2t).

These are exact identities using cd=4t/N and c^2+d^2=1. The resonance term does not enter D_mu and hence adds no direct connection term to E. This is a statement about the retained prescribed fields; actual dynamical changes to those fields would still change E.

## Independent selected-current identity

For constant selector S_AB=S_BA=1/2 and V=A_0+alpha^i A_i+beta_D Omega, the probe equations require

partial_mu j_S^mu = i Psi^dagger [V,S] Psi.

The connection part is minus twice the contracted coframe correction, so it vanishes for the fitted connection on these fields. Since i[Y,S]=diag(1,-1,0), the resonance contribution is

h_m(A^dagger beta_D A-B^dagger beta_D B)=h_m n Delta=8.

This is exactly partial_mu(2x^mu)=8 for the prescribed cross current. Thus the same h_m obtained from the A/B density balance also satisfies the selected-current identity; no additional fitted coefficient is needed. It also shows why connection-only repair with zero coframe correction could not have worked in this restricted model.

## What has and has not been achieved

Simultaneously compatible: all three individual phase-current divergences; total phase-current conservation; the selected cross-current divergence; zero total axial spin of the prescribed fields; the full nondegenerate cross coframe E=I including its connection correction.

Still unsolved: the complete four-component probe equations (current identities are only necessary projections); derivatives of the spatial spin texture; gauge-field equations and curvature; coframe/gravitational stress equations; connection/multiplier response; and the derivation and symmetry admissibility of these coefficients from native M16/C7/T. The amplitudes and couplings are inverse engineered on a patch. Divergences near v=0, Delta=0 or other patch boundaries are not removed. Nothing here identifies a measured coupling or changes the status of the cosmological constant.

Verification: exact symbolic reduction of both individual-current residuals and h_m n Delta-8 to zero, plus the selector commutator. An initial trigonometric simplifier did not reduce an identity to literal zero; polynomial reduction modulo c^2+d^2-1 then verified it exactly. This is not a full PDE residual check or independent review. Local uncommitted note. OP5 remains open.
