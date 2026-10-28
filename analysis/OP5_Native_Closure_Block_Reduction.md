# OP5: exakte Blockreduktion des nativen Closure-Funktionals

26. Oktober 2026. Lokale Fortsetzung von
`OP5_Native_Readout_Generator_Bridge.md`; keine Manuskriptänderung.

## Fragestellung und Urteil

Kann das minimale native Closure-Funktional selbst einen neutralen
Zweimodenzustand, dessen Ausleseachsen und eine physikalische Uhr festlegen?

**Urteil: unvollständig, mit einer expliziten fehlenden Identifikation.**
Unter den unten genannten Voraussetzungen lässt sich das Funktional exakt
reduzieren. Im hermiteschen Zweimodensektor ist es skalar und legt deshalb
keine Zustandsrichtung fest. Die notwendige Verbindung von Millennium-Matrix,
physischem Hamiltonoperator, Zeitnormierung und Messinstrument folgt daraus
nicht. Die Blockidentitäten selbst sind unter diesen Voraussetzungen bewiesen.

Quelle: `sources/research/parts/v470/10_sphaera_and_physics.tex`, Definitionen
„Projected closure residue“ und „Explicit closure functional“, unmittelbar
vor `prop:equivalent-closure-criteria`. Die Darstellung des vollständigen
Generators und die fehlende gemeinsame Feldlösung sind in
`sources/research/parts/hc-dynamics-and-geometry.tex` ausdrücklich getrennt.

## 1. Voraussetzungen und exakte Identität

Wir arbeiten endlichdimensional über C mit einem festgelegten positiven
Skalarprodukt und dessen Adjungierter. P sei ein orthogonaler Projektor,
Q = I-P, M ein beliebiger linearer Operator und rho,sigma >= 0. Definiere

    C = [M,P],    R = QMP + PMQ,
    H_C = rho C†C + sigma R†R.

Diese Voraussetzungen sind wesentlich: Ein bloß idempotentes, nicht
orthogonales P oder eine andere Adjungierte ist nicht stillschweigend erfasst.
Für Feldoperatoren wären zusätzlich Definitionsbereiche zu kontrollieren.

In der orthogonalen Zerlegung ran(P) + ran(Q) schreibe

    M = [[A,B],[D,E]],    P = diag(I,0).

Dann gilt durch direkte Multiplikation

    C = [[0,-B],[D,0]],    R = [[0,B],[D,0]],
    C†C = R†R = diag(D†D, B†B).

Also lautet das native minimale Funktional in diesem Sektor exakt

    H_C = (rho+sigma) diag(D†D, B†B).

Insbesondere kommutiert H_C mit P, auch wenn M nicht mit P kommutiert.
Die beiden nichtnegativen Summanden liefern hier keine voneinander
unabhängigen Richtungsinformationen. Bei rho+sigma > 0 ist H_C = 0 genau
dann, wenn B=D=0. Für rho=sigma=0 ist das Funktional identisch null und
dieser Rückschluss unzulässig.

Die vollständige Familie blockdiagonaler Ergänzungen M -> M + diag(X,Y)
lässt H_C unverändert. Das betrifft insbesondere M -> M + cI. Das Funktional
allein bestimmt somit weder die Binnenentwicklung der Sektoren noch einen
skalaren Offset von M. Ein Offset von M ist erst nach einer zusätzlichen
physikalischen Identifikation ein Energieoffset.

## 2. Hermitescher Fall: gepaarte positive Spektren

Falls M=M†, ist D=B† und daher

    H_C = (rho+sigma) diag(BB†, B†B).

Für jedes positive Singulärwertquadrat s_j² von B besitzt H_C auf beiden
Seiten den gleichen positiven Eigenwert (rho+sigma)s_j². Nullräume können
bei verschiedenen Sektordimensionen verschieden groß sein. Die beiden
Blockspuren sind gleich und nichtnegativ:

    Tr(P H_C) = Tr(Q H_C) = (rho+sigma) ||B||_F².

Dies ist eine Paarung gleicher positiver Werte, keine Aufhebung durch
entgegengesetzte Vorzeichen. Eine Differenz beider Blockspuren ist zwar null,
die vollständige Spur im Allgemeinen nicht. Eine solche Differenz wäre ein
zusätzlich gewähltes Ausleseobservable, kein verschwindender Energieinhalt.

## 3. Kleinster Sektor: Closure sieht keine Zustandsrichtung

Für zwei eindimensionale Sektoren und hermitesches M gilt

    M = [[a,b],[b*,d]],    H_C = (rho+sigma)|b|² I_2.

Die Koeffizienten a,d und die Phase von b verschwinden aus H_C. Alle
normierten Zustände dieses Sektors haben denselben Erwartungswert von H_C.
Eine allein daraus gebildete Funktion f(H_C) kann daher keinen bestimmten
reinen Zustand oder eine bestimmte Mischung auswählen.

Wird zusätzlich, nur als Modellannahme, ein Generator G=-kappa H_C-i gamma H_C
verwendet, so ändert er eine normierte bedingte Zustandsbahn überhaupt nicht:
Er erzeugt einen gemeinsamen Normfaktor und eine globale Phase. Selbst die
spurtreue Ergänzung mit L=sqrt(2 kappa H_C), kappa>=0, hat einen identisch
verschwindenden Dissipator, weil L skalar ist. Andere Rücksprunginstrumente
mit demselben L†L können nichttriviale Zustandsänderungen liefern; sie müssen
zusätzlich begründet werden. Für den vollständigen nativen Generator mit
Gamma-Faktoren ist G=-kappa H_C-i gamma H_C gerade nicht vorausgesetzt.

## 4. Enger Kandidat für zwei Auslesungen und eine Vergleichsuhr

Als ausdrücklich zusätzliche Identifikation nehme man im Zweimodensektor

    H_phys = M = m I + omega sigma_y,    hbar=1,
    P = (I+sigma_z)/2.

Dann ist H_C=(rho+sigma)omega² I. Die unitäre Entwicklung bewahrt die
reelle Bloch-Scheibe b_y=0. Für Anfangswerte x,z ist die Wahrscheinlichkeit
eines P-Ergebnisses nach Zeit t

    p_P(t) = [1 + z cos(2 omega t) - x sin(2 omega t)]/2.

Messungen auf gleich präparierten Exemplaren bei t=0 und t=tau bestimmen
z und x genau dann, wenn sin(2 omega tau) != 0. Bei
2 omega tau = pi/2 modulo 2pi liest die zweite Messung die negative
x-Komponente aus. Man erhält zwei komplementäre Informationen aus einem
Projektor und bekannter freier Evolution. Das ist Ensemble-Tomographie;
eine erste destruktive Messung am selben Exemplar verändert das zweite
Experiment und ist hier nicht stillschweigend enthalten.

Dies liefert einen konsistenten bedingten Kandidaten mit positiver Norm,
reversibler Uhr und zwei Auslesungen. Es beweist weder die native
Identifikation H_phys=M noch eine bestimmte Frequenz in Sekunden. Selbst
mit dieser Identifikation wäre die Uhr durch H_C allein nicht eindeutig:

    M = m I + d_x sigma_x + d_y sigma_y + d_z sigma_z,
    H_C = (rho+sigma)(d_x²+d_y²) I,
    Energieabstand = 2 sqrt(d_x²+d_y²+d_z²).

Bei gleichem Closure-Wert kann d_z den Energieabstand verändern. Der
spezielle sigma_y-Sektor setzt gleiche Diagonale und eine bestimmte Phase
der Kopplung voraus. Eine beliebige Bloch-Kugel hat zudem einen dritten
Zustandsparameter; die beiden obigen Auslesungen rekonstruieren ihn nicht.

## 5. Konsequenz für Neutralität und OP5

Zwei komplementäre Auslesungen können Informationsverlust beheben. Das
minimale Closure-Funktional bestimmt aber im geprüften kleinsten Sektor
keinen bevorzugten neutralen Zustand. Sein skalarer Anteil misst die Stärke
der Off-Sektor-Kopplung; eine kosmologische Vakuumenergie ist damit nicht
identifiziert. Insbesondere kann es einen von M unabhängigen gravitativen
Volumenterm nicht ausschließen oder dessen Koeffizienten bestimmen.

Der nächste native Nachweis müsste einen zulässigen invarianten Sektor der
vollen Gleichung angeben und dort zugleich die positive Adjungierte, die
Identifikation des Hamiltonoperators, die physikalische Zeit und die
Ausleseinstrumente herleiten. Der hier konstruierte Zweimodenkandidat erfüllt
die internen endlichen Algebra-Bedingungen; seine Einbettung ist offen.

## Überprüfung und Geltungsgrenzen

Alle verwendeten Ergebnisse wurden durch die ausgeschriebenen Blockprodukte,
die Singulärwertpaarung und die explizite Pauli-Rotation analytisch geprüft.
Es gibt keine numerische Stichprobe, die eine native Einbettung vortäuscht.
Nicht untersucht sind die volle 16-Moden-Dynamik, die native physikalische
Adjungierte, unbeschränkte Operatoren, eine Reservoirherleitung oder ein
gravitierender Energie-Impuls-Tensor. OP5 bleibt offen.
