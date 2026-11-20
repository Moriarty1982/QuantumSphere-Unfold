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

Bei zwei konkurrierenden Vorhersagen mit absoluter Fehlerhalbbreite $\epsilon$ pro Stützstelle gibt die untere Schranke sichere Trennung, wenn $2\epsilon<\sigma_2/B$. Ist $2\epsilon$ mindestens der berechnete obere Fehler, bestehen dagegen überlappende Vorhersageintervalle sogar auf dem ganzen Bereich. Dazwischen bleibt die Schwelle mit diesen beiden Schranken offen. Die Auswertung benutzt synthetische Antworten. Zugängliche Skalen, Tracerfehler, tatsächliche Beobachtbarkeit und H96 bleiben offen.

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

## Exakter Minimax-Einzelpol für zwei gleichsignierte Pole

Seien $0<t_1<t_2$, $a_1,a_2>0$, $0\le L<U$ und $d\ge0$. Unter allen $g=p+b/(x+\tau)$ mit $\deg p\le d$, $b\in\mathbb R$ und $\tau>0$ gibt es genau eine beste gleichmäßige Approximation von $f=a_1/(x+t_1)+a_2/(x+t_2)$. Sie hat $t_1<\tau<t_2$ und $b>0$. Der Fehler alterniert an genau $d+4$ Punkten einschließlich der Intervallenden. Bei zwei negativen Zielgewichten folgt die entsprechende Aussage durch Vorzeichenwechsel.

### Konstruktion der alternierenden Funktion

Setze $m=(L+U)/2$, $h=(U-L)/2$, $n=d+3$ und
$$
\rho(t)=\frac{h}{m+t+\sqrt{(m+t)^2-h^2}},\qquad
\rho_1=\rho(t_1),\quad \rho_2=\rho(t_2),\quad \rho_3=\rho(\tau).
$$
Alle $\rho_i$ liegen in $(0,1)$. Unter $x=m+\frac h2(z+z^{-1})$ entsprechen $-\rho_i$ und $-1/\rho_i$ den Stellen $-t_1,-t_2,-\tau$. Definiere
$$
B(z)=z^d\prod_{i=1}^3\frac{z+\rho_i}{1+\rho_i z},
\qquad R_\tau(x)=\frac{B(z)+B(z)^{-1}}2,
\qquad D_\tau(x)=(x+t_1)(x+t_2)(x+\tau).
$$
Auf $z=e^{i\theta}$, $0\le\theta\le\pi$, hat jeder Quotient in $B$ Betrag eins. Sein stetiges Argument wächst von $0$ bis $\pi$ mit Ableitung $(1-\rho_i^2)/(1+2\rho_i\cos\theta+\rho_i^2)>0$. Das Argument von $B$ wächst damit strikt von $0$ bis $n\pi$. Folglich ist $\lVert R_\tau\rVert_\infty=1$ und $R_\tau$ erreicht die Werte $\pm1$ abwechselnd genau an den $n+1$ Punkten, an denen dieses Argument ein ganzzahliges Vielfaches von $\pi$ ist.

Schreibe $N(z)=\prod_i(z+\rho_i)$, $H(z)=\prod_i(1+\rho_i z)$ und $K=(h/2)^3/(\rho_1\rho_2\rho_3)$. Aus $D_\tau(x(z))=K z^{-3}N(z)H(z)$ folgt
$$
P_\tau(x(z)):=D_\tau(x(z))R_\tau(x(z))
=\frac K2\left(z^{d-3}N(z)^2+z^{-d-3}H(z)^2\right).
$$
Der Ausdruck ist unter $z\mapsto z^{-1}$ invariant. Seine Laurentpotenzen liegen zwischen $-n$ und $n$. Er ist also ein Polynom in $x$ vom Grad höchstens $n$. Dazu setzt man $S_k=z^k+z^{-k}$ und zeigt per Induktion mit $S_{k+1}=2(x-m)S_k/h-S_{k-1}$, dass $S_k$ ein Polynom in $x$ vom Grad $k$ ist. Für $u_1=t_1$, $u_2=t_2$, $u_3=\tau$ liefert die Auswertung bei $z=-\rho_i$
$$
P_\tau(-u_i)=(-1)^n\frac K2 V_i,\qquad
V_i=\rho_i^{-n}\prod_{j=1}^3(1-\rho_i\rho_j)^2>0.
$$

### Abgleich der Ausgangspole

Für $\tau\in(t_1,t_2)$ sind die Werte von $D_\tau f$ an den beiden Zielpolen
$$
A_1=a_1(t_2-t_1)(\tau-t_1),\qquad
A_2=a_2(t_2-t_1)(t_2-\tau).
$$
Die stetige Funktion $A_1/V_1-A_2/V_2$ ist bei $\tau=t_1$ negativ und bei $\tau=t_2$ positiv. Wähle eine innere Nullstelle und setze $E=2A_1/(KV_1)>0$. Dann stimmt $(-1)^n E P_\tau$ bei $-t_1$ und $-t_2$ mit $D_\tau f$ überein. Also lässt sich der Zähler von
$$
g_*(x)=f(x)-(-1)^n E R_\tau(x)
$$
durch $(x+t_1)(x+t_2)$ kürzen. Der verbleibende Zähler hat Grad höchstens $d+1$, sein Nenner ist $x+\tau$. Polynomdivision ergibt $g_*=p_*+b_*/(x+\tau)$ mit $\deg p_*\le d$. Aus der Auswertung vor der Kürzung bei $-\tau$ folgt
$$
b_*=\frac{E K V_3}{2(\tau-t_1)(t_2-\tau)}>0.
$$

Das Residuum $f-g_*$ alterniert mit Betrag $E$ an $d+4$ Stützstellen. Das vorangehende Nullstellenargument beweist die Optimalität. Für die Eindeutigkeit sei $g$ ein weiterer Kandidat mit Fehler höchstens $E$. An den Alternationspunkten $x_j$ hat der Zähler $Q$ von $g-g_*$ schwach alternierende Vorzeichen. Die dividierte Differenz
$$
\sum_{j=0}^{d+3}\frac{Q(x_j)}{\prod_{i\ne j}(x_j-x_i)}
$$
verschwindet wegen $\deg Q\le d+2$. Die Nenner haben ebenfalls alternierende Vorzeichen, sodass alle Summanden dasselbe schwache Vorzeichen haben. Daher verschwinden alle $Q(x_j)$ und damit $Q$ identisch. Weil $b_*>0$, besitzt $g_*$ einen echten Pol. Seine Lage bestimmt $\tau$ eindeutig. Somit gibt es auch genau eine Nullstelle der Abgleichgleichung in $(t_1,t_2)$.

### Quadratische Gleichung und Zahlenprobe

Mit $C_i=\rho_i^{-n}(1-\rho_i\rho_1)^2(1-\rho_i\rho_2)^2$ für $i=1,2$ und $r=\rho_3$ ist $V_i=C_i(1-\rho_i r)^2$. Setzt man $t=\frac h2(\rho(t)+1/\rho(t))-m$ in den Polabgleich ein, ergibt sich
$$
a_1\rho_2 C_2(\rho_1-r)(1-\rho_2r)
=a_2\rho_1 C_1(r-\rho_2)(1-\rho_1r).
$$
Die quadratische Gleichung hat genau eine Lösung im offenen Intervall $(\rho_2,\rho_1)$. Aus ihr folgen $\tau$, der exakte Modellabstand $E$ und das Residuum. Für $[L,U]=[1,10]$, $(t_1,t_2)=(4,9)$, $a_1=a_2=1$ und $d=1$ ergibt die numerische Auswertung der Formel $\tau\simeq4.61571010347817$, $b_*\simeq1.54907564544239$ und $E\simeq2.8588362842460\times10^{-5}$. Das liegt in der zuvor rational geprüften Einschließung. Die fünf Alternationspunkte stimmen auf neun Nachkommastellen mit der obigen Stützstellenwahl überein. Für H96 bleibt die Abbildung auf messbare Antworten offen.

Eine verwandte Darstellung gewichteter Chebyshev-Polynome über den Einheitskreis findet sich bei [Kroó und Pinkus, *Strong Uniqueness*, Abschnitt 13](https://www2.math.ethz.ch/EMIS/journals/SAT/papers/12/12.pdf).

## Gegenläufige Polgewichte und Grenzfälle

Seien weiterhin $0<t_1<t_2$, $0\le L<U$ und $d\ge0$, jetzt mit $a_1>0>a_2$. Ein gemeinsamer Vorzeichenwechsel deckt die andere Reihenfolge der Vorzeichen ab. Mit den $\rho_i,C_i$ aus der vorigen Konstruktion setze
$$
k=\frac{a_1\rho_2 C_2}{|a_2|\rho_1 C_1},\qquad
F(r)=\frac{(\rho_2-r)(1-\rho_1r)}{(\rho_1-r)(1-\rho_2r)},\qquad
k_\infty=F(0)=\frac{\rho_2}{\rho_1},\qquad k_0=F(\rho(0)).
$$
Es gilt $0<k_\infty<1\le k_0$. Für $L>0$ ist $k_0>1$. Für $L=0$ gilt $\rho(0)=1$ und $k_0=1$.

| Bereich | Gleichmäßig beste Antwort oder Grenzwert | Wird das Infimum bei $\tau>0$ erreicht? |
| --- | --- | --- |
| $0<k<k_\infty$ | Eindeutiger Einzelpol mit $\tau>t_2$ und $b<0$ | Ja |
| $k_\infty\le k<1$ | Bestes Polynom vom Grad $d+1$ als Grenzwert für $\tau\to\infty$ | Nein |
| $k=1$ | Eindeutige Antwort als Kontaktpolynom vom Grad höchstens $d$. Bei $b=0$ bleibt $\tau$ frei. | Ja |
| $1<k\le k_0$ | Beste Antwort $p+b/x$ mit $b\ne0$ als Grenzwert für $\tau\downarrow0$ | Nein |
| $k>k_0$ | Eindeutiger Einzelpol mit $0<\tau<t_1$ und $b>0$ | Ja |

Für $L=0$ ist der vierte Bereich leer. Die Grenzen betreffen das Massenquadrat $\tau$ und die gleichmäßige Abweichung auf dem gegebenen Intervall.

### Endliche Einzelpole und der Fall $b=0$

Der Abgleich $A_1/V_1=A_2/V_2$ bleibt gültig, jetzt mit $A_2=a_2(t_2-t_1)(t_2-\tau)$. Innerhalb $(t_1,t_2)$ haben $A_1$ und $A_2$ entgegengesetzte Vorzeichen. Außerhalb dieses Bereichs ist der Abgleich für $r=\rho(\tau)$ äquivalent zu $k=F(r)$. Auf $(0,\rho_2)$ fällt $F$ strikt von $k_\infty$ auf null. Auf $(\rho_1,1]$ fällt $F$ strikt von $+\infty$ auf eins. Dies folgt in beiden Bereichen aus der Ableitung von $\log F$: Die Beiträge aus den beiden Quotienten $(\rho_2-r)/(\rho_1-r)$ und $(1-\rho_1r)/(1-\rho_2r)$ sind jeweils negativ. Positive endliche $\tau$ entsprechen $0<r<\rho(0)$. Jede solche Lösung liefert $f-g_*=(2A_1/(KV_1))(-1)^n R_\tau$ und damit einen eindeutigen Minimax-Kandidaten nach dem Alternationsargument. Die Vorzeichen von $b$ folgen aus der Auswertung des Residualzählers bei $-\tau$.

Für die Notwendigkeit betrachte eine optimale Antwort mit $b\ne0$ und setze $s=1/(1+\tau)$, $D_s=1-s+sx$. Schreibe die Antwort als $M/D_s$ mit $\deg M\le d+1$. Im Inneren $0<s<1$ spannen die Variationen von $M$ und $s$ alle Funktionen
$$
\frac{\Delta M\, D_s-M(x-1)\Delta s}{D_s^2}
=\frac{Q}{D_s^2},\qquad \deg Q\le d+2,
$$
auf. Dazu wählt man $\Delta s$ über die Auswertung des Zählers am Pol, wo $M$ und $x-1$ von null verschieden sind. Der Rest ist dann durch $D_s$ teilbar. Ohne $d+4$ alternierende Extremwerte gäbe es ein $Q$ vom Grad höchstens $d+2$ mit passendem strengem Vorzeichen auf allen Extremstellen. Die Nullstellen von $Q$ lassen sich zwischen den aufeinanderfolgenden Gruppen entgegengesetzter Vorzeichen platzieren. Eine hinreichend kleine Variation in dieser Richtung senkt den Maximalfehler, da die Variation gleichmäßig bis auf einen quadratischen Rest gilt und der Fehler abseits der Extremstellen unter seinem Maximum liegt.

Der Residualzähler $D_\tau(f-g)$ hat Grad höchstens $d+3$. Bei $d+4$ alternierenden Extremwerten muss er Grad $d+3$ haben. Er ist ein Vielfaches von $P_\tau$ aus der Einheitskreiskonstruktion. Beide sind, nach Anpassung des Leitkoeffizienten, ausgezeichnete Polynome minimaler Norm mit Gewicht $1/D_\tau$. Das Alternationsargument mit dividierten Differenzen beweist die Eindeutigkeit auch in dieser Klasse. Bei $\tau=t_i$ verschwindet $D_\tau(f-g)$ an der doppelten Nennernullstelle, während $P_\tau$ dort von null verschieden ist. Damit sind alle optimalen Lösungen mit einem endlichen positiven Pol und $b\ne0$ durch die genannte skalare Gleichung erfasst.

Ein Kontaktpolynom $p$ vom Grad höchstens $d$ kann nur dann für alle $\tau$ optimal sein, wenn $f-p$ mindestens $d+3$ alternierende Extremwerte besitzt. Das folgt bereits aus der linearen Approximation bei einer festen positiven $\tau$, deren Differenzen Zähler vom Grad höchstens $d+1$ und einen positiven Nenner haben. Umgekehrt reichen diese $d+3$ Werte für die Optimalität und Eindeutigkeit von $p$ in der ganzen Klasse. Dazu ordnet man den Zähler von $g-p$ für jedes $\tau$ demselben Grad zu und benutzt wieder die dividierte Differenz.

Für diese Alternation verwendet man die Einheitskreiskonstruktion mit zwei Faktoren in $B$ und dem Vorfaktor $z^d$. Der Residualzähler über $(x+t_1)(x+t_2)$ ist dann vom Grad $d+2$. Die beiden Beträge an den Zielpolen sind proportional zu $\rho_1 C_1$ und $\rho_2 C_2$. Wie im Dreifaktorenfall erzwingt die Alternation ein Vielfaches dieses Zählers. Die vorgegebenen Zählerwerte sind $a_1(t_2-t_1)$ und $|a_2|(t_2-t_1)$. Ihr Verhältnis stimmt genau für $k=1$ mit dem Verhältnis der konstruierten Werte überein. Dann kürzen sich beide Polfaktoren aus der Approximation heraus und es bleibt das eindeutige Kontaktpolynom.

### Grenzen des Massenbereichs

Für $L>0$ lässt sich die Klasse $M/D_s$ auf $0\le s\le1$ erweitern. Der Nenner bleibt gleichmäßig positiv. Für eine beschränkte Folge von Antworten sind auch die Zähler gleichmäßig beschränkt, also haben ihre Koeffizienten eine konvergente Teilfolge. Ein Minimum existiert daher in der erweiterten Klasse. Beide Randräume sind gleichmäßig durch Antworten mit $0<s<1$ approximierbar. Sie bestehen aus Polynomen vom Grad höchstens $d+1$ bei $s=0$ und Antworten $p+b/x$ bei $s=1$.

Falls bei $k\ne1$ kein innerer Minimierer existiert, kann nur einer der beiden Ränder optimal sein. Wären $M_0/D_0$ und $M_1/D_1$ beide optimal, ergäbe $(M_0+M_1)/(D_0+D_1)$ durch punktweise positive Mittelung eine ebenso gute innere Antwort. Innerhalb jedes Randraums ist die beste Antwort durch den linearen Alternationssatz eindeutig.

Wenn $k$ von unten gegen $k_\infty$ wächst, geht die Lösung der skalaren Gleichung gegen $r=0$ und daher $s\to0$. Aus der Kompaktheit und der stetigen Abhängigkeit der minimalen Fehler von $f$ folgt die Optimalität von $s=0$ bei $k=k_\infty$. Ebenso liefert die Annäherung an $k_0$ von oben den optimalen Rand $s=1$ bei $k=k_0$. Die minimalen Fehler in den beiden festen Randräumen sind stetig in $k$, etwa bei festem $a_1$ und stetig variiertem $a_2$. Sie können sich in den offenen Bereichen $(k_\infty,1)$ und $(1,k_0)$ nicht schneiden, da dort kein innerer Minimierer existiert. Somit bleibt in jedem dieser Bereiche derselbe Rand optimal wie an seiner äußeren Grenze. Die jeweilige Antwort kann dort kein Kontaktpolynom vom Grad höchstens $d$ sein, denn das würde $k=1$ voraussetzen.

Für $L=0$ und $k_\infty<k<1$ gilt die Klassifikation als Polynomgrenze zunächst auf $[\delta,U]$ für hinreichend kleines $\delta>0$, da $k$ und $k_\infty$ stetig in der unteren Intervallgrenze sind. Die besten Polynomfehler auf $[\delta,U]$ konvergieren beim Grenzübergang $\delta\downarrow0$ gegen den besten Polynomfehler auf $[0,U]$. Dazu sind die Polynomkoeffizienten auf einem festen Teilintervall gleichmäßig beschränkt und jede konvergente Teilfolge liefert ein Polynom auf $[0,U]$ mit derselben Fehlerschranke. Der Polynomfehler ist damit eine Untergrenze für das ursprüngliche Infimum. Die gleichmäßige Approximation des Polynoms durch $s\downarrow0$ auf $[0,U]$ liefert die andere Richtung. Der Endpunkt $k=k_\infty$ folgt durch Stetigkeit der Fehler in den Zielgewichten. In diesem Bereich gibt es auch auf $[0,U]$ keine zulässige Antwort, die das Infimum annimmt.

### Zahlenprobe

Für $[1,10]$, $(t_1,t_2)=(4,9)$, $d=1$ und $a_1=1$ gilt näherungsweise $k=4.296900/|a_2|$, $k_\infty=0.631685$ und $k_0=1.275882$.

| $a_2$ | $k$ (gerundet) | Optimale Antwort |
| --- | --- | --- |
| $-10$ | $0.429690$ | Einzelpol bei $\tau\simeq20.215712$ |
| $-6$ | $0.716150$ | Quadratisches Polynom als Grenzwert |
| $-4$ | $1.074225$ | Pol bei null als Grenzwert |
| $-3$ | $1.432300$ | Einzelpol bei $\tau\simeq0.620242$ |

Die Gewichte und Skalen sind synthetisch. Für H96 bleibt die Zuordnung zu Beobachtungen offen.

Der [Minimax-Abgleich für mehr als zwei gleichsignierte Pole](OP5_J_Minimax_Polreduktion.md) behandelt die allgemeine Reduktion von $r$ auf $r-1$ Pole und die dafür nötigen exakten Stützstellen.
