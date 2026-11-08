# HC-Beobachterwechsel und das Flächenquantum aus r10

7. November 2026. Analytische Erkundung zu T6/T14. [r10.3](v4_10_0_r10/README.md) benennt ein frameabhängiges Flächenquantum als zusätzliche Annahme. [r11.5](v4_10_0_r11/README.md) ordnet den HC-Boost als möglichen kinematischen Anschluss ein. Geprüft wird dieselbe Horizontfläche mit unverändertem zugänglichem Zustandsraum, wie in dieser Lesart vorausgesetzt.

Im lokalen Feldmodell verbindet der äußere HC-Boost Beobachter gleicher Feldskala mit entgegengesetztem Energiefluss. Er liefert einen Uhrfaktor $G=n/|s|$. Das sagt zunächst nichts über den Spektralabstand eines Flächenoperators aus.

Falls der Profilwechsel auf dem Horizontzustandsraum als unitäre Äquivalenz desselben Flächenoperators implementiert wird, gilt $\widehat A_T=U\widehat A_MU^{-1}$. Beide Operatoren haben dasselbe Spektrum. Insbesondere ist bei einer kleinsten positiven Spektralfläche $a_{\min}$ diese Größe in beiden Profilen gleich. Die zusätzliche Forderung, dass sich dieselbe Spektralmenge um $1/G$ skaliert, verlangt dann $a_{\min}=a_{\min}/G$, also $G=1$. Für den r10-Wert $G=1{,}8647$ ist dieser konkrete Anschluss ausgeschlossen.

Dasselbe zeigt der lokale Energie-Temperatur-Vergleich von r10.1. Bei einem gemeinsamen Wechsel der Normierung des Horizontflusses skalieren seine Energie und seine Temperatur gemeinsam. Ihr Verhältnis bleibt gleich. Eine reine Normierungsänderung erzeugt daher keine neue Gewichtung der Flächenstufen. Eine Skalierung des Flächenquantums verlangt eine zusätzliche Modellabbildung, etwa einen anderen Flächenoperator oder einen begründet anderen zugänglichen Spektralbereich. Deren Konstruktion ist offen. Das Argument setzt die unitäre Implementierung desselben Operators und eine kleinste positive Fläche voraus. Es schließt anders definierte Profile nicht aus.

Für QAM sind damit Uhrfaktor, Horizontzugang und Flächenoperator getrennte Daten. Der Feldboost kann den Uhrfaktor liefern, während die Spektralabbildung als eigene Beweispflicht bestehen bleibt. Aus dieser Prüfung folgt keine Änderung der Zählregel oder der Vorhersagen.

## Kann eingeschränkter Zugang das Flächenquantum verkleinern?

Nimm an, dass T aus dem M-Zustandsraum nur einen kleineren Bereich auswählt und dass die ursprüngliche Flächenmessung auf diesem Bereich erhalten bleibt. Ein reduzierender Teilraum des Flächenoperators enthält nur Spektralwerte des ursprünglichen Operators. Die kleinste zugängliche positive Fläche kann dadurch gleich bleiben, steigen oder ganz entfallen. Sie kann nicht unter die kleinste positive M-Fläche sinken. Insbesondere kann eine Beschränkung auf eine Teilmenge der vorhandenen Spinsektoren bei unverändertem Operator die in r10 verlangte Verkleinerung um $1/G$ für $G>1$ nicht erklären.

Eine andere Operation ist die Kompression $P\widehat A P$ auf einen Teilraum, den $\widehat A$ nicht erhält. Im zweidimensionalen Vergleichsmodell $\widehat A=\operatorname{diag}(0,a)$ hat die Kompression auf die von $\psi=\sqrt{1-1/G}\,e_0+G^{-1/2}e_1$ erzeugte Gerade den einzigen Eigenwert $a/G$. Bei einer ursprünglichen Flächenmessung auf $\psi$ wären die Ausgänge aber weiterhin $0$ und $a$, mit Wahrscheinlichkeiten $1-1/G$ und $1/G$. Der neue Eigenwert ist ihr Erwartungswert. Als scharfe Fläche gehört er zum komprimierten Operator und damit zu einer anderen Auslesung. Die Wahl des Teilraums setzt $G$ in diesem Beispiel bereits ein.

Der Unterschied ist für QAM entscheidend. Spektrale Auswahl kann Zählgewichte ändern, aber bei gleichem Operator keine kleineren positiven Messausgänge erzeugen. Eine effektive Auslesung könnte kleinere Werte haben, benötigt jedoch eine physikalische Begründung und einen unabhängigen Mechanismus für die Wahl des Teilraums. Das Vergleichsmodell verwendet keinen nativen Horizontzustand.

## Gleicher Mittelwert, verschiedene Flächenstatistik

Sei $A$ eine nichtnegative Flächenmessung mit Ausgängen in $\{0\}\cup[a,\infty)$ und endlichem zweiten Moment. Punktweise gilt $A^2\ge aA$. Für jeden Zustand mit mittlerer Fläche $\mu\in(0,a)$ folgt

$$
\operatorname{Var}(A)\ge\mu(a-\mu).
$$

Gleichheit tritt genau dann ein, wenn nur die Werte $0$ und $a$ positive Wahrscheinlichkeit tragen. Für $\mu=a/G$ ist die Mindestvarianz $a^2(G-1)/G^2$. Beim nominalen r10-Faktor $G=1{,}8647$ beträgt die Mindeststandardabweichung ungefähr $0{,}499a$. Die relative Standardabweichung ist mindestens $\sqrt{G-1}\approx0{,}930$. Ein Zustand mit scharfem Eigenwert $a/G$ eines effektiven Operators hat dagegen Varianz null bezüglich dieses Operators.

Damit können erste und zweite Momente eine konkrete Zuordnung unterscheiden. Bei bekannter Untergrenze $a$ und Mittelwert unterhalb davon würde eine nachweislich kleinere Varianz als $\mu(a-\mu)$ die ursprüngliche Messung mit dieser Spektrallücke ausschließen. Die Rechnung betrifft Verteilungen der Einzelergebnisse einer deklarierten Messung. Die Varianz eines Mittelwertschätzers aus vielen Wiederholungen ist eine andere Größe. Die Aussage setzt keine native Messvorschrift für den effektiven Operator voraus.

## Exponentielles Gewicht bei gleicher mittlerer Fläche

Für $\lambda>0$ sei das spektral ausgewertete Gewicht $W=\mathbb E[e^{-\lambda A}]$. Dies ist eine Zustandsauslesung. Eine Identifikation mit der vollständigen Zustandssumme aus r10 würde zusätzlich deren Entartungen und Zustandsgewichte benötigen. Wenn $A$ Werte in $\{0\}\cup[a,\infty)$ hat und $\mu=\mathbb E[A]=a/G$ mit $G>1$, folgt

$$
W\ge 1-\frac1G+\frac{e^{-\lambda a}}G
> e^{-\lambda a/G}.
$$

Für den ersten Schritt liegt die Exponentialfunktion bei $A=0$ und $A=a$ auf ihrer Sekante. Für $A>a$ liegt sie strikt über der fortgesetzten Sekante, da sie streng konvex ist. Mittelung der Sekante liefert die untere Schranke. Das Zweiniveaubeispiel erreicht sie. Die zweite Ungleichung ist die strikte Konvexität auf $[0,a]$. Der rechte Ausdruck ist das Gewicht eines scharfen effektiven Flächenwerts $a/G$.

Bei der gewählten dimensionslosen Normierung $\lambda a=1$ und $G=1{,}8647$ ist die untere Schranke für die alte Messung ungefähr $0{,}6610$. Der scharfe effektive Wert liefert ungefähr $0{,}5849$. Die Zahlen dienen dem Vergleich und sind keine Horizontzustandssumme. Wer die Flächenmessung zunächst auf ihren Mittelwert reduziert und danach die Exponentialfunktion anwendet, ändert somit die Gewichtung. Eine Begründung des effektiven Flächenoperators muss erklären, welche dieser Auslesungen in die r10-Zählung eingeht.

## Kann ein scharfer Wert ein gemischtes Gewicht nachbilden?

Bei einer einzelnen Gewichtung $\lambda>0$ kann jede Flächenverteilung durch den angepassten Wert $a_{\rm eff}(\lambda)=-\log W(\lambda)/\lambda$ dargestellt werden. Für einen nichtkonstanten nichtnegativen Flächenausgang ist dieser Wert streng fallend in $\lambda$. Denn für $0<\lambda_1<\lambda_2$ ist $x\mapsto x^{\lambda_2/\lambda_1}$ streng konvex und damit $W(\lambda_2)>W(\lambda_1)^{\lambda_2/\lambda_1}$. Ein scharfer Flächenausgang hat dagegen für alle $\lambda$ denselben angepassten Wert. Für endlichen ersten Moment konvergiert $a_{\rm eff}(\lambda)$ bei $\lambda\to0^+$ zum Mittelwert. Hat die Verteilung positive Wahrscheinlichkeit für den Ausgang null, konvergiert der angepasste Wert bei $\lambda\to\infty$ gegen null.

Im Zweiniveaubeispiel mit $G=1{,}8647$ ergibt sich für $\lambda a=1$ der angepasste Wert ungefähr $0{,}4140a$, für $\lambda a=2$ ungefähr $0{,}3116a$. Ein einzelnes exponentielles Gewicht kann also einen scharfen Wert vortäuschen, dessen Größe von der Auswertung abhängt. Zwei exakt bestimmte Gewichte bei verschiedenen positiven $\lambda$ können einen konstanten scharfen Wert von einer nichtkonstanten Flächenverteilung unterscheiden, sofern beide aus derselben Präparation und demselben Operator stammen.

Im r10-Setup erzeugt ein bloßer Wechsel des Beobachterabstands keine zweite Gewichtung, da Energie und Unruh-Temperatur gemeinsam skalieren. Für diesen Abgleich braucht es daher entweder einen unabhängig verfügbaren zweiten Ausleseparameter oder die Messung eines zweiten Moments. Das Argument betrifft das Gewicht eines Zustands und wird nicht auf die vollständige Zählgleichung übertragen.

## Kompression vor und nach der exponentiellen Gewichtung

Im endlichdimensionalen Vergleichsmodell sei $P$ der orthogonale Projektor auf den zugänglichen Teilraum und $A_{\rm eff}=PAP$ auf dessen Bild. Auf diesem Teilraum sind die beiden Auslesungen $P e^{-\lambda A}P$ und $e^{-\lambda A_{\rm eff}}$ verschieden zu behandeln. Die nullte und erste Ordnung stimmen überein. In zweiter Ordnung gilt

$$
P e^{-\lambda A}P-e^{-\lambda A_{\rm eff}}
=\frac{\lambda^2}{2}\,PA(I-P)AP+O(\lambda^3).
$$

Der Koeffizient ist positiv semidefinit, weil $PA(I-P)AP=((I-P)AP)^\dagger((I-P)AP)$. Er verschwindet als Operator genau dann, wenn $A$ den zugänglichen Teilraum erhält. Für selbstadjungiertes $A$ ist dieser Teilraum dann reduzierend, und beide Auslesungen stimmen für alle $\lambda$ überein. Umgekehrt würde Übereinstimmung für alle hinreichend kleinen positiven $\lambda$ den quadratischen Koeffizienten zum Verschwinden zwingen.

Im Zweiniveaubeispiel mit der komprimierten Fläche $a/G$ ist der Koeffizient vor $\lambda^2/2$ genau $a^2(G-1)/G^2$. Das ist die Varianz der ursprünglichen Flächenmessung im gewählten Zustand. Die Rechnung lokalisiert somit die erste Abweichung der exponentiellen Auslesungen in der Kopplung zwischen zugänglichem und ausgeblendetem Teilraum.

Für eine r10-Anwendung müsste feststehen, ob zuerst die ursprüngliche Flächenmessung gewichtet und dann ihr Zugriff eingeschränkt wird oder ob der komprimierte Operator selbst in die Gewichtung eingeht. Falls beide Auslesungen als dieselbe modelliert werden sollen, zeigt die endliche Rechnung die notwendige Reduktionsbedingung. In diesem Fall kann die kleinste positive Fläche durch die Einschränkung nicht sinken. Das ist ein Operatorvergleich im endlichen Modell und kein Nachweis für einen konkreten Horizontoperator.

## Spurvergleich bei einer festen Gewichtung

Auf dem endlichen zugänglichen Teilraum wähle eine orthonormale Eigenbasis $\psi_j$ von $A_{\rm eff}$ mit Eigenwerten $\mu_j$. Dann ist $\mu_j=\langle\psi_j,A\psi_j\rangle$. Strikte Konvexität liefert für jedes feste $\lambda>0$

$$
\langle\psi_j,e^{-\lambda A}\psi_j\rangle
\ge e^{-\lambda\mu_j}.
$$

Gleichheit beim einzelnen Vektor verlangt eine auf einen einzigen Eigenwert konzentrierte ursprüngliche Flächenmessung. Dann gilt $A\psi_j=\mu_j\psi_j$. Summiert man über die Eigenbasis, ergibt sich

$$
\operatorname{tr}_{P}\!\left(Pe^{-\lambda A}P\right)
\ge \operatorname{tr}_{P}e^{-\lambda A_{\rm eff}}.
$$

Gleichheit bei auch nur einem positiven $\lambda$ gilt genau dann, wenn $A$ den gesamten zugänglichen Teilraum erhält. Andernfalls ist mindestens ein Summand strikt größer. Die Aussage betrifft die Spur, keine Ordnung der beiden Operatoren. Sie stärkt den Vergleich über die Taylorentwicklung: Für eine endliche, nichtreduzierende Kompression lassen sich die beiden Spurgewichte am selben festen $\lambda$ schon grundsätzlich unterscheiden.

Der Spurvergleich verwendet dieselbe zugängliche Basis und das gleiche Gewichtungsmaß auf beiden Seiten. Für die r10-Zählgleichung müsste zuerst gezeigt werden, dass ihre jeweiligen Entartungen und Zugangsregeln durch genau diese beiden Spurformulierungen beschrieben werden. Eine Übereinstimmung der Flächenmittelwerte allein liefert diesen Schritt nicht.

## Was die Zählgleichung aus r10 tatsächlich vergleicht

Die [r10-Erkundung](v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md) setzt im Ein-Punkt-Modell $\sum_j g(j)e^{-2\pi\gamma a(j)}=1$. Bei festem $\gamma$ und denselben positiven Gewichten kann die Beschränkung von allen Spins auf $j=1/2$ als Spektralauswahl dargestellt werden. Sie lässt die vorhandene Flächenstufe unverändert, entfernt aber positive Summanden. Ist die volle Summe bei $\gamma_M$ eins, ist die eingeschränkte Summe dort strikt kleiner als eins. Weil sie mit $\gamma$ streng fällt, braucht ihre erneute Normierung auf eins ein kleineres $\gamma_T$, sofern die eingeschränkte Gleichung eine positive Lösung hat.

Die beiden normierten r10-Gleichungen vergleichen somit verschiedene Spektralstützen und verschiedene Operator-Normierungen. Der Spurvergleich bei festem Operator und festem Teilraum identifiziert sie nicht als zwei Rechenreihenfolgen derselben Messung. Das kleinere $\gamma_T$ erklärt sich mathematisch aus der erneuten Normierung, sobald die Spin-Auswahl vorgegeben ist. Physikalisch offen bleibt, warum T diese Auswahl und einen entsprechend neu normierten Flächenoperator haben soll.

Für den einfachen Minimalspin-Term $g(1/2)=2$ und $a(1/2)=\sqrt3/2$ ergibt die Normierung $\gamma_T=\log 2/(\pi\sqrt3)$, wie in r08/r10 angegeben. Der HC-Boost liefert dafür keinen Auswahlmechanismus. Dieser Abgleich betrifft die in r10 verwendete skalare Zählgleichung und behauptet keine Äquivalenz der vollständigen Horizontzustandsräume.

## Kann die T-Abbildung die Minimalspinmaske erzeugen?

[r07.2](v4_10_0_r07/Erkundung_Gravitation_Tachyonframe_Dualitaet.md) verwendet eine Abbildung, die das Vakuum festhält, die Keilalgebra auf sich abbildet und mit dem Boostfluss vertauscht. Damit wird die Keilalgebra als Ganzes transportiert. Eine zusätzliche Einschränkung auf Spin $1/2$ ist in dieser Abbildung nicht spezifiziert.

Auf einem als Vergleich deklarierten Ein-Punkt-Zustandsraum sei dieselbe Abbildung durch ein unitäres $U$ implementiert, das mit dem Boostgenerator $K$ im Sinne seiner Spektralprojektionen kommutiert. Nutzt man das gemeinsame lokale erste Gesetz aus r10 mit festem Flächenoperator, so ist $K$ proportional zu $A$ mit positivem Faktor. Da die Ein-Punkt-Flächen $a(j)$ streng mit $j$ wachsen, ist der Minimalspinprojektor eine Spektralprojektion von $K$. Es folgt $U P_{1/2}U^{-1}=P_{1/2}$. Auch der volle Zugangsprojektor bleibt unter Konjugation die Identität. Die Abbildung kann damit weder die bereits vorhandene Minimalspinmaske verändern noch den vollen Zugang in diese Maske umwandeln.

Die Annahme $K\propto A$ betrifft den hier deklarierten Ein-Punkt-Vergleich. Sie ist keine Identifikation der gesamten Maxwell-Keilalgebra aus r07 mit dem Horizontzählraum. Bei mehrteiligen Zuständen kann derselbe Boostwert verschiedene Spinbelegungen tragen. Dann erhält ein boostkommutierendes $U$ zwar die Boostspektralräume, aber nicht automatisch jede feinere Spinmaske. In beiden Fällen bleibt eine native Zugangsregel separat zu begründen. Die frühere [Projektorprüfung](op5_projector_spin_bridge_2026_11_06.md) behandelt einen anderen Kandidaten auf dem Dixon-Träger.

## Gesamtfläche und Minimalspin bei mehreren Durchstoßpunkten

Im additiven Vergleichsmodell mit $a(j)=\sqrt{j(j+1)}$ haben vier Punkte mit $j=1/2$ dieselbe Gesamtfläche wie ein Punkt mit $j=3$:

$$
4a(1/2)=2\sqrt3=a(3).
$$

Der erste Zustand gehört zur Maske „alle Punkte tragen Minimalspin“, der zweite nicht. Bei gemeinsamem $K\propto A$ haben beide denselben Boostwert. Auf einem Träger, der beide Belegungen zulässt, kann somit keine Funktion von Gesamtfläche oder Boostgenerator allein diese Maske erzeugen. Die Rechnung setzt die additive Fläche voraus und führt keine zusätzliche Horizont-Zulassungsbedingung ein.

Für eine bloße obere Energieschwelle genügt sogar ein Vergleich ohne Gleichstand: $a(1)=\sqrt2<2a(1/2)=\sqrt3$. Wenn die Schwelle zwei Minimalspinpunkte zulässt, lässt sie auch einen einzelnen Punkt mit $j=1$ zu. Eine Schwelle für die Gesamtenergie ist daher etwas anderes als eine Schwelle für den Spin jedes einzelnen Punkts. Der zweite Zugang würde zusätzliche aufgelöste Punktdaten benötigen.

Der exakte Gleichstand zeigt auch die Grenze des Kommutationsarguments. Auf der zweidimensionalen Vergleichsebene beider Belegungen ist $K$ ein Vielfaches der Identität. Eine unitäre Vertauschung der beiden Zustände kommutiert dort mit $K$, verändert aber die Minimalspinmaske. Damit sind aus Boostkommutation allein weder Erhaltung noch Erzeugung der feineren Maske ableitbar. Ob beide Belegungen im selben **nativen** Horizontzustandsraum zulässig sind und ob die T-Abbildung auf solchen Entartungsräumen wirkt, bleiben eigene Fragen.

## Gesamtfläche und Punktzahl genügen gemeinsam

Im additiven Vergleichsmodell zählen wir ausschließlich Punkte mit $j\ge1/2$. Sei $N$ ihre Zahl und $\mathcal A=\sum_i a(j_i)$ die Fläche in gemeinsamen dimensionslosen Einheiten. Dann ist der Überschuss

$$
X=\mathcal A-a(1/2)N=\sum_i[a(j_i)-a(1/2)]\ge0.
$$

Für $N>0$ gilt $X=0$ genau dann, wenn alle Punkte Minimalspin tragen. Jeder andere Zustand hat mindestens $X\ge a(1)-a(1/2)=\sqrt2-\sqrt3/2\approx0{,}5482$. Die Schranke wird schon durch einen $j=1$-Punkt bei sonst minimalen Spins erreicht. Bei exakt bekannter Punktzahl reicht daher eine absolute Fehlergrenze für $\mathcal A$ kleiner als die Hälfte dieser Lücke, um die beiden Fälle anhand der Mittelschwelle zu unterscheiden. Der leere Zustand ist durch $N>0$ separat ausgeschlossen.

Die früheren flächengleichen Zustände haben $N=4$ und $N=1$. Der Überschuss trennt sie, obwohl die Fläche gleich ist. In einer gemeinsamen Belegungsbasis ist die Minimalspinmaske damit eine gemeinsame Spektralprojektion von Fläche und Punktzahl. Ein Übergang, der mit beiden Spektralauflösungen kommutiert, erhält die Maske. Zur Behauptung, T sehe nur ihre Nullfaser, braucht es weiterhin eine zusätzliche Zugangsregel. Insbesondere ist zu begründen, ob und wie die Punktzahl im nativen Horizontprofil auslesbar ist.

## Thermisches Gewicht auf dem Flächenüberschuss

Ein möglicher Modellkandidat wäre, statt der Gesamtfläche den Überschuss $X=\mathcal A-a(1/2)N$ thermisch zu gewichten. Bei fester Punktzahl ändert dies die normierten Wahrscheinlichkeiten überhaupt nicht. Der Faktor $e^{\lambda a(1/2)N}$ ist für alle Belegungen desselben $N$ gemeinsam und kürzt sich. Bei variabler Punktzahl ändert er das relative Gewicht verschiedener Punktzahlen. Innerhalb eines festen $N$ bleibt die Statistik der Spins dieselbe.

Auch eine zusätzliche endliche Unterdrückung $e^{-\nu X}$ mit $\nu>0$ liefert auf einem Träger mit positiven Ausgangsgewichten keine exakte Minimalspinmaske. Jeder zugelassene Zustand mit endlichem $X>0$ behält positives Gewicht. Bei endlichem Modellträger und mindestens einem Zustand mit $X=0$ konvergiert die normierte Statistik für $\nu\to\infty$ auf die Nullfaser. Bezeichnet $W_0>0$ das gesamte ursprüngliche Gewicht auf der Nullfaser und $W_+$ das übrige Gewicht, gilt für die Wahrscheinlichkeit außerhalb der Nullfaser

$$
\Pr_\nu(X>0)\le
\frac{W_+e^{-\nu\Delta}}{W_0+W_+e^{-\nu\Delta}},
\qquad \Delta=a(1)-a(1/2).
$$

Das folgt aus $X\ge\Delta$ für alle nichtminimalen Belegungen. Die Grenze wird erreicht, wenn alle nichtminimalen Belegungen genau den Überschuss $\Delta$ tragen. Bei unendlichem Träger wäre zusätzlich die Summierbarkeit der Ausgangsgewichte oder eine andere Konvergenzkontrolle nötig.

Damit ist die lokale Restgröße $X$ zwar ein genauer Selektor über ihre Nullfaser. Eine thermische Verschiebung des Energienullpunkts bei festem $N$ erzeugt diese Auswahl aber nicht. Eine echte Auswahl erfordert eine Projektion, einen begründeten Grenzprozess oder eine andere Zugangsregel. r10 liefert durch Wechsel des Beobachterabstands keinen veränderlichen Gewichtungsparameter, da sich Energie und Unruh-Temperatur gemeinsam skalieren. Die zusätzliche Gewichtung $\nu$ ist hier ein Modellkandidat und kein Bestandteil der nativen T-Abbildung.

## Wie sich die Unterdrückung mit der Punktzahl ändert

Im Vergleichsmodell mit $N$ unabhängig gewichteten Punkten sei $R_\nu$ das Verhältnis des gesamten höheren Spingewichts zum Minimalspingewicht pro Punkt. Dann gilt exakt

$$
\Pr_\nu(\text{alle Punkte minimal})=(1+R_\nu)^{-N}.
$$

Falls $R_0$ endlich ist, folgt aus der Überschusslücke $\Delta$ die Schranke $R_\nu\le R_0e^{-\nu\Delta}$. Um die Wahrscheinlichkeit mindestens $1-\varepsilon$ zu garantieren, genügt daher

$$
R_0e^{-\nu\Delta}\le (1-\varepsilon)^{-1/N}-1.
$$

Für festes $0<\varepsilon<1$ ist die rechte Seite asymptotisch $-\log(1-\varepsilon)/N$. Der nötige Strafparameter wächst daher im Zweiniveaumodell mit einer einzigen höheren Stufe wie $(\log N)/\Delta$. Dort gilt $R_\nu=R_0e^{-\nu\Delta}$ exakt. Wenn $\nu$ fest bleibt und $R_\nu>0$, geht die Wahrscheinlichkeit einer vollständig minimalen Belegung bei $N\to\infty$ gegen null.

Mit den gewählten Modellwerten $R_0=1$, $N=100$ und $\varepsilon=0{,}01$ ergibt die Formel für $\Delta=\sqrt2-\sqrt3/2$ den Mindestwert $\nu\approx16{,}79$ im Zweiniveaumodell. Das ist keine native Horizontrechnung. Insbesondere können gemeinsame Horizontbedingungen die unabhängige Gewichtung der Punkte ändern. Der Befund zeigt, warum ein kleiner höherer Spinanteil pro Punkt nicht automatisch eine gute Minimalspinmaske für den gesamten Horizont liefert.

## Was bei korrelierten Punktbelegungen aus den Einzelwerten folgt

Sei $p$ die Wahrscheinlichkeit eines höheren Spins an jedem der $N$ Punkte, ohne Unabhängigkeit vorauszusetzen. Für die Wahrscheinlichkeit $P_{\rm alle}$ einer vollständig minimalen Belegung liefern das Einschließen jedes Einzelereignisses und die Vereinigungsabschätzung

$$
\max(0,1-Np)\le P_{\rm alle}\le1-p.
$$

Beide Grenzen sind scharf. Die obere Grenze wird erreicht, wenn mit Wahrscheinlichkeit $p$ alle Punkte gleichzeitig höheren Spin tragen und sonst alle minimal sind. Für $Np\le1$ wird die untere Grenze erreicht, wenn mit Wahrscheinlichkeit $Np$ genau ein gleichverteilt ausgewählter Punkt höheren Spin trägt und sonst keiner. Für $Np\ge1$ kann man die Zahl höherer Spins auf die beiden benachbarten ganzen Zahlen um $Np$ verteilen und bei gegebener Zahl die Punkte gleichverteilt wählen. Dann ist stets mindestens ein Punkt höher und jede Einzelwahrscheinlichkeit weiterhin $p$.

Bei den gewählten Modellwerten $N=100$ und $p=0{,}01$ reichen die möglichen Werte somit von null bis $0{,}99$. Die unabhängige Wahl liefert $0{,}99^{100}\approx0{,}366$. Alle diese Modelle haben dieselbe Einzelpunktstatistik. Ohne Annahmen über die Kopplung kann man $P_{\rm alle}\ge1-\varepsilon$ aus den Einzelwerten allein nur dann für alle gemeinsamen Verteilungen garantieren, wenn $p\le\varepsilon/N$.

Für QAM trennt dies die Einzelpunkt-Auslesung von der gemeinsamen Minimalspinmaske. Die $1/N$-Bedingung ist als Garantie auch ohne unabhängige Spins verfügbar. Sie ist keine notwendige Bedingung für eine spezielle korrelierte Präparation. Die native Horizontrechnung müsste gemeinsame Belegungsgewichte oder wenigstens eine Schranke für das Ereignis „mindestens ein höherer Spin“ liefern.

## Gemeinsame Minimalspinwahrscheinlichkeit aus Flächenmomenten

Im additiven Modell mit $N>0$ sei $\mu=\mathbb E[X]$ und $M_2=\mathbb E[X^2]<\infty$. Jeder nichtminimale Zustand hat $X\ge\Delta$. Damit folgt aus $\mu\ge\Delta\Pr(X>0)$ eine untere Schranke für die Minimalspinwahrscheinlichkeit. Umgekehrt liefert Cauchy–Schwarz auf dem Ereignis $X>0$ die Schranke $\mu^2\le M_2\Pr(X>0)$. Für $M_2>0$ ergibt sich

$$
\max(0,1-\mu/\Delta)\le P_{\rm alle}\le1-\mu^2/M_2 .
$$

Bei $M_2=0$ sind alle zugelassenen Belegungen fast sicher vollständig minimal. Beide Ungleichungen gelten ohne Unabhängigkeit. Die untere Schranke ist exakt, wenn die einzige positive Überschussstufe $\Delta$ ist und $\mu\le\Delta$. Die obere ist exakt, wenn der Überschuss bedingt auf $X>0$ konstant ist.

Bei den beiden korrelierten Beispielen mit $N=100$, höherer Einzelspinwahrscheinlichkeit $p=1/100$ und nur einer höheren Stufe mit Lücke $\Delta$ ist $\mu=\Delta$ in beiden Fällen. Wenn genau ein Punkt höher ist, gilt $M_2=\Delta^2$ und damit $P_{\rm alle}=0$. Wenn alle Punkte gemeinsam wechseln, gilt $M_2=100\Delta^2$ und die obere Schranke ist $0{,}99$, hier erreicht. Der gemeinsame Flächenmittelwert unterscheidet sie nicht. Das zweite Moment liefert eine zusätzliche Schranke, bestimmt die Wahrscheinlichkeit aber im Allgemeinen nicht allein.

Für eine Anwendung im Horizontprofil müssen $X$ und sein zweites Moment aus derselben gemeinsamen Auslesung von Fläche und Punktzahl stammen. Bei variabler Punktzahl gehören dazu auch ihre Korrelationen. Die Rechnung liefert eine mögliche Prüfung der Zugangsmaske, keinen Mechanismus, der sie erzeugt.

## Exponentielle Auslesung als Schranke für die Minimalspinmaske

Sei $W_\nu=\mathbb E[e^{-\nu X}]$ im selben Zustand und $\Delta>0$ die kleinste positive Überschussstufe. Mit $P_0=\Pr(X=0)$ und $q_\nu=e^{-\nu\Delta}<1$ gilt

$$
P_0\le W_\nu\le P_0+q_\nu(1-P_0),
\qquad
\max\left(0,\frac{W_\nu-q_\nu}{1-q_\nu}\right)\le P_0\le W_\nu .
$$

Die obere Schranke für $W_\nu$ wird erreicht, wenn die gesamte nichtminimale Wahrscheinlichkeit auf $X=\Delta$ liegt. Ist die Auslesung nur durch $W_\nu\in[W_-,W_+]$ bekannt, verwendet man $W_-$ in der unteren und $W_+$ in der oberen Schranke für $P_0$. Die deterministische Fehlergrenze zwischen Auslesung und Maskengewicht lautet $0\le W_\nu-P_0\le q_\nu$. Auf Operatorebene ist dies die Normschranke für die Differenz von $e^{-\nu X}$ und der Spektralprojektion auf null. Sie setzt einen nichtnegativen selbstadjungierten Überschussoperator mit derselben Lücke voraus.

Für $\nu\Delta=\log 100$ und eine gewählte exakte Auslesung $W_\nu=0{,}99$ folgt $98/99\le P_0\le0{,}99$. Das bestimmt die gemeinsame Minimalspinwahrscheinlichkeit ohne Einzelpunkt-Unabhängigkeit. Die Gewichtung betrifft $X$ im festgehaltenen Zustand. Sie ist weder eine thermische Neupräparation noch direkt die r10-Zählsumme für Gesamtfläche. Um sie nativ einzusetzen, müsste der Horizontzugang die gemeinsame Auslesung von Fläche und Punktzahl oder den Überschussoperator selbst liefern.

## Flächengleichstand trotz verschwindendem Gesamtspin

Ergänze das additive Vergleichsmodell um die Forderung, dass der Gesamtzustand unter gemeinsamen $SU(2)$-Drehungen invariant ist. Für zwei gleiche Spins $j$ liefert der normierte Vektor

$$
S_j=\frac{1}{\sqrt{2j+1}}\sum_{m=-j}^j(-1)^{j-m}
|j,m\rangle\otimes|j,-m\rangle
$$

ein Singulett. Der Gesamtoperator $J_z$ verschwindet termweise. Bei $J_+$ und $J_-$ heben sich benachbarte Summanden wegen gleicher Leiterkoeffizienten und entgegengesetzter Vorzeichen auf.

Vergleiche nun vier Paare in $S_{1/2}$ mit einem Paar in $S_3$. Beide Gesamtzustände sind invariant, da jedes Paar ein Singulett ist. Sie haben exakt dieselbe dimensionslose Fläche

$$
8a(1/2)=2a(3)=4\sqrt3.
$$

Der erste Zustand besteht ausschließlich aus Minimalspinpunkten. Der zweite besteht aus zwei höheren Spins. Die gemeinsame Auslesung von Gesamtfläche und Gesamtspin trennt sie daher nicht. Die Punktzahl $N$ trennt sie weiterhin, ebenso der Überschuss $X$ bei bekannter gemeinsamer Flächenkalibrierung.

Das Beispiel prüft nur die additive Flächenformel und die gewöhnliche gemeinsame $SU(2)$-Invarianz im Tensorprodukt. Es setzt variable Punktzahl voraus. Ob beide Belegungen dieselben weiteren nativen Horizontbedingungen erfüllen, bleibt separat zu prüfen. Der Schluss ist, dass eine Forderung nach verschwindendem Gesamtspin allein die frühere Mehrdeutigkeit nicht beseitigt.

## Maximale Punktzahl bei fester Fläche

Im selben additiven Modell sei $\mathcal A=A_*>0$ fest. Dann gilt $N\le A_*/a(1/2)$. Ist $A_*=m a(1/2)$ mit ganzzahligem $m$ und eine vollständig minimale Belegung mit $m$ Punkten tatsächlich zulässig, ist die maximale Punktzahl genau $m$. Ihre gesamte Faser besteht aus Minimalspinbelegungen, denn $X=A_*-ma(1/2)=0$. Umgekehrt hat jede vollständig minimale Belegung bei dieser Fläche $N=m$. In diesem Fall fallen die Maximalpunktmaske und die Minimalspinmaske zusammen.

Im Singulettvergleich bei $A_*=4\sqrt3$ sind acht Punkte zulässig und sättigen die Schranke. Der Zustand mit zwei $j=3$-Punkten hat dieselbe Fläche und denselben Gesamtspin, wird aber durch die Maximalpunktregel ausgeschlossen. Die Existenz der sättigenden Belegung ist wesentlich. Bei $A_*=a(1)=\sqrt2$ gilt $N\le1$, und die maximalpunktige Belegung hat $j=1$. Eine Maximalpunktregel erzeugt daher bei beliebiger Fläche keine Minimalspinmaske.

Bei fester Fläche ist die Maximierung von $N$ äquivalent zur Minimierung von $X$. Sie ist eine konkrete Kandidatenregel für einen zusätzlichen Horizontzugang. Die T-Abbildung und die gemeinsame Unruh-Gewichtung aus r07/r10 liefern jedoch keine Maximierung der Punktzahl. Für eine native Anwendung müsste begründet werden, warum T diese Extremalregel verwendet und wann die Fläche eine zulässige sättigende Belegung trägt.

## Singulettzahl beim Flächengleichstand

Im gewöhnlichen Tensorproduktmodell mit unterscheidbaren Punkten tragen acht Spin-$1/2$-Punkte genau $14$ unabhängige Singuletts. Die Zahl der Zustände mit magnetischer Gesamtkomponente $m=0$ ist $\binom84=70$, die mit $m=1$ ist $\binom85=56$. Jede ganzzahlige Gesamtspin-Darstellung mit Spin mindestens eins trägt je einen Zustand zu beiden Zahlen bei. Ihre Differenz zählt daher genau die Spin-null-Darstellungen. Zwei Spin-$3$-Punkte tragen genau ein Singulett, denn es gibt sieben Paare mit $m=0$ und sechs mit $m=1$.

Beide Konfigurationen haben die Fläche $4\sqrt3$. Bei gleicher Gewichtung jedes Singuletts und **Beschränkung auf diese beiden Konfigurationen** ergibt sich für die vollständig minimale Belegung $14/15$. Ein gemeinsames Boltzmanngewicht, das allein von der Gesamtfläche abhängt, kürzt sich heraus. Die größere Entartung bevorzugt die Maximalpunktbelegung in diesem Vergleich. Der Spin-$3$-Sektor behält aber positives Gewicht.

Das Verhältnis $14/15$ ist keine Aussage über die vollständige r10-Zählung. Weitere Belegungen, Projektionsbedingungen und andere Zählmaße können die Normierung ändern. Die Rechnung zeigt für das gewählte gemeinsame Maß einen Unterschied zwischen statistischer Bevorzugung und exakter T-Auswahl. Für die letztere braucht es weiterhin eine Zugangsregel.

## Vollständige Belegungsliste bei exakt dieser Fläche

Im additiven Tensorproduktmodell lässt sich die gesamte Flächenfaser bei $\mathcal A=4\sqrt3$ bestimmen. Schreibe $k=2j+1\ge2$, dann gilt $2a(j)=\sqrt{k^2-1}$. Wegen der Flächengrenze kommen nur $2\le k\le13$ vor. Schreibt man jede Wurzel als positives ganzzahliges Vielfaches einer quadratfreien Wurzel, können nur Beiträge mit quadratfreiem Teil $3$ in die Summe $2\mathcal A=8\sqrt3$ eingehen. Verschiedene quadratfreie Wurzeln sind über den Rationalen linear unabhängig. Das folgt etwa aus der Monombasis der durch die beteiligten Primzahlwurzeln erzeugten multiquadratischen Erweiterung. Weil alle Beiträge positiv sind, kann kein Koeffizient einer anderen Wurzel intern verschwinden.

Im Bereich $2\le k\le13$ haben nur $k=2,7$ den quadratfreien Teil $3$. Dies sind $j=1/2,3$ mit Flächenbeiträgen im Verhältnis $1:4$. Die Gleichung $n_{1/2}+4n_3=8$ lässt daher genau die Belegungen $(8,0)$, $(4,1)$ und $(0,2)$ zu. Der mittlere Fall besitzt kein Singulett. Vier Spin-$1/2$-Punkte können höchstens Gesamtspin $2$ tragen, während zur Kopplung an einen Spin $3$ zu Gesamtspin null ein Spin $3$ erforderlich wäre. Die mögliche Platzierungsentartung dieser Mischbelegung spielt deshalb keine Rolle.

Somit enthält die ganze exakte Flächenfaser unter der gewöhnlichen Gesamtspin-null-Bedingung im gewählten Modell $14+1=15$ Singuletts. Der Anteil $14/15$ gilt dort ohne die frühere Beschränkung auf zwei vorab ausgewählte Belegungen. Er bleibt an exakte Fläche, die additive Formel und das gewählte Tensorprodukt-Zählmaß gebunden. Ein Flächenfenster oder zusätzliche native Horizontbedingungen wären separat zu behandeln.

## Der Minimalspinanteil muss bei großer exakter Fläche nicht gegen eins gehen

Wähle eine gerade Minimalpunktzahl $N=2m$ und die exakte Fläche $A_*=N a(1/2)$. Im gewöhnlichen Tensorproduktmodell zählt die reine Belegung

$$
d_0(N)=\binom{N}{m}-\binom{N}{m+1}
=\frac{1}{m+1}\binom{N}{m}
$$

Singuletts. Ersetze in einer fest gewählten Anordnung vier Minimalspinpunkte durch einen Spin-$3$-Punkt. Wegen $a(3)=4a(1/2)$ bleibt die Fläche exakt gleich. Ein Singulett entsteht hier aus jeder Kopie von Gesamtspin $3$ unter den verbleibenden $N-4$ Minimalspinpunkten. Für $N\ge10$ ist die Zahl

$$
d_3(N-4)=\binom{N-4}{m+1}-\binom{N-4}{m+2}
=\frac{7}{m+2}\binom{N-4}{m+1}.
$$

Aus dem Quotienten der Binomialkoeffizienten folgt $d_3(N-4)/d_0(N)\to7/16$. Schon diese einzelne feste Anordnung liefert also asymptotisch einen positiven Anteil an Konkurrenten bei gleicher Fläche. Falls alle Singuletts im betrachteten Flächenraum gleich gewichtet und beide Belegungen zugelassen sind, gilt $P_{\rm minimal}\le d_0/(d_0+d_3)$ und damit $\limsup P_{\rm minimal}\le16/23\approx0{,}696$. Weitere zugelassene Belegungen oder Platzierungsentartungen können die obere Schranke nur senken.

Dies ist ein bedingter Modellbefund. Der Vergleich setzt variable Punktzahl, gewöhnliche $SU(2)$-Tensorprodukte und dasselbe Gewicht pro Singulett bei gleicher Fläche voraus. Er zeigt, dass selbst eine statistische Konzentration auf Minimalspin bei großer Fläche nicht allein aus diesen Annahmen folgt.

## Platzierungsentartung und eine mögliche Punktzahlgewichtung

Wenn Belegungen als geordnete Spinlisten gezählt werden, hat die Mischbelegung mit einem Spin-$3$-Punkt genau $N-3$ mögliche Positionen. Jede trägt dieselbe Singulettzahl $d_3(N-4)$. Die reine Minimalspinliste hat genau eine Spinreihenfolge. Unter dieser zusätzlichen Zählannahme folgt

$$
P_{\rm minimal}\le
\frac{1}{1+(N-3)d_3(N-4)/d_0(N)}
=O(1/N).
$$

Schon die eine Familie mit einem höheren Spin erzwingt dann den Grenzwert null. Werden die Positionen dagegen identifiziert, gilt dieser zusätzliche Faktor nicht. Der vorige Vergleich einer einzigen festen Mischanordnung bleibt davon getrennt.

Eine deklarierte Punktzahlgewichtung $e^{\chi N}$ bevorzugt größere $N$ bei gleicher Fläche. Die Mischbelegung hat $N-3$ Punkte und wird relativ zur reinen Belegung um $e^{-3\chi}$ gewichtet. Soll $P_{\rm minimal}\ge1-\varepsilon$ gelten, ist deshalb notwendig

$$
(N-3)\frac{d_3(N-4)}{d_0(N)}\,e^{-3\chi}
\le\frac{\varepsilon}{1-\varepsilon}.
$$

Für feste Zielgenauigkeit muss $\chi$ in diesem geordneten Modell daher mindestens wie $(\log N)/3$ wachsen, bis auf einen additiven konstanten Term. Die Bedingung berücksichtigt nur diese Konkurrenten und ist für die gesamte Flächenfaser nicht hinreichend. Der Vergleich zeigt, welche zusätzliche Zähl- und Gewichtungsinformation eine statistische Maximalpunktregel benötigt. Die r07/r10-Abbildung liefert weder eine positionsabhängige Zählkonvention noch eine solche Punktzahlgewichtung als T-Selektor.

## Mehrere Spin-3-Ersetzungen bei logarithmischer Gewichtung

Für jede feste Zahl $m$ ersetze $4m$ der $N$ Minimalspinpunkte durch $m$ Spin-$3$-Punkte. Die Fläche bleibt exakt gleich und die Punktzahl ist $N-3m$. Im geordneten Modell gibt es $\binom{N-3m}{m}$ Platzierungen. Für eine feste Platzierung zerlege das Tensorprodukt der $m$ höheren Spins in Gesamtspin-Darstellungen mit Multiplizitäten $b_J$. Dabei ist $\sum_J b_J(2J+1)=7^m$. Die Zahl der Singuletts der Mischbelegung ist $\sum_J b_J d_J(N-4m)$, wobei $d_J(n)=\binom n{n/2+J}-\binom n{n/2+J+1}$ die Multiplizität von Spin $J$ unter $n$ Minimalspinpunkten ist.

Für festes $m,J$ liefert der Quotient der Binomialkoeffizienten $d_J(N-4m)/d_0(N)\to(2J+1)/16^m$. Mit der Punktzahlgewichtung $\chi=(\log N)/3+b$ für eine feste reelle Konstante $b$ konvergiert das Gesamtgewicht dieser Familie relativ zur reinen Belegung daher zu

$$
\frac{\Lambda^m}{m!},\qquad \Lambda=\frac7{16}e^{-3b}.
$$

Für jede feste obere Ersetzungszahl kann man diese Beiträge summieren und damit den reinen Minimalspinanteil von oben begrenzen. Lässt man erst $N$ und danach die obere Ersetzungszahl wachsen, folgt $\limsup P_{\rm minimal}\le e^{-\Lambda}$. Das Argument setzt keinen Grenzwert für die vollständige Zählung voraus. Weitere Belegungen können die Schranke nur senken.

Bei $b=0$ ist die obere Schranke etwa $0{,}646$. Selbst die kritische logarithmische Gewichtung mit festem Zusatzterm erzeugt somit keinen Grenzwert eins. Für Konvergenz auf die reine Belegung muss in diesem Modell $\chi-(\log N)/3$ gegen $+\infty$ gehen. Das folgt bereits aus der Familie mit einer Ersetzung. Ob diese stärkere Gewichtung auch für alle nativen Flächenbelegungen genügt, bleibt separat zu prüfen.

## Hinreichende Gewichtung auf der gesamten additiven Flächenfaser

Im geordneten Tensorproduktmodell bei exakter Fläche $N a(1/2)$ ist die Bedingung $\chi-(\log N)/3\to+\infty$ auch hinreichend. Die Unabhängigkeit der quadratfreien Wurzeln erzwingt für jeden Punkt einen ganzzahligen Flächenbeitrag $\ell=a(j)/a(1/2)$ mit $(2j+1)^2=3\ell^2+1$. Die kleinste Alternative zu $\ell=1$ ist $\ell=4$, weil $13$ und $28$ keine Quadrate sind. Zudem gilt $2j+1\le2^\ell$ für $\ell\ge1$. Die Dimension eines Belegungstensorprodukts ist damit höchstens $2^N$.

Sei $n$ die Zahl der Minimalspinpunkte. Für $n\ge N/2$ kann man die Singulettzahl schärfer abschätzen. Die Multiplizität von Spin $J$ unter $n$ Minimalspinpunkten ist höchstens $C(2J+1)2^n n^{-3/2}$ mit einer absoluten Konstante $C$. Das folgt aus der Differenz benachbarter Binomialkoeffizienten, deren Quotientenform den Faktor $(2J+1)/(n/2+J+1)$ liefert. Die mittlere Binomialgröße ist höchstens von der Ordnung $2^n/\sqrt n$. Summiert über die Darstellungen der höheren Spins, ist die Misch-Singulettzahl daher höchstens $C'2^N N^{-3/2}$. Da die reine Singulettzahl von genau dieser Größenordnung ist, ist das Verhältnis pro geordneter Belegung nach oben durch eine Konstante beschränkt.

Setze $z=e^{-\chi}$. Eine höhere Flächenstufe $\ell$ kostet gegenüber $\ell$ Minimalspinpunkten den Faktor $z^{\ell-1}$. Für $m$ höhere Punkte gibt es höchstens $\binom Nm$ Platzierungen, nachdem ihre Flächenstufen in Reihenfolge feststehen. Über alle Stufen abgeschätzt, ist der gesamte relative Beitrag mit $n\ge N/2$ und mindestens einem höheren Punkt daher höchstens

$$
C''\left[\left(1+\frac{z^3}{1-z}\right)^N-1\right].
$$

Dieser Ausdruck verschwindet, wenn $Nz^3\to0$. Für $n<N/2$ kostet die Punktzahldifferenz mindestens $3(N-n)/4>3N/8$, da jeder höhere Punkt mindestens vier Flächeneinheiten trägt. Die Zahl geordneter positiver Ganzzahlzerlegungen von $N$ ist höchstens $2^N$. Zusammen mit der groben Dimensionsschranke bleibt dieser relative Beitrag höchstens von der Ordnung $N^{3/2}2^N z^{3N/8}$ und verschwindet ebenfalls unter derselben Bedingung.

Zusammen mit der notwendigen Bedingung aus einer Spin-3-Ersetzung folgt im deklarierten Modell die Äquivalenz

$$
P_{\rm minimal}\to1\quad\Longleftrightarrow\quad
\chi-\tfrac13\log N\to+\infty .
$$

Das Ergebnis gilt bei geradem $N$, exakter Fläche, geordneten Spinlisten, gewöhnlicher $SU(2)$-Singulettzählung und dem deklarierten Gewicht $e^{\chi N_{\rm Punkte}}$. Für den notwendigen Teil muss insbesondere die Spin-3-Mischfamilie zugelassen sein. Es leitet weder eine native Punktzahlgewichtung noch eine T-Zugangsregel her.

## Exakter Grenzwert im kritischen Bereich

Setze $\chi=(\log N)/3+b$ mit festem $b$ und $z=e^{-\chi}$. Für Belegungen mit mindestens $N/2$ Minimalspinpunkten ist das Singulettverhältnis pro Liste wie oben einheitlich beschränkt. Der relative Beitrag aller Listen, die mindestens eine höhere Flächenstufe $\ell\ge5$ enthalten, ist damit höchstens

$$
C N\frac{z^4}{1-z}
 \left(1+\frac{z^3}{1-z}\right)^{N-1}.
$$

Für die Abschätzung markiert man eine Position mit $\ell\ge5$. Ihr Gewicht wird durch die geometrische Summe ab $z^4$ beschränkt. Für alle anderen Positionen verwendet man die Summe ab $z^3$ oder einen Minimalspin. Der Ausdruck verschwindet, weil $Nz^4\to0$ und $Nz^3=e^{-3b}$ fest ist. Auch die Listen mit weniger als $N/2$ Minimalspinpunkten verschwinden durch die bereits gegebene grobe Abschätzung.

Für die verbleibenden Listen mit ausschließlich $\ell=1$ und $\ell=4$ hat die Familie mit festem $m$ Spin-$3$-Punkten das relative Grenzgewicht $\Lambda^m/m!$, $\Lambda=(7/16)e^{-3b}$. Für mindestens $N/2$ Minimalspinpunkte werden ihre Beiträge einheitlich durch $C(e^{-3b})^m/m!$ beschränkt. Diese summierbare Majorante erlaubt den Grenzübergang über alle Ersetzungszahlen. Die gesamte gewichtete Flächenfaser hat relativ zur reinen Belegung somit Grenzgewicht $e^\Lambda$. Die normierte Anzahl der Spin-$3$-Punkte konvergiert im Sinn ihrer Verteilung zu einer Poisson-verteilten Zufallszahl mit Mittel $\Lambda$. Insbesondere

$$
\lim_{N\to\infty}P_{\rm minimal}
=\exp[-(7/16)e^{-3b}].
$$

Damit ist die frühere obere Schranke im gesamten deklarierten additiven Modell scharf. Die übrigen höheren Spinarten tragen im kritischen Grenzfall asymptotisch kein Gewicht. Dies setzt dieselben geordneten Spinlisten, exakte Fläche, gerade $N$, gewöhnliche Singulettzählung und vollständige Zulassung der Modellbelegungen voraus. Native Horizontbedingungen können diese Voraussetzungen ändern.

## Gegenrechnung bei endlicher Fläche

Die [Gegenrechnung](qam_hc_area_fiber_check.py) baut geordnete Spinlisten durch Anhängen eines Punkts auf und summiert nach Fläche und doppelter magnetischer Gesamtkomponente. Die Differenz der Gewichte bei magnetischer Gesamtkomponente null und eins ergibt die gewichtete Singulettzahl. Dabei wird für jede Flächeneinheit ein gemeinsamer Faktor $1/2$ und für die Punktzahldifferenz die deklarierte Strafe angesetzt. Der erste Faktor kürzt sich bei fester Fläche. Die Rechnung verwendet Gleitkomma für die Gewichte und überprüft den analytischen Grenzwert numerisch. Sie verwendet keine Entwicklung nach der Anzahl der Spin-3-Ersetzungen.

| $N$ | Minimalspinanteil bei $b=0$ |
|---:|---:|
| 8 | 0,998885173 |
| 32 | 0,806904830 |
| 64 | 0,734695452 |
| 128 | 0,692603255 |
| 256 | 0,669792565 |
| Grenzwert | 0,645648526 |

Der Wert für $N=8$ enthält bereits die kritische Punktzahlgewichtung und ist daher von der früheren Gleichgewichtung $14/15$ zu unterscheiden. Die Gegenrechnung ist ein nachträglicher Modellabgleich und keine native Horizontzählung.

## Was eine native Punktzahlgewichtung ändern müsste

Im endlichen Vergleichsmodell seien $A$ und $N_{\rm Punkte}$ gemeinsam diagonal. Die Gewichte $e^{-\lambda A+\chi N_{\rm Punkte}}$ entsprechen einem dimensionslosen Generator $K_\chi=\lambda A-\chi N_{\rm Punkte}$. In einer festen Flächenfaser und für zwei normierte Mikrozustände mit Punktzahlen $N_x,N_y$ ist ihr Gewichtsverhältnis

$$
\frac{p_y}{p_x}=e^{\chi(N_y-N_x)}.
$$

Damit lässt sich der gesuchte Term von einer reinen Normierung des ursprünglichen Flächengenerators unterscheiden. Für einen Übergang $|y\rangle\langle x|$ zwischen diesen gleichflächigen Zuständen erzeugt $K_0=\lambda A$ keine relative Phase. Dagegen liefert $K_\chi$ im Fluss $O(t)=e^{itK_\chi}Oe^{-itK_\chi}$ die Phase $e^{-it\chi(N_y-N_x)}$. Eine Skalierung von $K_0$ kann diesen Unterschied nicht erzeugen, denn seine Eigenwerte sind auf beiden Zuständen gleich.

Wenn die zugänglichen Observablen ausschließlich innerhalb fester Punktzahlsektoren wirken, fällt der zusätzliche Term aus ihrem Fluss heraus. Dann legt dieser Fluss die relativen Gewichte zwischen den Punktzahlsektoren nicht fest. Das Gewicht müsste durch die Präparation, eine Randbedingung oder einen anderen Mechanismus begründet werden. Sind Übergänge zwischen verschiedenen Punktzahlen zugänglich, wäre deren relative Phase ein unabhängiger Prüfpunkt für den zusätzlichen Generator.

Beim flächengleichen Spin-3-Ersatz ist die Punktzahldifferenz $-3$. Für einzelne Mikrozustände beträgt das Verhältnis an der kritischen Schwelle $e^{-3b}/N$. Die zuvor gezählten Platzierungen und Singuletts wirken erst beim Übergang von einzelnen Gewichten zum Gesamtanteil. Die gewöhnliche gemeinsame Unruh-Normierung aus [r10](v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md) liefert keinen solchen Unterschied bei gleicher Fläche. Diese Rechnung beschreibt die Beweispflicht im deklarierten endlichen Modell, ohne einen nativen Punktzahloperator oder einen neuen T-Generator anzunehmen.

## OP1 rückwärts: Ausschlusskorridor für einen T-Flächenoperator

Analytische Erkundung ohne neue H-Nummer. Zielwert aus r10, nicht unabhängig gemessen: $r_A=a_T/a_M=1/1{,}8647\approx0{,}53628$. Die zulässigen Änderungen werden vorwärts aus ihrem Typ begrenzt. In der geprüften Kette r07/r10/r11 ist der Boost beziehungsweise die Dualität der Maxwell-Keilalgebra beschrieben. Ein daraus konstruierter quantisierter T-Flächenoperator fehlt. r10.3 gibt die gewünschte Normierung an und r11 benennt die fehlende Abbildung ausdrücklich.

| Mechanismus | Erreichbarer Bereich für $r_A$ unter seinen Voraussetzungen |
|---|---|
| Unitärer Wechsel desselben Operators | Genau $1$ |
| Auswahl vorhandener Flächenstufen | Mindestens $1$, falls eine positive Stufe verbleibt |
| Kompression ausschließlich auf Zustände oberhalb der M-Flächenlücke | Mindestens $1$ |
| Änderung auf gemeinsamem positiven Sektor mit relativer Formschranke $\varepsilon<1$ | $[1-\varepsilon,1+\varepsilon]$ |
| Kompression mit Zugang zum Nullsektor | Werte unter $1$ möglich, mit quantitativer Bedingung unten |

Für die Formschranke identifiziere zunächst die Träger und den gemeinsamen Nullraum. Auf dessen Orthogonalkomplement gelte $(1-\varepsilon)A_M\le A_T\le(1+\varepsilon)A_M$ auf einer gemeinsamen Formdomäne. Infima der normierten Erwartungswerte geben den angegebenen Korridor für die unteren positiven Spektralgrenzen. Die Aussage verwendet positive Lücken auf diesem Sektor. Eine Verschiebung des Nullraums ist ein anderer Fall. Um den nominalen Zielwert zu erreichen, muss $\varepsilon\ge1-1/G\approx0{,}46372$ sein. Jede nachgewiesen kleinere relative Änderung ist damit ausgeschlossen.

Für einen normierten Eigenzustand $\psi$ einer Kompression mit effektiver Fläche $a_M/G$ gilt aufgrund der M-Lücke $A_M\ge a_M(I-P_0)$, wobei $P_0$ die ursprüngliche Nullprojektion ist. Damit

$$
\|P_0\psi\|^2\ge1-1/G\approx0{,}46372.
$$

Die Schranke ist scharf im Zweiniveaumodell. Ein Kompressionskandidat braucht also mindestens rund 46 Prozent Überlappungsgewicht mit der ursprünglichen Nullfläche. Falls diese im T-Horizontprofil als Ausgangsdaten ausgeschlossen sind, fällt der gesamte Kompressionsweg weg. Sind sie zugänglich, müsste eine native Map diese Mischung und die geänderte Messung unabhängig von $G$ herleiten. Der Vergleich betrifft genau den kleinsten positiven Ausgang und setzt nicht voraus, dass das volle Spektrum skaliert.

Dieser Korridor ist kein universelles Intervall für beliebige T-Operatoren. Er schließt Kandidaten nach ihren unabhängig belegten Eigenschaften aus. Die nächste überprüfbare Quellenaussage wäre daher eine explizite native Ausleseabbildung mit Angabe, ob sie den Nullraum erhält und welchen relativen Formunterschied sie zulässt. Die Spektralschranken ersetzen keine physikalische Identifikation des T-Profils.

## Operator zuerst: die unveränderte Geometrie als konkrete Referenz

Im transversalen Durchstoßpunktmodell von r10 sei $F_p^i$ der **gravitatorische** Fluss durch ein kleines Flächenstück am Punkt $p$. Mit dimensionslosen Spinoperatoren $J_p^i$ und der gemeinsamen Planck-Flächeneinheit ist $\widehat F_{M,p}^i=8\pi\gamma_M\ell_P^2 J_p^i$. Der M-Operator für den festgehaltenen Schnitt $S$ ist

$$
\widehat A_M(S)=8\pi\gamma_M\ell_P^2\sum_{p\in S}
 \sqrt{\sum_i(J_p^i)^2}.
$$

Auf einer Spinbelegung liefert das den in r10 verwendeten Eigenwert $8\pi\gamma_M\ell_P^2\sum_p\sqrt{j_p(j_p+1)}$. Der Anwendungsbereich ist das additive Durchstoßpunktmodell, nicht die allgemeine Flächenformel für beliebige Knoten auf einer Fläche. Quellen: [Ashtekar–Lewandowski](https://arxiv.org/abs/gr-qc/9602046), [Isolated Horizons](https://arxiv.org/abs/gr-qc/0005126) und [r10](v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md).

Die vorhandene T-Abbildung aus r07 wirkt auf elektromagnetischem $E+iB$. Sie gibt keine Abbildung der gravitativen Flüsse $F_p^i$, der Durchstoßpunkte oder ihrer Spinoperatoren an. Eine konkrete Referenzdefinition auf einem gewählten Produktträger ist daher $D_T=D_{\rm Maxwell}\otimes I_{\rm Geometrie}$ und $\widehat A_T^{(0)}=I\otimes\widehat A_M(S)$. Sie realisiert unveränderte Geometrie als explizite zusätzliche Modellwahl. Sie liefert auf demselben Durchstoßpunktträger $a_{\min,T}^{(0)}=a_{\min,M}=4\pi\sqrt3\,\gamma_M\ell_P^2$, vor jeder neuen Zählung. Auch eine orthogonale Rotation der drei Flusskomponenten erhält die Quadratsumme.

Eine scheinbar einfache alternative Definition wäre $J^i\mapsto\lambda J^i$. Sie erhält jedoch bei unveränderter normierter Spin-Algebra $[J^i,J^j]=i\epsilon^{ijk}J^k$ die Kommutatoren nur bei $\lambda=1$ oder bei der trivialen Nullabbildung $\lambda=0$. Denn der Kommutator skaliert quadratisch, die rechte Seite linear. Das schließt eine nichttriviale gleichförmige Reskalierung **der normierten Generatoren als Automorphismus** aus. Eine andere Flussnormalisierung, andere Quantisierungsdaten oder eine andere Observable sind dadurch nicht ausgeschlossen. Sie müssen als eigene Definition hergeleitet werden. Die erste fehlende native Schnittstelle ist somit die Wirkung von T auf den gravitativen Fluss und seine Quantisierung, vor der Wurzelbildung und vor der Horizontzählung.

## Gravitativer Fluss vor der Quantisierung

Der geometrische Fluss stammt im betrachteten klassischen Vergleich aus dem räumlichen Coframe $e^i$. Auf einer orientierten Fläche ist seine interne Zweiform $\Sigma^i=\tfrac12\epsilon^i{}_{jk}e^j\wedge e^k$. Auf einem kleinen Flächenstück ergibt ihre Norm die lokale Fläche. Eine interne Rotation der Coframes rotiert $\Sigma^i$ und erhält seine Norm. Die einfache Skalierung $e_T^i=\sqrt\lambda\,e_M^i$ würde $\Sigma_T=\lambda\Sigma_M$ liefern, aber zugleich die induzierte Metrik $q_T=\lambda q_M$ und die klassische Fläche desselben Schnitts um $\lambda$ ändern. Der r10-Ansatz hält diese klassische Fläche in gemeinsamen Einheiten fest. Er schließt diese gleichförmige geometrische Reskalierung für $\lambda\ne1$ aus.

Eine Änderung der Koordinaten auf dem Phasenraum ist ein weiterer, getrennter Fall. In einem lokalen kanonischen Vergleichspaar mit $\{Q,P\}=1$ erhält $Q'=Q/\lambda$, $P'=\lambda P$ die Poisson-Klammer. Wenn die physikalische Flächenauslesung als Funktion von $P$ feststeht, muss sie nach dem Koordinatenwechsel als dieselbe Funktion von $P'/\lambda$ ausgewertet werden. Wer stattdessen direkt $P'$ als Fluss definiert, hat die physikalische Auslesung geändert. Dieses kanonische Paar illustriert die Unterscheidung und ersetzt keine Rechnung mit der nativen Holonomie-Fluss-Algebra.

In der geprüften r07/r10-Kette ist weder eine T-Abbildung auf dem gravitativen Coframe noch ein zugehöriger Horizont-Randterm angegeben, der die Quantisierung bei gleicher klassischer Fläche ändern würde. Ein konkreter nächster Ansatz müsste den T-Randterm oder die T-Symplektik aus einer vorhandenen Dynamik gewinnen und daraus die Flussdarstellung bestimmen. Der gewünschte BI-Wert darf dabei nicht als Normierungsparameter vorweg eingesetzt werden.

## Prüfung des vorhandenen Palatini-Terms und reiner Randableitungen

Die [Gravitationsschicht r01](../../sources/research/parts/v4100-post-release-layers.tex) untersucht die Wirkung und die Verbindungsgleichung. Die [ausgeschriebene Palatini-Vergleichswirkung](../../analysis/HC_Cross_Cartan_Parent.md) verwendet gewöhnliche Palatini-Krümmung ohne Holst-Term. In den geprüften r01/r07/r10-Quellen ist daraus kein eigener quantisierter T-Horizontsektor angegeben. Das folgende Variationsargument prüft den gewöhnlichen Palatini-Term als Kandidaten und benötigt keine Wiederaufnahme der eingefrorenen W1/W2-Dynamik.

Schreibe den gravitativen Term als $L=c\,\Sigma_{IJ}\wedge F^{IJ}(\omega)$ mit $\Sigma_{IJ}=\tfrac12\epsilon_{IJKL}e^K\wedge e^L$. Variation von $F$ ergibt $D_\omega\delta\omega$. Durch partielle Integration erhält man als Randpotential $\theta=c\,\Sigma_{IJ}\wedge\delta\omega^{IJ}$. Der zugehörige symplektische Strom für zwei kommutierende Variationen enthält daher

$$
\omega_{\rm symp}(\delta_1,\delta_2)
=c\bigl(\delta_1\Sigma_{IJ}\wedge\delta_2\omega^{IJ}
       -\delta_2\Sigma_{IJ}\wedge\delta_1\omega^{IJ}\bigr).
$$

Lässt die elektromagnetische T-Abbildung $e,\omega$ und deren Randbedingungen fest, bleibt dieser Strom unverändert. Auch die bloße Ergänzung einer lokal definierten totalen Ableitung $L\mapsto L+dB$ verschiebt das Potential nur um $\delta B$. Ihr Beitrag zum antisymmetrisierten Strom verschwindet, weil $\delta_1\delta_2 B=\delta_2\delta_1 B$. Diese Rechnung setzt denselben Variationsraum und dieselbe Wahl von Eckendaten voraus. Andere Randbedingungen, eigenständige Randfreiheitsgrade, eine Änderung der Eckenterme oder globale Quantisierungseffekte sind dadurch nicht geprüft.

Damit fällt im gemeinsamen lokalen Setup sowohl der unveränderte Palatini-Term als auch eine reine totale Ableitung als Ursprung eines neuen symplektischen T-Faktors weg. Eine tragende Alternative müsste eine tatsächlich geänderte Horizont-Symplektik oder einen anderen Randzustandsraum herleiten. Der Ausdruck für den Strom benennt, an welcher Stelle die Änderung sichtbar werden müsste.

## Ein Randmodell mit gleicher klassischer Fläche und anderer Flächenstufe

Wähle als Vergleich einen kompakten Randwinkel $\theta$ mit Periode $2\pi$ und einen reellen orientierten Fluss $P$. Halte in beiden Profilen dieselbe klassische Flächenauslesung $A=|P|$ fest. Die gewählte Randwirkung enthält den Term $kP\dot\theta$ mit $k>0$. Seine symplektische Form ist $k\,dP\wedge d\theta$. Der zu $\theta$ konjugierte Impuls ist daher $p_\theta=kP$. In der gewählten Quantisierung mit periodischen Wellenfunktionen gilt

$$
\widehat p_\theta=-i\hbar\partial_\theta,\qquad
\widehat A^{(k)}=\frac{|\widehat p_\theta|}{k},\qquad
a_{\min}^{(k)}=\frac{\hbar}{k}.
$$

Die Fouriermoden $e^{im\theta}$ mit ganzzahligem $m$ liefern das Spektrum direkt. Für zwei Profile mit derselben klassischen Flächenauslesung und derselben Winkelperiode folgt $a_{\min,T}/a_{\min,M}=k_M/k_T$. Hier könnte der gewünschte Wert aus einem **vorab hergeleiteten** Verhältnis der symplektischen Koeffizienten folgen. Die Definition des Operators setzt weder einen Spin noch ein Zählgewicht ein.

Die Festlegung, dass $P$ in beiden Profilen derselbe geometrische Fluss ist und $\theta$ dieselbe Periode hat, ist wesentlich. Eine bloße Umbenennung von $p_\theta$ oder ein Koordinatenwechsel mit mittransformierter Flächenauslesung ergibt diese Änderung nicht. Auch die periodische Randbedingung ist eine Wahl. Das Beispiel ist ein kanonisches Randmodell und keine Herleitung einer isolierten Horizontquantisierung. Es berechnet eine andere Stufe aus einer geänderten Rand-Symplektik, liefert jedoch keinen nativen Wert für $k_T/k_M$ und keine Identifikation seiner Moden mit den Spinbeiträgen aus r10.

Der nächste native Anschluss wäre ein Randterm, der bei festgehaltener Fläche und derselben normierten kompakten Randkoordinate einen Koeffizienten in der Rolle von $k$ liefert. Aus dem HC-Uhrfaktor allein folgt $k_T/k_M=G$ nicht.

## Was eine Umnormierung oder Überlagerung des Randwinkels leisten kann

Für eine Winkelkoordinate $\theta$ mit Periode $L$ und Randterm $kP\dot\theta$ liefert dieselbe periodische Quantisierung $a_{\min}=2\pi\hbar/(kL)$. Ein Koordinatenwechsel $\theta'=c\theta$ mit $c>0$ ändert $L$ zu $cL$ und $k$ zu $k/c$. Das Produkt $kL$ und die Flächenstufe bleiben gleich. Ein Faktor in der Winkelkoordinate allein reicht also nicht.

Prüfe als anderen Kandidaten eine Überlagerung $\theta_M=d\theta_T\bmod 2\pi$ bei beiden Perioden $2\pi$. Eine stetige gleichförmige Abbildung dieser Form ist nur für ganzzahliges $d$ wohldefiniert. Für $d>0$ und festgehaltenen geometrischen Fluss $P$ zieht sie den Randterm auf $d k_M P\dot\theta_T$ zurück. Quantisiert man auf dem **vollen** T-Kreis mit allen periodischen Wellenfunktionen, ist die kleinste Stufe daher $a_M/d$. Der nominale Zielwert $1/1{,}8647$ entspricht keinem solchen ganzzahligen Überlagerungsgrad.

Nutzt man auf dem T-Kreis dagegen nur die aus M zurückgezogenen Zustände, sind die Fouriermoden $e^{idm\theta_T}$. Ihre Impulse sind Vielfache von $d\hbar$. Der Faktor $d$ kürzt sich in der Flächenauslesung wieder heraus, und die kleinste positive Fläche bleibt $a_M$. Eine feinere Stufe aus diesem Modell erfordert also tatsächlich zusätzliche Randzustände. Der Nachweis betrifft periodische Quantisierung und gleichförmige Kreisüberlagerungen bei unverändertem $P$. Er ist kein Ausschluss anderer symplektischer Randstrukturen.

## Randphase bei unveränderter Symplektik

Lasse den Randwinkel, seine Periode $2\pi$, den Koeffizienten $k$ und die klassische Flächenauslesung $|P|$ unverändert. Erlaube für T stattdessen die Randbedingung $\psi(\theta+2\pi)=e^{2\pi i\alpha}\psi(\theta)$ mit $0\le\alpha<1$. Die Eigenfunktionen des Winkelimpulses sind dann $e^{i(m+\alpha)\theta}$, $m\in\mathbb Z$. Bezogen auf die periodische M-Stufe $a_M=\hbar/k$ gilt für die kleinste positive T-Fläche

$$
\frac{a_T}{a_M}=
\begin{cases}
1,&\alpha=0,\\
\min(\alpha,1-\alpha),&0<\alpha<1.
\end{cases}
$$

Damit sind bei vollständigem orientierten Impulsspektrum und anschließender Betragsbildung nur die Verhältnisse in $(0,1/2]\cup\{1\}$ erreichbar. Der nominale Zielwert $0{,}536279\ldots$ liegt dazwischen und ist durch eine Randphase allein ausgeschlossen. Bei jeder nichttrivialen Randphase entfällt zudem der ursprüngliche Nullwert. Soll der T-Operator denselben Nullsektor behalten, bleibt in diesem Modell nur $\alpha=0$.

Eine Einschränkung auf nur positive orientierte Impulse würde den Zweig mit dem anderen Vorzeichen entfernen und könnte andere Verhältnisse liefern. Das wäre eine zusätzliche Zugangsregel. Auch eine gleichzeitige Änderung von $k$ fällt außerhalb dieses Ausschlusses. Die Rechnung prüft eine konkrete alternative Quantisierung des Vergleichsmodells und identifiziert keine native Horizont-Randphase.

## Flussumkehr und Randphase

Prüfe die kanonische Flussumkehr $(\theta,P)\mapsto(-\theta,-P)$ des Winkelmodells bei gleichem $k$. Sie erhält $k\,dP\wedge d\theta$ und die geometrische Auslesung $|P|$. Ihre Wirkung auf Wellenfunktionen ist $R\psi(\theta)=\psi(-\theta)$. Für eine Randphase $\alpha$ folgt

$$
(R\psi)(\theta+2\pi)=e^{-2\pi i\alpha}(R\psi)(\theta).
$$

Die Flussumkehr bildet daher den Sektor $\alpha$ auf $-\alpha$ modulo eins ab. Innerhalb eines einzigen Sektors ist sie nur für $\alpha=0$ oder $\alpha=1/2$ implementierbar. Im ersten Fall bleibt die Nullstufe erhalten, im zweiten Fall ist die kleinste Fläche $a_M/2$ und die Nullstufe fehlt. Bei zwei gepaarten Phasen $\alpha$ und $1-\alpha$ vertauscht die Flussumkehr die Impulsspektren bis auf ihr Vorzeichen. Die Betragsflächen sind gleich. Beginnt M periodisch, ist unter dieser Abbildung auch T periodisch.

Die Flussumkehr kann somit keinen kleineren Flächenwert **zwischen zwei durch sie verbundenen Profilen** erzeugen. Eine bewusst anders gewählte T-Randphase wäre keine Folge dieser Abbildung. Der Befund gilt im Winkelmodell bei gleicher Symplektik und gleicher Winkelperiode. Insbesondere ist die Identifikation der HC-Operation mit einer Umkehr des gravitativen Randflusses weiterhin eine Kandidatenannahme.

## Beliebiger flächenerhaltender kanonischer Wechsel auf dem Randzylinder

Betrachte zwei Randzylinder mit Periode $2\pi$, $\Omega_M=k_M\,dP\wedge d\theta$ und $\Omega_T=k_T\,dP_T\wedge d\theta_T$, wobei beide Koeffizienten positiv sind. Ein glatter invertierbarer Profilwechsel soll $|P_T|=|P|$ erhalten und $\Omega_T$ auf $\Omega_M$ zurückziehen. Auf jeder zusammenhängenden Komponente mit $P\ne0$ gilt dann $P_T=\epsilon P$ mit festem $\epsilon=\pm1$. Deshalb verlangt die Symplektik

$$
k_T\epsilon\,\partial_\theta\theta_T=k_M.
$$

Für jedes feste $P$ bildet der Profilwechsel den Winkelkreis invertierbar auf einen Winkelkreis ab. Dessen Grad ist $+1$ oder $-1$. Integration der Ableitung über den Kreis ergibt folglich $k_M/k_T=1$ und Grad $\epsilon$. Die Abbildung hat auf dieser Komponente die Form $\theta_T=\epsilon\theta+\phi(P)$ modulo $2\pi$. Die flussabhängige Verschiebung $\phi(P)$ erweitert den Raum der möglichen Abbildungen, ändert den Koeffizienten aber nicht.

Damit ist im Randzylindermodell jede glatte invertierbare kanonische Abbildung ausgeschlossen, die dieselbe klassische Fläche und die Kreisstruktur bewahrt und zugleich $k_T\ne k_M$ erzeugt. Bei periodischer Quantisierung bleibt die Stufe gleich. Eine nichtinvertierbare Überlagerung, eine Änderung der Quantisierungsrandphase oder zusätzliche Randfreiheitsgrade liegen außerhalb der Voraussetzungen. Das Resultat betrifft den eindimensionalen Winkel-Fluss-Träger, nicht die vollständige gravitative Horizontphase.

## Zwei Randkanäle und eine unveränderte Gesamtfläche

Betrachte zwei Winkel-Fluss-Paare $(\theta_1,P_1)$ und $(\theta_2,P_2)$ mit gleicher Symplektiknormierung $k$ pro Paar. Die gewählte klassische Flächenauslesung sei $|P_1|+|P_2|$. Wähle eine reduzierte Randfläche durch

$$
P_1=wP,\quad P_2=(1-w)P,\quad
\theta_1=d_1\theta,\quad\theta_2=d_2\theta
\quad(0\le w\le1).
$$

Für ganzzahlige Windungen $d_1,d_2$ ist die Winkelabbildung auf dem Torus wohldefiniert. Die Flächenauslesung bleibt $|P|$. Die zurückgezogene Symplektik ist dagegen $k_{\rm eff}\,dP\wedge d\theta$ mit

$$
k_{\rm eff}=k[wd_1+(1-w)d_2].
$$

Bei gleicher Windung $d_1=d_2=1$ ändert die Flussaufteilung den Koeffizienten überhaupt nicht. Bei $(d_1,d_2)=(2,1)$ ist die Winkelkurve injektiv und $k_{\rm eff}/k=1+w\in[1,2]$. Quantisiert man die reduzierte Fläche anschließend mit periodischer Winkelwellenfunktion, liegt der Flächenquotient $a_T/a_M$ folglich im Korridor $[1/2,1]$. Der nominale r10-Wert liegt darin. Um ihn genau zu treffen, müsste ein unabhängiges Gesetz $w=G-1\approx0{,}8647$ liefern.

Das Modell benutzt eine reduzierte zweidimensionale Randfläche im erweiterten vierdimensionalen Träger. Es ist kein invertierbarer Koordinatenwechsel des alten Zylinders. Die Wahl des relativen Winkellaufs und der Flussaufteilung sind neue Eingaben. Die Rechnung setzt außerdem „zuerst reduzieren, dann quantisieren“ voraus. Eine Projektion auf bereits quantisierte Zweikanalzustände kann andere Stufen ergeben und ist separat zu prüfen. Der Befund zeigt einen überlebenden Korridor für einen konkreten Mechanismus, ohne daraus einen nativen BI-Wert abzuleiten.

## Zweikanalmodell in umgekehrter Quantisierungsreihenfolge

Bei unabhängiger periodischer Quantisierung der beiden Kreise sind die Flüsse $P_i=a_M m_i$ mit $m_i\in\mathbb Z$ und $a_M=\hbar/k$. Fordert man danach die Flussaufteilung exakt als Spektralbedingung, gilt $(1-w)m_1=w m_2$. Für irrationales $w$ ist nur $(m_1,m_2)=(0,0)$ möglich. Für $w=p/q$ in gekürzter Form mit $0\le p\le q$ lauten alle Lösungen $(m_1,m_2)=(p t,(q-p)t)$ mit $t\in\mathbb Z$. Die ursprüngliche gemeinsame Flächenauslesung $|P_1|+|P_2|$ hat dann kleinste positive Stufe $q a_M$. Sie ist niemals kleiner als $a_M$. Liest man $w=0{,}8647$ als exakt gewählten Dezimalbruch, ist $q=10000$. Dies ist keine Aussage über die Rationalität des physikalischen Zielwerts.

Die Winkelbedingung $\theta_1=2\theta_2$ und die Flussbedingung sind zudem keine zwei gleichzeitig kommutierenden Bedingungen. Im lokalen Winkelchart haben $C_\theta=\theta_1-2\theta_2$ und $C_P=(1-w)P_1-wP_2$ bei $\{\theta_i,P_j\}=\delta_{ij}/k$ die Poisson-Klammer $(1+w)/k\ne0$. Sie bilden ein Paar von Nebenbedingungen zweiter Klasse. Auf ihrer gemeinsamen klassischen Fläche erhält man die reduzierte Symplektik aus dem vorigen Abschnitt. Im unabhängig quantisierten Zweikanalraum darf man die zweite Bedingung daher nicht still als weitere kommutierende Spektralprojektion behandeln.

Damit scheidet die Verkleinerung für „zuerst getrennt quantisieren, danach nur die exakte Flussaufteilung auswählen“ aus. „Zuerst die gekoppelte Randfläche reduzieren, dann quantisieren“ liefert dagegen den berechneten Korridor $[1/2,1]$. Eine native Anwendung müsste diese gekoppelte Randstruktur vor der Quantisierung herleiten oder eine eigenständige Quantisierung der beiden Nebenbedingungen angeben. Die Rechnung behauptet keine allgemeine Inäquivalenz beliebiger Quantisierungen mit Nebenbedingungen.

## Variationsregel für die Flussaufteilung

Prüfe als Kandidaten bei festem Gesamtfluss $P_1+P_2=P$ die Randenergie

$$
H_{\rm Rand}=\tfrac12 c_1P_1^2+\tfrac12 c_2P_2^2,\qquad c_1,c_2>0.
$$

Strikte Konvexität liefert einen eindeutigen Minimierer. Die Stationarität entlang der zulässigen Variation $(\delta P_1,\delta P_2)=(u,-u)$ ergibt $c_1P_1=c_2P_2$ und damit $w=c_2/(c_1+c_2)$. Beide Flüsse haben am Minimum dasselbe Vorzeichen wie $P$, sodass die gewählte klassische Flächenauslesung $|P_1|+|P_2|=|P|$ erhalten bleibt. Diese Energieregel bestimmt die Aufteilung unter einer separat deklarierten Winkelbindung $(d_1,d_2)=(2,1)$. Sie leitet die Winkelbindung nicht her.

Bei gleichen Steifigkeiten ist $w=1/2$. Die reduzierte Quantisierung liefert dann $k_{\rm eff}/k=3/2$ und $a_T/a_M=2/3$. Damit ist die symmetrische quadratische Aufteilung für den nominalen r10-Zielwert ausgeschlossen. Allgemein verlangt $k_{\rm eff}/k=G$ mit $1<G<2$ die unabhängige Vorhersage

$$
\frac{c_2}{c_1}=\frac{G-1}{2-G}.
$$

Für $G=1{,}8647$ beträgt dieses Verhältnis ungefähr $6{,}391$. Ein Einsetzen dieses Verhältnisses nach Kenntnis des Zielwerts wäre eine Anpassung. Der Variationskandidat macht daher zwei getrennte Nachweispflichten sichtbar: die primitive Winkelbindung und eine begründete Asymmetrie der Randantwort. Die Randenergie ist hier eine gewählte Modellannahme und keine aus der T-Dynamik abgeleitete Wirkung.

## Dynamische Winkelbindung statt statischer Flussaufteilung

Ergänze im ungekürzten Zweikanalmodell die gewählte Randenergie um $V(\theta_1-2\theta_2)$ mit einem stationären Minimum bei Winkelabweichung null. An diesem Minimum gilt $\dot P_1=\dot P_2=0$. Die Hamilton-Gleichungen für die Winkel sind $\dot\theta_i=c_iP_i/k$. Damit bleibt $\theta_1-2\theta_2=0$ nur auf der Teilfläche $c_1P_1=2c_2P_2$ erhalten. Die frühere Minimierung bei festem $P_1+P_2$ liefert dagegen $c_1P_1=c_2P_2$. Für nichtverschwindenden Fluss ist ihr Ergebnis ohne Zwangskraft also kein stationär gekoppelter Winkelverlauf.

Die tatsächlich erhaltene Impulskombination in diesem Modell ist $J=2P_1+P_2$. Sie gehört zur Symmetrie $(\theta_1,\theta_2)\mapsto(\theta_1+2t,\theta_2+t)$. Minimiert man die quadratische Energie bei festem $J$, erhält man genau die dynamisch verträgliche Bedingung $c_1P_1=2c_2P_2$. Auf dieser invarianten klassischen Teilfläche gilt

$$
w=\frac{2c_2}{c_1+2c_2},\qquad k_{\rm eff}/k=1+w.
$$

Bei gleichen Steifigkeiten ist $w=2/3$ und die nach Reduktion quantisierte Flächenstufe beträgt $a_T/a_M=3/5$. Für den nominalen r10-Zielwert müsste $c_2/c_1=(G-1)/(2(2-G))\approx3{,}1955$ aus der Randdynamik folgen. Das ist eine andere Bedingung als bei der statischen Minimierung. Die Randenergie und der winkelfixierende Potentialterm sind gewählte Vergleichsdaten. Die Quantisierung der vollen Dynamik mit Fluktuationen quer zur invarianten Teilfläche bleibt getrennt.

## Volle Quantisierung der gekoppelten Winkel

8. November 2026. Auf dem vollen Torus mit periodischen Wellenfunktionen setze $\phi=\theta_1-2\theta_2$, $\theta=\theta_2$. Der ganzzahlige Koordinatenwechsel ist invertierbar. Die Fouriermoden lauten $e^{i(m\phi+n\theta)}$ mit $m=m_1$, $n=2m_1+m_2$ und $a_M=\hbar/k$. Im Sektor mit festem $n$ ist die Hamiltonfunktion nach Quantisierung

$$
\widehat H_n=\frac{a_M^2}{2}\left[c_1\widehat m^2+
c_2(n-2\widehat m)^2\right]+V(\phi),\qquad \widehat m=-i\partial_\phi.
$$

Das Winkelpotential koppelt verschiedene $m$ bei gleichem $n$. Die ursprüngliche Flächenauslesung bleibt in dieser Basis diagonal mit Ausgängen $a_M(|m|+|n-2m|)$. Ihre Ausgänge sind ganzzahlige Vielfache von $a_M$, unabhängig von der Stärke der Winkelbindung. Für $n\ne0$ ist null ausgeschlossen und jeder Ausgang ist mindestens $a_M\lceil |n|/2\rceil$, weil $|n|\le2(|m|+|n-2m|)$. Die Untergrenze wird durch ganzzahlige Aufteilung mit gleichem Vorzeichen erreicht. Insbesondere kann auch der niedrigste Energiezustand im Sektor $n=1$ im Mittel keine ursprüngliche Fläche unter $a_M$ haben.

Demgegenüber setzt die klassische Reduktion bei gleichen Steifigkeiten $m=2n/5$ als kontinuierlichen Flusswert ein und quantisiert anschließend nur den gemeinsamen Winkel. Sie ergibt im ersten positiven Sektor $3a_M/5$. Dieser Wert ist weder ein scharfer Ausgang noch ein möglicher Mittelwert der ursprünglichen Flächenmessung bei $n=1$. Eine niedrige Energie der relativen Winkelmode oder ein starkes Bindungspotential ändert diese Schranke nicht. Ein solcher reduzierter Flächenoperator braucht damit eine eigene physikalische Auslesevorschrift. Die Rechnung prüft das gewählte periodische Torusmodell und lässt andere Quantisierungen oder andere Observablen offen.

## Gemischte QAM-Auslesung des erhaltenen Randflusses

Erkundung. Im selben Torusmodell seien die beiden orientierten Flüsse die Komponentenauslesungen. Der Selektor lässt das Paar im gemeinsamen Randmodell zu, sofern beide Flüsse auf dieselbe Normierung bezogen sind und der Winkelterm nur von der relativen Phase abhängt. Als Aggregation wähle einen linearen orientierten Fluss $L=uP_1+vP_2$ und verlange, dass er unter der gekoppelten Dynamik erhalten bleibt. Für nichtkonstantes $V$ gilt

$$
\dot L=(2v-u)V'(\phi)/k,
$$

also $u=2v$. Die positive Flächenausgabe $|L|$ stimmt auf der klassisch gebundenen Teilfläche mit $|P_1|+|P_2|$ überein, wenn der positive Normierungsfaktor

$$
v=\frac{c_1+2c_2}{c_1+4c_2}
$$

gewählt wird. Dies folgt aus $c_1P_1=2c_2P_2$ und gilt für beide Vorzeichen des Gesamtflusses. Der Betrag wird nach der Aggregation genommen. Damit ist der Kandidat auf dem vollen quantisierten Torus durch die gemeinsame Fourierbasis wohldefiniert:

$$
\widehat A_{\rm mix}=v|2\widehat P_1+\widehat P_2|=v a_M|\widehat n|.
$$

Jeder Zustand im Sektor $n=1$ hat für diese Observable den scharfen Wert $va_M$, auch wenn das Potential verschiedene relative Fouriermoden mischt. Bei gleichen Steifigkeiten ist das $3a_M/5$. Der Befund nutzt die volle Quantisierung. Er benötigt weder einen scharfen relativen Winkel noch eine exakte Flussaufteilung im Quantenzustand.

Die Kalibrierung gilt auf der klassisch gebundenen Teilfläche. Auf dem ganzen Träger sind beide Auslesungen verschieden, etwa bei $(P_1,P_2)=(p,-2p)$: Die gemischte Auslesung ergibt null, die additive $3|p|$. Der Selektor allein erzwingt keine Erhaltung und keine Kalibrierung. Die Eindeutigkeit gilt innerhalb der linearen orientierten Aggregate mit positivem Normierungsfaktor. Der nominale Zielwert $a_M/G$ verlangt weiterhin das unabhängig zu begründende Verhältnis $c_2/c_1=(G-1)/(2(2-G))$. Offen bleibt insbesondere, ob die native T-Randauslesung den erhaltenen orientierten Fluss aggregiert und erst danach den Betrag nimmt.

## Qiskit-Erkundung der zwei Flächenauslesungen

Das Skript `qam_hc_area_qiskit.py` kodiert die Fouriermoden $(0,1)$ und $(1,-1)$ des Sektors $n=1$ als ein Qubit. Die Projektion von $g\cos\phi$ liefert die X-Kopplung. Eine X-Rotation gefolgt von einer Z-Rotation modelliert einen getrennten Kopplungs- und Kinetikschritt. Aus den Wahrscheinlichkeiten der Fourierbasis berechnet das Skript die beiden Verteilungen durch Zuordnung der jeweiligen Flächenwerte.

Analytisch ergibt der Kopplungswinkel $\pi/2$ die additive Verteilung $a_M$ und $2a_M$ mit je $1/2$. Die gemischte Verteilung ergibt $3a_M/5$ mit Wahrscheinlichkeit eins. Das Skript lässt sich mit installiertem Qiskit über `python notes/research/qam_hc_area_qiskit.py` starten. Der lokale Lauf blieb bei der fehlenden Qiskit-Installation stehen. Die Erkundung implementiert beide vorgegebenen Auslesungen im abgeschnittenen Modell.

## Welche Information muss die gemischte Auslesung behalten?

Erkundung. Schreibe die additive Fläche als $a_M s$ mit $s=|m_1|+|m_2|$ und den gemischten Ausgang als $v a_M |n|$ mit $n=2m_1+m_2$ und $v>0$. Die Moden $(0,1)$ und $(1,0)$ haben dieselbe additive Fläche $a_M$, aber gemischte Flächen $v a_M$ und $2v a_M$. Jede Nachverarbeitung, die nur den additiven Messwert empfängt, gibt für beide Moden dieselbe Ausgangsverteilung. Daher scheitert auch randomisierte Nachverarbeitung an diesen beiden scharfen Sollwerten.

Allgemeiner liegen für jedes ganzzahlige $s\ge0$ die Moden $(j,s-j)$ mit $0\le j\le s$ auf derselben additiven Faser. Ihre Beträge $|n|=s+j$ sind paarweise verschieden. Ein klassischer Zusatzcode, der zusammen mit $s$ den exakten gemischten Ausgang bestimmen soll, benötigt daher auf dieser Faser mindestens $s+1$ verschiedene Symbole. Ein festes Zusatzbit genügt schon bei $s=2$ nicht. Die Untergrenze gilt für exakte Dekodierung auf allen Moden dieser Faser, einschließlich probabilistischer Codes, deren Träger für verschiedene Sollwerte disjunkt sein müssen.

Als hinreichendes Ausleselabel dient $|n|$ selbst. Seine Spektralprojektion unterscheidet keine relativen Fouriermoden mit gleichem $|n|$. Eine Auslesung allein im festen Sektor $n=1$ kann dagegen die sektorenübergreifende Information nicht prüfen, da dort der gemischte Ausgang konstant ist. Ein Übergangsmodell lässt sich daher zuerst an verschiedenen Sektoren mit gleicher additiver Fläche prüfen. Das Ergebnis gilt für die gewählten Observablen im Torusmodell.

### Kohärenter Flusszeiger auf der Faser s=1

Die Erkundung `python -m qam.examples.flux_pointer_qiskit` kodiert $(j,1-j)$ mit $j=0,1$ und schreibt $n-1=j$ per CNOT auf ein anfangs leeres Zeigerqubit. Die Qiskit-Simulation ergibt in beiden Basiszuständen additive Fläche $a_M$ mit Wahrscheinlichkeit eins. Die Zeigerwerte $n=1$ und $n=2$ sind jeweils scharf. In der gleichgewichteten Überlagerung treten nur die korrelierten Paare $(n,n_{\rm Zeiger})=(1,1),(2,2)$ mit je $1/2$ auf. Mit der separat deklarierten Skalierung $v=3/5$ entsprechen diese Zeigerwerte $3a_M/5$ und $6a_M/5$. Die Schaltung liest ein in der Modellkodierung bereits vorhandenes Sektorlabel aus. Ihre Wirkung ist auf diese beiden Moden beschränkt.

### Betragszeiger und Vorzeichenkohärenz

Erkundung. Bei $n=+1,-1$ ist $A_{\rm mix}=va_M$ entartet. Eine ideale projektive Betragsmessung erhält daher die Kohärenz einer Überlagerung innerhalb dieser beiden Sektoren. Eine feinere Messung, die das Vorzeichen in einem orthogonalen Zusatzregister festhält und für die Flächenangabe anschließend ignoriert, liefert dieselbe Flächenstatistik. Der reduzierte Zustand verliert dabei seine Vorzeichenkohärenz.

Die Schaltung `python -m qam.examples.flux_magnitude_qiskit` prüft die beiden Vorgänge im Ausschnitt $|n|=1$. Das Betragsbit wird dort konstant gesetzt. Nach Präparation der gleichgewichteten Überlagerung und Rückrotation mit Hadamard liefert die Qiskit-Simulation ohne Vorzeichenregister das Interferenzbit null mit Wahrscheinlichkeit eins. Mit gespeichertem Vorzeichen liefert sie null und eins mit je $1/2$. Der Interferenztest setzt voraus, dass die beiden Vorzeichensektoren kohärent präpariert und rekombiniert werden können. Ob dies nativ zulässig ist und ob die T-Auslesung die Kohärenz erhält, bleibt offen.

### Dynamischer Zugang zur Vorzeichenphase

Erkundung. Im Torusmodell erzeugt $\hat n$ die gemeinsame Winkelverschiebung. Jede zugelassene Präparation und Auslesung, die mit $\hat n$ kommutiert, ist blockdiagonal in $n$. Für jedes solche Ausleseobservable verschwindet insbesondere das Matrixelement zwischen $+n$ und $-n$ für $n\ne0$. Die relative Phase der Überlagerung ist in dieser Operationsklasse unbeobachtbar. Das Winkelpotential $V(\phi)$ liegt in dieser Klasse. Eine Flussumkehr kann Sektoren vertauschen, liefert durch diesen Tausch allein aber keinen Interferenzzugang. Die r51-Korrektur trennt zudem die Zeitumkehr mit Porttausch vom Tachyon-Framewechsel. Eine dortige Vorzeichenregel identifiziert den gravitativen Randfluss noch nicht mit der betreffenden Ladung.

Ein relationaler Kandidat ist ein zweiter periodischer Winkel $\theta_R$ mit ganzzahligem Referenzfluss $r$. Die Zustände $(n,r)=(+1,-1),(-1,+1)$ liegen beide im Gesamtsektor $n+r=0$. Der Operator $U=\exp[2i(\theta-\theta_R)]$ verschiebt $(n,r)$ um $(2,-2)$, kommutiert also mit $\hat n+\hat r$ und hat zwischen diesen Zuständen ein nichtverschwindendes Matrixelement. Für $X=U+U^\dagger$ hat die normierte Überlagerung mit relativer Phase $\alpha$ den Erwartungswert $\cos\alpha$, das inkohärente Gemisch den Wert null. Der Kandidat setzt einen Referenzkanal und eine zulässige Kopplung voraus, die zwei Flusseinheiten austauscht. Im bisherigen Randmodell sind diese Daten nicht gegeben.

### r30 als Kandidat für die relationale Vorzeichenauslesung

Der Heisenberg-Kompensator aus v4.9.0-r30 ist eine vorhandene phasensensitive Portauslesung. Auf seinem Doublet ist der Portprojektor $(I+\sigma_x)/2$. Um die Struktur im Randmodell zu prüfen, identifiziere vorläufig je ein solches Doublet mit den Flusslabels $+1,-1$ von Rand und Referenz. Im Gesamtsektor null mit Projektor $\Pi_0$ ist $\Pi_0(\sigma_x\otimes I)\Pi_0=0$. Ein einzelner r30-Port komprimiert daher auf $\Pi_0/2$. Der kombinierte Paritätsport hat dagegen den Effekt

$$
\Pi_0\frac{I+\sigma_x\otimes\sigma_x}{2}\Pi_0.
$$

Er unterscheidet die symmetrische und antisymmetrische Überlagerung der Paare $(+1,-1),(-1,+1)$. Für relative Phase $\alpha$ beträgt seine Wahrscheinlichkeit $(1+\cos\alpha)/2$, für das inkohärente Gemisch $1/2$. Eine auf allen Gesamtsektoren erhaltende Erweiterung verwendet den Austausch $\sigma_+\otimes\sigma_-+\sigma_-\otimes\sigma_+$ anstelle des unbeschränkten Doppel-Flips. Außerhalb des Gesamtsektors null würde der Doppel-Flip auch gleichgerichtete Paare umkehren. Der kombinierte Effekt ist somit ein konkreter Modellkandidat; r30 liefert weder die Identifikation seiner Doublets mit Randflüssen noch die native Zulassung des gemeinsamen Ports.

### Austauschanteil der vorhandenen r27-Zweikopien-Auslesung

Erkundung. Identifiziere in beiden r27-Doublets versuchsweise die $Z$-Eigenwerte mit den Flussvorzeichen. Auf dem Gesamtflusssektor null gilt $ZZ=-I$ und $XX=S$, wobei $S$ die beiden gegenläufigen Paare vertauscht. Damit hat die vorhandene r27-Observable $H=XX+ZZ$ dort die Einschränkung $S-I$. Das symmetrische Paar hat Eigenwert null, das antisymmetrische Eigenwert minus zwei, das gleichgewichtete inkohärente Gemisch Erwartungswert minus eins. Der aus r30 motivierte Austauschport hat auf diesem Sektor also den Effekt $I+H/2$.

Auf dem ganzen Doubletprodukt koppelt $XX$ auch die gleichgerichteten Paare und erhält $Z_1+Z_2$ daher nicht. Eine gemeinsame Mittelung über die von $Z_1+Z_2$ erzeugten Phasen entfernt genau diesen Anteil: Aus $H$ wird $ZZ+(XX+YY)/2$. Diese Observable erhält den Gesamtfluss auf dem ganzen Produkt und hat dieselbe Einschränkung im Nullsektor. Die Mittelung ist eine zusätzliche Modelloperation.

Auch die Präparation kann auf eine konkrete Zulassungsfrage reduziert werden: Projiziert man die r27-Eingabe $|+_x\rangle\otimes|+_x\rangle$ kohärent auf den Gesamtsektor null, entsteht das symmetrische Paar mit Erfolgswahrscheinlichkeit $1/2$. Eine Messung beider lokalen Vorzeichen mit nachträglicher Auswahl gegenläufiger Paare liefert stattdessen das inkohärente Gemisch. r27 deklariert unabhängige identische Präparation und eine Zweikopien-Auslesung. Die kohärente Gesamtflussprojektion und die Identifikation der r27-Achse mit Randfluss sind zusätzliche Voraussetzungen. Die Ausleseobservable ist außerdem für sich noch kein dynamischer Kopplungsterm.

### Kohärente Auswahl des Gesamtflusses als Paritätsmessung

Erkundung. Auf zwei Vorzeichendoublets entspricht ungerade Z-Parität genau dem Gesamtfluss null. In `python -m qam.examples.flux_parity_qiskit` speichern zwei CNOTs nur diese Parität in einem gemeinsamen Zeiger. Die Simulation wählt aus der r27-Produktpräparation in beiden Varianten mit Wahrscheinlichkeit $1/2$ aus. Beim reinen Paritätszeiger ist der positive Austauschport danach sicher. Werden zusätzlich die lokalen Vorzeichen gespeichert und ignoriert, ergibt der positive Austauschport nur noch Wahrscheinlichkeit $1/2$. Die abschließende Auswertung des X-Paritätswerts dient im gewählten Nullsektor als Austauschdiagnose. Die Hadamard-Rotationen zur Simulation dieser Auswertung sind keine hergeleitete flusserhaltende Randoperation. Die Paritätsprojektoren des Orbit-Scans betreffen die Indexparität; eine Identifikation mit der Gesamtflussmessung ist nicht belegt.

### Orbit-Parität als Kandidat für den gemeinsamen Selektor

Erkundung. Der Orbit-Scan definiert Projektoren auf gerade und ungerade Indexwerte und einen einfachen Shift, der ihre Bilder vertauscht. Auf den zwei Vorzeichendoublets gilt für die Indexwahl $j=(n+r)/2$: Gegenläufige Paare haben $j=0$, gleichgerichtete Paare $j=\pm1$. Auf diesem Ausschnitt reproduziert daher der gerade Orbit-Projektor den Nullsektor. Eine treue Kodierung braucht innerhalb von $j=0$ ein zusätzliches Multiplizitätslabel, um die zwei orthogonalen Zustände zu erhalten. Der Projektor muss auf dieses Label als Identität wirken. Ein Zeiger, der es zusätzlich speichert, würde die Austauschinterferenz im reduzierten Zustand entfernen.

Die Identifikation benötigt einen nativen Nachweis für $j\equiv(n+r)/2\pmod 2$. Die Shift-Regel allein liefert ihn nicht: Der relative Austausch erhält $n+r$ und muss die gemeinsame Parität erhalten, während ein einfacher Orbit-Shift sie umkehrt. Auf dem erweiterten Bereich mit geradem Gesamtfluss wählt dieselbe Paritätsregel sämtliche $n+r\equiv0\pmod4$ aus, einschließlich $n+r=\pm4$. Die genaue Nullselektion durch ein einzelnes Paritätsbit gilt daher nur in einem Bereich ohne diese weiteren Sektoren. Der Orbit-Projektor legt zudem die selektierten Zustände fest, während ein kohärenzerhaltender Messkanal eine zusätzliche instrumentelle Realisierung verlangt.

### Gemeinsamer Phasenzeiger über den Paritätsausschnitt hinaus

Erkundung. Sei $j=(n+r)/2$ ganzzahlig auf dem betrachteten Bereich. Für eine ganze Zahl $L\ge2$ bildet die Charakter-Mittelung

$$
Q_L=\frac1L\sum_{k=0}^{L-1}\exp(2\pi i k\hat j/L)
$$

den Projektor auf $j\equiv0\pmod L$. Jeder Summand hat auf demselben Gesamtfluss dieselbe Phase, unabhängig von den lokalen Vorzeichen. Ein gemeinsames $L$-dimensionales Zeigerregister, kontrollierte Phasen und inverse Fouriertransformation schreiben $j\bmod L$ in den Zeiger und lassen die interne Multiplizität unverändert. Im Ausgang null lautet die unnormierte Zustandsabbildung $\rho\mapsto Q_L\rho Q_L$.

Für einen begrenzten Bereich $|j|\le J$ genügt $L>J$ zur exakten Nullselektion. Beispielsweise erfasst Parität bei $j=-2,-1,0,1,2$ die drei Werte $-2,0,2$. Ein gemeinsamer Dreiphasenzeiger wählt dort nur null. Auf unbeschränktem ganzzahligem Bereich bleiben bei jedem festen $L$ Aliaswerte $j=\pm L,\pm2L,\ldots$. Die kontinuierliche gemeinsame Phasenmittelung über eine volle Periode projiziert exakt auf null. Für diese Umsetzung muss die QAM kontrollierte Phasen des Gesamtflussgenerators zulassen. Ein Zugriff nur auf den einfachen Orbit-Shift liefert diese Operation nicht unmittelbar.

### Ausschluss für Shift und Parität als alleinige Orbit-Operationen

Erkundung. Auf dem ganzzahligen Orbit kommutieren sowohl der Shift $\Sigma$ als auch die Paritätsprojektoren mit $\Sigma^2$. Dies bleibt bei Summen, Produkten und Adjungieren erhalten. Eine daraus gebaute Schaltung mit orbitunabhängig präpariertem Zeiger und nur am Zeiger ausgelesenem Ergebnis hat folglich Effekte, die ebenfalls mit $\Sigma^2$ kommutieren. Für solche Effekte gilt $\langle e_j,Ee_j\rangle=\langle e_{j+2},Ee_{j+2}\rangle$. Auch mit einem Zeiger bleiben somit die Basiszustände $e_0$ und $e_2$ anhand der Ausgangsstatistik ununterscheidbar.

Ein diagonaler Effekt innerhalb dieser Operationsklasse kann nur auf der Indexparität beruhen. Der Modulo-$L$-Nullprojektor für $L>2$ und der exakte Nullprojektor erfüllen die Kommutationsbedingung nicht. Für den Modellindex $j=(n+r)/2$ kann man den benötigten Zusatz als Diagonalphase $D_L e_j=e^{2\pi i j/L}e_j$ formulieren. Sie erfüllt $D_L\Sigma=e^{2\pi i/L}\Sigma D_L$ und unterscheidet $j=0$ von $j=2$ für $L>2$. Ein numerischer Ausschnitt mit abgeschnittenem Shift kann die Zweiershift-Symmetrie am Rand verlieren. Eine dadurch gewonnene Ortsauflösung zählt nur mit unabhängig begründeter physikalischer Randbedingung als native Ressource. Der Ausschluss setzt die genannten Generatoren und den gemeinsamen Zeiger voraus und lässt weitere QAM-Operationen offen.

### Markierter Orbit-Ursprung oder relationaler Vergleich

Erkundung. Der Orbit-Scan definiert die Basiszustände und die Paritätsprojektoren, aber in der geprüften Shift-Definition keinen auslesbaren Projektor auf einen ausgezeichneten Ursprung. Ein zusätzlicher Punktprojektor $E_0=|e_0\rangle\langle e_0|$ würde genügen: $E_j=\Sigma^j E_0\Sigma^{-j}$. In einer Flusskodierung mit interner Multiplizität muss der Punktprojektor auf allen Zuständen desselben Gesamtindex als Identität wirken. Ein Rang-eins-Projektor auf einen einzelnen internen Zustand genügt dafür nicht.

Eine relationale Alternative ist ein Referenzorbit mit Index $b$ und der gemeinsame Gleichheitsprojektor $E_{=}=\sum_j E_j\otimes F_j$, wobei $F_j$ der Indexprojektor auf der Referenz ist. Dieser Vergleich ist invariant unter gleichzeitiger Translation beider Indizes. Für eine unabhängig präparierte Referenz mit Indexverteilung $p_b$ ist die Akzeptanzwahrscheinlichkeit bei Systemindex $j$ genau $p_j$. Eine scharfe Referenz bei $b=0$ reproduziert daher die Nullselektion; eine unscharfe Referenz liefert eine gewichtete Akzeptanz. Im exakten Nullsektor liest der ideale Gleichheitskanal keine interne Flussaufteilung aus. Die native Hürde verschiebt sich auf zwei konkrete Ressourcen: die Präparation eines markierten Referenzindex und ein kohärentes Gleichheitsinstrument. Shift und Parität auf beiden getrennten Orbits erzeugen dieses Instrument nicht, da sie auch unter unabhängigem Zweiershift invariant sind und Gleichheit dabei im Allgemeinen wechselt.

### Gleichheitsauslesung durch kontrollierte Orbit-Verschiebungen

Erkundung. Verwende einen dritten Orbit als Arbeitsregister mit scharfem Index $d=0$. Ein durch den Systemindex $j$ kontrollierter Shift und ein durch den Referenzindex $b$ kontrollierter inverser Shift bilden $(j,b,d)$ auf $(j,b,d+j-b)$ ab. Das gilt auf dem ganzzahligen Orbit und modulo der Orbitlänge auf einem endlichen zyklischen Orbit. Der Vergleich ist invariant unter gemeinsamer Verschiebung von $j$ und $b$.

Um nur Gleichheit zu speichern, kopiere das Prädikat $d=0$ nach den Shifts auf einen binären Zeiger und führe beide Shifts rückwärts aus. Das Arbeitsregister kehrt auf null zurück. Im Zeiger steht nur $[j=b]$. Wer dagegen den vollständigen Differenzindex im Arbeitsregister ausliest oder ihn dort speichert und ignoriert, kann Kohärenzen zwischen unterschiedlichen ungleichen Paaren entfernen. Der Unterschied betrifft also auch den abgelehnten Zweig des Instruments.

Die Orbit-Definition liefert die festen Potenzen $\Sigma^k$. Für diesen Aufbau braucht man deren kohärente Auswahl durch einen anderen Orbit, das heißt eine gemeinsame Operation der Form $\sum_j E_j\otimes\Sigma^j$, sowie einen Nulltest für das Arbeitsregister. Die feste Shift-Familie liefert diese kontrollierte Operation nicht für sich. Der Aufbau benennt einen hinreichenden Satz von Ressourcen und setzt keine native Verfügbarkeit voraus.

### Relationaler Vergleich über mehrere Referenzkopien

Erkundung. Als Alternative zur Differenzrechnung betrachte einen Systemindexzustand $e_j$ und $k\ge1$ Referenzkopien im scharfen Zustand $e_b$. Der Projektor auf den symmetrischen Unterraum der $k+1$ Indexregister ist das Mittel aller Registerpermutationen. Bei $j=b$ bleibt der Eingang unverändert und wird sicher akzeptiert. Bei $j\ne b$ tragen im Erwartungswert genau die Permutationen bei, die den Systemplatz festlassen: Jede andere setzt einen orthogonalen Index an diesen Platz. Die bedingte Akzeptanz beträgt damit $k!/(k+1)!=1/(k+1)$. Für eine Referenzkopie ist das der symmetrische Ausgang des Swap-Tests.

Bei einer gemeinsamen Referenzmischung, die zuerst $b$ mit Wahrscheinlichkeit $p_b$ wählt und dann $k$ identische Indexzustände präpariert, beträgt die Akzeptanz für Systemindex $j$ genau $p_j+(1-p_j)/(k+1)$. Das beschreibt gemeinsam gezogene Referenzindizes. Die Formel gilt nicht allgemein für unabhängige Ziehungen. Für jede endliche Kopienzahl und scharfe Referenz bleibt eine positive Falschakzeptanz. Im akzeptierten Zweig kann der Symmetrieprojektor den Systemindex bei einer Falschakzeptanz auf mehrere Register verteilen. Die Rechnung belegt daher eine Vergleichsstatistik, keinen exakten Gleichheitskanal.

Für die Kohärenz der gegenläufigen Paare muss die Permutation nur die Indexregister betreffen und die interne Flussaufteilung als separates Register unangetastet lassen. Die vorhandene r27-Zweikopien-Auslesung motiviert einen Vergleich mit Kopien, liefert aber allein weder einen solchen separaten Indexträger noch den symmetrischen Projektor als natives Messinstrument.

### Grenze des basisunabhängigen Vergleichs mit Referenzkopien

Erkundung. Betrachte einen endlichen Indexraum und einen gemeinsamen Akzeptanzeffekt $0\le E\le I$ auf $k+1$ Registern. Verlange sichere Akzeptanz gleicher Eingaben in jeder möglichen Indexbasis. Dann gilt $\langle u^{\otimes(k+1)}, E u^{\otimes(k+1)}\rangle=1$ für jeden Einheitsvektor $u$. Positivität von $I-E$ impliziert, dass $E$ jeden dieser Vektoren festlässt. Die reinen Tensorpotenzen spannen den symmetrischen Unterraum auf: Die Koeffizienten der Potenz $(\sum_i t_i e_i)^{\otimes(k+1)}$ sind die symmetrisierten Basistensoren. Damit wirkt $E$ auf dem symmetrischen Unterraum als Identität und hat wegen Selbstadjungiertheit keine Kreuzblöcke. Also gilt $E\ge\Pi_{\rm sym}$.

Für orthogonale Indexzustände $u\perp v$ mit Eingabe $u\otimes v^{\otimes k}$ ist die Falschakzeptanz folglich mindestens $1/(k+1)$. Der symmetrische Projektor erreicht die Schranke. Eine fest bekannte und zugängliche Indexbasis ändert die Voraussetzungen: Der diagonale Gleichheitseffekt kann die Basiszustände exakt vergleichen und muss keine beliebigen gleichen Superpositionen sicher akzeptieren. Die native Frage lautet daher, ob die QAM für den Vergleich Zugriff auf die physikalisch ausgezeichnete Indexzerlegung bereitstellt.

### Relativer Shift und relative Indexphase

Erkundung. Auf zwei identischen zyklischen Orbits der Länge $N$ setze $R=\Sigma\otimes\Sigma^{-1}$. Für jedes Basispaar $(j,b)$ gilt $\langle j,b|R^k|j,b\rangle=1$ für $k\equiv0\pmod N$ und null sonst. Die Spektralverteilung von $R$ ist daher auf den $N$-ten Einheitswurzeln gleichverteilt, unabhängig von $j-b$. Insbesondere geben gleiche und ungleiche Indizes dieselbe Statistik. Auf dem ganzzahligen Orbit ergibt dieselbe Momentenrechnung das gleichförmige Maß auf dem Einheitskreis. Der relative Shift liefert somit auch mit idealer Phasenmessung für sich keinen Gleichheitszeiger.

Falls dagegen die lokale Diagonalphase $D_N e_j=\exp(2\pi i j/N)e_j$ auf beiden Orbits zugänglich ist, hat $D_N\otimes D_N^\dagger$ den Eigenwert $\exp(2\pi i(j-b)/N)$. Die Eins-Eigenspace-Auswahl ist auf dem zyklischen Orbit exakt der Gleichheitsprojektor. Die entgegengesetzten lokalen Phasen heben sich unter einer gemeinsamen Verschiebung des Ursprungs auf. Für einen kohärenten binären Vergleich muss das Instrument nur Eins gegen den Rest aufzeichnen; ein vollständiger Phasenrekord kann die Kohärenz im abgelehnten Zweig weiter auflösen. Die lokale Diagonalphase und ihre kontrollierte gemeinsame Anwendung bleiben native Voraussetzungen.

### Prüfkriterium für die r11-Stufenphase als Orbit-Zeiger

Erkundung. r11 liefert eine pro Stufe angewandte Dualitätsrotation und eine akkumulierte Phase von $30^\circ$ pro Stufe. Diese Aussage betrifft die Fortentwicklung eines Zustands. Ein Indexzeiger müsste dagegen eine Phase auf gleichzeitig vorhandene Indexsektoren schreiben, ohne sie zu verschieben. Der direkte Kandidat $D\Sigma=\omega\Sigma D$ mit $\omega=\exp(i\pi/6)$ erzwingt für ein $D$-Eigenobjekt $v$ mit Eigenwert $\lambda$, dass $\Sigma^jv$ die Eigenwerte $\lambda\omega^j$ hat. Bei unitärem $D$ sind die ersten zwölf nichtverschwindenden Orbitvektoren deshalb paarweise orthogonal. Ein Träger für dieses Shift-Phase-Paar braucht mindestens zwölf Dimensionen.

Die in r11 verwendete Bloch-Doublet-Darstellung kann diese zwölf orthogonalen Indexsektoren nicht tragen. Auch eine Stufenfolge mit zwölf verschiedenen Feldphasen liefert die nötige Orthogonalität nicht allein. Eine mögliche zusätzliche Ressource wäre ein separates kohärentes Indexregister mit zwölf unterscheidbaren Sektoren, das durch eine gemeinsame Operation an die Randkanäle gekoppelt ist. r11 stellt im geprüften Stufenmodell die Rotationsphase bereit; die Verwendung als indexabhängige Zeigerphase verlangt diesen weiteren Nachweis.

### Zwölferphase aus einem gemeinsamen Dreier- und Viererindex

Erkundung. Für einen Orbit mit ganzzahligem Index $j$ seien $D_3 e_j=e^{2\pi i j/3}e_j$ und $D_4 e_j=e^{2\pi i j/4}e_j$. Sind beide Phasen auf demselben Indexträger verfügbar, gilt $D_3D_4^\dagger e_j=e^{2\pi i j/12}e_j$. Alternativ liefert das Produkt der kommutierenden Nullprojektoren für $j\bmod3$ und $j\bmod4$ genau den Nullprojektor für $j\bmod12$. Auf $|j|\le11$ ist das eine exakte Nullselektion. Werden die beiden Restwerte dauerhaft getrennt gespeichert, können sie zusätzliche Information im abgelehnten Zweig hinterlassen. Berechnung, binäre Nullmarkierung und Rückrechnung liefern dagegen nur das gemeinsame Nullbit.

Eine explizite Modellkodierung ist der Produktraum $\mathbb C^3\otimes\mathbb C^4$ mit Basisindex $(j\bmod3,j\bmod4)$. Der gemeinsame Shift inkrementiert beide Reste und durchläuft alle zwölf Paare. Die Phasen wirken jeweils diagonal auf einem Faktor. Der zwölfstufige Träger ist der gemeinsame Indexraum; der endgültige Nullzeiger braucht nur zwei Zustände. Die triolische Dreierphase und die Vierteldrehung in den Quellen reichen für die physikalische Identifikation erst dann aus, wenn sie beide als diagonale Charaktere desselben Randindex ausgewiesen sind. Zwei Rotationen mit passenden Winkeln belegen diese Zuordnung allein nicht.

### Was die r11-Rotation nach sechs Schritten unterscheidet

Erkundung. In der reellen Doublet-Darstellung setze $R=R_{\pi/6}$. Auf der komplexifizierten Darstellung hat $R^j$ die Eigenwerte $e^{\pm i\pi j/6}$. Daher gilt $R^{j+6}=-R^j$. Die gewöhnliche Zustandsentwicklung $\rho\mapsto R^j\rho(R^j)^\dagger$ ist folglich für $j$ und $j+6$ identisch. Die $120^\circ$- und $90^\circ$-Rotationen sind in dieser Darstellung $R^4$ und $R^3$. Ihre Konjugationswirkungen haben Ordnung drei beziehungsweise zwei; bei gemeinsamer Potenzierung sehen sie zusammen höchstens den Rest modulo sechs. Für einen idealen Vergleich der beiden Wirkungen ist die gemeinsame Periode genau sechs, da $3$ und $2$ teilerfremd sind. Dies betrifft die unkompensierten Rotationskanäle und keine Stufenfolge mit protokollierten Zwischenauslesungen.

Eine kohärent kontrollierte Anwendung wäre stärker. Wenn ein gemeinsamer Zeiger kontrolliert $R^j$ auf ein präpariertes Eigenobjekt von $R$ anwenden darf, erhält der Zeiger die relative Phase $e^{i\pi j/6}$. Sie wechselt zwischen $j$ und $j+6$ das Vorzeichen. Dazu muss der Gesamtflussindex $j$ kohärent die Potenz steuern; die vorhandene Einzeldoublet-Rotation belegt diese Operation nicht. Der zusätzliche Indexträger kann in diesem Modell den Gesamtfluss tragen, während das Doublet nur als Phasenquelle dient.

### Gemeinsame Phase aus zwei lokalen Flusskopplungen

Erkundung. Ein Zeigerqubit mit Zuständen $|0\rangle,|1\rangle$ kopple nacheinander an Rand und Referenz. Die beiden bedingten Phasen seien $\exp(i\kappa_n\hat n\otimes |1\rangle\langle1|)$ und $\exp(i\kappa_r\hat r\otimes |1\rangle\langle1|)$. Bei gleicher Kopplungsstärke $\kappa_n=\kappa_r=\pi/12$ trägt der Zeigerzweig eins die Phase $\exp(i\pi(n+r)/12)=\exp(i\pi j/6)$. Damit reicht im Modell ein gemeinsamer Zeiger mit zwei lokalen kontrollierten Kopplungen. Ein direkter Rand-Referenz-Austausch ist für diese Phasenabfrage nicht erforderlich. Der Zeiger darf zwischen den Kopplungen nicht ausgelesen werden.

Bei ungleichen Stärken und anfangs gleichgewichteten Zeigerzweigen haben die Nullsektor-Eingaben $(+1,-1)$ und $(-1,+1)$ die bedingten Zeigerzustände $(|0\rangle+e^{\pm i\delta}|1\rangle)/\sqrt2$ mit $\delta=\kappa_n-\kappa_r$. Beim Ignorieren des Zeigers wird der Betrag der Vorzeichenkohärenz mit $|\cos\delta|$ multipliziert. Bei $\delta\equiv0\pmod\pi$ bleibt die Kohärenz erhalten, auch wenn eine verbleibende Phase separat zu kalibrieren ist. Eine Störung, die bereits nach dem ersten Puls einen lokalen Flussrekord hinterlässt, wird durch die zweite Phase nicht gelöscht. Die beiden lokalen kontrollierten Flusskopplungen und der gemeinsame kohärente Zeiger sind hier Modellressourcen; die r11-Rotation allein liefert sie nicht.

Die Qiskit-Erkundung `python -m qam.examples.common_flux_phase_qiskit` unterscheidet bei passenden Pulsen die Modellindizes $j=0$ und $j=6$ mit Sicherheit. Im Nullsektor liefert der feste Hadamard-Interferenzport für $\delta=0,\pi/6,\pi/2$ die Wahrscheinlichkeiten $1,7/8,1/2$. Hier misst die feste Auslese den Realteil des Kohärenzfaktors $e^{i\delta}\cos\delta$, also $\cos^2\delta$, während die phasenoptimierte Sichtbarkeit $|\cos\delta|$ beträgt. Die Simulation kodiert jeweils zwei ausgewählte Flusspaare auf einem Qubit und realisiert die lokalen Phasen als Summe zweier Gatterfolgen in dieser komprimierten Basis. Sie implementiert keinen vollständigen Modulo-Zeiger.

### Qiskit-Abgleich aller zwölf Restklassen

Erkundung. `python -m qam.examples.flux_mod12_qiskit` präpariert einen gleichgewichteten Zeiger über zwölf der sechzehn Basiszustände von vier Qubits. Für jede fest vorgegebene Flussbelegung tragen die beiden lokalen Pulsfolgen gemeinsam die Phase $\exp(2\pi i k j/12)$ am Zeigerindex $k$ auf. Die inverse Präparation gibt beim Nullausgang das Quadrat des Betrags des Mittels dieser zwölf Phasen. Qiskit bestätigt Akzeptanz eins bei $j=0$ und null für alle Reste eins bis elf. Die beiden gegenläufigen Flusspaare bei $j=0$ und die erwarteten Aliaswerte $j=\pm12$ werden ebenfalls akzeptiert. Die Flüsse sind in dieser Simulation klassische Schaltungsparameter. Eine kohärente Steuerung durch dynamische QAM-Randregister wird damit nicht getestet.

### Kohärent gesteuerter Zwölferzeiger

Erkundung. `python -m qam.examples.coherent_flux_mod12_qiskit` kodiert die beiden Flussvorzeichen in separaten Qubits und steuert die beiden lokalen Phasen kohärent. Nach der binären Nullmarkierung invertiert die Schaltung die gesamte Phasenabfrage. Der Arbeitszeiger kehrt auf null zurück. Für die gleichgewichtete Produktpräparation ergibt sich Akzeptanz $1/2$ und im akzeptierten Zweig positive Austauschparität mit Wahrscheinlichkeit eins. Damit bleibt die relative Phase der beiden gegenläufigen Paare erhalten. Die kohärente Simulation betrifft die Vorzeichendoublets mit $j=-1,0,1$. Die Prüfung aller zwölf Restklassen in der vorigen Erkundung verwendet dagegen klassische Flussparameter. Native Flusskodierung und kontrollierte Kopplung bleiben Modellannahmen.

### Lineare Zeigerphase aus quadratischer Randenergie

Erkundung. Auf dem ganzzahligen Flussgitter sei $S|n\rangle=|n+1\rangle$ und $U(t)=\exp(-it\lambda\hat n^2)$, wobei $\lambda$ die Energienormierung in Frequenzeinheiten enthält. Die Folge aus Drift und um einen Schritt versetzter Gegenevolution ergibt

$$
U(t)^\dagger S^\dagger U(t)S
=\exp[-it\lambda(2\hat n+1)].
$$

Sie verschiebt den Fluss am Ende nicht. Kontrolliert der Zeiger nur $S$ und $S^\dagger$, während Drift und Gegenevolution auf beiden Zeigerzweigen laufen, ist der Nullzweig die Identität. Der Einszweig liefert nach einer bekannten konstanten Zeigerphasenkorrektur $\exp(-2it\lambda\hat n)$. Zwei solche Folgen für Rand und Referenz ergeben die gemeinsame Phase, wenn $t_n\lambda_n=t_r\lambda_r$. Damit lässt sich der benötigte lineare Term aus einer quadratischen Drift gewinnen. Die Konstruktion setzt kohärent kontrollierte Flussshifts und inverse Drift voraus.

Der lokale Shift ändert den Gesamtfluss während der Folge. Falls jede Zwischenoperation den Gesamtfluss erhalten muss, scheidet er ohne Ausgleichskanal aus. Ein Shift $(n,r)\mapsto(n+1,r-1)$ erhält den Gesamtfluss, liefert für die Summe der quadratischen Driften aber den linearen Term $2(\lambda_n n-\lambda_r r)$ und misst bei gleichen Koeffizienten die Differenz. Gerade die beiden gegenläufigen Nullsektorpaare werden dadurch im Allgemeinen verschieden markiert. Eine Vorzeichenumkehr der Referenzdrift oder eine weitere Ressource müsste getrennt begründet werden. Die quadratische Randenergie des früheren Modells betrifft die Flüsse $P_1,P_2$; die hier verwendeten getrennten Driften in $n,r$ sind eine Kandidatenannahme.

### Flusserhaltende Phasenabfrage mit einem Pufferkanal

Erkundung. Ergänze einen Pufferfluss $b$ mit quadratischer Drift $Q=\lambda_n n^2+\lambda_r r^2+\lambda_b b^2$. Der gemeinsame Shift $B:(n,r,b)\mapsto(n+1,r+1,b-2)$ erhält $n+r+b$. Er kann als Folge zweier flusserhaltender Transfers aus dem Puffer ausgeführt werden. Die kontrollierte Driftfolge $e^{itQ}B^\dagger e^{-itQ}B$ schreibt die Phase mit Exponent

$$
-it[2\lambda_n n+2\lambda_r r-4\lambda_b b+\lambda_n+\lambda_r+4\lambda_b].
$$

Für $\lambda_n=\lambda_r=\lambda$ und einen scharf bei $b=b_0$ präparierten Puffer bleiben nach Korrektur der bekannten konstanten Zeigerphase nur $-2it\lambda(n+r)$ übrig. Der inverse Transfer setzt den Puffer auf $b_0$ zurück. Die beiden gegenläufigen Paare erhalten denselben Zeigerzustand. Der Puffer muss im verwendeten Bereich zwei Einheiten abgeben und wieder aufnehmen können. Bei einem unscharfen Puffer bleibt für $\lambda_b\ne0$ im Allgemeinen eine pufferabhängige Phase.

Damit ist Gesamtflusserhaltung in jedem Schritt mit dem Summenzeiger vereinbar. Voraussetzung sind hier ein dritter Kanal, die kontrollierten Transfers, passende Driftkoeffizienten und die inverse Drift. Ihre native Zulassung folgt weder aus dem Orbit-Shift noch aus dem vorhandenen Zweikanalmodell.

### Pufferzeiger mit ausschließlich vorwärts laufender Drift

Erkundung. Präpariere den Zeiger in $|+\rangle$, führe $B$ nur im Einszweig aus, lasse beide Zweige gleich lange unter $Q$ vorwärts entwickeln und führe $B^\dagger$ wieder nur im Einszweig aus. Die beiden Zweige tragen danach $e^{-itQ}$ und $B^\dagger e^{-itQ}B$. Auf einem Flusseigenzustand ist ihre relative Phase dieselbe wie in der Konstruktion mit Gegenevolution. Eine inverse Drift ist damit für die Zeigerstatistik überflüssig. Der gemeinsame Faktor $e^{-itQ}$ bleibt auf dem Flussregister und muss bei Aussagen über den Rückweg mitgeführt werden.

Für gleiche Rand- und Referenzkoeffizienten haben die gegenläufigen Paare $(+1,-1,b_0)$ und $(-1,+1,b_0)$ dieselbe Energie und dieselbe relative Zeigerphase. Deshalb wirkt der gemeinsame Faktor auf ihrer Überlagerung nur als globale Phase. Der Puffer kehrt in beiden Zeigerzweigen zum scharfen Ausgangsfluss zurück. Die Konstruktion setzt weiterhin die reversiblen, kohärent kontrollierten Transfers und eine gemeinsame quadratische Drift voraus. Für allgemeinere Superpositionen innerhalb eines Gesamtsektors kann die gemeinsame Drift relative Phasen ändern, auch wenn der Zeiger keine interne Information aufzeichnet.

### Ausschluss für zwei Kanäle mit stabiler quadratischer Drift

Erkundung. Sei $x=(n,r)$ und $Q(x)=x^{\mathsf T}Ax$ mit reeller symmetrischer positiv semidefiniter Matrix $A$, einschließlich eines Kreuzterms. Jeder flusserhaltende Gittertransfer ist eine Verschiebung um ein ganzzahliges Vielfaches von $v=(1,-1)$. Die Phasendifferenz einer verschobenen und unverschobenen Drift hat als linearen Anteil $2x^{\mathsf T}Av$ pro Transfereinheit. Auch mehrere stückweise konstante Verschiebungen bei derselben Driftmatrix liefern im Zweigvergleich nur ein skalares Vielfaches dieser linearen Form plus einen konstanten Term.

Eine nichttriviale reine Summenphase auf dem ganzen Gitter, als linearer Generator, würde $Av\propto(1,1)$ mit von null verschiedenem Faktor verlangen. Dann wäre $v^{\mathsf T}Av=0$. Positive Semidefinitheit erzwingt aber $Av=0$, etwa durch $v^{\mathsf T}Av=\|A^{1/2}v\|^2$. Somit liefert ein fester stabiler quadratischer Driftterm selbst mit Kreuzkopplung keinen reinen Summengenerator über diese Transfers.

Der Ausschluss betrifft den linearen Generator und dieselbe Driftmatrix in allen Abschnitten. Er lässt zeitlich umschaltbare Driftmatrizen sowie spezielle Phasenübereinstimmungen modulo $2\pi$ auf diskreten Ausschnitten offen. Der Pufferaufbau umgeht die Bedingung, weil seine Transferachse im Dreikanalraum liegt und der Pufferfluss scharf präpariert wird.

### Summenzeiger mit zwei vertauschten stabilen Driften

Erkundung. Verwende $Q_1=a n^2+b r^2$ und $Q_2=b n^2+a r^2$ mit $a,b>0$ und $a\ne b$. In der ersten Driftzeit $t$ verschiebe nur den Einszweig des Zeigers um $(+1,-1)$, in der zweiten um $(-1,+1)$. Jeder Transfer wird nach seiner Driftzeit rückgängig gemacht. Beide Zweige laufen jeweils vorwärts, und alle Transfers erhalten $n+r$. Die Energiedifferenzen in den beiden Abschnitten sind

$$
\Delta Q_1=2an-2br+a+b,\qquad
\Delta Q_2=-2bn+2ar+a+b.
$$

Nach Abzug der bekannten konstanten Zeigerphase ergibt sich die relative Phase $\exp[-2it(a-b)(n+r)]$. Der Nullzweig und der gemeinsame Faktor im Einszweig tragen die symmetrische Drift $\exp[-it(a+b)(n^2+r^2)]$. Diese ist für die beiden gegenläufigen Paare gleich und verändert ihre relative Phase nicht. Somit genügt ein Zweikanalmodell mit umschaltbarer Asymmetrie und kohärent kontrollierten Transfers. Bei $a=b$ verschwindet das Signal.

Ein hypothetischer kohärenter Registertausch $W|n,r\rangle=|r,n\rangle$ könnte die zweite Drift durch $Q_2=W^\dagger Q_1W$ synthetisieren. Falls der Tausch und sein Rückweg auf beide Zeigerzweige wirken, erhalten sie den Gesamtfluss und hinterlassen keinen zusätzlichen Zeigerrekord. Ein Austauschobservable oder eine klassische Portumbenennung belegt die Verfügbarkeit dieses dynamischen Tauschs nicht. Beide Transferwege müssen auf dem gewählten Gitterbereich ausführbar sein.

### Summenzeiger bei fester Drift durch diskrete Phasenübereinstimmung

Erkundung. Auf dem ganzzahligen Flussgitter liefert ein kontrollierter Transfer $(n,r)\mapsto(n+1,r-1)$ mit Rücktransfer und gleicher Vorwärtsdrift beider Zweige nach konstanter Phasenkorrektur den Faktor $\exp[-2it(an-br)]$ für $Q=an^2+br^2$, $a,b>0$. Schreibe $an-br=a(n+r)-(a+b)r$. Bei $t(a+b)=\pi k$ mit ganzzahligem $k$ ist der zweite Term in der Exponentialphase ein ganzzahliges Vielfaches von $2\pi$. Der Zeiger trägt dann exakt $\exp[-2\pi i k a(n+r)/(a+b)]$. Für das ganze Gitter ist diese Zeitbedingung auch notwendig, damit benachbarte Paare gleicher Summe denselben Zeigerfaktor haben. Der lineare Generator bleibt verschieden vom Summengenerator; die Übereinstimmung gilt für die endliche Phase.

Für $k=1$ und $a:b=1:23$ ergibt sich auf dem Bereich mit geradem Gesamtfluss $n+r=2j$ genau $\exp(-2\pi i j/12)$. Das Verhältnis ist ein Beispiel für einen Modellwert, keine native Vorhersage. Bei festem Verhältnis bestimmen die verfügbaren Resonanzzeiten, welche Charaktere erreichbar sind. Der Gesamtfluss bleibt beim Hin- und Rücktransfer erhalten. Die gemeinsame Vorwärtsdrift bleibt auf dem Flussregister. Für die beiden Vorzeichenpaare mit $n^2=r^2=1$ ist sie trotz ungleicher Koeffizienten identisch.

Bei einer Zeitabweichung $t=t_0+\varepsilon$ von einer Resonanzzeit $t_0$ unterscheiden sich die Zeigerphasen innerhalb einer Summenfaser zwischen zwei Paaren mit Referenzindexdifferenz $\Delta r$ um $2\varepsilon(a+b)\Delta r$ modulo $2\pi$. Für einen anfangs gleichgewichteten binären Zeiger beträgt der Betrag ihres Überlapps $|\cos[\varepsilon(a+b)\Delta r]|$. Der Kandidat setzt kohärent kontrollierte Transfers, stabile Driftkoeffizienten und die ganzzahlige Flusskodierung voraus.

### Erreichbare Restklassen bei festem Driftverhältnis

Erkundung. Auf dem geraden Gesamtflussgitter ist die Resonanzphase bei $t(a+b)=\pi k$ gleich $\exp(-2\pi i k\eta j)$ mit $\eta=2a/(a+b)$ und $j=(n+r)/2$. Ist $\eta=p/q$ gekürzt, hat diese Phase die Ordnung $q/\gcd(k,q)$. Mehrere Resonanzabfragen können zusammen höchstens modulo $q$ unterscheiden, da alle bei $j$ und $j+q$ identisch sind. Für $a:b=u:v$ in kleinsten positiven ganzen Zahlen ist $q=(u+v)/\gcd(2,u+v)$. Bei gleichen Driftgewichten gilt $q=1$, und die Phase ist auf dem geraden Gitter für alle Resonanzzeiten trivial. Ein Charakter von Ordnung zwölf ist genau dann durch eine Resonanzzeit erreichbar, wenn zwölf den maximalen Modulus $q$ teilt.

Für irrationales $\eta$ hat die Eigenphase nur bei $j=0$ den Wert eins. Das allein ergibt keinen exakten Nullzeiger mit endlich vielen kohärenten Abfragen auf dem unbeschränkten Gitter. Die Wahrscheinlichkeiten eines festen endlichen Protokolls, das nur die kontrollierten Resonanzphasen als Indexzugriff verwendet, hängen stetig von $z=\exp(-2\pi i\eta j)$ ab, da jede Abfrage eine feste Potenz von $z$ beiträgt. Nichtnull-Indizes liefern Phasen beliebig nahe bei eins, wie die Schubfachapproximation für die Vielfachen von $\eta$ zeigt. Sichere Nullakzeptanz erzwingt daher Nichtnull-Indizes mit Akzeptanz beliebig nahe bei eins. Auf einem endlichen Flussbereich gilt dieses Stetigkeitsargument nicht als Ausschluss. Die Driftkoeffizienten dieses Zeigermodells sind von den Steifigkeiten der früheren Flächenkalibrierung getrennt, solange keine dynamische Identifikation hergeleitet ist.

### Drift aus der ursprünglichen Winkelbindung

Erkundung. Im ursprünglichen Torusmodell mit erhaltenem $n=2m_1+m_2$ ergibt quadratische Ergänzung mit $D=c_1+4c_2$ und $\gamma=2c_2/D$

$$
\widehat H_n =
\frac{a_M^2D}{2}(\widehat m-\gamma n)^2
+\frac{a_M^2c_1c_2}{2D}n^2+V(\phi).
$$

Der explizite quadratische Anteil liefert bei klassischer Minimierung über den relativen Fluss die Sektordrift mit Koeffizient $a_M^2c_1c_2/(2\hbar D)$ in Frequenzeinheiten. Zwei identische reduzierte Kopien haben gleiche Driftgewichte. Auf dem geraden Gesamtflussgitter ist ihr Resonanzzeiger daher trivial. Eine absichtlich ungleiche Referenzkopie wäre eine zusätzliche Modellannahme.

Im vollen quantisierten Modell bleibt außerdem der relative Term $(\widehat m-\gamma n)^2$ erhalten. Eine reelle Verschiebung von $\widehat m$ kann auf periodischen Zuständen nur dann durch eine periodische Multiplikation $e^{ik\phi}$ entfernt werden, wenn die Verschiebung ganzzahlig ist. Da $0<\gamma<1/2$, kann ein Schritt $n\mapsto n+1$ den relativen Term nicht auf diese Weise identifizieren. Für gleiche Steifigkeiten ist $\gamma=2/5$: Erst ein Schritt um fünf Einheiten ändert $\gamma n$ um eine ganze Zahl. Allgemein ist bei $\gamma q\in\mathbb Z$ der relative Hamiltonterm bei $n+q$ durch einen ganzzahligen Fourier-Shift zum relativen Term bei $n$ unitär äquivalent; das Multiplikationspotential $V(\phi)$ kommutiert mit diesem Shift. Die skalare Sektordrift bleibt dabei bestehen. Ein solcher größerer Transfer ist eine Kandidatenoperation und müsste physikalisch zugelassen werden.

Die volle Randdynamik rechtfertigt daher den reinen quadratischen Zeigeransatz nicht unmittelbar. Der Ansatz benötigt entweder eine reduzierte Dynamik mit unabhängig begründeter Asymmetrie oder eine Transferabbildung, die die relative Winkelmode kontrolliert mitführt. Die ganzzahlige Bedingung bezeichnet einen exakten Weg über Fourier-Shifts, keinen Ausschluss beliebiger Sektorintertwiner.

### Winkelharmonische für den exakten Fünfertransfer

Erkundung. Bei gleichen Steifigkeiten verlangt der Schritt $\Delta n=5$ die relative Fouriertranslation $\Delta m=2$. Aus $m=m_1$ und $n=2m_1+m_2$ folgt $(\Delta m_1,\Delta m_2)=(2,1)$. Der Multiplikator $e^{i(2\theta_1+\theta_2)}$ implementiert genau diese Verschiebung. Für eine Referenzkopie mit Winkeln $\vartheta_1,\vartheta_2$ trägt

$$
B=e^{i[2(\theta_1-\vartheta_1)+(\theta_2-\vartheta_2)]}
$$

fünf Einheiten des erhaltenen Flusses vom Referenzkanal zum Rand. Der Gesamtfluss bleibt erhalten, und die relativen Hamiltonterme beider Kopien werden exakt mitgeführt. Allgemeiner gilt für einen Schritt $q$ mit $\gamma q=p\in\mathbb Z$ das Windungspaar $(p,q-2p)$.

Das vorhandene Bindungspotential hängt nur von $\theta_1-2\theta_2$ ab. Seine Fourierkomponenten verschieben die lokalen Modenzahlen entlang $(1,-2)$ und erhalten den Fluss jeder Kopie einzeln. Es liefert die neue kopienübergreifende Harmonische daher nicht. Eine reelle Kopplung proportional zu $B+B^\dagger$ ist mit der Gesamtflusssymmetrie vereinbar, erzeugt aber im Allgemeinen eine Überlagerung mehrerer Transfers. Der einzelne gerichtete Shift $B$, den der Zeigeraufbau verlangt, müsste als kontrollierte Operation eigens realisiert werden. Dies trennt Symmetrieverträglichkeit, Kopplungsterm und ausführbares Messinstrument.

### Gerichteter Fünfertransfer durch ein Hilfsdoublet

Erkundung. Sei $B$ der unitäre Fünfertransfer auf dem vollen Flussgitter. Auf einem Hilfsdoublet setze $K=B\otimes|1\rangle\langle0|+B^\dagger\otimes|0\rangle\langle1|$. Dieser Term ist hermitesch und erfüllt $K^2=I$. Er erhält den Gesamtfluss der beiden Randkopien. Ein idealer Puls $\exp(-i\pi K/2)=-iK$ führt bei vorbereitetem Hilfszustand null genau den gerichteten Transfer $B$ aus und setzt das Doublet auf eins. Ein zweiter identischer Puls nach der Drift führt $B^\dagger$ aus und setzt das Doublet zurück. Die beiden Pulse ergeben zusätzlich eine konstante Phase minus eins im aktiven Zweig, die am Zeiger korrigiert werden kann.

Ein separates Zeigerqubit kann beide Pulse gemeinsam steuern. Das Hilfsdoublet bleibt dann im unverschobenen Zweig bei null und kehrt im verschobenen Zweig nach dem Rückpuls dorthin zurück. Die Konstruktion setzt einen Puls mit isoliertem $K$ oder eine gleichwertige Kontrolle voraus. Bei gleichzeitig wirksamer quadratischer Drift haben die gekoppelten Paare im Allgemeinen verschiedene Energieabstände; die ideale Pulsformel gilt dann nicht unmittelbar. Die vorhandene reelle Kosinuskopplung allein liefert das bedingte Flip-Flop nicht.

### Transferpuls bei gleichzeitig laufender Drift

Erkundung. Verwende Frequenzeinheiten und betrachte den vom Hilfsdoublet gekoppelten Zweizustandsblock für einen Transfer um $q$. Bei Drift $Q=an^2+br^2$ und einstellbarer Hilfsfrequenz $\omega$ ist die Verstimmung

$$
\Delta(n,r)=2q(an-br)+q^2(a+b)-\omega.
$$

Nach Abzug der mittleren Energie lautet der Blockhamiltonian bis auf die Wahl der Z-Achse $gX+\Delta Z/2$. Ein konstanter Rechteckpuls der Dauer $\tau$ überträgt mit Wahrscheinlichkeit

$$
P(\tau)=\frac{g^2}{g^2+\Delta^2/4}\sin^2\!\left(\tau\sqrt{g^2+\Delta^2/4}\right).
$$

Vollständiger Transfer verlangt bei endlichem $g\ne0$ daher $\Delta=0$. Für die gegenläufigen Paare $(+1,-1)$ und $(-1,+1)$ unterscheiden sich die Verstimmungen um $4q(a+b)$. Keine gemeinsame Hilfsfrequenz kann beide gleichzeitig resonant machen. Die mittige Wahl $\omega=q^2(a+b)$ minimiert die größte absolute Verstimmung und ergibt $\Delta=\pm2q(a+b)$. In beiden Blöcken ist dann dieselbe optimale Pulsdauer möglich, aber die maximale gemeinsame Transferwahrscheinlichkeit ist $g^2/[g^2+q^2(a+b)^2]$. Das Ergebnis gilt für den einzelnen konstanten Puls, die quadratische Sektordrift und ideale Mitführung der relativen Mode. Geformte Pulse oder abschaltbare Drift liegen außerhalb des Ausschlusses. Gleiche Transferwahrscheinlichkeiten allein prüfen noch keine Übereinstimmung der komplexen Amplituden des vollständigen Zeigerprotokolls.

### Zwei Rechteckpulse für entgegengesetzte Verstimmungen

Erkundung. Bei mittiger Abstimmung seien die beiden Nullsektorblöcke durch $s=\pm1$ und Verstimmung $\Delta=2sd$ mit $d=q(a+b)>0$ bezeichnet. Ziehe je Block die mittlere Energie ab. Wähle in zwei aufeinanderfolgenden Abschnitten die Kopplung $+d$ und dann $-d$, jeweils für $\tau=\pi/(2\sqrt2 d)$. Die zentrierten Hamiltonoperatoren lauten $d(X+sZ)$ und $d(-X+sZ)$. Die normierten Rotationsachsen stehen senkrecht aufeinander. Das Produkt in zeitlicher Reihenfolge ist

$$
\exp[-i\tau d(-X+sZ)]\exp[-i\tau d(X+sZ)]=-isY.
$$

Somit erfolgt in beiden Blöcken vollständiger Transfer trotz laufender Drift. Die Transferamplitude trägt ein sektorabhängiges Vorzeichen. Wird dieselbe Doppelfolge nach einer Wartezeit als Rückpuls benutzt, multiplizieren sich ihre beiden zentrierten Flip-Amplituden zu $-1$ in beiden Blöcken. Die während der Pulse akkumulierten skalaren Phasen der mittleren Blockenergien müssen bei der vollständigen Zeigerrechnung dennoch mitgeführt werden. Die Konstruktion gilt für das genau abgestimmte Verstimmungspaar und setzt eine kontrollierte Vorzeichenumkehr der Kopplung voraus. Sie liefert keinen einheitlichen Puls für alle Flusssektoren und keinen Nachweis nativer Pulskontrolle.

### Vollständige Phasenbilanz des Doppelpulses

Erkundung. Sei $E_s$ die Energie des unverschobenen Zustands und $E_s+\Delta_s$ die des verschobenen Zustands einschließlich Hilfsfrequenz, mit $\Delta_s=2sd$. Jede Doppelfolge dauert $2\tau$ und trägt neben ihrem zentrierten Flip den Faktor $\exp[-2i\tau(E_s+\Delta_s/2)]$. Nach zwei Doppelfolgen und einer Wartezeit $T$ im verschobenen Zustand beträgt die Phase relativ zum unverschobenen Zweig, der dieselbe Gesamtzeit $4\tau+T$ driftet,

$$
-\exp[-i\Delta_s(T+2\tau)].
$$

Das Minuszeichen ist für beide Blöcke gleich. Ihre Zeigerphasen stimmen genau dann überein, wenn $4d(T+2\tau)=2\pi k$ für ganzzahliges $k$. Mit $\tau=\pi/(2\sqrt2 d)$ ist die kürzeste nichtnegative Wartezeit $T=\pi(1-1/\sqrt2)/d$ ($k=2$). Dann ist die relative Phase in beiden Blöcken minus eins und kann gemeinsam korrigiert werden. Die unverschobenen Energien sind für die beiden gegenläufigen Paare im quadratischen Modell gleich. Damit bleibt auch nach der gemeinsamen Drift ihre relative Phase unverändert. Der Befund betrifft genau diese beiden abgestimmten Blöcke. Eine Trennung von Null- und Nichtnullsektoren durch dieselbe Pulsfolge ist damit noch nicht geprüft.

### Nullselektion des Doppelpulses auf vier Vorzeichenpaaren

Erkundung. Bei $a=b$ haben die gleichgerichteten Paare nach mittiger Abstimmung $\Delta=0$. Die zwei entgegengesetzten Pulshamiltonoperatoren sind dann $+gX$ und $-gX$. Jede Doppelfolge ist exakt die Identität; die Wartezeit lässt den unverschobenen Zustand in beiden Zweigen gleich driften. Die relative Zeigerphase ist daher $+1$. Die gegenläufigen Paare liefern nach der vorigen Rechnung $-1$. Ein X-Zeiger selektiert damit die Nullflussfaser innerhalb der vier Vorzeichenpaare exakt und setzt das Hilfsdoublet zurück. Das steht mit der trivialen Resonanzphase symmetrischer Driften in Einklang: Hier unterscheidet die Wirkung der endlichen Transferpulse die Verstimmungsblöcke.

Die numerische Erkundung `python notes/research/qam_flux_double_pulse.py` berechnet die komplexen Blockamplituden. Bei $a:b=1:23$ akzeptiert derselbe für den Nullsektor abgestimmte Puls gleichgerichtete Paare mit Wahrscheinlichkeit rund $0{,}932730$. Die Transferleckage im aktiven Zweig ist dabei rund $0{,}000072$. Eine kleine Leckage garantiert somit keine gute Selektion. Die exakte symmetrische Auswahl ist für die vier Eingaben gezeigt, nicht für das volle Flussgitter. Die native Realisierung der Kopplung bleibt offen.

### Gleiche Verstimmung bei verschiedenem Gesamtfluss

Erkundung. Im Transferblock hängt die relative Dynamik nach Abzug der unverschobenen Drift nur von $an-br$ ab. Das gilt auch für zeitabhängige, in allen Flussblöcken gleich gesteuerte Kopplung und Hilfsfrequenz, solange dieselben zwei Zustände pro Block gekoppelt bleiben. Damit haben zwei Eingaben mit demselben $an-br$ denselben Zeigereffekt und dieselbe Rückkehrwahrscheinlichkeit des Hilfsdoubletts. Die gemeinsame Flussphase kann zwischen den Eingaben verschieden sein, geht aber in diese Zeigerstatistik nicht ein.

Bei symmetrischer Drift haben $(1,-1)$ und $(2,0)$ dieselbe Differenz und damit dieselbe Verstimmung. Der Doppelpuls akzeptiert beide sicher, obwohl ihre Gesamtflüsse null und zwei sind. Die exakte Auswahl auf dem Vorzeichendoublet funktioniert, weil dort die Differenzwerte der Null- und Nichtnullpaare disjunkt sind. Auf dem unbeschränkten Gitter kann kein Pulsprofil innerhalb der genannten Zweizustandsblöcke diese Kollision beheben.

Allgemeiner bleibt bei gekürztem rationalem Driftverhältnis $a:b=u:v$ der Ausdruck $an-br$ unter $(n,r)\mapsto(n+v,r+u)$ invariant, obwohl der Gesamtfluss um $u+v$ wächst. Auf dem geraden Gesamtflussgitter genügt bei ungeradem $u+v$ die doppelte Verschiebung. Ein zweiter Zugriff mit anderer Gewichtung könnte die Kollision auflösen. Auf einem begrenzten Gitter lässt sich vor der Pulssuche prüfen, ob die erlaubten Null- und Nichtnullpaare überhaupt disjunkte Verstimmungsmengen besitzen.

### Selektiver Transfer bei getrennten Verstimmungen

Erkundung. Betrachte endlich viele verschiedene Verstimmungen $\Delta_1,\ldots,\Delta_M$ und setze nach Abzug der Blockspuren $D=\bigoplus_j \Delta_j Z/2$. Nehme zwei unabhängig steuerbare Kopplungsquadraturen $X_\Sigma=\bigoplus_j X$ und $Y_\Sigma=\bigoplus_j Y$ an. Kommutatoren mit $D$ erzeugen die beiden transversalen Achsen mit Gewichten $\Delta_j^k$ für alle $k\ge0$: Ein Kommutator erhöht den Grad um eins und vertauscht die transversale Achse bis auf Vorzeichen und Normierung. Linearkombinationen mit den Lagrange-Polynomen der verschiedenen Verstimmungen isolieren damit $X$ und $Y$ in jedem Block. Ihr Kommutator liefert das lokale $Z$. Die erzeugte spurfreie Lie-Algebra ist also die direkte Summe der einzelnen $\mathfrak{su}(2)$.

Im idealen Lie-Kontrollmodell mit verfügbaren inversen Generatorfolgen kann man deshalb einen Transfer in den Nullblöcken und die Identität in den anderen Blöcken beliebig genau synthetisieren. Für einen binären Zeiger wird der Hilfsflip auf ein gemeinsames Bit kopiert und die Pulsfolge rückgängig gemacht. Dadurch verschwinden auch die während der Vorwärtsfolge angesammelten Blockphasen, sofern der vollständige Puls propagator einschließlich seiner skalaren Phasen invertiert wird. Die Algebraanalyse liefert keine Pulsdauer, keine Fehlertoleranz und keinen Nachweis der nativen Inversen.

Als minimaler Kandidat trennt $a:b=1:2$ auf den Vorzeichenpaaren plus dem Gegenbeispiel $(2,0)$ die Nullverstimmungslabels $an-br=\pm3$ von den übrigen Labels $-1,1,2$. Die symmetrische Drift tut dies nicht. Auf dem unbeschränkten Gitter bleiben bei $1:2$ die rationalen Verstimmungskollisionen bestehen. Der Kandidat belegt eine mögliche endliche Aufgabenstellung für die Pulssuche, kein universelles Driftverhältnis.

### Qiskit-Selektor für die getrennten Verstimmungslabels

Erkundung. `python -m qam.examples.detuning_selector_qiskit` kodiert $n-2r$ modulo acht in einem Quantenregister. Kontrollierte Phasen und inverse Fouriertransformation schreiben den Rest in ein Arbeitsregister. Ein Nullflussbit markiert die beiden Reste drei und fünf gemeinsam; die inverse Berechnung setzt das Arbeitsregister zurück. Auf den fünf untersuchten Flusspaaren werden die beiden Nullpaare sicher akzeptiert und alle drei anderen sicher abgewiesen. Der Zustandsvektorabgleich bestätigt auch unveränderte relative Amplituden der gleichgewichteten Nullüberlagerung. Die Schaltung setzt kohärenten Zugriff auf das Verstimmungslabel voraus. Sie synthetisiert keine physikalische Pulsfolge aus dem Transferhamiltonian. Auf einem größeren Gitter können weitere Flusspaare dieselben Verstimmungsreste haben.

### Numerische Pulsfolge direkt im Transferblock

Erkundung. `python notes/research/qam_flux_selective_pulse.py` optimiert eine gemeinsame Folge von 16 Abschnitten mit Dauer $0{,}5$ in dimensionslosen Einheiten. Die beiden Quadraturen sind je Abschnitt auf $[-4,4]$ beschränkt. Für ein Label $\ell$ wirkt $\ell Z+xX+yY$. Die Verstimmung geht nur als Drift in die Propagation ein. Das Optimierungsziel unterdrückt die unerwünschte komplexe Amplitude auf den fünf Blöcken. Im berechneten Lauf sind die Flip-Wahrscheinlichkeiten auf zwölf Dezimalstellen eins für $\ell=\pm3$ und null für $\ell=-1,1,2$. Die größte Abweichung der ausgegebenen Wahrscheinlichkeiten von ihren Sollwerten lag bei $8{,}88\cdot10^{-16}$ und ist ein Gleitkommawert.

Die gemeinsame Folge belegt numerisch einen selektiven Hilfsflip auf diesen fünf Blöcken. Für einen kohärenten Zeiger muss man den Flip noch auf ein Ergebnisbit kopieren und den vollständigen Propagator invertieren. Der Lauf prüft weder die native Realisierbarkeit dieser Inversion noch Robustheit gegen Verstimmungsfehler, andere Blöcke oder Beschränkungen der Umschaltgeschwindigkeit.

### Vollständiger selektiver Zeiger und Verstimmungsfehler

Erkundung. Das Skript `qam_flux_selective_pulse.py` berechnet nach Puls, Kopieren des Hilfsbits und exakter mathematischer Inversion für jeden Block $U_\ell$ die Zeigerzweige $\langle p|U_\ell|0\rangle U_\ell^\dagger|p\rangle$ für $p=0,1$. Der größte Zustandsvektorabstand zum idealen Zeiger mit zurückgesetztem Hilfsbit beträgt im Lauf $1{,}11\cdot10^{-14}$. Der Vergleich erfolgt ohne separate Phasenanpassung der Blöcke und erfasst damit auch die relative Phase bei Überlagerungen. Blockweise skalare Phasen heben sich mit dem vollständigen Inversen auf.

Ohne erneute Optimierung führen gemeinsame positive Verstimmungsoffsets von $0{,}01$, $0{,}05$ und $0{,}1$ zu maximalen Fehlklassifikationswahrscheinlichkeiten von rund $0{,}00348$, $0{,}0857$ und $0{,}317$. Dabei wird das jeweils exakte mathematische Inverse des verschobenen Propagators angenommen. Diese Werte prüfen einzelne Offsets, keinen kontinuierlichen Toleranzbereich und keinen unabhängigen Fehler im Rückpuls. Die native Realisierung des Inversen bleibt offen.

### Robuste Pulsfolge über mehrere Verstimmungsoffsets

Erkundung. Die Variante im Skript `qam_flux_selective_pulse.py` verwendet 24 statt 16 Abschnitte gleicher Dauer und dieselben Quadraturgrenzen. Die Optimierung unterdrückt die falsche Amplitude gleichzeitig bei den gemeinsamen Offsets $-0{,}05,0,+0{,}05$ auf allen fünf Blöcken. Auf den 98 bei der Optimierung nicht verwendeten Zwischenpunkten eines 101-Punkte-Gitters ist der größte numerische Klassifikationsfehler rund $1{,}68\cdot10^{-6}$, gegenüber $0{,}0824$ für die nominelle Folge. Einschließlich der drei Trainingspunkte bleibt das gesampelte Maximum gleich. Die längere Pulsdauer ist Teil der Änderung. Der Vergleich isoliert daher den Beitrag der Mehrpunktoptimierung nicht von dem der zusätzlichen Abschnitte. Die Stichprobe belegt weder eine kontinuierliche Fehlerschranke noch Robustheit gegen unabhängige Pulsfehler oder eine physikalische Realisierung des inversen Propagators.

### Interpolation der Fehlamplitude über das ganze Offsetintervall

Erkundung. Für die fest gewählte Pulsfolge gilt $H_\epsilon(t)=H_0(t)+\epsilon Z$. Zweimalige Ableitung der unitären Propagation nach $\epsilon$ ergibt zwei zeitgeordnete Einfügungen von $Z$ in die Evolution. Da alle Teilpropagatoren unitär sind und $\|Z\|=1$, ist $\|\partial_\epsilon^2 U_\epsilon(T)\|\le 2\int_0^T ds\int_0^s du=T^2$. Das gilt auch für jede komplexe Fehlamplitude. Zwischen zwei Gitterpunkten mit Abstand $h$ weicht die Amplitude von ihrem linearen Interpolanten daher um höchstens $T^2 h^2/8$ ab, per Integralform des Interpolationsfehlers. Die interpolierte Amplitude bleibt betragsmäßig unter dem Maximum der beiden Stützwerte.

Für $T=12$, $h=0{,}001$ und numerischem Stützstellenmaximum der Fehlwahrscheinlichkeit $1{,}6797\cdot10^{-6}$ ergibt sich über $[-0{,}05,0{,}05]$ die Obergrenze rund $1{,}727\cdot10^{-6}$. Die Ableitungs- und Interpolationsschranke ist analytisch. Die Stützwerte stammen aus Gleitkomma ohne Intervallzertifizierung; eine rigorose numerische Obergrenze erfordert zertifizierte Stützwerte. Die Aussage betrifft die Klassifikation bei gemeinsamem statischem Offset im idealen Blockmodell.

### Intervallabgleich der gespeicherten Pulsfolge

Die 24 Pulsabschnitte sind als Dezimalwerte in `qam_flux_robust_controls.txt` fixiert. Der unabhängige Nachlauf `python notes/research/qam_flux_verify_interval.py` schließt alle 505 Stützstellenamplituden mit der Intervallarithmetik von mpmath ein. Alle oberen Betragsgrenzen liegen unter $0{,}001297$. Zusammen mit der analytischen Interpolationsschranke ergibt sich für die gespeicherte Folge auf dem gesamten statischen Offsetintervall $[-0{,}05,0{,}05]$ eine Fehlklassifikationswahrscheinlichkeit unter $1{,}73\cdot10^{-6}$. Der Nachlauf braucht weder den Optimierer noch Qiskit. Die Schranke betrifft die fünf Blöcke des idealen Hamiltonmodells und setzt bei einem vollständigen Zeiger weiterhin den inversen Propagator voraus.

### Rückrechnung durch Echo und gemeinsame Wartezeit

Erkundung. Für den zentrierten Transferblock $H_\ell(t)=\ell Z+x(t)X+y(t)Y$ invertiert die folgende Sequenz den Propagator exakt: ein blockunabhängiger X-Flip, die zeitlich umgekehrte Pulsfolge mit Quadraturen $(-x,+y)$, dann ein zweiter X-Flip. Denn $X[\ell Z-xX+yY]X=-H_\ell$. Dies funktioniert auch bei einem gemeinsamen statischen Offset. Ein unselektiver X-Flip ist dabei eine zusätzliche Steuerressource, die der selektive Puls allein nicht bereitstellt.

Relativ zur unverschobenen Grundenergie hat der volle Block die Form $\ell I+H_\ell$. Nach Vorwärtspuls, Kopieren und Echo-Rückpuls verbleibt deshalb der gemeinsame skalare Faktor $e^{-2i\ell T}$ bei Pulsdauer $T=12$, obwohl das Hilfsbit zentriert zurückgerechnet ist. Eine kompensierende Phase lässt sich im idealisierten Modell durch eine Wartezeit $W$ im verschobenen Hilfszustand gewinnen: vor der Messsequenz X anwenden, $W$ vorwärts warten und X zurück anwenden. Der initiale Hilfszustand null erhält dadurch relativ zur Grundenergie den Faktor $e^{-2i\ell W}$. Mit $W=4\pi-12>0$ ergibt die Gesamtphase $e^{-8\pi i\ell}$. Für die ganzzahligen Labels ist sie eins; bei einem gemeinsamen Offset ist sie in allen Blöcken gleich. Die unverschobene Grunddrift bleibt als gemeinsamer Entwicklungsschritt relativ zum Leerlauf. Die Rechnung behandelt die globalen X-Flips als ideal und ohne zusätzliche Dauer. Eine endliche Implementierung muss ihre Fehler und Phasen gesondert bilanzieren.

### Endlicher gemeinsamer Hilfsflip

Erkundung. `python notes/research/qam_flux_common_flip.py` optimiert 32 Pulsabschnitte der Dauer $0{,}5$ mit denselben Quadraturgrenzen wie der selektive Puls. Ziel ist in jedem Block die volle spurfreie Gattermatrix $-iX$, ohne separate Phasenanpassung. Die Optimierung nutzt die Offsets $-0{,}05,0,+0{,}05$. Auf dem 101-Punkte-Gitter für alle fünf Labels ergibt sich ein maximaler Operatornormfehler von $0{,}00156182$, bei Offset null höchstens $0{,}00136291$.

Für vier solche Hilfsflips ist der zusätzliche Fehler im vollständigen Zustandsvektor auf den geprüften Punkten durch die Teleskopsumme der einzelnen unitären Gatterfehler auf $4\cdot0{,}00156182$ begrenzt, wenn die skalaren Blockphasen exakt mitgeführt werden. Die vier Flip-Dauern $F=16$ ergänzen die skalare Phase relativ zum Leerlauf um $-4\ell F$. Die ideale Wartezeitrechnung verwendet daher $T+2F+W\in\pi\mathbb Z$, zum Beispiel $W=15\pi-44>0$. Das resultierende Protokoll wurde hier noch nicht als Ganzes simuliert. Die Gatterfehler sind numerische Stichproben, und die Pulse setzen die modellierten Quadraturen voraus.

### Vollständiger Zeiger mit endlichen Echo-Pulsen

Erkundung. `python notes/research/qam_flux_common_flip.py` verbindet den gespeicherten selektiven Puls mit vier endlichen gemeinsamen Hilfsflips, der Wartezeit $15\pi-44$, dem Kopieren des Hilfsbits und dem gespiegelten Echo. Beide Zeigerzweige werden als komplexe Amplituden berechnet. Der Vergleich entfernt die unverschobene Leerlaufentwicklung und eine bei gemeinsamem Offset für alle Blöcke gleiche Phase. Auf fünf Verstimmungsblöcken und 101 Offsets zwischen $-0{,}05$ und $+0{,}05$ betragen die maximalen numerischen Fehler rund $3{,}60\cdot10^{-6}$ für die Klassifikation, $6{,}71\cdot10^{-6}$ für ein am Ende angeregtes Hilfsdoublet und $0{,}003294$ für den vollständigen Zustandsvektorabstand. Der letzte Wert prüft auch sektorabhängige Phasenfehler. Das Ergebnis ist eine Stichprobe mit endlichen modellierten Pulsen, keine Intervallzertifizierung dieses Gesamtprotokolls. Das binäre Kopiergatter bleibt idealisiert.

### Interpolation des vollständigen Echo-Zeigers

Erkundung. Im leerlaufbereinigten Modell ist die Gesamtdauer $88+W$ mit $W=15\pi-44$. Der skalare Phasenfaktor nach Abzug der gemeinsamen Offsetphase hat eine Ableitungsnorm von $W$. Zusammen mit den zentrierten Propagatoren und dem offsetunabhängigen Kopiergatter ergibt sich ein Ableitungsbudget $88+2W=30\pi$. Die zweite Offsetableitung des gesamten Ausgangsvektors ist daher in Norm höchstens $(30\pi)^2$. Dieselbe Schranke gilt für seine Projektionen auf falsche Zeigerwerte oder ein angeregtes Hilfsdoublett.

Bei Gitterabstand $h=0{,}001$ beträgt die Interpolationszugabe zur Norm höchstens $(30\pi)^2h^2/8\approx0{,}001111$. Mit den numerischen Stützwerten ergibt das über $[-0{,}05,0{,}05]$ rund $0{,}004405$ für den Zustandsvektorabstand, $9{,}05\cdot10^{-6}$ für die Fehlklassifikation und $1{,}37\cdot10^{-5}$ für die Restanregung. Für die Wahrscheinlichkeiten wird zuerst die projizierte Amplitudennorm interpoliert und erst danach quadriert. Der Interpolationsschritt ist analytisch. Für eine zertifizierte Gesamtschranke müssen die Stützwerte der endlichen Echo-Pulse noch eingeschlossen werden.

### Intervallabgleich des vollständigen Echo-Zeigers

`python notes/research/qam_flux_verify_echo.py` verwendet die fixierten Dezimalkoeffizienten beider Pulsfolgen. Der Lauf schließt die komplexen Zweigamplituden für fünf Blöcke und 101 Offsets ein. Mit der analytischen Interpolation gelten auf dem gesamten statischen Offsetintervall $[-0{,}05,0{,}05]$ die Obergrenzen $0{,}004406$ für den leerlaufbereinigten Zustandsvektorabstand, $9{,}06\cdot10^{-6}$ für Fehlklassifikation und $1{,}371\cdot10^{-5}$ für Restanregung. Der Abgleich setzt das idealisierte binäre Kopiergatter und das gemeinsame statische Offsetmodell voraus. Er benötigt keine erneute Pulsoptimierung und keine native QAM-Implementierung.

### Kopieren auf das Zeigerbit bei laufender Drift

Erkundung. Im Hilfsdoublet sei $P_s=|s\rangle\langle s|$. Verwende einen Kopierpuls mit Hamiltonterm $gP_1\otimes(I-X_{\rm Z})$ während einer halben Kopierzeit, dann einen gemeinsamen Hilfsflip, danach denselben Puls mit $P_0$ während der zweiten Hälfte und schließlich einen Rückflip. Der Kopierterm kommutiert in jedem Abschnitt mit der diagonalen Blockdrift. Der Hilfszustand durchläuft in beiden Zweigen beide Energien für gleich lange Zeiten. Der Zeigerterm wirkt dagegen in beiden Hälften genau dann, wenn der ursprüngliche Hilfszustand eins war. Bei Gesamtkopierzeit $L=\pi/(2g)$ ist $\exp[-igL(I-X_{\rm Z})]=X_{\rm Z}$, einschließlich der Gatterphase.

Mit der Konvention $H_{\ell,\rm zentriert}=\ell Z$ und nach Abzug der unverschobenen Leerlaufentwicklung ergibt die Kopierzeit den gemeinsamen Blockfaktor $e^{i\ell L}$. Werden die beiden zusätzlichen Hilfsflips als Pulse mit Dauer $F$ und idealem zentrierten Gatter $-iX$ behandelt, kommt $-e^{2i\ell F}$ hinzu. Die Wartezeitbedingung des vollständigen Zeigers lautet dann $T+3F+W+L/2\in\pi\mathbb Z$. Das konstante Minuszeichen kann in der globalen Phase des Protokolls berücksichtigt werden. Die algebraische Konstruktion ersetzt das sofortige Kopiergatter durch zwei diagonale Kopplungen und zwei Hilfsflips. Sie setzt Zugriff auf beide komplementären Kopplungen voraus. Die vorhandenen numerisch approximierten Hilfsflips sind in dieser erweiterten Folge noch nicht simuliert oder intervallgeprüft.

### Simulation mit endlichem Kopierpuls

Erkundung. `python notes/research/qam_flux_finite_copy.py` verwendet die beiden gespeicherten Pulsfolgen, sechs endliche Hilfsflips und zwei komplementär gesteuerte Kopierhälften. In dimensionslosen Einheiten sind $g=1$, $L=\pi/2$ und $W=20\pi-60-L/2$. Auf fünf Verstimmungsblöcken und 101 statischen Offsets betragen die größten numerischen Fehler $4{,}396\cdot10^{-6}$ für Fehlklassifikation, $1{,}507\cdot10^{-5}$ für Restanregung und $0{,}003989$ für den vollständigen Zustandsvektorabstand. Gemeinsame Leerlauf- und Offsetphasen sind beim Zustandsvergleich abgezogen.

Das Ableitungsbudget ist nun $40\pi$, da die physikalische Dauer plus der Betrag des skalaren Phasenkoeffizienten $120+L+2W$ beträgt. Analytische Interpolation mit den numerischen Stützstellen ergibt für das gesamte Offsetintervall Schätzungen von $1{,}657\cdot10^{-5}$ für Fehlklassifikation und $3{,}429\cdot10^{-5}$ für Restanregung. Die Stützstellen des erweiterten Protokolls sind nicht intervallzertifiziert. Das Modell setzt die komplementären diagonalen Kopierkopplungen voraus.

### Intervallprüfung mit endlichem Kopierpuls

Die Rechnung `python notes/research/qam_flux_verify_finite_copy.py` schließt die vollständigen komplexen Ausgangsamplituden an allen 505 Stützstellen ein. Mit dem Ableitungsbudget $40\pi$ folgen für das gesamte statische Offsetintervall die Obergrenzen $0{,}005964$ für den Zustandsvektorabstand, $1{,}658\cdot10^{-5}$ für die Fehlklassifikation und $3{,}431\cdot10^{-5}$ für die Restanregung. Die Aussage gilt für die fünf Modellblöcke und setzt die beiden komplementären diagonalen Kopierkopplungen voraus.

### Komplementäre Kopierhälfte aus einer einzigen Kopplung

Erkundung. Setze $A=I-X_{\rm Z}$ auf dem Zeiger. Die zweite Kopierhälfte lässt sich aus derselben bedingten Kopplung wie die erste aufbauen, sofern ihr Vorzeichen umkehrbar ist und der Zeiger unabhängig um dieselbe Achse gedreht werden kann. Denn $P_0\otimes A=I\otimes A-P_1\otimes A$. Bei gleichzeitiger Anwendung der freien Zeigerrotation $+gA$ und der bedingten Kopplung $-gP_1\otimes A$ entsteht daher exakt die komplementäre Kopplung. Beide Summanden kommutieren auch mit der diagonalen Blockdrift. Die Dauer der Kopierhälfte und die Phasenbilanz bleiben bei gleichzeitiger Anwendung gleich. Die vorigen Fehlerschranken gelten deshalb im idealen Modell auch für diese Zerlegung.

Eine Vorzeichenumkehr der $X$-Komponente durch Zeigerkonjugation genügt allein nicht: Ein Zeiger-$Z$-Puls bildet $I-X_{\rm Z}$ auf $I+X_{\rm Z}$ ab, während für die Zerlegung $-I+X_{\rm Z}$ benötigt wird. Die Differenz ist ein bedingter skalarer Energieterm $2gP_1$. Er kann als zusätzliche Phase im Hilfsregister wirken und muss bei der kohärenten Rückrechnung mitgeführt werden. Die Konstruktion ersetzt zwei unabhängig angenommene bedingte Kopplungen durch eine vorzeichensteuerbare bedingte Kopplung und eine freie Zeigerrotation. Eine native Realisierung dieser Steuerung ist nicht hergeleitet.

### Kopierpuls mit ausschließlich positiver bedingter Kopplung

Erkundung. Setze $A=I-X_{\rm Z}$, $L=\pi/(2g)$ und $h=L/2$. Da $A$ die Eigenwerte null und zwei hat, ist $\exp(-4ighA)=I$. Somit realisieren $3h$ mit positiver Kopplung $gP_1\otimes A$ dieselbe Zeigeroperation wie $h$ mit negativer Kopplung. Während dieser $3h$ ergänzt eine freie Zeigerrotation mit Stärke $g/3$ genau den Winkel $gh$ und synthetisiert damit die komplementäre Kopierhälfte. Beide Beiträge kommutieren mit der Drift.

Damit beide Hilfszustände gleich lange auf den beiden Driftenergien liegen, wird auch die erste Hälfte auf $3h$ verlängert: $h$ bedingter Kopierpuls und $2h$ freie Drift. Die Kopierzeit steigt insgesamt von $L$ auf $3L$. Die zwei Hilfsflips bleiben unverändert. Die Wartezeitbedingung wird $T+3F+W+3L/2\in\pi\mathbb Z$. Für die bisherigen Werte $T=12$, $F=16$, $g=1$ ist $W=20\pi-60-3\pi/4>0$. Die algebraische Gleichheit der bedingten Zeigerrotationen gilt exakt bei den angegebenen Pulsflächen. Die längere Drift zwischen den numerisch approximierten Hilfsflips ändert das Fehlermodell. Die bisherigen Intervallschranken werden daher nicht auf diese Variante übertragen. Der Ansatz verlangt weiterhin eine abschaltbare positive bedingte Kopplung und eine freie Zeigerrotation.

### Intervallprüfung der ausschließlich positiven Kopierkopplung

Der Aufruf `python notes/research/qam_flux_verify_finite_copy.py --positive-only` schließt die 505 Stützwerte für die verlängerte Kopierfolge ein. Da beide Kopierhälften dieselbe Zeigerwirkung wie zuvor haben und nun gleich lange unter der Drift laufen, genügt im Blockpropagator der Ersatz der Kopierzeit durch $3L$. Die verkürzte Wartezeit erfüllt weiterhin $120+3L+2W=40\pi$, sodass das Ableitungsbudget gleich bleibt. Auf dem gesamten Offsetintervall betragen die aufgerundeten Obergrenzen $0{,}005357$ für den Zustandsvektorabstand, $1{,}091\cdot10^{-5}$ für die Fehlklassifikation und $1{,}866\cdot10^{-5}$ für die Restanregung. Die Rechnung setzt exakte Kopierpulsflächen, eine frei steuerbare Zeigerrotation und den gemeinsamen statischen Offset voraus.

### Fehlerschranke für ungenaue Kopierpulsflächen

Erkundung. Halte die Abschnittsdauern und die statische Drift fest. Bezeichne die absoluten Fehler der integrierten Koeffizienten für den ersten bedingten Puls, den langen bedingten Puls und die freie Zeigerrotation mit $e_1,e_2,e_f$. Für jeden dieser drei Terme hat der zugehörige Generator Norm zwei, da $A=I-X_{\rm Z}$ die Eigenwerte null und zwei hat. Die Duhamel-Schranke und die Teleskopsumme der unitären Teiloperationen begrenzen daher den zusätzlichen Zustandsvektorfehler durch $B=2(e_1+e_2+e_f)$. Die Schranke gilt auch für beliebige Eingangssuperpositionen der fünf Blöcke, sofern die Störung blockdiagonal bleibt. Für eine Fehlerwahrscheinlichkeit wird erst $B$ zur jeweiligen zertifizierten projizierten Amplitudennorm addiert und danach quadriert.

Bei einem gemeinsamen relativen Fehlerbetrag höchstens $\eta$ haben die drei nominellen Flächen die Beträge $\pi/4,3\pi/4,\pi/4$. Damit gilt $B\le(5\pi/2)\eta$. Für $\eta=10^{-3}$ folgt aus der bisherigen Schranke für Fehlklassifikation $[\sqrt{1{,}091\cdot10^{-5}}+(5\pi/2)\eta]^2<1{,}25\cdot10^{-4}$. Dies ist eine konservative Obergrenze für Fehler in den Kopieramplituden. Änderungen der Pulslängen, zeitabhängige Verstimmung und Fehler der übrigen Pulse sind durch diese Erweiterung nicht abgedeckt.

### Unabhängige Blockoffsets und die relative Phase

Erkundung. Die Intervallrechnung umschließt jeden der fünf Blöcke einzeln für jeden Offset im Intervall. Ihre Schranken für Fehlklassifikation und Restanregung gelten deshalb auch bei unterschiedlichen statischen Offsets $\epsilon_\ell$ der Blöcke. Für kohärente Superpositionen muss dagegen die beim Zustandsvergleich abgezogene Phase wieder eingesetzt werden. Relativ zur unverschobenen Leerlaufentwicklung ist sie in der positiven Kopierfolge $e^{i40\pi\epsilon_\ell}$. Bei gemeinsamem Offset war sie global. Bei verschiedenen Offsets entsteht zwischen den beiden akzeptierten Blöcken eine relative Phase $\varphi=40\pi(\epsilon_{+3}-\epsilon_{-3})$.

Für eine gleichgewichtete kohärente Eingabe ist die ideale Wahrscheinlichkeit am positiven Austauschport nach erfolgreicher Nullauswahl dann $\cos^2(\varphi/2)$. Bereits eine Offsetdifferenz $0{,}025$ vertauscht den positiven und negativen Austauschport. Das Nullbit behält dabei seine Klassifikationsschranke. Mit den zertifizierten leerlaufbereinigten Zustandsfehlern $d<0{,}005357$ liegt bei dieser Differenz die tatsächliche bedingte Wahrscheinlichkeit des positiven Ports unter $d^2/(1-1{,}091\cdot10^{-5})<2{,}88\cdot10^{-5}$, sofern die Austauschmessung ideal ist. Hierzu wird die akzeptierte positive Komponente gegen die ideale, rein negative Austauschkomponente verglichen. Ein konstanter Offsetunterschied dreht die Phase kohärent; erst ein unbekannter oder fluktuierender Unterschied kann beim Mitteln die beobachtete Interferenz dämpfen. Die Rechnung betrifft die modellierten Blockoffsets und lässt physikalische Ursachen und Kalibrierbarkeit offen.

### Austausch-Echo gegen unterschiedliche statische Blockphasen

Erkundung. Beschränke den Aufbau auf die beiden gegenläufigen Nullzustände. In der leerlaufbereinigten Beschreibung sei ein idealer Zeigerlauf auf diesen Zuständen diagonal mit Faktoren $d_\pm=e^{i40\pi\epsilon_{\pm3}}$ und schreibe in beiden Fällen eine Eins. Zwischen zwei Läufen vertausche die beiden Nullzustände kohärent mit $S$ und mache den Tausch am Ende rückgängig. Jeder Eingang durchläuft beide Phasen genau einmal. Daher gilt $S^\dagger D S D=d_+d_- I$ für $D=\operatorname{diag}(d_+,d_-)$. Dies gilt für beliebige statische Blockoffsets im geprüften Intervall, sofern dieselben Offsetwerte bei beiden Läufen gelten. Zwei getrennte Zeigerbits halten beide Ausgänge fest. Würde dasselbe Bit zweimal per XOR beschrieben, wäre es am Ende gelöscht.

Mit frischen Hilfs- und Zeigerregistern im zweiten Lauf und idealem Austausch ergibt die Teleskopsumme aus der zertifizierten Einzellaufschranke $d<0{,}005357$ einen Zustandsvektorfehler unter $2d<0{,}010714$ relativ zum idealen gemeinsamen Phasenfaktor. Der unbereinigte physikalische Ablauf benötigt zusätzlich die Bilanz der Leerlaufentwicklung. Außerhalb der beiden Nullzustände kann der Austausch zu Verstimmungslabels führen, die nicht geprüft wurden. Das Echo setzt einen kohärenten Austausch und seinen inversen Rückweg voraus. Das r27-Austauschobservable weist diese dynamische Operation allein nicht nach.

### Zusammenführung: Modellschluss und native OP1-Brücke

Ziel ist eine aus der nativen QAM-Dynamik begründete T-Flächenauslesung. Der Modellschluss setzt dagegen den periodischen Randträger, die Flussgeneratoren und die gewählte Kalibrierung voraus. Auf diesem Träger erhält die Winkelbindung $J=2P_1+P_2$. Unter linearen orientierten Aggregaten bestimmt die Erhaltung die Gewichte $2:1$. Die Gleichheit mit der klassischen additiven Fläche auf der gebundenen Teilfläche bestimmt den positiven Faktor $v=(c_1+2c_2)/(c_1+4c_2)$. Die quantisierte Auslesung ist damit $v a_M|\hat n|$. Auf dem gleichen Träger hat die ursprüngliche additive Observable nur ganzzahlige Vielfache von $a_M$ im Spektrum. Insbesondere kann eine unitäre Konjugation der additiven Observable innerhalb des Zweimodensektors $n=1$ die gemischte Observable nicht erzeugen. Das Modell liefert $3a_M/5$ bei gleichen Steifigkeiten und den nominalen r10-Quotienten nur bei einer zusätzlich festgelegten Steifigkeitsasymmetrie.

Für den relationalen Kohärenztest seien Rand und Referenz zwei getrennte Flussregister. Setze $N=\hat n\otimes I+I\otimes\hat r$. Eine Präparation und Steuerung, die mit beiden lokalen Flüssen kommutiert, kann die relative Phase der gegenläufigen Paare nicht auslesen: Das betreffende Matrixelement jedes so erzeugten Effekts verschwindet. Ein gemeinsamer Swap $S|n,r\rangle=|r,n\rangle$ auf identischen Flussträgern kommutiert dagegen mit $N$ und tauscht im Null-Doublet die beiden Paare. Sein Partial-Swap $e^{-i\theta S}=\cos\theta I-i\sin\theta S$ realisiert bei $\theta=\pi/2$ den für das Echo benötigten Tausch bis auf globale Phase. Mit dem binären, intern kohärenten Nullselektor und zwei frischen Hilfsregistern entfernt das Echo die statische blockabhängige Phase relativ zum Leerlauf. Die zertifizierte Einzellaufschranke liefert im Null-Doublet den Abstand kleiner als $0{,}010714$ für idealen Swap. Der Nullselektor testet die kohärente gemeinsame Auslesung, während die T-Flächenausgabe zusätzlich das Betragslabel des Randflusses und die Kalibrierung $v$ benötigt.

Quellenabgleich: r28.2(c) verwendet einen Partial-Swap mit dem eigenen Tachyonbild und betrachtet die Kontraktion des Bloch-Vektors. r30.3 motiviert kohärenten Austausch über den Kompensator. Daraus folgt keine Identifikation der beiden dortigen Register mit unabhängigen gravitativen Randflussregistern. Ein hinreichender nativer Nachweis müsste eine QAM-Kodierung der Rand- und Referenzsektoren angeben, unter der der dortige Swap die Flussregister vertauscht, der Gesamtfluss erhalten bleibt und das gemeinsame Ausleseinstrument innerhalb der Nullfaser keinen lokalen Vorzeichenrekord hinterlässt. Unabhängig davon muss die T-Ausgabe mit der nativen T-Geometrie und ihrer Flächennormierung verbunden werden. Die bisher geprüften Quellen und Simulationen liefern diese Brücken nicht. OP1 bleibt offen. Weitere Optimierung desselben idealisierten Pulsmodells entscheidet diese Zuordnungen nicht.
