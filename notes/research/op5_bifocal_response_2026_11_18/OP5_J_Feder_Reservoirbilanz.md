# OP5 – Federarbeit und Reservoir in zweiter Ordnung

20. November 2026. Analytische Erkundung im Materieframe M. Geprüft wird der direkte Energiebeitrag zweiter Ordnung für die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md). Verwendet werden zwei überlagerte linearelastische Kontinua bei fester Higgs-Referenz sowie ein lokaler Energiespeicher für die verstellte innere Feder. Die Rechnung bestimmt Beiträge zu $T^{00}$ auf dem erreichten Plateau.

## Vorwissen geprüft

Die [statische Halterung](OP5_J_Halterung_Spannungsbilanz.md) bestimmt die positive gespeicherte Energie und die lineare Schwächung der gewöhnlichen Außenquelle. Die [Antriebsenergie der Paarroute](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f384c6363c5356aef515a851c989fa943ab818b5/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Antriebsenergie_und_Gravitation.md) verlangt den vollständigen Arbeitsausgleich einschließlich Reservoir oder Randfluss. Die [Quadrupolkompensation](OP5_J_Quadrupol_Kompensation.md) bezieht sich auf die direkte Dichte in erster Ordnung. Rückwärts ist zu prüfen, welche Momentbedingungen das Reservoir zusätzlich zu seiner Gesamtarbeit erfüllen müsste. Diese Rechnung gehört zur lokalen OP5-Auslese im [Gesamtbild](../../../wiki/Gesamtbild.md). Die bei I3 erforderliche kosmologische Bestandsdynamik bleibt offen.

## Leistung und lokaler Energiefluss

Schreibe $R_{\rm F}=u-w-d$ für die Auslenkung der inneren Feder um die vorgeschriebene relative Ruhelage $d$. Die beiden mechanischen Gleichungen seien $\rho_1\ddot u=\nabla\cdot\sigma_1-kR_{\rm F}$ und $\rho_2\ddot w=\nabla\cdot\sigma_2+kR_{\rm F}$. In der verwendeten Koordinatenbeschreibung sind die Unterschiede der linearen und dehnungsmitgeführten Raummaße für die quadratische mechanische Energie erst in höherer Ordnung relevant. Aus kinetischer Energie, elastischer Energie und Federenergie $k|R_{\rm F}|^2/2$ folgt
$$
\partial_t e_{\rm mech}=\nabla\cdot\mathbf F+P_{\rm Schalt},\qquad
\mathbf F=\sigma_1\dot u+\sigma_2\dot w,\qquad
P_{\rm Schalt}=-kR_{\rm F}\cdot\dot d .
$$
Der mechanische Energiefluss im Kontinuitätssinn ist $-\mathbf F$. Interne Federkräfte übertragen Impuls zwischen den Komponenten. Die Änderung der Feder-Ruhelage leistet die darüber hinaus nötige Arbeit.

Für einen idealen ortsfesten Speicher ohne eigenen räumlichen Fluss sei $\partial_t e_{\rm res}=-P_{\rm Schalt}$. Dann ist für den Übergang von einem unbelasteten Ausgangspunkt zu einem ruhenden Plateau
$$
\delta e_{\rm int}=\delta(e_{\rm mech}+e_{\rm res})=\nabla\cdot\int\mathbf F\,dt,\qquad
\int\delta e_{\rm int}\,d^3x=0.
$$
Der Speicher kann einen anfänglich positiven Energievorrat haben. Seine **Änderung** ist die Gegenbuchung zur mechanischen Arbeit. Bei Versorgung von außen ohne diesen Speicher im betrachteten Volumen bleibt auf dem Plateau die positive gespeicherte mechanische Energie. Der zugehörige Gesamtmonopol hängt davon ab, wo und wie die Versorgung bilanziert wird.

## Eine gemeinsame Rampe legt die Endverteilung fest

Im linearen Modell der dynamischen Gegenbewegung bestehen bei einer räumlich festen Profilform mit einer gemeinsamen glatten Schaltfunktion $f(t)$ die Verschiebungen aus Summen räumlicher Felder mal geradzahliger Zeitableitungen $f^{(2n)}$. Die verwendeten zeitlichen Operatoren enthalten nur gerade Ableitungen. Setze $f=0$ vor der Schaltung, $f=1$ nach der Schaltung und alle Ableitungen an den Enden gleich null. Für alle nichtnegativen $n,m$ gilt
$$
\int f^{(2n)} f^{(2m+1)}\,dt =
\begin{cases}
1/2,& n=m=0,\\
0,&n+m>0.
\end{cases}
$$
Man verschiebt durch partielle Integration Ableitungen von der höheren zur niedrigeren Ordnung, bis das Produkt proportional zu $f^{(n+m)}f^{(n+m+1)}$ ist. Für $n+m>0$ verschwindet dessen Randquadrat. Für $n=m=0$ liefert $f^2/2$ die angegebene Differenz. Daraus folgt für die Plateauverschiebungen $u_*,w_*$ exakt in quadratischer Ordnung
$$
\int\mathbf F\,dt=\tfrac12\bigl[\sigma(u_*)u_*+c\,\sigma(w_*)w_*\bigr].
$$
Mit $w_*=-u_*/c$ bleibt
$$
\delta e_{\rm int}=\frac{1+1/c}{2}
\nabla\cdot\bigl[\sigma(u_*)u_*\bigr].
$$
Die Endverteilung ist in dieser Ansteuerklasse unabhängig von der Länge und Form der Rampe. Langsameres Schalten allein ändert daher diesen statischen Term nicht. Andere zeitlich unabhängige Stellgrößen oder ein räumlicher Speicherfluss können die Aussage ändern.

## Direkte Quadrupolmomente

Sei $Q=z^2-r_\perp^2/2$ mit $\Delta Q=0$. Für die longitudinale Plateauverschiebung $u_*=\nabla\varphi$ und isotrope Lamé-Koeffizienten $\lambda,\mu$ gilt
$$
\sigma(u_*)u_*=\mu\nabla |u_*|^2+\lambda\,u_*\,\nabla\cdot u_* .
$$
Der erste Term trägt durch partielle Integration kein harmonisches Moment. Für den zweiten Term ergibt die Integration von $\nabla\cdot[(\nabla Q\cdot u_*)u_*-|u_*|^2\nabla Q/2]$ die Identität $\int (\nabla Q\cdot u_*)\nabla\cdot u_*=-\int u_*^{\mathsf T}(\nabla^2 Q)u_*$. Also
$$
\int Q\,\delta e_{\rm int}\,d^3x
=\frac{1+1/c}{2}\lambda
\int \bigl(2u_{*,z}^2-|u_{*,\perp}|^2\bigr)\,d^3x.
$$
Der monopolfreie Reservoirabgleich liefert damit im Allgemeinen einen Quadrupol. Derselbe Ausdruck mit linearem $Q$ hat wegen der verschwindenden Hesse-Matrix keinen Dipol. Ist $\lambda=0$, reduziert sich der interne Energiebeitrag für longitudinale Verschiebungen sogar auf eine volle Laplace-Ableitung. Dann verschwinden seine gesamten äußeren Newton-Multipole. Die transportierte Restmasse bleibt davon gesondert.

Für den direkten Transport einer konstanten Referenzmasse ist die quadratische Entwicklung der Dichte des ersten Materials
$$
\delta\rho_1^{(2)}=-\rho_1\nabla\cdot u_2
+\tfrac12\rho_1\partial_i\partial_j(u_{*,i}u_{*,j}),
$$
wenn die Verschiebung als $\epsilon u_*+\epsilon^2u_2$ geschrieben wird. Diese Identität folgt durch Testen der Massenerhaltung an $Q(x+\epsilon u_*+\epsilon^2u_2)$. In der kinematischen Kontrolle $u_2=w_2=0$ trägt die Summe der beiden Restmassenverteilungen deshalb
$$
\int Q\,\delta\rho_{\rm rest}^{(2)}\,d^3x
=\frac{\rho_1+\rho_2/c^2}{2}
\int \bigl(2u_{*,z}^2-|u_{*,\perp}|^2\bigr)\,d^3x .
$$
Der Monopol bleibt durch Massenerhaltung null. Der quadratische Transportterm allein hat auch keinen Dipol. Die Vorgabe $u_2=w_2=0$ ist ein kinematischer Vergleich. Die tatsächliche Mechanik zweiter Ordnung kann weitere Verschiebungen erzwingen.

Für die langgestreckte Profilfamilie mit Längsfunktion $p(z/L)$ und festem Querprofil dominiert die transversale Komponente für hinreichend großes $L$. Der longitudinale Plateauoperator auf dem Skalarpotential ist konstantkoeffizientig und enthält nur gerade Längsableitungen. Sein führender transversaler Term ist für das kompakte nichttriviale Querprofil ungleich null. Mit dem reskalierten $z/L$ beträgt daher $\|u_{*,\perp}\|_2^2$ in führender Ordnung $L C_\perp$ mit $C_\perp>0$, während $\|u_{*,z}\|_2^2=O(L^{-1})$. Bei $\lambda\ge0$ addieren sich dadurch in der kinematischen Kontrolle der Restmassenterm und der interne Energiebeitrag zu einem negativen direkten Quadrupol. Unbekannte zweite Verschiebungen, Spannungen und die vollständige relativistische gravitative Quelle sind in diesem Vorzeichenbefund unbestimmt.

Ein Speicher mit einem eigenen Fluss $\mathbf j_{\rm res}$ hätte auf dem Plateau stattdessen die interne Energieänderung $\nabla\cdot\int(\mathbf F-\mathbf j_{\rm res})dt$. Für eine punktweise Kompensation dieses internen Terms genügt der örtliche Abgleich der beiden integrierten Flüsse. Der Restmassentransport und die Spannungsbilanz brauchen daneben eigene Bedingungen. Der vollständige äußere Gravitationsbeitrag zweiter Ordnung lässt sich aus der direkten Energiedichte allein nicht bestimmen. Er benötigt insbesondere die materiellen Spannungen, die Energieversorgung, mögliche zweite Verschiebungen und die gewöhnliche Gravitation jenseits der bisher verwendeten linearen Bilanz. Die native Higgs–OP5-Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_feder_reservoirbilanz.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_feder_reservoirbilanz.txt) · [Laufmanifest](op5_j_feder_reservoirbilanz.json)

Wolfram prüfte die Leistungsidentität, 25 Rampenintegrale einer exakten polynomiellen Kontrollrampe, die Identität des longitudinalen Spannungsflusses und den quadratischen Dichtetransport. Die allgemeine Rampenformel folgt aus der partiellen Integration. Lokal reproduzierbar im Notizordner mit `wolframscript -file op5_j_feder_reservoirbilanz.wl`. Ausgeführt wurde der Wolfram-Kernel über den Connector. Qiskit wurde erwogen. Die Rechnung enthält klassische Kontinuumsgrößen und keine definierten Quantenschaltungen.
