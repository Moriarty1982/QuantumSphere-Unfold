# OP5: Mehrpolrekonstruktion mit unbekannten Kontakttermen

20. November 2026. Analytische Erkundung in M. Die [Mehrpolrekonstruktion](OP5_J_Mehrpolrekonstruktion.md) identifiziert statische Yukawa-Pole aus der [gravitativ kalibrierten Antwort](OP5_J_Gravitative_Reichweitenkalibrierung.md). Dort musste ein lokaler Kontaktbeitrag vor dem Eigenwertschritt abgezogen werden. Hier wird er als unbekanntes Polynom begrenzten Grades mitgeführt. Vorausgesetzt bleiben dieselbe Tracerbereinigung, kalibrierte Antwortwerte und die statische rationale Modellklasse. Es erfolgt kein H96-Datenvergleich.

## Unbekannten polynomialen Anteil entfernen

Schreibe $x=q^2$ und setze
$$
f(x)=p(x)+\sum_{\ell=1}^r\frac{a_\ell}{x+t_\ell},
\qquad \deg p\le d,\quad t_\ell>0.
$$
Die $t_\ell$ seien verschieden, die $a_\ell$ seien reell und von null verschieden. Gleiche Polmassen werden wie zuvor zusammengefasst. Ein konstanter Kontaktterm entspricht $d=0$. Lokale Terme mit einer endlichen Zahl räumlicher Ableitungen liefern in dieser isotropen statischen Darstellung ein Polynom in $q^2$. Eine weitergehende effektive Reihe braucht zusätzlich eine Schranke für den weggelassenen Rest.

Wähle $k=d+1$ feste verschiedene Anker $z_1,\ldots,z_k\ge0$ und davon verschiedene Messknoten $x$. Die dividierte Differenz $[z_1,\ldots,z_k,x]f$ hat Ordnung $k$. Sie ist der höchste Koeffizient des Interpolationspolynoms an diesen Knoten und verschwindet deshalb für $p$. Für eine einzelne reziproke Funktion gilt
$$
[z_1,\ldots,z_k,x]\frac{1}{\,\cdot+t\,}
=\frac{(-1)^k}{(x+t)\prod_{i=1}^k(z_i+t)}.
$$
Die Formel folgt durch Induktion aus der Rekursion für dividierte Differenzen. Subtrahiert man bei jedem Schritt die beiden Ausdrücke mit ausgelassenem erstem bzw. letztem Knoten, hebt der Faktor aus der Differenz dieser Knoten den Rekursionsnenner auf und liefert ein zusätzliches Minuszeichen.

Die transformierte Antwort lautet somit
$$
h(x)=(-1)^k[z_1,\ldots,z_k,x]f
=\sum_{\ell=1}^r\frac{\widetilde a_\ell}{x+t_\ell},
\qquad
\widetilde a_\ell=\frac{a_\ell}{\prod_i(z_i+t_\ell)}.
$$
Alle Pole bleiben an derselben Position. Ihre Gewichte bleiben bei den nichtnegativen Ankern von null verschieden und behalten ihre Vorzeichen. Die Matrizen der vorigen Rekonstruktion können daher auf $h$ angewandt werden. Mit zwei Gruppen zu je $r$ Knoten genügen insgesamt $2r+d+1$ verschiedene exakte Stützstellen. Für einen unbekannten konstanten Kontaktterm kostet dies gegenüber der reinen Polrechnung genau eine zusätzliche Stützstelle. Nach Bestimmung der Pole werden die Gewichte mit den Ankerfaktoren zurückgerechnet. Subtrahiert man den rekonstruierten Polanteil an den $d+1$ Ankern, bestimmen die verbleibenden Werte eindeutig $p$. Für ein reines Kontaktpolynom ist $h$ identisch null.

## Kontrolle für zwei Pole und einen linearen Kontaktterm

Setze $f(x)=0{,}4-0{,}02x+3/(x+4)-1/(x+9)$. Mit den positiven Ankern $z=(2,6)$ und den zwei Knotengruppen $(1,4)$ und $(9,16)$ sind die transformierten Gewichte $1/20$ und $-1/165$. Die numerische Rekonstruktion aus den sechs ursprünglichen Funktionswerten lieferte
$$
(t_1,t_2)\simeq(4{,}000000000002,8{,}999999999987),\qquad
(a_1,a_2)\simeq(3{,}000000000004,-1{,}000000000007).
$$
Die zurückgerechneten Kontaktkoeffizienten sind $0{,}4000000000002$ und $-0{,}0200000000000$. Ein nicht zur Rekonstruktion benutzter siebter Wert bei $x=25$ wich um weniger als $6\times10^{-14}$ von der Rückrechnung ab. Das Beispiel nutzt keinen Nullmodus und prüft die Rechenformel, keine Beobachtungsgenauigkeit.

## Welche Information noch benötigt wird

Für die Knoten $u=(z_1,\ldots,z_k,x)$ und absolute Fehlergrenzen $\epsilon(u_j)$ folgt aus der Lagrange-Darstellung
$$
|\delta h(x)|\le
\sum_{j=1}^{k+1}
\frac{\epsilon(u_j)}{\prod_{i\ne j}|u_j-u_i|}.
$$
Diese Grenzen können in die Singulärwertabschätzung der [Mehrpolrechnung](OP5_J_Mehrpolrekonstruktion.md) eingesetzt werden. Eng benachbarte Knoten und hohe Differenzenordnungen können Fehler stark verstärken. Dieselben Ankerfehler wirken in mehreren $h(x)$ und dürfen für eine statistische Fehlerrechnung nicht als unabhängige Eingaben behandelt werden. Mit geeigneter absoluter Fehlerschranke kann der Rangtest eine Untergrenze für die Zahl sichtbarer Pole geben. Ohne Grad- oder Restschranke könnte ein passend hohes Polynom jede endliche Menge von Messwerten interpolieren. Dann lässt sich aus diesen Daten allein kein Poleffekt erzwingen.

Der Kontaktterm kann somit innerhalb einer kontrollierten endlichen Modellklasse zusammen mit den Polmassen bestimmt werden. Reale Tracerfehler, die Kontrolle des höheren lokalen Rests, absolute Dichtekalibrierung und H96 bleiben offen.
