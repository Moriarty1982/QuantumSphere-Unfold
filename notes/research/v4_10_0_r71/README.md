# Layer v4.9.0-r71 on the 4.10 base (source-only): structure of the OP5 comparison symbol, an exact polar gauge symmetry, H49 and H50

Continuation of [`../v4_10_0_r70/`](../v4_10_0_r70/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.
Everything concerns the fixed OP5 comparison model of the second language model (`analysis/op5-field-slices/state-sufficiency-2026-10-30`, last commit `cf48496`).

| Item | Content |
|---|---|
| r71.1 | Independent check of the 70-digit germ at (1, 3/5, 0, 0). Two own implementations: exact series along seven lines (F through order 4 ≤ 1.2e-60, g through order 5) and a Taylor evaluator of the full R = (F, G, dg) (all coefficients through degree 3 ≤ 2.4e-12, so G is checked too). Degree-4 symbol rank 528, left kernel 112, as recorded by the second model |
| r71.2 | The degree-5 Spencer count 1/0/−1 is resolved. −1 counts a direction that lies 98 % outside the kernel of the outgoing map (δ² = 0 violated). Exact rule dim H^{5,2} = dim g₇ − 722. A direct symbol construction gives dim g_p = 127, 208, 308, 427, 565, 726, 910, 1118, 1351 (p = 2…10), so dim H^{5,2} = 4 for the stored θ |
| r71.3 | Structure: a random θ gives quadratic growth, the stored θ cubic growth again from p = 7. θ lies exactly on a special locus and is blind to the free direction (θ·k ≈ 1e-15). The four degree-7 relations are q·d_k·Ω ∈ ⟨J⟩. q is the light cone of the reconstructed coframe (Minkowski to 8e-13). The d_k cut out two real skew 2-planes (signatures (0,2) and (1,1)), on which J loses one further rank |
| r71.4 | The free direction is δΨ = f·c^μD_μΨ with c = ρ∂_z − z∂_ρ (∝ ∂_ϑ). It is an **exact gauge symmetry** of the comparison model: the background is h(t, r) and A = M(t) dφ, and L_{fc}A = 0, L_{fc}h = 0 for every f |
| r71.5 | H49 (pre-registered, local commit `e2d3394`): an earlier hidden condition off the equator. **Refuted**; the second-jet compatibility defect is 1–3e-10 everywhere. Its premise was wrong (Cartesian coefficient instead of the Lie derivative) |
| r71.6 | H50 (pre-registered, local commit `ea36f39`): does Ω couple back to Ψ through ϑ? **Refuted** (first class through order 3). Ω changes by ≤ 1.5e-10 under all ϑ-shifts with f up to cubic, controls 0.04–0.11; Ω is gauge invariant |

Consequence: a gauge condition for ϑ is needed before an involution (Cartan–Kuranishi) test. OP5 is not closed.

| Path | Content |
|---|---|
| `rounds/v490_r71_round.tex` | the layer |
| `llm/Gegenpruefung_OP5_Stand_cf48496.md`, `llm/k109_*` | independent check of the germ (German note) |
| `llm/Erkundung_OP5_Symbolstruktur_Grad7.md` | the symbol exploration with all numbers (German) |
| `llm/k110_*` … `llm/k132_*` | scripts of r71.2–r71.4; each takes the path of `analysis/op5-field-slices/state-sufficiency-2026-10-30` as first argument and runs from this folder |
| `llm/k133_test_h49.py`, `llm/k134_kontrolle.py`, `llm/k133_out.json`, `llm/Ergebnis_H49_Polarwinkel_Bedingung.md` | H49 |
| `llm/k135_tps.py`, `llm/k135_check.py`, `llm/k135_test_h50.py`, `llm/k135_out.json`, `llm/k135_log.txt`, `llm/Ergebnis_H50_Omega_Psi_Kopplung.md` | H50 (series evaluator of R and the test) |
| `../predictions/Vorab_Notiz_H49_Polarwinkel_Bedingung.md`, `../predictions/Vorab_Notiz_H50_Omega_Psi_Kopplung.md` | the pre-registrations |
