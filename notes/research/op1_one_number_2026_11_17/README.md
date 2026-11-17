# OP1: Eine Zahl in sechs Gestalten, und woher die Frequenz von M kommt (Erkundung, Zusammenstellung, nicht blind)

17. November 2026. Auftrag des Autors: „weiter“ nach PR #171 (offene Kernfrage: woher kommt die Frequenz der Auslesung M?). Skript `one_number.py`,
Ausgabe `run/one_number_stdout.txt`. Keine neue Rechnung im engeren Sinn; geprüft wird, dass alle Formen numerisch dieselbe Zahl sind, und es wird
gekennzeichnet, welche Gleichheit Definition, Satz oder Lesart ist. Keine H-Nummer.

## Vorwissen geprüft
r11.5(b) (γ_L als Lorentz-Faktor zweier flussentgegengesetzter Beobachter; ausdrücklich keine Gleichsetzung mit M und T), r17 (γ_L = 1/|b|),
`../op1_readout_frequency_2026_11_17/` (ω_M/ω_T = γ_L), `../op1_moran_geometry_2026_11_17/` (Moran, Dimensionsleiter, Spannung zu P),
`../op1_flux_lines_2026_11_17/` (Breite verlangt Frequenz).

## Die Zahl γ_L = 1,864699765 in sechs Gestalten

| Nr. | Gestalt | Art der Gleichheit | Quelle |
|---|---|---|---|
| 1 | γ_M/γ_T, Verhältnis der Zählparameter | Definition | r08–r10, H98 |
| 2 | Hausdorff-Dimension D_M des M-Fraktals | Satz (Moran-Gleichung, offene-Mengen-Bedingung nachgewiesen) | PR #170 |
| 3 | ω_M/ω_T, Verhältnis der Bohr-Frequenzen der kleinsten Schritte | Identität unter der Bohr-Lesart | PR #168 |
| 4 | cosh 2η mit β_sym = tanh η | Definition von η | r63, r68 |
| 5 | 1/b_M, Kehrwert der Registerbreite von M | Identität in Konvention F | r17, r22 |
| 6 | Lorentz-Faktor zwischen zwei flussentgegengesetzten Beobachtern | Lesart (Kinematik exakt, Zuordnung zu M und T nicht) | r11.5(b) |

Alle sechs Formen geben numerisch 1,864699765 (Skript).

## Woher die Frequenz von M kommt (Lesart)
Setzt man (3) und (6) zusammen: Das Bit-Quant von T hat die Energie ω_T = ln 2 · T_H (Bekenstein-Bit bei der Hawking-Temperatur, in jedem Spektrum,
PR #168). Ein Beobachter, der sich relativ zu T mit der Rapidität 2η bewegt, sieht dieses Quant mit der Energie

  γ_L · ln 2 · T_H = 1,2925 · T_H = ω_M.

**Die Frequenz von M ist danach keine eigene Horizontfrequenz, sondern die Bit-Frequenz von T, gesehen vom Gegenbeobachter.** Das erklärt, warum die
Quellensuche unter den Frequenzen eines ruhenden Schwarzschild-Horizonts (16 Kandidaten, 0 Treffer, PR #168) leer bleiben musste: Gesucht war eine
Ruhefrequenz, gefunden wird eine geboostete. Und es passt zu den Nachträgen der letzten Stunden: Die Flächenauslesung braucht eine Frequenz und kann nicht
statisch sein (PR #171); ein Beobachter in Bewegung relativ zum statischen Horizont liefert genau das.

## Was damit geschlossen ist und was nicht
- **Geschlossen (als Lesart):** Die drei Fragen „welche Frequenz“, „welche Breite“ und „welcher Frame-Faktor“ sind eine Frage. Wer eine der sechs Formen
  begründet, begründet alle.
- **Einziger parameterfreier Festleger bisher:** das Moran-Prinzip (größte ganze Kopienzahl je SU(2)-Skala, die auf eine Fläche passt, gibt 2 und damit
  D_M = γ_L). Es ist nachträglich formuliert.
- **Offen:** (a) die Gleichsetzung des flussentgegengesetzten Beobachterpaars aus r11.5(b) mit T und M; der Bestand hat sie ausdrücklich nicht. Erst mit
  ihr wäre (6) mehr als eine Lesart. (b) Warum ein Beobachter in M sich relativ zu T gerade mit der Rapidität bewegt, die das Moran-Prinzip fordert.
  (c) Ein blinder Test; keine der sechs Formen liefert eine noch unbekannte Zahl.
- Nicht blind; alle Gleichheiten außer (2) und (6) sind Definitionen oder Identitäten. OP1 offen.

## Ergebnis in einem Satz
Frame-Faktor, Moran-Dimension, Frequenzverhältnis, Lorentz-Faktor und Registerbreite sind dieselbe Zahl; liest man sie als Lorentz-Faktor des
flussentgegengesetzten Beobachterpaars, ist die Frequenz von M die Bit-Frequenz von T, vom Gegenbeobachter gesehen. Fehlt noch: die Zuordnung des Paars zu
M und T. OP1 offen.
