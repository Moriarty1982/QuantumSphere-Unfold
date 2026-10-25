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

## Layer v4.9.0-r65: status notes (rule C)

On 2026-10-25 the author decided to add the status notes named by r64. The main-body text stays; three `\qsstatus` notes are added or extended by
`llm/revision_spec_v490_r64.py` (applied with `llm/apply_patches.py`, locally to the monolith and here to `sources/research/parts/v470/10_sphaera_and_physics.tex`):

| Place | Note |
|---|---|
| thm:k-values | existing note extended: k(γ_BI) = 0 contradicts thm:frame-offset; k(ħ), k(G) need a source other than γ_L |
| thm:planck-photon | existing note extended: γ_L^{−3/2} not supported by the counting reading |
| thm:hawking-triolic | new note: the tachyon counting is assigned to the escaping photon (T read as R) |

The layer `rounds/v490_r65_round.tex` is appended to `v490-post-release-layers.tex`; guard vectors unchanged.
Local monolith: 1266 → 1267 pages, SHA256 prefix `0e6d2568c89c8807`, hard values 0, overfull 45, guard linter 0 hits.
Candidate build: 1294 → 1295 pages, 3977 → 3981 labels, same hard values.

## Layer v4.9.0-r66: correction to r64 and the local frame factor

r64.1(a) (k(γ_BI) = 0 in thm:k-values against thm:frame-offset) is **not new**: it is item 1 of the two contradictions of v4.9.0-r09, which resolved them by
reading thm:frame-offset as a statement about the structural factor γ_L alone. r64 did not cite this. The r65 note on thm:k-values is extended with the
reference by `llm/revision_spec_v490_r66.py`. r64.1(b)–(h) are unaffected. Under the counting reading the structural factor is a fixed number, and the two
counting rules are discrete, so the reading gives no mechanism for a continuously drifting local factor (the drift readings of r08/r09 are excluded by atomic
clocks anyway). The corollary "α-drift as a frame effect" is a candidate for a status note.
Local monolith: 1267 → 1269 pages, SHA256 prefix `8efc9603eafe0404`, hard values 0, overfull 45, guard linter 0 hits.
Candidate build: 1295 → 1298 pages, 3981 → 3986 labels, same hard values.

## Layer v4.9.0-r67: Einstein's "greatest blunder" under the counting reading

At the author's request, rem:einstein-blunder was read again together with thm:dark-energy and rem:omega-bsym. Findings: thm:dark-energy puts β² on
matter (Ω_M = β²), while the field equation G + β² g = 8πG T of rem:omega-bsym and Λ_obs = β² of rem:einstein-blunder put the same β² on Λ, i.e. they give Λ
the matter share (separate from the dimensional problem of r03 F3/F4). In counting form Ω_M = (γ_M − γ_T)/(γ_M + γ_T) = 0.301847 and
Ω_Λ = 2γ_T/(γ_M + γ_T) = 0.698153. With β fixed, the identification holds at one epoch only. After the fact: +0.5σ against DESI DR2 BAO alone, −1.8σ against
Planck 2018. Reading (not adopted): Λ itself is frame-independent like G; only the share Ω_Λ could be explained, as the floor share of a horizon counting.
Candidates for status notes: rem:einstein-blunder and the field equation in rem:omega-bsym. Layer: `rounds/v490_r67_round.tex`.
Local monolith: 1269 → 1271 pages, SHA256 prefix `dd57342cbfa5c861`, hard values 0, overfull 45, guard linter 0 hits.
Candidate build: 1298 → 1300 pages, 3986 → 3991 labels, same hard values.
