# OP5: geometrische Richtung der zentralen Krümmungsbedingung
29.10.2026. Vier-Punkt-Test mit analytisch differenziertem Vollsystem.

## Daten und Vertrag
Gleicher festgehaltener Vergleichszweig wie OP5_Central_Phase_Analytic_Full_Jet_Result.md: ursprüngliche proportionale Spinorfamilie, kanonische Coframe E0=2dt, Ei=dxi+vi dt, zusätzlicher sektorerhaltender interner Kommutant, Lorentz-Spinverbindung null. Basis, Quellen und Coframe wurden analytisch differenziert; lineare Algebra anschließend in Gleitkomma.

Neue Kontrollpunkte zusätzlich zu P1/P2:
P3=(.9,.3,.2,.1), P4=(1.1,.2,-.3,-.15).
An allen vier Punkten hat das freie erste-Jet-System Rang90 und Rest unter1.1e-13. Mit geschlossenem zentralem Anteil ist der reduzierte Rang89, und der Rest bleibt groß (P3 3.54174, P4 2.23075). Die Krümmungsfreiheit hat wiederum Rang5: genau eine lineare Kombination bleibt fest.

## Geometrische Zuordnung
rho²=x²+y², v=(x,y,z)/t.
Definiere die Koordinatenvektoren
V=(1,-v_x,-v_y,-v_z),
W=(0,-xz/rho²,-yz/rho²,1).
Für die Coframe gilt E(V)=(2,0,0,0), E(W)=(0,W_spatial).
Daher ist V/2 die normierte zeitartige Frame-Richtung. W ist räumlich und orthogonal dazu.

W_spatial steht sowohl auf der radialen Richtung als auch auf dem azimutalen Spinvektor s=(-y/rho,x/rho,0) senkrecht:
W_spatial=(r cross s)/rho.
Die Formulierung gilt auf dem ohnehin verwendeten Chart rho>0; sie beansprucht keine Regularität auf der ausgeschlossenen Achse.

Die sechs Komponenten von V wedge W in der Reihenfolge (tx,ty,tz,xy,xz,yz) stimmen numerisch mit der einzigen linken Krümmungsbedingung überein. Relative Projektionsfehler:
P1 6.97e-15, P2 3.41e-15, P3 1.03e-14, P4 4.59e-15.
Es handelt sich um starke Stichprobenevidenz; ein symbolischer Beweis der Zuordnung über den gesamten Chart fehlt.

Damit ist die bisher abstrakte Bedingung am Punkt als F(V,W)=Quelle lesbar, wobei F=dc der Curl des zentralen internen Verbindungsanteils ist.
Erforderliche Werte in dieser unnormierten Basis:
P1 -2.150462963,
P2 -2.685543336,
P3 -3.187729015,
P4 -1.917075493.

Für die normierten Frame-Vektoren e0=V/2 und e_perp=W/|W_spatial| ist der Wert durch 2|W_spatial| zu teilen. Die obigen Zahlen sind also weder universelle Konstanten noch koordinatenunabhängige Feldstärken ohne Angabe der Bezugsvektoren. Eine gemeinsame Transformation von Tensor und Bezugsvektoren erhält die jeweilige Kontraktion, bestimmt aber noch keine Messvorschrift.

## Physikalische Bedeutung und Grenzen
Die Rechnung verlangt in diesem Zweig eine interne Krümmungskomponente in einer Zeit-Raum-Ebene. „Elektrischartig“ könnte diese Lage relativ zum gewählten Beobachter beschreiben, identifiziert sie jedoch nicht mit Elektromagnetismus. Ebenso ist interne Verbindungskrümmung nicht automatisch Riemann-Krümmung der Raumzeit.

Die ausgezeichnete Raumrichtung stammt aus unserer gewählten radialen Bewegung und Spintextur. Sie ist damit noch kein universeller physikalischer Primbaustein. Der örtlich wechselnde Quellwert zeigt ebenfalls keinen festen Primwert oder Primzahlmechanismus.

Offen bleibt die native Dynamik dieses Feldes: Die eine Bedingung folgt aus Konsistenz der vorgeschriebenen Spinorfamilie. Sie ersetzt keine eigene Verbindungs-/Wirkungsgleichung und beweist keine regionale vollständige Lösung. Auch fünf freie Krümmungskombinationen sind keine automatisch identifizierten Eichfreiheiten.

Nächster Schritt: die Quellfunktion und Richtungszuordnung symbolisch herleiten, dann mit einer konkret angegebenen nativen Verbindungsdynamik vergleichen. Keine neue Feldgleichung allein zur Erfüllung dieser Bedingung postulieren.

Artefakte: OP5_Central_Curvature_Geometric_Check.py/.json. Lokal gesichert, nicht committed; OP5 offen.
