# Layer v4.9.0-r56 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r48_r55/`](../v4_10_0_r48_r55/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release.

- Public baseline: v4.9.0, Version DOI `10.5281/zenodo.23534954`, Concept DOI `10.5281/zenodo.19210728`; working version `4.10.0-draft`.
- Guard and residual vectors unchanged: `R_glob = (0,1,1,1,1)`, `Gamma_guard = (1,1,1,1,1)`, `beta_4 = 1/256` unspent.
- r56 records the test H40, whose note (`llm/Vorab_Notiz_H40_Kalibrierung_Ausleseschicht.md`) was committed before the computation (local commit `fdb27ae`,
  reachable from this branch).

| Layer | Test | Result |
|---|---|---|
| r56 | H40: calibrating the readout layer (author's idea: tune the readout layer to reproduce data, then learn from its settings) | form S with a Brannen coupling and one ε per sector, 16 settings for 17 quantities; settings recorded (ε_u ≈ 1.36–1.63, ε_d ≈ 1.42–1.47, ε_e ≈ 0.44–0.82, ε_ν ≈ 0.27–0.55); 14 candidate values from the corpus hit the ranges 76 times against 65.3 for random values, p = 0.019 above the threshold 0.01: no structure beyond chance; \|b\|/\|a\| ≈ 1 for the quarks follows from the hierarchy. The path needs fewer settings or sharper data |

| Path | Content |
|---|---|
| `rounds/v490_r56_round.tex` | the layer as an append-only block |
| `llm/Vorab_Notiz_H40_Kalibrierung_Ausleseschicht.md`, `llm/Ergebnis_H40_Kalibrierung_Ausleseschicht.md` | note and result (German) |
| `llm/k96_test_h40.py`, `llm/k96_out.txt` | script and output |

Source of the carried block: `Quantum_Sphaera_Companion_v4_8_0_source.tex` after layer v4.9.0-r56, SHA256 prefix `35586eac2dc7edc2`. Block SHA256 prefix: r56 `6b47a6d1`.
Local build of the monolith (three pdfLaTeX passes): 1248 → 1250 pages, 0 undefined references or citations, 0 duplicate labels, no rerun warning, overfull boxes
unchanged (45). Guard linter over the new layer: 0 hits.
Build of the candidate with `.github/scripts/qsc_latex_build.py --source-dir sources/research` under TeX Live: 1275 → 1277 pages, 3930 → 3936 labels, same hard values.
