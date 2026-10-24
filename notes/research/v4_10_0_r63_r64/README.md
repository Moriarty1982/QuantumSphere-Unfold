# Layers v4.9.0-r63 and r64 on the 4.10 base (source-only)

Continuation of [`../v4_10_0_r61/`](../v4_10_0_r61/README.md). Both layers are appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.

| Layer | Content | Result |
|---|---|---|
| r63 | the frame offset as the ratio of two horizon countings (pre-registered check H47, note commit `df0c788`); uncertainty saturation; tachyon floor | Spin ½ only (ABCK) vs all spins: weight 2 (Domagała–Lewandowski, Meissner) gives β = 0.549406, inside the lepton window [0.545, 0.570]; weight 2j+1 (Ghosh–Mitra) gives 0.604468, outside (not blind). Exactly the states m = ±j saturate the Robertson bound, so weight 2 counts only minimal-uncertainty states; at j = ½, ΔJx = ½. A tachyon's energy falls to 0 as v → ∞; the floor seen from a frame with velocity u moves at −1/u with negative energy. Only the floor of the mirror frame −η reproduces γ_L = cosh 2η; the tachyon of Convention F is that floor. Lean: `formal/QSFormal/Zaehlung.lean` |
| r64 | frame audit of the gravity statements under the counting reading | thm:k-values (k(γ_BI) = 0) contradicts thm:frame-offset. Under the counting reading the frame difference sits in γ, not in ħ or G; the photon-frame Planck length, the γ_L⁵ vacuum ratio and Hawking item (i) are not supported by it. thm:hawking-triolic reads the tachyon counting as the photon value. Gravity itself is frame-independent in this reading |

| Path | Content |
|---|---|
| `rounds/v490_r63_round.tex`, `rounds/v490_r64_round.tex` | the layers |
| `llm/Vorab_Notiz_H47_Zaehlregel_beta_sym.md` | pre-registration (German) |
| `llm/Ergebnis_H47_Zaehlregel_beta_sym.md`, `llm/k102_zaehlregeln.py`, `llm/k102_out.txt` | H47 |
| `llm/k103_robertson_tachyon.py`, `llm/k103_out.txt` | uncertainty saturation (j ≤ 6, exact), tachyon floor |
| `llm/Pruefung_Gravitation_Frames.md` | the audit (German) |

Source after layer v4.9.0-r64: SHA256 prefix `86bb4b2ee3d4fd1c`. Local build of the monolith: 1261 → 1266 pages, hard values 0, overfull unchanged (45);
guard linter 0 hits. Candidate build with `.github/scripts/qsc_latex_build.py --source-dir sources/research`: 1289 → 1294 pages, 3967 → 3977 labels, same hard values.
Lean workflow green on the module.
