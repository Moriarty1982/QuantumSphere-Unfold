# OP5 — Luminaler Einstein-Kanal und gerichteter massiver Kontrast

20. November 2026. Analytische Erkundung im Materieframe M. Das Einstein-Feld bleibt im linearen Vergleich unmodifiziert in seinem freien Hauptteil. Seine Ankopplung wird geändert. Für den gerichteten massiven Austausch verwenden wir weiterhin nur den reduzierten langsameren Vergleich.

## Vorwissen geprüft

Die [metrische Kegelgrenze](OP5_J_Metrische_Kegelgrenze.md) verlangt verschwindende Hauptmischung für einen bereits luminalen Vermittler. Der [metrische Abgleich](OP5_J_Metrischer_Abgleich.md) behandelt Ricci-Kopplungen und Feldumdefinitionen. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) gibt die Kontraktion des massiven Zählers mit einer erhaltenen Quelle. Die [Ansteuerung mit Rückwirkung](OP5_J_Rueckwirkung_und_Charakteristiken.md) liefert den polynomialen kompakten Antrieb. Rückwärts wird eine Einstein-Quelle verlangt, die keine transversale Strahlungsmode mischt. Danach wird geprüft, ob dieselbe Quellenform den massiven Kontrast tragen kann. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt das weiterhin vor der OP5-Messabbildung und H96. Für I3 folgt keine Populationsdynamik.

## Konforme Verbesserung am Einstein-Kanal

Mit $p^\mu=(\omega,\mathbf k)$, $d=p_\mu p^\mu=q-x$, $q=|\mathbf k|^2$ und $x=\omega^2$ setze pro Einheit des Skalars $h$
$$
S^{\mu\nu}=p^\mu p^\nu-\eta^{\mu\nu}d.
$$
Dies ist die identisch erhaltene lineare Quellenform einer skalaren Kopplung an die Ricci-Skalare, bis auf Normierung und Vorzeichen. Es gilt $p_\mu S^{\mu\nu}=0$, $\operatorname{tr}S=-3d$ und $S:S=3d^2$. Damit wird die Einstein-Kontraktion
$$
\frac{S:S-(\operatorname{tr}S)^2/2}{d}=-\frac32d
$$
zu einem lokalen Skalarterm. Der freie gravitativ transversale Pol wird nicht gemischt. Konkret ist der spurgespiegelte Zähler $p^\mu p^\nu+\eta^{\mu\nu}d/2$. Nach Division durch $d$ ergibt er einen reinen linearen Eichterm und eine lokale konforme Metrikstörung proportional zu $\eta^{\mu\nu}h$. Die lineare Krümmung ist bei kompaktem $h$ ebenfalls kompakt. Eine reine Konformänderung erhält die unparametrisierte Nullbahn. Für einen erhaltenen spurlosen Teststrahl fällt auch die direkte Kontraktion mit dem konformen Feld weg. Die Apparatursensitivität gegenüber anderen Quellen wird hier nicht bestimmt.

Die gleiche Verbesserung hat im unmodifizierten Fierz–Pauli-Zähler $S:S-(\operatorname{tr}S)^2/3=0$. Allgemeiner ergibt der massive Zähler auf dieser Quelle $(1+d/m^2)p^\mu p^\nu$, bevor durch $d+m^2$ geteilt wird. Der verbleibende Beitrag ist rein longitudinal und koppelt nicht an einen erhaltenen zweiten Tensor. Diese gemeinsame konforme Quellenform liefert daher in diesem Vergleich keinen massiven OP5-Laufzeitkontrast. Der konstruktive folgende Schritt benutzt zwei verschiedene erhaltene Quellenformen.

## Gerichtete massive Quelle und positive Geschwindigkeitsgrenzen

Am massiven Vergleichsfeld bleibe die gerichtete frühere Quelle mit $P=\mathrm{diag}(1,1,0)$ erhalten. Setze $a=|P\mathbf k|^2$, $N_m=2(x^2-ax+a^2)/3$ und $d_m=r_m q+m^2-x$ mit $0<r_m<1$. Quellzähler und verlangsamter Nenner sind weiterhin gesetzte Daten des reduzierten Oszillatormodells. Mit kanonischen Kopplungen $g_0,g_m$ gilt
$$
\mathcal K=Z(x-\Omega_k^2)-3g_0^2 d/2+g_m^2N_m/d_m .
$$
Die Einstein-Strahlungsmoden liegen frei auf der metrischen Geschwindigkeit. Im übrigen gekoppelten Hauptblock sind bei $\alpha=a/q$ der kinetische Skalareintrag $A$, die durch $q$ geteilte statische Diagonale $b$ und die Hauptkopplung $j_m$ gegeben durch
$$
A=Z+3g_0^2/2-2g_m^2/3,\quad
b=Zc_h^2+3g_0^2/2+\tfrac23g_m^2(r_m-\alpha),\quad
j_m^2=\tfrac23g_m^2(r_m^2-r_m\alpha+\alpha^2).
$$
Für $A>0$ gilt die Geschwindigkeitsgrenze genau bei $j_m^2/r_m<b\le A-j_m^2/(1-r_m)$.

Wähle $Z=1$, $r_m=c_h^2=1/2$, $g_0^2=g_m^2=3/100$ und positive $\Omega_h^2,m^2$. Die beiden konkaven Richtungsabstände betragen an den Intervallenden $(109/200,101/200)$ und $(23/50,23/50)$. Damit liegen alle übrigen charakteristischen Geschwindigkeiten strikt unter der metrischen. Auch das vollständige statische Schur-Komplement ist für alle $q$ positiv im gekoppelten verbleibenden Block. Der massive Abzug ist höchstens $q/25$, während der statische skalare Beitrag $Z\Omega_k^2+(3g_0^2/2)q$ größer als $q/2$ ist. Diese Prüfung gehört zum gewählten reduzierten Modell.

## Kompakter Achsenkontrast

Für ein glattes räumlich kompaktes $H$ ohne frühere Störung setze $h=d_mH/m^2$. Der polynomielle Antrieb
$$
J=\left([Z(\Omega_k^2-x)+3g_0^2d/2]\,d_m-g_m^2N_m\right)H/m^2
$$
erfüllt $\mathcal K h+J=0$. Die Einstein-Krümmung bleibt aufgrund der lokalen Konformänderung kompakt. Die massive retardierte Faltung liefert das gerichtete Profil aus $H/m^2$. Im bisherigen axialen Vergleich mit dem lokalen Spur- und Ableitungszähler bleibt sein direkter Linienbeitrag $\int\Delta_\perp H\,dz/m^2$. Wähle auf dem Endplateau $H=-A_Hp(z)g(\mathbf b)$ mit $A_H>0$, $p$ positiv im Inneren der Strecke und einem transversalen kompakten Profil $g$, das nahe der Achse mit $e^{-|\mathbf b|^2/R^2}$ übereinstimmt. Dann beträgt der geometrische Kontrast $4A_H\int p(z)dz/(R^2m^2)>0$, bis auf die Kopplungsnorm. Die Spurterme fallen in der Nullkontraktion oder als integrierte Randableitung heraus. Die unveränderte Einstein-Ausbreitung und der kompakte gerichtete Kontrast sind damit im getrennt gekoppelten Vergleich gleichzeitig möglich.

Eine messbare J–A-Differenz braucht weiter verschiedene effektive Kopplungsgewichte an der sichtbaren Auslese. Die geladene Apparatur ist nicht allein durch die spurfrei idealisierten Strahlen beschrieben. Ob beide unterschiedlichen Quellenformen und der langsamere massive Hauptteil aus einer gemeinsamen physischen Wirkung folgen, bleibt offen.

## Wolfram-Ausgabe

Das [Prüfskript](op5_j_luminaler_einstein_kanal.wl) kontrolliert Quellenerhaltung, Kontraktionen, Metrikzähler, Antrieb, Richtungsgrenzen und die Laplace-Wirkung auf der Achse. Es handelt sich um klassische Operator- und Tensoralgebra.

~~~text
Conformal source divergence: {0, 0, 0, 0}
Einstein contact residual: 0
Same-source Fierz-Pauli contraction: 0
Trace-reversed metric residual: {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}}
Compact drive residual: 0
Characteristic lower endpoint margins: {109/200, 101/200}
Characteristic upper endpoint margins: {23/50, 23/50}
Margin curvatures: {-2/25, -2/25}
Axial transverse Laplacian: -4/rad^2
~~~

Der separate Rückgabewert des letzten `Print` war `Out[1]= Null`. Native Kopplung, wirklicher Empfang, Antrieb und H96 bleiben offen.
