# OP5 — Notwendige Spannungsbilanz des Kontrollprofils

20. November 2026. Analytische Erkundung im Materieframe M. Verwendet werden flache Geometrie und ein symmetrischer erhaltener Gesamtquelltensor. Änderungen der Quelle sind lokalisiert, sodass die gewichteten Integrationen über den Raum keinen Randterm liefern.

## Vorwissen geprüft

Der [Quertransport](OP5_J_Quertransport.md) gibt einen kompakten Strom und einen formal erhaltenen Tensor für das [Kontrollprofil](OP5_J_Kontrollkontrast.md) an. Die [Antriebsrechnung](OP5_J_Antrieb_Quertransport.md) bestimmt das Hindernis für Gradientenkräfte im homogenen Fluid. Die [gebundene Tensorbilanz](OP5_Gebundener_Tensor.md) findet die integrierte statische Virialaufhebung im Zweikörpermodell. Die [W2-Fokusrechnung](W2_Fokusabstand.md) verwendet den Maxwell- und Higgsbeitrag im getrennten, radialen Vergleich. Hier wird rückwärts die räumlich integrierte Spannung aus dem vorgegebenen Dichtemoment bestimmt. Dies betrifft die Messabbildung vor H96 im [Gesamtbild](../../../wiki/Gesamtbild.md). Der präparierte Transport liefert keinen Mechanismus für die Überschussdynamik von I3.

## Von der Zieldichte zur notwendigen Spannung

Sei $\delta T^{\mu\nu}$ die Änderung relativ zu einem festen stationären Referenztensor. Für eine Erhaltungsgleichung $\partial_\mu\delta T^{\mu\nu}=0$ und hinreichend abklingende Ränder folgt durch zweimalige partielle Integration
$$
\frac{d^2}{dt^2}\int_{\mathbb R^3} x_i x_j\,\delta T^{00}\,d^3x
=2\int_{\mathbb R^3}\delta T^{ij}\,d^3x .
$$
Die erste Ableitung ergibt $\int(x_i\delta T^{0j}+x_j\delta T^{0i})$. Die zweite liefert die gewichtete Impulsbilanz. Die Identität gilt für den vollständigen erhaltenen Gesamttensor einschließlich eventueller Ansteuerung, sofern er den genannten Randbedingungen unterliegt. Bei Verwendung eines externen Kraftterms in einer Teilquelle muss dessen Beitrag berücksichtigt werden.

Verwende $\delta T^{00}=s(t)f$ mit $f=(1-\Delta/m^2)\psi$ wie im Kontrollprofil. Die Identität prüft genau diese Änderung der Gesamtenergiedichte. Eine zusätzliche Energiedichte des Antriebs würde die Momente verändern. Für $\psi=A p(z)(g_a(r)-g_{2a}(r)/4)$ und $Q=64\pi Aa^4\ell/1575>0$ gilt
$$
\int x^2 f\,d^3x=\int y^2 f\,d^3x=-Q,
\qquad \int z^2 f\,d^3x=0.
$$
Der Laplacebeitrag verschwindet bei jedem der drei Momente, da $\Delta x_i^2=2$ und $\int\psi=0$. Das $z$-Moment verschwindet aufgrund der Massenerhaltung in jeder Querebene. Das transversale Moment folgt aus $\int r^2g_a\,d^2b=\pi a^4/30$ und der axialen Norm.

Damit ist unabhängig von der Wahl des lokalen Spannungsträgers
$$
\int\delta T^{xx}=\int\delta T^{yy}=-\frac Q2\,\ddot s,\qquad
\int\delta T^{zz}=0.
$$
Alle räumlichen Integrale verwenden $d^3x$. Die integrierte Differenz zwischen Längs- und gemittelter Querspannung ist $Q\ddot s/2$. Rein isotroper Stress kann diese Bilanz während der Beschleunigung nicht erfüllen. Beginnt und endet die Umschaltung in Ruhe, wechselt $\ddot s$ für jeden nichttrivialen Übergang sein Vorzeichen. Während $\ddot s>0$ ist die integrierte transversale Spannungsänderung negativ. Eine alleinige Teilchenkinetik aus einem kalten Referenzzustand mit verschwindendem Teilchenstress hat dagegen $\int \delta T^{xx}=\int T^{xx}\ge0$, da der kinetische Beitrag bei nichtnegativer Belegung ein Integral von $p_x^2/E$ ist. Bewegter gebundener Stoff mit Anfangsstress oder zusätzlichen Feld- und Wechselwirkungsbeiträgen fällt außerhalb dieses Ausschlusses.

Für $s(0)=0$, $s(\tau)=1$ und $\dot s(0)=\dot s(\tau)=0$ benötigt jede zweimal stetig differenzierbare Umschaltung $\sup|\ddot s|\ge4/\tau^2$. Aus $|\dot s(t)|\le\sup|\ddot s|\min(t,\tau-t)$ folgt dies durch Integration. Der Betrag der integrierten Anisotropie muss folglich mindestens einmal $2Q/\tau^2$ erreichen.

## Lineare Antwort der ausgeschriebenen Feldterme

Im reduzierten Maxwell-Higgs-Sektor von [W2](../v4_10_0_r82/Wirkung_W2_Higgs.md) haben die räumlich spurfreien Gradientenbeiträge die Formen
$$
(T_{\rm Maxwell}^{ij})^{\rm TF}=-(E_iE_j+B_iB_j)^{\rm TF},
\qquad
(T_h^{ij})^{\rm TF}=Z_h(\partial_i h\,\partial_j h)^{\rm TF}.
$$
Für den zweiten Ausdruck wird wie bei der radialen Fokusrechnung ein reeller Higgsradius mit kinetischem Faktor $Z_h$ verwendet. Die Ausdrücke folgen durch räumlichen Spurabzug beim Maxwell-Tensor und beim kanonischen skalaren Tensor. Das Potential des radialen Skalars trägt isotrop bei. Bei der Linearisierung um $E=B=0$ und einen homogenen statischen Higgsradius sind diese spurfreien Beiträge von zweiter Ordnung in den Feldstörungen. Der geforderte integrierte anisotrope Stress ist dagegen bei festem Zeitprofil und fester Dauer von erster Ordnung in der Dichtemodulation $A$. Eine reguläre Feldantwort mit $E,B,\nabla h=O(A)$ kann ihn in dieser Näherung daher nicht tragen. Die Rechnung erfasst weder die Tensorantwort eines gebundenen mikroskopischen Hintergrunds noch Störungen, die nicht regulär in $A$ skalieren.

Ein gerichteter vorhandener Feldhintergrund kann einen linearen Term eröffnen. Beispielsweise hat ein Axialfeld $B_0\hat z$ den Maxwell-Kreuzterm $-(B_0\hat z_i\delta B_j+\delta B_i B_0\hat z_j)^{\rm TF}$. Dieser Term kann lokal anisotrop sein. In einem räumlich konstanten Hintergrund reicht jedoch eine kompakte glatte magnetische Störung allein für das **integrierte** Moment nicht aus. Wegen $\nabla\cdot\delta\mathbf B=0$ gilt $\int\delta B_i=\int\nabla\cdot(x_i\delta\mathbf B)=0$. Der integrierte lineare Maxwell-Kreuzterm verschwindet dann. Für inhomogene Hintergrundfelder oder zusätzliche Materie- und Randbeiträge muss die gewichtete Bilanz neu geprüft werden.

## Rechenkontrollen und offene Folgerung

[Wolfram Language](op5_j_spannungsbilanz.wl) bestätigt das transversale Moment, den Zeitfaktor der unteren Schranke, die Laplace-Terme der Momentidentität und den linearen Spurabzug im feldfreien und im gerichteten Hintergrund. Die Prüfung benötigt klassische Tensoralgebra und keine Quantenschaltung. Eine konkrete W2-Konfiguration mit passendem Moment, kontrolliertem Antrieb und bekannter Wirkung auf die Apparatur ist offen. H96 erhält keinen neuen Vergleichswert.
