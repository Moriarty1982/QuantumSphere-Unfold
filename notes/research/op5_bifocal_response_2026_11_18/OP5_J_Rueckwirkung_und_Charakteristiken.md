# OP5 — Kompakte Ansteuerung mit Rückwirkung und charakteristische Geschwindigkeiten

20. November 2026. Analytische Erkundung im Materieframe M. Betrachtet wird das lineare konstante Vergleichsmodell mit vorgeschriebener Strahlrichtung, gleichen Quellenformen für beide Vermittler und verschwindenden früheren Störungen. Die freie elastische Bewegung bleibt in der Variablen $v$ entkoppelt.

## Vorwissen geprüft

Die [zweifache Außenfeldkompensation](OP5_J_Zweifache_Aussenfeldkompensation.md) präpariert die Quelle als Bild beider Wellenoperatoren. Die [Antriebswirkung](OP5_J_Lokale_Antriebswirkung.md) verwendet einen gesteuerten Skalar. Die [Stabilitätsrechnung](OP5_J_Stabilitaet_Doppelkopplung.md) gibt seinen inversen Operator mit Rückwirkung und den positiven Parameterbereich. Der [frühere Zweikegelvergleich](../../../analysis/OP5_Operational_Two_Cone_Coupling.md) trennt charakteristische Geschwindigkeiten von endlichen Gruppen- und Phasengeschwindigkeiten. Dort wird ein algebraischer Austausch verwendet, hier beeinflusst die Ableitungskopplung den Hauptteil. Im [Gesamtbild](../../../wiki/Gesamtbild.md) bleibt beides Bestandteil der lokalen Messabbildung vor H96. Rückwärts werden ein kompakter Zielverlauf und eine mögliche gemeinsame Kegelgrenze geprüft. Es folgt keine Populationsdynamik für I3.

## Kompakte Ansteuerung trotz beider Rückwirkungen

Verwende $x=\omega^2$, $q=|\mathbf k|^2$, $a=|P\mathbf k|^2$, $d=q-x$ und $r=q+m^2-x$. Die Zähler sind $N_0=a^2/2$, $N_m=2(x^2-ax+a^2)/3$ und $\Omega_k^2=\Omega_h^2+c_h^2q$. Mit der Wirkungsquelle $+Jh$ lautet die Skalarbilanz im Fourierbild $\mathcal K h+J=0$, wobei
$$
\mathcal K=Z(x-\Omega_k^2)+g_0^2 N_0/d+g_m^2 N_m/r.
$$
Sei $H(t,\mathbf x)$ glatt, räumlich kompakt und vor der Schaltung null. Mit Fouriermultiplikatoren geschrieben wähle
$$
h=\frac{dr}{m^4}H,\qquad
J=\frac{Z(\Omega_k^2-x)dr-g_0^2N_0r-g_m^2N_md}{m^4}\,H.
$$
Der Ausdruck für $J$ ist ein Polynom in Frequenz und Wellenvektor. Er ist ein lokaler Differentialoperator und erzeugt einen räumlich kompakten Antrieb. Für ruhende, nichttriviale Endprofile im strikt positiven Bereich bleibt die Ansteuerung im Allgemeinen auch auf dem Plateau nötig. Tatsächlich ist $\mathcal K(0)$ für $q>0$ strikt negativ. Unter den retardierten Anfangsbedingungen heben sich die beiden Nenner auf dem präparierten Verlauf auf. Die masselose und massive Feldantwort bleiben kompakt. Das gilt für die Wirkung mit festgesetzter Steuerquelle $J$. Ihr eigener materieller Energie-Impuls-Tensor ist noch zu berücksichtigen.

## Grenze des gemeinsamen metrischen Lichtkegels

Für die homogene Ausbreitung ohne Antrieb betrachte $q\to\infty$ bei fester Richtung. Setze $y=x/q$ und $\alpha=a/q\in[0,1]$. Im gekoppelten Block hat der Hauptteil von $dr\mathcal K$ nach Division durch $q^3$ die Form
$$
(1-y)F_\alpha(y),
\qquad
F_\alpha(y)=Z(y-c_h^2)(1-y)+g_0^2\alpha^2/2+
 \frac{2g_m^2}{3}(y^2-\alpha y+\alpha^2).
$$
Dieser Faktor folgt aus dem Determinantenpolynom der Oszillatordarstellung, sodass die Moden auch am entarteten Hauptpol durch das gemeinsame Polynom definiert sind. Im strikt positiven Bereich ist der höchste Koeffizient von $F_\alpha$ gleich $-(Z-2g_m^2/3)<0$. Am Hintergrundlichtkegel gilt
$$
F_\alpha(1)=g_0^2\alpha^2/2+\frac{2g_m^2}{3}(1-\alpha+\alpha^2).
$$
Ist $g_m\ne0$, ist dieser Wert für jede Richtung positiv. Bei $g_m=0$ und $g_0\ne0$ ist er für $\alpha>0$ positiv. Daher hat das Hauptpolynom in diesen Fällen eine Nullstelle $y_+>1$. Die entsprechende charakteristische Geschwindigkeit $\sqrt{y_+}$ überschreitet die der flachen Hintergrundmetrik. Das Ergebnis hängt nicht davon ab, dass der ungemischte Skalar bereits $c_h>1$ hätte. Es gilt auch bei $c_h\le1$.

Der positive Energiebereich behebt die Kegeldifferenz somit in dieser Fortsetzung des Modells bis zu beliebig großen Wellenzahlen nicht. Die exakt kompakte Lösung gehört zu einem speziell abgestimmten Antrieb und legt den Ausbreitungsbereich allgemeiner Störungen nicht fest. Wenn nur eine effektive Theorie mit endlichem Gültigkeitsbereich gemeint ist, kann aus diesem Grenzwert allein keine Aussage über den Bereich jenseits der Gültigkeitsgrenze abgeleitet werden. Eine physische Metrikzuordnung und die Dynamik des Richtungsträgers sind weiterhin offen.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_rueckwirkung_und_charakteristiken.wl) kontrolliert den Antrieb, die beiden Umkehrungen und die Faktorisierung des Hauptpolynoms. Es handelt sich um klassische Operatoralgebra.

~~~text
Compact drive residual: 0
Massless response residual: 0
Massive response residual: 0
Principal factorization residual: 0
Principal polynomial at metric cone: (alpha^2*g0^2)/2 + (2*gm^2)/3 - (2*alpha*gm^2)/3 + (2*alpha^2*gm^2)/3
Highest coefficient of that polynomial: (2*gm^2)/3 - z0
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Ansteuerung, reale J–A-Differenz und H96 bleiben offen.
