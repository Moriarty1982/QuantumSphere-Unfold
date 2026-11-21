# OP5 – Zwei spannungsfreie Ruhelagen für die statische Auslese

21. November 2026. Analytische Erkundung im Materieframe M. Zwei überlagerte elastische Komponenten erhalten jeweils einen internen Zustandsparameter, der zwischen zwei kompatiblen Ruhelagen unterscheidet. Gesucht ist ein stationäres A/B-Paar mit der bisherigen linearen Higgsquelle und kompakter gewöhnlicher Gravitationsänderung bis zur zweiten Ordnung in der Auslenkung. Die Gravitation wird dabei nur in erster Ordnung in $G$ ausgewertet.

## Vorwissen geprüft

Die [dynamische Gegenbewegung](OP5_J_Dynamische_Gegenbewegung.md) liefert das longitudinale Plateau und den linearen Auslesekontrast. Der [Reservoirabgleich](OP5_J_Reservoir_Quadrupolabgleich.md) identifiziert die quadratische Dichte aus dem Materialtransport. Die [Saint-Venant–Kirchhoff-Halterung mit Paarfeder](OP5_J_Hyperelastische_Halterung.md) hat in zweiter Ordnung ein positives Piola-Spurmittel, das einen kompakten stationären Abgleich in diesem Modell ausschließt. Die Suche in Vorab-Notizen, Rundennotizen und OP5-Analysen nach Eigenverformung, zentraler Feder, Biot-Dehnung und kubischer Elastizität ergab für das vorliegende Profil keinen Abgleich mit zwei kompatiblen spannungsfreien Ruhelagen. Die Erkundung gehört zur lokalen Messschnittstelle von OP5 im [Gesamtbild](../../../wiki/Gesamtbild.md). I3 betrifft eine eigenständige kosmologische Bestandsdynamik.

## Materieller Träger der Ruhelage

In jeder der beiden Komponenten sei die positive Referenzmassendichte $\rho_a$ im Bereich der Störung konstant. Beide Komponenten können auf einen endlichen Träger mit freiem Rand beschränkt werden. Alle Formänderungen liegen im Inneren. Wir verwenden das idealisierte überlagerte Kontinuum aus der Vorarbeit. Die Komponenten seien im Modell mechanisch unabhängig und trügen je einen lokalen skalaren Freiheitsgrad $q_a$ mit positiver Trägheit $I_a$ pro Referenzvolumen. Für die vorzugebende kompakte Endverschiebung $d_a(X)$ setze
$$
F_{a,*}(X,q_a)=I+q_a\nabla_X d_a,\qquad
E_a(F_a,q_a)=\tfrac12(F_a^{\mathsf T}F_a-F_{a,*}^{\mathsf T}F_{a,*}).
$$
Für hinreichend kleine $d_a$ in $C^1$ sind die beiden Endabbildungen glatte Diffeomorphismen und nahe $I$. Gewählt wird die materielle Energie pro Referenzvolumen
$$
W_a=\tfrac12 E_a:\mathsf C_a E_a+V_a(q_a),\qquad
V_a(q)=\kappa_a q^2(1-q)^2,\quad \kappa_a>0 .
$$
Der Elastizitätstensor $\mathsf C_a$ ist symmetrisch und positiv definit auf symmetrischen Dehnungen. Man kann wie zuvor $\mathsf C_2=c\mathsf C_1$ wählen. Hier bezeichnet $c>0$ das Steifigkeitsverhältnis. Die Referenzmetrik $F_{a,*}^{\mathsf T}F_{a,*}$ ist an jedem räumlich konstanten $q_a$ die Metrik der expliziten Abbildung $X\mapsto X+q_a d_a(X)$. Sie ist damit kompatibel. Die konkrete Schaltvariable und die beiden Zielmetriken sind Modellannahmen. Zum elastischen Formalismus mit veränderlicher natürlicher Konfiguration siehe [Lubarda und Hoger, Abschnitt 8](https://newmaeweb.ucsd.edu/~vlubarda/research/pdfpapers/ijss-02.pdf).

Aus $P_a=F_a\mathsf C_a E_a$ folgt ein symmetrischer Cauchy-Stress $\sigma_a=(\det F_a)^{-1}P_aF_a^{\mathsf T}$. Die Ruhelagen $q_a=0$, $x_a=X$ und $q_a=1$, $x_a=X+d_a$ haben beide $P_a=0$, $W_a=0$ und $\partial_{q_a}W_a=0$. Dies gilt auch für die quadratische Variation der räumlichen Spannung entlang dieser beiden Familien. Die Volumenkräfte und Randtraktionen sind null. Ein gesonderter Kraftdipol zwischen den Komponenten entfällt, da die Zielform über eine lokale Materialmetrik erreicht wird. Der symmetrische Spannungstensor bilanziert das Drehmoment der Materialkräfte. Das Modell setzt gleiche Ruheenergie pro materiellem Massenelement in beiden Zuständen und keine Beiträge technischer Leitungen voraus.

Mit kinetischer Energie $\rho_a|\dot x_a|^2/2+I_a\dot q_a^2/2$ kann eine generalisierte Kraft $\tau_a$ auf den internen Skalar wirken. Im Materialchart gelten $\rho_a\ddot x_a=\operatorname{Div}P_a$ und $I_a\ddot q_a=-\partial_{q_a}W_a+\tau_a$. Multipliziert man die Gleichungen mit $\dot x_a$ und $\dot q_a$, so folgt für die Summe $\mathcal E_a$ aus kinetischer und potenzieller Energie
$$
\partial_t\mathcal E_a
  =\operatorname{Div}_X(P_a^{\mathsf T}\dot x_a)+\tau_a\dot q_a .
$$
Die Barriere des internen Potentials beträgt $\kappa_a/16$ pro Referenzvolumen bei $q_a=1/2$, zusätzlich zu gegebenenfalls vorhandener elastischer und kinetischer Energie. Für eine Amplitudenfamilie mit quadratischer Potentialbarriere kann $\kappa_a$ proportional zum Quadrat der Zielamplitude gewählt werden. Bei freiem Rand und ruhenden Endzuständen ist die über den gesamten Körper und Übergang integrierte Nettoarbeit null.

Ein mitbewegter Arbeitsspeicher mit Energie $R_a$ pro Referenzvolumen kann den Port über $\dot R_a+\operatorname{Div}_X J_{\rm R,a}=-\tau_a\dot q_a$ versorgen. Bezeichne $K_a=\int P_a^{\mathsf T}\dot x_a\,dt$. Für beide ruhenden Endzustände gilt
$$
\Delta R_a=\operatorname{Div}_X\left(K_a-\int J_{\rm R,a}\,dt\right).
$$
Für einen Speicher ohne inneren Energietransport kann folglich trotz globaler Nullarbeit eine lokale Endenergieänderung auftreten. Eine hinreichende Bedingung für die Wiederherstellung der Speicherenergie pro Massenelement ist $\int J_{\rm R,a}\,dt=K_a$. Sein unveränderter mitbewegter Ruheenergieanteil muss dann bereits in $\rho_a$ enthalten sein. Diese Bilanz bestimmt eine Anforderung an die Energieversorgung. Eine Umschalttrajektorie und ein Speicher mit diesem Fluss und verschwindendem zusätzlichen Endstress sind für eine Apparatur noch herzuleiten.

## Rückwärtsrechnung für die gewöhnliche statische Quelle

Schreibe $u=\nabla\varphi$ mit glattem kompaktem $\varphi$, $v=-u/c$ und $B_\rho=\rho_1+\rho_2/c^2$. Behalte aus der Federvariante die beiden ersten Verschiebungen bei und stelle die Endlagen auf
$$
d_1=\epsilon u,\qquad d_2=\epsilon v+\epsilon^2 b,\qquad
b_i=\frac{B_\rho}{2\rho_2}\partial_j(u_i u_j).
$$
Aus der Massenerhaltung ergibt der Pushforward jeder Referenzdichte in den gemeinsamen Raum auf dem Plateau
$$
\delta\rho^{(1)}=(\rho_2/c-\rho_1)\Delta\varphi,\qquad
\delta\rho^{(2)}=-\rho_2\nabla\cdot b+\tfrac12B_\rho\partial_i\partial_j(u_i u_j)=0.
$$
Die Vorzeichen folgen durch Taylorentwicklung einer Testfunktion entlang der beiden Endabbildungen und partielle Integration. Der Koeffizient $b$ ist kompakt. Seine Form wird durch den zuvor identifizierten quadratischen Transportterm bestimmt. Da die beiden Komponenten auf dem Plateau ruhen und ihre gespeicherte Energie und ihr Cauchy-Stress in den beiden Zuständen gleich null sind, besteht die Differenz des mechanischen Spannungstensors nur aus $\delta T^{00}=\delta\rho$ in Einheiten mit Lichtgeschwindigkeit eins. Dieser statische symmetrische Tensor ist erhalten. Jede Änderung der stationären Ruheenergie eines externen Antriebs wäre ein separater Beitrag.

Mit der räumlich abklingenden Randbedingung hat $\Delta\delta\Phi=4\pi G\delta\rho$ daher die kompakte Lösung
$$
\delta\Phi
= 4\pi G\,\epsilon(\rho_2/c-\rho_1)\varphi
\quad\text{bis einschließlich Ordnung }\epsilon^2.
$$
Dies ist in linearer Gravitation zugleich der Befund für die statische mechanische Quelle im vollen Tensor, da $\delta T^{0i}=\delta T^{ij}=0$ auf dem Plateau. Die gewöhnliche linearisierte Außenkrümmung dieses A/B-Unterschieds verschwindet außerhalb des Trägers von $\varphi$. Die Selbstgravitation der Materialien in der Elastizitätsgleichung und Terme höherer Ordnung in $G$ liegen außerhalb dieser Näherung.

## Bedeutung für die Messung

Für $\rho_2\ne c\rho_1$ bleibt die lineare Dichtevariation lokal vorhanden. Im restmassendominierten W2-Vergleich bleibt damit die lineare Higgsquelle $-\delta\rho^{(1)}/v_{\rm H}$ dieselbe wie in der Federvariante. Wählt man deren Plateauprofil, bleibt unter der angenommenen Higgs–OP5-Kopplung auch der berechnete lineare Achsenkontrast erhalten. Der gewöhnliche Effekt kann **innerhalb** des Profils weiter zur Auslese beitragen. Eine außen platzierte Gravimetermessung prüft im stationären Vergleich den mechanischen Außenbeitrag. Eine Sonde im Profil braucht zusätzlich eine Kalibrierung des gewöhnlichen Binnenfeldes. Die Aussage betrifft die statischen Endzustände. Retardierte Schalttransienten, die mechanische und energetische Bilanz eines tatsächlichen Antriebs, die Feld- und Bindungsenergien der gesamten Apparatur, die native Kopplung, freie J-Ausbreitung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_spannungsfreie_ruhelagen.wl) · [Tatsächliche Ausgabe](op5_j_spannungsfreie_ruhelagen.txt) · [Laufmanifest](op5_j_spannungsfreie_ruhelagen.json)

Wolfram prüft Piola-Differentiation, Spannungssymmetrie, die beiden Minima, die Barrierenhöhe, die Dichtekoeffizienten und die Poisson-Gleichung symbolisch. Die schwache Form kontrolliert den Materialtransport unabhängig über die Entwicklung der Testfunktion. Reproduzierbar mit `wolframscript -file op5_j_spannungsfreie_ruhelagen.wl`. Der Einsatz eines Quantenschaltkreis-Simulators wurde erwogen. Die Rechnung ist klassische symbolische Mechanik.
