# OP5: Bindung des Sechserkandidaten im J-Coulomb-Vergleich

19. November 2026. Analytische Erkundung für OP5/T9 im M-Frame. Die [Ladungsauslese](OP5_Paarstabilitaet.md) ergibt $udd+3\bar\nu$ als kleinsten neutralen Kandidaten mit $B-L=4$. Für [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) wären eine hinreichend langlebige gebundene Komponente und ihre Dichte nötig. Wir prüfen rückwärts die notwendige Energieschwelle. Wir ersetzen die drei Quarks durch einen vorgegebenen punktförmigen, stabilen Kern der Masse $M>0$ und J-Ladung $+3$ in Einheiten der J-Ladung eines Quarks. Die Antineutrinos sind drei identische Spin-½-Fermionen mit Masse $m>0$ und J-Ladung $-1$. Schwache Umwandlung, innere Kernzerlegung, Higgs und dynamische Strahlungsmoden sind nicht Teil dieses Hamiltonoperators.

## Modell und Fragmentationsschwellen

In Einheiten $\hbar=c=1$, mit $A=g_J^2/(4\pi)>0$, gilt vor Abtrennung der freien Schwerpunktsbewegung
$$
H_N=-\frac{\Delta_X}{2M}-\sum_{i=1}^N\frac{\Delta_{x_i}}{2m}
-3A\sum_{i=1}^N\frac1{|x_i-X|}
+A\sum_{i<j}\frac1{|x_i-x_j|},\qquad 0\le N\le3.
$$
Die inneren Spektralunterkanten heißen $E_N$, ohne Ruhemassen und mit $E_0=0$. Der Spinraum ist eingeschlossen. Die Leptonkoordinaten sind gemeinsam mit den Spins antisymmetrisiert. Im Schwerpunktsystem ist die Bindung bei fester Teilchenzahl gegen alle Fragmentierungen äquivalent zu $E_N<\inf\sigma_{\rm ess}(H_N^{\rm int})$. Nach dem HVZ-Satz ist die Unterkante des wesentlichen Spektrums die kleinste Summe der inneren Clusterenergien. Jeder kernlose Cluster besteht aus gleichnamigen Ladungen. Seine innere Energie ist nichtnegativ und hat Infimum null, erreicht im Grenzfall immer größerer Abstände und verschwindender Impulse. Antisymmetrisierung gestattet solche Grenzfolgen durch räumlich getrennte Wellenpakete. Für $N=3$ bleiben nur die drei Schwellen $E_0,E_1,E_2$, je nachdem, wie viele Antineutrinos beim Kern verbleiben. Eine Kontrolle der 14 echten Partitionen der vier effektiven Objekte ergibt fünf Partitionen für $E_0$, sechs für $E_1$ und drei für $E_2$. [HVZ-Satz für Mehrteilchen-Hamiltonoperatoren, B. Simon](https://citeseerx.ist.psu.edu/document?doi=a41147b429710dae9930e171049f2511e69f6110&repid=rep1&type=pdf)

## Vollständige Induktion, auch für endliche Kernmasse

**Anfang.** Für $N=1$ ist die reduzierte Masse $\mu_1=Mm/(M+m)$ und der Coulomb-Grundzustand hat $E_1=-9\mu_1 A^2/2< E_0$. Er ist ein diskreter innerer Eigenzustand.

**Schritt.** Für $N=2,3$ gelte $E_{N-1}<E_{N-2}<\cdots<E_0$, und der innere Grundzustand des Clusters mit $N-1$ Antineutrinos existiere. Wähle die Koordinate des letzten Teilchens relativ zum Schwerpunkt dieses Clusters. Ihre kinetische Energie trennt sich in Jacobi-Koordinaten mit reduzierter Masse $m[M+(N-1)m]/[M+Nm]$ ab. Schneide den inneren Grundzustand mit einem symmetrischen glatten Abschneider so ab, dass jede Clusterkoordinate höchstens $R/4$ vom Clusterschwerpunkt entfernt liegt. Der Abschneider ist auf einem festen kleineren Anteil dieses Bereichs eins, sein Gradient ist $O(1/R)$. Die Eigenwertgleichung liefert für seine normierte abgeschnittene Version eine Energieabweichung $O(R^{-2})$ über $E_{N-1}$: Beim Einsetzen des Produkts heben sich die Kreuzterme über die Eigenwertgleichung auf und es bleibt der quadratische Gradient des Abschneiders. Seine Norm konvergiert gegen eins.

Setze das zusätzliche Antineutrino auf eine normierte, kugelsymmetrische glatte Schale zwischen $R$ und $2R$. Seine kinetische Energie ist $O(R^{-2})$. Für festgehaltene innere Koordinaten liefert das Winkelmittel des Coulomb-Kerns auf einer Kugel mit Radius $r$ exakt $1/r$ für jede Quelle im Inneren. Die resultierende Erwartung der Wechselwirkung ist
$$
-(4-N)A\,\langle 1/r\rangle\ \le\ -(4-N)A/(2R).
$$
Hier ist $4-N$ die J-Nettoladung des inneren Clusters. Sie ist für beide Schritte positiv. Bei der Antisymmetrisierung des Produkts sind die Beiträge mit verschiedenen äußeren Teilchen auf disjunkten Konfigurationsbereichen getragen: Innere Teilchen befinden sich höchstens $R/4$ vom Clusterschwerpunkt und damit höchstens $R/2$ voneinander bzw. vom Kern entfernt. Das äußere Teilchen hat einen Abstand von mindestens $3R/4$ zum Kern. Somit bleiben Erwartungswert und obere Schranke bei normierter Antisymmetrisierung erhalten. Für hinreichend großes $R$ dominiert die Anziehung der Ordnung $1/R$ die Kosten der Ordnung $1/R^2$. Das Variationsprinzip ergibt $E_N<E_{N-1}$. Aus den niedrigeren Clusterschwellen und HVZ folgt die Diskretheit.

Damit gilt **$E_3<E_2<E_1<E_0$**. Die schwächste Ionisationsschwelle ist $E_2$, und die Bindungslücke $E_2-E_3$ ist strikt positiv. Der Beweis gibt keinen Zahlenwert für die Lücke. Er gilt für jede positive Masse $M,m$ und $A>0$ im angenommenen nichtrelativistischen Operator. Im physikalischen Vergleich werden schwache Kopplung und eine Kerngröße klein gegenüber den relevanten Orbitalskalen benötigt.

## Die Anomalie lässt sich durch Mischen mit B−L nicht beheben

Sei $X$ eine gemeinsame Dirac-Vektorladung $x_q$ auf Quarks und $x_\ell$ auf Leptonen derselben Generation. Mit den [vorher gezählten Weyl-Dubletts](OP5_Paarstabilitaet.md) gilt $\mathcal A_{SU(2)^2X}=(3x_q+x_\ell)/2$. Ein Zusatz $\lambda(B-L)$ zu $J$ liefert $3(1+\lambda/3)+(1-\lambda)=4$. Die gemischte Anomalie bleibt also für jedes $\lambda$ gleich $2$. Innerhalb der beiden universellen Vektorladungen ist die einzige nichttriviale Richtung mit verschwindender gemischter Spur proportional zu $B-L$. Beim Kandidaten hätten dann der $udd$-Kern und jedes Antineutrino dasselbe Ladungsvorzeichen und die gesamte Ladung wäre in der $B-L$-Normierung $+4$. Der attraktive neutrale Coulomb-Verband würde bei diesem Austausch des Generators entfallen. Eine Erweiterung, die den ursprünglichen J-Generator gleichzeitig mit schwachem $SU(2)$ eicht und seine Ladungen erhält, braucht daher einen zusätzlichen Mechanismus zur Anomalieaufhebung. Zur Konsistenz einer konkreten Erweiterung wären auch die übrigen Anomaliespuren zu prüfen.

## Geltungsbereich für OP5

Die Rechnung zeigt einen gebundenen Grundzustand des effektiven Kernmodells unter allen seinen Aufbruchsschwellen. Der $udd$-Kern und die Vernachlässigung seiner Umwandlungen sind Eingaben. Native Kerndynamik, konkurrierende Kanäle in einer konsistenten Quantentheorie und die kosmologische Besetzung sind offene Voraussetzungen für H96. Für I3 könnte ein eigener Überschussmechanismus den Anfangsbestand festlegen. Der Bindungsbeweis bestimmt ihn nicht.
