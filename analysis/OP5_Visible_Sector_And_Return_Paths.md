# Visible-sector closure and hidden return paths

2026-10-27. Conditional operator audit; not native detector identification.

## Native compatibility already available

analysis/OP5_Common_Operator_Representation.md records the source-backed normal equation, with internal orthogonal P=P_C7, Q=I-P, independent full Dirac spin factor and a chosen positive adjoint:

 N=i Gamma^mu Q(nabla_mu P)P-beta g_Y Q T P.

For closure of the entire P-spinor carrier under those representation assumptions, the independent Clifford components require nabla_mu P=0 and beta g_Y QTP=0. Merely checking [M,P]=0 or H_C=0 does not check these conditions. The minimal HC expression is block diagonal and is not itself an amplitude-damping law. The detector instrument and structural C=(I+J)/2 have not been natively identified with this P.

## Exact unitary-sector test

For i partial_t psi=H psi with a fixed orthogonal P and self-adjoint H, preservation of the visible subspace requires QHP=0. Self-adjointness gives PHQ=0 as well, so H is block diagonal and there is neither exit nor return. Domain conditions are needed for unbounded operators; the elementary identities here apply to finite matrices or a common invariant domain.

For time-dependent P(t), differentiating P psi=psi gives Q dot psi=dot P psi and hence

 Q H P=i dot P P.

The factor i belongs to the Hamiltonian convention just stated; formulas for a directly defined evolution generator G=partial_t instead have no such factor. This is not permission to identify an arbitrary moving projector with a dynamically preserved detector.

Sources must create states in im P and the measurement instrument must not introduce transitions to Q. A projector condition on free evolution does not establish these preparation and detector properties.

## Eliminating the hidden block exposes the missing term

For fixed P and finite block H, the visible resolvent obtained by eliminating Q has energy-dependent effective operator

 H_eff(z)=H_PP+H_PQ (z-H_QQ)^(-1) H_QP,

where z-H_QQ must be invertible. For a spatial field theory the hidden resolvent carries its spatial/temporal propagation; it cannot generally be replaced by a local constant. Exact block decoupling removes this contribution. If off-diagonal blocks are epsilon V, the return term starts at order epsilon^2, not zero.

For the exact two-state example H=[[0,epsilon],[epsilon,0]], a visible initial state has hidden probability sin^2(epsilon t). It may be below a detector threshold at early times while being nonzero. With suitable time it reaches one. This illustrates leakage, not a spatial speed calculation. When a hidden field channel has a different cone, its return contribution must separately be tested for spacetime support.

A bounded off-diagonal perturbation of norm epsilon gives a finite-time Duhamel amplitude bound ||Q U(t) P||<=|t| epsilon relative to the decoupled evolution (under self-adjoint unitary assumptions). Such a bound is not an exact all-time causal prohibition. Threshold closure and exact signal isolation are distinct claims.

## Implication

There is a mathematically coherent route by which a larger information structure can coexist with a single accessible cone: invariant physical subspace, compatible preparation and detector, and one causal kinetic structure within that subspace. The currently inspected native material has candidate projectors and a normal-equation criterion, but not the full evaluated representation, detector coupling and physical cone needed to prove this route.

Local OP5 detector-threshold closure is not invalidated by this audit; it simply cannot be promoted into exact isolation of a hypothetical faster hidden channel. No hidden faster channel has itself been established. The next needed native data are the represented connection, triadic operator, moving-projector terms and measurement coupling. Their absence is a precise open input, not grounds to invent matrices and label them derived.
