# OP3: Hälften von HS(8) in verschiedenen Frames lesen (Erkundung, nicht blind)

16. November 2026. Frage des Autors: „Wieso könnte nur das $M_Z$ korrekt berechnet werden? Kann es sein, dass man verschiedene
Partitionierungen in unterschiedlichen Frames lesen muss?“ Auftrag: die Zuordnung „Frame je Hälfte“ aus dem Bestand herleiten und, falls
ein zulässiger Mechanismus entsteht, als H109 vorab festlegen. Diese Notiz ist eine **Rückwärtssuche vor einem Test**: Das Ergebnis steht
analytisch fest, sobald die Symmetriebedingung gesetzt ist. Es ist deshalb eine Erkundung, kein blinder Test. Keine H-Nummer vergeben.

## Bestand
- v4.10.0-r16.7: Auf dem Dublett $\chi$ wirken die Frame-Abbildungen als halbe Drehungen $R=\sigma_z$, $T=\sigma_x$, $J_B=\sigma_y$ um drei
  senkrechte Achsen.
- Das Oktant hat die Zyklusachse $(1,1,1)/\sqrt3$; die Generationszustände von r25 und H107 liegen auf einem Kegel um sie
  (Spin-1-Dreieck, Überlappung ½, $\psi=38{,}6763^\circ$).
- H106–H108: Gesucht ist ein gemeinsames Singulettgewicht $w$ für alle drei Generationen. Eine Lesung, die die Generationen
  unterschiedlich behandelt, liefert kein gemeinsames $w$.

## Bedingung
Eine Frame-Lesung einer Hälfte ist für die Frage nur zulässig, wenn sie den Generationszyklus achtet, also für alle drei Generationen
dieselben Kastengewichte liefert. Das tun genau die Drehungen um die Zyklusachse und die halben Drehungen um Achsen senkrecht zu ihr.

## Ergebnis (`frame_halves.py`, Ausgabe in `run/frame_halves_stdout.txt`)
| Lesung | Kastengewichte 00/01/10/11 | je Generation gleich |
|---|---|---|
| keine | 0,7927 / 0,0976 / 0,0976 / 0,0120 | ja |
| $R$, $T$ oder $J_B$ (Frame-Achsen, geneigt zur Zyklusachse) | z. B. 0,0132/0,1016/0,1016/0,7836; 0,3906/0,2344/0,2344/0,1406; 0,1368/0,2331/0,2331/0,3970, unter den Generationen vertauscht | **nein** |
| halbe Drehung senkrecht zur Zyklusachse | 0,0120 / 0,0976 / 0,0976 / 0,7927 (Tausch 00↔11) | ja |
| Drehung um die Zyklusachse | unverändert | ja |

1. Die Frame-Abbildungen von r16.7 brechen die Generationsgleichheit: Jede Generation bekommt andere Kastengewichte. Ein gemeinsames
   Singulettgewicht gibt es dann nicht.
2. Die zykluserhaltenden Lesungen geben nur den Tausch 00↔11. In einer Hälfte normiert wird daraus 0,1097 ↔ 0,8903; beide Werte sind
   schon in der H107-Familie geprüft.

## Folgerung
Unter Zyklussymmetrie gibt es keine neue zulässige frame-getypte Lesung der Hälften. **H109 wird deshalb nicht angelegt.** Eine
Fortsetzung müsste generationsabhängige Lesungen zulassen (je Generation ein anderer Frame). Das wäre eine neue Familie mit freien
Wahlen (Zuordnung Generation → Frame, 3! Möglichkeiten je Hälfte) und bräuchte eine Begründung aus dem Bestand, die es bisher nicht gibt.
Diese Entscheidung liegt beim Autor.

Zur Frage nach $M_Z$: Die Renormierungs-Erkundung (`../op3_renormalisation_2026_11_16/`) zeigt, dass der Wert $3\delta$ an der Skala $M_Z$
nur durch das Laufen der QED-Kopplung entsteht und den Rest in die falsche Richtung verschiebt. Eine Frame-Lesung der Hälften ändert
daran nichts. OP3 bleibt offen; der Rest 0,012376 ist unerklärt.
