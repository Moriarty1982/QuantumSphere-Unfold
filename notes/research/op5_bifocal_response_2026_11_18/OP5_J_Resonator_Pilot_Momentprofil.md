# OP5 – Resonatorbandbreite, lokaler Pilotabgriff und Momentprofil

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Phasenanpassungs- und Gradientenrechnung](OP5_J_Phasenanpassung_Pilot_Gradient.md) wird am Zweimodenresonator, an einer lokalen Pilotkalibrierung und an der Momentgrenze des gewöhnlichen Potentials fortgesetzt. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur lokalen Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Ein Zweimodenresonator verkürzt den Wandler auf Kosten des Bands

Betrachte zwei lineare, gekoppelte Moden bei gleicher Resonanzfrequenz mit zeitlicher Kopplungsrate $g$, externen Amplitudenraten $\kappa_A,\kappa_J$ und inneren Verlustraten $\alpha_A,\alpha_J$. Jede Mode koppelt nur an ihren eigenen Anschluss. Für gemeinsamen Frequenzabstand $\omega$ in Winkelfrequenzeinheiten ist die A/J-Konversionsamplitude bis auf einen bekannten Phasenfaktor
$$
S_{JA}=\frac{2\sqrt{\kappa_A\kappa_J}\,g}{(\kappa_A+\alpha_A-i\omega)(\kappa_J+\alpha_J-i\omega)+g^2}.
$$
Das Modell lässt eine kurze resonante Kopplungsstrecke zu, setzt die zeitliche Kopplungsrate und die beiden physisch zugänglichen Portmoden aber bereits voraus.

Im verlustfreien Fall erzwingt vollständige Konversion am Bandzentrum $\kappa_A\kappa_J=g^2$. Dann bleibt
$$
|S_{AA}|^2=\frac{\omega^4+\omega^2(\kappa_A-\kappa_J)^2}{4g^4+\omega^4+\omega^2(\kappa_A-\kappa_J)^2}.
$$
Symmetrische Extraktion minimiert den Leckbetrag bei jeder Frequenz. Für das Ziel $|S_{AA}|\le p$ folgt selbst in diesem besten synchron resonanten Fall am Bandrand
$$
g\ge|\omega_{\rm Rand}|\left[\frac{1-p^2}{4p^2}\right]^{1/4}.
$$
Mit $p=9\cdot10^{-6}$ und 100 MHz voller Bandbreite entspricht das etwa $g/(2\pi)=11{,}785$ GHz. Der frühere räumliche Kopplungsmaßstab aus dem Hüllkurvenmodell ergibt bei Umrechnung mit $v=c$ nur etwa $8{,}713$ MHz. Bei diesem Maßstab wäre die A-Leckamplitude am Bandrand selbst im symmetrisch angepassten verlustfreien Resonator etwa $0{,}998$. Diese Rechnung verwendet eine angenommene Umrechnung von räumlicher in zeitliche Kopplung. Eine andere Modenüberlappung, ein langsamerer oder schnellerer effektiver Transport oder ein Mehrresonatornetz erfordern einen eigenen Abgleich.

Bei reiner A-Dämpfung und symmetrischer externer Extraktion $\kappa_A=\kappa_J=\kappa$ maximiert $\kappa=g$ die Amplitude am Zentrum. Der Maximalwert ist $2g/(2g+\alpha_A)$. Beim bisherigen illustrativen Verlustverhältnis $\alpha_A/(2g)\simeq1{,}25$ liegt er bei rund $0{,}4445$. Die verbleibende A-Reflexion am Optimum liegt bei rund $0{,}5555$. Eine unsymmetrische Anpassung kann den Zentralwert ändern; die berechnete verlustfreie Bedingung zeigt bereits die Schwierigkeit des ganzen Bands für diesen Zwei-Resonator-Aufbau. Weder eine native J-Mode noch eine unabhängige physische Portnormierung folgt aus dem Resonatormodell.

## Lokaler Pilotabgriff mit eigener Referenz

Im [Pilottransfer](OP5_J_Phasenanpassung_Pilot_Gradient.md) war das komplexe Einspeiseverhältnis $a_1/a_0$ am Leerkörper und Marker unabhängig zu bestimmen. Ein lokaler gerichteter Abgriff $Q_j=h_jk_ja_j$ und ein kohärenter Referenzton $C_j=h_jd_j$ im selben Empfängerkanal liefern
$$
a_1/a_0=(Q_1C_0)/(Q_0C_1)\,\xi,\qquad \xi=(d_1/d_0)(k_0/k_1).
$$
Damit kürzt sich der lokale, auch zustandsabhängige Empfängergewinn $h_j$. Der kombinierte Referenz- und Abgriffquotient $\xi$ muss seinerseits unabhängig kalibriert sein. Ohne ihn erhalten die Ersetzungen $B_j,a_j\mapsto t_jB_j,t_ja_j$ sowie $g_j,k_j\mapsto g_j/t_j,k_j/t_j$ die vier idealen Datensätze aus Direktabgriff, Hauptpilot, lokalem Abgriff und Referenzton. Ein nominell gleich eingespeister Pilot beseitigt diese Freiheit erst nach vermessenem Moden- und Abgrifftransfer.

Die gemeinsame Schätzung des Marker-Direktwertes hat sechs komplexe Zähler- und vier Nennerfaktoren. Bei einer relativen Eingabegrenze $e$ reicht $[(1+e)^6+(1+e)^4-2]/(1-e)^4$. Ein richtungsabhängiger Abgriff mit zusätzlicher relativer Beimischung $\ell_j r_j$ aus der Rückwelle trägt im Quotienten höchstens $(z_0+z_1)/(1-z_0)$ bei, $z_j=|\ell_jr_j|$. Für $e\le2{,}5\cdot10^{-9}$, $|r_j|\le1{,}04\cdot10^{-4}$ und $|\ell_j|\le10^{-5}$ gibt die zusammengesetzte Grenze $2{,}7081\cdot10^{-8}$. Im bisherigen Achtphasenbudget bliebe eine normierte Anzeigedifferenz bis $5{,}5988\cdot10^{-8}$ für die separate Prüfung des sichtbaren Rücklaufs. Die einzelnen Grenzen setzen denselben komplexen Maßstab am realen Marker voraus.

Alternativ können separat kalibrierte vorwärts und rückwärts gerichtete Abgriffe $q_+=a^++\ell a^-$ und $q_-=\mu a^++a^-$ die Rückwelle rechnerisch entfernen. Dann ist $a^+=(q_+-\ell q_-)/(1-\ell\mu)$. Bei bekannten Leckkoeffizienten gehen absolute Abgriffsfehler mit $(\epsilon_++|\ell|\epsilon_-)/|1-\ell\mu|$ ein. Unbekannte Gain- oder Leckkoeffizienten gehören in einen zusätzlichen Transferrest.

## Das Potential direkt aus fünf Nullmomenten bauen

Sei $P$ das normierte gewöhnliche $b_4$-Potential mit $P=1$ im Kern bis $a=1/4$ und $P=0$ ab $b=3/4$. Die fünf Nullmomente der Vorarbeit bedeuten
$$
\int Q(u)\,dP(u)=-Q(0)\qquad(\deg Q\le5).
$$
An den sechs Chebyshev-Lobatto-Knoten $u_i=(a+b+(b-a)\cos(i\pi/5))/2$ erhält man eine atomare Ableitung mit Gewichten $-\ell_i(0)$, wobei $\ell_i$ die Lagrange-Polynome sind. Polynominterpolation prüft alle sechs Ableitungsbedingungen exakt. Die Gewichte alternieren entsprechend dem Chebyshev-Polynom. Ihre absolute Summe ist exakt $362$. Damit ist die frühere Untergrenze für diese Momentklasse scharf. Um glatte Profile anzunähern, rücke die Knoten nach innen, ersetze die einzelnen Atome durch disjunkte normierte glatte Kerne und löse die Momentgleichungen für deren Gewichte. Die Matrix geht im Grenzfall in die invertierbare Interpolationsmatrix über. Bei beliebig schmalen Kernen nähert sich die Totalvariation $362$. Das sagt nichts über hohe Ableitungen oder materielle Realisierbarkeit.

Für die bisherige **Selektivität des Achsenpotentials für $b_4$** reichen diese fünf Momente allein nicht. Schreibe $f=576 G^4P$, wobei $G$ der reguläre radiale Inversoperator von $H=\partial_u(u\partial_u)$ mit Dirichletwert null am Außenrand ist. Die Potenzmomente sichern Kompaktheit der Inversion und das Null-Quermoment. Tatsächlich ist $\int G^jP=(j!)^{-2}\int u^jP$ nach Wegfall der niedrigeren Momente. Damit verschwinden bei den vier Inversionsschritten die äußeren Flüsse. Auf der Achse ist $H^3f$ proportional zu $\int P\log u\,du$ und $H^2f$ zu $\int uP\log u\,du$. Dies folgt aus dem logarithmischen Achsenkern von $G$ und einem weiteren Schritt mit seinem selbstadjungierten Kern. Beide Größen müssen verschwinden, damit weder der $b_2$- noch der $b_0$-Term das gewöhnliche Achsenpotential verschiebt. Für die Ableitung $dP$ entspricht dies zusätzlich den Momenten $\int u\log u\,dP=\int u^2\log u\,dP=0$, weil die gewöhnlichen Potenzmomente bereits verschwinden. Im Kern hat die Inversion dann $f=u^4+c_0+c_1u$. Die beiden niederen Terme beeinflussen weder $H^2f$ noch $H^3f$ oder $H^4f$. Ein exakt vorgegebenes Trägerprofil $f=u^4$ wäre eine zusätzliche Anforderung.

Ein numerischer Acht-Knoten-Vergleich mit beiden logarithmischen Momenten ergibt eine atomare Totalvariation von rund $1{,}0753\cdot10^5$. Die zusätzliche Matrix ist für verschiedene positive Knoten invertierbar: Die sechste Ableitung eines Polynoms vom Grad höchstens fünf plus $\alpha u\log u+\beta u^2\log u$ ist $u^{-5}(24\alpha-12\beta u)$ und hat bei nichttrivialem Loganteil höchstens eine Nullstelle. Acht Knoten-Nullstellen würden nach Rolle mindestens zwei erzwingen. Glatte exakte Momentprofile lassen sich damit analog approximieren. Die Zahl ist ein konstruktiver Vergleich und kein nachgewiesenes Minimum der erweiterten Klasse. Sie verbessert die vorherige konkrete Beta-Form erheblich, lässt aber hohe lokale Gradientenverstärkung und unbekannte Anforderungen an die Ansteuerung zurück. Die gewöhnlich-selektive Messung, freie J-Ausbreitung, native Metrik und H96 bleiben offen.

Für die um beide Logmomente ergänzte Klasse gibt es auch eine strengere Untergrenze. Konstruiere ein Prüfglied $Q$ in der Basis $\{1,u,\dots,u^5,u\log(2u),u^2\log(2u)\}$ durch abwechselnde Werte an den acht Knoten und runde seine Koeffizienten auf rationales Raster $10^{-18}$. Das zulässige Moment bleibt $\int Q\,dP=-Q(0)$. Für die Normzertifizierung wird $\log(2u)$ auf $[1/4,3/4]$ als $\log(1+t)$ mit $t=2u-1$ bis Grad 44 entwickelt. Der absolute Rest ist höchstens $1/(45\cdot2^{44})$. Exakte rationale Bernstein-Koeffizienten auf 32 Teilintervallen begrenzen das resultierende Polynom. Einschließlich Logrest ergibt sich $\|Q\|_\infty<1{,}233525$ und $\operatorname{TV}(P)>87172{,}5$. Das numerische Acht-Knoten-Profil mit glatter Approximation liefert eine obere Vergleichsgröße von rund $107530$. Das Intervall bezieht sich auf die beiden zusätzlichen Achsenbedingungen und nicht auf weitere experimentelle Regularitätsanforderungen.

## Rechenkontrolle

Wolfram prüfte die Resonatoridentitäten und Bandwerte, das lokale Pilotbudget, die sechs exakten Polynom-Momente und den hochpräzisen Acht-Knoten-Vergleich. Qiskit wurde für diese klassischen Übertragungs- und Potentialrechnungen erwogen.

[Wolfram-Skript](op5_j_resonator_pilot_momentprofil.wl) · [Tatsächliche Ausgabe](op5_j_resonator_pilot_momentprofil.txt) · [Laufmanifest](op5_j_resonator_pilot_momentprofil.json)
