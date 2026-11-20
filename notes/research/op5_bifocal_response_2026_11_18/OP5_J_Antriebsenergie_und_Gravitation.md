# OP5 — Antriebsenergie und gewöhnliche Gravitation

20. November 2026. Analytische Erkundung im Materieframe M. Die kompakte vorgeschriebene Quelle des dynamischen Modells werde zusätzlich als vollständiger gravitativer Störungstensor in linearer Einstein-Gravitation behandelt. Hintergrund und Apparaturgeometrie sind flach und fest vorgegeben. Für die Energierechnung wird die lineare Quellenordnung verwendet.

## Vorwissen geprüft

Die [dynamische Kompensation](OP5_J_Dynamische_Kompensation.md) konstruiert die volle erhaltene Quelle aus einem kompakten Hilfstensor. Die [Paarmodulation](OP5_J_Gebundene_Paare_Spannung.md) liefert die Arbeit der gesteuerten Zugspannung. Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) bestimmt das benötigte transversale Moment. Der [metrische Abgleich](OP5_J_Metrischer_Abgleich.md) unterscheidet den masselosen Gravitationspol vom separaten Vermittler. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur OP5-Messkette vor der kosmologischen Materieauslese. Rückwärts werden Quellen- und Endpunktbedingungen bestimmt. Die Konstruktion ersetzt keine für I3 benötigte Populationsdynamik.

## Woher die Paararbeit kommen muss

Schreibe die gewünschte Gesamtquelle als $\delta T=(1+D/m^2)S$ mit $D=\partial_t^2-\Delta$, $S^{00}=\psi$, $S^{z\mu}=0$ und verschwindender transversaler Nullmode $\int \psi\,d^2b=0$ in jeder Ebene. Dann gilt
$$
\int \delta T^{00}\,d^2b
=\left[1+(\partial_t^2-\partial_z^2)/m^2\right]\int\psi\,d^2b
=0.
$$
Der transversale Laplace-Term fällt wegen des kompakten Trägers heraus. Es gibt in dieser Modellquelle keinen axialen Energiefluss. Somit hat jede zwischen zwei festen $z$-Ebenen liegende Schicht in der vollständigen Modellquelle über die Umschaltung dieselbe Gesamtenergie.

Für ein gesteuertes Paar im Potential $C/R+\mathcal T(t)R$ mit $C>0$ ist die innere Endenergie auf einem ruhenden Plateau $2C/R$. Bei der Verkürzung von $R_0$ auf $R_1$ steigt sie um $W=2C(1/R_1-1/R_0)>0$. Bei $N$ vollständigen Paaren in einer energetisch abgeschlossenen Schicht muss die Summe der **anderen** Energieänderungen daher $-NW$ betragen. Ist nur ein Reservoir für diesen Ausgleich vorgesehen, muss es genau diesen Betrag abgeben. Falls Paar, Feld oder Ansteuerung Energie über die Grenzen des betrachteten Bereichs austauschen, muss der Fluss oder die Energie des Antriebs in die Gesamtquelle aufgenommen werden. Nur die Paar-Ruhemassen zu kompensieren genügt für diesen vollständigen Quellenvertrag nicht.

## Die masselose Antwort bleibt übrig

Im linearen schwachen Feld und mit derselben retardierten Anfangsbedingung gilt komponentenweise
$$
D_{\rm ret}^{-1}\delta T
=D_{\rm ret}^{-1} S+\frac{S}{m^2}.
$$
Denn $D_{\rm ret}^{-1} D S=S$, wenn $S$ vor Beginn verschwindet. Der zweite Term ist lokal. Außerhalb des Trägers hat das lineare spurgespiegelte Gravitationsfeld daher genau die Antwort auf $S$, bis auf den üblichen gravitativen Normierungsfaktor. Das gilt für die gesamte lineare Fernantwort und benötigt keine Entwicklung in $\omega/m$. Der massive Austausch bleibt durch die frühere Konstruktion kompakt.

Auf einem ruhenden Plateau sind die Ströme und räumlichen Spannungen der Modellstörung null. Für $I_{ij}=\int x_i x_j S^{00}\,d^3x$ gilt relativ zum unmodulierten Profil $I=-Q s\,\mathrm{diag}(1,1,0)$. Masse und Dipoländerung verschwinden. Die Entwicklung des Newton-Kerns $1/|\mathbf x-\mathbf y|$ liefert in Entfernung $r$ bei Polarwinkel $\theta$ zur Strahlachse
$$
\delta\Phi(r,\theta)
=-\frac{GQ s}{2r^3}(3\cos^2\theta-1)+O(r^{-4}).
$$
In der unbeschränkten Vakuumregion kann dieses statische Potential daher nicht überall verschwinden. Ein konstanter Potentialoffset kann den Quadrupol und seine Gezeitenwirkung nicht entfernen. Für $s\ne0$ schließt das vorgegebene Moment die gleichzeitige exakte statische Außenfeldgleichheit beider Kanäle aus, solange die Platteauquelle denselben Momentwert und verschwindenden räumlichen Stress hat.

Während der Umschaltung hat die gewöhnliche Gravitation in der langsamen Fernzonen-Näherung eine transversale spurfreie Antwort. Mit $c=1$, retardierter Zeit $t-r$ und Polarisationsbasis $(\mathbf e_\theta,\mathbf e_\phi)$ lautet der führende Term
$$
h_+(t,r,\theta)=\frac{GQ}{r}\sin^2\theta\,\ddot s(t-r),\qquad h_\times=0.
$$
Denn die Differenz der beiden transversalen Momente ist $Qs\sin^2\theta$. Der Strahl entlang der Symmetrieachse liegt in einer Nullrichtung dieses führenden Strahlungsterms. Der statische Quadrupol ist auf der Achse hingegen ungleich null. Die Näherung benötigt eine kleine Quellregion verglichen mit der charakteristischen Schaltwellenlänge. [Lineare gravitative Fernzone und TT-Projektion, Novak](https://apc.u-paris.fr/APC/Conferences/Site_Cargese/Courses_files/novak_notes.pdf)

Die gewöhnliche Geometrie kann bei gleichem Weg und minimaler Kopplung beiden Signalen gemeinsam sein, wie im metrischen Abgleich. Die Rechnung liefert deshalb einen möglichen gemeinsamen Beitrag für die Apparaturbilanz, keinen berechneten Rest einer konkreten J–A-Differenzmessung. Die Energiebilanz enthält keine Rückwirkung der gewöhnlichen Gravitationsstrahlung.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_antriebsenergie_und_gravitation.wl) berechnet die Winkelprojektionen, die algebraische Zerlegung des masselosen Nenners und die Reservoirbilanz. Es liegt keine Quantenschaltung vor.

~~~text
Static angular factor: amp*s*(2 - 3*Sin[theta]^2)
TT plus moment: amp*s*Sin[theta]^2
TT cross moment: 0
Massless operator split residual: 0
Reservoir balance: {{deltaE -> -(pairCount*work)}}
~~~

Der separate Rückgabewert des abschließenden `Print` war `Out[1]= Null`. Native Zug- und Reservoiransteuerung, ein vollständiges Modell der Apparaturantwort und H96 bleiben offen.
