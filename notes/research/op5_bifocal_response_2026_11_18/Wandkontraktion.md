# OP5: Überschwingt die beladene Wand beim Schrumpfen?

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/8efd662f48e1df089a5be37b6677d68070f2a751/notes/research/op5_bifocal_response_2026_11_18/Wandkontraktion_Vorab.md). Aufbauend auf [Wandladung.md](Wandladung.md) und [Pauli_Beladung.md](Pauli_Beladung.md). Führende Dünnwandnäherung, kugelförmige neutrale Wand, gleiche Vakuumenergien beidseits, langsame lokale Anpassung des Fermigases, festes N bis zur betrachteten Emissionsschwelle. Keine Selbstgravitation.

## Radiales Energieprofil

Für nackte Spannung σ lautet die Ruhenergie U(R)=4πσR²+D/R mit D>0 bei festem N. Sei R_* das Minimum und U_*=U(R_*). Aus der Gleichgewichtsbedingung folgt D=8πσR_*³. Mit x=R/R_* ist

    U(x)/U_* = (x²+2/x)/3,
    k_F(x) = k_*/x.

Im konservativen radialen Kollektivmodell ist die Energie bei einem Umkehrpunkt gleich der Ruhenergie. Beispielsweise gilt in der führenden Oberflächenbeschreibung mit zu vernachlässigendem Normaldruck E=γ U(R), da die Flächenelemente nur normal zur Oberfläche bewegt werden. Die Lage der Umkehrpunkte folgt schon aus E=U bei radialer Ruhe. Aus anfänglicher Ruhe bei x_L>1 hat der innere Umkehrpunkt dieselbe Ruhenergie. Faktorisieren liefert

    x_- = [√(x_L²+8/x_L)−x_L]/2.

Eine Wand ohne Energiedissipation bleibt daher nicht am Minimum stehen. Diese Aussage behandelt nur die radiale Bewegung bei fester Ladung.

## Kalte Vorbeladung und lokale Emissionskante

Schreibe r=k_*/M mit 1/2<r<1 und freier Fermion-Ruhemasse M. Die Wand wäre am Minimum gegen quasistatische direkte Emission unterhalb der Schwelle. Bei gerade bis k_F=M/2 kalter Beladung ist x_L=2r. Die lokale Fermikante erreicht beim Schrumpfen M bei x_ev=r. Ob die Bewegung dorthin gelangt, entscheidet der Vergleich

    [U(x_L)−U(x_ev)]/U_* = r²−1/(3r).

Für r<3^(−1/3)≈0,693361 erreicht die konservative radiale Bewegung die Kante nicht. Bei Gleichheit berührt sie die Kante im inneren Umkehrpunkt. Für r>3^(−1/3) würde sie die Kante im Modell fester Ladung überschreiten. Um die Kante in diesem letzten Fall gar nicht zu erreichen, muss bei unverändertem N vor dem ersten möglichen Erreichen mehr Energie abgeführt werden als U_*[r²−1/(3r)]. Beginnt die Kontraktion bei noch größerer Fläche oder bereits mit radialer Bewegungsenergie, erhöht sich die für dieselbe Schwelle nötige Abgabe.

| r | x_L | x_- bei festem N | k_F(x_-)/M | [U(x_L)−U(x_ev)]/U_* |
|---:|---:|---:|---:|---:|
| 0.6 | 1.2 | 0.823610 | 0.728500 | -0.195556 |
| 0.8 | 1.6 | 0.574773 | 1.391855 | 0.223333 |

Die eingesetzten Umkehrpunkte reproduzieren U(x_L)/U_* mit Abweichung höchstens 2,3·10⁻¹⁶. Für r=0,8 wäre der theoretische innere Umkehrpunkt bei fester Ladung bereits hinter der Emissionskante. Die Tabelle beschreibt dort keine tatsächliche Bewegung nach einsetzender Emission.

## Grenze für OP5

Die Rechnung liefert ein Kriterium für das Erreichen der lokalen energetischen Schwelle k_F=M. Sie bestimmt weder die Emissionsrate einer bewegten Wand noch den Energieabtransport oder die nach Abgabe einzelner Teilchen verbleibende Ladung. Weitere inelastische Kanäle können auch unterhalb dieser vereinfachten Schwelle relevant sein. Die Bildung eines radial und gegen Verformung stabilen Objekts bleibt offen. H96 bleibt offen. Für I3 bliebe die Materiezuordnung vor einer späteren Λ-Auslese separat zu begründen.
