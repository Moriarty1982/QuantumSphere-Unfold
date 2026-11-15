# v4.10.0-r15: Berichtigung der Frame-Lesart von r38 und Statusvermerke

15. November 2026. Auftrag des Autors: „prüfe r38 nochmal, könnte noch auf alten annahmen basieren“, danach
„Ja, r15 schreiben“. Die Runde steht als Datei `rounds/v4100_r15_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Alle Einträge sind Erkundungen ohne Vorab-Notiz und ohne
Datenvergleich (nicht blind). Guards unverändert, keine neue H-Nummer, kein CT-Eintrag.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r15.1 | Berichtigung zu r38: Frames sind keine Triality-Slots, sie wirken über den C-Faktor (r51); M ↔ T ist kein Chiralitätswechsel; r38.1 bleibt gültig; der Slot-Konflikt Frames/Generationen entfällt in seiner ursprünglichen Form; Folgen für die Benennung in H29 (r44) und r14.3(d) | `../op3_frame_map_generations_2026_11_15/README.md` |
| r15.2 | Kern als Schatten eines Horizonts: fehlende Abbildung, von selbst flussfrei; Größe offen (Synge r = 17,99 M, Sektor γ/2); Lesung im Frame M | `../op3_horizon_shadow_2026_11_15/README.md` |
| r15.3 | Spin-1-Dreieck: cos a = √2 − 1, Phase 0,679042, Rang 3; Bezugsrichtung nicht nativ (143 Kandidaten) | `../op3_spin1_triangle_2026_11_15/README.md` |
| r15.4 | Koide als vollständige Komplementarität: K = 2/(d + 1), nur d = 2 gibt drei Zustände | `../op3_koide_complementarity_2026_11_15/README.md` |
| r15.5 | Eine Generation je Frame-Abbildung T, J_B, R: unverzerrt, K = 2/3, Phase ±π/4; R erhält, Konjugation kehrt das Vorzeichen | `../op3_frame_map_generations_2026_11_15/README.md` |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 1955`):
  0 Kandidaten in den Zeilen 1955–2111.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1416 Seiten (vorher 1412), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r15 im Inhaltsverzeichnis.
