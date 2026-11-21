# OP5 – Kohärente J-Terminierung, unmarkierter Rücklauf und Radialraster

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Leistungs-, Fourier- und Ringrechnung](OP5_J_Leistungsbilanz_Fourier_Ringmessung.md) lässt den komplexen J-Standard, den nackten Direktweg bei unmarkierten Echos und die effiziente Dichteabtastung offen. Hier werden dafür bedingte Messkonstruktionen geprüft. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft das die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Was eine kalibrierte J-Terminierung kohärent liefert

Wähle einen äußeren A-Port und genau einen J-Port, alle anderen Ports seien abgeglichen oder als Rest separat erfasst. Für eine komplex kalibrierte passive J-Last $\gamma$ an derselben Referenzebene gilt im stationären Zweitor
$$
r_A(\gamma)=r_A(0)+t_{AJ}t_{JA}\frac{\gamma}{1-r_J\gamma}.
$$
Das ist eine A-seitige kohärente Messung des J-Rundlaufs. Die gewöhnliche A-Reflexion und die Durchgänge dürfen sich beim Lastwechsel nur gemäß dem angegebenen festen Streumodell ändern. Ohne Reziprozitätsnachweis folgt aus dem Rücklauf nur das Produkt der beiden Richtungen. Bei ko-normalisierten reziproken Ports ist das Produkt $t^2$ für den gemeinsamen Einwegkoeffizienten $t$.

Mit $\gamma$ und $-\gamma$ liefert die antisymmetrische Differenz
$$
\frac{r_A(\gamma)-r_A(-\gamma)}{2\gamma}
=\frac{t_{AJ}t_{JA}}{1-(r_J\gamma)^2}.
$$
Sie entfernt die ungeschaltete A-Reflexion und unterdrückt den linearen Einfluss von $r_J\gamma$. Sobald zusätzlich $r_A(0)$ bekannt ist, liefern $u_\pm=[r_A(\pm\gamma)-r_A(0)]/(\pm\gamma)$ den exakten Produktwert $2u_+u_-/(u_++u_-)$, sofern das Produkt und der Nenner hinreichend von null entfernt sind. Bei unbekannter J-Rückreflexion lässt sich die einfachere antisymmetrische Differenz mit einer separaten Reflexionsgrenze budgetieren.

Für ein reziprokes Beispiel $|t|=0{,}003$, $|\gamma|=0{,}5$, $|r_J|\le0{,}1$ und zwei komplexe A-Messfehler höchstens $5\cdot10^{-8}$ beträgt der Produktfehler der antisymmetrischen Differenz höchstens $1{,}226\cdot10^{-7}$. Darin stehen der quadratische Rücklaufrest und der additive Messfehler. Ein hinreichender Radius für ein Prozent komplexen Fehler der richtigen Quadratwurzel ist $|t|^2(1-0{,}99^2)=1{,}791\cdot10^{-7}$. Dafür muss die Lastphase samt übrigen Schaltfehlern separat kontrolliert werden. Der gewählte Wurzelzweig muss durch einen bekannten kohärenten Standard oder eine gemeinsam beibehaltene Phasenkonvention verankert werden. Das A-Echo allein lässt das Vorzeichen von $t$ frei. Es liefert keine physische J-Terminierung und beweist keine freie J-Ausbreitung.

## Schaltbarer unmarkierter Rücklauf

Nach separater Kontrolle der markierten Fourier-Aliase sei die verbleibende Antwort $H_a=C(I-aU)^{-1}D$ bei bekannter Rücklaufdämpfung $a\in[0,1]$. Dieselben Direktkopplungen $C,D$ und dasselbe $U$ müssen in beiden Stellungen gelten. Ein wirklich abschaltbarer Pfad bei $a=0$ liefert direkt $CD$. Ein verbleibender Off-Pfad mit Norm höchstens $u_0<1$ kostet höchstens $\|C\|\|D\|u_0/(1-u_0)$.

Für $0<a<1$ kann man aus $H_a,H_1$ den Extrapolat
$$
\widetilde B=(H_a-aH_1)/(1-a)
$$
bilden. Die Neumann-Reihe oder die Resolventenidentität liefert exakt
$$
\widetilde B-CD=-a C U^2(I-U)^{-1}(I-aU)^{-1}D .
$$
Bei $\|U\|\le u<1$ ist die Biasgrenze $\|C\|\|D\|a u^2/[(1-u)(1-au)]$. Die Mess-, Fourier- und Abgleichfehler der beiden Stellungen gehen als $(\epsilon_a+a\epsilon_1)/(1-a)$ ein. Zur letzten Grenze gehört insbesondere eine Zustandsänderung des Direktwegs. Symmetrisch flankierende Referenzmessungen entfernen affine zeitliche Drift des gemeinsamen Log-Gains. Eine feste schaltkorrelierte Änderung von $C,D$ braucht eine separate Kalibrierung. [Flankierende Nullmessung](OP5_J_Einkanal_Nullreferenz.md)

Ist der Nennwert $a$ um höchstens $d_a$ unsicher, kommt nach der Resolventenidentität höchstens
$$
\frac{\|C\|\|D\|u d_a}{(1-a)(1-au)(1-(a+d_a)u)}
$$
hinzu, sofern $(a+d_a)u<1$. Bei $a=0{,}1$, $u=0{,}001$, $d_a=10^{-4}$, jeweils $\epsilon_i/|CD|\le10^{-7}$ und $\|C\|\|D\|/|CD|=1$ ist die relative Gesamtabweichung unter $3{,}335\cdot10^{-7}$. Für acht skalare Rohwerte entspricht das weniger als $2{,}668\cdot10^{-6}$ rad, wenn diese Abschätzung den ganzen betrachteten Rücklaufrest umfasst. Dämpft der Schalter nur $W$ in $U(a)=V+aW$, extrapoliert dieselbe Rechnung nach Herausziehen von $(I-V)^{-1}$ auf $C(I-V)^{-1}D$. Der ungeschaltete Anteil $V$ bleibt eigenständig zu begrenzen.

## Feinere Ringe nahe der Achse

Für eine bekannte Lipschitzkonstante $L_\sigma$ der gewöhnlichen Säulendichte in der Flächenkoordinate $u=r^2/R_c^2$ verbessert sich das Ringbudget gegenüber einer reinen Betragsgrenze. Liegen kalibrierte Flächenmittel vor, ist der scharfe Formfehler eines Rings $[a,b]$ höchstens $L_\sigma B(a,b)$, wobei
$$
B(a,b)=\tfrac12\int_a^b\frac{(u-a)(b-u)}u\,du
=\frac{b^2-a^2}{4}-\frac{ab}{2}\log(b/a),\quad B(0,b)=b^2/4 .
$$
Der Fehler des konstant angesetzten Ringmittels ist die Kovarianz von Dichte und logarithmischem Gewicht. Im Doppelintegral dieser Kovarianz kann man den Dichteunterschied durch $L_\sigma|u-v|$ begrenzen. Lineare Profile mit Steigung $\pm L_\sigma$ erreichen die Grenze in allen Ringen mit gleichem Vorzeichen. Der Potentialfehler ist $\pi G R_c^2 L_\sigma\sum_i B(a_i,b_i)$.

Für kleine Ringbreite $h$ fern der Achse ist $B\simeq h^3/(12u)$. Die asymptotische optimale Dichte der Ringgrenzen ist damit proportional zu $u^{-1/3}$. Das Raster $u_i=(i/N)^{3/2}$, also $r_i/R_c=(i/N)^{3/4}$, liefert den asymptotischen Formfaktor $9/(32N^2)$. Die Achsengrenze wurde bei der endlichen Rechnung exakt eingesetzt. Bei acht Ringen sinkt die normierte Schranke von $0{,}006595$ auf $0{,}004328$. Für ein isoliertes Formbudget von $0{,}001\,\pi G R_c^2 L_\sigma$ erfüllt das abgestufte Raster es mit 17 Ringen. Das gleichflächige Raster überschreitet es noch bei 22 Ringen und erfüllt es mit 23.

Das Formbudget setzt eine belegte Lipschitzkonstante selbst in der kompensierenden Randregion voraus. Außennull, Längsendterme, Fehler der Ringmittel, Übertragung des gewöhnlichen Detektors und $b_4$-Transfer beanspruchen eigene Anteile. Insbesondere lässt eine reine Messung im flachen Kern die für $b_4$ nötige Randstruktur aus. Reale J-Terminierung, freier J-Durchgang, native Vermittlermetrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte die kohärente Produktformel, die Kontrollzustandsidentität, die Ringformel und die numerischen Budgets. Qiskit wurde für diese klassischen Streu- und Dichteaufgaben erwogen.

[Wolfram-Skript](op5_j_terminierung_echo_radialraster.wl) · [Tatsächliche Ausgabe](op5_j_terminierung_echo_radialraster.txt) · [Laufmanifest](op5_j_terminierung_echo_radialraster.json)
