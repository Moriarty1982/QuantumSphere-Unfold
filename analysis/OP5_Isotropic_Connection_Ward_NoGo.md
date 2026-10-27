# Free isotropic boost connection: exact Ward compatibility exclusion

2026-10-27. Exact exclusion of one declared ansatz family, not all two/three-probe or torsionful models.

Retain the actual common-boost triad bilinears J^a=(8t,-8x/3,-8y/3,-8z/3), j_S=J/4 from OP5_Boosted_Triad_And_Coframe_Feedback.md. Replace the fixed connection by an arbitrary differentiable real function h(t):

 omega^i_0=omega^0_i=h(t)dxi, omega^i_j=0.

Keep the compatible dictionary E=(1/2)D j_S, t>0. Then

 E0=dt-(h/3)x_i dxi, Ei=b(t)dxi,
 b=th-1/3, det E=b^3.

On a connected nondegenerate patch b!=0 the sign of the determinant is constant, so testing divergence with b^3 or |b^3| is equivalent. The coordinate current is

 J^t=8t-8h r^2/(9b), Ji=-8xi/(3b).

Exact density divergence is

 partial_mu(det(E)J^mu)
 =8b^2[b+3t b'-1] -(8/9)(h b^2)'r^2.

On an open spatial region the independent constant and r^2 coefficients must vanish:

 b+3t b'=1, (h b^2)'=0.

Use h=(b+1/3)/t. Substituting the first equation into the second yields

 (h b^2)'=-(2b/(9t^2))(9b^2-2b-1)=0.

Since b!=0, b must take one of the two discrete values (1+sqrt(10))/9 or (1-sqrt(10))/9 throughout the connected interval. Differentiability then makes b constant. But the first equation for constant b requires b=1, which is neither root. Contradiction.

Therefore NO differentiable isotropic time-only boost-connection profile in this family makes the chosen triad current conserved in its own reconstructed geometry on an open spacetime patch. This is stronger than failure of h=1/t and cannot be repaired by fitting a different time profile. Degenerate b=0 is excluded because no inverse coframe or nondegenerate spacetime exists there. Matching only a point or a shell does not satisfy the open-patch conditions.

Scope: the current was fixed from a common boost and a spin-balanced triad. Relative boosts, different amplitude distributions, spatially dependent connection components, rotational connection components, a nonparallel selector, additional geometric terms or a different readout are not covered. The result is a necessary Ward-identity exclusion before solving the remaining field equations, so no candidate within this family can solve a real common phase-invariant induced action with this current and no additional charge sources.

Next research choice should change an explicitly justified structural assumption, not retune h(t). The native triadic coupling can in principle yield different relative currents; those must be derived together with the connection and coframe. No general OP5 no-go is asserted.
