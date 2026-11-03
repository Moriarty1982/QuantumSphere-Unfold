# Befund: In exakter Rechnung hat das Symbol weniger Identitäten (Fast-Identitäten der Größe 1e-16)

Stand: 3. November 2026. Methodenbefund aus dem Aufbau der hochgenauen Rechnung (kein Test). Skripte `k153_hp_linear.py`
(Linearisierung A, B mit 100 Stellen aus der punktweisen Feldgleichung, Taylor bis Grad 2 aus 41 Stützpunkten),
`k154_hp_tools.py` (python-flint, 60 Stellen; Kerne durch Newton-Nachbesserung mit double-Pseudoinverse),
`k155_hp_theta.py` (Ω hochgenau). Betrifft nur das OP5-Vergleichsmodell.

## Prüfungen der hochgenauen Daten

- A(0), B(0) mit 100 Stellen gegen 120 Stellen (kleinere Sprungweite): Abweichung 5,5e-50 bzw. 1,7e-50.
- Taylor-Grad 0 gegen direkte Rechnung: 1,1e-43; gegen die bisherigen double-Werte: A 1,1e-10, B 9,4e-10 (deren Genauigkeit).
- dg-Symbol außerhalb der Diagonale exakt 0.
- Das Nachbesserungsverfahren konvergiert an exakt rangdefekten Zufallsmatrizen in hoher Genauigkeit auf 1e-57 (etwa
  14 Stellen je Schritt).

## Befund

Block der Gleichungen vom Grad 3 auf c₄ (prolongiertes Symbol der Ordnung 4 mit Eichzeilen, 675 × 840):

- double precision: Rang 563, Linkskern 112 (Lücke 2,4e-5 gegen 1,9e-15).
- hohe Genauigkeit: nur **48** Richtungen sind exakte Identitäten (Residuum → 1e-30 und weiter). Die übrigen **64** haben
  Singulärwerte von 1,7e-16 bis 8,9e-20, gleichmäßig verteilt, danach ein Sprung auf 4e-30.
- Ebenso K₃ (zulässige c₃ bei festem 2-Jet): 29 der 189 double-Kernrichtungen sind keine exakten Kernrichtungen.

## Deutung (Vermutung)

Mehrere Komponenten von Ψ am Keim sind sehr klein (Real- bzw. Imaginärteile 1,5e-5 bis 3,6e-4). Der Keim liegt nahe an
einer symmetrischen Konfiguration, in der diese Komponenten verschwinden. Dort würden mehr Identitäten exakt gelten.
Produkte zweier kleiner Komponenten (1e-8 bis 1e-10) entsprechen dem Gewicht von Ω, das in r74.3 als „fast von J
abhängig, ~1e-8“ gemessen wurde. Produkte aus drei bis vier (1e-12 bis 1e-20) entsprechen dem Spektrum der
Fast-Identitäten.

## Folgen

- Double precision sieht die Struktur nur bis zur Ordnung (kleine Komponente)². Alle bisherigen Zählungen (g_p, Ω, die vier
  Bedingungen, H51, Involution bei 6 bzw. 8) beschreiben den nahezu symmetrischen Grenzfall, nicht den Keim exakt.
- In exakter Rechnung ist das System am Keim generischer: weniger Identitäten, andere Symboldimensionen, andere Folge
  versteckter Bedingungen. Die bisherigen Ergebnisse sind damit nicht falsch gerechnet, aber anders zu lesen: als Aussagen
  über die führende Ordnung in den kleinen Komponenten.

## Offene Entscheidung

1. Die nahe symmetrische Konfiguration bestimmen (kleine Komponenten = 0) und prüfen, ob es dort einen exakten Keim gibt.
   Dort sollten die double-Zählungen exakt gelten. Das wäre der saubere Rahmen für die bisherigen Ergebnisse.
2. Oder die ganze Analyse am jetzigen Keim exakt neu machen (Werkzeuge k153–k155 sind vorhanden). Die Hierarchie kleiner
  Werte könnte sich fortsetzen (1e-24, 1e-32 …) und mehr als 60 Stellen verlangen.
