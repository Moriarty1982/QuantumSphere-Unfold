# OP5: Gebundener protonhaltiger Verband nach dem Beta-Zerfall

19. November 2026. Analytische Erkundung in M. Der eingeschränkte [$udd$-Vergleich](OP5_Sechserbindung.md) bindet drei Antineutrinos, bleibt aber für den [Beta-Zerfall](OP5_Anomalie_Betazerfall.md) offen. Sein ursprünglich geladener schwacher Kanal liefert $p+e^-+4\bar\nu_e$. Hier werden die Aufbruchsschwellen dieses Produkts im nichtrelativistischen Coulomb-Modell bestimmt. Proton und Elektron werden als vorgegebene effektive Teilchen mit endlichen Massen und mit den gewöhnlichen elektromagnetischen Ladungen benutzt. Antineutrinos sind identische Spin-½-Fermionen mit der positiven Masse $m$, elektrisch neutral. Dynamische Strahlung, kinetische Mischung von Photon und J, Higgs-Austausch, Kernstruktur und zusätzliche Materie der Anomalie-Erweiterung werden für den Bindungssatz weggelassen. Die schwache Rückumwandlung wird anschließend als eigene kinematische Schwelle verglichen.

## Energie der möglichen Fragmente

Sei $A=g_J^2/(4\pi)>0$ die J-Kopplung, $\alpha>0$ die elektromagnetische Kopplung und $0<3A<\alpha$. Die J-Ladungen von $p,e^-,\bar\nu_e$ sind $+3,+1,-1$. In Einheiten $\hbar=c=1$ lauten die Paarpotentiale
$$
V_{pe}=-\frac{\alpha-A\,3}{r_{pe}},\qquad
V_{p\bar\nu}=-\frac{3A}{r_{p\bar\nu}},\qquad
V_{e\bar\nu}=-\frac{A}{r_{e\bar\nu}},\qquad
V_{\bar\nu\bar\nu}=\frac{A}{r_{\bar\nu\bar\nu}}.
$$
Die unteren inneren Energien für ein gemeinsames Proton-Elektron-Fragment mit $k$ Antineutrinos bezeichnen wir mit $F_k$. Ohne Antineutrinos gilt mit der reduzierten Proton-Elektron-Masse $\mu_{pe}$ bereits
$$
F_0=-B_H(A),\qquad B_H(A)=\frac{\mu_{pe}}2(\alpha-3A)^2 .
$$
Der gewöhnliche Wasserstoffwert am Punkt $A=0$ liegt bei rund $13{,}6$ eV. [NIST, Ionisierungsenergie von Wasserstoff](https://physics.nist.gov/cgi-bin/Ionization/atom.php?element=H)

Ein Fragment ohne Proton und Elektron enthält nur gleichnamig geladene Antineutrinos und hat innere Unterkante null. Ein Fragment mit nur einem der beiden positiven Zentren der J-Ladung $Z\in\{1,3\}$ und $k$ Antineutrinos hat innere Unterkante mindestens $-k m Z^2 A^2/2$. Dazu schreibt man die inneren kinetischen Terme in den Koordinaten relativ zum Zentrum, lässt den nichtnegativen Rückstoßterm und die gegenseitige Antineutrinoabstoßung weg und benutzt die Einteilchenunterkante $-mZ^2A^2/2$ für jedes Antineutrino. Die Pauli-Beschränkung kann diese Schranke nur verbessern. Für einen Aufbruch mit räumlich getrenntem Proton und Elektron folgt deshalb bei höchstens vier Antineutrinos die Untergrenze $-18mA^2$ für jede Summe der inneren Fragmentenergien. Der Coulomb-Anteil zwischen verschiedenen Fragmenten verschwindet am unendlichen Abstand. Ein Aufbruch mit gemeinsamem Proton-Elektron-Fragment hat Energieunterkante $F_j$ für ein $j<k$.

Eine hinreichende Trennung beider Schwellenfamilien ist damit
$$
0<3A<\alpha,\qquad B_H(A)>18m A^2 .
$$
Beispiel im führenden Modell: Für $A\le\alpha/6$ und $m\le 1$ eV gilt $B_H\gtrsim 3{,}3996$ eV und $18mA^2\lesssim 2{,}67\times10^{-5}$ eV. Gezählt wurden außerdem alle 202 echten Partitionen der sechs effektiven Objekte mit für die Zählung markierten Antineutrinos. 51 Partitionen enthalten ein gemeinsames Proton-Elektron-Fragment, 151 trennen Proton und Elektron. Die physikalischen Schwellen hängen allein von der Zusammensetzung der Fragmente ab.

## Induktion bis zum vierten Antineutrino

Der Zweikörper-Grundzustand für $F_0$ ist diskret. Angenommen, der gemeinsame Cluster mit $k-1$ Antineutrinos besitzt einen diskreten Grundzustand, und die bisher erhaltenen Energien sind strikt fallend. Nach der obigen Trennung und dem [HVZ-Satz für Coulomb-Cluster](https://citeseerx.ist.psu.edu/document?doi=a41147b429710dae9930e171049f2511e69f6110&repid=rep1&type=pdf) ist $F_{k-1}$ die niedrigste Aufbruchsschwelle des Systems mit $k$ Antineutrinos. Für $k=1$ ist das unmittelbar $F_0$.

Schneide den inneren Grundzustand des Clusters auf einen Radius $R/4$ um seinen Schwerpunkt ab. Die additive Erwartungswertänderung ist $O(R^{-2})$ und folgt aus der Eigenwertgleichung und dem quadrierten Gradienten des Abschneiders. In Jacobi-Koordinaten lege das zusätzliche Antineutrino in eine kugelsymmetrische Schale von $R$ bis $2R$ um den Clusterschwerpunkt. Seine kinetische Energie ist $O(R^{-2})$. Der neue Fermionzustand wird antisymmetrisiert. Austauschanteile sind räumlich disjunkt, da zum Beispiel der Abstand zum Proton das äußere Antineutrino eindeutig identifiziert: innen höchstens $R/2$, außen mindestens $3R/4$. Das Winkelmittel jeder Coulomb-Quelle des inneren Clusters ist am Schalenradius $r$ der Betrag ihrer Ladung mit Vorzeichen geteilt durch $r$. Die gesamte äußere Wechselwirkung hat daher den Erwartungswert $-(5-k)A\langle 1/r\rangle\le -(5-k)A/(2R)$. Für $k\le4$ ist $5-k>0$. Damit senkt ein hinreichend großes $R$ die Energie strikt unter $F_{k-1}$. Der Schritt funktioniert auch mit endlicher Proton- und Elektronenmasse.

Es folgt
$$
F_4<F_3<F_2<F_1<F_0.
$$
Der volle Verband besitzt einen diskreten Grundzustand mit $Q_J=0$, $Q_{\rm em}=0$ und $B-L=4$. Seine tiefste Aufbruchsschwelle im Modell ist $(p+e^-+3\bar\nu_e)_{\rm geb}$ plus ein freies Antineutrino. Der Beweis liefert keinen Zahlenwert für die letzte Ionisationsenergie $F_3-F_4$.

## Rückumwandlung und Bildung

Der gewöhnliche geladene schwache Strom gestattet $p+e^-\to n+\nu_e$. Mit den vier Antineutrinos im Eingang ist auch der Sektor mit einem Neutron und drei Antineutrinos mit allen drei relevanten Ladungen vereinbar. Die vorige Bindungsschranke $B_n\le81mA^2/8$ gilt für diesen Neutronsektor im Coulomb-Vergleich. Setze $B_p=-F_4>0$ und $\Delta_{\rm free}=M_n-M_p-m_e-m$ wie in der [Beta-Rechnung](OP5_Anomalie_Betazerfall.md). Der Abstand der gebundenen Massenschwellen ist
$$
(M_n+3m-B_n)-(M_p+m_e+4m-B_p)
=\Delta_{\rm free}+B_p-B_n.
$$
Mit den gewöhnlichen Nukleonmassen, leichter Neutrinomasse und schwacher J-Kopplung ist er positiv, denn bereits $\Delta_{\rm free}>81mA^2/8$. Damit liegt der protonhaltige Grundzustand unter dem neutronhaltigen Sektor in diesem Vergleich. Die direkte Rückumwandlung mit zusätzlichem Neutralpaar hat eine höhere Schwelle im selben schwachen Regime, sofern nur die vorgegebenen kleinen Coulomb-Bindungen der Leptonen berücksichtigt werden. Für die Untergrenze in diesem größeren Sektor kann man alternativ die attraktivsten negativen Kreuzterme grob abschätzen: Bei $n+4\bar\nu+\nu$ hat je Antineutrino insgesamt höchstens die Anziehung eines Zentrums mit Ladung $+4$. Für feste Positionen der beiden positiven Zentren erhält man die Einteilchenuntergrenze $-m(4A)^2/2$ durch Zerlegung in eine gewichtete Summe zweier Einzentrum-Hamiltonoperatoren mit demselben Gesamtladungsfaktor $4$. Rückstoß und alle gleichnamigen Abstoßungen können weggelassen werden. Der Bindungsbetrag ist daher höchstens $32mA^2$. Die zusätzliche freie Schwelle liegt bei $\Delta_{\rm free}+2m$ relativ zum protonhaltigen freien Bestand und bleibt unter denselben leichten und schwach gekoppelten Bedingungen energetisch unzugänglich.

Gebundene Zustände der Zerfallsprodukte sind damit im Vergleich möglich. Die Rechnung bestimmt weder den Verzweigungsanteil des Beta-Zerfalls in gebundene Endzustände noch die Ionisation durch einen Strahlungshintergrund. Der Zustand enthält ein gewöhnliches Proton und Elektron und trägt Baryonenzahl eins. Seine elektromagnetische Kopplung und kosmologische Zuordnung müssen in einer Materiedichtebilanz berücksichtigt werden. Eine zusätzliche Population und ihr Beitrag zu H96 bleiben offen.
