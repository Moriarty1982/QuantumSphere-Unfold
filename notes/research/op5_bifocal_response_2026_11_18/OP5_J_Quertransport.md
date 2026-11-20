# OP5 — Quertransport für den Kontrollkontrast

20. November 2026. Analytische Erkundung im Materieframe M.

## Vorwissen geprüft

Der [Kontrollkontrast](OP5_J_Kontrollkontrast.md) konstruiert eine kompakte statische Antwort $\psi$ aus $f=(1-\Delta/m^2)\psi$. Die [transversale Massenmodulation](OP5_J_Transversale_Massenmodulation.md) erklärt, warum die Projektion auf den Strahl von der Querumverteilung abhängt. Der [longitudinale Spin-2-Abgleich](OP5_J_Longitudinaler_Abgleich.md) setzt einen erhaltenen vollständigen D-Tensor voraus. Rückwärts verlangt eine physische Modulation deshalb zuerst einen Strom, der $f$ erzeugt, und eine Impulsbilanz für den vollständigen Quelltensor. Im [Gesamtbild](../../../wiki/Gesamtbild.md) liegt das vor der absoluten Materieauslese. Die präparierte Modulation liefert keine Populationsdynamik für I3.

## Massenerhaltender Transport in jeder Querebene

Für das zylindersymmetrische Profil $\psi(r,z)=A p(z)(g_a(r)-g_{2a}(r)/4)$ gilt $\int_{\mathbb R^2}\psi(\mathbf b,z)\,d^2b=0$ für jedes $z$. Das planare Integral von $\Delta f_0$ verschwindet für $f_0=\psi$: Der transversale Anteil ist ein Randintegral und der longitudinale Anteil ist $\partial_z^2$ des identisch verschwindenden Querintegrals. Daher gilt auch $\int_{\mathbb R^2}f(\mathbf b,z)\,d^2b=0$.

Schreibe die gewünschte Dichte als $\rho=\rho_0+s(t)f$ und wähle $0\le s\le1$ sowie $\rho_0$ so, dass $\rho\ge\rho_{\min}>0$ in einer Umgebung des Trägers von $f$. Die Fortsetzung von $\rho_0$ außerhalb darf kompakt sein. Der rein radiale, transversale Massenstrom ist
$$
j_r(t,r,z)=-\dot s(t)\frac{1}{r}\int_0^r u\,f(u,z)\,du,\qquad j_z=0.
$$
Denn $r^{-1}\partial_r(rj_r)=-\dot s f$. Der Strom ist an der Achse regulär, da das Integral $O(r^2)$ ist. Er ist außerhalb des Profilträgers null, da das gewichtete Querintegral verschwindet. Es fließt keine Masse zwischen Querebenen. Auf dem Träger gilt $\mathbf v=\mathbf j/\rho$. Für eine zeitlich um den Faktor $\tau$ gestreckte Umschaltung ist $\mathbf v=O(\tau^{-1})$. Die nichtrelativistische kinetische Energiedichte $\rho|\mathbf v|^2/2$ nimmt dort wie $\tau^{-2}$ ab. Der seitlich versetzte Kontrollblock erhält Strom und Geschwindigkeitsfeld durch dieselbe räumliche Translation, sofern auch die Grunddichte entsprechend übersetzt wird. Alternativ kann dieselbe Grunddichte auf beiden Trägern konstant gewählt werden.

## Ein kompakter erhaltener Quelltensor

Wähle eine kompakte Lösung von $\Delta_\perp\chi=f$ durch
$$
\partial_r\chi=\frac1r\int_0^r u f(u,z)\,du,\qquad \chi(2a,z)=0.
$$
Der radiale Ausdruck ist außerhalb des Profils null, sodass $\chi$ dort ebenfalls null gesetzt werden kann. Somit ist $\mathbf j=-\dot s\nabla_\perp\chi$. Die Kontinuitätsgleichung allein legt noch keine impulsbilanzierende Spannung fest. Ein formaler symmetrischer Quelltensor ist in Einheiten $c=1$
$$
T^{00}=\rho_0+s f,\qquad
T^{0a}=T^{a0}=-\dot s\,\partial_a\chi,\qquad
T^{ab}=\ddot s\,\chi\,\delta^{ab},\qquad T^{z\mu}=T^{\mu z}=0,
$$
mit transversalen Indizes $a,b=x,y$. Dann ist $\partial_\mu T^{\mu0}=\dot s(f-\Delta_\perp\chi)=0$ und $\partial_\mu T^{\mu a}=-\ddot s\,\partial_a\chi+\ddot s\,\partial_a\chi=0$. Der Impulsstrom ist $O(\tau^{-1})$ und die erforderliche Gesamtspannung in dieser Konstruktion $O(\tau^{-2})$. Auf ruhenden Plateaus sind beide null. Der Tensor ist eine Erhaltungskonstruktion für die Gesamtquelle. Für einen nichtrelativistischen Stoff muss eine konkrete Wechselwirkung die Differenz zwischen dieser Gesamtspannung und dem konvektiven Impulsfluss $\rho v^a v^b$ tragen. Eine solche Materialgleichung und ein Antrieb des D-Sektors sind offen.

Für den freien Strahl in $z$-Richtung ist die direkte Nullkontraktion $n_\mu n_\nu T^{\mu\nu}=T^{00}$ mit $n_\mu=(-1,0,0,1)$. Dagegen lautet die Spur $T^\mu{}_\mu=-T^{00}+2\ddot s\chi$. Die zusätzlichen transversalen Spannungen fallen in der direkten Nullkontraktion weg. Der longitudinale Quellenabgleich der geladenen Endpunkte kann weiterhin auf die Spur reagieren.

## Endpunktrest bei zeitabhängiger Dichteantwort

Der statische Kern wird in dieser Abschätzung nur für die Dichtekomponente durch den linearen massiven Wellenresolventen ersetzt. Für eine harmonische Komponente $s_\omega$ mit $|\omega|<m$ und $\kappa=\sqrt{m^2-\omega^2}$ gilt bei räumlichem Abklingen
$$
u_\omega
 =s_\omega\left[\psi+\omega^2\,\frac{e^{-\kappa|\cdot|}}{4\pi|\cdot|}*\psi\right].
$$
Im Fourierbild folgt dies aus $(m^2+|\mathbf q|^2)/(m^2+|\mathbf q|^2-\omega^2)=1+\omega^2/(m^2+|\mathbf q|^2-\omega^2)$. In einer Apparaturregion mit Abstand mindestens $d>0$ vom Träger erhält man
$$
|u_\omega|\le |s_\omega|\frac{\omega^2 e^{-\kappa d}}{4\pi d}\|\psi\|_1.
$$
Damit gilt der exakte statische Endpunktabgleich auch bei passender Vermittlermasse im Allgemeinen nur für $\omega=0$. Die Formel ist eine Schranke pro submassiver harmonischer Komponente der Dichteantwort. Eine zeitlich begrenzte Schaltflanke kann auch Frequenzen ab der Massenschwelle enthalten. Der vollständige Einschwingrest und die Umrechnung auf die Apparaturphase brauchen den dynamischen Tensortransport und ein getrenntes Endpunktmodell.

## Kontrolle

[Wolfram Language](op5_j_quertransport.wl) prüft die verschwindende radiale Randbilanz, die vier Divergenzen des Tensors, seine Nullkontraktion und Spur sowie die Fourier-Identität. Die Prüfung betrifft klassische Kontinuität, Tensoralgebra und Feldpropagation. Eine Qiskit-Phasenmessung würde erst nach Festlegung einer solchen Endpunktantwort einen unabhängigen Beitrag liefern. Native Ansteuerung, reale J-Auslese und H96 bleiben offen.
