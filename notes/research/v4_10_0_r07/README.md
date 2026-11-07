# Layer v4.10.0-r07: the relative-entropy chain in the tachyon frame, and a correction to r06.5

Author question: can the companion map the derivation of Dorau–Much (layer r06) onto its own frames? A test was planned; the search of prior work showed the answer is fixed analytically, so this is an exploration and no hypothesis number is assigned.

| Record | Content |
|---|---|
| r07.1 | **Correction to r06.5:** z = E + iB is the field, z ↦ iz the electromagnetic duality rotation (E ↦ −B, B ↦ E), a map of field space. It commutes with every Lorentz transformation (v4.8.0-r20.1). The boost stays a boost; z ↦ iz is not the Wick rotation of thm:artqft. |
| r07.2 | **The chain in frame T (exploration, not blind):** for the free Maxwell field the Dorau–Much chain gives the same Einstein equation in frames M and T. Duality is a symmetry fixing the vacuum and commuting with the modular group; relative entropy is invariant; the energy–momentum tensor is Hermitian in z and duality invariant, while the bilinear invariant z·z (Lagrangian, E·B) changes sign. Gravity is frame blind for the Maxwell field (r64 reading becomes a statement). Not new physics. Numerical control k217. |
| r07.3 | **QAM bookkeeping:** `qam_dorau_much_companion.tex` passes `qam.sty`; the internal Einstein equation carries the same inputs as Dorau–Much (local flatness, area law). `qam_dorau_much_paper.tex` checks the paper itself (promotion, input as result, frame mixing under the companion's typing). |
| r07.4 | **Why frame independence is reached and the prefactor is not:** the frame map is a symmetry and yields equalities, not values. Both horizon countings are calibrated to the area law, γ* = Nκ for S = A/(Nℓ_P²); the normalization N cancels in γ_L = κ_DL/M/κ_ABCK = 1.8647, in β_sym and in Ω_M = β². The prefactor cannot be derived from these inputs; one absolute value of γ from the structure would be needed. The 1/4 of the Hopf point (r17) is not proposed as an identification. |

Files: `rounds/v4100_r07_round.tex`; exploration note `Erkundung_Gravitation_Tachyonframe_Dualitaet.md` (German); `llm/k217_dualitaet_gravitation.py` with output; QAM files in `llm/`. The r06 exploration note carries a correction supplement.
The guards are unchanged.
