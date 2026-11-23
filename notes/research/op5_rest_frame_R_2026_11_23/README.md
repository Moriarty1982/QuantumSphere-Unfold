# Das Feldruhesystem R als Bezugssystem der Verlangsamung: trägt teilweise; nachträglich ein No-go für den lichtschnellen Higgsradius (Erkundung, nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** Ein Feld mit E ∥ B ist unter Boosts entlang seiner Achse invariant; jede daraus gebaute Ausbreitungsstruktur ist
entlang der Achse lichtschnell und kann nur quer zur Achse verlangsamen. Damit hält die Kegelgrenze quer zur Achse, bricht aber für Wellen
entlang der Achse im massiven Kanal. **Nach dem vorab festgelegten Raster: trägt teilweise.** Nachträglich gefunden: Mit dem lichtschnellen
Higgsradius, den W2 erzwingt (c_h² = 1, r33), ist die Grenze für keine Wahl der Vermittlergeschwindigkeiten zu halten.

Auftrag des Autors: „weiter“ nach r48. Verfahren vorab: `Methoden_Notiz.md` (Commit a306f879). Nicht blind (Symmetrieüberlegung vorab).
Skripte `rest_frame_R.wl` (Wolfram exakt, Ausgabe `run/rest_frame_R.txt`) und, nachträglich, `higgs_luminal_check.py` (sympy, Ausgabe
`run/higgs_luminal_check.txt`; die Wolfram-Fassung brach zweimal mit Serverfehlern ab). Qiskit nicht geeignet. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) Symmetrie | Ein Boost entlang der Achse lässt F unverändert, ein Boost quer dazu nicht. R ist damit nur bis auf Boosts entlang der Achse bestimmt: eine zeitartige Ebene (t, z), kein einzelnes Ruhesystem. |
| (1) invariante Tensoren | Unter Boosts entlang der Achse und Drehungen um sie invariant sind genau S = diag(s₁, s₂, s₂, −s₁); der Energie-Impuls-Tensor des Feldes gehört dazu (T = ρ·diag(1, 1, 1, −1)). |
| (2) Ausbreitung | Für jeden solchen Tensor ist die Geschwindigkeit entlang der Achse genau 1. Beispiel G = η + λT: quer (1 − λρ)/(1 + λρ), also ½ bei λρ = ⅓. |
| (3) Kegelgrenze, c_h² = ½ | mit r(α) = 1 − α/2: verletzt nahe der Achse (α = 0: 1,040; α = 1/20), erfüllt sonst (α = 1: 0,675). Ursache: Bei α = 0 ist r = 1 und j_m² = ⅔g_m² ≠ 0; der masselose Kanal koppelt dort nicht (j_0 = 0). |
| (3) Kegelgrenze, c_h² = 1 | verletzt bei allen 21 Rasterpunkten (größter Wert 1,165, auch α = 1: 1,064). |
| nachträglich | Bei c_h² = 1 ist die obere Bedingung identisch −⅔g_m²(1 + r_m − α) − j_0²/(1 − r_0) − j_m²/(1 − r_m) < 0 für alle r_0, r_m ∈ (0, 1), α ∈ [0, 1], g_m > 0. |

## Lesart
- R kann die Verlangsamung nur quer zur Achse liefern. Entlang der Achse bräuchte es ein Bezugssystem, das Boosts entlang der Achse bricht,
  also einen zeitartigen Ruhevektor eines Mediums. Das Feld mit E ∥ B hat keinen. Die in r48 benannte Zuordnung hilft damit zur Hälfte.
- Nachträglich, nicht vorab festgelegt, aber für das ganze Vergleichsmodell wichtig: Die Kegelgrenze verlangt außer langsamen Vermittlern auch
  einen verlangsamten Higgsradius (c_h² < 1; im Modell gesetzt ½). W2 erzwingt aber c_h² = 1 (r33). Mit dem Higgsradius von W2 ist die
  gerichtete Kopplung (g_m ≠ 0) deshalb mit keinem Vermittler kausal verträglich. Das ist ein No-go für die Verbindung „Vergleichsfeld =
  Higgs-Radialmodus von W2“ (r33) zusammen mit der gerichteten Kopplung, unabhängig von Feldseite oder Ausleseseite.
- Verlangsamt werden müssten also drei Ausbreitungen: der Higgsradius und beide Vermittler. Alle drei brauchen ein Medium mit eigenem Ruhevektor.
- OP1 und OP5 bleiben offen.
