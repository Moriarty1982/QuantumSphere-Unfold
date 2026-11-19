# OP5: J-Feldantwort eines unter J neutralen Verbands

19. November 2026. Analytische Erkundung in M nach [PR #199](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/199). Der [gemeinsame J-Strom](OP5_J_Gemeinsamer_Strom.md) koppelt die Bindung und die Neutronenabstoßung fest aneinander. Ein eigenständiger abelscher Bindungsstrom D vermeidet diese Proportionalität, lässt aber seine Konstituenten ohne ursprüngliche J-Ladung. Wir prüfen rückwärts, ob die [gerade OP5-Auslese](OP5_Gerade_Dipolauslese.md) einen lokalen Kanal zu einem solchen Verband haben kann. Betrachtet wird eine zusätzliche effektive Wechselwirkung, ohne Ableitung aus W1/W2 und ohne H96-Datentest.

## Eine lokale Kopplung ohne J-Quellladung

Die beiden gleich schweren Dirac-Singuletts $X_\pm$ tragen entgegengesetzte D-Ladung und $Q_J=Q_{\rm em}=0$. Wähle die bereits vorgeschlagene Symmetrie $D_\mu\mapsto-D_\mu$ und $X_+\leftrightarrow X_-$ bei unveränderten sichtbaren Feldern. Sie verbietet den bilinearen Term $F_J^{\mu\nu}F^D_{\mu\nu}$. Der folgende Term ist hingegen eichinvariant und unter dem Austausch gerade:
$$
\mathcal L_{\rm Felder}=-\frac14 F_J^2-\frac14 F_D^2
-\frac{c}{4\Lambda^4}\,(F_J^2)(F_D^2),\qquad
F_I^2=F_I^{\mu\nu}F^I_{\mu\nu}.
$$
Wir arbeiten bei kleinen Feldinvarianten relativ zu $\Lambda^4$ und wählen positive effektive kinetische Koeffizienten. Der dimensionslose Koeffizient $c$ ist frei. Der Operator ist ein einzelner Feldstärkeoperator der Dimension acht. Eine UV-Vervollständigung kann weitere Operatoren derselben oder niedrigerer Dimension liefern. [Feldstärkeoperatoren der Euler–Heisenberg-EFT als Referenz](https://digibug.ugr.es/bitstream/handle/10481/106675/JHEP08%282025%29099.pdf?isAllowed=y&sequence=1).

Im flachen Vergleich ergibt die Variation des J-Potentials
$$
\partial_\mu\left[\left(1+\frac{c}{\Lambda^4}F_D^2\right)F_J^{\mu\nu}\right]
=g_J j_{\rm gewöhnlich}^\nu .
$$
Eine D-Konfiguration liefert in dieser Gleichung einen Multiplikator für ein anliegendes oder einfallendes J-Feld. Bei $j_{\rm gewöhnlich}=0$ und verschwindenden J-Anfangs- und Randdaten bleibt $F_J=0$ eine Lösung. Der Verband hat in dieser gewählten Wirkung keinen inhomogenen J-Quellterm und erzeugt kein permanentes signiertes J-Monopol- oder Dipolfeld. Eine J-Welle kann trotzdem an einem örtlich wechselnden Koeffizienten gestreut werden. Der Ausdruck betrifft den statischen oder führenden klassischen Austausch im angegebenen Modell. Er schließt Mehrfeldwechselwirkungen und induzierte Antworten ein und setzt sie nicht mit einer neuen J-Monopolladung gleich.

## Bindungsantwort in einem langsam variierenden J-Hintergrund

Nimm D in dieser Runde masselos und setze $A_D=g_D^2/(4\pi)$. Auf der Skala des Bohr-Radius $a_D=(\mu A_D)^{-1}$ eines Paars mit reduzierter Masse $\mu$ werde der äußere J-Hintergrund als konstant angenommen. Dann ist $Z_D=1+c F_J^2/\Lambda^4$ ein konstanter Faktor vor dem kinetischen D-Term. Nach kanonischer Normierung gilt $g_{D,\rm eff}=g_D/\sqrt{Z_D}$ und die Coulomb-Kopplung ist $A_D/Z_D$. Wenn die renormierten Konstituentenmassen beim Vergleich festgehalten werden, folgt für den isolierten Bindungsbeitrag
$$
E_{\rm bind}(F_J^2)=-\frac{\mu A_D^2}{2Z_D^2},\qquad
\Delta E_{\rm bind}=\frac{c\mu A_D^2}{\Lambda^4}F_J^2
+O\!\left(\frac{c^2(F_J^2)^2}{\Lambda^8}\right).
$$
Gradientenkorrekturen aus einem veränderlichen Hintergrund sind hier weggelassen. Lokale selbstenergieartige Antworten der beiden Konstituenten könnten zusätzlich zum Bindungsterm beitragen. Ihre Koeffizienten werden durch diese Rechnung nicht fixiert.

Mit $F_J^2=2(\mathbf B_J^2-\mathbf E_J^2)$ ist der reine elektrische Beitrag
$$
\Delta E_{\rm bind}=-\tfrac12\alpha_{J,\rm bind}|\mathbf E_J|^2,\qquad
\alpha_{J,\rm bind}=\frac{4c\mu A_D^2}{\Lambda^4}.
$$
Damit ist der energetische Effekt in einem statischen J-Hintergrund vorzeichengerade. Die induzierte elektrische Antwort ist linear im *angelegten* Feld, falls der Bindungsbeitrag in dieser Form ausgewertet wird. Sie ist kein permanentes Dipolmoment. Bei einem zuvor festgelegten Hintergrund $\mathbf E_0$ enthält der Energieunterschied zu $\mathbf E_0+\delta\mathbf E$ den Kreuzterm $-\alpha_{J,\rm bind}\mathbf E_0\cdot\delta\mathbf E$. Ein lineares Signal in der Störung setzt somit die zusätzliche Referenz voraus. Die Rechnung liefert weder den Hintergrund noch eine native Randdynamik, die ihn festlegt.

Für eine weit entfernte statische J-Punktquelle physikalischer Ladung $q$ ergibt sich in der masselosen Referenz $|\mathbf E_J|=|q|/(4\pi r^2)$. Unter der Langsamkeitsbedingung $r\gg a_D$ liefert der Bindungsbeitrag zum effektiven Quelle–Verband-Potential
$$
\Delta V(r)=-\frac{c\mu A_D^2q^2}{8\pi^2\Lambda^4 r^4}.
$$
Der Abstand $r$ bezeichnet hier den Abstand von der Quelle zum Schwerpunkt, nicht den inneren Relativabstand des Paars. Dieser induzierte Beitrag hat einen anderen Abstandsverlauf als der direkte Ein-Vektor-Austausch aus dem gemeinsamen J-Strom. Sein Vorzeichen hängt von $c$ ab. Die Annahme eines masselosen äußeren Vergleichsfeldes dient dieser Fernformel und legt die physikalische Reichweite von J nicht fest.

## Reichweite der Aussage für OP5

Die Konstruktion liefert eine lokale Kopplung einer neutralen gebundenen Einheit an eine gerade, feldabhängige Beobachtung. Der Unterschied zwischen permanenter Quellladung, Antwort auf ein anliegendes Feld und der gemittelten Materiedichte ist entscheidend. Weder $c/\Lambda^4$ noch der Hintergrund oder die Populationsdichte folgen aus dem Modell. Insbesondere lässt sich aus der Existenz des Terms kein H96-Wert und keine Epochenwahl ableiten. Der signierte quellenfreie OP5-Zweig und H96 bleiben offen.
