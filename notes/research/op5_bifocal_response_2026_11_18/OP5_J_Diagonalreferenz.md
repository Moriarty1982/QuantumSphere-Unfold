# OP5 – Diagonalfehler der skalaren Markerreferenz

21. November 2026. Analytische Erkundung im Materieframe M. Der homogene Zweikanalmarker hat einen endlichen A-Hub und eine schwache J-Beimischung. Gesucht ist eine bandweite Fehlergrenze für die Diagonalreferenz $(1,t_A)$.

## Vorwissen geprüft

Der [endliche Markerhub](OP5_J_Endlicher_Markerhub.md) liefert den Green-Kern und die Neumann-Reihe. Die [Rücklauftoleranzen](OP5_J_Ruecklauf_Toleranzen.md) bestimmen die Parameterbox für massive J-Dispersion, Schichtdicke und komplexen A-Index. Die [komplexe Referenz](OP5_J_Komplexe_Referenz.md) lässt nach Abzug des Rücklaufs eine Reserve von rund $6{,}234\cdot10^{-6}$ und gibt für $|T_{AA}-t_A|$ die gröbere Grenze $9{,}968\cdot10^{-6}$. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## A-Diagonale

Seien $A=k_A L$, $J=k_JL$, $U=\kappa L$ und $S=(U^2-A^2)/A=L g|q_A|^2$. Der Betrag von $S$ ist durch $s$ aus der Toleranzrechnung begrenzt. Setze $x=|q_J/q_A|$, $r=(U-A)/(U+A)$, $c=(1-r)/(1-r^2e^{2iU})$. Auf der auf eins skalierten Schicht ist das linke A-Referenzfeld
$$
F(\xi)=c[e^{iU\xi}+r e^{iU(2-\xi)}].
$$
Am rechten Rand liefert der mit $k_A$ gewichtete A-Green-Kern $F(1-\xi)/(2i)$. Die äußere Phase für die Transmission ist $e^{-iA}$. Das erste A-Diagonalglied verschwindet, da $E_{AA}=0$. Das zweite läuft vollständig über J, dessen gewichteter Green-Kern $e^{iJ|\xi-\eta|}/(2i)$ ist. Damit gilt
$$
T_{AA}^{(2)}=-\frac{S^2x^2e^{-iA}}4
\int_0^1\!\!\int_0^1 F(1-\xi)\,e^{iJ|\xi-\eta|}\,F(\eta)\,d\eta\,d\xi .
$$
Das Quadrat $S^2$ kann komplex sein. Die relativen Phasen von $q_A$ und $q_J$ kürzen sich im Produkt der beiden Umwandlungen.

Ohne die beiden internen Gegenwellen ist das Integral
$$
c^2 e^{iU}[H(J-U)+H(J+U)],
\qquad
H(w)=\int_0^1(1-d)e^{iwd}\,dd=\frac{1+iw-e^{iw}}{w^2}.
$$
Die beiden Dreiecke des Ortsquadrats geben die Phasen $J-U$ und $J+U$. Für die Gegenwellen ist der absolute Beitrag durch $|c|^2(2\rho+\rho^2)$ beschränkt, mit $\rho\ge|r|$, da die enthaltenen A-Weglängen nichtnegativ sind.

Schreibe $b=\delta_J+\delta_U$ für die Summe der Phasenradien um $J_0=9999\pi$ und $U_0=10001\pi$. Sei $d_-=U_0-J_0-b>0$ und $d_+=U_0+J_0-b>0$. Für den direkten Term gilt
$$
|e^{iU}H(J\pm U)|\le\frac1{d_\pm}+\frac b{d_\pm^2}.
$$
Der lineare Zählerterm liefert $1/d_\pm$. Für den übrigen Zähler vergleiche die Exponenten $U$ und $J+2U$ beim Pluszeichen sowie $U$ und $J$ beim Minuszeichen. Im Zentrum unterscheiden sie sich jeweils um ein ganzzahliges Vielfaches von $2\pi$. Nach dessen Abzug liegen die beiden Argumente in der oberen Halbebene und höchstens $b$ auseinander. Diese Form vermeidet eine wachsende Exponentialschranke für $J-U$ bei Verlusten.

Die dritte Ordnung hat nur die Kanalfolge $A\to J\to J\to A$. Ihre Norm ist höchstens $F_0(Cs x)^2(Cs x^2)$, mit den Green- und Randkonstanten $C,F_0$ der Vorarbeit. Ab vierter Ordnung genügt $F_0\theta^4/(1-\theta)$.

## J-Diagonale

Die erste Korrektur ist $iS x^2/2$. Bei der zweiten Ordnung verläuft der gemischte Beitrag über den A-Green-Kern. Nach Abzug der freien J-Phase lautet dessen direkter Teil
$$
-\frac{S^2 x^2}4
\frac{A}{U(1-r^2e^{2iU})}[H(U-J)+H(U+J)] .
$$
Die linearen Zählerterme der beiden $H$-Funktionen kombinieren sich mit der ersten Korrektur zum Faktor
$$
\frac{iS x^2}{2}\left[
1-\frac{U^2-A^2}{(U^2-J^2)(1-r^2e^{2iU})}
\right].
$$
Ohne den Grenzflächenfaktor bleibt in eckigen Klammern $(A^2-J^2)/(U^2-J^2)$. Die massive freie J-Dispersion macht den Zähler bei fester Dicke energieunabhängig. Über die Dickenbox ist sein Höchstwert $(A_0^2-J_0^2)(1+t)^2$, mit $t$ als relativer Dickentoleranz. Setze $\gamma=(A_0^2-J_0^2)(1+t)^2/(d_-d_+)$. Einschließlich des Grenzflächenfaktors ist der Betrag der Klammer durch $\gamma+(1+\gamma)\rho^2/(1-\rho^2)$ begrenzt.

Für die restlichen direkten Zählerterme gilt die Summe $b/d_-^2+b/d_+^2$. Die Bildterme in der A-Referenz geben zusätzlich $2\rho+\rho^2$, jeweils mit dem Vorfaktor $s^2x^2/[4(n_0-t)(1-\rho^2)]$ in der gleich großen Index- und Dickenbox. Der rein diagonale J-Beitrag zweiter Ordnung ist durch $(sx^2)^2/4$ begrenzt. Für die restliche Reihe genügt $F_0\theta^3/(1-\theta)$.

## Ergebnis im 100-MHz-Band

Es gelten die bisherigen gemeinsamen Grenzen $2{,}5\cdot10^{-7}$ für relativen Dickenfehler, reelle A-Indexabweichung und imaginären A-Index sowie $x\le10^{-3}$. Die folgenden Grenzen gelten stetig über die gesamte Parameterbox.

| Diagonalfehler | Analytische Obergrenze, aufgerundet |
| --- | ---: |
| $|T_{AA}-t_A|$ | $1{,}612\cdot10^{-6}$ |
| $|T_{JJ}-1|$ | $1{,}638\cdot10^{-6}$ |

In der Spurauslese gehen beide Fehler über das Maximum der Beträge in die Operatornorm des Diagonalfehlers ein. Wenn der J-Eintrag separat bekannt ist, bleiben mindestens $4{,}622\cdot10^{-6}$ für die skalare A-Kalibrierung und sonstige Beiträge. Wird auch J durch den freien Referenzwert eins modelliert, bleiben mindestens $4{,}596\cdot10^{-6}$, ausgehend von der abgerundeten Reserve $6{,}234\cdot10^{-6}$. Der Rücklauf ist darin bereits berücksichtigt. Die Reserve gilt für eine skalare Referenz, deren frequenzabhängige A-Transmission selbst hinreichend genau bestimmt ist. Bei konstanter Fortsetzung des A-Zentralwerts über das Band und Verwendung beider skalarer Diagonalen genügt für die komplexe Indexänderung $\sup_f|n(f)-n(f_0)|\le8{,}8443\cdot10^{-11}$ bei perfekter Zentralmessung oder $\le2{,}4781\cdot10^{-11}$ bei einem komplexen Messfehler von $2\cdot10^{-6}$. Dabei wird der übrige Rest ausschließlich für die in der Referenzrechnung aufgeführten Dispersions- und Grenzflächenterme verwendet.

Wolfram kontrollierte die Integralidentität, beide zentralen Werte von $H$ und die algebraische J-Kürzung exakt. Eine unabhängige 60-stellige Auswertung der vollen Transfermatrix prüfte die Bandmitte und zwei Randfälle, einschließlich eines verlustbehafteten. Die Kontrollen ersetzen die analytischen Bandschranken nicht. Die tatsächliche A-Transmission, die HCl/H-Anschlusskondition, freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

[Wolfram-Skript](op5_j_diagonalreferenz.wl) · [Tatsächliche Ausgabe](op5_j_diagonalreferenz.txt) · [Laufmanifest](op5_j_diagonalreferenz.json)
