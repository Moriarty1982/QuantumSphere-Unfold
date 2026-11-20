# OP5: Gravitative Kalibrierung der Vermittlerreichweite

20. November 2026. Analytische Erkundung in M nach [PR #200](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/200). Die [Tomographie](OP5_J_Tomographische_Mehrdeutigkeit.md) liefert den gefalteten D-Antwortkörper und lässt Dichte und Reichweite gemeinsam variieren. Der [Gravitationsabgleich](OP5_J_Gravitationsabgleich.md) zeigt, wie korrelierte gewöhnliche Materie mithilfe eines Tracers unter bestimmten Voraussetzungen projiziert werden kann. Wir verbinden beide Rechnungen. Vorausgesetzt sind räumliche Karten auf demselben Zeitschnitt und in demselben Frame, eine bekannte räumliche Filterung und der lineare, statische Yukawa-Abgleich. Die Karten werden hier als Eingaben behandelt. Linsen-, Geschwindigkeits- oder Laufzeitrohdaten werden nicht rekonstruiert. Es erfolgt kein H96-Datenvergleich.

## Kalibrierung aus dem Kreuzspektrum

Auf einem Fouriermodus mit Betrag $q$ sei
$$
\widetilde U=C_\Delta F_m(q)\widetilde{\rho_D},\qquad
F_m(q)=\frac{m^2}{m^2+q^2},\qquad
\widetilde{\rho_G}=\widetilde{\rho_D}+\widetilde{\rho_{\rm sonst}}.
$$
Hier sind $U$ der tomographisch gedachte J–Licht-Antwortkörper, $\rho_D$ die D-Massendichte und $\rho_G$ die unabhängig rekonstruierte gravitative Materiedichte. Die bekannte räumliche Projektion und Filterung muss auf die gemeinsame Karte zurückgeführt sein. $C_\Delta$ enthält die physikalische Norm der Laufzeitdifferenz. Für die folgenden Verhältnisse gilt $C_\Delta\ne0$ und $m>0$.

Schreibe die übrigen Materiefluktuationen auf dem Modus als $s_B\widetilde B+\widetilde\epsilon$. $B$ ist ein separat gemessener Materietracer. Der unbekannte Koeffizient $s_B$ darf mit dem Modus variieren. Das Residuum $\epsilon$ sei spektral sowohl zu $U$ als auch zu $B$ unkorreliert. Definiere mit der Konvention $P_{XY}=\langle\delta\widetilde X\,\delta\widetilde Y^*\rangle$ und $P_{BB}>0$
$$
P_{XY\cdot B}=P_{XY}-\frac{P_{XB}P_{BY}}{P_{BB}}.
$$
Der Tracerterm kürzt sich aus dem partiellen Kreuzspektrum heraus. Für $P_{UU\cdot B}>0$ ergibt sich
$$
\mathcal B(q)=\frac{P_{U\rho_G\cdot B}}{P_{UU\cdot B}}
=\frac1{C_\Delta F_m(q)}
=\alpha+\beta q^2,\qquad
\alpha=C_\Delta^{-1},\quad \beta=(C_\Delta m^2)^{-1}.
$$
Die Gleichung verlangt keine Poisson-Verteilung. Sie setzt dieselbe lineare Yukawa-Antwort pro Masse im benutzten Bereich voraus. Ist $P_{UU\cdot B}=0$, ist das verbleibende J-Signal mit dem Tracer kollinear und der Modus liefert keine solche Kalibrierung. Ein korreliertes Residuum würde den Quotienten um $P_{U\epsilon\cdot B}/P_{UU\cdot B}$ verschieben; eine beobachtete Skalenabhängigkeit könnte also auch von der unvollständigen Materiebereinigung stammen.

Zwei verschiedene Beträge mit gültigem Quotienten bestimmen $\alpha,\beta$ und damit $C_\Delta=1/\alpha$, $m^2=\alpha/\beta$, sofern das Resultat endlich und $m^2>0$ ist. Ein zusätzlicher Betrag prüft die vorhergesagte Linearität in $q^2$. Wegen $F_m(0)=1$ folgt für absolut kalibrierte Karten $\bar\rho_D=\bar U/C_\Delta$. Reine Differenzdaten ohne absoluten J-Nullmodus bestimmen diesen Mittelwert weiterhin nicht.

Bei zwei unabhängigen J-Messungen $U_1=U+\eta_1$, $U_2=U+\eta_2$ kann im Nenner $P_{U_1U_2\cdot B}$ benutzt werden. Die Erwartungsidentität bleibt erhalten, wenn beide Messfehler weder mit dem Signal, der Gravitation und dem Tracer noch miteinander korreliert sind. Das entfernt in dieser Algebra den additiven Eigenbeitrag des J-Messrauschens; es löst keine Probleme durch unbekannte Filter oder systematische Phasenfehler.

## Kontrolle und Vergleich mit mehreren Polmassen

Als algebraische Kontrolle setze $m=2$, $C_\Delta=1/2$, $P_{UU}=9$, $P_{BB}=4$, $P_{UB}=3$ und $s_B=5$. Die partiellen Quotienten bei $q=1,3,5$ sind $2{,}5$, $6{,}5$ und $14{,}5$. Die ersten beiden ergeben $\alpha=2$, $\beta=1/2$ und damit $m^2=4$, $C_\Delta=1/2$. Der dritte Punkt stimmt mit der daraus folgenden Vorhersage überein.

Für mehrere statische Pole mit gleichem positivem Vorzeichen und nichtverschwindenden Gewichten lautet die Antwort allgemein $L(x)=\sum_i a_i/(x+t_i)$ mit $x=q^2$, $t_i=m_i^2>0$ und $a_i>0$. Die inverse Antwort ist dann konkav:
$$
\frac{d^2}{dx^2}\frac1{L(x)}
=\frac{2(L')^2-L L''}{L^3}\le0.
$$
Das folgt aus Cauchy–Schwarz mit $S_k=\sum_i a_i/(x+t_i)^k$, denn $L=S_1$, $-L'=S_2$, $L''=2S_3$ und $S_2^2\le S_1S_3$. Die Ungleichung ist strikt für wenigstens zwei verschiedene Massen mit positivem Gewicht. Bei insgesamt negativem Vorzeichen kann vor dem Vergleich das gemeinsame Vorzeichen herausgezogen werden. Gemischte Vorzeichen erlauben diese Folgerung nicht. Krümmung ist daher ein bedingter Hinweis gegen einen einzelnen Pol, sobald korrelierte Materiereste und Messfilter geeignet beschränkt sind.

Die Verbindung von J und Gravitation kann damit die statische Dichte-Reichweiten-Mehrdeutigkeit unter den angegebenen Voraussetzungen brechen. Sie liefert keine Populationsdynamik und kein garantiert messbares J-Signal. Ohne absolute Norm und kalibrierten Mittelwert lässt sich daraus auch keine D-Komponente für den H96-Datenvergleich gewinnen. H96 bleibt offen.
