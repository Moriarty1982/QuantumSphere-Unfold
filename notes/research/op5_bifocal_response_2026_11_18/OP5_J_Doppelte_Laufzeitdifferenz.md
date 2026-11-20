# OP5: Doppelte Laufzeitdifferenz und lokale Endpunktantwort

20. November 2026. Analytische Erkundung in M. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) trennt die freie differentielle J-Laufphase von den in geladenen Quell- und Detektorregionen möglichen Beiträgen. Hier wird geprüft, ob eine kontrollierte Änderung der D-Säule diese Beiträge trennen könnte. Wir setzen eine ebene, statische Referenzgeometrie, eine lineare Messkette und zwei reproduzierbare D-Profile voraus. Der Apparat und die Kontrolle der D-Population sind Annahmen. Es erfolgt kein H96-Datenvergleich.

## Phase einer Übertragungsfunktion

Sei $I=J,A$ für den J-Kanal und das elektromagnetische Referenzfeld und $s=0,1$ für zwei Profile derselben Anordnung. Im Einwegmodell ohne relevante Mehrfachreflexionen schreibe die komplexe Übertragungsfunktion bei einer gemeinsamen Frequenz $\omega$ als
$$
H_I^{(s)}(\omega)=E_I^{(s)}(\omega)\,P_I^{(s)}(\omega)\,R_I^{(s)}(\omega).
$$
$E_I$ und $R_I$ beschreiben die lokale Einspeisung und Auslese einschließlich ihrer Phasen, $P_I$ die Ausbreitung zwischen ihnen. Die vier Funktionen müssen im verwendeten Frequenzfenster von null verschieden sein. Für den Zeitfaktor $e^{-i\omega t}$ hat eine ideale Verzögerung $\tau$ den Faktor $e^{+i\omega\tau}$. Entsprechend ist die Gruppenlaufzeit hier $\partial_\omega$ der stetig entfalteten Übertragungsphase. [Keysight, Gruppenlaufzeit aus der Phase einer Übertragungsfunktion](https://helpfiles.keysight.com/csg/89600B/Webhelp/Subsystems/gui/content/trace_format_groupdelay.htm)

Die beobachtbare doppelte Differenz ist
$$
\Delta\tau_{\rm mess}
=\partial_\omega\arg\left[\frac{H_J^{(1)}H_A^{(0)}}{H_J^{(0)}H_A^{(1)}}\right].
$$
Sind die beiden Endfaktoren jedes Kanals über die Profiländerung unverändert, fallen sie algebraisch heraus. Sie brauchen nicht zwischen den Kanälen gleich zu sein. Bei veränderten Endfaktoren ist ihr verbleibender Beitrag die entsprechende Differenz ihrer Phasensteigungen. Die Produktform setzt einen identifizierten Einzelpfad voraus. Ein Interferometer mit unbehandelten zusätzlichen Pfaden oder eine resonante Messkette erfordert eine eigene Übertragungsrechnung.

## Endliche Reichweite im planaren Modell

Lege die Ausbreitungsstrecke auf $0\le z\le L$. Beide Profile unterscheiden sich nur in der ruhenden D-Dichte $\delta\rho=\rho_1-\rho_0$; deren Träger liegt zwischen $d$ und $L-d$, mit $0<d<L/2$. Die übrige Geometrie und die sichtbare Materie seien festgehalten oder ihr gemeinsamer Beitrag unabhängig entfernt. Im linearen massiven Modell und für eine planare D-Verteilung ist der statische Nenner $q_z^2+m^2$. Für den transversalen J–A-Unterschied definiere die normierte Faltung
$$
K_m(z)=\frac{m}{2}e^{-m|z|},\qquad
\delta\rho_m=K_m*\delta\rho,\qquad
\int_{\mathbb R}K_m(z)\,dz=1.
$$
Die Faltung ersetzt die lokale D-Dichte, während der Faktor $1/m^2$ im gemischten Koeffizienten erhalten bleibt. Die Quellen- und Detektorbeiträge sind hier noch nicht in die Ausbreitungsphase eingerechnet. In erster Ordnung in den Kopplungen und im langsam veränderlichen, reflexionsarmen Vergleich ist
$$
\Delta\tau_{\rm prop}
=\frac{(g_J-g_A)g_D}{m^2}\int_0^L \delta\rho_m(z)\,dz.
$$
Wir verwenden natürliche Einheiten wie in der vorigen Notiz. Die Frequenzabhängigkeit des führenden Phasenbeitrags kommt aus dem Faktor $\omega$; weitere Dispersion würde eine eigene Gruppenlaufzeitkorrektur ergeben.

Der über die endliche Strecke gefaltete Säulenbeitrag lässt sich genau integrieren:
$$
\int_0^L \delta\rho_m(z)\,dz
=\int_d^{L-d}\!\delta\rho(z')
\left[1-\tfrac12e^{-mz'}-\tfrac12e^{-m(L-z')}\right]\,dz'.
$$
Die Abweichung von $\int\delta\rho\,dz$ ist also betragsmäßig höchstens $e^{-md}\|\delta\rho\|_1$. Die Schranke gilt auch für eine vorzeichenwechselnde Profiländerung; dann ist sie eine absolute und keine relative Schranke. Als Kontrolle ergibt eine normierte Teststufe auf $[3,7]$ mit $m=2$, $L=10$ die gefaltete Säule $3{,}99876103968$ statt $4$. Eine direkte Mittelpunktintegration stimmt bis auf etwa $2{,}1\times10^{-12}$ relativ mit der Randformel überein. Die Teststufe kontrolliert die Faltung, nicht die Annahmen zur Wellenausbreitung.

## Was an Sender und Empfänger noch bleibt

Liegt ein Punkt der Apparatur mindestens $d_{\rm app}>0$ vom Träger der Profiländerung entfernt, folgt für jede feste Ableitungsordnung $j$
$$
|\partial_z^j\delta\rho_m(z)|
\le \frac{m^{j+1}}2 e^{-m d_{\rm app}}\|\delta\rho\|_1 .
$$
Daher ist die Änderung des statischen Vermittlerhintergrunds an beiden Enden in dieser Geometrie exponentiell klein. Das gilt auch für seine zweiten Ableitungen, an die der vorher berechnete longitudinale Zusatz in der lokalen Entwicklung anschließt. Die Schranke bezieht sich auf das veränderte Hintergrundfeld. Sie wird erst dann zur Schranke für eine Endpunktphase, wenn die entsprechenden lokalen Apparaturempfindlichkeiten endlich und bekannt sind. Direkte Änderungen der sichtbaren Last, rücklaufende Wellen und gravitative beziehungsweise frequenzabhängige Kalibrierung sind damit nicht automatisch eliminiert.

Unter den genannten Voraussetzungen ist die doppelte Differenz ein Messmodell für eine Änderung der D-Massensäule. Sie bestimmt ohne Kalibrierung nur das Produkt aus Säulenänderung und Spin-2-Kopplung. Ein realer Aufbau, die kontrollierte Profiländerung, die Endpunktantwort und die kosmologische Zuordnung zu H96 bleiben offen.
