# v4.10.0-r23: Wohin führt die Kaskade? Zwei Kaskaden unter einem Namen

16. November 2026. Auftrag des Autors: „Ja, Runde r23“, nach der Erkundung `../cascade_endpoint_2026_11_16/README.md`. Die Runde steht
als Datei `rounds/v4100_r23_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht
blind, ohne Vorab-Notiz. Keine H-Nummer, kein CT-Eintrag, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r23.1 | drei Beschreibungen der Kaskade im Hauptkorpus (Nullachsen-Transport, K̂ = C ∘ Π_J, Hopf- und Markov-Kette) | `../cascade_endpoint_2026_11_16/README.md` |
| r23.2 | Kompensator-Kaskade endet in R: Kompensatorbild hat φ = 1, auch bei lichtartigen Feldern | ebenda, `cascade_endpoint.py` |
| r23.3 | Nullachsen-Transport bleibt in der lichtartigen Klasse: trägt P, führt nicht hin | ebenda |
| r23.4 | Reservoir-Attraktor zwischen P und R je nach Kopplung; Dephasierung zu P nur im Grenzwert | ebenda |
| r23.5 | Antwort auf r22.4: zwei Kaskaden unter einem Namen; zum Nullzustand P führt keine endliche Kaskade | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3199`):
  0 Kandidaten in den Zeilen 3199–3330.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1444 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r23 im Inhaltsverzeichnis.
