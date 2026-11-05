# Erkundung: Mischungsmatrix der Konnektoren (k187)

**5. November 2026. Status: Erkundung, vollständig durchgespielt, ohne Kriterium.** Autor: „Man müsste wohl alles mal durchspielen, ob es da Unterschiede gibt, und die Mischungen in einer Matrix festhalten.“

## Aufbau
Vier Konnektoren aus k185 zwischen Materie p_M und ihrem Tachyonbild (Konvention F):
- c0 = p_M − p_T(gegen), tachyonisch;
- c1a = p_M + p_T(mit), lichtartig;
- c1b = p_M − p_T(mit), lichtartig;
- c2 = p_M + p_T(gegen), massiv.

Alle 15 Σ-Mischungen (Teilmengen, Impulse addiert), q² über η ∈ {0,1 … 2}, dazu die Maskennummer (Summe der Bits) unter allen 24 Bit-Zuordnungen.

## Matrix
| Mischung | q² | Maskennummern über alle Zuordnungen |
|---|---|---|
| c0 | −2m² sinh 2η | 1, 2, 4, 8 |
| c1a, c1b | 0 | 1, 2, 4, 8 |
| c2 | +2m² sinh 2η | 1, 2, 4, 8 |
| **c0 + c2** | **4m², konstant** | 3, 5, 6, 9, 10, 12 |
| **c1a + c1b** | **4m², konstant** | ebenso |
| c0 + c1a, c0 + c1b, c1a + c2, c1b + c2 | η-abhängig | ebenso |
| **c0 + c1a + c2, c0 + c1b + c2** | **8m², konstant** | 7, 11, 13, 14 |
| c0 + c1a + c1b, c1a + c1b + c2 | η-abhängig | ebenso |
| **c0 + c1a + c1b + c2** | **16m², konstant** | 15 |

## Ergebnisse
1. **Die Bit-Zuordnung macht keinen Unterschied.** Sie benennt nur die Masken um; welche Mischung η-unabhängig ist, hängt allein davon ab, welche Konnektoren darin stehen. Für jede Größe der Teilmenge laufen die Maskennummern über dieselbe Menge.
2. **Die η-unabhängigen Mischungen** haben q² ∈ {0, 4, 8, 16}·m².
3. **Grund:** Für jedes η ist das Tachyonbild Minkowski-orthogonal zur Materie, p_M·p_T(mit) = m²(cosh η sinh η − sinh η cosh η) = 0. Eine Mischung aus n-mal p_M und k-mal ±p_T(mit) hat deshalb q² = (n² − k²)m², unabhängig von η: (1, 1) → 0, (2, 0) → 4, (3, 1) → 8, (4, 0) → 16. Gegenläufige Anteile (c0, c2) sind nur in Paaren η-frei, weil c0 + c2 = 2p_M.
4. **Zum 2^k-Shift:** 4, 8, 16 sehen wie Zweierpotenzen aus, folgen aber aus n² − k² (8 = 3² − 1). Bei mehr Konnektoren käme zum Beispiel 9 = 3² dazu. Die Übereinstimmung mit H_mask ist bei diesen kleinen Zahlen ein Zufall.

## Lesart
- Das klarste Ergebnis ist strukturell: **Materie und ihr Tachyonbild stehen in Konvention F für jede Rapidität senkrecht aufeinander** (Minkowski). Daraus folgen der lichtartige mitlaufende Konnektor (k185), die Paarschwelle 4m² und das ganze η-freie Gitter n² − k².
- Ein String- oder 2^k-Turm entsteht so nicht; die η-freien Massen bilden das Gitter n² − k².
