# Ergebnis H57: Cartan-Test mit projizierten Bedingungen (nicht blind)

Vorab-Notiz: `Vorab_Notiz_H57_Cartan_Test_projizierte_Bedingungen.md`, lokaler Commit 11a64a4 (3. November 2026), vor der
Rechnung. Rechnung: `k147_cartan_projiziert.py`, Protokoll `k147_log.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Messwerte (in allen drei Koordinatensystemen gleich)

| p | dim g''_p | Lücke Symbolrang | dim g''^{(k)}_p | Summe | dim g''_{p+1} | Befund |
|---|---|---|---|---|---|---|
| 6 | 477 | 4e6 | 477, 107, 12, 0 | 596 | 594 | nicht involutiv |
| 7 | 594 | 1e4 | 594, 118, 12, 0 | 724 | 724 | „involutiv“ |
| 8 | **724** | **8e2** (4,8e-6 \| 5,6e-9) | 724, 130, 12, 0 | 866 | 865 | „nicht involutiv“ |
| 9 | 865 | 1e3 | | | | |

## Ergebnis: ungültig

Die Symbolränge bei p = 8 und 9 haben keine Lücke ≥ 1e4. Bei p = 8 liegt ein Singulärwert (5,6e-9) genau zwischen echten
Werten und Rauschen; davon hängt ab, ob dim g''_8 = 723 (H56) oder 724 (H57) ist und bei welcher Ordnung der Test
„besteht“. Die Projektion hat das nicht behoben.

## Was feststeht

- Bis p = 7 sind die Zahlen in H56 und H57 gleich und sauber: dim g''_6 = 477, dim g''_7 = 594, nicht involutiv bei p = 6.
- Ab p = 8 reicht die Genauigkeit nicht. Das gespeicherte θ stammt vom älteren Keim (Abweichung etwa 1e-7). Die
  Bedingungen σ_k stammen vom echten Keim. Bei p = 8 gibt es echte kleine Singulärwerte um 1e-8, die von der Abweichung
  nicht mehr zu trennen sind.

## Folgerung

Ob das erweiterte Symbol bei p = 7 oder 8 involutiv wird, ist in double precision mit dem gespeicherten θ nicht
entscheidbar. Nötig ist ein konsistenter Datensatz: θ (die Ω-Bedingung) und die vier Bedingungen am selben, reparierten
Keim, mit höherer Genauigkeit (mpmath, mindestens 30 Stellen) für die Symbolränge bis p = 9.
