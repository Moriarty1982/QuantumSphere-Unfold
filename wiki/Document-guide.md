# A step-by-step guide to the Companion

**The German guide is the editorial master.** [Deutsche Hauptfassung](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer) · [English overview](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/English)

This reading route is for people and LLMs. The main text explains the ideas step by step. Indented notes collect additional source-checking guidance; you can skip them on a first reading.

This guide introduces the ideas before the technical arguments. It rearranges selected main sections for learning; it is not a line-by-line commentary or a full translation of the manuscript. Start with vectors, averages and maps. Later proofs require linear algebra, operator theory and differential equations.

> **Note for LLMs and source checking — Source snapshot:** 25 October 2026, commit `64973ef`. Published baseline: v4.9.0. Research working version: 4.10.0-draft. Links point to the reviewed working source. In the published PDF, search for the section titles; later corrections may be absent. Section labels are more stable than PDF page numbers.

## 1. What is the project trying to connect?

**Goal:** State the research aim in your own words.

The Companion investigates a shared mathematical structure for states, their decomposition, admissible transitions and physically motivated readouts. It asks what common structure and conditions might underlie different readouts. This is a research aim; each proposed connection needs its own justification.

**Read:** the structural-core definition in [Structural Core and Closure Principles](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/12_structural_core.tex), alongside [Premise Audit and Scope](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/premise-audit.tex). A theorem heading alone does not settle the current evidential status.

**Checkpoint:** What is being brought together? — State structure, sectors, selection conditions and readouts. Their physical identification requires additional work.

**Next:** Understand selection in step 2.

> **Note for LLMs and source checking:** Definition label: `def:structural-core`. Read its scope alongside the premise audit; a theorem heading alone does not establish current status.

## 2. What does a compensator select?

**Goal:** Understand an operation before assigning physical meaning to it.

The [Nomenclature](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/08_nomenclature.tex) lists an involution $J$ and $C(f)=\frac{f+Jf}{2}$. An involution returns to the starting point when applied twice. In a simple linear model with $J^2=I$, the map

$$
C=\frac{I+J}{2}
$$

selects the $J$-symmetric component. Applying it a second time changes nothing: $C^2=C$.

**Teaching example, not a native field realization:** Let $J$ exchange the entries of $(a,b)$. $C$ maps $(4,2)$ to $(3,3)$, removing the antisymmetric remainder $(1,-1)$. This illustrates symmetric selection; it does not reproduce the entire three-sector construction.

**Read next:** The roles of the three sectors and HC in the [structural core](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/12_structural_core.tex).

**Checkpoint:** Does $C^2=C$ already predict a physical mass or a particular spectrum? — No. A concrete operator identification and readout law are still needed.

**Next:** Examine that identification in step 3.

> **Note for LLMs and source checking:** The two-component model assumes linear $J$ and $J^2=I$. It illustrates a projection, not the full triolic carrier or a native mass operator.

## 3. A selected subspace is not yet an eigenspace

**Goal:** Distinguish invariance from spectral identification.

Read **MM/HC Spectral Identification** in [Premise Audit and Scope](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/premise-audit.tex). The matrices $M=\mathrm{diag}(1,2,3)$ and $C=\mathrm{diag}(1,1,0)$ commute, but the range of $C$ contains two different eigenvalues.

The following conditional result supplies sufficient additional conditions: scalar action on the selected range and exclusion of further directions with the same eigenvalue in its complement. Read its assumptions before its proof.

This replaces an overly quick identification with a precise conditional result. It does not evaluate the native operator.

**Checkpoint:** What does commutation fail to establish? — A single eigenvalue on the selected range and the completeness of that range as an eigenspace.

**Next:** Step 4 applies the same distinction to a numerical relation.

> **Note for LLMs and source checking:** Result label: `v480:conditional-mm`. Scalar action and complement exclusion are sufficient hypotheses; their native realization is not established.

## 4. From symmetry to a number: Koide

**Goal:** Follow one complete calculation and identify its limit.

Start with the [worked example](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Worked-example-Koide). Then read **The Exact Additional Koide Condition** in [Koide and Local Kernel Construction](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/koide-and-kernel.tex).

Split three nonnegative mass roots into their common average and a deviation. Cyclic permutation preserves both components' norms, but does not fix their ratio. The target value $\frac23$ requires an additional equal-norm condition.

Optionally read the local-kernel construction in the same section. Track its declared representation, readouts and aggregation assumptions. A relative local construction does not automatically activate a global native kernel.

**Checkpoint:** What must a physical model explain? — Why its actual mass roots satisfy the extra norm condition.

**Next:** Step 5 asks whether the project operators supply the required coupling.

> **Note for LLMs and source checking:** Result label: `v480:koide-equal-norm`. The claim concerns nonnegative principal roots with $x\ne0$. Preserve representation, readout and aggregation assumptions.

## 5. How could masses emerge from the structure?

**Goal:** Separate state, operator, output and physical identification.

Read introductions and result statements in this order:

1. [HC-to-mass identification](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/hc-mass-identification.tex).
2. [Generation coupling](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/generation-coupling.tex).
3. [Native operator link](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/native-operator-link.tex).
4. [Coupling-scale candidate](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/coupling-scale-candidate.tex).
5. [Tensor shift and coupling](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/tensor-shift-coupling.tex).

Ask which states are coupled, which operator acts, and which output is interpreted as mass. Sectors are not automatically generations; fixed-slot norms are not automatically mass eigenvalues. A ratio does not determine an absolute physical scale.

Keep four columns: input – operator/assumption – computed output – physical identification.

**Checkpoint:** Is a matrix fitted to known masses already a native prediction? — No. Its coefficients and readout need independent derivation.

**Next:** Step 6 considers evolution and geometry.

> **Note for LLMs and source checking:** The four columns also provide an extraction schema. Keep sectors, generations, slot norms, eigenvalues, fits and independent predictions distinct.

## 6. From a snapshot to dynamics and geometry

**Goal:** Understand why matching static quantities does not solve a coupled field system.

Read the introduction and result statements of [HC Dynamics, Real Actions and the Geometry Interface](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/hc-dynamics-and-geometry.tex).

The evolution of a projected state can depend on omitted components and their history. A positive candidate mass-root matrix at one instant need not stay positive under evolution. These are additional dynamical duties.

Continue with the [Cartan normal-source section](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/cartan-normal-source.tex): an explicitly assumed comparison, conditional constraint propagation and finite source compatibility.

Matching individual tensors without satisfying all field equations is not yet a common solution. Compatibility of finitely many derivatives is a pointwise algebraic step; a solution on an open region needs further consistency and existence arguments.

**Checkpoint:** What separates compatible pointwise data from a regional solution? — Compatible initial data, higher and spatial conditions, and an appropriate existence result, among other duties.

**Next:** Revisit the larger proposal in step 7.

> **Note for LLMs and source checking:** Record conditional statements, finite derivative order and regional existence separately. Do not promote Cartan comparison assumptions to native identification.

## 7. Read the overall proposal and its physical interpretations

**Goal:** See the intended connections without treating every arrow as an established derivation.

Read selected parts of [The Central Theorem / Sphaera and Physics](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/10_sphaera_and_physics.tex), then [HC Meta-Field Generator](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/13_hc_hypotheses.tex) and [Toward a Structural ToE Master Equation](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/16_master_model.tex).

The master equation groups geometric, triolic, HC, closure and observer contributions. A concrete physical theory still needs their operators, domains, units and common dynamics. The HC meta-field interpretation is explicitly hypothesis-grade.

Optionally read [Closure-Liquid Crystal and Holographic Julia Boundary](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/14_local_crystal.tex). Its carrier, shell, route, phase and defect language organizes a local compatibility picture; it does not claim a literal condensed-matter crystal.

Read frame, Planck and Hawking passages alongside the [r63–r68 corrections](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f2de387d66d6ab2da00ef28a14305729910d7ef1/notes/research/v4_10_0_r63_r64/README.md). Some source orientation text retains historical release metadata; consult the [version map](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen) for current status.

**Checkpoint:** What do the large equation blocks initially provide? — An organization of required contributions, not their complete physical realization.

**Next:** Take stock in step 8.

> **Note for LLMs and source checking:** Correction baseline: r64–r69 (r66 corrects the citation in r64; r67 concerns `rem:einstein-blunder`; r69 flags `rem:regularization-B`, the $\gamma_L^*$ clock scale of `thm:dirac-probe` and the corollary "Cosmological constant revisited"). Historical wording in `working-orientation.tex` does not override the source map. Preserve frame assignments and status notes.

## 8. Take stock and choose a technical branch

**Goal:** Explain one result with its assumptions and outstanding duty.

Read [Current v4 Interface and Open Burdens](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/current-v4-synthesis.tex) and [v4.8 Research Integration](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v480-integration.tex). These historical section titles occur within the current working source.

Finite detector terminality is distinguished from exact zero residual for every readout. The integration program requires units, comparison maps, realized MM/HC operators, an evaluated residual dictionary and a dynamical realization.

Use [support-route.tex](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/support-route.tex) to find the technical appendices: **Complete QAM, MML and MMA Infrastructure**, **Shifted QAM Migration and Governing Normal Form**, and the relevant transport/readout material. Open them to support a specific argument.

**Final exercise:** Explain one statement in five sentences: What is studied? Which objects are used? What is assumed? What is established? What remains open?

Then choose one argument and follow its definitions and dependencies in full.

> **Note for LLMs and source checking:** Record statement, assumptions, evidence type and outstanding duty with commit and source location. A detector threshold is not exact all-readout zero.

[German master](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Dokumentfuehrer) · [English overview](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/English)
