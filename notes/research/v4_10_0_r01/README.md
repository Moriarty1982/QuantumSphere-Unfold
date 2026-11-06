# Layer v4.10.0-r01: the full Einstein equation of W1 and the sign of the gravitational action

First layer after the v4.10.0 release (Version DOI 10.5281/zenodo.23991357).

| Record | Content |
|---|---|
| r01.1 | **H90 confirmed (not blind):** Einstein–Cartan equations of W1 fully non-linear, at generic points of three random curved backgrounds (jets to third order, three Weyl fields, Maxwell field). (a) Cartan equation solved by ω = ω̃ + K, K_cab = −(σ_g/4)κ ε_cabd j^d. (b) Vierbein variation = multiple of G̃ + σ_g κ T^eff, T^eff = T^Bel − g L_W + T^Maxwell − g λ j·j, λ = −σ_g·3κ/16; symmetric. (c) ∇̃^μ T^eff_μν = 0 on the field equations (4·10⁻¹⁵); negative controls 0.1–1. (d) **W1 as written (+R/2κ, signature +−−−) gives G̃ = −κT: gravity repels**; weak-field check in Wolfram (G_00 = 2∇²Φ). |
| r01.2 | **Author decision (6 Nov 2026):** W1 corrected to S_grav = −(1/2κ)∫e R. Then G̃ = κT^eff, L_4f = +(3/16)κ j·j, T^(4f) = −(3κ/16) j² g. |
| r01.3 | **Corrections (signs only, moduli and forms stay):** r81.1(b)/r86.2 torsion term +(3/16)κ j·j; r86.3 homogeneous state ρ = p = −(3κ/16) n² < 0; r86.4 withdrawn in its sign part; r82.4 pairing channel repulsive, Planck-scale ν^c condensate and seesaw estimate fall. Not affected: H69–H86 otherwise (review in `llm/Durchsicht_Vorzeichen_kappa_r81_r86.md`). |

Folders: `rounds/v4100_r01_round.tex`; script `llm/k205_w1_einstein_nichtlinear.py` (Python, output `llm/k205_out.json`), Wolfram `llm/k205b_schwachfeld.wl`, review `llm/Durchsicht_Vorzeichen_kappa_r81_r86.md`; H90 in `../predictions/`; W1 notes and the decision in `../v4_10_0_w1/`.
W1 still produces no vacuum term. OP5 is not closed, and the guards are unchanged.
