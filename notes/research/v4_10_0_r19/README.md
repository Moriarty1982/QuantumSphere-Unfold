# v4.10.0-r19: Statusvermerke zum Kommutanten einer Generation und zur Vorliteratur für Dublett und Oktant

15. November 2026. Auftrag des Autors: „kannst du versuchen die brücke aus r15.5 zu zeigen“, danach „Ja, Runde r16“. Die
Nummer r16 war auf `main` schon vergeben (r16 bis r18 kamen nach dem Start der Sitzung hinzu); vergeben ist deshalb **r19**
(Dauerauftrag Versionsverwaltung). Die Runde steht als Datei `rounds/v4100_r19_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung ohne Vorab-Notiz, nicht blind (das Ergebnis folgt
vor der Rechnung aus dem Lemma von Schur). Guards unverändert, keine neue H-Nummer, kein CT-Eintrag.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r19.1 | Kommutant der Eich- und Lorentzgeneratoren auf einer Generation von C ⊗ ℍ ⊗ O: C⁶, kommutativ, kein antilinearer Anteil; kein Generations-Qubit; R zentral, T und J_B keine Symmetrien; mit n Kopien enthält er M_n(C) | `../op3_frame_bridge_2026_11_15/README.md` |
| r19.2 | Folge für den „geladenen Träger“ von r16.7: auch Auslesezustände brauchen Kopien, die vorher gesetzt sind; die Lesart „drei Generationen = drei Frame-Abbildungen“ nimmt die Zahl als Eingabe | ebenda |
| r19.3 | Vorliteratur: drei Basen des Felddubletts mit Helizitätsachse (Golat et al. 2024); Riemann–Silberstein-Lesart (Bialynicki-Birula 2013) | `../literature_check_2026_11_15/README.md` |
| r19.4 | Vorliteratur: Oktant aus drei unverzerrten Basen, Phase π/4, Neutrino-Phase 2/9 + π/12 (Brannen 2010); K = 2/3 als 45° (Foot 1994); δ ≈ 2/9 (Żenczykowski) | ebenda |

## Prüfung
- Skript `../op3_frame_bridge_2026_11_15/frame_bridge_commutant.py`, Ausgabe `run/frame_bridge_commutant_stdout.txt` dort:
  g₂ = 14, su(3) = 8, Konstruktion geprüft, Spektrum von Y richtig, Kommutant 6 (linear) und 0 (antilinear).
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2557`):
  0 Kandidaten in den Zeilen 2557–2683.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1430 Seiten (vorher 1427), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r19 im Inhaltsverzeichnis.
