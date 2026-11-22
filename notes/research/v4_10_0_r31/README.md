# v4.10.0-r31: Orientierung des Oktanten als Zeitorientierung; Holst-Term und Frame-Abbildungen (Stand 22.11.)

22. November 2026. Auftrag des Autors: „Runde r31 schreiben“. Die Runde bringt die Arbeiten nach v5.3.0 in den Companion: H118 (PR #235),
die Entscheidung „OP3 ruht“, die Holst-Erkundung (PR #236) mit Nachtrag (PR #237), die Bemerkung zu Horizontnormale und Helizitätsachse und
den Datenstand der offenen Vorhersagen. Sie steht als Datei `rounds/v4100_r31_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Keine neue Rechnung, keine neue H-, k- oder CT-Nummer, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r31.1 | H118: Phase τ·ε·π/4; R, T, J_B erhalten, Θ kehrt um; kein Kandidat legt die Bahn fest; Zeitumkehr = komplexe Konjugation kehrt um, Parität (σ_x) nicht | `llm/Ergebnis_H118_Oktant_Orientierung.md` |
| r31.2 | keine zeitliche Reihenfolge aus Feldabbildungen (r16.4(c)); H119 nicht vergeben; OP3 ruht (Autor) | Übergabe 22.11., Issue #131 |
| r31.3 | W1 + Holst: Boosts (auch komplex) invariant; Dualität der Krümmung: arctan γ′ = arctan γ + θ; kein gelisteter Winkel gibt γ_T | `../w1_holst_frame_maps_2026_11_22/` |
| r31.4 | Dualität erhält A² + B²; a′/a = ±√((1+γ′²)/(1+γ²)) = ±0,981; γ_L bei gleichem G ausgeschlossen (nachträglich) | ebenda, Nachtrag |
| r31.5 | Horizontnormale und Helizitätsachse fallen nur über (S1) zusammen | `../op1_u1_check_2026_11_16/`, `../op1_flux_lines_2026_11_17/` |
| r31.6 | Datenstand 22.11.: kein offener Test entschieden | Übergabe 22.11. |

Die Notizen zu H113–H118 bleiben unter `llm/` (dort von den Preprint-Literaturangaben verlinkt); `../predictions/README.md` verweist auf sie.

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 4341`): 0 Kandidaten in den Zeilen 4341–4480.
- Dokumentbau über den Workflow `qsc-v5-dual-documents` im PR.

OP1–OP5, C5, C6/T2 offen.
