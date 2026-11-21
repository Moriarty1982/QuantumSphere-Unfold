# OP5 – Gewöhnliches Binnenfeld auf dem A/B-Messweg

21. November 2026. Analytische Erkundung im Materieframe M. Berechnet wird die gewöhnliche metrische Antwort der bisherigen kompakten mechanischen A/B-Quelle im Messzylinder auf dem statischen Plateau. Die Rechnung verwendet lineare gewöhnliche Gravitation und geometrische Optik auf geraden Referenzstrahlen mit festen Endpunkten außerhalb des geänderten Profils. Lichtgeschwindigkeit eins, Signatur $(-,+,+,+)$.

## Vorwissen geprüft

Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) liefert das kompakte A/B-Profil $\delta H=\Delta^3V$ und dessen OP5-Achsengezeitenkontrast. Die [spannungsfreien Ruhelagen](OP5_J_Spannungsfreie_Ruhelagen.md) und die [Umschaltung](OP5_J_Umschaltung_Ruhelagen.md) eliminieren die gewöhnliche Außenantwort des vorbereiteten mechanischen Tensors bis zur zweiten Auslenkungsordnung. Der [luminale Einstein-Kanal](OP5_J_Luminaler_Einstein_Kanal.md) liefert das statische Antriebspolynom und die charakteristischen Bedingungen des reduzierten Vermittlermodells. Die [sichtbare Krümmungskopplung](OP5_J_Sichtbarer_Kruemmungsterm.md) und das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) definieren den idealisierten Laufzeitkanal und die Messfehlerschranke. Die Suche nach Binnenfeld, Laufzeit und Achsenkontrast im bisherigen Forschungszweig ergab dafür keinen Abgleich des gewöhnlichen Potentials des materiellen Antriebs mit seinem OP5-Gezeitenkontrast. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigene kosmologische Bestandsdynamik.

## Gewöhnliches Potential des direkten mechanischen Quellenanteils

Setze $s=(x^2+y^2)/R^2$ und verwende das bisherige Profil
$$
V=-\frac{A_H a R^6}{230400}\,p(z)\chi(s)(s^5-\kappa s^6),\qquad
\kappa=\frac{\int_0^\infty s^5\chi(s)\,ds}{\int_0^\infty s^6\chi(s)\,ds}.
$$
$\chi$ ist im Strahlkern eins. $p$ ist glatt und hat kompakten Träger zwischen beiden Anschlüssen. $\delta H=\Delta^3V$ bezeichnet die Differenz B minus A. Setze $\delta J=\mathcal P_{\rm stat}\delta H$ für den statischen OP5-Antrieb. Im restmassendominierten W2-Vergleich wähle wie bisher $\delta\rho=-v_{\rm H}\delta\mathcal J_h$ und schreibe $\delta\mathcal J_h=\zeta\,\delta J$. $\zeta$ bezeichnet die bedingte Identifikation und Normierung der beiden Quellen. Die bisherige Rechnung setzt sie in ihren Einheiten eins. Bei einem anderen konstanten $\zeta$ wird die Amplitude der Materialbewegung entsprechend gewählt.

Für die im stationären Modell spannungsfreie mechanische Quelle erfüllt das gewöhnliche Potential $\Delta\Phi=4\pi G\delta\rho$. Die abklingende Lösung ist
$$
\Phi=-4\pi G v_{\rm H}\zeta\,\mathcal P_{\rm stat}\Delta^2 V .
$$
Sie bleibt kompakt. Die quadratische Dichtekorrektur der Sollbahn verschwindet im bisherigen Modell punktweise. Die folgende optische Rechnung verwendet den linearen metrischen Beitrag und damit keine Terme höherer Ordnung in $G$.

Ein Überstrich bezeichne das Integral in $z$ über die Strecke. Alle Längsableitungen der kompakten Profile integrieren sich weg. Mit $D_\perp=\Delta_\perp$ gilt im Linienintegral
$$
\mathcal P_{\rm stat}=b_0-b_2D_\perp+b_4D_\perp^2 ,
$$
$$
b_0=Z\Omega_0^2,\qquad
b_2=\alpha+b_0r_m/m^2,\qquad
b_4=(r_m\alpha-2g_m^2/3)/m^2,\qquad
\alpha=Zc_h^2+\tfrac32g_0^2 .
$$
Denn bei $k_z=0$ stimmt im Antrieb aus dem Einstein-Kanal der transversale Impulsbetrag mit dem vollen räumlichen überein. Mit $P_z=\int p(z)\,dz$ erhält man im flachen Zuschnitt
$$
\overline{\Phi}
=4\pi G v_{\rm H}\zeta A_HaP_z\left[
 \frac{16b_4}{R^2}(s-9\kappa s^2)
 -b_2(s^2-4\kappa s^3)
 +\frac{b_0R^2}{36}\left(s^3-\frac94\kappa s^4\right)
\right].
$$
Dazu genügt $D_\perp s^j=(4j^2/R^2)s^{j-1}$. Im nicht integrierten $\Phi$ haben auch die Längsableitungsterme mindestens einen Faktor $s$, da der Antrieb höchstens vier transversale Laplace-Ableitungen auf $V$ zulässt.

## Laufzeit, Phase und Gezeitenkrümmung

Im gewöhnlichen schwachen statischen Feld ist die Metrikstörung $h_{\mu\nu}=-2\Phi\,\delta_{\mu\nu}$. Die Nullbedingung ergibt entlang eines ungestörten geraden Strahls $\delta\tau_G(s)=-2\overline\Phi(s)$ und im Übertragungsvorzeichen des A/B-Vergleichs $\delta\phi_G=\omega\,\delta\tau_G$. Der Bahnfehler des minimalen Strahls trägt bei festen Endpunkten erst oberhalb erster Ordnung zur Laufzeit bei. Der statische Änderungsterm verschwindet in den Uhrenumgebungen an den Enden. Daher ist $\delta\tau_G(0)=0$ auf der Mittelachse. Abseits der Achse beginnt der gewöhnliche Laufzeitwechsel im Kern bei Ordnung $s$ für $b_4\ne0$. [Schwache statische Metrik, Carroll](https://ned.ipac.caltech.edu/level5/March01/Carroll3/Carroll4.html)

Für $n=(1,0,0,1)$ und eine transversale Einheitsrichtung $e$ lautet die gewöhnliche linearisierte Gezeitenkontraktion
$$
R_G^{(1)}(n,e,n,e)=2\partial_e^2\Phi+\partial_z^2\Phi .
$$
Nach Integration verschwindet der zweite Summand. Auf der Achse folgt pro transversaler Polarisation
$$
\mathcal I_G
=\frac{256\pi G v_{\rm H}\zeta A_H a P_z}{R^4}\,b_4,\qquad
\mathcal I_{\rm OP5}=\frac{16 A_H a P_z}{m^2 R^4},\qquad
\frac{\mathcal I_G}{\mathcal I_{\rm OP5}}=16\pi G v_{\rm H}\zeta m^2 b_4 .
$$
Der Vergleich setzt die bisherigen Normierungen der beiden Metrikantworten voraus. Beide geometrischen Gezeitenkontraste haben auf der Achse dieselbe Polarisationssymmetrie. Der gewöhnliche Laufzeitnullpunkt ist daher mit einem gewöhnlichen transversalen Krümmungswechsel verträglich.

Die Proportionalität gilt allgemeiner für radiale kompakte Profile derselben Antriebsklasse mit $\overline{\delta H}(0)=D_\perp\overline{\delta H}(0)=0$. Denn
$$
\overline\Phi
=-4\pi G v_{\rm H}\zeta\left[b_0D_\perp^2\overline V-b_2\overline{\delta H}
                       +b_4D_\perp\overline{\delta H}\right].
$$
Am radialen Mittelpunkt ist $\partial_e^2 f=D_\perp f/2$. Damit fallen die ersten beiden Beiträge zu $\partial_e^2\overline\Phi$ bei diesem Profilabgleich weg. Der letzte ist genau proportional zu $-\partial_e^2D_\perp\overline{\delta H}/(2m^2)$, der OP5-Gezeitenablesung. Eine Änderung höherer radialer Koeffizienten allein trennt diese beiden Achsensignale innerhalb der deklarierten Klasse nicht.

Auch die Einstellung $b_4=0$ ist in der bisherigen strikt stabilen Vermittlerfamilie versperrt. Im [charakteristischen Vergleich](OP5_J_Luminaler_Einstein_Kanal.md) ist für rein transversalen Wellenvektor die untere Stabilitätsreserve
$$
\left.b-\frac{j_m^2}{r_m}\right|_{|P\mathbf k|^2/|\mathbf k|^2=1}
=\alpha-\frac{2g_m^2}{3r_m}=\frac{m^2b_4}{r_m}.
$$
Strikte Positivität verlangt $b_4>0$. $b_4=0$ erreicht den Rand und lässt dort eine räumliche Hauptsteifigkeit verschwinden. Die Feststellung betrifft die strikte Charakteristikenbedingung des reduzierten Modells. Im dort gewählten Parametersatz ist $m^2 b_4=101/400$ in dessen Normierung.

## Konsequenz für die Zweimodenauslese

Sehen beide idealen minimal gekoppelten Moden dieselbe ungestörte Bahn oder dasselbe frequenzunabhängige transversale Gewicht, multipliziert der gewöhnliche Laufzeitanteil die Feldübertragung mit dem gemeinsamen Skalar $e^{i\omega\delta\tau_G}$. Der Quotient der beiden Eigenwerte der A/B-Übertragung und seine Phasensekante sind von diesem Faktor unabhängig. Die gewöhnliche Gezeitenkrümmung kann zusätzlich Beiträge liefern, wenn die beiden Moden unterschiedliche Krümmungsoperatoren am gewöhnlichen Feld besitzen. Für einen RFF-Term in der Normierung der Vorarbeit wäre dieser Zusatz auf der Achse $\Delta\lambda_G\,\mathcal I_G$. Er ist von $\Delta\lambda_{\rm OP5}\,\mathcal I_{\rm OP5}$ wegen der obigen Proportionalität durch eine reine Amplitudenänderung des achsenabgeglichenen Profils nicht zu identifizieren. $\Delta\lambda_G$ bezeichnet hier ein mögliches getrenntes Gewicht am gewöhnlichen Feld. Es wird nicht aus der minimalen Laufzeit abgeleitet.

Bei unterschiedlichen frequenzunabhängigen schmalen Bündelgewichten im Kern liefern die entsprechenden Mittelungen von $\overline\Phi$ bereits einen gewöhnlichen Wegfehler. Mit $\Delta\langle s\rangle=\langle s\rangle_J-\langle s\rangle_A$ beginnt er bei
$$
B_G=-\frac{128\pi G v_{\rm H}\zeta A_H a P_z b_4}{R^2}\Delta\langle s\rangle
+\text{Terme aus unterschiedlichen höheren Momenten}.
$$
Die vollständige lineare Mittelung folgt durch Differenz der Momente im oben gegebenen Potentialpolynom. Für die gemittelte gewöhnliche Gezeitenablesung trägt der $b_4$-Anteil denselben Faktor $1-36\kappa\langle s\rangle$ wie der bisherige OP5-Riemann-Kontrast. Die $b_2$- und $b_0$-Anteile bringen höhere Potenzen von $s$ in die Abhängigkeit der Gezeitenablesung.

Für einen diagonalen, in der Modenbasis kommutierenden, nichtdispersiven Laufzeitrest mit Eigenlaufzeitdifferenz $B$ hat die zugehörige Einwegmatrix nach Abzug der gemeinsamen Phase einen Abstand $2|\sin(\omega B/4)|$ zur Einheitsmatrix. Der direkte, systematische Laufzeitrest muss im [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) innerhalb des dafür vorgesehenen Anteils liegen. Für eine gemeinsame Normschranke kann zusätzlich $2|\sin(\omega B/4)|\le|\omega B|/2$ als multiplikativer Rest an den verwendeten Frequenzen eingesetzt werden. Für frequenzabhängige Gewichte ist der Rest an beiden Bandenden für die tatsächliche Phasensekante auszuwerten. Eine Zahl verlangt Material- und Profilnormierung, gemessene Modengewichte und einen unabhängig kalibrierten gewöhnlichen Krümmungskanal. Beugung, Bewegung der Anschlüsse, direkte aktive Felder und native Higgs–OP5-Kopplung bleiben offen.

## Ein Kalibrierprofil für den gewöhnlichen Krümmungskanal

Die Proportionalität gilt für den achsenabgeglichenen Haupterwerb. In einem eigenen Kalibrierlauf darf sich $\overline{\delta H}(0)$ ändern, während beide Anschlüsse außerhalb des Trägers bleiben. Verwende mit demselben $p$ und $\chi$
$$
V_C=p(z)\chi(s)(c_2s^2+c_3s^3+c_6s^6),\qquad
c_2=\frac{36 b_2}{b_0R^2}\,c_3,\qquad
c_6=-\frac{c_2M_2+c_3M_3}{M_6},
$$
mit $b_0>0$, $c_3\ne0$ und $M_j=\int s^j\chi(s)ds$. So bleibt das Querintegral von $V_C$ null. Der höchste Term beeinflusst die relevanten Achsenjets nicht. Es gelten
$$
D_\perp^2\overline V_C(0)=64 c_2P_z/R^4,\qquad
\overline{\delta H_C}(0)=2304 c_3P_z/R^6,\qquad
D_\perp\overline{\delta H_C}(0)=D_\perp^2\overline{\delta H_C}(0)=0 .
$$
Dabei sind die von Längsableitungen kommenden Anteile bereits ausintegriert. Die Wahl von $c_2$ ergibt $\overline{\Phi_C}(0)=0$. Der modellierte massive Linienbeitrag und der OP5-Riemann-Kontrast verschwinden auf der Achse. Der gewöhnliche Gezeitenkontrast bleibt
$$
\mathcal I_{G,C}=-4\pi G v_{\rm H}\zeta\,b_0\frac{2304c_3P_z}{R^6}.
$$
Bei gleichen effektiven Krümmungsgewichten beider Läufe, schmalen Achsenstrahlen und separat kontrollierten Anschlüssen ergeben die differentiellen Laufzeiten $D_S$ für das Signalprofil und $D_C$ für das Kalibrierprofil
$$
D_S-\frac{\mathcal I_{G,S}}{\mathcal I_{G,C}}\,D_C
=\Delta\lambda_{\rm OP5}\,\mathcal I_{\rm OP5,S}
$$
im deklarierten RFF-Modell. Bei exaktem bekanntem Skalierungsfaktor addieren sich die Fehlergrenzen zu $\eta_S+|\mathcal I_{G,S}/\mathcal I_{G,C}|\eta_C$. Für gleiches $p$ kann $c_3=-A_H a b_4R^2/(36 b_0)$ den Skalierungsfaktor auf eins stellen, sofern diese Einstellung materiell erreichbar ist. Das Kalibrierprofil prüft nur den angenommenen gewöhnlichen Krümmungsoperator. Reale Änderungen der Anschlüsse, der Modengewichte und weitere gewöhnliche Operatoren brauchen eigene Kontrollen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_binnenfeld_messweg.wl) · [Tatsächliche Ausgabe](op5_j_binnenfeld_messweg.txt) · [Laufmanifest](op5_j_binnenfeld_messweg.json)

Wolfram prüfte die schwache Nullbedingung, die lineare gewöhnliche Gezeitenkontraktion, das transversale Antriebspolynom, Potentialspalte, Achsenverhältnis und Stabilitätsreserve. Die geometrische Optik und der A/B-Quotient werden im Text analytisch ausgewertet. Reproduzierbar mit **wolframscript -file op5_j_binnenfeld_messweg.wl**.
