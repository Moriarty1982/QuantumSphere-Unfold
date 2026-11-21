# OP5 – Rücklauftoleranzen bei massiver J-Dispersion

21. November 2026. Analytische Erkundung im Materieframe M. Im homogenen Zweikanalmarker wird eine freie massive J-Dispersion als Modellannahme eingesetzt. Gesucht sind gemeinsame Toleranzen für Dicke, A-Index und A-Verlust, die aus dem Quotientenbudget folgen.

## Vorwissen geprüft

Die [phasenaufgelöste Reflexionsrechnung](OP5_J_Rueckstreuung_Band.md) liefert drei zentrale Nullintegrale, die Abschätzung der zweiten Iteration und die Bandgrenze im verlustfreien proportionalen Beispiel. Der [endliche Markerhub](OP5_J_Endlicher_Markerhub.md) behandelt den skalaren A-Hub exakt. Der [Feldreferenzvergleich](OP5_J_Feldreferenz.md) liefert das illustrative Quotientenbudget. Die Erkundung betrifft im [Gesamtbild](../../../wiki/Gesamtbild.md) die lokale Auslese. I3 würde eine eigenständige kosmologische Bestandsdynamik erfordern.

## Rückwärtsbedingung und massive J-Phase

Reserviere die Hälfte des illustrativen Quotientenbudgets $\epsilon=9{,}81742885\cdot10^{-6}$ für den einfachen instrumentellen Rücklauf. Für $\|T\|\le 1$ und $\|F_{\rm rück}\|\le1$ genügt dann
$$
\|R\|\le \frac{\epsilon/2}{1+\epsilon/2}=4{,}9086903\cdot10^{-6}.
$$
Mit $e=(E-E_0)/E_0$, $L=L_0(1+\ell)$ und $E_0=0{,}360329$ eV seien $A=k_A L$, $J=k_J L$, $U=\kappa L$. Die Sollwerte am Bandzentrum sind $(A_0,J_0,U_0)=(10000,9999,10001)\pi$. Für den masselosen freien A-Kanal ist $A=A_0(1+e)(1+\ell)$. Für einen massiven freien J-Kanal setze
$$
\mu^2=1-(J_0/A_0)^2,\qquad
J=J_0(1+\ell)\sqrt{\frac{(1+e)^2-\mu^2}{1-\mu^2}} .
$$
Die so gewählte Ruheenergie $\mu E_0=0{,}00509569419$ eV ist ein Modellparameter. Bei Sollschicht und Bandmitte bleiben $2J$, $J+U$ und $J-U$ exakt ganzzahlige, von null verschiedene Vielfache von $2\pi$. Im 100-MHz-Band wächst bei Solldicke die maximale J-Phasenabweichung von $0{,}0180269753$ auf $0{,}0180305813$ rad. Der Anstieg der lokalen Steigung beträgt $0{,}020003\,\%$. Für $\delta_J=\sup|J-J_0|$ genügen wegen Monotonie die Eckwerte bei größter Energie und Dicke sowie kleinster Energie und Dicke.

## Gleichmäßige Abschätzung mit Verlusten

Schreibe $n=\kappa/k_A=n_0+\Delta n+i\nu$ mit $n_0=1{,}0001$, $\nu\ge0$. Es gelten $|e|\le u$, $|\ell|\le t$, $|\Delta n|\le d_n$, $\nu\le v$. Die Indexgrenzen gelten punktweise im gesamten Band und setzen kein bestimmtes Dispersionsgesetz für $\Delta n$ voraus. Mit $A_{\max}=A_0(1+u)(1+t)$ folgen
$$
|\Re U-U_0|\le U_0(u+t+ut)+A_{\max}d_n,\qquad \Im U\le A_{\max}v.
$$
Die quadratische Zusammenfassung der beiden Grenzen liefert $\delta\ge\sup|U-U_0|$. Für $r=(n-1)/(n+1)$ und $s=L|g||q_A|^2=A|n^2-1|$ kann man
$$
\rho=\frac{\sqrt{(n_0-1+d_n)^2+v^2}}{n_0+1-d_n},\qquad
s_{\max}=A_{\max}\sqrt{(n_0-1+d_n)^2+v^2}\sqrt{(n_0+1+d_n)^2+v^2}
$$
als Obergrenzen einsetzen. $k_A/|\kappa|\le 1/(n_0-d_n)$. Auf jeder Strecke in der oberen Halbebene ist $|\exp(iz)-\exp(iw)|\le |z-w|$, weil der Betrag der Ableitung höchstens eins ist. Damit ist die skalare Referenzreflexion durch $2\rho\delta/(1-\rho^2)$ beschränkt.

Für $I$ aus der Vorarbeit folgen die drei dimensionslosen Obergrenzen
$$
\begin{aligned}
|I(2k_J)|/L &\le \delta_J/(J_0-\delta_J),\\
|I(k_J+\kappa)|/L &\le (\delta_J+\delta)/(J_0+U_0-\delta_J-\delta),\\
|e^{2iU}I(k_J-\kappa)|/L &\le (\delta_J+\delta)/(U_0-J_0-\delta_J-\delta).
\end{aligned}
$$
Hier müssen alle drei Nenner positiv sein. In der letzten Zeile ist der Zähler die Differenz der Exponentialwerte bei $J+U+2\pi$ und $2U$. Beide Argumente bleiben in der oberen Halbebene. Mit diesen Grenzen $B_{JJ}, B_+, B_-$ und $x=|q_J/q_A|\le10^{-3}$ ist
$$
\|R^{(1)}\|\le \tfrac12 s_{\max}\,[x^2 B_{JJ}+x(B_++\rho B_-)/(1-\rho)] .
$$

Auch die Phasenabschätzung der zweiten Iteration gilt für $\Im U\ge 0$. Auf jedem Dreieck des Ortsintegrals zerfällt die Phase in $(\alpha+\beta)z_{\min}$ und $(\alpha+\sigma)$ oder $(\beta+\sigma)$ mal Ortsdifferenz. Alle diese Frequenzen haben nichtnegative Imaginärteile. Das Integral im kleineren Ortsparameter bleibt durch $2/|\alpha+\beta|$ beschränkt, und der Differenzfaktor hat Betrag höchstens eins. Im dimensionslosen Ausdruck der Vorarbeit genügt deshalb das Minimum von $J_0-\delta_J$ und $U_0-\delta$ als Wellenzahluntergrenze. Die Bildkernphasen und Gegenwellen enthalten jeweils nichtnegative Weglängen und bleiben im Betrag höchstens eins. Mit $f\le1/(1-\rho)$, $b\le\rho/(1-\rho)$ und $F_0\le(1+\rho)/(1-\rho)$ gelten die übrigen Abschätzungen weiter. Die obere Grenze für $L\|E_{\rm Feld}\|$ ist $s_{\max}(x^2+\sqrt{x^4+4x^2})/2$.

## Zahlen und Kalibrierung

Wähle gleichzeitig $t=d_n=v=2{,}5\cdot10^{-7}$. Das entspricht einer Dickentoleranz von etwa $\pm4{,}30$ nm bei $L_0\simeq17{,}2043$ mm. Die Grenzen für $\Re U-U_0$, $\Im U$ und $J-J_0$ betragen rund $0{,}03374$, $0{,}007854$ und $0{,}02588$ rad. Es gilt $\theta<0{,}003152$ für die Neumann-Reihe.

| Beitrag zur Obergrenze von $\|R\|$ | Obergrenze, aufgerundet |
| --- | ---: |
| Skalare A-Referenz | $3{,}473\cdot10^{-6}$ |
| Erste Iteration | $4{,}573\cdot10^{-9}$ |
| Zweite Iteration | $2{,}624\cdot10^{-9}$ |
| Ab der dritten Iteration | $3{,}140\cdot10^{-8}$ |
| Gesamt | $3{,}512\cdot10^{-6}$ |

Im einfachen Rücklaufmodell bleibt der Transmissionsrest damit unter $3{,}513\cdot10^{-6}$. Bei gleicher Toleranz für alle drei Größen steigt die berechnete Reflexionsobergrenze bei $4{,}4\cdot10^{-7}$ auf $4{,}834\cdot10^{-6}$. Bei $4{,}6\cdot10^{-7}$ liegt die Obergrenze mit $4{,}974\cdot10^{-6}$ über dem reservierten Schwellenwert. Dieser Vergleich bestimmt die Reichweite der gewählten Abschätzung.

Die skalare Transmission erfüllt $t_A=e^{i(U-A)}(1-r^2)/(1-r^2 e^{2iU})$. Ihr Unterschied zum reinen Ausbreitungsfaktor ist im Betrag höchstens $2\rho^2/(1-\rho^2)$. In der ausgewerteten Toleranzbox ist der Amplitudenverlust des Ausbreitungsfaktors durch $1-e^{-A_{\max}v} < 0{,}7824\,\%$ begrenzt, und der Phasendrift des Ausbreitungsfaktors relativ zu $\pi$ ist auf $0{,}007857$ rad begrenzt. Für letzteren folgt die Grenze direkt aus $U-A=A[(n_0-1)+\Delta n+i\nu]$. Die Transmissionskalibrierung braucht somit eine eigene komplexe Referenz. Die geometrische HCl/H-Anschlussschranke ist separat offen, ebenso die freie J-Ausbreitung, die realen Materialdaten, die native Kopplung und H96.

## Rechenkontrolle

[Wolfram-Skript](op5_j_ruecklauf_toleranzen.wl) · [Tatsächliche Ausgabe](op5_j_ruecklauf_toleranzen.txt) · [Laufmanifest](op5_j_ruecklauf_toleranzen.json)

Wolfram liefert fünf exakte Nullreste für die Sollphasen und die drei Integrale. Die Toleranzwerte stammen aus den stetigen analytischen Schranken. Reproduzierbar mit **wolframscript -file op5_j_ruecklauf_toleranzen.wl**.
