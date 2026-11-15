# v4.10.0-r19: Ein Nullaugenblick der Feldinvariante als Kandidat für einen C5-Zeugen der Form (iii)

15. November 2026. Auftrag des Autors: „Runde r19 schreiben“. Die Runde steht als Datei `rounds/v4100_r19_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht blind, ohne Vorab-Notiz. Keine H-Nummer,
kein CT-Eintrag, kein Guard ausgegeben. **Die verbotene Aussage C5 = 0 wird nicht gemacht.**

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r19.1 | Nullaugenblicke von s(t): existieren für eine Familie von Kodimension 1; Lorentz-invariant; Zustand im Photonpunkt P, Score ½; trivialer Fall ausgeschlossen | `../c5_null_instant_2026_11_15/README.md`, `null_instant.py` |
| r19.2 | Abgleich mit (α)–(δ) aus r88: (β)–(δ) erfüllt; (α) innerhalb der Lesart von r10, weil Lesart B augenblickliche reelle Felder betrachtet | ebenda (Nachtrag) |
| r19.4 | Frame-Audit: zwei Port-Begriffe (Scheibe gegen r51); pro Frame ist die alte Frage C5 = 0 ein vollständiger Frame-Wechsel; frame-freier Punkt P; Nullaugenblick = gleiche Anteile ½ | ebenda (Nachtrag), `frame_audit.py` |
| r19.3 | Zeit und Kollar-Stufe fallen nur bei reiner Helizität zusammen, die keinen Nullaugenblick hat | ebenda (Nachtrag), `time_vs_stage.py` |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2557`):
  0 Kandidaten in den Zeilen 2557–2681.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1430 Seiten (vorher 1427), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r19 im Inhaltsverzeichnis.
