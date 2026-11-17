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

## Nachtrag (17.11.2026): Die Dimensionsleiter T, M, P
Auftrag des Autors: „weiter“ (blinden Test zur Moran-Lesart suchen). Skript `dimension_ladder.py`, Ausgabe `run/dimension_ladder_stdout.txt`.
**Nicht blind:** Die Fälle d = 1 und d = 3 waren vor der Rechnung überschlagen.

Im Regelraum S von H98 (Spinbereiche alle, halbzahlig, ganzzahlig, nur ½, nur 1; Gewichte 2, 2j + 1), Spektrum √(j(j+1)), ist die Regel mit der
größten Moran-Dimension unter denen, die in ℝ^d passen (Σ g r^d ≤ 1):

| d | Regel | D | Σ g r^d | Frame |
|---|---|---|---|---|
| 1 | nur j = ½, Gewicht 2 | 1 | 1 (die zwei Hälften füllen die Strecke genau) | **T** |
| 2 | alle Spins, Gewicht 2 | 1,8647 | 0,869 | **M** |
| 3 | alle Spins, Gewicht 2j + 1 | 2,1515 | 0,410 | **P** |

**Lesart:** Die drei Frames sind die reichsten selbstähnlichen Auslesungen auf einer Linie, einer Fläche und im Raum. Das passt zum Bestand: T zählt
Querungen, also einzelne Stränge (r24.4); M zählt auf der Horizontfläche; P zählt alle 2j + 1 Zustände und liegt außerhalb der Fläche (eigener HC,
`../op1_hc_blur_2026_11_16/`). Die geschachtelte Zählung T ⊆ M ⊆ P wird zur Folge von Dimensionen 1 ⊂ 2 ⊂ 3.

**Grenzen.**
- Die Leiter gilt im Regelraum S. Mit beliebigen konstanten Kopienzahlen über alle Spins gäbe d = 3 fünf Kopien (D = 2,83), nicht P; d = 1 hätte dann
  keine Regel über alle Spins (Σ r = 1,46 > 1).
- Spannung zu `../op1_flux_lines_2026_11_17/`: Dort liegen die statischen Felder eines Horizonts im Gleichgewicht in der Lage von P. Die Leiter liest P
  als Raum- statt Flächenauslesung. Beides zugleich verlangt, dass der Gleichgewichtshorizont nicht als Fläche, sondern als Volumen ausgelesen wird; das
  ist offen.

**Blinder Test.** Rückwärtssuche: Gesucht war eine Folgerung, die (a) ohne freien Parameter aus der Leiter folgt, (b) keine der schon verwendeten
Größen ist (γ_L, β_sym, Ω_M, m_W, m_τ) und (c) mit Daten verglichen werden kann. Die Leiter legt nur die drei bekannten Regeln fest; jenseits von d = 3
bleibt sie bei P, eine vierte Stufe gibt es in S nicht. Ein blinder Test ist aus der Moran-Lesart allein **nicht** zu gewinnen; sie ist eine
Strukturaussage über bekannte Zahlen. Ein Test bräuchte einen neuen Sektor mit eigener Zählung (etwa eine Farb- oder Quarkauslesung); das wäre eine
neue Setzung. OP1 offen.

## Nachtrag (17.11.2026): Die Spannung zu P aufgelöst
Auftrag des Autors: „Spannung zu P klären“. Skript `register_threshold.py`, Ausgabe `run/register_threshold_stdout.txt`. Erkundung ohne Zielwert.

**Die beiden Bedeutungen von P.** (a) Flusslinien-Notiz: Ein statisches, reelles Feld liegt auf dem χ-Äquator, also in der Registerlage von P (b = 0).
(b) Dimensionsleiter: P ist die Zählregel 2j + 1 mit D = 2,15, die nur im Raum Platz hat. Verbunden sind beide über das Registermodell
(`../op1_entropy_count_2026_11_17/`): Ein Bündel im Register b = 0 zählt genau 2j + 1.

**Rechnung: Ab welcher Sichtbarkeit b passt die Registerzählung auf eine Fläche?**

| Zählung | Σ N r² bei b = 0 | bei b_M = 0,5363 | bei b = 1 | Schwelle b_c (Σ N r² = 1) | D bei b_M |
|---|---|---|---|---|---|
| Register allein, Shannon | 1,199 | 0,837 | 0,435 | 0,347 | 1,838 |
| Register allein, Beteiligung | 1,199 | 0,721 | 0,435 | 0,254 | 1,700 |
| Mischung mit Spiegel (unbekannter Port), Shannon | 1,199 | 1,117 | 0,869 | 0,800 | 2,097 |
| Mischung mit Spiegel, Beteiligung | 1,199 | 1,074 | 0,869 | 0,693 | 2,064 |

**Auflösung.**
1. **Kein Widerspruch, sondern eine gemeinsame Aussage:** Mit b = 0 passt keine Registerzählung auf eine Fläche. Ein statischer Horizont, der seine
   Punktierungen über ihr eigenes Register zählt, ist deshalb **keine Flächenauslesung**, sondern eine Raumauslesung (P, D = 2,15). Die Flusslinien-Notiz
   (statische Felder liegen bei P) und die Leiter (P ist die Raumstufe) sagen dasselbe.
2. **Fläche verlangt Frequenz:** Auf eine Fläche passt die Registerzählung erst ab b > b_c > 0 (0,25 bis 0,35 für das Register allein). Eine Breite b ≠ 0
   gibt es nach `../op1_flux_lines_2026_11_17/` (Nachtrag) nur mit relativen Phasen, also bei Frequenz ω > 0. Die drei Notizen fügen sich damit zu einer
   Kette: **Flächenauslesung ⇒ b > b_c ⇒ Frequenz ⇒ nicht statisch.** Die Zählregel von M ist die Flächenstufe und setzt eine zeitharmonische
   Auslesung voraus; der statische Gleichgewichtshorizont liest wie P.
3. **Die Regel von M ist nicht das Register von M:** Das Register bei b_M allein gibt D = 1,838 (Shannon), 1,4 % unter γ_L (wie schon in der
   Entropie-Notiz, γ = 0,2342 statt 0,2375); die Mischung des M-Registers mit seinem Spiegel passt nicht auf die Fläche (1,117). Nur reine Stränge mit
   unbekanntem Port (b = 1, gemischt) geben genau Gewicht 2 und passen (0,869). Das bestätigt die Lesart „M zählt reine Stränge mit unbekanntem Port“.
4. Keine Schwelle b_c fällt auf b_M; behauptet wird kein Treffer.

**Was offen bleibt:** warum die Flächenauslesung M reine Stränge mit Frequenz sieht, während der statische Horizont wie P liest. Damit ist OP1 an
derselben Stelle wie nach der Auslesefrequenz: Woher kommt die Frequenz der Auslesung M? OP1 offen.

## Nachtrag (17.11.2026, nach `../op1_two_readings_2026_11_17/`): nur unter Lesart (H)
Die Folgerung, die Breite von M verlange eine Frequenz, nimmt die Registerbreite b als Helizitätsbreite (Lesart H). Der Test beider Lesarten zeigt,
dass Konvention F nur in der Beobachterlesart (B), φ = sech 2η, widerspruchsfrei ist (r21.8: R ist ein reelles Feld mit E ∥ B und φ = 1). Unter (B)
erreichen auch statische Felder die Breite b_M (Beobachter mit Rapidität η), und die Frequenzbedingung entfällt. Die Rechnungen dieser Notiz bleiben
richtig; ihre Deutung für das Register von M gilt nur unter (H).
