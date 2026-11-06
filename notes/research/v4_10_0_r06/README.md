# Layer v4.10.0-r06: semiclassical Einstein equations from relative entropy (Dorau–Much) and the readouts of the companion

Literature: P. Dorau, A. Much (Leipzig), *From Quantum Relative Entropy to the Semiclassical Einstein Equations*, Phys. Rev. Lett. **136**, 091602 (2026), DOI [10.1103/lmq8-nsty](https://doi.org/10.1103/lmq8-nsty), [arXiv:2510.24491](https://arxiv.org/abs/2510.24491). Pointed out by the author. Exploration of the literature, no pre-registered test, no new prediction.

| Record | Content |
|---|---|
| r06.1 | **The result (literature):** at a local Rindler horizon the Araki relative entropy between the vacuum and a coherent excitation of a scalar field equals the energy flux across the horizon (modular group = boost, Bisognano–Wichmann; KMS at 2π/κ). With the *assumed* area law S_rel = δA/4 and Raychaudhuri this gives G_ab + Λ g_ab = 8π⟨T_ab⟩, Λ an arbitrary integration constant. The vacuum is the reference state, not a source of energy. |
| r06.2 | **Entropy factor = gravitational coupling (analytic, not blind):** a counting S = c·A/4 gives G_eff = G/c. The two countings of the companion differ by γ_L = 1.8647 at equal γ (v4.8.0-r03 F11a), so frames counting with one γ would see different G. One measured G requires each frame to use the γ at which its counting reproduces S_BH; the frame difference sits in γ (r64). |
| r06.3 | **Λ as integration constant:** same situation as v4.10.0-r03/r05 (Λ free, Λ a readout). Supports the classification, not a success of the companion; H96 neither supported nor contradicted. |
| r06.4 | **Sign from positivity (afterwards):** S_rel ≥ 0 gives attractive gravity, coinciding with the correction of W1 in v4.10.0-r01. Not a derivation of W1 (scalar vs. spinors with torsion). |
| r06.5 | **Frames (open):** under z ↦ iz the boost becomes a rotation; the KMS period 2π is the Euclidean full angle (Wick rotation, thm:artqft). Open: is z ↦ iz that Wick rotation, and is the tachyon image of the boost the modular group of some state? |

Files: `rounds/v4100_r06_round.tex`; exploration note `Erkundung_Dorau_Much_relative_Entropie.md` (German, with a supplement of 7 November correcting the first reading of r06.5).
The guards are unchanged.
