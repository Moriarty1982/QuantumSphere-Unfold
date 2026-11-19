# OP5: Schwacher Rückstoß des baryonenfreien Neutrinopaars

19. November 2026. Analytische Erkundung in M. Der [baryonenfreie Kandidat](OP5_Baryonenfreies_Neutrinopaar.md) enthält ein leichtes Dirac-Neutrino der Masse $m$ und ein schweres sequentielles Dirac-Neutrino der Masse $M$. Beide Vektorladungen am Z haben dasselbe Vorzeichen. Auf dem Weg zur kosmologischen Materieauslese prüfen wir, ob die endliche Größe des Coulomb-Systems schwache Rückstöße abschirmt. Es geht um den führenden spinunabhängigen Vektoranteil des Z-Austauschs. Die Rechnung setzt einen ungestörten Coulomb-Grundzustand, eine nichtrelativistische Schwerpunktsbewegung und den Einteilchen-Stromoperator in Impulsnäherung voraus. Zusätzliche neue Austauschbosonen und Stromterme bleiben außerhalb der Rechnung.

## Elastischer Beitrag bei endlichem Impuls

Sei $A=g_J^2/(4\pi)>0$, $\mu=mM/(m+M)$ und $a=(\mu A)^{-1}$. Die relative Koordinate sei $\mathbf r=\mathbf x_l-\mathbf x_H$. Nach Abtrennen der Schwerpunktphase lautet der normierte Vektoroperator für Impulsübertrag $\mathbf q$
$$
S(\mathbf q)=U_H+U_l,\qquad U_H=\exp[-i\tfrac{m}{M+m}\mathbf q\cdot\mathbf r],\qquad
U_l=\exp[i\tfrac{M}{M+m}\mathbf q\cdot\mathbf r].
$$
Die elastische Amplitude ist die Summe der beiden positiven Coulomb-$1s$-Formfaktoren. Da $a\,m/(m+M)=1/(MA)$, gilt für den schweren Summanden exakt
$$
\langle U_H\rangle_0=\left(1+\frac{q^2}{4M^2A^2}\right)^{-2}.
$$
Die dimensionsbehaftete Skala für seinen elastischen Formfaktor ist damit $MA$. Bei $q\ll 2MA$ bleibt der schwere Beitrag nahezu erhalten. Bei $q\gg 2MA$ kann der elastische Beitrag klein werden. Ein Detektor zählt aber prinzipiell auch Kernrückstöße, bei denen der Verband angeregt oder ionisiert wird.

## Inklusive Untergrenze unterhalb einer internen Energie $\Delta$

Sei $H_{\rm rel}=\mathbf p^2/(2\mu)-A/r$, $H_{\rm rel}|0\rangle=E_0|0\rangle$. $P_\Delta$ projiziere auf innere Endenergien höchstens $E_0+\Delta$, einschließlich gebundener und freier Zustände. Ein Impuls auf die schwere Komponente verschiebt den Relativimpuls nur um $-m\mathbf q/(M+m)$. Das Coulombpotential kommutiert mit $U_H$, und $\langle\mathbf p\rangle_0=0$. Seine mittlere Anregungsenergie ist deshalb
$$
\varepsilon_H=\langle 0|U_H^\dagger(H_{\rm rel}-E_0)U_H|0\rangle
=\frac{q^2m}{2M(M+m)} .
$$
Aus der spektralen Zerlegung des nichtnegativen Operators $H_{\rm rel}-E_0$ folgt
$$
\|(1-P_\Delta)U_H|0\rangle\|^2\le\varepsilon_H/\Delta .
$$
Die Überlappung der schweren Antwort mit der Gesamtantwort ist
$\langle U_H0|S|0\rangle=1+\langle0|\exp(i\mathbf q\cdot\mathbf r)|0\rangle=1+(1+a^2q^2/4)^{-2}\ge1$.
Außerdem ist $\|S|0\rangle\|\le2$. Setzt man $P_\Delta+(1-P_\Delta)$ zwischen die beiden Zustände und wendet Cauchy–Schwarz an, erhält man
$$
\boxed{\ \|P_\Delta S|0\rangle\|^2
\ \ge\ \left[\max\!\left(0,1-2\sqrt{\varepsilon_H/\Delta}\right)\right]^2 .\ }
$$
Die Einheit ist die normierte Vektorstärke des freien schweren Teilchens. Die Aussage setzt voraus, dass im führenden Stromoperator auch für den leichten Beitrag die angegebene Impulsnäherung benutzt wird. Die Abschätzung benötigt keine nichtrelativistische Energieabschätzung für den großen direkten Impuls auf das leichte Teilchen. Dessen Endzustände gehen lediglich über die Projektion, Überlappung und Norm in den Beweis ein. Eine relativistische Erweiterung des leichten Stroms und ihrer Interferenz ist für eine vollständige Vorhersage separat zu prüfen.

Für $m\le1$ eV, $M\ge45{,}6$ GeV und $q\le100$ MeV gilt $\varepsilon_H\le2{,}41\times10^{-6}$ eV. Bei $\Delta=1$ eV bleiben mindestens $0{,}9938$ Einheiten Vektorstärke unterhalb dieses internen Energieaufwands, für jede Kopplung im Gültigkeitsbereich des Coulomb-Modells. Bei einem Kern der Masse $M_T$ ist ein solcher Endzustand nur zugänglich, falls $vq-q^2/(2\mu_{PT})$ mindestens seinem Energieaufwand entspricht, wobei $v$ die relative Einlaufgeschwindigkeit und $\mu_{PT}$ die reduzierte Masse von Verband und Kern ist. Die Untergrenze gilt als zugänglicher Beitrag, wenn dieses Fenster mindestens $\Delta$ breit ist. Bei $q$ im Bereich einiger zehn MeV hat der reine Kernrückstoß $q^2/(2M_T)$ für Xenon die Größenordnung keV. Nahe dem Geschwindigkeitsendpunkt muss das zusätzliche Energiefenster explizit berücksichtigt werden.

## Einordnung der Stärke

Ein aktives Dirac-Neutrino mit Standard-Z-Kopplung hat als führenden Vektoranteil für einen freien Neutronstreuer
$$
\sigma_n^{Z}=\frac{G_F^2\mu_n^2}{8\pi}\simeq1{,}8\times10^{-39}\,{\rm cm}^2
$$
für $M\gtrsim45$ GeV. Hier ist $\mu_n$ die reduzierte Masse, $g_V^n=-1/2$ auf Baumebene und der Betrag des nichtrelativistischen Kontaktkoeffizienten $G_F/(2\sqrt2)$. Im Kern addieren sich die Vektorladungen kohärent; die Protonladung ist bei kleinem Impuls $g_V^p=1/2-2\sin^2\theta_W$ und daher betragsmäßig viel kleiner. Die experimentelle Standardgrenze benutzt eine andere Proton-Neutron-Normierung. Sie ist ein Größenvergleich und keine neu berechnete Ausschlusskurve für diesen Verband. [PDG, elektroschwache Neutralströme](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-standard-model.pdf)

LZ berichtet für sein Standardmodell für spinunabhängige WIMP-Nukleon-Streuung eine stärkste Grenze von $2{,}1\times10^{-48}\,{\rm cm}^2$ bei 36 GeV. Das ist ein Referenzpunkt in der Nähe der unteren Masse des schweren Partners und kein Grenzwert bei dessen Masse. Der Vergleich zeigt die Größenordnung des Problems für einen üblichen lokalen Halo aus solchen Paaren bei elektroschwacher Kopplung. Eine quantitative Grenze verlangt Geschwindigkeitsverteilung, genaue Massenkurve, Kernladungen, Akzeptanz und gegebenenfalls ein Modell für den lokalen Anteil. [LZ, Suche mit 4,2 Tonnenjahren](https://arxiv.org/abs/2410.17036)

Die endliche Größe verschiebt in diesem Modell schwache Streustärke zwischen elastischen und ionisierenden Kanälen. Sie unterdrückt die niederenergetische inklusive Antwort des schweren Neutrinos kaum. Eine kohärente Abschirmung durch die J-neutrale Bindung liefert diese Route damit nicht. Die Rechnung setzt keine neue Hauptvorhersage und führt keinen Beobachtungstest für H96 durch. Der Ursprung des kosmologischen Bestands und H96 bleiben offen.
