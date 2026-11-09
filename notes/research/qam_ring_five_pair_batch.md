# Erkundung zur Auswahl von fünf Paarbedingungen am markierten Ring

9. November 2026. Bezug zu T6 (OP1) und T14 (QAM) im Gesamtbild.

Die bisherige Präfixsynthese betrachtet aufeinanderfolgende Paarbedingungen.
Hier wählen wir fünf der acht benachbarten Ringkanten und verlangen für jede
ausgewählte ungeordnete Kante das durch die Rotation um einen Punkt
vorgegebene Bild. Gesucht ist die Eindeutigkeit unter den $8!$ Punktpermutationen
des markierten Acht-Punkte-Modells. Die folgende Zählregel bestimmt das
Ergebnis vorab, daher ist der MMA-Lauf eine Erkundung und ein Abgleich.

Für jede zulässige Permutation komponieren wir mit der inversen Sollrotation.
Die resultierende Permutation erhält jede gewählte Kante als Menge. In einem
Pfad mit mindestens zwei Kanten sind die Schnittpunkte benachbarter Kanten
fixiert. Über die Kanten folgen die übrigen Punkte des Pfads. Auf einer
isolierten Kante bleiben zwei Vertauschungsmöglichkeiten. Die isolierten
Punkte lassen sich frei untereinander permutieren. Mit $i$ isolierten Punkten
und $s$ isolierten Kanten gibt es daher $i!2^s$ Kandidaten.

Mit höchstens vier Kanten ist Eindeutigkeit unmöglich. Ohne isolierte Kante
gibt es höchstens zwei nichttriviale Pfade, die zusammen höchstens sechs
Punkte belegen. Mindestens zwei isolierte Punkte bleiben vertauschbar.
Unter den 56 Fünferauswahlen liefern 16 genau einen, 32 genau zwei und
8 genau vier Kandidaten. Ein Beispiel für eine eindeutige Auswahl sind
die Kantenanfänge $0,1,2,4,5$ modulo acht. Das zusammenhängende
Fünferpräfix lässt zwei Punkte ungebunden und liefert zwei Kandidaten.

```sh
python notes/research/qam_ring_five_pair_batch.py --db build/qam-ring-five.sqlite3 --workers 2
```

Der Lauf prüft alle 56 Fälle gegen die Graphzählung und speichert den
Sammelbericht. Unter Windows mit Python 3.12.10 lieferten ein und zwei
Prozesse denselben Bericht. Die einmal gemessenen Wandzeiten lagen bei
1,11 und 0,80 Sekunden in dieser Reihenfolge mit derselben temporären
Datenbank. Die Messung umfasst Start und Datenbankzugriff und wurde
einmal je Einstellung durchgeführt.

Der Befund gilt für Punktpermutationen. Die frühere Aussage zum Transport
allgemeiner unitärer Kandidaten auf dem Singulettträger hat andere
Voraussetzungen. Die native Ausführung der Rotation und OP1 bleiben offen.
