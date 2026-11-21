# OP5 – Phasenangepasste Konversion, Pilottransfer und Radialgradient

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Konverterlast und lokale Ringrechnung](OP5_J_Konverter_Leerkoerper_Ringfehler.md) lässt den starken A/J-Durchgang, den komplexen Leerkörpertransfer und eine besser konditionierte gewöhnliche Messgröße offen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Verteilte Konversion unter schwacher Kopplung

Betrachte ein idealisiertes verlustfreies Hüllkurvenmodell mit Kopplung $g$, reeller Restverstimmung $\Delta$, Länge $\mathcal L$ und Ausbreitungsmatrix
$$
\begin{pmatrix}\Delta/2 & g\\g&-\Delta/2\end{pmatrix}.
$$
Die Konversionswahrscheinlichkeit ist $g^2\sin^2(\mathcal L\sqrt{g^2+\Delta^2/4})/(g^2+\Delta^2/4)$. Für den zuvor angenommenen H/HCl-Mischfaktor $x=10^{-3}$ setze als optimistischen Kopplungsmaßstab $g_0 L_0=(U_0^2-A_0^2)x/(2A_0)$ aus der schwachen Feldumwandlung ein. Dieser Schritt überträgt einen Modellparameter und berücksichtigt keine zusätzliche Streuung oder Variation des Modenprofils. Im [100-MHz-Schichtbeispiel](OP5_J_Ruecklauf_Toleranzen.md) gilt $L_0\simeq17{,}20$ mm, $g_0 L_0\simeq0{,}003142$ und unabgeglichen $\Delta L_0=2\pi$. Bei dieser festen Verstimmung bleibt die Konversionswahrscheinlichkeit unter $1{,}001\cdot10^{-6}$ für jede Länge.

Ein idealer räumlicher Abgleich kann $\Delta(E_0)$ entfernen. Bei unverändertem effektivem Kopplungsmaßstab wäre die erste volle Konversion $\mathcal L=\pi/(2g_0)\simeq8{,}60$ m. Wenn nur der resonante Fourieranteil einer reellen Sinusmodulation mit halber Amplitude verfügbar ist, sind es im Hüllkurvenmodell etwa $17{,}20$ m. Das setzt einen Abgleich ohne zusätzliche Verlust- oder Reflexionskanäle voraus. Bei konstantem reellem A-Index ist die durch die illustrative massive Dispersion verbleibende Abweichung von $(\kappa-k_J)L_0$ über das bisherige Band durch $1{,}814\cdot10^{-10}$ begrenzt. Dafür wurden die erste Ableitung am Zentrum und eine uniforme zweite Ableitungsgrenze eingesetzt. Im Sinusfall liegt die entsprechende Verstimmung relativ zu $2g$ unter $5{,}773\cdot10^{-8}$.

Für die zuvor geforderte A-Leckamplitude $p=9\cdot10^{-6}$ ist bei fester Verstimmung notwendig, dass $|\Delta|/(2|g|)\le p/\sqrt{1-p^2}$, aus dem maximalen Kontrast der Hüllkurvenlösung. Wird der gesamte Fehler nur einer verbleibenden Indexabweichung zugerechnet, ergibt das einen Indexrahmen von rund $1{,}80\cdot10^{-12}$ beim vollen Kopplungsmaßstab und $9{,}00\cdot10^{-13}$ beim halben. Bei exakt passender Phase darf der relative Fehler von $g\mathcal L$ um $\pi/2$ höchstens rund $5{,}73\cdot10^{-6}$ betragen. Die beiden Einzelbudgets sind nicht gleichzeitig voll nutzbar. Die bisherige reelle Indexgrenze $2{,}5\cdot10^{-7}$ reicht für den Entwurf allein nicht aus.

Auch die frühere Verlustgrenze darf nicht unverändert aus der kurzen Schicht übernommen werden. Für reinen A-Amplitudenverlust $\alpha=k_A\Im n$ und exakten Phasenabgleich hat das Modell bei $r=\alpha/(2g)>1$ die J-zu-A-Amplitude $e^{-r g\mathcal L}\sinh(g\mathcal L\sqrt{r^2-1})/\sqrt{r^2-1}$. Bei $\Im n=2{,}5\cdot10^{-7}$ und vollem Kopplungsmaßstab ist $r\simeq1{,}25$. Selbst die über alle Längen optimierte Amplitude liegt dann bei etwa $0{,}315$. Damit kann die alte erlaubte Verlustspanne keinen verlustfreien Konverter zertifizieren. Ein anderer Resonator oder ein adiabatischer Konverter wäre ein eigenes Modell. Eine unabhängige Kalibrierung des tatsächlichen J-Porttransfers bleibt auch bei idealem Phasenabgleich nötig.

## Getrennter Modenabgriff und Gain-Pilot

Schreibe im Leerkörper- oder Markerzustand $j$ einen kohärenten Direktabgriff mit gezielt invertierter J-Projektion als $M_j^\pm=g_j B_j(1\pm r_j)+n_j^\pm$. Komplexes Mitteln schätzt $g_jB_j$; die Halb-Differenz diagnostiziert den ungeraden projizierten Anteil. Bei tatsächlicher negativer Stellung $-e^{i\delta_j}$ kostet der Phasenfehler höchstens $|r_j\sin(\delta_j/2)|$ relativ zu $g_jB_j$. Unmarkierte oder bei der Umkehr unveränderte Kopien bleiben im Mittel.

Ein zweiter Pilot $P_j=g_j a_j$ kann den komplexen Gaintransfer liefern, wenn $a_1/a_0$ unabhängig bekannt ist und der Pilot ab derselben Referenzebene dieselbe Messkette durchläuft. Dann lautet der Direktstandardschätzer
$$
\widehat B_1
=\widehat B_0\frac{\widehat M_1\widehat P_0}{\widehat M_0\widehat P_1}
\,\widehat{(a_1/a_0)}.
$$
Für sechs relative komplexe Eingabefehler von höchstens $e$ genügt die Hülle $[(1+e)^4+(1+e)^2-2]/(1-e)^2$. Bei $e=5\cdot10^{-9}$ sind das rund $3{,}0001\cdot10^{-8}$. Wenn $|r_j|\le4\cdot10^{-6}$ und $|\delta_j|\le10^{-3}$ rad, verbraucht die Phasenumkehr rund $2\cdot10^{-9}$ pro Zustand. Im früheren Achtphasenbudget kann mit diesen Bedingungen ein sichtbarer Echo-Rest getrennt geprüft werden, wenn $|\widehat E/\widehat B_1-1|\le5{,}3068\cdot10^{-8}$. Ohne unabhängiges Pilotverhältnis bleiben alle Daten unter $(B_j,a_j,g_j)\mapsto(k_j B_j,k_j a_j,g_j/k_j)$ invariant. Bauteile vor der Pilotebene sowie gerade Echoanteile bleiben separate Prüfgrößen.

## Gewöhnlicher Radialgradient und Annulusbreite

Für eine gewöhnlich-selektive integrierte Beschleunigung $\bar a_r=-\partial_r\bar\Phi$ können kalibrierte Intervallmittel direkt zu $\bar\Phi(0)-\bar\Phi(R_c)$ integriert werden. Uniformer absoluter Beschleunigungsfehler $\eta_a$ kostet bei unabhängig bestätigtem reinem $b_4$-Träger $a<u<b$ höchstens $R_c(\sqrt b-\sqrt a)\eta_a$. Ohne gesicherten Träger ist die volle Integrationslänge einzusetzen. Beiträge von $b_0,b_2$, endlichem Längsfenster und Außenreferenz müssen separat begrenzt werden.

Bei unabhängigen lokalen relativen Fehlern ist die Verstärkung dagegen durch die Totalvariation des normierten Potentials $P=H^4 f/576$ bestimmt, mit $H=\partial_u(u\partial_u)$ als radialer Operator in Flächenkoordinate. Für das kompensierte Profil gilt $P=1$ im Kern $u\le a$, $P=0$ außerhalb $u\ge b$ und $\int_0^b u^jP(u)\,du=0$ für $j=0,\ldots,4$. Die Momente folgen durch viermaliges Übertragen des selbstadjungierten $H$ auf die Monome, für das vierte Moment zusätzlich aus $\int f=0$. Für jedes Polynom $Q$ vom Grad höchstens fünf folgt $\int_a^b QP'=-Q(0)$. Die Wahl $Q(u)=T_5((2u-a-b)/(b-a))$ ergibt
$$
\operatorname{TV}(P)\ge T_5((a+b)/(b-a)).
$$
Für $(a,b)=(1/4,3/4)$ ist diese notwendige Mindestverstärkung $362$. Nur die äußere Grenze auf $7/8$ zu verschieben senkt sie auf rund $194{,}69$. Mit kleinerem Kern und breiterem Übergang $(1/10,9/10)$ ergibt sich rund $16{,}016$. Die Grenzen gelten für diese Momentklasse und erlauben keine monotone Abnahme.

Für den bisherigen konkreten Beta-Übergang liefern rationale Bernstein-Grenzen auf 32 Zellen TV-Obergrenzen von rund $3{,}286\cdot10^8$, $1{,}588\cdot10^8$ beziehungsweise $1{,}516\cdot10^7$ für diese drei Geometrien. Die Gradientenmessung vermeidet die zusätzliche Laplace-Ableitung der Dichteauswertung. Die Kompensation bleibt für unabhängige lokale relative Fehler in diesem Entwurf trotzdem schlecht konditioniert. Gemeinsame Gainfehler skalieren die integrierte Nettogröße. Ein absolut kalibrierter gewöhnlicher Gradient oder ein anders geformtes Profil sind daher getrennt zu prüfen. Die tatsächliche gewöhnlich-selektive Messung, freie J-Ausbreitung, HCl/H-Portkondition, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte die gekoppelten Hüllkurvenzahlen, den Gewinntransfer und die Beschleunigungsgrenzen. Qiskit wurde für die klassischen Streu- und Potentialrechnungen erwogen.

[Wolfram-Skript](op5_j_phasenanpassung_pilot_gradient.wl) · [Tatsächliche Ausgabe](op5_j_phasenanpassung_pilot_gradient.txt) · [Laufmanifest](op5_j_phasenanpassung_pilot_gradient.json)
