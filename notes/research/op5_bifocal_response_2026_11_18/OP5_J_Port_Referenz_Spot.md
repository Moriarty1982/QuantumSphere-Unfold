# OP5 – Richtungsselektiver Anschlussabgleich, feste Referenzen und endliche Spots

21. November 2026. Analytische Erkundungen im Materieframe M. Fortgesetzt werden die [Anschluss-, Pilot- und Polarisationsprüfung](OP5_J_Anschluss_Pilot_Polarisation.md) und das [HCl/H-Konditionsmodell](OP5_J_HCl_Anschlusskondition.md). Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 erfordert eine unabhängige kosmologische Bestandsdynamik.

## Welche Portdaten die Kreuzreflexion bestimmen

Am äußeren Anschluss werde mit abgeglichener innerer Last die komplexe Gerätematrix $M=LDF$ gemessen. $F$ setzt Ansteuerungen in einlaufende Feldamplituden um und $L$ misst auslaufende Feldamplituden. Für eine beliebige unbekannte Anschlussmatrix $D$ ist der einzelne Eintrag $D_{AJ}$ genau dann bestimmt, wenn $e_J\in\operatorname{im}F$ und $e_A\in\operatorname{im}L^\dagger$. Für $Fu=e_J$ und $L^\dagger v=e_A$ gilt $D_{AJ}=v^\dagger M u$. Ist eine der Richtungen unerreichbar, gibt es eine Rang-eins-Störung von $D$ mit verschwindender Gerätematrix und einem nichtverschwindenden $AJ$-Eintrag. Damit kann auch eine singuläre Gesamtmatrix einen gezielten Eintrag liefern, wenn die beiden passenden Richtungen unabhängig verfügbar sind.

Bei genau bekannten Ports und $\|\widehat M-M\|\le\epsilon_M$ ist der Fehler höchstens $\|u\|\|v\|\epsilon_M$. Normminimale Lösungen oder eine unabhängige A-Projektion können die Fehlerverstärkung gegenüber der vollständigen Matrixinversion reduzieren. Wenn beide benötigten Richtungen effektiv nur einen Gain von $0{,}00254$ haben, genügen für eine absolute Eintragsgenauigkeit von $2\cdot10^{-7}$ höchstens $1{,}29032\cdot10^{-12}$ in der normierten Gerätematrix. Bei einem unabhängig kalibrierten A-Empfang mit Gain eins und demselben J-Sendegain ergibt sich $5{,}08\cdot10^{-10}$. Die Zahl $0{,}00254$ ist aus dem idealisierten schwachen HCl/H-Winkelvergleich entnommen. Sie ist keine gemessene richtungsabhängige Verstärkung und auch keine Garantie einer unteren Singulärzahl.

## Direkte Projektion mit gemessener Modenreinheit

Für eine nominelle J-Einspeisung $(\alpha,1)^{\mathsf T}$ und A-Empfangszeile $(1,\beta)$ in der Feldbasis ergibt sich nach kohärentem Gainabgleich
$$
m_{AJ}=D_{AJ}+\alpha D_{AA}+\beta D_{JJ}+\alpha\beta D_{JA}+\epsilon.
$$
Die Amplitudenverhältnisse $\alpha,\beta$ umfassen die tatsächlich verbleibenden Projektionsfehler. Für $\|D\|\le10^{-4}$, $|\alpha|,|\beta|\le4\cdot10^{-4}$ und $|\epsilon|\le10^{-7}$ beträgt die Eintragsunsicherheit höchstens $1{,}80016\cdot10^{-7}$. Ein Anzeigegrenzwert von $8{,}19984\cdot10^{-7}$ zertifiziert unter diesen Bedingungen $|D_{AJ}|\le10^{-6}$. Die additive Grenze umfasst eine gegebenenfalls verbleibende Fehlanpassung der inneren Terminierung und den kalibrierten komplexen Gainrest. Damit ist die direkte Messung nur dann informativer als die Inversion, wenn gerade diese lokale J-Einspeisung und A-Empfangsrichtung nachgewiesen werden.

Bei einem passiven Durchgangsblock mit Norm höchstens eins gilt dieselbe Identität. Bei sonst gleichen Werten ist die Eintragsunsicherheit dann $8{,}0026\cdot10^{-4}$. Werden beide Kreuzrichtungen separat gemessen, ist die Norm des außerdiagonalen Teils das Maximum der beiden Eintragsbeträge. Die bisherige illustrative Mischgrenze $0{,}01$ ist damit unter denselben Bedingungen prüfbar. Das Reflexionsziel benötigt die absolute komplexe Prüfung an jeder der beiden Frequenzen und in allen relevanten Marker-/Schalterzuständen.

## Stationäre Referenzabschnitte und rohe Phasenmessung

Beim Zwei-Längen-Vergleich fällt jede Phase der Form $h_i+h_f$ in der doppelten Differenz $\Delta_i\Delta_f$ weg. Eine einzelne kohärente Messkette kann die freie Strecke ändern, wenn ihre Sende- und Empfangsreferenzen und die Überführung der bewegten Empfangsphase entsprechend abgeglichen sind. Zwei alternative feste Arme haben im Allgemeinen unterschiedliche chromatische Schaltphasen. Dann muss der gemischte Rest $|\Delta_i\Delta_f h|$ unabhängig bestimmt werden. Für die Längenphase bleibt ein kohärenter Phasenanker nötig. Auf diese Weise wird der gemischte Referenzfehler als eigener Messwert erfasst.

Sei $S$ der Abstand der modellierten Zweibandkontraste. Für vier komplexe A- und vier J-Rohwerte, deren additive Fehler je Messwert relativ zur gemessenen Amplitude durch $r_A,r_J<1$ begrenzt sind, genügt für getrennte Fehlerintervalle
$$
B_{\rm geom}+|\Delta_i\Delta_f h|+4\arcsin(r_J)+4\arcsin(r_A)<S/2 .
$$
$B_{\rm geom}$ ist eine für beide Modelle gültige Restgrenze des Wegterms. Aus dem früheren 4-m-Beispiel folgt $S\simeq8{,}3842185\cdot10^{-4}$ rad. Ohne weitere Beiträge sind bei gleichen Rohfehlern $r_A=r_J<5{,}2401\cdot10^{-5}$ hinreichend. Für $r_J=10^{-4}$ muss der A-Rohfehler unter $4{,}8027\cdot10^{-6}$ bleiben. Bei stattdessen unabhängig begrenzter A-Paarphase $\delta_A$ tritt $2\delta_A$ an Stelle von $4\arcsin(r_A)$. Mit dem früheren Wert $\delta_A=2\cdot10^{-6}$ rad und $r_J=10^{-4}$ bleiben etwa $1{,}5211\cdot10^{-5}$ rad für zusätzliche Beiträge. Als alleiniger gemischter Referenzrest entspricht dies einer mittleren Änderung der differentiellen Referenzgruppenlaufzeit von höchstens rund $24{,}21$ fs über 100 MHz. Die Umrechnung folgt durch Integration der Frequenzableitung der entfalteten Referenzphase.

Stationäre Referenzen beseitigen keine längenabhängigen Echos. Für ein isoliertes skalares Zweispiegelecho $D/(1-qe^{i\vartheta})$ mit $q=|r_1r_2|<1$ ist der Phasenfehler höchstens $\arcsin q$. Bei gleicher Reflexionsstärke und dieser einzigen Fehlerquelle entspricht die symmetrische Rohfehlergrenze rund $42{,}81$ dB Rückflussdämpfung je Spiegel. Weitere Pfade und A/J-Umwandlungen müssen in die komplexe Mehrweggrenze einbezogen werden. Das skalare Zweispiegelmodell liefert dafür keine Schranke.

## Endliche runde Spots im Polarisationsprofil

Im kompensierten Modell aus der Vorarbeit sind die radiale massive Weyl-Antwort proportional zu $s=b^2/R^2$ und die gewöhnliche proportional zu $s f(s)$, $f(s)=a_0+a_1s+qs^2$. Betrachte identische rotationssymmetrische Spots um die Mittelpunkte $(b,0)$, mit festen radialen und tangentialen Analyseachsen am jeweiligen Mittelpunkt. Ihr Träger liege vollständig im flachen Profilkern. Setze $m_2=\langle\rho^2\rangle/R^2$ und $m_4=\langle\rho^4\rangle/R^4$ für den Radius $\rho$ relativ zum Spotmittelpunkt. Die Winkelmomente von $(x^2-y^2)(x^2+y^2)^j$ für $j=0,1,2$ geben für die beiden gemittelten Spalten
$$
s,\qquad s f_{\rm eff}(s),\qquad
f_{\rm eff}(s)=a_0+a_1(s+3m_2)+q(s^2+8s m_2+6m_4).
$$
Der quadratische Koeffizient $q$ bleibt erhalten. Gleiche Spotmomente sind wesentlich. Unterschiede $\delta m_{2,i},\delta m_{4,i}$ ändern die gewöhnliche Spalte um $s_i[(3a_1+8qs_i)\delta m_{2,i}+6q\delta m_{4,i}]$.

Für $h=s_0/4$, $s_i=ih$ und $i=1,2,3$ seien $v_i=s_i$, $w_i=s_i f_{\rm eff}(s_i)$. Der Kontrastvektor $(3,-3,1)$ annihiliert $v$ und liefert $6qh^3$ auf $w$. Somit ist der Abstand von $w$ zur Geraden durch $v$ mindestens $6|q|h^3/\sqrt{19}$. Für die Matrix $[v,w]$ folgt in dieser Spaltennormierung aus dem Gramdeterminanten und $\sigma_{\max}\le\|v\|\sqrt{1+F^2}$,
$$
\sigma_{\min}\ge\frac{6|q|h^3}{\sqrt{19}\sqrt{1+F^2}},\qquad F=\max_i|f_{\rm eff}(s_i)|.
$$
Bei bekanntem Profil und unabhängig je Spot begrenztem Messfehler $\eta$ ist die Abweichung des geschätzten Koeffizientenvektors höchstens $\sqrt3\eta/\sigma_{\min}$. Für zwei profilierte Amplituden müssen die Spotparameter und die gewöhnliche Form bis auf ihre gemeinsame Amplitude bekannt sein. Insbesondere ist ein frei einstellbarer konstanter Term in $f_{\rm eff}$ mit der massiven Spalte entartet. Für kreisförmig begrenzte Spots an allen drei Orten genügt Radius $a<R\sqrt{s_0}(1-\sqrt3/2)$.

Diese Resultate gelten für die deklarierten Vergleichsmetriken. Reale Anschlussmessungen, freie J-Ausbreitung, die effektive Vermittlermetrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram prüfte die Portprojektion, das Rohphasenbudget, die Referenzkürzung, die Winkelmomente und den Drei-Spot-Kontrast. Qiskit wurde für diese klassischen komplexen Mess- und Tensorrechnungen erwogen.

[Wolfram-Skript](op5_j_port_referenz_spot.wl) · [Tatsächliche Ausgabe](op5_j_port_referenz_spot.txt) · [Laufmanifest](op5_j_port_referenz_spot.json)
