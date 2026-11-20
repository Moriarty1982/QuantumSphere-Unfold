# OP5 – W2-Dichteantrieb und sein gravitativer Begleitterm

20. November 2026. Analytische Erkundung im Materieframe M. Die [vorzeichenfähige Profilquelle](OP5_J_Signierter_Profilantrieb.md) setzte eine zusätzliche lineare Kopplung an einen Aktor an. Hier wird geprüft, welche lineare Materiequelle schon in W1 oder W2 vorhanden ist und welchen eigenen Energie-Impuls-Beitrag sie mitbringt.

## Vorwissen geprüft

[W1](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) enthält Einstein–Cartan-, Weyl- und abelsche Eichterme. Die Torsionselimination ergibt die [Quadratik des Gesamtstroms](W1_Strom.md). [W2](../v4_10_0_r82/Wirkung_W2_Higgs.md) ergänzt Higgs-Dublett und Yukawa-Terme. Die [radiale W2-Quelle](W2_Higgsquelle.md) liest die massengewichtete Besetzungssumme und ist unter Ladungskonjugation gerade. Das [Higgsportal](Higgsportal.md) behandelt zusätzliche Singulett-Kopplungen. Der [Quellenabgleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Differenzphase_Quellenerhaltung.md) verlangt die Bilanz aller am Impulsaustausch beteiligten Felder. Die lokale Suche nach Dichtegradient, Dehnung und Higgs-Kopplung ergab im jüngsten Zweig noch keine Rückführung des schaltbaren Profils auf ein materielles Dichtefeld. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt dies bei der lokalen OP5-Auslese. I3 und die Kondensationsidee I4 benötigen ein eigenes dynamisches Modell für den kosmologischen Zusammenhang.

## Was die vorhandenen Wirkungen koppeln

W1 hat im geprüften Wirkungsansatz kein unabhängiges radiales Skalarfeld, an das ein Materialaktor so ankoppeln könnte. Die Eichkopplung liest den Vektorstrom. Die Torsionsquadratik liefert bei Änderung eines Referenzstroms eine lineare Variation des Terms, aber keinen eigenen propagierenden Aktorskalar. Eine Identifikation des OP5-Vergleichsfelds damit würde eine zusätzliche Dynamik voraussetzen.

W2 enthält dagegen einen tatsächlich vorhandenen lokalen Operator. Bei festen Higgswinkeln sei $h_{\rm W}=|\Phi|=v+\eta$, $v>0$, in der Normierung $m_i(h_{\rm W})=y_i h_{\rm W}$. Der radiale Yukawa-Term ist $-h_{\rm W}\sum_i y_i\bar\psi_i\psi_i$. Für nichtrelativistische Dirac-Besetzungen mit vernachlässigter kinetischer und innerer Bindungsenergie ergibt die restmassendominierte Materiereduktion
$$
\epsilon_{\rm mat}(h_{\rm W},n_i)=h_{\rm W}\sum_i y_i n_i,\qquad
\mathcal J_h=-\partial_{h_{\rm W}}\epsilon_{\rm mat}=-\sum_i y_i n_i .
$$
Hier bezeichnet $n_i$ die Gesamtbesetzung der Art, einschließlich beider Ladungsvorzeichen, sofern beide besetzt sind. $\mathcal J_h$ bezeichnet die Quelle des Higgsradius und ist vom elektrischen oder J-Eichstrom zu unterscheiden.

Bei festgehaltenem Referenzradius ist $\delta\mathcal J_h=-\sum_i y_i\,\delta n_i$. Für eine gemeinsame kleine Materialverschiebung $\mathbf u$ bei homogener Referenzdichte folgt aus Teilchenzahlerhaltung $\delta n_i=-n_{i0}\nabla\cdot\mathbf u$. Damit ist
$$
\delta\mathcal J_h=\left(\sum_i y_i n_{i0}\right)\nabla\cdot\mathbf u .
$$
Der lineare gemischte Term der lokalen Wirkung ist entsprechend $+\eta(\sum_i y_i n_{i0})\,\nabla\cdot\mathbf u$. Kompression und Verdünnung um eine positive Referenzdichte liefern entgegengesetzte Störungen der Higgsquelle. Eine volumenbewahrende Scherung und eine Umpolung der Besetzung bei fester Summe geben in dieser Reduktion keinen linearen Dichteantrieb. Das ist die gesuchte **vorzeichenfähige Materialvariation** für den Higgsradius unter den genannten Annahmen. Die Wirkungen geben keine Identität zwischen $h_{\rm W}$ und dem gerichteten OP5-Vergleichsskalar vor.

Für eine einzelne Art mit $y n_0>0$ kann eine radial glatte Zielquelle $j(r,z)$ mit $\int_0^\infty r\,j(r,z)\,dr=0$ in jeder Querebene durch
$$
u_r(r,z)=\frac{1}{y n_0 r}\int_0^r r' j(r',z)\,dr',\qquad u_z=0
$$
kinematisch erreicht werden. Die Lösung ist am Ursprung regulär und außerhalb des radialen Trägers null. Die Momentenbedingung gilt für die Antriebsdifferenz des [querausgeglichenen Nullprofils](OP5_J_Gleicher_Messweg_Nullprofil.md), weil sein Querintegral bei jedem $z$ verschwindet und der Antriebsoperator konstantkoeffizientig ist. Das ist eine Lösung für Teilchenzahl und Quelle, keine elastische Gleichgewichtslösung ohne Halterungen. Sie setzt kleine Verschiebungen, unabhängige Ansteuerung und eine geeignete Materialreferenz voraus.

## Materielle Energiedichte und Impulsbilanz

Für eine lokale Energie $\epsilon(h_{\rm W},n)$ bei festgehaltener Entropie pro Teilchen ist der isotrope Druck $p_{\rm mat}=n\partial_n\epsilon-\epsilon$. Seine Higgsvariation ist $n\partial_n\partial_{h_{\rm W}}\epsilon-\partial_{h_{\rm W}}\epsilon$. In der reinen Ruhemasse-Näherung verschwindet der Druck. Das direkte Dichtesignal in der materiellen Energie erfüllt bei festem $v$
$$
\delta\epsilon_{\rm mat}\big|_{v}=v\sum_i y_i\delta n_i=-v\,\delta\mathcal J_h .
$$
Bei verändertem Radius kommt der Term $(\sum_i y_i n_{i0})\eta$ hinzu. Eine reine Umverteilung der Arten kann daher in der Restmassen-Näherung nicht punktweise die direkte Energiedichte festhalten und zugleich den Higgsantrieb ändern. Kinetische, elastische und Bindungsenergien haben eigene Koeffizienten.

Mit der Stresskonvention $T_{\mu\nu}=-2\,\delta S_{\rm mat}/(\sqrt{-g}\,\delta g^{\mu\nu})$ und Signatur $(-,+,+,+)$ liefert die Variation unter Diffeomorphismen für die Materie allein auf ihren Gleichungen $\nabla_\mu T^\mu{}_\nu=\mathcal J_h\partial_\nu h_{\rm W}$, sofern nur der Higgsradius als externer Hintergrund wirkt. In einem materiellen Antrieb gehören zusätzlich die Eichkräfte und die Halterungskräfte in die Bilanz. Die gemeinsame Wirkung muss die Gegenbeiträge der beteiligten Sektoren mitführen. Der direkte Restmassenbeitrag allein ist deshalb ein bestimmter Teil der Quelle und keine abschließende Aussage über den gesamten Stress.

## Der bisherige Profilwechsel hat einen gewöhnlichen Quadrupol

Setze für den aus der Vorarbeit übernommenen Profilwechsel $\delta H=-A_H a\,p(z)\chi(s)(s^2-\kappa s^3)$ mit $s=r^2/R^2$, $M_j=\int_0^\infty s^j\chi(s)\,ds$ und $\kappa=M_2/M_3$. Bezeichne das harmonische Polynom $Q_2=z^2-r^2/2$. Für den statischen Antriebsoperator $P_0/m^2$ aus der [signierten Profilquelle](OP5_J_Signierter_Profilantrieb.md) gilt
$$
\int Q_2\,\delta J\,d^3x=Z\Omega_0^2\int Q_2\,\delta H\,d^3x,\qquad
\delta J=P_0\delta H/m^2.
$$
Partielle Integration schiebt den Operator auf $Q_2$. Dort verschwinden der volle Laplace-Operator und der transversale Bi-Laplace-Operator, sodass nur der konstante Term übrig bleibt. Durch das kompensierte Querintegral verschwindet der $z^2$-Anteil. Der verbleibende Anteil ist
$$
\int Q_2\,\delta H\,d^3x
=\frac{\pi A_H a R^4}{2}\left(\int p(z)\,dz\right)
\frac{M_3^2-M_2M_4}{M_3}.
$$
Für glattes $\chi\ge0$ mit nichttrivialem radialem Träger gilt $M_3^2<M_2M_4$ nach striktem Cauchy–Schwarz für die Funktionen $s,s^2$ im Maß $\chi(s)\,ds$. Das Moment ist daher für den verwendeten Profilwechsel ungleich null.

Wird der Zielantrieb $\delta J$ mit der direkten W2-Quelle $\delta\mathcal J_h$ identifiziert, erbt $\delta\epsilon_{\rm mat}|_v=-v\,\delta J$ diesen Quadrupol. Wegen der axialen Symmetrie und des pro Querebene verschwindenden Gesamtmassenwechsels hat der direkte Dichteanteil weder Monopol noch Dipol. In der schwachen statischen gewöhnlichen Gravitation trägt der Quadrupol auf der entfernten Achse einen Potentialterm proportional zu $L_{\rm obs}^{-3}$ bei. Der Term zweiter Ordnung in der Entwicklung des Newton-Kerns bei großer Beobachterdistanz $L_{\rm obs}$ ist $Q_2/L_{\rm obs}^3$. Zusätzlich zur Kompaktheit des OP5-Vergleichshintergrunds müsste die gewöhnliche Gravitationsänderung der Quelle geprüft werden. Eine Halterung, ein weiterer Energiebeitrag oder ein geändertes Profil könnte den direkten Quadrupol kompensieren. Die Summe wurde hier nicht berechnet. Ein gemeinsamer Gravitationsbeitrag kann zudem aus einer idealen Differenzauslese herausfallen. Ob er die realen Endpunkte gegeneinander verschiebt, erfordert eine eigene Empfindlichkeitsrechnung.

Damit liefert W2 eine kompressionsabhängige lineare Higgsquelle und eine verpflichtende materielle Begleitbilanz. Die gerichtete OP5-Kopplung, ein realisierter Antrieb mit bilanzierten Halterungen, freie J-Ausbreitung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_w2_dichteantrieb.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_w2_dichteantrieb.txt) · [Laufmanifest](op5_j_w2_dichteantrieb.json)

Wolfram prüfte die Quell- und Druckvariation, die radiale Divergenzlösung und die Wirkung des statischen Antriebspolynoms auf den harmonischen Quadrupol symbolisch. Die scharfe Scheibe im Skript prüft nur die Vorzeichenrechnung der Momentenformel. Die Konstruktion und die Ungleichung gelten für den glatten Zuschnitt. Im Notizordner reproduzierbar mit `wolframscript -file op5_j_w2_dichteantrieb.wl`. Ausgeführt wurde der Wolfram-Kernel über den Connector. Qiskit wurde erwogen. Für diese statische Quellen- und Momentenrechnung ist kein Quantenschaltkreis definiert.
