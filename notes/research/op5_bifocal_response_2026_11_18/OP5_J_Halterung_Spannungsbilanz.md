# OP5 – Statische Spannungsbilanz mit elastischem Gegenkörper

20. November 2026. Analytische Erkundung im Materieframe M. Die [Quadrupolkompensation](OP5_J_Quadrupol_Kompensation.md) hält den direkten Newton-Beitrag der Restmassenänderung kompakt. Jetzt wird ein explizites lineares Modell mit einem elastischen Gegenkörper und inneren Haltekräften geprüft. Betrachtet werden statische Plateaus, kleine Verschiebungen, feste Higgs-Referenz $v$ und eine spannungsfreie Ausgangskonfiguration.

## Vorwissen geprüft

Der [W2-Dichteantrieb](OP5_J_W2_Dichteantrieb.md) gibt die lineare Yukawa-Quelle und die direkte Begleitdichte. Der [elastische Quellenabgleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/842f3a0365bdabd04cc45de4a8e12f4454314d9f/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Elastischer_Quellenabgleich.md) realisiert einen anderen vorgegebenen Tensor mit aktiver Eigenverformung und führt die Arbeit des Antriebs mit. Hier wird rückwärts von den für das Laplace-Profil erforderlichen Stoffverschiebungen auf die stationäre Impulsbilanz geschlossen. Die lokale Suche nach Gegenkörper und Halterung ergab in diesem Zweig bisher keine selbst bilanzierte Zweikomponenten-Referenz. Die Frage gehört zur lokalen OP5-Auslese im [Gesamtbild](../../../wiki/Gesamtbild.md). I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Statisches Materialmodell

Zwei homogen idealisierte, am selben Ort beschriebene elastische Kontinua haben Verschiebungen $u,w$ und positive Referenzruhedichten $\rho_1,\rho_2$. Für die erste Komponente sei $\sigma_1=\mathsf C\varepsilon(u)$ mit $\varepsilon(u)=\operatorname{sym}\nabla u$ und einer positiven, konstanten isotropen Steifigkeit $\mathsf C$. Die zweite Komponente habe $\sigma_2=c\,\mathsf C\varepsilon(w)$ für $c>0$. Eine lokale Verbindung mit Steifigkeit $k>0$ hat die Energiedichte $k|u-w-d|^2/2$. Die vorgegebene Vektorgröße $d$ ist die relative Ruhelage der Verbindung, die im Referenzzustand null ist. Der Antrieb wird durch Änderung dieser Ruhelage modelliert.

Die statischen Gleichungen lauten
$$
0=\nabla\cdot\sigma_1-k(u-w-d),\qquad
0=\nabla\cdot\sigma_2+k(u-w-d).
$$
Für eine glatte kompakte Zielverschiebung $u$ liefert
$$
w=-u/c,\qquad
d=(1+1/c)u-\frac{\nabla\cdot\sigma_1}{k}
$$
eine Lösung. Die Verbindung trägt die nötigen entgegengesetzten inneren Kräfte, und $\sigma_2=-\sigma_1$ punktweise. Die gewählte Ruhelage ist kompakt. Auf dem Plateau gilt in erster Ordnung mit der Konvention des elastischen Quellenabgleichs
$$
\delta T^{00}_{\rm mech}=-\rho_1\nabla\cdot u-\rho_2\nabla\cdot w,\qquad
\delta T^{0i}_{\rm mech}=0,\qquad
\delta T^{ij}_{\rm mech}=-(\sigma_{1,ij}+\sigma_{2,ij})=0.
$$
Dieser statische lineare Tensor ist erhalten. Die Verbindung ist im Ausgangszustand unbelastet und trägt zu Energie und zum eigenen metrischen Stress der quadratischen Referenz erst ab zweiter Ordnung bei. Die Gleichungen setzen einen Antrieb voraus, dessen sonstige Materialparameter und Ruheenergie beim Verstellen von $d$ in erster Ordnung festgehalten werden. Separate Hilfsfelder oder eine reale räumliche Trennung der beiden Kontinua sind zusätzliche Modelländerungen.

## Halterung und Higgsquelle

Bezeichne mit $\gamma_i$ die skalare W2-Quellstärke pro Volumendehnung der Komponente $i$. Dann gilt im vorstehenden Vergleich
$$
\delta\mathcal J_h=\Gamma\nabla\cdot u,\qquad
\delta T^{00}_{\rm mech}=-D_\rho\nabla\cdot u,\qquad
\Gamma=\gamma_1-\gamma_2/c,\quad D_\rho=\rho_1-\rho_2/c.
$$
Im restmassendominierten W2-Ansatz bei festem $v$ ist $\gamma_i=\rho_i/v$. Punktweise Dichtekompensation durch $\rho_2=c\rho_1$ hebt daher auch $\delta\mathcal J_h$ auf. Ein Gegenkörper mit anderer effektiver Higgsantwort könnte in einem erweiterten Materialmodell $D_\rho=0$ und $\Gamma\ne0$ erlauben. Die reine W2-Restmassen-Näherung stellt diese Freiheit nicht bereit.

Der Abgleich des Außenfelds kann stattdessen durch räumliche Momente erfolgen. Setze $U_0=\mathcal P V$ aus der [Laplace-Konstruktion](OP5_J_Quadrupol_Kompensation.md), sodass der gewünschte Quellenwechsel $\delta J=\Delta U_0$ ist. Da $V$ in jeder Querebene ein verschwindendes Integral hat und $\mathcal P$ konstantkoeffizientig ist, gilt $\int_{\mathbb R^2}U_0\,dx\,dy=0$ für jedes $z$. Für $\Gamma\ne0$ liefert die radiale Wahl
$$
b_r(r,z)=\frac1{\Gamma r}\int_0^r r'\,U_0(r',z)\,dr',\qquad b_z=0
$$
ein glattes kompaktes Vektorfeld mit $\nabla\cdot b=U_0/\Gamma$. Setze $u=\Delta b$. Dann sind $u,w,d$ kompakt und
$$
\delta\mathcal J_h=\Delta U_0,\qquad
\delta T^{00}_{\rm mech}=-\frac{D_\rho}{\Gamma}\Delta U_0 .
$$
Die Spannungsterme der einzelnen Kontinua sind ebenfalls Laplace-Bilder kompakter Tensoren, weil die linearen elastischen Operatoren mit $\Delta$ kommutieren. Die Summe der Spannungen verschwindet in der hier gewählten Halterung sogar punktweise. Damit hat die vollständig bilanzierte **lineare statische Mechanik dieses Modells** einen kompakten Newton-Beitrag einschließlich des materiellen Gegenkörpers. Im reinen W2-Restmassenvergleich ist $D_\rho/\Gamma=v$. Die vorhandene Higgsquelle bleibt im Inneren erhalten. Ihr Anschluss an das gerichtete OP5-Profil bleibt eine bedingte Identifikation.

## Einschalten und gespeicherte Energie

Mit den gleichen Verschiebungsrelationen während einer zeitabhängigen Schaltung liefert die Summe der Bewegungsgleichungen $D_\rho\ddot u=0$. Denn die inneren Kräfte heben sich auf, und der Gesamtstress verschwindet bei $w=-u/c$ identisch. Für $\Gamma\ne0$ im reinen W2-Restmassenansatz ist $D_\rho\ne0$. Ein nichttrivialer Wechsel zwischen zwei ruhenden Zuständen lässt sich daher mit dieser starren Gegenbewegung allein nicht als dynamische Lösung einsetzen. Während des Umschaltens braucht man eine andere Halterungsbewegung, zeitabhängigen Gesamtstress oder einen expliziten zusätzlichen Impulsträger.

Selbst auf dem statischen Plateau speichert die Mechanik gegenüber dem unbelasteten Ausgangspunkt die positive Energie
$$
\Delta E_{\rm elast+Feder}=\int\left[
\frac{1+1/c}{2}\varepsilon(u):\mathsf C\varepsilon(u)
+\frac{|\nabla\cdot\sigma_1|^2}{2k}
\right]\,d^3x.
$$
Für nichttriviales kompaktes $u$ ist sie strikt positiv und quadratisch in der Störungsamplitude. Ihre Gegenbuchung erfordert die Energiequelle der Ruhelagenänderung. Für eine geschlossene ruhende Quelle gilt $\int T^{ij}=0$, wenn $T^{ij}$ erhalten und kompakt ist. Das folgt aus der Integration von $\partial_k(x^i T^{kj})$. Der vollständige gewöhnliche statische Monopol hängt dann von der Gesamtenergie einschließlich Versorgung und Reservoir ab. Der lineare Laplace-Abgleich bestimmt diese zweite Ordnung nicht. Die Beiträge einer realen Halterung, die Einschaltantwort und die native Higgs–OP5-Kopplung bleiben offen. Zu freier J-Ausbreitung und H96 folgt aus dem Materialvergleich kein neuer Befund.

## Rechenkontrolle

[Wolfram-Skript](op5_j_halterung_spannungsbilanz.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_halterung_spannungsbilanz.txt) · [Laufmanifest](op5_j_halterung_spannungsbilanz.json)

Wolfram prüfte beide Kraftbilanzen, die kombinierte Spannung, das gemeinsame Verschwinden von Restmassenänderung und Higgsquelle bei punktweiser Kompensation, die Trägheitssumme, die Federenergie und die Laplace-Kommutatoren symbolisch. Im Notizordner reproduzierbar mit `wolframscript -file op5_j_halterung_spannungsbilanz.wl`. Der tatsächliche Lauf erfolgte im Connector. Qiskit wurde erwogen. Das Prüfobjekt ist klassische Elastostatik mit einer gesonderten linearen Impulsbedingung.
