# OP5: Zwei Pole gegen einen frei angepassten Einzelpol

20. November 2026. Analytische Erkundung in M. Der [Minimax-Abstand eines schweren Pols](OP5_J_Minimax_Kontaktterm.md) betrifft einen festen Pol gegenüber einem Kontaktpolynom. Hier prüfen wir ein Zweipolmodell gegenüber einem frei angepassten Einzelpol plus Kontaktpolynom. Wir bestimmen eine konstruktive obere und eine unabhängige untere Schranke für den gleichmäßigen Modellabstand. Die Eingabe ist die schon gravitationskalibrierte statische Antwort in $x=q^2$. Es erfolgt kein H96-Datenvergleich.

## Ein Einzelpol mit angepasster Masse und Stärke

Sei $f(x)=a_1/(x+t_1)+a_2/(x+t_2)$ mit $a_1,a_2>0$ und verschiedenen $t_1,t_2>0$. Das Beispiel setzt positive Gewichte voraus. Ein gemeinsames negatives Vorzeichen kann herausgezogen werden. Wir approximieren auf $[L,U]$ mit $0\le L<U$ durch $g(x)=p(x)+b/(x+\tau)$, wobei $\deg p\le d$ und $\tau>0$ frei sind. Ein bereits im Zielmodell vorhandenes Kontaktpolynom bis Grad $d$ kann in $p$ aufgenommen werden.

Wähle ein Zentrum $c\in[L,U]$, schreibe $y=x-c$, $k=d+1$ und $r_i=(c+t_i)^{-1}$. Über die endliche geometrische Reihe verbleibt nach Abzug der Taylor-Terme bis Grad $d$ aus $f$ der Term
$$
(-y)^k \sum_i\frac{w_i}{1+r_i y},\qquad w_i=a_i r_i^{k+1}.
$$
Setze $W=w_1+w_2$ und $r_*=(w_1r_1+w_2r_2)/W$. Wähle
$$
\tau=r_*^{-1}-c,\qquad b=W/r_*^{k+1},
$$
und für $p$ die Differenz der Taylor-Polynome von $f$ und dem gewählten Einzelpol bis Grad $d$. Die neue Masse zum Quadrat $\tau$ liegt zwischen $t_1$ und $t_2$, da $r_*$ zwischen $r_1$ und $r_2$ liegt. Damit stimmen auch die nächsten beiden Taylor-Koeffizienten überein. Der genaue Rest lautet
$$
f(x)-g(x)=
\frac{(-y)^k y^2}{(1+r_*y)^2}
 \sum_i\frac{w_i(r_i-r_*)^2}{1+r_i y}.
$$
Dazu entwickelt man jede reziproke Funktion um $r_*$ und benutzt $\sum_i w_i(r_i-r_*)=0$. Für positive Gewichte und $x\ge0$ sind alle Nenner positiv. Der Betrag wächst auf jeder Seite des Zentrums mit dem Abstand. Links nimmt mit wachsendem $|y|$ der Zähler zu und jeder Nenner ab. Rechts ist die logarithmische Ableitung jedes Summanden für $y>0$ positiv, weil jede der drei Nennerpotenzen einen Beitrag kleiner als $1/y$ hat und $k+2\ge3$ ist. Damit liegt der Maximalfehler dieses konkreten Kandidaten immer an einem der beiden Intervallenden. Durch Wahl von $c$ kann man die Fehlerbeträge an beiden Enden ausgleichen. Daraus folgt eine obere Schranke für die beste Approximation, ohne Optimalität dieses Kandidaten zu behaupten.

Die Formel zeigt zugleich den quadratischen Effekt naher Massenquadrate: $\sum w_i(r_i-r_*)^2=(w_1w_2/W)(r_1-r_2)^2$. Bei nichtverschwindenden gleichsignierten Gewichten geht die Abweichung mindestens so schnell wie das Quadrat des Polabstandes gegen null. Für gemischte Vorzeichen gilt diese positive gewichtete Konstruktion nicht allgemein.

## Untere Schranke unabhängig von der Wahl des Einzelpols

Für das Zielmodell und jeden Kandidaten benutze die $k=d+1$ festen Anker $z_1,\ldots,z_k$ der [Kontakttermrekonstruktion](OP5_J_Kontakttermrekonstruktion.md). Mit zwei weiteren Knoten je Gruppe entsteht die $2\times2$-Rangmatrix $L_0$ der [Mehrpolrechnung](OP5_J_Mehrpolrekonstruktion.md). Ihre Einträge sind bis auf ein gemeinsames Vorzeichen die dividierten Differenzen $[z_1,\ldots,z_k,x_i,y_j]f$ der ursprünglichen Antwort. Damit lassen sich die Auswirkungen gemeinsamer Anker auf die Fehlerschranke direkt behandeln.

Definiere für jeden Eintrag die Knotenliste $V_{ij}=(z_1,\ldots,z_k,x_i,y_j)$ und
$$
B_{ij}=\sum_{u\in V_{ij}}\frac{1}{\prod_{v\in V_{ij},\,v\ne u}|u-v|},
\qquad B=\left(\sum_{i,j}B_{ij}^2\right)^{1/2}.
$$
Falls ein Kandidat an allen benutzten Knoten um höchstens $e$ vom Ziel abweicht, ist $\|L_0(f)-L_0(g)\|_2\le Be$ aus der Lagrange-Formel und der Frobeniusnorm. Der Einzelpol plus Kontaktterm hat Rang höchstens eins. Deshalb ist sein Abstand in der Matrixoperatornorm mindestens der zweite Singulärwert von $L_0(f)$. Das folgt auch durch Anwenden der Differenz auf einen Einheitsvektor im Kern von $L_0(g)$. Es gilt folglich für *jeden* Kandidaten
$$
\|f-g\|_{\infty,[L,U]}\ge\frac{\sigma_2(L_0(f))}{B}.
$$
Die Schranke beschränkt keine unbekannte Einzelpolmasse oder Einzelpolstärke. Sie ist für zwei sichtbare verschiedene Zielpole mit ausreichenden exakten Stützstellen positiv und kann trotzdem schwächer als der wahre Abstand sein.

## Zahlenbeispiel

Setze $t=(4,9)$, $a=(1,1)$, $[L,U]=[1,10]$ und $d=1$. Eine numerische Halbierung zur Gleichheit der Randfehler liefert $c\simeq4{,}073785$, $\tau\simeq4{,}634890$, $b\simeq1{,}550510$ und $p(x)\simeq0{,}02230463-0{,}000747067(x-c)$. Der Maximalfehler dieses Kandidaten beträgt rund $2{,}3670\times10^{-4}$. Für die untere Schranke verwende Anker $(2,8)$ und Gruppen $(1,6)$ sowie $(4,10)$. Die direkte Auswertung ergibt $\sigma_2\simeq5{,}3013\times10^{-7}$ und $B\simeq0{,}26747$. Der tatsächliche gleichmäßige Abstand liegt somit mindestens bei $1{,}98\times10^{-6}$ und höchstens bei etwa $2{,}37\times10^{-4}$.

Bei zwei konkurrierenden Vorhersagen mit absoluter Fehlerhalbbreite $\epsilon$ pro Stützstelle gibt die untere Schranke sichere Trennung, wenn $2\epsilon<\sigma_2/B$. Ist $2\epsilon$ mindestens der berechnete obere Fehler, bestehen dagegen überlappende Vorhersageintervalle sogar auf dem ganzen Bereich. Dazwischen bleibt die genaue Schwelle offen. Die Auswertung benutzt synthetische Antworten. Zugängliche Skalen, Tracerfehler, tatsächliche Beobachtbarkeit und H96 bleiben offen.

## Minimax-Schranken aus fünf alternierenden Stützstellen

Für zwei Kandidaten $g$ und $g_*$ aus derselben Modellklasse ist
$$
g(x)-g_*(x)=\frac{Q(x)}{(x+\tau)(x+\tau_*)},\qquad \deg Q\le d+2.
$$
Seien $x_0<\cdots<x_{d+3}$ Stützstellen, an denen $f-g_*$ alternierende Vorzeichen und jeweils einen Betrag von mindestens $E_-$ hat. Falls $|f-g|<E_-$ an jeder dieser Stellen wäre, hätte $g-g_*=(f-g_*)-(f-g)$ dort dieselben alternierenden Vorzeichen. Die positiven Nenner übertragen diese Vorzeichen auf $Q$. Zwischen den Stützstellen müsste $Q$ mindestens $d+3$ verschiedene Nullstellen haben, im Widerspruch zur Gradgrenze und zu den von null verschiedenen Werten an den Stützstellen. Damit ist $E_-$ eine Untergrenze für die beste gleichmäßige Approximation auf diesen Stützstellen und auf dem gesamten Intervall. Das Argument gilt für beliebige reelle Einzelpolstärken und Kontaktkoeffizienten bei $\tau>0$.

Für das Zahlenbeispiel mit $d=1$ setzen wir $g_*(x)=p_0+p_1x+b/(x+\tau)$ mit den exakten rationalen Koeffizienten
$$
(p_0,p_1,b,\tau)=\frac{1}{10^{12}}
(24800178816,-675564271,1549075645442,4615710103478).
$$
Der Kandidat stammt aus einem numerischen Abgleich alternierender Residuen an beiden Endpunkten und drei inneren Extremstellen. Für die Schranken verwenden wir nur die gerundeten Werte. An den Stützstellen
$$
(x_0,x_1,x_2,x_3,x_4)=(1,1.715805257,4.068462517,7.810339505,10)
$$
gilt $(-1)^j(f-g_*)(x_j)\ge 28588359/10^{12}$. Auf dem äquidistanten Gitter $1+9j/N$ mit $N=65536$ und $0\le j\le N$ ist jeder Residuenbetrag kleiner als $2858837/10^{11}$. Für $r=f-g_*$ gilt zusätzlich
$$
\sup_{[1,10]}|r''|\le\frac{2}{5^3}+\frac{2}{10^3}+\frac{2b}{(1+\tau)^3}<\frac1{20}.
$$
Auf jedem Gitterteilintervall der Länge $h=9/N$ weicht $r$ von seiner linearen Interpolante um höchstens $h^2\sup|r''|/8$ ab. Das folgt aus der Interpolationsfehlerformel mit dem Produkt der beiden Abstände zu den Teilintervallgrenzen. Die Interpolante selbst bleibt im Betrag unter dem größeren Randwert. Damit folgt für $E_*=\inf_g\|f-g\|_{\infty,[1,10]}$ die Einschließung
$$
2.8588359\times10^{-5}\le E_*<2.8588488\times10^{-5}.
$$

Die rationalen Ungleichungen lassen sich so nachrechnen.

~~~python
from fractions import Fraction as F

scale = 10**12
p0, p1, b, tau = (F(n, scale) for n in
                   (24800178816, -675564271, 1549075645442, 4615710103478))

def residual(x):
    return 1/(x + 4) + 1/(x + 9) - p0 - p1*x - b/(x + tau)

nodes = (1000000000, 1715805257, 4068462517, 7810339505, 10000000000)
lower = F(28588359, scale)
assert all((-1)**j * residual(F(n, 10**9)) >= lower
           for j, n in enumerate(nodes))

N = 65536
grid_bound = F(2858837, 10**11)
assert all(abs(residual(1 + F(9*j, N))) < grid_bound
           for j in range(N + 1))
curvature_bound = F(1, 20)
assert F(2, 5**3) + F(2, 10**3) + 2*b/(1 + tau)**3 < curvature_bound
assert grid_bound + F(9, N)**2 * curvature_bound/8 < F(28588488, scale)
~~~

Bei derselben absoluten Fehlerhalbbreite $\epsilon$ für beide Modellvorhersagen garantieren die fünf Stützstellen getrennte Vorhersageintervalle an mindestens einer Stelle für $\epsilon<1.42941795\times10^{-5}$. Ab $\epsilon=1.4294244\times10^{-5}$ überlappen die Vorhersageintervalle von $f$ und $g_*$ auf dem gesamten Bereich. Diese Schwellen gelten für die synthetische Antwort und ihre Normierung. Die Beobachtungsabbildung für H96 bleibt offen.
