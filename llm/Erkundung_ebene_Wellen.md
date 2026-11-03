# Erkundung: Symbolräume aus ebenen Wellen auf dem Lichtkegel

Stand: 3. November 2026. Erkundung / Methodenprüfung ohne Vorab-Notiz. Skript `k152_wellen.py` (konsistente Daten wie
`k148`). Betrifft nur das OP5-Vergleichsmodell.

## Idee

Ist der Symbolmodul reduziert, wird jedes g_p von ebenen Wellen ξ^p ⊗ u mit ξ auf der charakteristischen Menge aufgespannt.
Dann lassen sich die Dimensionen aus Wellen der Größe 1 berechnen. Ω und die vier Bedingungen werden auf ihnen punktweise
Bedingungen der Größe 1, und das Konditionsproblem (Methodenprüfung Elimination) entfiele.

## Methodenprüfung (ohne die vier Bedingungen)

300 Nullrichtungen, je 7 Polarisationen (Kern von J(ξ), θ(ξ), Eichung):

| p | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| Spann der Kegelwellen | 115 | 184 | 267 | 364 | 475 |
| g'_p | 117 | 188 | 273 | 371 | 481 |
| Fehlbetrag | 2 | 4 | 6 | 7 | 6 |

Alle Ränge mit Lücken ≥ 2e11; die Fehlbeträge sind echt.

## Lesart

- Der Lichtkegel allein spannt das Symbol nicht auf. Ein konstanter Fehlbetrag ließe sich durch einzelne charakteristische
  Richtungen abseits des Kegels erklären (davon wurde in k145 eine gefunden). Der Fehlbetrag wächst aber und ist
  unregelmäßig. Das spricht für einen nicht reduzierten Modul (Vielfachheiten, eingebettete Komponenten, etwa auf
  Kegel ∩ Ebenen).
- Der Ansatz bräuchte zusätzlich Ableitungen der Wellen nach ξ (Noether-Operatoren) an den Stellen mit Vielfachheit. Das
  ist ein deutlich größerer Umbau und mit ungewissem Ausgang.
- In der einfachen Form trägt der Weg nicht. Der Test mit den vier Bedingungen wurde deshalb nicht festgeschrieben.
