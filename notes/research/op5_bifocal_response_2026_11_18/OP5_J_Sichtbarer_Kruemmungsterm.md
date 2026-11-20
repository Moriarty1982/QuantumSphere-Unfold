# OP5 — Erhaltener sichtbarer Krümmungsterm und Laufzeitkontrast

20. November 2026. Analytische Erkundung im Materieframe M. Verwendet wird der kompakte massive Tensorhintergrund des linearen Vergleichs, bei statischem Plateau, schwacher Kopplung und geometrischer Optik. J und Referenz A werden als Maxwell-Testwellen behandelt. Der neue sichtbare Koeffizient ist ein gesetzter effektiver Parameter.

## Vorwissen geprüft

Der [luminale Einstein-Vergleich](OP5_J_Luminaler_Einstein_Kanal.md) trennt die kompakte konforme Einstein-Antwort von der gerichteten massiven Antwort. Die [Quellenerhaltungsrechnung](OP5_J_Differenzphase_Quellenerhaltung.md) verlangt gleiche **minimale** Gewichte im betrachteten verbundenen Materieverbund. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) lässt zusätzlich einen lokalen Spurterm. Rückwärts wird daher ein unabhängig erhaltener nichtminimaler Quellterm mit einem prüfbaren axialen Empfangssignal gesucht. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt diese Messabbildung vor H96. Der Bezug zu I3 wäre erst nach einer Populationsdynamik und absoluten Normierung zu prüfen.

## Ein unabhängig erhaltener sichtbarer Term

Für $I=J,A$ verwende neben $-F_I^2/4$ den Vergleichsterm
$$
\mathcal L_{\mathrm{vis},I}=\frac{\lambda_I}{4}R^{(1)}_{\mu\alpha\nu\beta}[b]\,
                                      F_I^{\mu\alpha}F_I^{\nu\beta}.
$$
Hier bezeichnet $b$ die massive lineare Antwort, und $R^{(1)}[b]$ das entsprechende lineare Krümmungsdifferential. Die Indexkonvention ist die aus der [lokalen Antriebswirkung](OP5_J_Lokale_Antriebswirkung.md). Die Struktur ist an bekannte $RFF$-Terme der effektiven Photonenoptik angelehnt. Deren QED-Koeffizienten werden für J und den massiven Vermittler hier nicht übernommen. [Vergleich mit der Drummond–Hathrell-Struktur](https://link.springer.com/article/10.1007/JHEP05%282026%29311)

Schreibe $C^{\mu\alpha\nu\beta}=F_I^{\mu\alpha}F_I^{\nu\beta}$. Die beiden Paare sind antisymmetrisch und untereinander austauschbar. Zweimalige partielle Integration bringt den Term in die Form $\tfrac12 b_{\mu\nu}\Delta T_I^{\mu\nu}$ mit
$$
\Delta T_I^{\mu\nu}=-\lambda_I\partial_\alpha\partial_\beta C^{\mu\alpha\nu\beta},
\qquad
\partial_\mu\Delta T_I^{\mu\nu}=0.
$$
Die letzte Identität gilt durch die Antisymmetrie auch ohne die sichtbaren Bewegungsgleichungen. Die Verbesserung respektiert außerdem beide gewöhnlichen Eichsymmetrien, weil sie nur die jeweiligen Feldstärken benutzt. Daher erzwingt die Erhaltung hier keine Gleichheit von $\lambda_J$ und $\lambda_A$. Für konstanten gesamten Transferimpuls null fällt diese doppelte Ableitung heraus. Ein räumlicher Feldgradient kann dagegen zum Empfang beitragen.

## Axiale Phase und Gruppenlaufzeit

Verwende den axialen Nullvektor $n=(1,0,0,1)$ und einen normierten transversalen Polarisationsvektor $e$. Für einen lokal ebenen Strahl bei Frequenz $\omega$ setze $F^{\mu\nu}\propto k^\mu e^\nu-k^\nu e^\mu$. Bei vernachlässigbaren Ableitungen des Hintergrunds auf einer Wellenlänge ergibt die Feldgleichung in einer Eigenpolarisation
$$
k^2=2\lambda_I\omega^2 R^{(1)}(n,e,n,e)
$$
in erster Ordnung. Da $k^2=-\omega^2+k_z^2$, ist $\delta k_z=\lambda_I\omega R^{(1)}(n,e,n,e)$. Auf dem statischen Plateau und im hier frequenzunabhängig angesetzten Vergleich ergibt die Ableitung der akkumulierten Phase die Gruppenlaufzeitänderung
$$
\delta\tau_I=\lambda_I\int R^{(1)}(n,e,n,e)\,dz .
$$
Diese Größe gilt für dieselbe ungestörte Bahn und dieselbe Polarisation in beiden Kanälen. Ein gleicher minimaler Beitrag fällt in der Differenz heraus.

Der gerichtete Teil von $b$ im früheren Plateauvergleich hat die Komponente $b_{00}=f=\Delta_\perp H/m^2$. Hinzu kommen ein konformer Term $\eta_{\mu\nu}\phi$ und ein lokaler longitudinaler Term $\partial_\mu\partial_\nu\chi$. Der longitudinale Term hat verschwindende lineare Krümmung. Der konforme Anteil liefert $-\frac12\partial_z^2\phi$ in der statischen axialen Gezeitenkontraktion und integriert sich wegen der kompakten Endbereiche zu null. Damit bleibt
$$
\int R^{(1)}(n,e,n,e)\,dz=-\tfrac12\int\partial_e^2f\,dz .
$$
Für den glatten axialen Kern $H=-A_Hp(z)\exp(-|\mathbf b|^2/R^2)$ in einer Umgebung der Achse sind beide transversalen Polarisationen gleich. Der äußere Zuschnitt ist glatt und kompakt. Bis auf den konstanten Normierungsfaktor des massiven Hintergrunds folgt
$$
\delta\tau_J-\delta\tau_A
=(\lambda_J-\lambda_A)\frac{8 A_H}{m^2 R^4}\int p(z)\,dz.
$$
Der neue Term prüft damit die transversale Krümmung des früheren Achsenprofils. Der Kontrollblock mit seitlich vollständig verschobenem Träger hat keine solche Wirkung entlang der Messachse. In den kompakten äußeren Endbereichen verschwindet der direkte lokale Krümmungsterm. Die geladenen Sender und Empfänger, ihre gemeinsamen Wechselwirkungen und möglicherweise zusätzliche effektive Operatoren bleiben getrennt zu kalibrieren. Das Ergebnis definiert eine bedingte Laufzeitablesung, die Koeffizientendifferenz ist aus W1/W2 noch nicht hergeleitet.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_sichtbarer_kruemmungsterm.wl) kontrolliert das Antisymmetrieargument symbolisch an einer parametrisierten Feldstärke, die linearen Krümmungsbeiträge und den axialen Hesse-Eintrag. Es handelt sich um klassische Operatoralgebra.

~~~text
Visible improvement divergence: {0, 0, 0, 0}
Longitudinal curvature residual: 0
Conformal tidal term: (-Derivative[0, 0, 0, 2][h][t, x, y, z] - 2*Derivative[1, 0, 0, 1][h][t, x, y, z] - Derivative[2, 0, 0, 0][h][t, x, y, z])/2
Axial transverse Hessian: (-16*amp*p[z])/(m^2*rad^4)
Axial tidal trace per polarization: (8*amp*p[z])/(m^2*rad^4)
~~~

Die letzte gedruckte Zeile bezeichnet die Gezeitenkontraktion für **eine** transversale Polarisation, nicht die Summe über Polarisationen. Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Der Empfang und H96 bleiben offen.
