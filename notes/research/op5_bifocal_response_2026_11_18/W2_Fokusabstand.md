# OP5: Halten die Feldterme zwei Foki auf Abstand?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem auf flachem Hintergrund. Die [Außenfeldauslese](W2_Fokusprofile.md) setzte zwei bekannte Foki voraus. Hier wird der Abstand variiert. Vorwissen: [J-Eichkraft](W2_J_Eichkanal.md), [radiale Higgsquelle](W2_Higgsquelle.md), [W2-Aufbau](../v4_10_0_r82/Wirkung_W2_Higgs.md), [skalare Sondenenergie](Grenze_W2.md), [direkte Randkopplung](Quellkopplung.md). Photon und Z gehören nur zur vorherigen [elektroschwachen Referenz](W2_Neutralstroeme.md). Die Rechnung enthält weder Gravitation noch eine materielle Grenzfläche.

## Zwei ladungskonjugierte Wolken

Sei $R>2b$ der Abstand zweier Mittelpunkte, mit glatten kugelsymmetrischen Quellen von Radius höchstens $b$. Für jede Dirac-Art haben die Wolken gleiche Teilchen-Antiteilchen-Summen und entgegengesetzte Differenzen. Die Besetzungen seien spinunpolarisiert und ohne mittleren Strom. Beim Verschieben der Foki bleiben die Profile und Besetzungen relativ zu ihrem jeweiligen Mittelpunkt zunächst fest. Dadurch ist jede vektorielle Ladungsquelle an den beiden Foki entgegengesetzt. Die radiale Higgsquelle $S$ hat dasselbe Profil und Vorzeichen an beiden Foki.

Für eine radiale Quelle $u$ und Feldmasse $m\ge0$ bezeichne

$$
a_m[u]=\int_{\mathbb R^3} u(x)\frac{\sinh(m|x|)}{m|x|}\,d^3x,\qquad
K_m(R)=\frac{e^{-mR}}{4\pi R},
$$

mit Gewicht eins für $m=0$. Zweimaliges Anwenden der Schalenformel aus der Fokusprofilrechnung ergibt für zwei beliebige radiale Quellen $u_1,u_2$ mit disjunktem Träger den Paarterm $a_m[u_1]a_m[u_2]K_m(R)$. Diese Aussage braucht keine Gleichförmigkeit der radialen Dichte.

## Warum Vektor- und Higgsfeld hier beide anziehen

Für einen statischen Vektorkanal mit vorgegebener Quelle $\rho$ ergibt die Gauß- bzw. Proca-Bedingung den positiven Feldbeitrag $\tfrac12\langle\rho,K_m*\rho\rangle$. Normierungen und Kopplungen sind in $\rho$ aufgenommen. Wegen entgegengesetzter Quellenprofile ist der abstandsabhängige Kreuzterm $-a_m[\rho_+]^2K_m(R)$. In der ausgeschriebenen Wirkung gilt das für das J-Maxwell-Feld mit $m=0$. Für Photon und Z gilt die gleiche Rechnung innerhalb der zusätzlichen linearen Neutralfeldreferenz.

Für den Higgsradius schreibe $h=v+\eta$. Am stabilen gebrochenen Vakuum ist die quadratische Energie bei festgehaltenen Besetzungen und zur führenden Ordnung in den kleinen Quellen

$$
E_h[\eta]=\tfrac{Z_h}{2}\langle\eta,(-\Delta+m_h^2)\eta\rangle
+\langle S,\eta\rangle,\qquad Z_h>0,\quad m_h^2=V''(v)/Z_h>0.
$$

Hier ist $S$ die erste Variation der Materieenergie nach $h$ bei $v$. Eine besetzungsabhängige Korrektur zur quadratischen Higgsenergie ist von höherer Ordnung, wenn die Quellen gemeinsam klein skaliert werden. Kreuzkopplungen wie $\eta Z_0^2$ liegen ebenfalls außerhalb dieser Ordnung. Die stationäre Antwort ist $\eta=-K_{m_h}*S/Z_h$, und ihre Einsetzung liefert $-\langle S,K_{m_h}*S\rangle/(2Z_h)$. Da die beiden skalaren Quellen gleich sind, ist der Kreuzterm $-a_{m_h}[S_+]^2 K_{m_h}(R)/Z_h$.

Die abstandsabhängige Energie hat somit die Form

$$
E(R)=E_{\rm selbst}-\sum_\alpha C_\alpha K_{m_\alpha}(R),
\qquad C_\alpha\ge0,\qquad
-\partial_R E=-\sum_\alpha C_\alpha\left(m_\alpha+1/R\right)K_{m_\alpha}(R).
$$

Bei einem nichtverschwindenden wirksamen Kanal zieht die Kraft die Foki strikt zusammen. Damit besitzt die geprüfte quadratische Wirkung in diesem getrennten Zweifokuszweig keinen stationären Abstand. Sind alle Außenamplituden null, ist die Energie in dieser Ordnung vom Abstand unabhängig. Beide Fälle lassen den gesuchten stabilen Abstand offen.

## Radiale Relaxation bei festem Zulässigkeitsraum

Erlaube zusätzlich, dass sich die Profile und ihre Radien innerhalb eines festen oberen Radius $b$ ändern, sofern die Ladungskonjugationsrelation weiter gilt. Reine Profilenergien dürfen beliebig vom Profil abhängen. Vorausgesetzt ist, dass sie den Abstand nicht direkt enthalten und dass die zulässige Profilmenge für alle $R>2b$ dieselbe bleibt. Dann ist jeder feste Profilzweig in $R$ monoton nicht fallend. Das punktweise Infimum über dieselbe Profilmenge ist ebenfalls monoton nicht fallend. Ist ein Profil im Inneren eines gemeinsamen stationären Zweigs ausgewählt, muss dort die partielle Ableitung nach $R$ verschwinden. Ein nichtverschwindender Außenkanal schließt dies durch die obige strikte Ungleichung aus. Das Argument erfasst weder überlappende Wolken noch Profile mit einer zusätzlichen, abstandsabhängigen Zwangsbedingung oder unbekannte höhere Ordnungen.

## Konsequenz

Die geprüften linearen Feldterme liefern eine Wechselwirkung, aber keine dynamische Festlegung eines getrennten Fokusabstands. Ein zusätzlicher mechanischer Beitrag mit Gegenkraft, ein anderer Zustand als das ladungskonjugierte Paar oder ein voll gekoppelter Zweig außerhalb dieser Näherung wäre gesondert zu begründen. Für eine ergänzte Energie müsste an einem stationären Abstand $R_*$ der zusätzliche Term die negative Steigung $-\partial_R E(R_*)$ liefern und für ein nichtentartetes Minimum eine positive Gesamtkrümmung ergeben. Der I3-Ansatz braucht weiterhin eine eigenständige Überschussdynamik. Die native OP5-Randwirkung und H96 bleiben offen.
