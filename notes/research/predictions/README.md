# Pending predictions (pre-registered)

Each note was committed locally before any comparison with data published after its date; the local commits are reachable from `main` through ours merges.

| Note | Prediction | Test data | Status |
|---|---|---|---|
| `Vorab_Notiz_H42_Grenze_theta23.md` (local commit `1c7f3e1`, 2026-10-24) | sin²θ23 ≤ 0.54 (normal ordering), from the trimaximal reading of r55 with the mask correction of r57 | first global fit or DUNE/Hyper-K result published after 2026-10-24 (2σ interval): refuted if entirely above 0.54, confirmed if entirely below, otherwise open | pending |
| `Vorab_Notiz_H46_theta23_bei_eps_eta.md` (local commit `dec51e7`, 2026-10-24) | sin²θ23 ∈ [0.49, 0.50] (normal ordering), from the trimaximal reading with the mask correction and ε = artanh β_sym (layer r60); sharper than H42, which stands independently | as H42: refuted if the 2σ interval misses [0.49, 0.50]; confirmed if the 1σ interval touches it and the 2σ interval is narrower than 0.06; otherwise open | pending |

The bound of H42 was noticed after the evaluation of r57; the reading ε = η of H46 was not chosen blind (the hit windows of r59 were known), but the value of θ23 was not known before and counts as a prediction only from the date of its note. H15 (m_W = 80.3615 ± 0.0018 GeV) is recorded in layer v4.9.0-r07.
