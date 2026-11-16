# Suche nach einem blinden Test für die Querungs-Lesart (OP1, r24.4)

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind**, ohne Kriterium. Auftrag des Autors: „Ja, Test suchen“. **Keine
H-Nummer vergeben (H105 bleibt frei)**, keine Vorab-Notiz, Guards unverändert. Skript `crossing_lines.py`, Ausgabe
`run/crossing_lines_stdout.txt`.

## Vorgehen
Gesucht ist eine Folge der Lesart „T zählt Querungen des Horizonts, eine Querung trägt einen Strang“ (v4.10.0-r24.4), die nicht γ_L
ist, eine noch nicht gemessene Größe festlegt und ohne neue freie Wahl auskommt. Erst dann wäre eine Vorab-Notiz sinnvoll.

**Vorwissen:** Die letzte Testsuche (`../blind_test_search_2026_11_15/README.md`, r18.1) fand keinen Test; frame-abhängige
logarithmische Entropiekorrekturen hielt sie für nicht messbar. Offene Vorhersagen: H9, H15, H42, H46, H96, H100, H102, H2. Hawking-
Strahlung kommt in keiner Vorab-Notiz vor.

## Die Folge: gleich große Flächenschritte
Trägt eine Querung genau einen Strang mit j = ½ und zählt T mit γ_T = ln 2/(π√3), dann ist der Flächenschritt einer Querung
a = 8πγ_T √(¾) l_P² = **4 ln 2 · l_P²** (nachgerechnet). Gleich große Schritte sind das **Bekenstein–Mukhanov-Spektrum** mit
α = 4 ln 2, also dem Wert für zwei Zustände je Quant. Für ein Schwarzschild-Loch liegen die Übergänge dann bei Vielfachen von
ω₀ = α/(32πM) = ln 2 · T_H.

Zum Vergleich die M-Regel (alle j, Gewicht 2, γ_M): Die Flächenquanten 8πγ_M √(j(j+1)) stehen nicht in rationalem Verhältnis, ihre
Summen liegen dicht. M allein gibt keine Linien, wie in der üblichen Schleifenquantengravitation.

## Was man messen könnte
Ein Loch, das nur in solchen Schritten Energie aufnimmt, kann eine Gravitationswelle zwischen zwei Linien nicht absorbieren; dann
erwartet man **Echos** im Ringdown. Lage des Grundtons (l = m = 2) zwischen den Linien:

| Endspin a | M ω₂₂₀ | Linienabstand M Δω | Lage n | Abstand zur nächsten Linie |
|---|---|---|---|---|
| 0 (genau 0,37367) | 0,3737 | 0,02758 | 13,55 | 0,45 Abstände |
| 0,5 | 0,4674 | 0,02560 | 7,79 | 0,21 |
| 0,69 (typisch nach Verschmelzung) | 0,5307 | 0,02316 | 5,63 | 0,37 |
| 0,8 | 0,5855 | 0,02068 | 4,13 | 0,13 |
| 0,9 | 0,6660 | 0,01674 | 2,34 | 0,34 |

(Die Kerr-Zeilen nutzen eine Näherungsformel für ω₂₂₀; bei a = 0 weicht sie um 1,5 % vom genauen Wert ab.)

**Literatur** (gefunden über alphaXiv, Ergebnisse nicht im Einzelnen nachgelesen): Echos aus Flächenquantisierung werden für
LIGO–Virgo und LISA untersucht (z. B. arXiv:2411.05645, LISA; arXiv:2609.14160, „Quantum black hole ringdown“, 2026). Eine Arbeit
argumentiert, dass Bekenstein–Mukhanov gar keine messbaren Echos erzeugt (arXiv:2201.03245). Bestätigte Echos gibt es nicht.

## Warum das kein blinder Test ist
1. **Neue Wahl nötig.** Die Lesart sagt, T zähle Querungen; sie sagt nicht, welche. Zwei Fassungen:
   - **(V1)** Jede Querung des Horizonts ist ein T-Quant, auch die einfallende Gravitationswelle. Dann gilt das Linienspektrum auch für
     die Absorption, und Echos wären zu erwarten.
   - **(V2)** Nur die einfallenden Partner der Hawking-Paare (negative Energie, `thm:hawking-triolic`, r64(e)) sind T-Querungen; was
     von außen einfällt, nimmt das Loch über M auf, also dicht. Dann gibt es Linien nur in der Hawking-Emission, die nicht messbar ist.

   Welche Fassung gilt, legt der Bestand nicht fest. (V1) zu wählen, um einen Test zu bekommen, wäre genau die freie Wahl, die ein
   blinder Test ausschließt.
2. **Ob es Echos gibt, ist selbst umstritten.** Die Linienbreite ist der Knackpunkt: Der Grundton hat bei a = 0 eine Dämpfung von
   M |Im ω| ≈ 0,089, gut dreimal der Linienabstand. Ob Linien, die so dicht liegen, die Absorption sperren, hängt von der Breite der
   Übergänge selbst ab; das wird in der Literatur gegensätzlich beurteilt (arXiv:2201.03245).
3. **Nicht projektspezifisch.** α = 4 ln 2 folgt aus jeder Zählung, die nur j = ½-Punktierungen kennt (ABCK). Ein Echo-Befund mit
   α = 4 ln 2 würde die Minimal-Spin-Zählung stützen, nicht die Querungs-Lesart im Besonderen.

## Ergebnis
**Kein blinder Test gefunden.** Die Querungs-Lesart hat eine messbare Folge, gleich große Flächenschritte von 4 ln 2 l_P² mit Echos im
Ringdown, aber nur in der Fassung (V1). Diese Fassung ist eine neue Wahl, ihre Beobachtbarkeit ist in der Literatur umstritten, und der
Wert ist nicht projektspezifisch. In der Fassung (V2) bleibt nur die nicht messbare Hawking-Emission.

**Mögliche Entscheidung des Autors:** Wird (V1) als Teil der Lesart gesetzt, ließe sich ein Test mit Frist formulieren (Echo-Suchen der
nächsten LVK-Läufe oder LISA, Vorab-Notiz mit H105). Er wäre dann offen als „unter Setzung (V1)“ zu führen.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
