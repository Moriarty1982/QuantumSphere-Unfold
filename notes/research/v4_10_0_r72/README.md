# Layer v4.9.0-r72 on the 4.10 base (source-only): the ϑ gauge of the OP5 comparison symbol, a Cartan test, and four hidden conditions

Continuation of [`../v4_10_0_r71/`](../v4_10_0_r71/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.
Everything concerns the fixed OP5 comparison model (`analysis/op5-field-slices/state-sufficiency-2026-10-30`).

| Item | Content |
|---|---|
| r72.1 | **ϑ gauge.** v = ∂_ϑΨ is a common kernel vector of all four J blocks (5.5e-15 vs 0.13); θ annihilates it (1.6e-14). Algebraic gauge Ψ†K₂Ψ = S(x), \|ds·v\|/\|ds\| = 0.45. At symbol level every transversal algebraic gauge gives g'_p = g_p − C(p+3,3) = 117, 188, 273, 371, 481, 606, 745 (p = 2…8) |
| r72.2 | **H51 confirmed** (pre-registered, local commit `10693a0`). Cartan test in three random frames, gaps ≥ 1e7: not involutive at p = 4, 5 (sums 372, 483 vs 371, 481), involutive at p = 6, 7 (606 = 606, 745 = 745). dim g'^{(k)}_6 = 481, 111, 14, 0: no free function of four variables left, formally 14 functions of three variables |
| r72.3 | **H52 invalid** (local commit `03527c6`). Large-system ranks without clean gap. Clean finding: the stored degree-5 coefficients cannot be extended (residual 4.0e-3 = positive-control level); they violate the once prolonged Ω condition (counts 381 = 371 + 10, 501 = 481 + 20). Test-design error |
| r72.4 | **H53 invalid** (local commit `64fd43b`). Only the repaired 4-jet fixed, exact linearization via symmetric probes. Through degree-6 equations everything clean (P₅ = 371, P₅₆ − P₅ = 481, residual 4e-12). With degree-7 equations (9865 × 10200) P₅₆ drops from 852 to 848, while P₅₆₇ − P₅₆ = 606; one rank gap 4e3 |
| r72.5 | Exploration (not pre-registered): Spencer cohomology, gaps ≥ 4e6. H^{4,2} = 0, H^{5,2} = 4 both ungauged (check) and gauged. At most four hidden conditions on 6-jets, none on 5-jets; not caused by the ϑ freedom |
| r72.6 | **H54 invalid** (local commit `ec705ec`). Weyl bound with measured error norms (reduced matrix ≤ 7e-13 vs 1.0e-9; full F₈ ≈ 5e-9 vs 2.7e-6) gives P₅₆ ≤ 848, with r72.5 P₅₆ ≥ 848. The criterion's gap demand in deliberately perturbed variants was unattainable by construction (3e3, 7e3) |

Consequence: the gauged symbol is involutive from order 6. The gauged system is, by all evidence, not formally integrable at
order 6 (four hidden conditions on 6-jets), but this is not formally confirmed. Next: a second base point (H55), then the
explicit conditions and a new Cartan test. OP5 is not closed.

| Path | Content |
|---|---|
| `rounds/v490_r72_round.tex` | the layer |
| `llm/k136_eichung.py`, `llm/k136_eichdaten.npy` | the gauge (r72.1); stores v and the gauge covector |
| `llm/k137_cartan_test.py`, `llm/k137_log.txt`, `llm/Ergebnis_H51_*.md` | H51 |
| `llm/k138_tps_d.py` | truncated power series of any degree (generalizes `k135_tps.py`) |
| `llm/k139_fortsetzung.py`, `llm/k139_log_H52.txt`, `llm/Ergebnis_H52_*.md` | H52 |
| `llm/k140_fortsetzung_exakt.py`, `llm/k140_f8_schritte.py`, `llm/k140_log_H53.txt`, `llm/Ergebnis_H53_*.md` | H53 (exact linearization; large system in memory-saving steps) |
| `llm/k141_spencer_geeicht.py`, `llm/Erkundung_Spencer_geeichtes_Symbol.md` | r72.5 |
| `llm/k142_h54.py`, `llm/k142_log_H54.txt`, `llm/Ergebnis_H54_*.md` | H54 |
| `../predictions/Vorab_Notiz_H51_*.md` … `Vorab_Notiz_H54_*.md` | the pre-registrations |

All scripts take the path of `analysis/op5-field-slices/state-sufficiency-2026-10-30` as first argument and run from this folder. Notes are in German.
