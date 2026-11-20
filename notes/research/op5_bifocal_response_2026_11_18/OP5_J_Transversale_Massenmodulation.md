# OP5: Laufzeitmodulation bei erhaltener Gesamtmasse

20. November 2026. Analytische Erkundung in M. Die [doppelte Laufzeitdifferenz](OP5_J_Doppelte_Laufzeitdifferenz.md) setzt eine veränderliche D-Massensäule zwischen festen Endpunkten voraus. Hier wird die planare Faltung durch eine dreidimensionale ersetzt. Geprüft wird, ob eine Umverteilung mit unveränderter Gesamtmasse ein Signal liefern könnte. Wir verwenden die lineare, statische Näherung des massiven Verhältnisabgleichs und eine vorgegebene flache Geometrie. Ein Mechanismus zur Kontrolle der D-Materie wird nicht angenommen. Es erfolgt kein H96-Datenvergleich.

## Projektion der dreidimensionalen Yukawa-Antwort

Sei $\mathbf b$ die transversale Koordinate und $z$ die Strahlrichtung. Im statischen Spin-2-Vergleich für den führenden Unterschied freier Wellen verwenden wir die normierte dreidimensionale Yukawa-Faltung
$$
G_m(\mathbf r)=\frac{m^2e^{-m|\mathbf r|}}{4\pi|\mathbf r|},\qquad
\delta\rho_m=G_m*\delta\rho,\qquad \int G_m\,d^3r=1.
$$
Der Faktor $1/m^2$ ist im Koeffizienten $C_\Delta=(g_J-g_A)g_D/m^2$ der Laufzeit enthalten. Definiere $\delta\Sigma(\mathbf b)=\int_{\mathbb R}\delta\rho(\mathbf b,z)\,dz$. Für eine über die gesamte Achse integrierte Ausbreitungsantwort ergibt sich
$$
\int_{\mathbb R}\delta\rho_m(\mathbf b,z)\,dz=(K_m^{(2)}*\delta\Sigma)(\mathbf b),\qquad
K_m^{(2)}(b)=\frac{m^2}{2\pi}K_0(mb).
$$
Hier ist $K_0$ die modifizierte Besselfunktion zweiter Art. Für $b>0$ macht die Substitution $z=b\sinh t$ im Integral des Yukawa-Kerns den Faktor $2\int_0^\infty e^{-mb\cosh t}dt$ sichtbar. Der Kern ist positiv, radial streng fallend und trotz logarithmischer Singularität bei $b=0$ integrierbar. Seine Flächennorm beträgt eins, direkt aus der Norm von $G_m$. In der Fourier-Darstellung lautet sein Multiplikator $m^2/(m^2+q_\perp^2)$, erhalten bei $q_z=0$. [NIST DLMF, Integraldarstellungen von $K_\nu$](https://dlmf.nist.gov/10.32)

Für eine breite oder gewichtete Probe seien $w(\mathbf b)\ge0$ das bekannte transversale Strahlgewicht mit $\int w\,d^2b=1$ und $L$ die Länge der Messstrecke. Im schwachen, reflexionsarmen Strahlmodell wird die Gruppenlaufzeitänderung aus der mit $w$ gewichteten integrierten Antwort mal $C_\Delta$ gebildet. Das setzt vernachlässigbare Änderungen des Strahlprofils und einen festen Phasenbezug voraus. Für den endlichen Abschnitt $0\le z\le L$ und eine Profiländerung mit Träger in $d\le z\le L-d$ folgt
$$
\left|\int d^2b\,w(\mathbf b)\int_0^L dz\,\delta\rho_m
-\int d^2b\,w(\mathbf b)(K_m^{(2)}*\delta\Sigma)(\mathbf b)\right|
\le \|w\|_\infty e^{-md}\|\delta\rho\|_1 .
$$
Dazu lässt sich im ausgelassenen Achsenbereich $w$ durch seine obere Schranke ersetzen. Das Integral des dreidimensionalen Kerns über die Transversalebene ist $(m/2)e^{-m|z|}$; seine beiden ausgelassenen Enden ergeben die Randfaktoren der planaren Formel. Die Abschätzung gilt für ein endlich breites, beschränktes Strahlgewicht und vorzeichenwechselnde Dichteänderungen.

## Welche Bewegung die Säule verändert

Eine reine Längsverschiebung jeder Dichteverteilung bei festem transversalen Profil lässt $\delta\Sigma(\mathbf b)=0$ für alle $\mathbf b$. Im vollständig projizierten Signal fällt sie exakt heraus. Auf einer endlichen Strecke können die zuvor begrenzten Randbeiträge verbleiben. Eine quer gerichtete Umverteilung bei erhaltener Gesamtmasse erzwingt dagegen nur $\int \delta\Sigma\,d^2b=0$. Sie kann unter dem Strahl eine große positive oder negative Änderung ergeben, obwohl der räumliche Nullmodus verschwindet.

Ein einfaches Beispiel ist die Verschiebung einer zentrierten, gleichförmigen Massensäule der Flächendichte $\Sigma_0$ und des Radius $R$ in einen konzentrischen Ring mit Innenradius $R$ und Außenradius $\sqrt{2}R$. Beide Flächen und beide Massen sind gleich. Auf der Achse ergibt sich für den Betrag des Unterschieds aus der projizierten Faltung
$$
\Delta\Sigma_m(0)=\Sigma_0\,[1-2xK_1(x)+\sqrt 2 xK_1(\sqrt 2 x)],\qquad x=mR .
$$
Das folgt aus $\int_0^x tK_0(t)\,dt=1-xK_1(x)$ und der Integration über Scheibe und Ring. Die Gleichheit der Flächen und der streng fallende Kern machen den Unterschied bei $x>0$ strikt positiv. Die Achsenformel ist der Grenzfall eines schmalen Strahls im Inneren einer langen Messstrecke. Die Randschranke oben ist für endliche Breite separat anzuwenden. Die beispielhafte stückweise konstante Säule dient dem Faltungsvergleich.

Numerische Simpson-Integration der Integraldarstellung von $K_1$ liefert für $x=1,3,5$ der Reihe nach $0{,}240528$, $0{,}799233$ und $0{,}962529$ für $\Delta\Sigma_m(0)/\Sigma_0$. Diese Zahlen bestimmen nur den geometrischen Faltungsfaktor. Sie kalibrieren weder die tatsächliche kontrollierbare Masse noch $C_\Delta$.

Der doppelte Laufzeitvergleich kann somit prinzipiell eine quer umverteilte Säule derselben Gesamtmasse unterscheiden. Reine Längsverschiebung ist für das projizierte Signal unbrauchbar. Die Auslese bleibt eine Projektion ohne Information über die genaue Tiefenlage. Der Aufbau, der J-Phasenbezug, die Kontrolle der Population und H96 bleiben offen.
