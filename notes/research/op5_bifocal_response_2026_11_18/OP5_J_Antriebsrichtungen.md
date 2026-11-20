# OP5 — Welche Verformungsrichtungen der Antrieb braucht

20. November 2026. Analytische Erkundung im Materieframe M. Geprüft wird eine symmetrische Teilfamilie des linearen elastischen OP5-Vergleichs. Ein Antrieb mit festen lokalen Materialantworten und ein Antrieb mit Ableitungskopplung sind verschiedene Klassen.

## Vorwissen geprüft

Der [elastische Quellenabgleich](OP5_J_Elastischer_Quellenabgleich.md) bestimmt die kompakte Eigenverformung aus Dichte, Impuls und Spannung. Die [zweifache Außenfeldkompensation](OP5_J_Zweifache_Aussenfeldkompensation.md) definiert den Operator $\mathcal P=(D/m^2)(1+D/m^2)$, $D=\partial_t^2-\Delta$. Die [Antriebsrechnung](OP5_J_Antrieb_Quertransport.md) schließt einen skalaren Gradientenantrieb für den rein transversalen Strom im homogenen barotropen Vergleich aus. Hier erhält das Skalarfeld gegebenenfalls eine andere Rolle, indem seine Ableitungen eine anisotrope Eigenverformung bestimmen. Der Zusammenhang im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt bei der lokalen OP5-Messabbildung. Für I3 wird keine Populationsdynamik ergänzt.

## Eine kompakte Teilfamilie mit Achsenkontrast

Sei $P_\perp=\mathrm{diag}(1,1,0)$ im an der Strahlachse ausgerichteten M-Koordinatensystem. Wähle das transversale Potential als $K=H P_\perp$ mit glattem räumlich kompaktem $H(t,\mathbf x)$. Dann ist $\psi=\Delta_\perp H$ und $\int\psi\,d^2b=0$ in jeder Querebene. Für einen konkreten Kontrast wähle $H=-A s(t)p(z)g(\mathbf b)$ mit $A>0$, einer nichtnegativen von null verschiedenen Längsfunktion $p$ und $g=\exp(-|\mathbf b|^2/a^2)$ in einer Umgebung der Achse. Außerhalb dieser Umgebung kann $g$ glatt radial auf null begrenzt werden. Die beiden Profile liegen innerhalb der Messstrecke. Auf der Achse gilt $\Delta_\perp^2 g=32/a^4$. Der geometrische Kontrast auf dem Endplateau ist damit
$$
-\frac{1}{m^2}\int \Delta_\perp\psi(0,z)\,dz
=\frac{32A}{a^4m^2}\int p(z)\,dz>0.
$$

## Rang eines Antriebs mit festen Tensoren

Schreibe $h=\mathcal P H$ und $B=hP_\perp$. Im elastischen Modell sind $u=-P_\perp\nabla h/\rho_0$ und $\sigma=-\ddot h P_\perp$. Auf einem ruhenden Endplateau verschwindet die Spannung und $\varepsilon_*=\varepsilon(u)$. Sei $h_{\rm f}$ ein räumlich kompaktes, von null verschiedenes Endprofil. Das folgt für die obige Wahl, da der statische Multiplikator $\mathcal P$ für $\mathbf k\ne0$ strikt positiv ist. Die fünf potenziell nichtverschwindenden Komponenten $xx,yy,xy,xz,yz$ von $\varepsilon_*$ haben im Fourierbild die Faktoren
$$
k_x^2,\quad k_y^2,\quad k_x k_y,\quad k_x k_z/2,\quad k_y k_z/2
$$
mal $\widehat h_{\rm f}/\rho_0$. Keine konstante Linearkombination dieser fünf Komponenten verschwindet identisch. Andernfalls verschwindet das entsprechende Polynom auf einer offenen Menge, auf der die stetige Fouriertransformierte $\widehat h_{\rm f}$ von null verschieden ist. Dann müssen alle Koeffizienten null sein. Die Tensorwerte über den ganzen Raum spannen auf dem Endplateau folglich den fünfdimensionalen Unterraum $\varepsilon_{*zz}=0$ auf.

Prüfe einen Antrieb der Form $\varepsilon_*=\sum_{\alpha=1}^N q_\alpha(t,\mathbf x)M_\alpha$ mit räumlich und zeitlich konstanten Symmetrietensoren $M_\alpha$. Dann ist $N\ge5$ schon am Endplateau nötig. Isotrope thermische Ausdehnung oder mehrere stets im selben festen Achsenkreuz diagonale Materialantworten reichen innerhalb dieser Klasse nicht. Während der Umschaltung ergibt die isotrope elastische Compliance zusätzlich
$$
\varepsilon_{*zz}=-\frac{\lambda}{\mu(2\mu+3\lambda)}\,\ddot h .
$$
Bei $\lambda\ne0$ und nichttrivialem Übergang von Ruhe zu Ruhe ist diese Komponente irgendwo von null verschieden. Deshalb ist über beide Phasen der volle sechsdimensionale Raum symmetrischer Tensoren nötig. Bei $\lambda=0$ bleibt es für diese Teilfamilie bei fünf. Dies zählt feste Tensorantworten, nicht frei zu wählende Steuergrößen eines allgemeineren physikalischen Modells.

## Ein Skalar mit gerichteter Ableitungskopplung

Mit demselben $P_\perp$ kann ein einziges kompaktes Skalarprofil $h$ die formal erforderliche Eigenverformung vorgeben:
$$
\varepsilon_*(h)
=-\frac1{\rho_0}\,\mathrm{sym}\,\nabla(P_\perp\nabla h)
+\mathsf C^{-1}(P_\perp)\,\partial_t^2h ,
$$
wobei $\mathrm{sym}\,\nabla v$ der symmetrische Gradient des Vektors $v$ ist. Der räumliche Teil erzeugt die fünf unabhängigen Komponenten auf dem Plateau, obwohl nur ein Skalarprofil eingesetzt wird. Der zeitliche Teil kommt aus der benötigten Impulsbilanz. Damit ist die feste Ranggrenze eine Grenze für lokale Tensorantworten ohne solche Ableitungen. Die Formel stellt eine notwendige und in dieser Teilfamilie hinreichende Antwort des linearen Vergleichsmaterials dar. Die ausgezeichnete Richtung, die Ableitungskopplung und die eigene Quelle des Antriebs bleiben physische Eingaben. Es ist keine Ableitung aus W1/W2.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_antriebsrichtungen.wl) bestimmt den Rang der fünf Polynome, die axiale Eigenverformung und den Rest im linearen Materialgesetz. Es prüft auch die Achsenkrümmung des glatten Profilkerns. Es handelt sich um klassische Tensoralgebra.

~~~text
Plateau polynomial rank: 5
Axial eigenstrain: -((lam*Derivative[2, 0, 0, 0][h][t, x, y, z])/(3*lam*mu + 2*mu^2))
Constitutive residual: {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
Transverse bi-Laplacian of axial core: 32/a^4
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Physische Ableitungskopplung, Energie-Impuls-Quelle des Antriebs, reale Apparatur und H96 bleiben offen.
