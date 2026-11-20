# OP5: Gemittelte J-Feldantwort und Teilchendichte

19. November 2026. Analytische Erkundung in M. Die [neutrale Feldantwort](OP5_J_Neutrale_Feldantwort.md) liefert für den Bindungsanteil eines Verbands $\Delta M=\kappa F_J^2$, wobei im Coulomb-Abgleich $\kappa=c\mu A_D^2/\Lambda^4$ gilt. Hier werden gleichartige Verbände in einem verdünnten Medium zusammengefasst. Ziel ist zu prüfen, ob der J-Kanal die Teilchendichte selbst bestimmt. Keine Herleitung aus W1/W2 und kein Datenvergleich nach dem [H96-Kriterium](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Von der einzelnen Einheit zum Feldmedium

Nehme eine ausreichend kleine interne Anregung, Feldvariation auf Skalen groß gegenüber dem Verband und eine effektive Wirkung der Form
$$
S_{\rm Paar}=-\sum_i\int [M+\kappa F_J^2(x_i)]\,d\tau_i .
$$
$M$ ist die Grundzustandsmasse bei ausgeschaltetem J-Hintergrund. $\kappa$ wird konstant gehalten. Zusätzliche Beiträge, etwa ein separater Term mit der Vierergeschwindigkeit und zwei Feldstärken, werden in dieser Erkundung nicht verwendet. Aus der Weltlinienmaßsumme wird beim Mitteln eines lokal ruhenden, dünnen Mediums $\int d^4x\sqrt{-g}\,n(x)$, wobei $n$ die physische Ruhesystem-Anzahldichte bezeichnet. Zusammen mit dem Maxwell-Anteil gilt
$$
S_{J,\rm eff}=-\frac14\int d^4x\sqrt{-g}\,Z(x)F_J^2,\qquad Z(x)=1+4\kappa n(x).
$$
Die Formel verwendet den gewählten Bindungsanteil. Andere Beiträge pro Verband, die dieselbe Struktur haben, würden in einen effektiv abgeglichenen Koeffizienten eingehen. Der Bereich setzt $Z>0$ voraus. Bei der linearen Feldgleichung wird $n$ als vorgegebene Mediumskonfiguration gehalten:
$$
\nabla_\mu[Z F_J^{\mu\nu}]=j^\nu_{\rm sichtbar}.
$$
Bei konstantem $Z$ und ohne sichtbare Quellen bleibt in einem homogenen Gebiet die Maxwell-Ausbreitungsgeschwindigkeit unverändert. Der Faktor multipliziert elektrische und magnetische kinetische Terme gleichzeitig. Grenzflächen, räumliche Fluktuationen, Kopplungen an sichtbare Quellen und zeitabhängiges $Z$ können weiterhin beobachtbare Antworten erzeugen.

## Homogenes expandierendes Medium

Im räumlich flachen FLRW-Vergleich sei $\eta$ die konforme Zeit und $a(\eta)$ der Skalenfaktor. Die inverse Metrik in zwei Feldstärken hebt das Volumengewicht auf. Für eine masselose transversale Mode $J_k$ ohne äußere Quelle gilt
$$
(ZJ_k')'+Zk^2J_k=0,\qquad
v_k=\sqrt Z\,J_k,\qquad
v_k''+\left[k^2-\frac{(\sqrt Z)''}{\sqrt Z}\right]v_k=0.
$$
Die Striche sind Ableitungen nach $\eta$. Die Mode ist die einer Maxwell-Wirkung mit zeitabhängiger kinetischer Normierung. [Martin und Yokoyama, zeitabhängiger Maxwell-Term im FLRW-Raum](https://arxiv.org/abs/0711.4307)

Erhält sich die komovierende Anzahl, gilt $n=n_0(a_0/a)^3$. Dann kennt die gesamte lineare gemittelte Mode im gegebenen Hintergrund nur $4\kappa n_0$. Beispielsweise ergibt $a\propto\eta^2$ im materiedominierten Vergleich für kleine $\chi=4\kappa n$ den Pumpterm $(\sqrt Z)''/\sqrt Z=21\chi/\eta^2+O(\chi^2/\eta^2)$. Ein gleichbleibendes Produkt unter $n_0\mapsto s n_0$ und $\kappa\mapsto\kappa/s$ lässt die Mode unverändert. Die Ruheenergiedichte $Mn$ ändert sich bei festem $M$ um den Faktor $s$. Der Vergleich hält die Hintergrundgeometrie fest. Zusätzliche unabhängige Gravitationsdaten oder ein dynamisch mitgerechneter Skalenfaktor unterliegen dieser Degenerierung nicht zwingend. Im J-Kanal allein liefert die gemittelte Ausbreitung keine absolute Dichtenormierung.

## Welche Zusatzinformation die Degenerierung aufheben könnte

Als explizite Erkundung setze an einem festen Zeitpunkt eine homogene räumliche Poisson-Verteilung identischer Verbände voraus. Verwende hier physische Koordinaten und einen normierten Glättungskern $W$ mit $\int W\,d^3x=1$, dessen Skala groß gegenüber den Verbandsradien ist. Sei $\chi_W(\mathbf x)=4\kappa\sum_iW(\mathbf x-\mathbf x_i)$. Der Mittelwert und das verbundene Leistungsspektrum sind
$$
m_\chi=\langle\chi_W\rangle=4\kappa n,\qquad
P_{\chi_W}(\mathbf k)=16\kappa^2 n\,|\widetilde W(\mathbf k)|^2 .
$$
Die Formel folgt aus dem Beitrag gleicher Teilchenindizes in der Zweipunktfunktion. Beiträge verschiedener Indizes sind für unabhängige Positionen das Produkt der Mittelwerte und fallen aus der verbundenen Kovarianz. Definition der Fourier-Normierung: $\langle\delta\widetilde\chi_W(\mathbf k)\,\delta\widetilde\chi_W(\mathbf k')^*\rangle=(2\pi)^3\delta^3(\mathbf k-\mathbf k')P_{\chi_W}(\mathbf k)$. Für bekanntes $W$ und von null verschiedenes Signal können aus der dekonvolvierten Poisson-Leistung $P_0=P_{\chi_W}/|\widetilde W|^2$ und dem Mittelwert beide Parameter bestimmt werden:
$$
n=\frac{m_\chi^2}{P_0},\qquad
\kappa=\frac{P_0}{4m_\chi}.
$$
Dafür braucht es eine Kalibrierung des mittleren Feldkoeffizienten gegen seine Referenz $Z=1$ und einen getrennt messbaren diskreten Fluktuationsanteil. Bei verklumpten Verbänden, unterschiedlichen Massen oder Kopplungen und unbekannten Beobachtungsfiltern ist dieses Inversionsgesetz nicht anwendbar, ohne diese Beiträge eigens zu bestimmen. Der Poisson-Vergleich ist eine bedingte Identifizierbarkeitsaussage und kein Beobachtungsvorschlag mit bereits bestimmter Empfindlichkeit.

Eine daraus gegebenenfalls bestimmte Anzahldichte wäre erst mit einer unabhängig bestimmten Verbandsmasse und den übrigen Materiebeiträgen in $\Omega_M$ umzusetzen. Die native Kopplung, eine kosmologische Populationsdynamik und H96 bleiben offen.
