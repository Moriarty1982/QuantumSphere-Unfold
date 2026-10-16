# HC, the Native Bilinear Coframe and a Local Curved Geometry

Date: 2026-10-16. Status: exact conditional coframe identities, a constructive common-probe realization and local Einstein/HC stress matching, now followed through to current conservation and a conditional same-frame exclusion. This is not a complete native field solution, a derivation of Newton's constant, a repaired Einstein-limit theorem or an edit to the main TeX.

## Result

There is a concrete geometric coupling to investigate. The [native Einstein reconstruction](../sources/research/parts/v470/10_sphaera_and_physics.tex), `prop:bilinear-einstein-reconstruction`, defines

```text
E^a_mu=Re[bar(Psi_triangle) Gamma^a D_mu Psi_triangle],
g_mu_nu=eta_ab E^a_mu E^b_nu,       eta=diag(-1,1,1,1).
```

Unlike the `i`-weighted transport in the real probe action, the real HC contribution to **this** coframe survives the Hermitian factorized interpretation. It changes the coframe by a rank-one term and can produce curvature while preserving the same null axis. A local logarithmic profile explicitly matches the resulting Einstein tensor to the paired HC-curvature stress in an isolated, independently varied metric sector.

This is a real advance in the mathematical connection, but not native closure: the example retains an unsolved probe/gauge source, omits other stresses and requires a nonzero HC branch different from exact minimal closure. Also, restricting to this null profile **before** variation misses the remaining Einstein equation. The boundary is demonstrated rather than hidden.

**Follow-through.** Sections 7--9 establish a stronger boundary: the unchanged transverse probe construction has induced-current divergence `8`, and identifying the master equation's gamma matrices directly with the inverse of this real bilinear coframe is impossible on shell when its mass bilinear is real. The short pointwise trace identity applies more broadly than this example. It excludes that additional same-frame identification, not every separate microscopic/effective interpretation of the paper. The earlier local geometry/stress calculation remains valid as a conditional off-shell construction.

## 1. A Useful Identity in the Existing Reconstruction

Continue the [real-probe/current analysis](HC_Real_Probe_Current_Closure.md) with fixed Hermitian frame weights `K^a=eta_D Gamma^a`, an internal/spin factorization, Hermitian internal `A_mu,H`, and constant `n`. The physical native adjoint and carrier map are still uncomputed. Suppress the closure load for this calculation; it vanishes on a probe with `(I-P)Psi=0`, but the other closure equations remain separate obligations.

Define the real frame current and HC-weighted current

```text
j^a=Psi^dagger K^a Psi,
v_H^a=Psi^dagger K^a H Psi.
```

For constant Hermitian `K^a`, direct differentiation gives

```text
Re[Psi^dagger K^a partial_mu Psi]=partial_mu j^a/2,
Re[i Psi^dagger K^a A_mu Psi]=0,
E^a_mu=partial_mu j^a/2+kappa v_H^a n_mu.              (1)
```

The second identity uses internal/spin commutation. Thus a pure internal unitary gauge field drops out of this particular real coframe, while HC does not. This complements the earlier real-action calculation; it does not undo its cancellation of `Re(i kappa bar(Psi) Gamma.n H Psi)`.

An important special case follows. If HC vanishes and the coframe has rank four, put `Y^a=j^a/2`. Then `E^a=dY^a`, and

```text
g=eta_ab dY^a dY^b
```

is locally flat in the coordinates `Y`. Rank four by itself does not generate Einstein curvature in this branch. A nonzero HC contribution, varying Clifford/adjoint data, a nonfactorized geometric spin connection or a different justified reconstruction is needed to escape this statement. The source's geometric/internal decomposition could matter precisely here, but its representation has not been evaluated. The statement concerns the direct fixed-frame reconstruction, not an arbitrary coarse-grained metric or every native completion.

For varying `K^a`, (1) acquires `-Psi^dagger(partial_mu K^a)Psi/2`; a spin connection need not commute with `K^a` and can also contribute. These are legitimate missing terms, not evidence that the flatness result applies to them.

## 2. Exact Rank-One Geometry and Null-Axis Preservation

Write (1) as a real matrix, with frame rows and coordinate columns:

```text
E=E0+kappa v n^T,
g0=E0^T eta E0,       w=E0^T eta v,
g=g0+kappa(n w^T+w n^T)+kappa^2(v^T eta v)n n^T.       (2)
```

For invertible `E0`, let `a0=E0^(-1)v` and `d=1+kappa n^T a0`. Then

```text
det E=det E0 d,
E^(-1)=[I-kappa a0 n^T/d]E0^(-1),
n^T g^(-1)n=(n^T g0^(-1)n)/d^2.                      (3)
```

Thus an initially null `n` remains null for **every** nonsingular update of this form, not only a specially aligned one. The denominator `d=0` is a real coframe degeneracy and is excluded. The HC contribution alone has rank at most one and cannot supply a four-dimensional nondegenerate metric.

With constant `n`, `dE^a=kappa dv^a wedge n` on the gradient baseline. Nonzero `dE` is not by itself proof of Riemann curvature: an explicit linear profile below has nonconstant/anholonomic coframe data but zero Riemann tensor. Curvature is computed from the metric, not inferred from that visual feature.

## 3. A Curved Null Profile From the Same Probe Amplitudes

Take

```text
E0=I,       n_mu=(-1,0,0,1),       l^a=(1,0,0,1),
eta l=n,    v_H=h(x,y)l,
E=I+kappa h l n^T,
g=eta+2kappa h n n^T.                                (4)
```

Here `n^T l=0`, so `det E=1`, `det g=-1`; signature stays Lorentzian and `n` stays null. This is an aligned null metric deformation. No claim of a wormhole, a photon rest frame or information transport between physical frames follows from it.

The baseline and HC direction in (4) can be realized by the **same** local probe; they need not be chosen independently. Use a declared four-component spin representation with

```text
eta_D=beta=diag(I2,-I2),
K^0=I4,       K^i=alpha_i=[[0,sigma_i],[sigma_i,0]],
Gamma^a=beta K^a,       {Gamma^a,Gamma^b}=-2eta^{ab}I.
```

This explicitly states the Clifford sign convention. It is not an identification with the native `C7/M16` carrier. Choose three internal spinor amplitudes, `Psi_1=(1,0,1,0)/sqrt(2)` with current `l`, `Psi_3=0`, and `H=diag(h,0,0)`. On a patch, set the required second current to

```text
J^a=2(x^a+c^a)-l^a,       c=(3,0,0,0),
J^0>|J_spatial|.
```

For this future timelike current define `m_J=sqrt((J^0)^2-|J_spatial|^2)`, `chi=(1,0)`, and

```text
Psi_2=sqrt((J^0+m_J)/2)
      [chi; (sigma.J_spatial)chi/(J^0+m_J)].            (5)
```

It satisfies `Psi_2^dagger K^a Psi_2=J^a`. Hence the total current is `j^a=2(x^a+c^a)`, its gradient gives `E0=I`, and HC weights only the fixed null-current mode: `v_H=h l`. The analytic spinor derivatives and direct coframe evaluation agree; this is a smooth local, positive-HC kinematic realization when `h>=0`.

Equation (5) is **not** a solved Dirac equation. Nor is an arbitrary three-by-four realization the native septonic factorization. Its purpose is to check consistency of the bilinear dictionary before asserting dynamics.

There is a useful special feature: `n_a v_H^a=0`, and more strongly `(Gamma.n)H Psi=0` for this constructed null-spin alignment. Pulling `n_mu` into the induced frame leaves it unchanged. HC is therefore geometrically active here while its direct ordered null transport annihilates the chosen probe, even before taking a real part. This avoids a direct HC norm source **on this ansatz**, not on arbitrary states. Its mass-like coupling is not annihilated in the same way, and the full mass/gauge/triadic evolution can leave the alignment. Persistence must be proved rather than inferred from the current formula.

For transverse `h(x,y)`, the Levi--Civita calculation from (4) gives

```text
Ricci_mu_nu=-kappa Delta_perp h n_mu n_nu,
R=0,
R_mu_i_nu_j=-kappa (partial_i partial_j h)n_mu n_nu,
                 i,j in {x,y}.                       (6)
```

The code independently builds Christoffel symbols and their derivatives from metric jets and checks the full Riemann tensor and symmetries. The null axis is parallel in this metric. Both `R` and the Kretschmann scalar can vanish while the Riemann tensor is nonzero; those scalar zeros are not flatness proofs. For linear `h`, the Hessian and full curvature instead vanish.

## 4. Conditional Einstein/HC Stress Matching Can Be Solved

There is also a calculable stress. Adopt the previous **alternative paired curvature action**, vary an independent, unconstrained metric at fixed covector `n` and curvature components, and only then evaluate on (4). For `H=h T` with fixed Hermitian `T`, `c_T=Tr(T^2)>0`, `A=0`,

```text
F_mu_nu=kappa T[(partial_mu h)n_nu-n_mu partial_nu h],
Tr(F^dagger_mu_nu F^mu_nu)=0,
T_mu_nu^HC=kappa^2 c_T |grad_perp h|^2 n_mu n_nu.      (7)
```

Zero action density does not imply zero metric stress. The null stress coefficient is nonnegative and its covariant divergence vanishes on this specific profile. A metric-enforced null constraint, a varying adjoint/comparison or extra metric dependencies changes the variation and can add terms; (7) must not be imported into those variants silently.

For an isolated Einstein-metric matching exercise, set the cosmological term to zero and omit probe, penalty and other collective stresses. Treat the source's effective Einstein coupling `kappa_eff` as an **input**, not a derived Newton/Planck scale. Equations (6)--(7) then obey `G_mu_nu=kappa_eff T_mu_nu^HC` precisely when

```text
Delta_perp h+a |grad_perp h|^2=0,
a=kappa_eff kappa c_T,       kappa!=0.                 (8)
```

For `a!=0`, this becomes a linear harmonic equation after a change of variable:

```text
F=exp(a h),       Delta_perp F=0,
h=log(F)/a.                                          (9)
```

A positive affine harmonic function `F=F0+b_x x+b_y y` supplies explicit local profiles on `F>0`. Restrict further to `log(F)/a>=0` if a positive HC field is required. This is a patch construction, not global regularity or positive asymptotic/boundary data.

For the unfitted dimensionless test `kappa=0.4`, `kappa_eff=1`, `c_T=1`, `F=2+0.1x`, at `x=0.2,y=0.3`,

```text
h=1.7577437785327834,
-kappa Delta h=0.0024507401235173026,
kappa_eff kappa^2 c_T |grad h|^2=0.0024507401235173026.
```

The full Einstein/HC stress mismatch is around `3e-18` in the test. The Riemann tensor is nonzero. Its displayed component norm is a numerical diagnostic, not a coordinate-invariant curvature magnitude. Other `c_T` values require a joint normalization of the probe/HC dictionary; the explicit common-probe realization above uses `T=diag(1,0,0)` and `c_T=1`.

This is a conditional **geometry/stress match**, not the full native equations. A harmonic `h` with nonzero gradient, for example, has zero Ricci but nonzero HC stress and fails (8); calling it a vacuum profile would discard a retained source.

## 5. The Action Must Be Varied Before the Null Restriction

If the effective action genuinely depends on the induced metric, its geometric contribution to HC is a real chain-rule source. Define the metric Euler tensor by

```text
delta S_metric=integral sqrt|g| Ecal^{mu nu} delta g_mu_nu/2.
```

At fixed probe, adjoint, spin frame and `n`, the coframe formula gives

```text
delta_H E^a_mu=kappa n_mu Tr(j^a_matrix delta H),
delta_H S_metric=kappa integral sqrt|g|
  n_mu Ecal^{mu nu} eta_ab E^a_nu Tr(j^b_matrix delta H). (10)
```

Here `j^a_matrix` is the generation-resolved current from the previous note. The script checks (10) by independent metric variations. It shows how HC can couple to a real geometric action even when its direct imaginary probe transport is absent. It does **not** add that effective metric action to the original source without deriving its coarse-graining and coefficients.

There is a sharp variational trap in the explicit example. On the entire transverse null family (4), the bulk Einstein--Hilbert scalar and the HC curvature scalar are both zero. Restricting those bulk terms to this family before variation therefore loses equation (8). With controlled boundary data this is a missing normal equation, not proof of full stationarity.

Equivalently `delta_h g_mu_nu=2kappa delta h n_mu n_nu`, while a residual with lower components `Ecal_mu_nu=C n_mu n_nu` satisfies

```text
Ecal^{mu nu} delta_h g_mu_nu=0
```

even when `C!=0`. In fact the HC source (10) also misses this residual, since `n_mu Ecal^{mu nu}=0`. The numerical nonmatching example has full residual norm `0.000416` but vanishing tangent contraction. This is an explicit geometric counterpart of the earlier omitted-normal-mode tests.

If `g` is defined from the probes, its action must be pulled back to **all** allowed probe, connection, projector and HC variations. Higher-derivative dependence uses the differential variational adjoint. Alternatively, treating `g` independently requires a justified change of variables or a multiplier enforcing its definition; such a multiplier contributes to the other equations and may change the metric equation. One cannot assume both a composite metric and unmodified independent-metric Einstein equations at once.

## 6. The Remaining Native Gap Is Concrete

The same explicit amplitudes (5) have a nonzero gauge charge. With `A=0`, commuting HC and no other gauge source, the paired gauge equation has zero curvature/commutator left side but nonzero `j^0`. Its residual norm at the sample point is about `5.474814`. Thus the geometric example **fails that full gauge equation** in the declared completion. The follow-through below strengthens this observation: an internal unitary gauge field alone cannot repair the unchanged nonconserved probe/current ansatz. A different joint probe/background solution would be needed, not merely an additional gauge potential for the existing source.

Matching-penalty, probe, projector and noncentral native mass/triadic stresses have likewise not been included in (8). The spinor/current ansatz is not an on-shell solution. Coordinate gamma matrices and the geometric spin connection must also be reconstructed from the same induced frame; one cannot continue using a frozen flat-space time equation without that check. The source's minimal exact-closure branch has `H_C=Lambda=0`; a nonzero HC profile does not simultaneously satisfy that Einstein-limit premise. Retaining HC there needs a justified independent/deeper-field completion or a different nonminimal closure functional. A geometric spin connection is another possible curvature source and need not obey the factorized cancellation in (1).

What is now established is narrower and useful: the actual coframe formula admits a real HC geometric contribution; the same local probe can realize it; its null geometry, curvature and paired stress can be computed; and one isolated matching equation has explicit logarithmic solutions. No mass phase, viscosity, information reservoir, wormhole, native Newton constant or complete Einstein/probe solution is obtained.

## 7. The Induced Current Fails Conservation Before Solving for A

The coordinate current of the same induced-frame Dirac interpretation is

```text
J^mu=e_a^mu j^a,       e=E^(-1),
div_g J=|det E|^(-1) partial_mu(|det E| J^mu).          (11)
```

This uses the induced volume and inverse frame, not just derivatives of flat-frame components. The real closed probe action has a common phase symmetry, and its on-shell traced current must be conserved. In the adopted fundamental `U(N)` gauge completion this is also the central gauge-current condition. More generally the phase-current test still applies even if a smaller gauge algebra is chosen. Matrix HC charge-exchange commutators have zero ordinary trace.

For the transverse null example put `Y=x+c`, `s=n_mu Y^mu`. The previous inverse-frame formula gives

```text
J^mu=2Y^mu-2kappa h s l^mu,       |det E|=1,
div_g J=8-2kappa s(l.partial h)=8,                   (12)
```

since `n.l=0` and `h=h(x,y)`. This holds for every transverse profile, including the logarithmic Einstein/HC stress match and zero HC. It is not cured by rescaling that transverse profile or adding a purely internal Hermitian `A_mu`: that gauge field does not change the real coframe, and `Tr[A_mu,j^mu]=0` cannot cancel the central divergence. The values `8` here and `4` below refer to the declared dimensionless coframe/current normalization, not a predicted physical production rate.

The HC-free full-rank gradient case has the same invariant problem. In the local coordinates `Y=j/2` its coframe is `dY`, metric is Minkowski, and current is `J^a=2Y^a`, so `div J=8`. It is not an artifact of the particular spinor parametrization (5). A nonlinear-coordinate test includes the nonconstant volume and verifies this statement independently.

Allowing a longitudinal derivative of `h` could satisfy the necessary condition `l.partial h=4/(kappa s)` on a patch with `s!=0`. That leaves the previous transverse/null-stress calculation, and it still does not solve the master-equation obstruction below. Current conservation is necessary, not sufficient.

In the fixed Hermitian branch the real coframe is invariant even under a local common phase with fixed `A`: the added `i(partial_mu alpha)j^a` has zero real part. A real geometric action depending only on that phase-blind coframe therefore does not supply an automatic compensating central phase current. Extra sources or modified equations must follow from a specified full action and its Ward identity, not be adjusted to subtract `8`.

## 8. A Short Same-Frame Trace Obstruction

This result has fewer assumptions than the gradient/continuity argument. Let

```text
B^a_mu=bar(Psi)Gamma^a D_mu Psi,
E^a_mu=s0 Re B^a_mu,       s0 real, finite, nonzero,
e=E^(-1),
Gamma^mu=e_a^mu Gamma^a.                             (13)
```

The last line is an **additional identification**: the coordinate gamma matrices in the written master equation are assumed to be those of this very induced coframe. The same probe, adjoint and derivative must be used in both formulas. The inverse frame here is an ordinary real classical matrix, as in the displayed metric reconstruction. An operator-valued noncommuting frame would need a different ordered definition. It is not enough merely to use the same letter `Gamma` in two different effective descriptions.

Invertibility and real `e` give

```text
4=e_a^mu E^a_mu
 =s0 Re[bar(Psi)Gamma^mu D_mu Psi].                   (14)
```

Now use the displayed ordered master residual and its mass bilinear:

```text
R=(i Gamma^mu D_mu-Omega)Psi,
w=bar(Psi)Omega Psi.
```

Multiplying by the same adjoint and taking the imaginary part yields the exact pointwise identity

```text
Im[bar(Psi)R]=4/s0-Im w.                             (15)
```

Consequently an on-shell full-rank coframe of this form requires `Im w=4/s0`. If the mass/resonance bilinear is real, this is impossible. A sufficient usual reality condition on the finite carrier is `(eta_D Omega)^dagger=eta_D Omega`; Euclidean Hermiticity of `Omega` alone is not sufficient if it does not commute with the adjoint. The tested central mass plus internal real HC Yukawa term meets the weighted reality condition.

The argument is not a perturbative estimate. It does not require a particular HC profile, a weak field, a positive probability metric, an internal/spin factorization of `Omega`, or solving the gauge equation. It does not even use a Clifford identity beyond the identification in (13). Adding a spin connection or changing the connection components cannot evade it **while preserving all the same-field/same-frame assumptions and the written master equation**. Such changes may escape the earlier gradient flatness identity without escaping (15).

A finite nonzero real normalization `s0` changes `4` to `4/s0`, not to zero. For commuting effective amplitudes the Cauchy inequality also gives

```text
||R|| >= |4/s0-Im w| / ||eta_D Psi||.                 (16)
```

At the existing sample, with unfitted central mass `0.6` and HC Yukawa coefficient `0.2`, the induced-frame calculation has

```text
Im w=0,
Im[bar(Psi)R]=4,
||R||=2.4559213537600737,
||R|| >= 4/sqrt(6)=1.6329931618554523.
```

Varying real mass/Yukawa coefficients or internal Hermitian gauge potentials leaves the imaginary contraction unchanged. A test with a fully nonfactorized weighted-Hermitian mass operator verifies that the argument is not confined to a diagonal internal toy mass.

Two negative controls delimit the result. A deliberately chosen nonreal image `Omega Psi=i Gamma^mu D_mu Psi` makes `R=0` and `Im w=4/s0`, precisely by dropping the real-bilinear hypothesis. That state-fitted image is not a native operator construction or a proposed physical repair. Conversely one can satisfy the reference-gamma master equation at a point and obtain an invertible real coframe, yet fail the equation after replacing the reference gammas by the induced ones. Thus the same-frame identification is essential; the test does not exclude every reference-probe/effective-metric architecture.

## 9. What Can Legitimately Change Next?

The native `thm:master-field-equation` and `prop:bilinear-einstein-reconstruction` have both been read here. The displayed reconstruction calls `Gamma^a` a fixed Clifford frame, while the current effective route does not yet derive a microscopic-to-induced identification of `Gamma^mu`. Its coarse-graining and geometric/internal split are explicitly model-dependent. Equation (15) excludes the direct standard identification just tested; it is **not** a universal inconsistency theorem for the whole paper.

There are distinct possible research directions, none implemented as an invisible correction:

1. Keep microscopic/reference gamma matrices and the effective metric separate, and derive their common action, scale transfer, currents and backreaction. Simply naming one quantity coarse-grained does not supply that relation. If the same induced inverse frame factors through an average of the same on-shell real bilinear, the trace identity still applies.
2. Change the coframe functional explicitly. For example the real kinetic combination `-Im(bar(Psi)Gamma^a D_mu Psi)` changes the on-shell trace condition to `4/s0=Re w`; it does not prove existence, and a massless real `w=0` still fails that direct identification. It also removes the simple real HC contribution used in the preceding geometry construction, so this is not a sign correction preserving that mechanism unchanged. An added background coframe similarly changes (14) and introduces genuinely new structure.
3. Derive a different effective probe equation from the full composite-metric action, retaining its measure, varying gamma matrices, spin connection and all differential chain-rule terms. Its source must pass the same conservation/phase tests. In particular the real symmetric probe law omits the ordered HC transport in the factorized case; then the derivative in the coframe and the derivative in that law are no longer the same. That drops a hypothesis of (15), but does not make the existing nonconserved null-aligned profile a solution.
4. If a nonreal mass bilinear, independent adjoint or open dynamics is intended, derive its reality, comparison and source balance. The value required by (15) is a consistency obligation, not permission to insert an imaginary constant. A nonreal mass contribution and non-unitary connection can exchange norm contributions; their combined action must be evaluated rather than judging either in isolation.

The immediate conclusion is definite: **do not try to repair the previous unchanged profile merely by solving for a missing internal gauge field.** Its current already fails a necessary identity, and the direct same-induced-frame ordered equation with real mass bilinear is excluded. The positive null geometry/stress match remains an off-shell structural example; the native geometry/probe identification has to be made explicit before another field-solution claim.

## 10. Reproduction

Run `python -B analysis/HC_Bilinear_Geometry_Bridge.py --output analysis/HC_Bilinear_Geometry_Bridge.json`. The 59 focused tests include the original 42 geometry checks and 17 follow-through checks of induced-current divergence, volume dependence, same-frame gamma contraction, residual bounds, normalization, real coefficient/gauge invariance, nonfactorized mass reality and the essential negative controls. These are numerical/algebraic checks, not a formal proof-assistant certificate or empirical validation. The short identities (12)--(16) are derived explicitly above; the numerical regressions are checks of their implementation, not substitutes for the argument. No package, main-TeX edit, compiler invocation or Git operation is part of this continuation.

## 11. Two-Frame and Common-Action Follow-Through

The subsequent [two-frame action bridge](HC_Two_Frame_Action_Bridge.md) tests the first route above: separate reference/effective frames still obey a zero mixed-trace condition if the unshifted bilinear dictionary and real reference master equation are retained. A multiplier parent makes the geometric backreaction and missing independent metric equation explicit. Adding a genuine background coframe changes the trace identity and admits a local massless neutral scalar-HC solution of an explicitly modified common action. Its curved geometry, scalar/probe/coframe equations and currents all match on that restricted model. Restoring mass/Yukawa, a charged Gauss source or a zero-target matching penalty fails on the unchanged profile. Thirty-two checks keep this existence comparison distinct from a native coframe correction, minimal exact closure or a solution of the main paper.
