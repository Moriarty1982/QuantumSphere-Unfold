# Fortsetzbarkeit des Zeitumkehr- und des Spiegel-Jets zum zweiten Jet: keine Einschränkung (Erkundung, 23.11.2026)

**Ergebnis in einem Satz:** Alle geprüften ersten Jets der Familie, der gespeicherte, das Zeitumkehr-Jet, das Spiegel-Jet und zwei
zufällige Glieder, lassen sich zu einem zweiten Jet fortsetzen; die 15 Verträglichkeitsbedingungen zweiter Ordnung sind auf ihnen von selbst
erfüllt. Auch der zweite Jet entscheidet also nicht zwischen Zeitumkehr und Spiegelung. **Nach dem vorab festgelegten Raster: keine
Einschränkung.**

Auftrag des Autors: „weiter“ nach r43. Verfahren vorab: `Methoden_Notiz.md` (Commit 2f835585, mit Prüfung der Suchrichtung). Blind im
Ergebnis. Skript `second_jet_images.py` (Python, mpmath 40 Stellen; Keimordner, Repo-Wurzel und Ausgabeordner als Argumente), Ausgabe
`run/second_jet_images.txt`, die fünf Jets in `run/second_jet_images_jets.json`. Wolfram nicht nötig, Qiskit nicht geeignet. Keine H-Nummer.

## Ergebnis
| erster Jet | \|R\| | Bilder T / R (relativ) | Abstand zum gespeicherten | Rang des Systems | voller Rest zweiter Jet |
|---|---|---|---|---|---|
| gespeichert (Kontrolle) | 2·10⁻⁴⁰ | 1,28 / 1,87 | 0 | 113 von 128 | 1,5·10⁻²¹ |
| T-Jet | 2·10⁻⁴⁰ | 7·10⁻⁴¹ / 2,0 | 3,16 | 113 | 6,6·10⁻²³ |
| R-Jet | 1·10⁻³⁶ | 1,49 / 4·10⁻⁴¹ | 2,67 | 113 | 5,3·10⁻²² |
| Zufall 1 | 3·10⁻³¹ | 1,48 / 2,13 | 0,97 | 113 | 2,4·10⁻²³ |
| Zufall 2 | 3·10⁻³⁵ | 1,02 / 1,99 | 0,99 | 113 | 3,7·10⁻²¹ |

Die rechten Seiten haben die Größe \|b\| ≈ 27 bis 38; die Reste liegen also rund 22 Größenordnungen darunter. Die Restgröße 10⁻²¹ statt
10⁻⁶⁶ im Original-Skript kommt von 40 Stellen, zentralen Differenzen für das Symbol und `mp.diff` für b; die Kontrolle am gespeicherten
Jet zeigt dieselbe Größe.

## Lesart
- Die Verträglichkeitsbedingungen zweiter Ordnung schränken die Familie der ersten Jets an diesen fünf Gliedern nicht ein. Entweder sind sie
  auf der ganzen Familie Identitäten, oder sie schneiden an Stellen ein, die diese Stichprobe nicht trifft; fünf Glieder sind kein Beweis.
- Damit sind Werte (r41), erster Jet (r43) und zweiter Jet (diese Runde) ausgeschöpft: Keine dieser Stufen entscheidet zwischen Zeitumkehr
  und Spiegelung. Höhere Jets hängen an der offenen Omega-Bedingung und der Kohomologie fünften Grades
  (`PRECISION_HIGHER_JET_CHECKPOINT.md`); eine regionale Lösung gibt es nicht.
- Die zurückgestellte Idee I1 (String zwischen M und T) bleibt der andere Weg; sie wird dem Autor vorgelegt, nicht still umgesetzt.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
