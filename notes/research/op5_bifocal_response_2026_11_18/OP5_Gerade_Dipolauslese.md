# OP5: Braucht H96 einen orientierten Dipol?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im gemeinsamen Materie-Ruhesystem. Die [Vorab-Notiz H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) setzt für heute $\Omega_M=\beta_{\rm sym}^2=(\gamma_L-1)/(\gamma_L+1)$. Darin ist weder eine Dipolrichtung noch ein Vorzeichen einer räumlichen Projektion festgelegt. Die [Induktion über Feldoperationen](W2_Port_Induktion.md) betrifft den signierten Zweig. Hier wird als Rückwärtsprüfung untersucht, welche gerade Dipolinformation übrig bleibt und welcher Teil der physikalischen Auslese damit erreicht ist. Das festgeschriebene H96-Kriterium wird unverändert verwendet. Es findet kein Datenvergleich statt.

## Richtungsunabhängige Information bleibt erhalten

Schreibe $\mathbf d$ für ein geometrisch ausgelesenes Dipolmoment oder für das Dipolmoment einer tatsächlich bezeichneten Quelle. Mittelt ein isotropes Ensemble über Orientierungen, dann gilt bei endlichem zweiten Moment exakt

$$
\langle d_i\rangle=0,\qquad
\langle d_i d_j\rangle=\frac{\delta_{ij}}3\langle|\mathbf d|^2\rangle .
$$

Die erste Aussage folgt daraus, dass kein von null verschiedener Vektor unter allen Drehungen fest bleibt. Die zweite folgt aus Rotationsinvarianz und Spur. Drei gleich kalibrierte orthogonale Projektionen bestimmen somit die Summe ihrer zweiten Momente. Der signierte lineare Randantrieb aus der [Quellkopplung](Quellkopplung.md) lässt sich daraus nicht rekonstruieren. Der lineare Dipol und das quadratische Invariant sind verschiedene Observablen.

Eine direkte geometrische Kontrolle gibt die [Sondenform](Sondenform.md). Auf ihrer Ellipse ist $D=d_--d_+=2w\cos t$. Das gleichmäßige Mittel über den Ellipsenparameter $t$ ergibt $\langle D\rangle_t=0$ und $\langle D^2\rangle_t=2w^2$. Im euklidischen dreidimensionalen isotropen Projektionsmodell wäre der entsprechende Wert $4w^2/3$. Diese Mittelungen verwenden verschiedene Maße. Der Quadratwert hängt weiterhin am Fokusabstand und beim rohen Sondensignal zusätzlich an der Kalibrierung. Im [Coulomb-Vergleich](W2_Quantendipol.md) liefert der isotrope Grundzustand analog $\langle\mathbf D\rangle=0$, aber $\langle|\mathbf D|^2\rangle=3 X^2 a_0^2$ für $\mathbf D=X\mathbf R$, wie das radiale Grundzustandsintegral zeigt. Daraus folgt keine klassische Feldkonfiguration eines einzelnen Quantenzustands.

## Ein nativer gerader J-Beitrag aus der Maxwell-Energie

Für eine glatte **statische** J-Ladungsverteilung mit Gesamtladung null und kompaktem Träger innerhalb einer Kugel verwende das physisch normierte elektrische Dipolmoment $\mathbf d_J=\int \mathbf x\,g_J\rho_J(\mathbf x)\,d^3x$. Es ist unabhängig von der Wahl des Ursprungs. Der Dipolanteil des Potentials außerhalb des Trägers ist $\phi_1=\mathbf d_J\cdot\hat{\mathbf r}/(4\pi r^2)$. Für die Energie dieses Anteils außerhalb eines Radius $R_0$, der den Träger einschließt, gilt

$$
E_{J,1}(r>R_0)
=\frac12\int_{r>R_0}|\nabla\phi_1|^2\,d^3x
=\frac{|\mathbf d_J|^2}{12\pi R_0^3}.
$$

Denn $|\nabla\phi_1|^2=(|\mathbf d_J|^2+3(\mathbf d_J\cdot\hat{\mathbf r})^2)/(16\pi^2r^6)$. Höhere Multipole sind bei Winkelintegration sowohl im Radial- als auch im tangentialen Gradientenanteil orthogonal. Die Formel ist daher zugleich eine untere Schranke für die gesamte elektrische Außenenergie. Isotrope Mittelung einer klassischen statischen Ensemblefamilie setzt den linearen Dipol auf null und lässt dieselbe positive Schranke mit $\langle|\mathbf d_J|^2\rangle$ bestehen. Hier wird keine Analogie zwischen dem Erwartungswert der Ladung und dem Erwartungswert der quantisierten Feldenergie benutzt.

Der Beitrag stammt aus dem [W1-Maxwell-Term](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) und liest $J$, dessen Ladungsgewichte im [Eichkanal-Abgleich](W2_J_Eichkanal.md) von $B-L$ unterschieden sind. Er liefert ohne zusätzliche Zuordnung keinen $B-L$-Quadratwert.

## Warum das noch keine Materiedichte ist

Der lokale Maxwell-Energie-Impuls-Tensor ist spurfrei. Bei isotroper Mittelung desselben Beitrags gilt darum $p_J=\rho_J^{\rm Energie}/3$. Das gilt für die Feldkomponente allein, unabhängig davon, ob eine präparierte statische Quellenverteilung diese Komponente hervorruft. Eine abgeschlossene lokal begrenzte statische Einheit kann durch zusätzliche Quell- und Bindungsspannungen eine andere effektive Zustandsgleichung haben. Ist ihr gesamter Tensor lokal konserviert, dann ergibt $\partial_k(x^iT^{kj})=T^{ij}$ unter verschwindendem Randterm gerade $\int T^{ij}d^3x=0$. Die Voraussetzungen dieser Identität müssen für den vollständigen gebundenen Zustand gezeigt werden. Die Energie des Maxwell-Außenteils allein erfüllt diese Voraussetzung wegen der inneren Schnittfläche am Radius $R_0$ nicht.

Damit kann auf der skalaren H96-Route die Forderung nach einem stationär orientierten Einzeldipol entfallen. Als Ersatz fehlt weiterhin eine aus W1/W2 hergeleitete Zuordnung einer geraden, gemittelten Observablen zur **gesamten** gravitativen Materiedichte, einschließlich Normierung und passender Zustandsgleichung. H96 enthält den Wert schon als Vorhersage aus der Kaskade. Die Fokus-Energie bestimmt weder diesen Zahlenwert noch die Epoche. Die native Randwirkung für den signierten Zweig bleibt separat offen. I3 erfordert weiterhin eigenständige Überschussdynamik.
