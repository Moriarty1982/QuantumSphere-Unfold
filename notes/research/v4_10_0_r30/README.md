# v4.10.0-r30: Eine Zahl und ihre Übersetzungen; Orientierung des Oktantschritts (Stand 22.11.)

22. November 2026. Auftrag des Autors: „Zenodo-Veröffentlichung vorbereiten“, Zielversion v5.3.0, Physik-Paper ergänzen. Die Runde bringt die
Arbeiten nach r29 (PR #175–#187 und die OP3-Tests H113–H117 aus PR #221/#222) in den Companion. Sie steht als Datei `rounds/v4100_r30_round.tex` und ist
an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Keine neue Rechnung, keine neue H-, k- oder CT-Nummer, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r30.1 | unitärer Boost ändert das Flächenspektrum nicht (Rovelli–Speziale); frame-abhängiges Quant nur nicht-unitär oder als Mittelwert | `op1_area_quantum_boost_2026_11_18/` |
| r30.2 | Boost mit η_M entlang der Normalen: Extremzustände bevorzugt (P 0,82–0,74), nicht ausgewählt | `op1_u2_boost_2026_11_18/` |
| r30.3 | T-Regel ohne datenfreien Grund; Leiter nur für γ₀ ∈ [1; 1,0757) · γ_T; J_B² = −1 wählt nie j = ½ allein; 0 von 47 Einheiten im Fenster | `op1_t_rule_2026_11_18/` |
| r30.4 | gemeinsame Prämisse: Bausteine K0–K3, K2 ohne Stütze, K3 schwächste Stelle | `op1_common_premise_2026_11_18/` |
| r30.5 | Zufallsabschätzung: 36 · P = 0,64–0,81, mit Zufall verträglich | `chance_estimate_2026_11_18/` |
| r30.6 | eine Zahl, fünf Übersetzungen, eigene Reste je OP | `op_root_map_2026_11_18/` |
| r30.7 | Vermittler-Profil A1–A5; I1, I4, k185 erfüllen es nicht | `op_mediator_profile_2026_11_18/` |
| r30.8 | H113: farbäquivariante Auslese verschwindet | `llm/Ergebnis_H113_*` |
| r30.9 | H114: Photonpunkt legt Bargmann-Phase nicht fest; bedingte Bures-Brücke | `llm/Ergebnis_H114_*` |
| r30.10 | H115: direkter Kompensator Rang null (H115a widerlegt); reelle Halbierung mit zusätzlicher Phasenwahl | `llm/Ergebnis_H115_*` |
| r30.11 | H116: Vorzeichen des Oktantschritts durch Beträge und Endpunkte nicht festgelegt | `llm/Ergebnis_H116_*` |
| r30.12 | H117: Zwei-Fenster-Modell, 3/3/9/1 von 16 Maskenpaaren | `llm/Ergebnis_H117_*` |
| r30.13 | OP5-Erkundungen (ungerades Plateau, bifokale Sonde, Paarungsauslese) und HDL/MMA-Vergleich in 209 Fällen | `op5_bifocal_response_2026_11_18/`, `op5_pairing_readout_2026_11_18/`, `qam/examples/zuse_machine/hdl/` |

## Physik-Paper (v5.3.0)
- `qam/editions/v5_expanded_masses.tex`: Unterabschnitt „Orientation of the octant step“ (r30.8–r30.12).
- `qam/editions/v5_expanded_limits.tex`: Unterabschnitt „One number and several translations“ (r30.1, r30.5–r30.7).
- `qam/editions/v5_physics_article.tex`: je ein Satz im Massen- und im Grenzenteil; `v5_physics_references.tex`: Rovelli–Speziale 2003.
- `qam/editions/v5_research_notes.json`: sechs neue Katalogeinträge (r30.1, r30.3, r30.5, r30.6, r30.10, r30.12).

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 4135`): 0 Kandidaten in den Zeilen 4135–4339.
- Editionstests (`python -m unittest qam.store.test_editions`): 3 Tests bestanden.

OP1–OP5, C5, C6/T2 offen.
