# Compensator Curvature, the Null Axis and a Real Action

Date: 2026-10-16. Status: an exact conditional curvature pullback, a real-form diagnostic and an explicitly alternative real-field completion. This is not a full native solution, a mass prediction, a fluid-viscosity derivation or an edit to the main TeX.

## Result

The connection already printed in the paper can supply a compensator kinetic term. For a fixed Hermitian internal direction `H_C=h(x)T`, constant null axis and commuting background, its curvature action reduces exactly to

```text
L_HC = kappa^2 Tr(T^2) (n.partial h)^2/2.
```

For homogeneous profiles this has positive temporal inertia under the declared ordinary positive internal trace. However, its full spacetime principal tensor has rank one. A temporal coefficient is not yet an ordinary Lorentzian wave operator, isotropic fluid dynamics, stable mass phase or irreversible damping.

There is also a convention issue worth settling before further coefficient fitting: interpreting both `A_mu` and `H_C` as Hermitian in the displayed `D_mu=partial_mu+i A_mu+kappa H_C n_mu+...` gives opposite electric kinetic signs in the **real part of the literal** `-Tr(F F)/4`. An alternative `-Tr(F^dagger F)/4` gives equal electric signs and has explicit coupled field equations, derived below. It is a different action, not a spelling correction. Neither the alternative nor the ordinary Hermitian interpretation is silently adopted as the native theory.

The existing quadratic matching penalty can then support a conditional homogeneous compensator oscillation, without adding a new potential. Its frequency is still a ratio of unevaluated native couplings, and its background/source equations remain to be solved. It does not supply particle masses or phase selection.

## 1. Source and Declared Assumptions

The retained [native field package](../sources/research/parts/v470/10_sphaera_and_physics.tex), at `thm:variational-form` and `thm:resonance-field-eq`, gives

```text
D_mu = partial_mu+i A_mu+kappa H_C n_mu+eta (I-P_C7)n_mu,
F_mu_nu = [D_mu,D_nu],
L_F = -Tr(F_mu_nu F^mu_nu)/4.
```

It explicitly calls `n` a null-axis direction. The curvature action has **no printed dagger**. The signature used here is the source's `(-,+,+,+)`. None of this fixes a complete physical adjoint, internal real form, gauge-current representation, allowed connection variations or positive energy theorem. A null direction is not a photon rest frame.

For the first calculation only, take flat fixed spacetime, a constant real `n_mu`, fixed finite Hermitian `T`, real `kappa`, `H_C=h(x)T`, `A=0`, and constant commuting `P_C7`. The closure background has no curvature in this branch. The scalar `h` is the compensator amplitude, not the vector of hidden probe partners called `h` in the [previous collective-action calculation](HC_Collective_Action_Reduction.md).

These assumptions isolate a native term; they do not establish that the ansatz satisfies the other native equations. If `n`, the internal direction, the projector, metric or gauge fields vary, their derivative, commutator and variational terms must be retained. For nonconstant `n`, the curvature also contains `kappa h T (partial_mu n_nu-partial_nu n_mu)`.

## 2. Exact Pullback and Its Principal Tensor

The commuting connection gives

```text
F_mu_nu = kappa T (n_nu partial_mu h-n_mu partial_nu h),
Tr(F_mu_nu F^mu_nu)
 = 2 kappa^2 Tr(T^2) [n^2 (partial h)^2-(n.partial h)^2].
```

Hence `L_F=(partial_mu h) K^{mu nu} (partial_nu h)/2`, with

```text
K^{mu nu}=kappa^2 Tr(T^2)(n^mu n^nu-n^2 g^{mu nu}).       (1)
```

For nonzero null `n`, nonzero `T` and `kappa`, this is rank one. For `n_mu=(-1,0,0,1)`, `n^mu=(1,0,0,1)`, put `C=kappa^2 Tr(T^2)>0`:

```text
L_F=C (partial_t h+partial_z h)^2/2,
EL_h=-C (partial_t+partial_z)^2 h.                      (2)
```

Nonzero transverse gradients can have zero action even though their curvature is nonzero. Thus positivity of the homogeneous `h_dot^2` coefficient does not establish a bounded physical Hamiltonian or well-posed full coupled dynamics. Constraints, boundaries, gauge fields and background fluctuations still matter. This term is conservative and contains no derived viscosity.

For a homogeneous profile, `I_h=C(n^0)^2`. If the internal direction or a parameterized `H_C(q)` changes, one must pull back its derivatives as well. This `I_h` cannot simply be added to the earlier probe inertia `I_theta=b^2/(2m)` without the common native map `H_C(b,theta,...)` and mode normalization. Rescaling `n` and inversely rescaling `kappa` leaves the connection fixed; the axis normalization must therefore accompany any physical coefficient identification.

There is a strict closure boundary: if the minimal functional gives `H_C=Lambda[M,P]=0` **identically on a spacetime branch**, this HC contribution and its derivatives vanish there. A zero value at one spacetime point does not imply zero derivative curvature. A nonzero independent HC excitation is not simultaneously the exact zero-defect closure branch. If HC is functionally defined rather than independently varied, its action variation must instead be propagated through `Lambda[M,P]`.

## 3. The Mixed-Hermiticity Issue

For constant `n` and the same suppressed closure background, assume ordinary Hermitian `A_mu,H_C` and define

```text
D_mu^A H = partial_mu H+i[A_mu,H],
F_A_mu_nu = partial_mu A_nu-partial_nu A_mu+i[A_mu,A_nu],
X_mu_nu = n_nu D_mu^A H-n_mu D_nu^A H,
F_mu_nu = i F_A_mu_nu+kappa X_mu_nu.                   (3)
```

Both `F_A` and `X` are Hermitian in their internal indices. The literal trace product contains a generically imaginary cross term, and

```text
Re L_F = +Tr(F_A_mu_nu F_A^mu_nu)/4
         -kappa^2 Tr(X_mu_nu X^mu_nu)/4.               (4)
```

For a purely electric mode, `Tr(Y_mu_nu Y^mu_nu)=-2Tr(Y_0i^2)`. Thus the two terms in (4) give opposite electric kinetic signs. Flipping the overall action sign flips both; it does not fix their relative sign.

The numerical witness uses `T=diag(1,2)`, `kappa=0.4` and an electric curvature with `F_0z=kappa T`. The compensator profile gives `Re L=+0.4`, the identical profile multiplied by `i` gives `Re L=-0.4`, and their sum gives `L=0.8i`. These are algebraic values in a declared test, not measured energies.

This is **not a native ghost theorem**. A different internal real form, adjoint, action pairing or field interpretation might change the analysis. Conversely, taking a real part, inserting a dagger, or absorbing `i` into `H_C` changes the conventions and potentially the probe/penalty equations; it must not be done invisibly. The scalar displayed currents do not decide this matrix-level question.

## 4. One Explicit Real Completion, Kept as an Alternative

An ordinary unitary-gauge-covariant comparison is

```text
L_dagger=-Tr(F_mu_nu^dagger F^mu_nu)/4
        =-Tr(F_A_mu_nu F_A^mu_nu)/4
         -kappa^2 Tr(X_mu_nu X^mu_nu)/4.               (5)
```

The dagger acts on internal indices; spacetime indices are still raised with the Lorentz metric. Under unitary gauge transformations `F -> U F U^dagger`, the trace is invariant, also for spacetime-dependent transformations of the full connection. The traced cross commutator vanishes. Both electric sectors now have the same positive coefficient, but the null HC tensor (1) remains rank one. An indefinite/nonunitary native carrier is not automatically covered by this ordinary adjoint.

For **independent** Hermitian `A_mu,H`, constant `n`, and compactly supported variations, varying this curvature action yields

```text
EL_A^nu = D_mu^A F_A^{mu nu}
          +i kappa^2 n_mu [H,X^{mu nu}],
EL_H = kappa^2 n_nu D_mu^A X^{mu nu}.                  (6)
```

Probe, matching-penalty, projector and other background contributions must be added from the same real full action. In particular (6) is **not automatically the printed complex resonance equation** with its existing currents. The script checks the noncommuting constant-field limit of both equations against independent variations of (5), as well as internal unitary covariance.

There is a useful concrete consequence of the already printed penalty. Set `H=h(t)T`, fixed `Lambda=h_Lambda T`, constant `h_Lambda`, `A=0`, and neglect other sources **only for this comparison**:

```text
L_h=I_h h_dot^2/2-lambda_H Tr(T^2)(h-h_Lambda)^2,
h_ddot+omega_H^2(h-h_Lambda)=0,
omega_H^2=2 lambda_H/[kappa^2(n^0)^2], lambda_H>0.      (7)
```

No extra stabilizing potential was invented: (7) uses the existing matching penalty. Nevertheless its independent-field interpretation, fixed target and source-free reduction are additional assumptions. A nonzero oscillation has `H!=Lambda` and cannot also obey exact matching as a separate constraint. The other fields can react to this mismatch. A local positive HC field can be arranged with `h_Lambda` larger than the oscillation amplitude, but positivity alone does not solve those other equations.

The ratio in (7) is not yet evaluated natively, the physical time/energy normalization is unknown, and a homogeneous oscillation frequency is not a relativistic particle-mass spectrum. No irreversible damping or selected root phase follows. The alternative therefore gives a coherent calculable candidate, not a declaration that the paper is now closed.

## 5. Which Full Equations Must a Null-Axis Ansatz Satisfy?

To expose the variational distinction, first consider an **independent real Abelian parent connection** with action `-Tr(F F)/4`. For the null-axis slice, with adjoint covariant differentiation reducing to ordinary differentiation, write

```text
E_nu=partial^mu F_mu_nu
     =kappa T[n_nu Box h-partial_nu(n.partial h)],
EL_h=kappa Tr(T n^nu E_nu).                            (8)
```

Thus the restricted equation tests only a contraction of the parent field equations. With the chosen axis, let `u=(partial_t+partial_z)h`. Then

```text
E_0=-kappa T partial_z u,       E_z=-kappa T partial_t u,
EL_h=-C(partial_t+partial_z)u.
```

Take `h=h_0+t cos(k(z-t))`. It has `u=cos(k(z-t))`, so `EL_h=0`, but

```text
E_0=+kappa k sin(k(z-t))T,
E_z=-kappa k sin(k(z-t))T.
```

These are generically nonzero, even though the Abelian identity `partial^nu E_nu=0` holds exactly. At the report's example point the residual norm is approximately `0.625176`, the tangent equation is zero, and the differential identity vanishes to numerical precision. Conservation identities do not supply the missing normal equations of this parent theory. For homogeneous commuting `h(t)`, its Gauss component `E_0` is zero; a nonzero temporal current would require other fields, flux or a matching cancellation.

**The field space matters.** For the alternative Hermitian-field action (5), that same commuting wave satisfies both curvature-only equations (6): the HC equation is the null contraction, and the gauge commutator source vanishes. It is not required to solve every component of the independent real parent equation (8). Hence the witness is not an automatic failure of the native allowed `A,H` variations. It becomes an extra test only if the source's full resonance equation is separately imposed in its adjoint interpretation. Interpreting its derivative as fundamental rather than adjoint would require a different computation again.

Nor has the example established vanishing of the native probe/closure/HC currents or solved their penalty and background equations. These must be calculated, not replaced by an invented compensating source. This is precisely why fixing the real action, field space and resulting currents together is the next prerequisite.

## 6. Verification and Next Native Step

Reproduce the machine-readable report with `python -B analysis/HC_Null_Axis_Action_Check.py --output analysis/HC_Null_Axis_Action_Check.json`. The focused suite has 42 tests: direct curvature, ordinary-trace contraction, kinetic Hessian/rank, electric signs, paired-action variation, covariance, smooth profile derivatives, full versus projected equations, differential identity, Gauss restriction and the existing-penalty oscillator. These are algebraic/numerical checks, not a proof-assistant certificate or evidence of empirical validity.

Before integrating a physical inertia or source into the main paper, specify its actual adjoint and real pairing, decide independent versus functionally constrained HC, derive all currents with those variations, and then substitute the same spacetime profiles into the probe, gauge, projector and HC equations. The field kinetic term is now explicit; its physical interpretation and full closure are not. No package installation, main-source edit, compiler run or Git operation is part of this follow-up.

The subsequent [real-probe/current calculation](HC_Real_Probe_Current_Closure.md) carries this candidate through the probe variation. In the declared factorized Hermitian realization a real symmetric action removes the ordered HC transport but retains its real Yukawa source and bosonic kinetic term. It derives the common matrix-current/Ward identity, the reaction of a noncentral matching target, an explicit nonunique open return model and the limits of absorbing transport into a moving positive comparison. These are distinct choices, not an adopted native action repair.
