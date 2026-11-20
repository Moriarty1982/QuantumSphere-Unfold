# OP5: Massiver Tensorvermittler und gebundene Begleitoperatoren

19. November 2026. Analytische Erkundung in M. Der [metrische Abgleich](OP5_J_Metrischer_Abgleich.md) liefert aus minimaler Gravitation keinen eigenständigen lokalen J–D-Tensorkoeffizienten. Hier prüfen wir einen zusätzlichen massiven Spin-2-Pol als expliziten Vermittler für die [Laufphase aus der Tensor-Kopplung](OP5_J_Tensorkopplung.md). Betrachtet werden lineare Fierz–Pauli-Felder, reelle Kopplungen, positive Polnormen und konservierte Quellen. Dies ist ein Baumabgleich der effektiven Theorie, keine nichtlineare UV-Vervollständigung und kein H96-Datenvergleich.

## Niederenergieabgleich

Für einen kanonisch normierten massiven Modus $h^{(i)}_{\mu\nu}$ der Masse $m_i>0$ nehme die lineare Kopplung $h^{(i)}_{\mu\nu}S_i^{\mu\nu}$ mit
$$
S_i^{\mu\nu}=g_{Ji}T_J^{\mu\nu}+g_{Di}T_D^{\mu\nu}.
$$
$T_D$ ist der vollständige D-Energie-Impuls-Tensor einschließlich der Konstituenten. Die $g$ haben Massendimension $-1$. Für konservierte Quellen reduzieren sich die longitudinalen Impulsterme im Fierz–Pauli-Austausch auf null. Die relevante bilineare Kontraktion in vier Raumzeitdimensionen ist
$$
\langle X,Y\rangle_2=X^{\mu\nu}Y_{\mu\nu}-\tfrac13 X^\mu{}_\mu Y^\nu{}_\nu .
$$
[Hinterbichler, Fierz–Pauli-Theorie und Austausch zwischen Quellen](https://arxiv.org/abs/1105.3735)

Bei Impulsen klein gegenüber allen berücksichtigten $m_i$ liefert der Baumabgleich das führende lokale Glied $\sum_i \langle S_i,S_i\rangle_2/(2m_i^2)$. Die nächsten Ableitungsglieder tragen relativ zwei zusätzliche Impulspotenzen. Da der klassische Maxwell-Tensor $T_J$ spurfrei ist, folgt
$$
\Delta\mathcal L_{\rm eff}
=\tfrac12 C_J T_J^{\mu\nu}T^J_{\mu\nu}
+C_{JD}T_J^{\mu\nu}T^D_{\mu\nu}
+\tfrac12 C_D\left[T_D^{\mu\nu}T^D_{\mu\nu}-\tfrac13(T_D^\mu{}_\mu)^2\right],
$$
mit
$$
C_J=\sum_i \frac{g_{Ji}^2}{m_i^2},\qquad C_D=\sum_i \frac{g_{Di}^2}{m_i^2},\qquad
C_{JD}=\sum_i \frac{g_{Ji}g_{Di}}{m_i^2}.
$$
Die Konvention schreibt einen Faktor $1/2$ vor die diagonalen Operatoren und keinen vor den gemischten. Alle drei $C$ haben Massendimension $-4$. Ein einzelner massiver Pol erzeugt den gesuchten gemischten Operator also explizit. Sein Vorzeichen hängt von der relativen Vorzeichenwahl der Quellkopplungen ab.

## Die Eigenwechselwirkungen begrenzen den Mischterm

Die Matrix der drei Koeffizienten ist die Gram-Matrix zweier reeller Vektoren mit Einträgen $g_{Ji}/m_i$ und $g_{Di}/m_i$. Daher gilt
$$
|C_{JD}|^2\le C_J C_D,\qquad
C_JC_D-C_{JD}^2
=\sum_{i<j}\frac{(g_{Ji}g_{Dj}-g_{Di}g_{Jj})^2}{m_i^2m_j^2}.
$$
Die Positivität betrifft die Matrix in den beiden Quellkanälen. Die Lorentzsche Kontraktion beliebiger Tensoren wird dabei nicht als positiv definiert. Ein einzelner Pol sättigt die Ungleichung; mehrere Pole tun dies genau für proportionale gewichtete Kopplungen, einschließlich der entarteten Fälle. Mehrere Pole können gemischte Beiträge verschiedener Vorzeichen gegenseitig aufheben. Die Eigenkopplungen addieren sich in diesem Vergleich stets nichtnegativ. Die Determinantenformel wurde mit einem Dreipolbeispiel aus nichtproportionalen Kopplungen auf Rundungsfehler kontrolliert.

Für einen ruhenden dünnen Verband liefert der vollständige D-Tensor nach dem [vorigen Abgleich](OP5_J_Tensorkopplung.md) im schwachen Vakuumregime $\Delta\varphi=\omega C_{JD}\Sigma_D$ mit $\Sigma_D=\int \rho_D\,d\ell$. Gelten anderweitig festgelegte Obergrenzen $C_J\le C_J^{\max}$ und $C_D\le C_D^{\max}$ für den durch diese Pole erzeugten Beitrag, folgt
$$
|\Delta\varphi|\le \omega\,\Sigma_D\sqrt{C_J^{\max}C_D^{\max}} .
$$
Es wurden keine phänomenologischen Obergrenzen eingesetzt. Eine separat hinzugesetzte lokale Wechselwirkung kann diese Beziehung für die *gesamten* EFT-Koeffizienten ändern. Sie gehört dann nicht zum hier geprüften reinen Polabgleich.

## Anschluss an den ursprünglichen J-Kanal

Die selektive Wahl setzt eine einzeln konservierte J-Quelle voraus. Im quellfreien Maxwell-Gebiet erfüllt der führende Tensor diese Eigenschaft. In der ursprünglichen [W1-Wirkung](../v4_10_0_w1/Wirkung_W1_Dixon_U1.md) gibt das J-Feld jedoch Impuls an geladene gewöhnliche Materie ab. In der flachen Hintergrundnäherung gilt bei einem Strom $j$ mit der physikalischen Kopplung in seiner Definition
$$
\partial_\mu T_J^{\mu\nu}=-F_J^{\nu\lambda}j_\lambda,\qquad
\partial_\mu T_{\rm gewöhnlich}^{\mu\nu}=+F_J^{\nu\lambda}j_\lambda.
$$
Koppelt ein Pol in diesem Gebiet an $g_{Ji}T_J+g_{{\rm gewöhnlich},i}T_{\rm gewöhnlich}$ und soll die Quelle ohne weitere Kompensation konserviert sein, verlangt ein nichtverschwindender Austausch $g_{{\rm gewöhnlich},i}=g_{Ji}$. Dann entstehen auch Operatoren mit gewöhnlicher Materie. Eine alternative Theorie kann nichtkonservierte Quellen mit einer vollständig mitgerechneten longitudinalen Dynamik zulassen. Der vereinfachte konservierte Baumabgleich gibt dafür keine Vorhersage.

Damit gibt es einen expliziten Ursprung des lokalen Terms in einer erweiterten linearen Theorie. Dieselbe Konstruktion erzwingt Begleitoperatoren und begründet im geladenen W1-Sektor keine reine J-Quellenkopplung. Der vollständige Abgleich von Sender, Empfänger und Materie, die Wilson-Koeffizienten und H96 bleiben offen.
