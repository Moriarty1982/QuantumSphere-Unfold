# Dirac fluctuations and a conditional induced Einstein term

## Status and question

The [stress-to-metric pullback](HC_Stress_Metric_Pullback.md) assumed an Einstein response. Can the prepared triadic Dirac carrier produce its leading geometric kinetic term instead?

**Conditional answer:** a regulated, parity-even Dirac determinant produces a positive Einstein coefficient in a declared four-dimensional Euclidean comparison. This supplies a concrete mechanism for the previously assumed effective-action term. It does **not** derive a native metric, the physical Newton constant or the native trace-formula theorem. It also generates an unsuppressed vacuum term, obstructing an unsubtracted weak-curvature interpretation.

This is a separate analysis, not a change to the main TeX or OP5 note. The numbers below are in the previous comparison's unspecified mass units, not SI/Planck predictions. Sections 8-11 continue the vacuum question: an explicitly additional scalar comparison cancels the flat vacuum coefficient without cancelling the Einstein term, but the native field content has not been identified with its required partners.

## 1. What the native text actually supplies

The inherited [trace-formula Einstein claim](../sources/research/parts/v470/10_sphaera_and_physics.tex), label `thm:einstein`, identifies `Tr exp(-i tau L0)` with a heat kernel, then applies a variation formula for `Tr exp(-tau L0)`. These are different objects. The displayed dilation operator `L0=-i(x d/dx+1/2)` has not there been supplied with a four-dimensional metric-dependent elliptic realization, domain, trace regularization or justified continuation. The trace-formula remainder `R(tau)` is not thereby the spacetime Ricci scalar `R(g)`. The unweighted integral of `Sigma` also differs from the proper-time determinant measure `ds/s` below. Its structural argument does not close these gaps.

The later proposition `prop:bilinear-einstein-reconstruction` is a better conditional anchor: it explicitly **assumes** an Einstein-Hilbert term after coarse-graining. The present calculation evaluates one possible source of such a term, subject to additional operator assumptions. It does not prove those assumptions from `C7`, `M16` or HC closure.

There is a normalization issue too. A constant action density and a cosmological curvature coefficient cannot be denoted by the same number without conversion. With Lorentzian conventions

\[
 S_L=\int\sqrt{|g|}\,[A R-\rho+\mathcal L_m],\qquad
 T_{\mu\nu}=-\frac{2}{\sqrt{|g|}}\frac{\delta S_m}{\delta g^{\mu\nu}},
\]

metric variation gives

\[
 G_{\mu\nu}+\frac{\rho}{2A}g_{\mu\nu}
 =\frac{1}{2A}T_{\mu\nu}.
\]

Thus a density written **plus** `Lambda_eff` in that proposition's action would give `Lambda_cos=-kappa_eff Lambda_eff`, not literally the same `Lambda_eff` in its field equation. We keep `rho`, `A` and `Lambda_cos` distinct. No inherited source has been silently rewritten.

## 2. Additional comparison assumptions

Supply a smooth Riemannian four-dimensional spin metric, a torsion-free compatible spin connection, and a positive elliptic Dirac square. On a closed manifold, or locally away from boundaries,

\[
 D_E^2=-\nabla^2+\frac14R,\qquad
 L=D_E^2\otimes I+I\otimes M^2.
\]

Here `M` is a constant finite Hermitian internal mass matrix, commuting with the spacetime Dirac operator. For a noncompact metric, the displayed traces mean regulated/local densities, not a finite unregulated volume trace. We compute only the parity-even modulus of a complex Grassmann Dirac determinant. Its phase, possible anomalous phases and mass-sign effects in that phase are not evaluated.

These assumptions neither construct spacetime nor establish an admissible Wick rotation for the native model. The same-induced-coframe trace obstruction from the earlier analyses remains in force under its hypotheses. An independent metric-dependent Dirac operator is not an escape from that obstruction.

The standard induced-gravity mechanism and its curvature/vacuum coefficients are developed in [Chaichian, Oksanen and Tureanu, sections 4.2-4.3](https://arxiv.org/html/1805.03148v1). We specialize to torsion-free Dirac matter, without adding the paper's nonminimal torsion couplings.

## 3. Determinant and heat coefficient

Grassmann integration gives `Gamma_E=-log det(slash nabla+M)`. Its even part can be regulated by

\[
 \Gamma_E^{\mathrm{even}}
 =-\frac12\operatorname{Tr}\log L
 \;\widehat{=}\;
 \frac12\int_{U^{-2}}^{v^{-2}}\frac{ds}{s}
                \operatorname{Tr}e^{-sL},\qquad U>v\geq0.
\]

The hat declares the chosen proper-time regularization, including its power-divergent local terms, not a regulator-independent equality of finite determinants. At `v=0`, the upper endpoint is infinity. The window is not an evaluated native fast/slow projector.

For a Laplace-type operator `-nabla^2+B`, the first local coefficients are `I` and `R I/6-B`. With `B=R I/4` and four complex spin components,

\[
 \operatorname{tr}_{\rm spin}a_0=4,\qquad
 \operatorname{tr}_{\rm spin}a_2=4\left(\frac16-\frac14\right)R=-\frac13R.
\]

The internal mass factor separates exactly:

\[
 \operatorname{Tr}e^{-sL}\sim\frac{1}{(4\pi s)^2}
 \int\sqrt g\;\sum_j e^{-s m_j^2}
       \left[4-\frac{sR}{3}+O(s^2)\right].
\]

The omitted terms include curvature-squared and derivative terms. It follows that

\[
 \Gamma_E^{\mathrm{even}}
 =\int\sqrt g\,[\rho_{\rm ind}-A_{\rm ind}R+\cdots],
\]

\[
 I_j=\int_{U^{-2}}^{v^{-2}}s^{-2}e^{-m_j^2s}\,ds,\quad
 J_j=\int_{U^{-2}}^{v^{-2}}s^{-3}e^{-m_j^2s}\,ds,
\]

\[
 \boxed{A_{\rm ind}=\frac{\sum_j I_j}{96\pi^2}>0},\qquad
 \boxed{\rho_{\rm ind}=\frac{\sum_j J_j}{8\pi^2}>0}.
\]

With the Euclidean Einstein convention `Gamma_E=int sqrt(g)[rho-R/(16 pi G)]`,

\[
 \frac1{G_{\rm ind}}=16\pi A_{\rm ind}
 =\frac{\sum_j I_j}{6\pi},\qquad
 \kappa_{\rm ind}=\frac1{2A_{\rm ind}}=8\pi G_{\rm ind}.
\]

For `N` massless Dirac species,

\[
 I=U^2-v^2,\quad J=\frac{U^4-v^4}{2},\quad
 \frac1{G_{\rm ind}}=\frac{N(U^2-v^2)}{6\pi}.
\]

At `v=0` this agrees with the pure-Dirac leading term in [equation (81) of the induced-gravity calculation](https://arxiv.org/html/1805.03148v1#S4.E81). The positive power-divergent coefficient is a statement about this regulator and field content, not a universal finite prediction independent of renormalization conditions.

## 4. Independent sphere-spectrum check

On a round auxiliary `S4` of radius `a`, the self-adjoint Dirac eigenvalues are `+/- (n+2)/a`. The degeneracy **per sign** is `2(n+1)(n+2)(n+3)/3`, specializing [Camporesi and Higuchi, equations (3.26), (3.44)](https://arxiv.org/pdf/gr-qc/9505009). Both signs must be retained for the squared operator:

\[
 K(s)=\frac43\sum_{k=2}^{\infty}(k^3-k)e^{-s k^2/a^2},\quad
 V=\frac{8\pi^2a^4}{3},\quad R=\frac{12}{a^2}.
\]

Euler-Maclaurin expansion gives

\[
 K(s)=\frac{2a^4}{3s^2}-\frac{2a^2}{3s}+\frac{11}{90}+O(s/a^2).
\]

Consequently `[(4 pi s)^2 K(s)/V-4]/(s R)` tends to `-1/3`, confirming the spin trace and sign without building them into the spectral sum. At `a=1`:

| s | extracted coefficient |
| --- | ---: |
| 0.0200 | -0.332107809 |
| 0.0100 | -0.332721399 |
| 0.0050 | -0.333027572 |
| 0.0025 | -0.333180504 |

For `alpha=s/a^2` and `K>=sqrt(3/(2 alpha))`, the discarded positive tail is bounded by

\[
 \frac43\sum_{k>K}(k^3-k)e^{-\alpha k^2}
 \leq\frac{2(\alpha K^2+1)e^{-\alpha K^2}}{3\alpha^2}.
\]

The script chooses `K` using this bound; truncation is far below the displayed asymptotic error. This sphere is an independent auxiliary spectral check, not a derived native background.

## 5. Prepared triadic example

Reuse the earlier declared Hermitian matrix, without fitting new entries:

\[
 M=\begin{pmatrix}0.6&0&4\\0&0.6&0.7\\4&0.7&0.6\end{pmatrix},\quad
 m_j=0.6,\;0.6\pm\sqrt{16.49}.
\]

The signed eigenvalues are approximately `(-3.460788101,0.6,4.660788101)`. A negative Dirac mass eigenvalue is **not** a negative `m^2` or evidence for a tachyon frame. The even determinant depends on their squares. Constant internal unitary conjugations, including diagonal phase changes, cannot alter its coefficients. A spacetime-dependent transformation would require transforming the connection too; freezing that connection is not a pure frame comparison.

At `U=20`, `v=2`, the evaluated coefficients are

\[
 A_{\rm ind}=1.133530367,\quad \rho_{\rm ind}=2882.555008,\quad
 G_{\rm ind}^{-1}=56.97745077,\quad\kappa_{\rm ind}=0.4410997841.
\]

Independent quadrature of the truncated determinant at `R=0.01` gives `2882.5436727761`, agreeing with `rho-A R`. Changing the regulator scale changes the induced coefficients. These are not measured couplings or an evaluation of the native `C7/M16` representation.

## 6. Vacuum obstruction: a bound, not merely a large example

If no bare terms or other sectors cancel the induced density, the Einstein truncation would assign

\[
 \Lambda_{\rm cos}^{\rm trunc}
 =\frac{\rho_{\rm ind}}{2A_{\rm ind}}
 =6\frac{\sum_j J_j}{\sum_j I_j}.
\]

For each squared mass `q>=0`, `J/I` is the expectation of `1/s` with positive weight `s^-2 exp(-q s)`. It is less than `U^2`. Increasing `q` shifts weight towards smaller `s`, increasing this expectation: where differentiable its derivative is `-Cov_q(1/s,s)>=0`. The massless value is `(U^2+v^2)/2`; at `v=0` use continuity from positive `q`. A positive weighted average over species preserves both bounds. Therefore

\[
 \boxed{3(U^2+v^2)\leq\Lambda_{\rm cos}^{\rm trunc}<6U^2}.
\]

Increasing the number of identical species, changing their constant relative phases or choosing different nonnegative `m_j^2` cannot make this ratio parametrically small. In the sample, `Lambda_cos_trunc=1271.494392`, giving the formal Einstein-vacuum trace `R_trunc=5085.977566`, or `R_trunc/U^2=12.71494`.

**This is not a reliable prediction of an actual large-curvature vacuum.** Such curvature is outside the small-proper-time/weak-curvature truncation used to obtain it; higher terms cannot be neglected there. The result diagnoses why an unsubtracted near-flat Einstein limit is not self-consistently obtained by keeping just these terms. It does not solve the full one-loop equations or prove a universal no-go after adding other sectors.

The native statement that the fundamental photon-frame cosmological constant vanishes does not itself cancel this density in the common metric. A cancellation, matching relation, symmetry or alternative metric variation must be calculated, including its effect on the curvature term and stress conservation.

## 7. What would connect this to the previous response

Write the actual matched coefficients as

\[
 A_{\rm ren}=A_{\rm bare}+A_{\rm ind},\qquad
 \rho_{\rm ren}=\rho_{\rm bare}+\rho_{\rm ind}.
\]

They also receive any omitted-sector contributions. Choosing `rho_bare=-rho_ind` permits a flat vacuum in the Einstein truncation, but this is an **input subtraction**, not a microscopic explanation. Even then, the independent finite local counterterm `A_bare` changes `G_ren` while preserving flatness. No physical Newton or Planck scale has been uniquely derived.

If native matching supplies `A_ren>0`, controls `rho_ren`, and validates the low-derivative regime, metric variation of the induced leading term yields the Einstein operator used previously. Linearizing around an admissible nearly flat background then gives

\[
 -\frac12\Box\bar h_{\mu\nu}=\kappa_{\rm ren}T_{\mu\nu},\qquad
 h=-2\kappa_{\rm ren}P\Box_B^{-1}T+h_{\rm free}.
\]

This explains the **conditional origin** of that kinetic operator, not its boundary prescription. A Euclidean determinant does not choose a Lorentzian quantum state, a retarded Green function or the free gravitational data. The previous doubled-history/in-in distinction still applies. Curvature-squared coefficients, possible nonlocal form factors and stress fluctuations have not been evaluated here. Explicit low-energy probes must not be counted again as already integrated-out modes; the regulator window alone does not prove this separation.

The next native tasks are sharply identified: construct the metric-dependent operator and its physical scales, then evaluate the vacuum/matching conditions and omitted closure sectors. The present comparison is a calculable route to the assumed Einstein term, not an activation token or completion certificate.

## 8. Cancel the vacuum coefficient, not the whole operator

The native `thm:string-lqg-duality` labels the `J`-even/odd subspaces bosonic/fermionic; `prop:shared-vacuum-planck` supplies a shared-vacuum interpretation. Neither establishes independent Bose/Grassmann integration variables, their fluctuation spectra or the determinant weights. An orthogonal decomposition or a relative phase alone does not produce the minus sign from Grassmann integration.

For a concrete test, **add comparison real scalar fields**, with positive flat kinetic operators and nonnegative squared masses `q_b`. These are not asserted to be new native particles or identified HC excitations. Let

\[
 L_b=-\nabla^2+q_b+\xi_b R,\qquad
 \Gamma_{E,b}=+\tfrac12\operatorname{Tr}\log L_b.
\]

The bosonic proper-time contribution has the opposite sign to the Dirac contribution. Positivity is required on the geometries where the determinant is defined; nonnegative flat masses alone do not ensure it for arbitrary curvature. The following expansion is local near a suitable weak-curvature background.

With `q_f=m_f^2`, define

\[
 W_0(s)=4\sum_f e^{-s q_f}-\sum_b e^{-s q_b},\qquad
 B_2(s)=\frac13\sum_f e^{-s q_f}
       +\sum_b\left(\frac16-\xi_b\right)e^{-s q_b}.
\]

Our sign convention is fermion-minus-boson, opposite to a frequently used supertrace convention. The effective action through first curvature order is

\[
 \Gamma_E=\frac1{32\pi^2}\int\sqrt g
 \int_{U^{-2}}^{v^{-2}}ds\,
 \left[\frac{W_0(s)}{s^3}-R\frac{B_2(s)}{s^2}+\cdots\right].
\]

Thus the desired selective condition is

\[
 W_0(s)=0,\qquad
 A=\frac1{32\pi^2}\int ds\,s^{-2}B_2(s)>0.
\]

This is stronger than tuning the integrated vacuum term to zero at one chosen window. For finite spectra with fixed determinant weights, `W0(s)=0` on all positive proper times holds **if and only if** each distinct squared mass carries four real scalar modes per complex Dirac mode. Proof: group equal squared masses, multiply the resulting finite exponential sum by the exponential of its smallest mass, send `s` to infinity to isolate its coefficient, then repeat. Conversely, equality at each mass gives zero term by term. Infinite spectra, constrained fields and regulator-dependent weights require a separate theorem.

Do not demand equality of the **complete** opposite-sign metric-dependent heat kernels. If their regulated contributions agree for every metric, their difference is zero and so are all its metric variations, including the Einstein term. If only their traced `a0` and `a2` coefficients agree, only those orders are cancelled; higher curvature terms may remain. A useful vacuum cancellation must distinguish `W0` from `B2`.

This distinction between vacuum compensation, curvature coefficients and finiteness conditions is standard; see [Visser, sections 2, 5-6](https://arxiv.org/html/gr-qc/0204062v1). The scalar coefficient `1/6-xi` agrees with [Chaichian, Oksanen and Tureanu, equations (80)-(81)](https://arxiv.org/html/1805.03148v1#S4.E80). No native supersymmetry or protecting identity is inferred from this bookkeeping.

## 9. Explicit selective cancellation with the prepared masses

Take four real scalar partners for each of the three prepared Dirac masses, with the **same squared mass** and common curvature coupling `xi`. This gives twelve additional real scalar modes in the comparison. Then

\[
 W_0(s)=0,\qquad B_2(s)=(1-4\xi)\sum_f e^{-s m_f^2},
\]

\[
 \boxed{\rho_{\rm ind}=0,\qquad
 A_{\rm ind}=\frac{1-4\xi}{32\pi^2}\sum_f I_f}.
\]

The vacuum coefficient cancels exactly for every common proper-time window, not merely in the leading massless limit. The Einstein coefficient is positive for `xi<1/4`; it vanishes at `xi=1/4` and has the wrong sign for this comparison at `xi>1/4`. This is cancellation of the flat zero-derivative density, not a claim that the full curved-space vacuum stress or higher curvature terms vanish.

At the existing example's `U=20`, `v=2`:

| scalar coupling xi | rho | A |
| --- | ---: | ---: |
| 0 | 0 | 3.400591100 |
| 1/6 | 0 | 1.133530367 |
| 1/4 | 0 | 0 |
| 0.3 | 0 | -0.680118220 |

For minimal scalars, the paired `A` is three times the earlier pure-Dirac value. Independent integration of the mixed heat density at `R=0.01` gives `-0.034005911003`, agreeing with `-A R`. The numerical report marks a coefficient unresolved near exact zero rather than dividing floating-point cancellation noise.

Mass matching is essential. For a common scalar squared-mass splitting `q_b=q_f+delta`, keeping the Dirac masses fixed,

\[
 \left.\frac{d\rho}{d\delta}\right|_0
 =\frac{\sum_f I_f}{8\pi^2}=12 A_{\rm Dirac},\qquad
 \left.\frac{d\Lambda_{\rm cos}^{\rm trunc}}{d\delta}\right|_0
 =\frac{2}{1-4\xi},\quad\xi\ne\frac14.
\]

The first identity follows by differentiating `J(q)` under the integral: `J'(q)=-I(q)`. The second uses `rho(0)=0` and `Lambda=rho/(2A)`. For `xi=0`, `delta=1e-5`, the report gives `rho=0.000136023638` and `Lambda_cos_trunc=0.0000200000003`. Such a tiny freely chosen splitting is not a derived physical residual. At a fixed window the identity is one-loop bookkeeping; stability against interactions, different regulators or higher loops needs an independently derived symmetry or matching law.

Cancelling just the divergent mass moments is weaker. For the signed measure

\[
 (q,w)=(0,4),(1,-12),(2,12),(3,-4),
\]

the moments `sum w`, `sum w q` and `sum w q^2` all vanish, but

\[
 W_0(s)=4(1-e^{-s})^3>0\quad(s>0).
\]

This is realized in the comparison by Dirac squared masses `(0,2,2,2)` and scalar squared masses twelve times `1`, four times `3`. The finite-window density at `(U,v)=(20,2)` remains `0.00261500124`, not zero. Even ultraviolet finiteness is not a cancellation theorem for the finite vacuum density. This is the distinction in [Visser's equations (33)-(34)](https://arxiv.org/html/gr-qc/0204062v1#S5).

## 10. What is missing for a native identification

The native `thm:variational-form` contains the connection, projector, compensator and probe action, but no evaluated real gauge-fixed fluctuation Hessian with the partner spectrum just used. Gauge components must be combined with constraints, measure factors and Faddeev-Popov ghosts before assigning determinant weights. Gauge ghosts are not freely selectable physical partners.

In particular, the [previous null-axis HC calculation](HC_Null_Axis_Action_Check.md) gives a rank-one principal tensor in its fixed-axis commuting branch. Its compensator amplitude cannot simply be counted as an ordinary four-dimensional elliptic scalar mode. This is a limitation of that branch, not a proof excluding every full native coupled Hessian.

Likewise, the [native photon-frame balance definition](../sources/research/parts/v470/23_physical_readouts.tex), `def:tr-balance`, is not yet a computation of `W0` or `B2`. To use it here one must derive a common regulated metric-dependent determinant or its valid alternative and show its zero-derivative cancellation while its curvature variation survives. A distributional trace identity, a `J` projection, a normalization token or an absorption probability does not supply that map.

A reference subtraction also has to be distinguished from an explanation. Subtracting the constant `Gamma[g0]` at a fixed reference metric cannot remove the local vacuum stress: its variation with respect to `g` is zero. Subtracting `rho_flat int sqrt(g)` **does** remove the density but is precisely a local cosmological counterterm. It is not a newly derived cross-sector mechanism. The determinant path, measure, Ward identities and any protecting symmetry must decide which, if either, is native.

The usable target is therefore an evaluated signed fluctuation spectrum with the selective conditions above, or a demonstrably different native response. No twelve-scalar extension has been inserted into the main theory.

## 11. A necessary dimensional correction in the inherited balance argument

The native `rem:open` calls the `10^-122` hierarchy a unit-system artifact and compares `Lambda_obs ell_P^2` to a number of order `beta^2`. A dimensionless ratio cannot lose its hierarchy by changing units.

Using **only the rounded values already quoted in that source**, not new measurements,

\[
 \ell_P=1.616\times10^{-35}\,{\rm m},\quad
 \Lambda_{\rm obs}=1.1\times10^{-52}\,{\rm m}^{-2},\quad
 \beta=0.5493,
\]

gives

\[
 \Lambda_{\rm obs}\ell_P^2=2.8726016\times10^{-122},\qquad
 \beta^2=0.30173049.
\]

The written identification `Lambda_obs=beta^2/ell_P^2` therefore misses this dimensionless observed value by approximately `1.05e121`. The modest photon/matter length factor quoted in the paper does not remove that discrepancy. This is a failure of that particular scale identification, not of every possible frame-dependent effective action.

For an ordinary common rescaling of all mass scales by `f`, `A -> f^2 A`, `rho -> f^4 rho` and `Lambda -> f^2 Lambda`, while `G -> G/f^2`. Hence `Lambda G` (equivalently `Lambda ell_P^2` with restored `hbar,c`) is invariant. If native frame changes are intended to alter dimensionless physics rather than units, their action/observable map must be specified and tested; it cannot simultaneously be justified as a unit artifact. Density units `mass^4` must also remain separate from curvature units `mass^2`.

These findings stay in the analysis until a deliberate correction audits the inherited balance argument and its dependent claims. They are not silently converted into a repaired native theorem.

## Reproduction

The subsequent [closure-fluctuation Hessian analysis](HC_Closure_Fluctuation_Hessian.md) derives `delta Lambda=0` at an exactly closed background and separates hard HC matching from independent soft fluctuations. Its full constant-background Euclidean dagger comparison retains gauge/projector mixing and ghosts, but has anisotropic degeneracies and no ordinary four-dimensional HC heat spectrum. It does not identify the scalar partners above with native fields.

Run `python -B analysis/HC_Induced_Gravity_Heat_Kernel.py --output analysis/HC_Induced_Gravity_Heat_Kernel.json` from the repository root. The report and script preserve the assumptions and remaining obligations. The 34 original tests are in `scripts/qsc_audit/tests/test_hc_induced_gravity_heat_kernel.py`; 30 additional vacuum-balance checks are in `scripts/qsc_audit/tests/test_hc_vacuum_balance.py`. They cover the selective cancellation, independent quadrature, curvature-coupling signs, split-mass sensitivity, finite-moment counterexample, dimensional hierarchy and native-identification boundaries. Finite numerical regression tests supplement the displayed conditional derivation; they do not establish native physical closure.
