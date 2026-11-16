# Ergebnis H111: Zeit-Oktant über die Frame-Eigenzustände ausgelesen (widerlegt)

Gerechnet am 2026-11-16 nach der Vorab-Notiz `Vorab_Notiz_H111_Zeitoktant_durch_Frames.md` (Commit b0493d0). Skript `k233_test_h111.py`, Ausgabe
`k233_out.txt`.

## Ergebnis
Kontrolle: Frame-Oktant gegen sich selbst gibt K = 2/3 und 3δ = π/4, wie erwartet.

| Achse | φ₀ | Singulärwerte (√m) | K | 3δ | Abstand zum Ziel |
|---|---|---|---|---|---|
| +z | 30° | 0; 0,6771; 2,2153 | 0,6414 | 0,9085 | +0,242 |
| +z | 90° | 0; 0,6771; 2,2153 | 0,6414 | 0,9085 | +0,242 |
| −z | 30° | 0; 0,8897; 1,6859 | 0,5478 | 1,6668 | +1,000 |
| −z | 90° | 0; 0,8897; 1,6859 | 0,5478 | 1,6668 | +1,000 |

**4 Versuche, kein Treffer → widerlegt.**

## Nachträglich erkannt
- **Rang zwei.** Beide Zustandsfamilien liegen im Spin-½-Raum ℂ². Die Kreuz-Gram-Matrix A = E†G hat deshalb höchstens Rang 2, und ein Singulärwert ist
  immer null: Die Konstruktion liefert stets ein masseloses leichtestes Teilchen. Auch die Kontrolle hat Rang 2 (der Oktant ist der Rand mit m_e = 0,
  r16.9(c)). Ein Treffer, der ein massives Elektron verlangt, war damit von vornherein unmöglich; mit K nahe 2/3 hätte nur π/4 herauskommen können.
  Das hätte vor der Rechnung auffallen müssen und wird hier offen als nachträglich vermerkt.
- **φ₀ = 30° und 90° sind gleichwertig** (gleiche Singulärwerte); tatsächlich waren es also nur zwei verschiedene Versuche.

## Einordnung
Eine Verbindung der beiden Oktanten über eine Spin-½-Kreuz-Gram kann die Biegung grundsätzlich nicht liefern; sie bleibt auf dem Rand (ein √m = 0). Eine
Verbindung, die biegen soll, muss den Rang erhöhen, also aus ℂ² hinausführen (etwa in die Spin-1-Darstellung der Kopien oder auf S, r16.8). Das wäre
eine neue Konstruktion mit eigener Vorab-Notiz.

OP3 offen. Zuletzt vergeben H111; frei H112, k234.
