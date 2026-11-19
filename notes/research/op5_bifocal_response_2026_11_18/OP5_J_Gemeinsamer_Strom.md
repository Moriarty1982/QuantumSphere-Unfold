# OP5: Gemeinsamer J-Strom, Vektormischung und Isotopendifferenz

19. November 2026. Analytische Erkundung in M. Im [thermischen Neutron–Blei-Vergleich](OP5_J_Neutron_Thermischer_Test.md) braucht der bisherige repulsive Außenkanal einen inneren Randpol, um zwei Referenzwerte zu reproduzieren. Wir prüfen rückwärts, ob zusätzliche abelsche Vektormassen oder kinetische Mischungen den Konflikt schon am Vertex trennen können. Es geht um den statischen, führenden Austausch zwischen punktförmig geschriebenen erhaltenen Ladungen. Protonstruktur, Kernformfaktoren, Abschirmung im Medium und nichtlineare Wechselwirkungen werden in dieser Erkundung nicht mitgerechnet.

## Beliebig viele abelsche Vektoren

Seien $K>0$ die symmetrische kinetische Matrix, $\mathsf M^2\ge0$ die symmetrische Massenmatrix und $\mathbf j,\mathbf e$ die reellen Kopplungsvektoren der beiden Quellströme $J,Q_{\rm em}$. Die Kopplung einer Art $s$ an die Vektorfelder ist
$$
\mathbf c_s=Q_J(s)\,\mathbf j+Q_{\rm em}(s)\,\mathbf e .
$$
Für räumlichen Impuls $\mathbf q$ hat der statische Austausch die Matrix $(q^2K+\mathsf M^2)^{-1}$. Kanonische Normierung mit $K^{-1/2}$ und orthogonale Diagonalisierung von $K^{-1/2}\mathsf M^2K^{-1/2}$ liefern Massen $m_i\ge0$ und reelle Kopplungen $c_{s,i}$ in der Massenbasis. Das setzt eine positive kinetische Form und ein stabiles abelsches Vakuum voraus. [Kinetische und Massenmischung abelscher Eichfelder](https://qft.org/gauge-theories-standard-model/new-physics-portals/consistent-new-matter-gauge-sectors/)

Mit der Ladungstabelle der [Singulett-Variante](OP5_Singulettpaar_J_Reichweite.md) gilt unabhängig von $\mathbf e$
$$
\mathbf c_n=3\mathbf j,\qquad \mathbf c_+=\mathbf j,\qquad \mathbf c_-=-\mathbf j .
$$
Alle drei Arten sind elektrisch neutral. Die Proportionalität bleibt unter jedem gemeinsamen Basiswechsel der Vektorfelder erhalten. Sei $g_i$ die Komponente von $\mathbf j$ nach kanonischer Normierung und Diagonalisierung. Die Fourier-Rücktransformation liefert
$$
V_{+-}(r)=-\mathcal Y_{JJ}(r),\qquad
V_{nn}(r)=9\mathcal Y_{JJ}(r),\qquad
\mathcal Y_{JJ}(r)=\sum_i\frac{g_i^2e^{-m_i r}}{4\pi r}.
$$
Der Faktor neun ist in diesem Austauschmodell exakt für alle Abstände der Punktrechnung. Die Gewichte der einzelnen Yukawa-Beiträge sind nichtnegativ. Verschiedene Vektorpole, die denselben J-Strom ablesen, können die statische Neutronenabstoßung daher nicht gegeneinander aufheben. Die Masse eines Pols entscheidet, auf welchen Abständen die verknüpften Beiträge wirksam sind. Die Identität setzt keine bestimmte Zahl von Polen und keine bestimmte kinetische Mischung voraus. Eine Gegenrechnung mit einer nichtdiagonalen positiven Zweifeld-Kinetik und einer nicht gleichzeitig diagonal gewählten Massenmatrix ergab den Faktor neun bei vier verschiedenen Impulsen bis auf Rundungsfehler.

## Isotope mit gleicher Protonenzahl

Ein Punktkern mit Protonenzahl $Z$ und Neutronenzahl $N$ hat $\mathbf c_{Z,N}=3(Z+N)\mathbf j+Z\mathbf e$. Definiere $\mathcal Y_{JQ}(r)=\sum_i g_i e_i e^{-m_i r}/(4\pi r)$, wobei $e_i$ die Komponente der elektrischen Kopplung in der Massenbasis bezeichnet. Dann gilt
$$
V_{n,(Z,N)}(r)=9(Z+N)\mathcal Y_{JJ}(r)+3Z\mathcal Y_{JQ}(r),
$$
und für zwei Isotope desselben Elements
$$
V_{n,(Z,N_2)}(r)-V_{n,(Z,N_1)}(r)=9(N_2-N_1)\mathcal Y_{JJ}(r).
$$
Der rein elektrische Quellanteil fällt in dieser Differenz aus. Bei neutralen Atomen gilt derselbe Vergleich im führenden gemeinsamen Punktlimit, wenn die Elektronenwolke in beiden Isotopen identisch behandelt wird. Unterschiede der Ladungsverteilung sowie isotopeigene starke und elektromagnetische Streueffekte gehören in eine wirkliche Datenanalyse. Der Ausdruck ist eine Identität der zusätzlichen Potentiale. Streulängen sind nichtlineare Funktionen der Potentiale, sodass die Identität nicht direkt auf Differenzen gemessener Streulängen übertragen werden kann.

Wenn ein äußerer Vergleich bei Abstand $R$ eine Obergrenze $C_n$ für $R V_{nn}(R)$ liefert, folgt zusätzlich für den gesamten Teil der Spektralgewichte mit Massen $m_i\le m_*$:
$$
\sum_{m_i\le m_*}\frac{g_i^2}{4\pi}
\le \frac{e^{m_*R}C_n}{9}.
$$
Die nichtnegativen Beiträge mit größeren Massen können beim Beweis weggelassen werden. Diese Schranke erklärt, was eine Messung auf einer gegebenen Distanz höchstens abdeckt. Ein kürzer reichender Anteil kann sich einer solchen Einzelmessung entziehen und verlangt eine eigenständige Kurzstreckenprüfung.

## Eine zusätzliche Ladungsrichtung

Innerhalb des gemeinsamen Stromansatzes ist ein Eichmodus mit $c_n=0$ zugleich ein Modus ohne Kopplung an $X_\pm$. Ein Vektormodus, der das Paar bindet und keine Neutronenkopplung besitzt, setzt daher nichtproportionale Kopplungsvektoren voraus. Als expliziter Vergleich kann ein weiteres $U(1)_D$ nur auf zwei vektorartigen Dirac-Singuletts wirken, mit entgegengesetzter D-Ladung und $Q_J=Q_{\rm em}=0$. Wähle gleiche Massen und eine Symmetrie $D_\mu\mapsto-D_\mu$, $X_+\leftrightarrow X_-$, wobei die gewöhnliche Materie unverändert bleibt. Eine Stückelberg-Koordinate für D transformiert bei Bedarf ebenfalls mit Minuszeichen. Dann sind bilineare Mischungen mit den gewöhnlichen Eichfeldern durch diese Symmetrie verboten. Die zwei Dirac-Singuletts haben jeweils verschwindende kubische und gemischt gravitative D-Anomalie. Mit getrennten erhaltenen Konstituentenzahlen erlaubt dieser Sektor die bereits betrachtete Coulomb- oder Yukawa-Bindung. Seine Teilchen liefern auf dieser Feldliste jedoch keinen ursprünglichen J-Strom. Eine Wirkung, die sie mit der nativen OP5-Auslese oder mit einer kosmologischen Häufigkeit verbindet, wäre noch herzuleiten.

Die Rechnung schließt die Entkopplung durch reine Vektormischung bei unverändert gemeinsamer Ladungsrichtung aus. Ein eigenständiger Bindungsstrom kann die statischen Kraftkanäle trennen. Seine Herkunft, sein kosmologischer Bestand und H96 bleiben offen.
