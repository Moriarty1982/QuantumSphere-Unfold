# v4.10.0-r17: Statusvermerke zum Uhr-Funktional und zur Zählregel als Irreduzibilitätsbedingung

15. November 2026. Auftrag des Autors: „Runde r17 schreiben“. Die Runde steht als Datei `rounds/v4100_r17_round.tex` und
ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Alle Einträge sind Erkundungen ohne Vorab-Notiz und
ohne Datenvergleich (nicht blind). Guards unverändert, keine neue H-Nummer, kein CT-Eintrag.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r17.1 | Koide-Bedingung = Kohärenzfunktional der Photon-Uhr-Sonde (r90); keine Fensterschwelle bei ½, Drift 120° ≫ 26,57°, keine Gleichsetzung der Frequenzen | `../op3_time_cycle_2026_11_15/README.md` (Nachtrag) |
| r17.2 | Treue ½ als maximale Unsicherheit „dasselbe Objekt?“ (Lesart) | ebenda (Nachtrag) |
| r17.3 | Frame-Abbildungen nur bei j = ½ irreduzibel; „T irreduzibel, M invariantes Extremdublett“ gibt das H98-Paar (γ_L = 1,864700) unter Annahme (A) | `../op1_frame_irreducibility_2026_11_15/README.md` |
| r17.4 | Barbero-Verbindung als Punkt des Dubletts (A₊, A₋); Frame-Abbildungen wirken auf γ, keine gibt γ_T aus γ_M; nicht die Brücke | ebenda (Nachtrag) |
| r17.5 | Penrose-Bündel geben (A), wenn ein Strang ein Quant von χ ist; Bose → M, Fermi → T; Abgleich mit CT-004; Setzungen (S1)–(S3) | ebenda (Nachtrag) |
| r17.6 | Berichtigung: Begründung von (S2) über R² = −1 zurückgenommen (führt auf Kramers) | ebenda (Nachtrag) |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2312`):
  0 Kandidaten in den Zeilen 2312–2445.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1424 Seiten (vorher 1421), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r17 im Inhaltsverzeichnis.
