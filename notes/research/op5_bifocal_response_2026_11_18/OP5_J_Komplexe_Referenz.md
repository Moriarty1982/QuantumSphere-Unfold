# OP5 – Genauigkeit der komplexen A-Referenz im Messband

21. November 2026. Analytische Erkundung im Materieframe M. Für den homogenen passiven Zweikanalmarker wird das nach dem Rücklauf verbleibende Budget rückwärts in eine Mess- und Dispersionsanforderung übersetzt.

## Vorwissen geprüft

Der [Zweikanalmarker](OP5_J_Zweikanal_Marker.md) liefert die Spurauslese mit allgemeiner Vorwärtsmatrix. Die [Rang-eins-Feldreferenz](OP5_J_Feldreferenz.md) bestimmt das illustrative Budget bei idealem Hub. Die [Rücklauftoleranzen](OP5_J_Ruecklauf_Toleranzen.md) liefern die gleichmäßige Reflexionsgrenze und getrennte Amplituden- und Phasenreserven. Die [Anschlusskondition](OP5_J_HCl_Anschlusskondition.md) behandelt den kleinsten Signalgewinn der HCl/H-Anschlüsse. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft die Rechnung die lokale Auslese. I3 benötigt eine eigenständige Bestandsdynamik.

## Budget für die gemessene Feldreferenz

Für diagonalen Solltransport $U=\operatorname{diag}(z_J,z_A)$ mit $|z_i|=1$ liefert die Spurauslese den Kontrast der Diagonaleinträge der tatsächlichen Einzelpassmatrix $T$. Sei $T_{\rm cal}=T+\operatorname{diag}(\delta_J,\delta_A)$ die Matrix mit den eingesetzten kalibrierten Diagonaleinträgen und unveränderter außerdiagonaler Antwort. Dann gilt $\|T-T_{\rm cal}\|=\max(|\delta_J|,|\delta_A|)=e_{\rm ref}$. Eine separat bereits bekannte J-Diagonale erlaubt also, dieses Budget allein für A einzusetzen. Andernfalls müssen beide Diagonalen dieselbe Genauigkeit erfüllen. Ohne Matrixfehler lautet der exakte modale Fehler, bei $\widehat\tau_i=T_{{\rm cal},ii}$ und $\tau_i=T_{ii}$,
$$
\widehat z_J-z_J=-(\widehat z_A-z_A)
=\frac{(\tau_J-\widehat\tau_J)z_J+(\tau_A-\widehat\tau_A)z_A}
{\widehat\tau_J-\widehat\tau_A}.
$$

Mit $D=|\widehat\tau_J-\widehat\tau_A|$ und $m=\max(|T_{JA}|,|T_{AJ}|)$ ist die Spurnorm des Selektors $T_{\rm cal}-\widehat\tau_i I$ durch $D+2m$ begrenzt. Für Quotientenfehler $r_Q$ der Vergleichsstrecke und $r_T$ relativ zu $T_{\rm cal}$ ist jeder Modalfehler somit höchstens
$$
\left(1+\frac{2m}{D}\right)r_Q+\frac{2(1+r_Q)}{D}r_T .
$$
Sei $r_T\le r_{\rm rück}+e_{\rm ref}+r_{\rm sonst}$, wobei alle drei Beiträge in derselben Feldbasis als additive Operatornormen bzw. Schranken vorliegen. Wird ein Rückweg bereits in der Referenz mitgemessen, muss dessen Rest gegenüber dieser Referenz angesetzt werden. Hier wird der volle Einzelpass-Rücklaufwert $r_{\rm rück}=3{,}513\cdot10^{-6}$ aus der Vorarbeit verwendet.

Im bisherigen 100-MHz-Beispiel sind $r_Q=9{,}81742885\cdot10^{-6}$ und $e_z=\sin(2\pi\,10^8/(32\cdot10^{12}))$ die illustrativen Werte. Für die Einzelpassmatrix liefert die skalare Schicht $|1-t_A|\ge 1+e^{-A_{\max}v}\cos\phi_{\max}-2\rho^2/(1-\rho^2)$, mit $\phi_{\max}$ als Drift der Ausbreitungsphase um $\pi$. Der zweikanalige Kontrastrest aus der Vorarbeit ist höchstens $F_0\bigl(\theta x+2\theta^2/(1-\theta)\bigr)$, weil $C e_d\le\theta x$ gilt. Damit liegt der Kontrast von $T$ über $1{,}9921230$. Die volle Normgrenze $F_0\theta/(1-\theta)$ liefert $m<0{,}00317$. Für Kandidaten mit $e_{\rm ref}\le10^{-5}$ folgt $D\ge1{,}992$, denn der Kontrast verschiebt sich um höchstens $2e_{\rm ref}$. Rückwärts aus dem geforderten Modalradius folgt die hinreichende Bedingung
$$
e_{\rm ref}+r_{\rm sonst}\le
\frac{1{,}992(e_z-r_Q)-2(0{,}00317)r_Q}{2(1+r_Q)}
-r_{\rm rück}
=6{,}2340382\cdot10^{-6}.
$$
Weitere Instrumentenfehler der Markierung teilen dieses Budget. Hier wurde $r_Q$ auf dem früheren Vergleichswert festgehalten. Die Zahl ist eine hinreichende Reserve unter dieser Aufteilung.

## Zentralwert und Dispersion

Für die skalare A-Referenz sei $\widehat t_A(f_0)$ eine Messung mit Fehler höchstens $\eta_0$, die konstant über das 100-MHz-Band eingesetzt wird. Mit $A_c=k_A(f_0)L$, $u=\sup|f/f_0-1|$, $n_c=n(f_0)$ und $\sigma=\sup|n(f)-n_c|$ gilt für den Unterschied der komplexen Ausbreitungsargumente
$$
|A(f)(n(f)-1)-A_c(n_c-1)|
\le A_{\max}\sigma+u A_c|n_c-1|.
$$
Die obere Halbebene liefert eine Einheits-Lipschitzgrenze für die Ausbreitungsexponentialfunktion. An beiden Frequenzen zusammen ist der Unterschied gegenüber der exakten Schichttransmission durch $4\rho^2/(1-\rho^2)$ abgedeckt. Folglich ist der reine skalare Referenzfehler höchstens
$$
\eta_0+A_{\max}\sigma+u A_c|n_c-1|+\frac{4\rho^2}{1-\rho^2}.
$$
Die letzten zwei Summanden betragen im bisherigen Toleranzmodell zusammen höchstens $1{,}81745\cdot10^{-6}$. Wenn dieser skalare Vergleich die A-Diagonale modelliert und sonstige Reste separat abgedeckt sind, genügt bei idealer Zentralmessung $\sigma\le1{,}4058\cdot10^{-10}$. Bei $\eta_0=2\cdot10^{-6}$ genügt $\sigma\le7{,}6922\cdot10^{-11}$, oder als hinreichende Ableitungsgrenze $\sup|\partial_fn|\le1{,}5384\cdot10^{-18}\ {\rm Hz}^{-1}$. Diese Zahlen setzen den gesamten Rest für die angeführten Fehler ein. Für einen beliebigen komplexen Referenzfehler gilt der Budgetwert aus dem vorigen Abschnitt direkt.

Die bisherige Schichttoleranz beschränkt den Index punktweise um $n_0$. Sie liefert keine ausreichend kleine Änderung gegenüber $n_c$. Schon die reelle lineare Rampe $n(f)=n_0+2{,}5\cdot10^{-7}(f-f_0)/(50\,{\rm MHz})$ bei Solldicke und ohne Verlust bleibt in der Toleranzbox. Sie hat den nominalen Zentralwert und eine komplexe Abweichung des skalaren $t_A$ am oberen Bandrand von $7{,}85577\cdot10^{-3}$. Auch glatte Dispersion kann daher eine Zentralmessung ohne eigene Dispersionsschranke unzureichend machen.

Die Übertragung vom skalaren $t_A$ auf den tatsächlichen gekoppelten Diagonaleintrag $T_{AA}$ erfordert zusätzlich dessen Modellrest. Für $T_{AA}$ verschwindet die erste Korrektur, die vorhandene Reihenabschätzung für den Rest ist aber $F_0\theta^2/(1-\theta)\simeq9{,}968\cdot10^{-6}$. Sie übersteigt bereits allein das Referenzbudget. Die skalare Dispersionsrechnung zertifiziert daher die Kalibrierung des gekoppelten Markers erst mit einer schärferen Restschranke oder einer Messung der tatsächlichen Diagonale.

## Referenz an den Bandenden

Die bisherige Laufzeitdifferenz liest die beiden Bandendpunkte mit stetig zugeordneten Moden und gewähltem Phasenzweig. Für den Kalibrierbeitrag an diesen beiden Punkten reichen komplexe Messungen der tatsächlichen Diagonaleinträge an beiden Enden, sofern die obige Genauigkeit in der gemeinsamen Feldbasis erreicht wird. Für eine gleichmäßige Referenz im ganzen Band kann man zwischen den zwei Messwerten linear interpolieren. Haben beide Messungen Fehler höchstens $\eta_{\rm end}$ und hat der tatsächliche komplexe Diagonaleintrag zweite Frequenzableitung mit Norm höchstens $M$, ist der Fehler höchstens
$$
\eta_{\rm end}+M(\Delta f)^2/8.
$$
Das folgt durch zweimaliges Integrieren mit dem Dirichlet-Green-Kern des Intervalls, dessen Betragsintegral im Mittelpunkt maximal ist. Die Betragsgrenze gilt damit auch für komplexe Transmission. Bei $\eta_{\rm end}=2\cdot10^{-6}$ und $\Delta f=100$ MHz reicht $M\le3{,}3872\cdot10^{-21}\ {\rm Hz}^{-2}$, wenn das restliche Budget für die Interpolation zur Verfügung steht. Das spricht für eine Messung der komplexen Diagonalen an beiden Enden der Laufzeitmessung. Den phasenstetigen Zweig, die tatsächliche Projektionsbasis und den geometrischen HCl/H-Anschluss prüft diese Kalibrierung nicht. Freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_komplexe_referenz.wl) · [Tatsächliche Ausgabe](op5_j_komplexe_referenz.txt) · [Laufmanifest](op5_j_komplexe_referenz.json)

Wolfram bestätigt den exakten modalen Fehler und wertet die analytischen Normgrenzen sowie das explizite lineare Dispersionsbeispiel aus. Qiskit wurde erwogen. Die Rechnung verwendet komplexe Transferkoeffizienten und algebraische Abschätzungen im Materieframe, ohne Quantenschaltung. Reproduzierbar mit **wolframscript -file op5_j_komplexe_referenz.wl**.
