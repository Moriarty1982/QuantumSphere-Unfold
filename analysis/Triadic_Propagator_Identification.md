# Triadic Interaction, Propagator and Invariant Loop Phase

Date: 2026-10-15. Status: exact conditional reduction of the written block architecture, not a native mass-spectrum or gravitational-operator identification. This analysis note does not add a section to the main TeX document.

## Result

The source's three-probe interaction supplies a concrete place where the proposed phase correction could arise. The OP5 working note already prepared its symbolic relay, retarded response, invariant interference phase and fixed-reversal tests. This follow-up connects that preparation to the newer generation-coupling candidate rather than presenting those earlier results as new discoveries. Eliminating the third channel gives an energy-dependent effective link, accompanying diagonal resonance shifts and a linked norm response. The link correction cannot be varied independently of those diagonal terms in a positive-gapped realization.

The meaningful scalar phase is a closed-cycle phase, not the individual choice of frame phases. Endpoint/frame rephasings preserve that cycle phase exactly. A nonzero cycle phase can change the spectrum at fixed coupling magnitudes, but the source's admissibility, Hermiticity and cyclic symmetry do not determine it. The inherited phenomenological phase law remains an assumption; this calculation does not derive its proposed correction.

An explicit tensor-factor witness now shows that a generation-dependent coupling phase can change the effective spectrum while preserving a fixed probe-exchange involution. This does not preserve the visible-only projector or supply the native generation embedding. Ordered background derivatives also give a concrete phase- and pole-response test. There is a possible geometric route through the source's resonance connection and curvature; using it requires represented, norm-consistent transport and specified paths. It is not already a gravitational holonomy, a spacetime tunnel or a wormhole.

The subsequent [phase-selection derivation](Phase_Selection_Derivation.md) audits the actual variational boundary. Its explicit minimal-native substitution shows that the matching penalty vanishes on `H_C=Lambda`; the earlier weighted residual-projection minimum remains conditional and is not derived from that native functional. The [source/backreaction follow-up](HC_Source_Backreaction.md) evaluates the spin source and a cyclic conservation obstruction, then constructs a fixed-radius positive-cone phase minimum only after replacing exact matching by an independently constrained positive-field variation. Its compensator has rank one and the selecting source/penalty ratio is input, not a native prediction. Releasing its unsupported radius or scale removes full stationarity; additional native shape/scale laws are necessary. The historical target remains a diagnostic, not a derived angle.

## 1. Actual Source Dictionary and Conditional Realization

The retained source `sources/research/parts/v470/10_sphaera_and_physics.tex` gives the relevant architecture at:

- `prop:triadic-two-probe`: two probe blocks, a complementary third component, direct coupling `g_Y T_12` and complementary couplings weighted by `chi`.
- `thm:master-field-equation`: the full effective resonance operator `Omega`.
- `thm:variational-form`: a proposed action, but no evaluated interaction matrices.
- The definitions "Covariant probe derivative" and "Curvature and closure current": a connection and its curvature, not evaluated transport phases on a specified cycle.

Write a finite canonical realization as

```text
Omega_tri = [[A1,   C12,  W1*],
             [C12*, A2,   W2*],
             [W1,   W2,   D  ]],
C12 = g_Y T_12,       Wi = chi T_perp_i,       D = Omega_perp.
```

`A1,A2` are Hermitian. Adjoint relations on the reverse links are additional requirements of this realization: if the source writes the same scalar coupling in both directions, its reality or an equivalent conjugation convention must be supplied. Assume `D >= Delta_min I > 0` on the retained complementary space, and real energy `E < Delta_min`. Neither a positive gap nor a numerical generation representation has been extracted from the source.

The block labels are probe components. Their identification with matter/tachyon/photon frames, or with the three lepton generations, is not made automatically. A signed first-order probe energy is not by itself a physical charged-lepton mass; the earlier chiral/kinetic matching obligations remain.

The source's resonance matrix is not automatically a time Hamiltonian. The following finite energy-domain realization additionally assumes a licensed positive-current modal reduction, kinetic normalization and operator domains. The three relevant preparations in `analysis/OP5_QAM_Residual_Lift.tex` are `sec:native-triadic-phase-metric-test`, `sec:native-normalized-readout` and `sec:hc-even-slow-supply`. The note also already gives the full-field kernel `V_2 R_X^ret U_1` and its ordered metric variation. In a stationary reduction `R_X(E)=(E-D)^(-1)=-(D-E)^(-1)`, so its plus-sign retarded relay agrees with the minus-sign Schur response used below. Spatially varying vertices must remain in order, including the intermediate homogeneous initial-data term in a time-domain solution.

## 2. Exact Effective Link and Pole Equation

The third row gives

```text
y = -R(E) [W1 x1 + W2 x2],       R(E)=(D-E I)^(-1).
```

Substitution into the first two rows yields

```text
Omega_eff(E) = [[A1-N11(E),       C12-N12(E)],
                [C12*-N21(E),    A2-N22(E)]],
Nij(E) = Wi* R(E) Wj.
```

In particular,

```text
C12_eff(E) = g_Y T_12 - W1* (Omega_perp-E I)^(-1) W2.
```

This is the interference of a direct link with an indirect link through the third component. It specializes the earlier prepared mediator correction. With a constant real scalar `chi`, the indirect term is `-chi^2 T_1perp (Omega_perp-E I)^(-1) T_perp2`. If `chi` varies spatially, it cannot be pulled through the propagator; the ordered vertices must be retained.

The poles solve `det(E I-Omega_eff(E))=0`. Evaluating `Omega_eff(0)` and diagonalizing once is a low-energy approximation, not the exact problem. More precisely, off the complementary spectrum,

```text
det(E I-Omega_tri)
    = det(E I-D) det(E I-Omega_eff(E)).
```

The numerical report checks this reduction through the exact full eigenvectors, including unequal probe dimensions and noncommuting blocks. Scalar illustrative low poles are `0.4137723267` and `0.9690076581` in arbitrary declared energy units, with Schur residuals below `2e-15`. These values are not lepton predictions.

## 3. A Phase Correction Cannot Be Added Alone

For `W=[W1 W2]`, the joint response `N(E)=W*R(E)W` is positive. Put `Li=R(E)^(1/2) Wi`. Then `Nij=Li*Lj`, and Cauchy-Schwarz gives

```text
|x1* N12 x2|^2 <= (x1* N11 x1)(x2* N22 x2).
```

For scalar links this becomes `|N12|^2 <= N11 N22`. A nonzero off-diagonal mediated correction therefore requires nonzero diagonal responses. A proposed matrix containing the new off-diagonal term but zero diagonal shifts has a negative eigenvalue and cannot be this positive response. Bare/direct terms may compensate a diagonal shift, but that compensation must be derived rather than silently deleted.

The exact reconstructed-state norm is

```text
||x||^2+||y||^2 = x* [I+N'(E)] x,
N'ij(E) = Wi* (D-E I)^(-2) Wj.
```

`I+N'(E)` is the reconstructed norm at that energy. Only in the expansion about a specified reference energy does it become the coefficient of a linearized generalized eigenproblem; the exact pole equation still contains `N(E)`.

An explicit scalar existence witness shows how a small phase rotation can occur consistently. At `E=0`, choose real `d>0`, nonzero direct `c`, and a target `c_eff=c exp(i delta)` with `delta_c=c_eff-c`. Taking

```text
w1 = sqrt(d |delta_c|),
w2 = -d delta_c/w1
```

gives `c-w1* w2/d=c_eff` and `N11=N22=|delta_c|`, saturating Cauchy-Schwarz. The code uses `c=0.2`, `d=3` in arbitrary energy units and the historically calibrated small rotation. Each mandatory diagonal response is about `0.00051320035`. The witness establishes existence, not a source selection law or a three-generation fit. Its raw zero-mode eigenvalue/determinant can be slightly negative at floating-point roundoff; the report retains those values and an explicit tolerance rather than treating them as physical instability.

The response is Hermitian below a positive gap. This is a coherent correction, not a derivation of dissipation or viscosity. A complex matrix entry does not imply an imaginary eigenenergy or a decay width.

## 4. The Physical Phase Lives Around a Cycle

For scalar links define the oriented cycle phase

```text
Phi = arg(conjugate(c) conjugate(w1) w2).
```

Under separate basis phases of the three probes, `Omega -> U* Omega U`, where `U=diag(exp(i alpha1),exp(i alpha2),exp(i alpha3))`,

```text
c  -> exp[i(alpha2-alpha1)] c,
w1 -> exp[i(alpha1-alpha3)] w1,
w2 -> exp[i(alpha2-alpha3)] w2.
```

All endpoint phases cancel from `conjugate(c) conjugate(w1) w2`. If one link is absent, there is no such triangle phase; assigning it zero would hide the missing cycle.

For scalar diagonal entries `a1,a2,d`, the determinant makes the spectral effect explicit:

```text
det(Omega_tri)
 = a1 a2 d - a1 |w2|^2 - a2 |w1|^2 - d |c|^2
   + 2 |c w1 w2| cos(Phi).
```

Thus phase-only changes of the cycle can alter the spectrum without altering the three link magnitudes. The spectrum sees `cos(Phi)`, not its sign by itself. Phase invariance under probe rephasing is also not by itself a claim of observable CP violation in a full chiral theory.

The illustrative independent-frame assignment `alpha=(pi beta_sym,-pi beta_sym,0)` with the written `beta_sym=0.5493` preserves the spectrum to numerical roundoff. Those phases are a diagnostic assignment, not a source-derived three-link law. More generally, endpoint differences around any closed cycle telescope to zero: such frame shifts cannot create a new cycle phase, although an already present cycle phase remains.

## 5. Relation to the Previous Cyclic Root Candidate

For the declared generation-root candidate

```text
B = a I + z U + conjugate(z) U*,       z=r exp(i theta),
```

the cycle `B_10 B_21 B_02=z^3` has phase `Phi_B=3 theta modulo 2 pi`.

| Diagnostic quantity | Value |
| --- | ---: |
| Original conditional cycle phase | `0.674385466392 rad` |
| Historical phase-inversion target cycle phase | `0.666687459003 rad` |
| Target-derived cycle-phase change | `-0.007698007388 rad = -0.441063334 degrees` |

This is three times the earlier relative-coefficient shift of approximately `-0.147021 degrees`. It is a **conditional target for a physical cycle calculation**, not a predicted gravitational phase. It applies only if a generation embedding identifies the native cycle with this cyclic root matrix. A phase of a mediated *individual link*, the native triadic-cycle phase and the generation-root-cycle phase must not be identified without that dictionary.

The inherited hypothesis `theta=pi-sqrt(2) asin(beta_sym)` already selects the original conditional value. The structural calculation here does not override it or supply its correction. Hermiticity and cyclic symmetry alone admit a continuous family of nearby phases with different spectra; numerical regression checks exhibit two such positive candidates. An independent phase-sensitive action, boundary condition or evaluated connection is needed to select a new value.

### The Fixed-HC Exchange Constraint Cannot Be Skipped

The OP5 note's scalar diagnostic uses a fixed exchange `J_s` of the first two probes, fixing the third. In that declared realization,

```text
||[Omega_tri,J_s]||_F^2
    = 2(a1-a2)^2 + 8(Im c)^2 + 4|w1-w2|^2.
```

Thus exact exchange preservation forces `a1=a2`, real `c` and `w1=w2`. For nonzero scalar links the cycle phase is then zero or pi. Adding an arbitrary small scalar cycle phase does not preserve this fixed guard. Co-transporting the involution is a passive chart operation, not permission to retain incompatible old states/readouts. This is a conditional probe-exchange statement, not an established identification with the native global reversal or the C7 projector.

### A Generation Tensor Can Remain Inside the Even Sector

Keep the probe and generation indices separate on `C^3_probe tensor C^3_gen`. Let each probe block now act on three internal generation coordinates. For real `c`, positive `mu,Delta` and the same declared `B(theta)`, choose

```text
A1=A2=-c I3,       C12=c I3,
W1=W2=mu B(theta)/sqrt(2),       D=Delta I3.
```

The resulting nine-dimensional Hermitian block commutes with `J_s tensor I3` for every allowed `theta`. In the exchange basis, its odd block is `-2c I3`, while its even block is exactly

```text
Omega_even = [[0,       mu B(theta)*],
              [mu B(theta), Delta I3]].
```

It therefore realizes the earlier six-dimensional coupling candidate without introducing a difference between the two probe legs. Changing the internal cyclic phase changes the even light spectrum while the fixed-exchange commutator stays exactly zero. The numerical compression errors are below `1e-15`, and the exact flat-gap formula is reproduced. This is a concrete reason to retain the generation tensor factor rather than treating three probe labels as three generations.

This also gives a source-product normalization, not a numerical scale prediction. If the equal canonical legs are `W1=W2=chi T_perp1`, the bright coupling is `V=sqrt(2) chi T_perp1`. Under `Tr(B*B)=1`,

```text
mu = sqrt(2) |chi| ||T_perp1||_F,
B = exp(i arg chi) T_perp1/||T_perp1||_F.
```

The common scalar phase of `chi` cancels from the normalized Gram matrix. Thus merely shifting `chi` by one overall phase does not provide the required internal cyclic phase; a change in the relative matrix elements of `T_perp1`, its propagation response, or the retained direct block must be calculated. The factor `sqrt(2)` comes from normalized equal-leg projection, not from a new physical scale supplied by channel counting.

This construction is an existence witness, not a native derivation: the three-generation embedding, `B(theta)`, its phase law and the cancellation `A1+C12=0` were chosen. Nor does evenness establish strict visible closure. The projector onto the visible three-generation input does not commute with this operator; the light states still have complementary components. In the test its projector commutator has Frobenius norm `0.5656854...`, while the declared exchange commutator is zero. Native Q/C7/C4/C6 and chiral-mass requirements must be evaluated separately. In particular, this witness does not prove the remaining C5 threshold or identify the third C5 residual with a probe/generation index.

## 6. Where a Geometric or Gravitational Cause Could Enter

The source already names a connection

```text
Gamma_mu = i A_mu + kappa H_C n_mu + eta (I-P) n_mu,
D_mu = partial_mu + Gamma_mu,
F_mu_nu = [D_mu,D_nu].
```

For a specified norm-preserving connection and a specified closed path, transport can carry a gauge-invariant holonomy. [David Tong's original gauge-theory lectures, section 2.1.3](https://www.damtp.cam.ac.uk/user/tong/gaugetheory/2ym.pdf), give the Wilson-line transformation and closed-loop construction. This is a standard transport mechanism, not a result about the paper's physical sectors.

In a declared Abelian, norm-preserving subsector with `D=partial+i a`, the parallel-transport convention is

```text
U_loop = exp(-i integral_loop a).
```

If the loop bounds a declared smooth surface in a chart where the Abelian connection is defined, Stokes' theorem gives `Phi=-integral_surface f`, with `f=da` and the chosen orientation. A pure endpoint phase has no such contractible-loop flux. Non-Abelian transport instead needs path ordering and conjugation-invariant loop data; one cannot replace the entire matrix curvature by this scalar formula. Flat connections on noncontractible loops are a separate possibility and are not ruled out by the contractible-loop statement.

Several missing steps prevent calling the present cycle gravitational:

1. The three source probe components have not been mapped to three transport paths. An abstract interaction triangle is not yet a spacetime loop.
2. The source's resonance curvature is not identified with gravitational Riemann/spin curvature. A physical geometric derivation must specify the connection, representation, paths and their relation to the triadic matrix elements.
3. Norm compatibility is not automatic. In a positive internal metric `K(x)`, parallel transport by `partial+Gamma` preserves the norm if `partial_mu K=Gamma_mu* K+K Gamma_mu`. For constant identity metric this requires `Gamma_mu*+Gamma_mu=0`. The written real-coefficient compensator/penalty additions need not meet that condition. This observation concerns the internal transport reading; it is not by itself a verdict on unitarity of the complete spacetime spinor equation, whose current and metric must be supplied.
4. A universal spin/geometric factor does not automatically produce a generation-dependent mass hierarchy. The mode/generation projection has to supply the needed nontrivial action, and all kinetic, gap and diagonal corrections must be retained.

An evaluated holonomy is therefore a plausible route to a physical loop phase. Merely labelling a cross term gravitational, or identifying the graph triangle with a wormhole, is not that derivation. No new spacetime topology is required by the algebra above.

### Background-to-Phase and Background-to-Pole Derivatives

The OP5 note already supplies the ordered response variation. In the present stationary convention, for a specified parameter/background perturbation and `u(E)=w1*R(E)w2`,

```text
delta u = (delta w1)* R w2 + w1* R (delta w2)
          - w1* R (delta D-delta E I) R w2.
```

For nonzero scalar modal amplitudes `c,u`, the invariant path-relative phase and effective-link phase have distinct derivatives:

```text
delta Phi = Im(delta u/u - delta c/c),
delta arg(c_eff) = Im[(delta c-delta u)/(c-u)].
```

These require a specified modal contraction; a matrix-valued vertex has no single scalar phase without it. Changes of the modal states themselves contribute additional variation terms. At a zero amplitude a differentiable phase is not defined.

For a single positive scalar gap, varying only the real gap changes `u` by a real factor. It cannot rotate `arg(u/c)` at fixed vertices, but it can rotate `c-u` by changing the weight of an already phase-shifted indirect path. With two hidden modes, even a variation of real gaps can rotate `u`: their differently phased contributions are reweighted. The supplied two-mode example has `d Phi/ds=0.0197894085...` per declared arbitrary background parameter. This is not a calculated gravitational response; the native map from curvature/fields to `delta D,delta w_i,delta c` is still missing. It shows why an additional elementary phase or holonomy is not the only possible cause of a changed effective phase.

For a simple pole in the full Hermitian finite realization, the actual energy response is more informative than a link phase alone. Let `A=[[A1,C12],[C12*,A2]]`, `W=[W1 W2]`, and let `x` be its retained pole coordinate. With the variation of `N` taken at fixed `E`, differentiation of the pole equation gives

```text
delta E = x* [delta A-delta N(E)|fixed_E] x
          / {x* [I+N'(E)] x}.
```

The denominator is the full reconstructed-state norm. A numerical example agrees with direct full-Hamiltonian eigenvalue differentiation within `4e-18`. This is the usable interface to the prepared metric/coframe derivative: evaluate its induced block variations, then compute pole shifts and residues together. It does not bypass the source's background solution, current conservation, fixed-domain and chiral-mass conditions. If the third component is actually gapless, the positive-gapped expansion used here must be replaced by its evaluated causal propagator; a photon-frame label alone does not select that operator.

## 7. The Earlier Planck/Electroweak Restriction Still Matters

For scalar links `|w1|,|w2| <= mu_EW`, a flat Planck mediator and `E=0`,

```text
|delta c| <= mu_EW^2/m_P = 2.48278e-15 GeV.
```

If additionally `|c|=mu_EW/sqrt(12)`, the mediated correction lies inside a disk around `c` with relative radius `4.93994e-17`. The maximum angular deflection is at most the arcsine of that radius. A fixed-modulus rotation by the previously calibrated `|delta theta|` would instead require about `0.128966 GeV`, larger by `5.1944e13`.

This is a bound for those explicit scale choices, not an exclusion of all Planck sectors, non-flat gaps, low-lying modes, intermediate couplings or a fundamental phase-bearing direct interaction. It shows that an electroweak-strength, Planck-gapped virtual mediator is not a quantitative explanation of the fitted phase shift in that particular setup.

## What Has Been Determined and What Remains

The prepared triadic block is now connected explicitly to the generation-coupling calculation: there is an energy-dependent propagator reduction, a positive-response consistency bound, the scalar fixed-exchange obstruction, an internally generation-resolved even-sector witness, and phase/pole derivatives for a specified background variation. A possible connection/curvature route is identified without treating frame-coordinate shifts as dynamics. The pre-existing relay/interference results remain credited to the OP5 preparation.

The native numerical problem remains underdetermined. The source still must provide `g_Y T_12`, `chi T_perp_i`, `Omega_perp`, a generation embedding and either a phase-selecting interaction or represented transport paths. Those are the exact missing inputs, rather than a need for a different number-tag convention. Their projection must also meet the charged-lepton chiral and gauge-matching requirements noted in the physical-origin diagnosis.

## Reproduction

`python -B analysis/Coupling_Scale_Candidate.py --output analysis/Coupling_Scale_Candidate.json` updates the separate `triadic_propagator_diagnosis` record. It includes an exact-pole check, independent-frame rephasing test, fixed-modulus cycle examples, conditional cyclic-root target, a consistent mediator witness and the conditional scale bound. Source-defined architecture, added finite assumptions and target-derived diagnostics have separate fields.

`scripts/qsc_audit/tests/test_triadic_propagator.py` adds 34 tests covering noncommuting/unequal blocks, exact poles and norms, Cauchy-Schwarz and diagonal-response obligations, input guards, invariant/absent cycles, pure-frame and genuine cycle-phase changes, the determinant formula, cyclic phase freedom, mediator scale suppression and conditional Abelian transport examples. They also verify the prepared scalar exchange defect, the internally generation-resolved even-sector construction and its visible-projector leakage, ordered background/gap/energy variations, different scalar/multimode phase responses, the simple-pole derivative and source-preparation anchors. They are finite regression checks, not a native physical closure proof. The main TeX source and its 1,031-page measurement are unchanged.
