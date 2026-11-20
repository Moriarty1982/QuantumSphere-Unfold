# OP5 – Umschaltung mit quadratisch nachgeführter Kompensation

21. November 2026. Analytische Erkundung im Materieframe M, bis zur zweiten Ordnung der Verschiebungsamplitude $\epsilon$ und in linearer Gravitation. Die Konstruktion verbindet die zwei spannungsfreien A/B-Endlagen durch eine kompakte Bewegung. Für das gewöhnliche Außenfeld wird ein mitbewegter Energiespeicher mit expliziter Flussbilanz und einem effektiven Spannungsgesetz angesetzt. Lichtgeschwindigkeit eins, gravitative Signatur $(-,+,+,+)$.

## Vorwissen geprüft

Die [spannungsfreien Ruhelagen](OP5_J_Spannungsfreie_Ruhelagen.md) gleichen den quadratischen Massentransport am Endpunkt aus und bestimmen den zeitintegrierten Leistungsfluss des Speichers. Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) erhält einen kompakten linearen Tensor über einen anderen, operatorwertigen Schaltweg. Der [Reservoirabgleich](OP5_J_Reservoir_Quadrupolabgleich.md) bilanziert bekannte direkte Dichteanteile. Die [Antriebsrichtungen](OP5_J_Antriebsrichtungen.md) beschränken Aktoren mit räumlich konstanten Dehnungsmustern. Die Rückwärtssuche setzt bei der quadratischen Transportdichte während des Schaltens an. Eine Suche nach quadratischer Nachführung, konvektivem Stress und zeitabhängiger Referenzmetrik in Vorab-Notizen, jüngeren Runden und OP5-Analysen ergab für diese Endlagen keinen entsprechenden dynamischen Abgleich. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört das zur lokalen Messschnittstelle. I3 bleibt ein Ausweg über eine eigenständige kosmologische Bestandsdynamik.

## Bewegungsplan und Kräfte

Sei $\varphi$ glatt und kompakt im Inneren beider idealisiert überlagerter Kontinua, $u=\nabla\varphi$, $u_1=u$, $u_2=-u/c$, mit $c>0$ dem Steifigkeitsverhältnis aus der Vorarbeit. Schreibe $\varphi_1=\varphi$, $\varphi_2=-\varphi/c$. Für konstante Referenzmassendichten im aktiven Bereich definiere
$$
M_{ij}=\sum_a\rho_a u_{a,i}u_{a,j},\qquad
B_1=0,\quad B_2=M/(2\rho_2),\qquad b_a=\operatorname{div}B_a .
$$
Hier wirkt die Tensordivergenz auf den zweiten Index. Für glattes $s(t)$, das vor dem Schalten null und danach eins ist, und einen zweiten Schaltverlauf $f(t)$ mit denselben Endwerten setze
$$
x_a=X+\epsilon s\,u_a(X)+\epsilon^2 f\,b_a(X).
$$
Für kleine $\epsilon$ bleiben die Materialabbildungen Diffeomorphismen mit unverändertem Rand. Die Dichte erhält in zweiter Ordnung aus der ersten Bewegung den Term $s^2\partial_i\partial_j M_{ij}/2$. Aus der zweiten Bewegung kommt $-f\partial_i\partial_j M_{ij}/2$. Daher ist $f=s^2$ die direkte zeitliche Nachführung für punktweisen Ausgleich. Der gemeinsame Verlauf $f=s$ erzeugt während des Übergangs im Allgemeinen einen Rest.

Am festen Raumpunkt ist der Pushforward der Referenzkraftdichte $\rho_a\ddot x_a$ bis zur zweiten Ordnung
$$
\epsilon\rho_a\ddot s\,u_a+
\epsilon^2\rho_a\big[\ddot f\,b_a-s\ddot s\,\operatorname{div}(u_a\otimes u_a)\big].
$$
Dafür genügt der kompakte symmetrische Cauchy-Stress
$$
\sigma_a=\epsilon\rho_a\ddot s\,\varphi_a I+
\epsilon^2\rho_a\big[\ddot f\,B_a-s\ddot s\,u_a\otimes u_a\big].
$$
Seine Divergenz liefert die Beschleunigung in jeder Komponente. Seine Symmetrie und der kompakte Träger liefern die Drehmomentbilanz ohne Randtraktion. Für $f=s^2$ ergibt die Summe der quadratischen Spannungen $\epsilon^2\dot s^2M$. Genau dieser Term steht mit umgekehrtem Vorzeichen im mechanischen Impulsfluss, der konvektiven Transport und $-\sigma_a$ enthält.

## Aktive Materialmetrik und Speicher

Seien $F_a=\nabla_X x_a$, $J_a=\det F_a$ und $\mathsf C_a$ die positive Elastizität der Vorarbeit. Die räumlich zeitabhängige Zielmetrik für das gleiche hyperelastische Gesetz ist
$$
G_{a,*}=F_a^{\mathsf T}F_a-
2\mathsf C_a^{-1}\left[J_aF_a^{-1}\sigma_a(x_a)F_a^{-\mathsf T}\right].
$$
Sie ist für kleine Auslenkung mit festem glattem Schaltverlauf positiv definit. Eingesetzt in $E_a=(F_a^{\mathsf T}F_a-G_{a,*})/2$ reproduziert sie den angegebenen Cauchy-Stress. Die Gleichung definiert die Zielmetrik vor der Fahrt aus der Sollbahn und wird als materieller Stellplan verwendet. Sie reduziert sich an den Enden auf die kompatiblen natürlichen Metriken. Im Übergang kann sie inkompatibel sein. Für $f=s^2$ lässt sich der Stellplan als Funktion der drei lokalen Sollwerte $s,\ddot s,\dot s^2$ angeben. Er setzt räumlich programmierbare Aktoren voraus.

Sei $\mathcal E_a$ die Summe aus kinetischer, elastischer und interner Stellenergie pro Referenzvolumen. Die Stellenergie und die Trägheiten der Stellfreiheitsgrade werden in dieser Amplitudenfamilie von Ordnung $\epsilon^2$ gewählt. Bei ruhenden Enden und gleich tiefen Potentialminima gilt $\mathcal E_a=0$ am Anfang und am Ende. Für $P_a=J_a\sigma_a F_a^{-\mathsf T}$ und Gesamtstellleistung $\mathcal W_a$ pro Referenzvolumen ist
$$
\dot{\mathcal E}_a=\operatorname{Div}_X(P_a^{\mathsf T}\dot x_a)+\mathcal W_a.
$$
Ein mitbewegter Speicher mit hinreichend großer Anfangsenergie $R_{a0}$ bilanziert die Leistung mit
$$
J_{{\rm R},a}=P_a^{\mathsf T}\dot x_a,\qquad
R_a=R_{a0}-\mathcal E_a,\qquad
\dot R_a+\operatorname{Div}_X J_{{\rm R},a}=-\mathcal W_a.
$$
Damit kommt der Speicher pro Massenelement auf seine Anfangsenergie zurück. Die Flussumrechnung $F_aJ_{{\rm R},a}/J_a=\sigma_a\dot x_a$ hebt den mechanischen Leistungsfluss $-\sigma_a\dot x_a$ am selben Raumpunkt auf. Der mitbewegte Ausgangsenergieanteil des Speichers steckt in $\rho_a$. Für den gravitativen Vergleich wird zusätzlich angenommen, dass der relative Speicherfluss bis einschließlich zweiter Ordnung keinen eigenen räumlichen Stress trägt. Ein druckfreier Träger mit positivem mitbewegtem Hintergrund und Relativdrift von Ordnung $\epsilon^2$ hat diese kinematische Eigenschaft. Sein zusätzlicher räumlicher Impulsfluss beginnt über zweiter Ordnung. Die Kräfte einer konkreten Transport- und Steuereinrichtung sind dadurch noch offen. Insbesondere kann ihr eigener Spannungsbeitrag die Kompensation verändern.

## Erhaltener Tensor und retardierte Krümmung

Unter diesem Speichergesetz wird die gespeicherte und kinetische Energieänderung im Gesamt-$T^{00}$ durch $R_a-R_{a0}$ kompensiert. Im Gesamt-$T^{0i}$ kompensieren sich die beiden relativen Leistungsflüsse. Die verbleibenden Größen sind der Pushforward der Referenzmasse, der konvektive Massenstrom und der räumliche Impulsfluss $\sum_a(\rho_{a,\mathrm{räumlich}}\dot x_a\otimes\dot x_a-\sigma_a)$. Sie bilden einen symmetrischen erhaltenen Tensor bis zur betrachteten Ordnung. Setze
$$
A=\epsilon(\rho_1-\rho_2/c)s\varphi,\qquad g=(s^2-f)/2 .
$$
Nach Abzug der ruhenden Referenz erhält man
$$
\begin{aligned}
\delta T^{00}&=-\Delta A+\epsilon^2g\,\partial_i\partial_jM_{ij},\\
\delta T^{0i}&=\partial_i\dot A-\epsilon^2\dot g\,\partial_jM_{ij},\\
\delta T^{ij}&=-\delta_{ij}\ddot A+\epsilon^2\ddot g\,M_{ij}.
\end{aligned}
$$
Die drei Restterme geben auch die Quelle einer Fehlsteuerung von $f$ an. Sie verschwinden bei $f=s^2$. Der lineare Teil ist lokal erhalten. Der quadratische Teil ist für beliebiges $f$ separat lokal erhalten.

Für $f=s^2$ definiere $D=\partial_t^2-\Delta$ und $U=D_{\rm ret}^{-1}A$ mit vor der Schaltung verschwindender Störung. In harmonischer Eichung ist die retardierte spurgespiegelte Metrik $\bar h_{\mu\nu}=16\pi G D_{\rm ret}^{-1}\delta T_{\mu\nu}$. Nach Spurumkehr gilt
$$
h_{\mu\nu}
=8\pi G\, A\,\delta_{\mu\nu}+\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,
\qquad
\xi_0=-16\pi G\,\dot U,\quad \xi_i=0 .
$$
Hier bezeichnet $\delta_{\mu\nu}$ die Einheitsmatrix aller vier Komponenten. Der Eichanteil hat verschwindenden linearisierten Riemann-Tensor. Damit verschwindet die gewöhnliche Außenkrümmung des definierten mechanischen Gesamttensors auch während des Schaltens, bei retardierten Daten und bis zur betrachteten Ordnung. Innerhalb des Profils bleibt eine zeitabhängige gewöhnliche Krümmung. Das Plateau behält seine lineare W2-Higgsquelle. Die native Higgs–OP5-Kopplung, die vollständige Quelle realer Steuer- und Feldkomponenten, höhere Amplitudenordnungen und Rückwirkung jenseits linearer Gravitation bleiben offen. [Harmonische Eichung und linearisierte Krümmung, Carroll `6](https://ned.ipac.caltech.edu/level5/March01/Carroll3/Carroll6.html)

## Rechenkontrolle

[Wolfram-Skript](op5_j_umschaltung_ruhelagen.wl) · [Tatsächliche Ausgabe](op5_j_umschaltung_ruhelagen.txt) · [Laufmanifest](op5_j_umschaltung_ruhelagen.json)

Wolfram prüfte beide Kraftdivergenzen, die Spannungssymmetrie, die Quelle bei allgemeinem Schaltverlauf, ihre lokale Erhaltung sowie Wellengleichung, Spurumkehr und Eichterm symbolisch. Es handelt sich um klassische Elastodynamik und linearisierte Gravitation. Reproduzierbar mit `wolframscript -file op5_j_umschaltung_ruhelagen.wl`.
