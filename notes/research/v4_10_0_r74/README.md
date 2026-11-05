# Layer v4.9.0-r74 on the 4.10 base (source-only): consistent data, Spencer bounds and the precision limit of the extended OP5 symbol

Continuation of [`../v4_10_0_r73/`](../v4_10_0_r73/README.md). The layer is appended verbatim to
[`sources/research/parts/v490-post-release-layers.tex`](../../../sources/research/parts/v490-post-release-layers.tex). This is **not** a release; guard vectors unchanged.
Everything concerns the fixed OP5 comparison model (`analysis/op5-field-slices/state-sufficiency-2026-10-30`).

| Item | Content |
|---|---|
| r74.1 | **H58 invalid** (pre-registered, not blind, local commit `99675a5`). All symbol parts from the exact linearization at the repaired germ; θ rebuilt (189 → 188, inclusion 2.8e-11). Known dimensions 117…898 reproduced (gaps ≥ 5e6). With the four conditions: 477, 594, 723, 865; not involutive at 6, 7, involutive at 8; characters 723, 130, 12, 0. The 724 of H57 was an artifact. Five gaps 3e3–8e3 instead of 1e4 |
| r74.2 | Exploration: Spencer cohomology with consistent data. Gauged g': H^{5,2} = 4, H^{6,2} = H^{7,2} = 0. Extended g'': H^{5,2} = 8, H^{6,2} = 4, H^{7,2} = 3 — room for up to four hidden conditions on 7-jets and three on 8-jets |
| r74.3 | Method check: a staged elimination (symbol-sized blocks) reproduces 371, 852, 481 but gives 476 instead of 477. The limit is structural: J alone is well conditioned (gap 3e10); Ω and the four conditions are nearly dependent on J (weight ~1e-8) because they act only on the cone and the planes |
| r74.4 | Exploration: plane waves on the cone span 115, 184, 267, 364, 475 instead of 117…481 (p = 2…6); the symbol module is not reduced, so the simple plane-wave reformulation does not carry |

Consequence: by all evidence the extended symbol is involutive first at order 8; further hidden conditions are not excluded.
Deciding them needs higher precision of the whole chain or a multiplicity-aware reformulation. OP5 is not closed.

| Path | Content |
|---|---|
| `rounds/v490_r74_round.tex` | the layer |
| `llm/k148_konsistent.py`, `llm/k148_log_H58.txt`, `llm/Ergebnis_H58_*.md` | H58 (consistent θ at the repaired germ) |
| `llm/k149_spencer_erweitert.py`, `llm/k149_log_kurz.txt`, `llm/Erkundung_Spencer_erweitertes_Symbol.md` | r74.2 |
| `llm/k150_stufen.py`, `llm/k151_kondition.py`, `llm/Methodenpruefung_Elimination_Kondition.md` | r74.3 |
| `llm/k152_wellen.py`, `llm/Erkundung_ebene_Wellen.md` | r74.4 |
| `../predictions/Vorab_Notiz_H58_*.md` | the pre-registration |

Scripts need the r72/r73 tools in the same folder. Notes are in German.
