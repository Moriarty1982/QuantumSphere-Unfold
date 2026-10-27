# Counterflow dynamics: a necessary inter-sector source

2026-10-27. Follow-up to OP5_Variable_Amplitude_Counterflow_Witness.md. Exact necessary-condition test in the stated flat classical Dirac comparison model. No native OP5 closure and no complete Dirac residual solution.

## Contract

Use the previous fields with E=I, omega=0, constant N, v=x/t, variable A/B mixing angle and opposite transverse rest spins. Let P denote the combined A/B current, not a projector:

J_P=(N/2)(1,v), J_C=(N/2)(1,-v).

The common total current is conserved, but separately

div J_P=3N/(2t), div J_C=-3N/(2t).

These identities hold throughout the admissible patch, independently of theta(t). They follow from div_x(x/t)=3/t. A time-dependent A/B rotation alone cannot supply the missing C-to-AB transfer. This is a local current-source requirement; no boundary claim is needed.

## Why even arbitrary scalar flavor exchange fails

Write i partial_t psi_a=-i alpha^i partial_i psi_a + sum_b V_ab psi_b. For a Hermitian total potential,

div J_C=2 Im sum_b C^dagger V_Cb psi_b.

Allow arbitrary spacetime-dependent flavor matrices in both structures V=F tensor I_4 + G tensor beta, with F,G Hermitian. This includes scalar flavor Hamiltonians and conventional scalar Dirac mass mixing, but not all possible native operators.

At each point let U=B(v)(chi_+,0), W=B(-v)(chi_-,0), with chi_- orthogonal to chi_+, and let B(v)=a I+b alpha_vhat (a,b real). Then

W^dagger U=(a^2-b^2) chi_-^dagger chi_+=0,
W^dagger beta U=(a^2+b^2) chi_-^dagger chi_+=0.

The omitted cross terms in the second expression have zero upper-upper block. A and B are scalar multiples of U, C of W. Therefore C^dagger A=C^dagger B=C^dagger beta A=C^dagger beta B=0. The diagonal Hermitian terms have real expectation. The entire C source is zero, in contradiction to -3N/(2t).

Thus NO potential in this scalar flavor family can make this prescribed witness solve the probe equations on the patch, regardless of how its coefficients are fitted. This is a necessary-condition obstruction stronger than merely finding one failed constant coupling. A general interaction or a modified coframe/differential operator is not excluded.

## A nonzero channel exists outside that family

At a point with v along x and spin along y, choose chi_+=(1,i)/sqrt(2), chi_-=(1,-i)/sqrt(2). Direct multiplication gives

W^dagger alpha_y U=-2 i a b,
W^dagger alpha_x U=W^dagger alpha_z U=0.

Consequently an appropriate off-diagonal flavor coupling carrying alpha_y structure can have a nonzero charge-transfer source when v is nonzero. This is an algebraic possibility, not a proposed derived interaction, not a complete residual fit, and not proof of Lorentz-covariant/native admissibility. Its coefficient, covariance, action origin and effect on all other equations must be checked. A common flavor-diagonal vector potential does not by itself transfer charge between species.

## Implication for OP5

The previous geometry/current/spin construction remains correct as a kinematic witness. It is dynamically excluded for scalar flavor exchange. The next question is whether the actual projected native operators provide off-diagonal spinor structure or whether the witness itself must change. Total-current conservation alone concealed this inter-sector obstruction. No physical frame identification or cosmological inference follows.

Verification: exact analytic current divergence and arbitrary-direction overlap proof, plus SymPy exact four-component matrix check for the representative x-boost/y-spin orientation. The full Dirac residual, gravitational/coframe response and multiplier equations remain uncomputed. Local uncommitted research note.
