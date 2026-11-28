# Ergebnis H218 (k431): Für χ und Λ ist keine Schleife und kein Zielwert herleitbar

Stand 28.11.2026. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H218_Schleife_fuer_chi_und_Lambda.md` (Commit 8e0b651). Die
Bestandssuche hat ein Suchagent durchgeführt. Die beiden tragenden Fundstellen (H124 und H211d) hat der Hauptagent im Text nachgelesen.

## Urteil: nicht herleitbar

Das Kriterium der Vorab-Notiz verlangt drei Dinge:

1. eine Fundstelle im Bestand;
2. keine neue Setzung;
3. einen Wert, der sich nicht auf β_sym zurückführen lässt.

Kein Kandidat erfüllt alle drei Bedingungen. Im Bestand gibt es für jede der beiden Größen genau eine Schleife mit anziehendem Fixpunkt,
und beide hängen an einer Setzung.

## χ (Neigung der Bandachse)

| Kandidat | Fundstelle | Scheitert an |
|---|---|---|
| Minimum der Bandenergie, Gradientenfluss (χ* = 63,63°, je nach Setzung 63,6° bis 71,1°) | H211b/c | 2: Paargewicht und Gesetz gesetzt |
| Formel cos θ_s = cos²χ + sin²χ cos(sφ) | H211a | keine Schleife, kein Zielwert; 45°-Schritt aus der Achter-Uhr (k407) |
| freie Lage von fünf gleichen Bändern, Schritt 72° → 57,097° | H211d | 1/2: nachträglich, 72° ist kein Schritt der Achter-Uhr |
| Materie-Frame-Neigung cos χ = 1/γ_L | r70.1/r70.3 | 3: führt auf β_sym zurück, keine Verbindung zur Bandachse |
| magischer Winkel (cos²χ = ⅓) und 45° (cos²χ = ½) | H211 | algebraisch, vom Rahmen nicht ausgewählt (H215: ½ von 530 Schleifen angezogen, ⅓ von 15) |
| Paarwinkel nahe 57,57°, 54,74° und 60° | H192, H209 | 1: nachträglich |

## Λ

| Kandidat | Fundstelle | Scheitert an |
|---|---|---|
| Kaskaden-Attraktor dΩ_M/dN = (1 − Ω_M)(εβ² − 3Ω_M), Fixpunkt εβ²/3 | H124, r57.1 | 2: Brücke 3 gesetzt, ε = 3 gewählt, damit der Attraktor β² ist; 3: Ziel = β² |
| Λ = 3(1 − β²)H*² | r56.4 | Epoche als Eingabe; der Rahmen hat keine Skala (r56.3, r56.5) |
| Ω_Λ = 1 − β² in Zählform | v4.9.0-r67, rem:omega-bsym | 3: β_sym; erklärt den Anteil, nicht Λ |
| V(M)/V(R) = 0,694 nahe 1 − β² | H159 | 3: β_sym, keine Identität; η und f frei |
| RG-Fluss 16π² dρ/dt = 64 λ_A ρ(ρ − 1), Fixpunkt μ = 1 | k297 | gibt nicht β_sym², wirkt nur mittelbar über H159 |
| Λ = 3Ω² (Drehrate) | k251 | keine Skala, sie wandert nach Ω |
| Λ als Mischung über Kreuzungen | k108 | Umschreibung, Treffer nachträglich |
| 10^122 | k353 | keine eigene Länge |

## Folgerung

Ein Stabilitätstest für χ oder Λ wäre nur mit einer neuen Setzung möglich. Dann würde er die Setzung prüfen und nicht den Rahmen. Wer χ
festlegen will, muss zuerst das Paargewicht der Bänder herleiten (offen seit H192, H209, H210). Für Λ braucht der Rahmen zuerst eine
eigene Länge (offen seit r56 und k353). Beides ist kein Rechenproblem des Coprozessors. Ein Test entfällt deshalb, wie in der Vorab-Notiz
vorgesehen.

Hergeleitet ist nichts Neues. Gesetzt sind das Kriterium und die Suchräume. Nachträglich ist nichts.
