# Native kinetic gap and a common-cone criterion

2026-10-27. Source audit plus a restricted exact criterion; not an assertion about all native operators.

## Source status

16_master_model.tex lines 29--46 gives a semi-concrete representative with D_a, Lambda_ab and R[Psi], and explicitly labels it as such. The displayed prose does not specify their full differential symbols or an evaluated mixed kinetic action. The two-probe cross-bilinear in 12_structural_core.tex specifies a readout, not the kinetic quadratic form governing both source probes. These inspected passages therefore do not determine a full coupled characteristic polynomial. No claim that all possible derivative terms are absent elsewhere is made. Lambda_ab must not be assumed either purely algebraic or differential without its actual realization.

## Exact conditional theorem for two isotropic scalar modes

Let q=(phi,chi) be two independent real local modes with frozen-coefficient kinetic action

 L_kin=(1/2) dot(q)^T A dot(q) -(1/2) sum_i (partial_i q)^T B (partial_i q),

where A is real symmetric positive definite, B is real symmetric, there are no mixed time-space terms, and the spatial form is isotropic. These are explicit restrictions, not derived features of the native spinor system. The squared characteristic speeds are eigenvalues of H=A^(-1/2) B A^(-1/2). Both equal c_*^2 if and only if

 B=c_*^2 A.

Proof: H is real symmetric, hence orthogonally diagonalizable. Two identical eigenvalues imply H=c_*^2 I. Multiplication by A^(1/2) proves the condition, whose converse is immediate. This is a common CONE condition, not a mass equality or a requirement that all dynamics coincide. Mass and local algebraic potentials are lower order here.

A nonsingular field change q=S q' sends A,B to S^T A S,S^T B S. The characteristic determinant changes only by det(S)^2, so basis mixing cannot merge distinct cones.

## Off-diagonal derivative mixing alone cannot repair the previous diagonal mismatch

Hold the earlier diagonal kinetic data fixed and allow both cross terms:

 A=[[1,a],[a,1]], B=[[1,b],[b,v^2]], |a|<1.

If both modes share one cone, B=c_*^2 A forces c_*^2=1 from the first diagonal entry, v^2=1 from the second, and b=a from the off-diagonal entries. Thus for v!=1 no choice of a,b with positive A repairs the mismatch while preserving these diagonal coefficients. Positivity is essential: singular or indefinite kinetic forms are outside the theorem and may introduce constraints or pathologies, not a free rescue.

A consistent auxiliary common-cone example is A=[[1,a],[a,1]], B=A with |a|<1. It has two independent healthy kinetic modes with the same unit cone. Adopting it changes the original second sector's diagonal kinetic term; it is a candidate model change, not a native derivation.

## What this asks of the information-layer proposal

If both readouts arise from one information structure, a precise target is a derived principal form proportional in internal space to one common Lorentzian quadratic form. For this restricted scalar example the condition is B=c_*^2 A. The native first-order spinor/constraint system needs its own full principal-symbol and physical-mode analysis; this theorem cannot simply be pasted onto it. Local coframes, projector constraints and field-dependent derivative maps may change the system.

The investigation has therefore narrowed from unspecified 'more coupling' to a testable kinetic compatibility condition. A successful common action must derive the relevant time/space coefficients, preserve admissible degrees of freedom and account for the coframe reactions. The common cone, even if obtained, does not determine a derivative-free vacuum coefficient and does not itself close OP5.
