# OP5 — Bedingungen für die metrische Geschwindigkeitsgrenze

20. November 2026. Analytische Erkundung im Materieframe M. Die Geschwindigkeiten beziehen sich auf die flache Referenzmetrik mit $c=1$. Die geänderten Vermittler werden als lokaler reduzierter Vergleich eingeführt. Ihre Ausbreitung wird nicht aus der Einstein- oder Fierz–Pauli-Wirkung im D-Sektor hergeleitet.

## Vorwissen geprüft

Die [Charakteristiken mit Rückwirkung](OP5_J_Rueckwirkung_und_Charakteristiken.md) liefern eine übermetrische Mode bei ursprünglicher kinetischer Kopplung. Die [Doppelkopplung](OP5_J_Stabilitaet_Doppelkopplung.md) stellt den linearen Energievergleich als Oszillatorsystem dar. Der [ältere Zweikegelvergleich](../../../analysis/OP5_Operational_Two_Cone_Coupling.md) behandelt algebraische Mischung bei bereits getrennten Kegeln. Rückwärts wird jetzt ein Hauptteil verlangt, dessen positive charakteristische Geschwindigkeiten die Referenzgeschwindigkeit nicht überschreiten. Das betrifft im [Gesamtbild](../../../wiki/Gesamtbild.md) weiterhin die lokale OP5-Messkette vor H96. Der Richtungsträger und die I3-Populationsdynamik bleiben unbestimmt.

## Exakte Bedingung im gekoppelten Block

Sei $A>0$ der kinetische Eintrag des Skalars. Die Vermittler seien kinetisch auf eins normiert. In einer festen räumlichen Richtung seien $r_0,r_m$ die Quadrate der ungemischten charakteristischen Geschwindigkeiten der Vermittler. Der auf $|\mathbf k|^2$ normierte Hauptteil der Potentialmatrix sei
$$
K=\mathrm{diag}(A,1,1),\qquad
V=\begin{pmatrix}
b & j_0 & j_m\\
j_0 & r_0&0\\
j_m&0&r_m
\end{pmatrix}.
$$
Die Quadrate der gekoppelten Geschwindigkeiten sind die Eigenwerte von $K^{-1/2}VK^{-1/2}$. Sie liegen genau dann in $(0,1]$, wenn $V\succ0$ und $K-V\succeq0$. Für $0<r_0,r_m<1$ ist dies äquivalent zu
$$
\frac{j_0^2}{r_0}+\frac{j_m^2}{r_m}
<b\le
A-\frac{j_0^2}{1-r_0}-\frac{j_m^2}{1-r_m}.
$$
Dafür werden die unteren Diagonalblöcke in den beiden Schur-Komplementen eliminiert. Wenn $r_i=1$, muss die entsprechende Hauptkopplung $j_i$ verschwinden. Sonst hat der zugehörige zweidimensionale Hauptminor von $K-V$ die Determinante $-j_i^2<0$. Eine Änderung allein am Skalarwert $b$ kann diese Bedingung bei metrisch luminalem gekoppeltem Vermittler nicht reparieren. Untergeordnete Kopplungen, die im Hauptteil verschwinden, sind dadurch nicht ausgeschlossen.

## Lokaler Vergleich mit zwei langsameren Vermittlern

Ersetze die Nenner der vorigen Rechnung durch $d_0=r_0 q-x$, $d_m=r_m q+m^2-x$ mit $q=|\mathbf k|^2$ und $x=\omega^2$. Die Quellpolynome $N_0=a^2/2$ und $N_m=2(x^2-a x+a^2)/3$ mit $a=|P\mathbf k|^2$ werden hier als Vergleichseingaben beibehalten. Schreibe $\alpha=a/q\in[0,1]$. Die Polteilung liefert
$$
A=Z-\frac{2g_m^2}{3},\quad
b=Zc_h^2+\frac{2g_m^2}{3}(r_m-\alpha),\quad
j_0^2=\frac{g_0^2\alpha^2}{2},\quad
j_m^2=\frac{2g_m^2}{3}(r_m^2-r_m\alpha+\alpha^2).
$$
Eine räumlich lokale Oszillatorform lässt sich unter anderem mit zwei entarteten massiven Vergleichsmoden bilden. Für $M'=r_m q+m^2$ zerfällt das Polgewicht in die Summe der beiden Quadrate
$$
\frac{2g_m^2}{3}(M'^2-aM'+a^2)
=\left[\sqrt{2/3}\,g_m(M'-a/2)\right]^2+
 \left[g_m a/\sqrt2\right]^2.
$$
Die Kopplungen sind dann Polynome in den räumlichen Ableitungen. In jeder Fouriermode koppelt eine massive Linearkombination, die andere bleibt frei. Dies ersetzt nicht den Zwangsgleichungsabgleich eines modifizierten Spin-2-Felds.

Ein expliziter rationaler Vergleich ist $Z=1$, $c_h^2=r_0=r_m=1/2$, $g_0^2=g_m^2=3/100$ und $\Omega_h^2,m^2>0$. Die beiden Abstände zu den Schur-Grenzen sind konkav quadratisch in $\alpha$. Die Mindestwerte liegen daher an den Intervallenden. Beide Abstände betragen dort mindestens $43/100$. Auch die vollständige Potentialmatrix bei endlichem $q>0$ ist positiv. In ihrem statischen Schur-Komplement sind die beiden abzuziehenden Beiträge zusammen höchstens $7q/100$, während $Z\Omega_k^2>q/2$. Damit gibt es im reduzierten Modell gleichzeitig positive Energie und charakteristische Geschwindigkeiten unterhalb der metrischen Geschwindigkeit. Die endliche Phasengeschwindigkeit einer massiven Mode ist eine andere Größe.

## Die kompakte erzwungene Lösung bleibt erhalten

Der skalare Operator lautet wieder $\mathcal K=Z(x-\Omega_k^2)+g_0^2N_0/d_0+g_m^2N_m/d_m$. Für ein glattes räumlich kompaktes $H$ ohne frühere Störung setze $h=d_0d_m H/m^4$ und
$$
J=\big[Z(\Omega_k^2-x)d_0d_m-g_0^2N_0d_m-g_m^2N_md_0\big]H/m^4 .
$$
Der Antrieb bleibt ein lokaler Differentialoperator und erfüllt $\mathcal K h+J=0$. Beide retardierten Feldinversen kürzen je einen Nenner aus. Das hält die beiden Vergleichsantworten kompakt. Eine neue J–A-Laufzeit folgt daraus zunächst nicht, weil die Kopplung der geänderten Vermittler an eine physische Messkette unbestimmt bleibt.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_metrische_kegelgrenze.wl) kontrolliert beide Schur-Komplemente, den Minor für den luminalen Grenzfall, die rationalen Richtungsränder und den kompakten Antrieb. Es handelt sich um klassische Matrix- und Operatoralgebra.

~~~text
Lower Schur residual: 0
Upper Schur residual: 0
Minor for a luminal coupled mediator: -j0^2
Example lower endpoint margins: {1/2, 43/100}
Example upper endpoint margins: {23/50, 43/100}
Example margin curvatures: {-7/50, -7/50}
Compact driven response residual: 0
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Die gewöhnliche metrische Lichtgeschwindigkeit des Einstein-Felds wird im konkreten langsameren Vergleich nicht beibehalten. Ein physischer Modellanschluss mit metrischem Einstein-Feld muss statt dessen seine Hauptkopplung ändern. Richtungsträger, reale Auslese und H96 bleiben offen.
