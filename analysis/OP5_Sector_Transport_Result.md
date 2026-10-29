# OP5: Transport der lokalen Sektoren
28.10.2026. Fortsetzung des relativen Verbindungskanals.

## Exakte Transportgleichung
Mit normalisiertem G_AC=cos(theta), G_BC=-sin(theta) ist
R=I-2G²=[[-cos(2theta),sin(2theta),0],[sin(2theta),cos(2theta),0],[0,0,-1]],
J=R tensor gamma5.
Der gemeinsame skalare Vorfaktor von G fällt aus R heraus.

Bei D=partial+iA lautet D_mu R=partial_mu R+i[A_mu,R].
Die bisherige Verbindung A_mu=s_mu G kommutiert mit R. Deshalb bleibt D_mu R=R_theta partial_mu theta, im Ausgangsansatz nicht null.

Eine kanonische hermitesche Ergänzung ist
B_mu=(i/2)(partial_mu R)R=-Y partial_mu theta.
Es gilt exakt partial_mu R+i[B_mu,R]=0. Zu B können weitere Matrizen addiert werden, die mit R kommutieren; die Ergänzung ist nicht eindeutig. Das Minuszeichen wurde durch direkte symbolische Einsetzung geprüft.

Diese Matrixrichtung Y war bereits als Faktor des Massenterms vorhanden. Ihre zusätzliche Verwendung als Verbindung ist dennoch eine neue Wahl von Kopplungskoeffizienten und nicht durch den Massenterm allein hergeleitet. Reine Spinverbindungen der üblichen Lorentzdarstellung kommutieren mit gamma5; die vollständige gemeinsame Wirkung und Geometrie sind hier nicht gelöst.

## Grenze durch den Ausleseoperator
Die konstante Auslese S kommutiert nicht mit B. Mehr noch:
Tr(SR)=sin(2theta).
Wären S und R gleichzeitig kovariant konstant, müsste diese Spur konstant sein. Ihre Ableitung ist aber 2cos(2theta) dtheta. Auf dem untersuchten regulären Patch, wo cos(2theta) und dtheta nicht verschwinden, ist das unmöglich.

Dies ist eine allgemeine Verträglichkeitsbedingung für die gleichzeitige Parallelität in dieser Familie, keine bloße Folge der kanonischen Wahl B. Zusätzlich wurde bei theta=pi/12 das volle lineare System für eine beliebige hermitesche 3x3-Verbindung gelöst: R_theta+i[X,R]=0 zusammen mit [X,S]=0 hat keine Lösung.

Der Befund verbietet nicht eine physikalische Auslese, die Sektoren mischt. Er zeigt nur, dass wir sie dann nicht zugleich als unabhängig transportierte UND von dieser Auslese getrennte Bereiche behandeln können. Die Frage nach fundamentaler Unzerlegbarkeit bleibt damit offen.

## Rückwirkung auf die Coframe
Für die Startfelder Psi=(c u,d u,w) gilt bei festgehaltenen Feldableitungen
delta E_mu^a=Re(i Psi†(S tensor K^a)B_mu Psi)
=Delta/2 (u†K^a u) partial_mu theta =a^a q0_mu.
Vorher war E=I, nun E_new=I+a q0^T. Mit a·q0=1 folgt det E_new=2. Die Reparatur des Sektortransports ist also nicht geometrisch kostenlos.

Für den ursprünglichen rein zeitlichen theta-Gradienten ist die neue Coframe
E_new=[[2,0,0,0],[v_x,1,0,0],[v_y,0,1,0],[v_z,0,0,1]].
Sie ist invertierbar, lorentzsch und hat g^{00}=-1/4. Anders als die vorherige große Mischungsgradient-Reparatur zerstört diese Änderung nicht die Raumartigkeit der alten t-Anfangsflächen. Die vollständigen Gleichungen im neuen Operator sind aber noch zu prüfen; det E=2 ist kein Lösungsnachweis.

## Folgerung
Die lokale Sektoraufteilung besitzt einen expliziten parallelen Transport, wenn die Verbindung erweitert wird. Die bisherige Verbindung leistet das nicht. Gleichzeitig ändern sich Coframe und Ausleseverhalten. Das erlaubt eine präzisere nächste Rechnung: die neue Verbindung und Coframe gemeinsam in die vollständigen Vergleichsgleichungen einsetzen und prüfen, ob die Sektorinterpretation dabei hilfreich bleibt.

Keine neue physikalische Konstante, kein Primzahlgesetz, kein nativer OP5-Beweis. Exakte SymPy-Prüfungen in OP5_Sector_Transport_Check.py/.json. Lokaler Stand, nicht committed.
