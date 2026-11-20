# OP5: Auflösungsgrenzen für nahe und schwere Vermittlerpole

20. November 2026. Analytische Erkundung in M. Die [Mehrpolrekonstruktion](OP5_J_Mehrpolrekonstruktion.md) trennt verschiedene statische Polmassen aus exakten Antwortwerten. Die [Kontakttermrekonstruktion](OP5_J_Kontakttermrekonstruktion.md) lässt zusätzlich unbekannte lokale Beiträge begrenzten Grades zu. Hier werden Modellpaare konstruiert, die bei endlicher absoluter Genauigkeit dieselben Daten zulassen. Die Fehlergrenzen beziehen sich auf die bereits kalibrierte Antwort $f$ nach Tracerbereinigung. Es erfolgt kein Vergleich mit H96-Daten.

## Nahe Pole gleicher oder entgegengesetzter Stärke

Sei $x=q^2\ge x_{\min}\ge0$, $t>0$ das mittlere Massenquadrat und $0<\delta<t$ der halbe Abstand der beiden Massenquadrate. Für gleich große Gewichte $a$ ergeben sich die beiden Fälle
$$
\begin{aligned}
f_+(x)&=\frac a{x+t-\delta}+\frac a{x+t+\delta},\\
f_-(x)&=\frac a{x+t-\delta}-\frac a{x+t+\delta}.
\end{aligned}
$$
Der Vergleich von $f_+$ mit dem Einzelpol $f_0=2a/(x+t)$ und von $f_-$ mit dem Modell ohne diese beiden Beiträge ergibt die exakten Differenzen
$$
f_+-f_0=\frac{2a\delta^2}{(x+t)[(x+t)^2-\delta^2]},\qquad
f_-=\frac{2a\delta}{(x+t)^2-\delta^2}.
$$
Die Beträge sind für $x\ge x_{\min}$ monoton fallend und am kleinsten zugänglichen $x$ am größten. Bei gleichem Vorzeichen ist die Abweichung vom passenden mittleren Einzelpol quadratisch im Abstand. Bei exakt entgegengesetzten Gewichten ist die Abweichung vom Modell ohne beide Pole linear. Dieselben anderen Pole oder lokalen Beiträge können in beiden Vergleichsmodellen hinzugefügt werden.

Für zwei Modelle $F_1,F_2$ und absolute Fehlerintervalle mit gemeinsamer Halbbreite $\epsilon(x_i)$ überlappen die zulässigen Daten an allen Stützstellen, wenn
$$
|F_1(x_i)-F_2(x_i)|\le2\epsilon(x_i)\qquad\text{für alle }i.
$$
Ein konkreter Datensatz im Überlapp ist der Mittelpunkt der beiden Vorhersagen. Bei einer konstanten Fehlerschranke genügt es daher, die obigen Maximalwerte bei $x_{\min}$ mit $2\epsilon$ zu vergleichen. Das ist eine deterministische Mehrdeutigkeit für diese Modellpaare und keine Aussage über ein Wahrscheinlichkeitsmodell oder über den optimalen Unterschied zu sämtlichen konkurrierenden Modellen.

Als Kontrolle mit $a=1$, $t=4$, $\delta=0{,}01$, $x_{\min}=1$ liegen die maximalen Unterschiede bei $1{,}6000064\times10^{-6}$ und $8{,}0000320\times10^{-4}$. Bei absolutem Fehler höchstens $5\times10^{-4}$ sind unter diesem Fehlerkriterium beide Modellpaare mehrdeutig. Ein sehr kleiner Fehler wäre daher besonders für gleichsignierte nahe Pole erforderlich.

## Dieselbe Grenze in der Rangmatrix

Für genau zwei Pole $t_1\ne t_2$ und je zwei Knoten $x_1,x_2$ und $y_1,y_2$ liefert die Cauchy-Faktorisierung der vorigen Rechnung im Betrag
$$
|\det L_0|
=
\frac{|a_1a_2|\,
|x_2-x_1|\,|y_2-y_1|\,(t_2-t_1)^2}
{\prod_{u\in\{x_1,x_2,y_1,y_2\}}(u+t_1)(u+t_2)} .
$$
Dazu multipliziert man die beiden zweidimensionalen Cauchy-Determinanten und die Gewichte. Der Ausdruck bleibt unabhängig von den Vorzeichen im Zählerfaktor quadratisch im Polabstand. Bei festen Knoten und Gewichten kann ein exakter Rang zwei also beliebig nahe an einer singulären Matrix liegen. Die Formel ist eine Aussage über das Produkt der beiden Singulärwerte, nicht über eine universelle Skalierung jedes einzelnen. Mit den obigen gleichsignierten Polen und $x=(1,4)$, $y=(9,16)$ stimmt die direkt gebildete Determinante $7{,}76632\times10^{-11}$ mit der Formel auf Rundungsgenauigkeit überein.

## Schwerer Pol und lokaler Kontaktterm

Für einen einzelnen Pol mit Massenquadrat $T>0$ und einen Messbereich $0\le x\le X$ lässt sich die Differenz zum Taylor-Kontaktpolynom bis Grad $d$ exakt schreiben:
$$
\frac{a}{x+T}
=\sum_{j=0}^d\frac{a(-x)^j}{T^{j+1}}
+\frac{a(-x)^{d+1}}{T^{d+1}(x+T)}.
$$
Der Rest hat auf dem gesamten Bereich die Schranke
$$
\left|\frac{a(-x)^{d+1}}{T^{d+1}(x+T)}\right|
\le\frac{|a|X^{d+1}}{T^{d+1}(X+T)} .
$$
Die rechte Seite ergibt sich am oberen Rand, da $x^{d+1}/(x+T)$ für $x\ge0$ nicht fällt. Kann das unbekannte Kontaktpolynom diese Taylor-Koeffizienten aufnehmen, sind ein Modell mit dem Pol und ein Modell mit dem entsprechenden Kontaktterm innerhalb der Fehlerintervalle nicht sicher trennbar, sobald die Schranke höchstens $2\epsilon$ beträgt. Für $T\gg X$ wird der Rest durch die hochgradige Potenz $ (X/T)^{d+1}$ gegenüber $|a|/T$ klein. Beispiel: $T=100$, $X=10$, $d=2$ und $a=1$ liefern höchstens $9{,}091\times10^{-6}$ Unterschied auf dem ganzen Messbereich. Ein Messbereich, der nicht bis $x=0$ reicht, kann dieselbe Obergrenze verwenden.

Die Rechnungen geben konkrete Gegenmodelle zur exakten Rekonstruktion bei endlicher Präzision. Kleinere zugängliche $q^2$ können die Trennung naher Pole verbessern; ein größerer kontrollierter Bereich in $q^2$ kann einen schweren Pol vom Kontaktterm unterscheiden. Ob beide Bereiche beobachtbar sind und ob die Tracer- und Restfehler klein genug sind, folgt nicht aus den Formeln. H96 bleibt offen.
