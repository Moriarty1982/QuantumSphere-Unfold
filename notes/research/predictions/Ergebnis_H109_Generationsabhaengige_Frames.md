# Ergebnis H109: generationsabhängige Frame-Lesung schließt den Rest nicht (widerlegt)

Gerechnet am 2026-11-16 nach der Vorab-Notiz `Vorab_Notiz_H109_Generationsabhaengige_Frames.md` (Commit 15004ce). Skript
`k231_test_h109.py`, Ausgabe `k231_out.txt`.

## Ergebnis
Kontrolle ohne Abbildung: 0,679042 (ψ = 38,6763° und 141,3237°), wie erwartet. In allen Lösungen sind die Kastengewichte und die drei
Überlappungen generationsgleich; die zyklische Zuordnung achtet also die Generationssymmetrie, wie in der Vorab-Notiz angenommen.

| Lesung | Zuordnungen | Phasen φ der Lösungen | Abstand zum Ziel 0,666665 |
|---|---|---|---|
| L1 ($F_k\otimes F_k$) | Z1, Z2 (je 2 Lösungen); Z3 keine Lösung | 0,679042 | +0,012377 |
| L2a (H1 im Frame der Generation) | Z1, Z2, Z3 | 0,051474; 0,442212; 0,443925; 0,780098; 0,241272 | ≥ 0,113 |
| L2b (H0 im Frame der Generation) | Z1, Z2, Z3 | 0,780098; 0,443925; 0,442212; 0,051474; 0,241272 | ≥ 0,113 |

**14 Versuche, kein Treffer → widerlegt** (Kriterium |φ − 0,666665| ≤ 0,0002).

## Einordnung
- **L1 ändert die Phase nicht.** $F\otimes F$ bildet einen kohärenten Produktzustand auf einen kohärenten Produktzustand ab (halbe Drehung des
  Punktes $n_k$). Die gelesenen Zustände bilden wieder ein gleichseitiges Dreieck kohärenter Spin-1-Zustände mit Überlappung ½, und dessen
  Phase ist durch die Überlappung festgelegt: 0,679042. Das gilt für jede Lesung durch Drehungen, generationsabhängig oder nicht.
  (Nachträglich erkannt; vorab nicht ausgeschlossen.)
- **L2 springt weit weg.** Die kontrollierte Lesung einer Hälfte verschränkt die Kopien-Bits; die Phasen liegen zwischen 0,05 und 0,78, ohne
  Häufung in der Nähe von 2/3. L2a und L2b liefern dieselben Werte mit vertauschten Zuordnungen (Spiegelung ψ ↔ π − ψ).
- Damit ist auch der letzte Rest der Frage des Autors („Partitionierungen in verschiedenen Frames lesen“) innerhalb der Frame-Abbildungen
  von r16.7 beantwortet: Drehungen lassen die Phase des Spin-1-Dreiecks stehen, kontrollierte Lesungen verschieben sie grob.

## Status
OP3 offen. Rest 0,012376 unerklärt nach fünf Wegen (H106 Singulett, H107 verschachtelte Normierung, H108 Verschränkung, Renormierung,
H109 generationsabhängige Frames). Folgerung aus der L1-Beobachtung: Solange die Generationen kohärente Zustände mit Überlappung ½ bleiben,
kann keine Drehung (in welchem Frame auch immer) den Rest erzeugen; eine Lösung müsste die Überlappung ½ selbst oder die Kohärenz der Zustände
ändern.
