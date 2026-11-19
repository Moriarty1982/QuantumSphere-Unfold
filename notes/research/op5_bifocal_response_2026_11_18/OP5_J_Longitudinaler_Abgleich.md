# OP5: Longitudinaler Abgleich bei ungleichen sichtbaren Kopplungen

20. November 2026. Analytische Erkundung in M. Die [konservierte Quellenrechnung](OP5_J_Differenzphase_Quellenerhaltung.md) gibt J und gewöhnlichem Licht dasselbe Gewicht, wenn beide Impuls mit derselben geladenen Materie austauschen. Hier lassen wir verschiedene sichtbare Gewichte in der linearen Fierz–Pauli-Theorie zu und behalten die impulsabhängigen Terme ihres Propagators. Der vollständige D-Tensor wird in nullter Ordnung als erhalten vorausgesetzt. Es gibt keinen nichtlinearen Stabilitätsnachweis und keinen H96-Datenvergleich.

## Gemischter Austausch mit einer konservierten Seite

Wir verwenden Signatur $(-,+,+,+)$ und einen kanonisch normierten massiven Tensor mit Masse $m>0$. Sei $S^{\mu\nu}=g_JT_J^{\mu\nu}+g_AT_A^{\mu\nu}+g_OT_O^{\mu\nu}$ die sichtbare gewichtete Quelle und $g_D T_D^{\mu\nu}$ die zweite Quelle. Setze $q_\mu T_D^{\mu\nu}=0$ in der Fourier-Transformation des ungestörten D-Sektors. Für den linearen Fierz–Pauli-Propagator definiere $\bar\eta_{\mu\nu}=\eta_{\mu\nu}+q_\mu q_\nu/m^2$. Der Zähler ist die symmetrisierte Zweifachkontraktion von $\bar\eta$ minus $\bar\eta_{\mu\nu}\bar\eta_{\alpha\beta}/3$. [Hinterbichler, Fierz–Pauli-Propagator, Gl. (2.44)](https://arxiv.org/abs/1105.3735)

Beim Kontrahieren mit der konservierten D-Seite verschwinden die Impulsterme aus der symmetrisierten Zweifachkontraktion. Aus der Spurprojektion bleibt auf der sichtbaren Seite jedoch ein Term übrig. Mit $S=\eta_{\mu\nu}S^{\mu\nu}$ und $T_D=\eta_{\mu\nu}T_D^{\mu\nu}$ lautet der gemischte Austausch in der Vorzeichenkonvention des [Baumabgleichs](OP5_J_Massiver_Tensorvermittler.md)
$$
\frac{g_D}{q^2+m^2}
\left[
S^{\mu\nu}T^D_{\mu\nu}
-\frac13 S T_D
-\frac{1}{3m^2}(q_\mu q_\nu S^{\mu\nu})T_D
\right].
$$
Das Polrezept ist in dieser Schreibweise weggelassen. Die Identität wurde mit einem nichtkonservierten sichtbaren Tensor und einem konservierten D-Tensor an drei Impulsen gegen die vollständige Kontraktion kontrolliert. Sie sagt nichts über den sichtbaren Eigenoperator aus, bei dem keine der beiden gewichteten Quellen konserviert sein muss. Auch ist das Verschwinden der genannten Impulsterme keine Zählung erzeugbarer physischer Helizitäten.

## Ableitungsglied und Quellregionen

Für $|q^2|\ll m^2$ ergibt die Rücktransformation des letzten Terms als führendes rein longitudinales gemischtes Kontaktglied
$$
\Delta\mathcal L_{\rm long,\,mix}
=\frac{g_D}{3m^4}(\partial_\mu\partial_\nu S^{\mu\nu})T_D
=\frac{g_D}{3m^4} S^{\mu\nu}\partial_\mu\partial_\nu T_D
$$
bis auf eine totale Ableitung. Dabei gilt $\partial_\mu\mapsto iq_\mu$. Die gewöhnliche Entwicklung des Propagatornenners erzeugt daneben weitere Ableitungskorrekturen aus den ersten beiden Termen. Der neu ausgewiesene Term ist an die Spur des vollständigen D-Tensors gebunden. Für einen stationären drucklosen D-Hintergrund in diesem Frame ist $T_D=-\rho_D$. Das longitudinale Kontaktglied spricht in der zweiten Form auf zweite räumliche Ableitungen dieser Dichte an. Bei konstantem Hintergrund verschwindet es im Inneren; es ist keine Korrektur proportional zur Massensäule. Für die genaue endliche Reichweite ersetzt der Propagator die lokale Spur durch ihre gefaltete Verteilung.

Aus der vorigen Impulsbilanz ist
$$
\partial_\mu S^{\mu\nu}
=(g_O-g_J)F_J^{\nu\lambda}j_{J,\lambda}
+(g_O-g_A)F_A^{\nu\lambda}j_{A,\lambda}.
$$
In einer geladenen Quell- oder Detektorregion bestimmt die Divergenz dieser Kraftdichten den gemischten longitudinalen Beitrag. Er hängt dort von der Materiedynamik sowie dem D-Hintergrund ab. Die Abschätzung als kleine Ableitungskorrektur setzt voraus, dass die tatsächlich vorkommenden Impulsüberträge niedrig gegenüber $m$ sind. Sie folgt nicht aus der Frequenz des ankommenden Strahls allein.

## Freie Wellen und die differentielle Laufzeit

Für ein Matrixelement des freien Maxwell-Tensors zwischen ungestörten physikalischen Wellen gilt $q_\mu T_I^{\mu\nu}=0$ und $T_I=0$ für $I=J,A$, auch wenn der jeweilige konstante Faktor $g_I$ verschieden ist. Hier ist $q$ der Austauschimpuls. Darum bleiben im gemischten freien Ausbreitungsgebiet zur ersten Ordnung nur die transversalen Kontraktionen. In der langsam veränderlichen, ruhenden D-Näherung lautet die differentielle Laufphase pro Frequenz relativ zur selben Vakuumgeometrie
$$
\frac{\Delta\varphi_J}{\omega_J}-\frac{\Delta\varphi_A}{\omega_A}
=\frac{(g_J-g_A)g_D}{m^2}\int \rho_D\,d\ell .
$$
Das ist die Differenz des führenden Kontaktterms bei vorgegebenen nichtuniversellen Gewichten. Die Rechnung liefert keinen zusätzlichen longitudinalen Massensäulen-Term. Sie setzt die bei ausgeschaltetem Vermittler quellfreien Wellen und dieselbe ungestörte Bahn voraus; die Änderungen der Wellen aufgrund der Kopplung werden erst in höherer Ordnung wieder in den Austausch eingesetzt.

Damit können ungleiche Gewichte lokal eine differentielle Phase ergeben. Ein experimenteller Vergleich müsste dieselben Kopplungen in geladenen Quellen und Detektoren einsetzen und dabei auch die sichtbare Eigenwechselwirkung und die Gültigkeitsgrenze des linearen Modells prüfen. Eine Ableitung der Gewichte aus W1/W2 und ein H96-Datenvergleich bleiben offen.
