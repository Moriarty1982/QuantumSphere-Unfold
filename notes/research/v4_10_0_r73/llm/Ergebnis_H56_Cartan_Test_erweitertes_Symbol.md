# Ergebnis H56: Cartan-Test des um die vier Bedingungen erweiterten Symbols

Vorab-Notiz: `Vorab_Notiz_H56_Cartan_Test_erweitertes_Symbol.md`, lokaler Commit 4ed4c3e (3. November 2026), vor der
Rechnung. Rechnung: `k146_cartan_erweitert.py`, Protokoll `k146_log.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Gültigkeit

- Hauptwinkel zwischen G₆ (echter Keim) und g'_6 (gespeichertes Symbol): max sin = 4,4e-7 ≤ 1e-5. Erfüllt.
- dim g''_6 = 477. Erfüllt.
- Lücken: Symbolränge p = 6 (4e6), p = 7 (**6e3**), p = 8 (**8e2**), p = 9 (**1e3**); Cartan-Teilränge 1e3 bis 1e15.
  Nicht erfüllt (gefordert ≥ 1e4).

## Messwerte (in allen drei Koordinatensystemen gleich)

| p | dim g''_p | dim g''^{(k)}_p, k = 0…3 | Summe | dim g''_{p+1} | Befund |
|---|---|---|---|---|---|
| 6 | 477 | 477, 107, 12, 0 | 596 | 594 | nicht involutiv |
| 7 | 594 | 594, 118, 12, 0 | 724 | 723 | nicht involutiv |
| 8 | 723 | 723, 130, 12, 0 | 865 | 865 | involutiv |

dim g''_9 = 865. Vergleich g'_p: 481, 606, 745, 898.

## Ergebnis: ungültig

Drei Symbolränge haben keine Lücke ≥ 1e4. Nach dem Vorab-Kriterium ist der Test ungültig.

## Ursache

Bei p = 6 liegt das Rauschniveau bei 4e-15, ab p = 7 bei 1e-11. Die Bedingungen σ_k stammen vom echten Keim; sie sind
nur bis auf den Annihilator der echten Faser bestimmt. Das gespeicherte Symbol weicht davon um 4,4e-7 ab (Hauptwinkel).
Der Anteil von σ_k längs dieser Abweichung erzeugt in den fortgesetzten Zeilen kleine Scheinränge. Abhilfe: σ_k vor der
Fortsetzung auf die gespeicherte Faser g'_6 projizieren.

## Was die Zahlen sagen

Inhaltlich eindeutig und in allen drei Koordinatensystemen gleich: Das erweiterte Symbol ist nicht involutiv bei
p = 6 und 7, involutiv bei p = 8. Die letzte Charakteristik ist 12 statt 14: Formal hängen die Lösungen dann von
12 Funktionen von drei Variablen ab. Formal unbestätigt; Wiederholung mit projizierten σ_k als H57 (nicht blind).
