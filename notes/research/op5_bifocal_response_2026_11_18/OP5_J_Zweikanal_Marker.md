# OP5 – Zweikanalstreuung am getrennten Feldmarker

21. November 2026. Analytische Erkundung im Materieframe M. Eindimensionaler Vergleich bei fester Frequenz mit zwei offenen Kanälen A und J. Die freien Wellenzahlen und Flussnormen dürfen verschieden sein. Die Kopplungsrichtung und das in beiden Außenräumen konstante freie Materialgesetz sind Modellparameter.

## Vorwissen geprüft

Der [passive Vorwärtshub](OP5_J_Passiver_Vorwaertshub.md) verwendet gleiche Wellenzahlen und Impedanzen und liefert in diesem Grenzfall einen skalaren hellen Kanal. Die [Rang-eins-Feldreferenz](OP5_J_Feldreferenz.md) und das [Zweilaufbudget](OP5_J_Zweilauf_Kalibrierung.md) geben die Anforderungen an eine kalibrierte Modenzuordnung. Die Suche nach unterschiedlichen Wellenzahlen, Impedanz und gekoppelter Rückstreuung ergab im lokalen A/B-Zweig keine solche Markerschicht. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Streumodell und exakte Schichtrechnung

Seien $K=\operatorname{diag}(k_J,k_A)$ mit $k_i>0$, $P=\operatorname{diag}(p_J,p_A)$ mit $p_i>0$ und $D=PK$. $D$ ist die Admittanz für die hier gewählten Feldamplituden. Der Marker liegt in $0<z<L$ und ändert in diesem Modell nur den lokalen Feldterm. Für Zeitabhängigkeit $e^{-i\omega t}$ gilt
$$
(P\psi')'+PK^2\psi+V(z)\psi=0,\qquad V(z)=g(z)vv^\dagger
$$
mit konstanter Dipolrichtung $v$. Der Fluss ist $\operatorname{Im}(\psi^\dagger P\psi')$. Seine Ableitung beträgt $-\psi^\dagger(\operatorname{Im}V)\psi$, wobei $\operatorname{Im}V=(V-V^\dagger)/(2i)$. Für einen passiven Marker ist diese Matrix positiv semidefinit. Eine freie Welle mit Feldamplitude $D^{-1/2}a$ hat Fluss $\|a\|^2$ nach rechts beziehungsweise $-\|a\|^2$ nach links.

Für konstantes $V$ in der Schicht setze
$$
G=\begin{pmatrix}0&P^{-1}\\-PK^2-V&0\end{pmatrix},\qquad
W=\begin{pmatrix}D^{-1/2}&D^{-1/2}\\ iD^{1/2}&-iD^{1/2}\end{pmatrix},
\qquad B=W^{-1}e^{LG}W.
$$
Die an den Grenzflächen stetigen Größen sind $\psi,P\psi'$. Der freie Auslauf bei ausschließlich linker Einspeisung liefert aus den $2\times2$-Blöcken von $B$
$$
R=-B_{--}^{-1}B_{-+},\qquad
T=e^{-iKL}\bigl(B_{++}-B_{+-}B_{--}^{-1}B_{-+}\bigr).
$$
$T$ ist auf freie Durchleitung normiert. Die Formel gilt bei invertierbarem $B_{--}$ für komplexe Kopplung und endliche Phase einschließlich Innenreflexionen. Bei $k_J=k_A$ lässt sich die Schicht durch die Skalierung $P^{1/2}\psi$ in eine helle und eine dunkle Richtung zerlegen, auch bei unterschiedlichen $p_i$. Die helle Richtung ist dann zur flussgewichteten Dipolrichtung proportional. Bei ungleichen $k_i$ ist die freie Diagonalmatrix im Allgemeinen nicht mit dem Projektor der Schicht verträglich. [Mehrkanalige Streu- und Transfermatrizen, Byrnes und Foreman](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.3.013129)

## Phasenanpassung der schwachen Streuung

Schreibe $q=D^{-1/2}v$. Mit dem auslaufenden eindimensionalen Green-Kern ergibt die erste Born-Ordnung
$$
(T-I)_{ij}=\frac{i}{2}q_i\overline q_j\int_0^L g(z)e^{i(k_j-k_i)z}\,dz,\qquad
R_{ij}=\frac{i}{2}q_i\overline q_j\int_0^L g(z)e^{i(k_j+k_i)z}\,dz.
$$
Für eine konstante Schicht sind die Betragsfaktoren die entsprechenden $\operatorname{sinc}$-Funktionen mit Argument $(k_j-k_i)L/2$ beziehungsweise $(k_j+k_i)L/2$. Die direkte Vorwärtsphase bleibt durch das Integral von $g$ bestimmt. Modenumwandlung in Vorwärtsrichtung und Rückstreuung lesen unterschiedliche räumliche Frequenzen des Markers.

Die Determinante der **ersten** Vorwärtskorrektur ist für konstantes $g$ gleich
$$
(igL/2)^2\,|q_Jq_A|^2\,\bigl[1-\operatorname{sinc}^2((k_J-k_A)L/2)\bigr].
$$
Sie hat damit bei nichtverschwindenden beiden Kopplungen und verschiedenen Wellenzahlen Rang zwei, obwohl der lokale Materialterm Rang eins hat. Das ist eine Aussage zur Ordnung eins der Vorwärtsmatrix. Für einen rein elektrischen Marker mit $q_J=0$ bleibt die Rang-eins-Struktur auch bei ungleichen Wellenzahlen exakt. Für eine Schicht mit gemischter Richtung ist die Kohärenzskala $|k_J-k_A|L/2\ll1$ ein Kriterium für die Rang-eins-Näherung. Bei Photon und relativistischer massiver J-Mode gilt für $m_J c^2\ll E$
$$
|k_J-k_A|L/2\simeq (m_Jc^2)^2L/(4E\hbar c).
$$
Bei $E=0{,}360329$ eV und illustrativ $L=1$ m entspricht das Argument eins rund $5{,}33\cdot10^{-4}$ eV Ruheenergie. Das ist eine geometrische Phasenanpassungsskala. Freie J-Ausbreitung wird vorausgesetzt.

Mit $\eta=\frac12\|q\|^2\int_0^L|g|\,dz<1$ hat die Neumann-Reihe der auslaufenden Integralgleichung pro Streumatrix einen Born-Rest in Operatornorm von höchstens $\eta^2/(1-\eta)$. Der Green-Kern trägt in den flussnormierten Variablen nur unitäre Phasen. Für einen endlichen Pi-Hub ist diese schwache Näherung im Allgemeinen nicht kontrolliert. Dafür steht die exakte Blockformel. Bei Annäherung an eine Schwelle kann $D_J^{-1/2}$ groß werden. Die Rechnung setzt zwei tatsächlich offene Kanäle voraus.

## Kalibrierung mit allgemeiner Vorwärtsmatrix

Eine gemessene Feldmarkierung $T$ genügt zur früheren Spurauslese, auch wenn $T-I$ Rang zwei hat. Bei diagonalem Solltransport $U=\operatorname{diag}(z_J,z_A)$ lesen die gemeinsamen Quotienten $\operatorname{tr}U$ und $\operatorname{tr}(TU)$. Mit $\tau_i=T_{ii}$ ergibt sich
$$
z_J=\frac{\operatorname{tr}(TU)-\tau_A\operatorname{tr}U}{\tau_J-\tau_A},
\qquad
z_A=\frac{\tau_J\operatorname{tr}U-\operatorname{tr}(TU)}{\tau_J-\tau_A}.
$$
Die Identifizierbarkeit hängt somit am kalibrierten Diagonalkontrast $\tau_J-\tau_A$. Die außerdiagonalen Einträge tragen bei diagonalem $U$ nicht zur idealen Spur bei. Bei bekannten $\tau_i$ und Matrixfehlern $r_Q,r_T$ in der Feldbasis genügt als Fehlerradius für $z_i$
$$
\frac{\|T-\tau_{\mathrm{anderer}}I\|_1 r_Q+2r_T(1+r_Q)}
     {|\tau_J-\tau_A|}.
$$
Hier ist $\|\cdot\|_1$ die Spurnorm und $|z_i|=1$ gesetzt. Unsicherheit in den Diagonaleinträgen braucht ein eigenes Budget. Im Born-Bereich ist der Diagonalkontrast in erster Ordnung proportional zu $|q_J|^2-|q_A|^2$. Zum Nachweis einer unteren Schranke kann vom Betrag dieses führenden Kontrasts $2\eta^2/(1-\eta)$ abgezogen werden. Modenmischung auf der eigentlichen Vergleichsstrecke oder zurückgekoppelte Reflexionen müssen dagegen als Teil des Übertragungsfehlers gemessen oder mitmodelliert werden.

Damit bleibt ein separater H-Marker im Vergleich ein Kandidat für die Modenzuordnung. Die Rechnung hebt die geometrische Schranke der HCl/H-Zweikanalanschlüsse nicht an. Gemessene freie Wellenzahlen und Admittanzen, ein kalibrierter komplexer Hub im tatsächlichen Band, native Higgs–OP5-Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_zweikanal_marker.wl) · [Tatsächliche Ausgabe](op5_j_zweikanal_marker.txt) · [Laufmanifest](op5_j_zweikanal_marker.json)

Wolfram prüfte die freie Flussbasis, den Wechselwirkungsblock, den verlustfreien Fluss, die Born-Determinante und die allgemeine Spurauslese. Die Integralformeln und Neumann-Schranke folgen analytisch. Reproduzierbar mit **wolframscript -file op5_j_zweikanal_marker.wl**.
