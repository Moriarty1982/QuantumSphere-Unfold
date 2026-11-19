# OP5: Gemeinsame J- und Gravitationsauslese

19. November 2026. Analytische Erkundung in M. Die [Ensembleantwort](OP5_J_Ensembleantwort.md) bestimmt aus einem homogenen J-Signal nur das Produkt von Anzahldichte und Einzelkopplung. Die dortige Inversion mit Poisson-Fluktuationen setzt unabhängige Teilchenpositionen voraus. Wir prüfen, ob ein gemeinsamer Dichtetracer auch bei räumlich korrelierten Populationen weiterführt. Die Gravitation geht hier ausschließlich als unabhängig rekonstruierte Materiedichte auf demselben räumlichen Schnitt ein. Eine Abbildung von realen Projektions- oder Linsendaten auf diesen Schnitt wird nicht hergeleitet. Es erfolgt kein Beobachtungstest nach [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Gemeinsame Fluktuationen derselben Verbände

Bezeichne mit $b=4\kappa$ die J-Antwort eines Verbands, mit $M$ seine Masse und mit $\chi=Z-1$ den effektiven J-Feldkoeffizienten. Für identische Verbände mit konstanten $b\ne0$, $M>0$ sind bei gleicher Glättung
$$
\chi(\mathbf x)=b\,n(\mathbf x),\qquad \rho_D(\mathbf x)=M\,n(\mathbf x).
$$
$\rho_D$ ist der Beitrag dieser Population zur Materiedichte, nicht die gesamte gravitative Dichte. Die Gleichungen sind punktweise und erfordern weder unabhängige Positionen noch eine lineare Beschreibung des Verklumpens. Bei unterschiedlicher, bekannter Glättung beziehen wir die Spektren auf dieselbe räumliche Filterung zurück. Unvermeidbares Messrauschen wird in den folgenden Gleichungen als bekannt oder separat abgezogen vorausgesetzt.

Mit der Konvention $P_{AB}=\langle\delta\widetilde A\,\delta\widetilde B^*\rangle$ bis auf den gemeinsamen Dirac-Faktor gilt auf Modi mit $P_{\chi\chi}\ne0$
$$
\frac{P_{\chi\rho_D}}{P_{\chi\chi}}=\frac{M}{b},\qquad
\bar\rho_D=\bar\chi\,\frac{P_{\chi\rho_D}}{P_{\chi\chi}} .
$$
Das unbekannte Dichtespektrum kürzt sich heraus. Derselbe Vergleich würde bei verschiedenen Arten funktionieren, wenn alle exakt dasselbe Verhältnis $M/b$ haben. Ein kalibrierter Mittelwert $\bar\chi$ und ein separat identifizierbares Kreuzspektrum würden dann die mittlere Masse pro Volumen bestimmen. Die Einzelmasse und die Anzahldichte lassen sich daraus weiterhin nicht separat entnehmen.

## Korrelierte gewöhnliche Materie und unabhängiger Tracer

Für $\rho_G=\rho_D+\rho_{\rm sonst}$ liefert das einfache Verhältnis
$$
\frac{P_{\chi\rho_G}}{P_{\chi\chi}}
=\lambda+\frac{P_{\chi\rho_{\rm sonst}}}{P_{\chi\chi}},\qquad \lambda=M/b .
$$
Das zweite Glied kann auch dann bestehen, wenn das J-Feld nur auf die D-Verbände reagiert, denn beide Populationen können in dieselben gravitativen Strukturen fallen. Ohne weitere Information verdeutlicht $\lambda\mapsto\lambda+\Delta$, $\rho_{\rm sonst}\mapsto\rho_{\rm sonst}-\Delta\chi$ die Mehrdeutigkeit der Zerlegung. Für eine hinreichend kleine Änderung und zulässige positive Hintergrunddichten bleiben beide Beiträge physisch sinnvoll.

Als konkrete Zusatzannahme sei die Fluktuation der übrigen Materie auf einem Modus durch einen unabhängigen Tracer $B$ bis auf ein Residuum beschreibbar, $\delta\widetilde\rho_{\rm sonst}=q\,\delta\widetilde B+\widetilde\epsilon$. Der Koeffizient $q$ darf vom Modus abhängen und muss nicht bekannt sein. $\epsilon$ sei im Kreuzspektrum sowohl zu $\chi$ als auch zu $B$ unkorreliert. Subtraktion der linearen Projektion auf $B$ ergibt für $P_{BB}>0$:
$$
P_{\chi\rho_G\cdot B}
=P_{\chi\rho_G}-\frac{P_{\chi B}P_{B\rho_G}}{P_{BB}}
=\lambda\left(P_{\chi\chi}-\frac{|P_{\chi B}|^2}{P_{BB}}\right).
$$
Ist die Klammer positiv, folgt daraus $\lambda$ modusunabhängig, und wieder $\bar\rho_D=\lambda\bar\chi$. Bei perfekt kollinearen Fluktuationen von $B$ und $\chi$ ist die Klammer null. Ein korreliertes Residuum der gewöhnlichen Materie bleibt ein offener systematischer Beitrag. Ein algebraisches Beispiel mit $P_{\chi\chi}=9$, $P_{BB}=4$, $P_{\chi B}=3$, echter $\lambda=2$ und $q=5$ liefert ohne Bereinigung $P_{\chi\rho_G}/P_{\chi\chi}=11/3$, nach der Projektion dagegen exakt $2$.

## Kontrolle bei unterschiedlichen Verbänden

Für einen isolierten Poisson-Anteil einer Population mit zufälligen Markierungen $(b,M)$ ist nach Rückrechnung der bekannten Filter
$$
\begin{pmatrix}
P_{\chi\chi}^{\rm diskret} & P_{\chi\rho_D}^{\rm diskret}\\
(P_{\chi\rho_D}^{\rm diskret})^*&P_{\rho_D\rho_D}^{\rm diskret}
\end{pmatrix}
=n\begin{pmatrix}
\mathbb E[b^2]&\mathbb E[bM]\\
\mathbb E[bM]&\mathbb E[M^2]
\end{pmatrix}.
$$
Dies folgt aus den Einzelobjekt-Beiträgen zur verbundenen Zweipunktfunktion, bei ortsunabhängiger Markierungsverteilung und endlichen zweiten Momenten. Die Determinante ist nichtnegativ. Bei nichtverschwindender Antwort und Masse ist sie genau dann null, wenn $M=\lambda b$ fast sicher gilt. Das ist die Gleichheitsbedingung von Cauchy–Schwarz. Zum Beispiel ergibt eine gleichgewichtete Mischung mit $(b,M)=(1,2),(3,5)$ eine Determinante von $n^2/4$. Eine hohe Kohärenz der gesamten Spektren allein beweist die Proportionalität nicht. Ein gemeinsamer großskaliger Dichtemodus kann auch bei verschiedenen $M/b$ beide Felder nahezu perfekt korrelieren. Die Rangbedingung betrifft daher den getrennt identifizierten diskreten Anteil.

Der gemeinsame Vergleich liefert eine bedingte Bestimmung von $\bar\rho_D$ ohne Poisson-Annahme, wenn die Antwort pro Masse feststeht und der gravitative Vergleichskanal die übrige Materie geeignet abbildet. Die echte Populationsdynamik, die Kalibrierung des J-Mittelwerts und die Abbildung auf kosmologische Beobachtungen sind zusätzliche Voraussetzungen. Der Übergang zu $\Omega_M$ benötigt die übrigen Materiebeiträge, den Hintergrund und die kritische Dichte. H96 bleibt offen.
