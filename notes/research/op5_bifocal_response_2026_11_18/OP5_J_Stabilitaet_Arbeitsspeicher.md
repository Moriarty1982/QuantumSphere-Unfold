# OP5 – Störungen des Arbeitsspeichers und der Eigenzeituhr

21. November 2026. Analytische Erkundung im Materieframe M. Der materielle Störungstest erfolgt auf dem ruhenden Eingangsplateau, in einem homogenen inneren Bereich und ohne gravitative Rückwirkung auf die Materie. Die gewöhnliche gravitative Antwort auf die Störung wird in linearer Gravitation ausgewertet. Anschließend wird die Wirkung so ergänzt, dass die vorbereitete Schaltbahn erhalten bleibt und Druck- sowie Uhrstörungen auf dem Eingangsplateau einen regulären Hauptteil erhalten.

## Vorwissen geprüft

Die [kovariante Speicherkopplung](OP5_J_Kovariante_Speicherkopplung.md) gibt die gemeinsame Wirkung und die vorbereitete Bahn mit Uhrmultiplikator null. Die [Umschaltrechnung](OP5_J_Umschaltung_Ruhelagen.md) bestimmt die Restquelle bei geänderter Sollzeitfunktion. Sie umfasst keine freien Störungen des Speichers oder der Uhr. Die Suche nach Drucklosigkeit, Jordanblock und Uhrenfehlern in Vorab-Notizen, jüngeren Rundennotizen und OP5-Analysen ergab für diese Materialwirkung keinen entsprechenden Störungstest. H75 behandelt ein anderes, kosmologisches Störungssystem. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Rechnung zur lokalen OP5-Auslese. I3 setzt weiterhin eine eigenständige kosmologische Bestandsdynamik voraus.

## Druckloser Speicher und gewöhnliches Außenfeld

Vor der Schaltung sind die Zielmetrik, die Teilchenruheenergie $m_0$ und die Referenzzahldichte $n_0$ konstant. Die 1-Form ist dort null. Die Speicherstörungen $\delta n$ und $\delta v$ erfüllen daher linear
$$
\partial_t\delta n+n_0\operatorname{div}\delta v=0,\qquad
\partial_t\delta v=0 .
$$
Für die longitudinale Geschwindigkeitskomponente hat das Hauptsymbol den Block
$\left(\begin{smallmatrix}0&n_0\\0&0\end{smallmatrix}\right)$.
Für $n_0>0$ ist er nicht diagonalisierbar. Die Fourierlösung bei Wellenvektor $k$ ist
$$
\delta n_k(t)=\delta n_k(0)-it\,n_0\,k\cdot\delta v_k(0).
$$
Die Abbildung von Geschwindigkeit auf Dichte kostet eine räumliche Ableitung. Der Faktor $|k|t$ verhindert eine frequenzgleichmäßige Abschätzung in derselben Euler-Sobolev-Ordnung. Kompakte Wellenpakete im inneren homogenen Gebiet zeigen dieselbe Ableitungsverstärkung. Das Wachstum ist linear in der Zeit. Der Befund betrifft die lokale Euler-Beschreibung. [Drucklose Gasdynamik, Bouchut, Jin und Li](https://epubs.siam.org/doi/10.1137/S0036142901398040)

Für die ideale Uhr gilt auf diesem Plateau $\partial_t\delta\theta=0$ und $\partial_t\delta\lambda=0$. Der Multiplikator trägt eine gewöhnliche Energiedichte $n_{\rm M}\delta\lambda$. Der Phasenfehler $\delta\theta$ allein trägt auf dem konstant programmierten Plateau bei $\delta\lambda=0$ keine lineare Quelle. Während der Schaltung kann eine Phasenabweichung die programmierten Materialparameter verschieben. Die folgende Außenfeldprüfung braucht bereits auf dem Eingangsplateau nur die freie Dichtestörung des Speichers.

Sei $w$ glatt und kompakt im homogenen Inneren, $\int w\ne0$. Wähle $\delta v=0$, $\delta\lambda=0$ und $\delta n=\eta\,\partial_z^2w$ mit kleinem $\eta$. Die Störung ist stationär und erhält Teilchenzahl und Dipol. Sie entsteht linear etwa aus der kompakten Teilchenverschiebung $-\eta\,\partial_z w\,e_z/n_0$. Für die lineare statische Antwort gilt $\Delta\delta\Phi=4\pi Gm_0\delta n$. Mit $r=|x|$ und Polarwinkel $\vartheta$ zur $z$-Achse ergibt partielle Integration
$$
\delta\Phi(x)
=-Gm_0\eta\left(\int w\right)\frac{3\cos^2\vartheta-1}{r^3}+O(r^{-4}).
$$
Die zweite räumliche Ableitung dieses Potentials erzeugt gewöhnliche Gezeitenkrümmung im Außenraum. Die Kompensation der Sollbahn ist also schon gegenüber einer massenerhaltenden Speicherstörung empfindlich. [Statische schwache Gravitation, Carroll](https://ned.ipac.caltech.edu/level5/March01/Carroll3/Carroll4.html)

## Druck und dynamische Uhr bei unveränderter Sollbahn

Sei $n_*(\theta,X)>0$ die Eigenzahldichte des Speichers **auf der vorbereiteten Bahn**, als feste Funktion der Matrixlabels und Eigenzeit gespeichert. Ersetze die Ruheenergiedichte $mn$ des Speichers durch
$$
e_{\rm R}(n,\theta,X)=mn+\frac{\kappa}{2 n_*}(n-n_*)^2,\qquad \kappa>0.
$$
Der Zusatz und seine erste Variation nach allen Feldern und der Metrik verschwinden auf der Sollbahn. Der Speicher erhält also auf ihr keine zusätzliche Kraft oder gravitative Quelle. Am homogenen Ruhepunkt gilt $p=n\,\partial_n e_{\rm R}-e_{\rm R}$ und $\delta p=\kappa\,\delta n$. Daraus folgt $c_{\rm R}^2=\kappa/m_0$ für die longitudinale akustische Störung. $0<\kappa<m_0$ gibt zwei verschiedene, subluminale longitudinale Geschwindigkeiten $\pm c_{\rm R}$. Die transversalen Geschwindigkeitsstörungen bleiben im homogenen Ruhesystem stationär. Das Druckglied stellt die Frequenzabschätzung des longitudinalen Speicherblocks wieder her.

Für die Uhr ersetze den idealen Multiplikatorterm durch
$$
S_\theta=\frac12\int\sqrt{-g}\,n_{\rm M}
\left[I(U_{\rm M}^\mu\partial_\mu\theta-1)^2
-H P^{\mu\nu}D_\mu\theta D_\nu\theta\right]d^4x,\qquad
D_\mu\theta=\partial_\mu\theta-a_I(\theta,X)\partial_\mu X^I .
$$
$P^{\mu\nu}=g^{\mu\nu}+U_{\rm M}^\mu U_{\rm M}^\nu$ und $I,H>0$. Wähle $a_I$ so, dass auf der Sollbahn $D_\mu\theta=-U_{{\rm M},\mu}$ gilt. Denn dort annihiliert $d\theta+U_{\rm M}^{\flat}$ den Materialfluss und ist daher eine Linearkombination der $dX^I$. Damit verschwinden sowohl die Uhrabweichung $U_{\rm M}\cdot d\theta-1$ als auch der projizierte räumliche Gradient. Der Zusatz ist quadratisch in diesen beiden Abweichungen. Er und seine erste Variation verschwinden auf der Sollbahn, auch bei Metrikvariation. Das Entfernen des bisherigen Multiplikatorterms ändert dort bei $\lambda=0$ ebenfalls keine Variationsgleichung. Die vorbereitete Schaltbahn und ihr Hilbert-Tensor bleiben somit bis zur bisher erreichten Ordnung erhalten.

## Linearisierte Uhr und Matrix im ruhenden Material

Im Eingangsplateau sei $n_{\rm M}=1$ in der Referenznormierung, $a_I=0$, und das elastische Gesetz isotrop. Sei $u$ die Verschiebungsstörung der Matrix und $q=\delta\theta$. Dann ist der lineare projizierte Uhrgradient $\nabla q+\dot u$. Mit $\rho_{\rm M}$ der Ruheenergiedichte der Matrix und $\mathsf C$ ihrer Elastizität lautet die quadratische Lagrangedichte
$$
\mathcal L_2=\frac{\rho_{\rm M}}2|\dot u|^2-\frac12\varepsilon(u):\mathsf C\varepsilon(u)
+\frac I2\dot q^2-\frac H2|\nabla q+\dot u|^2.
$$
Für $0<H<\rho_{\rm M}$ ist die zugehörige quadratische Energie positiv in Geschwindigkeiten und Dehnungen. Die Matrix hat effektive Trägheit $\rho_{\rm M}-H$. Ihre transversale Geschwindigkeit zum Quadrat ist $\mu/(\rho_{\rm M}-H)$. Mit longitudinaler Steifigkeit $K=\lambda_{\rm el}+2\mu>0$ lösen die beiden gekoppelten Werte $z=(\omega/|k|)^2$
$$
(\rho_{\rm M}-H) I z^2-(KI+\rho_{\rm M}H)z+KH=0.
$$
Die Diskriminante ist $(KI-\rho_{\rm M}H)^2+4KI H^2>0$. Summe und Produkt der Wurzeln sind positiv. Als dimensionsloses Beispiel in Einheiten der Matrixruhedichte nehme $\rho_{\rm M}=I=1$, $\mu=H=1/8$, $K=1/2$, $\kappa/m_0=1/4$. Dann gilt $z_\pm=(5\pm\sqrt{11})/14$, $c_{\rm T}^2=1/7$, und alle gezeigten Geschwindigkeiten sind kleiner als Lichtgeschwindigkeit. Das Beispiel garantiert einen regulären gekoppelten Hauptteil auf dem homogenen Eingangsplateau. Die variable Dynamik einschließlich der Schaltphase ist weiter zu prüfen.

Die reguläre Uhr trägt bei Störung schon in erster Ordnung $\delta T^{00}_\theta=I\dot q$ und $\delta T^{0i}_\theta=-H(\partial_i q+\dot u_i)$ im ruhenden Referenzsystem. Ihre Divergenz summiert sich zur Uhrgleichung. Die Druckregel trägt zudem $\delta p\,\delta^{ij}$ zur räumlichen Speicherquelle bei. Der Stabilitätsgewinn am Ruhepunkt garantiert daher keine gewöhnliche Außenkompensation für beliebige Störungen. Quantitative Fehlergrenzen während der Schaltung, die Realisierung der Materialparameter und Uhr, die Binnenfeldkalibrierung und die native Higgs–OP5-Kopplung bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_stabilitaet_arbeitsspeicher.wl) · [Tatsächliche Ausgabe](op5_j_stabilitaet_arbeitsspeicher.txt) · [Laufmanifest](op5_j_stabilitaet_arbeitsspeicher.json)

Wolfram kontrollierte Rang und Propagator des drucklosen Symbols, Druckableitung, longitudinales Uhr-Matrix-Symbol samt Energie und Beispielwerten, Metrikvariation der linearen Uhrquelle sowie den Quadrupolkern. Die Aussagen zur Sollbahn folgen analytisch aus der verschwindenden ersten Variation der neuen Terme. Reproduzierbar mit **wolframscript -file op5_j_stabilitaet_arbeitsspeicher.wl**.
