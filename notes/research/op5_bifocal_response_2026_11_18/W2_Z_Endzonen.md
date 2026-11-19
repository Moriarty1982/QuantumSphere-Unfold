# OP5: Welche Endsteifigkeit ergibt ein abklingendes Außenfeld?

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Die [Einmodenrechnung](W2_Z_Segment.md) setzte eine Endsteifigkeit frei an. Der [Längenvergleich](W2_Z_Laengenskala.md) ergab eine Obergrenze von rund 0,0068 fm für starre Enden. Hier wird die Endsteifigkeit in einem expliziten Projektionsmodell aus der Außenlösung gewonnen. Die [Nambu-Endpunkte](W2_Z_Strang.md) werden weiterhin nicht als vollständige Feldlösung vorausgesetzt.

## Außenraum eliminieren

Setze für dieselbe kanonisch normierte Amplitude auf der ganzen Achse eine statische quadratische Energie
$$
\mathcal Q[f]=\int_{\mathbb R}\!\left(|f'|^2+V(x)|f|^2\right)dx,\qquad
V(x)=
\begin{cases}
-\mu^2,&0<x<R,\\
m_L^2,&x<0,\\
m_R^2,&x>R.
\end{cases}
$$

Dabei seien $m_L,m_R>0$. Die positiven Außenmassen sind Modellparameter. Der Ansatz setzt dieselbe Amplitude und dasselbe Gradientenmaß in allen drei Bereichen voraus. Bei festgehaltenen Übergangswerten $u=f(0)$ und $v=f(R)$ minimieren die abklingenden Lösungen $u e^{m_Lx}$ bzw. $v e^{-m_R(x-R)}$ die beiden Außenenergien. Ihre Beiträge sind genau $m_L|u|^2$ und $m_R|v|^2$. Das erhält man durch direktes Integrieren oder quadratisches Ergänzen. Jede Abweichung mit denselben Übergangswerten addiert nichtnegative Energie.

An der statischen Stabilitätsschwelle entspricht das exakt den Robin-Steifigkeiten $h_L=m_L$ und $h_R=m_R$, in natürlichen Einheiten. Die positive Außenenergie kann die Inneninstabilität nur über diese endliche Steifigkeit unterdrücken. Wenn man das gesamte Eigenwertspektrum statt der statischen Schwelle bestimmt, ist die passende Abklingzahl für $\lambda<\min(m_L^2,m_R^2)$ dagegen $\sqrt{m_i^2-\lambda}$. Der konstante Robin-Wert wird hier ausschließlich für das Vorzeichen der quadratischen Form verwendet.

## Exakte Schwelle und glatte Übergänge

Die erste Nullmode im Innenraum hat keine Knoten und erfüllt $f''=-\mu^2 f$. Die linke Randbedingung $f'(0)=m_L f(0)$ lässt sich durch $f(x)\propto\cos(\mu x-\delta_L)$ mit $\delta_L=\arctan(m_L/\mu)$ erfüllen. Die rechte Randbedingung $f'(R)=-m_R f(R)$ fordert $\mu R-\delta_L=\arctan(m_R/\mu)$ für die knotenfreie Mode. Damit gilt

$$
R_{\rm crit}=\frac{\arctan(m_L/\mu)+\arctan(m_R/\mu)}{\mu}.
$$

Für kürzere Segmente ist die gewählte quadratische Form positiv, bei Gleichheit hat sie eine Nullmode und für längere Segmente eine negative Richtung. Das Vorzeichen folgt aus der stetigen, monotonen Absenkung des niedrigsten Eigenwerts beim Verbreitern des Potentialtopfs. Für $R\to0$ bleibt der Außenoperator strikt positiv. Für große $R$ liefert eine Sinusfunktion im Inneren einen negativen Testwert. Die erste Nullstelle muss knotenfrei sein und ist damit durch die obige Rechnung festgelegt.

Für einen ausgedehnten Übergang auf einem Halbstrahl mit nichtnegativem Potential $V_{\rm out}$ ist die effektive Steifigkeit seine minimale Außenenergie bei Randamplitude eins. Liegt $0\le V_{\rm out}(x)\le m^2$ überall und bleibt das Gradientenmaß gleich, ist $h_{\rm eff}\le m$. Die feste Exponentialfunktion $e^{-mx}$ auf dem Halbstrahl ist ein zulässiger Vergleich. Eine glatte Zone, die sich der Außenmasse von unten nähert, kann in dieser Modellklasse also keine größere Stabilisierung als die abrupte positive Stufe liefern. Ein zusätzlicher positiver Kernterm, veränderte Gradientenkoeffizienten und Mischungen mit weiteren Moden sind von dieser Schranke nicht erfasst.

## Elektroschwache Größenordnung

Als reine Skalenprobe verwende $\mu\simeq91{,}2$ GeV aus dem vorigen Literaturvergleich und beide Außenmassen gleich der W-Masse $80{,}4$ GeV. Die Wahl der Außenmasse ist eine Modellannahme und keine aus den Nambu-Enden extrahierte Impedanz. Dann ergibt sich unter Wiedereinsetzen von $\hbar c$

$$
R_{\rm crit}\simeq0{,}00313\ {\rm fm}
\simeq1{,}27\,\hbar c/M_W .
$$

Für eine Länge von zwei W-Abschirmlängen wäre in demselben symmetrischen Modell an jedem Ende bereits $h>\mu\tan(\mu/M_W)\simeq196$ GeV nötig. Das ist mehr als doppelt so viel wie die hier angenommene Außenmasse. Der einfache Übergang in einen massiven Außenraum stellt daher im Vergleichsmodell kein zugleich klar getrenntes und stabilisiertes Segment bereit. Ob eine echte Endzone einen stärkeren positiven Beitrag liefert, hängt von ihrem Feldprofil und den gekoppelten physischen Moden ab. I1 bleibt eine mögliche Verbindungsidee ohne hergeleitete Endantwort. I3 braucht eigenständige Überschussdynamik. Native W2-Randwirkung und H96 bleiben offen.
