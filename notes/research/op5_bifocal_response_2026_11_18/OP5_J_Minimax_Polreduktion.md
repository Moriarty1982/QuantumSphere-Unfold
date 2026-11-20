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

def data(tau, auxiliary=(), sigma_scale=F(1)):
    bounds = [rho_bounds(u) for u in t + tau + auxiliary]
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
    return weights, (2/(sigma_scale*ku*sum(whigh)),
                     2/(sigma_scale*kl*sum(wlow)))

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

## Unterschiedliche Genauigkeit der Stützstellen

Sei $\sigma(x)>0$ auf $[L,U]$ stetig. Verglichen wird jetzt der Fehler relativ zur örtlichen Fehlerskala,
$$
E_\sigma=\inf_g\left\|\frac{f-g}{\sigma}\right\|_\infty.
$$
Für $r$ gleichsignierte Zielpole bleibt die optimale Antwort mit höchstens $r-1$ Polen eindeutig. Die Ersatzpole liegen weiterhin je einzeln in den Lücken. Das gewichtete Residuum erreicht seinen Maximalbetrag mit wechselnden Vorzeichen an mindestens $d+2r$ Stellen. An einer solchen Auswahl aus genau $d+2r$ Stellen ergibt sich derselbe Minimax-Fehler wie auf dem ganzen Intervall.

### Stetige positive Fehlerhülle

Für einen vorläufigen Lückenvektor $\tau$ sei $P_\tau$ jetzt das Polynom mit Leitkoeffizient eins vom Grad $n=d+2r-1$, das
$$
\lambda_\tau=\left\|\frac{P_\tau}{D_\tau\sigma}\right\|_\infty
$$
minimiert. Der [gewichtete Alternationssatz](https://people.sc.fsu.edu/~jburkardt/publications/vgb_2016.pdf) liefert Existenz, Eindeutigkeit und $n+1$ Alternationspunkte. Er wird auf die Approximation von $x^n$ durch Polynome vom Grad höchstens $n-1$ mit dem stetigen positiven Gewicht $1/(D_\tau\sigma)$ angewandt. Zwischen den Alternationspunkten liegen $n$ verschiedene Nullstellen von $P_\tau$. Daher sind alle Werte
$$
V_i(\tau)=(-1)^n P_\tau(-u_i)
$$
positiv. Die Koeffizienten von $P_\tau$ hängen stetig von $\tau$ ab. Auf der kompakten Lückenbox sind die Gewichte $1/(D_\tau\sigma)$ gleichmäßig nach unten und oben beschränkt, und der Vergleich mit $x^n$ liefert eine einheitliche Normschranke für $P_\tau$. Die Koeffizienten sind deshalb beschränkt. Bei $\tau^{(k)}\to\tau$ minimiert jede Koeffizientengrenze die Grenznorm, da die Gewichte gleichmäßig konvergieren. Die Eindeutigkeit des Grenzpolynoms ergibt die Stetigkeit.

Mit diesen $V_i$ definiert man $w_i,S,Q_\tau$ wie oben. Die Vorzeichen von $Q_\tau(-t_i)$ liefern dieselbe stetige Abbildung der Lückenbox in ihr Inneres. Am Brouwer-Fixpunkt ist
$$
g_*=f-\frac{(-1)^nP_\tau}{S D_\tau},\qquad E_\sigma=\frac{\lambda_\tau}{S}.
$$
Das Kürzen der Zielpole und die positiven Ersatzgewichte folgen aus denselben Auswertungen wie im ungewichteten Fall. Da $\sigma>0$ ist, übertragen die gewichteten Extremwerte ihre Vorzeichen unverändert auf die Differenz zweier Kandidaten. Die Gradgrenze und die dividierte Differenz beweisen damit Optimalität und Eindeutigkeit. Für allgemeine $\sigma$ liefert der Satz mindestens $n+1$ Alternationspunkte. Der Beweis setzt keine Alternation an den Intervallenden voraus.

### Trennschwelle für Fehlerintervalle

Haben beide Vorhersagen die Fehlerhalbbreite $\kappa\sigma(x)$, dann ist die genaue Schwelle für ihre Trennung $\kappa_*=E_\sigma/2$. Für $\kappa<\kappa_*$ sind die Vorhersageintervalle jedes reduzierten Kandidaten und des Zielmodells an wenigstens einem der $n+1$ Alternationspunkte disjunkt. Ab $\kappa=\kappa_*$ überlappen die Intervalle des optimalen Kandidaten und des Zielmodells auf dem ganzen Intervall. An den Extrempunkten berühren sie sich bei Gleichheit. Mit nur $n$ beliebigen exakten Stützstellen existiert der Interpolant aus dem vorigen Abschnitt, auch bei beliebiger positiver $\sigma$.

Für eine bekannte gemeinsame Beobachtungsabbildung $y(x)=A(x)f(x)+C(x)$ mit stetigem $A$ ohne Nullstelle und einer positiven Fehlerskala $\sigma_y$ der beobachteten Antwort kann man $\sigma=\sigma_y/|A|$ setzen. Der gemeinsame additive Beitrag $C$ fällt in der Differenz heraus. Bei H96 ist eine solche Abbildung mit belastbarer Fehlerskala weiterhin herzuleiten.

### Explizite Rechnung bei polynomialer Fehlerhülle

Für $\sigma(x)=c_\sigma\prod_{\ell=1}^k(x+\eta_\ell)$ mit $c_\sigma>0$, $\eta_\ell>0$ und $0\le k\le d$ kann man die Einheitskreiskonstruktion direkt verwenden. Man hängt die festen $\eta_\ell$ an die Parameterliste $u$ an und ersetzt den Vorfaktor $z^d$ in $B_\tau$ durch $z^{d-k}$. Die Phase wächst weiterhin insgesamt um $n\pi$. Mit
$$
D_\tau^{+}(x)=D_\tau(x)\prod_\ell(x+\eta_\ell)
$$
ist $D_\tau^{+}R_\tau$ der Residualzähler bis auf Normierung. $K_\tau$ und $V_i$ aus der ursprünglichen expliziten Formel werden über die verlängerte Liste berechnet. Dann gelten $f-g_*=(-1)^n c_\sigma E_\sigma\big(\prod_\ell(x+\eta_\ell)\big)R_\tau$ und
$$
E_\sigma=\frac{2}{c_\sigma K_\tau S}.
$$
Die zusätzlichen Faktoren sind im Quotienten $w_i(\widehat\tau)/w_i(\tau)$ zweier Lückenvektoren fest und kürzen sich. Daher gelten die monotone Fixpunktiteration und ihre Einschließungen auch für diese Fehlerhüllen. Die Phase liefert in diesem Fall genau $n+1$ Alternationspunkte einschließlich beider Intervallenden.

Beim Drei-Pol-Beispiel mit $d=1$ und $\sigma(x)=(x+2)/3$ ist die Fehlerskala am unteren Ende eins und am oberen Ende vier. Der gewichtete Minimax-Abgleich liefert
$$
(\tau_1,\tau_2)\simeq(4.04310364408,11.13017049743),
\qquad
2.022788725072\cdot10^{-8}<E_\sigma<2.022788725075\cdot10^{-8}.
$$
Die inneren Alternationspunkte liegen näherungsweise bei $1.263417489$, $2.115391605$, $3.707800639$, $6.101426025$ und $8.738411472$. Die Fehlerhalbbreite $\kappa\sigma$ hat damit eine Trennschwelle von $\kappa_*\simeq1.01139436254\cdot10^{-8}$.

Die Fehlerschranke lässt sich mit der obigen Bruchrechnung nachprüfen. Das zusätzliche feste Argument $2$ geht nur in die Liste der $\rho$-Werte ein. Der Faktor $c_\sigma=1/3$ geht in die Fehlergrenzen ein. Mit diesen Argumenten für `data` ergibt sich die Prüfung:

~~~python
lo = tuple(map(F, ("4.0431036440795", "11.1301704974249")))
hi = tuple(map(F, ("4.0431036440798", "11.1301704974252")))
wl, el = data(lo, auxiliary=(F(2),), sigma_scale=F(1, 3))
wu, eu = data(hi, auxiliary=(F(2),), sigma_scale=F(1, 3))
assert all(root_sum_bounds(x, wl)[1] < 0 for x in lo)
assert all(root_sum_bounds(x, wu)[0] > 0 for x in hi)
assert F("2.022788725072e-8") < eu[0] <= el[1] < F("2.022788725075e-8")
~~~

## Minimax-Abgleich auf vorgegebenen Stützstellen

Seien $x_0<\cdots<x_n$ beliebige vorgegebene Stützstellen in $[L,U]$, mit $n=d+2r-1$. Die lokalen Fehlerskalen $\sigma_j$ sind positiv. Gesucht ist jetzt
$$
E_X=\inf_g\max_{0\le j\le n}\frac{|f(x_j)-g(x_j)|}{\sigma_j}
$$
für dieselbe Klasse von Antworten mit höchstens $r-1$ Polen. Die Stützstellen und Fehlerskalen bestimmen eine $r\times r$-Matrix, aus deren größtem Eigenwert und positivem Eigenvektor der beste Abgleich folgt.

### Konstruktion aus der Interpolationsmatrix

Setze
$$
\omega(x)=\prod_{j=0}^n(x-x_j),\quad
\gamma_j=\frac{1}{|\omega'(x_j)|},\quad
L_i(x)=\prod_{\ell\ne i}(x+t_\ell),\quad
\Delta_i=L_i(-t_i).
$$
Für einen Ersatznenner $Q=\sum_{i=1}^r v_i L_i$ mit $v_i>0$ und $\sum_i v_i=1$ gilt $Q(-t_i)=v_i\Delta_i$. Somit liegt je eine einfache Nullstelle in jeder Lücke der negativen Zielpole. Schreibe $D(x)=Q(x)\prod_i(x+t_i)$ und interpoliere das Polynom $P$ vom Grad höchstens $n$, das an $x_j$ den Wert $(-1)^{n-j}D(x_j)\sigma_j$ annimmt. In der Lagrange-Formel kürzen sich die alternierenden Vorzeichen gegen die von $\omega'(x_j)$. Daher ist der Leitkoeffizient $\sum_j\gamma_j D(x_j)\sigma_j>0$. An den negativen Zielpolen ergibt sich
$$
(-1)^n P(-t_i)=
\left(\prod_{j=0}^n (t_i+x_j)\right)
  \sum_{j=0}^n\gamma_j\sigma_j L_i(x_j)Q(x_j).
$$
Am Zielpol nimmt $D f$ den Wert $a_i\Delta_i^2 v_i$ an. Damit alle Zielpole beim Abzug des skalierten Residuals auf einmal verschwinden, definiere
$$
c_i=\frac{\prod_j(t_i+x_j)}{a_i\Delta_i^2},\qquad
G_{ik}=\sum_{j=0}^n\gamma_j\sigma_j L_i(x_j)L_k(x_j),\qquad
A=\operatorname{diag}(c_i)\,G.
$$
Die Kürzungsbedingungen für $g=f-(-1)^n E P/D$ lauten dann $Av=E^{-1}v$.

$G$ ist als Gram-Matrix positiv definit. Eine Linearkombination der $L_i$ kann nur dann an allen Stützstellen verschwinden, wenn sie als Polynom vom Grad höchstens $r-1$ identisch null ist. Auswerten bei $-t_i$ zeigt dann, dass sämtliche Koeffizienten null sind. $A$ ist ähnlich zu der symmetrischen positiv definiten Matrix $\operatorname{diag}(\sqrt{c_i})\,G\,\operatorname{diag}(\sqrt{c_i})$ mit strikt positiven Einträgen. Ihr größter Eigenwert $\mu$ ist einfach und hat einen strikt positiven Eigenvektor. Im Rayleigh-Quotienten verbessert der komponentenweise Betrag jeden Vektor mit gemischten Vorzeichen strikt. Ein nichtnegativer maximierender Eigenvektor muss wegen der positiven Matrix strikt positiv sein. Ein zweiter Eigenvektor zum selben Eigenwert könnte orthogonal zu ihm gewählt werden und hätte gemischte Vorzeichen. Der zugehörige Eigenvektor von $A$ wird auf $\sum_i v_i=1$ normiert.

Mit diesem $v$ lassen sich alle Zielpolfaktoren aus $g_*=f-(-1)^n P/(\mu D)$ kürzen. Die Gradgrenze liefert danach ein Kontaktpolynom bis Grad $d$. Aus der Lagrange-Formel ist $(-1)^n P(-\tau)>0$ bei jeder positiven Ersatzpolposition $\tau$. Die Vorzeichen der übrigen Nennerfaktoren liefern damit wieder strikt positive Ersatzgewichte. Das Residuum alterniert auf allen $n+1$ Stützstellen mit gewichtetem Betrag $1/\mu$. Das Gradargument mit dividierten Differenzen beweist, dass $g_*$ der eindeutige Abgleich und
$$
E_X=\frac{1}{\mu}
$$
der exakte diskrete Minimax-Abstand ist. Die scharfe Schwelle für gemeinsame symmetrische Fehlerintervalle der Halbbreite $\kappa\sigma_j$ ist $E_X/2$.

### Rationale Einschließung

Für jeden Vektor $v$ mit positiven Komponenten erfüllen die Quotienten die [Collatz-Wielandt-Schranken](https://ddu.ext.unb.ca/6634/Lecture_notes/Lecture_4_centrality_measure.pdf)
$$
\min_i\frac{(Av)_i}{v_i}\ \le\ \mu\ \le\ \max_i\frac{(Av)_i}{v_i}.
$$
Mit einem positiven linken Eigenvektor von $A$ ist $\mu$ ein positiv gewichteter Mittelwert dieser Quotienten. Die Potenziteration aus jedem positiven Startvektor konvergiert nach Normierung zum positiven Eigenvektor, da alle anderen Eigenwerte zwischen null und $\mu$ liegen. Bei rationalen Eingaben kann man sowohl die Iteration als auch die Einschließung von $E_X$ mit exakter Bruchrechnung auswerten.

Im Drei-Pol-Beispiel mit $\sigma_j=(x_j+2)/3$ und dem Raster $(1,2,3,4,6,8,10)$ ergibt sich
$$
9.85758091713774\cdot10^{-9}<E_X<9.85758091713777\cdot10^{-9}.
$$
Das sind rund $48.73$ Prozent des gewichteten Intervallabstands $E_\sigma$. Die gerundeten Massenquadrate des für dieses Raster optimalen Abgleichs sind $\tau_1\simeq4.04760479864$ und $\tau_2\simeq11.19226082154$. Die folgende Rechnung prüft den diskreten Fehler und sein Verhältnis zur obigen Intervallschranke.

~~~python
from fractions import Fraction as F
from math import prod

t = (4, 9, 16)
a = (1, 1, 1)
x = (1, 2, 3, 4, 6, 8, 10)
sigma = tuple(F(z + 2, 3) for z in x)
gamma = [F(1, prod(abs(z - y) for y in x if y != z)) for z in x]

def L(i, z):
    return prod(z + u for j, u in enumerate(t) if j != i)

c = [F(prod(z + u for z in x), a[i]*L(i, -u)**2)
     for i, u in enumerate(t)]
A = [[c[i]*sum(g*s*L(i,z)*L(k,z) for z,g,s in zip(x,gamma,sigma))
      for k in range(len(t))] for i in range(len(t))]

v = [F(1)]*len(t)
for _ in range(10):
    v = [sum(row[k]*v[k] for k in range(len(t))) for row in A]
Av = [sum(row[k]*v[k] for k in range(len(t))) for row in A]
ratios = [y/z for y,z in zip(Av,v)]
lo, hi = 1/max(ratios), 1/min(ratios)
assert F("9.85758091713774e-9") < lo <= hi < F("9.85758091713777e-9")
assert F("0.48732627") < lo/F("2.022788725075e-8")
assert hi/F("2.022788725072e-8") < F("0.48732628")
~~~

Die Rasterwerte und die Fehlerhülle sind synthetisch. Das Verfahren ist auf gegebene Stützstellen und lokale Unsicherheiten anwendbar, sobald die Beobachtungsabbildung für H96 vorliegt.
