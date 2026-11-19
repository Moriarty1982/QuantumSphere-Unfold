# OP5: Quantenbindung und stationärer Dipol

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im Materie-Schwerpunktsystem. Die [Fokusbahn](W2_Fokusbahn.md) hielt den Abstand im konservativen klassischen Modell zeitweise, verlor jedoch durch das masselose J-Feld Energie. Hier wird das relative Zweikörperproblem aus der [Fokusabstandsrechnung](W2_Fokusabstand.md) quantisiert. Geprüft wird ein Punktquellenvergleich ohne quantisierte Strahlungsmoden.

## Bindung und Parität

Sei $\mathbf R$ die relative Position eines Paars mit entgegengesetzten B−L-Ladungen $\pm X$. Sein Dipolobservable ist $\mathbf D=X\mathbf R$. Für einen zentralen Hamiltonoperator gilt $[H,P]=0$ und $P\mathbf DP^{-1}=-\mathbf D$. Ein stationärer Zustand mit bestimmter Parität hat deshalb exakt $\langle\mathbf D\rangle=0$. Für einen stationären Zustand mit einem Dipol in einer bestimmten Richtung benötigt man im betreffenden Energieeigenraum ein nichtverschwindendes Matrixelement zwischen Zuständen entgegengesetzter Parität. Für stationäre Dichtematrizen folgt dasselbe aus ihrer Blockdiagonalität in den Energien.

Der Coulomb-Grundzustand hat bei $a_0=(m_r A)^{-1}$ den mittleren Abstand $\langle R\rangle=3a_0/2$ und verschwindende Dipolerwartung. Die Rechnung benutzt $\hbar=c=1$.

## Coulomb-Entartung als Gegenprobe

Der ideale Hamiltonoperator $H_0=-\nabla^2/(2m_r)-A/R$ besitzt für $n=2$ einen gemeinsamen Energieeigenraum der $2s$- und $2p$-Zustände. Mit geeigneter Phase gilt $\langle 2s|z|2p,0\rangle=3a_0$. Folglich sind $(|2s\rangle\pm|2p,0\rangle)/\sqrt2$ im exakt entarteten Vergleich stationär und tragen $\langle D_z\rangle=\pm3Xa_0$. Das Matrixelement ist auch aus der [Standardrechnung zum linearen Stark-Effekt](https://ocw.mit.edu/courses/22-51-quantum-theory-of-radiation-interactions-fall-2012/557c789eb1685b35876322b79a3473f0_MIT22_51F12_Ch11.pdf) bekannt. Ein äußeres Feld wird hier nicht eingesetzt. Die Richtung wird bei der Präparation gewählt. Die Lebensdauer unter Kopplung an quantisierte Strahlung bleibt offen.

## Die Higgs-Korrektur trennt die Paritäten

Die zentrale Korrektur $V_1=-B e^{-m_h R}/R$ mit $B>0$ und $m_h>0$ mischt $2s$ und $2p$ aufgrund der Rotationssymmetrie nicht. Für schwaches $B$ liefert die erste Störungsordnung mit $x=m_h a_0$ und $s=1+x$

$$
\begin{aligned}
\langle 2s|e^{-m_h R}/R|2s\rangle
 &=\frac{1}{2a_0}(s^{-2}-2s^{-3}+\tfrac32s^{-4}),\\
\langle 2p|e^{-m_h R}/R|2p\rangle
 &=\frac{1}{4a_0}s^{-4},\\
E_{2p}-E_{2s}
 &=\frac{B}{2a_0}\frac{x^2}{(1+x)^4}+O(B^2).
\end{aligned}
$$

Die Integrale verwenden die normierten Radialfunktionen $R_{20}=(2-r/a_0)e^{-r/(2a_0)}/(2\sqrt2\,a_0^{3/2})$ und $R_{21}=(r/a_0)e^{-r/(2a_0)}/(2\sqrt6\,a_0^{3/2})$. Für jedes feste $x>0$ und hinreichend kleines $B>0$ ist die Aufspaltung positiv. Bei $x=0$ ist die Korrektur erneut rein coulombisch und die Aufspaltung verschwindet. Der Faktor $x^2/(1+x)^4$ nimmt bei $x=1$ den Höchstwert $1/16$ an. Der Befund betrifft nur das betrachtete Coulomb-Dublett.

Ein anfänglich orientierter Zustand aus den beiden fortgesetzten Eigenzuständen entwickelt eine relative Phase $\Delta E\,t$. Sein Dipol ist proportional zu $\cos(\Delta E\,t+\varphi)$ und mittelt sich über einen vollständigen Schwebungszyklus zu null. Eine kleine Aufspaltung kann die Richtung für kurze Zeiten annähernd erhalten. Die ideale stationäre Orientierung ist gegen die abgeschirmte, paritätserhaltende Korrektur nicht geschützt.

Ein gebundener Abstand kann somit auch im Quantenvergleich vorliegen. Für einen stationären Dipol braucht die geprüfte Route eine aus der Wirkung ausgewählte Orientierung oder eine geschützte Entartung entgegengesetzter Paritäten. Eine Auslese am Rand, die innere Dynamik der Fokuswolken und die Überschussdynamik von I3 bleiben offen. Native Randwirkung und H96 bleiben offen.
