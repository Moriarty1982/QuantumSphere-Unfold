# OP5 – Phasenaufgelöste Rückstreugrenze im Messband

21. November 2026. Analytische Erkundung im Materieframe M. Der endliche A-Hub aus der Vorarbeit wird exakt als skalare Referenz behandelt. Die ersten beiden Korrekturen der J-Beimischung werden mit ihren Ausbreitungsphasen abgeschätzt. Für das Bandbeispiel wird eine verlustfreie Schicht mit reellen offenen Wellenzahlen verwendet.

## Vorwissen geprüft

Der [Zweikanalmarker](OP5_J_Zweikanal_Marker.md) unterscheidet Wellenzahldifferenz und -summe für einen schwachen Gesamtmarker. Der [endliche Markerhub](OP5_J_Endlicher_Markerhub.md) liefert den verzerrten Green-Kern und eine Rückstreugrenze von rund $0{,}003156$ im illustrativen 100-MHz-Band. Der [Feldreferenzvergleich](OP5_J_Feldreferenz.md) gibt das Quotientenbudget. Die Suche nach Phasenanpassung, Wellenzahlsumme und Rücklaufgrenzen ergab für den starken A-Hub bisher keine bandweite Abschätzung mit den ersten beiden Reflexionstermen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Erste Rückumwandlung

Seien $k_J,k_A$ die freien Wellenzahlen, $\kappa$ die innere A-Wellenzahl, $r=(\kappa-k_A)/(\kappa+k_A)$ und $c=(1-r)/(1-r^2e^{2i\kappa L})$. Das normierte Referenzfeld bei linkem Einfall ist die Diagonalmatrix
$$
F(z)=\operatorname{diag}\left(e^{ik_Jz},\ c[e^{i\kappa z}+r e^{i\kappa(2L-z)}]\right).
$$
Sei $E=g\bigl(\begin{smallmatrix}|q_J|^2&q_J\overline q_A\\q_A\overline q_J&0\end{smallmatrix}\bigr)$ der zu iterierende konstante Feldterm aus der Vorarbeit. Für die auslaufende Referenzmatrix $\mathcal G$ gilt an der Eintrittsebene $K\mathcal G(0,z)=F(z)/(2i)$. Die erste Reflexionskorrektur lautet deshalb $R^{(1)}=(i/2)\int_0^L F(z)E F(z)\,dz$. Die Auswertung enthält keine komplexe Konjugation der laufenden Referenzphase. [Auslaufende Green-Funktionen für geschichtete Medien](https://arxiv.org/abs/1703.01034)

Schreibe $I(a)=(e^{iaL}-1)/(ia)$ mit $I(0)=L$. Dann gilt
$$
R^{(1)}_{JJ}=\tfrac i2 E_{JJ}I(2k_J),\qquad R^{(1)}_{AA}=0,\qquad
R^{(1)}_{JA}=\tfrac i2 E_{JA}\,c\left[I(k_J+\kappa)+r e^{2i\kappa L}I(k_J-\kappa)\right].
$$
Für die Gegenrichtung der Modenumwandlung wird $E_{JA}$ durch $E_{AJ}$ ersetzt. Der erste Term liest die Wellenzahlsumme. Der zweite liest wegen der kleinen internen A-Gegenwelle die Differenz und ist mit $r$ gewichtet. Am Zentrum des bisherigen Beispiels gilt $(k_J L,\kappa L)=(9999\pi,10001\pi)$. Somit verschwinden dort alle drei Integrale exakt. Wenn nur die Beimischung in einer ansonsten festen A-Referenz einen glatten kompakten Faktor $w(z)$ erhält, ersetzt $\int w(z)e^{iaz}dz$ das jeweilige $I(a)$. Für $w\in C_c^m(0,L)$ ist der Betrag für $a\ne0$ durch $\|w^{(m)}\|_{L^1}/|a|^m$ begrenzt. Dies hilft bei großer Summe. Kleine Differenzen brauchen weiterhin eine eigene Kontrolle. Eine gleichzeitige Glättung der A-Referenz würde ihren Green-Kern ändern.

## Zweite Iteration mit laufenden Phasen

Mit $\theta=C L\|E\|_2<1$ und $F_0$ aus der Vorarbeit bleibt für die Iterationen ab der dritten die Normgrenze $F_0\theta^3/(1-\theta)$. Um die zweite Iteration besser als mit $\theta^2$ zu begrenzen, zerlege $F=F_++F_-$ in die vorwärts laufende Komponente und die mit $r$ gewichtete Gegenwelle. Schreibe $f=\max(1,|c|)$ und $b=|cr|$. Für den mit $K$ gewichteten Green-Kern gelten die Grenzen
$$
C_{\rm dir}=\max\left\{\tfrac12,\frac{k_A}{2|\kappa|(1-|r|^2)}\right\},\qquad
C_{\rm img}=\frac{k_A(2|r|+|r|^2)}{2|\kappa|(1-|r|^2)}
$$
für den direkten Term und die Summe der drei übrigen Terme. $C$ bleibt die Grenze des vollen Kerns.

In der zweiten Reflexionskorrektur enthält der direkte Kern zwischen zwei vorwärts laufenden Referenzfeldern Integrale der Form
$$
\int_0^L\!\!\int_0^L e^{i\alpha z+i\beta y+i\sigma|z-y|}\,dy\,dz,
\qquad \alpha,\beta,\sigma\in\{k_J,\kappa\}.
$$
Auf jedem der beiden Dreiecke führe den kleineren Ortsparameter und die Differenz als Koordinaten ein. Bei festgehaltener Differenz ist die Frequenz im kleineren Parameter $\alpha+\beta$. Sein Integral ist im reellen Fall durch $2/|\alpha+\beta|$ begrenzt. Der Betrag des gesamten Doppelintegrals ist damit höchstens $4L/|\alpha+\beta|$. Bei $k_{\min}=\min(k_J,\kappa)>0$ folgt
$$
\|R^{(2)}\|_2\le
\frac{ f^2 C_{\rm dir}L}{k_{\min}}\|E\|_2^2+
\frac{L^2\|E\|_2^2}{2}\left[f^2 C_{\rm img}+(2fb+b^2)C\right].
$$
Der erste Term verwendet den Phasenabgleich. Für die Bildterme und Produkte mit einer Gegenwelle genügt die Betragsabschätzung. Bei dieser $E$-Struktur hat die Matrix der Eintragsbeträge dieselbe Operatornorm wie $E$, da sich die relative Phase der beiden Kopplungsrichtungen mit einem diagonalen unitären Basiswechsel beseitigen lässt. Damit gilt die Abschätzung auch für die komplexe Dipolrichtung. Das hier ausgewertete Bandbeispiel verwendet reelle $\kappa$ und reelle freie Wellenzahlen.

## Durchgehende 100-MHz-Grenze im Vergleichsbeispiel

Verwende die mittlere Energie $0{,}360329$ eV und die unveränderten Schichtwerte der Vorarbeit. Setze für dieses Beispiel ausdrücklich $k_A,k_J,\kappa$ proportional zur Energie bei konstantem Fluss-Kopplungsverhältnis $10^{-3}$ und festem $L$. Die relative Halbbreite sei $u=h_E/E_0$. Für jedes der drei im Zentrum ganzperiodigen Argumente von $I(a)$ gilt über das Band $|I(a)|/L\le u/(1-u)$. Die skalare A-Reflexion bleibt durch $2r(\kappa_0 L)u/(1-r^2)$ beschränkt. Für den Neumannparameter, die Feldtermnorm und die erste Korrektur werden die Bandmaxima, für $k_{\min}$ das Bandminimum eingesetzt.

| Beitrag zur Obergrenze der Reflexionsnorm | Wert |
| --- | ---: |
| Exakte A-Referenz, bandweit abgeschätzt | $1{,}8030\cdot10^{-6}$ |
| Erste Iteration | $1{,}8048\cdot10^{-9}$ |
| Zweite Iteration | $2{,}6051\cdot10^{-9}$ |
| Rest ab dritter Iteration | $3{,}1156\cdot10^{-8}$ |
| Summe, konservativ gerundet | $1{,}839\cdot10^{-6}$ |

Im einfachen Rücklaufmodell der Vorarbeit folgt mit $\|T\|\le1$ und selbst $\|F_{\rm rück}\|\le1$ ein Transmissionsrest unter $1{,}84\cdot10^{-6}$. Das liegt unter dem illustrativen Quotientenbudget $9{,}82\cdot10^{-6}$. Das Budget muss in einem Experiment auch für alle anderen Fehlerquellen reichen. Der frühere viel kleinere exakte Zentralwert wird hier nicht auf das Band übertragen. Stattdessen berücksichtigt die Schranke alle Frequenzen im idealisierten Band und wird vor allem vom skalaren A-Anteil bestimmt. Für eine reale massive J-Dispersion, Verluste oder eine abweichende Schichtdicke sind die drei Argumentbereiche und die skalare Rückstreugrenze mit den tatsächlichen Werten neu zu prüfen.

Das Beispiel zeigt, wann bereits die Phasenanpassung der homogenen Schicht genügt. Eine Konzentrationsglättung oder separate Rücklaufmessung bleibt für andere Schichtdaten zu bewerten. Die geometrische HCl/H-Anschlussschranke, freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_rueckstreuung_band.wl) · [Tatsächliche Ausgabe](op5_j_rueckstreuung_band.txt) · [Laufmanifest](op5_j_rueckstreuung_band.json)

Wolfram prüfte die Randidentität des Green-Kerns, den Integranden der ersten Umwandlung und die zentralen Auslöschungen exakt. Die Bandwerte wurden aus den analytischen Schranken berechnet. Kein Frequenzgitter ist Teil des Nachweises. Reproduzierbar mit **wolframscript -file op5_j_rueckstreuung_band.wl**.
