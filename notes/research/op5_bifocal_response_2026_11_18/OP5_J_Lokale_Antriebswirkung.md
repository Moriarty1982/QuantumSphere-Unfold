# OP5 — Lokale Antriebswirkung und Metrikquelle

20. November 2026. Analytische Erkundung im Materieframe M. Geprüft wird eine konstruierte quadratische Wirkung im festen flachen Vergleich und ihre lineare Kopplung an eine vorgegebene Metrikstörung. Der Richtungsträger bleibt vorgegeben.

## Vorwissen geprüft

Die [Antriebsrichtungen](OP5_J_Antriebsrichtungen.md) bestimmen die gerichtete skalare Eigenverformung. Der [elastische Abgleich](OP5_J_Elastischer_Quellenabgleich.md) gibt die nötige Cauchy-Spannung. Die [zweifache Außenfeldkompensation](OP5_J_Zweifache_Aussenfeldkompensation.md) verlangt dafür den vollständigen Quellenbeitrag. Der [metrische Abgleich](OP5_J_Metrischer_Abgleich.md) unterscheidet zusätzliche Krümmungsoperatoren von minimaler Gravitation. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt der Aufbau vor der realen OP5-Messabbildung. Rückwärts werden zuerst Bewegung und lineare Quellenvariation verlangt. Eine für I3 nötige Populationsdynamik folgt daraus nicht.

## Eine Wirkung für die gerichtete Bewegung

Setze $P=\operatorname{diag}(1,1,0)$, $\rho_0>0$, $v=u+P\nabla h/\rho_0$ und $\varepsilon(v)=\operatorname{sym}\nabla v$. Im naheliegenden elastischen Ansatz mit dem vollständigen Quadrat der Eigenverformung enthält die Lagrangedichte einen Term
$$
-\tfrac12(P:\mathsf C^{-1}P)(\ddot h)^2,\qquad
P:\mathsf C^{-1}P=\frac{\lambda+2\mu}{\mu(2\mu+3\lambda)}>0 .
$$
Für die betrachteten positiven elastischen Moduli ist die skalare Wirkung in der höchsten Zeitableitung nicht entartet. Wenn $h$ dynamisch ist, hat dieser Ansatz eine skalare Gleichung vierter zeitlicher Ordnung. Er ist damit keine unmittelbare Konstruktion eines zweiten gewöhnlichen stabilen Oszillators.

Eine andere lokale Wahl mit nur ersten Zeitableitungen im Wirkungsintegranden ist
$$
\mathcal L_0=\tfrac12\rho_0|\dot v|^2
-\tfrac12\varepsilon(v):\mathsf C\varepsilon(v)
+\tfrac Z2(\dot h^2-c_h^2|\nabla h|^2-\Omega_h^2h^2)+J h .
$$
Hier $Z,c_h^2,\Omega_h^2>0$ und $J$ eine vorgegebene Ansteuerung. Die Änderung $(u,h)\leftrightarrow(v,h)$ ist lokal invertierbar. Bei $J=0$ sind in den Variablen $v,h$ beide linearen Gleichungen entkoppelt, und die quadratische Energie ist bei positiver elastischer Steifigkeit nichtnegativ. Die räumliche Ableitung von $\dot h$ in den ursprünglichen Variablen führt durch diese Umparametrisierung zu keiner zusätzlichen Anfangsbedingung in der Zeit.

Die $u$-Gleichung ist genau
$$
\rho_0\ddot u=\operatorname{div}\!\left[\mathsf C\varepsilon(v)-P\ddot h\right].
$$
Das ist die gewünschte Gleichung mit der bisherigen effektiven Cauchy-Spannung. Die kompakte Zielbewegung $u=-P\nabla h/\rho_0$ bedeutet $v=0$. Für einen vorgeschriebenen Verlauf ist $J=Z(\partial_t^2-c_h^2\Delta+\Omega_h^2)h$. Ohne $J$ und mit verschwindenden Anfangsdaten bleibt $h=0$. Ein nichttriviales kompaktes ruhendes Endprofil braucht im gewählten skalaren Modell auch auf dem Plateau eine Quelle. Die Quadratform legt weder eine native Ansteuerung noch einen eigenen dynamischen Richtungsträger fest.

## Die Metrikvariation erfordert eine eigene Kopplung

Der kanonische Impuls zu $u$ in $\mathcal L_0$ ist $\rho_0\dot v$. Er unterscheidet sich von $\rho_0\dot u$ um $P\nabla\dot h$. Die Gleichheit der elastischen Bewegungsgleichung genügt daher nicht, um den gravitativen Energie-Impuls-Tensor zu bestimmen.

Für eine vorgegebene Metrikstörung $\gamma_{\mu\nu}$ lässt sich der gewünschte lineare Zusatz als Variation des Krümmungsterms
$$
\mathcal L_\gamma=-hP^{ij}R^{(1)}_{0i0j}[\gamma]
$$
erzeugen. Die Vorzeichenkonvention ist
$$
R^{(1)}_{0i0j}
=\tfrac12(\partial_t\partial_i\gamma_{0j}+
\partial_t\partial_j\gamma_{0i}-\partial_i\partial_j\gamma_{00}
-\partial_t^2\gamma_{ij}).
$$
Nach partieller Integration lautet die Kopplung $\tfrac12\gamma_{\mu\nu}\delta T^{\mu\nu}$ mit
$$
\delta T^{00}=P^{ij}\partial_i\partial_j h,\quad
\delta T^{0i}=-P^{ij}\partial_t\partial_j h,\quad
\delta T^{ij}=P^{ij}\partial_t^2h .
$$
Dieser Zusatz ist identisch erhalten und stimmt mit dem Zielbeitrag aus $B=hP$ überein. Die beiden gemischten Komponenten werden bei Variation der symmetrischen Metrik jeweils einmal gezählt. Für einen kovarianten Vergleich wäre $-h\,U^\mu U^\rho P^{\nu\sigma}R_{\mu\nu\rho\sigma}$ ein möglicher Operator, mit materialgebundenem Zeitvektor $U$ und $P^{\nu\sigma}=g^{\nu\sigma}+U^\nu U^\sigma-N^\nu N^\sigma$ für eine normierte, zu $U$ orthogonale Raumachse $N$. Eine Wirkung für $U,N$ ist hier unbestimmt.

Damit liegt ein Kopplungsterm vor, der genau den geforderten linearen Zusatz zur gewöhnlichen Metrikquelle liefert. Wird die Metrik dynamisch, mischt der neue Term die Gleichungen von $h$ und Gravitation. Die positive Energie von $\mathcal L_0$ im flachen Vergleich beweist für dieses gekoppelte System keine Stabilität. Der Term leitet auch keine gleichartige Kopplung an den separaten massiven Vermittler her. Für den vollständigen OP5-Abgleich müssen die beiden Kopplungen und die Beiträge von $J$ und Richtungsträger festgelegt werden.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_lokale_antriebswirkung.wl) prüft die höchste Zeitableitung des direkten Ansatzes, die elastische Gleichung, die Determinante der vervollständigten kinetischen Form und den linearen Metrikquellterm. Diese Variation ist eine klassische Rechnung ohne Quantenschaltung.

~~~text
Higher-time-derivative coefficient: -((lam + 2*mu)/(3*lam*mu + 2*mu^2))
Elastic equation residual: {0, 0, 0}
Completed kinetic determinant: rho^3*zz
Canonical momentum minus material momentum: {Derivative[1, 1, 0, 0][h][t, x, y, z], Derivative[1, 0, 1, 0][h][t, x, y, z], 0}
Metric variation residual (00, 0x, 0y, xx, yy): {0, 0, 0, 0, 0}
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Richtungsträger, massive Quellenkopplung, Stabilität bei dynamischer Gravitation, reale Apparatur und H96 bleiben offen.
