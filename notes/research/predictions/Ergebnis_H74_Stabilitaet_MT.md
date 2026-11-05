# Ergebnis H74: Die exakte M–T-Aufhebung ist gegen jede direkte Kopplung instabil

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H74_Stabilitaet_MT.md` (Commit b24bb08, nicht blind). Skripte `k188_test_h74.py` (Lauf 1), `k188b_lauf2.py` (Lauf 2), Ausgaben `k188_out.json`, `k188b_out.json`. Status: bestätigt; nach dem Wortlaut von Lauf 1 für die kleinen Kopplungen unentschieden wegen eines Planungsfehlers, in Lauf 2 bestätigt.**

## Lauf 1 (wie vorab festgelegt, T = 400)
| Fall | Wachstum | Rate | erwartet | Urteil nach Wortlaut |
|---|---|---|---|---|
| a, ω₁ = ω₂, ε = 1e-3 | 1,02 | – | 5e-4 | unentschieden (T zu kurz) |
| a, ε = 1e-2 | 3,7 | – | 5e-3 | unentschieden (T zu kurz) |
| a, ε = 0,1 | 9,6e5 | 0,0498 | 0,05 | bestätigt |
| b, ω₂² = 1,1, ε = 0,02 / 0,04 | 1,09 / 1,67 | – | beschränkt | bestätigt |
| b, ε = 0,06 | 578 | 0,0163 | wachsend | unentschieden (< 10³, T zu kurz) |
| b, ε = 0,1 | 1,0e6 | 0,042 | wachsend | bestätigt |
| c normal, ε = 1e-3 / 0,1 / 0,4 | 1 / 1 / 1 | – | beschränkt | bestätigt |
Energieerhaltung ≤ 6e-9 (gültig).
**Planungsfehler:** Bei Rate ε/2 braucht ein Faktor 10³ eine Laufzeit von etwa 14/ε. Die vorab festgelegte Zeit 400 reichte für ε ≤ 0,01 und den knappen Fall ε = 0,06 nicht.

## Lauf 2 (nach Lauf 1, Laufzeit an die Rate angepasst, offen als zweiter Lauf)
| Fall | T | Wachstum | gemessene Rate | exakte Rate |
|---|---|---|---|---|
| a, ε = 1e-3 | 36 841 | 9,9e5 | 5,011e-4 | 5,000e-4 |
| a, ε = 1e-2 | 3 684 | 9,3e5 | 4,985e-3 | 5,000e-3 |
| b, ε = 0,06 | 1 138 | 9,2e5 | 1,594e-2 | 1,618e-2 |

## Ergebnis
- **Gleiche Spektren (exakte Aufhebung) sind gegen jede Kopplung instabil**, mit Rate ε/(2ω). Das ist eine Resonanz: Ein Feld positiver und eines negativer Energie mit gleicher Frequenz tauschen Energie aus, und beide wachsen bei erhaltener Gesamtenergie.
- **Stabil nur bei Verstimmung:** beschränkt, solange ε < |ω₁² − ω₂²|/2.
- Zwei normale Felder sind immer stabil (Kontrolle).

## Lesart
- Die exakte Aufhebung der Vakuumenergie bei Photon-Gewichten (W2) verlangt, dass Materie und Tachyonbild dasselbe Spektrum haben. Gerade das ist der instabile Fall. **Exakte Aufhebung und Stabilität schließen sich bei direkter Kopplung aus.**
- Stabilität verlangt eine Verstimmung |Δω²| > 2ε, also verschiedene Massen in M und T. Dann ist die Aufhebung nicht mehr exakt, und es bleibt ein Rest der Vakuumenergie in der Größenordnung |V_min|·|Δω²|/ω² ≥ 2ε|V_min|/ω². **Der Rest ist durch die Kopplungsstärke nach unten beschränkt.**
- Daraus folgt eine Bedingung, die dem Modell vorgegeben ist: M- und T-Sektor dürfen höchstens extrem schwach direkt gekoppelt sein. Ein kleiner Rest-Λ und eine schwache Kopplung gehören zusammen. Ob eine Kopplung nur über die Gravitation (nichtlinear) stabil ist, ist offen; das ist die Lage bei Kaplan–Sundrum.
- Für die Konnektoren aus r44 und k185 heißt das: Ein Higgs-artiger Übergang, der M und T direkt koppelt, würde die exakte Paarung destabilisieren. Das spricht dafür, dass die Paarung (falls sie physikalisch ist) nur über eine sehr schwache Kopplung bestehen kann.
