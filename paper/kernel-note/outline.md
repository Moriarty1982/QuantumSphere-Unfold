# Kernel note — outline and novelty check (draft, 15 Nov 2026)

**Working title:** *The electric–magnetic doublet as a two-level system: a biquaternion view of field invariants, duality and
the state disk*

**Type:** short expository note (8–10 pp.), not a research paper. **Status:** outline only; no text written.

This file records (1) the result of a literature check on the algebra-kernel material, (2) how it relates to the existing draft
in `../short/`, and (3) an outline for a re-scoped note. The decision whether to write it is open (Section 5).

## 1. Result of the novelty check

The kernel material is correct but, as far as the check goes, not new. This agrees with finding 1 of the internal referee report
(`../short/review/referee_report_2026-11-04.md`: "Sections 2–4 are correct but not new"). The check adds one close prior work
that the report does not name.

| Statement | Where in the repository | Prior work found | Verdict |
|---|---|---|---|
| Natural norm `N(q) = q q̄ = −t² + s`, multiplicative | v4.8.0-r06.1; `short/p2_kernel` Prop. 2.2 | `C⊗H ≅ M₂(C)`, `N = det`: standard | known |
| `SO(3,C) ≅ SO⁺(1,3)` acts on `z = E + iB`; `s` collects both invariants | r06 Reading B; Prop. 2.3 | Riemann–Silberstein literature: Bialynicki-Birula and Bialynicka-Birula, J. Phys. A 46 (2013) 053001, arXiv:1211.2655; arXiv:1211.1218; arXiv:1604.01876 | known |
| Orbits: level sets of `s`, punctured null cone, `{0}` | r06.3; Prop. 2.4 | invariant classification of fields (null / non-null, canonical frame with `E ∥ B`; Synge) | known |
| Duality `z ↦ e^{iα}z`, duality angle, two orbits under `SO(3,C) × U(1)` | r07.1, r07.2; `short/p3_frames` Prop. 3.2 | duality rotation as a phase of the RS vector (arXiv:1211.2655) | known; the two-orbit phrasing is a restatement |
| Null cone as image of spinors, `±ψ`, equivariance | r06.4; Prop. 2.6 | Cartan / Penrose spinor map; RS vector in `SL(2,C)` form, null field ⇔ nilpotent (arXiv:1811.09684) | known |
| Triple lemma: centred and null ⇔ `z = c(1, ω, ω²)` | r06.2; Lemma 2.5 | no source found; two-line algebra | elementary; centring is not Lorentz-invariant (referee, minor 1) |
| `J_B z = i z̄` as `σ_x` on `F = [E | B]`; ports `E ± B` | v4.9.0-r04.1; Prop. 3.4, 3.5 | "parallel–antiparallel" basis of the `(E, H)` two-level space: Golat, Vernon, Rodríguez-Fortuño, arXiv:2405.15718 | known in substance |
| State disk: `ρ = G/tr G`, `|b| ≤ 1`, duality rotates by `2α`, `T` and `J_B` reflect | r04.2; Prop. 3.6 | "energy symmetry sphere" of arXiv:2405.15718: Stokes-type parameters `W₀..W₃` on the `(E, H)` space, duality rotates about `W₃`, time reversal mirrors | the disk is the `W₃ = 0` slice for real instantaneous fields |
| Boosts leave `s` fixed and change `u` | r04.2(c); Prop. 3.6 | arXiv:2405.15718: boosts change `W₀`, `W₃` and leave `W₁`, `W₂` unchanged | known |
| Compensator image is not null; no non-null state reaches the null sector by Lorentz or duality maps | k220, Gesamtbild note of 6 Nov | follows from the orbit classification | consequence, not a result |

**Limits of the check.** Searches: alphaXiv and web, 15 Nov 2026. Read in part only: arXiv:2405.15718 (introduction, the
Bloch-sphere section, the paragraph on Lorentz boosts; not the supplement). arXiv:1211.2655, 1211.1218, 1811.09684, 1604.01876
were judged from abstracts and search excerpts; their full texts were not read. A statement marked "known" therefore means "a
source covering it was found", not "the exact formulation was located on a page". Before any submission each row needs a page
reference.

**One open item of the Companion is answered by the literature.** v4.9.0-r04 leaves open whether a third axis (`σ_y`) turns the
disk into a sphere. For time-harmonic fields with complex phasors it does: the third axis is the helicity `W₃` of
arXiv:2405.15718. The Companion uses this axis since v4.10.0-r16.2; round v4.10.0-r19.3 (PR #144) records the reference.

## 2. Relation to the existing short paper

`../short/` (16 pp.) already contains this material: `p2_kernel.tex` (norm, Lorentz action, orbits, triple lemma, null cone) and
`p3_frames.tex` (sectors, duality angle, compensator, doublet, state disk, compatible operators). A kernel note would be those
two sections taken out, without the `C⊗H⊗O` generation, the readout hypothesis and the numerical section. It must not be
submitted in parallel with a version of the short paper that still contains them.

## 3. What a note could honestly offer

- A compact dictionary between the biquaternion form and the Riemann–Silberstein form, with all proofs in one place.
- The real-field doublet picture as the instantaneous counterpart of the symmetry sphere, stated as such.
- A machine-checked core: `formal/QSFormal/Doublet.lean`, `StateDisk.lean`, `Boost.lean`, `Frames.lean` (Lean 4 with Mathlib).
- A plain statement of what does not follow (Section 6 of the outline).

It cannot offer new mathematics. Suitable venues are pedagogical or expository (the referee report names Eur. J. Phys.; Am. J.
Phys. and Adv. Appl. Clifford Algebras are of the same kind), or Zenodo only.

## 4. Outline (8–10 pp.)

| # | Section | Content | Source | Lean | pp. |
|---|---|---|---|---|---|
| 1 | Introduction | aim: a dictionary, not a new result; prior work named up front; one paragraph on the programme with the Companion DOI | new | – | 1 |
| 2 | Kernel and norm | `q = it + z·e`; `N = det` under `C⊗H ≅ M₂(C)`; the Hermitian form has signature (1,6) and no boosts | `short/p2` §2.1 | no | 1 |
| 3 | Lorentz action and orbits | `SL(2,C) → SO(3,C)`; `z = E + iB` as the (1,0) representation; orbit classification; frame with `E ∥ B` | `short/p2` §2.2 | `Boost.lean` (invariance of `s` only) | 1.5 |
| 4 | Null cone and spinors | spinor map, `±ψ`, conic; triple lemma as a remark, with the caveat on centring | `short/p2` §2.3 | no | 1 |
| 5 | Duality | duality angle; two non-trivial orbits; the sign of real `s` needs a duality frame | `short/p3` §3.1 | no | 1 |
| 6 | Doublet and state disk | `F = [E | B]`, `O(2)` on the right; `J_B = σ_x`, `T = σ_z`; Gram matrix; `|b| ≤ 1`; relation to the symmetry sphere | `short/p3` §3.2–3.3 | `Doublet`, `StateDisk`, `Frames` | 2 |
| 7 | What does not follow | ports sit at `b = (0, ±1)`, transversal to the `s`-axis; `Cf` is in general not a Maxwell solution; nothing tachyonic appears; `t` plays no role | referee M1, M2; k220 | – | 0.5 |
| 8 | Formalization and data | modules, build, disclosure of language-model use | `short/appendix_method` | – | 0.5 |
| | References | | | | 1 |

**Per-section work before writing.**
- Sections 2–5 have no Lean coverage. Either formalize them or say so.
- Section 3: v4.8.0-r06.3 and r07.2 rest on "checked constructively / numerically"; the note needs the proofs written out (the
  ones in `short/p2`, `short/p3` are complete but brief) or a citation.
- Section 6: `StateDisk.lean` does not formalize `|b| = 1/cosh 2η_f` or part (c) on boosts; `Boost.lean` covers the invariance
  of `s` and the parallel frame. Check `bloch_boost` and `visibility` against Prop. 3.6 before citing them.
- Vocabulary: "positive / negative / null" sectors as in the revised short paper; "compensator" once, with the neutral
  description "projector onto the `σ_x`-even part".
- Drop: `short/p3` §3.4 (compatible operators; referee M3), the Hopf-cascade subsection, the parameter `t` beyond one sentence.

## 5. Open decisions for the author

1. Write the note at all, or leave the material where it is (Sections 2–3 of the short paper, plus the Companion)?
2. If written: expository journal or Zenodo only?
3. Which paper goes first. The Koide-overlap material needs the same check before it is chosen: the referee report already
   points to Foot (hep-ph/9402242) and Brannen for the circulant form, and the reading `K = 2/3 ⇔ ρ² = 1/2` has to be compared
   with Foot's geometric statement before it is called new. Done on 15 Nov: see `../koide-note/novelty_check.md` (the central
   reading is in Brannen, arXiv:1006.3114).

No open problem and no guard is affected by this file.
