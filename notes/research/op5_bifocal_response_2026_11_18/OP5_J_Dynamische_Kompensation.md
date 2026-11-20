# OP5 — Dynamische Kompensation des linearen Vermittlerfelds

20. November 2026. Analytische Erkundung im Materieframe M. Betrachtet wird der lineare retardierte massive Spin-2-Vergleich in flacher Raumzeit bei festgelegter Masse $m>0$. Die D-Quelle wird von außen vorgeschrieben. Vor Beginn der Umschaltung verschwinden die Änderungen der Quelle und des Feldes.

## Vorwissen geprüft

Der [Quertransport](OP5_J_Quertransport.md) liefert für eine rein statisch abgestimmte Dichte pro submassiver Frequenzkomponente einen Endpunktrest mit Faktor $\omega^2$. Die [Paarkompensation](OP5_J_Paarkompensation.md) liefert ein kompaktes Antwortprofil $\psi(t,\mathbf x)$ mit verschwindender Quermasse und einen transversalen Erhaltungstensor. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) gibt den Fierz–Pauli-Zähler für eine erhaltene D-Quelle auch an der geladenen Apparatur an. Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) bestimmt den Stress aus dem Dichtemoment. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale OP5-Messabbildung vor der Auslese für H96. Rückwärts wird zuerst eine kompakte retardierte Antwort verlangt. I3 liefert keinen Antrieb für diese präparierte Modulation.

## Retardierte Konstruktion

Sei $\psi$ glatt, gerade in $x$ und $y$, mit $J_0[\psi](t,z)=0$ in jeder Querebene. Ihr räumlicher Träger bleibt in einer festen kompakten Region zwischen den Endpunkten. Wende die doppelte transversale Integration aus der Paarkompensation jetzt auf $\psi$ an. Sie liefert eine kompakte symmetrische Matrix $K_{ab}$ für $a,b=x,y$ mit $\partial_a\partial_b K_{ab}=\psi$. Der Hilfstensor
$$
S^{00}=\psi,\qquad S^{0a}=S^{a0}=-\partial_t\partial_b K_{ab},
\qquad S^{ab}=\partial_t^2 K_{ab},\qquad S^{z\mu}=S^{\mu z}=0
$$
ist erhalten. Die Raumträger der $K_{ab}$ liegen in einem festen Rechteck in der Querebene und in demselben inneren Längsbereich. Setze
$$
\mathcal L_{\rm dyn}=1+\frac{\partial_t^2-\Delta}{m^2},
\qquad
\delta T^{\mu\nu}=\mathcal L_{\rm dyn}S^{\mu\nu}.
$$
Die Erhaltung bleibt bestehen, weil $\mathcal L_{\rm dyn}$ mit den Ableitungen kommutiert. Mit verschwindender Anfangsstörung ist die retardierte Lösung $\mathcal L_{\rm dyn}^{-1}\delta T=S$. Dies folgt aus der Eindeutigkeit des freien Anfangswertproblems, einschließlich für Profile mit Frequenzanteilen oberhalb von $m$. Der Schluss setzt die vollständige Operatorquelle voraus.

Für den im longitudinalen Abgleich verwendeten Propagator bleibt bei erhaltener D-Quelle, bis auf einen konstanten Normierungs- und Kopplungsfaktor, das vermittelte Feld
$$
S_{\mu\nu}-\tfrac13\left(\eta_{\mu\nu}-\partial_\mu\partial_\nu/m^2\right)S^\alpha{}_\alpha.
$$
Der Zähler enthält nur lokale Ableitungen. Daher verschwinden auch der Spurbeitrag und seine Ableitungen in den Endpunktregionen. Der lineare vermittelte Feldbeitrag hat bei dieser präparierten Quelle keinen Nachlauf außerhalb des gemeinsamen Trägers. Andere Wechselwirkungen und die direkte Änderung der Apparatur durch die Ansteuerung sind davon getrennt.

Für einen ungestörten axialen Nullstrahl gilt direkt $n^\mu n^\nu S_{\mu\nu}=\psi$. Die metrische Spur fällt in der Nullkontraktion heraus. Der Term mit zwei Ableitungen ist entlang des geraden Nullstrahls eine zweite Ableitung nach dem affinen Parameter und ergibt bei Integration einen verschwindenden Randterm. Damit bleibt im führenden Linienintegral der Ausbreitungsbeitrag von $\psi$ entlang der zeitabhängig durchlaufenen Strecke. Auf den Plateaus ist das genau derselbe statische Modellkontrast wie zuvor.

## Welche Quellenkorrektur das Umschalten benötigt

Die vorgeschriebene Gesamtenergiedichte ist während der Umschaltung
$$
\delta T^{00}=(1-\Delta/m^2)\psi+\partial_t^2\psi/m^2.
$$
Die Zusatzdichte hat in jeder Querebene Integral null. Sie tritt auch im inneren Messgebiet auf und ist keine reine Ringkorrektur. Für das Zielmoment $J_2[\psi]$ mit $\int J_2[\psi]dz=-2Qs(t)$ und der bisherigen Spiegel- und Vierteldrehsymmetrie gilt
$$
\int x^2\delta T^{00}d^3x=-Q(s+\ddot s/m^2),\qquad
\int\delta T^{xx}d^3x=-\tfrac Q2(\ddot s+s^{(4)}/m^2).
$$
Dasselbe gilt in $y$. Der Längsbeitrag bleibt null. Die Änderung verschwindet auf ruhenden Plateaus. Für einen festen glatten Rampenverlauf, gestreckt auf die Zeit $\tau$, ist die Zusatzdichte von Ordnung $(m\tau)^{-2}$ relativ zur charakteristischen Amplitude von $\psi$. Ein Antrieb muss die zeitlichen und räumlichen Spannungskorrekturen mitliefern. Für die Bewegung gebundener Paare und reale Reservoirs ist eine solche Quelle weiterhin nicht hergeleitet.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_dynamische_kompensation.wl) enthält die tatsächlich ausgeführte klassische Tensor- und Fourieralgebra. Für diese Konstruktion ist keine Quantenschaltung definiert.

~~~text
Divergence of auxiliary tensor: {0, 0, 0, 0}
Divergence of corrected source: {0, 0, 0, 0}
Density counterterm residual: 0
Fourier denominator cancellation residual: 0
Axial null contraction residual: 0
Moment identity residual: 0
~~~

Der separate Rückgabewert war `Out[1]= Null` durch den letzten Aufruf von `Print`. Die sechs gedruckten Zeilen enthalten die Rechenbefunde. Die Modellkompensation ist exakt bei der angesetzten Vermittlermasse. Native Ansteuerung, reale J-Auslese, andere Apparaturantworten und H96 bleiben offen.
