# v4.10.0-r25: Zwei und vier Dixon-Kopien auf dem Tensor-Shift; die vierte als Normale der drei Generationen

16. November 2026. Idee und Auftrag des Autors: „Ja, Runde r25“, nach der Erkundung `../op3_dixon_copies_2026_11_16/README.md`. Die Runde
steht als Datei `rounds/v4100_r25_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht
blind, ohne Vorab-Notiz. Keine H-Nummer, kein CT-Eintrag, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r25.1 | Kommutant auf n Kopien: 6n², Kopienanteil M_n(C), Ladung bestimmt | `../op3_dixon_copies_2026_11_16/README.md`, `dixon_copies.py` |
| r25.2 | HS(7): Kopien-Qubit, drei unverzerrte Zustände = flacher Oktant (det G = 0) | ebenda |
| r25.3 | HS(8): Triplett + Singulett; Spin-1-Dreieck gebogen; Spatprodukt im Singulett, \|det V\|² = det G | ebenda |
| r25.4 | Halbierung HS(8) = 2 × HS(7) = 4 × HS(6); 3 + 1 quer dazu | ebenda |
| r25.5 | nachträglich: Kästen tragen die Wurzel-Gewichte (τ 0,05 %, μ 0,9 %, e 11 %) | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3458`):
  0 Kandidaten in den Zeilen 3458–3587.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1450 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r25 im Inhaltsverzeichnis.
