# Integration der OP5-Serie vom 25. bis 27. Oktober 2026 (Runde v4.9.0-r69)

Stand: 28. Oktober 2026. Auftrag des Autors: die Arbeit, die er lokal mit einem anderen Sprachmodell gemacht hat, in die laufende Arbeit einbinden.
Der Autor hat entschieden, sie als Runde v4.9.0-r69 aufzunehmen.

## Quelle

Sechs Commits auf `main` von `Moriarty1982/QuantumSphere-Unfold`, alle unter `analysis/`, ohne PR:

| Commit | Datum | Inhalt |
|---|---|---|
| `3fa5ba9` | 25.10., 23:59 | Frame-Bilanz neu geprüft, Abhängigkeiten bis Λ, neutrale Bezüge aus zwei Frames |
| `a97e32d` | 26.10., 09:02 | Auslese-Energie, Reihenfolge, Paardynamik, HS(5)-Partnersektor, Realifizierung, M16/P_C7-Frame-Herkunft |
| `bb975d2` | 27.10., 01:12 | Suche nach einer Regel für den absoluten Vakuumterm, affiner Zweig, lineare Mode, triadische Energie |
| `cf9e167` | 27.10., 07:01 | Nulltransport und Signal-Lokalität, zwei komplexe Sonden, Kegelvergleich, relative Verbindung, gemeinsame Wirkung |
| `5913abb` | 27.10., 20:58 | triadischer Transport, Torsion, Ward-Ausschluss, Gegenstrom, Bloch-Residuum, Boost- und chirale Tangente |
| `337d9cb` | 27.10., 22:22 | Zustandsmenge und Ensemble, Literaturwege |

Zusammen 173 Dateien, 20 912 Zeilen: 84 Notizen, 23 Prüfskripte, 64 JSON- und Textausgaben (Ergebnisse, Rechenverträge, Manifeste, Literaturkatalog), eine Grafik und eine HTML-Visualisierung.
Lokal mit `git checkout github/main -- <Dateien>` nach `analysis/` übernommen (Muster wie `34d2a41`).

## Reproduktion

Alle 23 Prüfskripte mit Python 3.13, SymPy und NumPy neu ausgeführt; vier brauchen `--output`. Alle laufen ohne Fehler durch.
Die drei Skripte, die ihre JSON-Ausgabe selbst schreiben, erzeugen Dateien, die sich von den eingecheckten nur in der letzten
Gleitkommastelle unterscheiden (z. B. `85.52615362395123` gegen `85.5261536239512`).

## Eigene Nachrechnung (`llm/k106_nachrechnung_op5.py`, Ausgabe `llm/k106_out.txt`)

| Aussage | Ergebnis |
|---|---|
| Reihe von R(τ) = −e^{−τ/2}/(e^τ − 1) | −1/τ + 1 − 11τ/24 + τ²/8 + … (bestätigt; der Companion druckt −1/τ + 1/2 − τ/12) |
| regularisierter Wert bei T = 0,393, μ = 1 | 1,6889 (der Companion druckt 0,940 mit falschem Gegenterm) |
| Ward-Ausschluss | (hb²)′ ∝ b(9b² − 2b − 1), Wurzeln (1 ± √10)/9, mit b + 3tb′ = 1 unverträglich (bestätigt) |
| Torsionszeuge | E = ½Dj und T = ½Rj exakt, T¹ = −(1/t) dt∧dx (bestätigt) |
| Austauschzeuge, Zeitachse | Residuum 544 t² + O(t⁴), Geschwindigkeit 1 − 80 t² (bestätigt) |
| zwei komplexe Sonden | g = diag(−9, 1, 1, 1) (bestätigt) |
| Mischung auf der reellen Scheibe | mit σ_y genau I/2, mit σ_x bleibt b_x (bestätigt) |
| q_rel = tanh²η = (cosh 2η − 1)/(cosh 2η + 1) | Identität (bestätigt) |
| V′/M⁴ bei historischer Trennung | 0,383564 (bestätigt) |

## Fehler im Hauptkorpus, an der Quelle geprüft

1. `rem:regularization-B` (`sources/research/parts/v470/23_physical_readouts.tex`, Z. 767–791): Reihe und Vorzeichen des Gegenterms falsch,
   Zahlenwert 0,940 nicht reproduzierbar; damit auch 0,893 in `prop:theta-required-B` nicht getragen. Der Weg ist seit v4.8.0-r05 als falsch markiert.
2. `thm:dirac-probe` (Z. 1974) und `prop:three-compatible-readings` (Z. 2001) in `v470/10_sphaera_and_physics.tex` stützen β_sym und die
   Uhrskala auf das archivierte `thm:gue-selfdet`; dort steht noch kein Statusvermerk.
3. Korollar „Cosmological constant revisited“ (ebenda, Z. 1891 ff.): Frame-Term null und endliches Verhältnis γ_L⁵ für dieselbe Größe.
   Ergänzt die Statusnotiz-Kandidaten aus r64 und r67.

Alle drei sind Kandidaten für Statusvermerke (Regeln B und C aus r25). Sie werden in r69 nicht geschrieben; das wäre eine eigene Runde
nach Autorentscheidung, wie r62 nach r61 und r65 nach r64.

## Einordnung

- Jede positive Aussage der Serie ist bedingt: deklariertes Vergleichsmodell, gewählter Zeuge oder zwei Stichpunkte.
- Die Notizen mit „Independent“ im Namen stammen von Unteragenten desselben Modells; ein externes Review gibt es nicht.
- Die Serie korrigiert sich einmal selbst (Realifizierung von J_B steht in r04.1).
- Guards unverändert; OP5_exact offen, OP5_eff unberührt.
