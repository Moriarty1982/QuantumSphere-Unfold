# QSC: Vermittlungsdiagramm für konkrete native Operationen

30.10.2026. Lokaler Vergleich im nativen E+iB-Doppelregister, keine neue physikalische Zeitentwicklung.

Quelle sources/research/parts/v490-post-release-layers.tex r04.1 bis r04.3: F=[E|B], G=F^T F; e^(i alpha) wirkt rechts mit R_alpha^T, J_B=i Konjugation mit sigma_x, T=Konjugation mit sigma_z, HC mit Cplus=(I+sigma_x)/2. Raumrotationen wirken links; gerichtete Boosts sind nicht allgemein rechte Doppelregistermatrizen.

## Gemeinsame Vermittlung

Für reguläres Rang2-Feld verwende F=O F0(G) aus QSC_Orientation_Complete_Mediator.md. Für jede der genannten Operationen M folgt exakt G'=M^T G M. Der verbleibende Orientierungsübergang wird aus F0(G)M bestimmt: F0(G)M=K F0(G'), dann O'=O K. Damit ergibt Rekonstruktion nach Vermittlung O'F0(G')=F M. Derselbe Schritt vor und nach dem Auslesen stimmt überein. Für die drei invertierbaren Operationen bleibt die Rang2-Karte regulär, solange der gewählte E'-Chart nicht verschwindet; andernfalls braucht es einen anderen Chart.

Direkte SymPy-Kontrollen für zwei unabhängige exakte Felder und vier Operationen (acht Fälle) bestätigen Feld-, Gram- und Orientierungsrekonstruktion. Die Phasendrehung nutzt cos alpha=3/5,sin alpha=4/5; J_B und T werden auch direkt auf dem komplexen z ausgeführt. Die Allgemeinheit von G'=M^TGM folgt aus der Matrixidentität, nicht allein aus acht Stichproben.

## Compensator braucht einen Rang1-Chart

HC erzeugt E'=B'=(E+B)/2, also Rang<=1. Die frühere vollständige Orientierungstriade lässt sich am Ausgang nicht eindeutig aus dem projizierten Feld bestimmen. Ein Richtungsvektor n'=E'/|E'| und die verbleibenden skalaren Amplituden rekonstruieren das nichtverschwindende Rang1-Feld; Rotationen um n' bilden eine Stabilisatorfreiheit. Diese Freiheit ist ein durch Projektion bedingter Informationsverlust, keine numerische Singularität eines ansonsten invertierbaren Schrittes.

Für jeden nichtverschwindenden HC-Ausgang gilt rho'=Cplus=[[1/2,1/2],[1/2,1/2]], ein reiner Registerzustand auf dem Rand. Wolfram bestätigt dies für allgemeines reelles symmetrisches G. Falls E+B=0, ist der ausgewählte Port null und rho' undefiniert; es wird kein normierter Nullzustand eingeführt.

Dieser projizierte Registerzustand ist nicht derselbe Gegenstand wie ein nichtverschwindendes lichtartiges EM-Feld im nativen Gramdiskus, das rho=I/2 im Mittelpunkt besitzt. Eine Identifikation der Compensator-Auslese mit einem physikalischen Photon benötigt deshalb die jeweils konkrete Projektion/Readout-Zuordnung. Die verschiedenen Photon-/Port-/Feldbegriffe werden hier nicht gleichgesetzt. Die Quelle r04 trennt Messport und Feld-Gram-Auslesung bereits; der Test hält diese Unterscheidung ausdrücklich fest.

## Was dieser Schritt beweist und was er offen lässt

Der erweiterte Vermittler transportiert die geprüften nativen algebraischen Operationen konsistent. Für ihre Gram-Komponente genügt bereits G; Orientierung ist für die Rekonstruktion des vollständigen Feldes und spätere gerichtete Beobachterwechsel erforderlich. Nicht jede Operation benötigt jede Zusatzinformation.

Das ist ein positiver begrenzter Vermittlungsnachweis, kein vollständiger Nachweis einer gemeinsamen Quanten/ART-Dynamik. Eine Phase als algebraische Dualitätsrotation ist nicht automatisch eine Zeitentwicklung; ein Compensator ist ein Projektions-/Ausleseschritt. Uhren wurden in diesem rein algebraischen Test nicht fortgeschrieben. Oktonionische Multiplikationsverträglichkeit und die native Zeitgeneratorwirkung sind noch anzuschließen.

Nächster diskriminierender Schritt: einen konkret benannten nativen zeitlichen Generator auf F bzw z auswerten und prüfen, welche vollständigen Vermittlungsdaten er benötigt. Darstellungswechsel, Messprojektion und Zeitentwicklung nicht aus der gemeinsamen Matrixschreibweise heraus identifizieren.

Artefakte QSC_Native_Operation_Mediator_Check.py/.json; Python/SymPy, Wolfram-Teilprüfung. Lokal gespeichert, nicht committed. OP5-Spinorfortsetzung bleibt offen.
