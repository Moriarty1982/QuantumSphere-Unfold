# OP5 — Kontrollkontrast bei unveränderten Endpunktfeldern

20. November 2026. Analytische Erkundung im Materieframe M. Vorausgesetzt ist die lineare statische Yukawa-Antwort im schwachen, reflexionsarmen Strahlmodell. Das Ergebnis betrifft die kontrollierte Vermittlerantwort im Modell.

## Vorwissen geprüft

Die [doppelte Laufzeitdifferenz](OP5_J_Doppelte_Laufzeitdifferenz.md) enthält das planare endliche Streckenintegral und eine Abschätzung der Endpunkte. Die [transversale Massenmodulation](OP5_J_Transversale_Massenmodulation.md) liefert einen Quer-Kontrast bei gleicher Gesamtmasse. Ihre Scheibe-Ring-Rechnung legt die Endpunktfelder nicht gleich. Die [Endpunktdrift](OP5_J_Endpunktdrift.md) verlangt rückwärts einen bekannten Kontrollkontrast mit gleicher Endpunktantwort. Verwendet wird der normierte dreidimensionale Yukawa-Kern aus der Massenmodulation. Die Rechnung liegt im [Gesamtbild](../../../wiki/Gesamtbild.md) vor der absoluten Materieauslese für H96.

## Planare Grenze

Sei $u$ die Änderung des gefalteten Profils und $f$ die Dichteänderung pro Transversalfläche, getragen im Inneren von $[0,L]$. Dann gilt $(1-\partial_z^2/m^2)u=f$. Aufgrund der abklingenden Außenlösung gilt $u'(0)=m u(0)$ und $u'(L)=-m u(L)$. Integration ergibt
$$
\int_0^L u(z)\,dz=\int_0^L f(z)\,dz-\frac{u(0)+u(L)}{m}.
$$
Bei gleicher Säulenmasse vor und nach der Änderung sowie gleicher Antwort an beiden Endpunkten ist der integrierte Kontrast exakt null. Die Differenz zweier Änderungen mit denselben Endpunktwerten und derselben Säulenmassenänderung unterliegt derselben Identität.

## Dreidimensionaler Kontrollkontrast

Bei vorgegebener Vermittlermasse $m_0>0$ sei $\psi$ eine kompakte $C^3$-Funktion im Inneren der Strecke mit $\int\psi\,d^3x=0$. Der Support liegt außerhalb der Sender- und Empfängerregionen. Definiere die vorzeichenwechselnde Dichteänderung
$$
f=(1-\Delta/m_0^2)\psi.
$$
Die Gesamtmasse bleibt erhalten, weil das Integral des Laplace-Terms verschwindet. Die gefaltete Antwort ist exakt $u=G_{m_0}*f=\psi$. Das folgt durch Invertieren des Multiplikators $1+|\mathbf q|^2/m_0^2$. Deshalb stimmen die Vermittlerfelder vor und nach der Änderung in ganzen Apparaturumgebungen überein, einschließlich ihrer lokalen Ableitungen. Getrennte nichtnegative Dichteprofile lassen sich etwa durch Hinzufügen derselben kompakten Grunddichte realisieren, die beide Änderungen auf ihren Trägern betragsmäßig dominiert. Dies ist eine statische Existenzkonstruktion.

Wähle Mittelpunkt $z_0\in(0,L)$, Längshalbbreite $\ell$ und Transversalradius $a$, alle so, dass der Träger von den Apparaturregionen getrennt bleibt. Schreibe $[x]_+=\max(x,0)$ und
$$
p(z)=[1-(z-z_0)^2/\ell^2]_+^4,\qquad
g_a(\mathbf b)=[1-|\mathbf b|^2/a^2]_+^4,\qquad
\psi(\mathbf b,z)=A p(z)\left[g_a(\mathbf b)-g_{2a}(\mathbf b)/4\right],
\quad A>0.
$$
Die beiden transversalen Integrale sind $\pi a^2/5$ und $4\pi a^2/5$. Somit ist die Gesamtänderung null. Auf der Achse bleibt der Faktor $3/4$. Da $\int p(z)\,dz=256\ell/315$, beträgt das endliche Streckenintegral auf der Achse genau $64 A\ell/105$. Bei einem normierten nichtnegativen Strahlgewicht im Radius $a/2$ ist das gewichtete Streckenintegral mindestens $17A\ell/315$. Dort gilt $g_a\ge81/256$ und $g_{2a}/4\le1/4$.

Als Nullkontrolle verschiebe dieselbe Modulation quer so weit, dass ihr Antwortträger den Strahl verfehlt. Bei Strahlradius $a/2$ genügt eine Verschiebung um mehr als $5a/2$. Die Masse bleibt gleich. In beiden Blöcken erfährt das statische Vermittlerfeld in den Apparaturregionen exakt dieselbe Änderung, nämlich null. Die Kontrolle hat auch entlang des Strahls Kontrast null, während die zentrierte Modulation einen positiven geometrischen Kontrast hat. Die Laufzeit ergibt sich durch Multiplikation mit dem weiterhin zu kalibrierenden Kopplungskoeffizienten $C_\Delta$.

## Empfindlichkeit gegenüber der Vermittlermasse

Wird dieselbe quellseitig auf $m_0$ abgestimmte Änderung bei tatsächlicher Masse $m$ eingesetzt, gilt
$$
G_m*f=\frac{m^2}{m_0^2}\psi+\left(1-\frac{m^2}{m_0^2}\right)G_m*\psi.
$$
Ein Endpunkt im Abstand mindestens $d>0$ vom Träger erfüllt daher
$$
|u|\le\left|1-\frac{m^2}{m_0^2}\right|
\frac{m^2e^{-md}}{4\pi d}\|\psi\|_1.
$$
Diese Schranke gilt für den Feldwert. Die Umrechnung in einen Kalibrierfehler der Endpunkte braucht eine Apparaturempfindlichkeit. Auch der exakte Nullkontrast des verschobenen Profils gilt bei $m=m_0$. Die Konstruktion kontrolliert den modellierten Yukawa-Beitrag. Änderungen der sichtbaren Last, der gewöhnlichen Gravitation oder der Ansteuerung benötigen eigene Kontrollen.

## Kontrolle und offene Anforderungen

[Wolfram Language](op5_j_kontrollkontrast.wl) prüft die planare Integrationsformel, die regulären Trägerränder, die Profilintegrale, die untere Schranke für endliche Strahlbreite und die Fourier-Identität für Verstimmung. Für diese Kontrollen sind klassische Feldoperatoren und Integrale maßgeblich. Die Phasenschaltung aus der Endpunktdrift-Notiz liefert dafür keine zusätzliche Information. Die kontrollierte Erzeugung der D-Profile, eine unabhängige Bestimmung von $m_0$ und $C_\Delta$, die physische Endpunktkalibrierung und H96 bleiben offen.
