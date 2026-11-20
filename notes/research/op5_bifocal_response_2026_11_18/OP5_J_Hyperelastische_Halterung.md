# OP5 – Hyperelastische Halterung in zweiter Ordnung

20. November 2026. Analytische Erkundung im Materieframe M. Es geht um die statische zweite Materialvariation der beiden Hauptkomponenten. Gewählt wird das Saint-Venant–Kirchhoff-Gesetz für kleine endliche Deformationen um den unbelasteten Zustand. Die Kopplung der Komponenten ist zunächst die bisherige Paarfeder pro gemeinsamem Referenzvolumen. Dieses Materialmodell ersetzt die lineare Kraftbilanz, auf der die [kinematische Reservoirrechnung](OP5_J_Reservoir_Quadrupolabgleich.md) aufbaut.

## Vorwissen geprüft

Die [statische Halterung](OP5_J_Halterung_Spannungsbilanz.md) liefert $w=-u/c$ und lineare Spannungskompensation. Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) liefert ein kompaktes longitudinales Plateau und einen linearen erhaltenen Tensor. Die [Federarbeit](OP5_J_Feder_Reservoirbilanz.md) bestimmt einen Beitrag zur Energie zweiter Ordnung bei vorgegebenen ersten Verschiebungen. Der [Reservoirabgleich](OP5_J_Reservoir_Quadrupolabgleich.md) kompensiert diesen direkten Beitrag ohne unbekannte zweite Verschiebungen. Die lokale Suche nach Piola und Hyperelastizität ergab im OP5-Zweig bisher keinen statischen zweiten Materialabgleich. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigene kosmologische Bestandsdynamik.

## Wirkung und erste Piola-Spannung

Im gemeinsamen Referenzchart $X$ seien die Materialabbildungen $x_1=X+u(X)$, $x_2=X+w(X)$. Für die erste Komponente sei $F_1=I+\nabla_X u$, $E_1=(F_1^{\mathsf T}F_1-I)/2$ und
$$
W_1^{\rm el}=\tfrac{\lambda}{2}(\operatorname{tr}E_1)^2+\mu\,\operatorname{tr}(E_1^2),
\qquad
\mathsf C E=\lambda\operatorname{tr}(E)I+2\mu E .
$$
Die zweite Komponente hat $W_2^{\rm el}=c\,W_1^{\rm el}(F_2)$ mit $F_2=I+\nabla_X w$, $c>0$. Die Namen $W_i^{\rm el}$ bezeichnen hier elastische Energiedichten. $\mu>0$ und $3\lambda+2\mu>0$ geben strikt positive lineare Energie. Der erste Piola-Tensor der ersten Komponente ist $P(F)=F\,\mathsf C E$. Die Wahl ist ein lokales konstitutives Vergleichsgesetz um $F=I$. [Herleitung der Spannungsmaße und des Materialgesetzes](https://www.weizmann.ac.il/chembiophys/bouchbinder/sites/chemphys.bouchbinder/files/uploads/Courses/2019/Q4-FiniteElasticity-sol.pdf)

Die statische Vergleichsenergie umfasst zusätzlich $k|u-w-d|^2/2$ pro Referenzvolumen. Bei beliebig vorgegebener relativer Ruhelage $d(X)$ sind die Federkräfte in den beiden Variationsgleichungen entgegengesetzt, sodass
$$
\operatorname{Div}_X(P_1+P_2)=0.
$$
Die Summe enthält keine direkte äußere Körperkraft. Das ist eine Gleichung im gemeinsamen Referenzchart.

Setze $u=\epsilon u_1+\epsilon^2u_2$ und $w=-\epsilon u_1/c+\epsilon^2w_2$. Das Plateau der dynamischen Konstruktion ist longitudinal, also $u_1=\nabla_X\varphi$ und $H=\nabla_X u_1$ symmetrisch. Mit $S=u_2+cw_2$ ist die lineare Summe der beiden Piola-Tensoren null und der Koeffizient zweiter Ordnung lautet
$$
(P_1+P_2)^{(2)}=\mathsf C\varepsilon(S)+(1+1/c)N(H),\qquad
N(H)=\tfrac{\lambda}{2}\operatorname{tr}(H^2)I+3\mu H^2+\lambda(\operatorname{tr}H)H.
$$
Die beiden quadratischen Materialterme addieren sich, weil $cN(-H/c)=N(H)/c$. Für die zweite Verschiebung entsteht eine erzwungene Navier-Gleichung. Eine weitere Änderung von $d$ beeinflusst die relative Kraftaufteilung, aber nicht diese Summengleichung.

## Kompaktheitsgrenze

Angenommen, $S$ sei glatt und kompakt. Dann folgt durch Testen der Summengleichung mit $X$ und partielle Integration
$\int\operatorname{tr}[(P_1+P_2)^{(2)}]=0$. Der lineare Dehnungsterm integriert sich wegen der Kompaktheit zu null. Für kompakte longitudinale $u_1$ gilt außerdem
$$
\int(\operatorname{tr}H)^2\,d^3X=\int\operatorname{tr}(H^2)\,d^3X.
$$
Die Differenz der Integranden ist die Divergenz von $(\Delta\varphi)\nabla\varphi-H\nabla\varphi$. Also
$$
\int\operatorname{tr}N(H)\,d^3X
=\left(\tfrac52\lambda+3\mu\right)\int|H|^2\,d^3X>0
$$
für jede nichttriviale kompakte longitudinale Verschiebung. Der Koeffizient liegt im strikt positiven Lamé-Bereich oberhalb von $4\mu/3$. Das widerspricht der angenommenen kompakten zweiten Summenverschiebung. Mindestens eine der beiden zweiten Verschiebungen muss im betrachteten unbeschränkten Modell einen mechanischen Ausläufer haben. In einer auf einen endlichen Träger begrenzten Variante müssten geeignete Randkräfte hinzukommen. Das Argument gilt für das gewählte Materialgesetz und die ausschließlich innere Paarfeder im Referenzchart.

Rückwärts benennt dieselbe Rechnung einen fehlenden Term. Eine unabhängig vorgegebene Eigenverformung zweiter Ordnung könnte im ersten Material den Zusatz $-(1+1/c)N(H)$ in der Summe liefern, da $N(H)$ symmetrisch ist und $\mathsf C$ invertierbar. Dafür wäre $\varepsilon_*^{(2)}=(1+1/c)\mathsf C^{-1}N(H)$ eine formale Wahl. Sie erlaubt eine kompakte Summenverschiebung in der korrigierten Referenzgleichung. Der materielle Träger dieser Eigenverformung und ihre eigene Quellenbilanz sind zusätzliche Anforderungen.

## Was in die gewöhnliche gravitative Quelle eingeht

Der direkte Restmassentransport erhält bei zweiter Ordnung gegenüber dem kinematischen Vergleich den Zusatz
$$
-\nabla\cdot(\rho_1 u_2+\rho_2 w_2).
$$
Die Navier-Summengleichung legt $u_2+cw_2$ fest. Die massengewichtete Kombination folgt daraus nur bei proportional passenden Dichten. Insbesondere ist ein mechanischer Ausläufer für sich keine Ableitung eines gewöhnlichen Gravitationsmultipols.

Für die räumliche Spannung braucht man außerdem den Cauchy-Tensor am gemeinsamen Raumpunkt. Für Material 1 gilt $\sigma(x)=\det(F_1)^{-1}P_1F_1^{\mathsf T}$ bei $x=x_1(X)$. Gegenüber $(P_1)^{(2)}$ kommen in zweiter Ordnung am festen Raumpunkt die Terme
$$
(\mathsf C H)H^{\mathsf T}-(\operatorname{tr}H)\mathsf C H-(u_1\cdot\nabla)\mathsf C H
$$
hinzu. Für Material 2 gelten die analogen Faktoren mit seiner Steifigkeit und ersten Verschiebung. Davon getrennt greifen die entgegengesetzten Federkräfte im Raum an $x_1$ und $x_2$ an. Mit Kraft $f_i$ am ersten Endpunkt und $\ell=x_1-x_2$ ist die räumliche Kraftdichte bereits in zweiter Ordnung ein Kraftdipol. In der Verteilungsform
$$
f_i[\delta(x-x_1)-\delta(x-x_2)]
=-\partial_j\left[f_i\ell_j\int_0^1\delta(x-x_2-s\ell)\,ds\right]
$$
sieht man den nötigen Verbindungsstress in der gewöhnlichen Impulsbilanz. Bei nichtzentralen Federkräften ist auch das Drehmoment der Vorrichtung für die relative Ruhelage zu bilanzieren. Die angesetzte Paarfeder allein legt den vollständigen symmetrischen Energie-Impuls-Tensor der Ansteuerung nicht fest.

Der bisherige Reservoirkompensator gleicht weiterhin die bereits berechneten direkten Beiträge aus. Eine vollständige gewöhnliche Quelle zweiter Ordnung braucht zusätzlich die jetzt erzwungenen Materialverschiebungen, die Verbindungs- und Halterungsbilanz sowie die Energie der aktiven Steuerung. Ein gewöhnlicher Außenmesswert, die native Higgs–OP5-Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_hyperelastische_halterung.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_hyperelastische_halterung.txt) · [Laufmanifest](op5_j_hyperelastische_halterung.json)

Wolfram prüfte den quadratischen Piola-Koeffizienten, das positive Spurgewicht am Lamé-Rand, die lokale Hessian-Divergenzidentität und die Cauchy-Umrechnung am Materialpunkt symbolisch. Die Kompaktheitsgrenze folgt aus dem analytischen Spurargument. Lokal reproduzierbar im Notizordner mit `wolframscript -file op5_j_hyperelastische_halterung.wl`. Ausgeführt wurde der Kernel über den Connector. Qiskit wurde erwogen. Die Rechnung verwendet klassische statische Materialvariation.
