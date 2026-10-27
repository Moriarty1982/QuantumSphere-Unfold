# Native operator slots and cross-coframe feedback

2026-10-27. Source audit and exact conditional algebra. Continuation of OP5_Counterflow_Intersector_Source_Obstruction.md. No repository edits, no claim of native PDE solution.

## Source findings

In sources/research/parts/v470/10_sphaera_and_physics.tex:
- Lines 2049-2057: D_mu=partial_mu+i A_mu+kappa H_C n_mu+eta(1-P_C7)n_mu.
- Lines 2074-2083: Omega=m0 I+alpha P M16 P+beta gY T+gamma H_C. Here beta is explicitly a real coefficient, NOT our Dirac beta matrix.
- Lines 2168-2183: explicit triadic off-diagonal entries T_(1,perp), T_(2,perp) and their reverse entries. The third mode already has an interaction slot.
- Lines 2403-2426: the free Dirac limit assumes A_mu=0 AND scalar reduction of Omega. These are additional limiting assumptions, not requirements for the full model.
- Lines 2430ff: A_mu is allowed as an internal projected connection.
- Lines 2513-2525: geometric/internal decomposition is assumed on the closed sector.

The displayed triadic block does not specify the four-component Clifford action of its entries. A repository search for these exact T subscript symbols found their operative display here, not a separate explicit spinor realization. Section 16_master_model.tex lines 29-46 likewise describes Lambda_ab as inter-sector couplings in a semi-concrete representative. This audit does not prove absence under every alternate notation; it establishes that the inspected blocks alone do not determine the needed matrix elements.

Therefore the previous scalar-exchange obstruction applies to the scalar comparison reduction, not automatically to the full native operator. Two potential locations already exist: non-scalar triadic T entries, or off-diagonal internal spatial connection A_i. In the usual Hamiltonian form, D=partial+i A yields A_0+alpha^i A_i; the spatial term has the alpha structure absent from a scalar mass. Off-diagonal flavor components are necessary for the inter-species source in this comparison. Their admissibility and equations of motion are still unspecified here.

## The connection cannot be added without checking the dictionary

For the declared symmetric cross readout, assume a tensor-product internal flavor representation commuting with K^a, Hermitian A_mu, and fixed Hermitian selector

S=(|A><B|+|B><A|)/2, j_S^a=Psi^dagger S K^a Psi.

Then exactly

E^a_mu=Re(Psi^dagger S K^a D_mu Psi)
       =(1/2) partial_mu j_S^a
         +(i/2) Psi^dagger [S,A_mu] K^a Psi.

This formula uses omega=0 and omits no connection term within this contract. In particular the old flat result E=I from j_S=2x does not automatically survive a new internal connection.

For third-mode entries A_AC=p, A_BC=q, Hermiticity gives

[S,A]_AC=q/2, [S,A]_BC=p/2.

Hence preserving the stronger operator condition [S,A]=0 forbids both third-mode couplings. SymPy verified these entries exactly. A moving selector can instead enter a covariant transport equation, but then its derivatives and interpretation must be included. Also a nonzero commutator does NOT force its expectation to be nonzero on every chosen field: cancellation of the displayed expectation is a weaker possible route, which has not been excluded.

## Precise remaining task

Instantiate the projected triadic/gauge representation, solve the required C-sector source -3N/(2t), and simultaneously check the connection correction to E. Then check the entire probe residual and action-derived gauge, coframe and connection equations. Simply fitting a source or declaring an interaction slot does not complete those steps. Neither changing the reference frame nor relabeling a scalar coefficient supplies a missing matrix element.

Result: the manuscript already allows a place for the missing interaction, but the inspected source does not yet derive its effective action on this witness. The earlier restricted no-go remains valid; a full-model no-go would be unjustified. OP5 remains open. Local uncommitted research note.
