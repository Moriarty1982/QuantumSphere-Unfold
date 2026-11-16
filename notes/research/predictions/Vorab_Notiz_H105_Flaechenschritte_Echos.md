# Vorab-Notiz H105: Gleich große Flächenschritte 4 ln 2 · l_P² und Echos im Ringdown (unter Setzung V1)

Festgelegt am 2026-11-16, **vor** jeder Auswertung von Daten zu dieser Frage. Auftrag des Autors: „V1 setzen, Test“. Einordnung OP1, T6,
v4.10.0-r24.4. Skript `k227_test_h105.py` (wird nach dieser Notiz geschrieben; es berechnet nur die Vorhersage, keine Daten).

## Offenlegung vorab
- **Unter einer Setzung.** Der Test gilt der Querungs-Lesart (r24.4) **mit der Setzung V1**: Jede Querung des Horizonts ist ein T-Quant,
  auch was von außen einfällt (Gravitationswellen eingeschlossen). V1 hat der Autor am 16.11.2026 gesetzt, nachdem die Testsuche
  (`../op1_crossing_test_search_2026_11_16/README.md`) gezeigt hatte, dass nur V1 eine messbare Folge hat. V1 ist damit eine Wahl, die
  den Test erst möglich macht; das wird hier offen gesagt. Die Gegenfassung V2 (nur Hawking-Partner sind T-Querungen) bleibt vom Test
  unberührt.
- **Nicht projektspezifisch.** Der vorhergesagte Wert α = 4 ln 2 folgt aus jeder Zählung, die nur j = ½-Punktierungen kennt (ABCK). Ein
  positiver Befund stützt die Minimal-Spin-Zählung für Querungen, nicht die Querungs-Lesart allein.
- **Beobachtbarkeit umstritten.** Ob Bekenstein–Mukhanov-Quantisierung überhaupt messbare Echos erzeugt, wird in der Literatur
  gegensätzlich beurteilt (z. B. arXiv:2201.03245 dagegen). Das ist im Kriterium als eigener Ausgang berücksichtigt.
- **Blind gegenüber Daten:** Bis zu dieser Notiz sind nur Kurzfassungen von Arbeiten zu Echos aus Flächenquantisierung gesehen worden
  (arXiv:2411.05645, 2609.14160, 2201.03245); keine Ergebnisse zu α = 4 ln 2. Bereits vor dieser Notiz erschienene Analysen zählen für das
  Urteil **nicht** (siehe Datenumfang).

## Vorwissen geprüft
- `Ergebnis_H98_Zaehlregel_Sonderstellung.md`, `Ergebnis_H104_Zaehlregel_Flaechenspektren.md`: Zählregel M alle Spins (g = 2), T nur j = ½;
  γ_T = ln 2/(π√3); Sonderstellung hängt am Spektrum a(j) = √(j(j+1)).
- `../op1_statistics_backward_2026_11_16/`, `../op1_i1_crossing_2026_11_16/` (r24): T zählt Querungen, eine Querung ein Strang.
- `../op1_crossing_test_search_2026_11_16/`: Folge der Querungs-Lesart; V1 gegen V2; Linienlagen für typische Endspins.
- `../blind_test_search_2026_11_15/`: frühere Suche ohne Test; keine Vorab-Notiz zu Hawking-Strahlung oder Echos im Repo.
- Offene Vorhersagen H2, H9, H15, H42, H46, H96, H100, H102 betreffen andere Größen.

## Vorhersage
Unter r24.4 mit V1 und (S1) ändert jede Querung die Horizontfläche um genau
  ΔA = 8π γ_T √(¾) · l_P² = **4 ln 2 · l_P²**,
also Bekenstein–Mukhanov-Quantisierung mit **α = 4 ln 2 ≈ 2,7726**. Ein Kerr-Loch mit Masse M, Spin a nimmt Energie dann nur bei
  ω_n = n · α κ/(8π) + m Ω_H = n · (ln 2/(2π)) κ + m Ω_H
auf (κ Oberflächengravitation, Ω_H Winkelgeschwindigkeit des Horizonts, n ganz). Liegt der Grundton (l = m = 2) zwischen zwei Linien,
wird er nicht absorbiert, und es sind **Echos nach dem Ringdown** zu erwarten, mit den Linienabständen, die `k227_test_h105.py` für jedes
Ereignis aus M und a berechnet.

## Datenumfang
- Zählt: jede auf arXiv oder in einer Fachzeitschrift **nach dem Commit dieser Notiz** erschienene Analyse von Gravitationswellendaten
  (LIGO–Virgo–KAGRA oder unabhängig, später LISA), die Bekenstein–Mukhanov-Flächenquantisierung oder daraus folgende Echos ausdrücklich
  prüft und ein Ergebnis für α = 4 ln 2 angibt oder für einen Bereich von α, der 4 ln 2 enthält.
- Zählt nicht: Analysen, die vor dem Commit dieser Notiz erschienen sind; allgemeine Echo-Suchen ohne Bezug auf Flächenquantisierung;
  reine Prognosen ohne Daten.
- **Frist:** 31.12.2028.

## Entscheidungskriterium (vor der Auswertung festgelegt)
- **bestätigt**, wenn eine zählende Analyse Belege für Echos oder Absorptionslinien angibt, die mit α = 4 ln 2 verträglich sind, mit
  Bayes-Faktor ≥ 10 gegen das Modell ohne Quantisierung oder mit Signifikanz ≥ 3σ.
- **widerlegt**, wenn eine zählende Analyse Bekenstein–Mukhanov-Echos mit α = 4 ln 2 für mindestens ein Ereignis ausschließt, mit
  Bayes-Faktor ≤ 1/10 oder auf dem 95-%-Niveau, jeweils unter den Modellannahmen der Analyse.
- **widersprüchlich**, wenn beides vorkommt; dann werden beide Analysen genannt und kein Urteil gefällt.
- **nicht entscheidbar**, wenn bis zur Frist keine zählende Analyse vorliegt, oder wenn die zählenden Analysen übereinstimmend
  festhalten, dass α = 4 ln 2 keine beobachtbaren Echos erzeugt. Das ist **keine** Bestätigung und keine Widerlegung.
- Eine Widerlegung trifft die Setzung V1 zusammen mit r24.4 und (S1); welche davon fällt, entscheidet der Test nicht. V2 und die übrigen
  Zählaussagen (H98, H15, H46, H96) bleiben davon unberührt.

## Ablauf nach dieser Notiz
1. Diese Notiz committen (vor jeder Auswertung).
2. `k227_test_h105.py` schreiben: Linienabstand und Lage des 220-Tons für gegebene Endmassen und -spins (nur Vorhersage).
3. Ergebnis-Notiz `Ergebnis_H105_Flaechenschritte_Echos.md` erst, wenn eine zählende Analyse vorliegt oder die Frist abläuft.
