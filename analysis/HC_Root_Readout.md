# An Explicit HC-to-Mass-Root Identification Test

Date: 2026-10-16. Status: explicit nonlinear readout, stronger finite countermodels, a conditional quadratic construction and an exact positivity/metric obstruction for that construction. The native HC does not yet determine the Koide radius. No empirical mass, target phase, new native activation or main-TeX change is used.

## Result

There is a specific nonzero quadratic alternative to the excluded linear map `B C f` on a `J`-odd input. It can preserve the desired zero on fixed inputs and equality on `J`-dual inputs. In an aligned antiunitary two-mode realization it removes one otherwise free bilinear component. A norm-isometric transfer of the remaining bilinears to the generation-root operator would then give Koide exactly.

That last metric transfer is **additional input**, not an implication of `C=(I+J)/2`. Leaving its relative coefficient `eta` explicit gives

```text
K=(1+eta^2)/3
```

on the admitted aligned odd branch. Thus setting `eta=1` without deriving the physical readout would simply move the assumed Koide radius into a new coefficient. The present calculation does not do that silently.

The further positivity test is stronger: this candidate is positive on **all** two-mode inputs if and only if `eta<=1/sqrt(2)`. Its Koide ratio is then at most `1/2`. Isometry at `eta=1` and unrestricted positivity are incompatible within this linear-in-density family. A restricted branch remains possible, but requires a native domain and preservation law; neither tensor activation nor a change of basis supplies them.

There is also a conclusive structural countercheck. Even exact Millennium closure, a genuine spectral HC projector, a fixed simple self-adjoint clock spectrum, cyclic compatibility and equal HC channel norms for **every** generation input still allow different Koide ratios. This refutes sufficiency of those conditions, not every possible fully specified native interaction.

The following [root-phase dynamics test](HC_Root_Phase_Dynamics.md) now identifies this candidate's normalized angle with the earlier fixed-radius phase energy. An explicitly added overdamped phase law preserves the chamber, while inertia requires an initial-energy condition. A freely complex canonical extension of the same energy generates the omitted bilinear and makes the selected point a transverse saddle. These distinct reductions do not determine the native projected dynamics or prepare its domain.

## 1. Source Dictionary and the Readout That Actually Needs Evaluation

The retained `sources/research/parts/v470/10_sphaera_and_physics.tex` supplies:

- `sec:central`: `C=(I+J)/2` and the odd residual `P_-=(I-J)/2`.
- `thm:three-generations`: a proposed three-slot dictionary and the biquaternion/matrix-spinor language.
- `thm:hopf`: a spinor/projective-geometry dictionary, not the map computed below.
- `thm:gauge-invariance`: an antiunitary `J` convention, whereas other inherited arguments call `J` unitary.

The existing [linear identification test](HC_Lepton_Readout_Identification.md) already proves that `C f=0` for a pure odd input and that the native root-space map and its metric are unspecified. Those results are not rediscovered or overridden here. The existing [generation-coupling interface](Generation_Closure_Coupling.md) instead gives

```text
A=(I-P) R_tilde S,
Q=A* A,
L=sqrt(Q),
x_i=sqrt(kappa) eigenvalue_i(L),
```

under its common-carrier, positive-metric, domain/unit and closed-seed assumptions. The last line is conditional on the additional physical mass law `M_mass=kappa Q`, with `kappa>0` carrying mass units. The norm/spectral readout is nonlinear, unlike a linear HC output; ordered eigenvalue coordinates are not a linear representation of the native carrier.

Write `L=aI+D`, where `a=Tr L/3` and `Tr D=0`. Orthogonality in the Hilbert-Schmidt comparison gives

```text
K=Tr(L^2)/(Tr L)^2
 =1/3+||D||_F^2/(9a^2),
K=2/3 iff ||D||_F^2=||aI||_F^2=3a^2.
```

This is the actual norm-transfer obligation. It concerns an identity/traceless splitting of a three-generation **root operator**, not merely two parity sectors of a native transition output. The slot cycle acting on operators is also not automatically a cycle permuting the ordered eigenvalue list.

## 2. Even Seedwise HC Channel Balance Does Not Prove Root Balance

The following finite construction strengthens the earlier unitary-dilation freedom test. Work in a positive complex Hilbert realization with a **complex-linear extension of a real orthogonal involution**. It is not the antiunitary convention used separately in section 3.

Take nine dimensions split into an input block and two output blocks:

```text
P=diag(I3,0,0),       S=(I3,0,0)^transpose,
J=diag(-I3,+I3,-I3),  C=(I9+J)/2,
M=C+3(I9-C).
```

These operators are fixed independently of the prospective mass spectrum. They satisfy

```text
S*S=I3,       P S=S,       J S=-S,
[M,P]=[J,P]=0,
M C=C.
```

Moreover `C` is exactly the full eigenspace projector of `M` at eigenvalue one; the complement has eigenvalue three. There is no unproved spectral-projector claim in this finite witness. Its minimal defect functional `Lambda[M,P]` is zero.

Now let `0<=Q<=I3` be any cyclic Gram matrix. Use bright/dark output coordinates related to the two parity-labelled outputs by

```text
output_plus  =(bright+dark)/sqrt(2),
output_minus =(bright-dark)/sqrt(2).
```

In the fixed Fourier basis of the cycle, choose input clock eigenvalues `(4,6,8)`, bright eigenvalues `(1,2,3)` and dark eigenvalues `(10,11,12)`. For each Fourier mode let `d_i` be the positive input/bright gap and `q_i` its Gram eigenvalue. Rotate its input/bright pair by

```text
alpha_i=arcsin(2sqrt(q_i)/d_i)/2.
```

The argument lies in `[0,1]` since `q_i<=1` and all gaps are at least three. The self-adjoint clock formed by these rotations has the **same simple spectrum** `(1,2,3,4,6,8,10,11,12)` for every `Q`. Its mixed input-to-bright block is `sqrt(Q)`, because `d_i sin(alpha_i)cos(alpha_i)=sqrt(q_i)`.

Return to the parity output coordinates. Then

```text
A=(I-P)R S=(0,sqrt(Q)/sqrt(2),sqrt(Q)/sqrt(2))^transpose,
A*A=Q,
A* C A=A*(I-C)A=Q/2,
A*J A=0.
```

The equal norm holds for every input vector, not only after taking a total trace. Nevertheless `Q` is free. For example, cyclic positive roots with different relative singlet/traceless weights give `K=1/3`, `5/12` and `2/3` while `M,P,J,C,S` and the clock spectrum remain fixed. The executable construction realizes all three without measured masses.

In this balanced case the HC-projected transition roots are only

```text
sqrt((C A)*(C A))=L/sqrt(2).
```

Projection changes their common scale, not their ratio. Similarly a unitary reversal on the output satisfies `sqrt((J A)*(J A))=L`. Reversal information is lost by the Gram map; it cannot automatically become a nontrivial root-space grading.

The scope matters: this clock is a finite countermodel, not a recovered Riemann clock or a solution of the entire native probe/gauge background. It is independent of `M`, as the presently uncomputed native bridge permits at the interface level. Imposing an additional relation between them can remove freedom, but identifying the clock with the exactly closed `M` algebra would instead kill this transition route, as already proved in the native-link audit. The counterexample establishes only that the listed HC/closure/clock conditions do not force Koide.

## 3. A Concrete Quadratic Alternative on Two Internal Modes

Assume an independently specified extraction of two dimensionless **internal** amplitudes `chi=(u,v)`. They are not identified with the physical spin components of an electron; doing that would require separate Lorentz/current matching and spin-independent mass tests.

Define real bilinears

```text
X0=|u|^2+|v|^2,
X1=|u|^2-|v|^2,
X2=2Re(conjugate(u)v),
X3=2Im(conjugate(u)v).
```

Expanding the products gives the exact identity

```text
X0^2-X1^2=4|u|^2|v|^2=X2^2+X3^2.
```

This is a bilinear identity, not an identification with a physical null photon or a gravitational metric.

On the generation space let `U` be the three-cycle, and choose the orthonormal Hermitian circulant basis

```text
E0=I3/sqrt(3),
E1=(U+U*)/sqrt(6),
E2=i(U-U*)/sqrt(6).
```

The relative physical transfer remains explicit:

```text
L_eta=X0 E0+eta X1 E1+eta X2 E2,       eta>=0.
```

This is a proposed nonlinear root-coupling functional of the mode amplitudes. The map from `(X0,X1,X2)` to `L_eta` is linear on those **bilinear coordinates**, with comparison matrix `diag(1,eta^2,eta^2)`. It is an isometry for the declared Euclidean/Hilbert-Schmidt metrics precisely at `eta=1`.

Neither normalization of the state nor common mass units fix this relative metric coefficient. Also, `E1,E2` commute whereas the corresponding two Pauli matrices do not: this is an observable readout, not a multiplication-preserving representation of the two-by-two matrix algebra. An assertion of unitary equivalence alone cannot establish that particular norm transfer.

### Exact Ratio and the Missing Bilinear Component

One has

```text
Tr L_eta=sqrt(3)X0,
Tr L_eta^2=X0^2+eta^2(X1^2+X2^2).
```

For a nonzero **positive** `L_eta`, the physical principal-root ratio is therefore

```text
K=[1+eta^2(1-(X3/X0)^2)]/3.
```

Thus the radius has two logically distinct requirements: eliminate `X3` and establish the relative metric transfer. At `eta=1`, a nonzero `X3` produces the exact deficit `2/3-K=X3^2/(3X0^2)`. This is a result of the candidate map, not a fit or a native prediction.

## 4. What an Aligned Antiunitary HC Would Supply

In a declared two-mode real structure `J=K_complex`, with `K_complex` complex conjugation, use the odd residual

```text
chi=P_- f=(f-conjugate(f))/2=i Im(f).
```

Its two components have a common imaginary phase, so `X3=0`. It follows that

```text
K=(1+eta^2)/3,
||traceless L_eta||_F^2-||singlet L_eta||_F^2
 =(eta^2-1)X0^2.
```

At an independently justified isometric readout `eta=1`, the required norm balance follows identically on every nonzero admitted residual. The resulting positive cyclic root has `r/a=1/sqrt(2)` without changing that radius as the internal mode direction varies. This would protect the fixed-radius surface used in the preceding phase-selection analysis **if** the native theory supplies this whole map and its metric. It does not stabilize the amplitude or select the remaining phase.

This evades the linear odd-input obstruction honestly: `C f=0`, but the proposed readout uses a quadratic function of `P_- f`, not a function only of `C f`. It vanishes on fixed inputs and is unchanged for `f->Jf`, because the residual changes sign and the bilinears do not. It does not follow that this is the native Yukawa or mass readout.

### The Convention and Alignment Are Essential

For a complex-linear reversal `J=-I` on the same complex two-mode space, every complex `chi` is odd. Choosing `chi=(1,i)/sqrt(2)` gives `X3=X0=1` and `L_eta=I/sqrt(3)`, hence `K=1/3`, even at `eta=1`. The unitary and antiunitary conventions cannot be silently exchanged to obtain the desired ratio.

Even antiunitarity alone is not sufficient with an unaligned readout. Under a unitary frame `V`, the real structure becomes `J'=V K_complex V*`. The extraction and Pauli-type tensors must be transported with it. At the illustrative odd mode below, rotating by `V=diag(1,i)` but retaining the old bilinear readout changes `K` to about `0.4648673668`. Co-transporting the readout restores `2/3`. Thus a native frame alignment, not merely existence of some conjugation basis, must be derived.

There is an additional phase/gauge gate. For fixed conjugation, multiplying a purely odd mode by `i` makes it fixed, so the residual-only root readout changes from nonzero to zero. The raw quadratic map on an already supplied residual is common-phase invariant; the preceding residual extraction on the original input at fixed `J` is not. Joint frame transport restores algebraic covariance. That is not a derivation of a local physical gauge theory with a specified dynamical real structure and connection. A physical mass observable cannot simply be declared invariant under state-only phase changes here.

## 5. Principal Positivity, Phase, Amplitude and Units

The quadratic construction can produce negative signed eigenvalues. For example, the odd mode `chi=(0,i)` at `eta=1` lies outside the positive principal-root cone. Squaring this signed matrix yields nonnegative candidate masses, but the physical root is then `|L_eta|`, not `L_eta`; its trace and Koide ratio change. All ratio claims above explicitly require a nonnegative principal root. The native admissible state cone and its preservation remain to be established.

For the illustrative admitted mode

```text
chi=i(cos(2.25/2),sin(2.25/2)),       eta=1,
```

the root eigenvalues are approximately `(0.0644486540,0.2836202430,1.3839819106)` in declared dimensionless root units. The singlet and traceless squared norms are both one, and `K=2/3`. These are not electron/muon/tau predictions. The angle `2.25` is an arbitrary admitted test angle, not obtained from beta, masses or the earlier target shift.

For a real mode direction `chi=i b(cos(alpha),sin(alpha))`, the coefficient phase is `theta=2alpha`; its amplitude is proportional to `b^2`. This algebraic doubling does not derive the inherited beta-to-Koide phase law or identify `alpha` with a spacetime Hopf angle.

The raw root map is homogeneous of degree two in the amplitudes, and its Gram matrix of degree four. If these were amplitudes of an individual freely rescalable probe, the state-dependent scale would need a physical explanation. They may instead be internal/background data, but the source has not identified that role. Normalizing away their size does not supply the missing mass unit or automatically preserve continuity at zero residual. The earlier scale-stability problem is not resolved.

## 6. Can the Native Tensor or Trace Structure Fix the Metric?

The answer from the inspected definitions is not yet. In the retained `07_qam_infrastructure.tex`, `def:two-sided-admissible-contractions` requires an explicitly declared comparison tensor for same-variance comparisons. Its following `rem:two-sided-conservative-reading-rule` does not assign numerical entries to that tensor. In `29_shifted_qam.tex`, `def:v3370-readout-package-translation` and `prop:v3370-machine-content-preservation` preserve the comparison tensor rather than construct one. The new `tensor-shift-coupling.tex` likewise distinguishes supplied positive metrics from a native metric extraction. These are source contracts, not a reason to set a free coefficient to one.

Even adding cyclic symmetry does not make the two weights equal. To see this without assuming any native representation theorem, impose a coefficient-space rotation

```text
D=diag(1,R(2pi/3)),       D^T G D=G,
```

on a real symmetric positive comparison matrix `G`. The singlet/doublet cross-vector would have to be fixed by the nontrivial plane rotation, hence is zero. The symmetric doublet block commuting with that rotation is a scalar. Therefore

```text
G=diag(g_s,g_d,g_d),       g_s>0, g_d>0,
```

with two independent weights. This coefficient rotation can represent a cyclic permutation of **labelled Fourier-root coordinates**. It must not be confused with conjugation by the slot cycle: every circulant `L` here satisfies `U L U*=L`, so that conjugation acts trivially on all three `E_a`.

Even invariance under all unitary conjugations on the output does not by itself remove the freedom. For Hermitian operators, the explicit comparisons

```text
G(A,B)=a Tr(A B)+b Tr(A)Tr(B),
a=g_d,       b=(g_s-g_d)/3,
```

have precisely these weights on `(E0,E1,E2)` and are positive on the full Hermitian space for `g_s,g_d>0`. Both terms are invariant under unitary conjugation. A specifically selected single trace comparison would exclude the second term, but that choice and the input/output norm matching are extra physical data, not consequences of symmetry alone.

For the already fixed Euclidean input and Hilbert-Schmidt output comparisons, the transfer has pullback `diag(1,eta^2,eta^2)`. Declaring this pullback to be the input metric makes any nonzero `eta` an isometry by construction; it does not determine `eta`. A chart change with co-transported comparisons likewise leaves physical spectra unchanged. The mass-root ratio `Tr L^2/(Tr L)^2` is still the ordinary ratio of actual eigenvalues; redefining its comparison to obtain `2/3` would change the question. The commuting `E1,E2` also rule out using multiplicative Clifford/Pauli equivalence as a shortcut to this transfer.

## 7. Exact Positivity Bound for the Quadratic Candidate

This test concerns the **specific candidate** `L_eta`, not every possible HC or nonlinear mass law. Its quadratic dependence on the amplitudes is linear in the two-mode matrix `rho=chi chi*`. Extend that same formula linearly to arbitrary `rho>=0`:

```text
X0=Tr rho,       X1=Tr(sigma_z rho),       X2=Tr(sigma_x rho),
L_eta(rho)=X0 E0+eta X1 E1+eta X2 E2.
```

In the fixed Fourier basis, with `phi_k=2pi k/3`, its signed root eigenvalues are

```text
ell_k=X0/sqrt(3)+sqrt(2/3)eta(X1 cos(phi_k)-X2 sin(phi_k))
     =sqrt(3) Tr(F_k rho),
F_k=[I2+sqrt(2)eta(cos(phi_k)sigma_z-sin(phi_k)sigma_x)]/3.
```

The three forms sum to `I2`. Thus `ell_k/(sqrt(3)X0)` sum to one for nonzero input, but are nonnegative only if the relevant positivity condition holds. This normalization is not an assertion that masses or roots are native outcome probabilities.

The two Pauli directions anticommute and square to identity, so the matrix in parentheses has eigenvalues `+1,-1`. Consequently each `F_k` has eigenvalues

```text
(1-sqrt(2)eta)/3,       (1+sqrt(2)eta)/3.
```

For all positive inputs to give `ell_k>=0`, each `F_k` must be positive: necessity follows by testing its negative eigenvector, and sufficiency by `Tr(F_k rho)>=0` for two positive matrices. This proves the sharp equivalence

```text
L_eta(rho)>=0 for every rho>=0   iff   0<=eta<=1/sqrt(2).
```

Necessity already holds if only **all aligned antiunitary-odd pure modes** are admitted. The odd mode `chi=(0,i)` gives

```text
min eigenvalue(L_eta)=(1-sqrt(2)eta)/sqrt(3).
```

At `eta=1` this is approximately `-0.2391463117`. Antiunitary oddness cannot itself eliminate the counterexample. At the boundary `eta=1/sqrt(2)`, that mode has roots `(0,sqrt(3)/2,sqrt(3)/2)`.

For any positive two-mode matrix, `X1^2+X2^2<=X0^2`. This also follows directly from positivity of its determinant after adding `X3=Tr(sigma_y rho)`. Therefore the whole globally positive family satisfies

```text
K=[X0^2+eta^2(X1^2+X2^2)]/(3X0^2)
 <=(1+eta^2)/3
 <=1/2.
```

The last bound is attained on nonzero aligned pure inputs at the maximal globally positive weight. It is incompatible with `2/3`. This does **not** require that an arbitrary physical mass readout be a positive linear density map; it states that demanding such a globally positive realization of this particular candidate rules out its intended isometric Koide mechanism. A different nonlinear readout or independently restricted background domain is not covered by this obstruction.

## 8. What a Restricted Isometric Branch Would Require

For a unit-norm aligned odd mode `chi=i(cos(theta/2),sin(theta/2))`, one has `X1=cos(theta)`, `X2=sin(theta)` and

```text
ell_k=[1+sqrt(2)eta cos(theta+2pi k/3)]/sqrt(3).
```

At `eta=1`, requiring all three roots to be nonnegative gives exactly

```text
theta=2pi k/3+delta modulo 2pi,
|delta|<=pi/12,       k=0,1,2.
```

For example, in the chamber nearest zero, the limiting cosine is `cos(2pi/3+|delta|)`. Its lower bound `-1/sqrt(2)` gives `|delta|<=3pi/4-2pi/3=pi/12`. The other chambers are cyclic copies. At their edges one root vanishes. The three intervals have total length `pi/2`, a quarter of the coefficient-angle circle. This fraction is a geometric measure in these declared coordinates, not a physical probability or a statement about spacetime/frame coverage.

More generally the half-width around the nearest `2pi k/3` is

```text
delta_max=pi/3                            if 0<=eta<=1/sqrt(2),
delta_max=acos(-1/(sqrt(2)eta))-2pi/3      if 1/sqrt(2)<eta<=sqrt(2).
```

The first line covers the whole circle. At `eta=sqrt(2)` only the three centers remain; for larger `eta` there is no positive pure aligned-odd input. General complex inputs are different: the mode with `X1=X2=0` still gives an isotropic positive root for any weight.

The isometric admitted set is not a vector space and is not preserved by arbitrary coherent superposition. In particular

```text
chi_1=i( 1/2,sqrt(3)/2),       chi_2=i(-1/2,sqrt(3)/2)
```

are both odd and have positive roots, but their sum is `i(0,sqrt(3))`, with negative minimum signed root `-0.7174389352`. By contrast, the **incoherent** matrix sum `rho_1+rho_2` remains admitted, since the readout is linear on matrices and its two outputs are positive. Confusing these two operations would hide the restriction. A nonlinear background/order-parameter domain need not be a state vector space, but its physical role must then be specified; arbitrary internal probe superpositions cannot simply be assumed admissible.

Likewise a nonzero constant angular drift eventually leaves an admitted chamber, even while antiunitary oddness is maintained. For a locally Lipschitz autonomous angular law `theta_dot=f(theta)` to preserve each closed chamber forward in time, its boundary values must point inward:

```text
f(left_edge)>=0,       f(right_edge)<=0.
```

This is an explicit invariance obligation, not a derived native evolution or an added fitted potential. Passive co-transport of the state, real structure and readout frame preserves the already chosen root for **any** `eta`; that coordinate covariance neither picks `eta=1` nor proves preservation under an active physical phase evolution.

Replacing signed roots by their absolute values is a different nonlinear map and does not rescue the constant ratio. For `chi=(0,i)` at `eta=1`, `Tr L^2=2` is unchanged but `Tr |L|=(1+2sqrt(2))/sqrt(3)`. Thus the physical principal-root ratio of the squared masses is

```text
K_abs=6/(1+2sqrt(2))^2=0.4093647858,
```

not `2/3`. Squaring, discarding signs, renormalizing a common amplitude or relabelling tensor indices cannot remove this mismatch.

## 9. The Exact Native Identification Still Required

The conditional construction turns the unspecified root map into an explicit test contract:

```text
chi=E_native P_- f,
E_native J=K_complex E_native in the selected two-mode frame,
A=(I-P) R_tilde S,
A*A=L_eta(chi)^2,
eta=1 through an independently justified physical comparison,
L_eta(chi)>=0 on a physically admitted RESTRICTED domain,
the native evolution preserves that domain.
```

The antiunitary equation presupposes that convention; a different native convention needs its own compatible extraction. The equality of the native Gram and the quadratic root functional is not established by engineering a clock after `L_eta`. The countermodels in section 2 do exactly that for a **sufficiency test**, not to claim a recovered native clock.

If the native extraction, alignment, metric isometry and restricted-domain preservation can all be shown, the identity in section 4 proves the Koide norm balance on that admitted branch. If all odd two-mode inputs must instead be admitted, the positivity bound in section 7 excludes this isometric candidate. If only ordinary HC balance or cyclic symmetry is available, the countermodels show the desired conclusion does not follow. A common scalar normalization, a QAM tag migration, the count of three slots or a fitted `eta` cannot substitute for the missing norm-transfer/domain law.

The result therefore narrows the open problem without declaring it solved: there is an explicit nonlinear candidate with testable native matching equations, a proof that the existing weaker HC/closure conditions do not force its special metric, and an obstruction to combining that metric with unrestricted positivity. The next justified alternatives are to derive a native restricted background domain and its dynamics, or to derive a genuinely different root readout. Neither alternative has yet been supplied by the source. Its linearity convention, physical mass law, phase, scale, gauge/current matching and full field stability remain open.

## Reproduction

Run `python -B analysis/HC_Root_Readout.py --output analysis/HC_Root_Readout.json`. The 60 tests in `scripts/qsc_audit/tests/test_hc_root_readout.py` cover the principal-root map, bilinear identity, metric coefficient, odd/fixed/dual and convention tests, covariance and the phase/gauge obstruction, the principal cone and scale behavior, and fixed-simple-clock countermodels with exact spectral HC, closure, cyclic compatibility and seedwise channel balance. The 24 added checks verify the density extension and Fourier forms, sharp all-input positivity bound and ratio ceiling, chamber formula and boundaries, coherent/incoherent distinction, absolute-root repair, angular drift, cyclic comparison freedom and covariance for arbitrary relative weights. The report is reproduced without historical mass data. No package was installed, main TeX changed, or commit/publication operation performed for this follow-up.
