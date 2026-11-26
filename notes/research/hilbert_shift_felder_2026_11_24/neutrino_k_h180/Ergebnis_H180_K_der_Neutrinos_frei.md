# Ergebnis H180: Die Mischungsdaten legen K der Neutrinos selbst auf ⅔ fest (auf ± 0,035)

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H180_K_der_Neutrinos_frei.md` (Commit 3495a67, vor der Rechnung). Skripte k381 (Python; Funktionen aus
k370/k371 unverändert) und k381b (Wolfram, zwei Punkte). Die Kontrolle reproduziert H176 (χ² = 2,86). Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Gibt man K_ν frei, so wählen die vier Messgrößen von selbst ρ_ν = 0,99 (K_ν = 0,660); erlaubt ist nur K_ν zwischen 0,634 und
0,701. **Die Daten stützen K_ν ≈ ⅔**, die Setzung war also nicht beliebig.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H180a | Profil über ρ_ν (frei: δ_ν, κ): Minimum χ² = 2,30 bei ρ_ν = 0,990; bei ρ_ν = 1: 2,39. Bereich Δχ² < 4: ρ_ν von 0,950 bis 1,050 (K_ν 0,634 bis 0,701). Außerhalb steigt χ² steil (ρ_ν = 0,90: 27; 1,10: 14). Ab ρ_ν ≈ 1,15 keine Lösung mehr | enthält 1 und schmaler als ± 0,1 | **Daten stützen K_ν ≈ ⅔** |
| H180b | Ohne kleine Drehung (κ = 0), frei ρ_ν und δ_ν: χ² = 8,16 bei ρ_ν = 0,9416 (K_ν = 0,629): sin²θ₁₃ = 0,02256 (+0,1σ), sin²θ₁₂ = 0,3179 (+2,2σ), sin²θ₂₃ = 0,5000 (+1,8σ), R exakt | χ² < 9,2 | **trägt** (knapp) |

## Bericht
- Entlang des erlaubten Bereichs aus a: Massensumme 58,7 bis 59,6 meV; sin δ_CP von 0,93 bis 1,00 (Betrag; Vorzeichen nicht gesetzt).
- Ein-Zahl-Fassung (δ_ν = π/6 − x, κ = tan x) bei festem ρ_ν: χ² = 1440 / 261 / **2,86** / 205 / 662 für ρ_ν = 0,8 / 0,9 / **1,0** / 1,1 / 1,2.
  Der Kandidat H176 funktioniert nur bei ρ_ν = 1.

## Lesart
- **Die Setzung K_ν = ⅔ ist geprüft, nicht mehr nur gesetzt.** Bisher hieß es, K_ν sei nicht gemessen. Über die Mischung ist es das doch: In der
  Ein-Feld-Form hängen die Mischungswinkel am Neutrinospektrum, und sin²θ₁₂ reagiert stark auf ρ_ν. Das Ergebnis K_ν = 0,660 (+0,041 / −0,026) ist
  modellabhängig (Ein-Feld-Form, Richtung der kleinen Drehung), aber innerhalb des Modells blind gewonnen.
- **Für die Weggabelung aus k380:** Die Daten sprechen für die Lesart, dass die Neutrinos wie die geladenen Leptonen am J-Fixpunkt sitzen, also in
  derselben farblosen Ebene {1, U} (Lesart seit H99). Die zweite farblose Ebene von HS(4) wird für die Neutrinos dann nicht gebraucht. Entschieden ist
  damit nichts Strukturelles: Auch ein freies K_ν könnte zufällig bei ⅔ liegen.
- **Eine zweite Möglichkeit für θ₁₃ (neu).** Ein etwas kleineres K_ν (0,629) erzeugt θ₁₃ ganz ohne Zusatzterm bei den geladenen Leptonen: Die Abweichung
  vom tribimaximalen Baumwert käme dann allein aus ρ_ν ≠ 1. Diese Fassung hat zwei Zahlen statt einer und passt schlechter (χ² 8,2 gegen 2,9), ist aber nach
  dem vorab gesetzten Kriterium nicht ausgeschlossen. Sie sagt sin²θ₂₃ = ½ exakt und sin²θ₁₂ = 0,318 voraus; der Kandidat H176 sagt 0,4954 und 0,3019.
  **JUNO (Zielgenauigkeit 0,002 in sin²θ₁₂) trennt die beiden.**
- H176 bleibt unverändert festgeschrieben.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k380 | Turmregel, U = e₇ | J legt nur einen von vier Sektoren fest | K_ν gedeckt oder frei? |
| H180 | Ein-Feld-Form, Richtung der Drehung | K_ν = 0,660 (+0,041 / −0,026) aus den Daten | warum die Neutrinos am J-Fixpunkt sitzen (gleiche Ebene wie e), bleibt Lesart |

## Grenzen
Ein-Feld-Form, Richtung (K₁ + K₂)/√2, Vorzeichen b > 0 und normale Ordnung aus H173 bis H176 übernommen. Raster in ρ_ν 0,005 um das Minimum; die
Bereichsgrenzen sind auf diese Schrittweite genau. Keine Übertragung in den Materie-Frame (Maske), wie in H176. Kein Vorzeichen gesetzt; kein Guard
berührt; OP3 und OP4 offen. Vergeben: H180, k381. Nächste frei: H181, k382.
