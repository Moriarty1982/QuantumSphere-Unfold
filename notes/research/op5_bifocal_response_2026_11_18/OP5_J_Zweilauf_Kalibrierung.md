# OP5 – Zweilauf-Kalibrierung bei endlicher Strahlbreite

21. November 2026. Analytische Erkundung im Materieframe M. Signal- und Kalibrierlauf werden im statischen Einweg-Vergleich auf geraden parallelen Strahlen gemittelt. Die beiden idealen Feldmoden sind fest zugeordnet, und ihre nichtnegativen, normierten Quergewichte sind im jeweiligen Lauf rotationssymmetrisch und entlang der aktiven Strecke konstant. Das Kernmodell behandelt die gewöhnliche minimale Laufzeit und die beiden deklarierten Riemann-Kopplungen. Ein reales Modenexperiment wird dadurch parametrisiert.

## Vorwissen geprüft

Der [Binnenfeldabgleich](OP5_J_Binnenfeld_Messweg.md) gibt gewöhnliche Laufzeit, gewöhnliche Gezeitenkrümmung und das auf der Achse reine Kalibrierprofil. Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) liefert die Profilfamilie und den bisherigen Strahlbreitenfaktor für den OP5-Kontrast. Das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) behandelt Anschlussdrift und Phasensekante eines einzelnen Laufs. Die Suche nach Zweilauf-Kalibrierung, Modengewichten und Kalibrierfaktor in Vorab-Notizen, Forschungsnotizen und OP5-Analysen ergab dafür bisher keine gemeinsame finite Rechnung. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft sie die lokale Auslese. I3 setzt eine eigene kosmologische Bestandsdynamik voraus.

## Geometrische Polynome und ringförmiger Ausgleich

Sei $s=r_\perp^2/R^2$, $D=4(\partial_s+s\partial_s^2)/R^2$ und $P=b_0-b_2D+b_4D^2$ wie im Binnenfeldabgleich. Schreibe $W_\ell=\int V_\ell dz$ für den Längsschnitt des Profils im Lauf $\ell=S,C$ und $k_G=4\pi G v_{\rm H}\zeta$. Im flachen Zuschnitt sind die pro Radius azimutal gemittelten Kurven für gewöhnliche Laufzeit $L_\ell$, gewöhnlichen Gezeitenkontrast $G_\ell$ und OP5-Gezeitenkontrast $O_\ell$ gegeben durch
$$
L_\ell=2k_G P D^2 W_\ell,\qquad
G_\ell=-k_G P D^3 W_\ell,\qquad
O_\ell=-D^5 W_\ell/(4m^2).
$$
Hier ist für eine feste transversale Polarisation das azimutale Mittel von $\partial_e^2 f(s)$ gleich $Df/2$. Die Längsableitungen integrieren sich wegen der kompakten Endbereiche weg. Für das Signalprofil folgt
$$
O_S(s)=\frac{16 A_H a P_z}{m^2R^4}(1-36\kappa s),\qquad P_z=\int p(z)\,dz .
$$
$G_S$ ist ein Polynom höchstens dritten und $L_S$ höchstens vierten Grades, beide aus der im Binnenfeldabgleich angegebenen Potentialspalte. Die Mittelung einer Kurve $f=\sum_j f_j s^j$ für Modus $I$ im Lauf $\ell$ ist $\langle f\rangle_{\ell I}=\sum_j f_j\mu_{\ell I,j}$ mit $\mu_{\ell I,j}=\langle s^j\rangle_{\ell I}$ und $\mu_{\ell I,0}=1$.

Der frühere Ausgleichsterm $c_6 s^6$ lässt bei endlicher Strahlbreite
$$
O_C(s)=-\frac{132710400\,c_6P_z}{m^2R^{10}}\,s
$$
zurück. Der Ausgleich des Querintegrals kann vollständig aus dem Strahlkern gerückt werden. Wähle dazu eine glatte Ringfunktion $\beta(s)$ mit Träger außerhalb des gesamten benutzten Kerns und mit $B_0=\int\beta(s)\,ds\ne0$. Bei denselben $p,\chi$ gilt für
$$
V_C=p(z)\big[\chi(s)(c_2s^2+c_3s^3)+c_\beta\beta(s)\big],\qquad
c_2=\frac{36 b_2c_3}{b_0R^2},\qquad
c_\beta=-\frac{c_2M_2+c_3M_3}{B_0},\quad M_j=\int s^j\chi(s)\,ds
$$
weiterhin ein verschwindendes Querintegral. Die verwendeten Antworten auf der präparierten kompakten Bahn sind lokale Differentialausdrücke in $V_C$. Deshalb trägt der Ring im Inneren seines freigehaltenen Kerns nichts zu diesen Kurven bei. Innerhalb des flachen Zuschnitts und außerhalb des Ringträgers ergibt sich exakt
$$
O_C(s)=0,\qquad G_C(s)=g_C=-k_G b_0\frac{2304c_3P_z}{R^6},\qquad
L_C(s)=-\frac{R^2g_C}{2}s .
$$
Der gewöhnliche Gezeitenkontrast bleibt also bei jeder im Kern getragenen Modengewichtung gleich. Bei einem Gewichtsanteil $\varepsilon_{\rm tail}$ außerhalb des Kerns lässt sich der dadurch entstehende OP5-Mittelungsrest durch $\varepsilon_{\rm tail}\sup_{\rm außerhalb}|O_C|$ begrenzen, sofern außerhalb eine entsprechende Strahlrechnung vorliegt. Die Größe des Rests hängt von Profil und Lage des Rings ab.

## Zwei Moden und zwei Läufe

Seien $\lambda^O_I,\lambda^G_I$ die über beide Läufe konstanten Kopplungen an die jeweiligen Krümmungskanäle. Für $X=O,G$ bezeichne $X_\ell^+=(\langle X_\ell\rangle_{\ell J}+\langle X_\ell\rangle_{\ell A})/2$ und $X_\ell^-=\langle X_\ell\rangle_{\ell J}-\langle X_\ell\rangle_{\ell A}$. Dieselbe Plus- und Minuskonvention gilt für die Kopplungen. Mit dem gewöhnlichen Wegrest $B_\ell=\langle L_\ell\rangle_{\ell J}-\langle L_\ell\rangle_{\ell A}$ lautet die differentielle Laufzeit
$$
D_\ell=B_\ell+O_\ell^+\lambda_O^-+G_\ell^+\lambda_G^-
+O_\ell^-\lambda_O^++G_\ell^-\lambda_G^+ .
$$
Im Ringprofil gilt für Kernstrahlen $O_C^\pm=G_C^-=0$ und $G_C^+=g_C$. Selbst dort ahmt eine unbekannte Differenz der ersten Strahlmomente die gewöhnliche Krümmungskopplung nach, denn
$$
D_C/g_C=\lambda_G^- -\tfrac12R^2(\mu_{CJ,1}-\mu_{CA,1}).
$$
Diese Gleichung gibt direkt die erforderliche Kontrolle des ersten Moments für eine gewünschte Fehlergrenze an $\lambda_G^-$. Das gemessene erste Moment darf zwischen den Läufen variieren, sofern die Zuordnung und Korrektur stimmen.

Im Signallauf treten bei unterschiedlichen Modengewichten weiterhin die mittleren Kopplungen $\lambda_O^+,\lambda_G^+$ als Störparameter auf. Die zwei differentiellen Laufzeiten allein bestimmen dann im Allgemeinen $\lambda_O^-$ nicht. Gleiche Modenmomente bis Grad vier innerhalb des Signallaufs sind hinreichend, um dort alle Differenzgewichte in den drei Kurven zu eliminieren. Für den OP5-Kanal genügt bereits das erste, für den gewöhnlichen Gezeitenkanal genügen die ersten drei Momente. Die Laufzeitkorrektur kann bei bekannten Momenten auch direkt ausgerechnet werden. Bei nur beschränkt bekannten mittleren Kopplungen kann man $|\lambda_O^+ O_S^-|+|\lambda_G^+ G_S^-|$ als eigene Fehlergrenze ansetzen. Dies zeigt, welche Kalibrierinformation fehlt, wenn die Modengewichte auseinanderlaufen.

## Kondition und gemeinsame Fehlergrenze

Seien $O_\ell,G_\ell$ in diesem Abschnitt die gemittelten Plus-Größen. Sei $d_\ell$ der um gewöhnliche Wegfehler und bekannte weitere Beiträge korrigierte differentielle Messwert. Bei gleichen Modengewichten oder einem bilanzierten Fehler für die Minus-Größen gilt als Idealgleichung $d_\ell=O_\ell\lambda_O^-+G_\ell\lambda_G^-$. Das Zweilaufsystem ist invertierbar genau dann, wenn
$$
\det\begin{pmatrix}O_S&G_S\\O_C&G_C\end{pmatrix}\ne0 .
$$
Für $G_C\ne0$ setze $r=G_S/G_C$ und $K=O_S-rO_C$. Dann ist $\lambda_O^-=(d_S-rd_C)/K$. Das Ringprofil gibt $K=O_S$ für Kernstrahlen. Ein hinreichendes Kriterium für einen sicheren Signalnenner ist $36\kappa s_{\max}<1$ bei Strahlträger in $0\le s\le s_{\max}$. Dann ist $|O_S|\ge |O_S(0)|(1-36\kappa s_{\max})$. Die gewöhnliche Kalibrieramplitude kann auf der Achse an den Signallauf angepasst werden. Für endliche Breite ist $r$ aus den gemittelten Kurven zu bestimmen.

Für Schätzwerte mit Hut und garantierte absolute Koeffizientenfehler $\delta O_\ell,\delta G_\ell$ genügt bei $|\widehat G_C|>\delta G_C$
$$
\delta r=\frac{\delta G_S+|\widehat r|\delta G_C}{|\widehat G_C|-\delta G_C},\qquad
\delta K=\delta O_S+|\widehat r|\delta O_C+
                 (|\widehat O_C|+\delta O_C)\delta r .
$$
Die Fehler der Mittelung eines bekannten Polynoms sind durch $\sum_j |f_j|\delta\mu_j$ beschränkt. Weitere Unsicherheiten der Profilkoeffizienten werden zusätzlich propagiert. Seien $\eta_\ell$ die Fehlergrenzen des jeweils korrigierten Messwerts mit Anschlussdrift, Fehler der gewöhnlichen Wegkorrektur und gegebenenfalls beschränkten Minus-Beiträgen. Für $\widehat N=\widehat d_S-\widehat r\,\widehat d_C$ gilt
$$
\eta_N=\eta_S+|\widehat r|\eta_C+\delta r\bigl(|\widehat d_C|+\eta_C\bigr).
$$
Bei $|\widehat K|>\delta K$ ist für $\widehat\lambda=\widehat N/\widehat K$ der Fehler höchstens
$$
|\widehat\lambda-\lambda_O^-|
\le\frac{\eta_N+|\widehat\lambda|\delta K}{|\widehat K|-\delta K}.
$$
Insbesondere trennt $|\widehat N|>\eta_N$ die Null in diesem Modell aus. Alle Schranken sind deterministisch und verlangen keine Unabhängigkeit der Fehler.

Die Beiträge der Übertragungsmatrizen werden in jedem Lauf aus dem bisherigen gewichteten Rest berechnet. Für Normradien $r_{\ell1},r_{\ell2}$ der Eigenwertstörung an den beiden Bandenden genügt
$$
\eta_{\ell,\mathrm{mat}}=
\frac{2\big(\arcsin r_{\ell1}+\arcsin r_{\ell2}\big)}{\omega_2-\omega_1}
$$
bei getrennten Eigenwertkreisen und korrekter Phasenentfaltung. Eine Kalibrierphase nahe null kann die beiden Eigenwerte zusammenfallen lassen. Dann reicht die ungeordnete Eigenwertliste für eine **vorzeichenbehaftete** Kalibrierung nicht aus. Sie setzt unabhängig über beide Läufe zugeordnete Moden oder eine bekannte auflösbare Phasentrennung im jeweils tatsächlich gemessenen Quotienten voraus. Zusatzdrift der Anschlüsse muss in jedem Lauf in dessen Matrixrest enthalten sein. Frequenzabhängige Strahlgewichte sind an beiden Bandenden in die Phasensekante einzusetzen. [Eigenwertausschluss für normale Matrizen im Bauer–Fike-Rahmen](https://epubs.siam.org/doi/10.1137/S0895479802217928)

Im bisherigen Rechenbeispiel mit $100\,\mathrm{MHz}$ Bandabstand und $0{,}25\,\mathrm{ps}$ Gesamtziel ergibt bei $|r|=1$, exakter Kalibrierung und gleicher Aufteilung auf beide Matrixfehler eine erforderliche Schranke je Bandende von etwa $1{,}96\cdot10^{-5}$. Dies setzt eine ausreichend große Phasentrennung in beiden Läufen voraus. Bei je $10^{-8}$ additivem Gerätefehler, driftfreien Enden und zwei gleich empfindlichen Anschlüssen steigt die geforderte kleinste Singulärzahl pro Ende auf etwa $0{,}0319$. Bei der früheren idealisierten HCl/H-Zahl $0{,}00254$ verbleiben rund $6{,}33\cdot10^{-11}$ additiver Fehler pro Matrix. Diese Zahlen verwenden das gesamte Laufzeitbudget für die Matrixmessung. Gemessene Momente, Profilfehler und zusätzliche Drift können das verfügbare Budget weiter verkleinern. Beugung, weitere gewöhnliche Operatoren, reale Anschlusskalibrierung und native Higgs–OP5-Kopplung bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_zweilauf_kalibrierung.wl) · [Tatsächliche Ausgabe](op5_j_zweilauf_kalibrierung.txt) · [Laufmanifest](op5_j_zweilauf_kalibrierung.json)

Wolfram prüfte die Kernpolynome, den Rest des ursprünglichen Ausgleichsterms, die Mittelung mit zwei Modengewichten sowie die Quotientenidentitäten. Das Zahlenbeispiel wurde aus exakten Eingaben gerundet. Die Wirkung des Ringträgers folgt aus Kompaktheit und Lokalität der Profiloperatoren. Reproduzierbar mit **wolframscript -file op5_j_zweilauf_kalibrierung.wl**.
