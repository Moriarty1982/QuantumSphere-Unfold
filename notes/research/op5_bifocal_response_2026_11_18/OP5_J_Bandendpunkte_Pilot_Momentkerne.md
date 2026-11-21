# OP5 – Schmalbandige Endpunkte, bidirektionaler Pilot und endliche Momentkerne

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Resonator- und Momentrechnung](OP5_J_Resonator_Pilot_Momentprofil.md) lässt die punktweise Kalibrierung der beiden Bandenden, den gerichteten Referenztransfer und ein endlich breites Momentprofil offen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur lokalen Auslese. I3 setzt eine eigenständige kosmologische Bestandsdynamik voraus.

## Zwei schmalbandig abgestimmte Endpunkte

Bei der bisherigen Zweiband-Laufzeitdifferenz sind für den Kalibrierbeitrag nur die komplexen Werte an den beiden tatsächlich gemessenen Bandenden erforderlich. Zwei einzeln eingestellte Resonanzen können deshalb die Forderung eines durchgehend 100 MHz breiten Konverters für genau diesen Beitrag ersetzen. Unabhängig zu sichern bleiben die Zweigwahl der entfalteten Modalphase, die kohärente Referenz und der kontrollierte Unterschied der Kalibrierzustände. Eine Zweipunktprüfung zertifiziert keine bandweite Rücklauf- oder Transmissionsgrenze.

Im verlustfreien symmetrisch ausgekoppelten Zweimodenresonator der Vorarbeit seien $\delta_A,\delta_J$ die Abstände der beiden Modenresonanzen vom jeweiligen Messpunkt, als Winkelfrequenzen. Der dimensionslose Reflexionsbetrag erfüllt
$$
|S_{AA}|^2=
\frac{\delta_A^2\delta_J^2+g^2(\delta_A-\delta_J)^2}
     {4g^4+\delta_A^2\delta_J^2+g^2(\delta_A-\delta_J)^2}.
$$
Bei $g/(2\pi)=8{,}713$ MHz und $p=9\cdot10^{-6}$ sind rein gemeinsamer Detuningsfehler und reine symmetrische Resonanzaufspaltung sehr verschieden. Der gemeinsame Frequenzfehler darf bei alleiniger Nutzung des Budgets rund $37$ kHz betragen. Die Differenz der beiden Resonanzfrequenzen darf bei perfekt getroffenem Mittelwert nur rund $157$ Hz betragen. Ein allgemeiner Fehler muss die gemeinsame Ungleichung für beide Beiträge erfüllen. Beide Endpunkte benötigen ihren eigenen komplexen Abgleich.

Eine unsymmetrische Auskopplung kann am Zentrum trotz A-Verlust die direkte A-Reflexion genau auslöschen. Für innere Verlustraten $\alpha_A,\alpha_J$ und äußere Kopplungen $\kappa_A,\kappa_J$ ist dafür
$$
\kappa_A=\alpha_A+\frac{g^2}{\kappa_J+\alpha_J}
$$
zu wählen. Die Konversionsleistung am Zentrum ist dann
$$
\eta=\frac{\kappa_J}{\kappa_J+\alpha_J}
     \frac{g^2}{g^2+\alpha_A(\kappa_J+\alpha_J)} .
$$
Die A-Null allein belegt deshalb keine vollständige Konversion. Bei $\alpha_J=0$, $\alpha_A/g\simeq2{,}50$ und beispielhaft $\eta=0{,}99$ muss $\kappa_J/g\simeq0{,}00404$ sein. Der Rücklaufrest $|S_{AA}|\le9\cdot10^{-6}$ erlaubt in diesem Modell dann nur etwa $0{,}64$ Hz gemeinsamen Frequenzfehler am jeweiligen Endpunkt. Das ist eine mögliche punktweise Einstellung mit deutlich engerer Stabilitätsanforderung, keine Forderung an das ganze Band. Die Konversionsamplitude und ihre Phase müssten unabhängig vermessen werden.

Sind beide inneren Verluste positiv, maximiert Auskopplung in J bei gleichzeitiger A-Anpassung die Leistung bis $\eta_{\max}=(\sqrt{1+C}-1)/(\sqrt{1+C}+1)$ mit $C=g^2/(\alpha_A\alpha_J)$. Ein Leistungsziel von $0{,}99$ setzt $C\ge39600$ voraus. Bei dem eingesetzten A-Verlustmaßstab darf die innere J-Verlustrate in Frequenzeinheiten nur rund $88$ Hz erreichen. Die Rechnung setzt separat adressierbare Moden voraus und liefert keine physische Verlust- oder Phasenkalibrierung.

## Pilotkalibrierung mit zwei gerichteten Wellenstandards

Für jeden Zustand von Leerkörper oder Marker seien die komplexen einlaufenden Vorwärts- und Rückwärtsamplituden zweier unabhängiger Standards als Spalten einer bekannten Matrix $A$ an derselben Referenzebene gegeben. Der unbekannte kalibrierstabile komplexe Empfängerblock $K$ enthält die endliche Richtwirkung und mögliche monokanalige Verstärkungen. Mit gemessener Standardmatrix $X=KA$ und Betriebsvektor $y=Ka$ folgt
$$
a=AX^{-1}y.
$$
Die tatsächlichen Wellenamplituden der beiden Standards sind nötig. Bekannte Rücklaufverhältnisse allein lassen je Zustand die gemeinsame relative Normierung frei. Der Maßstab darf in beiden Zuständen gemeinsam unbekannt sein, sofern er nachweislich in deren Quotienten herausfällt. Die Kalibrierung und der Betrieb müssen denselben Empfängerpfad teilen oder unabhängig für denselben Gain normiert sein.

Für Messfehler setze $E=K^{-1}\delta X A^{-1}$, $F=\delta A A^{-1}$ und $\nu=K^{-1}\delta y$. Dann ist die exakte Fehleridentität
$$
\widehat a-a=(F-E)(I+E)^{-1}a+(I+F)(I+E)^{-1}\nu .
$$
Bei $\|E\|<1$ ergibt sich die entsprechende Normhülle mit Nenner $1-\|E\|$. Für $A=\bigl(\begin{smallmatrix}1&1\\0{,}5&-0{,}5\end{smallmatrix}\bigr)$, normierte Empfängerdiagonale eins, beide Kreuzleckamplituden bis $0{,}01$ und $\|\delta A\|,\|\delta X\|,\|\delta y\|\le3\cdot10^{-10}$ ergibt sich bei $|a^+|=1$, $|a^-/a^+|\le1{,}04\cdot10^{-4}$ ein relativer Vorwärtsfehler unter $1{,}156\cdot10^{-9}$ je Zustand. Das komplexe Leerkörper-/Marker-Verhältnis hat unter diesen Bedingungen einen Fehler unter $2{,}312\cdot10^{-9}$. Das liegt knapp unter der früher angesetzten Einzelgrenze von $2{,}5\cdot10^{-9}$. Die Inversion ersetzt extrem reine Richtkoppler durch separat sehr genaue Wellenstandards und Messdaten. Sie beweist diese Genauigkeit auf einer physischen Ebene nicht.

## Endlich breite glatte Kerne für das Momentprofil

Die [Momentrechnung](OP5_J_Resonator_Pilot_Momentprofil.md) begrenzt das Infimum der Totalvariation bei beiden zusätzlichen logarithmischen Achsenbedingungen. Eine endlich breite Konstruktion ersetzt die acht rationalen Knoten durch disjunkte symmetrische Kerne. Verwende pro Knoten die normierte Dichte aus $(1-t^2)^{12}$ auf $[-1,1]$, auf Halbbreite $h$ skaliert, und falte mit einem nichtnegativen symmetrischen glatten Kern von Radius $\delta=10^{-9}$. Dafür kann der normierte Kern $\exp[-1/(1-(t/\delta)^2)]$ im offenen Träger verwendet werden. Die Randknoten rücken um $h+\delta$ nach innen. Für die unten angegebenen Breiten überschneiden sich die Träger nicht. Die acht Amplituden sind durch die **exakten** gemittelten Momente in den Basisfunktionen $1,u,\dots,u^5,u\log(2u),u^2\log(2u)$ bestimmt.

Zur Zertifizierung kann der Logarithmus über das Taylorpolynom vom Grad 60 substituiert werden. Sein Rest ist auf dem Annulus höchstens $1/(61\,2^{60})$. Die normierten ungeraden Beta-Momente sind null und die geraden Momente lauten $(1/2)_k/(27/2)_k$. Die symmetrische Glättung ändert die Integrale um höchstens $16\delta^2$ pro Matrixeintrag, weil alle Basisfunktionen zweite Ableitung höchstens 32 im Betrag haben. Rationale Auswertung dieser Ersatzmatrix und eine Neumann-Schranke für die Inverse sichern die Existenz der exakten Gewichte. Die Totalvariation von $P$ ist die Summe ihrer Beträge. Der Spitzenwert von $|P'|$ in $u$ ist höchstens der größte Gewichtsbetrag mal dem unvergrößerten Beta-Spitzenwert $\beta(0)/h$. Die Umrechnung in den physischen Gradienten liefert den Faktor $2\sqrt{3/4}/R_c$.

| Halbbreite $h$ in $u$ | Zertifizierte Obergrenze für $\operatorname{TV}(P)$ | Obergrenze für $R_c\sup|dP/dr|$ |
| ---: | ---: | ---: |
| $0{,}0001$ | $96334{,}44$ | $6{,}509\cdot10^8$ |
| $0{,}001$ | $99342{,}66$ | $6{,}842\cdot10^7$ |
| $0{,}005$ | $116181{,}56$ | $1{,}762\cdot10^7$ |

Die Werte trennen die relative Gewichtsempfindlichkeit vom absoluten Spitzenbedarf. Für ein isoliertes $b_4$-Gradientensignal und ein Prozent Potentialgenauigkeit reicht bei diesem Träger $R_c\eta_a/|\Phi_0|\le0{,}0273205$, falls der gesamte Fehler dem absolut kalibrierten Gradienten zugewiesen wird. Außenreferenz, Transfer, gewöhnliche Restterme und mögliche Längsendfehler verkleinern das Budget. Auch ein mathematisch glattes Profil mit den gewünschten Momenten braucht eine nachgewiesene materielle Ansteuerung. Physische J-Ausbreitung, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram prüfte die Resonatoridentitäten und Frequenzgrenzen, die numerische bidirektionale Pilothülle sowie die rationalen Integralmatrixgrenzen für die endlichen Momentkerne. Qiskit wurde für diese klassischen Streu- und Potentialrechnungen erwogen.

[Wolfram-Skript](op5_j_bandendpunkte_pilot_momentkerne.wl) · [Tatsächliche Ausgabe](op5_j_bandendpunkte_pilot_momentkerne.txt) · [Laufmanifest](op5_j_bandendpunkte_pilot_momentkerne.json)
