# QAM-Artikel

*Vom Plan zum Guard: QAM als Spezifikations- und Abhängigkeitsarchitektur für sprachmodellgestützte Forschung*

Deutscher Entwurf vom 22.11.2026, 18 Seiten Text und Anhang, mit Literaturverzeichnis 20 Seiten. Er ersetzt den englischen Methodenentwurf vom 4.11.2026 (in der Git-Geschichte erhalten).
Veröffentlichung nur auf Zenodo. Aufbau: zuerst QAM als eigenständiges, projektunabhängiges Modell, dann die Umsetzung (LaTeX, Lean,
Maschine, MCP), erst danach der Einsatz im Projekt Quantum Sphaera.

PDF: [`qam_paper_draft.pdf`](qam_paper_draft.pdf).

Übersetzen (der Artikel lädt `qam.sty`; die Beispiele in Abschnitt 3 und 6 werden beim Setzen geprüft):

```sh
TEXINPUTS=../../qam/tex: pdflatex main.tex   # zweimal; unter Windows ../../qam/tex;
```

| Datei | Inhalt |
|---|---|
| `main.tex` | Präambel, Zusammenfassung, Literatur |
| `s1_einleitung.tex` | stille Übergänge; Zuse (Plan und Rechenwerk), Turing (Entscheidbarkeitsgrenze) |
| `s2_modell.tex` | Akte, Eintrag, Regeln R1–R4, offene Bedingungen, Hash-Kette, Objektebene |
| `s3_latex.tex` | LaTeX-Anbindung: Betriebsarten, Deklarationen, erzeugte Notation (live), Export, Profile, Belegfragmente, Tests |
| `s4_guards.tex` | drei Prüfer; Ebene A (Statusvererbung, Lean) und Ebene B (Guards der Maschine) |
| `s5_maschine.tex` | Datenbank, MML/MMA, Belege, Stapel, Bandmaschine, MCP-Server |
| `s6_einsatz.tex` | Einsatz im Projekt: Ablauf, Koide-Beispiel (konstruiert, live geprüft), β-Fall, Fehlerklassen |
| `s7_abgrenzung.tex` | Abgrenzung zu Beweisassistenten, verwandte Ansätze, Weiterentwicklung, Grenzen und Schluss |
| `a1_lean.tex` | Lean-Module, Übersetzung, Einsatz von Sprachmodellen |
| `outline.md` | Gliederung |

Offen: unabhängige Gutachterrunde. Abschnitt 7.2 ordnet QAM gegen Blueprints (leanblueprint, KnowTeX, LeanMarathon),
Autoformalisierung, Annahmenverwaltung (TMS/ATMS, GSN), Informationsfluss- und Herkunftsmodelle sowie Workflow-Werkzeuge ein. Die Testzahlen in Abschnitt 6 stammen aus `wiki/Vorhersagen-und-Tests.md` (Stand 22.11.2026),
die Aktenzahl aus den im Repository versionierten `.qam`-Dateien ohne absichtlich fehlerhafte Beispiele.
