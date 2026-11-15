# v4.10.0-r18: Statusvermerke zur Suche nach einem blinden Test, zur Nachrechnung von H2 und zu den Auslesegruppen der Mischung

15. November 2026. Auf „weiter“ des Autors nach dem Hinweis, dass vier Arbeitsstände seit r17 in keiner Runde stehen. Die Runde
steht als Datei `rounds/v4100_r18_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Alle
Einträge sind Erkundungen ohne Vorab-Notiz; H2 ist unter seinem ursprünglichen Kriterium nachgerechnet. Guards unverändert,
keine neue H-Nummer, kein CT-Eintrag.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r18.1 | Kein blinder Test aus r15–r17; zwei Neutrino-Kandidaten durch vorhandene Daten ausgeschlossen (R = 0 bzw. 0,0052 gegen 0,0298) | `../blind_test_search_2026_11_15/README.md` |
| r18.2 | H2 nachgerechnet: Σm_ν = 0,0592 eV, stabil mit JUNO und NuFIT 6.1, verträglich; Berichtigung der Wiki-Angabe zur Ordnung | ebenda (Nachträge) |
| r18.3 | Dreierzyklus der Dirac-Auslesung = Zeitzyklus; Slotzustände = Auslesungen zu 0, T/3, 2T/3; T fixiert die Slots, ρ gibt θ₁₃ = 0 | `../op4_time_cycle_mixing_2026_11_15/README.md` |
| r18.4 | Neutrino-ℤ₂ = Zentrumselement von Spin(8) (Fermionparität); gibt TM2; mit der r57-Maske nur maskenfreie feste Slots (je 388 Treffer) | ebenda (Nachtrag) |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2446`):
  0 Kandidaten in den Zeilen 2446–2556.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1427 Seiten (vorher 1424), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r18 im Inhaltsverzeichnis.
