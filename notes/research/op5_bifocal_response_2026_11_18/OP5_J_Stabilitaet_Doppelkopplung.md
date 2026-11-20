# OP5 — Lineare Stabilität der doppelten Vermittlerkopplung

20. November 2026. Analytische Erkundung im Materieframe M. Geprüft werden ein Skalar, linearisierte Einstein-Gravitation und ein gesondertes freies Fierz–Pauli-Feld um flachen Raum. Die Strahlrichtung wird als fester Hintergrund behandelt. Beide Vermittler koppeln im Vergleich an dieselbe erhaltene Verbesserung des Quelltensors. Die zweite Kopplung wird ausdrücklich gesetzt.

## Vorwissen geprüft

Die [lokale Antriebswirkung](OP5_J_Lokale_Antriebswirkung.md) erzeugt im flachen elastischen Vergleich positive Energie und gibt den linearen Metrikquellterm an. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) gibt den massiven Propagator an erhaltener Quelle. Die [zweifache Außenfeldkompensation](OP5_J_Zweifache_Aussenfeldkompensation.md) verwendet gleiche Quellenform für die beiden linearen Kanäle. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört die Rechnung zur lokalen Messkette vor H96. Rückwärts wird zuerst ein positives gekoppeltes Spektrum verlangt. Eine Population und ihre Ansteuerung folgen daraus nicht.

## Kontraktion der identisch erhaltenen Quelle

Verwende Fourierkonvention $e^{-i\omega t+i\mathbf k\cdot\mathbf x}$, $P=\operatorname{diag}(1,1,0)$, $x=\omega^2$, $a=|P\mathbf k|^2$ und $k^2=|\mathbf k|^2$. Pro Einheit des Skalarfelds $h$ hat dessen linearer Quellterm die Komponenten
$$
T^{00}/h=-a,\qquad
T^{0i}/h=-\omega(P\mathbf k)_i,\qquad
T^{ij}/h=-xP^{ij}.
$$
Daraus folgt $q_\mu T^{\mu\nu}=0$ mit $q_\mu=(-\omega,\mathbf k)$. Der Spuranteil pro Einheit $h$ ist $a-2x$, die normierte Zweifachkontraktion $a^2-2ax+2x^2$. Die Zähler der masselosen und massiven Kontraktion mit einer erhaltenen Quelle unterscheiden sich durch die Spurkoeffizienten $1/2$ und $1/3$. [Hinterbichler, lineare masselose und Fierz–Pauli-Propagatoren](https://arxiv.org/abs/1105.3735)
$$
N_0=\frac{a^2}{2},\qquad N_m=\frac23(x^2-ax+a^2).
$$
Im masselosen Zähler verschwinden alle expliziten $\omega$-Terme. Für den massiven Pol setze $M=k^2+m^2$. Die Polteilung ergibt
$$
\frac{N_m}{M-x}=\frac23\left[-x+a-M+\frac{M^2-aM+a^2}{M-x}\right].
$$
Das Polgewicht $M^2-aM+a^2=(M-a/2)^2+3a^2/4$ ist strikt positiv. Der affine Term enthält eine lokale Korrektur an der Skalarkinetik.

## Positive Energie im reduzierten quadratischen Modell

Die freien elastischen Moden in der Variablen $v$ bleiben in der gewählten Vergleichswirkung entkoppelt. Setze $\Omega_k^2=\Omega_h^2+c_h^2k^2$ und bezeichne die Kopplungen in kanonischer Normierung mit $g_0,g_m$. Die Normierung wird so gewählt, dass die Beiträge nach Eliminierung der Vermittler $g_0^2N_0/(k^2-x)$ und $g_m^2N_m/(M-x)$ betragen. Der inverse Skalaroperator ist damit
$$
\mathcal K(x)=Z(x-\Omega_k^2)+\frac{g_0^2N_0}{k^2-x}
                         +\frac{g_m^2N_m}{M-x}.
$$
Durch die Polteilung entspricht dieser Operator dem Schur-Komplement einer reellen quadratischen Oszillatorform. Ihre kinetische Matrix lautet $\mathrm{diag}(Z-2g_m^2/3,1,1)$. Die beiden Vermittler haben Diagonaleinträge $k^2,M$ in der Potentialmatrix. Die Kopplungen an den Skalar haben Betragsquadrate $g_0^2a^2/2$ und $2g_m^2(M^2-aM+a^2)/3$. Entkoppelte Polarisationen der freien Vermittler werden dadurch nicht verändert.

Für $k>0$ sind beide Matrizen genau unter folgenden strikten Bedingungen positiv definit
$$
Z>\frac{2g_m^2}{3},
\qquad
Z\Omega_k^2 > \frac{g_0^2a^2}{2k^2}+\frac{2g_m^2a^2}{3M}.
$$
Die zweite Bedingung ist $-\mathcal K(0)>0$, das statische Schur-Komplement. Bei beiden Bedingungen liegen die gekoppelten Eigenwerte $x$ strikt positiv, da sie die verallgemeinerten Eigenwerte zweier positiv definiter symmetrischer Matrizen sind. Bei $k=0$ entkoppelt der masselose Beitrag und sein freier Nullmodus ist nicht Teil des strikten Tests. Ist $\Omega_h^2>0$, genügt gleichmäßig in $\mathbf k$ neben der kinetischen Grenze
$$
Zc_h^2\ge g_0^2/2+2g_m^2/3,
$$
weil $a\le k^2$ und $M> k^2$ gelten. Dies zeigt einen nichtleeren Bereich mit beiden Kopplungen im reduzierten Modell. Die Bedingung behauptet keine Kausalitätsgrenze, keine Stabilität jenseits der quadratischen Näherung und keine Dynamik des Richtungsträgers.

Dieser Vergleich erlaubt dem massiven Vermittler dieselbe Quellenform. Daraus folgen weder ihre native Kopplung noch der nötige kontrollierte Verlauf von $h$. Die sichtbare Kopplungsdifferenz, Rückwirkung eines realen Antriebs und die Kompensation in einer dynamischen materiellen Umgebung müssen getrennt bestimmt werden.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_stabilitaet_doppelkopplung.wl) kontrolliert die Quellenerhaltung, beide Zähler, die Polteilung und die Oszillatordarstellung. Es verwendet klassische Tensor- und Matrixalgebra.

~~~text
Conserved source residual: {0, 0, 0, 0}
Massless numerator residual: 0
Massive numerator residual: 0
Massive pole division residual: 0
Oscillator representation residual: 0
Static scalar Schur complement: (a^2*g0^2)/(2*kk) + (2*a^2*gm^2)/(3*mm) - om*z0
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Dynamik, Apparatur und H96 bleiben offen.
