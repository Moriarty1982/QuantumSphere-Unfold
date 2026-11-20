# OP5 – Dynamische Gegenbewegung mit kompakter linearer Gravitation

20. November 2026. Analytische Erkundung im Materieframe M nach [PR #210](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/210). Die [statische Halterung](OP5_J_Halterung_Spannungsbilanz.md) trägt auf dem Plateau ein nichttriviales Dichteprofil. Bei ungleicher Trägheit kann die dortige starre Gegenbewegung während des Umschaltens den Gesamtimpuls nicht erhalten. Hier wird für die beiden idealisierten, überlagerten Materialien eine zeitabhängige Gegenbewegung konstruiert.

## Vorwissen geprüft

Die [Quadrupolkompensation](OP5_J_Quadrupol_Kompensation.md) gibt das kompakte statische Newton-Potential des direkten W2-Dichtebeitrags. Die [W2-Dichtequelle](OP5_J_W2_Dichteantrieb.md) knüpft die Higgsantwort an die Restmassenvariation. Die [Antriebswirkung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/842f3a0365bdabd04cc45de4a8e12f4454314d9f/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Lokale_Antriebswirkung.md) setzt die geformte skalare Kraft von außen ein. Die [zweifache Außenfeldkompensation](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/842f3a0365bdabd04cc45de4a8e12f4454314d9f/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Zweifache_Aussenfeldkompensation.md) nutzt bereits die Bildform eines Wellenoperators. Der neue Schritt verbindet diese Bildform mit konkret bilanzierten elastischen Materialverschiebungen und einer inneren Federkraft. Die Arbeit bleibt bei der lokalen Auslese im [Gesamtbild](../../../wiki/Gesamtbild.md). I3 benötigt weiterhin eine kosmologische Bestandsdynamik.

## Zeitabhängige Impulsbilanz

Sei $\sigma(u)=\mathsf C\varepsilon(u)$ der lineare isotrope Cauchy-Tensor im ersten Material und $\mathcal L u=\nabla\cdot\sigma(u)$. Die zweite Steifigkeit sei $c\mathsf C$ mit $c>0$. Für die Ruhedichten $\rho_1,\rho_2>0$ definiere
$$
A_1=\rho_1\partial_t^2-\mathcal L,\qquad A_2=\rho_2\partial_t^2-c\mathcal L.
$$
Die Operatoren kommutieren bei konstanten Materialparametern. Für ein beliebiges glattes, räumlich kompaktes Vektorfeld $B$ setze
$$
u=A_2 B,\qquad w=-A_1 B,\qquad d=u-w+k^{-1}A_1u .
$$
Die innere Feder mit Steifigkeit $k>0$ und vorgeschriebener relativer Ruhelage $d$ liefert dann $A_1u=-k(u-w-d)$ und $A_2w=+k(u-w-d)$. Beide Gleichungen gelten während der ganzen Schaltung. Bei verschwindenden früheren Daten und einem später statischen Plateau geht die Lösung in $w=-u/c$ über. Alle vorgeschriebenen Verschiebungen und $d$ haben kompakten räumlichen Träger. Voraussetzung bleibt, dass die relative Ruhelage räumlich und zeitlich gezielt verstellt werden kann.

Mit $M=\rho_2-c\rho_1$ sind die gewichtete Materialverschiebung $\rho_1u+\rho_2w=M\mathcal L B$ und die Spannungsverschiebung $u+cw=M\partial_t^2 B$. Der **lineare mechanische Tensor** lautet in der Konvention des elastischen Quellenabgleichs
$$
\delta T^{00}=-M\nabla\cdot\mathcal L B,\qquad
\delta T^{0i}=M(\mathcal L\dot B)_i,\qquad
\delta T^{ij}=-M\sigma_{ij}(\ddot B).
$$
Beide Divergenzgleichungen $\partial_\mu\delta T^{\mu\nu}=0$ folgen aus der Definition von $\mathcal L$. Während des Schaltens kann der Gesamtstress jetzt von null verschieden sein. Die unbelastete Feder und ihre ideale Steuerung tragen wie in der statischen Referenz erst ab zweiter Ordnung Energie bei. Eine Änderung der Ruheenergie der technischen Ansteuerung ist eine eigene mögliche Quelle.

## Higgsquelle und retardierter gewöhnlicher Außenbeitrag

Setze $K_L=\lambda+2\mu>0$ für die Lamé-Koeffizienten der ersten Komponente. Im restmassendominierten W2-Vergleich bei festem Referenzradius $v$ ist $\delta\mathcal J_h=-\delta T^{00}/v$. Für ein longitudinales $B=\nabla S$ gilt daher
$$
\delta\mathcal J_h=\frac{M K_L}{v}\,\Delta^2 S.
$$
In diesem Ansatz muss $M\ne0$ gelten, sonst fällt mit dem mechanischen Tensor auch die direkte Higgsquelle weg. Das zusätzliche Laplace-Glied ist der Preis dafür, ein kompaktes longitudinales Profil zusammen mit der dynamischen Impulsbilanz zu konstruieren.

Rückwärts kann man den gewöhnlichen linearen Außenbeitrag auch während des Umschaltens eliminieren. Sei $D=\partial_t^2-\Delta$ mit Lichtgeschwindigkeit eins. Wähle
$$
\delta H=-D\Delta^2 V,\qquad
S=-\frac{v}{M K_L}D\,\mathcal P_{\rm dyn}V
$$
für eine glatte, räumlich kompakte Funktion $V$, die vor dem Einschalten null ist. $\mathcal P_{\rm dyn}$ ist der konstante polynomielle Antriebsoperator der vorigen kompakten OP5-Konstruktion, mit $\delta J=\mathcal P_{\rm dyn}\delta H$. Die Operatoren kommutieren. Deshalb stimmt die direkte Materialquelle mit $\delta J$ überein, sofern sie an den OP5-Skalar gekoppelt wird. Aus $B=-D B_*$ mit $B_*=(v/(M K_L))\nabla\mathcal P_{\rm dyn}V$ folgt $\delta T=-D\,T_*$, wobei $T_*$ aus demselben linearen mechanischen Ausdruck mit $B_*$ gebildet und separat erhalten ist.

In der linearisierten gewöhnlichen Gravitation in harmonischer Eichung gilt $D\bar\gamma_{\mu\nu}=16\pi G\,\delta T_{\mu\nu}$. Mit verschwindenden früheren Störungen und ohne einlaufende freie Welle ist die Lösung $\bar\gamma_{\mu\nu}=-16\pi G T_{*,\mu\nu}$. Sie hat kompakten räumlichen Träger. Der lineare Krümmungswechsel durch diesen mechanischen Beitrag verschwindet außerhalb, einschließlich während der Schaltung. Diese Aussage gilt für die gezielt präparierte Quelle und ihre retardierten Daten. Eine frei laufende Störung oder ein Formfehler braucht den Wellenfaktor nicht zu besitzen. Die zu den Enden gehörenden übrigen Felder und deren Apparaturwirkung sind separat zu prüfen.

## Erhaltener Achsenkontrast

Auf dem Plateau ist $-D=\Delta$. Wähle $s=r^2/R^2$, einen glatten radialen Zuschnitt $\chi(s)$, der im Strahlkern eins ist, und $\kappa=M_5/M_6$ mit $M_j=\int_0^\infty s^j\chi(s)\,ds$. Für glattes $p(z)$ mit Träger in der Streckenmitte wähle als Plateau
$$
V=-\frac{A_H a R^6}{230400}\,p(z)\chi(s)(s^5-\kappa s^6).
$$
Das Querintegral verschwindet in jeder Ebene. Es bleibt unter den verwendeten Ableitungen null. Im Achsenkern ergibt $\Delta_\perp^3(s^5-\kappa s^6)=230400(s^2-4\kappa s^3)/R^6$. Die Beiträge mit Längsableitungen beginnen erst bei $s^3$. Somit beginnt die Plateauänderung $\delta H=\Delta^3 V$ mit dem früheren Achsenterm $-A_Ha\,p(z)s^2$. Der im linearen Krümmungsvergleich berechnete Achsenkontrast pro Polarisation bleibt
$$
\frac{16 A_Ha}{m^2R^4}\int p(z)\,dz .
$$
Bei einem rotationssymmetrischen Bündel paralleler Teststrahlen mit konstantem Querschnitt innerhalb des flachen Zuschnitts erhält der reine Riemann-Kontrast den Mittelungsfaktor $1-36\kappa\langle s\rangle$. Die Terme mit Längsableitungen integrieren sich bei dieser Mittelung weg. Eine stärkere Abhängigkeit von der Strahlbreite ist damit eine Kostenfolge der zusätzlichen Ableitungen im betrachteten Profil. Die Aussage betrifft die statische Auslese des erreichten Plateaus. Eine ausgesandte Welle im Schaltintervall braucht wegen der Zeitabhängigkeit eine eigene Übertragungsrechnung.

Die Bilanz umfasst die beiden elastischen Kontinua und ihre linearen inneren Kräfte im festgelegten Modell. Die Energieversorgung der Feder, elastische Energie höherer Ordnung, der reale Ort der Kräfte und die native Kopplung zwischen Higgsradius und OP5-Feld bleiben offen. Eine nutzbare Apparatur und H96 folgen aus der Konstruktion weiterhin nicht.

## Rechenkontrolle

[Wolfram-Skript](op5_j_dynamische_gegenbewegung.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_dynamische_gegenbewegung.txt) · [Laufmanifest](op5_j_dynamische_gegenbewegung.json)

Wolfram prüfte die inneren Kraftbilanzen, den erhaltenen Tensor, die longitudinale Higgsvariation, den gemeinsamen Wellenfaktor und die Achsen- sowie Azimutalkoeffizienten symbolisch. Lokal reproduzierbar im Notizordner mit `wolframscript -file op5_j_dynamische_gegenbewegung.wl`. Ausgeführt wurde der Kernel über den Connector. Qiskit wurde erwogen. Die Gleichungen beschreiben klassische Elastodynamik und linearisierte Gravitation.
