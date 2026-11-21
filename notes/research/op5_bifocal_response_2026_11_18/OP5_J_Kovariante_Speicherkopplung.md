# OP5 – Kovariante Kopplung des Arbeitsspeichers

21. November 2026. Analytische Erkundung im Materieframe M. Eine lokale Wirkung verbindet elastische Matrix, druckfreien Speicher und eine mitbewegte Eigenzeituhr. Die Wirkung ist kovariant formuliert. Die vorbereitete Umschaltlösung und ihre gravitative Quelle werden im flachen Hintergrund bis zur zweiten Ordnung in der Auslenkung $\epsilon$ geprüft. Signatur $(-,+,+,+)$ und Lichtgeschwindigkeit eins.

## Vorwissen geprüft

Die [Umschaltung zwischen den Ruhelagen](OP5_J_Umschaltung_Ruhelagen.md) ergibt die kompakte Sollbahn, die symmetrische Cauchy-Spannung und die retardierte linearisierte Außenkompensation. Der [druckfreie Arbeitsspeicher](OP5_J_Druckfreier_Arbeitsspeicher.md) konkretisiert Teilchenstrom, Ruheenergiewechsel und die notwendigen lokalen Kräfte. Die Suche in Vorab-Notizen, aktuellen Forschungsnotizen und OP5-Analysen nach Materialkoordinaten, Mitnahmekraft und Wechselwirkungsstress ergab dafür keine gemeinsame Wirkung. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 setzt weiterhin eine eigenständige kosmologische Bestandsdynamik voraus.

## Rückwärtsprüfung eines einzigen Massenskalares

Für die Weltlinienwirkung $-\int m\,d\tau$ ist mit $U$ der Trägervierergeschwindigkeit und $\Pi_\mu{}^\nu=\delta_\mu{}^\nu+U_\mu U^\nu$
$$
m a_\mu=-\Pi_\mu{}^\nu\partial_\nu m,\qquad \dot m_\tau=U^\nu\partial_\nu m .
$$
Der Ruheenergieabgleich verlangt auf der Familie der Sollbahnen $m=m_0+O(\epsilon^2)$. Auf einem offenen Teil des Trägers und für eine reguläre Entwicklung mit festen räumlichen Skalen ist deshalb auch $\partial m=O(\epsilon^2)$. Die Mitnahme eines positiven Speicherhintergrunds verlangt dagegen $a_i=\epsilon\ddot s\,\partial_i\varphi+O(\epsilon^2)$. Ein einzelner Massenskalar dieser Familie reicht für beide Aufgaben nicht aus. Der Schluss setzt die bisherige Energieaufteilung und eine reguläre Amplitudenentwicklung voraus.

## Lokale Wirkung

Die Konstruktion gilt für jede der beiden überlagerten Komponenten. Unterdrückt wird deren Index. Sei $X=(X^1,X^2,X^3)$ die Materialabbildung der Matrix und $Z$ die unabhängige Teilchenlabelabbildung des Speichers. Durch Rückzug der jeweiligen Referenzvolumenform entstehen identisch erhaltene Stromdichten $\mathcal J_{\rm M}^\mu$ und $\mathcal J_{\rm R}^\mu$. Sie enthalten keinen Metrikfaktor. Die Matrixreferenzform zählt Referenzvolumen, die Speicherreferenzform Teilchen. Schreibe
$$
\mathcal J_b^\mu=\sqrt{-g}\,n_b U_b^\mu,\qquad
\sqrt{-g}\,n_b=\sqrt{-g_{\mu\nu}\mathcal J_b^\mu\mathcal J_b^\nu},
\quad b\in\{\mathrm M,\mathrm R\}.
$$
Für einen skalaren Eigenzeitparameter $\theta$ und Multiplikator $\lambda$ wähle
$$
\begin{aligned}
S={}&-\int \sqrt{-g}\,[n_{\rm M}(\rho_{\rm M}+W)+n_{\rm R}m(\theta,X)]\,d^4x\\
 &+\int\mathcal J_{\rm R}^\mu A_\mu(\theta,X,d\theta,dX)\,d^4x\\
 &+\int \lambda\,[\mathcal J_{\rm M}^\mu\partial_\mu\theta-\sqrt{-g}\,n_{\rm M}]\,d^4x .
\end{aligned}
$$
$\rho_{\rm M}=\rho-r_0$ ist die Referenzruhedichte der Matrix mit $r_0=n_0m_0$. $W$ ist die elastische Energie pro Referenzvolumen. Die Programmdaten sind Funktionen von Materiallabels und Eigenzeit. Die Raumzeitkoordinate $t$ kommt in der Wirkung nicht als äußere Steuergröße vor. Die Variation von $\lambda$ erzwingt $U_{\rm M}^\mu\partial_\mu\theta=1$. Der Uhrterm hat den Hilbert-Tensor $\lambda n_{\rm M}U_{\rm M}^\mu U_{\rm M}^\nu$. Die 1-Form-Kopplung ist bei festgehaltenen Skalarfeldern und deren Ableitungen metrikunabhängig und hat identisch verschwindenden Hilbert-Tensor. Sie ist ein materieller Kopplungsterm ohne eigenständigen Feldkinetikterm. [Variationsprinzipien für relativistische Fluide, Brown](https://arxiv.org/abs/gr-qc/9304026)

## Konstruktion der Kraft und der elastischen Spannung

Die Speicherbewegung mit Kopplung $+\int A_\mu dx^\mu$ erfüllt
$$
m a_\mu+\Pi_\mu{}^\nu\partial_\nu m=(dA)_{\mu\nu}U^\nu .
$$
Sei $\alpha$ die linke Seite auf der gewünschten Trägerbahn. Sie ist orthogonal zu $U_{\rm R}$. Im aktiven Bereich sind $(\theta,X)$ lokale Koordinaten. Setze $Y=Y(\theta,X)$ als feste Funktion so, dass es auf der gewünschten Trägerbahn das anfängliche Trägerlabel liefert. Das ist eine programmierte Änderung der Materialkoordinaten, unabhängig vom zu variierenden Speicherfeld $Z$. Im Chart $(\theta,Y)$ ist $U_{\rm R}=(U^\theta,0,0,0)$ auf der Sollbahn mit $U^\theta>0$. Wähle
$$
A=C_I(\theta,Y)\,dY^I,\qquad
C_I(\theta,Y)=-\int_{\theta_{\rm vor}}^\theta
       \frac{\alpha_I(\vartheta,Y)}{U^\theta(\vartheta,Y)}\,d\vartheta .
$$
Dann ist $(dA)_{I\theta}U^\theta=\alpha_I$ und die Zeitkomponente im adaptierten Chart null. Das Integral bestimmt die Koeffizienten der später lokalen Wirkung aus der Sollbahn. Es wird bei der Dynamik nicht als nichtlokaler Operator ausgeführt. Das Verfahren liefert die Trägergleichung für die gewünschte Bahn einschließlich des für die Mitnahme nötigen Kraftanteils. Die Ableitungen von $A$ nach den Matrix- und Uhrfeldern bleiben Bestandteil ihrer Variationsgleichungen.

Für die Matrix definiere die inverse Dehnung $B^{AB}=g^{\mu\nu}\partial_\mu X^A\partial_\nu X^B$, $C=B^{-1}$ und die Energie $W=\frac12 E:\mathsf C E$ mit $E=(C-G_*)/2$ und positivem Elastizitätstensor $\mathsf C$. Im flachen Hintergrund mit Matrixabbildung $x(t,X)$, $F=\partial x/\partial X$ und $v=\dot x$ gilt
$$
C=F^{\mathsf T}(I-vv^{\mathsf T})^{-1}F,\qquad
n_{\rm M}=\frac{\sqrt{1-|v|^2}}{\det F}.
$$
Die kontravarianten räumlichen Komponenten des Spannungsteils im Matrixtensor sind $-\sigma$, mit $\sigma=n_{\rm M} L(\mathsf C E)L^{\mathsf T}$ und $L_{iA}=\partial_i X^B C_{BA}$. Der gewünschte Stress der vorigen Schaltbahn folgt daher aus
$$
G_*=C-2\mathsf C^{-1}[n_{\rm M}^{-1}L^{-1}\sigma L^{-\mathsf T}]
$$
auf der Sollbahn, als Funktion von $(\theta,X)$ gespeichert. Für kleine $\epsilon$ ist $G_*$ positiv definit. Anders als die rein räumliche Zielmetrik im vorigen Vergleich enthält diese Einstellung auch den relativistischen Term aus $vv^{\mathsf T}$. In den ruhenden Endlagen reduziert sie sich auf die jeweils kompatible natürliche Metrik. Der vollständige Spannungsteil ist orthogonal zu $U_{\rm M}$ und liefert den mechanischen Energiefluss $-\sigma v$ im Laborsystem. [Relativistische Elastizität in Materialkoordinaten, Beig und Schmidt](https://arxiv.org/abs/gr-qc/0211054)

## Uhrgleichung, Gegenkraft und gewöhnliche Quelle

Bestimme $m(\theta,X)$ aus dem bisherigen Energiekriterium
$$
n_0(m-m_0)=-\mathcal E+r_0\operatorname{Div}_X d.
$$
Hier ist $d=O(\epsilon^2)$ der relative Speicherweg, $r_0\dot d=\sigma v$ bis zur betrachteten Ordnung, und $\mathcal E$ umfasst die gemeinsame kinetische Energie und die auf der Sollbahn ausgewertete elastische Energie pro Referenzvolumen. Die Gleichung wird in die lokalen Koordinaten $(\theta,X)$ übertragen. Der relative Versatz liefert $-r_0\operatorname{div}d$ in der räumlichen Trägerdichte. Die Summe der beiden Hilbert-Tensoren bei $\lambda=0$ hat deshalb durch zweite Ordnung dieselbe Energiedichte, denselben Impulsstrom und denselben räumlichen Impulsfluss wie in der [Umschaltrechnung](OP5_J_Umschaltung_Ruhelagen.md). Die 1-Form steuert die Bewegung mit eigenen Variationskräften und ohne eigenen Hilbert-Tensor.

Es bleibt zu prüfen, ob Uhr und Matrix bei $\lambda=0$ die Gleichungen der gemeinsamen Wirkung erfüllen. Auf der vorbereiteten Bahn erfüllt $\theta$ die Multiplikatorgleichung, wenn $\theta$ entlang jeder Matrixweltlinie als Eigenzeit integriert wird. Der Speicher erfüllt seine Euler-Lagrange-Gleichung durch die Konstruktion von $A$. Der schon berechnete Gesamttensor ist bis zur zweiten Ordnung erhalten. Diffeomorphismeninvarianz der gemeinsamen Wirkung gibt für ihre normierten Euler-Lagrange-Ausdrücke
$$
\nabla_\mu T^\mu{}_\nu =
 E_\theta\partial_\nu\theta+E_{X^I}\partial_\nu X^I
 +E_{Z^I}\partial_\nu Z^I+E_\lambda\partial_\nu\lambda .
$$
Die Form folgt durch infinitesimale Koordinatentransformation der Metrik und der Skalarfelder und partielle Integration. Da $d\theta,dX^1,dX^2,dX^3$ eine Koframe bilden, folgen auf der Bahn $E_\theta=0$ und $E_X=0$ bis zur selben Ordnung. Damit ist $\lambda=0$ auf dieser Lösung konsistent. Der Uhrtensor verschwindet dort. Die Gegenkraft auf die Matrix folgt aus der Wirkung. Sie muss nicht als äußerer, von der Energiequelle unabhängiger Term ergänzt werden.

Für die Kompensationsbahn $f=s^2$ bleibt die retardierte gewöhnliche Außenkrümmung des Modells in linearer Gravitation bis zur zweiten Auslenkungsordnung null. Die lineare lokale W2-Quelle auf dem Plateau bleibt erhalten. Die Uhr ist ein idealer Zwangsfreiheitsgrad, und die räumlich aufgelösten Kopplungsfunktionen sind auf die Sollbahn vorprogrammiert. Offen bleiben die Stabilität gegenüber Störungen, die Realisierung einer realen Uhr und eines realen materiellen Wandlers samt ihrer zusätzlichen Quellen, die gewöhnliche Innenfeldkalibrierung und die native Higgs–OP5-Kopplung.

## Rechenkontrolle

[Wolfram-Skript](op5_j_kovariante_speicherkopplung.wl) · [Tatsächliche Ausgabe](op5_j_kovariante_speicherkopplung.txt) · [Laufmanifest](op5_j_kovariante_speicherkopplung.json)

Wolfram prüfte die Metrikvariation des Uhrterms, die Kraft im adaptierten Chart, die Metrikunabhängigkeit des Kopplungsterms sowie die Beiträge der gespeicherten und kinetischen Energie. Die Spannungsumrechnung wurde für eine exakte nichtdiagonale Beispielmatrix und eine rationale Geschwindigkeit kontrolliert. Der allgemeine Schluss folgt aus der Tensorrechnung und der Variationsidentität im Text. Reproduzierbar mit **wolframscript -file op5_j_kovariante_speicherkopplung.wl**.
