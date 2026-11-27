# k422: Was passiert, wenn die Bänder nicht gleich lang sind? (Erkundung, nicht blind, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz; die drei Aussagen stehen vor der Rechnung geometrisch fest, deshalb **nicht blind**. **Anlass:** Auftrag des
Autors vom 27.11.2026, 14:37 UTC („prüfe, was passiert, wenn die Bänder nicht gleich lang sind“), dazu seine Lesart von 14:16 UTC („die niedrigen
Bänder könnten genau so lang sein wie das längste, aber sich evtl. wiederholen“). **Werkzeuge:** Python (numpy, scipy, matplotlib), Wolfram (k422b)
für die exakten Summen und die Stufenbedingung. Kein HDL/MMA-Vergleich. Kein Guard berührt.

## Vorwissen geprüft
k399 (ein einzelnes Band abseits des Äquators erzwingt keine neue Form, weil die Sphäre sich drehen kann; Zahlen erst mit mehreren Bändern);
H192 und H209 (Abstoßung 1/sin aus dem Überlapp an Kreuzungen); k420 (Großkreise sind auf der runden Sphäre alle maximal lang); Fragenliste F18
bis F20 (Rotor mit 8 Stellungen, Längen als Zweierpotenzen; nicht gerechnet).

## Setzung
Länge des Bands der Stufe mit Dimension d: 2π·d/16, also 1/16, 1/8, 1/4, 1/2, 1 des Großkreises für R, ℂ, ℍ, 𝕆, 𝕊. Ein straffes geschlossenes
Band dieser Länge auf der runden Sphäre ist ein Kleinkreis beim Polwinkel θ = arcsin(d/16): 3,58°, 7,18°, 14,48°, 30°, 90°.

## Ergebnis
**1 Die Bänder müssen sich nicht mehr kreuzen.** Zwei Kleinkreise schneiden sich nur, wenn der Winkel ihrer Achsen zwischen |θ_i − θ_j| und
θ_i + θ_j liegt. Nur Großkreise kreuzen einander zwingend, und 𝕊 ist hier der einzige. Von 20 000 Zufallslagen sind 22 % ganz kreuzungsfrei;
die koaxiale Lage ist es auch. Die Überlappenergie aus H209 hat ihr Minimum 0 auf einer ganzen Schar von Lagen. **Kein Winkel zwischen den
Bändern ist dann festgelegt**, auch der Oktant nicht.

**2 Die Regel des Autors erzwingt jetzt eine Verformung.** Auf der runden Sphäre ist nur 𝕊 ein längster Kreis. Ein kurzes Band liegt auf einem
Breitenkreis, an dem die Fläche mit cos θ (0,87 bis 0,998) geneigt ist; ein Breitenkreis ist aber nur dort ein längster Kreis, wo der Abstand von
der Achse stationär und maximal ist (Clairaut). Anders als bei einem einzelnen Band (k399, Teil 3) hilft Drehen nicht, weil die Länge nicht zum
Großkreis passt. Zwei Grenzformen:
- **Stufen (kleinster Eingriff):** An jedem Band wird die Fläche waagerecht, Ring und Rille; ρ(θ_i) = sin θ_i, ρ′ = 0, ρ″ = −sin θ_i < 0
  (Wolfram exakt). Die Höhe der Stufe ist frei.
- **Perlenkette (größter Eingriff):** Jedes Band ist Äquator einer eigenen Kugel mit Radius d/16. Fläche 341/256 = 1,332 (Grenzwert des
  unendlichen Turms 4/3), Volumen 4681/4096 = 1,1428 (Grenzwert 8/7), Höhe 31/16 Durchmesser (Grenzwert 2).

Welche Form zwischen diesen beiden gilt, entscheidet erst eine Elastizität der Fläche. Die ist nicht hergeleitet.

**3 Lesart „gleich lang, aber wiederholt“.** Sind alle Bänder Großkreise und läuft das Muster der Stufe d auf ihnen 16/d-mal um, so ist die
Geometrie die von H192 mit Gewicht = Windungszahl (16, 8, 4, 2, 1). Die Energie ist dieselbe (322,1532), die Rollen sind gespiegelt: **R ⟂ ℂ**
(89,54°) statt 𝕆 ⟂ 𝕊, und 𝕆–𝕊 = 35,59°. Die Winkelliste aus H192 bleibt, nur die Namen tauschen ihre Plätze (R ↔ 𝕊, ℂ ↔ 𝕆).

## Lesart
Gleich lange Bänder (Großkreise) geben Winkel, aber keine Verformung. Ungleich lange Bänder geben eine Verformung, aber keine Winkel. Beides
zugleich gibt es in diesem Bild nicht. Die Lesart „gleich lang, aber wiederholt“ behält die Winkel und vertauscht, welches Paar senkrecht steht.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Länge ~ Dimension (Zweierpotenzen) | gesetzt |
| „kein Kreuzen erzwungen“, Winkel frei | folgt (Geometrie der Kleinkreise) |
| Verformung nötig für die vier kurzen Bänder | folgt aus der Regel des Autors |
| Stufen oder Perlenkette, Höhe der Stufen | frei (Elastizität fehlt) |
| koaxiale Lage in der Zeichnung | nur Darstellung |
| Windungszahl als Gewicht (Teil 3) | gesetzt, wie das Gewicht in H192 |

## Grenzen
Starre Kreise, Rotationsflächen, keine Dynamik, kein Bezug zu Messdaten. OP-Fragen bleiben offen. Nächste frei: H210, k423.
