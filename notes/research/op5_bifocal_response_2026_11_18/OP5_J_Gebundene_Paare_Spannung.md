# OP5 — Gebundene Paare als Spannungsträger

20. November 2026. Analytische Erkundung im Materieframe M. Verdünnte, voneinander unabhängige Paare mit kleinen Relativgeschwindigkeiten. Der geometrische Dichteabgleich verwendet die konstante Ruhemasse der Konstituenten als führenden Anteil. Bindungsenergie und Antrieb brauchen für die vollständige Tensorquelle einen eigenen Abgleich.

## Vorwissen geprüft

Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) verlangt für das [Kontrollprofil](OP5_J_Kontrollkontrast.md) die integrierte Längs- minus Querspannung $Q\ddot s/2$, wobei $Q=64\pi A a^4\ell/1575$. Der [gebundene Zweikörpervergleich](OP5_Gebundener_Tensor.md) liefert die Aufhebung von kinetischem und Bindungsstress im stationären Mittel. Die [Fokusabstandsrechnung](W2_Fokusabstand.md) findet für getrennte ladungskonjugierte Foki nur Anziehung. Die [gleichnamigen Foki](W2_Gleichnamige_Foki.md) enthalten dagegen den bedingten stabilen Vergleich mit Coulombabstoßung und zusätzlichem geradem Zugterm. Diese Zugkraft ist eine Modellannahme. Die Frage wird im [Gesamtbild](../../../wiki/Gesamtbild.md) der lokalen OP5-Messabbildung zugeordnet. Rückwärts werden das benötigte Dichtemoment und das unveränderte Endpunktfeld getrennt geprüft.

## Die integrierte Spannungsbilanz ist erreichbar

Nimm $N$ Paare gleicher Konstituentenmasse $M$ mit reduzierter Masse $\mu=M/2$. Die Paarzentren bleiben fest. Je die Hälfte der Paarachsen liegt entlang $x$ und $y$. Die relative Separation ist $R(t)$ für alle Paare. Die Veränderung des zweiten Ruhemassenmoments ist
$$
\delta I_{xx}=\delta I_{yy}=\frac{N\mu}{2}(R^2-R_0^2),\qquad
\delta I_{zz}=0.
$$
Die Faktoren folgen aus den Ortsverschiebungen $\pm R/2$ um jedes Zentrum. Das Zielmoment $\delta I_{xx}=\delta I_{yy}=-Qs(t)$ verlangt
$$
R(t)=\sqrt{R_0^2-\frac{2Q}{N\mu}s(t)},\qquad R_0^2>\frac{2Q}{N\mu},
$$
für $0\le s\le1$. Dadurch stimmt die Momentbilanz. Die räumlich aufgelöste Funktion $f$ ist damit noch nicht eingestellt.

Im effektiven Vergleich $V(R,t)=C/R+\mathcal T(t)R$ mit $C>0$ ist die Relativgleichung $\mu\ddot R=C/R^2-\mathcal T$. Sie bestimmt rückwärts die nötige Zugspannung
$$
\mathcal T(t)=C/R^2-\mu\ddot R .
$$
Bei glatter, hinreichend langsamer Umschaltung bleibt sie positiv. Eine hinreichende Bedingung ist $\mu\sup|\ddot R|<C/R_0^2$. Mit einer glatten Schaltfunktion, bei der auch $\ddot s$ auf beiden Plateaus null ist, liegt jedes ruhende Plateau im stabilen Minimum des jeweils eingestellten Potentials. Bei festem $C,\mathcal T>0$ besitzt das Modell nur ein solches Minimum. Die Änderung muss also von einer steuerbaren Zugspannung kommen.

In der führenden mechanischen Impulsbilanz hat eine Paarachse $\mathbf e$ den integrierten radialen Stress
$$
\bigl[\mu\dot R^2-R\,\partial_R V(R,t)\bigr]e_i e_j
=\mu(\dot R^2+R\ddot R)e_i e_j.
$$
Damit ergeben die beiden Achsengruppen die nötige Querspannung $-Q\ddot s/2$ und keine Längsspannung. Das ist die Summe aus Teilchenkinetik und zentralem Kraftstress in der instantanen Näherung. Die Energiebilanz zeigt den Beitrag des Antriebs:
$$
\frac{d}{dt}\left(\frac\mu2\dot R^2+\frac C R+\mathcal T R\right)
=R\,\dot{\mathcal T}.
$$
Bei einer Verkürzung von $R_0$ auf $R_1$ steigt die interne Energie relativ zum Modellnullpunkt um $2C(1/R_1-1/R_0)>0$ pro Paar. Der Antrieb muss diese Arbeit bzw. einen entsprechenden Energieaustausch liefern. Die Energie seines Trägers ist im Vergleichspotential nicht bestimmt. Wird die vollständige D-Quelle statt der Ruhemassenverteilung ausgewertet, müssen Bindungsenergie und Antriebsquelle in die Momente und in die Beobachtungsabbildung eingehen.

## Gleichsinnige Verkürzung verfehlt den exakten Endpunktabgleich

Für eine endliche, freiräumliche Anordnung mit festen Zentren $\mathbf c_j$, Paarachsen $\mathbf e_j$ und kompaktem Träger liefert der statische Yukawa-Kern $G_m$ entlang $\mathbf x=r\mathbf n$ asymptotisch $u(r\mathbf n)\sim e^{-mr}m^2 F(\mathbf n)/(4\pi r)$, falls $F(\mathbf n)\ne0$. Denn $|\mathbf x-\mathbf y|=r-\mathbf n\cdot\mathbf y+O(1/r)$. Der Koeffizient der Änderung bei Punktkonstituenten ist
$$
F(\mathbf n)=2M\sum_j e^{m\mathbf n\cdot\mathbf c_j}
\left[
\cosh\!\left(\frac{mR_1}{2}\mathbf n\cdot\mathbf e_j\right)
-\cosh\!\left(\frac{mR_0}{2}\mathbf n\cdot\mathbf e_j\right)
\right].
$$
Identische kompakte radial symmetrische Konstituenten multiplizieren ihn mit einem strikt positiven Formfaktor. Jede Klammer ist bei $R_1<R_0$ nichtpositiv und bei nichtverschwindender Projektion strikt negativ. Das Außenfeld verschwindet daher nicht identisch. Es kann dann auf keiner offenen Teilmenge seiner zusammenhängenden unbeschränkten Vakuumregion exakt null sein, weil dort die homogene modifizierte Helmholtz-Gleichung analytische Lösungen hat. Endpunktgleichheit in ganzen Apparaturumgebungen dieser Region scheitert für diese Ruhemassenroute. Einzelne Messpunkte oder eine bloß angenäherte Übereinstimmung sind dadurch nicht ausgeschlossen.

Somit erfüllt die Verkürzung den integrierten Spannungstest, während die volle quellenseitige Kompensation fehlt. Eine zusätzliche Änderung mit entgegengesetztem Yukawa-Beitrag ist nötig, sofern die exakte Außenfeldgleichheit erhalten bleiben soll. Eine einzelne räumlich integrierte Momentbedingung kann sie nicht sichern.

## Kontrolle und Status

[Wolfram Language](op5_j_gebundene_paare_spannung.wl) kontrolliert den aus dem Zielmoment bestimmten Paarabstand in der Bewegungsgleichung, den mechanischen Stress, die Arbeitsbilanz und die Ableitung des Yukawa-Richtungsfaktors. Dessen Vorzeichen folgt daraus, dass $\sinh$ dasselbe Vorzeichen wie sein Argument hat. Für diese klassische Bindungs- und Feldrechnung ist keine Quantenschaltung definiert. Eine native Erzeugung der Zugspannung, ein erhaltener vollständiger Antriebstensor, die räumliche Kompensation und H96 bleiben offen.
