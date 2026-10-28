# Variational parent for the symmetric two-probe readout

2026-10-27. Explicit alternative common-action construction; not a native derivation or a solved self-induced Einstein-Dirac model.

## A precisely declared first parent

Let Psi=(A,B), S=sigma_x/2 on the two internal modes, K^a=(I,alpha_i) fixed Hermitian spin weights, beta the fixed Dirac adjoint, and M a Hermitian internal matrix. Work on a reference coordinate patch with the ordinary fixed reference Dirac kinetic term. Independent variables are Psi, a real invertible coframe E and a real multiplier density lambda_a^mu. Set g=E^T eta E and

 C^a_mu=Re(Psi^dagger S K^a partial_mu Psi)
       =(1/2)partial_mu j_S^a,
 j_S^a=Psi^dagger S K^a Psi=Re(A^dagger K^a B).

S and K commute. Consider compactly supported variations of

 S_parent= integral d4x { (i/2)[Psi^dagger K^mu partial_mu Psi
                    -(partial_mu Psi^dagger)K^mu Psi]
                  -Psi^dagger beta M Psi }
          +S_geom[E]+integral d4x lambda_a^mu(E^a_mu-C^a_mu).

S_geom must be specified, e.g. the Einstein-Hilbert and vacuum terms with their usual boundary treatment. This parent is explicit and real under the declared assumptions. Its microscopic kinetic operator uses the reference frame; adopting it is not the same as deriving the desired common induced kinetic frame. It is a controlled action-level test of the missing feedback.

## Exact variations

Variation in lambda gives E=C. Write pi_a^mu=delta S_geom/delta E^a_mu. Variation in E gives lambda=-pi. Integrating the multiplier coupling by parts gives

 -integral lambda C = integral Psi^dagger V_lambda Psi + boundary,
 V_lambda=(1/2)(partial_mu lambda_a^mu) S K^a.

Thus the probe equation is

 i K^mu partial_mu Psi-beta M Psi+V_lambda Psi=0,

and its adjoint must also hold. The source V_lambda is Hermitian for real lambda; it is not an arbitrary damping term. Eliminating E and lambda reproduces the chain rule for varying S_geom[C[Psi]]. Therefore the earlier free reference evolution omitted precisely this feedback whenever partial lambda is nonzero.

The total reference phase current is conserved. Since V_lambda commutes with S, its contribution to the selected cross-current divergence vanishes directly:

 partial_mu j_S^mu=i Psi^dagger beta [M,S] Psi.

For M=g sigma_y this becomes g(bar A A-bar B B). The geometric feedback can change the state and hence this source, but does not independently create selected-current exchange through a noncommuting internal multiplier. This provides an additional consistency check for future solutions.

## Why this parent is still too small for the target

The constraint remains E=d(j_S/2), hence g is locally flat wherever E is invertible. A more explicit variational identity explains why the flat branch is not a gravitational vacuum solution in the ordinary sense: the pullback volume integral is a boundary quantity under compactly supported variations of Y=j_S/2 on a fixed-orientation nondegenerate patch. For a pure constant vacuum term, lambda is proportional to det(E) E^-T; its divergence vanishes by the cofactor/Piola identity for E=dY. Therefore its V_lambda vanishes in this restricted model. The Einstein tensor vanishes on the same flat branch. This is restricted composite insensitivity, not a cancellation of vacuum energy under unrestricted metric variation.

For independent E variations the multiplier balances the vacuum stress; discarding it would change the equations. This parent therefore can account for the flat reference comparison without deriving ordinary Einstein gravity or fixing the vacuum coefficient. Adding arbitrary nonzero V_lambda while keeping this pure flat geometric action would also be inconsistent.

## Requirements for the stronger parent

To make the geometry govern the SAME probe kinetic term, replace the reference kinetic action by its induced coframe/connection version BEFORE varying. This introduces probe stress in the E equation and connection reactions. If the cross dictionary also uses a geometric spin connection, its variation contributes to that connection equation. Treating connection as independent is one possible first-order formulation; setting torsion to zero or imposing compatibility must then be justified in that formulation. If the connection is eliminated first, all derivative chain-rule terms must instead be retained.

Neither choice is uniquely fixed by the inspected native source. This note does not silently choose one and claim a native result. What is now explicit is the missing feedback term in the simpler parent and the reason a purely exact cross coframe cannot supply the desired curved common dynamics.

Conclusion: a common real parent exists for the fixed-reference symmetric readout, but that construction by itself preserves its flatness restriction. The next needed physical input is the justified non-exact geometric readout/connection and its consistent induced kinetic action, not an arbitrary correction to the already solved reference trajectories.
