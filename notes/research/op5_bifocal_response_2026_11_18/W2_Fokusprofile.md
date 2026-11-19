# OP5: Außenfeldauslese für zwei radiale Fokusquellen

19. November 2026. Analytische Erkundung, nicht blind. OP5/T9 im statischen Materie-Ruhesystem. Linearer Photon-Z-Vergleich der [Neutralstrom-Notiz](W2_Neutralstroeme.md) mit konstanter Z-Masse $m>0$. Die [Sondenform](Sondenform.md) setzt getrennt kalibrierte Felder voraus. Die [radiale Yukawa-Lösung](Grenze_W2.md) und die [Coulomb-Fokusrechnung](W2_J_Eichkanal.md) liefern die Ausgangspunkte. Neu ist, welche Quelleninformation die radiale Einschränkung aus dem Außenfeld zurückgewinnt. Die zwei Foki und ihre festen radialen Profile sind Modellannahmen. Die ausgeschriebene W2-Wirkung liefert dafür bisher kein Kriterium.

## Außenfeld einer radialen Quelle

Schreibe $\rho_\alpha(x)=q_{\alpha,+}n_{\alpha,+}(|x-F_+|)+q_{\alpha,-}n_{\alpha,-}(|x-F_-|)$ für den Photon- oder Z-Kanal. Hier sind $F_\pm=\pm w\,e_1$ mit $w>0$ bekannte Foki. Jedes Profil $n_{\alpha,\pm}$ ist radial, nichtnegativ, auf Gesamtintegral eins normiert und im Ball um den jeweiligen Fokus mit Radius $b<w$ getragen. Das Vorzeichen der Quelle sitzt ganz im zugehörigen $q_{\alpha,\pm}$.

Für Abstand $r>s$ vom Mittelpunkt ist das Winkelmittel des Yukawa-Kerns $K_m(r)=e^{-mr}/(4\pi r)$ über eine Quellschale mit Radius $s$ exakt

$$
\frac1{8\pi}\int_{-1}^{1}
 \frac{\exp(-m\sqrt{r^2+s^2-2rsu})}{\sqrt{r^2+s^2-2rsu}}\,du
=K_m(r)\frac{\sinh(ms)}{ms}.
$$

Das folgt mit der Abstandssubstitution $d=\sqrt{r^2+s^2-2rsu}$, deren Grenzen $r-s$ und $r+s$ sind. Am Ursprung ist das Gewicht stetig eins. Das Außenfeld eines Fokus besitzt folglich die Punktquellenform, aber mit Amplitude $a_{\alpha,\pm}=\kappa_{\alpha,\pm}q_{\alpha,\pm}$, wobei

$$
\kappa_{\alpha,\pm}
=4\pi\int_0^b s^2 n_{\alpha,\pm}(s)\frac{\sinh(m_\alpha s)}{m_\alpha s}\,ds,
\qquad m_\gamma=0,\quad m_Z=m.
$$

Für das Photon gilt $\kappa_{\gamma,\pm}=1$. Die tatsächliche Z-Gesamtladung eines Fokus hängt zusätzlich am radialen Profil.

## Zwei Messpunkte und ihr Rang

An den bekannten Punkten $\pm L e_1$ mit $L>w+b$ und kalibrierten statischen Potentialen $V_{\alpha,\pm}$ gilt pro Kanal

$$
\begin{pmatrix}V_{\alpha,+}\\ V_{\alpha,-}\end{pmatrix}
=
\begin{pmatrix}k_n&k_f\\k_f&k_n\end{pmatrix}
\begin{pmatrix}a_{\alpha,+}\\ a_{\alpha,-}\end{pmatrix},
\qquad
k_n=K_{m_\alpha}(L-w),\quad k_f=K_{m_\alpha}(L+w).
$$

Es gilt $k_n>k_f>0$. Die Summe und Differenz der Messwerte bestimmen die Amplitudensumme und -differenz durch Division durch $k_n+k_f$ bzw. $k_n-k_f$. Damit reichen unter den Modellannahmen zwei Messpunkte pro Kanal. Die beiden Potentiale werden in derselben statischen Eich- bzw. Normierungskonvention mit Nullwert im Unendlichen verglichen. Für $w\to0$ degeneriert die Inversion, und bei stark abgeschirmten Signalen ist die formale Invertierbarkeit keine Genauigkeitsgarantie.

Sind die Z-Profilfaktoren kalibriert, folgt aus $q_{\alpha,\pm}=a_{\alpha,\pm}/\kappa_{\alpha,\pm}$ das gewöhnliche Dipolmoment entlang der Achse,

$$
P_{B-L}=w\left[
(2-4s_W^2)\frac{q_{\gamma,+}-q_{\gamma,-}}{e}
-4\frac{q_{Z,+}-q_{Z,-}}{g_Z}\right].
$$

Die Radialsymmetrie lässt den intrinsischen Dipol jeder einzelnen Wolke um ihren Fokus verschwinden. Die Formel setzt keine Änderung der Randform voraus.

## Was bei unbekanntem Profil ausfällt

Da $\sinh z/z$ für $z\ge0$ monoton wächst, liegt $\kappa_Z$ zwischen $1$ und $H=\sinh(mb)/(mb)$. Aus den Außenfeldern folgt daher das Vorzeichen jeder einzelnen Z-Quellamplitude und die Schranke $|a_Z|/H\le|q_Z|\le|a_Z|$. Für $mb\ll1$ ist $H=1+(mb)^2/6+O((mb)^4)$. Bei identischen unbekannten Profilen an beiden Foki ist auch das Vorzeichen der Z-Differenz bestimmt, während ihr Betrag den gemeinsamen unbekannten Faktor behält. Für die Kombination mit dem Photon können sich Beiträge aufheben. Das Vorzeichen von $P_{B-L}$ ist durch diese Schranken nur dann gesichert, wenn das aus ihnen gebildete Intervall die Null ausschließt.

Die Restmehrdeutigkeit besteht sogar bei vollständigem Zugang zum Außenfeld. Wähle zwei verschiedene normierte glatte radiale Profile, deren Träger in getrennten radialen Intervallen innerhalb desselben Fokusballs liegen. Die strikte Monotonie gibt unterschiedliche Profilfaktoren $\kappa_1\ne\kappa_2$. Verwende in jeder Konfiguration das jeweilige Profil an beiden Foki und setze $q_{Z,\pm}=\pm a/\kappa_j$ mit demselben $a\ne0$. Beide Konfigurationen geben exakt dieselben Außenpotentiale, tragen aber unterschiedliche Z-Dipolmomente $2wa/\kappa_j$. Der reine Z-Vergleich lässt sich wie in der Neutralstrom-Notiz durch die Dirac-Besetzungsrichtung $(d_u,d_d,d_\nu,d_e)=(0,3,-2,-1)f$ bei verschwindender Photon- und J-Quelle realisieren. Die Gegenprobe betrifft diese linearen Außenfelder, nicht eine mitvariierte Higgs- oder Gravitationslösung.

## Konsequenz für den OP5-Rand

Bekannte Foki und kalibrierte Profile genügen für die betrachtete Auslese. Nichtnegative Profile ohne Kalibrierung geben Schranken und können ein reines Z-Vorzeichen sichern. Die W2-Wirkung müsste die Quellenform oder ihre Profilfaktoren selbst festlegen und erklären, wie die Felder auf eine dynamische Formkoordinate wirken. I3 bleibt an eine eigenständige Überschussdynamik gebunden. Native Randwirkung und H96 bleiben offen.
