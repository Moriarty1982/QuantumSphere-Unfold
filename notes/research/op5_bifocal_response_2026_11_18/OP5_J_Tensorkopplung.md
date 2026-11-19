# OP5: Laufphase aus einer Tensor-Kopplung

19. November 2026. Analytische Erkundung in M. Die [skalare Wellenauslese](OP5_J_Wellenauslese.md) hat im geometrisch-optischen Grenzfall keine zusätzliche Laufphase. Hier prüfen wir, ob diese Nullstelle aus den Symmetrien folgt oder nur aus der Wahl des Operators $F_J^2F_D^2$. Die Wechselwirkung in dieser Notiz ist eine zusätzliche EFT-Annahme. Es gibt keine Ableitung ihres Koeffizienten aus W1/W2 und keinen [H96-Datentest](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Ein erlaubter unabhängiger Operator

Nehme in lokalen Lorentz-Koordinaten mit Signatur $(-,+,+,+)$ die Maxwell-Tensoren $T_J^{\mu\nu}$ und $T_{D,\mathrm{Feld}}^{\mu\nu}$ in kanonischer Normierung. Für einen statischen Beobachter ist $T_J^{00}=(\mathbf E_J^2+\mathbf B_J^2)/2$ und $\sum_i T_J^{ii}=T_J^{00}$. Der Operator
$$
\Delta\mathcal L=\frac{\gamma}{\Lambda^4}T_J^{\mu\nu}\mathcal T^D_{\mu\nu}
$$
ist eichinvariant und unter $D_\mu\mapsto-D_\mu$, $X_+\leftrightarrow X_-$ gerade. Dabei kann $\mathcal T^D$ entweder den D-Maxwell-Tensor oder, als andere Modellwahl, den vollständigen D-Energie-Impuls-Tensor bezeichnen. In beiden Fällen hat der Operator Dimension acht. Er ist vom skalaren Produkt der Feldinvarianten unabhängig. Beispielsweise ist $F_J^2$ für eine laufende ebene J-Welle null, ihr $T_J^{00}$ bei nichtverschwindender Amplitude aber positiv. Die Symmetrie verbietet keine der beiden erhaltenen Antwortformen. Der Ansatz bleibt quadratisch im J-Feld und erzeugt in dieser Trunkierung bei ausgeschaltetem J-Feld keine inhomogene J-Quelle.

## Abgleich an einer gebundenen Einheit

Wir betrachten einen stationären, im Mittel isotropen Verband. Ein von außen angelegtes J-Feld variiere langsam über seinen Radius. Zur ersten Ordnung in $\gamma$ ist der zusätzliche Wirkungsbeitrag mit dem ungestörten D-Zustand auszuwerten. Setze
$$
\int d^3x\,\mathcal T^D_{00}=U,\qquad
\int d^3x\,\mathcal T^D_{ij}=\delta_{ij} S,\qquad
\int d^3x\,\mathcal T^D_{0i}=0.
$$
Dann trägt der Verband $(\gamma/\Lambda^4)(U+S)T_J^{00}$ zur integrierten Lagrangefunktion bei. In einem dünnen ruhenden Ensemble mit physischer Anzahldichte $n$ definieren wir
$$
\zeta=\frac{\gamma n}{\Lambda^4}(U+S).
$$
Die zwei Operatorwahlen liefern unterschiedliche Zuordnungen:

- **Nur D-Feld.** Im statischen Coulomb-Vergleich zählt hier als isolierter Bindungsbeitrag der Kreuzterm der beiden entgegengesetzt geladenen Quellen. Nach Abzug der Einzel-Selbstterme ist $U=\langle V_C\rangle=-\mu A_D^2$ im $1s$-Grundzustand. Der Maxwell-Tensor ist spurfrei, sodass isotrop $S=U/3$. Damit gilt für diesen Beitrag $\zeta_{\rm Feld}=-(4/3)\gamma n\mu A_D^2/\Lambda^4$. Renormierte Beiträge aus Einteilchenoperatoren sind darin nicht festgelegt.
- **Vollständiger D-Tensor.** Für das isolierte, stationäre gebundene System ist $U=M$, die Gesamtmasse einschließlich Bindung. Lokale Erhaltung und ein verschwindender Oberflächenterm ergeben $\int \mathcal T^D_{ij}\,d^3x=0$, weil $\partial_k(x^i\mathcal T^{D\,kj})=\mathcal T^{D\,ij}$. Dies ist die tensorielle Form der [integrierten Stressbilanz](OP5_Gebundener_Tensor.md). Daher folgt $\zeta_{\rm ges}=\gamma\rho_D/\Lambda^4$ mit $\rho_D=n M$. Diese Form setzt die Kopplung an den vollständigen, erhaltenen Tensor voraus. Sie folgt nicht allein aus Eichinvarianz oder aus dem Austauschsymmetrieargument.

## Wellenantwort und Vorwärtsamplitude

Zusammen mit dem skalaren Koeffizienten $Z$ aus der [Ensemblewirkung](OP5_J_Ensembleantwort.md) lautet die ruhende, isotrope Wellenlagrangefunktion
$$
\mathcal L_{J,\rm eff}
=\tfrac12(Z+\zeta)\mathbf E_J^2
-\tfrac12(Z-\zeta)\mathbf B_J^2 .
$$
Wir verwenden $Z>|\zeta|$ für positive elektrische und magnetische kinetische Koeffizienten. Ein Verlust-, Dispersions- oder UV-Kausalitätsmodell ist darin nicht enthalten. Die Permittivität ist $Z+\zeta$, die inverse Permeabilität $Z-\zeta$. Für transversale ebene Wellen in einem homogenen Gebiet folgt
$$
v_J^2=\frac{Z-\zeta}{Z+\zeta},\qquad
n_J=\sqrt{\frac{Z+\zeta}{Z-\zeta}}
=1+\frac{\zeta}{Z}+O\!\left((\zeta/Z)^2\right).
$$
Die lineare Entwicklung wurde bei vier kleinen positiven und negativen Verhältnissen numerisch kontrolliert. Eine Änderung des relativen Gewichts elektrischer und magnetischer Beiträge ist die hier relevante Form eines effektiven Ausbreitungskegels. [Disformale Ausbreitung als externer Vergleich](https://arxiv.org/abs/1605.03567)

In flacher Raumzeit und bei schwacher, langsam räumlich variierender Antwort ist die Laufphase relativ zum Vakuum auf dem in erster Ordnung ungestörten Weg $\Delta\varphi=\omega\int (\zeta/Z)\,d\ell$. Für die vollständige Tensor-Kopplung ist das im führenden Vakuumabgleich $Z\simeq1$ die gewichtete Massensäule $\omega\gamma\int\rho_D d\ell/\Lambda^4$. In einer flachen, statischen Born-Probe tritt dasselbe Vorzeichenmuster auf: Die Permittivitätsstörung ist $\chi+\zeta$, die Störung der inversen Permeabilität $\chi-\zeta$. In der Vorwärtsrichtung heben sich nur die beiden $\chi$-Beiträge auf. Für eine normierte gleichpolarisierte Welle bleibt $f(0)=k^2\widetilde\zeta(0)/(2\pi)$ mit der Fourier-Normierung der vorigen Notiz. Die Größen sind Vorhersagen für den gewählten J-Kanal und keine Behauptung über die Ausbreitung gewöhnlicher Photonen.

Eine lineare Laufphase ist somit im größeren symmetrieverträglichen Ansatz möglich. Ihre Interpretation als Gesamtmassensäule verlangt den Abgleich an den vollständigen D-Tensor. Die Feldvariante misst dagegen eine bindungsgewichtete Säule. Die Stärke $\gamma/\Lambda^4$, der Referenzzeitpunkt, die Populationsdynamik und eine tatsächlich messbare J-Welle bleiben offen. Eine einzelne Projektion bestimmt ohne Geometrie und Kalibrierung weder eine dreidimensionale Dichte noch $\Omega_M$. H96 bleibt offen.
