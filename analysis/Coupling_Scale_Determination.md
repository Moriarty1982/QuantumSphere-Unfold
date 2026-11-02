# Attempt to Determine Coupling Matrices and Scales

Date: 2026-10-15. Status: evaluated conditional effective candidate, not a native operator identification or a physical mass prediction. The unreleased full-source research working copy includes this analysis as `sources/research/parts/coupling-scale-candidate.tex`.

## Result

A concrete normalized three-channel matrix can be calculated from the inherited Koide radius and proposed frame-phase law. Neither of those hypotheses has acquired a first-principles derivation. The overall coupling and complementary gap remain undetermined. More strongly, no choice of these two positive scales repairs the fixed candidate's muon/tau mass ratio in the zero-direct-block, flat-positive-gap model. A one-mass calibration is possible but is not a solution for the full spectrum.

The follow-up diagnosis finds that the fixed-ansatz shape discrepancy is dominated by the inherited relative-phase law, not matrix arithmetic or decimal rounding. The Planck-scale test has no SI conversion error; its tiny masses follow from the added assumptions `A=0`, `Delta=m_P` and electroweak-sized mixing. This is not a general failure of a Planck-scale sector. Non-flat gaps can absorb a target spectrum by fitting, and a retained direct block can carry the masses while a Planck-gapped complement supplies only tiny corrections.

The tensor follow-up further limits that diagnosis to identity input/output metrics. The active tensor grammar allows explicit comparisons, but the governing QAM shift preserves numerical payloads. Correct tensor transport leaves the spectrum invariant. A separately specified physical comparison can change it; the source does not yet supply its numerical entries on these generation/transition spaces.

The subsequent [physical-origin diagnosis](Coupling_Physical_Origin_Diagnosis.md) derives a possible response tensor from inverse complementary gaps and distinguishes it from induced norm dressing. The latter is negligible in both previously tested Planck-gap scenarios. A small relative triadic-phase correction can change the near-cancelled root substantially, but independent phases cancel unless the sectors share or coherently mix channels. Ordinary one-loop QED matching cannot supply the required opposite-sign ratio corrections. These tests narrow mechanisms; they do not identify the native cause or establish a frame/gravitational interaction.

## What Was Actually Available

The retained `10_sphaera_and_physics.tex` provides the generation dictionary (`thm:three-generations`), Brannen radius and phase proposal (`thm:koide-triolic`), rounded input `beta=0.5493`, a named `g_Y` multiplying unspecified triadic operators, and a free coefficient `chi` in `prop:triadic-two-probe`. The same fragment explicitly acknowledges the missing Yukawa/Higgs mechanism in "Mass spectrum beyond Koide." The refined `16_master_model.tex` retains symbolic field coefficients rather than numerical generation matrices.

The [native-link audit](Native_Operator_Link_Audit.md) already establishes why the clock spectrum, common frame phase and minimal penalty do not determine the missing cross block. No new evaluated native `R_GUE`, `P`, or Dixon embedding was found in this follow-up. The following matrices are therefore additional effective candidates whose assumptions are listed, not hidden replacements of the native symbols.

## Normalization Does Not Fix the Physics

Writing `V=mu B` has a redundancy: multiplying `mu` by `t>0` and dividing `B` by `t` leaves `V` unchanged. If an actual nonzero finite `V` were given, the convention `Tr(B*B)=1` would fix `mu=||V||_F` and `B=V/mu`. Choosing that normalization without supplying `V` does not determine a mass scale. The matrix `Q=B*B` also leaves output isometries in the polar factor of `B` undetermined.

In the flat-gap model, put `eta=mu/Delta`. The exact masses are

```text
m_i = Delta [sqrt(1+4 eta^2 q_i)-1]/2.
```

The shape and `eta` fix ratios. Simultaneous scaling `(mu,Delta) -> (s mu,s Delta)` leaves ratios and complementary weights unchanged while scaling every mass by `s`. An independent mass reference removes the unit choice, but does not supply the dimensionless gap and coupling coefficients.

## Why a Minimal Two-Channel Matrix Fails

For a cyclic generation matrix `U`, try `B=b0 I+b1 U`. Its Fourier eigenvalues are `lambda_k=b0+b1 omega^k`, `omega=exp(2 pi i/3)`. The complex numbers `omega^k lambda_k` sum to zero and have magnitudes `|lambda_k|`. The existing closed-triole bound therefore gives `K <= 1/2` for the mass law proportional to `B*B`, excluding `2/3`. Arbitrary operator-valued two-channel models are not excluded by this particular cyclic argument.

## Evaluated Three-Channel Candidate

Now explicitly retain the unproved hypotheses `r/a=1/sqrt(2)` and `theta=pi-sqrt(2) asin(beta)`, using the inherited rounded `beta=0.5493`. Unit Frobenius normalization gives

```text
theta = 2.3191902578571373,
B = I/sqrt(6) + [exp(i theta) U + exp(-i theta) U*]/sqrt(12),
Tr(B*B)=1.
```

With `U epsilon_i=epsilon_(i+1 mod 3)`, the evaluated matrix is

```text
B = [[ 0.40824829,             -0.19643267-0.21153614i, -0.19643267+0.21153614i],
     [-0.19643267+0.21153614i,  0.40824829,            -0.19643267-0.21153614i],
     [-0.19643267-0.21153614i, -0.19643267+0.21153614i,  0.40824829            ]].
```

The diagonal entries of `Q=B*B` are `1/3`; its ascending eigenvalues and ratios are

| Assigned position, not derived identity | `q_i` | `q_i/q_largest` | Historical paper mass ratio |
| --- | ---: | ---: | ---: |
| Smallest / attempted electron | 0.0002366350012 | 0.0002509434394 | 0.0002875859663 |
| Middle / attempted muon | 0.0567819436407 | 0.0602153365428 | 0.0594633229405 |
| Largest / attempted tau | 0.9429814213581 | 1 | 1 |

The comparison uses only the masses already quoted in the inherited Koide block (`0.51100`, `105.658`, `1776.86` MeV). These are historical comparison/calibration inputs, not a claim of a newly verified experimental fit or updated world averages. They do not enter the function constructing `B`.

The leading ratio discrepancies are -12.74% and +1.265%. The Koide diagnostic is `2/3` because its radius was imposed. The proposed phase and rounded beta remain assumptions. At `beta=0`, this fixed-radius expression is not a positive principal-root matrix and does not give three equal masses; the evaluation rejects it as outside the specified positive branch. It is not a global photon-to-matter interpolation.

An explicit common finite carrier is obtained with `P=diag(I3,0)`, `S=(I3,0)^T`, `R_cand=[[0,B*],[B,0]]` and `Omega_cand=[[0,mu B*],[mu B,Delta I3]]`. These realize the displayed cross block and effective mass law. They are not identified with the native Riemann clock or the inherited Millennium/Dixon carrier. In particular, constructing a Hermitian finite clock with the desired Gram matrix does not prove the missing GUE-clock action.

## A Rigorous Scale-Only Obstruction

For the exact positive-gap masses and `0<q_i<q_j`, rationalization gives

```text
m_i/m_j = (q_i/q_j)
          [sqrt(Delta^2+4 mu^2 q_j)+Delta]
          /[sqrt(Delta^2+4 mu^2 q_i)+Delta]
        > q_i/q_j.
```

The muon/tau ratio already exceeds the inherited comparison. Every finite positive-gap correction increases it. Thus no positive `mu,Delta` fits that ratio for this fixed matrix, zero direct block and flat gap. This is an exclusion of this candidate branch, not a claim that all possible triadic field matrices fail. A non-flat gap, direct block or changed relative phase/radius changes the assumptions and needs an independent native equation.

## External Scale References and Explicit Calibration

For a single ordinary reference frame, `m_P=sqrt(hbar c/G)=hbar/(c ell_P)`. NIST's [2022 CODATA Planck energy reference](https://physics.nist.gov/cgi-bin/cuu/Value?plkmc2gev) is `1.220890(14)e19 GeV`. Its [Fermi constant reference](https://physics.nist.gov/cgi-bin/cuu/Value?gf) is `1.1663787(6)e-5 GeV^-2`. These primary sources were checked on 2026-10-15; central values suffice for the illustrative scale exclusions, not an uncertainty fit.

Define the electroweak reference `v_F=(sqrt(2) G_F)^(-1/2)=246.21965... GeV` and `mu_EW=v_F/sqrt(2)=174.10358... GeV`. Identifying this reference with the unknown coupling is an extra choice, not a native Higgs/Yokamono derivation.

| Explicitly chosen scenario | Result |
| --- | --- |
| `Delta=m_P`, `mu=mu_EW` | `kappa=2.48278e-6 eV`; mass magnitudes approximately `(5.8751e-10, 1.4098e-7, 2.3412e-6) eV`, not the quoted charged-lepton scales |
| `Delta=mu=m_P` | Exact masses approximately `(2.8884e15, 6.5780e17, 7.2306e18) GeV`; the weak-coupling approximation is not used |
| Fix `Delta=m_P`, calibrate only the quoted tau mass | `mu=4.7964e9 GeV`; predicted middle mass remains about `106.994 MeV`, not the quoted `105.658 MeV` |
| Fix `mu=mu_EW`, calibrate only the quoted tau mass | `Delta=1.6085e4 GeV`; middle ratio increases further |

The last two rows use `mu^2=m_tau(m_tau+Delta)/q_tau` or `Delta=mu^2 q_tau/m_tau-m_tau`. They are explicitly one-mass calibrations, not predictions and not spectrum fits. Choosing another externally known scale or a numerical power of the frame factor without a governing equation would simply introduce another scale ansatz.

Frame references cannot be mixed. Conditional use of the paper's assignments `hbar_f=gamma_L^-1 hbar_m`, `G_f=gamma_L^-2 G_m`, `c_f=c_m` gives `m_P,f=gamma_L^(1/2) m_P,m`. Substituting the matter `hbar` into the proposed photon Planck length would instead introduce an erroneous extra `gamma_L`. This consistency check does not validate those proposed frame laws.

## Remaining Determination

### Why the Matrix Deviates in the Present Ansatz

The Fourier spectrum of the implemented matrix exactly matches the written Brannen roots. Cyclic relabelling or complex conjugation only permutes the eigenvalues; the normalization cancels from the ratios. Rounding the displayed matrix entries to six decimal places changes the electron/tau ratio by about 0.01225%, far below its 12.74% discrepancy.

For a diagnostic inversion of the historical mass benchmark, define `x_k=sqrt(m_k/sum(m))`, `a=sum(x)/3`, `z=sum(x_k exp(-2 pi i k/3))/3`, `rho=abs(z)/a` and `theta=arg(z)` on the local ascending branch. This inversion uses masses as inputs and is explicitly not a derived coupling law.

| Shape quantity | Original conditional candidate | Historical benchmark inversion |
| --- | ---: | ---: |
| Relative phase `theta` | 2.319190257857 | 2.316624255394 |
| Radius `rho=r/a` | 0.707106781187 | 0.707100578472 |
| Equivalent beta within the assumed phase law | 0.5493 | 0.550815284909 |

The phase difference is -0.00256600246 rad, or -0.147021 degrees. The radius differs by only -8.77 parts per million. Replacing only the phase gives ratios `(0.0002874631,0.0594619634,1)`, close to the benchmark. Replacing only the radius leaves `(0.0002510584,0.0602167023,1)`, almost the original discrepancy. The relevant phase is the relative coefficient of `U` and `U*`; it is not the common clock phase, which cancels from `Q`.

For `h_k=1+2 rho cos(phi_k)>0`, `phi_k=theta+2 pi k/3`, direct differentiation gives

```text
d_theta log(q_i/q_j) = -4 rho [sin(phi_i)/h_i - sin(phi_j)/h_j],
d_rho   log(q_i/q_j) =  4     [cos(phi_i)/h_i - cos(phi_j)/h_j],
d_beta theta = -sqrt(2)/sqrt(1-beta^2).
```

The electron/tau and muon/tau beta sensitivities are about `92.6426` and `-8.28621`. The electron root is close to a zero at the positive phase-chamber boundary, so a small angular change produces a large relative mass change. This explains the amplification within this ansatz, not its physical origin.

If the issue were only four-decimal rounding, beta would lie in `[0.54925,0.54935]`. The middle/largest ratio decreases throughout that interval, from `0.06024029` to `0.06019039`, but stays above the benchmark. The equivalent diagnostic beta shift is about thirty rounding half-steps. This is not an experimental uncertainty assignment. Replacing the rounded string value by its exact written expression `log(2)/(pi sqrt(3))`, while retaining the approximate `gamma_BI=0.2375`, gives beta `0.549348248360` and middle/largest ratio `0.06019127`; it does not solve the discrepancy. A benchmark-calibrated `gamma_BI=0.2383454...` is not a justified replacement for the original input.

### Auditing the Planck Calculation

An independent SI calculation with exact defining `h,c,e` and [NIST's CODATA central Newton constant](https://physics.nist.gov/cgi-bin/cuu/Value?bg) gives

```text
m_P = 2.1764343427...e-8 kg,
ell_P = 1.6162550244...e-35 m,
m_P c^2 = 1.2208901286...e19 GeV.
```

The extra digits are reproducible central-value arithmetic, not added measurement precision. The energy agrees with the rounded reference used above to about `1.05e-7` relatively. The micro-eV estimate has no missing eV/GeV or `c^2` factor. It is the expected quadratic suppression `mu_EW^2/Delta` under the three added hypotheses `A=0`, a flat Planck gap and electroweak mixing.

The largest candidate mass then misses the quoted tau by a factor `7.589e14`. Replacing the chosen physical gap by the reduced reference `m_P/sqrt(8 pi)` only multiplies the result by `sqrt(8 pi)`, giving at most about `1.174e-5 eV`. That is another gap hypothesis, not a unit correction. The paper's conditional frame conversion multiplies the Planck mass by about `1.3654`; the inconsistent mixed-hbar construction gives about `2.5453`. Neither explains fourteen orders of magnitude. Standard SI definitions do not themselves imply the paper's proposed frame dependence of constants.

Crucially, a fundamental reference length or UV cutoff does not determine the spectral gap of a particular complementary field block. That identification requires an additional operator equation. The tau-calibrated gap with electroweak mixing is `16.085 TeV`, whose inverse energy length `hbar c/Delta` is about `1.227e-20 m`, or `7.59e14 ell_P`. This is an effective gap length, not a replacement of the fundamental Planck length. A Planck gap can instead be retained with the tau-calibrated intermediate mixing `4.7964e9 GeV`; that scale is not derived either.

### A Non-Flat Planck Gap Is Not Excluded

For the positive candidate `B=F diag(sqrt(q_i)) F*`, choose a target triple `t_i>0` and a mixing large enough that `mu^2 q_i > t_i^2`. Defining

```text
Delta_i = mu^2 q_i/t_i - t_i,
H_perp = F diag(Delta_i) F*
```

makes the three independent block equations have exact light signed eigenvalues `-t_i`. This is a fitted realization, not a recovered physical interaction. The eigenbasis alignment is part of the additional choice; diagonal gaps in an unrelated output basis do not give the same fit.

Keeping `Delta_tau=m_P` and the tau-calibrated intermediate mixing gives

```text
(Delta_e,Delta_mu,Delta_tau)/m_P = (0.87258583,1.01264668,1).
```

All gaps remain Planck-sized. The three historical masses are reproduced by construction and the complementary weights are at most about `1.46e-19`, nonzero but tiny. This disproves a blanket exclusion of Planck-order gaps, while demonstrating the fit freedom. It does not derive those anisotropies or the intermediate mixing. With electroweak mixing and every gap still of Planck order, these moderate anisotropies cannot cure the absolute suppression.

### The Direct Mass Block Was Not Forced to Vanish

The original `Omega` already contains bare, projected-Millennium, triadic and compensator terms. Their compressed sum `A` was set to zero as an additional simplification of the induced-mass test, not as a theorem of the paper.

For a supplied Hermitian block model with `H_perp >= Delta I` and a light eigenvalue `abs(lambda)<=E<Delta`, the Schur equation implies

```text
dist(lambda,spec(A)) <= ||V||^2/(Delta-E).
```

The closed coordinate cannot vanish below the complementary gap; the bound follows from its Schur equation and the spectral lower bound for `||(A-lambda)x||`. With the candidate electroweak coupling norm, a Planck gap and `E=2 GeV`, the correction bound is only about `2.3412e-6 eV`. A direct block at charged-lepton scales can therefore coexist with a Planck-order complementary sector. This is a conditional interpretation, not a derived native `A` or mass hierarchy.

### What This Diagnosis Can Identify

The source must still supply a represented triadic interaction and complementary-sector equation, with canonical kinetic normalization, that fixes the cross-block matrix, its rank, phase/radius, `g_Y`/`chi` products, and the positive gap independently of observed lepton masses. The strict-versus-dressed closure limitation remains. The present calculation gives an explicit numerical test candidate and rules out scale-only repair of it; it does not uniquely determine the native physical matrices and scales.

The matrix diagnosis is conditional on the chosen root spectrum and mass law. Its success as a phase inversion does not identify the physical cause uniquely: a different gap structure or direct block can redistribute the discrepancy. Likewise, the Planck diagnosis rejects the earlier flat-gap, zero-direct-block, electroweak-mixing combination, not the Planck reference itself.

## Tensor Activation and the Shift

The new research section `sources/research/parts/tensor-shift-coupling.tex` applies the current shifted normal form rather than returning to pre-v4 syntax. Three different operations must remain distinct:

- The global namespace migration `Sigma_4(k)=k+1` preserves the numerical tensor/readout payload (`def:v400-r01-shifted-tensor-payload-migration`, `thm:v400-r01-shifted-activation-conservativity`). Packed masks are rebuilt from shifted supports: `{0,2,5}`/37 becomes `{1,3,6}`/74, not 38. The local HC first-boundary shift is not a numerical mass correction either.
- A coordinate change transports the coupling and both metrics together. For input `x=A x'` and output `y=D y'`, use `B'=D^-1 B A`, `K'=A* K A`, `H'=D* H D`. Then `Q'_H=A* Q_H A` and the generalized eigenvalues are invariant, including nonunitary charts. A numerical example returns the old eigenvalues within `2e-15`; wrongly resetting the metrics to identity gives spurious different ratios.
- A new physical comparison, held independently of chart transport, can change the spectrum. This requires actual coefficients and index-space assignments. The source's residual comparison tensor is not automatically a generation kinetic metric or a transition-output inner product. The later typed coefficient ledger also explicitly separates bookkeeping/selector/admissibility multipliers; these are not supplied Yukawa coefficients.

For a declared positive finite realization `B:(V_gen,K)->(W_out,H)`, the contraction and canonical coupling are

```text
Q_H = B* H B,
Q_H v = q K v,
C = H^(1/2) B K^(-1/2),
Q_canonical = C* C.
```

Here `H` is dimensionless positive comparison data, not the energy-valued complementary block `H_perp` or a Lorentz metric. The adjoint is `B^sharp=K^-1 B* H`. A weighted self-adjoint block `[[0,mu B^sharp],[mu B,Delta I]]` with metric `diag(K,H)` becomes the canonical Hermitian flat-gap model. Its exact masses obey the previous equation with the new generalized `q`. The tensor grammar does not derive this mass law.

With `K=I` and the output comparison aligned to the candidate singular modes, the historical leading ratios can be fitted by weights

```text
(h_e,h_mu,h_tau) = (1.146019066893,0.987511261324,1).
```

These weights demonstrate a possible effect of a nontrivial comparison, not an explanation already obtained: they are calculated from the target masses. For invertible `B`, any positive target matrix `T` can be absorbed into `H=(B^-1)* T B^-1`. This fit freedom must be controlled by an independent native equation. The preceding phase inversion therefore does not identify the physical cause uniquely. The listed weights fit leading ratios only; finite positive-gap corrections still apply. An exact target fit uses `t_i=m_i(m_i+Delta)/mu^2` instead of the leading shape target.

For `h_- I <= H <= h_+ I` and `k_- I <= K <= k_+ I`, min--max gives

```text
(h_-/k_+) lambda_i(B*B) <= q_i(K,H) <= (h_+/k_-) lambda_i(B*B).
```

At the previously chosen fixed numerical `B`, electroweak `mu`, zero direct block and canonical flat Planck gap, the tau mass requires `h_+/k_- >= 7.589e14`. The modest shape weights do not repair this absolute scale. This is a bound on absolute relative normalization, not on condition numbers: a huge scalar output metric can have condition number one. At fixed numerical `B,mu`, it is equivalent to increasing the canonical coupling norm by `2.755e7`; the missing scale has been inserted, not derived. A mere chart rescaling cancels covariantly. Physical Frobenius normalization must use `Tr(C*C)`, with the associated scale adjusted consistently.

Finally, carrier enlargement alone is insufficient: for normalized ancilla `a`, the isometry `Jv=v tensor a` and `B'=B tensor I` obey `J* B'* B' J=B*B`. This does not prohibit new cross-channel interactions; it requires their entries and seed embedding to be supplied rather than inferred from the HS(5)/HS(6) channel or mask count.

## Reproduction and Checks

Run `python -B analysis/Coupling_Scale_Candidate.py --output analysis/Coupling_Scale_Candidate.json`. Matrix real/imaginary parts, eigenvalues, ratios, reference inputs, scope assumptions, illustrative scale choices and single-mass calibrations are separately recorded. Rationalized exact masses avoid catastrophic cancellation at a Planck-sized gap.

`scripts/qsc_audit/tests/test_coupling_scale_candidate.py` contains 42 finite regression checks. They cover the original 23 candidate/scale checks and 19 further checks for analytic spectra, phase/radius recovery, derivative sensitivities, rounding and convention alternatives, SI conversion, reduced/reference frame factors, effective gap length, fitted non-flat spectra and their output alignment, and the direct-block bound. A route regression keeps the section before inherited claims; a further guard regression preserves the post-hoc, calibration and Planck-scope boundaries. These tests supplement the written arguments; they are not a native-operator or physical-validity certificate.

`scripts/qsc_audit/tests/test_tensor_shift_coupling.py` adds 18 checks for positive metrics and malformed inputs, rectangular maps, generalized eigenvectors, nonunitary covariance, spurious identity-metric reuse, global-phase invariance, weighted self-adjoint block spectra, modewise min--max bounds, target-derived metric fits, normalization and Planck-scale bounds, identity tensor extensions, tag/mask migration and saved-report reproducibility. A further route regression checks the five propositions and their shift/fit scope guards.

`scripts/qsc_audit/tests/test_coupling_physical_origin.py` adds 20 mechanism checks. The separate physical-origin report contains their derivations and primary-source references; these diagnostic calculations do not add new claims to the main TeX document.
