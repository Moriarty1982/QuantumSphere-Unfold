# OP5 — Elastischer Vergleich für die vollständige Quelle

20. November 2026. Analytische Erkundung im Materieframe M. Betrachtet wird ein homogenes linearelastisches Kontinuum mit vorgegebener kompakter aktiver Dehnung. Die Elastizität ist eine Vergleichsannahme für einen möglichen Spannungsträger des D-Sektors. Die gravitative und massive Antwort werden in erster Ordnung der Störungsamplitude ausgewertet.

## Vorwissen geprüft

Die [Kompensation beider Außenfelder](OP5_J_Zweifache_Aussenfeldkompensation.md) liefert den Zielquelltensor $\delta T=\mathcal P S$ mit $\mathcal P=(D/m^2)(1+D/m^2)$ und $D=\partial_t^2-\Delta$. Die [Paarkompensation](OP5_J_Paarkompensation.md) schreibt $S$ mithilfe des transversalen symmetrischen Potentials $K_{ab}$. Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) gibt das notwendige integrierte Moment vor. Die [Antriebsenergie](OP5_J_Antriebsenergie_und_Gravitation.md) verlangt die Bilanz des Antriebs. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Messabbildung vor H96. Rückwärts wird zuerst das für den vollständigen Zieltensor nötige Materialgesetz bestimmt. I3 liefert für diese Modulation weiterhin keine Ansteuerung oder Populationsdynamik.

## Verschiebung, Dichte und Cauchy-Spannung

Sei $K_{ab}$ glatt und kompakt, mit den transversalen Indizes $a,b=x,y$. Die Profile können glatt gewählt werden, da für den Achsenkontrast eine nichtverschwindende transversale Krümmung genügt. Erweitere $B_{ab}=\mathcal P K_{ab}$ zu einer symmetrischen räumlichen Matrix mit $B_{zi}=0$. Für die konstante Referenzdichte $\rho_0>0$ setze die Materialverschiebung $u_i$ und Cauchy-Spannung $\sigma_{ij}$ als
$$
u_i=-\partial_jB_{ij}/\rho_0,\qquad
\sigma_{ij}=-\partial_t^2 B_{ij}.
$$
Lineare Massenerhaltung liefert dann $\delta\rho=-\rho_0\partial_i u_i=\partial_i\partial_j B_{ij}=\delta T^{00}$ in Einheiten $c=1$. Der Impulsfluss $\rho_0\dot u_i$ entspricht $\delta T^{0i}$, und $-\sigma_{ij}$ entspricht $\delta T^{ij}$ in erster Ordnung. Der konvektive Stress ist quadratisch in der Störung. Die Bewegungsgleichung $\rho_0\ddot u_i=\partial_j\sigma_{ij}$ ist mit diesen Definitionen erfüllt. Im Vergleich kommt die Kraft aus der inneren Spannung. Eine zusätzliche äußere Volumenkraft ist in dieser Bilanz entbehrlich.

Für die isotrope Elastizität schreibe $\mathsf C e=2\mu e+\lambda\,\operatorname{tr}(e)\mathbf 1$ mit $\mu>0$ und $2\mu+3\lambda>0$. Sei $\varepsilon(u)$ der symmetrische Verschiebungsgradient und $\varepsilon_*$ die lokal spannungsfreie Dehnung. Das Materialgesetz lautet $\sigma=\mathsf C(\varepsilon(u)-\varepsilon_*)$. [Esh3D zur Eigenverformung und elastischen Dehnung](https://doi.org/10.1029/2018EA000442)

Die nötige vorgegebene Dehnung ist damit explizit
$$
\varepsilon_*=\varepsilon(u)-\mathsf C^{-1}\sigma,\qquad
\mathsf C^{-1}\sigma
=\frac1{2\mu}\left[\sigma-\frac{\lambda}{2\mu+3\lambda}
                         \operatorname{tr}(\sigma)\mathbf 1\right].
$$
Sie ist kompakt und im Allgemeinen anisotrop, etwa durch die gemischten Verformungen $\partial_z u_a/2$. Auf der Endplattform können Dichte und Verschiebung geändert sein, obwohl die Zielspannung null ist. Dafür muss die lokale spannungsfreie Form auf dem Plateau geändert bleiben. Ein passiver Vergleich mit unveränderter Eigenverformung und ohne Randlast trägt kein anderes kompaktes statisches Profil. Die Energieidentität der statischen Gleichung ergibt durch Multiplikation mit $u$ und partielle Integration $\int\varepsilon(u):\mathsf C\varepsilon(u)=0$. Positive Steifigkeit erzwingt starre Bewegung, die bei kompaktem Träger null ist.

## Arbeit und Reichweite der Konstruktion

Die mechanische Energiedichte in der linearen Elastodynamik ist
$$
e_{\rm mech}=\tfrac12\rho_0|\dot u|^2+
\tfrac12(\varepsilon-\varepsilon_*):\mathsf C(\varepsilon-\varepsilon_*).
$$
Aus Impulsbilanz und Materialgesetz folgt
$$
\partial_t e_{\rm mech}
=\partial_j(\sigma_{ij}\dot u_i)-\sigma:\partial_t\varepsilon_*.
$$
Der letzte Term ist die vom Antrieb an das Material übertragene Leistungsdichte. Ein ideales lokales Reservoir ohne eigenen Energiefluss könnte in diesem Vergleich $\partial_t e_{\rm res}=+\sigma:\partial_t\varepsilon_*$ liefern. Dann ist der Energiefluss des kombinierten Systems $-\sigma_{ij}\dot u_i$. Bei ruhenden spannungsfreien Endpunkten und fehlendem äußeren Randfluss ist die Nettoarbeit an der elastischen Probe null. Während der Schaltung muss dennoch Energie lokal aufgenommen und abgegeben werden. Diese Referenz speichert die elastische Energie relativ zu ihrer jeweils eingestellten spannungsfreien Form. Eine Änderung der mikroskopischen Ruheenergie dieser Form ist im Materialgesetz nicht enthalten.

Bei einer kleinen Modulationsamplitude $\epsilon$ sind die berechneten kinetischen und elastischen Energien und die modellierte Reservoirarbeit von Ordnung $\epsilon^2$. Damit kann die erste Ordnung des Zieltensors durch Dichte, linearen Impuls und lineare Spannung dargestellt werden. Die kompakte lineare Antwort folgt nur, wenn die tatsächliche aktive Struktur keine zusätzlichen Quellen erster Ordnung einbringt. In zweiter Ordnung müssen ihr Energieinhalt, der Konvektionsstress und weitere Materialbeiträge eigens abgeglichen werden. Auch die Kausalität einer konkreten Ansteuerung muss durch ein physisches Modell belegt werden.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_elastischer_quellenabgleich.wl) kontrolliert Dichte, Impulsbilanz und das Materialgesetz für die diagonale Wahl des transversalen Potentials. Die letzte Zeile prüft die Ableitung der elastischen Energie an einem symbolischen diagonalen Beispiel. Es handelt sich um klassische Elastodynamik ohne definierte Quantenschaltung.

~~~text
Density residual: 0
Momentum residual: {0, 0, 0}
Constitutive residual: {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}
Energy derivative sample residual: 0
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Eigenverformung, realer Antrieb, Beiträge höherer Ordnung, Apparaturabgleich und H96 bleiben offen.
