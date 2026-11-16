# OP1: Folgt die Zählung je Frame aus der Register-Entropie? (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „Zählung aus Entropie prüfen“, nach `../op1_hc_blur_2026_11_16/` (Nachtrag Lage von P: Auf dem reellen Ast
R → M → P wächst die Zählung mit der Register-Entropie). Skript `entropy_count.py`, Ausgabe `run/entropy_count_stdout.txt`. Nicht blind: Die Zählgewichte
und γ-Werte sind bekannt. Keine H-Nummer.

## Vorwissen geprüft
- Konvention F (r22): Registerzustand je Frame, Sichtbarkeit |b| (R 1, M 0,5363, P 0), Entropie (M 0,781 bit, P 1 bit).
- r17.5, (S1): eine Punktierung mit Spin j ist ein Bündel aus 2j Strängen, jeder ein χ-Qubit.
- r63/r09/r10: M Gewicht 2 je j, T nur j = ½, P bisher ohne Zählung; Vorschlag P = alle 2j + 1 (`../op1_hc_blur_2026_11_16/`).

## Modell
Jeder der 2j Stränge einer Punktierung ist im Registerzustand des Frames, ρ(b) = ½(1 + b σ_z). Das Bündel liegt im symmetrischen Unterraum (Spin j);
das Gewicht des Zustands |j, m⟩ ist dann p₊^(j+m) p₋^(j−m), also eine geometrische Verteilung mit Quotient x = p₋/p₊ = β². Als effektive Zustandszahl
je Punktierung dienen 2^H (Shannon) und die Beteiligung 1/Σw².

## Ergebnis

| j | R (b = 1) | M (b = 0,536): Shannon / Beteiligung | P (b = 0) | Regel M / Vorschlag P |
|---|---|---|---|---|
| ½ | 1 | 1,72 / 1,55 | 2 | 2 / 2 |
| 1 | 1 | 2,11 / 1,77 | 3 | 2 / 3 |
| 2 | 1 | 2,36 / 1,86 | 5 | 2 / 5 |
| 5 | 1 | 2,40 / 1,865 | 11 | 2 / 11 |
| 10 | 1 | 2,40 / 1,865 | 21 | 2 / 21 |

1. **Für P folgt die Zählung exakt aus dem Register.** Der Photonpunkt ist maximal gemischt (I/2); das Bündel verteilt sich gleichmäßig auf alle 2j + 1
   Zustände. Daraus folgt γ_P = 0,274067, genau die dritte Zählart. Der Vorschlag „P zählt alles“ ist damit nicht nur aus F2 motiviert, sondern aus dem
   Registerzustand von P hergeleitet (unter (S1)).
2. **Für R folgt eine Zählung von 1 je Spin** (reiner Zustand: nur m = +j).
3. **Für M folgt die Regel nicht.** Das Register von M gibt eine vom Spin abhängige Zahl, die gegen 2,40 (Shannon) bzw. 1,865 (Beteiligung) strebt, nicht
   die konstante 2. Mit der Shannon-Zahl käme γ = 0,2342 heraus statt 0,2375 (1,4 % daneben; nachträglich, kein Befund). Nebenbei: Die Beteiligung strebt
   für großes j gegen (1 + x)/(1 − x) = γ = 1,8647, den Frame-Faktor; das ist eine algebraische Identität der geometrischen Verteilung, kein Zufall und
   keine neue Aussage.
4. **Die Regel von M entspricht reinen Strängen mit unbekanntem Port.** Die gleichgewichtete Mischung aus dem reinen Zustand (b = 1) und seinem Spiegel
   (b = −1) gibt genau 2 Zustände je Spin (1 bit je Punktierung) und damit γ = 0,237533. Mischt man dagegen das Register von M mit seinem Spiegel, wächst
   die Zahl mit j. Die Zählung von M liest sich also wie die Zählung reiner R-Zustände, deren Vorzeichen (Kompensator- oder Partner-Port) unbekannt ist,
   nicht wie die Zählung des M-Registers.

## Einordnung
- Auf dem reellen Ast stimmt die Zählung nur an den Enden mit dem Register überein: R (rein) gibt 1, P (maximal gemischt) gibt 2j + 1. Dazwischen gibt das
  M-Register keine konstante Zahl.
- Die Regel „M zählt 2 je Spin“ ist gleichwertig mit „M zählt reine Bündel mit unbekanntem Port“: ein Bit je Punktierung, unabhängig von j. Das passt zu
  den früheren Lesarten (Extremdublett der Port-Auslesung, r24.2; unschärfeminimale Zustände, r63.2) und zum Bild, dass M in R ausgelesen wird
  (`../op1_r_readout_precheck_2026_11_16/`), aber es leitet die 2 nicht aus der Entropie des M-Registers her.

## Ergebnis in einem Satz
Die Register-Entropie erklärt die Zählung von P (alle 2j + 1, exakt) und von R (1), nicht die von M; die Regel von M entspricht reinen Strängen mit
unbekanntem Port. OP1 offen.
