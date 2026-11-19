# OP5: Kernrandbedingung und effektive Reichweite der Neutron–Blei-Streuung

19. November 2026. Nicht blinde analytische Erkundung in M. Die [vorige Neutron–Blei-Rechnung](OP5_J_Neutron_Blei.md) gibt am elektromagnetischen Lepton-Nullpunkt eine Streulängenuntergrenze für nichtnegative innere Randdaten. Hier invertieren wir die äußere Gleichung für eine vorgegebene Streulänge nahe dem tabellierten Wert. Das zeigt, was ein beliebiger reeller Kernrand bei Nullenergie leisten müsste. Für die effektive Reichweite setzen wir zusätzlich ein reelles, lokales, energieunabhängiges Einkanalpotential mit regulärer Randbedingung am Ursprung voraus. Es wird kein H96-Datentest durchgeführt.

## Rückwärts von der tabellierten Streulänge

Wir behalten den reellen, repulsiven Punktkern-Yukawa-Anteil für $r\ge r_0=20$ fm bei,
$$
V(r)=2118 A\,\frac{\hbar c}{r}\exp[-m_Jr/(\hbar c)],\qquad
W(r)=\frac{2\mu_{nT} V(r)}{(\hbar c)^2},\qquad u_a''=W u_a .
$$
Alle Längen in dieser Rechnung sind in fm. Die Eingaben sind $A=0{,}01$, $\mu_{nT}=0{,}935$ GeV und $m_J\le1{,}238$ MeV im [vorgegebenen Massenfenster](OP5_Endliche_J_Reichweite.md). NIST gibt für $^{208}\mathrm{Pb}$ die gebundene kohärente Streulänge $9{,}50$ fm. Die freie Streulänge unterscheidet sich durch den kinematischen Faktor von rund $1{,}005$. Das Vergleichsintervall $9\le a\le10$ fm umfasst beide Konventionen. [NIST, Neutronenstreulängen](https://www.ncnr.nist.gov/resources/n-lengths/list.html)

Normiere die reelle, äußere Nullenergielösung durch $u_a(r)=r-a+o(1)$ im Unendlichen. Dann gilt die Volterra-Gleichung
$$
u_a(r)=r-a+\int_r^\infty(t-r)W(t)u_a(t)\,dt.
$$
Sie impliziert $u_a(r)\ge r-a>0$ für $r\ge r_0$. Ein erster Nullpunkt beim Rückwärtsgehen wäre wegen des positiven Integranden jenseits dieses Punkts unmöglich. Auf $[100,200]$ fm ist $W(r)\ge W(200\,{\rm fm};1{,}238\,{\rm MeV})>0{,}286\,{\rm fm}^{-2}$. Ableiten der Volterra-Gleichung liefert
$$
u'_a(100\,{\rm fm})\le1-\int_{100}^{200}W(t)(t-10)\,dt<-4000.
$$
Ferner ist $u_a(100\,{\rm fm})\ge90$ fm. Auf dem inneren Intervall $[20,100]$ fm gilt $W\ge\kappa^2$, mit $\kappa=\sqrt{W(100\,{\rm fm};1{,}238\,{\rm MeV})}\simeq1{,}03527\,{\rm fm}^{-1}$. Vergleich in der rückwärts orientierten Koordinate $100\,{\rm fm}-r$ liefert
$$
u_a(r)\ge90\,{\rm fm}\,\cosh[\kappa(100\,{\rm fm}-r)].
$$
Die Anfangsableitung in dieser rückwärts orientierten Koordinate ist positiv. Für die inverse logarithmische Bedingung am Kernrand folgt zusätzlich
$$
L(a):=\frac{u'_a(r_0)}{u_a(r_0)}\le-\kappa\tanh(\kappa\,80\,{\rm fm})<-1{,}03\,{\rm fm}^{-1}.
$$

## Wie eng der Randwert liegen muss

Die Ableitung der äußeren Lösung nach $a$ hat im Unendlichen Wert $-1$ und Ableitung null. Der Wronskian $u_a\partial_a u'_a-u'_a\partial_a u_a$ ist konstant und gleich eins. Damit gilt genau
$$
\frac{dL}{da}=\frac{1}{u_a(r_0)^2}.
$$
Setzt man die obige Vergleichsschranke ein, ist die Variation von $L$ über das gesamte Intervall von 9 bis 10 fm kleiner als $6\times10^{-76}\,{\rm fm}^{-1}$. Die Lage dieses engen Randwertintervalls hängt vom Mediator ab. Seine Breite ist im geprüften Fenster gleichmäßig beschränkt. Das ist eine Aussage über die inverse Abbildung für den reellen äußeren Operator. Ein frei gewählter negativer Kernrand kann eine einzelne Nullenergie-Streulänge grundsätzlich reproduzieren. Die Rechnung bestimmt keine Eintrittswahrscheinlichkeit für die erforderliche Abstimmung.

## Konsequenz für einen reellen lokalen Kern

Für ein reelles, lokales, energieunabhängiges Einkanalpotential mit exponentiell abfallendem Außenanteil gilt Bethe's Integralformel in der Normierung $u_a(r)\sim r-a$:
$$
k\cot\delta_0(k)=-\frac1a+\frac12r_{\rm eff}k^2+\cdots,\qquad
r_{\rm eff}=2\int_0^\infty\!\left[(1-r/a)^2-(u_a(r)/a)^2\right]\,dr .
$$
Die Formel ergibt sich aus dem Wronskian der regulären Lösungen bei Nullenergie und kleinem $k^2$, mit dem freien äußeren Anteil als Gegenstück. Ein exponentieller Yukawa-Ausläufer erlaubt den Grenzübergang im Integral. [Hammer und Lee, effektive Reichweite und Bethe-Integral](https://arxiv.org/abs/1002.4603)

Der positive Beitrag aus dem unbekannten Bereich $r<20$ fm ist höchstens $2\int_0^{20}(1-r/a)^2\,dr<106$ fm. Der Integrand außerhalb von 20 fm ist wegen $u_a\ge r-a$ nichtpositiv. Für das obere Limit der effektiven Reichweite genügt es, nur das Teilintervall $[20,21]$ fm zu berücksichtigen. Dort gilt $u_a/a\ge9\cosh(\kappa\,79\,{\rm fm})$. Daraus folgt
$$
r_{\rm eff}<-4{,}4\times10^{72}\ {\rm fm}.
$$
Die Schranke lässt das genaue reelle Kernpotential im Inneren offen. Die aus dem quadratischen Term allein geschätzte Energieskala, bei der er mit $1/a$ vergleichbar wird, beträgt höchstens ungefähr $10^{-66}$ eV, aus $E_*=(\hbar c)^2/(\mu_{nT}|a r_{\rm eff}|)$. Diese Schätzung ist keine Extrapolation der effektiven Reichweitenentwicklung auf experimentelle Neutronenenergien. Höhere Koeffizienten mögen ebenfalls außergewöhnlich groß sein.

Damit kann eine einzelne kleine Streulänge bei Nullenergie die große J-Abstoßung formal verbergen. Im reellen lokalen Einkanalmodell geht das zwingend mit einem extremen Koeffizienten der Energieabhängigkeit einher. Um einen tatsächlichen nuklearen Ausschluss herzustellen, wären Daten bei endlicher Energie und eine Rechnung einschließlich Absorption, weiterer Kanäle und gegebenenfalls energieabhängiger optischer Potentiale erforderlich. Das Ergebnis ersetzt keinen solchen Fit und lässt H96 offen.
