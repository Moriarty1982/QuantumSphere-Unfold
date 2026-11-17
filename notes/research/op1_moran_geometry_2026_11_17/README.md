# OP1: Eine Geometrie, die die Zählregel von selbst festlegt? Die Zählgleichung als Moran-Gleichung (Erkundung, nicht blind)

17. November 2026. Frage des Autors: „Alternativ, kann man eine geometrische Struktur konstruieren, die das Problem von selbst löst?“ Skripte `moran.py`,
`layout2d.py`, `rule_space.py`, `branching.py` (`pack2d.py` ist ein verworfener erster Packversuch mit ungeeignetem Schnittverfahren), Ausgaben unter
`run/`. Nicht blind: Alle γ-Werte und der Zielwert γ_L waren bekannt; das Maximalitätsprinzip unten ist nachträglich formuliert. Keine H-Nummer.

## Vorwissen geprüft
- `thm:fractal` (v470/10): „fraktal“ heißt dort selbstähnlicher Transport der Null-Achse durch die Strata, ausdrücklich keine fraktale Dimension (Kernkarte,
  Abschnitt 5); D_res ≈ 2,435 der Kristall–Fraktal-Probe ist eine Diagnosezahl (v470/32). Eine Moran-Lesart der Zählregeln gibt es im Bestand nicht.
- r28.2: Endliche symmetrische Konstruktionen sind starr und liefern algebraische Winkel; eine Zahl wie γ_L kann aus ihnen nicht kommen.
- `../op1_readout_frequency_2026_11_17/`: ω_M/ω_T = γ_L; das T-Quant ist 4 ln 2 in jedem Spektrum.

## Die Umschreibung (exakt)
Die Zählgleichung eines Frames, Σ_j g(j) e^{−2πγ a(j)} = 1, lautet in Einheiten des T-Quants (2πγ_T a(½) = ln 2) mit D = γ/γ_T:

  Σ_j g(j) · r_j^D = 1,  r_j = 2^{−a(j)/a(½)}.

Das ist die **Moran-Gleichung**: Ein selbstähnliches Fraktal mit g(j) Kopien auf der Skala r_j hat, wenn die Kopien sich nicht überlappen (offene-Mengen-
Bedingung), die Hausdorff-Dimension D (für abzählbar viele Abbildungen nach Mauldin–Urbański; Literatur aus Vorwissen, hier nicht nachgelesen).
**Die Frame-Faktoren sind also Dimensionen:** γ_L = D_M, und die Breite von M ist b_M = 1/D_M.

| Spektrum | T | M (Gewicht 2) | P (Gewicht 2j + 1) |
|---|---|---|---|
| √(j(j+1)) (Bestand) | **1** (Strecke aus zwei Hälften) | **1,8647 = γ_L** | 2,1515 = γ_P/γ_T |
| j (linear) | 1 | log₂ 3 = 1,585 (Dimension des Sierpinski-Dreiecks) | log₂(2 + √2) = 1,772 |
| j + ½ | 1 | 2 | 2,336 |

Die Quasinormal-Lesart aus der Notiz zur Auslesefrequenz ist in dieser Sprache das Sierpinski-Dreieck.

## Passt das Fraktal auf eine Fläche?
Für ein Ähnlichkeits-Fraktal mit offener-Mengen-Bedingung in ℝ^d ist Σ g r^d ≤ 1 notwendig (Volumenargument).
- **M:** Σ 2r² = 0,869. Eine explizite Anordnung im Einheitsquadrat (`layout2d.py`: die 12 größten Kopien von Hand gesetzt und auf Überlappung geprüft; der
  Rest mit Fläche 0,0063 passt nach Moon–Moser in ein freies Quadrat der Fläche 0,0204) zeigt: **Das M-Fraktal liegt in der Ebene**, offene-Mengen-
  Bedingung mit V = offenes Einheitsquadrat, Dimension 1,8647.
- **P:** Σ (n + 1) r² = 1,199 > 1. **Die volle SU(2)-Zählung kann auf keiner Fläche als solches Fraktal liegen** (D = 2,15 > 2); im Raum passt sie.
- **Regelraum S von H98** (Spinbereiche alle, halbzahlig, ganzzahlig, nur ½, nur 1; Gewichte 2, 2j + 1): Die Ebenenbedingung schließt genau eine Regel aus,
  (alle Spins, 2j + 1), also die GM/ENP-Zählung mit 0,274. Unter den übrigen hat (alle Spins, 2), die Regel von M, die größte Dimension.

## Ganzzahlige Kopienzahl je Skala

| Kopien je Skala w | D | Σ w r² | Ebene |
|---|---|---|---|
| 1 | 1,2685 | 0,435 | passt |
| **2** | **1,8647** | 0,869 | **passt** |
| 3 | 2,2688 | 1,304 | passt nicht |
| 4 | 2,5769 | 1,739 | passt nicht |

D = 2 genau läge bei w = 1/Σ r² = 2,30, nicht ganzzahlig. **2 ist die größte ganze Kopienzahl je Skala, die auf eine Fläche passt.**

## Die Struktur, die das Problem von selbst löst (Lesart, nachträglich)
**Prinzip:** Ein Horizont trägt das reichste selbstähnliche Gebilde, das (i) auf jeder Skala des SU(2)-Flächenspektrums eine ganze Zahl von Kopien hat und
(ii) auf der zweidimensionalen Fläche überlappungsfrei liegt. Daraus folgt ohne freien Parameter: zwei Kopien je Skala, also die Zählregel von M
(Gewicht 2 für jeden Spin), γ_M = 0,237533, γ_L = D_M = 1,8647, b_M = 1/γ_L = 0,5363, β² = (D − 1)/(D + 1) = 0,3018. T ist der Grenzfall „nur die
größte Skala“, eine Strecke mit D = 1; P (alle 2j + 1) passt nicht auf die Fläche, sondern nur in den Raum.
- Das passt zu den Lesarten der letzten Tage: zwei Kopien je Skala ist „ein Bit je Punktierung“ (`../op1_entropy_count_2026_11_17/`, reine Stränge mit
  unbekanntem Port), und P außerhalb der Fläche passt zu „P hat einen eigenen HC, keinen Grenzwert“ (`../op1_hc_blur_2026_11_16/`).
- Es berührt den Streit der Literatur (U(1) gegen SU(2)): Die SU(2)-Zählung zählt mehr Zustände, als ein selbstähnliches Gebilde auf einer Fläche tragen kann.

## Grenzen
- **Nicht blind:** γ_L war bekannt; das Prinzip (ganzzahlig, maximal, zweidimensional) ist nachträglich so gewählt, dass es trifft. Es ist eine Lesart,
  kein Beweis.
- **Annahmen:** Die Skalen werden in Einheiten des T-Quants gemessen (ABK, j = ½); die Punktierungen werden als selbstähnliches Gebilde auf dem Horizont
  gelesen; „maximal“ ist gesetzt. Warum der Horizont ein solches Gebilde tragen soll, ist offen.
- **Abhängigkeit vom Spektrum:** Mit j + ½ gibt w = 2 genau D = 2 (Grenzfall), linear gibt w = 3 genau D = 2; eindeutig ist das Prinzip nur mit √(j(j+1)).
- Moran, Mauldin–Urbański und Moon–Moser sind Vorwissen, hier nicht nachgelesen.
- Ein blinder Test bräuchte eine Folgerung, die noch nicht feststeht, etwa die Dimension 1,8647 als messbare Skalierung an anderer Stelle. Nicht festgelegt.
- OP1 offen; die Regel ist umformuliert und durch ein Prinzip gestützt, nicht hergeleitet.

## Ergebnis in einem Satz
Die Zählgleichung ist exakt eine Moran-Gleichung, die Frame-Faktoren sind Hausdorff-Dimensionen (T 1, M 1,8647, P 2,1515), und die Regel von M ist die
größte ganze Kopienzahl je SU(2)-Skala, deren Fraktal noch auf eine Fläche passt; die volle SU(2)-Zählung passt nicht. Lesart, nicht blind. OP1 offen.
