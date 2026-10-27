# Two meanings of Menge: admissible states and probe ensembles

2026-10-27. Continuation of the chiral tangent checkpoint. Reproduce with OP5_Constraint_Set_And_Ensemble_Check.py and its JSON. Conditional comparison model, two sample points, no native OP5 closure.

## 1. Is the admissible state set invariant?

For equalities C(z)=0 a necessary tangency test is DC(z)F(z)=0; under suitable regularity and existence assumptions tangency can establish invariance. Here z must include field jets and connections, not just finite spinor amplitudes: the cross coframe depends on derivatives. We test selected necessary conditions, not all jet constraints or a PDE existence theorem.

The old prescribed trajectory satisfies zero total axial vector, zero total spatial vector current, j_S=2x, and E=I. Set w=iR, the difference between the old trajectory's time derivative and the time derivative demanded by the old flat Hamiltonian. For a bilinear psi^dagger O psi its derivative difference is 2 Re(psi^dagger O w). Since the prescribed total spin/current restrictions hold identically, nonzero differences demonstrate failure of tangency to those restrictions.

At P1=(1,0.6,0,0):
- Total vector-current derivative difference: (0,48,0,0).
- Total axial-vector derivative difference: (0,0,-36,0).
- Selected cross-current derivative difference: (0,-4,0,0).

At P2=(1,0.4,0.2,0.2):
- Total vector-current derivative difference: (0,58.529271,29.264635,3.419206).
- Total axial-vector derivative difference: (0,15.363244,-30.726489,0).
- Cross-current derivative difference: (0,-4.427401,-2.213700,-0.213700).

Thus the narrow zero-spin, zero-spatial-current, fixed-cross-field set is NOT preserved by this comparison dynamics. This is not a violation of the total continuity equation: a current can acquire spatial components while its divergence still obeys its evolution law. Nor does it show these restrictions are all required by the native model; several are choices of the witness.

### Does the geometry become inadmissible immediately?

At the same field value, replace only the time derivative by the Hamiltonian-demanded one, retain spatial jets and the old connection, and evaluate the dictionary. The resulting time coframe column changes by half the cross-current derivative difference. Therefore

E=[[1,0],[b,I_3]], det E=1,
g=E^T eta E=[[-1+|b|^2,b^T],[b,I_3]].

b=(-2,0,0) at P1 and approximately (-2.213700,-1.106850,-0.106850) at P2. Both have Lorentzian signature, verified numerically and guaranteed algebraically by invertibility of E (congruence with eta). The negative eigenvalues are about -0.2361 and -0.1588. A positive g00 in these coordinates is not a loss of Lorentzian signature or evidence of superluminal signaling.

This preserves rank and signature at these recomputed jets; it does NOT preserve the original E=I or prove a self-consistent solution. The Hamiltonian used to select the derivative was the old flat one. Feeding the new coframe back into the kinetic operator is an outstanding coupled problem. Curvature needs derivatives of a consistent coframe field and cannot be read off from these point matrices.

## 2. Can a population of probes compensate the defect?

For a statistical mixture with fixed nonnegative weights, mean bilinears and their rates average linearly. Identical copies retain the same normalized drift; greater number alone cannot remove a systematic mismatch. This uses a mixture or distinguishable copies, NOT coherent addition of spinors, which would generate extra cross terms.

### Explicit local two-configuration test

At each sample choose the proper spatial rotation by pi around the radial direction n=x/|x|: Q=2nn^T-I, det Q=1. Use a partner obtained by actively rotating the entire local field configuration, its spatial jets and the prescribed connection together. The point is fixed by this rotation. In a rotationally covariant comparison system its vector/axial rates transform by L=diag(1,Q). This is not just relabeling the same configuration and not a proof that two branches share one common connection. A different constant rotation is chosen for each sample; no global position-dependent rotation without derivative terms is assumed.

The original spin drift is transverse to x, so the equally weighted pair cancels it at both samples. The original cross-field dictionary j_S=2x is covariant under simultaneous spatial/internal rotation, and the initial E=I is retained by the rotated prescribed configuration.

At P1, mean axial drift becomes exactly zero, but mean vector drift remains (0,48,0,0) and mean cross drift remains (0,-4,0,0). At P2 the mean axial drift vanishes to rounding, while mean spatial vector drift is approximately (49.914128,24.957064,24.957064), and mean cross spatial drift is (-3.760734,-1.880367,-1.880367). Radial contributions survive. The rotated pair therefore repairs one mean constraint, not the dynamics as a whole.

Proper rotations also leave each species' pseudoscalar-rate obstruction unchanged. They cannot cancel that scalar diagnostic within the same species merely by changing orientation. The A/B/C sum previously cancels, but that is a different condition from preserving each individual zero-pseudoscalar ansatz.

### Averaging geometry requires an additional choice

Define the ensemble coframe as the arithmetic mean of the two recomputed coframes in this fixed common gauge, solely as a comparison. Its determinant remains one. However,

mean(E^T eta E) != mean(E)^T eta mean(E)

in general. At P2 the difference has only a 00 entry of about 0.8333333333 in these coordinates. For this shear-form example it equals the variance of b; P1 gives zero. This is an explicit algebraic fluctuation term, not a derived stress tensor, cosmological constant, or universal averaging prescription. The native theory must specify what is averaged and why a common frame/gauge is available.

## Result and next task

The state-set route identifies which witness constraints fail and separates them from nondegeneracy/signature, which survive the instantaneous dictionary recomputation. The ensemble route constructs a local mean spin cancellation but leaves radial current drift and the individual pseudoscalar condition unresolved. Neither route closes OP5. The next substantive calculation is a self-consistent coframe/kinetic update with the enlarged spinor family, or a specified ensemble evolution and common-action averaging law; two independent point constructions cannot replace that work.

All numerical values use arbitrary comparison normalization. Analytic derivatives were evaluated at 30 digits; matrix eigenvalues and ensemble operations use ordinary floating point. Assertions check rotation determinant, mean spin cancellation, surviving vector drift, coframe rank and metric signature. Research checkpoint: retained with the literature survey; OP5 remains open.
