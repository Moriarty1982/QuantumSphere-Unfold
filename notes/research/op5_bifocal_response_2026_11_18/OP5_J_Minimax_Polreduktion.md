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

## Größere Messraster und bestimmende Teilmengen

Sei $X=\{x_1<\cdots<x_m\}$ ein vorgegebenes Raster mit $m\ge n+1$, $n=d+2r-1$. An jedem Knoten sei eine positive Fehlerskala $\sigma(x_j)$ gegeben. Für $r$ gleichsignierte Zielpole gilt
$$
E_X=\max_{\substack{Y\subseteq X\\ |Y|=n+1}} E_Y,
\qquad
E_Y=\frac{1}{\mu(A_Y)} .
$$
Hier verwendet jede Teilmenge ihre eigenen Lagrange-Gewichte in der Matrix $A_Y$ aus dem vorigen Abschnitt. Der optimale Abgleich für $X$ ist eindeutig und wird von jeder maximierenden Teilmenge bereits bestimmt.

### Beweis auf einem endlichen Raster

Für einen vorläufigen Lückenvektor $\tau$ wähle das Polynom $P_\tau$ mit Leitkoeffizient eins und Grad $n$, das $\max_{x\in X}|P_\tau(x)|/(D_\tau(x)\sigma(x))$ minimiert. Ein Minimum existiert, da eine Normschranke auf mindestens $n+1$ verschiedenen Knoten die Koeffizienten beschränkt und die Zielfunktion stetig ist. Ein Minimierer erreicht den gewichteten Maximalbetrag an mindestens $n+1$ Stellen mit wechselnden Vorzeichen. Andernfalls lassen sich die Extremstellen in höchstens $n$ aufeinanderfolgende Gruppen mit jeweils gleichem Vorzeichen aufteilen. Ein Polynom mit je einer Nullstelle zwischen den Gruppen hat Grad höchstens $n-1$ und kann durch ein gemeinsames Vorzeichen an die Extremwerte angepasst werden. Sein hinreichend kleines Vielfaches verringert nach Abzug den Fehler an allen Extremstellen. An den übrigen Knoten bleibt der Fehler wegen des strikten Abstands zum Maximum und der Endlichkeit von $X$ ebenfalls unter dem alten Maximum. Die Eindeutigkeit folgt aus der dividierten Differenz der Kandidatendifferenz an $n+1$ alternierenden Stellen.

Wie beim kontinuierlich gewichteten Vergleich liegen alle $n$ Nullstellen von $P_\tau$ zwischen Alternationspunkten. Die Werte $(-1)^n P_\tau(-t_i)$ sind positiv. Sie hängen stetig von $\tau$ ab. Die gewichteten Normen auf dem endlichen Raster sind auf der kompakten Lückenbox gleichmäßig äquivalent zur Koeffizientennorm. Bei Konvergenz der Lückenvektoren ist deshalb jede Koeffizientengrenze ein Minimierer der Grenzaufgabe. Seine Eindeutigkeit liefert die Stetigkeit.

Die Interpolation der Zielpolwerte und die Fixpunktkonstruktion aus dem Abschnitt zur Fehlerhülle gelten daher auch für $X$. Sie liefern genau eine beste Antwort mit positiven Ersatzgewichten und einem Massenquadrat pro Lücke. Sei $Y$ eine Auswahl von $n+1$ gewichteten Alternationspunkten dieser Antwort. Das Alternationsargument für Kandidatendifferenzen zeigt, dass sie bereits auf $Y$ optimal ist und $E_Y=E_X$ gilt. Für jede Teilmenge $Y'$ gilt $E_{Y'}\le E_X$, da sie nur einen Teil der Ungleichungen auf $X$ prüft. Nimmt eine Teilmenge das Maximum an, ist der Rasterminimierer auf ihr optimal. Die Eindeutigkeit auf der Teilmenge zeigt, dass sie denselben Kandidaten bestimmt.

### Lineare Machbarkeit bei festem Fehlerniveau

Die Teilmengenformel erlaubt eine exakte Kontrolle kleiner Raster. Auf größeren Rastern lässt sich die Kombinationenzahl umgehen. Für ein vorgegebenes $e\ge0$ schreibe $g=N/Q$ mit $\deg N\le d+r-1$ und $Q=\sum_i v_i L_i$, $v_i\ge0$, $\sum_i v_i=1$. Auf $X$ sind alle $L_i$ positiv. Die Bedingungen
$$
-e\,\sigma(x)Q(x)\le f(x)Q(x)-N(x)\le e\,\sigma(x)Q(x)
\qquad (x\in X)
$$
sind linear in $v_i$ und den Koeffizienten von $N$. Für $e\ge E_X$ ist das System mit dem konstruierten Rasterminimierer erfüllbar. Für $e<E_X$ widerspricht bereits die bestimmende Alternationsmenge der Machbarkeit. Der Zähler einer Differenz $N/Q-g_*$ hat auch in dieser geschlossenen Suchmenge Grad höchstens $n-1$ und der Nenner bleibt überall auf $X$ positiv. Damit kann auch ein möglicher mehrfacher Pol am Rand des Suchraums den Fehlerwert nicht senken. Eine Halbierung des Fehlerniveaus mit linearen Machbarkeitstests schließt $E_X$ ein.

### Zehn ganzzahlige Stützstellen

Für das Drei-Pol-Beispiel mit $\sigma(x)=(x+2)/3$ wählen wir $X=\{1,2,\ldots,10\}$. Über alle $\binom{10}{7}=120$ Teilmengen ergibt sich eindeutig
$$
Y_*=\{1,2,3,4,6,9,10\},\qquad
1.10277872903767\cdot10^{-8}<E_X<1.10277872903768\cdot10^{-8}.
$$
Die Obergrenzen aller anderen Teilmengen liegen unter der Untergrenze für $Y_*$. Das Raster erreicht rund $54.52$ Prozent des kontinuierlichen gewichteten Abstands. Für gemeinsame Fehlerintervalle ist die scharfe Schwelle daher $\kappa_*=E_X/2\simeq5.51389\cdot10^{-9}$. Die folgende Rechnung prüft die Auswahl und Schranken rational.

~~~python
from fractions import Fraction as F
from itertools import combinations
from math import prod

t = (4, 9, 16)
a = (1, 1, 1)
grid = tuple(range(1, 11))

def basis(i, z):
    return prod(z + u for j, u in enumerate(t) if j != i)

def error_bounds(x):
    gamma = [F(1, prod(abs(z-y) for y in x if y != z)) for z in x]
    sigma = [F(z+2, 3) for z in x]
    scale = [F(prod(z+u for z in x), a[i]*basis(i,-u)**2)
             for i,u in enumerate(t)]
    A = [[scale[i]*sum(w*s*basis(i,z)*basis(k,z)
                       for z,w,s in zip(x,gamma,sigma))
          for k in range(len(t))] for i in range(len(t))]
    def apply(v):
        return [sum(a*b for a,b in zip(row,v)) for row in A]
    v = [F(1)]*len(t)
    for _ in range(8):
        v = apply(v)
    rates = [y/z for y,z in zip(apply(v),v)]
    return 1/max(rates), 1/min(rates)

bounds = {x: error_bounds(x) for x in combinations(grid, 7)}
best = max(bounds, key=lambda x: bounds[x][0])
lo, hi = bounds[best]
other = max(upper for x, (_, upper) in bounds.items() if x != best)
assert len(bounds) == 120
assert best == (1, 2, 3, 4, 6, 9, 10)
assert other < lo
assert F("1.10277872903767e-8") < lo <= hi < F("1.10277872903768e-8")
assert F("0.54517741") < lo/F("2.022788725075e-8")
assert hi/F("2.022788725072e-8") < F("0.54517742")
~~~

Die Formel vergleicht eine gegebene gleichsignierte Zielantwort mit der reduzierten Modellklasse. Die Zuordnung einer solchen Zielantwort und ihrer Fehlerhalbbreiten zu H96-Messungen bleibt offen.

## Prüfung direkt aus Messwerten und Fehlerbalken

Auf $n+1=d+2r$ verschiedenen Stützstellen seien Messmitten $y_j$ sowie positive Fehlerskalen $\sigma_j$ bekannt. Ein Kandidat muss $|g(x_j)-y_j|\le\kappa\sigma_j$ für alle $j$ erfüllen. Setze $m=r-1$, $\omega(x)=\prod_{j=0}^{n}(x-x_j)$ und $v(x)=(1,x,\ldots,x^m)^\mathsf T$. Definiere aus den Messwerten
$$
H(y)=(-1)^n\sum_{j=0}^{n}\frac{y_j}{\omega'(x_j)}v(x_j)v(x_j)^\mathsf T,\qquad
G=\sum_{j=0}^{n}\frac{\sigma_j}{|\omega'(x_j)|}v(x_j)v(x_j)^\mathsf T.
$$
Die Prüfung und ihre Eigenwerte sind unabhängig von der gewählten Polynombasis. $G$ ist positiv definit, da ein Polynom bis Grad $m$ mit null Norm an mehr als $m$ verschiedenen Stellen verschwinden würde.

### Ausschluss eines Modells mit weniger Polen

Ein Kandidat mit höchstens $m$ Polen hat die Form $g=N/Q$ mit $\deg N\le d+m$ und $\deg Q\le m$. Sein Nenner hat auf den Stützstellen keine Nullstelle. Sind $q$ die Koeffizienten von $Q$, dann gilt
$$
q^\mathsf T H(g)q=(-1)^n\sum_j\frac{N(x_j)Q(x_j)}{\omega'(x_j)}=0.
$$
Die Summe ist eine dividierte Differenz der Ordnung $n=d+2m+1$ eines Polynoms vom Grad höchstens $n-1$. Für jedes $z$ innerhalb der Fehlerintervalle ist
$$
H(z)\succeq H(y)-\kappa G,
$$
weil in jeder quadratischen Form der maximale Abzug durch $|z_j-y_j|\le\kappa\sigma_j$ beschränkt wird. Ist $H(y)-\kappa G$ positiv definit, ist das reduzierte Modell ausgeschlossen, auch mit frei vorgegebenen Vorzeichen seiner Polgewichte. Die Prüfung verwendet weder Zielmassen noch eine bekannte Zielantwort. Ein Kontaktpolynom vom Grad höchstens $d$ fällt in $H$ heraus.

Für positiv definites $H(y)$ liefert
$$
\kappa_0=\lambda_{\min}(H(y),G)
$$
den kritischen Wert dieses Ausschlusses. Bei negativ definit orientierten Daten kann man dieselbe Rechnung mit $-y$ durchführen. Auf größeren Rastern genügt für den Ausschluss jede Teilmenge von $d+2r$ Stützstellen mit positiver Definitheit. Hier bezeichnet $\kappa$ den Fehlerbalken um einen gemessenen Datenvektor. Beim früheren Vergleich zweier Modelle mit einem gemeinsamen Fehlerbalken um jede Vorhersage gilt weiterhin der Faktor zwei.

### Wann die Schwelle erreicht wird

Definiere bei $\kappa=\kappa_0$ den alternierend verschobenen Vektor
$$
y_j^- = y_j-\kappa_0\sigma_j\,(-1)^n \operatorname{sgn}\omega'(x_j).
$$
Dann gilt $H(y^-)=H(y)-\kappa_0G$. Liegt im Kern ein Polynom $Q$ vom Grad $m$ mit $m$ einfachen, streng negativen Nullstellen, wird die Schwelle durch ein zulässiges Modell erreicht. Dazu interpoliere $N(x_j)=Q(x_j)y_j^-$ durch ein Polynom bis Grad $n$. Die Kernbedingung besagt, dass für $k=0,\ldots,m$ jeweils $\sum_j N(x_j)x_j^k/\omega'(x_j)=0$. Zuerst verschwindet damit der Koeffizient von $x^n$ in $N$. Nach jedem solchen Schritt ist der Grad von $x^kN$ beim nächsten Test höchstens $n$, und die Summe liefert dessen Leitkoeffizienten zu $x^n$. Nacheinander verschwinden damit die obersten $m+1$ Koeffizienten von $N$. Übrig bleibt $\deg N\le n-m-1=d+m$. Polynomdivision und Partialbruchzerlegung von $N/Q$ ergeben einen zulässigen Kandidaten, der $y^-$ exakt trifft. Ohne Nachweis eines solchen Kernpolynoms liefert $\kappa_0$ eine Untergrenze für den nötigen Fehlerbalken.

Ein hinreichender Test verwendet beliebige Referenzwerte $0<u_1<\cdots<u_r$ und die Basis $L_i(x)=\prod_{\ell\ne i}(x+u_\ell)$. Hat die Darstellung von $H(y)-\kappa_0G$ in dieser Basis strikt negative Nebendiagonaleinträge, so ist ihr Kern eindimensional und hat einen strikt positiven Koeffizientenvektor. Für einen Kernvektor mit gemischten Vorzeichen würde sein komponentenweiser Betrag die quadratische Form strikt absenken und damit die positive Semidefinitheit verletzen. Ein nichtnegativer Kernvektor kann wegen der negativen Nebendiagonale keine Nullkomponente haben. Zwei unabhängige Kernvektoren würden eine Linearkombination mit einer Nullkomponente erlauben. Die positiven Koeffizienten erzwingen wechselnde Vorzeichen von $Q(-u_i)$ und damit die benötigten einfachen negativen Nullstellen.

### Anschluss an die Eigenwertformel und Zahlenprobe

Für eine exakte gleichsignierte Zielantwort mit positiven Gewichten gilt
$$
H(f)=\sum_{i=1}^r \frac{a_i}{\prod_j(t_i+x_j)}v(-t_i)v(-t_i)^\mathsf T .
$$
Bei der dividierten Differenz ersetzt man jeden Polynomfaktor in der quadratischen Form durch seinen Wert bei $-t_i$. Der bei der Division durch $x+t_i$ entstehende Polynomialteil hat Grad kleiner als $n$ und verschwindet. In der Basis der Zielpole ist $H(f)$ diagonal mit Einträgen $1/c_i$ aus der Konstruktion für feste Stützstellen. Daher ist $\lambda_{\min}(H(f),G)=1/\mu(A)$ derselbe exakte Abstand.

Für die sieben Stützstellen $(1,2,3,4,6,9,10)$ aus dem Zehn-Punkte-Raster sei $\sigma_j=(x_j+2)/3$. Die Messmitten werden synthetisch aus drei Polen bei $4,9,16$ mit Gewichten eins gewonnen und zusätzlich um $10^{-10}\sigma_j$ mal $(1,-2,1,0,2,-1,1)_j$ verschoben. Der datenbasierte Test liefert
$$
1.11248856266898\cdot10^{-8}<\kappa_0<1.11248856266900\cdot10^{-8}.
$$
An der unteren Grenze ist die Prüfmatrix positiv definit und ihre Nebendiagonale in der Referenzbasis strikt negativ. Die Nebendiagonale bleibt bis zur kritischen Schwelle negativ, da $G$ in dieser Basis strikt positive Einträge besitzt. Die negative Determinante an der oberen Grenze prüft den Verlust der positiven Definitheit. Damit ist die Schwelle im Beispiel scharf. Die folgende Rechnung prüft alle Vorzeichen und Schranken mit exakten Brüchen.

~~~python
from fractions import Fraction as F
from math import prod
from itertools import permutations

x = (1, 2, 3, 4, 6, 9, 10)
u = (4, 9, 16)  # Reference poles for the polynomial basis.
s = tuple(F(z+2, 3) for z in x)
noise = (1, -2, 1, 0, 2, -1, 1)
y = tuple(sum(F(1,z+t) for t in u) + F(v,10**10)*scale
          for z,v,scale in zip(x,noise,s))
omega_prime = tuple(prod(z-w for w in x if w != z) for z in x)
basis = [[prod(z+t for k,t in enumerate(u) if k!=i) for z in x]
         for i in range(len(u))]

def gram(weights):
    return [[sum(w*p*q for w,p,q in zip(weights,row,col)) for col in basis]
            for row in basis]

H = gram([val/den for val,den in zip(y,omega_prime)])  # n=6 is even.
G = gram([scale/abs(den) for scale,den in zip(s,omega_prime)])

def matrix(kappa):
    return [[h-kappa*g for h,g in zip(hr,gr)] for hr,gr in zip(H,G)]

def det(B, size):
    total = F(0)
    for p in permutations(range(size)):
        swaps = sum(p[i]>p[j] for i in range(size) for j in range(i+1,size))
        total += (-1)**swaps * prod(B[i][p[i]] for i in range(size))
    return total

def positive_definite(B):
    return all(det(B,k)>0 for k in range(1,len(B)+1))

lo, hi = F("1.11248856266898e-8"), F("1.11248856266900e-8")
assert positive_definite(matrix(lo))
assert det(matrix(hi), len(u)) < 0
assert all(matrix(lo)[i][j] < 0 for i in range(len(u)) for j in range(i))
~~~

Das Beispiel verwendet gesetzte Messmitten und Fehlerbalken. Die Umrechnung realer H96-Messungen in diese statische Antwort bleibt offen.

## Gemeinsame Kalibrierfehler

Zusätzlich zu den einzelnen Fehlerbalken seien $s$ bekannte Kalibrierprofile $b_\alpha=(b_\alpha(x_j))_j$ gegeben. Jedes Profil hat einen gemeinsamen unbekannten Koeffizienten für alle Stützstellen. Wir erlauben Datenvektoren
$$
z_j=y_j+\kappa\left(\epsilon_j\sigma_j+
      \sum_{\alpha=1}^s\eta_\alpha b_\alpha(x_j)\right),
\qquad |\epsilon_j|\le1,\quad |\eta_\alpha|\le1.
$$
Dieses Modell beschreibt beschränkte Fehleramplituden. Es setzt keine Wahrscheinlichkeitsverteilung voraus. Setze $B_\alpha=H(b_\alpha)$ mit derselben linearen Datenmatrix wie im vorigen Abschnitt.

Für feste $\eta$ ist die kleinste Matrix in der positiven Semidefinitheitsordnung
$$
H(y)-\kappa G+\kappa\sum_\alpha\eta_\alpha B_\alpha.
$$
Sie wird erreicht, indem die unabhängigen Fehler die alternierenden Vorzeichen $\epsilon_j=-(-1)^n\operatorname{sgn}\omega'(x_j)$ erhalten. Denn jede andere Wahl addiert zu dieser Matrix eine Summe positiv semidefiniter Rang-eins-Matrizen. Die kleinsten Matrizen für alle $\eta$ sind Konvexkombinationen der Werte an den Ecken $\nu\in\{-1,1\}^s$. Daher ist die Prüfmatrix für alle erlaubten Fehler genau dann positiv definit, wenn alle Eckmatrizen
$$
H(y)-\kappa M_\nu\succ0,\qquad M_\nu=G-\sum_{\alpha=1}^s\nu_\alpha B_\alpha
$$
positiv definit sind. In diesem Fall ist die reduzierte Polklasse ausgeschlossen.

Für $H(y)\succ0$ ist die kritische Amplitude der Matrixprüfung
$$
\kappa_{\mathrm{gemeinsam}}
 =\left[\max_{\nu\in\{-1,1\}^s}\lambda_{\max}(M_\nu,H(y))\right]^{-1}.
$$
Der Ausdruck in der Klammer ist positiv, weil der Mittelwert der $M_\nu$ gleich $G\succ0$ ist. An einer maximierenden Ecke wird die Matrix an der kritischen Amplitude singulär und bleibt positiv semidefinit. Liefert ihr Kern einen zulässigen Nenner, konstruiert die Interpolation aus dem vorigen Abschnitt an genau diesem erlaubten Datenvektor einen reduzierten Kandidaten. Dann ist die Ausschlussschwelle scharf für die gekoppelten Fehler. Bei fehlendem Nennernachweis ist sie eine Untergrenze.

### Gemeinsamer Offset und Drift

Ist $b_\alpha$ ein Polynom vom Grad höchstens $d$, dann ist $B_\alpha=0$. Jede Matrixkomponente ist eine dividierte Differenz der Ordnung $n=d+2m+1$ eines Polynoms vom Grad höchstens $d+2m$. Solche Profile fallen aus dem Test heraus und können vor der Eckenauswertung gestrichen werden. Das entspricht der Möglichkeit, sie direkt in das Kontaktpolynom aufzunehmen. Bei $d=1$ gilt dies für einen gemeinsamen Offset und eine gemeinsame lineare Drift in $x=q^2$.

Für $d=1$ ist der nächste monomiale Beitrag $b(x)=c x^2$. In einer Basis aus Polynomen mit Leitkoeffizient eins und Grad $m$ hat $H(b)$ in jeder Zelle den Eintrag $(-1)^n c=c$, da $n=2m+2$ gerade ist. Die dividierte Differenz erfasst genau den Leitkoeffizienten des Produkts. Für $c>0$ ist $H(b)$ positiv semidefinit und die Eckauswertung reduziert sich bei diesem einzelnen wirksamen Profil auf $G+H(b)$.

### Synthetische Zahlenprobe

Zum gestörten Drei-Pol-Datensatz aus dem vorigen Abschnitt fügen wir die gemeinsamen Profile $10$, $x$ und $100x^2$ hinzu. Die ersten beiden verschwinden in der Prüfmatrix. Die Matrixrechnung für die gemeinsame quadratische Drift ergibt
$$
8.36123007008602\cdot10^{-9}<\kappa_{\mathrm{gemeinsam}}<
8.36123007008604\cdot10^{-9}.
$$
An der unteren Schranke hat die Prüfmatrix in der gewählten Referenzbasis strikt negative Nebendiagonaleinträge. Da $G+H(b)$ nur positive Einträge hat, bleiben die Nebendiagonaleinträge bis zur singulären Grenze negativ. Der Kern liefert dort einen zulässigen Nenner und die Schranke ist scharf.

Würde man dieselben Profile stattdessen als zusätzliche unabhängige Punktschwankungen behandeln, ergäbe die Fehlerskala $\sigma_j+10+x_j+100x_j^2$ eine Matrixschwelle von rund $9.17353\cdot10^{-12}$. Im Beispiel ist die scharfe Schwelle bei korrekt gemeinsamem Fehler mehr als 900-mal größer. Die Größen der Profile sind für den Vergleich synthetisch gewählt. Die Rechnung verwendet die Variablen und Hilfsfunktionen aus der vorigen Zahlenprobe.

~~~python
offset = [F(10) for z in x]
tilt = [F(z) for z in x]
curvature = [F(100*z*z) for z in x]

def mode(values):
    return gram([val/den for val,den in zip(values,omega_prime)])

assert all(val == 0 for vals in (offset,tilt) for row in mode(vals) for val in row)
C = mode(curvature)
assert all(val == 100 for row in C for val in row)
G_joint = [[g+c for g,c in zip(gr,cr)] for gr,cr in zip(G,C)]
G_box = gram([(scale+a+b+c)/abs(den) for scale,a,b,c,den
              in zip(s,offset,tilt,curvature,omega_prime)])

def reduced(k, B):
    return [[h-k*b for h,b in zip(hr,br)] for hr,br in zip(H,B)]

def bracket(B):
    lo, hi = F(0), F("2e-8")
    for _ in range(75):
        mid = (lo+hi)/2
        if positive_definite(reduced(mid,B)):
            lo = mid
        else:
            hi = mid
    return lo, hi


lo, hi = bracket(G_joint)
assert F("8.36123007008602e-9") < lo <= hi < F("8.36123007008604e-9")
assert all(reduced(lo,G_joint)[i][j] < 0 for i in range(3) for j in range(i))
box_lo, box_hi = bracket(G_box)
assert F("9.17353229881560e-12") < box_lo <= box_hi < F("9.17353229881564e-12")
assert lo > 900*box_hi
~~~

Die [OP5-Kalibrierprofile](OP5_J_Kalibrierprofile.md) leiten die Antwort auf gemeinsame Gain-, Transfer-, Tracer- und Skalenfehler her. Für Messprofile müssen die Rohspektren und Kalibriergrenzen aus der tatsächlichen Messung bestimmt werden.
