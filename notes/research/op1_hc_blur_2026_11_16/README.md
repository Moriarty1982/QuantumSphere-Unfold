# OP1: Verwischte HC-Auslesung und Gegen-HC (Erkundung, analytisch, nicht blind)

16. November 2026. Zwei Ideen des Autors: (1) „Was ist, wenn der Materie-Frame doch mehr ausliest, aber heimlich Sachen verwischt?“ (2) „In unserem Frame
gilt die Unschärferelation; der HC teilt sie in berechenbare Werte auf, aber vielleicht brauchen wir in gewissen Frames oder beim Wechseln, Vergleichen
oder Anpassen einen Gegen-HC, der den ersten wieder rückgängig macht, sobald wir messen.“ Skript `hc_blur.py`, Ausgabe `run/hc_blur_stdout.txt`. Keine
H-Nummer, kein Zielwertvergleich (die γ-Werte sind die bekannten Zählwerte).

## Vorwissen geprüft
- `../qam_hc_flaechenquantum_2026_11_07.md`, „Gemeinsame Form der M- und T-Zählmasken“: Die M-Maske P_M(u) = 1{J² − J_u² − |J_u| = 0} braucht eine Achse u;
  „über alle Achsen gemittelt … Spur bleibt zwei … 2I/(2j+1)“, „kein scharfer zweidimensionaler Unterraum“. Dort als Nachteil verbucht.
- v4.9.0-r63.2 (Unschärfesättigung genau bei m = ±j), r68.3/r68.4 (U(1)- gegen SU(2)-Zählung), `../op1_counting_rule_data_2026_11_16/`,
  `../op1_u1_check_2026_11_16/`, `../op1_s1_check_2026_11_16/` (ABK: Achse = Horizontnormale, internes Feld r vom Grad 1).
- v470/09 und Konvention F: HC als Kompensator-Projektor C = ½(1 + J) mit Kompensator- und Partner-Port.

## 1. Verwischen: mehr auslesen, Richtung verwischen
Die HC-Maske wählt längs einer Achse die Zustände m = ±j. Mittelt man sie über alle Achsen (Haar-Mittel, 4000 Drehungen), wird sie voll drehinvariant:

| j | Spur der Maske | gemittelte Maske | Annahmewahrscheinlichkeit 2/(2j+1) |
|---|---|---|---|
| ½ | 2 | 1,000 · I | 1 |
| 1 | 2 | 0,667 · I | 0,667 |
| 3/2 | 2 | 0,500 · I | 0,500 |
| 2 | 2 | 0,400 · I | 0,400 |
| 3 | 2 | 0,286 · I | 0,286 |

**Die verwischte Auslesung ist SU(2)-invariant und hat das Zählgewicht 2 je Spin; daraus folgt γ = 0,237533**, der Wert des Frames M, ohne
Eichfixierung. Der Frame „liest“ dabei den ganzen Spin, verwischt aber die Richtung. Damit ist der Haupteinwand der Literatur (die U(1) sei nur eine
Eichfixierung) entkräftet: Das Gewicht 2 ist mit voller Drehinvarianz verträglich.

**Preis:** Gezählt werden keine scharf unterscheidbaren Zustände mehr, sondern die Spur einer unscharfen Auslesung (Annahmewahrscheinlichkeiten). Die
Literatur (SU(2), Engle–Noui–Perez) zählt orthogonale Zustände und kommt auf 0,274. Die offene Frage wird damit genauer: Ist die Horizontentropie des
Frames M eine Zustandszahl oder die Spur einer unscharfen Auslesung?

## 2. Unschärfe, HC und Gegen-HC
Nach r63.2 (nachgerechnet bis j = 3) sättigen genau die Zustände m = ±j die Robertson-Schranke ΔJ_x·ΔJ_y ≥ |m|/2. Der HC teilt jede Punktierung in den
**unschärfeminimalen Teil** (m = ±j, 2 Zustände) und den **Rest** (|m| < j, 2j − 1 Zustände). Für einen Gegen-HC gibt es zwei Formen:

| Gegen-HC | Wirkung | Zählgewicht | γ |
|---|---|---|---|
| Komplement (Partner-Port statt Kompensator-Port) | holt den Rest dazu; HC + Gegen-HC = alles | 2j + 1 | 0,274067 (SU(2)) |
| Verwischen der Achse | hebt die Achsenwahl auf, behält das Gewicht | 2, drehinvariant | 0,237533 |
| (Rest allein, zum Vergleich) | | 2j − 1 | 0,182486 |

**Lesart (nicht hergeleitet):** Der Satz des Autors („macht den ersten wieder rückgängig, sobald wir messen“) passt zur zweiten Form. Der HC hat im
eigenen Rahmen eine scharfe Achse und wählt die unschärfeminimalen Zustände; wer die Achse nicht kennt, sieht dieselbe Auslesung verwischt. Das
Zählgewicht bleibt in beiden Ansichten 2, die Unschärferelation bleibt unangetastet.

## 3. Woher das Verwischen kommen könnte (Abgleich mit dem Bestand)
- **Nicht aus dem Vergleich M ↔ T.** Nach Konvention F sind M und T über dieselbe Port-Achse definiert (T ist das J_B-Bild mit getauschten Ports). Ihre
  Achsen sind gleich (umgekehrt), also nicht unbekannt zueinander. Ein Verwischen beim Vergleich der beiden Frames ist damit ausgeschlossen.
- **Möglich aus der Horizontgeometrie (Lesart).** In ABK ist die Achse an jeder Punktierung die Normale, gegeben durch ein internes Feld r vom Grad 1:
  Über den ganzen Horizont überdeckt die Normale jede Richtung genau einmal. Eine Auslesung mit fester innerer Achse sieht die Punktierungen dann unter
  allen relativen Richtungen. Sind die Punktierungen gleichmäßig über den Horizont verteilt, ist das genau das Mittel über alle Achsen von Abschnitt 1.
  Ob die Punktierungen gleichmäßig verteilt sind und ob die Auslesung von M eine feste innere Achse hat, ist nicht geprüft.

## Ergebnis
1. Ein Zählgewicht 2 je Spin (also γ_M = 0,2375) ist mit voller Drehinvarianz verträglich, wenn die Auslesung die Achse verwischt. Der Einwand
   „U(1) = Eichfixierung“ trifft dann nicht.
2. Der HC wählt die unschärfeminimalen Zustände (r63.2). Ein Gegen-HC als Komplement führt zum SU(2)-Wert 0,274; ein Gegen-HC als Verwischen behält 0,2375.
3. Das Verwischen kann nicht aus dem Vergleich M ↔ T kommen (gemeinsame Port-Achse), möglicherweise aber aus der Horizontgeometrie (Normale vom Grad 1).
4. Offen bleibt, warum M das Gewicht 2 hat und nicht 2j + 1; neu ist die genauere Form: Zustandszahl oder Spur einer unscharfen Auslesung.

OP1 offen; H98, H102 unverändert.
