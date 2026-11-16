# v4.10.0-r24: OP1, Statistik je Frame rückwärts geprüft; T zählt Querungen

16. November 2026. Auftrag des Autors: „Ja, Runde r24“, nach den Erkundungen `../op1_statistics_backward_2026_11_16/README.md` und
`../op1_i1_crossing_2026_11_16/README.md`. Die Runde steht als Datei `rounds/v4100_r24_round.tex` und ist an
`sources/research/parts/v4100-post-release-layers.tex` angehängt. Erkundung, nicht blind, ohne Vorab-Notiz. Keine H-Nummer, kein
CT-Eintrag (CT-004 unverändert), kein Guard ausgegeben. Auslöser I1-3 getroffen; I1 auf Autorentscheidung verfolgt.

| Eintrag | Inhalt | Quelle |
|---|---|---|
| r24.1 | (S2) aus Frame- und Portstruktur nicht begründbar: Frame-Abbildungen, Port-Parität J und strangweiser Kompensator wirken strangweise | `../op1_statistics_backward_2026_11_16/README.md`, `statistics_backward.py` |
| r24.2 | Lesart für (S3): strangweise Port-Auslesung gibt das Extremdublett \|j, ±j⟩ | ebenda |
| r24.3 | Guard „T = String-Sektor“ nicht von T11 gestützt, mit Scheiben-Ports widersprochen; γ_string nur dem Namen nach | `../op1_i1_crossing_2026_11_16/README.md` |
| r24.4 | Ersatz: T zählt Querungen des Horizonts, eine Querung ein Strang, j = ½ ohne Statistik; Stütze `thm:core`, r64(e), r63.3 | ebenda |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 3331`):
  0 Kandidaten in den Zeilen 3331–3457.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1447 Seiten, 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r24 im Inhaltsverzeichnis.
