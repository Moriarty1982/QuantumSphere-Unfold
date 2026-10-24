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

## Layer v4.9.0-r62: status notes (rule C)

On 2026-10-24 the author decided to add the status notes named by r61. The main-body text stays; four `\qsstatus` notes are added by
`llm/revision_spec_v490_r61.py` (applied with `llm/apply_patches.py`, locally to the monolith and here to `sources/research/parts/v470/10_sphaera_and_physics.tex`,
`18_op1_op2_mathematics.tex`, `19_local_op_entry.tex`):

| Place | Note |
|---|---|
| thm:bsym-hopf | reads a pure R-frame state as the matter offset |
| rem:bsym-hopf-gap | OP1 open, target the matter value; window from lepton mixing (not blind) |
| thm:tribonacci | existing note extended: not a frame-consistent fixed point |
| rem:op1-tribonacci | claimed resolution withdrawn; OP4 ill-posed as stated |

The layer `rounds/v490_r62_round.tex` is appended to `v490-post-release-layers.tex`; guard vectors unchanged.
Local monolith: 1260 → 1261 pages, SHA256 prefix `cd1995203a3ee22e`, hard values 0, overfull 45, guard linter 0 hits.
Candidate build: 1287 → 1289 pages, 3963 → 3967 labels, same hard values.
