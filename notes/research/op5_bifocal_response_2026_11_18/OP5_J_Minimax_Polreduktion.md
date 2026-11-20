# OP5: Minimax-Reduktion um einen Pol

20. November 2026. Analytische Erkundung in M. Wir erweitern den [Zweipolvergleich](OP5_J_Zweipol_gegen_Einzelpol.md) auf $r$ gleichsignierte Zielpole gegen höchstens $r-1$ freie Pole. Die Eingabe ist wieder die gravitationskalibrierte, statische Antwort in $x=q^2$.

## Aussage

Sei
$$
f(x)=\sum_{i=1}^r\frac{a_i}{x+t_i},
\qquad 0<t_1<\cdots<t_r,\qquad a_i>0,\qquad r\ge2.
$$
Auf $[L,U]$ mit $0\le L<U$ gibt es unter allen Antworten $g=p+\sum_{j=1}^{r-1} b_j/(x+\tau_j)$ mit $\deg p\le d$, $d\ge0$, $\tau_j>0$ und reellen $b_j$ genau eine beste gleichmäßige Approximation als Funktion. Nullgewichte und zusammenfallende Pole sind als Kandidaten zugelassen. Die beste Antwort hat $r-1$ verschiedene Pole und erfüllt
$$
t_j<\tau_j<t_{j+1},\qquad b_j>0\qquad(1\le j\le r-1).
$$
Ihr Fehler alterniert an genau $d+2r$ Punkten einschließlich der Intervallenden. Bei negativen Zielgewichten gilt die Aussage nach gemeinsamem Vorzeichenwechsel.

## Interpolation der Polwerte und Fixpunkt

Setze $J=2r-1$, $n=d+J$, $c=(L+U)/2$, $h=(U-L)/2$ und
$$
\rho(u)=\frac{h}{c+u+\sqrt{(c+u)^2-h^2}}.
$$
Für einen vorläufigen Vektor $\tau$ in der abgeschlossenen Box $\prod_{j=1}^{r-1}[t_j,t_{j+1}]$ fasse die $J$ Parameter $(t_1,\ldots,t_r,\tau_1,\ldots,\tau_{r-1})$ als $u_i$ zusammen. Schreibe $\rho_i=\rho(u_i)$ sowie
$$
\begin{aligned}
D_\tau(x)&=\prod_{i=1}^J(x+u_i), &
K_\tau&=\frac{(h/2)^J}{\prod_{i=1}^J\rho_i}, \\
B_\tau(z)&=z^d\prod_{i=1}^J\frac{z+\rho_i}{1+\rho_i z}, &
R_\tau(x)&=\tfrac12(B_\tau(z)+B_\tau(z)^{-1}),
\qquad x=c+\tfrac h2(z+z^{-1}).
\end{aligned}
$$
Die Argumente der $J$ Faktoren wachsen auf dem oberen Einheitskreis jeweils streng von $0$ bis $\pi$. Daher erreicht $R_\tau$ an genau $n+1$ Punkten abwechselnd die Werte $\pm1$ und hat Norm eins. Der Ausdruck $P_\tau=D_\tau R_\tau$ ist ein Polynom vom Grad höchstens $n$. Wie im Zweipolfall erhält man nach Multiplikation mit $D_\tau$ symmetrische Laurentpotenzen zwischen $-n$ und $n$. Die Auswertung bei $z=-\rho_i$ ergibt
$$
P_\tau(-u_i)=(-1)^n\frac{K_\tau}{2}V_i(\tau),\qquad
V_i(\tau)=\rho_i^{-n}\prod_{k=1}^J(1-\rho_i\rho_k)^2>0.
$$
Die Formeln bleiben auf der ganzen Box stetig, auch wenn vorläufige Pole zusammenfallen.

Definiere für $i\le r$
$$
\Delta_i=\prod_{\ell\ne i}(t_\ell-t_i),\qquad
w_i=\frac{V_i(\tau)}{a_i\Delta_i^2},\qquad S=\sum_{i=1}^r w_i,
\qquad
Q_\tau(x)=\frac{1}{S}\sum_{i=1}^r w_i\prod_{\ell\ne i}(x+t_\ell).
$$
$Q_\tau$ ist normiert auf Leitkoeffizient eins und hat Grad $r-1$. An $-t_i$ ist sein Wert $V_i(\tau)/(S a_i\Delta_i)$, dessen Vorzeichen $(-1)^{i-1}$ ist. Zwischen je zwei aufeinanderfolgenden Stellen $-t_i$ gibt es somit genau eine einfache Nullstelle. Deren Negative $\tau'_j\in(t_j,t_{j+1})$ hängen stetig von den Koeffizienten ab, da die Nullstellen einfach und durch feste Lücken getrennt sind. Die Abbildung $\tau\mapsto\tau'$ bildet die abgeschlossene Box stetig in sich ab. [Brouwers Fixpunktsatz](https://www.math.tifr.res.in/Documents/Publications/Lectures/tifr26.pdf) liefert einen Fixpunkt, der wegen der strikten Interlazierung im Inneren liegt.

Am Fixpunkt gilt $Q_\tau=\prod_j(x+\tau_j)$. Der Zähler $D_\tau f$ nimmt an $-t_i$ den Wert $a_i\Delta_i Q_\tau(-t_i)=V_i(\tau)/S$ an. Für
$$
E=\frac{2}{K_\tau S},\qquad g_*=f-(-1)^n E R_\tau
$$
verschwinden daher sämtliche Zielpolfaktoren im Zähler von $g_*$. Nach Kürzung verbleibt über $Q_\tau$ ein Zähler vom Grad höchstens $d+r-1$. Polynomdivision und Partialbruchzerlegung liefern die verlangte Form. Auswertung vor der Kürzung bei $-\tau_j$ ergibt
$$
b_j=-\frac{V_{r+j}(\tau)}{S\prod_{i=1}^r(t_i-\tau_j)
                              \prod_{k\ne j}(\tau_k-\tau_j)}.
$$
Im ersten Produkt sind $j$ Faktoren negativ und im zweiten $j-1$. Damit ist $b_j>0$.

## Optimalität und minimale Zahl exakter Stützstellen

Für zwei Kandidaten $g,g_*$ hat ihre Differenz nach Multiplikation mit den beiden Ersatznennern einen Zähler vom Grad höchstens $d+2r-2=n-1$. Die Ersatznenner sind auf dem Intervall positiv. Hätte $g$ einen kleineren Fehler als $E$, müsste dieser Zähler an den $n+1$ Extrempunkten des Residuals $f-g_*$ alternierende Vorzeichen haben und dazwischen mindestens $n$ verschiedene Nullstellen. Bei Fehler höchstens $E$ hat der Zähler schwach alternierende Vorzeichen. Seine dividierte Differenz der Ordnung $n$ ist null. In der Lagrange-Formel für diese Differenz haben alle Summanden dasselbe schwache Vorzeichen, also müssen sämtliche Zählerwerte und damit der Zähler identisch verschwinden. Damit ist $g_*$ eindeutig. Seine echten, geordneten Pole sind eindeutig, also ist auch der Fixpunkt eindeutig. Das Argument liefert denselben Minimax-Fehler $E$ bereits auf den $n+1$ Extrempunkten.

Bei nur $n$ beliebigen verschiedenen Stützstellen $x_1,\ldots,x_n$ in $[L,U]$ kann das reduzierte Modell die Zielwerte genau interpolieren. Setze $\Omega(x)=\prod_{j=1}^n(x-x_j)$ und ersetze in der obigen Formel für $w_i$ die Werte $V_i(\tau)$ durch $V_i^{\mathrm{int}}=(-1)^n\Omega(-t_i)>0$. Der so konstruierte Nenner $Q$ hat wieder eine einfache Nullstelle in jeder Lücke. Mit $D=(\prod_i(x+t_i))Q$ lautet der interpolierende Kandidat
$$
g_{\mathrm{int}}(x)=f(x)-\frac{(-1)^n\Omega(x)}{S D(x)}.
$$
An jedem $-t_i$ stimmen die beiden Zähler überein, sodass sich die Zielpole kürzen. An den neuen Polen ist $(-1)^n\Omega(-\tau_j)>0$, also haben auch hier die Ersatzpole positive Gewichte. Der Rest verschwindet an den vorgegebenen Stützstellen. Dieselbe Gradgrenze für Kandidatendifferenzen zeigt, dass der Interpolant auf $n$ Stellen eindeutig ist. Bei weniger Stellen kann man auf $n$ ergänzen.

Bei $n+1=d+2r$ verschiedenen exakten Stützstellen scheidet jeder Kandidat mit höchstens $r-1$ Polen aus. Der Zähler von $f-g$ hat über dem Produkt der Ziel- und Ersatznenner Grad höchstens $n$ und müsste an $n+1$ Stellen verschwinden. Ein identisch verschwindender Zähler würde alle $r$ sichtbaren Zielpole in $g$ erzwingen. Genau $d+2r$ Stellen sind daher nötig und ausreichend, wenn nur zwischen diesen Modellklassen entschieden werden soll und der Zielvektor $f$ gegeben ist.

## Drei Pole gegen zwei

Für $[L,U]=[1,10]$, $d=1$, $(t_1,t_2,t_3)=(4,9,16)$ und $a_i=1$ liefert die numerische Auswertung
$$
(\tau_1,\tau_2)\simeq(4.04687865984,11.18640619550),\qquad
(b_1,b_2)\simeq(1.05766563432,1.76305659918),\qquad
E\simeq4.16856060828\times10^{-8}.
$$
Die Fixpunktiteration aus den Lückenmitten stabilisierte sich in diesem Beispiel nach sieben Anwendungen bis auf $10^{-13}$ in den Massenquadraten. Brouwers Satz liefert die Existenz, und die Alternation beweist die Eindeutigkeit. Die globale Konvergenz und rationale Fehlerschranken sind im nächsten Abschnitt hergeleitet. Die sieben Alternationspunkte liegen näherungsweise bei
$$
1,\quad 1.328587207,\quad 2.359037983,\quad 4.162774779,\quad
6.605852285,\quad 8.972871652,\quad 10.
$$
Für die sechs Stellen $(1,2,3,4,6,10)$ ergibt der exakte Interpolationsabgleich hingegen
$$
Q(x)=x^2+\frac{14995625}{991073}x+\frac{44413452}{991073},\qquad
S=\frac{1982146}{147}.
$$
An diesen sechs Stellen stimmen die Antworten exakt überein. Bei $x=8$ beträgt das Residuum $f-g_{\mathrm{int}}=-1715/7745442216$.

Die Fehlerwerte beziehen sich auf synthetische Antworten in der verwendeten Normierung. Die Abbildung auf tatsächlich messbare H96-Antworten bleibt offen.

## Globale Konvergenz und überprüfbare Schranken

Bezeichne die Abbildung des Lückenvektors mit $T(\tau)=\tau'$. Sie erhält die komponentenweise Ordnung und ist strikt in jeder Ausgabekomponente, sobald mindestens eine Eingabekomponente strikt wächst und die anderen nicht sinken.

Seien dazu $\tau\le\sigma$ und $w_i(\tau)$, $w_i(\sigma)$ die jeweiligen Interpolationsgewichte. Die Funktion $\rho(u)$ fällt strikt mit $u$. Im Quotienten der Gewichte kürzen sich sämtliche festen Faktoren und es bleibt
$$
c_i:=\frac{w_i(\sigma)}{w_i(\tau)}
=\prod_{j=1}^{r-1}
  \left(\frac{1-\rho(t_i)\rho(\sigma_j)}
             {1-\rho(t_i)\rho(\tau_j)}\right)^2.
$$
Jeder Faktor wächst als Funktion von $\rho(t_i)$ und wächst strikt, wenn $\sigma_j>\tau_j$. Daher fällt $c_i$ mit $t_i$, im strikten Fall sogar strikt.

Innerhalb einer Lücke sind die Nullstellen von $Q_\tau(-x)$ genau die Nullstellen von
$$
M_\tau(x)=\sum_{i=1}^r\frac{w_i(\tau)}{t_i-x}.
$$
$M_\tau$ wächst dort strikt, da seine Ableitung $\sum_i w_i(\tau)/(t_i-x)^2$ positiv ist. Setze $\xi=T_j(\tau)$ und wähle $c$ zwischen $c_j$ und $c_{j+1}$. Dann gilt
$$
M_\sigma(\xi)=\sum_i \frac{w_i(\tau)(c_i-c)}{t_i-\xi}\le0.
$$
Hier wurde $cM_\tau(\xi)=0$ abgezogen. Für $i\le j$ ist der Nenner negativ und $c_i\ge c$. Für $i>j$ ist der Nenner positiv und $c_i\le c$. Daher liegt die neue Nullstelle $T_j(\sigma)$ rechts von $\xi$ oder stimmt mit ihr überein. Im strikten Fall kann man $c_j>c>c_{j+1}$ wählen, und die Ungleichung wird strikt.

Beginne mit $\ell^{(0)}=(t_1,\ldots,t_{r-1})$ und $u^{(0)}=(t_2,\ldots,t_r)$. Weil $T$ die Box ins Innere abbildet, gilt $\ell^{(0)}<T(\ell^{(0)})$ und $T(u^{(0)})<u^{(0)}$. Die Iterierten der unteren Ecke steigen komponentenweise, die der oberen fallen. Beide bleiben in der Box und schließen die Iterierten jedes anderen Startwerts in der Box ein. Die Grenzvektoren sind wegen der Stetigkeit Fixpunkte. Die bereits bewiesene Eindeutigkeit ergibt denselben Grenzwert $\tau_*$ für beide Folgen. Dies liefert auch einen Existenzbeweis über monotone Folgen.

Allgemeiner sind $\ell\le T(\ell)$ und $T(u)\le u$ bei $\ell\le u$ hinreichend für $\ell\le\tau_*\le u$. Der Beweis verwendet dieselben monotonen Iterationen. Bei Vektoren strikt innerhalb ihrer Lücken lassen sich diese beiden Bedingungen über $M_\ell(\ell_j)\le0$ und $M_u(u_j)\ge0$ direkt prüfen. Das ermöglicht eine Zertifizierung auch dann, wenn die gerundeten Näherungswerte durch schnelle numerische Verfahren gewonnen wurden.

Definiere $e(\tau)=2/(K_\tau S(\tau))$ auch für vorläufige $\tau$. Bei steigenden Eingabekomponenten wachsen $K_\tau$ und die $w_i$ gemäß ihren Formeln. Daraus folgt
$$
e(u)\le E\le e(\ell).
$$
So liefert die Poleinschließung zugleich eine Einschließung des optimalen Fehlers.

### Rationale Prüfung im Drei-Pol-Beispiel

Für die vorigen Werte ergeben sich die strikten Schranken
$$
\begin{aligned}
4.0468786598444 &< \tau_1 < 4.0468786598446,\\
11.1864061954984 &< \tau_2 < 11.1864061954986,\\
4.168560608275\cdot10^{-8} &< E < 4.168560608277\cdot10^{-8}.
\end{aligned}
$$
Die Randvektoren sind exakte Dezimalbrüche. Der folgende Nachweis schließt jede benötigte Quadratwurzel rational ein und prüft die Vorzeichen sowie die Fehlerschranken mit exakter Bruchrechnung.

~~~python
from fractions import Fraction as F
from math import isqrt, prod

t = (F(4), F(9), F(16))
c, h = F("5.5"), F("4.5")
n = 6
scale = 10**36

def rho_bounds(u):
    square = (c + u)**2 - h*h
    k = isqrt(square.numerator * scale**2 // square.denominator)
    return h/(c + u + F(k + 1, scale)), h/(c + u + F(k, scale))

def data(tau):
    bounds = [rho_bounds(u) for u in t + tau]
    low, high = zip(*bounds)
    weights = []
    for i in range(len(t)):
        delta = prod(v - t[i] for j, v in enumerate(t) if i != j)
        wl = high[i]**(-n) * prod((1 - high[i]*v)**2 for v in high)
        wu = low[i]**(-n) * prod((1 - low[i]*v)**2 for v in low)
        weights.append((wl/delta**2, wu/delta**2))
    wlow, whigh = zip(*weights)
    kl = (h/2)**len(bounds) / prod(high)
    ku = (h/2)**len(bounds) / prod(low)
    return weights, (2/(ku*sum(whigh)), 2/(kl*sum(wlow)))

def root_sum_bounds(x, weights):
    terms = [sorted((lo/(v-x), hi/(v-x)))
             for v, (lo, hi) in zip(t, weights)]
    return tuple(map(sum, zip(*terms)))

lo = tuple(map(F, ("4.0468786598444", "11.1864061954984")))
hi = tuple(map(F, ("4.0468786598446", "11.1864061954986")))
wl, el = data(lo)
wu, eu = data(hi)
assert all(root_sum_bounds(x, wl)[1] < 0 for x in lo)
assert all(root_sum_bounds(x, wu)[0] > 0 for x in hi)
assert F("4.168560608275e-8") < eu[0] <= el[1] < F("4.168560608277e-8")
~~~
