# Ergebnis H65: ungültig nach Kriterium. Teil (b) stimmt, Teil (a) liegt auf dem Niveau der Kontrolle

Grundlage ist die Vorab-Notiz H65 (48a5019) mit ihrem Nachtrag. Lauf 1 rechnete `k165_kovarianz_rest.py`, Lauf 2 `k165b_werte.py`, der nicht blind ist.

## (b) Stabilisator der Eichung, Lauf 1
Die Generatoren X ∈ so(1,3) mit K₂X + X†K₂ = 0 bilden eine 3-dimensionale Unteralgebra (Singulärwerte 1, 1, 1, 0, 0, 0): Drehung um y, Boost entlang x, Boost entlang z. Das ist so(1,2), der Stabilisator von e_y, genau wie vorhergesagt.

## (a) R auf Werteebene
- **Lauf 1 ist ungültig.** Die positive Kontrolle ergab für F 0.24, weil C aus dem Symbol bestimmt wurde.
- **Lauf 2, nicht blind:** C wurde aus 80 Datensätzen bestimmt und an 20 weiteren geprüft.

| Fall | F | G | dg | Mischung zwischen Blöcken |
|---|---|---|---|---|
| Kontrolle positiv (M = 1, S = 1) | 2.0e-12 | 5.6e-11 | 2.6e-12 | 3e-11 |
| (M, S) Paar 0 | 1.3e-13 | 4.2e-11 | 1.7e-14 | 5e-11 |
| (M, S) Paar 1 | 6.6e-12 | 1.0e-11 | 1.1e-10 | 3e-11 |

Die vorab festgelegte Schranke der positiven Kontrolle (≤ 1e-12) wird für F knapp und für G deutlich verfehlt. Damit ist **(a) auch in Lauf 2 ungültig, und H65 als Ganzes ungültig.** Die Schranke lag unter dem numerischen Boden der Pseudoinversen (etwa 1e-11). Sie wird nicht nachträglich gelockert.

## Lesart (kein Testergebnis)
- Die Testwerte liegen auf demselben Niveau wie die positive Kontrolle (1e-14 bis 1e-10), fünf bis zehn Größenordnungen unter allem, was eine Brechung anzeigen würde (Lauf 1, falsches C: 0.1 bis 0.24).
- C hat dabei Blockgestalt: Die Mischung zwischen F, G und dg beträgt nur etwa 3e-11.
- Alles spricht dafür, dass R samt den Termen niedrigerer Ordnung kovariant ist. Dann wäre auch Ω kovariant, weil es aus R allein abgeleitet ist.
- Die vier Bedingungen stammen aus R zusammen mit der Eichung. Sie sind daher höchstens unter so(1,2), dem Stabilisator von e_y, kovariant.
- Eine formale Bestätigung von (a) braucht einen neuen, vorab festgelegten Test, dessen Kontrollschranke über dem Rechenboden liegt, etwa 1e-9.
