# Ergebnis H58: Cartan-Test des erweiterten Symbols mit konsistenten Daten (nicht blind)

Vorab-Notiz: `Vorab_Notiz_H58_konsistente_Daten.md`, lokaler Commit 99675a5 (3. November 2026), vor der Rechnung.
Rechnung: `k148_konsistent.py`, Protokoll `k148_log_H58.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Konsistente Daten

- J = A(0) aus der exakten Linearisierung; Abweichung vom gespeicherten J 1,2e-13.
- θ neu am reparierten Keim: dim K₃ = 189, dim K₄ = 188, Differenz 1; K₄ ⊂ K₃ auf 2,8e-11.
- Ohne σ: g'_p = 117, 188, 273, 371, 481, 606, 745, 898 (p = 2…9), alle Lücken ≥ 5e6. Gültigkeit erfüllt.

## Messwerte mit σ (in allen drei Koordinatensystemen gleich)

| p | dim g''_p | Lücke Symbolrang | dim g''^{(k)}_p | Summe | dim g''_{p+1} | Befund |
|---|---|---|---|---|---|---|
| 6 | 477 | 5e6 | 477, 107, 12, 0 | 596 | 594 | nicht involutiv |
| 7 | 594 | 1e5 | 594, 118, 12, 0 | 724 | 723 | nicht involutiv |
| 8 | 723 | **5e3** (8,1e-9 \| 1,7e-12) | 723, 130, 12, 0 | 865 | 865 | involutiv |
| 9 | 865 | **3e3** (1,8e-8 \| 6,6e-12) | | | | |

Cartan-Teilränge bei p = 8: kleinste Lücken 7e3, 8e3 (Seeds 1, 2).

## Ergebnis: ungültig

Fünf verwendete Ränge haben Lücken zwischen 3e3 und 8e3, gefordert waren ≥ 1e4. Nach dem Vorab-Kriterium ist der Test
ungültig. Alle Zahlen stimmen mit der Hypothese überein.

## Was sich geklärt hat

- Der fragliche Singulärwert aus H57 (5,6e-9 zwischen echten Werten und Rauschen) gibt es mit konsistenten Daten nicht
  mehr. Das Rauschniveau liegt bei 1,7e-12, der kleinste echte Wert bei 8,1e-9. dim g''_8 = 724 (H57) war ein Artefakt
  der Mischung aus altem θ und neuen Bedingungen.
- Damit sprechen H56 und H58 übereinstimmend dafür, dass das erweiterte Symbol erstmals bei p = 8 involutiv ist, mit
  Charakteren 723, 130, 12, 0: formal 12 Funktionen von drei Variablen.
- Die verbleibende Unsicherheit ist klein: Der Abstand zwischen echtem Wert und Rauschen beträgt 5e3. Nach Weyl müsste
  der Datenfehler der σ-Zeilen über 8e-9 liegen, um das Ergebnis zu kippen; das gemessene Rauschniveau (1,7e-12) spricht
  dagegen. Ein formaler Nachweis bräuchte die vier Bedingungen in höherer Genauigkeit.
