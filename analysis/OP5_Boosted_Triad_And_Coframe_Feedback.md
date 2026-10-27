# Boosted triad: actual current realization and coframe feedback failure

2026-10-27. Exact algebraic spinor realization, not an on-shell common-action solution.

On t>0, r<3t, the conserved flat-reference current J^a=(8t,-8x/3,-8y/3,-8z/3) is timelike. Set v=-x/(3t), gamma=(1-|v|^2)^(-1/2), n0=8t/gamma. In the local rest frame choose

 A0=B0=sqrt(n0/4)u_up, C0=sqrt(n0/2)u_down.

Apply the SAME standard Lorentz spinor boost to all three:

 B(v)=sqrt((gamma+1)/2)[I+gamma/(gamma+1) alpha.v].

The boosted fields A=B(v)A0, B=B(v)B0, C=B(v)C0 have total vector current J^a=n0 gamma(1,v) and zero TOTAL axial spin, since both vector and axial bilinears transform covariantly. The selected cross current is necessarily j_S^a=J^a/4=(2t,-2x/3,-2y/3,-2z/3). This is a pointwise smooth spinor field on the patch. Differentiating the boost and n0 creates nontrivial probe-equation terms; no Dirac solution is inferred from current conservation alone.

## Old connection, new complete cross current

Retain the previous candidate connection omega^i_0=omega^0_i=dxi/t. Under the compatible covariant-gradient dictionary the new spinors give

 E0=dt-(x_i dxi)/(3t), Ei=(2/3)dxi,
 det E=8/27.

Thus the current realization does not preserve the old identity coframe. The spatial cross current cannot be discarded while keeping the boosted total current.

## Recompute the Ward current in the NEW geometry

The total coordinate current is J^mu=e_a^mu J^a. Inverting the displayed coframe gives

 J^t=8t-4r^2/(3t), Ji=-4xi,
 volume density=8/27.

Therefore

 partial_mu(volume J^mu)=(8/27)[-4+4r^2/(3t^2)],

which is not identically zero. The flat-reference conserved current is no longer conserved under the reconstructed geometric current/volume. Consequently these exact bilinears do not satisfy a phase-invariant common induced action. The zero on an isolated shell is not an open-region solution. This is a new feedback failure, not a failure of the boost formulas or the original reference continuity test.

## Consequence

Moving spinors can realize the local influx and zero total spin together. The obstacle shifts to their generated geometry: its inverse frame changes the very current whose conservation was used. The coframe, connection, currents and probe equations must be solved simultaneously. Neither selecting another coordinate chart nor retaining only the desired time component repairs this invariant density-divergence residual.

This particular common-boost, fixed-connection ansatz is rejected as a self-consistent induced solution. Different relative motions, connection profiles or source states remain untested. No native OP5 closure or physical torsion prediction follows.
