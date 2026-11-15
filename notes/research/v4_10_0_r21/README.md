# v4.10.0-r21: C5 frame-sauber neu gestellt

16. November 2026. Auftrag des Autors: „C5 neu stellen“ (Entscheidung zur offenen Frage aus r20.4). Die Runde steht als Datei
`rounds/v4100_r21_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht blind,
ohne Vorab-Notiz. Keine H-Nummer, kein CT-Eintrag, kein Guard ausgegeben. **Die verbotene Aussage C5 = 0 wird nicht gemacht; C5
bleibt offen.**

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r21.1 | Definition: Anteile C5_M = (1 + b_x)/2 (Materie-Frame), C5_T = (1 − b_x)/2 (Tachyon-Frame), Boden φ = \|s\|/2u | `../c5_restatement_2026_11_16/README.md` |
| r21.2 | Neufassung: Übergangsfrage C5_tr (frame-typisiert), Photonpunkt-Frage C5_P (frame-frei), Brückenfrage C5_br | ebenda |
| r21.3 | Summe 1; R tauscht die Anteile; Boden fest unter R, T, J_B; gleiche Anteile ⇔ E·B = 0, notwendig, nicht hinreichend für P (Berichtigung zu r20.4) | ebenda, `restatement_checks.py` |
| r21.4 | C5_tr ist innerhalb der Lesart von r10 eine Verlagerung: C5_M = 0 ⇔ E = −B, mit C5_T = 1 und φ = 1 | ebenda |
| r21.5 | C5_P: für Felder positiv (freie Zeitentwicklung, Kodimension 1); Transporte von Lesart B und Rekursion nicht | ebenda |
| r21.6 | Bleibende Null nur für s₊ = s₋ = w = 0, von Anfang an; Zeitmittel von \|s(t)\|² = (\|s₊\|² + 4\|w\|² + \|s₋\|²)/16 | ebenda |
| r21.7 | Offen ist allein C5_br, abhängig von (B1) Lesart r10, (B2) Augenblick oder Dauer (Autorentscheidung), (B3) Vorliegen | ebenda |
| r21.8 | Zwei Klassen: Unter Lorentz-Gruppe, Dualität und Skala gibt es genau zwei Bahnen von Feldern ≠ 0 (lichtartig oder nicht); Vertreter P (φ = 0) und R (φ = 1); φ = sech 2η_R | ebenda (Nachtrag), `two_classes.py` |
| r21.9 | Kollapszustand z⁻ = 0 des Hauptkorpus heute: zwei Rollen, Nullpunkt des Versatzes (R) und invariantes Objekt (P); eine Spannung mit r24.3 vermerkt (Lesart) | ebenda (Nachtrag) |
| r21.10 | Arbeitsannahme des Autors zu (B2): Ereignis-Lesart; gesetzt, nicht hergeleitet | ebenda (Nachtrag) |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2809`):
  0 Kandidaten in den Zeilen 2809–3019.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1438 Seiten (mit Nachtrag r21.8–r21.10), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r21 im Inhaltsverzeichnis.
