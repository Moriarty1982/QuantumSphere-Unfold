# Layer v4.9.0-r61 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r56_r60/`](../v4_10_0_r56_r60/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.

| Layer | Content | Result |
|---|---|---|
| r61 | frame audit of the open problems OP1–OP5 (author's suspicion: mixed frame configurations, as found earlier for the main statements) | OP1: the Tribonacci fixed point γ_L = 1/β (⇔ cosh 2η = e^η) equates a matter readout quantity with the tachyon offset, mixing frames and classes; the Hopf value reads a pure reference-frame state (populations 2/3, 1/3) as the mixed matter state (3/4, 1/4); only γ_BI/γ_string is frame-consistent. OP4 (closing the Hopf/Tribonacci gaps) is ill-posed as stated; OP2 (T4) carries the same class mixing; OP5 has a class mixing that does not explain its failure. Observation (not blind): under the reading r55–r60 the lepton data fix β_sym ∈ [0.545, 0.570]; the measured value lies inside, Hopf and Tribonacci outside |

| Path | Content |
|---|---|
| `rounds/v490_r61_round.tex` | the layer |
| `llm/Pruefung_OP_Frames.md` | the audit (German) |
| `llm/k101_fenster_eta.py`, `llm/k101_out.txt` | window of η from lepton mixing |

Source after layer v4.9.0-r61: SHA256 prefix `df0398d672ed5cd0`; block r61 `7fd9811b`. Local build of the monolith: 1258 → 1260 pages, hard values 0, overfull unchanged (45);
guard linter 0 hits.
Candidate build with `.github/scripts/qsc_latex_build.py --source-dir sources/research`: 1285 → 1287 pages, 3958 → 3963 labels, same hard values.
