# A Real Probe Action, Its Currents and the HC Transport Choice

Date: 2026-10-16. Status: exact variational/current identities in a declared factorized sector; a conditional real completion, not the native full field theory. No main TeX, empirical masses, selected phase, fitted restoring force or microscopic bath is introduced.

## Result

The [previous curvature calculation](HC_Null_Axis_Action_Check.md) can be coupled to a real probe action with explicit matrix sources. There is a substantive choice, however: under the usual Hermitian kinetic/adjoint conditions and a factorization in which internal fields commute with spin matrices,

```text
Re[i kappa bar(Psi) Gamma.n H_C Psi]=0.                 (1)
```

Taking the real action removes the original ordered HC transport term from the probe equation. It does **not** remove HC from the bosonic curvature action or its real `gamma H_C` mass-like coupling. That coupling supplies an explicit HC matrix source. The resulting source and gauge-current equations satisfy a common Ward identity, including the reaction of a noncentral matching background.

Keeping the ordered transport instead generally changes the declared probe norm. Three interpretations must be distinguished: a changed conservative real probe law, an open/conditional law with a specified return or reservoir, or a genuinely derived moving comparison. None is obtained merely by calling the existing complex expression real. The existing QAM comparison has not been identified with a spacetime kinetic metric.

## 1. Exactly Which Conventions Are Assumed?

Use commuting effective probe amplitudes on `V_gen tensor S_spin`, Hermitian internal `A_mu,H`, and

```text
bar(Psi)=Psi^dagger eta_D,       eta_D^dagger=eta_D,
K^mu=eta_D Gamma^mu,            (K^mu)^dagger=K^mu,
W=eta_D Omega,                 W^dagger=W.             (2)
```

Take `K^mu` constant in this calculation and `K^0>0` when interpreting the temporal integral as a positive norm. The physical adjoint also needs a nondegenerate carrier and the native gamma/Clifford and boundary conventions. Neither the native full gamma representation nor this factorization is derived here. In particular, an internal mismatch metric is not automatically the spinor time norm. These are classical/effective amplitude variations, not a calculation of quantum fermion expectation values or a Grassmann path integral.

The [printed field package](../sources/research/parts/v470/10_sphaera_and_physics.tex), `thm:variational-form`, inserts a Hermitian HC load through

```text
D_mu=partial_mu+i A_mu+kappa H n_mu+eta(I-P_C7)n_mu.
```

Internal operators commute with spin weights in the declared factorization. Therefore `bar(Psi) Gamma.n H Psi` is real: its matrix weight is the commuting Hermitian product `(K.n)H`. Multiplication by `i kappa` makes this contribution purely imaginary. The same statement holds for the Hermitian closure load, without identifying it with HC.

In a nonfactorized realization the exact rule is instead

```text
Herm(i K.n H)=i[K.n,H]/2.                              (3)
```

It may retain a Hermitian commutator interaction, but it still does not equal the original ordered term in general. Native noncommutation or an indefinite/modified adjoint must be evaluated rather than presumed absent or presumed to solve the issue.

For constant Hermitian `K^mu`, the real part of the ordered derivative term is exactly

```text
L_kin=i[Psi^dagger K^mu partial_mu Psi
       -(partial_mu Psi^dagger)K^mu Psi]/2.
```

Symmetrizing with a true conjugate is essential. A formally left-acting derivative with the opposite HC sign is not automatically that conjugate when the connection contains a Hermitian non-unitary part. Treating `bar(Psi)` as an independent formal variable is possible, but requires its real field space, adjoint relation and physical norm to be specified.

## 2. A Common Real Gauge--HC--Probe Action

Isolate a test sector with constant real `n`, the alternative paired curvature action from the previous note, a central bare coefficient `m`, and `Omega=m I+gamma H`. Suppress other projector/triadic/background interactions **only for this sector calculation**, not because their full equations have been solved. In particular, a separate Hermitian matching target `Lambda` here is not asserted to be the native minimal `Lambda[M,P]` on an exactly closed carrier.

Let `D_mu^A=partial_mu+i[A_mu,.]` on adjoint fields and

```text
F_A_mu_nu=partial_mu A_nu-partial_nu A_mu+i[A_mu,A_nu],
X_mu_nu=n_nu D_mu^A H-n_mu D_nu^A H,
F_mu_nu=i F_A_mu_nu+kappa X_mu_nu.
```

The explicitly **alternative** real action is

```text
L = L_kin-Tr(A_mu j^mu)-m Tr(S)-gamma Tr(H S)
    -Tr(F_A_mu_nu F_A^mu_nu)/4
    -kappa^2 Tr(X_mu_nu X^mu_nu)/4
    -lambda_H Tr[(H-Lambda)^2],                       (4)
lambda_H>0.
```

The bosonic part equals `-Tr(F^dagger F)/4`; it is not the literal printed `-Tr(F F)/4`. This is a candidate completion, not a silent native correction. Its internal gauge transformations are declared unitary transformations of the generation carrier; that carrier/group has not been matched to the actual Millennium operator.

The matrix currents are fixed by (4):

```text
j^mu=Tr_spin[(I_gen tensor K^mu)|Psi><Psi|],
S=Tr_spin[(I_gen tensor eta_D)|Psi><Psi|].              (5)
```

For amplitudes written with generation rows and spin columns, these are `Psi (K^mu)^transpose Psi^dagger` and `Psi eta_D^transpose Psi^dagger`. They are Hermitian; `S` need not be positive. The transpose is required by the row convention and is not an adjoint.

With `R=EL_{Psi^dagger}`, the independent-field equations are

```text
R=i K^mu partial_mu Psi-K^mu A_mu Psi-W Psi=0,

E_A^nu=D_mu^A F_A^{mu nu}
       +i kappa^2 n_mu[H,X^{mu nu}]-j^nu=0,

E_H=kappa^2 n_nu D_mu^A X^{mu nu}
    -2lambda_H(H-Lambda)-gamma S=0.                   (6)
```

Tensor order is implicit in the first line; internal and spin factors commute in this sector. In particular the HC probe source is `-gamma S`, with **no surviving `i kappa K.n` source in the real action**. The missing transport is not reintroduced by claiming the bosonic HC kinetic term is still present.

At fixed independent `H,Lambda`, the matching penalty has no explicit `A_mu` dependence. It contributes an algebraic HC reaction, not a direct gradient-trace gauge current. The printed `lambda_H partial_nu Tr(H M16)` and closure trace current are therefore not automatically recovered by (4). Their intended representation or extra interaction must be supplied. An algebraic functional `Lambda[M,P]` requires the corresponding chain rule and background equations, not an invented current.

## 3. Conservation Checks the Background as Well

For a covariantly transforming matching background, define its reaction for bookkeeping,

```text
E_Lambda=2lambda_H(H-Lambda).
```

This is **not** a new instruction to vary `Lambda` freely or impose `E_Lambda=0`. Under `U=exp(i epsilon)`, the infinitesimal transformations are

```text
delta A_mu=-D_mu^A epsilon,
delta H=i[epsilon,H],       delta Lambda=i[epsilon,Lambda],
delta Psi=i epsilon Psi.
```

Gauge covariance of (4), allowing the background to transform as a spurion, gives the off-shell identity

```text
D_mu^A E_A^mu+i[H,E_H]+i[Lambda,E_Lambda]
  +i Tr_spin(Psi R^dagger-R Psi^dagger)=0.             (7)
```

Here a spurion is a prescribed background assigned a transformation rule; it is not thereby a solved dynamical field. For the probe part alone, direct differentiation gives

```text
D_mu^A j^mu+i gamma[H,S]
  =i Tr_spin(Psi R^dagger-R Psi^dagger).
```

On shell `D_mu^A j^mu=-i gamma[H,S]`. This is a matrix charge exchange with the adjoint HC field. Its ordinary trace vanishes, so the global probe `U(1)` current is conserved. An adjoint HC field is neutral under the central `U(1)`; it cannot silently absorb a missing amount of that charge. Energy and noncentral charge exchange are different questions.

The complete identity has a useful consistency consequence. If all `A,H,Psi` equations (6) hold while a noncentral `Lambda` remains fixed and no other reactions are included, then

```text
[Lambda,E_Lambda]=0  ==>  [H,Lambda]=0.                (8)
```

This requires commutation, **not** exact equality. A central target satisfies it automatically. For a native functional target `Lambda[M,P]`, transfer the reaction to the allowed `M,P` variations via the variational chain rule. Their covariant reactions replace the spurion term in (7); omitting them is not a proof that (8) must hold in every native completion. Tangent projector variations and prescribed external backgrounds must be treated consistently.

The finite noncommuting test has a Ward residual around `2e-17`, but a nonzero omitted-target torque around `0.04243`. It is deliberately **off shell**. Neither it nor the homogeneous probe below solves the full Gauss equation. Indeed, constant matrix curvature/commutator terms have zero ordinary trace and cannot support the positive central `j^0` of a homogeneous isolated probe without spatial flux or other charge data.

## 4. What the Original Ordered Transport Does to the Norm

Keep the original equation instead of the real-action equation, with (2), constant kinetic weights and no additional anti-Hermitian mass term. Directly pairing it with its actual adjoint gives

```text
partial_mu(Psi^dagger K^mu Psi)
  =-2 kappa Psi^dagger(K.n)H Psi
   -2 eta Psi^dagger(K.n)(I-P_C7)Psi.                 (9)
```

This need not be an attenuation: its sign depends on orientation, coefficients, representation and state. Positivity of `H` alone does not fix it. If `K^mu` varies, add `Psi^dagger(partial_mu K^mu)Psi`; if `W` is not Hermitian, add `i Psi^dagger(W^dagger-W)Psi`. Such terms require their own native specification.

The executable example is an embedded **1+1-dimensional spin test**, not a full native 3+1 gamma representation:

```text
eta_D=sigma_z,   K^0=I,   K^z=sigma_x,   K^x=K^y=0,
n_mu=(1,0,0,1),  K.n=I+sigma_x,
H=diag(0.7,1.2), kappa=0.4.
```

Choose the first internal mode and the normalized `sigma_x=+1` spinor. At the sample instant its norm is `1`. The real-action law gives `N_dot=0`; the ordered law gives `N_dot=-1.12`, exactly matching (9). Reversing `n` reverses the ordered source. These are dimensionless algebraic inputs, not measured couplings or a native choice of null-axis orientation. A spinor instantaneously in `ker(K.n)` is a special case; subsequent evolution need not preserve that kernel.

Thus a single closed real probe with the **fixed declared norm** does not implement the active ordered attenuation. This is not a contradiction theorem for every possible interpretation of the paper's probe, whose physical probability and adjoint remain unspecified.

## 5. An Open Completion Exists but Is Not Determined

In a positive modal realization, suppose the ordered evolution actually has `f_dot=(-i H_modal-D)f`, with `H_modal` Hermitian and `D>=0`. This positivity is an additional check; the full gamma-ordered native HC term need not have it. Its unnormalized conditional density obeys

```text
rho_dot_cond=-i[H_modal,rho]-{D,rho},
Tr(rho_dot_cond)=-2Tr(D rho).
```

One explicit trace-preserving comparison adds a return term:

```text
L_jump=sqrt(2D),
rho_dot=rho_dot_cond+L_jump rho L_jump^dagger.          (10)
```

This is a concrete mathematical completion, not a derived native environment. Positivity can be checked without assuming a microscopic mechanism. For a small nonnegative step with `2dt lambda_max(D)<=1`, take

```text
M0=exp(-i H_modal dt) sqrt(I-2dt D),
M1=sqrt(dt)L_jump,
rho_next=M0 rho M0^dagger+M1 rho M1^dagger.
```

Every positive input stays positive, and `M0^dagger M0+M1^dagger M1=I` gives exact trace preservation. Expansion to first order yields (10). Tests verify both the finite-step statement and convergence of its generator.

For the norm example, the conditional trace rate `-1.12` is balanced by a return rate `+1.12`. However, replacing `L_jump` by `V L_jump` with unitary `V` keeps the same `L_jump^dagger L_jump=2D` and the same conditional decay, while generally changing the return. The ordered loss does not determine the complete dynamics or identify where information went. A return within the modal space, a charged sink in an enlarged carrier and a geometric reservoir are distinct completions. No such reservoir, gravity-mediated channel, jump law or irreversible viscosity has been extracted from the native action.

## 6. A Moving Comparison Is a Separate Route

For a time-chart generator `f_dot=G f` and a positive comparison `Q_kin(t)`, the exact conservation condition is

```text
Q_kin_dot+G^dagger Q_kin+Q_kin G=0.                    (11)
```

Given an invertible evolution `U(t)`, the formal construction `Q_kin(t)=U(t)^(-dagger) Q_kin(0) U(t)^(-1)` always supplies such a norm locally in this finite model. For example `G=-D`, `Q_kin=exp(2Dt)` and `f=exp(-Dt)f0` conserve `f^dagger Q_kin f`. This is a choice derived from an already chosen evolution, not a physical derivation of the paper's QAM comparison, root Gram or spacetime metric. A real symmetric action with a varying kinetic coefficient also has its derivative term; it must not be analyzed with constant (2).

Changing a physical comparison also requires reconsidering the adjoint in the curvature pairing and the probe/matching norms, not only renormalizing the final output. Those simultaneous native changes have not been made here.

A stronger geometric proposal is a **positive internal bundle comparison** compatible with the whole connection `B_mu`:

```text
partial_mu Q_kin=B_mu^dagger Q_kin+Q_kin B_mu.
```

Commuting two ordinary derivatives then requires

```text
F_mu_nu^dagger Q_kin+Q_kin F_mu_nu=0.                  (12)
```

For the pure commuting HC wedge from the previous note, `F_mu_nu` is ordinary Hermitian. If `F v=lambda v`, (12) gives `2 lambda v^dagger Q_kin v=0`. Strict positivity makes every `lambda` zero, hence `F_mu_nu=0`. Thus this strong positive-bundle route cannot absorb **nonzero pure Hermitian HC curvature** as metric transport.

It does allow a flat example: constant Hermitian `H`, `B_mu=kappa n_mu H` and `Q_kin(x)=exp(2 kappa H n_mu x^mu)` obey the compatibility equation with `F=0`. The ordered amplitude change can then be a comparison change, but the HC curvature kinetic term is absent in that branch. A non-Hermitian full curvature can also be skew in a different positive comparison; the tests include such a counterexample to an overbroad conclusion.

This is **not** a general no-go for the complete noncommuting connection, an indefinite spin adjoint, a restricted physical subspace or the weaker contracted Dirac-current condition. In particular, the positive internal `Q_kin` here must not be confused with the indefinite `eta_D`. The native QAM transport law and its identification with these kinetic data are still missing.

The relevant retained definitions do not yet make that identification. The two-sided QAM block in `07_qam_infrastructure.tex`, `def:two-sided-admissible-contractions` and `ex:two-sided-residual-comparison`, requires a named comparison for residual channels; it does not set its values to the Dirac time metric or impose (11). In the Einstein reconstruction in `10_sphaera_and_physics.tex`, `prop:bilinear-einstein-reconstruction`, metric compatibility is assumed for the induced spacetime metric after a geometric/internal decomposition. That is a different condition from positive internal bundle compatibility or an evaluated probe adjoint. The earlier quaternionic inner product used for basis orthogonality likewise needs a representation map before becoming any of these kinetic data.

Nor is changing `kappa H n_mu` to `i kappa H n_mu` a harmless way to retain all conclusions. With an independent unrestricted `A_mu`, that Hermitian vector shift can be absorbed into `A_mu+kappa H n_mu`; curvature then depends on the total vector connection. A separately derived HC kinetic mode cannot be inferred by freezing `A_mu` before that field redefinition. Its other couplings and penalty would have to be reanalyzed.

## 7. Outcome and Verification

There is now a common, explicitly conditional real action for the gauge--HC--probe sector, with matrix currents, HC source and background-aware Ward identity. The calculation also makes precise why real-action dynamics, ordered norm-changing transport and moving comparisons are not interchangeable. The next native decision is to supply the actual adjoint/comparison and choose which interpretation is intended, then evaluate its projector, native mass/triadic backgrounds and spatial solutions under the same variations.

The next [bilinear geometry bridge](HC_Bilinear_Geometry_Bridge.md) follows the existing coframe reconstruction rather than identifying QAM residual comparisons with a kinetic metric. It proves a conditional flatness result for the HC-free fixed-frame branch, derives a null-preserving HC deformation and constructs it from the same local probe amplitudes. A logarithmic profile matches an isolated Einstein tensor to paired HC stress. The null-aligned probe can be directly HC-transport-dark while geometrically active, but the follow-through finds a nonconserved induced current and excludes the direct same-induced-frame ordered master equation with real mass bilinear. This is a stronger boundary than an unsolved A=0 Gauss source; the off-shell matching is not native variational closure or a universal no-go for separate microscopic/effective geometries.

Reproduce the report with `python -B analysis/HC_Real_Probe_Current_Closure.py --output analysis/HC_Real_Probe_Current_Closure.json`. Forty-two focused tests cover direct bilinears, real and complex variations, local unitary covariance, current/Ward identities, norm balance, external background reaction, positive finite-step return, nonunique open completions and moving-metric integrability. They are numerical/algebraic regressions, not a proof-assistant certificate or validation of the full paper. No package installation, main-source edit, compiler invocation or Git operation is required.
