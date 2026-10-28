# Layer v4.9.0-r69 on the 4.10 base (source-only): the OP5 research series of 25–27 October

Continuation of [`../v4_10_0_r63_r64/`](../v4_10_0_r63_r64/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.

Between 25 and 27 October the author worked on OP5 with another language model. The results went straight to `main` under
[`analysis/`](../../../analysis/) (commits `3fa5ba9`, `a97e32d`, `bb975d2`, `cf9e167`, `5913abb`, `337d9cb`; 173 files: 84 notes, 23 check scripts,
64 JSON/text outputs, one figure, one HTML visualization). At the author's request this layer integrates them. The notes stay where they are; the layer
names the note behind each item.

| Item | Content |
|---|---|
| Reproduction | All 23 check scripts rerun (Python 3.13, SymPy, NumPy); all pass; regenerated outputs differ only in the last floating-point digit |
| Recheck | Nine statements recomputed with new code, `llm/k106_nachrechnung_op5.py` → `llm/k106_out.txt`; all hold |
| r69.1 | A passive frame change only rescales a balance defect; three distinct neutral objects (midpoint of two scale frames, equal mixture ρ + σ_yρσ_y = I/2 with label P, flux-free observer of two null streams); β_sym² offered as relative separation tanh²(χ/2); no route selects the absolute vacuum term; no nontrivial doublet projector respects both involution and M/T exchange |
| r69.2 | Probe cone comes from the Clifford structure; two complex probes give rank four but different cones; E = ½Dj ⇒ T = ½Rj, torsion-free + Einstein vacuum ⇒ Λ_geom = 0 where j ≠ 0 (exclusion, not cancellation); Ward exclusion for an isotropic boost connection; two-point fits are not solutions |
| r69.3 | Errors in the main body, candidates for status notes: rem:regularization-B (series −1/τ + 1 − 11τ/24, counterterm −log(ε/μ), value 1.689 instead of 0.940); thm:dirac-probe and prop:three-compatible-readings rest on the archived thm:gue-selfdet; the corollary "Cosmological constant revisited" gives zero and γ_L⁵ for one quantity |

| Path | Content |
|---|---|
| `rounds/v490_r69_round.tex` | the layer |
| `llm/Integration_OP5_Serie.md` | integration protocol (German) |
| `llm/k106_nachrechnung_op5.py`, `llm/k106_out.txt` | recheck |

Local monolith: 1273 → 1277 pages, SHA256 prefix `598bec721a246fa0`, hard values 0, overfull 45, guard linter 0 hits.
Candidate build with `.github/scripts/qsc_latex_build.py --source-dir sources/research` (TeX Live 2022): 1302 → 1306 pages, 4000 → 4005 labels,
undefined references 0, duplicate labels 0, rerun 0, overfull 45 (unchanged). GitHub workflow "QSC LaTeX PDF Build" on the branch: green.
The series was also copied into the local repository under `analysis/` (local commit `6a2705e`).
