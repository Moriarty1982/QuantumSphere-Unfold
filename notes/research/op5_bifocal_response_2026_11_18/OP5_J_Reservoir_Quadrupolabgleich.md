# OP5 – Reservoirfluss und Abgleich des direkten Quadrupols

20. November 2026. Analytische Erkundung im Materieframe M. Der [ortsfeste Speicher](OP5_J_Feder_Reservoirbilanz.md) gleicht die gesamte Federarbeit aus. Er hinterlässt bei der langgestreckten Profilfamilie in der kinematischen Vergleichsrechnung einen Quadrupol im direkten Beitrag zu $T^{00}$ zweiter Ordnung. Gesucht ist eine räumliche Kompensation mit eigener Impulsbilanz.

## Vorwissen geprüft

Die [Feder- und Reservoirbilanz](OP5_J_Feder_Reservoirbilanz.md) liefert den elastischen Restfluss und den kinematischen Restmassentransport. Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) erhält den linearen mechanischen Tensor. Die [frühere elastische Quellkonstruktion](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f384c6363c5356aef515a851c989fa943ab818b5/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Elastischer_Quellenabgleich.md) verwendet einen symmetrischen Hilfstensor und eine geformte Eigenverformung. Hier wird diese Konstruktion rückwärts aus dem tatsächlich berechneten Rest der Federroute bestimmt. Die lokale Suche nach Reservoirfluss und Wärmeleitung ergab dafür keine frühere Kompensation. Im [Gesamtbild](../../../wiki/Gesamtbild.md) bleibt der Schritt bei der lokalen OP5-Auslese. I3 erfordert weiterhin eine kosmologische Bestandsdynamik.

## Das Ziel für einen räumlichen Fluss

Sei $u=\nabla\varphi$ die kompakte longitudinale Plateauverschiebung, $w=-u/c$, $\alpha=(1+1/c)/2$ und $B_\rho=\rho_1+\rho_2/c^2$. Für den in der Vorarbeit berechneten Anteil der Energiedichte gilt auf dem Plateau
$$
e_{\rm bek}=\nabla\cdot K,\qquad
K_i=\alpha[\sigma(u)u]_i+\tfrac12 B_\rho\,\partial_j(u_i u_j).
$$
Der erste Summand kommt aus dem elastischen Energiefluss bei gemeinsamem Schaltverlauf und ortsfestem Arbeitsreservoir. Der zweite kommt aus dem direkten quadratischen Restmassentransport. Zweite Materialverschiebungen sind wie in der kinematischen Kontrolle auf null gesetzt. Aktuelle Größen sind die Koeffizienten zweiter Ordnung in der Amplitude der Hauptschaltung.

Ein zusätzlicher Reservoirfluss $j_{\rm R}$ ergibt die Enddichteänderung $-\nabla\cdot J_{\rm R}$ mit $J_{\rm R}=\int j_{\rm R}\,dt$. Für punktweisen Ausgleich der berechneten Dichte genügt $J_{\rm R}=K$. Eine divergenzfreie Änderung am Fluss verändert die Enddichte nicht. Ist nur der Achsenquadrupol $Q=z^2-r_\perp^2/2$ abzugleichen, reicht
$$
\int\nabla Q\cdot J_{\rm R}\,d^3x=-\int Q\,e_{\rm bek}\,d^3x .
$$

Für ein homogenes isotropes Wärmeleitgesetz $j_{\rm R}=-\kappa\nabla\theta$ mit skalarer, räumlich konstanter Leitfähigkeit ist der Beitrag zur Enddichte eine volle Laplace-Ableitung. Ist die zeitintegrierte Temperaturstörung kompakt und verschwindet der Randbeitrag, ist ihr Moment gegen jedes harmonische Polynom null. Daher kann ein solcher Fluss den vorhandenen Quadrupol nicht korrigieren. Das ist eine Einschränkung des Flussansatzes mit diesen Randbedingungen. Für einen konstanten, uniaxialen Leitfähigkeitstensor mit Einträgen $(\kappa_\perp,\kappa_\perp,\kappa_z)$ beträgt der zusätzliche Quadrupol dagegen
$$
2(\kappa_z-\kappa_\perp)\int\Theta\,d^3x,\qquad \Theta(x)=\int\theta(t,x)\,dt .
$$
Eine passend gesteuerte $\Theta$ hätte damit die algebraisch nötige Freiheit für das eine Moment. Die erreichbare Temperaturverteilung, die zugehörigen Quellen und andere Momente sind in dieser Prüfung unbestimmt.

## Elastischer Speicher mit erhaltener Quelle

Für die isotrope Hauptmechanik gilt $\sigma(u)u=\mu\nabla|u|^2+\lambda u\nabla\cdot u$. Da $u$ longitudinal ist, ist $u_i\nabla\cdot u=\partial_j(u_i u_j)-\partial_i|u|^2/2$. Der geforderte Transport ist somit die Divergenz eines symmetrischen kompakten Tensors
$$
A_{ij}=\alpha(\mu-\lambda/2)|u|^2\delta_{ij}
+(\alpha\lambda+B_\rho/2)u_i u_j,\qquad K_i=\partial_j A_{ij}.
$$
Dies bestimmt die Form des Kompensators aus der bereits berechneten Dichte. Für einen glatten Schaltfaktor $g(t)$ von 0 nach 1 mit ruhenden Enden setze
$$
\delta T_{\rm R}^{00}=-g\,\partial_i\partial_j A_{ij},\qquad
\delta T_{\rm R}^{0i}=\dot g\,\partial_j A_{ij},\qquad
\delta T_{\rm R}^{ij}=-\ddot g\,A_{ij}.
$$
Dieser zusätzliche symmetrische Tensor ist identisch erhalten. Die Energiegleichung kürzt $-\dot g\,\partial_i\partial_j A_{ij}$ gegen die Divergenz des Flusses. Die Impulsgleichung kürzt $\ddot g\,\partial_j A_{ij}$ gegen die Divergenz des räumlichen Tensors. Auf dem Plateau hat er weder Fluss noch räumlichen Stress und hebt $e_{\rm bek}$ punktweise auf. Die Kompensation des direkten Beitrags betrifft alle seine statischen Newton-Multipole.

Ein konkretes lineares Materialmodell für diesen Tensor ist eine zusätzliche elastische Komponente mit homogener positiver Referenzdichte $\rho_{\rm R}$ und positiver Steifigkeit $\mathsf C_{\rm R}$. Wähle die Verschiebung $\xi=gK/\rho_{\rm R}$ und den Cauchy-Stress $\sigma_{\rm R}=\ddot g\,A$. Dann erfüllen $\delta\rho_{\rm R}=-\rho_{\rm R}\nabla\cdot\xi$, $\rho_{\rm R}\dot\xi$ und $\rho_{\rm R}\ddot\xi=\nabla\cdot\sigma_{\rm R}$ genau den vorstehenden Tensor. Die kompakte spannungsfreie Eigenverformung
$$
\varepsilon_{\rm R,*}=\operatorname{sym}\nabla\xi-\mathsf C_{\rm R}^{-1}(\ddot g\,A)
$$
realisiert das lineare Materialgesetz. Sie ist eine vorgegebene aktive Stellgröße. Da $\xi$ und die induzierte Dehnung quadratisch in der Amplitude der Hauptmodulation sind, beginnt die kinetische und elastische Energie dieser zusätzlichen spannungsfreien Referenz bei vierter Ordnung. Eine von der Stellgröße abhängige mikroskopische Ruheenergie oder die Quelle ihrer Steuerung wären getrennt mitzuführen.

Auf dem Plateau verschwindet damit die Summe **der beiden berechneten direkten Dichtebeiträge** aus der kinematischen Hauptrechnung und der zusätzlichen Kompensationskomponente. Während des Umschaltens ist der Tensor des Kompensators erhalten. Er kann selbst zu einem retardierten Außenfeld beitragen. Die Rechnung liefert keine gemeinsame gravitative Kompensation für den gesamten Übergang oder für den unbekannten vollständigen Stress zweiter Ordnung. Zweite Bewegungen der Hauptkomponenten, weitere Reservoir- und Materialbeiträge sowie die nichtlineare gewöhnliche Gravitation bleiben offen. Auch die native Higgs–OP5-Kopplung und H96 bleiben gesonderte Fragen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_reservoir_quadrupolabgleich.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_reservoir_quadrupolabgleich.txt) · [Laufmanifest](op5_j_reservoir_quadrupolabgleich.json)

Wolfram prüfte die Zerlegung des direkten Flusses, die Erhaltung des zusätzlichen Tensors und seine elastische Realisierung symbolisch. Der isotrope Leitungsterm hat Quadrupolkoeffizient null, der uniaxiale den Koeffizienten $2(\kappa_z-\kappa_\perp)$. Im Notizordner reproduzierbar mit `wolframscript -file op5_j_reservoir_quadrupolabgleich.wl`. Der tatsächliche Lauf erfolgte im Connector. Qiskit wurde erwogen. Es handelt sich um klassische Kontinuums- und Tensoridentitäten.
