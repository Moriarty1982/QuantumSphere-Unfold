# Layers v4.9.0-r56 to r58 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r48_r55/`](../v4_10_0_r48_r55/README.md). The layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version `4.10.0-draft`.
- Guard and residual vectors unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
- r56 to r58 record the tests H40 to H43 (H42 is a pending prediction, see `../predictions/`), whose notes (`llm/Vorab_Notiz_H40_…`, `llm/Vorab_Notiz_H41_…`) were committed before the computation (local
  commits `fdb27ae`, `74bd018`, `59d8d04`, reachable from `main`).

| Layer | Test | Result |
|---|---|---|
| r56 | H40: calibrating the readout layer (author's idea: tune the readout layer to reproduce data, then learn from its settings) | form S with a Brannen coupling and one ε per sector, 16 settings for 17 quantities; settings recorded (ε_u ≈ 1.36–1.63, ε_d ≈ 1.42–1.47, ε_e ≈ 0.44–0.82, ε_ν ≈ 0.27–0.55); 14 candidate values from the corpus hit the ranges 76 times against 65.3 for random values, p = 0.019 above the threshold 0.01: no structure beyond chance; \|b\|/\|a\| ≈ 1 for the quarks follows from the hierarchy. The path needs fewer settings or sharper data |
| r57 | H41: trimaximal mixing (r55) with the mask as a correction | charged leptons corrected in form S, Majorana neutrinos ℤ2-invariant with one angle and form K; with ε_ν = 0 (776 cases) or a common ε (3 808 cases) θ12 reaches the JUNO 2σ range while θ13, θ23 stay in NuFIT 3σ: the TM2 tension with JUNO is resolvable. θ23 is not fixed (sin²θ23 0.31–0.54); a bound sin²θ23 ≲ 0.54 was noticed afterwards |
| r58 | H43: the CP phase of the corrected trimaximal reading | not fixed: \|sin δ\| 0.17–1, cos δ −0.98 to 0.99 over all fitting cases; no prediction registered |

| Path | Content |
|---|---|
| `rounds/v490_r56_round.tex` … `v490_r58_round.tex` | the layers as append-only blocks |
| `llm/Vorab_Notiz_H40_Kalibrierung_Ausleseschicht.md`, `llm/Ergebnis_H40_Kalibrierung_Ausleseschicht.md` | note and result (German) |
| `llm/k96_test_h40.py` … `llm/k98_test_h43.py`, `*_out.txt` | scripts and outputs; notes and results of H41, H43 in `llm/` |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r58, SHA256 prefix `df5f465ebda93f07`. Block SHA256 prefix: r58 `1cd0b790`, r57 `704edc5b`, r56 `6b47a6d1`.
Local build of the monolith (three pdfLaTeX passes): 1248 → 1254 pages, 0 undefined references or citations, 0 duplicate labels, no rerun warning, overfull boxes
unchanged (45). Guard linter over the new layer: 0 hits.
Build of the candidate with `.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live: 1275 → 1281 pages, 3930 → 3947 labels, same hard values.
