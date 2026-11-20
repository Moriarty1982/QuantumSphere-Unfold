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
