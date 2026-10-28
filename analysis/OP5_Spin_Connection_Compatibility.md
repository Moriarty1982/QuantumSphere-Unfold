# Compatible spin connection: curvature allowed, unchanged probe law obstructed

2026-10-27. Exact conditional identities. Source anchor: 10_sphaera_and_physics.tex geometric/internal decomposition near line 2515. Prior invariant obstruction: analysis/HC_Bilinear_Geometry_Bridge.md section 9.

Assume a real invertible coframe E, standard compatible Dirac adjoint, a spin connection preserving the Clifford vector bilinear and an internal connection preserving its pairing. Let j^a=barPsi Gamma^a Psi, with real components, and retain the unshifted dictionary E^a_mu=Re(barPsi Gamma^a D_mu Psi). Compatibility gives

 D_mu^(vector) j^a=2 Re(barPsi Gamma^a D_mu Psi)=2 E^a_mu.

Using the tetrad postulate and j^nu=e_a^nu j^a, this becomes

 nabla_mu j^nu=2 delta_mu^nu,
 nabla_mu j^mu=8.

For the same induced Dirac operator with the usual mass-adjoint reality and a compatible unitary internal connection, the probe equation and adjoint instead give nabla_mu j^mu=0. The contradiction is invariant, not a consequence of choosing photon versus matter coordinates. With a nonzero fixed real normalization s in the dictionary the required divergence is 8/s, still nonzero.

The pointwise version needs even fewer geometric assumptions: for residual R=(i Gamma^mu D_mu-Omega)Psi, induced Gamma^mu=e_a^mu Gamma^a and w=barPsi Omega Psi,

 Im(barPsi R)=4-Im w.

Thus real w excludes R=0 for this exact dictionary in any compatible spin connection. Adding spin connection terms to BOTH the dictionary and unchanged equation cannot evade it. Euclidean Hermiticity alone is not the requisite adjoint-weighted reality condition. Different derivatives, different source/readout fields or additional equation terms alter the premises and need their own analysis.

## Geometry alone need not be flat

Taking another derivative of nabla_mu j^nu=2 delta_mu^nu gives R^nu_(rho mu lambda) j^rho=0. That is a curvature-kernel condition, not R=0. A concrete geometry-only example is

 ds^2=-d tau^2+tau^2(dx^2+dy^2+dz^2), tau>0,
 j=2tau partial_tau.

Direct covariant differentiation gives nabla_mu j^nu=2 delta_mu^nu and divergence 8. Spatial Riemann components are nonzero; for the usual curvature convention R=6/tau^2. This is an example of an admissible geometric vector, NOT a compatible conserved Dirac current or a solved native probe construction. It demonstrates precisely why the spin-connection possibility was not excluded merely by earlier flatness.

## Cross-readout caveat

The identical current-conservation contradiction must not be applied automatically to a selected two-probe cross current. Interacting probes can source that current while conserving the total, as the earlier Hermitian exchange first-jet witness demonstrated. To use this route requires deriving the selected cross coframe and all source reactions from a common action. A native full-triadic coframe is not interchangeable with that selected observable.

Outcome: ordinary spin-connection compatibility alone does not repair the unchanged same-field/same-induced-frame equation. The next substantive choice concerns the physical readout map or the equation obtained by full variation, not merely a new coordinate frame. The fixed-reference affine parent and cross-readout constructions are explicitly different model routes; none has yet supplied native OP5 closure.
