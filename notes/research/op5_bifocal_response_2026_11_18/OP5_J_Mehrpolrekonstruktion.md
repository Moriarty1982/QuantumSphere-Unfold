# OP5: Mehrpolrekonstruktion mit gemischten Vorzeichen

20. November 2026. Analytische Erkundung in M. Die [gravitative Reichweitenkalibrierung](OP5_J_Gravitative_Reichweitenkalibrierung.md) liefert ideal einen partiellen Kreuzquotienten $\mathcal B(q)$ als inverse räumliche Antwort. Dessen Konkavitätsprüfung für mehrere Pole setzt gleichsignierte Beiträge voraus. Gemischte J–D-Kopplungen können aber verschiedene Vorzeichen haben. Hier prüfen wir eine endliche Rekonstruktion der statischen Polmassen ohne dieses Vorzeichenkriterium. Voraussetzung sind dieselben kalibrierten und bereinigten Karten. Es erfolgt kein H96-Datenvergleich.

## Faktorisierung der dividierten Differenzen

Schreibe $x=q^2$ und $f(x)=1/\mathcal B(q)$ auf Modi mit definiertem und nichtverschwindendem Quotienten. Die geprüfte Modellklasse lautet
$$
f(x)=\sum_{\ell=1}^r\frac{a_\ell}{x+t_\ell},\qquad
t_\ell=m_\ell^2>0,\quad a_\ell\ne0.
$$
Die Massenquadrate seien paarweise verschieden und die $a_\ell$ reell. Beiträge mit identischer Masse werden vorher addiert. Wenn sich dabei das Gesamtgewicht aufhebt, ist diese Masse im betrachteten J–D-Kanal unsichtbar. Die Summe enthält keinen zusätzlichen lokalen Kontaktterm. Modi an einer tatsächlichen Nullstelle von $f$ können aus dem gewählten inversen Kreuzquotienten nicht eingesetzt werden. Ein unabhängig rekonstruierter D-Kanal könnte die direkte Antwort dort liefern.

Wähle zwei disjunkte Gruppen $x_i$ und $y_j$, die innerhalb ihrer Gruppen jeweils verschieden sind. Bilde zwei Matrizen der dividierten Differenzen:
$$
(L_0)_{ij}=\frac{f(x_i)-f(y_j)}{y_j-x_i},\qquad
(L_1)_{ij}=\frac{y_j f(y_j)-x_i f(x_i)}{y_j-x_i}.
$$
Die Konstruktion ist eine Vorzeichenkonvention des Loewner- und verschobenen Loewner-Verfahrens für rationale Funktionen. [Mayo und Antoulas, verallgemeinerte Realisierung](https://doi.org/10.1016/j.laa.2007.03.008)

Setze $X_{i\ell}=(x_i+t_\ell)^{-1}$ und $Y_{j\ell}=(y_j+t_\ell)^{-1}$. Direktes Subtrahieren der einzelnen Brüche liefert
$$
L_0=X\,\operatorname{diag}(a_\ell)\,Y^{\mathsf T},\qquad
L_1=X\,\operatorname{diag}(a_\ell t_\ell)\,Y^{\mathsf T}.
$$
Sind pro Gruppe mindestens $r$ Knoten vorhanden, haben $X$ und $Y$ vollen Spaltenrang. Eine verschwindende Linearkombination ihrer Spalten wäre eine rationale Funktion mit gemeinsamem Nenner $\prod_\ell(x+t_\ell)$ und Zählergrad höchstens $r-1$. Aus mindestens $r$ verschiedenen Nullstellen folgt der identisch verschwindende Zähler, danach das Verschwinden aller Residuen. Wegen der nichtverschwindenden $a_\ell$ ergibt das $\operatorname{rang}(L_0)=r$, unabhängig von deren Vorzeichen.

Für quadratische Blöcke mit genau $r$ Knoten je Gruppe ist $L_0$ invertierbar und
$$
L_1L_0^{-1}=X\,\operatorname{diag}(t_\ell)\,X^{-1}.
$$
Die Eigenwerte sind also die Massenquadrate. Die Gewichte ergeben sich anschließend aus einem linearen Cauchy-System mit den gefundenen $t_\ell$. Bei bekannter Zahl $r$ genügen dafür bereits $2r$ exakte verschiedene Stützstellen, sofern sie in zwei geeignete Gruppen fallen. Bei unbekanntem $r$ zählt der Rang nur dann vollständig, wenn beide Gruppen mindestens so viele Knoten wie tatsächlich sichtbare Pole enthalten. Ein voller Rang bei zu wenigen Knoten kann nur eine Untergrenze liefern. Zusätzliche Stützstellen dienen zur Prüfung der rationalen Form.

## Gegenprobe mit entgegengesetzten Gewichten

Setze $f(x)=3/(x+4)-1/(x+9)$ und verwende $x_i\in\{1,4\}$, $y_j\in\{9,16\}$. Aus den vier Werten $(0{,}5,0{,}2980769231,0{,}1752136752,0{,}11)$ ergeben sich Rang zwei und die Eigenwerte $4{,}0000000000004$ und $8{,}99999999999998$. Das nachfolgende lineare System liefert die Gewichte $3$ und $-1$ bis auf Rundung. Bei $x=25$ ergibt das Modell $f(25)\simeq0{,}0740365$ als nicht zur Rekonstruktion benutzten Kontrollwert. In derselben Gegenprobe nimmt die Sekantensteigung von $1/f$ zwischen $x=1,4,9$ zu, während der vorige Gleichzeichenvergleich eine Abnahme vorhersagt. Die Rekonstruktion arbeitet hier trotzdem.

## Grenzen bei endlicher Genauigkeit

Bezeichne mit $\epsilon(x_i)$ und $\epsilon(y_j)$ obere absolute Fehlergrenzen der bereinigten Antwortwerte. Dann gilt
$$
|(\delta L_0)_{ij}|
\le\frac{\epsilon(x_i)+\epsilon(y_j)}{|y_j-x_i|}.
$$
Deren quadratische Summe über alle Einträge liefert über die Frobeniusnorm eine obere Grenze $\mathcal E$ für die Operatornorm von $\delta L_0$. Singulärwerte des gemessenen $L_0$, die sicher über $\mathcal E$ liegen, geben eine untere Grenze für den wahren Rang. Ein kleiner Singulärwert beweist dagegen keine kleine Zahl von Polen. Schwach gekoppelte oder nahe beieinanderliegende Massen können schlecht auflösbar sein. Die Fehlergrenzen müssen Unsicherheiten der Tracerbereinigung und der Umrechnung des Kreuzquotienten berücksichtigen.

Ein zusätzlicher konstanter Kontaktbeitrag zu $f$ fällt aus $L_0$ heraus, verschiebt aber jeden Eintrag von $L_1$ um diese Konstante. Der hier angegebene Eigenwertschritt setzt daher voraus, dass ein solcher Beitrag abwesend oder zuvor bestimmt und abgezogen ist. Die endliche Rekonstruktion unterscheidet unter ihren Annahmen sichtbare Polmassen mit beliebigen Vorzeichen. Reale Spektren, systematische Fehlergrenzen, der J-Mittelwert und H96 bleiben offen.
