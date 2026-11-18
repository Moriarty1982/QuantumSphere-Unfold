# Gemeinsame Dualität und die M–T–P-Kopplung

Analytische Erkundung gemäß [Vorab-Notiz](Dualitaet_Vorab.md), Commit 0b23d5acf4b6051617d198dfb85940b0939a7a22. Die Beispiele sind mögliche effektive Randterme im gemeinsamen Modellchart, keine aus dem Companion abgeleitete native Wirkung.

## Energie der Kopplung

Schreibe U(θ)z=exp(iθ)z. Dann ist H=z_M†z_P unter der gemeinsamen Drehung invariant, B=z_M·z_P dagegen wird zu exp(2iθ)B. Setze z_M=e1, z_T=i e1 und z_P=e1+i e2, sodass S(z_P)=0 und H=B=1. Der Term λ|H−1|²/2 mit λ>0 ist unter gemeinsamer Drehung konstant und bindet zugleich die relative Phase: Bei Drehung nur von P liefert er λ(1−cos θ) mit Krümmung λ. Der Term λ(Im B)²/2 ist unter der gemeinsamen diskreten Vierteldrehung invariant, weil B→−B. Bei kontinuierlicher gemeinsamer Drehung liefert er λ sin²(2θ)/2 mit Krümmung 4λ. Der Nullstatus von P und eine diskrete Vierteldrehung reichen folglich selbst bei diesen gemeinsamen Ausgangsdaten nicht zur Energiesymmetrie. Die diskrete Feldzuordnung allein ist zudem keine Invarianzannahme für eine Wirkung.

## Vergleich mit dem Kompensator

Der positive Ansatz in v470/13 addiert Normquadrate des Kommutators und des Restterms. Transformieren beide unter der gemeinsamen stetigen Drehung etwa durch unitäre Konjugation oder eine andere normerhaltende Darstellung, bleibt ihr Gesamtbeitrag konstant. So folgt z.B. bei gemeinsamem U M U† und U P_C7 U† der transformierte Kommutator U[M,P_C7]U†. Werden Projektor, Quellen oder Randdaten stattdessen festgehalten, muss diese Eigenschaft separat gezeigt werden. Eine solche native Transformationsregel und die induzierte Schnittstellenabbildung sind in den geprüften Abschnitten nicht instanziiert.

## Konsequenz für den Reparaturmechanismus

Der stärkere Befund: Ist die gemeinsame Drehung bei festem Überschuss n eine exakte Symmetrie des Defektnormquadrats, ist dieses auf jeder Drehbahn konstant. Ein bereits vorhandener Defekt mit positiver Norm kann durch diese Bewegung allein nicht verschwinden. Die gemeinsame Symmetrie liefert damit bei festem n zwar eine Richtung ohne Zusatzenergie, aber keine Reparaturrichtung für den invarianten Geometriedefekt. In Verbund.md muss s dagegen G tatsächlich ändern. Für s braucht man also eine relative Bewegung oder eine andere dynamische Änderung der Zellkonfiguration, die das Defizit übernimmt und deren minimierte zusätzliche Energie auf der reparierten Familie separat geprüft wird. Der Quadratterm für relative Phasen oben zeigt, dass diese Bewegung schon bei gemeinsamer stetiger Symmetrie verankert sein kann. OP5 und H96 bleiben offen.
