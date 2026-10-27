# Variable-amplitude transverse counterflow: a kinematic flat witness

Date: 2026-10-27. Continuation of OP5_Transverse_Triadic_Counterflow.md. Exact classical bilinear construction, NOT a solution of the native probe equations. Metric convention (-,+,+,+); cross coframe E^a = (1/2) d j_S^a; connection omega=0 in the displayed frame.

## Equal amplitudes do not suffice

For balanced transverse counterflow with equal A/B amplitudes and phase,
J^a=(N,0,0,0), j_S^0=N/4, even when N varies. If E is invertible, Y^a=j_S^a/2 are local coordinates and E^a=dY^a. Thus J=8Y^0 partial_Y0, and its metric divergence is 8, not zero. Arbitrary spatial profiles of the cross current cannot repair this identity within these assumptions. At fixed N, d j_S^0=0 already makes E singular. Fixed spin along z and boosts restricted to its transverse plane also leave j_S^z=0 and rank at most three. These are restricted-ansatz obstructions, not an OP5 no-go.

## Release the A/B amplitude ratio explicitly

Use opposite transverse velocities +v for A/B and -v for C, equal combined rest densities n for A/B and C, and opposite rest spins. Choose A/B amplitudes sqrt(n) cos(theta), sqrt(n) sin(theta), and C amplitude sqrt(n). A/B have the same phase and normalized rest spinor chi_+; C has chi_- with opposite spin. Then

J^a=(2n gamma,0),
j_S^a=(n gamma sin(2theta)/2)(1,v),
S_total^a=0.

Axial cancellation holds because the local spin direction is perpendicular to v; boosts leave these transverse axial vectors unchanged. This is pointwise even when directions vary, but derivatives then enter the unsolved probe equations.

## Explicit nondegenerate witness

Take constant N>0 on an open patch with 0<t<N/8 and |x|<t. Define

v=x/t, gamma=(1-|v|^2)^(-1/2), n=N/(2gamma),
theta=(1/2) asin(8t/N).

Choose a smooth unit spin direction s(x) perpendicular to x on a local patch, e.g. s=(-y,x,0)/sqrt(x^2+y^2) away from the z axis. Smooth normalized Pauli eigenvectors chi_+, chi_- exist after shrinking the patch. No globally regular spin texture at the origin is asserted.

Boost the above positive-energy rest spinors with the standard Lorentz spinor boosts for +v and -v. Their bilinears obey exactly

J^a=(N,0,0,0),
j_S^a=(2t,2x,2y,2z),
S_total^a=0.

Consequently E^a=dx^a, det E=1, g=eta, and div_g J=0. Each constituent vector current is future timelike because |v|<1. The bounded domain also enforces |j_S^0|<N/4. No causal speed above c is used (units c=1).

This simultaneously satisfies the selected cross-coframe dictionary, full coframe rank, total phase-current conservation, and vanishing total axial spin. The earlier equal-amplitude obstruction therefore does not extend to variable A/B amplitudes. The new degree of freedom is an explicit population transfer between A and B, not a coordinate relabeling.

## What is still missing

The construction is inverse specified. It does not prove that the native exchange operator generates theta(t), the velocity field, or the spatial spin texture. No Dirac residual, coframe stress equation, multiplier equation or complete connection equation has yet been solved. Vanishing spin makes one source vanish; it does not establish the remaining gravitational equations. In particular, the spatially varying boosts and spin direction introduce derivatives that a time-only fitted exchange may fail to supply. The next substantive check is the actual probe-equation residual and whether an allowed Hermitian native coupling can supply it while respecting all other equations.

SymPy exact scalar checks verified the chosen density and cross-current identities. The vector boost and axial transformation formulas supply the analytic construction; no independent full spinor/PDE verification is claimed. OP5 remains open. This note is local and uncommitted.
