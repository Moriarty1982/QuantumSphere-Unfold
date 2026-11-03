# Ergebnis H52: Formale Integrabilität des ϑ-geeichten Systems ab Ordnung 6

Vorab-Notiz: `Vorab_Notiz_H52_formale_Integrabilitaet_Ordnung6.md`, lokaler Commit 03527c6 (3. November 2026), vor der
Rechnung. Rechnung: `k139_fortsetzung.py`, Protokoll `k139_log_H52.txt`, Reihenauswerter `k138_tps_d.py`.

## Messwerte

| Lauf | Größe | Rang (Lücke, Verhältnis) | κ | Projektionen |
|---|---|---|---|---|
| Referenz (Grad 4 fest, N = 5, reparierter Jet) | 1176 × 1344 | 963 (5,8e-5 \| 7,9e-13; 7e7) | 5,2e-12 | P₅ = 381 |
| Positivkontrolle (alter Grad-4-Jet, N = 5) | 1176 × 1344 | 963 (7e7) | 3,5e-3 | P₅ = 381 |
| E₆ (Grad 5 fest; zusätzlich, nicht im Kriterium) | 1876 × 2016 | 1515 (4,6e-5 \| 8,4e-13; 6e7) | 4,0e-3 | P₆ = 501 |
| E₇ (Grad 5 fest) | 4684 × 4896 | 3778 (4,7e-10 \| 1,1e-12; **4e2**) | 3,5e-3 | P₆ = 481 (4e3), P₆₇ = 1118 |
| E₈ (Grad 5 fest) | 8689 × 8856 | 6984 (1,9e-10 \| 9,7e-13; **2e2**) | 2,4e-3 | P₆ = 478 (**7e1**), P₆₇ = 1083 (6e2) |

Die Kontrollen funktionieren: κ_pos / ε_ref = 7e8 ≥ 1e4. Die Linearisierung stimmt mit dem gespeicherten Symbol überein,
max|A_μ(0) − J| = 3,8e-11, und der Eichvektor wird vernichtet, |A_μ(0) v| ≤ 1,7e-11.

## Ergebnis: ungültig

In E₇ und E₈ haben die verwendeten Ränge keine saubere Lücke (Verhältnis 7e1 bis 6e2, gefordert ≥ 1e4). Nach dem
Vorab-Kriterium ist der Test ungültig. Die Zahlen P₆ und P₆₇ aus E₇/E₈ werden nicht bewertet.

## Was trotzdem feststeht

- **Der gespeicherte Jet bis Grad 5 lässt sich nicht fortsetzen.** Das zeigt E₆ mit sauberer Lücke (6e7): κ = 4,0e-3,
  auf dem Niveau der Positivkontrolle. Weil die Grad-5-Gleichungen nur c₆ enthalten, gilt das auch für jedes E_N.
- **Ursache im Testaufbau, nicht im System.** Die Grad-5-Koeffizienten des Keims wurden am 30. Oktober nur gegen die
  Grad-4-Gleichungen gelöst (`PRECISION_FIFTH_GATE_REPAIR.md`). Die einmal mehr abgeleitete Ω-Bedingung (Ordnung 5,
  10 Zeilen) erfüllen sie nicht. Dazu passen die Zählungen: In den kurzen Systemen fehlen die fortgesetzten Ω-Zeilen,
  daher P₅ = 381 = 371 + 10 und P₆ = 501 = 481 + 20. Ein fester 5-Jet ist für die Prüfung also falsch gewählt; der
  Grad-5-Anteil muss frei bleiben.
- **Ursache der schlechten Lücken (Vermutung).** A und B bis Grad 2 kommen aus Differenzenquotienten (h = 1e-3). Bei
  Keimkoeffizienten bis 3e4 sind sie zu ungenau für Systeme mit mehreren Graden.

## Folgerung

Neuer Test mit eigener Vorab-Notiz (H53): nur der reparierte Jet bis Grad 4 fest, c₅ … c_N frei, Linearisierung exakt.
Exakt ist sie, weil Sonden ab Grad 4 bis Grad 6 streng linear eingehen.
