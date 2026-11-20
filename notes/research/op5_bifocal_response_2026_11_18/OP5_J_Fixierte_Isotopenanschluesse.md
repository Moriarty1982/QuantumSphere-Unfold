# OP5 — Zwei fixierte neutrale Isotope als Dipolanschlüsse

20. November 2026. Analytische Erkundung im Materieframe M. Rückwärts gesucht ist eine zweite innere Stromrichtung ohne ansteuerbare Schwerpunktbewegung.

## Vorwissen geprüft

Die [gebundenen Anschlüsse](OP5_J_Gebundene_Anschluesse.md) ergeben bei fixiertem Schwerpunkt eine Stromrichtung je neutralem Proton–Elektron-Paar. Der [gemeinsame J-Strom](OP5_J_Gemeinsamer_Strom.md) liefert die Punktkernladung $3A$ und eine statische Isotopendifferenz. Der [Wasserstoff-Spektralvergleich](OP5_J_Wasserstoffspektrum.md) benutzt denselben effektiven J-Vertex. Hier geht es um innere elektrische Dipolbewegungen im selben Frequenzfenster. Der [kohärente A/B-Vergleich](OP5_J_Sende_Empfangsports.md) braucht separat verfügbare Anschlüsse an beiden Enden und stabile Übertragungsmatrizen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört der Befund zur lokalen Auslese. Die bei I3 erforderliche Populationsdynamik bleibt davon getrennt.

## Die innere Dipolrichtung einer Atomsorte

Der nichtrelativistische Punktkern einer neutralen Sorte $s$ hat Masse $M_s$, elektrische Ladung $Z_s e$ und J-Ladung $3A_s g_J$ mit Massenzahl $A_s$. Jedes Elektron hat Ladungen $(g_J,-e)$. Sei $\mathbf x_N$ die Kernposition, $\mathbf R$ der gemeinsame Massenschwerpunkt und $\mathbf X=\sum_{a=1}^{Z_s}(\mathbf x_N-\mathbf x_a)$. Aus der Schwerpunktbedingung folgt
$$
\mathbf x_N=\mathbf R+\frac{m_e}{M_s+Z_s m_e}\mathbf X,\qquad
\binom{\mathbf D_J}{\mathbf D_A}
=\binom{(3A_s+Z_s)g_J\mathbf R}{0}+
\binom{-g_J(1-\epsilon_s)}{e}\mathbf X,\qquad
\epsilon_s=\frac{(3A_s+Z_s)m_e}{M_s+Z_s m_e}.
$$
Bei festem $\mathbf R$ wird der integrierte Strom durch dieselbe Feldrichtung mal $\dot{\mathbf X}$ beschrieben. Alle internen elektrischen Dipolübergänge derselben Sorte in derselben räumlichen Projektion haben deshalb in diesem Modell dasselbe Verhältnis der Feldkomponenten. Das gilt auch bei mehreren Elektronen mit elektronischen Korrelationen, da die Beziehung eine Operatoridentität der Dipole ist. Kerninterne Bewegung, relativistische Korrekturen und höhere Multipole sind hier weggelassen.

Für zwei getrennt anregbare und auslesbare Sorten ist die Determinante ihrer Dipolrichtungen $e g_J(\epsilon_1-\epsilon_2)$, wenn die Richtungen als Spalten in der Reihenfolge 1, 2 stehen. Bei $e g_J\ne0$ und endlichen, nichtverschwindenden Antworten folgt Rang zwei genau für $\epsilon_1\ne\epsilon_2$. Ein gemeinsamer invertierbarer Feldbasiswechsel erhält diese Aussage. Die beiden Antworten müssen sich bei derselben Frequenz unabhängig erfassen lassen. Das bloße Vorhandensein beider Sorten in einem Gemisch sichert das nicht.

## Konditionierung im kanonischen Vergleich

Für $K=I$ setze $\rho=|g_J/e|>0$, $u_s=1-\epsilon_s$ und nehme wie bei H und D $u_1,u_2>0$ an. Nach Entfernen der jeweiligen relativen Verstärkung und Normierung auf Einheitslänge haben die zwei Zeilen die Richtungen $(-\rho u_s,1)$. Eine gemeinsame Spiegelung deckt negatives $g_J/e$ ab. Ihre Winkeltrennung und die spektrale Konditionszahl lauten
$$
|\sin\theta|=\frac{\rho|u_1-u_2|}{\sqrt{(1+\rho^2u_1^2)(1+\rho^2u_2^2)}},\qquad
\kappa_2=\sqrt{\frac{1+|\cos\theta|}{1-|\cos\theta|}}.
$$
Die quadratische inverse Winkelfunktion ist bis auf den Faktor $|u_1-u_2|^{-2}$ gleich $\rho^{-2}+u_1^2+u_2^2+\rho^2u_1^2u_2^2$. Für ungleiche $u_s>0$ wird die beste Konditionierung daher bei $\rho^2=1/(u_1u_2)$ erreicht:
$$
|\sin\theta|_{\max}=\frac{|u_1-u_2|}{u_1+u_2},\qquad
\kappa_{2,\min}=\frac{(\sqrt{u_1}+\sqrt{u_2})^2}{|u_1-u_2|}.
$$
Das gilt ebenso nach Absorption einer diagonal positiven Kinetik in das effektive Kopplungsverhältnis. Bei allgemeiner Mischung muss die Konditionierung in der kanonischen Norm neu berechnet werden. Mit $B=K^{-1/2}$ ergibt sich aus der Flächenformel für beliebige zwei Richtungen $v_s$
$$
|\sin\angle(Bv_1,Bv_2)|
=\frac{|\det B|\,\|v_1\|\,\|v_2\|}{\|Bv_1\|\,\|Bv_2\|}|\sin\angle(v_1,v_2)|
\le \kappa_2(B)|\sin\angle(v_1,v_2)|.
$$
Damit bleibt eine kleine Winkeltrennung bei mäßig konditioniertem $B$ klein. Die konkrete Zahl unten gilt für den diagonal-kinetischen Vergleich. Messfehler und profilgebundene Endpunktänderungen werden durch die Inversion kleiner singulärer Werte verstärkt. Für eine lineare Rekonstruktion $P=L^{-1}H R^{-1}$ bei festen bekannten Endpunktmatrizen ist die absolute Fehlerverstärkung in Spektralnorm höchstens $\|L^{-1}\|_2\|R^{-1}\|_2$. Für die Eigenphasenmethode ist dies keine eigene Fehleranalyse.

## H und D mit CODATA-Massen

Für H gilt $\epsilon_H=4/(1+m_p/m_e)$ und für D $\epsilon_D=7/(1+m_d/m_e)$. Verwendet werden die Proton- und Deuteronmassen relativ zur Elektronenmasse aus [CODATA 2022](https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf). Der Unterschied beträgt rund $2{,}707\times10^{-4}$. Bei $\rho=1$ beträgt die kleinere Singularzahl der normierten Portmatrix rund $9{,}59\times10^{-5}$. Selbst bei optimalem $\rho$ bleibt $\kappa_2$ bei rund $1{,}475\times10^4$. Das ist ein Rang-zwei-Beispiel mit schlecht trennbaren Anschlüssen. Reale Suszeptibilitäten, Rauschpegel und unabhängige Adressierung sind zusätzliche offene Bedingungen.

[Wolfram Language](op5_j_fixierte_isotopenanschluesse.wl) prüft Determinante, Winkeloptimierung und numerische Konditionierung. Tatsächlich erzeugte Print-Ausgabe

```text
symbolic determinant = -(rho*(u - v))
stationary sine residual = 0
optimal sine squared = (u - v)^2/(u + v)^2
H recoil coefficient = 0.00217728230095358968557196813546826087`10.
D recoil coefficient = 0.00190658653782913922414553143919969516`10.
absolute recoil splitting = 0.00027069576312445046142643669626856571`10.
balanced normalized singular values = {1.41421355912146192392259842447102942891`10., 0.00009590102877215716649050100228233072`10.}
balanced normalized condition = 14746.5942464639012544048`10.
best diagonal-kinetic coupling ratio = 1.0020461216626864961767263610372563987`10.
best diagonal-kinetic normalized condition = 14746.5634404136793064994`10.
```

Der separate Rückgabewert war `Null`. Die Rechnung ist symbolische und numerische lineare Algebra für eine klassische lineare Antwort. Eine Qiskit-Schaltung würde zur fehlenden unabhängigen Adressierung oder zur Konditionierung dieser Anschlussmatrix keine zusätzliche Information liefern. Physische Kopplung, stabil kalibrierte Anschlüsse und H96 bleiben offen.
