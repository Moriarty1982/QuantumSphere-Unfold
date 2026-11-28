# Vorab-Notiz H218 (k431): Gibt der Rahmen eine Schleife oder einen Zielwert für χ und Λ?

Stand 28.11.2026, vor der Suche festgeschrieben. Auftrag des Autors vom 28.11.2026, 00:08 („alles drei“), Folgetest 3 zu H215.

## Frage

In H215 wurden χ und Λ nicht getestet, weil keine der beiden Größen einen Zielwert hat. H218 sucht zuerst eine Schleife oder ein
Zielkriterium aus dem Rahmen. Nur wenn sich eines findet, wird getestet.

## Was als „aus dem Rahmen“ gilt (Kriterium, fest)

Eine Schleife f oder ein Zielwert zählt nur, wenn alle drei Bedingungen erfüllt sind:

1. Er folgt aus einem vorhandenen Befund oder Postulat im Bestand, mit Fundstelle.
2. Er braucht keine neue Setzung. Eine neue Zuordnung wie „Operation X wirkt auf cos²χ“ ist eine Setzung.
3. Sein Wert lässt sich nicht auf β_sym zurückführen, sonst prüft er nichts Neues.

Kandidaten, die 1 oder 2 verletzen, werden als Erkundung mit ihren Fixpunkten und ihrer Stabilität angegeben, aber nicht als Test gewertet.

## Vorgehen

1. Bestandssuche über `notes/research/`, `analysis/`, `wiki/`, `sources/research/parts/` und `llm/` nach Schleifen, Fixpunktgleichungen
   und Zielwerten für χ und Λ.
2. Jeder Kandidat wird nach dem Kriterium eingeordnet.
3. Erfüllt ein Kandidat alle drei Bedingungen, folgt ein Test wie bei H215: Fixpunkt, |f′| und Kontrollen. Für Λ ist das nur mit einer
   dimensionslosen Größe möglich.

## Urteil

- **Herleitbar:** mindestens ein Kandidat erfüllt 1 bis 3. Dann wird er getestet.
- **Nicht herleitbar:** sonst. Das wird offen gesagt, mit der Liste der geprüften Kandidaten und der Bedingung, an der jeder scheitert.

## Vorwissen (vor der Suche)

- χ: H211b/c (Minimum der Bandenergie 63,63°, abhängig von der Setzung), H209, H210, H192.
- Λ: k251 (keine Skala), k353 (10^122 braucht eine eigene Länge), H159, rem:omega-bsym (β = √Ω_M, nur Konsistenzvergleich).
- **Erwartung:** nicht herleitbar. Für Λ führt die einzige dimensionslose Lesart Ω_Λ = 1 − β² auf β_sym zurück und verletzt damit
  Bedingung 3.

Ordner: `notes/research/hilbert_shift_felder_2026_11_24/stabilitaet_folgetests_h216_h218/`.
