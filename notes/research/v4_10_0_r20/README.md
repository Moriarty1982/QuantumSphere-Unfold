# v4.10.0-r20: Ein Nullaugenblick der Feldinvariante als Kandidat für einen C5-Zeugen der Form (iii)

15. November 2026. Auftrag des Autors: „Runde r19 schreiben“. **Umbenannt in r20:** Eine andere Sitzung hatte r19 parallel
vergeben und über PR #144 gemergt (Kommutant einer Generation); diese Runde trägt deshalb die nächste freie Nummer. Die Runde steht als Datei `rounds/v4100_r20_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht blind, ohne Vorab-Notiz. Keine H-Nummer,
kein CT-Eintrag, kein Guard ausgegeben. **Die verbotene Aussage C5 = 0 wird nicht gemacht.**

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r20.1 | Nullaugenblicke von s(t): existieren für eine Familie von Kodimension 1; Lorentz-invariant; Zustand im Photonpunkt P, Score ½; trivialer Fall ausgeschlossen | `../c5_null_instant_2026_11_15/README.md`, `null_instant.py` |
| r20.2 | Abgleich mit (α)–(δ) aus r88: (β)–(δ) erfüllt; (α) innerhalb der Lesart von r10, weil Lesart B augenblickliche reelle Felder betrachtet | ebenda (Nachtrag) |
| r20.3 | Zeit und Kollar-Stufe fallen nur bei reiner Helizität zusammen, die keinen Nullaugenblick hat | ebenda (Nachtrag), `time_vs_stage.py` |
| r20.4 | Frame-Audit: zwei Port-Begriffe (Scheibe gegen r51); pro Frame ist die alte Frage C5 = 0 ein vollständiger Frame-Wechsel; frame-freier Punkt P; Nullaugenblick = gleiche Anteile ½ | ebenda (Nachtrag), `frame_audit.py` |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2684`):
  0 Kandidaten in den Zeilen 2684–2808.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1433 Seiten (mit Runde r19 aus PR #144), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r19 und r20 im Inhaltsverzeichnis.
