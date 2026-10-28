# Native exact-closure branch and the geometry tradeoff

2026-10-27. Source interpretation correction and conditional implication chain.

The closed-master-system block in 10_sphaera_and_physics.tex explicitly includes Q Psi=0, H_C=Lambda[M,P] and R_C=0. Therefore the manuscript does not merely leave a finite penalty as its only closure statement. Exact closure is declared as part of a subsequent system. The earlier finite-penalty audit concerns its derivation from the displayed unconstrained action and preservation by the full dynamics, not absence of an exact condition in the text.

The equivalent-closure-criteria proposition correctly identifies R_C=0 with [M,P]=0 for the block decomposition. With the stated minimal positive functional, exact closure implies H_C=0. This algebraic implication is separate from the normal compatibility equation for the full probe operator: M preservation alone does not verify connection transport, T, or detector couplings.

The Einstein reconstruction explicitly starts from a 'closed triadic probe field' on the physical sector. This supports reading all three triadic components as physical, rather than reading the third component as the hidden complement. It does not supply the actual represented embedding matrix or kinetic/detector operators.

## Consequence for the already tested flat comparison

Under the declared constant Hermitian spin weights K^a, an internally factorized Hermitian gauge connection commuting with K, and H_C=0, the source coframe reduces to

 E^a_mu=Re(Psi^dagger K^a partial_mu Psi)=partial_mu j^a/2.

The internal unitary gauge term has zero real part under these assumptions. At rank four the corresponding geometry is locally flat. Thus exact minimal closure removes the HC deformation used in the earlier conditional curved construction. This is a restricted result, not a theorem that every native closed state is flat: moving weights, nonfactorized geometric spin connections and alternative justified readout maps are excluded from these premises.

For general fixed-dimension fields with D=partial+B and Hermitian K(x), the exact identity is

 E^a_mu=(1/2)partial_mu(Psi^dagger K^a Psi)
       +(1/2)Psi^dagger[K^a B_mu+B_mu^dagger K^a-partial_mu K^a]Psi.

The second term is the precise remaining candidate for non-exact coframes when minimal H_C vanishes. It cannot be replaced by an arbitrary curvature source: the connection/weight compatibility, native adjoint and field equations must be specified. A non-exact coframe alone also does not prove nonzero Riemann curvature.

## Variational alternatives must be distinguished

If H_C is an independent field, its Euler equation includes its kinetic, probe and potential sources; a finite square penalty alone is not identical to H_C=Lambda. If H_C=Lambda[M,P] is substituted as a functional definition, the reduced action must include chain-rule variations through M,P and any other dependencies. If exact conditions are imposed by multipliers, their reaction equations must be retained. These are distinct variational formulations. The source display alone does not justify treating all three as interchangeable.

Research consequence: keep the exact closed branch as a legitimate declared target, evaluate its full normal compatibility and geometric connection terms, and derive the corresponding constrained or reduced action consistently. Do not reopen leakage merely to obtain curvature before checking whether the geometric connection already supplies the missing terms. This prioritizes the native geometric/internal connection split over new auxiliary hidden-sector guesses. OP5's absolute energy coefficient remains unselected.
