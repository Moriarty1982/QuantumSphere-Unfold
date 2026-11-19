# OP5: Beobachtbare Streuung der skalaren J-Feldantwort

19. November 2026. Analytische Erkundung in M. Der [Gravitationsabgleich](OP5_J_Gravitationsabgleich.md) setzt voraus, dass der J-Feldkoeffizient $\chi=Z-1$ räumlich rekonstruiert werden kann. Die [Ensemblewirkung](OP5_J_Ensembleantwort.md) gibt die Feldgleichung $\nabla_\mu(ZF_J^{\mu\nu})=0$ in einem quellenfreien Messgebiet vor. Wir leiten die geometrisch-optische Antwort und die lineare Streuamplitude daraus her. Die Rechnung gilt für ein masseloses J-Feld, eine fest vorgegebene Geometrie und den skalaren Maxwell-Koeffizienten. Eigenständige elektrische und magnetische Antwortoperatoren, Absorption und sichtbare Quellen entlang des Ausbreitungswegs sind nicht Teil dieser Näherung.

## Kein zusätzlicher Brechungsindex im geometrisch-optischen Grenzfall

Setzt man eine rasch variierende Phase $\varphi$ und eine langsam variierende transversale Amplitude mit Betrag $\mathcal A$ an, folgt mit $k_\mu=\nabla_\mu\varphi$ in führender geometrisch-optischer Ordnung $k^\mu k_\mu=0$ für $Z>0$. Der Faktor $Z$ kürzt sich aus dem Hauptsymbol. Da $k$ der Gradient der Phase ist, gilt $k^\mu\nabla_\mu k_\nu=0$. Die transversale Amplitudentransportgleichung ist
$$
\nabla_\mu(Z|\mathcal A|^2 k^\mu)=0.
$$
Sie folgt aus der nächsten Ordnung der Maxwell-Gleichung oder durch den Ansatz mit kanonischer Amplitude $\sqrt{Z}\mathcal A$. Relativ zu einem Strahlbündel derselben Geometrie und denselben anfänglichen Bedingungen ändert sich die Feldamplitude um $\sqrt{Z_{\rm in}/Z_{\rm out}}$. Haben beide Endpunkte denselben Wert von $Z$, verschwindet dieser reine geometrisch-optische Amplitudenfaktor. Es gibt in dieser Ordnung keine zusätzliche Phase proportional zu einem Linienintegral von $\chi$. Höhere Wellenordnungen, Beugung, Grenzflächen und Wirkungen auf die Kalibrierung von Quelle und Empfänger sind separate Beiträge. [Hees, Minazzoli und Larena, geometrische Optik bei multiplikativer Feldkopplung](https://arxiv.org/abs/1406.6187)

## Born-Streuung an einer stationären Inhomogenität

In flachem M sei $Z=1+\chi(\mathbf x)$ mit kleiner statischer $\chi$ und Vakuum außerhalb einer endlichen Probe. Arbeite in Einheiten $c=1$ mit Zeitfaktor $e^{-i\omega t}$. Elektrische und magnetische Feldgleichungen liefern
$$
\nabla\times(Z\nabla\times\mathbf E)-\omega^2 Z\mathbf E=0.
$$
Seien $\mathbf k_i,\mathbf k_s$ einlaufender und gestreuter Wellenvektor, beide von Betrag $k=\omega$, und $\mathbf q=\mathbf k_s-\mathbf k_i$. Normiere die einlaufende elektrische Welle auf Einheitsamplitude und bezeichne ihre Polarisation und die ausgewählte Ausgangspolarisation mit $\boldsymbol\epsilon_i$ und $\boldsymbol\epsilon_s$. In erster Born-Ordnung wird im Quellterm $-\nabla\times(\chi\nabla\times\mathbf E)+k^2\chi\mathbf E$ das Einfallfeld eingesetzt. Projektion auf die transversale Ausgangswelle und der auslaufende Green-Kern $e^{ikr}/(4\pi r)$ ergeben als Koeffizient der Kugelwelle
$$
f_{si}(\mathbf q)=\frac{\widetilde\chi(\mathbf q)}{4\pi}\left[
k^2\boldsymbol\epsilon_s^*\cdot\boldsymbol\epsilon_i
-(\mathbf k_s\times\boldsymbol\epsilon_s^*)\cdot(\mathbf k_i\times\boldsymbol\epsilon_i)
\right],
$$
mit $\widetilde\chi(\mathbf q)=\int d^3x\,e^{-i\mathbf q\cdot\mathbf x}\chi(\mathbf x)$. Die beiden Terme stammen aus dem elektrischen bzw. magnetischen Anteil desselben Skalars. Für lineare Polarisationen in und senkrecht zur Streuebene ist die Polarisationsmatrix diagonal mit Einträgen $-k^2(1-\cos\theta)$ und $+k^2(1-\cos\theta)$. Die Identität wurde für vier Winkel durch direkte Auswertung der Kreuzprodukte kontrolliert.

Da $q^2=2k^2(1-\cos\theta)$, verschwindet die lineare Vorwärtsamplitude. Bei Summation über die Ausgangspolarisation und Mittelung der Eingangspolarisation ergibt sich
$$
\frac{d\sigma}{d\Omega}=\frac{q^4}{64\pi^2}|\widetilde\chi(\mathbf q)|^2
$$
in führender Intensitätsordnung. Kleine Winkel werden damit für eine feste endliche Probe unterdrückt. Dieser Befund sagt nichts über den Imaginärteil der Vorwärtsamplitude in höherer Born-Ordnung bei tatsächlich vorhandener Streuung. Er setzt außerdem die gleiche skalare Normierung der elektrischen und magnetischen Terme voraus.

## Information über den Mittelwert und das Kreuzspektrum

Der kohärente komplexe Ausgang enthält für $q\ne0$ einen bekannten Faktor mal $\widetilde\chi(\mathbf q)$, vorausgesetzt das J-Einfallfeld und die Polarisation sind phasenkalibriert. In einem kontrollierten Versuchsaufbau mit geeigneten Einfallsrichtungen könnte dies die benötigten räumlichen Modi liefern. Die Feldphase wird in diesem Vergleich als Messinformation vorausgesetzt. Die bloße Intensität liefert nur $|\widetilde\chi|^2$ und verliert Vorzeichen und räumliche Fourierphase. Sie reicht deshalb für das lineare Kreuzspektrum $P_{\chi\rho_G}$ aus dem [Gravitationsabgleich](OP5_J_Gravitationsabgleich.md) im Allgemeinen nicht aus. Bei stationärer Statistik auf einem großen gemeinsam gefilterten Volumen wäre die mittlere diffuse Intensität hingegen ein Kanal zu $P_{\chi\chi}$, nach Berücksichtigung des Faktors $q^4$ und des Beobachtungsfensters.

Der räumlich konstante Anteil wird durch die exakte Vorwärtsauslöschung dieser linearen Messgröße nicht bestimmt. Ein endliches Objekt mit bekanntem Rand kann auch aus einem konstanten inneren Koeffizienten Beugung erzeugen. Eine separate Mittelwertkalibrierung wäre etwa im idealisierten homogenen Gebiet mit einer Quelle bekannter physikalischer J-Ladung $Q$ denkbar: Die modifizierte Gauß-Gleichung gibt bei Kugelsymmetrie $E_r=Q/(4\pi Zr^2)$. Dazu müssten sowohl $Q$ als auch die Feldmessung gegen die Vakuumnormierung kalibriert sein. Keines dieser Messmittel folgt aus dem bisher betrachteten OP5-Sektor.

Die Rechnung zeigt, welche Wellenobservablen das mathematische Dichteverfahren benötigen würde. Ein beobachtbares J-Signal, eine reale Messgeometrie samt Empfindlichkeit und die kosmologische Normierung bleiben offen. H96 wird dadurch nicht geprüft.
