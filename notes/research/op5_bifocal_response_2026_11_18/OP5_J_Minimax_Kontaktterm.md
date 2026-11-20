# OP5: Optimaler Kontaktterm für einen schweren Pol

20. November 2026. Analytische Erkundung in M. Die [Auflösungsrechnung](OP5_J_Polaufloesung.md) hat einen schweren statischen Pol durch sein Taylor-Polynom angenähert. Das liefert ein Gegenmodell, aber noch keine optimale Grenze, weil die lokalen Koeffizienten im Fit frei sein können. Hier übertragen wir die klassische beste gleichmäßige Approximation des Reziproken auf den [kalibrierten OP5-Kanal](OP5_J_Gravitative_Reichweitenkalibrierung.md) und geben die dafür nötigen Stützstellen an. Es erfolgt kein H96-Datenvergleich.

## Exakter Abstand zur polynomialen Modellklasse

Sei $x=q^2$ auf $[0,X]$, $X>0$, und der zu prüfende Beitrag $f(x)=a/(T+x)$ mit $T>0$ und reellem $a\ne0$. Die Vergleichsklasse enthält jedes reelle Polynom vom Grad höchstens $d\ge0$. Setze
$$
\lambda=1+2T/X,\qquad s=\lambda-\sqrt{\lambda^2-1}
=\frac{X}{(\sqrt{T}+\sqrt{T+X})^2}.
$$
Mit der Abbildung $\xi=2x/X-1$ wird $f(x)=(2a/X)/(\xi+\lambda)$. Für den kleinsten maximalen Fehler gilt genau
$$
E_*=\inf_{\deg p\le d}\|f-p\|_{\infty,[0,X]}
=\frac{|a|X}{2T(T+X)}\,s^d.
$$
Die klassische Reziproken-Approximation gibt denselben Ausdruck auf $[-1,1]$. Für $d=0$ folgt er auch unmittelbar als halbe Differenz der beiden Endpunktwerte. Liegt das Messintervall bei $[x_{\min},x_{\max}]$, ersetzt man in der Formel $T$ durch $T+x_{\min}$ und $X$ durch seine Breite. [Kraus, Pillwein und Zikatanov, Satz 3.1](https://www.ricam.oeaw.ac.at/files/reports/09/rep09-17.pdf)

## Alternation und Lage der Stützstellen

Eine Herleitung zugleich mit den Stützstellen benutzt für $\xi=\cos\theta$ den Einheitskreisparameter $z=e^{i\theta}$. Der Faktor $z^d(z+s)/(1+sz)$ hat Betrag eins. Sein Realteil ist die rationale Funktion
$$
Q(\xi)=
\frac{T_{d+1}(\xi)+2sT_d(\xi)+s^2T_{d-1}(\xi)}
     {1+2s\xi+s^2},
$$
wobei $T_j$ das Chebyshev-Polynom und $T_{-1}=T_1$ ist. Der Nenner ist $2s(\xi+\lambda)$. Für $\xi=-\lambda$ kann man $z=-s$ in der algebraischen Formel für den Zähler wählen. Der Zähler lautet dort $\tfrac12(-s)^{-d-1}(1-s^2)^2$. Damit hat $(-1)^{d+1}s^d Q/(\lambda^2-1)$ am Pol exakt dasselbe Residuum wie $1/(\xi+\lambda)$. Ihre Differenz ist ein Polynom vom Grad höchstens $d$. Der entsprechende Approximationsfehler hat damit maximalen Betrag $s^d/(\lambda^2-1)$.

Die Phase
$$
\Theta(\theta)=d\theta+\arg\frac{e^{i\theta}+s}{1+s e^{i\theta}}
$$
wird stetig von $0$ bis $(d+1)\pi$ gewählt. Ihre Ableitung ist $d+(1-s^2)/(1+2s\cos\theta+s^2)>0$. Daher gibt es genau $d+2$ Punkte mit $\Theta=j\pi$, $j=0,\ldots,d+1$. An ihnen nimmt der Fehler abwechselnd beide Extremwerte an. Ein Polynom mit kleinerem Maximalfehler müsste gegenüber dem konstruierten Polynom an allen diesen Punkten alternierende Vorzeichen annehmen. Es hätte also wenigstens $d+1$ Nullstellen und könnte nicht vom Grad höchstens $d$ sein. Dasselbe Argument gilt für die auf diese $d+2$ Punkte beschränkte Datenreihe. Die Stützstellen sind $x_j=(X/2)(1+\cos\theta_j)$. Sie setzen voraus, dass die zu prüfende Kandidatenmasse $T$ festgelegt oder im Design berücksichtigt wird. [NIST DLMF, Chebyshev-Polynome und Minimax-Eigenschaft](https://dlmf.nist.gov/18.38)

## Fehlerschwelle im Beispiel

Für $T=100$, $X=10$, $d=2$ und $a=1$ ergibt die exakte Formel
$$
E_*\simeq2{,}579714\times10^{-7}.
$$
Die numerisch berechneten Alternationspunkte sind in aufsteigender Reihenfolge $0$, $2{,}4404424$, $7{,}4404424$ und $10$. An ihnen beträgt der Fehler abwechselnd $\pm E_*$. Der bisherige maximale Taylor-Rest war $9{,}090909\times10^{-6}$. Für $T\gg X$ ist die Verbesserung gegenüber dem Taylor-Rest asymptotisch der Faktor $2\cdot4^d$, da $s\sim X/(4T)$.

Werden beide konkurrierenden Modelle mit einer gemeinsamen absoluten Halbbreite $\epsilon$ pro Stützstelle verglichen, dann können sie auf den Alternationspunkten genau dann einen gemeinsamen zulässigen Datensatz besitzen, wenn $E_*\le2\epsilon$. Für $E_*>2\epsilon$ lässt sich der festgelegte Pol dort von *jedem* zulässigen Kontaktpolynom trennen. Andernfalls liefert die punktweise Mitte aus Pol und optimalem Kontaktterm ein überprüfbares Gegenbeispiel. Im Zahlenbeispiel ist die Halbbreitenschwelle etwa $1{,}289857\times10^{-7}$. Sie setzt dieselben Fehlerintervalle, keine weitere Polkomponente und einen kontrollierten Polynomgrad voraus. Werden zusätzliche Pole zwischen den beiden Modellen neu angepasst oder ist die lokale Reihe nur näherungsweise beschränkt, ist die Schwelle neu herzuleiten.

Der Vergleich verschärft die bisherige Auflösungsgrenze für einen festgelegten schweren Pol. Tatsächliche Fehlergrenzen, zugängliche räumliche Skalen, die Tomographie und H96 bleiben offen.
