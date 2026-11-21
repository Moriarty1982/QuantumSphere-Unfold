# OP5 – Endlicher Markerhub mit schwacher J-Beimischung

21. November 2026. Analytische Erkundung im Materieframe M. Eine exakt behandelte A-Schicht dient als Referenz für einen endlichen Phasenhub. Die J-Beimischung wird mit einer konvergenten Störungsreihe begrenzt. Das Modell gilt für zwei offene eindimensionale Kanäle mit gleichen Außenmedien links und rechts. Wellenzahlen und Admittanzen von J und A dürfen voneinander abweichen.

## Vorwissen geprüft

Die [Zweikanalrechnung](OP5_J_Zweikanal_Marker.md) gibt die exakte Blockmatrix, den Born-Kern und die Auslese über den Diagonalkontrast. Der [passive Vorwärtshub](OP5_J_Passiver_Vorwaertshub.md) behandelt die skalare Schicht und das gemeinsame Anschlussband. Die [Feldreferenz](OP5_J_Feldreferenz.md) liefert den Fehleranteil für Markierung und zeitgleiche Null. Die Suche nach endlichem Hub, Admittanzschranke und gekoppelter Schicht ergab keine bisherige Fehlerkontrolle um einen starken A-Hub. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft die Rechnung die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Exakte A-Referenz und auslaufender Kern

Verwende die flussnormierten Variablen der Vorarbeit. Für konstantes $g$, $q=D^{-1/2}v$ und $K=\operatorname{diag}(k_J,k_A)$ gilt in der Schicht $\psi''+K^2\psi+K gqq^\dagger\psi=0$. Wähle als Referenz den A-Anteil $g|q_A|^2$ und lasse J frei. Dann sind die exakten Referenzmatrizen $T_0=\operatorname{diag}(1,t_A)$ und $R_0=\operatorname{diag}(0,r_A)$. Die innere A-Wellenzahl und der interne Reflexionskoeffizient sind
$$
\kappa^2=k_A^2+k_A g|q_A|^2,\qquad r=\frac{\kappa-k_A}{\kappa+k_A}.
$$
Verwendet wird der Ast mit $\operatorname{Re}\kappa>0$ und $\operatorname{Im}\kappa\ge0$, sodass $|r|<1$. Für $\kappa$ nahe null oder stark evaneszente Schichten kann die folgende Schranke schlecht werden.

Der auslaufende A-Green-Kern in $[0,L]$ ist
$$
G_A(z,z')=
\frac{e^{i\kappa |z-z'|}+r e^{i\kappa(z+z')}
+r e^{i\kappa(2L-z-z')}+r^2 e^{i\kappa(2L-|z-z'|)}}
 {2i\kappa(1-r^2e^{2i\kappa L})}.
$$
Er folgt aus den beiden auslaufenden Lösungen $e^{-i\kappa z}+r e^{i\kappa z}$ und derselben Funktion an $L-z$. Der Wronskian normiert den Sprung der ersten Ableitung auf eins. Alle vier Längen im Zähler sind im Schichtinneren nichtnegativ. An beiden Grenzen geben die Werte die auslaufenden Amplituden bis auf freie Phasen. Daraus folgt für die mit $K$ gewichtete Green-Matrix die gleichmäßige Normgrenze
$$
C=\max\left\{\tfrac12,\frac{k_A}{2|\kappa|}\frac{(1+|r|)^2}{1-|r|^2}\right\}.
$$
Die von links eingespeiste innere Referenzlösung hat für Einheits-Eingangsnorm Supremumsnorm höchstens
$$
F_0=\max\{1,|1-r|/(1-|r|)\}.
$$
Hier liefert die skalare A-Lösung den Zähler $(1-r)[e^{i\kappa z}+r e^{i\kappa(2L-z)}]$ und den Nenner $1-r^2e^{2i\kappa L}$. Die exakte Referenz enthält den gesamten A-Hub einschließlich der Innenreflexionen. [Schicht- und Mehrfachreflexionsrechnung](https://arxiv.org/abs/1603.02720)

## Fehlerkontrolle bei endlichem A-Hub

Gegenüber der Referenz ist der zu iterierende Feldterm
$$
E=g\begin{pmatrix}|q_J|^2 & q_J\overline q_A\\ q_A\overline q_J&0\end{pmatrix},
\qquad
e_d=L|g||q_J|^2,\qquad
\theta=C L\|E\|_2.
$$
$\|E\|_2$ ist $|g|/2$ mal $|q_J|^2+\sqrt{|q_J|^4+4|q_Jq_A|^2}$. Für $\theta<1$ konvergiert die Neumann-Reihe der um die exakte Referenz gebildeten Gleichung. Der Integraloperator hat in der Supremumsnorm über die Schicht höchstens Norm $\theta$. Derselbe Operatorwert begrenzt die Auswertung an den Schichtgrenzen. Damit gelten für linken Einfall die Matrixgrenzen
$$
\|T-T_0\|_2,\quad\|R-R_0\|_2 \le \frac{F_0\theta}{1-\theta}.
$$
In der ersten Iteration tritt im Diagonaleintrag nur die direkte quadratische J-Komponente von $E$ auf. Der lineare Kreuzterm wandelt eine Mode um. Der Rest ab der zweiten Iteration ist je Eintrag durch $F_0\theta^2/(1-\theta)$ begrenzt. Für den zur markierten Spurauslese benötigten Kontrast folgt deshalb
$$
\left|T_{JJ}-T_{AA}-(1-t_A)\right|
\le F_0\left(C e_d+\frac{2\theta^2}{1-\theta}\right).
$$
Bei festen A-Daten ist der Kontrastfehler quadratisch im kleinen Verhältnis $|q_J/q_A|$. Die volle Matrixabweichung samt Umwandlung kann linear darin sein. Diese Abschätzung benötigt keinen kleinen A-Phasenhub und gilt ohne Annahme kleiner Wellenzahldifferenz.

Für eine Bandschranke sind das Infimum von $|1-t_A|$ sowie die Suprema der rechten Seiten und von $|r_A|$ über dasselbe Band und dieselbe Schicht zu bilden. Ein Rückweg mit Feldmatrix $F_{\rm rück}$ koppelt im einfachen Rücklaufmodell den reflektierten Feldanteil erneut in den Eingang. Ist $\|F_{\rm rück}\|\|R\|<1$, so ist sein Transmissionsrest gegenüber dem Einzelpass höchstens
$$
\frac{\|T\|\,\|F_{\rm rück}\|\|R\|}{1-\|F_{\rm rück}\|\|R\|}.
$$
Diese Schranke folgt aus dem geometrischen Rücklaufsummenoperator an der Eintrittsebene. Sie ergänzt den gemessenen oder modellierten Rückstreuwert. Eine exakt mitgemessene Rückwirkung kann stattdessen in der kalibrierten Feldmatrix berücksichtigt werden.

## Dimensionsloses Beispiel und Messbudget

Setze zur Illustration bei $E_0=0{,}360329$ eV $k_A L=10000\pi$, $\kappa L=10001\pi$, $k_J L=9999\pi$ und $|q_J/q_A|=10^{-3}$. Der skalare Referenzmarker hat am Bandzentrum exakt $t_A=-1$ und $r_A=0$. Die dimensionslose Normbedingung ergibt $\theta\simeq0{,}00314332$. Die analytischen Grenzen am Zentrum sind rund $2{,}30\cdot10^{-5}$ für den komplexen Diagonalkontrastfehler und $3{,}15\cdot10^{-3}$ für die Reflexionsnorm. Die gekoppelte $4\times4$-Transferrechnung am gleichen Punkt liefert rund $3{,}14\cdot10^{-6}$ bzw. $1{,}57\cdot10^{-10}$. Die geringe Reflexion am Zentrum ist im Beispiel an die Schichtphase gebunden.

Für dasselbe Beispiel nehme über 100 MHz einen reellen, konstanten Index $\kappa/k_A=1{,}0001$, konstantes Fluss-Kopplungsverhältnis und $k_A\propto E$ an. Dann ist $C=1/2$ und $F_0=1$. Mit relativer Bandhalbweite $u=h_E/E_0$ ist die skalare Kontrastuntergrenze $2\cos(\pi u/2)-2r^2/(1-r^2)$. Die skalare Reflexionsobergrenze ist $2r(\kappa_0L)u/(1-r^2)$, da die genaue Reflexion am Bandzentrum null ist. Die zweikanaligen Schranken geben kombiniert
$$
\inf_E |T_{JJ}-T_{AA}|\ge 1{,}9999770,\qquad
\sup_E \|R\|_2\le 0{,}003156
$$
mit konservativer Rundung. Dieser Modellfall zeigt einen robust großen Kontrast. Die analytische Reflexionsschranke allein zertifiziert noch keinen unberücksichtigten Rest im Quotientenbudget von rund $9{,}82\cdot10^{-6}$. Wenn ausschließlich der Rücklauf dieses Budget nutzen dürfte, müsste im einfachen Rücklaufmodell beispielsweise $\|F_{\rm rück}\|\lesssim0{,}0031$ gelten. Der einzelne exakte Punkt ist keine Zertifizierung des gesamten Bandes.

Die schwache HCl/H-Anschlussschranke wird durch einen starken Feldmarker nicht verbessert. Reale Dispersions- und Verlustparameter, Fluss-Kopplungsverhältnis, Empfängerrücklauf, freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_endlicher_markerhub.wl) · [Tatsächliche Ausgabe](op5_j_endlicher_markerhub.txt) · [Laufmanifest](op5_j_endlicher_markerhub.json)

Wolfram kontrollierte Wronskian, Randbedingungen und Normpolynom und berechnete die Schranken sowie einen vollständigen Transferpunkt mit 55-stelliger Eingabe. Die Bandschranke folgt aus der analytischen Abschätzung, ohne numerisches Frequenzgitter. Reproduzierbar mit **wolframscript -file op5_j_endlicher_markerhub.wl**.
