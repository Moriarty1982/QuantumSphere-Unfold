# v4.10.0-r16: Statusvermerke zu Helizitätsachse, invariantem Dublett und Frame-Vorzeichen

15. November 2026. Auftrag des Autors: „Runde r16 schreiben“. Die Runde steht als Datei `rounds/v4100_r16_round.tex` und
ist an `sources/research/parts/v4100-post-release-layers.tex` angehängt. Alle Einträge sind Erkundungen ohne Vorab-Notiz und
ohne Datenvergleich (nicht blind). Guards unverändert, keine neue H-Nummer, kein CT-Eintrag.

| Theoremlet | Inhalt | Quelle |
|---|---|---|
| r16.1 | Einschränkung von r15.5: Auf C⊗O ist R skalar, T und J_B haben dieselben Eigenstrahlen ohne bestimmte Ladung; die drei Basen gibt es nur auf der Ebene z | `../op3_frame_map_generations_2026_11_15/README.md` (Nachtrag) |
| r16.2 | Koide-Phase braucht die Helizitätsachse: R erhält, T und J_B kippen die Helizität (wie Chiralität in r51); σ_y-Pole = Ports; Σ b_y² = 1; Hermitesches b_y nicht boost-invariant | `../op3_helicity_axis_2026_11_15/README.md` |
| r16.3 | Invariantes Dublett χ = (√s₊, √s₋): reelle Felder auf dem Äquator, selbstduale an den Polen, Licht ohne Punkt; boost-invariantes Oktant; Zweigwahl = R | ebenda, Nachtrag |
| r16.4 | Drei Feldvorzeichen; jede Frame-Abbildung erhält genau eines (Vierergruppe); Pole = Eigenzustände; Überlappung ½ bedingt; kein Dreierzyklus aus Feldabbildungen | ebenda, Nachtrag |
| r16.5 | Hurwitz-Zyklus auf N liefert den Dreierzyklus nicht (R skalar auf N, T: N → N̄) | ebenda, Nachtrag |
| r16.6 | „Ein Objekt“ (k220, 7.11.): Bahnen von SO(3,ℂ) × Dualität; M und T eine Bahn, Licht Fixpunkt; Zählregel nicht aus G | `../k220_ein_objekt_2026_11_07/README.md` |

## Prüfung
- Guard-Linter (`python tools/qs.py guards sources/research/parts/v4100-post-release-layers.tex --start 2112`):
  0 Kandidaten in den Zeilen 2112–2258.
- Kandidaten-Build (`python .github/scripts/qsc_latex_build.py --source-dir sources/research --output-dir <Pfad>`, MiKTeX):
  1419 Seiten (vorher 1416), 0 Fehler, 0 undefinierte Verweise, 0 Overfull; r16 im Inhaltsverzeichnis.
