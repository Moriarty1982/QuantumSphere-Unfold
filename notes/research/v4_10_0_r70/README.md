# Layer v4.9.0-r70 on the 4.10 base (source-only): the 4.10 consolidation in the monolith, a correction to r69, H48 and Λ over sector crossings

Continuation of [`../v4_10_0_r69/`](../v4_10_0_r69/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.

| Item | Content |
|---|---|
| r70.1 | On 29–30 October the second language model changed the research candidate directly (`f98b29b`..`cf48496`, see [`../v4_10_0_consolidation/`](../v4_10_0_consolidation/README.md)): the three main-body errors of r69.3 are corrected or annotated, further status notes (shared-time entanglement, prediction register, Theta-sum dependency), the wrong group label on the Hopf fibre S⁷ removed, new section `sec:v410-state-mediator` and `subsec:op5-multimode-slices` with a figure. The layer records these changes and carries them into the local monolith |
| r70.2 | Correction: the finite part in r69.3(a) is 1.686953464, not 1.689 (the quadrature in `k106` lost accuracy near τ = 0) |
| r70.3 | H48, pre-registered (`../predictions/Vorab_Notiz_H48_Einfrieren_beta.md`, commit `0ff3ab2`): β_sym as the frozen length of the M/T state. **Refuted**: the frozen value depends on expansion rate and density; the Einstein–Cartan contact term has no effect (the state lies on the R/T axis in the dense phase). Files: [`../v4_10_0_h48/`](../v4_10_0_h48/) |
| r70.4 | Exploration, not a test: Λ as a mixture over sector crossings; 26 readings, one hit at chance level; identity β² = λ₋/λ₊ for the eigenvalues of the M/T state |

| Path | Content |
|---|---|
| `rounds/v490_r70_round.tex` | the layer |
| `llm/revision_spec_v410_konsolidierung.py` | the eight main-body patches of the consolidation, reproduces the GitHub fragments exactly; applied to the local monolith with `llm/apply_patches.py` |
| `llm/einbau_v410_abschnitte_lokal.py` | local insertion of the two new sections before the archive appendix (monolith only) |
| `llm/k108_kreuzungen.py`, `llm/k108_out.*`, `llm/Erkundung_Lambda_Kreuzungen.md` | the crossing exploration (German note) |

Local monolith: 1277 → 1287 pages, 3884 → 3897 labels, SHA256 prefix `8d49a38e38b83715`, hard values 0, overfull 45, guard linter 0 new hits. The figure
`figures/op5-slices-9x9.pdf` is the first external graphic of the monolith. Local backup tag `vor-konsolidierung-v410-r70`.
Candidate build with `.github/scripts/qsc_latex_build.py --source-dir sources/research` (TeX Live 2022): 1312 → 1315 pages, 4013 → 4018 labels,
undefined references 0, duplicate labels 0, rerun 0, overfull 45 (unchanged). Local history up to `5c1eba7` joined by an ours-merge.
