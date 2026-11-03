# Layer v4.9.0-r73 on the 4.10 base (source-only): four hidden sixth-order conditions of the gauged OP5 comparison system

Continuation of [`../v4_10_0_r72/`](../v4_10_0_r72/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.
Everything concerns the fixed OP5 comparison model (`analysis/op5-field-slices/state-sufficiency-2026-10-30`).

| Item | Content |
|---|---|
| r73.1 | **H55 confirmed** (pre-registered, local commit `04a3950`). At a second 4-jet (50 % away, seed 55) again P₅₆ = 852 with equations through degree 6 and 848 with degree 7; gaps ≥ 4e4, error bounds 710 and 1390 times below the deciding values. The reduced matrix depends only on the 2-jet and is shared by both points; new is the rank of the full system |
| r73.2 | **The four conditions determined** (exploration). Linear forms on K₇ (852) vanishing on K₈ (848). (a) genuine sixth-order equations, rank 4 on g'_6: the complete symbol at order 6 has dimension 477; (b) they act only on light-like plane waves (seven polarizations per null direction), vanish off the cone; (c) rank 1 on the polarizations of each null direction; (d) direction quadratic in ξ, spanned with q by the four quadrics of the planes Π₀, Π₁. Reading: on the cone σ_k = d_k(ξ)·s(ξ,u), the curvature of the four r71 relations q·d_k·Ω |
| r73.3 | **H56 and H57 invalid** (pre-registered, local commits `4ed4c3e`, `11a64a4`; H57 not blind). Extended symbol: dim g''_6 = 477, dim g''_7 = 594, not involutive at 6 (clean). From p = 8 the ranks have gaps of only 8e2–1e3; one singular value (5.6e-9) decides 723 vs 724 and involution at 8 vs 7. Cause: θ from the older germ (1e-7) mixed with conditions from the repaired germ |

Consequence: the gauged system is not formally integrable at order 6; the four extra conditions are determined and
understood. Whether the extended symbol is involutive at 7 or 8 needs consistent high-precision data at the repaired germ.
OP5 is not closed.

| Path | Content |
|---|---|
| `rounds/v490_r73_round.tex` | the layer |
| `llm/k143_h55.py`, `llm/k143_log_H55.txt`, `llm/Ergebnis_H55_*.md` | H55 |
| `llm/k144_vier_bedingungen.py`, `llm/k145_charakteristik.py`, `llm/k144_bedingungen_p1.npy`, `llm/Erkundung_vier_Bedingungen_6Jets.md` | the determination (r73.2); the `.npy` holds the four linear forms on (c₅, c₆) in balanced coordinates |
| `llm/k146_cartan_erweitert.py`, `llm/k146_log.txt`, `llm/Ergebnis_H56_*.md` | H56 |
| `llm/k147_cartan_projiziert.py`, `llm/k147_log.txt`, `llm/Ergebnis_H57_*.md` | H57 |
| `../predictions/Vorab_Notiz_H55_*.md` … `Vorab_Notiz_H57_*.md` | the pre-registrations |

Scripts need the r72 tools (`../v4_10_0_r72/llm/`, e.g. `k138_tps_d.py`, `k140_fortsetzung_exakt.py`, `k136_eichdaten.npy`) in the same folder and take the path of `analysis/op5-field-slices/state-sufficiency-2026-10-30` as first argument. Notes are in German.
