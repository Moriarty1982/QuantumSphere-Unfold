# OP5: Quell- und Bindungsstress eines gebundenen Paars

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 in einem Materie-Schwerpunktsystem. Die [gerade Auslese](OP5_Gerade_Dipolauslese.md) zeigt positive Maxwell-Außenfeldenergie bei verschwindendem orientiertem Dipolmittel. Der Feldanteil allein hat isotrop gemittelt $p=\rho/3$. Hier werden im [gebundenen Zweikörpervergleich](W2_Quantendipol.md) die fehlenden Quell- und Bindungsanteile auf führender nichtrelativistischer Ordnung ergänzt. Dies ist weder eine vollständige W2-Lösung noch ein kosmologischer Datentest für [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md).

## Integrierter Stress der beiden Felder

Behandle die Foki als schwere Punktquellen im statischen Feldproblem. Ihre Einzelselbstenergien und die zugehörigen internen Spannungen gehören zur Definition der renormierten isolierten Massen $M_1,M_2$. Wir rechnen nur die Wechselwirkungsbeiträge bei $R>0$. Die Feldantwort wird anschließend in der führenden instantanen Näherung als Funktion des relativen Abstands $R$ ausgewertet. Die [Fokusabstandsrechnung](W2_Fokusabstand.md) ergibt

$$
V(R)=-\frac{A}{R}-\frac{Be^{-mR}}R,\qquad A>0,\quad B\ge0,\quad m>0.
$$

Für die elektrische J-Kopplung ist die Spur des räumlichen Maxwell-Stresses die elektrische Energiedichte. Der Kreuzterm zweier entgegengesetzt geladener Quellen ist daher
$$
\mathcal S_J(R)=\int T^{ii}_{J,\mathrm{Kreuz}}\,d^3x
=\int \mathbf E_1\cdot\mathbf E_2\,d^3x
= -A/R .
$$

Für den radialen Higgsanteil schreibe $\eta=\eta_1+\eta_2$ und verwende $K_m=e^{-mr}/(4\pi r)$ sowie $\eta_i=-s_i K_m(\cdot-\mathbf R_i)/Z_h$. Hier sind $s_i$ die skalaren Quellstärken und $Z_h>0$ die Gradientennorm. Die Spur des statischen, quadratischen skalaren Feldstresses ist $-Z_h(|\nabla\eta|^2+3m^2\eta^2)/2$. Ihr Kreuzterm ergibt

$$
\begin{aligned}
\mathcal S_h(R)
&=-Z_h\int\big(\nabla\eta_1\cdot\nabla\eta_2+3m^2\eta_1\eta_2\big)\,d^3x\\
&=-\frac{s_1s_2}{Z_h}\big[K_m(R)+2m^2(K_m*K_m)(R)\big]\\
&=-B\frac{(1+mR)e^{-mR}}R .
\end{aligned}
$$

Für die zweite Zeile nutzt man die Greensche Gleichung und partielle Integration. Für die dritte gilt $K_m*K_m=-\partial_{m^2}K_m$, sichtbar durch Differenzieren von $(|\mathbf k|^2+m^2)^{-1}$ im Fourierraum. Hier ist $B=s_1s_2/(4\pi Z_h)$. Die Kopplungsenergie der skalaren Quellen zählt bei der Gesamtenergie mit. Ihr Beitrag zum räumlichen kinetischen Quellstress durch die veränderte Ruhemasse ist von höherer nichtrelativistischer Ordnung.

## Der Quellenstress schließt die Virialbilanz

Im Schwerpunktsystem hat der kinetische Teil der Quellen die integrierte Spur $\mathcal S_{\rm Quellen}=2\langle K\rangle$ mit $K=\mathbf p^2/(2m_r)$ und der reduzierten Masse $m_r$. Die beiden Feldkreuzterme ergeben zusammen $-RV'(R)$. Für einen stationären gebundenen Zustand gilt aus der Erwartung des Kommutators der symmetrisierten Dilatation mit $K+V$

$$
2\langle K\rangle=\langle RV'(R)\rangle,\qquad
\langle\mathcal S_{\rm Quellen}+\mathcal S_J+\mathcal S_h\rangle=0.
$$

Die Kommutatorrechnung gilt für Zustände mit den erforderlichen endlichen Momenten und ohne Randterm. In einem isotropen Ensemble ist der gemittelte räumliche integrierte Stress ein Vielfaches der Identität. Die verschwindende Spur macht deshalb den integrierten isotropen Druck des vollständigen Zweikörpervergleichs null. Das setzt ruhende Schwerpunkte voraus. Schwerpunktsbewegung und Wechselwirkungen zwischen verschiedenen Paaren wären eigene Druckbeiträge.

Die positive Feldenergie außerhalb einer Schnittkugel ist damit kein separater Materiedichtebeitrag. Im Coulomb-Grenzfall ist beispielsweise die Grundzustands-Bindungsenergie $E_{\rm bind}=-m_r A^2/2$, obwohl die elektrische Außenenergie positiv ist. Mit schwacher Yukawa-Korrektur ist der zusätzliche Grundzustandsterm $-B/[a_0(1+m a_0/2)^2]$ erster Ordnung, $a_0=(m_r A)^{-1}$. Er folgt durch Integration mit der Coulomb-Dichte $|\psi_{1s}|^2=e^{-2R/a_0}/(\pi a_0^3)$.

## Grenze für die skalare Materieauslese

Für ein verdünntes isotropes Ensemble solcher gebundenen Einheiten, mit physischer Anzahldichte $n$ und vernachlässigbarer Schwerpunktsgeschwindigkeit, ist im Modell $\rho_{\rm Paar}=n(M_1+M_2+E_{\rm bind})$ und der interne Druck in dieser Ordnung null. Das zeigt, welche Kombination aus Quell- und Bindungstermen für eine materieartige Bilanz nötig ist. Es liefert keine Häufigkeit gebundener Einheiten, keine Vorhersage der renormierten Quellmassen und keine epochemäßige Fixierung von $\Omega_M=\rho_M/\rho_{\rm crit}$. Die Paaranzahl könnte sich in einem dynamischen Modell außerdem durch Bildung oder Zerfall ändern.

Für H96 fehlt daher weiterhin die hergeleitete Zuordnung und Normierung der vollständigen gravitativen Materiedichte. Ein dauerhaft orientierter Dipol ist für diesen skalaren Vergleich entbehrlich. Die signierte native Randwirkung bleibt separat offen. I3 setzt weiterhin eigenständige Überschussdynamik voraus.
