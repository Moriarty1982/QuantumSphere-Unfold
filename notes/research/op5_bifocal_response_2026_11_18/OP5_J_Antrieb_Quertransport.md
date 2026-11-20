# OP5 — Antrieb des Quertransports

20. November 2026. Analytische Erkundung im Materieframe M. Ausgangspunkt ist ein homogenes, ruhendes, barotropes Vergleichsfluid der Massendichte $\rho_0>0$ in flacher Geometrie. Alle Störungen werden linear behandelt. Der auf das Fluid wirkende Yukawa-Selbstbeitrag ist quasistatisch. Das ist ein reduzierter Vergleich für einen möglichen Antrieb. Das vollständige W1/W2-Materialgesetz wird nicht vorausgesetzt.

## Vorwissen geprüft

Der [Quertransport](OP5_J_Quertransport.md) realisiert das Dichteprofil kinematisch durch einen kompakten Querstrom und gibt einen formal erhaltenen Tensor mit transversaler Spannung an. Der [Kontrollkontrast](OP5_J_Kontrollkontrast.md) liefert $f=(1-\Delta/m^2)\psi$. Der [Quellenerhaltungsabgleich](OP5_J_Differenzphase_Quellenerhaltung.md) zeigt, dass ein physischer Austausch die Quellen aller beteiligten Sektoren berührt. [W1](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) enthält Dirac-, Eich- und Stromkopplungen. Daraus wird hier kein Materialgesetz für die gebundene D-Population abgeleitet. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Frage zur lokalen Messabbildung vor H96. Rückwärts wird zuerst die für den Zieltransport notwendige Kraft bestimmt.

## Ein rein transversaler Strom benötigt eine Kraft mit Rotation

Setze $\delta\rho=s(t)f$, $\delta p=c_s^2s f$ mit konstantem $c_s^2\ge0$, ein Selbstpotential $g\,s\psi$ und ein externes skalares Potential $V$. Das Selbstpotential entspricht dem bereits abgeglichenen Yukawa-Profil. Mit $\Delta_\perp\chi=f$ und $\nabla_\perp\chi=(\partial_x\chi,\partial_y\chi,0)$ ist der zylindersymmetrische Strom aus der Vorrechnung $\mathbf j=-\dot s\nabla_\perp\chi$. Die lineare Impulsbilanz des Fluids wäre
$$
\partial_t\mathbf j=-\nabla\delta p-\rho_0\nabla(g s\psi+V).
$$
Der zur Realisierung notwendige äußere Potentialgradient müsste also
$$
\rho_0\nabla V=\ddot s\nabla_\perp\chi
              -s\nabla(c_s^2 f+\rho_0g\psi)
$$
sein. Die Rotation der rechten Seite ist
$$
\ddot s(-\partial_z\partial_y\chi,\partial_z\partial_x\chi,0).
$$
Ein nichttriviales, in $z$ kompaktes $\chi$ hat diese gemischten Ableitungen irgendwo ungleich null. Wären sie überall null, wäre $\nabla_\perp\chi$ von $z$ unabhängig und aufgrund der Kompaktheit überall null. Somit kann während $\ddot s\ne0$ kein skalares $V$ den vorgegebenen rein transversalen Strom antreiben. Derselbe Befund folgt aus der Wirbelgleichung des linearen homogenen Fluids: Alle Kräfte des geprüften Ansatzes sind Gradienten, während der verlangte Strom bei $\dot s\ne0$ Rotation besitzt. Ein Übergang von Ruhe zu Ruhe braucht Beschleunigungsphasen.

Das Hindernis beschreibt den geforderten kinematischen Strom. Insbesondere ist die transversale Spannung aus der Vorrechnung anisotrop und kann einen Kraftterm dieser Form liefern. Eingriffe über Randspannungen, zusätzliche Felder, eine inhomogene Grunddichte oder ein anderes Materialmodell benötigen eine neue Impulsbilanz.

## Das passive barotrope Plateau

Für ein ungetriebenes Plateau mit $s\ne0$ und $V=0$ verlangt die stationäre Gleichung $c_s^2 f+\rho_0g\psi=0$. Eine räumlich konstante rechte Seite entfällt, weil beide Störungen kompakt sind. Im Fourierbild ergibt sich
$$
\left[c_s^2(1+|\mathbf k|^2/m^2)+\rho_0g\right]\widehat\psi(\mathbf k)=0.
$$
Sofern $(c_s^2,g)\ne(0,0)$, ist der Multiplikator höchstens auf einer einzelnen Kugelschale oder am Ursprung null. Ein stetiger, von null verschiedener Fouriertransformierter kann nicht auf einer Menge ohne Inneres getragen sein. Damit hält das passive homogene Vergleichsfluid dieses kompakte Profil nicht selbst im Gleichgewicht. Der entartete druck- und kraftfreie Fall erlaubt ruhende Profile und liefert keinen Antrieb zum Umschalten.

## Skalarantrieb bei zugelassenem Längsstrom

Im selben linearen Modell kann ein skalarer Antrieb die vorgegebene Dichteänderung realisieren, wenn der Strom frei gewählt werden darf. Sei $\Xi$ die auf $\mathbb R^3$ abklingende Poissonlösung mit $\Delta\Xi=f$. Dann erfüllen
$$
\mathbf j=-\dot s\nabla\Xi,\qquad
V=\frac{\ddot s\Xi-s(c_s^2 f+\rho_0g\psi)}{\rho_0}
$$
die Kontinuitäts- und Impulsgleichung. Dieser Strom hat im Allgemeinen auch eine Komponente entlang der Messstrecke.

Für das konkrete kompakte Profil mit Amplitude $A$, Transversalradius $a$ und Längshalbbreite $\ell$ verschwinden Gesamtintegral und Dipolmoment von $f$. Verwende die Koordinaten relativ zum Profilzentrum und das harmonische Polynom $H=z^2-(x^2+y^2)/2$. Partielle Integration liefert $\int H f=\int H\psi$, da $\Delta H=0$. Das Querintegral von $\psi$ verschwindet in jeder Ebene. Der Beitrag aus $-(x^2+y^2)/2$ ergibt
$$
\int_{\mathbb R^3}H f\,d^3x=\frac{64\pi A a^4\ell}{1575}\ne0.
$$
Die abklingende Poissonlösung besitzt daher einen Quadrupolterm proportional zum inversen Kubus des Abstands. Insbesondere kann sie nicht kompakt sein. Während des Umschaltens besitzt der Strom einen Fernanteil mit inverser vierter Potenz des Abstands. Der dafür nötige Antrieb hat während der Beschleunigung ebenfalls einen Fernanteil. Im ursprünglichen kompakten Transportmodell bleiben diese Beiträge durch den vorgeschriebenen rein transversalen Strom und die dafür nötige Spannung ausgeschlossen. Für die erweiterte Bewegung muss der Endpunktabgleich neu gerechnet werden.

## Symbolische Kontrolle und verbleibende Voraussetzung

[Wolfram Language](op5_j_antrieb_quertransport.wl) prüft die Rotation, die Harmonizität von $H$, das Quadrupolmoment und den Multiplikator des stationären Gleichgewichts. Qiskit ist für diese klassische Impuls- und Potentialrechnung ohne definierte Quantenschaltung nicht geeignet. Der nächste physische Abgleich braucht einen nachgewiesenen anisotropen Spannungsträger oder eine konkrete Ansteuerung, deren Fernbeiträge mitgemessen werden. Native D-Dynamik, Endpunktkalibrierung und H96 bleiben offen.
