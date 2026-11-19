# OP5: Drehimpuls als dynamischer Fokusabstand

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 in einem Materie-Schwerpunktsystem. Die [Fokusabstandsrechnung](W2_Fokusabstand.md) zeigte Anziehung für zwei getrennte ladungskonjugierte Wolken. Die [Fermionprüfung](W2_Z_Gleichgewicht.md) lieferte keine native Stabilisierung des Z-String-Vergleichs. Hier wird ein anderer Zustand geprüft: bewegliche Foki mit Drehimpuls. Es wird kein weiterer String- oder Endzonenterm angesetzt. Die [J-Maxwell-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) und die bereits berechnete [J-Kraft](W2_J_Eichkanal.md) geben die langreichweitige Wechselwirkung vor.

## Kreisbahnen bei festem Drehimpuls

Behandle zwei kompakte Wolken mit starren internen Profilen, entgegengesetzten physisch normierten J-Ladungen $\pm q$ und positiven Trägheitsmassen $M_1,M_2$. Ihre reduzierte Masse ist $m_r=M_1M_2/(M_1+M_2)$. Im nichtrelativistischen Bereich, außerhalb der Überlappung und in retardierungsfreier Näherung, lautet das Paarpotential $V(R)=-A/R-Be^{-m_hR}/R$ mit $A=q^2/(4\pi)>0$ und $B\ge0$. Der Koeffizient des Higgsanteils ist für feste Profile derjenige aus der früheren Fokusrechnung. Das Modell setzt die Existenz der beiden Wolken voraus und untersucht ihre relative Bewegung.

Bei mechanischem Drehimpuls $L$ ist $U_L=L^2/(2m_rR^2)+V(R)$. Setze $x=m_hR$. Eine Kreisbahn liegt bei

$$
L^2=m_rR[A+B(1+x)e^{-x}],\qquad
U_L''(R)=\frac{A+B(1+x-x^2)e^{-x}}{R^3}.
$$

Für hinreichend große Radien ist die Krümmung positiv. Ist sogar $A>5e^{-3}B$, ist jede Kreisbahn in der getrennten Modellklasse radial stabil. Denn der größte Wert von $(x^2-x-1)e^{-x}$ auf $x\ge0$ ist $5e^{-3}$ bei $x=3$. Bei Gleichheit kann die quadratische Radialkrümmung bei $x=3$ verschwinden. Im reinen Coulomb-Grenzfall gilt $R_*=L^2/(m_rA)$, also ein dynamisch ausgewählter Abstand bei vorgegebenem $L$.

## Maxwell-Abstrahlung begrenzt den Zustand

Für die beiden Wolken ist das elektrische J-Dipolmoment $\mathbf d=q\,\mathbf R$. Auf der Kreisbahn rotiert es mit Winkelgeschwindigkeit $\omega$, auch wenn die Gesamtladung null ist. Im Langwellenlimit $\omega R\ll1$ liefert das auslaufende Maxwell-Feld im rationalisierten Einheitensystem mit $c=1$ die Dipolstrahlungsleistung

$$
P_J=\frac{|\ddot{\mathbf d}|^2}{6\pi}
=\frac{q^2 R^2\omega^4}{6\pi}>0 .
$$

Die Formel folgt aus der transversalen Dipol-Leistung pro Raumwinkel und $\int\sin^2\theta\,d\Omega=8\pi/3$. Der [Dipolstrahlungsabschnitt in den Vorlesungsnotizen der University of Oregon](https://pages.uoregon.edu/dbelitz/teaching/2025_26/PHYS_622/lecture_notes/Typeset_Notes/622_3_Lecture_Notes.pdf) verwendet gaußsche Ladungseinheiten; die Umrechnung ist $q_{\rm Gauss}=q/\sqrt{4\pi}$ bei $c=1$. Für den Energieverlust werden auslaufende Randbedingungen ohne externe Energiezufuhr gewählt. Das vollständige System kann seinen Gesamtdrehimpuls einschließlich des Feldes erhalten, während die mechanische Näherung mit konstantem $L$ nur auf kurzen Zeitskalen gilt.

Im Coulomb-Grenzfall sind $\omega^2=A/(m_rR^3)$ und die kreisförmige Bahnenergie $E_{\rm circ}=-A/(2R)$. In adiabatischer Kreisbahnnäherung ergibt $\dot E_{\rm circ}=-P_J$

$$
\dot R=-\frac{4A^2}{3m_r^2R^2},\qquad
t(R_0\to R_f)=\frac{m_r^2}{4A^2}(R_0^3-R_f^3).
$$

Die Formel wird nur bis zu einem $R_f$ benutzt, für das die Wolken getrennt und die Bewegung langsam bleiben. Sie ist keine Aussage über das Kollisionsende. Die lokale Driftskala $R/|\dot R|$ geteilt durch die Umlaufzeit ist $3(m_rR/A)^{3/2}/(8\pi)$. Damit kann der Abstand bei langsamer Bewegung viele Umläufe näherungsweise halten und bleibt dennoch nicht stationär. Für ein ladungskonjugiertes Paar mit $B-L$-Ladungen $\pm X$ rotiert auch $\mathbf d_{B-L}=X\,\mathbf R$. Sein zeitlicher Mittelwert über eine vollständige ideale Kreisbahn ist null.

## Konsequenz für OP5

Drehimpuls erlaubt einen radial stabilen, zeitabhängigen Abstand im konservativen Modell. Die vorhandene masselose J-Kopplung lässt das isolierte klassische Paar auf der langsam driftenden Bahn Energie verlieren. Ein dauerhafter räumlich orientierter Randdipol ist damit nicht hergeleitet. Die Rechnung prüft weder eine quantenmechanisch gebundene Zustandslösung noch die interne Stabilität der Wolken. Native Randwirkung und H96 bleiben offen. Die Lesart I3 setzt weiter eine eigenständige Überschussdynamik voraus.
