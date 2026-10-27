# Torsion-free balance: index-symmetry obstruction

2026-10-27. Conditional continuation of OP5_Connection_Reaction_Followthrough.md. Applies to the minimal real symmetrized Dirac action with an independent metric-compatible Lorentz connection and the stated covariant-gradient cross dictionary. Not a theorem for nonminimal/native-unspecified couplings.

## Minimal Dirac spin structure

For the symmetrized Dirac kinetic term the connection variation contains the Clifford anticommutator {gamma^c,gamma^[a gamma^b]}. Clifford multiplication makes this proportional to gamma^[c gamma^a gamma^b]; metric-contraction terms cancel. Thus, after converting the coordinate current index to a Lorentz index with the coframe and lowering it consistently, the minimal Dirac spin coefficient s_abc is totally antisymmetric. Overall factors/signs depend on gamma and variation conventions and do not affect this symmetry test. Summing several minimally coupled Dirac probes preserves total antisymmetry.

The cross-dictionary multiplier source has form

 L_abc=lambda_ac j_b-lambda_bc j_a,

where the third index has been converted using the same nondegenerate coframe. The prior torsion-free equation requires s_abc=L_abc/4 in its full-index convention.

## Exact algebraic lemma

For any nonzero covector j, if L_abc of this form is totally antisymmetric, it vanishes identically.

Proof: choose a linear basis in which j has only its 0 component nonzero. For i,j different from 0, L_ijc=0 for every c. Any totally antisymmetric three-index component either has a repeated index and vanishes, or has three distinct indices, at least two different from 0. Permuting that pair into the first two slots shows that component vanishes too. Hence L=0. The proof is tensor-algebraic and does not require j to be timelike; a general linear basis can align a nonzero null covector as well. It is not claiming that this basis change is an allowed Lorentz observer transformation.

Consequently, where j!=0, the torsion-free minimal-Dirac balance forces

 s_abc=0 AND L_abc=0,
 lambda_ac=j_a v_c for some covector v,
 rank(lambda)<=1.

A nonzero totally antisymmetric Dirac spin coefficient cannot cancel this multiplier source: their allowed tensor structures intersect only at zero. This strengthens the previous zero-spin-only control. At j=0 the multiplier source vanishes and the rank conclusion does not follow. The total spin of several probes may cancel, so this result does not require each individual probe spin to vanish.

## What this does and does not decide

Under these particular action and readout assumptions, a generic nonzero spin or generic coframe reaction rules out the torsion-free branch. Allowing torsion makes the geometric connection variation nonzero and can balance different source components, but one must solve that equation together with T^a=(1/2)R^a_b j^b. Existence and compatibility of that torsionful branch have not been established.

Alternatively, a nonminimal probe coupling, selector-dependent connection term, changed cross dictionary, or a different treatment of the connection changes the premises. Such terms must come from a justified common action, not be introduced solely to cancel the mismatch. The native ordered complex kinetic expression has not automatically been identified with the minimal real symmetrized Dirac action used in this test.

No physical torsion prediction, native M16 representation, absolute vacuum-energy determination or OP5 closure follows. The concrete result is that a hoped-for cancellation is unavailable in this specific minimal torsion-free parent.
