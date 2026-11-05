# Ergebnis H86: CPT-Zuordnung und endliche Beimischung am Urknall an neuen Einstellungen bestätigt

Vorab-Notiz `Vorab_Notiz_H86_CPT_Zuordnung_Urknall.md`, Commit `851297a` (nicht blind, nachträglich aus H85 motiviert). Skript `k201_cpt_zuordnung.py`, Ausgabe `k201_out.json`. Neue Einstellungen: Δ = 2, Profile tanh und Fehlerfunktion. Kontrolle: holomorphe Wronski-Determinante konstant auf 4·10⁻¹².

## Ergebnisse
- **H86a bestätigt:** Für kΔ = 6, 7, 8 ist |C| < 10⁻² in beiden Profilen und Drehrichtungen, und √(|D₊||D₋|) = √(b/a) auf 10⁻¹³. Das Produkt der beiden Drehrichtungen trifft den Grenzwert also im Rahmen der Rechengenauigkeit exakt.
- **H86b bestätigt, knapp:** ln|C| ist für kΔ ∈ [2, 8] linear (R² = 0,99987). Die Steigung ist −2,673 je Einheit kΔ, 14,9 % unter π; das Kriterium (15 %) ist gerade noch erfüllt. Die lokalen Steigungen schwanken zwischen 2,58 und 2,81 und laufen im geprüften Bereich nicht erkennbar gegen π. Die Erwartung „Abfall wie e^{−πkΔ}“ ist damit nicht gestützt, nur der exponentielle Abfall selbst. |C| ist für beide Drehrichtungen gleich.
- **H86c bestätigt:** Bei kΔ = 0,01 trifft C den scharfen Wert C₀ auf 1,7·10⁻⁴ (tanh) bzw. 1,1·10⁻⁴ (erf).
- **H86d bestätigt:** Bei kΔ = 0,02 ist |D₋|/|D₊| = 1,131 (tanh) bzw. 1,104 (erf), und √(|D₊||D₋|)/D₀ = 0,9977 bzw. 0,9985.

## Folge (wie vorab)
Die nachträgliche Lesart aus H85 hält an neuen Einstellungen:
- Unter G2 ordnet der Urknall jeder Mode der Tachyon-Lesart vor ihm im adiabatischen Bereich eine Mode negativer Frequenz danach zu (CPT-Zuordnung).
- Die Beimischung der anderen Frequenz ist für lange Wellen durch β_sym festgelegt (C₀ = (1 + β_sym²)/2 in Einheiten von a; n = (1 − β_sym²)²/(4β_sym²) im scharfen Grenzfall) und fällt oberhalb von 1/Δ exponentiell ab. Das Spektrum ist endlich, Δ bleibt frei.
- Die beiden Drehsinne des komplexen Übergangs verteilen D asymmetrisch, aber so, dass ihr Produkt fest ist (b/a im adiabatischen Bereich, D₀² bei langen Wellen bis auf 0,2–0,5 %). Die Asymmetrie wächst mit kΔ.
- Was die Asymmetrie physikalisch bedeutet, entscheidet der Test nicht.
