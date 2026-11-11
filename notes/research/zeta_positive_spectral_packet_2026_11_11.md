# Zeta-Wellenpaket im positiven kontinuierlichen Spektralraum

11. November 2026, Codex. Analytische, nicht blinde Erkundung; keine
Simulation, H-/k-Neuvergabe oder native physikalische Identifikation.

## Vorwissen und Ziel

`zeta_prime_operator_uncertainty_2026_11_11.md` konstruiert für sigma>1
den beschränkten reellen ungeraden Multiplikator

$$
a(t)=\operatorname{Im}\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)}
=\sum_{n\geq2}\Lambda(n)n^{-\sigma}\sin(t\log n).
$$

Die Reihe und ihre Ableitungen konvergieren für festes sigma>1 absolut
und gleichmäßig. a ist nichtnullig, reell-analytisch und hat eine
maßnullige Nullmenge. Der dortige Auswahloperator T=-iRA besitzt keine
normierbaren Eigenzustände. Die frühere Signumkonstruktion hatte zudem
ein H¹-Domänenproblem, falls das Profil am Vorzeichenwechsel nicht null war.

Abschnitt 4 von `hc_root_transfer_rotation_gate_2026_11_11.md` eröffnet
eine Alternative: Positive Spektralpakete können Balance haben, ohne
Eigenvektoren zu sein. Hier wird diese Alternative ausgeführt und die
Impulsdomäne geprüft, vor einer Massenauslesung. Keine zusätzlichen
MMA-Belege oder Reaktivierung der historischen RH-Spektralroute.

Träger bleibt ausdrücklich komplexes L²(R,dt) mit positiver Metrik,
Rf(t)=f(-t), Af=af. t ist dimensionslos, nicht physikalisch als Ort/Zeit
identifiziert. Quelle der arithmetischen Reihenidentität:
[NIST DLMF 27.4.12](https://dlmf.nist.gov/27.4#E12).

## 1. Explizites normalisierbares Paket

Mit dem reellen geraden Fenster g(t)=exp(-t²) setze

$$
f(t)=N a(t)^2g(t),\quad \|f\|=1,\qquad
S=\operatorname{sgn}(A),\qquad \psi=(f+iSf)/\sqrt2.
$$

N>0 ist nur die L²-Normierung, kein Massenfit. f ist gerade, Sf ungerade;
beide sind normiert und orthogonal. Damit sind psi normiert und <R>=0.
Da T²=A² gilt, ist sign(T)=-iRS. Direkt folgt

$$
\operatorname{sgn}(T)\psi=\psi,\qquad T\psi=|a|\psi.
$$

psi liegt somit im strikt positiven Spektralraum von T. Die zweite
Gleichung ist KEINE Eigenwertgleichung: |a(t)| ist kein konstanter
Eigenwert. Das widerspricht der früheren Eigenvektorsperre nicht.
Für F_+=1_(0,infinity)(T) gilt F_+f=(f+iSf)/2; Normierung ergibt psi.
F_+ ist eine zusätzlich gewählte Operation, nicht von Zeta oder Robertson
gefordert. Auch Fenster und Nullstellenunterdrückung a² sind keine
aus der nativen Dynamik hergeleiteten Profilregeln.

## 2. Endliche Parameter-/Fourier-Unschärfe

Sf=N a|a|g. Seine schwache Ableitung und die von f sind

$$
f'=N(2aa'g+a^2g'),\qquad
(Sf)'=N(2|a|a'g+a|a|g').
$$

a und a' sind beschränkt, g und g' quadratintegrierbar. Also liegen
f, Sf und psi in H¹(R). An jeder Nullstelle von a verschwindet das
Profil ausreichend stark; kein Delta-Term entsteht beim Vorzeichenwechsel.
Auch t psi und t psi' sind quadratintegrierbar. Damit sind für
Q=t und den üblichen selbstadjungierten P=-i d/dt beide zweiten
Momente endlich; QP psi und PQ psi existieren und [Q,P]psi=i psi.
Folglich gilt Delta Q Delta P>=1/2. Die Einheiten sind dimensionslos;
eine physikalische hbar-Skala ist nicht hergeleitet. Es wurde kein
numerischer Streuungswert bestimmt und kein Fenstermaßstab vorhergesagt.

## 3. HC-Balance ohne Sättigung von Robertson

Setze mu1=Integral |a| |f|² und mu2=Integral a² |f|². Dann

$$
\langle R\rangle=\langle A\rangle=0,\qquad
\Delta R=1,\quad\Delta A=\sqrt{\mu_2},\quad
\langle RA\rangle=i\mu_1.
$$

Robertson ist sqrt(mu2)>=mu1. Die Ungleichung ist hier strikt:
Gleichheit würde |a| konstant fast überall auf dem Träger von f
verlangen, doch die Niveaumengen von a² haben Maß null.
Die Balance stammt somit aus der positiven Spektralauswahl, nicht aus
einer Sättigung der Unschärferelation.

## Ergebnis und offene native Pflichten

Erreicht: ein tatsächlich arithmetischer Operator bei sigma>1, ein
normierter positiver kontinuierlicher Spektralzustand, exakte HC-Balance,
gültige Robertson-Relation und endliche Parameter-/Fourier-Streuungen.

Offen: T als physikalische Energie, native Präparation und Erhaltung von
F_+, Profil-/Fensterwahl, HC-Identifikation und positive Drei-Generationen-
Wurzelauslesung. Die bisherigen Ausleseschranken bleiben bestehen.
sigma=1/2 ist nicht durch diese konvergente Primzahlreihe gedeckt.

Nächster Schritt: F_+ und die reguläre Profildomäne mit vorhandener
Dynamik abgleichen. e^{-isT} erhält den Spektralraum, ist aber noch kein
nativer Generator und präpariert aus beliebigen Eingängen keinen Zustand
darin. Eine reine Norm- oder Massenpositivität reicht dafür nicht.

Validierung: analytische Selbstprüfung von Norm, Spektralzeichen, schwachen
Ableitungen, Operatorprodukten und Erwartungswerten. Keine Simulation,
unabhängige Begutachtung, QAM-Beweisfreigabe oder OP-Schließung.
