# OP5 – Fehlerbudget für die differentielle A/B-Laufzeit

20. November 2026. Analytische Erkundung im Materieframe M. Ausgangspunkt ist eine hypothetische verlustfreie Zweimodenstrecke. Die Rechnung geht von einer geforderten Auflösung der Laufzeitdifferenz rückwärts zu den maximalen komplexen Messfehlern und minimalen Anschlussstärken.

## Vorwissen geprüft

Die [HCl/H-Anschlusskondition](OP5_J_HCl_Anschlusskondition.md) gibt die kleinste Singulärzahl eines Endes einschließlich Übersprechen und ein vorläufiges Lorentz-Fenster. Der [A/B-Matrixvergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Sende_Empfangsports.md) identifiziert im idealen Fall die Eigenphasen. Die [skalare Endpunktdrift](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Endpunktdrift.md) motiviert eine unabhängige Nullkontrolle. Die lokale Suche nach Eigenphase und Phasentrennung ergab im HCl-Zweig bisher nur die Matrixfehlerschranke ohne Phasen- oder Laufzeitbudget. Im [Gesamtbild](../../../wiki/Gesamtbild.md) bleibt dies beim lokalen Auslesezweig von OP5. I3 würde später eine eigene kosmologische Bestandsdynamik erfordern.

## Matrixfehler in den Feldkoordinaten

Alle Normen sind Operatornormen zur 2-Norm, mit konsistent kalibrierten Bezugsamplituden der Gerätekanäle. Nach Ausklammern der gemeinsamen Grundlaufzeit seien die idealen Matrizen $M_A=LF$ und $M_B=LUF$. Dabei sind $L$ und $F$ die invertierbaren Empfangs- und Sendematrizen, und $U$ ist der unitäre A/B-Streckenkontrast. Diese Darstellung übernimmt die verlustfreie kommutierende Einweg-Näherung des A/B-Vergleichs. Die idealen Eigenwerte sind $\lambda_j=e^{i\phi_j}$.

Die gemessenen Matrizen haben die Form
$$
\widehat M_A=L(I+N_A)F,\qquad
\widehat M_B=L(U+N_B+D)F.
$$
Hier sind $N_X=L^{-1}E_X F^{-1}$ für additive Gerätefehler $E_X$. Die Änderung der Anschlüsse im Profil B sei durch
$D=(I+D_L)U(I+D_R)-U$ modelliert. Für $\|D_L\|\le d_L$ und $\|D_R\|\le d_R$ gilt $\|D\|\le d=d_L+d_R+d_L d_R$. Die Parameter $d_L,d_R$ beziehen sich auf die Feldbasis. In ihnen steckt die Unsicherheit nach einer etwaigen unabhängigen Endpunktkorrektur.

Die Eigenwerte des gemessenen Matrixpaars sind die Eigenwerte von
$Q=(I+N_A)^{-1}(U+N_B+D)$. Der Grund ist die Ähnlichkeit $\widehat M_A^{-1}\widehat M_B=F^{-1}QF$. In der Feldbasis gilt exakt
$$
Q-U=(I+N_A)^{-1}(N_B-N_A U+D).
$$
Eine direkte Schranke für den gewichteten Rest $N_B-N_AU+D$ kann daher bekannte Fehlerkorrelationen nutzen. Für unstrukturierte Normschranken $\|E_X\|\le\epsilon_X$ und $p=\sigma_{\min}(L)\sigma_{\min}(F)>\epsilon_A$ folgt
$$
\|Q-U\|\le r=\frac{\epsilon_A+\epsilon_B+p\,d}{p-\epsilon_A}.
$$
Dies folgt aus $\|N_X\|\le\epsilon_X/p$, der inversen Normschranke $1/(1-\|N_A\|)$ und $\|U\|=1$. Die Rechnung erfolgt vor dem Rückwechsel in die Gerätebasis, sodass kein zusätzlicher Konditionsfaktor der Ähnlichkeit nötig ist. Ist der gewichtete Rest bekannt, kann seine direkte Schranke erheblich kleiner sein als die Summe der Einzelfehler.

## Von Eigenwerten zur Laufzeitauflösung

Jeder Eigenwert von $Q$ liegt höchstens um $r$ von mindestens einem der beiden idealen Eigenwerte entfernt. Außerhalb beider Kreise hat der Resolvent des normalen $U$ die Norm $1/\min_j|z-\lambda_j|$. Dort kann $Q-zI$ wegen $\|(U-zI)^{-1}(Q-U)\|<1$ keinen Kern haben. Sind die Kreise disjunkt, enthält jeder genau einen Eigenwert mit algebraischer Vielfachheit. Entlang $U+t(Q-U)$ für $0\le t\le1$ bleibt die Eigenwertzahl in jedem durch eine etwas größere disjunkte Scheibe getrennten Gebiet konstant.

Bei geforderter kleinster zirkulärer Phasentrennung $\theta_{\min}>0$ an den für die Zuordnung benutzten Frequenzen genügt $r<\sin(\theta_{\min}/2)$. Für $r<1$ erzeugt der Kreis um einen idealen Eigenwert auf dem Einheitskreis eine Winkelabweichung von höchstens $\arcsin r$. Dies ergibt sich aus der Tangente vom Ursprung an diesen Kreis. Durch die Zuordnung erhält man an jeder Frequenz damit einen Fehlerbetrag pro Eigenphase.

Sei $\Delta\omega=\omega_2-\omega_1>0$. Die differentielle Laufzeit wird als Sekante der entfalteten Phasendifferenz geschätzt. Für dieselbe Fehlerschranke $r$ an beiden Endfrequenzen beträgt der maximale Fehler
$$
\left|\widehat{\Delta\tau}-\Delta\tau_{\rm Sekante}\right|
\le\frac{4\arcsin r}{\Delta\omega}.
$$
Die vier Beiträge stammen aus zwei Phasen an zwei Frequenzen. Die Schranke setzt eine korrekte Modenzuordnung und Entfaltung voraus. Ein hinreichendes Unwrapping-Kriterium entlang eines Abtastgitters ist, dass jeder wahre Phasenschritt betragsmäßig kleiner als $\pi-2\arcsin r$ ist und die Zuordnung auf diesem Gitter verfolgt werden kann. Die Sekante ist eine mittlere Gruppenlaufzeitdifferenz über das Band. Eine punktweise Ableitung erfordert zusätzlich eine Dispersionsannahme oder lokale Frequenzinformation. Bei Phasengleichheit modulo $2\pi$ liefert der Kreistest keine eindeutige Zuordnung.

Für ein vorgegebenes Laufzeitfehlerziel $\eta$ und $0<\Delta\omega\,\eta/4<\pi/2$ verwende
$$
r_*=\min\{\sin(\theta_{\min}/2),\ \sin(\Delta\omega\,\eta/4)\}.
$$
Eine hinreichende Anforderung mit strikter Reserve ist für $0\le d<r_*$
$$
p>\frac{(1+r_*)\epsilon_A+\epsilon_B}{r_*-d}.
$$
Sender und Empfänger müssen jeweils im gemeinsamen Frequenzfenster genügend empfindlich bleiben. Bei belegten Matrizenfehlern auf der Feldseite kann direkt die exakte Restform verwendet werden. Liegt $d$ bereits bei $r_*$ oder darüber, liefert die Summenschranke selbst bei idealem additivem Fehler keine strikte Reserve. Ein aus den Messwerten gebildetes Intervall schließt eine Nulldifferenz aus, wenn der Betrag des gemessenen Werts größer als die gesamte Fehlerhalbbreite ist.

## Exakte Mehrdeutigkeit und eine Matrix-Nullkontrolle

Für einen hermiteschen Laufzeit-Zusatz $B$, der mit $T$ kommutiert, sind die beiden idealen Beschreibungen
$$
L\,e^{i\omega(T+B)}F
\quad\text{und}\quad
L\,e^{i\omega T}\bigl(e^{i\omega B}F\bigr)
$$
identische Daten. In der zweiten Beschreibung sitzt die zusätzliche, profilsynchrone Phase am Sender. Wenn $B$ verschiedene Eigenwerte hat, betrifft die Mehrdeutigkeit gerade die differentielle Laufzeit. Wiederholungen mit demselben Profil lösen diese Gleichheit auch bei verschwindendem additivem Fehler nicht auf.

Ein parallel erfasster Kontrollpfad mit bekanntem Einheitskontrast würde im idealen Fall dieselben aktuellen Endpunktmatrizen $L_B,F_B$ teilen. Für $C_B=L_BF_B$ und Messpfad $M_B=L_BUF_B$ hat $C_B^{-1}M_B=F_B^{-1}UF_B$ die gewünschten Eigenphasen. Dazu muss der physische Kontrollpfad dieselben Endpunktantworten mit derselben kohärenten Referenz sehen. Verschiedene Wegüberlappungen oder eine unbekannte relative Phase müssten als Restfehler erfasst werden. Sind die beiden Endpunktmatrizen im Kontrollpfad praktisch gleich, setzt dieselbe Matrixfehlerschranke das Budget für diesen Quotienten.

## Größenordnung im Rechenbeispiel

Bei 100 MHz Frequenzabstand, Fehlerziel 0,25 ps für die differentielle Sekante und einem garantierten zirkulären Phasenabstand von mindestens 0,1 rad ist $r_*\simeq3{,}927\cdot10^{-5}$. Alle drei Vorgaben dienen allein dem Rechenbeispiel. Für $\epsilon_A=\epsilon_B=10^{-8}$ in denselben normierten Gerätekanälen und $d=0$ fordert die Summenschranke $p>5{,}093\cdot10^{-4}$, also an zwei gleichstarken Enden jeweils eine kleinste Singulärzahl über 0,02257. Bei $d=10^{-5}$ steigt der gleich verteilte Mindestwert auf 0,02614.

Zum Vergleich erreicht bei $|g_J/e|=10^{-3}$ jedes ideale HCl/H-Ende selbst im Grenzfall einer starken HCl-Linie höchstens rund 0,00254 bei H-Gewinn eins. Bei diesen zwei Enden und $d=0$ verlangt die unstrukturierte Summenschranke für das Beispiel dann Fehler je Matrix unter rund $1{,}26\cdot10^{-10}$. Dies ist die Obergrenze der Fehlertoleranz dieser Zertifizierung mit dem Produkt $p$. Die tatsächliche Gerätekalibrierung, die Rauschkorrelation und das auflösbare Frequenzfenster wurden nicht gemessen. Die Linienenergie 0,360329 eV erlaubt freie J-Ausbreitung nur in einem entsprechend leichten Kanal. Native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_ab_fehlerbudget.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_ab_fehlerbudget.txt) · [Laufmanifest](op5_j_ab_fehlerbudget.json)

Wolfram liefert exakte Nullreste für den gewichteten Matrixrest, die Produktentwicklung der Endpunktdrift und die Tangentialgeometrie. Eine komplexe, nichtdiagonale Zweimoden-Matrix wurde mit 40-stelliger Eingabe direkt auf Norm- und Eigenwertfehler geprüft. Die numerische Stichprobe enthält genau diese eine Matrix. Das allgemeine Argument steht oben. Lokal reproduzierbar mit `wolframscript -file op5_j_ab_fehlerbudget.wl` im Notizordner. Ausgeführt wurde der Wolfram-Kernel über den Connector. Qiskit wurde erwogen. Das Prüfobjekt ist ein klassisch rekonstruiertes Matrixpaar mit im Allgemeinen nichtunitären Gerätefehlern.
