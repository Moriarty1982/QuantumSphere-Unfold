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

## Nachtrag (17.11.2026): Das Beobachterpaar ist nicht (M, T); die Boost-Lesart der Frequenz wird zurückgenommen
Auftrag des Autors: „Paar M und T prüfen“. Skript `pair_check.py`, Ausgabe `run/pair_check_stdout.txt`. Analytisch vorher entschieden, nachgerechnet.

| Prüfung | Ergebnis |
|---|---|
| (1) Ein Boost lässt s = (E + iB)² fest | Abweichung 7,7·10⁻¹⁴ (500 Felder, beliebige Richtungen) |
| Frame-Abbildungen auf s | R: −s; T-Abbildung: s̄; J_B: −s̄. Der T-Frame ist in Konvention F das J_B-Bild von M: Materiefeld s = 1 → s = −1 (Tachyonseite) |
| (2) Paar aus r11.5(b): vom flussfreien Profil R um +η und −η | beide r = 0,5363 = b_M, Fluss entgegengesetzt (±0,787), gleiches s; Feld des einen = Drehung um π des anderen |
| relativer Lorentz-Faktor des Paars | cosh 2η = 1,864701 = γ_L |
| (3) Energiedichte u(M)/u(R) | cosh 2η = γ_L |
| T-Abbildung (E, −B) auf Feldern mit E·B = 0 | gleich einer Drehung um π um E |
| (4) imaginäre Verschiebung η → η + iπ/2 | x = 0,3018 → 3,3129 = 1/x (Tachyon-Ast, Konvention F) |

**Ergebnis.**
1. **Das Paar ist (M, M̄), nicht (M, T).** Ein reeller Boost erhält s; der T-Frame verlangt s ↦ −s̄ (Materie → Tachyon). Zwischen M und T liegt die
   imaginäre Verschiebung iπ/2, keine reelle Rapidität. Das bestätigt die Lage von T in `../op1_hc_blur_2026_11_16/` (Nachtrag Lage von P) und Konvention F.
2. **Warum das Beispiel in r11.5(b) wie T aussah:** Auf Feldern mit E·B = 0 ist die T-*Abbildung* (E, −B) eine Drehung um π um E. Die beiden
   Beobachter sehen also gedrehte Kopien desselben Felds; der T-*Frame* (J_B-Bild) ist damit nicht erreicht. r11.5(b) hatte die Gleichsetzung zu Recht offen
   gelassen; sie fällt.
3. **Gestalt (6) in der Tabelle oben** gilt für das Paar (M, M̄): γ_L ist ihr gegenseitiger Lorentz-Faktor und das Verhältnis der Energiedichten
   zwischen M und dem flussfreien Profil R. Sie sagt nichts über M gegen T.
4. **Die Lesart „Frequenz von M = Bit-Frequenz von T, vom Gegenbeobachter gesehen“ ist zurückgenommen.** Übrig bleibt ω_M/ω_T = γ_L als Identität der
   Bohr-Lesart und γ_L = u(M)/u(R) als Kinematik. Beide zusammen ergäben eine Boost-Lesart nur, wenn die Bit-Frequenz von T die Ruhefrequenz in R wäre;
   T und R sind aber verschiedene Frames (R flussfrei mit b = 1, T auf dem imaginären Ast mit |b| = b_M). Dafür gibt es keinen Grund im Bestand.

**Stand der Frage nach der Frequenz von M:** wieder offen. Gesichert ist: Sie ist γ_L · ln 2 · T_H (Bohr-Lesart), sie ist keine Ruhefrequenz eines
Schwarzschild-Horizonts (16 Kandidaten), und sie entsteht nicht durch einen reellen Boost aus der T-Frequenz. OP1 offen.
