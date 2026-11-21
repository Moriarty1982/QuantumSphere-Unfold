# OP5 – Energieabschätzung in der Schaltphase und Grenze für das Außenfeld

21. November 2026. Analytische Erkundung im Materieframe M. Die Druck- und Uhrkorrektur wird um die vorbereitete, bewegte Schaltbahn linearisiert. Die Abschätzung gilt bei kleiner Auslenkungsamplitude, festem glattem Schaltprofil und positiver Hintergrunddichte im betrachteten Inneren. Materielle Rückwirkung der Gravitation wird vernachlässigt. Das gewöhnliche Signal wird in linearer Gravitation berechnet, in Einheiten mit Lichtgeschwindigkeit eins.

## Vorwissen geprüft

Die [kovariante Kopplung](OP5_J_Kovariante_Speicherkopplung.md) liefert die lokale Wirkung samt Materiallabels und 1-Form. Der [Störungstest des Arbeitsspeichers](OP5_J_Stabilitaet_Arbeitsspeicher.md) zeigt den druckfreien Ableitungsverlust, ein gewöhnliches Fehlerquadrupol und die regulierenden Druck- und Uhrterme am homogenen Eingang. Die [Schaltrechnung](OP5_J_Umschaltung_Ruhelagen.md) gibt die retardierte Außenkompensation der ungestörten Bahn. Das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) betrifft die Endpunktmatrizen des hypothetischen Messkanals. Die Suche nach Symmetrisierung, Energieabschätzung und Fehlertoleranz ergab für diese bewegte Materialbahn bisher keine Weitergabe bis zum gewöhnlichen Außensignal. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 setzt eine eigenständige kosmologische Bestandsdynamik voraus.

## Variabler Hauptteil

Seien $y=(u^1,u^2,u^3,q)$ die Matrix- und Uhrenstörung in festen Raumkoordinaten, mit $u=-\delta X$ und $q=\delta\theta$. Der Hauptteil der zweiten Variation ist von der Form
$$
L_{\rm pr}
=\tfrac12\dot y^{\mathsf T}M\dot y+\dot y^{\mathsf T}B^i\partial_i y
-\tfrac12(\partial_i y)^{\mathsf T}K^{ij}\partial_j y .
$$
$M$ und $K^{ij}=(K^{ji})^{\mathsf T}$ ergeben sich als Ableitungshessians der regulierten Wirkung auf der Sollbahn. Am homogenen Eingang hat $M$ die Diagonale $(\rho_{\rm M}-H,\rho_{\rm M}-H,\rho_{\rm M}-H,I)$ aus der Vorarbeit. Der räumliche Elastizitätsterm kontrolliert zunächst nur die symmetrische Dehnung. Für $L_{ij}=\partial_j u_i$ füge der räumlichen Energie den Term
$$
\frac{\mu}{2}\big[(\operatorname{tr} L)^2-\operatorname{tr}(L^2)\big]
$$
mit konstantem Eingangsmodul $\mu$ hinzu. Sein Euler-Lagrange-Ausdruck verschwindet identisch. Die resultierende räumliche Energie am Ausgangspunkt ist
$$
\tfrac{\mu}{2}|L|^2+\tfrac{\lambda_{\rm el}+\mu}{2}(\operatorname{tr} L)^2
+\tfrac H2|\nabla q|^2 .
$$
Sie ist punktweise koerziv bei $\mu>0$, $3\lambda_{\rm el}+2\mu>0$ und $H>0$. Mit $0<H<\rho_{\rm M}$ und $I>0$ sind beide Hauptblöcke am Eingang strikt positiv.

Auf der bewegten Bahn variieren die tatsächlichen Hessians mit Verschiebungsgradient, Materialgeschwindigkeit, Uhrenkoeffizienten und Zielmetrik. Bei festem glattem Schaltplan nähern sie sich für $\epsilon\to0$ gleichmäßig den Eingangsblöcken. Die programmierte Zielmetrik ist nahe der Einheitsmetrik, die Bahn hat $v=O(\epsilon)$, und der räumliche Uhrkorrekturkoeffizient ist auf der Sollbahn durch $d\theta+U_{\rm M}^{\flat}$ bestimmt und geht am Ruhepunkt auf null. Der konstante Zusatzterm bleibt eine Null-Lagrangedichte. Daher behalten $M$ und der räumliche Block $K=(K^{ij})$ auf dem kompakten betrachteten Raum-Zeit-Bereich eine gleichmäßige positive Untergrenze. Zum Beispiel genügt für jeden der beiden Blöcke, dass seine Abweichung im Operatornormmaß unter der Hälfte der kleinsten Eigenwertschranke am Eingang liegt. Dieses Argument setzt einen festen Schaltverlauf voraus. Steigende Schaltfrequenz bei fallender Auslenkung erfordert eine erneute Schrankenprüfung.

Für $v_y=\partial_t y$ und $w_i=\partial_i y$ lauten die Hauptgleichungen
$$
\begin{aligned}
M\partial_t v_y+(B^i+B^{i\mathsf T})\partial_i v_y-K^{ij}\partial_i w_j&=0,\\
K^{ji}(\partial_t w_i-\partial_i v_y)&=0 .
\end{aligned}
$$
Die unteren Terme sind hier unterdrückt. Die zweite Zeile folgt aus der Verträglichkeit der Ableitungen. Dadurch sind die räumlichen Hauptmatrizen symmetrisch, und die Zeitmatrix ist positiv. Die Gleichung $\partial_t y=v_y$ liefert gleichzeitig eine Kontrolle der ungedifferenzierten Störung.

Beim Speicher verwende $(\delta n,\delta v_{\rm R})$ als Variablen. Im lokalen Trägerruhesystem ist der eingefrorene Hauptteil am Sollwert $n=n_*$ ein akustisches System
$$
\partial_t\delta n+n_*\operatorname{div}\delta v_{\rm R}=0,\qquad
n_*m\,\partial_t\delta v_{\rm R}+\kappa\nabla\delta n=0 .
$$
Die Zeitmatrix nach Symmetrisierung ist $\operatorname{diag}(\kappa/n_*,n_*m\,I_3)$. Die räumlichen Kopplungen haben in beiden Zeilen den Faktor $\kappa$. Für positive $n_*,m,\kappa$ und kleine Trägergeschwindigkeit bleibt die Zeitmatrix auch in Laborkoordinaten positiv. Die Beiträge von $m(\theta,X)$ und $n_*(\theta,X)$ enthalten als Kräfte höchstens erste Ableitungen von $y$. Diese sind im reduzierten System Zustandsvariablen. Umgekehrt enthält die Druckkorrektur in den Matrix- und Uhrgleichungen $\delta n$ ohne Ableitung. Die 1-Form koppelt über ihren äußeren Ableitungsoperator. Beim Variieren ihres Rückzugs liefert der exakte Anteil nur einen Randterm, da der Teilchenstrom erhalten ist. Die verbleibenden Kräfte hängen von den Strömen und ersten Labelableitungen ab. So koppeln Speicher und Matrix-Uhr-System im reduzierten Hauptteil nicht über Ableitungen ihrer Erstordnungszustände. Zwei überlagerte Komponenten werden im Modell durch direkte Summe behandelt.

## Energieabschätzung im Inneren

Der resultierende lineare Zustand $Z$ aus $y,v_y,w_i,\delta n,\delta v_{\rm R}$ erfüllt
$$
A^0\partial_t Z+A^i\partial_i Z+C Z=F,\qquad A^\mu=A^{\mu\mathsf T},\quad A^0\ge a_0 I>0 .
$$
$F$ kann für freie Störungen auf null gesetzt werden. Sei $\Omega$ ein fester innerer Bereich mit positiver Hintergrunddichte und glatten Koeffizienten. Betrachte kompakt in $\Omega$ bleibende Störungen im zertifizierten Zeitintervall, oder einen Bereich mit nichtnegativem auswärts gerichtetem Energiefluss. Für $e(t)=\|Z(t)\|_{A^0}$ mit $e(t)^2=\int_\Omega Z^{\mathsf T}A^0 Z\,d^3x$ gilt
$$
\partial_t(Z^{\mathsf T}A^0Z)+\partial_i(Z^{\mathsf T}A^i Z)
=Z^{\mathsf T}(\partial_t A^0+\partial_i A^i-C-C^{\mathsf T})Z+2 Z^{\mathsf T}F .
$$
Bezeichne den halben räumlichen Supremumswert der Operatornorm von $(A^0)^{-1/2}(\partial_t A^0+\partial_i A^i-C-C^{\mathsf T})(A^0)^{-1/2}$ mit $\gamma(t)$. Dann ist
$$
e(t)\le e^{\int_{t_0}^t\gamma}\,e(t_0)
+\int_{t_0}^t e^{\int_\tau^t\gamma}\,\|(A^0)^{-1/2}F(\tau)\|_2\,d\tau .
$$
Die Rechnung braucht keine zusätzliche räumliche Ableitung der Zustandsdaten. Sie liefert für freie Fehler eine gleichmäßige Abschätzung über eine endliche Schaltzeit. Die Koeffizienten und ihre Ableitungen stammen aus der programmierten Bahn. Ein Rand mit einlaufenden Störungen erfordert seine eigene Flussbilanz. [Symmetrisch-hyperbolische Systeme, Friedrichs](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160070206)

## Weitergabe an einen äußeren Gezeitensensor

Im Folgenden seien die Störungen frei und räumlich in einer festen Quellenregion $\Omega$ vom Volumen $V$ enthalten. Der linearisierte Hilbert-Tensor ist auf diesen Lösungen erhalten. In der Spurkehre $S_{\mu\nu}=\delta T_{\mu\nu}-\eta_{\mu\nu}\delta T/2$ ist $S=\mathcal L_T Z$ mit glatten Koeffizienten. Alle nötigen ersten Ableitungen sind bereits Zustandsteile. Schreibe $C_T=\sup\|\mathcal L_T(A^0)^{-1/2}\|$, mit euklidischer Frobeniusnorm am Tensor. Dann gilt auf einem zertifizierten Zeitintervall $\mathcal I$
$$
\|S\|_{L^2(\mathcal I\times\Omega)}\le C_T\sqrt{|\mathcal I|}\sup_{t\in\mathcal I}e(t).
$$
Ein unabhängiger Antrieb mit eigener Energie und eigenem Impuls müsste für die gravitative Auswertung im erhaltenen Gesamttensor enthalten sein.

Für einen festen Außenmesspunkt $x_o$ mit Abstand mindestens $d>0$ zur Quelle wird die retardierte Metrik ohne unabhängige freie Welle aus $4G\int_\Omega S_{\mu\nu}(t-r,y)/r\,d^3y$ mit $r=|x_o-y|$ gebildet. Sei $\chi(t)$ ein glattes kompaktes Empfangsfenster und $\chi_\omega(t)=\chi(t)e^{i\omega t}$. Definiere das gemessene Fensterintegral einer festen Gezeitenkomponente als $\mathcal R_{ij}(\omega)=\int\chi_\omega(t)\,\delta R_{0i0j}(t,x_o)\,dt$. Alle zugehörigen retardierten Quellzeiten $t-r$ seien in $\mathcal I$ enthalten. Es wird am Empfänger gefenstert. Der Quelltensor wird nicht zeitlich abgeschnitten. [Retardierte Lösung, Carroll, Gl. 6.74](https://ned.ipac.caltech.edu/level5/March01/Carroll3/Carroll6.html)

Für den räumlichen Gradienten der retardierten Radialfunktion gelten die Gewichte $1/r$ und $1/r^2$ vor erster Zeitableitung und Wert. In der Hesse-Matrix sind es $1/r$, $2/r^2$, $2/r^3$ vor zweiter, erster und keiner Zeitableitung. Die Winkelmatrizen $nn^{\mathsf T}$ und $3nn^{\mathsf T}-I$ haben die Normen 1 und 2. In $\delta R_{0i0j}$ treten zwei gemischte Ableitungen, eine räumliche und eine doppelte Zeitableitung auf. Partielle Integration überträgt die Zeitableitungen auf $\chi_\omega$. Cauchy-Schwarz auf Quellraum und -zeit ergibt
$$
|\mathcal R_{ij}(\omega)|\le
2G\sqrt V\,\|S\|_{L^2(\mathcal I\times\Omega)}
\left(\frac{4\|\chi_\omega''\|_2}{d}
+\frac{4\|\chi_\omega'\|_2}{d^2}
+\frac{2\|\chi\|_2}{d^3}\right).
$$
Die Schiebung um die Laufzeit hängt vom Quellpunkt ab und ändert die Zeitnorm des jeweiligen verschobenen Empfangsfensters nicht. Die Abschätzung nutzt keine Fernfeldnäherung.

Für ein Band $|\omega|\le\omega_{\max}$ setze
$$
w_0=\|\chi\|_2,\quad w_1=\|\chi'\|_2+\omega_{\max}w_0,\quad
w_2=\|\chi''\|_2+2\omega_{\max}\|\chi'\|_2+\omega_{\max}^2w_0 .
$$
Eine hinreichende Toleranz der Anfangsstörung für einen gewöhnlichen Störgrenzwert $\mathcal R_{\max}$ ist damit
$$
e(t_0)\le
\frac{\mathcal R_{\max}}
 {2G\sqrt{V|\mathcal I|}\,C_T e^{\int_{\mathcal I}\gamma}
  (4w_2/d+4w_1/d^2+2w_0/d^3)} ,
$$
wobei $\mathcal I$ auch die Fortpflanzungszeit ab $t_0$ umfasst. Das ist eine konservative Schranke für das definierte Fensterintegral einer äußeren Gezeitenkomponente. Für eine Zahl im OP5-Messsignal sind Material- und Profilparameter, Empfängerfenster und die Übertragung von gewöhnlicher Gezeitenkrümmung in die tatsächlich gemessene Größe festzulegen. Randdynamik, Binnenfeld auf dem Messweg und native Higgs–OP5-Kopplung bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_schaltphase_fehlergrenze.wl) · [Tatsächliche Ausgabe](op5_j_schaltphase_fehlergrenze.txt) · [Laufmanifest](op5_j_schaltphase_fehlergrenze.json)

Wolfram kontrollierte den elastischen Nullterm, die akustische Symmetrisierung, die algebraische symmetrische Reduktion in einer eingefrorenen Raumrichtung, die variable Energieidentität sowie Gradienten und Hesse-Matrix des retardierten Kerns. Die Positivität entlang der Bahn und die Messschranke folgen analytisch. Reproduzierbar mit **wolframscript -file op5_j_schaltphase_fehlergrenze.wl**.
