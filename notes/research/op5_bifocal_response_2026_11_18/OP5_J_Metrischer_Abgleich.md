# OP5: Metrischer Ursprung einer J-Tensor-Kopplung

19. November 2026. Analytische Erkundung in M. Die [J-Tensor-Kopplung](OP5_J_Tensorkopplung.md) würde mit dem vollständigen D-Energie-Impuls-Tensor eine gewichtete Massensäule liefern. Hier prüfen wir drei verschiedene Ebenen der Herleitung: minimale Gravitation in [W1](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) und [W2](../v4_10_0_r82/Wirkung_W2_Higgs.md), masselosen Gravitonenaustausch und einen zusätzlichen lokalen Ricci-Operator. Der D-Sektor wird dabei als zusätzliche, minimal gravitative Materie vorausgesetzt. Seine Feldliste und Population werden nicht aus W1/W2 gewonnen. Es erfolgt kein H96-Datenvergleich.

## Minimale Gravitation und gemeinsamer Lichtkegel

Im torsionsfreien Referenzsektor ist der führende J-Term in W1 der Maxwell-Term $-\sqrt{-g}F_J^2/4$. W2 ergänzt Higgs- und Yukawa-Terme. Im hier geprüften Vergleich gibt es keinen direkten Higgs-Hintergrundbeitrag zum Hauptsymbol der quellfreien J-Welle. Mit $F_J=dJ$ und in einem masselosen, quellenfreien Messgebiet gilt
$$
\nabla_\mu F_J^{\mu\nu}=0,\qquad g^{\mu\nu}k_\mu k_\nu=0
$$
für transversale geometrisch-optische Moden. Ein minimal gekoppeltes Referenzsignal im selben metrischen Hintergrund besitzt denselben charakteristischen Kegel. Bei identischen Randbedingungen und gemeinsamem metrischen Ausbreitungsweg tragen beide dieselbe gravitative Laufzeitänderung. Ein bereits gravitativ berücksichtigter D-Verband erzeugt daraus auf Baumebene keine zusätzliche differentielle J-Laufphase. Gewöhnliche Medien, Eichmassen, verschiedene Emissionszeiten und nichtminimale Materieeffekte sind hier nicht einbezogen.

## Austausch ist kein unabhängiger lokaler Koeffizient

Die linearisierte Einstein-Wirkung enthält ein masseloses Graviton. Mit reduzierter Planckmasse $M_{\rm Pl}$ und konservierten Quellen trägt sein Austausch im Vierimpulsraum eine Struktur proportional zu
$$
\frac{T_J^{\mu\nu}(q)
  [T^D_{\mu\nu}(-q)-\tfrac12 g_{\mu\nu}T^D(-q)]}
 {M_{\rm Pl}^2(q^2+i0)} .
$$
Hier sind die Abschlussbedingungen des Propagators für den Vergleich des Pols ohne Belang. Der klassische J-Maxwell-Tensor ist spurfrei. Die Tensorstruktur im Zähler enthält also die gewünschte Kontraktion. Der masselose Pol bleibt jedoch bestehen. Bei kleinen Impulsen lässt er sich nicht als konstanter Wilson-Koeffizient vor $T_J^{\mu\nu}T^D_{\mu\nu}$ entwickeln. Auf Baumebene ist dies die bereits im gravitativen Hintergrund enthaltene Wechselwirkung. Den Pol nochmals als unabhängige lokale Laufphase anzusetzen würde denselben gravitativen Beitrag doppelt zählen. [Donoghue, Gravitation als effektive Feldtheorie](https://arxiv.org/abs/gr-qc/9512024)

## Was ein zusätzlicher Ricci-Term ergeben würde

Ergänze gezielt den lokalen Operator $\sqrt{-g}\lambda R_{\mu\nu}T_J^{\mu\nu}$ mit $[\lambda]=\mathrm{Masse}^{-2}$. Dies ist eine zusätzliche Eingabe. Wegen $g_{\mu\nu}T_J^{\mu\nu}=0$ ist die Kontraktion über $R_{\mu\nu}$ dieselbe wie über $G_{\mu\nu}$. Die führende Einstein-Gleichung $M_{\rm Pl}^2G_{\mu\nu}=T_{\mu\nu}^{\rm alle}$ legt nahe, dass der Operator zur ersten Ordnung in $\lambda$ zur Kontaktstruktur
$$
\sqrt{-g}\,\frac{\lambda}{M_{\rm Pl}^2}T_J^{\mu\nu}T_{\mu\nu}^{\rm alle}
$$
äquivalent ist. Der Index „alle“ umfasst die gewöhnliche Materie, den zusätzlich angenommenen D-Sektor und den J-Tensor selbst. Ein kosmologischer konstanter Vakuumterm proportional zur Metrik trägt in dieser Kontraktion nicht bei.

Der Abgleich lässt sich direkt durch die inverse Metrikumdefinition
$$
g^{\mu\nu}=\widetilde g^{\mu\nu}-\frac{2\lambda}{M_{\rm Pl}^2}T_J^{\mu\nu}(\widetilde g)+O(\lambda^2)
$$
kontrollieren. Die lineare Variation der Einstein-Wirkung gibt $(M_{\rm Pl}^2/2)G_{\mu\nu}\delta g^{\mu\nu}$ und entfernt den Ricci-Term. Die gemeinsame Materievariation ist $-T_{\mu\nu}^{\rm alle}\delta g^{\mu\nu}/2$. Sie liefert damit genau das positive Kontaktglied oben. Die Umdefinition gilt perturbativ und verlangt die konsistente Transformation sämtlicher Vergleichsfelder. Sie setzt eine gemessene Laufzeitdifferenz nicht dadurch auf null, dass man nur die J-Gleichung umschreibt.

In einer ruhenden isotropen Quelle mit Energie $\rho$ und Druck $p$ ergibt die Kontaktkontraktion $(\rho+p)T_J^{00}$. Für mehrere solche Quellen addieren sich ihre Beiträge. Für drucklose gewöhnliche Materie und D-Verbände lautet der im [Ausbreitungsabgleich](OP5_J_Tensorkopplung.md) auftretende Koeffizient daher in dieser Ricci-Variante $\zeta=\lambda(\rho_{\rm gewöhnlich}+\rho_D)/M_{\rm Pl}^2$, sofern übrige Feld- und Druckbeiträge vernachlässigbar sind. Die Differenz gegenüber einer Referenz setzt zusätzlich voraus, dass die entsprechenden höheren Operatoren der Referenz getrennt festgelegt sind.

## Geltungsbereich

Quantenkorrekturen geladener Felder im gekrümmten Raum können eigene Krümmungsoperatoren erzeugen. Dazu gehören auch skalare und Weyl-Terme mit anderen Signaturen. Der hier geprüfte Ricci-Term ist kein allgemeiner Ausschluss solcher Effekte. Eine Berechnung aus W2 bräuchte das tatsächliche massive Spektrum, die J-Ladungen, Renormierungsbedingungen und die Wilson-Koeffizienten beider Vergleichskanäle. Der minimale gemeinsame metrische Term bestimmt keinen sektorselektiven Koeffizienten. Der zusätzliche Ricci-Term koppelt in seiner kontaktäquivalenten Form an das gesamte Stressbudget. Die Auswahl eines eigenständigen D-Operators, seine Normierung, reale J-Beobachtbarkeit und H96 bleiben offen.
