# Two complex probes: exact rank-four coframe and cone mismatch

2026-10-27. Exact conditional construction in the fixed standard Dirac representation. No native M16/C7 embedding, full action solution, mass generation or OP5 closure is claimed.

## Construction

Use c=hbar=1, K=(I,alpha_x,alpha_y,alpha_z), standard Dirac alpha matrices, beta=diag(1,1,-1,-1), Gamma=beta K, eta=diag(-1,1,1,1). Then {Gamma^a,Gamma^b}=-2 eta^{ab}I. The probes are commuting classical complex four-spinors. Let

 A=(1,0,0,0)^T,
 B=(6t,0,-2z,-2x-2iy)^T.

They are two fields with internal complex components, NOT two complex scalar fields and NOT two single plane waves. Define Z^a=A^dagger K^a B and the symmetric readout

 Y^a=Re Z^a/2,
 E^a_mu=Re(A^dagger K^a partial_mu B+B^dagger K^a partial_mu A)/2.

Direct multiplication gives

 Z=(6t,-2x-2iy,-2y+2ix,-2z),
 Y=(3t,-x,-y,-z), E=diag(3,-1,-1,-1), det E=-3,
 g=E^T eta E=diag(-9,1,1,1).

Thus rank four holds everywhere in this formal local example. The fields grow polynomially and are not normalized finite-energy whole-space states. The constants and initial data are chosen witnesses, not dynamically selected parameters. The complex fourth component supplies independent x and y readouts through alpha_x and alpha_y. For fixed A=e1 the readout ignores Im B1 and Im B3: complex coordinates alone should not be counted as observable directions without evaluating K.

## Both probes satisfy the reference massless equation

The chosen equation is i(partial_t+alpha_i partial_i)Psi=0, equivalent to i Gamma^mu partial_mu Psi=0 in the fixed reference coordinates. A is constant. For B,

 partial_t B=6e1,
 alpha_x partial_x B=alpha_y partial_y B=alpha_z partial_z B=-2e1.

The sum is zero identically. This is a full local solution for both probes, not merely a first-jet fit or an off-shell geometry construction. No coupling or third field is required for this comparison witness. A common constant phase preserves both equations and E; a general spacetime-dependent common phase preserves the symmetric E but does not preserve these free equations at fixed connection.

## Same-cone test fails for this witness

Reference propagation uses eta: a reference null tangent v=(1,1,0,0) has eta(v,v)=0 but g(v,v)=-8. Conversely w=(1,3,0,0) is g-null but eta(w,w)=8. Therefore the two cones differ in the SAME x chart. In coordinates Y the reconstructed metric is eta, but the transformed reference metric is diag(-1/9,1,1,1); the mismatch is not removed by a coordinate change.

If one replaces the probe operator by the induced operator Gamma_ind^mu=(E^-1)^mu_a Gamma^a, the derivative contraction on B becomes

 (1/3)partial_t B - alpha_x partial_x B
                  - alpha_y partial_y B - alpha_z partial_z B=8e1.

Thus the induced Dirac residual is 8i e1, not zero. A still solves it. The test disproves self-consistency of this witness under that replacement; it does not rule out differently coupled probes or alternative readouts.

## Why this failure is structural for the restricted free flat model

Take a constant nondegenerate E, fixed Hermitian K and two probes obeying the SAME massless induced equation K^a e_a^mu partial_mu A=K^a e_a^mu partial_mu B=0, with e=E^-1. Their complex cross current has divergence

 e_a^mu partial_mu(A^dagger K^a B)=0,

because each differentiated term vanishes by one probe equation and its adjoint. The symmetric derivative dictionary then implies

 e_a^mu E^a_mu=(1/2)Re[e_a^mu partial_mu(A^dagger K^a B)]=0.

But the inverse-coframe contraction is 4. Contradiction. Equal real Dirac masses also give a conserved cross current and the same obstruction in this constant-frame setting. Different masses, exchanges between channels, additional connection/weight terms, nonconstant frames with their full spin connection, or a changed dictionary require separate analysis. In particular, the argument is not a blanket impossibility result for two complex fields.

## Consequence

Two structured complex spinors suffice for rank four and can satisfy a genuine reference evolution simultaneously. The unresolved issue is making this SAME readout geometry govern their dynamics. Complexity removes the earlier plane-wave rank limitation but does not by itself remove the current/trace obstruction. A meaningful next candidate must have an explicitly derived cross-current source or a justified change to the derivative-only coframe, and must solve the common variational equations. A reference photon frame or an absolute energy zero is not selected by this witness.

Run OP5_Two_Complex_Probes_Check.py for exact integer/complex component checks of the fields, coframe, both reference residuals, induced residual and the cone mismatch. The general restricted obstruction above is an analytic proof, not inferred from those samples.
