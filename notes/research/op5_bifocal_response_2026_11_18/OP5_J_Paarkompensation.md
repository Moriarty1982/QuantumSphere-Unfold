# OP5 — Kontinuierliche Kompensation der Paarmodulation

20. November 2026. Analytische Erkundung im Materieframe M. Vorausgesetzt sind der lineare statische Yukawa-Kern bei bekannter Vermittlermasse $m>0$ und eine Dichtequelle in freier flacher Geometrie. Die Geometrie beschreibt einen statischen Antwortabgleich und eine anschließende formale Erhaltungsrechnung.

## Vorwissen geprüft

Die [Paarmodulation](OP5_J_Gebundene_Paare_Spannung.md) erfüllt das integrierte Spannungsmoment, lässt aber bei gleichsinniger Verkürzung ein Yukawa-Außenfeld. Der [Kontrollkontrast](OP5_J_Kontrollkontrast.md) konstruiert kompakte Antworten. Die [Spannungsbilanz](OP5_J_Spannungsbilanz.md) gibt das einzuhaltende Moment vor. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt die Konstruktion vor der realen J-Messabbildung und der H96-Dichtenormierung. Rückwärts wird eine Feldänderung gesucht, die den Paarbeitrag in einem Kernbereich belässt, außen verschwindet und das vorgegebene Moment erhält. Für I3 liefert dies weiterhin keine Populationsdynamik.

## Lokalisieren der Antwort

Schreibe $L_m=1-\Delta/m^2$, $f_p$ für die führende Ruhemassenänderung der glatten, kompakten Paarprofile und $u_p=G_m*f_p$. Wähle eine glatte kompakte Funktion $0\le\eta\le1$, die auf einer Umgebung aller Paarquellen gleich eins und in den Apparaturregionen null ist. Ihr Träger liegt längs im Inneren der Messstrecke. Eine rotationssymmetrische Wahl um die Strahlachse genügt. Dann gilt
$$
L_m(\eta u_p)=f_p-\frac{2\nabla\eta\cdot\nabla u_p+u_p\Delta\eta}{m^2}.
$$
Die zusätzliche Dichte liegt in der Übergangszone der Fensterfunktion. Die Antwort ist exakt null außerhalb ihres Trägers und belässt $u_p$ im Kern. Am Ort der Paarquellen wird deren Ruhemassenänderung also beibehalten.

## Zwei Ringprofile erhalten Masse und Moment

Definiere die Quermomente $J_0[v](z)=\int v(\mathbf b,z)d^2b$ und $J_2[v](z)=\int |\mathbf b|^2v(\mathbf b,z)d^2b$. Wähle zwei glatte normierte radiale Ringprofile $w_1,w_2$ mit getrennten Trägern außerhalb des Kerns und des Strahls. Ihre zweiten Momente $b_1,b_2$ unterscheiden sich. Wähle ein glattes, längs kompaktes Zielmoment $p_2(z)$ mit $\int p_2(z)dz=-2Qs(t)$, wobei $Q$ aus dem früheren Kontrollprofil stammt. Setze
$$
\begin{aligned}
h_0&=J_0[\eta u_p], & h_2&=J_2[\eta u_p]-p_2,\\
\alpha&=(b_2h_0-h_2)/(b_2-b_1),&
\beta&=(h_2-b_1h_0)/(b_2-b_1),\\
\psi&=\eta u_p-\alpha(z)w_1(\mathbf b)-\beta(z)w_2(\mathbf b),&
f&=L_m\psi .
\end{aligned}
$$
Damit sind $J_0[\psi]=0$ und $J_2[\psi]=p_2$. Zugleich $J_0[f]=(1-\partial_z^2/m^2)J_0[\psi]=0$. Wegen $\Delta_\perp|\mathbf b|^2=4$ gilt $J_2[f]=(1-\partial_z^2/m^2)p_2$, da der Term aus $J_0[\psi]$ verschwindet. Das integrierte transversale Moment ist folglich $-2Qs(t)$. Die Änderung des zweiten Längsmoments ist null. Werden die Paare in vierzähliger Symmetrie um die Messachse und mit Spiegelung in den beiden Querkoordinaten gewählt, bleiben die gemischten Momente null und $\int x^2 f=\int y^2 f=-Qs(t)$.

Die gesamte Kompensationsdichte ist $f-f_p$. Sie liegt in der Fenster-Übergangszone und in den äußeren Ringträgern. Weil auch $J_0[f_p]=0$ bei einer rein transversalen Paarverschiebung unveränderter Konstituenten gilt, besitzt sie in jeder Querebene Gesamtintegral null. Mit einer ausreichend großen gemeinsamen kompakten Grunddichte auf dem Träger der Kompensation können beide Dichtezustände nichtnegativ gehalten werden. Die Kompensationsänderung ist im Allgemeinen vorzeichenwechselnd.

Auf der Strahlachse ist $\psi=\eta u_p$. Ein konkreter positiver Kontrast entsteht mit quer orientierten Paaren, deren Zentren auf der Strahlachse liegen. Je eine Paarachse in $x$- und $y$-Richtung pro Zentrum erzeugt die verwendete Symmetrie. Für radial symmetrische Konstituenten mit Radius kleiner als die halbe Endseparation liegt die Achse stets außerhalb der Teilchenprofile. Bei Verkürzung sinkt der Abstand jedes Konstituenten von jedem Achsenpunkt. Die äußere radiale Yukawa-Antwort einer positiven Konstituentendichte ist streng fallend mit dem Abstand. Daher ist $u_p(0,z)>0$, wenn die Paare kürzer sind. Das integrierte Achsensignal mit nichttrivialem $\eta\ge0$ bleibt positiv. Die Ringe ändern weder diesen Beitrag noch die statische Nullantwort in den Apparaturregionen. Wie zuvor kann ein seitlich ausreichend weit verschobenes Gesamtsystem im Modell eine Nullkontrolle außerhalb des Strahls liefern.

## Formale Erhaltungsrechnung

Für das volle zeitabhängige Profil $f(t,x,y,z)$ aus den vorigen Abschnitten gibt es einen kompakten transversalen Erhaltungstensor. Es genügen Geradheit in $x$ und $y$ sowie $J_0[f]=0$. Setze $g(t,y,z)=\int f(t,x,y,z)dx$ und wähle eine feste glatte gerade normierte kompakte Funktion $b(x)$. Zerlege $f=f_x+b(x)g$ mit $f_x=f-b(x)g$. Für jedes $t,y,z$ hat $f_x$ verschwindendes nulltes und erstes $x$-Moment. Entsprechend hat $g$ verschwindendes nulltes und erstes $y$-Moment. Daher sind
$$
K_{xx}(t,x,y,z)=\int_{-\infty}^{x}(x-u) f_x(t,u,y,z)\,du,\qquad
K_{yy}(t,x,y,z)=b(x)\int_{-\infty}^{y}(y-u)g(t,u,z)\,du
$$
kompakt und erfüllen $\partial_x^2 K_{xx}+\partial_y^2 K_{yy}=f$. Mit den übrigen $K_{ab}=0$, $a,b=x,y$, ergibt sich
$$
\delta T^{00}=f,\qquad
\delta T^{0a}=\delta T^{a0}=-\partial_t\partial_b K_{ab},\qquad
\delta T^{ab}=\partial_t^2 K_{ab},\qquad
\delta T^{z\mu}=0.
$$
Die vier Divergenzen verschwinden. Damit erfüllt dieser Vergleich die Erhaltung und über die alte Momentidentität auch die notwendige integrierte Spannungsbilanz. Der formal konstruierte Strom kann andere Gebiete durchqueren als der Träger der momentanen Dichteänderung. Er ist kein separates Materialgesetz für die Ringe.

## Kontrolle und offene Voraussetzungen

[Wolfram Language](op5_j_paarkompensation.wl) prüft die Produktregel für $L_m$, die beiden Momentgleichungen und die Divergenzen des Tensors. Eine Quantenschaltung ist für diese Feld- und Kontinuumsrechnung nicht definiert. Die Konstruktion legt eine steuerbare Dichteänderung von außen fest. Native Ansteuerung, Dynamik und Wechselwirkungsenergie der Kompensationsreservoirs, endliche Schaltfrequenzen, die reale Apparaturantwort und H96 bleiben offen.

### Ausgabe des Wolfram-Laufs

Die gedruckte Liste in linearer Darstellung enthält: `{0, {a -> -( (-h2 + h0 j2)/(j1 - j2)), b -> -( (h2 - h0 j1)/(j1 - j2))}, {0, 0}, 0, {0, 0}}`. Dabei sind `j1,j2` die zweiten Ringmomente und `a,b` die Ringkoeffizienten. Der separate Rückgabewert des abschließenden `Print` war `Null`.
