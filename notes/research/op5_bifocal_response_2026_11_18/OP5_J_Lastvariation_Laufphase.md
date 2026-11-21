# OP5 – Zweikanal-Lastvariation und Grenzen der J/A-Laufphase

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Durchgangs- und Parallelprüfung](OP5_J_Durchgang_Parallelpruefung.md) behandelte den skalaren A-Durchgang, den Drei-Längen-Abschluss und das Kinetikkriterium. Hier werden die offene J-Rückwelle, die robuste Phasenauswertung und die Ordnung des gemeinsamen Hauptteils geprüft. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 braucht eine unabhängige kosmologische Bestandsdynamik.

## Wie viele Laststellungen den A-Durchgang bestimmen

Bei reiner A-Einspeisung von links und zwei offenen Rücklaufmoden rechts ist der gemessene A-Ausgang durch
$$
y_i=t+r_A x_{i,A}+r_J x_{i,J}
$$
gegeben. Die komplexen $x_i=(x_{i,A},x_{i,J})$ sind einfallende normierte Wellen an derselben kalibrierten Ebene, $r$ ist die A-Zeile des rechtsseitigen Reflexionsblocks. Lastvariationen müssen denselben Streuer sehen. Ein konstantes, bei der Variation verborgenes J-Signal fällt unter diese Bedingung, ist aber gesondert zu erfassen.

Der Durchgang $t$ ist genau dann durch die Laststellungen bestimmt, wenn es komplexe Gewichte $w_i$ mit $\sum_i w_i=1$ und $\sum_i w_i x_i=0$ gibt. Dann gilt $t=\sum_i w_i y_i$. Die Bedingungen bedeuten, dass der Ursprung im komplexen affinen Spann der gemessenen Einfallspunkte liegt. Falls dieser affine Spann den Ursprung verfehlt, gibt es eine affine Linearform, die für alle Messpunkte null und am Ursprung ungleich null ist. Die Addition dieser Form zum Übertragungsmodell hält alle Daten fest und verschiebt $t$. Drei affin unabhängige Laststellungen bestimmen bei zwei Rücklaufmoden den Durchgang und beide Rückstreukoeffizienten. Zwei genügen, wenn ihre affine Gerade durch den Ursprung läuft, etwa bei entgegengesetzten Rückwellen. Eine bekannte reflexionsfreie Stellung genügt unmittelbar.

Eine reine Variation der A-Last bei festem J-Reflexionsfaktor $\gamma_J$ erzeugt im Allgemeinen einen Offset. Mit $u_J$ als vorwärts erzeugter J-Amplitude und $R$ als rechtsseitiger Reflexionsmatrix gilt
$$
x_J=\frac{\gamma_J(u_J+R_{JA}x_A)}{1-\gamma_J R_{JJ}},
\qquad
y|_{x_A=0}-t=\frac{R_{AJ}\gamma_J u_J}{1-\gamma_J R_{JJ}} .
$$
Eine schwache Variation ausschließlich der A-Last kann den Offset mit beliebig genauer A-Messung nicht bestimmen. Ist sein zulässiger Betrag $b$, genügt
$$
|\gamma_J|\le \frac{b}{|R_{AJ}u_J|+b|R_{JJ}|}
$$
bei zusätzlich $|\gamma_JR_{JJ}|<1$. Wer beide Offdiagonalbeträge an den gewählten Ebenen nur durch $0{,}00317$ und $|R_{JJ}|$ durch eins begrenzt, braucht für $b=10^{-7}$ beispielsweise $|\gamma_J|\le0{,}00985$. Das ist eine illustrative Worst-Case-Grenze; gemessene kleinere Reflexionen oder ein unabhängiger Abgleich ändern sie.

## Robuste Dreilastmessung

Als Sollpunkte wähle ein gleichseitiges Dreieck um null im reellen Anteil der zweikomponentigen komplexen $x$-Ebene. Die Punkte seien $a(1,0)$ und $a(-1/2,\pm\sqrt3/2)$. Die Matrix $M_0$ mit Zeilen $(1,x_i/a)$ hat $M_0^\dagger M_0=\operatorname{diag}(3,3/2,3/2)$. Aus den tatsächlich gemessenen Punkten bilde $\widehat M$ und löse $\widehat M^{\mathsf T}w=(1,0,0)^{\mathsf T}$. Für Fehler $\|\widehat x_i-x_i\|_2\le\epsilon_x$ und Sollpunkte $x_i$ gilt $\|\widehat M-M_0\|\le\sqrt3\epsilon_x/a$. Mit $\kappa=\sqrt2\epsilon_x/a<1$ liefert eine Neumann-Abschätzung um die Sollgewichte $(1,1,1)/3$ die Schranke $\sum |w_i|\le1/(1-\kappa)$. Wenn die realisierten Punkte zusätzlich von den Sollpunkten abweichen, geht ihre Abweichung in diese Konditionsschranke ein. Der eigentliche Amplitudenfehler verwendet den Fehler der gemessenen Punkte gegenüber den realisierten Punkten:
$$
|\widehat t-t|\le\frac{\epsilon_y+\|r\|_2\epsilon_x}{1-\kappa},
$$
bei den ideal realisierten Sollpunkten und $|\widehat y_i-y_i|\le\epsilon_y$.

Für $a=0{,}02$, $\epsilon_x=\epsilon_y=10^{-8}$ und passive $\|r\|_2\le1$ ist der Durchgangsfehler pro Zustand höchstens $2{,}001\cdot10^{-8}$. Mit $|t_{ms}|\ge0{,}99$ und separat höchstens $4\cdot10^{-7}$ an Fehlern der Referenzebenen bleibt die komplexe Logabweichung des Vier-Zustands-Durchgangs unter $4{,}809\cdot10^{-7}$. Das Beispiel setzt einen Aufbau voraus, der zwei unabhängige komplexe Rückwellenrichtungen einstellen oder einspeisen und messen kann. Die Lastgeometrie liefert keine eigene Schranke für die HCl/H-Portkondition.

## Auflösbarkeit des J-Längentests

Für das komplexe gemessene Signal $\widehat S_n$ einer Länge sei der additive Gesamtfehler durch $\eta_n<|\widehat S_n|$ begrenzt. Das schließt Fremdmoden, Mehrwege, Anschlussrest und Messfehler ein, soweit sie nicht separat budgetiert werden. Der Punktphasenfehler ist höchstens $\arcsin(\eta_n/|\widehat S_n|)$, aus der Tangente an die komplexe Fehlerscheibe. Für ein Längenpaar summieren sich die beiden Phasengrenzen und der unabhängige Fehler des A-Phasenabzugs zu $\delta_\phi$. Für den Abschluss über drei Längen gelten Gewichte $1,2,1$. Ist die differentielle Wellenzahl $g=k_J-k_A$ um einen Anker bis auf $W$ bekannt, wählt $dW+\delta_\phi<\pi$ den eindeutigen Zweig innerhalb der Messfehler. Danach beträgt der Fehler von $g$ höchstens $\delta_\phi/d$, bei unabhängig ausreichend genauem Längenmaß.

Im Modell aus der [Rücklauftoleranzrechnung](OP5_J_Ruecklauf_Toleranzen.md) setze $\eta_n/|\widehat S_n|\le10^{-4}$ und den A-Phasenfehler auf $2\cdot10^{-6}$ rad je Paar. Damit ist $\delta_\phi\simeq2{,}02\cdot10^{-4}$ rad. Die physische massive Modellspanne $g\in[-k_A,0]$ verankert eine Messung bei $1{,}7\ \mu{\rm m}$. Deren Fehlerintervall reicht zur Zweigwahl bei $1$ cm. Die nominale Phase $-1{,}82605$ rad ist in diesem Beispiel deutlich auflösbar. Die vorhergesagte Änderung über 100 MHz beträgt dagegen $2{,}0961\cdot10^{-6}$ rad gegenüber $4{,}0401\cdot10^{-4}$ rad für den Vergleich beider Bandenden. Die Auflösung für eine Längenphase genügt hier nicht für den Nachweis der massiven Frequenzsteigung gegenüber einem konstanten differentiellen Wellenzahlversatz. Ein unabhängiger J/A-Abgleich ist Voraussetzung für beide Aussagen.

## Ordnung des gemeinsamen Hauptteils

W1 schreibt ein J-Maxwellfeld aus. W2 ergänzt minimal kovariante Higgs-Kinetik und nichtderivative Yukawa-Terme. Für einen ergänzten minimalen A-Kanal auf derselben Metrik ist der transversale Hauptteil bei zwei Ableitungen auf klassischer Baumebene proportional zu $K_{ab}g^{\mu\nu}k_\mu k_\nu$. Ein positiver gemeinsamer Kinetikfaktor und die algebraischen Massenterme ändern diese Aussage bei endlicher Hintergrundamplitude in dieser Trunkierung nicht. Massen können die Dispersion bei endlicher Frequenz verändern. Die unabhängige A-Dynamik wird in W1/W2 nicht vollständig hergeleitet. [Metrischer Abgleich](OP5_J_Metrischer_Abgleich.md)

Zusätzliche Krümmungsoperatoren wie $R_{\mu\nu\rho\sigma}F_a^{\mu\nu}F_b^{\rho\sigma}$ haben in vier Dimensionen Massendimension sechs. Eine Aufspaltung erfordert den wirksamen Krümmungskontrast und nichtproportionale J/A-Koeffizienten. Ein skalarer Faktor vor $F^2$ lässt den führenden Kegel gemeinsam. In einem flachen homogenen Higgsgrundzustand $D_\mu\Phi_0=0$ beginnt $\operatorname{Re}[(D_\mu\Phi)^\dagger D_\nu\Phi]T_J^{\mu\nu}$ bei zweiter Ordnung in der Higgsstörung. Ein linearer Hesseterm $\nabla_\mu\nabla_\nu(\Phi^\dagger\Phi)T_J^{\mu\nu}$ kann lokal beitragen. Entlang des affinen Referenzstrahls ergibt seine lineare Phasenkorrektur ein Endglied, das bei abgeglichenen oder kompakt getragenen Profilen verschwindet. Diese Aussagen setzen den jeweiligen Vergleichshintergrund voraus. Der [Dirac-Schwellenabgleich](OP5_J_Dirac_Schwellenabgleich.md) zeigt eine bedingte Krümmungsroute. Der native Koeffizient und die freie J-Ausbreitung bleiben offen.

## Rechenkontrolle

Wolfram prüfte Lastdreieck, festen J-Offset, Phasenanker und Bandänderung, die Abwesenheit der Masse im höchsten homogenen Symbolgrad und ein Gradient/Hessian-Beispiel. Qiskit wurde erwogen. Die Rechnung verwendet klassische komplexe Übertragungskoeffizienten und klassische Hauptsymbole.

[Wolfram-Skript](op5_j_lastvariation_laufphase.wl) · [Tatsächliche Ausgabe](op5_j_lastvariation_laufphase.txt) · [Laufmanifest](op5_j_lastvariation_laufphase.json)
