# v4.10.0-r26: Verdopplungsregel über HS(6) und Zulässigkeit von HS(7) und HS(8)

16. November 2026. Auftrag des Autors: „Ja, Runde r26“, nach der Erkundung `../op3_hs78_admissibility_2026_11_16/README.md`. Die Runde steht
als Datei `rounds/v4100_r26_round.tex` und ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht blind,
ohne Vorab-Notiz. Keine H-Nummer, kein CT-Eintrag, kein Guard ausgegeben.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r26.1 | Definition (Setzung): HS(n + 1) = HS(n) ⊕ HS(n), P⁽ⁿ⁺¹⁾ = 1₂ ⊗ P⁽ⁿ⁾, Schuld wie in HS(5) | `../op3_hs78_admissibility_2026_11_16/README.md` |
| r26.2 | Kopienoperationen leck- und schuldfrei, auch alle Konstruktionen aus r25; Schuld nur innerhalb einer Kopie; Stufen verschachtelt | ebenda, `hs78_admissibility.py` |
| r26.3 | Grenzen: Regel gesetzt, Bildprüfung von HS(6) offen; Verträglichkeit, keine Stütze der Generations-Lesart | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3588`):
  0 Kandidaten in den Zeilen 3588–3689.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1452 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r26 im Inhaltsverzeichnis.
