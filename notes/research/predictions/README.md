# Pending predictions (pre-registered)

Each note was committed locally before any comparison with data published after its date; the local commits are reachable from `main` through ours merges.

| Note | Prediction | Test data | Status |
|---|---|---|---|
| `Vorab_Notiz_H42_Grenze_theta23.md` (local commit `1c7f3e1`, 2026-10-24) | sin²θ23 ≤ 0.54 (normal ordering), from the trimaximal reading of r55 with the mask correction of r57 | first global fit or DUNE/Hyper-K result published after 2026-10-24 (2σ interval): refuted if entirely above 0.54, confirmed if entirely below, otherwise open | pending |
| `Vorab_Notiz_H46_theta23_bei_eps_eta.md` (local commit `dec51e7`, 2026-10-24) | sin²θ23 ∈ [0.49, 0.50] (normal ordering), from the trimaximal reading with the mask correction and ε = artanh β_sym (layer r60); sharper than H42, which stands independently | as H42: refuted if the 2σ interval misses [0.49, 0.50]; confirmed if the 1σ interval touches it and the 2σ interval is narrower than 0.06; otherwise open | pending |

The bound of H42 was noticed after the evaluation of r57; the reading ε = η of H46 was not chosen blind (the hit windows of r59 were known), but the value of θ23 was not known before and counts as a prediction only from the date of its note. H15 (m_W = 80.3615 ± 0.0018 GeV) is recorded in layer v4.9.0-r07.

Resolved pre-registered tests whose notes also lie in this folder: H48 (layer v4.9.0-r70, refuted), H49 and H50 (layer v4.9.0-r71, both refuted; local commits `e2d3394` and `ea36f39`, results in [`../v4_10_0_r71/`](../v4_10_0_r71/README.md)).

Layer v4.9.0-r77 (4 Nov 2026) resolves H59 (confirmed), H60 (confirmed), H61, H62 and H63 (refuted) and H64 (confirmed, run 2 not blind). The pre-registration and result notes lie in this folder (`Vorab_Notiz_H59…H64`, `Ergebnis_H59…H64`); scripts are in [`../v4_10_0_r77/`](../v4_10_0_r77/README.md).

Layer v4.9.0-r78 (4 Nov 2026) resolves H65 (invalid by criterion; part (b), the gauge stabilizer so(1,2), as predicted) and H66 (confirmed, not blind). Scripts are in [`../v4_10_0_r78/`](../v4_10_0_r78/README.md).

H67 (4 Nov 2026, confirmed): the four hidden conditions and their support on the cone are independent of the gauge (K₂, K₀, K₃, Q₃ and the Lorentz scalar Ψ̄Ψ all give F₆ = 477 and 6 polarizations). Scripts and logs are in `../v4_10_0_r79/llm/`.

Layer v4.9.0-r79 records H67.

Layer v4.9.0-r86 (5/6 Nov 2026) resolves H87 (a, c confirmed; b refuted as formulated), H88 (confirmed) and H89 (confirmed), all not blind and computed with Wolfram Language as a second, independent system. Code is in [`../v4_10_0_r86/`](../v4_10_0_r86/README.md).

H99 (13 Nov 2026, not blind; note `Vorab_Notiz_H99_Neutrino_Phase_Bogenrand.md`, commit `5b23c5a`, script `k221_test_h99.py`): with equal overlap (K = 2/3) in both colour-neutral sectors and the neutrino phase shifted by π/12 against the charged-lepton phase, the ratio Δm²₂₁/Δm²₃₁ is 0.030839. H99a (NuFIT 6.0): compatible, +1.31σ. H99b (NuFIT 6.1, primary table, IC24 with SK, NO: Δm²₂₁ = 7.537 +0.094/−0.10, Δm²₃₁ = 2.511 +0.021/−0.020): compatible, +1.80σ (decided 13 Nov 2026 afternoon; the earlier substitute calculations used secondary values and are superseded). After the evaluation: the IC23 column would give +2.03σ; against JUNO alone (7.50 ± 0.12) the implied Δm²₂₁ = 7.744·10⁻⁵ eV² lies +2.0σ high. The relation is known from the literature (Brannen) and is not derived. Exploration notes: `../op3_indefinite_form_2026_11_13.md`, `../op3_gram_eigen_readout_2026_11_13.md`.

H100 (13 Nov 2026, pending; note `Vorab_Notiz_H100_Neutrino_Verhaeltnis_naechster_Fit.md`, commit `9c77ddd`, script `k222_test_h100.py`): three fixed predictions for R = Δm²₂₁/Δm²₃₁ in the next NuFIT release (normal ordering, column with SK atmospheric data): A (H99, pole masses) 0.030839, B (one scale, coupling side at M_Z) 0.030087, C (Sumino-type family correction, c = 1, PMNS-averaged) 0.030375. Each is compatible if |z| ≤ 2; H100 is confirmed if A is refuted and B or C is compatible, refuted if both B and C are refuted. Blind against future data, not blind against NuFIT 6.1. Expires without a new NuFIT version by 31 Dec 2027.

H101 (13 Nov 2026, refuted; note `Vorab_Notiz_H101_Maske_hebt_Elektron.md`, commit `f470817`, script `k223_test_h101.py`, result `Ergebnis_H101_Maske_hebt_Elektron.md`): the lepton mask of r47 in form K (M = D C D) applied to the exact qubit octant cannot lift the electron, since a congruence keeps the rank (Sylvester). After the evaluation: the linear r47 form lifts it, giving m_μ/m_τ +0.35 % but K off by 3·10⁻⁴, about 60 times the pole uncertainty.

H102 (13 Nov 2026, pending; note `Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`, commit `ee0a103`, script `k224_test_h102.py`): the charged-lepton flux Φ_e = 3θ_e = π/4 − γ_M/2 with γ_M = 0.237533 from the matter-frame counting rule, together with m_e/m_μ, gives m_τ = 1777.134 MeV (exact Koide: 1776.969 MeV). Data: the first PDG edition after 13 Nov 2026; confirmed if |z| ≤ 2. Found a posteriori (scan of 154 trials, one hit); against PDG 2024 already +2.3σ. Expires end of 2028.
