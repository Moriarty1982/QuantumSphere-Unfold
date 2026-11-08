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

### Zählnormierung und Selektor sind zwei getrennte OP1-Bedingungen

Erkundung nach dem Merge. In r63.1 wird derselbe dimensionslose Einpunkt-Flächenterm $a(j)=\sqrt{j(j+1)}$ in zwei Normierungsgleichungen verwendet. Der Unterschied liegt im zugelassenen Spinträger: volle Zählung mit Gewicht zwei gegenüber nur $j=1/2$ mit Gewicht zwei. Eine gemeinsame Skalierung aller Flächenwerte $a(j)\mapsto\lambda a(j)$ bei unverändertem Träger kann den numerischen Normierungsparameter ändern. Die neue Lösung ist exakt $\gamma_M/\lambda$, denn die Gleichung hängt nur vom Produkt $\gamma\lambda$ ab. Die einzelnen normierten Gewichte bleiben identisch und jeder zuvor zugelassene Spin behält positives Gewicht. Eine numerische Übereinstimmung des Normierungsparameters allein weist daher keinen Übergang zur Minimalspinzählung nach.

Die r63-Brücke lässt sich als Forderung an einen nativen Selektor formulieren. Auf einem Einpunktträger mit Casimir $C=J^2$ ist der erforderliche Effekt der Spektralprojektor $P_{1/2}=\mathbf1_{\{3/4\}}(C)$, bis auf eine Beschreibung, die dieselbe Zählung reproduziert. Ein interner invertierbarer Framewechsel, der $C$ erhält, transportiert die vorhandenen Spinsektoren, entfernt aber keinen davon. Selbst ein normerhaltender Wechsel auf einem vergrößerten Träger liefert die Einschränkung erst durch ein Ausleseinstrument, das höhere Spins verwirft oder aus dem zugänglichen Zählträger ausschließt. Das für die r63.1-Normierung benötigte Gewicht zwei auf dem verbleibenden Sektor ist zusätzlich zu prüfen. Mehrpunktbedingungen und die native Identifikation des T-Trägers folgen aus dieser Einpunktrechnung nicht.

Damit sind zwei zuvor zusammen diskutierte Modellschritte getrennt. Der gemischte Torusoperator kann eine kleinere Flächenstufe modellieren. Der kohärente Nullzeiger implementiert eine Auswahl nach Flusslabel. Um daraus r63 zu gewinnen, müsste eine Abbildung zeigen, dass der native T-Selektor gerade den Casimirwert $3/4$ mit der geforderten Multiplizität auswählt. In den geprüften Quellen ist diese Zuordnung noch offen.

### Minimalspin aus einer transversalen quadratischen Auslesung

Erkundung. Eine einzelne normierte Flusskomponente $J_z$ liefert das Label $m$. Die Werte $m=\pm1/2$ kommen in jedem halbzahligen Spinsektor vor. Jede Auslesung, die ausschließlich von $J_z$ abhängt, akzeptiert daher bei diesen Labels auch höhere Spins. Gemeinsame Vorzeichenparität oder Auswahl der beiden Vorzeichen allein behebt die Kollision nicht.

Ein hinreichender Einpunkt-Selektor ist die spektrale Auslesung der gemeinsamen transversalen Quadratsumme $B=J_x^2+J_y^2=J^2-J_z^2$. Ihr Eigenwert ist $j(j+1)-m^2\ge j$, mit Gleichheit bei $|m|=j$. Somit gilt $\mathbf1_{\{1/2\}}(B)=P_{1/2}$ auf dem gesamten Spinträger, einschließlich eines möglichen Spin-null-Sektors. Die beiden Minimalspinzustände tragen denselben Zeigerwert. In einer einzelnen Kopie des Spin-$1/2$-Irreps hat dieser Projektor Rang zwei. Bei zusätzlichen Kopien oder weiteren Horizontbedingungen muss das effektive Zählgewicht separat bestimmt werden.

Die gemeinsame Spektralmessung der Quadratsumme ist eine eigenständige Modelloperation. Getrennte Auslesungen der transversalen Komponenten mit nachträglicher Addition ergeben im Allgemeinen ein anderes Instrument. Die native Frage ist damit, ob der T-Übergang einen gemeinsamen quadratischen Flusseffekt oder ein dazu äquivalentes Instrument bereitstellt. Der bisherige skalare Torus-Flusszeiger allein reicht dazu nicht aus.

### Minimalspin durch zwei binäre Flussfilter

Erkundung. Wenn die gemeinsame Quadratsumme nicht direkt messbar ist, genügen im Einpunktmodell zwei ideale binäre Filter als Grenzverfahren. Setze $P_x=\mathbf1_{\{1/4\}}(J_x^2)$ und $P_y=\mathbf1_{\{1/4\}}(J_y^2)$. Ihr gemeinsamer Bildraum ist exakt der Spin-$1/2$-Sektor: Jeder Vektor im Schnitt erfüllt $(J_x^2+J_y^2)\psi=\psi/2$, und auf Spin $1/2$ sind beide Filter die Identität. Die Filter messen nur den jeweiligen Betragstest und speichern kein Vorzeichen.

Für einen normierten Zustand im Bild von $P_x$ innerhalb eines höheren halbzahligen Spins $j$ gilt $\langle J_y^2\rangle\ge j-1/4$ und $J_y^2\le j^2 I$. Folglich ist die Ablehnungswahrscheinlichkeit des $y$-Filters mindestens $(j-1/2)/(j^2-1/4)=1/(j+1/2)$. Nach einer anfänglichen $x$-Auswahl und $k$ erfolgreichen $y$-Abfragen mit erneuter $x$-Auswahl vor jeder weiteren Abfrage beträgt die gesamte Falschakzeptanz für $j\le J$ höchstens $(1-1/(J+1/2))^k$. Ganzzahlige Spins scheitern schon am ersten Filter. Bei Spin $1/2$ passieren beide magnetischen Zustände und alle ihre Überlagerungen sicher. Ohne Spinobergrenze liefert diese Abschätzung punktweise Konvergenz und keine einheitliche endliche Fehlerschranke.

Damit gibt es neben der gemeinsamen Quadratsummenmessung eine zweite Modellroute: zwei binäre, vorzeichenblinde Spektralfilter auf transversalen Achsen. Die Robertson-Aussage in r63.2 liefert die Spektralarithmetik, aber kein natives Messinstrument für diese Filter. Eine endliche Filterfolge liefert im Allgemeinen eine Näherung, und das effektive Horizontzählgewicht bleibt separat zu prüfen.

### Kronecker-Delta und exakter Betragszeiger

Erkundung. In der $J_x$-Eigenbasis ist der binäre Filter durch $P_x|j,m_x\rangle=\delta_{4m_x^2,1}|j,m_x\rangle$ gegeben. Für einen Spinträger mit Obergrenze $J$ wähle eine ganze Zahl $L>4J^2+1$. Dann liefert die endliche Charakter-Mittelung

$$
P_x=\frac1L\sum_{k=0}^{L-1}\exp\!left[\frac{2\pi i k}{L}(4J_x^2-I)\right]
$$

den exakten Projektor, denn $2m_x$ ist ganzzahlig und kein von null verschiedener Wert von $4m_x^2-1$ ist ein Vielfaches von $L$. Analog ergibt $2B-I$ mit $B=J_x^2+J_y^2$ ganzzahlige Eigenwerte und liefert bei $L>2J(J+1)+1$ einen einzelnen exakten Minimalspinzeiger. Die kontrollierten Phasen sind Modellressourcen. Eine gemeinsame Zeigerkopplung an die jeweilige quadratische Observable erhält die Kohärenz innerhalb ihres Ja-Sektors, sofern nur das Ja-Nein-Bit gespeichert und das Arbeitsregister zurückgesetzt wird. Die alternierenden Achsenfilter bleiben im Allgemeinen von einer einmaligen gemeinsamen Minimalspinmessung verschieden.

### Minimalspin-Delta aus gemeinsamen Rotationen

Erkundung. Kopple den Einpunktträger an ein Referenzdoublet $R$ mit Spin $1/2$ und mittlere die gemeinsame $SU(2)$-Rotation mit normiertem Haarmaß. Der so erhaltene Operator $Q$ projiziert auf die invarianten Zustände. Nach der Drehimpulsaddition enthält $V_j\otimes V_{1/2}$ genau dann ein Singulett, wenn $j=1/2$. Ein maximales Verschränkungspaar aus $R$ und einem unberührten zweiten Doublet $A$ präpariert auf $R$ den reduzierten Zustand $I_R/2$. Bezeichne die Einbettung durch Anhängen dieses Paares mit $V$. Dann gilt

$$
V^\dagger(Q\otimes I_A)V=\tfrac14 P_{1/2}.
$$

Der Faktor folgt daraus, dass die partielle Spur des Singulettprojektors auf dem ausgewählten Systemdoublet $I/2$ ist. Multiplizitätsräume des Systemspins bleiben unangetastet.

Der Faktor vier lässt sich kohärent entfernen. Schreibe $Q'=Q\otimes I_A$, $R_V=2VV^\dagger-I$ und $R_Q=I-2Q'$. Für jeden eingebetteten Minimalspinzustand $v=V\psi$ gilt $VV^\dagger Q'v=v/4$, also $R_VR_Qv=2Q'v$. Dieser Zustand ist normiert und liegt vollständig im Singulettbild. Für höhere Spins und Spin null ist $Q'v=0$ und $R_VR_Qv=v$. Eine binäre Singulettmarkierung zwischen dieser Folge und ihrer Inversion liefert daher exakt $P_{1/2}$ als Ja-Effekt und setzt die Referenz zurück. Sie erhält beide magnetischen Zustände und ihre Überlagerungen.

Dies ist eine alternative ideale Konstruktion zur quadratischen Phasenmessung. Die Haarmittelung definiert den Projektor algebraisch. Der physikalische Aufbau braucht eine kohärente gemeinsame Singulettreflexion und eine Reflexion um die Referenzpräparation. Eine zufällige gemeinsame Rotation mit anschließendem Vergessen des Winkels realisiert diese Reflexion nicht. Native Verfügbarkeit und das tatsächliche Horizontzählgewicht bleiben offen.

### Austauschgenerator und Horizontzählung des Referenzfilters

Erkundung. Mit Referenzspin $R=\boldsymbol\sigma/2$ hat der rotationsinvariante Austausch $K=2\mathbf J\cdot\mathbf R=(\mathbf J+\mathbf R)^2-\mathbf J^2-\mathbf R^2$ auf den gekoppelten Sektoren $j+1/2$ und $j-1/2$ die Eigenwerte $j$ beziehungsweise $-(j+1)$; bei $j=0$ existiert nur der erste Zweig. Der Eigenwert $-3/2$ gehört genau zum gemeinsamen Singulett von System und Referenz. Auf einem Träger mit $j\le J$ lässt sich sein Projektor per kontrollierter Phase des ganzzahligen Operators $2K+3I$ bestimmen. Ein ganzzahliger Modulus $L>2J+3$ verhindert Aliaswerte. Binäre Markierung und Rückrechnung geben sowohl den Singulettzeiger als auch die für die Verstärkung benötigte Reflexion. Damit ist der gesuchte Kopplungsterm konkret: isotroper Austausch zwischen gravitativem Durchstoßpunkt und einer Spin-$1/2$-Referenz. Eine verfügbare gewöhnliche Spinrotation oder ein elektromagnetischer Kompensator allein etabliert diesen Term nicht.

Die beiden Referenzdoublets können als gemeinsames Singulett statt als ein anders orientiertes maximal verschränktes Paar präpariert werden. So sind die Präparation und ihre Reflexion invariant unter gemeinsamer Rotation aller Register. Der verstärkte und rückgerechnete Filter lässt auf einer einzelnen Systemkopie von Spin $1/2$ beide magnetischen Zustände intakt. Würde man stattdessen das Punkt-Referenz-Singulett als Endzustand zählen, erhielte man pro Systemkopie nur einen invarianten Zustand. Das ursprüngliche Zählgewicht zwei bezieht sich auf den nach der Rückrechnung verbleibenden lokalen Systemträger.

Auch perfekte lokale Filter entscheiden die Mehrpunktzählung nicht. Für $N=2k$ ausgewählte Punkte hat der freie Produktträger Dimension $2^N$, der Teilraum mit magnetischer Gesamtsumme null Dimension $\binom{2k}{k}$ und der volle $SU(2)$-Singulettsektor Dimension $\binom{2k}{k}-\binom{2k}{k+1}$. Beide Einschränkungen behalten denselben führenden Exponenten pro Punkt $\ln2$, haben aber verschiedene endliche Multiplizitäten. Bei ungeradem $N$ sind beide Nullsektoren leer. Damit kann der lokale Filter die minimale Spinunterstützung und das lokale Gewicht zwei reproduzieren, ohne eine konkrete native Horizontprojektion zu bestimmen. Offen bleiben die Ableitung der Austauschkopplung und der von T tatsächlich zugängliche Mehrpunktträger.

### Gemeinsame Form der M- und T-Zählmasken

Erkundung. Auf dem Einpunktträger ohne $j=0$ wähle eine Achse $u$ und setze $B_u=J^2-J_u^2$. Die beiden Spektralmasken

$$
P_M(u)=\mathbf1_{\{0\}}(B_u-|J_u|),\qquad
P_T=\mathbf1_{\{1/2\}}(B_u)
$$

reproduzieren gemeinsam die r63-Einpunktgewichte. Denn $B_u-|J_u|=(j-|m|)(j+|m|+1)$ verschwindet genau bei $m=\pm j$, während $B_u=1/2$ genau Spin $1/2$ auswählt. Damit gilt $P_T\le P_M(u)$. Bei einer Kopie je Irrep hat $P_M(u)$ Rang zwei in jedem Spin und $P_T$ Rang zwei insgesamt. Die beiden Spuren mit Gewicht $\exp[-2\pi\gamma\sqrt{J^2}]$ sind genau die beiden r63-Normierungsgleichungen im Einpunktmodell. Die Achsenwahl allein genügt nicht: Jeder Effekt $f(J_u)$ muss demselben $m$ in verschiedenen Spins denselben Wert geben. Insbesondere kann er $m=1/2$ in Spin $1/2$ nicht akzeptieren und in Spin $3/2$ verwerfen. Beide oben definierten Masken brauchen daher mehr Information als ein U(1)-Label.

Über alle Achsen gemittelt ist der M-Effekt innerhalb jedes Irreps nach Schur skalar. Seine Spur bleibt zwei, sodass er dort genau $2I/(2j+1)$ beträgt. Die r63-Zählspur bleibt bei der Mittelung gleich. Der gemittelte Effekt akzeptiert jedoch für $j>1/2$ jeden Zustand mit einer Wahrscheinlichkeit zwischen null und eins. Er definiert dort keinen scharfen zweidimensionalen Unterraum. Der T-Projektor ist bereits achsenunabhängig. Somit erzwingt das M-Zählgewicht zwei allein keine physikalisch ausgezeichnete Achse, wohl aber eine zusätzliche Erklärung, wenn es als scharfe Auswahl verstanden wird. Die innere Einheit der QAM ist bislang weder mit der gravitativen Achse $u$ identifiziert noch als Erzeuger der gemeinsamen quadratischen Auslesung nachgewiesen. Globale Horizontbedingungen bleiben separat.

### Quadratischer Erwartungswert und Spinfilter

Erkundung. r63.2 gibt die Robertson-Arithmetik in $|j,m\rangle$. Daraus folgt die Spektralformel für $B=J_x^2+J_y^2$, aber keine gravitative Zeigerkopplung. Auch eine Messung des Erwartungswerts von $B$ allein rekonstruiert den binären T-Effekt für allgemeine Eingaben nicht. Der Extremzustand $|1,1\rangle$ hat $B=1$ und Minimalspin-Gewicht null. Eine gleichgewichtete Mischung aus $|1/2,1/2\rangle$ und $|3/2,3/2\rangle$ hat denselben Erwartungswert $1$, aber Minimalspin-Gewicht $1/2$. Die gemeinsame Spektralabfrage trennt diese Eingaben.

Der QAM-Routenkatalog unterscheidet deshalb den nativen Zugriff auf die gravitative Quadratsumme von der Zulassung eines Spektralinstruments für ihren Wert $1/2$. Selbst wenn der erste Zugriff deklariert ist, bleibt der zweite Guard offen. Die r63-Formel und die elektromagnetische Dualitätsabbildung aus r28 liefern in den geprüften Abschnitten keinen Nachweis für diese beiden gravitativen Operationen.

### Minimalspin aus der Achsenmittelung einer festen Spinrotation

Erkundung. Auf dem gravitativen Einpunktträger bilde das kohärente Operatormittel $C=\int_{S^2}\exp(-i\pi J_u/2)\,du$ mit normiertem Flächenmaß. Die Mittelung ist rotationsinvariant und wegen der Paarung $u,-u$ selbstadjungiert. Nach Schur ist sie auf jedem Spin-$j$-Irrep ein Skalar. Seine Spur kann für die $z$-Achse berechnet werden. Für $d=2j+1$ ergibt die geometrische Reihe

$$
c_j=\frac{\sin(d\pi/4)}{d\sin(\pi/4)}.
$$

Der Spin $1/2$ hat $c_{1/2}=1/\sqrt2$. Für alle höheren Spins ist $d\ge3$ und damit $|c_j|\le\sqrt2/3<1/\sqrt2$. Der mögliche Spin null hat $c_0=1$. Somit ist der Spektralprojektor von $C$ zum Wert $1/\sqrt2$ exakt $P_{1/2}$, auch ohne Spinobergrenze. Das Ergebnis bleibt bei mehreren Kopien eines Irreps gültig, wählt dann aber alle Kopien. Der Abstand zum restlichen Spektrum ist mindestens $\sqrt2/6$.

Das Integral mittelt Operatoramplituden. Der Kanal, der eine zufällig ausgewählte Rotation anwendet und die Achse vergisst, ist eine andere Operation. Er akzeptiert keinen Spin allein durch diese Mittelung. Auch der Erwartungswert von $C$ auf einer gemischten Eingabe ersetzt die binäre Spektralabfrage nicht. Die Route braucht kohärenten Zugriff auf die gravitativen Rotationen und ein Spektralinstrument für das zentrale Operatormittel. Diese Voraussetzungen sind im bisherigen Routenkatalog nicht als nativ zugelassen belegt.

### Endliches exaktes Achsenmittel bei Spinobergrenze

Erkundung. Auf dem Spin-$j$-Irrep ist die Rotation die symmetrische Potenz vom Grad $2j$ der fundamentalen Matrix $\cos(\alpha/2)I-i\sin(\alpha/2)\,u\cdot\boldsymbol\sigma$. Jeder Matrixeintrag ist daher ein Polynom in den Achsenkomponenten vom Grad höchstens $2j$. Setze $D=2J$ für die deklarierte Spinobergrenze. Schreibe $z=u_z$ und $u_x\pm i u_y=\sqrt{1-z^2}e^{\pm i\phi}$. Ein gleichverteiltes Gitter mit $D+1$ Azimuten löscht alle nichtnulligen Fouriermoden bis Grad $D$. Jeder verbleibende Monomterm hat gleiche Potenzen der beiden transversalen Faktoren und ist daher ein Polynom in $z$ vom Grad höchstens $D$. Eine Gauss-Legendre-Regel mit $\lfloor D/2\rfloor+1$ Knoten integriert diese Terme exakt. Die Gewichte für das normierte Achsenmittel sind die Gauss-Legendre-Gewichte dividiert durch $2(D+1)$.

Für das Beispiel bis $j=5/2$ genügen sechs Azimute und drei Höhen, also 18 gewichtete Rotationen. Die Routensuche gibt diese hinreichende Knotenzahl automatisch aus. Die exakte Formel gilt auf dem deklarierten endlichen Träger; die 18 Achsen sind keine behauptete Minimalzahl. Die endliche Summe ist ein Operatormittel und erfordert weiterhin kohärente Steuerung, damit sie als QAM-Messressource nutzbar ist.

### Kohärente endliche Rotationssumme und binärer Spektralzeiger

Erkundung. Für die endliche Quadratur mit positiven normierten Gewichten $w_i$ präpariere ein Achsenregister in $|w\rangle=\sum_i\sqrt{w_i}|i\rangle$. Wende kontrolliert $U_i=\exp(-i\pi J_{u_i}/2)$ an und mache die Achsenpräparation rückgängig. Der Nullblock dieses unitären Aufbaus ist genau $C=\sum_i w_i U_i$. Ein einzelner Nullausgang implementiert damit den Effekt $C^2$. Beim Minimalspin hat er Wahrscheinlichkeit $1/2$; er ist noch kein binärer Minimalspinfilter. Auch wiederholte Nullauswahl lässt die Zielakzeptanz auf $2^{-k}$ sinken, während das relative Gewicht höherer Spins pro erfolgreicher Abfrage höchstens mit $4/9$ multipliziert wird, sofern Spin null ausgeschlossen ist.

Für den begrenzten Träger lässt sich dagegen aus dem berechneten Spektrum ein exakter Filter konstruieren. Sei $\lambda=1/\sqrt2$ und $S$ die Menge der übrigen verschiedenen Eigenwerte von $C$. Das Polynom

$$
p(x)=\prod_{s\in S}\frac{x-s}{\lambda-s}
$$

ergibt $p(C)=P_{1/2}$. Produkte von unabhängigen Nullblöcken kodieren die Potenzen $C^k$. Eine weitere gewichtete kohärente Summe der Potenzen mit den Vorzeichen der Polynomkoeffizienten kodiert $P_{1/2}/\sum_k|p_k|$. Dieser Aufbau liefert einen skalierten Filter; eine deterministische binäre Messung braucht zusätzlich eine passende kohärente Verstärkung oder eine direkte Spektralmessung. Der Polynombeweis garantiert den exakten Zieloperator auf dem Modellträger. Er begründet weder eine effiziente Pulskonstruktion noch die native Verfügbarkeit kontrollierter gravitativer Rotationen.

Im Beispiel bis $j=5/2$ sind die konkurrierenden Eigenwerte $1/3,0,-1/5,-\sqrt2/6$. Das Polynom hat daher Grad vier. Seine Nullstellen und sein Grad können unmittelbar aus dem bereits berechneten Charakterspektrum in den Suchbeleg übernommen werden.

### Exakte Verstärkung des endlichen Rotationsfilters

Erkundung. Für die Nullstellen $-1/5,-\sqrt2/6,0,1/3$ und den Zielwert $\lambda=1/\sqrt2$ ergibt die exakte Auswertung der Koeffizientensumme des normierten Polynoms

$$
\alpha=\sum_k |p_k|=\frac{582+201\sqrt2}{161}\approx5{,}38048.
$$

Die kohärente Polynomsumme kodiert den Projektor mit Zielamplitude $1/\alpha$ und hat auf dem Komplement Nullamplitude. Ein zusätzliches Zeigerbit kann die Zielamplitude weiter mit $\alpha\sin(\pi/18)\approx0{,}93431$ multiplizieren. Dann ist der Ausgangswinkel $\theta=\pi/18$. Vier gewöhnliche Amplitudenverstärkungsschritte rotieren den Zielzweig auf $(2\cdot4+1)\theta=\pi/2$ und lassen die Erfolgswahrscheinlichkeit auf dem Komplement null. Drei Schritte mit bloßer Abschwächung reichen in diesem Schema nicht, weil $\sin(\pi/14)>1/\alpha$. Der Verstärker wirkt mit derselben Amplitude auf beiden magnetischen Zuständen.

Die verstärkte Vorbereitung benötigt neun Anwendungen der Polynomsummen-Unitären oder ihres Inversen und die dazugehörigen Reflexionen. Kopieren des Erfolgsbits und Rückrechnung verdoppeln die Zahl auf 18 Anwendungen. Diese Zahl zählt Blockzugriffe, keine elementaren Rotationen oder Pulse. Die Konstruktion setzt exakte gewichtete Präparationen, kontrollierte Rotationen, Inverse und die beiden Reflexionen voraus. Sie ist für den endlichen Beispielträger hergeleitet und wurde nicht als vollständige Schaltung simuliert.

Die reduzierte Qiskit-Erkundung `python -m qam.examples.rotation_filter_amplification` setzt die abgeschwächte Zielamplitude durch eine auf die zwei Minimalspinlabels konditionierte Rotation um. Vier Verstärkungsschritte, Kopieren und Rückrechnung liefern den erwarteten Zeiger auf allen vier Modelllabels. Für eine kohärente Eingabe mit verschiedenen komplexen Phasen ergibt sich ein Zustandsvektorabstand von $5{,}14\cdot10^{-16}$. Die Schaltung setzt die vorberechnete spektrale Markierung voraus. Sie simuliert weder die 18 Achsenrotationen noch die kohärente Polynomsumme selbst.

Die numerische Gegenrechnung `python -m qam.examples.rotation_filter_axis_check` bildet auf jedem der fünf Spinblöcke die Matrizen aller 18 gewichteten Vierteldrehungen direkt aus den Drehimpulsgeneratoren. Das Mittel weicht in Operatornorm um höchstens $4{,}12\cdot10^{-16}$ vom Charakterwert mal Identität ab. Das angewandte Polynom weicht um höchstens $2{,}09\cdot10^{-15}$ vom Zielprojektor ab. Diese Rechnung prüft die Matrixbausteine getrennt von der reduzierten Qiskit-Verstärkung. Sie zerlegt die gewichtete Summe nicht in eine vollständige kohärente Gatterschaltung.

### Zusammengesetzte kohärente Simulation des Rotationsfilters

Erkundung. `python -m qam.examples.rotation_filter_coherent` berechnet das Achsenmittel aus den 18 Drehungen und bettet seine hermitisierte Matrix in die unitäre Blockmatrix mit Diagonalblöcken $C,-C$ und Nebendiagonalblock $\sqrt{I-C^2}$ ein. Vier Arbeitsbits ermöglichen die Produkte der Nullblöcke. Ein Auswahlregister kombiniert die vier nichtverschwindenden Polynomterme kohärent einschließlich ihrer Vorzeichen. Abschwächung, vier Verstärkungsschritte, Kopieren und Rückrechnung laufen danach in derselben Qiskit-Schaltung. Für alle fünf Spinblöcke bleibt der Zustandsvektorabstand vom idealen markierten Eingang unter $7{,}5\cdot10^{-14}$. Die Eingaben sind innerhalb jedes Irreps kohärente Überlagerungen. Die Schaltung verwendet die kompakte Matrixdilatation des bereits berechneten Achsenmittels; die kohärente Ansteuerung einzelner Achsen wird darin nicht als eigene Gatefolge ausgeführt.

### Qiskit-Abgleich der kontrollierten Achsenauswahl

Erkundung. `python -m qam.examples.rotation_filter_axis_lcu` präpariert das Achsenregister mit den Quadratwurzeln der 18 Quadraturgewichte. Eine kontrollierte Blockmatrix wendet auf jedem Achsenlabel die zugehörige Vierteldrehung an. Die inverse Achsenpräparation liefert im Nullblock das kohärente Mittel. Die Simulation vergleicht alle Spalten dieses Blocks auf fünf Irreps mit dem exakten Charakter. Der größte Operatornormfehler beträgt $8{,}95\cdot10^{-15}$. Ungenutzte Achsenlabels sind mit Identität aufgefüllt und haben kein Präparationsgewicht. Die kontrollierte Blockmatrix ist eine Qiskit-Unitary; eine Zerlegung in elementare Hardwaregatter wurde nicht geprüft.

Die algebraische Verbindung zur Polynomsumme gilt für jede unitäre Einbettung mit demselben Nullblock: Mit einem frischen Arbeitsregister je Faktor ist der gemeinsame Nullblock eines Produkts genau das Produkt der Einzelnullblöcke. Die anschließende kohärente Termwahl hängt im Erfolgsblock nur von diesen Produkten ab. Damit kann die hier geprüfte Achsenauswahl die kompakte Einbettung in der mathematischen Konstruktion ersetzen. Die gemeinsame Qiskit-Simulation mit sämtlichen separaten Achsenregistern wurde nicht ausgeführt.

### Kürzerer Rotationsfilter mit zentraler Vorselektion

Erkundung. Eine kohärent kontrollierte volle Spinrotation wirkt auf dem Spin-$j$-Sektor als $(-1)^{2j}I$. Ein Ramsey-Zeiger kann daher die ganzzahligen und halbzahligen Sektoren exakt trennen, ohne innerhalb eines Sektors magnetische Zustände zu unterscheiden. Die Volldrehung scheitert als alleiniger Minimalspinselektor, taugt aber als Vorfilter. Auf dem Beispielträger bis $j=5/2$ bleiben nach der halbzahligen Vorselektion außer dem Zielwert $1/\sqrt2$ nur die Werte $0$ und $-\sqrt2/6$ des Vierteldrehungsmittels. Der Filtergrad sinkt von vier auf zwei:

$$
p_{\rm halb}(x)=\tfrac32 x^2+\tfrac{\sqrt2}{4}x.
$$

Der Koeffizientennormierungsfaktor ist $3/2+\sqrt2/4<2$. Nach Abschwächung auf Zielamplitude $1/2$ genügt ein Amplitudenverstärkungsschritt. Mit Kopieren und Rückrechnung erfordert der Polynomteil sechs statt 18 Zugriffe auf seine jeweilige Polynomsummen-Unitäre oder deren Inverses. Hinzu kommt die kohärente Vorselektion und ihre Rückrechnung. Für den zusammengesetzten binären Zeiger wird die Polynommarkierung nur im halbzahligen Zweig ausgeführt; die Nebenregister können danach gelöscht werden. Die QAM gibt die reduzierten Nullstellen aus, wenn eine Volldrehung deklariert ist. Diese Ausgabe bewertet die algebraische Vorselektion, keine vollständige Hardware-Gatterzahl oder native Verfügbarkeit.

Die erweiterte Qiskit-Simulation `python -m qam.examples.rotation_filter_coherent` prüft den verkürzten Filter auf der direkten Summe der fünf Spinblöcke. Sie verwendet eine kohärente Ramsey-Markierung der zentralen Volldrehung, den Filter zweiten Grades und einen Verstärkungsschritt. Eine Überlagerung aller 20 magnetischen Basiszustände mit komplexen Phasen hat nach Kopieren und Rückrechnung Zustandsvektorabstand $1{,}31\cdot10^{-14}$ zum idealen Zeiger. Wie bei der längeren Schaltung ist das berechnete Achsenmittel durch seine kompakte unitäre Dilatation eingebettet. Die zentrale Volldrehung ist als ihre exakte Blockwirkung kodiert.

### Eichverträglichkeit der kontrollierten Spinrotation

Erkundung. Auf dem Einpunktmodell sei $D(g)$ die lokale interne $SU(2)$-Wirkung und der Zeiger ein Eichsingulett. Die kontrollierte Rotation um eine fest eingesetzte Achse $u$ ist $W_u=P_0\otimes I+P_1\otimes D(h_u)$. Gemeinsame Eichkonjugation ergibt $W_{gu}$, da $D(g)D(h_u)D(g)^\dagger=D(gh_ug^{-1})$. Eine einzelne feste Vierteldrehung ist daher im Allgemeinen kein eichinvarianter Zeigeroperator. Das Ausschlussargument gilt ohne physikalisch mittransformierende Referenzachse. Die zentrale Volldrehung ist eine Ausnahme: Ihr Element $-I\in SU(2)$ kommutiert mit jeder Eichrotation und die kontrollierte Operation ist auf diesem Modellträger invariant. Die Existenz der abstrakten zentralen Wirkung liefert noch keine dynamische Steuerung.

Auch das kohärente Achsenmittel ist invariant. Eine mögliche Realisierung muss daher entweder die Achse relational mitführen oder das invariant gemittelte Objekt direkt koppeln. Aus r28s elektromagnetischer Dualitätsrotation und aus r63s Spin-Arithmetik folgt in den geprüften Abschnitten keine solche gravitative Steuerung. Die Einschränkung betrifft den festen Achsenpuls mit neutralem Zeiger. Sie schließt kein eichinvariantes Instrument für das ganze Achsenmittel aus.

### Relationales Achsenmittel mit einem Quantenrotor

Erkundung. Verwende als Achsenreferenz $L^2(S^2,du)$ mit normiertem Maß und konstanter normierter Wellenfunktion $\Omega(u)=1$. Der gemeinsame Operator auf referenzabhängigen Spinvektoren lautet $(W\psi)(u)=D_j(h_u)\psi(u)$, wobei $h_u$ die Vierteldrehung um $u$ bezeichnet. Er ist unitär. Unter gemeinsamer interner Rotation wirkt $(G_g\psi)(u)=D_j(g)\psi(g^{-1}u)$. Wegen $D_j(g)D_j(h_{g^{-1}u})=D_j(h_u)D_j(g)$ kommutieren $W$ und $G_g$. Der Referenz-Nullblock $\langle\Omega|W|\Omega\rangle$ ist genau das kohärente Achsenmittel. Die Präparation und die Reflexion um $\Omega$ sind rotationsinvariant. Damit ist die Symmetriehürde im Modell konstruktiv gelöst, sofern der Rotor ein eigener physikalischer Freiheitsgrad ist und die gemeinsame Kopplung zugelassen wird.

Für $j\le J$ reicht für einen Blockzugriff ein endlicher Referenzträger mit Kugelflächenfunktionen bis Grad $D=2J$. Auf der Eingabe $\Omega\otimes\psi$ ist die Ausgabe von $W$ ein achsenabhängiges Polynom vom Grad höchstens $D$ und liegt daher im abgeschnittenen Referenzträger. Die Dimension der Referenz ist $(D+1)^2$, im Beispiel also 36. Die so definierte Isometrie auf dem Eingangsunterraum ist ein Intertwiner und lässt sich auf dem endlichen Gesamtträger zu einer eichverträglichen Unitären ergänzen: Quelle und Bild sind äquivalente Unterdarstellungen, daher sind auch ihre orthogonalen Komplemente äquivalent. Diese Ergänzung ist im Allgemeinen nicht die Kompression des vollen Multiplikationsoperators. Frische Referenzregister pro Polynomfaktor und die inverse gewählte Ergänzung reichen für die zuvor beschriebene kohärente Rückrechnung. Die Rechnung zeigt Existenz im Modell, ohne eine native Rotorvariable oder einen erzeugenden gravitativen Hamiltonterm herzuleiten.

### Rotorkopplung als eigener Pfad im QAM-Katalog

Erkundung. Der Multiplikationsoperator des relationalen Modells ist die Zeitentwicklung des invariant kontrahierten Generators $H=\kappa\sum_i J_i\otimes U_i$, wobei $U_i$ die Multiplikation mit der $i$-ten Achsenkoordinate auf dem Rotor bezeichnet. Die $U_i$ transformieren als Vektor; ihre Kontraktion mit dem gravitativen Spin ist unter der gemeinsamen Wirkung invariant. Die Pulsfläche $\kappa t=\pi/2$ liefert die modellierte Vierteldrehung im vollen Rotorraum. Bei endlichem Rotorträger genügt die zuvor konstruierte unitäre Ergänzung für denselben Nullblock. Die Projektion des Hamiltonterms auf den abgeschnittenen Rotorraum und anschließende Exponentiation liefern diese Ergänzung im Allgemeinen nicht automatisch.

Der Routenkatalog unterscheidet die invariante Rotorkopplung und die kohärente Rückkehrabfrage in den Rotorsingulettzustand. Beide sind native Voraussetzungen, zusätzlich zur binären Spektralabfrage des resultierenden Achsenmittels. Damit ersetzt der Modellpfad die direkt von außen gesteuerte gravitative Achsenrotation. Er liefert keine Identifikation des Rotors mit einem bereits vorhandenen QAM-Feld.

### Fehlerkontrolle für den direkt abgeschnittenen Rotorgenerator

Erkundung. Setze $H=\mathbf J\cdot\mathbf U$ und $H_K=P_{\le K} H P_{\le K}$ auf dem Rotorträger bis Kugelflächenordnung $K$. Multiplikation mit einer Achsenkomponente verbindet nur benachbarte Ordnungen. Eine Potenz, die von der konstanten Rotorwelle startet, den abgeschnittenen Bereich verlässt und zur Konstante zurückkehrt, braucht daher mindestens $2K+2$ Faktoren. Die Rotor-Nullblöcke von $H^m$ und $H_K^m$ stimmen für $m<2K+2$ exakt überein. Beide Generatoren haben auf Spin $j$ Norm höchstens $j$, denn punktweise ist $\mathbf J\cdot u$ unitär äquivalent zu $J_z$, und orthogonale Kompression vergrößert die Norm nicht. Für den Vierteldrehungspuls folgt daher

$$
\big\|\langle\Omega|(e^{-i\pi H/2}-e^{-i\pi H_K/2})|\Omega\rangle\big\|
\le 2\sum_{m\ge 2K+2}\frac{(\pi j/2)^m}{m!}.
$$

Der abgeschnittene Hamiltonterm bleibt eichinvariant, da der Ordnungsprojektor mit den Rotorrotationen kommutiert. Die Abschätzung liefert somit eine kontrollierbare Annäherung mit einem konkreten endlichen Generator. Sie ist von der zuvor gezeigten exakten unitären Ergänzung zu unterscheiden. Für $j\le5/2$ liefert $K=12$ bereits eine Normabweichung unter $1{,}7\cdot10^{-11}$ nach der geometrischen Abschätzung der Reihe. Die Rechnung betrifft den Nullblock vor dem Polynomfilter und setzt die gravitative Rotorkopplung weiterhin voraus.

Die Restschranke ist konservativ. Für den idealen isotropen Generator gibt es einen stärkeren exakten Schluss: $\Omega\otimes V_j$ hat unter gemeinsamen Rotationen Gesamtspin $j$. Der invariante Generator erhält diesen Gesamtspin. In $V_j\otimes V_\ell$ kann Gesamtspin $j$ nach der Dreiecksregel nur für $\ell\le2j$ vorkommen. Damit bleibt der gesamte von der Eingabe erreichte Raum innerhalb des Rotorträgers bis $K=2j$. Der direkt komprimierte Generator liefert dort exakt dieselbe Evolution wie der volle Rotor, nicht nur denselben Nullblock. Für alle fünf Beispielblöcke genügt gemeinsam $K=5$, also Referenzdimension 36. Für $K<2j$ bleibt die obige Restabschätzung anwendbar.

Die Gegenrechnung `python -m qam.examples.rotation_filter_rotor_check` baut die drei projizierten Achsenoperatoren in der Kugelflächenbasis auf und exponentiert den invarianten Hamiltonoperator direkt. Bei $K=5$ liegt der Operatornormfehler des Rückkehrblocks auf allen fünf Spins unter $9\cdot10^{-16}$. Bei $K=4$ weicht der Block für $j=5/2$ um rund $1{,}75\cdot10^{-4}$ ab. Der Vergleich prüft den numerischen Aufbau des Modellgenerators. Die Exaktheit bei $K\ge2j$ folgt analytisch aus der Gesamtspin-Erhaltung.

### Coframe-Normale als Referenz: Eigenfluss und zweiter Randpunkt

Erkundung. Für ein nichtentartetes infinitesimales Flächenstück ist die interne Coframe-Normale im bereits verwendeten Flusswörterbuch $u^i=F^i/\|F\|$. Die Einsetzung in $\mathbf F\cdot\mathbf u$ ergibt klassisch $\|F\|$. Sie stellt damit keine unabhängige Achse für denselben Fluss bereit. Auf dem quantisierten nichttrivialen Spinträger ergibt die analoge symmetrische Wahl $U_i=J_i(J^2)^{-1/2}$ die Kontraktion $\sum_i J_iU_i=\sqrt{J^2}$. Außerdem gilt $[J_i,U_j]=i\epsilon_{ijk}U_k$. Das unterscheidet diese Wahl vom Rotormodell, in dem $J_i$ und $U_j$ auf getrennten Faktoren wirken und kommutieren. Die Eigenfluss-Normale reduziert den Ansatz folglich auf direkten Casimirzugriff. Sie liefert weder den relationalen Rotor noch seine unabhängige Präparation.

Eine Normale eines zweiten Flächenstücks wäre davon zu unterscheiden. Wenn sein Fluss auf einem separat zugänglichen Faktor einen scharfen Spin $s>0$ trägt, lautet der entsprechend normierte Kandidat $\mathbf J\cdot\mathbf R/\sqrt{s(s+1)}$. Ein gemeinsames Singulett dieses Paars existiert genau für $j=s$. Ohne eine unabhängige Festlegung $s=1/2$ ist die Singulettbedingung daher nur ein Vergleich der Spins. Insbesondere genügt die globale Horizontschließung nicht, um einen Punkt mit Minimalspin als Referenz zu liefern. Selbst ein vorhandenes Punktpaar benötigt die zugelassene lokale Kopplung und ein kohärentes Paarinstrument. Der Befund betrifft die aus demselben beziehungsweise einem zweiten Fluss konstruierte Normale und lässt zusätzliche Randfreiheitsgrade offen.

### Fundamentale Holonomie und Spin-null-Auslesung

Erkundung. Auf dem Modellträger $L^2(SU(2),dg)$ mit normiertem Haarmaß sei $W$ die unitäre Multiplikation $(W\psi)(g)=g\psi(g)$ auf einem fundamentalen Hilfsdoublet. Der Spin-null-Ausgang projiziert das Gruppenregister auf die konstante Funktion. Für die Hilfszustände $b$ und $a$ ist die Übergangsamplitude $\int g_{ab} f(g)\,dg$. Schur-Orthogonalität zeigt, dass nur der Peter-Weyl-Block $j=1/2$ beiträgt. Für ein anfänglich maximal gemischtes Hilfsdoublet ist die Erfolgswahrscheinlichkeit $\tfrac12\sum_{ab}|\int g_{ab} f(g)\,dg|^2=\tfrac14\|P_{1/2}f\|^2$, weil die vier Funktionen $\sqrt2\,\overline{g_{ab}}$ eine Orthonormalbasis dieses Blocks bilden.

Mit einer kohärenten Reinigung des Hilfszustands gilt daher dieselbe $1/4$-Kompression wie beim Referenzfilter. Ein Verstärkungsschritt, Kopieren des Spin-null-Bits und Rückrechnung liefern im Modell den exakten Spin-$1/2$-Effekt. Das Modell setzt eine fundamentale Holonomie als kontrollierte Randoperation und ein kohärentes Spin-null-Instrument voraus. Die zusätzliche Referenz ist hier ein fundamentales Hilfsdoublet und kein bereits auf Minimalspin selektierter gravitativer Randpunkt.

Der volle Peter-Weyl-Block $V_{1/2}\otimes V_{1/2}^*$ hat allerdings Rang vier. Die r63-Einpunktzählung verlangt Gewicht zwei. Dazu muss eine native Randbedingung erklären, welcher der beiden magnetischen Indizes zugänglich ist beziehungsweise wie das Zählmaß entsteht. Die geprüften Companion-Fundstellen zur Holonomie liefern diese Zuordnung und das Spin-null-Instrument nicht. Der holonomische Modellweg beseitigt daher die zirkuläre Forderung nach einem bereits ausgewählten Randpunkt, lässt aber die native Randrepräsentation und Auslesung offen.

### U(1)-Randladung und das Gewicht des Holonomiedoublets

Erkundung. Auf dem Peter-Weyl-Block $V_j\otimes V_j^*$ lasse die gravitative $SU(2)$-Wirkung links und eine Rand-$U(1)$ rechts wirken. Die rechte magnetische Ladung $q$ hat in $V_j^*$ genau dann einen eindimensionalen Gewichtsraum, wenn $|q|\le j$ und $j-q$ ganzzahlig ist. Ein scharf festgelegter rechter Ladungssektor lässt deshalb genau eine Kopie des linken $V_j$ übrig. Nach dem Minimalspinfilter hat diese Einschränkung bei $q=+1/2$ oder $q=-1/2$ Rang zwei. Lässt man beide Ladungen als unabhängige Zustände zu, bleibt der Rang vier. Ein strikter rechter U(1)-Quotient ohne Ladung entspricht $q=0$ und entfernt den Spin-$1/2$-Block vollständig.

Unter der vollen linken und rechten $SU(2)$-Wirkung ist der Spin-$1/2$-Peter-Weyl-Block irreduzibel als Produktdarstellung. Ein scharfer Rang-zwei-Projektor kann daher nicht beide Wirkungen erhalten. Bei nur linker Invarianz ist er von der Form $I\otimes |v\rangle\langle v|$. Wählt man zusätzlich rechte U(1)-Invarianz, muss $v$ eine der beiden Ladungen tragen. Eine vorzeichensymmetrische Mischung mit Effekt $I/2$ hat zwar Spur zwei, aber keinen scharfen Rang-zwei-Zählträger.

Die U(1)-Lesart aus r68 benennt die Zählweise, aber in den geprüften Abschnitten keine rechte äquivariante Randbedingung mit einzeln festgelegter halbzahliger Ladung für den T-Holononomieträger. Das Modell liefert somit eine konkrete hinreichende Randbedingung für das lokale Gewicht. Die Auswahl der Ladung und ihre Vereinbarkeit mit der globalen Horizontbedingung bleiben zu begründen. Ein festes $q=1/2$ allein lässt alle höheren halbzahligen Spins zu; der Minimalspinfilter bleibt erforderlich.

### Lokale Randladung und globale Neutralität

Erkundung. Auf $N$ Minimalspin-Peter-Weyl-Blöcken sei $q_p=\pm1/2$ die rechte Randladung am Punkt $p$. Die linke Doubletseite bleibt bei der rechten U(1)-Projektion unangetastet. Die Bedingung $\sum_p q_p=0$ lässt bei geradem $N$ genau $\binom{N}{N/2}$ rechte Vorzeichenlisten zu und bei ungeradem $N$ keine. Wenn alle diese Listen als orthogonale Zustände gezählt werden und links keine weitere Projektion erfolgt, ist die Dimension also $2^N\binom{N}{N/2}$. Die führende Entropie pro Punkt ist dann $2\ln 2$ statt $\ln 2$. Die globale rechte Neutralität ersetzt somit unter diesem Zählmaß keine punktweise Festlegung der rechten Ladung.

Eine vorab festgelegte ausgeglichene Vorzeichenliste genügt dagegen für die Neutralität und lässt links exakt $2^N$ Zustände vor weiteren Bedingungen. Wird an jedem Punkt dasselbe Vorzeichen festgelegt, ist für $N>0$ ein Hintergrund mit kompensierender Gesamtladung erforderlich. Eine Identifikation nur unter globaler Vorzeichenumkehr reduziert die Zahl der rechten Listen für gerades positives $N$ höchstens um den Faktor zwei und ändert den führenden Exponenten nicht. Wenn zusätzlich links ein globaler Singulettprojektor wirkt, ersetzt er im Produktmodell den Faktor $2^N$ durch die Singulettmultiplizität; der zusätzliche rechte Listenfaktor bleibt. Diese Folgerungen setzen unterscheidbare Punkte, unabhängige linke und rechte Faktoren und Zählung der zugelassenen Listen als Zustände voraus. Eine native Zuordnung, die die rechten Labels als feste Randdaten oder als Redundanz behandelt, ist gesondert herzuleiten.

### Paarweise rechte Schließung statt fester Vorzeichenliste

Erkundung. Für $N=2k$ Minimalspinpunkte und eine fest vorgegebene Paarung hat jedes rechte Doubletpaar unter der bloßen Bedingung $q_1+q_2=0$ zwei orthogonale Zustände. Auf dem getrennten linken und rechten Produktträger bleibt die Gesamtdimension daher $2^N2^k$. Die führende Entropie pro Punkt beträgt $3\ln2/2$. Wählt man hingegen pro Paar das rechte $SU(2)$-Singulett, bleibt dort genau eine kohärente Kombination beider Vorzeichen. Die Produktprojektion über die fest vorgegebene Paarung hat rechts Rang eins und lässt links exakt $2^N$ Zustände vor weiteren Horizontbedingungen. Beide lokalen rechten Vorzeichen haben dabei je Gewicht $1/2$.

Eine bloße globale rechte Singulettbedingung genügt nicht zur Rang-eins-Aussage: Bei $2k$ Doublets ist ihre Multiplizität $\binom{2k}{k}/(k+1)$. Diese wächst exponentiell und beträgt schon bei vier Punkten zwei. Wenn die Paarung nicht ausgezeichnet ist, muss die Dynamik erklären, ob sie einen bestimmten rechten Zustand auswählt oder mehrere Invarianten mitzählt. Paarweise Singuletts auf einer deklarierten Paarung sind somit eine hinreichende Modellbedingung für Gewicht zwei pro Punkt, ohne ein lokales Vorzeichen festzulegen. Native Paarstruktur, Kopplung und Zugang zu den linken Zuständen sind weiterhin Voraussetzungen.

### Dynamische Auswahl rechter Paarsinguletts

Erkundung. Für eine feste disjunkte Paarung $\mathcal M$ wähle im rechten Minimalspinregister den positiven Hamiltonoperator

$$
H_R=\sum_{(p,q)\in\mathcal M} g_{pq}
\left(\mathbf R_p\cdot\mathbf R_q+\tfrac34 I\right),\qquad g_{pq}>0.
$$

Jeder Summand ist der gewichtete Tripletprojektor. Die Summanden kommutieren, da die Paare disjunkt sind. Der rechte Grundraum ist eindimensional, das Produkt der Paarsinguletts, und die Lücke beträgt $\min g_{pq}$. Auf dem getrennten linken Register wirkt der Hamiltonoperator als Identität, sodass der gemeinsame Grundraum vor weiteren Bedingungen Dimension $2^N$ hat. Die Auswahl dieses Grundraums erfordert zusätzlich eine Grundraumpräparation, Relaxation oder einen Spektralfilter. Die reine Zeitentwicklung unter $H_R$ ändert die Besetzungen nicht.

Wenn zwei geforderte Singulettkanten einen Punkt teilen, haben ihre Singulettbilder keinen gemeinsamen Vektor. Ein reiner Zustand, der für $(p,q)$ im Singulettbild liegt, faktorisiert als Paarsingulett mal Rest. Das reduzierte System $(p,r)$ für eine zweite Kante ist dann $I_p/2\otimes\rho_r$ und hat Singulettwahrscheinlichkeit $1/4$, nicht eins. Das Argument erstreckt sich per Konvexität auf gemischte Zustände im ersten Singulettbild. Eine Summe positiver Tripletprojektoren auf überlappenden Kanten hat daher keinen gemeinsamen Nullraum. Gleich starke Kopplungen zwischen allen Paaren liefern hingegen bis auf eine Konstante den rechten Gesamtcasimir und unterscheiden die mehrfach vorkommenden globalen Singuletts nicht. Der Modellschluss benötigt somit eine begründete disjunkte Paarstruktur oder eine andere Dynamik, die eine eindeutige rechte Grundlinie wählt.

### Eindeutiger rechter Grundzustand ohne feste Paarung

Erkundung. Teile $N=2k$ rechte Spin-$1/2$-Faktoren in zwei gleich große Gruppen $A,B$ und kopple alle gruppenübergreifenden Paare gleich antiferromagnetisch. Mit $\mathbf S_A=\sum_{p\in A}\mathbf R_p$ und analog $\mathbf S_B$ lautet der Hamiltonoperator $H=g\mathbf S_A\cdot\mathbf S_B$, $g>0$. Seine Energien sind $g[S(S+1)-a(a+1)-b(b+1)]/2$ für Gruppenspins $a,b$ und Gesamtspin $S$. Setze $s=k/2$. Da $a,b\le s$ und $S(S+1)\ge0$, ist $E\ge-gs(s+1)$. Gleichheit verlangt $a=b=s$ und $S=0$. Der maximale Spin kommt in jeder Gruppe genau einmal vor, weil der maximale magnetische Gewichtsraum eindimensional ist. Das Singulett ihrer Kopplung kommt ebenfalls genau einmal vor. Somit hat der rechte Grundraum Rang eins und links bleiben vor weiteren Bedingungen $2^N$ Zustände.

Im Block $a=b=s$ liegt $S=1$ genau um $g$ höher. In allen anderen Blöcken sinkt mindestens einer der beiden Gruppenspins um mindestens eins, was allein aus den beiden negativen Casimirtermen eine Energieerhöhung von mindestens $gs$ gibt. Für $k\ge2$ ist $gs\ge g$; für $k=1$ existiert kein anderer Gruppenblock. Die Lücke ist daher exakt $g$. Bei extensiver Skalierung $g=g_0/k$ sinkt sie auf $g_0/k$. Die Route ersetzt die feste Paarung durch eine ausgezeichnete balancierte Zweiteilung und gruppenübergreifende Kopplung. Sie setzt weiterhin die Auswahl des Grundraums und die Entkopplung des linken Faktors voraus. Eine native Zweiteilung oder solche Randwechselwirkung ist hier nicht hergeleitet.

### Unbalancierte Zweiteilung und Auswahl zwischen Gruppengrößen

Erkundung. Seien die beiden Gruppen $N_A,N_B>0$ groß und setze $s_A=N_A/2$, $s_B=N_B/2$. Bei gegebenen Gruppenspins $a,b$ minimiert $S=|a-b|$ die Energie. Der zugehörige Wert ist $-g\min(a,b)(\max(a,b)+1)$. Für positive Spins sinkt diese Energie strikt, wenn einer der beiden Spins steigt. Daher sind beide Gruppen im Grundraum maximal ausgerichtet, $a=s_A,b=s_B$. Der rechte Grundraum trägt genau eine Kopie des Spins $|N_A-N_B|/2$ und hat Dimension $|N_A-N_B|+1$. Er ist nur bei gleicher Gruppengröße eine Singulettlinie. Beispielsweise lässt eine Aufteilung $3+1$ rechts ein Triplett statt einer einzigen Linie.

Falls die Gruppengröße selbst variieren darf und alle Aufteilungen bei gleicher Gesamtpunktzahl und gleichem Kopplungskoeffizienten verglichen werden, ergibt sich für $N=2k$ und $N_A=k+d,N_B=k-d$ die Grundenergie

$$
E_0(d)=-\frac g4\,[k(k+2)-d(d+2)],\qquad d\ge0.
$$

Die tiefste Energie liegt bei $d=0$. Das Modell bevorzugt dann eine balancierte Aufteilung, unterscheidet aber die verschiedenen balancierten Zuordnungen der Punkte nicht. Wenn diese Zuordnungen als physische orthogonale Zustände mitgezählt werden, kann ihre Multiplizität das Zählgewicht erneut erhöhen. Die Energieaussage setzt vergleichbare Gruppensektoren und denselben Koeffizienten voraus; bei festem Gruppenträger gibt es keine Dynamik zwischen den Aufteilungen. Native Sektorzuordnung, Auswahl oder Identifikation der balancierten Aufteilungen bleiben offen.

### Permutationsquotient der balancierten Aufteilungen

Erkundung. Betrachte unterscheidbare Punktplätze und zunächst benannte Gruppen mit je $k$ Punkten. Die rechte Grundlinie einer festen Aufteilung ist unter Permutationen innerhalb jeder Gruppe invariant, weil beide rechten Gruppenspins maximal und damit vollständig symmetrisch sind. Wenn alle balancierten Aufteilungen als orthogonale Sektoren vorkommen und Punktpermutationen zugleich die Aufteilung und die linken Doublets permutieren, ist der physikalische invariante Raum durch seinen Vektor auf einer festen Aufteilung bestimmt. Dieser Vektor muss unter ihrem Stabilisator $S_k\times S_k$ invariant sein. Links bleibt daher $\operatorname{Sym}^k(\mathbb C^2)\otimes\operatorname{Sym}^k(\mathbb C^2)$ mit Dimension $(k+1)^2$. Dies folgt durch Fortsetzen des Vektors auf alle Aufteilungen mittels der Permutationswirkung; die Stabilisatorinvarianz macht die Fortsetzung wohldefiniert.

Sind die Gruppen unbenannt und zählt auch ihr Tausch zur Redundanz, wirkt dieser auf dem rechten Singulett zweier Spins $k/2$ mit $(-1)^k$. Links ist deshalb die entsprechend symmetrische oder antisymmetrische Kombination der beiden Faktoren erforderlich. Für $d=k+1$ beträgt die Dimension $d[d+(-1)^k]/2$. Beide Quotienten haben nur polynomiales Wachstum. Sie beseitigen in diesem Modell die zusätzliche Aufteilungsentartung, reduzieren aber zugleich das linke Zustandswachstum unter $2^{2k}$.

Die Aussage hängt an der diagonalen Wirkung derselben Punktpermutation auf Aufteilung und linke Doublets. Eine Redundanz, die ausschließlich ein separates Referenzlabel verändert und alle linken Punktfaktoren festhält, hätte diese Wirkung nicht. Der Companion müsste eine solche getrennte Redundanz oder eine ausgezeichnete geometrische Aufteilung eigens begründen. Die Rechnung behandelt keine native Horizont-Diffeomorphismusbedingung.

### Kohärentes Mischen der balancierten Aufteilungen

Erkundung. Für $N=2k$ sei $A$ eine $k$-elementige Teilmenge der Punktplätze, mit benannter Komplementärgruppe $A^c$. Führe ein Aufteilungsregister ein und bezeichne mit $|A,\Omega_A\rangle$ den Registerzustand zusammen mit der rechten Grundlinie der zugehörigen Zweigruppenkopplung. Die Singulettphasen können für benannte Gruppen so gewählt werden, dass Punktpermutationen diese Basisvektoren ohne Vorzeichen permutieren: Der Stabilisator wirkt auf den beiden maximalen Gruppenspins trivial.

Verbinde zwei Aufteilungen, wenn sie durch Austausch eines Punkts aus jeder Gruppe auseinander hervorgehen. Dieser Graph ist zusammenhängend, denn man kann jede Abweichung von einer Zielmenge durch einen solchen Austausch verringern. Auf den rechten Grundlinien definiere den positiven Mischterm als Summe der Kantenprojektoren $(|A,\Omega_A\rangle-|B,\Omega_B\rangle)(\langle A,\Omega_A|-\langle B,\Omega_B|)$ mit gleicher positiver Gewichtung. Seine quadratische Form ist die Summe der Betragsquadrate der Koeffizientendifferenzen. Sein Kern ist daher genau die gleichgewichtete kohärente Überlagerung aller balancierten Aufteilungen. Der Term ist permutationsinvariant. Er wirkt als Identität auf den linken Doublets. Ergänzt man ihn zur blockdiagonalen Zweigruppenkopplung und setzt ihn außerhalb der balancierten Grundlinien auf null, bleibt rechts genau eine Grundlinie und links Dimension $2^N$ vor weiteren Bedingungen.

Das ist eine dynamische Auswahl in einem erweiterten Modellträger. Sie setzt kohärente Übergänge zwischen Aufteilungen voraus, welche auch die zugehörigen rechten Singuletts transportieren. Klassische Mischung oder das bloße Vergessen der Aufteilung liefert diesen Grundzustand nicht. Wird die diagonale Punktpermutation darüber hinaus als Eichbedingung auch auf dem linken Träger erzwungen, reduziert sich dessen Dimension weiterhin. Die Permutationsinvarianz des Hamiltonoperators allein erzwingt eine solche Projektion nicht. Native Verfügbarkeit des Aufteilungsregisters, Mischterm und Auswahl des Grundzustands bleiben offen.

### Warum ein permutationsinvarianter rechter Term allein nicht genügt

Erkundung. Auf dem unvergrößerten rechten Träger $(\mathbb C^2)^{\otimes 2k}$ ist der Gesamtspin-null-Raum unter Punktpermutationen die irreduzible symmetrische Gruppendarstellung zum Young-Diagramm $(k,k)$, nach der Schur-Weyl-Zerlegung. Ein rechter Hamiltonoperator, der die gemeinsame Spinrotation und alle Punktpermutationen erhält, wirkt daher auf diesem Singulettsektor nach Schur als Skalar. Für $k\ge2$ hat dieser Sektor Dimension größer eins. Ein solcher Hamiltonoperator kann darin keine eindeutige Grundlinie auswählen, selbst mit Mehrpunkttermen.

Die vorige Mischung umgeht das Hindernis durch einen vergrößerten Träger: Auf den balancierten Aufteilungslabels gibt es eine triviale Permutationsdarstellung, deren konstante Linie der Mischterm auswählt. Auf dem nackten rechten Singulettträger gibt es für $k\ge1$ keine solche triviale Linie. Das Ausschlussargument setzt volle Permutationssymmetrie, einen rechten Term und die Spin-null-Bedingung voraus. Eine nur geometrisch verbleibende Untergruppe, zusätzliche Randregister oder eine Änderung des Zählträgers liegen außerhalb dieser Voraussetzungen. Die nächste Quellenfrage ist somit, welche Punktpermutationen die native Randdynamik tatsächlich erhalten muss und ob sie bereits zusätzliche Randregister definiert.

### Zyklische Punktordnung als hinreichende Randstruktur

Erkundung. Falls die Horizontpunkte einen geraden zyklischen Orbit bilden, liefert die vorhandene Orbit-Parität eine alternierende balancierte Zweiteilung. Der einfache Shift vertauscht die beiden Gruppen. Der Hamiltonoperator $g\mathbf S_{\rm gerade}\cdot\mathbf S_{\rm ungerade}$ bleibt darunter invariant. Er hat den bereits hergeleiteten eindeutigen rechten Singulettgrundzustand. Die beiden Farben brauchen dabei keine physische Benennung, und ein Register aller balancierten Aufteilungen entfällt. Eine Rotation des zyklischen Ursprungs tauscht die maximalen Gruppenspins $k/2$ und wirkt auf deren rechtem Singulett mit $(-1)^k$ für $N=2k$. Permutationen innerhalb der Gruppen ändern diese rechte Linie nicht.

Falls nur die zyklischen Shifts als Eichredundanz identifiziert werden und sie auch links wirken, muss die linke Seite dieselbe Shiftphase $\chi=(-1)^k$ tragen. Der zugehörige Projektor auf $N$ linken Doublets hat Rang

$$
\frac1N\sum_{a=0}^{N-1}\chi^{-a}\,2^{\gcd(N,a)}.
$$

Denn die Spur eines Shifts um $a$ zählt binäre Listen, die auf seinen Zyklen konstant sind. Der Summand $a=0$ liefert $2^N/N$. Jeder andere Summand hat Betrag höchstens $2^{N/2}/N$. Der zyklische Quotient erhält damit den führenden Exponenten $\ln2$ pro Punkt, verändert aber die endliche Zählung. Das unterscheidet ihn vom zuvor ausgeschlossenen Quotienten nach allen Punktpermutationen.

Der Orbit-Scan definiert Shift und Parität auf seinem Scanindex. Die geprüften Horizontstellen r63 und r10 geben den Punktspins und Flächentermen keine solche zyklische Ordnung. Der Nachweis muss daher die Scanindizes mit den gravitativen Durchstoßpunkten verknüpfen und die gruppenübergreifende Kopplung sowie Grundraumauswahl begründen. Die Rechnung setzt keine native zyklische Ordnung voraus.

### Spiegelungen der zyklischen Randordnung

Erkundung. Auf $N=2k$ zyklischen Punktplätzen mit Indizes modulo $N$ wirken die Spiegelungen als $i\mapsto a-i$. Sie erhalten die Zweigruppenkopplung. Bei geradem $a$ erhalten sie beide Gruppen und bei ungeradem $a$ tauschen sie diese. Die rechte Grundlinie trägt daher unter Spiegelung dieselbe Phase $(-1)^{ka}$ wie unter Shift um $a$. Die linke Dimension nach gemeinsamer Diederprojektion ist

$$
\frac1{2N}\sum_{a=0}^{N-1}(-1)^{ka}
\left[2^{\gcd(N,a)}+2^{k+\mathbf1_{\{a\,{\rm gerade}\}}}\right].
$$

Die Spiegelung hat bei geradem $a$ zwei Fixpunkte und bei ungeradem $a$ keine. Die übrigen Punkte bilden Zweierzyklen, woraus der zweite Spurfaktor folgt. Für $N=8$ bleiben bei zyklischer Projektion 36, mit Spiegelungen 30 linke Zustände. Asymptotisch ergibt die Identität $2^N/(2N)$ und die übrigen Beiträge sind insgesamt $O(2^{N/2})$. Der führende Exponent bleibt $\ln2$ pro Punkt. Diese Aussage setzt eine native zyklische Punktordnung und die angegebene gemeinsame Wirkung auf dem linken und rechten Träger voraus; sie belegt weder diese Ordnung noch die Auswahl der rechten Grundlinie durch die QAM.

### Linke Singulettbedingung mit zyklischer oder Diederprojektion

Erkundung. Auf $N=2k$ linken Doublets kommutieren Punktpermutationen mit dem gemeinsamen $SU(2)$. Die Spur einer Punktpermutation $g$ auf dem linken Singulettsektor ist deshalb die Differenz ihrer Spuren auf magnetischer Gesamtsumme null und eins. Jede Kopie eines höheren ganzzahligen Spins trägt denselben Permutationsoperator zu beiden Gewichtsräumen bei. Hat $g$ Zyklenlängen $d_1,\ldots,d_r$, zählen die beiden Spuren in der Produktbasis konstante Vorzeichen auf den Zyklen. Mit $F_g(x)=\prod_i(1+x^{d_i})$ ergibt sich

$$
\operatorname{tr}_{S=0}(g)=[x^k]F_g-[x^{k+1}]F_g.
$$

Setzt man diese Spur statt $2^{\#\text{Zyklen}}$ in die vorigen Charakterprojektionen ein, erhält man die exakten Dimensionen nach beiden Bedingungen. Bei acht Punkten bleiben sowohl für zyklische als auch für Diederprojektion drei linke Singuletts. Die Identität trägt die Catalan-Zahl $\binom{2k}{k}/(k+1)$ bei. Die Nichtidentitätsterme sind nach Division durch die Gruppenordnung insgesamt $O(2^{N/2})$, da jede Nichtidentität höchstens $N/2+1$ Zyklen hat. Die Dimension ist daher asymptotisch Catalan-Zahl geteilt durch $N$ beziehungsweise $2N$. Insbesondere bleibt der führende Exponent $\ln2$ pro Punkt erhalten, während die Unterkorrektur $-5/2\ln N$ beträgt. Der Befund gilt für die linke volle Singulettprojektion und die deklarierten Punktgruppen. Er identifiziert keine dieser Projektionen mit der nativen T-Horizontbedingung.

### Vergleich der linken U(1)- und SU(2)-Schließung

Erkundung. Für die linke U(1)-Bedingung ist die Spur der Punktpermutation $g$ mit Zyklenlängen $d_i$ gleich $[x^k]\prod_i(1+x^{d_i})$. Für SU(2) wird zusätzlich der Koeffizient von $x^{k+1}$ abgezogen. Beide Spuren werden mit derselben rechten Shift- beziehungsweise Spiegelphase projiziert. Bei acht Punkten ergibt U(1) zehn Zustände unter zyklischer und acht unter Diederprojektion. SU(2) ergibt in beiden Fällen drei.

Asymptotisch liefert U(1) ohne Punktquotient die zentrale Binomialzahl und mit zyklischem oder Diederquotient dieselbe Zahl geteilt durch die Gruppenordnung, bis auf exponentiell kleinere Beiträge. Der logarithmische Koeffizient in $\ln\dim$ ist folglich $-1/2$ ohne Punktquotient und $-3/2$ mit Punktquotient. Bei SU(2) sind es entsprechend $-3/2$ und $-5/2$. Der führende Term ist in allen vier Fällen $N\ln2$. Insbesondere ist der Koeffizient $-3/2$ allein im Modell mehrdeutig: Er kommt bei linker SU(2)-Schließung ohne Punktquotient sowie bei U(1)-Schließung mit zyklischem oder Diederquotient vor. Die exakten endlichen Zählungen und die tatsächlich zulässigen Randoperationen müssen bei einem Vergleich zusätzlich angegeben werden.

### Die Zweigruppenkopplung ersetzt den Minimalspinfilter nicht

Erkundung. Erweitere den rechten Zweigruppen-Hamiltonoperator $H=g\mathbf S_A\cdot\mathbf S_B$ auf zugelassene höhere Punktspins, mit derselben positiven Konstante $g$ für beide Belegungen. Für gleiche maximale Gruppenspins $s$ ist seine niedrigste Energie $-gs(s+1)$. Auf der bereits betrachteten exakten dimensionslosen Flächenfaser $A_*=4\sqrt3$ liegen sowohl acht Spin-$1/2$-Punkte als auch zwei Spin-$3$-Punkte. Bei alternierender Zuordnung zu den beiden Gruppen ergeben acht Minimalspinpunkte vier pro Gruppe und damit $s=2$, also $E_0=-6g$. Die beiden Spin-$3$-Punkte ergeben einen pro Gruppe und $s=3$, also $E_0=-12g$. Beide rechten Grundzustände sind Singuletts; links existiert für beide Belegungen ebenfalls ein Gesamtspin-null-Zustand.

Damit bevorzugt die ungeänderte Zweigruppenkopplung auf dieser gemeinsamen Flächenfaser die höhere Spinbelegung. Die Rechnung vergleicht die Energien vor einem zusätzlichen Punktquotienten und setzt voraus, dass Punktzahl und Spinbelegung variieren dürfen. Sie schließt andere Normierungen, eigene Selektoren oder Zusatzterme nicht aus. Sie zeigt aber, dass die Zweigruppenkopplung als Mechanismus für die rechte Multiplizität erst nach einer unabhängig begründeten Minimalspinselektion eingesetzt werden kann, wenn man die bisherige Auslesung erhalten will.

### Skalierungstest für einen lokalen Casimir-Gegenterm

Erkundung. Auf der exakten Fläche $A_k=4k\sqrt3$ vergleiche $8k$ Minimalspinpunkte mit $2k$ Spin-$3$-Punkten. Bei balancierter Zuordnung sind die maximalen Gruppenspins $2k$ beziehungsweise $3k$. Ergänze zur bisherigen Zweigruppenkopplung den lokalen Term $\lambda\sum_p[J_p^2-3I/4]$ mit $\lambda\ge0$. Die Energiedifferenz (Spin-$3$-Belegung minus Minimalspinbelegung) beträgt exakt

$$
\Delta E=-g(5k^2+k)+\frac{45}{2}\lambda k.
$$

Ein fixes $\lambda$ kann die höhere Spinbelegung bei konstantem Paargewicht $g>0$ daher für hinreichend große Fläche nicht verdrängen. Der Austauschgewinn wächst quadratisch, die lokale Strafe nur linear. Dies ist ein Ausschluss für diese feste Normierung und diese Vergleichsfamilie; er benötigt keine vollständige Klassifikation der Flächenfaser.

Skaliert man das Paargewicht auf der gemeinsamen Flächenfaser als $g=g_0/k$, ist für diese Familie die Minimalspinbelegung bei allen $k\ge1$ energetisch bevorzugt, wenn $\lambda>4g_0/15$. In diesem Fall ist die rechte Anregungslücke der reinen Zweigruppenkopplung jedoch $g_0/k$. Die Flächennormierung und der positive lokale Term sind zusätzliche Modellannahmen. Der Vergleich belegt weder eine globale Minimalspinauswahl gegenüber allen Belegungen noch eine native T-Wirkung.

### Gleichmäßige Spinselektion bei inverser Flächennormierung

Erkundung. Betrachte die dimensionslose exakte Fläche $A=\sum_p\sqrt{j_p(j_p+1)}$ mit nichttrivialen Punktspins. Vorausgesetzt sei eine reine Minimalspinbelegung mit gerader Punktzahl und gleich großen Gruppen. Setze $S=\sum_p j_p$, $S_0=A/\sqrt3$ für die reine Minimalspinbelegung und $D=\sum_p[j_p(j_p+1)-3/4]$. Aus $j/\sqrt{j(j+1)}\in[1/\sqrt3,1)$ folgt $S_0\le S\le A$. Außerdem gilt

$$
S-S_0\le (1-1/\sqrt3)D,
$$

denn Minimalspinpunkte tragen zur Differenz nichts bei, und für $j\ge1$ gilt $j\le j(j+1)-3/4$.

Für beliebige Gruppenspins $a,b$ ist $a+b\le S$. Die tiefste Austauschenergie des Blocks ist $-g\min(a,b)(\max(a,b)+1)\ge-g(S/2)(S/2+1)$, weil bei fester Summe das Produkt und der kleinere Summand bei Balance maximal sind. Die reine Minimalspinbelegung erreicht diese Schranke bei $S=S_0$. Daher ist der mögliche Austauschgewinn jeder anderen Belegung höchstens

$$
g(S-S_0)\big[(S+S_0)/4+1/2\big].
$$

Bei $g=g_0/A$ und $A\ge\sqrt3$ ist dies höchstens $g_0 D/(2\sqrt3)$, nach Einsetzen der obigen Schranken. Folglich garantiert $\lambda>g_0/(2\sqrt3)$, dass der lokale Term $\lambda D$ jede Belegung mit einem höheren Spin energetisch abweist. Dies ist eine hinreichende, nicht als scharf beanspruchte Schranke über alle Belegungen auf solchen Flächenfasern. Sie setzt die Zulassung der balancierten reinen Minimalspinbelegung, den Vergleich vor weiteren Punktprojektionen und das Fehlen anderer Energieterme voraus. Die inverse Flächennormierung und die Casimir-Strafe sind zusätzliche Modellannahmen; weder die native T-Dynamik noch die Präparation ihres Grundraums folgt daraus.

### Thermische Grenze der rechten Grundraumauswahl

Erkundung. Beschränke zunächst auf die reine Minimalspinbelegung mit $N=2k$ und $A=k\sqrt3$. Schon im rechten Block mit maximalen Gruppenspins $a=b=k/2$ gibt es für jeden Gesamtspin $S=0,\ldots,k$ genau ein Multiplett mit Entartung $2S+1$. Relativ zum Singulettgrundzustand ist seine Energie $g_0 S(S+1)/(2A)$. Der lokale Casimir-Term verschwindet auf der gesamten Minimalspinbelegung und ändert diese Abstände nicht. Für einen Gibbszustand des Modellhamiltonoperators bei inverser Temperatur $\beta$ gilt deshalb für das rechte Grundgewicht

$$
p_0\le
\left[\sum_{S=0}^k (2S+1)e^{-\beta g_0 S(S+1)/(2A)}\right]^{-1}.
$$

Für festes $\beta g_0>0$ kann man alle Terme bis $L=\lfloor\sqrt{A/(\beta g_0)}\rfloor$ verwenden, sobald $L\le k$ und $A$ hinreichend groß ist. Ihre Exponentialfaktoren sind gleichmäßig nach unten beschränkt, und ihre Multiplizitäten summieren sich zu $(L+1)^2$. Damit ist $p_0=O(A^{-1})$ bei fester Temperatur. Höhere Gruppenblöcke können das Grundgewicht nur weiter senken. Bereits das erste Triplett zeigt, dass $\beta g_0/A\to\infty$ notwendig ist, wenn das Grundgewicht gegen eins gehen soll. Diese notwendige Bedingung wird hier nicht als hinreichend für den gesamten Modellträger beansprucht.

Die Rechnung gilt für Gibbsgewichte des angesetzten rechten Hamiltonoperators vor einer zusätzlichen globalen Projektion. Eine harte rechte Gesamtspin-null-Bedingung entfernt die hier benutzten angeregten Multipletts und verlangt einen eigenen Vergleich. Ebenso kann eine direkte Grundraumselektion die thermische Besetzung umgehen. Die gefundene energetische Bevorzugung begründet daher für sich keine T-Zählung im thermischen Zustand.

### Thermik nach harter rechter Singulettprojektion

Erkundung. Beschränke auf $2k$ Minimalspinpunkte mit $A=k\sqrt3$ und zwei gleich großen Gruppen. Die rechte Gesamtspin-null-Bedingung erzwingt gleiche Gruppenspins $a=b=k/2-d$, $0\le d\le\lfloor k/2\rfloor$. Die Multiplizität pro Gruppe ist $m_d=\binom{k}{d}-\binom{k}{d-1}$, mit $\binom{k}{-1}=0$. Daher gibt es $m_d^2$ rechte Singuletts auf dieser Stufe. Bei Paargewicht $g_0/A$ beträgt der Abstand zur eindeutigen Grundlinie $\Delta_d=(g_0/\sqrt3)d(1+(1-d)/k)$. Schon $d=1$ hat den konstanten Abstand $g_0/\sqrt3$, aber Multiplizität $(k-1)^2$. Das Gibbsgewicht der Grundlinie ist folglich höchstens $[1+(k-1)^2 e^{-\beta g_0/\sqrt3}]^{-1}$. Bei fester positiver Temperatur sinkt es auch nach der harten Projektion auf höchstens $O(k^{-2})$.

Eine Temperaturskala lässt sich für dieses Modell genauer eingrenzen. Setze $b=\beta g_0/\sqrt3$. Für $b\le(2-\eta)\ln k$ mit festem $\eta>0$ erzwingt schon $d=1$ verschwindendes Grundgewicht. Für $b\ge(2+\eta)\ln k$ geht das Grundgewicht gegen eins: Wähle ein festes kleines $\delta>0$ mit $(2+\eta)(1-\delta)>2$. Für $1\le d\le\delta k$ begrenzt $m_d\le k^d/d!$ die relativen Gibbsgewichte durch $k^{-c d}/(d!)^2$ mit $c=(2+\eta)(1-\delta)-2>0$. Für $d>\delta k$ ist der Energieexponent mindestens $b\delta k/2$ und die gesamte Multiplizität höchstens $4^k$. Beide Restbeiträge verschwinden. Der kritische Bereich um $b=2\ln k$ wird hier nicht weiter aufgelöst. Die Rechnung behandelt die rechte projizierte Gibbsstatistik auf einer festen Minimalspinbelegung; zusätzliche Randbedingungen können die Multiplizitäten ändern.

### Thermisches Übergangsfenster der rechten Singuletts

Erkundung. Setze im projizierten Zweigruppenmodell $b=\beta g_0/\sqrt3=2\ln k+c$ mit festem reellem $c$. Für jedes feste $d$ gilt $m_d/k^d\to1/d!$. Zusammen mit dem Energieabstand folgt

$$
m_d^2\exp[-b d(1+(1-d)/k)]\longrightarrow \frac{e^{-cd}}{(d!)^2}.
$$

Der Grenzübergang gilt für die ganze Summe. Für $d\le k/\ln k$ liefert $m_d\le k^d/d!$ eine summierbare Majorante $e^{C d}/(d!)^2$ mit einer nur von $c$ abhängigen Konstanten $C$: Der Korrekturexponent $b d(d-1)/k$ ist dort höchstens linear in $d$. Für $k/\ln k<d\le k/2$ gilt $m_d\le(ek/d)^d$ und $1+(1-d)/k\ge1/2$. Der logarithmische Summand ist damit höchstens $d[2\ln(e\ln k)-\ln k-c/2]$, sodass der gesamte Rest verschwindet.

Das Grenzgewicht der eindeutigen rechten Grundlinie ist folglich

$$
\lim_{k\to\infty}p_0(k)=\left[\sum_{d=0}^{\infty}\frac{e^{-cd}}{(d!)^2}\right]^{-1}.
$$

Bei $c=0$ ergibt sich rund $0{,}4387$. Eine feste additive Verschiebung oberhalb der logarithmischen Schwelle liefert eine feste Reinheit unter eins. Aus Monotonie im inversen Temperaturparameter und der Grenzfunktion folgt zudem: Auf dieser festen Minimalspinbelegung geht das Grundgewicht genau dann gegen eins, wenn $b-2\ln k\to+\infty$; es geht genau dann gegen null, wenn diese Differenz gegen $-\infty$ geht. Die Aussage betrifft Gibbsgewichte nach harter rechter Singulettprojektion. Sie begründet keine native Temperaturwahl oder rechte Projektion.

### Exponentieller Beitrag der rechten Singuletts bei fester Temperatur

Erkundung. Für festes $b=\beta g_0/\sqrt3\ge0$ sei $Z_k$ die rechte Singulett-Zustandssumme relativ zur Grundenergie. Für $x=d/k$ gilt gleichmäßig auf $0\le d\le\lfloor k/2\rfloor$:

$$
\ln m_d=k h(x)+O(\ln k),\qquad h(x)=-x\ln x-(1-x)\ln(1-x).
$$

Dies folgt aus der Binomialabschätzung und $m_d=\binom{k}{d}(k-2d+1)/(k-d+1)$, dessen zusätzlicher Faktor zwischen $1/(k+1)$ und eins liegt. Der Energieexponent beträgt $bkx(1-x)+bx$. Da es nur linear viele Stufen gibt, bestimmt die größte Stufe den Grenzwert

$$
\lim_{k\to\infty}\frac{\ln Z_k}{k}
=\max_{0\le x\le1/2}\{2h(x)-bx(1-x)\}=:f(b).
$$

Für jedes endliche $b$ ist $f(b)>0$: Für kleine positive $x$ wächst $2h(x)/x$ unbeschränkt, während $b(1-x)$ beschränkt bleibt. Das rechte Grundgewicht $1/Z_k$ fällt daher bei fester Temperatur exponentiell. Die frühere polynomial schwächere Schranke verwendete nur eine einzelne angeregte Stufe.

Der Maximierer ist für $b\le4$ bei $x=1/2$, mit $f(b)=2\ln2-b/4$. Für $b>4$ liegt er im Inneren und ist eindeutig. Mit $y=1-2x$ lautet die stationäre Bedingung $b=4\operatorname{artanh}(y)/y$. Die rechte Seite steigt auf $0<y<1$ von vier gegen unendlich, wie die positive Potenzreihe zeigt. Der Vorzeichenwechsel der Ableitung liefert das Maximum. Wenn die linke Zustandszählung unabhängig bleibt, trägt der rechte Faktor zur logarithmierten thermischen Zustandssumme pro Punkt zusätzlich $f(b)/2$ bei. Das ist eine Aussage über die relativ zur Grundenergie normierte Gibbs-Summe, keine Gleichsetzung mit der mikrokanonischen Horizontentropie. Sie gilt für die feste Minimalspinbelegung mit harter rechter Singulettprojektion und dem deklarierten Hamiltonoperator.

### Führendes Zählgewicht und Grundzustandsreinheit

Erkundung. Im projizierten rechten Gibbsmodell sind zwei Grenzforderungen verschieden. Für den führenden Zählbeitrag genügt und ist notwendig, dass $b(k)=\beta g_0/\sqrt3\to\infty$: Dann gilt $k^{-1}\ln Z_k(b(k))\to0$. Zum Beweis ist $Z_k$ monoton fallend in $b$ und mindestens eins. Für jede feste Schranke $B$ liegt der obere Grenzwert daher bei höchstens $f(B)$. Die Funktion $f(B)=\max_x[2h(x)-Bx(1-x)]$ geht gegen null: Außerhalb einer beliebig kleinen Umgebung von null wird der Ausdruck schließlich negativ, innerhalb kann $2h(x)$ beliebig klein gemacht werden. Umgekehrt liefert eine beschränkte Teilfolge $b(k)\le B$ einen positiven unteren Grenzwert $f(B)>0$ entlang dieser Teilfolge.

Auch die rechte Gibbsentropie pro Punkt verschwindet unter derselben Bedingung. Schreibe $Z=\sum_i e^{-b e_i}$ mit dimensionslosen Energien $e_i\ge0$. Dann ist $S_R=\ln Z(b)+b\langle e\rangle_b$. Aus der Konvexität von $\ln Z$ folgt $(b/2)\langle e\rangle_b\le\ln Z(b/2)-\ln Z(b)$. Damit liegt $S_R$ zwischen $\ln Z(b)$ und $2\ln Z(b/2)$. Beide Schranken liefern dasselbe Kriterium für einen verschwindenden Beitrag pro Punkt.

Für Grundzustandsreinheit ist dagegen $b(k)-2\ln k\to+\infty$ erforderlich. Bei $b(k)=\ln k$ verschwindet der rechte Beitrag pro Punkt, obwohl das Gewicht der einzigen rechten Grundlinie gegen null geht. Folglich lässt sich die führende linke Entropie $\ln2$ pro Punkt thermisch reproduzieren, ohne einen scharfen Rang-eins-Träger zu erhalten. Diese Unterscheidung betrifft den deklarierten Gibbsvergleich auf der festen Minimalspinbelegung. Welche Forderung der native T-Horizont stellt, bleibt offen.

### Zwischenregime der rechten Gibbs-Zustandssumme

Erkundung. Setze $b=\alpha\ln k+c$ mit festem $0<\alpha<2$ und $c\in\mathbb R$. Dann ist $t=k e^{-b/2}=e^{-c/2}k^{1-\alpha/2}$ divergent und sublinear. Für die relative rechte Zustandssumme gilt

$$
\ln Z_k=2t+o(t).
$$

Für die untere Schranke genügt die Stufe $d=\lfloor t\rfloor$. Dort ist $\ln m_d=d\ln k-\ln(d!)+O(d^2/k+d/k)$, aus dem Binomialprodukt und dem Faktor $(k-2d+1)/(k-d+1)$. Der quadratische Anteil der Energie liefert eine Korrektur $O(bd^2/k)=o(t)$. Stirling liefert für den einzelnen Logarithmus $2t+o(t)$.

Für die obere Schranke wähle $1-\alpha/2<p<1$ und $D=\lfloor k^p\rfloor$. Bis $D$ ist $m_d\le k^d/d!$ und $bd(d-1)/k\le (bD/k)d$ mit $bD/k=o(1)$. Die Teilsumme ist höchstens $\sum_d (t e^{bD/(2k)})^{2d}/(d!)^2\le\exp(2t e^{bD/(2k)})$. Zwischen $D$ und $k/\ln k$ ist $bd/k$ beschränkt, während $t/d\to0$ gleichmäßig. Mit $d!\ge(d/e)^d$ verschwindet diese Teilsumme. Oberhalb $k/\ln k$ gilt $\ln m_d\le d\ln(e\ln k)$ und der Energieexponent ist mindestens $bd/2$, sodass auch dieser Rest verschwindet.

Bei $b=\ln k$ wächst die rechte Log-Zustandssumme somit wie $2\sqrt k$. Sie ist subextensiv, aber größer als jede logarithmische Korrektur der linken Zählung. Die Aussage betrifft die relativ zur Grundenergie normierte Zustandssumme des projizierten Modells. Sie setzt keinen solchen Temperaturverlauf im nativen T-Frame voraus.

### Gibbsentropie im kritischen Temperaturfenster

Erkundung. Im projizierten Zweigruppenmodell setze $b=2\ln k+c$ mit festem reellem $c$ und $e_d=d(1+(1-d)/k)$. Die zuvor für die Zustandssumme gezeigte Majorisierung gilt auch nach Multiplikation der Summanden mit $e_d$: Im kleinen Bereich genügt der zusätzliche Faktor $d$ in der summierbaren Majorante, und im großen Bereich bleibt selbst ein Faktor $k$ gegenüber dem exponentiellen Abfall unschädlich. Damit konvergiert die mittlere dimensionslose Anregungsenergie gegen

$$
\mu(c)=\frac{\sum_{d\ge0} d\,e^{-cd}/(d!)^2}{\sum_{d\ge0} e^{-cd}/(d!)^2}.
$$

Die rechte Gibbsentropie lautet $S_R=\ln Z_k+b\langle e_d\rangle$. Obwohl $\ln Z_k$ im kritischen Fenster beschränkt bleibt, gilt daher $S_R/\ln k\to 2\mu(c)$. Bei $c=0$ ergibt sich $2\mu(0)\approx1{,}39555$. Wenn der linke Faktor separat und gleichverteilt gezählt wird, addiert sich dieser Beitrag zu dessen logarithmischer Entropiekorrektur. Das ist ein Gibbsvergleich und keine Ableitung einer mikrokanonischen Horizontentropie.

Die rechte Entropie ist bei $b\ge0$ monoton fallend in $b$, denn ihre Ableitung ist $-b\operatorname{Var}_b(e_d)$. Aus dem Fenstergrenzwert und $\mu(c)\to0$ für $c\to+\infty$ folgt deshalb für beliebige nichtnegative Temperaturfolgen: $S_R=o(\ln k)$ gilt genau dann, wenn $b-2\ln k\to+\infty$. Für die Notwendigkeit genügt jede Teilfolge mit $b-2\ln k\le C$, auf der die Entropie mindestens so groß wie bei festem $c=C$ ist. Der Befund gilt für die feste Minimalspinbelegung mit harter rechter Singulettprojektion und schließt die thermische Unterscheidung zwischen führendem und logarithmischem Zählbeitrag in diesem Modell.

### Unruh-Normierung und rechte Kühlschwelle

Erkundung. In der lokalen r10-Statistik ist die inverse Unruh-Temperatur proportional zum Beobachterabstand $\ell$, während die lokale Horizontenergie bei gleicher Flächenanregung proportional zu $1/\ell$ ist. Setzt man für die modellierte Austauschskala dieselbe Rotverschiebung an, $g_0(\ell,k)=\bar g(k)/\ell$, ergibt sich in den Einheiten von r10

$$
b(k)=\beta_U(\ell)g_0(\ell,k)/\sqrt3=2\pi\bar g(k)/\sqrt3.
$$

Eine Änderung des Beobachterabstands allein verändert $b$ damit nicht. Bei flächenunabhängigem $\bar g$ bleibt der rechte thermische Beitrag extensiv, selbst nach harter Singulettprojektion. Für unveränderte logarithmische Gibbsentropie müsste stattdessen $2\pi\bar g(k)/\sqrt3-2\ln k\to+\infty$ gelten oder eine andere Zugriffsregel den Grundraum auswählen. Eine logarithmisch wachsende Kopplung ist aus dem lokalen ersten Gesetz nicht abgeleitet. Dieses Argument setzt die gleiche Rotverschiebung für den angesetzten Austausch voraus und identifiziert seinen Hamiltonoperator nicht mit dem Modularhamiltonoperator.

Auf jedem endlichen zugelassenen Träger ist zudem der Gibbsoperator bei endlicher inverser Temperatur und endlichen Energien strikt positiv. Ein endlicher Energieabstand kann Gewichte unterdrücken, aber keine zuvor zugelassenen Spinsektoren exakt entfernen. Die scharfe Minimalspinzählung verlangt daher einen Projektor, einen eingeschränkten Zustandsraum oder einen geeigneten Grenzprozess. Das sind getrennte Möglichkeiten, deren native Realisierung die r10-Thermik für sich nicht liefert.

### Beobachterzugriff, Flächenobservable und Spinunterstützung

Erkundung. Sei $\rho_M$ ein Zustand mit positivem Gewicht in höheren Spins auf einem endlichen Einpunktträger. Eine reine Einschränkung auf eine unital eingebettete Beobachteralgebra $\mathcal A_T$ übernimmt die Erwartungswerte aller darin enthaltenen Observablen. Bleibt die ursprüngliche Flächenobservable $A=a(J)$ darin enthalten, dann liegen wegen endlicher Spektralinterpolation auch ihre Spinprojektoren $P_j$ darin. Da $a(j)=\sqrt{j(j+1)}$ streng wächst, ist jeder $P_j$ ein Polynom in $A$. Also bleibt insbesondere $\operatorname{tr}(\rho_M P_{j>1/2})$ als zugängliche Wahrscheinlichkeit erhalten. Eine Beschränkung auf weniger Observablen kann dieses Gewicht unter diesen Voraussetzungen nicht entfernen. Das Argument gilt auch nach einem invertierbaren Framewechsel, wenn Zustand und Observable gemeinsam transportiert werden.

Eine Projektion auf den Minimalspin ist dagegen ein eigener Auswahlzweig $\rho\mapsto P_{1/2}\rho P_{1/2}$. Sein Spurfaktor $p=\operatorname{tr}(\rho P_{1/2})$ bleibt Teil des Instruments; erst konditioniert auf Erfolg ergibt sich der normierte Minimalspinzustand. Ein Zugriff, der die ursprüngliche Fläche nicht enthält, kann die Spinsektoren ununterscheidbar machen, begründet aber ohne zusätzliche Definition keine neue Flächenstatistik. Die r06/r07-Lesart der Beobachterbeschränkung liefert somit keinen Minimalspinselektor, solange dieselbe gravitative Flächenobservable zugänglich bleibt. Für eine native T-Route braucht es eine begründete Selektion, eine neue Ausleseobservable oder einen eigenständig definierten Randzustand. Die Rechnung ist eine endliche Modellfolgerung und setzt keine konkrete T-Algebra voraus.

### Aktiver T-Kanal und Erhaltung der Einpunktfläche

Erkundung. Sei $A=\sum_j a(j)P_j$ die ursprüngliche Einpunktfläche in gemeinsamen Einheiten, auf einem endlichen Träger ohne Spin null. Ein deterministischer Quantenkanal $\Phi$ mit ausschließlich minimalem Ausgang hat $\Phi^*(P_{1/2})=I$ und daher $\Phi^*(A)=a(1/2)I$. Sobald höhere Spins zugelassen sind, kann er die Fläche nicht für alle Eingaben erhalten. Für jeden Eingang mit höherem Spingewicht $w=\operatorname{tr}[\rho(I-P_{1/2})]$ ist die Differenz der Flächenerwartungswerte mindestens $(a(1)-a(1/2))w$. Ist der Ausgang nur näherungsweise minimal, mit höherem Gewicht $\varepsilon$, ergibt die Messung des binären Ereignisses höherer Spin einen Abstand der Flächenverteilungen in Totalvariation von mindestens $|w-\varepsilon|$. Diese Schranke setzt keine unitäre oder passive Umsetzung voraus.

Ein selektives Instrument kann die ursprüngliche Flächenstatistik dagegen über beide Ausgänge hinweg erhalten. Für $P=P_{1/2}$ und $Q=I-P$ lauten die unnormierten Zweige $P\rho P$ und $Q\rho Q$. Weil $A$ und seine Spektralprojektoren mit $P,Q$ kommutieren, ergibt ihre Summe dieselben ursprünglichen Flächenwahrscheinlichkeiten wie der Eingang. Konditioniert auf Ja ist die Fläche minimal. Damit ist eine genaue Unterscheidung möglich: Der gemeinsame, nichtselektive Vorgang kann die Fläche erhalten, während nur der Ja-Zweig die Minimalspin-Zählung trägt. Eine native Identifikation von T mit genau diesem Zweig müsste den Selektor und sein Eingangsgewicht erklären. Die Aussage betrifft die Einpunktfläche, nicht automatisch eine Gesamtfläche bei veränderlicher Punktzahl oder eine neu kalibrierte T-Observable.

### Flächengleiche Punktaufspaltung und Drehimpulserhaltung

Erkundung. Auf einer Minimalspin-Flächenfaser muss für jeden Punkt der Quotient $r=a(j)/a(1/2)$ ganzzahlig sein, wie bereits in der quadratfreien Faseranalyse gezeigt. Dann ist eine Aufspaltung in $r$ Minimalspinpunkte zwar flächengleich, kann aber für $j>1/2$ keinen lokalen $SU(2)$-Intertwiner liefern. Der größte Gesamtspin der $r$ Doublets ist $r/2$, während

$$
j>r/2\quad\Longleftrightarrow\quad 3j>j+1
$$

für $j>1/2$ gilt. Schon beim einfachsten Beispiel $j=3$ können vier Doublets höchstens Spin zwei tragen. Auch ein kovarianter Kanal mit einer Stinespring-Realisierung und einem anfangs invarianten Hilfszustand braucht im Ausgangsumfeld mindestens einen Spin $j-r/2$, damit der Eingangsspin in der gemeinsamen Darstellung überhaupt vorkommt. Falls dieser Rest selbst als gravitativer Flächenbeitrag gezählt wird, muss seine Fläche in die Bilanz aufgenommen werden.

Für die vollständige ungefilterte Mehrpunktfaser gilt analog: Eine Belegung mit höherem Spin besitzt einen maximalen Gesamtspin $\sum_p j_p>N/2$, wobei $N=\sum_p r_p$ die flächengleiche Zahl der Minimalspinpunkte ist. Der reine Minimalspinträger enthält diesen Sektor nicht. Das Argument schließt keinen Übergang auf einem vorab eingeschränkten globalen Singulettträger aus, weil dort der maximale Gesamtspin bereits entfernt wurde. Es trennt somit arithmetische Flächengleichheit von der Möglichkeit einer nativen, lokal drehimpulserhaltenden Aufspaltung.

### Dimensionsgrenze nach globaler Singulettprojektion

Erkundung. Die bereits vollständig klassifizierte Faser bei $A=4\sqrt3$ enthält im betrachteten Tensorproduktmodell 14 Singuletts aus acht Minimalspinpunkten und ein weiteres Singulett aus zwei Spin-$3$-Punkten. Die gemischte Belegung liefert kein Singulett. Der Eingangsraum hat damit Dimension 15, das ausschließlich minimale Ausgabe-Singulettbild Dimension 14. Die Drehimpulsobstruktion aus der vorigen Rechnung entfällt, aber eine reversible oder isometrische Umwandlung aller Eingaben auf denselben Minimalspinträger bleibt dimensionsbedingt unmöglich.

Ein deterministischer Quantenkanal kann den Übergang auf dieser Faser mit einem zweidimensionalen Umfeld realisieren. Er bettet jeden der 14 Minimalspinzustände als denselben Zustand mit Umfeldflag null ein. Das Spin-$3$-Singulett wird auf einen ausgewählten Minimalspinzustand mit Umfeldflag eins abgebildet. Die 15 Bilder sind orthogonal, haben dieselbe Gesamtfläche und tragen insgesamt Spin null, wenn das Flag rotationsinvariant ist. Das Flag ist also ein hinreichender zusätzlicher Träger und Dimension zwei zugleich notwendig, da $14\dim\mathcal H_{\rm Umfeld}\ge15$ gelten muss. Nach Ignorieren des Flags gehen die Kohärenzen zwischen den beiden Belegungszweigen verloren.

Für einen selektiven Ja-Zweig mit nur einem Krausoperator $K$ in den 14-dimensionalen Raum gilt $\operatorname{tr}(K^\dagger K)\le14$. Bei gleichverteilter Eingabe auf der ganzen Faser ist die Ja-Wahrscheinlichkeit daher höchstens $14/15$; der einfache Minimalspinprojektor erreicht dies. Mehrere Krausoperatoren können den Erfolg erhöhen, wenn ein zusätzliches Register die Zweige trägt. Diese Grenze setzt exakt die angegebene Faser, den ausgewählten Ausgabe-Singulettträger und die gleichverteilte Eingabe voraus. Der konstruktive Kanal belegt keine native QAM-Realisierung und kann nicht als bloße Umbenennung der beiden Belegungen gelesen werden.

### Der zusätzliche Träger muss auf großen Flächen wachsen

Erkundung. Verwende das geordnete Tensorproduktmodell auf der exakten Faser $A=N a(1/2)$ und nehme $N$ als Vielfaches von 128. Setze $m=N/64$, also gerade. Die reine Minimalspinbelegung hat $N$ Punkte und Singulettdimension $D_0=\binom N{N/2}/(N/2+1)$. Eine flächengleiche Mischbelegung besteht aus $m$ Spin-$3$-Punkten und $N-4m$ Minimalspinpunkten. Es gibt $\binom{N-3m}{m}$ orthogonale geordnete Spinlisten. Je Liste kann man die Spin-$3$-Punkte disjunkt zu Singuletts koppeln und unabhängig jedes Singulett der verbleibenden Minimalspinpunkte verwenden. Damit ist die Zahl der Misch-Singuletts mindestens

$$
D_{\rm mix}\ge\binom{N-3m}{m}\frac{\binom{N-4m}{(N-4m)/2}}{(N-4m)/2+1}.
$$

Aus $\binom{L}{m}\ge(L/m)^m$ folgt hier der Faktor $61^m$. Das Verhältnis der beiden Catalan-Zahlen ist nach Stirling ein positiver asymptotisch konstanter Faktor mal $2^{-4m}$. Also wächst $D_{\rm mix}/D_0$ mindestens proportional zu $(61/16)^{N/64}$. Eine isometrische Einbettung der gesamten Eingangsfaser in einen ausschließlich minimalen Ausgang mit zusätzlichem Register benötigt deshalb mindestens $\log_2\dim\mathcal H_{\rm Umfeld}\ge (N/64)\log_2(61/16)-O(1)$ Bits an Zustandskapazität. Dieselbe Dimensionsgrenze gilt für die Stinespring-Einbettung eines deterministischen Kanals auf dieser Faser. Ein einzelner selektiver Krausoperator hat bei gleichverteilter Eingabe höchstens $D_0/(D_0+D_{\rm mix})$ Erfolg; dieser obere Wert fällt exponentiell.

Das Argument benutzt nur eine Teilfamilie der Eingänge. Es setzt orthogonale geordnete Listen, globale $SU(2)$-Schließung, einen reinen Minimalspin-Ausgang derselben exakten Fläche und keine zusätzlichen Punktquotienten voraus. Andere Zählmaße oder ein bereits eingeschränkter Eingangsträger können die Schranke ändern. Die native QAM müsste daher neben dem zusätzlichen Kanal auch begründen, welche Eingangsfaser tatsächlich zugänglich ist.

### Kapazitätsgrenze nach zyklischem Punktquotienten

Erkundung. Verwende dieselbe Mischfamilie mit $m=N/64$ und Listenlänge $L=N-3m$. Die zyklische Gruppe $C_L$ verschiebt die Listen und transportiert die zugehörigen Tensorfaktoren. Eine Liste mit trivialem Stabilisator erzeugt einen Orbit aus $L$ orthogonalen Listensektoren. Ihr invarianter Raum hat dieselbe Dimension wie ein einzelner Listensektor: Jeder Vektor auf einer Repräsentantenliste setzt sich eindeutig durch zyklische Translation fort. Das gilt auch für eine vorgegebene zyklische Charakterphase, sofern sie ein Charakter von $C_L$ ist.

Ein nichtidentischer Shift der Ordnung $q\ge2$ kann eine Liste nur fixieren, wenn $q$ sowohl $L$ als auch $m$ teilt. In diesem Fall fixiert er genau $\binom{L/q}{m/q}$ Listen. Mit $p=m/L=1/61$ ist diese Zahl höchstens $\exp[L h(p)/2]$, wobei $h$ die binäre Entropiefunktion in natürlichen Logarithmen ist. Die Gesamtzahl $\binom Lm$ wächst dagegen wie $\exp[Lh(p)+O(\ln L)]$. Selbst die Summe über alle nichttrivialen Shifts ist asymptotisch vernachlässigbar. Daher bleiben asymptotisch $\binom Lm/L$ freie Orbits. Pro Orbit steht mindestens die bereits verwendete Catalan-Zahl der Minimalspinreste zur Verfügung.

Die reine minimale Ausgabedimension nach zyklischer Projektion ist höchstens die unprojizierte Dimension $D_0$. Der Quotient kostet im Eingang daher höchstens einen polynomialen Faktor in der bisherigen unteren Schranke: Die Zustandskapazität des Umfelds bleibt mindestens $(N/64)\log_2(61/16)-O(\ln N)$ Bits. Voraussetzung ist, dass die zyklische Identifikation je Listenlänge wirkt und verschiedene freie Orbits weiterhin orthogonale Eingangssektoren sind. Die Rechnung setzt keine native zyklische Punktordnung voraus und gilt nicht für einen Quotienten nach sämtlichen Punktpermutationen.

### Kapazitätsgrenze nach Diederquotient

Erkundung. Ergänze die zyklischen Shifts auf den Listen der Länge $L=N-3m$ durch Spiegelungen. Eine Spiegelung hat höchstens zwei Fixpunkte; alle übrigen Zyklen sind Paare. Eine fixierte Spinliste mit $m$ höheren Spins muss daher nach der Wahl der höheren Spins auf den Fixpunkten ganze Zweierzyklen belegen. Für $m/L=p=1/61$ ergibt das höchstens $\exp[(L/2)h(p)+O(\ln L)]$ Listen je Spiegelung, aus der Binomialabschätzung und den höchstens vier Fixpunktwahlen. Auch die Vereinigung aller Spiegelungs- und Shiftfixmengen ist damit gegenüber $\binom Lm$ exponentiell kleiner. Die Zahl der freien Diederorbits ist asymptotisch $\binom Lm/(2L)$. Auf jedem freien Orbit kann ein beliebiger Vektor des Repräsentantensektors zu einem invarianten Vektor fortgesetzt werden.

Mit $m=N/64$ und der zuvor verwendeten Catalan-Untergrenze pro Liste folgt für die erforderliche Umfeldkapazität nun die schärfere Schranke

$$
\log_2\dim\mathcal H_{\rm Umfeld}
\ge N\left[\frac{61}{64}H_2(1/61)-\frac1{16}\right]-O(\log N),
$$

wobei $H_2$ die binäre Entropie mit Logarithmus zur Basis zwei bezeichnet. Der Koeffizient beträgt rund $0{,}05252$ Bit pro Minimalspin-Flächeneinheit. Die Schranke gilt ebenso ohne Spiegelungen und verwendet die volle unprojizierte Minimalspindimension als Obergrenze für den möglichen Ausgang. Sie betrifft den geordneten Modellträger modulo der jeweils auf die Listenlänge wirkenden Diedergruppe. Ein nativer Quotient, der auch verschiedene freie Orbits identifiziert oder ihre Singulettsektoren beschränkt, ist nicht durch dieses Argument erfasst.

### Optimierte Mischfamilie für die Umfeldkapazität

Erkundung. Lasse in derselben Konstruktion die Dichte $\rho=m/N$ zwischen null und $1/4$ variieren. Die Singulett-Untergrenze pro Liste und die freie zyklische oder Dieder-Orbitzählung ergeben für jede feste innere Dichte den Exponenten

$$
F(\rho)=(1-3\rho)H_2\!\left(\frac{\rho}{1-3\rho}\right)-4\rho
$$

für das Verhältnis zur reinen Minimalspin-Ausgabedimension. Rundung von $m$ auf eine gerade Zahl bei geradem $N$ ändert den Exponenten nur um $O(\log N)$. Setze $p=\rho/(1-3\rho)$, den Spin-$3$-Anteil unter den Listeneinträgen. Dann ist $1+F=(H_2(p)+1-p)/(1+3p)$.

Sei $z\in(0,1/2)$ die eindeutige Lösung von $2z+z^4=1$. Vergleiche die Bernoulli-Verteilung $(1-p,p)$ mit $(2z,z^4)$. Die Nichtnegativität der relativen Entropie liefert $H_2(p)+1-p\le-(1+3p)\log_2 z$, mit Gleichheit genau bei $p=z^4$. Daher maximiert diese Dichte die bewiesene Untergrenze und ergibt $F_{\max}=-\log_2 z-1$. Die Optimierung betrifft ausschließlich die Mischfamilie mit Spin $1/2$ und Spin $3$ und einer ausgewählten Singulettkopplung der höheren Spins je Liste. Zusätzliche Belegungen oder höhere Multiplizitäten können die tatsächliche Kapazität weiter erhöhen.

### Interne Spin-3-Singuletts verschärfen die Kapazitätsgrenze

Erkundung. Für gerades $m=2s$ zerlege die erste Hälfte der Spin-$3$-Faktoren in $V_3^{\otimes s}=\bigoplus_{j=0}^{3s} V_j\otimes\mathbb C^{n_j}$. Die zweite Hälfte hat dieselbe Zerlegung. In der gemeinsamen Kopplung enthält genau jedes Paar gleicher Spins ein Singulett. Die Zahl der Spin-$3$-Singuletts ist daher $\sum_j n_j^2$. Cauchy-Schwarz und $\sum_j(2j+1)n_j=7^s$ geben

$$
\frac{7^m}{\sum_{j=0}^{3s}(2j+1)^2}
\le\sum_j n_j^2\le 7^m.
$$

Die interne Spin-$3$-Zählung liefert somit $m\log_2 7-O(\log m)$ Bits pro Liste. Man kann diese Singuletts unabhängig mit allen Singuletts der Minimalspinreste kombinieren. Auf einem freien zyklischen oder Diederorbit setzt sich der gesamte so konstruierte Unterraum vom Repräsentanten fort. Die vorige Orbitabschätzung bleibt unverändert.

Mit $p=m/(N-3m)$ ist der optimierte Logarithmus der Eingangsdimension pro Minimalspin-Flächeneinheit mindestens das Maximum von $[H_2(p)+(1-p)+p\log_2 7]/(1+3p)$. Die relative Entropie zu $(2z,7z^4)$ liefert das Maximum $-\log_2 z$ bei $p=7z^4$, wobei $2z+7z^4=1$. Nach Abzug der maximalen reinen Ausgabekapazität von einem Bit pro Flächeneinheit folgt die entsprechende Untergrenze $N[-\log_2 z-1]-O(\log N)$. Dies verwendet weiterhin nur zwei Spinarten und getrennte Singulettbildung der beiden Spinarten; eine vollständige Faserzählung ist damit nicht behauptet.

### Exakte exponentielle Kapazitätsrate im geordneten Faser-Modell

Erkundung. Die auf $A=N a(1/2)$ möglichen Spinarten entsprechen den positiven Lösungen $d^2-3r^2=1$, mit $d=2j+1$ und Flächengewicht $r$. Die ersten Paare $(r,d)$ sind $(1,2),(4,7),(15,26),(56,97)$. Sei $z_*$ die eindeutige Lösung von $\sum_r d_r z_*^r=1$ in $(0,1/2)$. Die Reihe konvergiert dort, denn $d_r\le2r$. Für die Summe $W_N$ der vollen Tensorproduktdimensionen aller geordneten Listen gilt $W_0=1$ und $W_N=\sum_{r\le N}d_r W_{N-r}$. Induktion liefert $W_N\le z_*^{-N}$. Dies ist auch eine Obergrenze für die Singulettdimension, vor oder nach Punktquotienten.

Für die untere Exponentenabschätzung wähle zunächst endlich viele Spinarten einschließlich Minimalspin. Sei $z_F$ die Wurzel der abgeschnittenen Summe und $p_r=d_r z_F^r$ die normierte Liste der Anteile. Für gerades $N$ wähle gerade Anzahlen jeder Spinart mit diesen asymptotischen Listenanteilen und fülle einen beschränkten Flächenrest mit einer geraden Anzahl Minimalspinpunkte auf. Je Spinart liefert die Halbierungs- und Cauchy-Schwarz-Abschätzung aus dem vorigen Abschnitt mindestens $d_r^{m_r}$ dividiert durch einen polynomialen Faktor an Singuletts. Zusammen mit der Multinomialzahl der Listen ergibt dies den Exponenten $-\log_2 z_F$ pro Flächeneinheit. Denn $H_2(p)+\sum_r p_r\log_2 d_r=-(\sum_r rp_r)\log_2 z_F$.

Auch unter zyklischer oder Diederidentifikation bleibt dieser Exponent bestehen: Für die feste endliche Zusammensetzung haben Listen mit nichttrivialem Stabilisator höchstens halb so viele frei belegbare Zyklen, bis auf höchstens zwei Fixpunkte bei Spiegelung. Ihre Multinomialzahlen sind exponentiell kleiner als die volle Listenzahl, sofern mindestens zwei Arten positive Anteile haben. Auf den freien Orbits bleibt der volle Singulettunterraum einer Repräsentantenliste verfügbar. Lässt man die endliche Spinmenge wachsen, folgt $z_F\downarrow z_*$. Damit ist auf geraden Flächenindizes die exakte Eingangs-Exponentenrate $-\log_2 z_*$ bewiesen, auch für die deklarierten zyklischen oder Diederinvarianten. Die reine Minimalspin-Ausgabedimension hat in diesen Fällen Exponent eins. Der kleinste mögliche Umfelddimensionsfaktor eines abstrakten deterministischen Kanals ist $\lceil D_{\rm in}/D_{\rm out}\rceil$; auf den Spin-null-Trägern genügt eine beliebige isometrische Einbettung in den Ausgaberaum mal rotationsinvariantes Umfeld. Seine asymptotische Rate ist folglich $-\log_2 z_*-1$ Bit pro Flächeneinheit. Diese Rate setzt die vollständige Modellfaser und das deklarierte Zählmaß voraus. Sie begründet weder eine native Punktidentifikation noch einen physikalisch ausführbaren Kanal.

### Exakte Flächenfaser und r63-Normierung

Erkundung. Die vorige Kapazitätsrate verwendet volle Irrep-Dimensionen $d_r=2j+1$ und ausschließlich die Spinarten mit $a(j)/a(1/2)=r\in\mathbb N$. Für einen Vergleich mit r63 müssen beide Änderungen getrennt werden. Setze $z=e^{-2\pi\gamma a(1/2)}$. Mit dem r63-Gewicht zwei, aber weiterhin nur auf der exakten Minimalspin-Flächenfaser, lautet die entsprechende Listennormierung $\sum_{r\in\mathrm{Pell}}2z^r=1$. Ihr Verhältnis zur Minimalspin-Normierung ist $-\log_2 z$. Die volle r63-Gleichung enthält dagegen zusätzlich alle positiven nichtganzzahligen Flächenquotienten $a(j)/a(1/2)$. Bei gleicher Gewichtung sind diese zusätzlichen Terme positiv, sodass ihre Nullstelle strikt kleiner und der r63-Normierungsquotient strikt größer ist.

Der Unterschied zwischen exakter Faser und voller r63-Zählung besteht also schon bei gleichem Gewicht zwei. Die Rechnung über $d_r$ liefert eine Dimensionsrate für einen flächengleichen Kanal im Tensorproduktmodell. Sie darf nicht als Herleitung der Barbero--Immirzi-Normierung interpretiert werden. Für eine native Brücke müsste man die tatsächlich verwendete Flächenauflösung und das Zählmaß deklarieren. Insbesondere ist eine exakte Flächenfaser mit einer Fläche in einem endlichen Fenster nicht gleichzusetzen.

### Festes Flächenfenster gewinnt den vollen Listenexponenten zurück

Erkundung. Verwende geordnete Spinlisten mit Gewicht zwei je Punkt und Flächeneinheiten $r_j=a(j)/a(1/2)$. Sei $D_N(\delta)$ das gewichtete Zählmaß im Fenster $[N,N+\delta]$ für festes $\delta>0$ und ganzzahliges $N$. Setze $s_*$ durch $\sum_{j>0}2e^{-s_*r_j}=1$. Für $s>s_*$ ist die Summe der Boltzmanngewichte aller Listen eine konvergente geometrische Reihe mit Quotient $\sum_j2e^{-sr_j}<1$. Da jede Liste im Fenster Gewicht mindestens $e^{-s(N+\delta)}$ relativ zu ihrem Zählgewicht hat, folgt $\limsup N^{-1}\ln D_N(\delta)\le s_*$.

Für die untere Schranke wähle eine endliche Spinmenge einschließlich $j=1/2$ und $j=1$ mit Normierung $s_F$ und Listenanteilen $p_j=2e^{-s_Fr_j}$. Wähle ganzzahlige Anzahlen nahe $Np_j/\sum_i p_i r_i$; der Flächenfehler ist beschränkt. Der Quotient $r_1=\sqrt{8/3}$ ist irrational. Endlich viele Vielfache von $r_1$ bilden modulo eins ein hinreichend feines Netz, sodass eine beschränkte Änderung der Spin-1-Anzahl den verbleibenden Flächenrest modulo eins in das Zielfenster legt. Eine weitere beschränkte Änderung der Minimalspinanzahl füllt den ganzzahligen Rest auf. Beide Anzahlen wachsen linear mit $N$, sodass die Änderungen bei großen $N$ zulässig sind. Die angepassten Listen behalten dieselben asymptotischen Anteile und ihre gewichtete Multinomialzahl hat nach Stirling Exponent $s_F N+o(N)$. Durch Vergrößern der Spinmenge folgt $s_F\uparrow s_*$.

Damit gilt für jedes feste positive Fenster der volle Listenexponent $s_*$. In Minimalspin-Normierung ist dies genau die r63-Skalargleichung, sofern das Gewicht zwei und die geordnete Listenzählung vorausgesetzt werden. Beim exakten Fenster der Breite null gilt stattdessen der zuvor gefundene Pell-Exponent. Die Grenzwerte der Fensterbreite null und der großen Fläche sind in diesem Sinn nicht austauschbar. Diese Rechnung berücksichtigt keine zusätzliche Horizontprojektion und leitet weder die native Fensterbreite noch die T-Auswahl her.

### Schrumpfende Flächenfenster mit magnetischer Neutralität

Erkundung. Sei $N$ gerade und $\delta_N>0$ mit $\delta_N\to0$ und $N\delta_N\to\infty$. Im geordneten Modell mit zwei magnetischen Labels $m=\pm j$ pro Punkt bleibt der volle r63-Listenexponent auch unter der zusätzlichen U(1)-Bedingung $\sum m=0$ erhalten. Die obere Schranke folgt wie zuvor durch Weglassen der Neutralitätsbedingung.

Für die untere Schranke fixiere eine endliche Spinmenge einschließlich $1/2$ und $1$. Runde die optimalen Anzahlen jeder Spinart auf gerade Zahlen. Der Flächenfehler bleibt beschränkt. Durch Änderungen um jeweils zwei Punkte kann man den Flächenrest modulo zwei mit dem irrationalen Quotienten $\alpha=\sqrt{8/3}$ korrigieren. Die benötigte Zahl der Änderungen ist $O(1/\delta_N)$. Hierzu liefert die elementare Dirichlet-Approximation für jedes große $Q$ einen gekürzten Bruch $p/q$ mit $1\le q\le Q$ und $|\alpha-p/q|\le1/(qQ)$. Weil $3p^2-8q^2$ eine von null verschiedene ganze Zahl ist, gilt zugleich $|\alpha-p/q|\ge C/q^2$ für eine feste Konstante $C>0$. Damit ist $q\ge CQ$. Die ersten $q$ Vielfachen von $\alpha$ unterscheiden sich auf dem Einheitskreis um höchstens $1/Q$ von den entsprechend permutierten Gitterpunkten der Schrittweite $1/q$. Ihr maximaler Abstand zu einem beliebigen Ziel ist damit $O(1/Q)$. Wähle $Q$ proportional zu $1/\delta_N$ und ziele auf die Fenstermitte modulo zwei. Danach passt eine Änderung der Minimalspinanzahl um ein gerades ganzzahliges Maß die Gesamtfläche an. Beide Änderungen sind $o(N)$ und lassen die asymptotischen Listenanteile bestehen.

Auf jeder so gewonnenen Liste wähle für jede Spinart genau die Hälfte ihrer magnetischen Vorzeichen positiv. Dies erfüllt die globale Neutralität und liefert mindestens $\prod_j\binom{n_j}{n_j/2}$ zulässige Zuweisungen. Bei fester endlicher Artenzahl unterscheidet sich ihr Logarithmus von $(\sum_j n_j)\ln2$ nur um $O(\ln N)$. Stirling liefert daher denselben führenden Exponenten wie ohne Neutralität, und das Vergrößern der endlichen Artenmenge liefert den vollen r63-Wert. Die Bedingung $N\delta_N\to\infty$ ist hinreichend. Engere Fenster, volle SU(2)-Schließung und eine native T-Zugriffsregel werden dadurch nicht entschieden.

### Schrumpfende Flächenfenster mit voller SU(2)-Schließung

Erkundung. Auf dem geordneten Modellträger mit einem vollen Spin-$j$-Irrep pro Punkt sei $D_N^{\rm sing}(\delta_N)$ die Summe der globalen Singulettdimensionen im Flächenfenster $[N,N+\delta_N]$. Die Flächeneinheit ist wieder $a(1/2)$. Für gerade $N$, $\delta_N\to0$ und $N\delta_N\to\infty$ gilt

$$
\lim\frac1N\ln D_N^{\rm sing}(\delta_N)=s_{SU(2)},\qquad
\sum_{j>0}(2j+1)e^{-s_{SU(2)}r_j}=1.
$$

Für die obere Schranke genügen die vollen Produktdimensionen. Die geometrische Listensumme konvergiert für jedes $s>s_{SU(2)}$. Für die untere Schranke fixiere eine endliche Spinmenge mit Minimalspin und Spin eins, wähle Listenanteile proportional zu $(2j+1)e^{-s_F r_j}$ bei abgeschnittener Normierung $s_F$, und verwende die gerade Rundung und Flächenkorrektur aus dem vorherigen Abschnitt. Sie ändert $o(N)$ Punkte. Für jede Spinart mit gerader Anzahl $n_j$ zerlege die Hälfte ihrer Faktoren in Irreps mit Multiplizitäten $m_s$. Die Singulettdimension der beiden Hälften ist $\sum_s m_s^2\ge(2j+1)^{n_j}/\sum_s(2s+1)^2$. Für festes $j$ und $s\le jn_j/2$ ist der Nenner polynomial in $N$. Das Produkt solcher Singuletts über endlich viele Spinarten liegt im vollen globalen Singulettsektor. Der Verlust gegenüber den Produktdimensionen ist daher nur polynomial, und die geordneten Listen liefern durch Stirling den Exponenten $s_F$. Vergrößern der Spinmenge ergibt die Behauptung.

Der Exponent unterscheidet sich von der Zwei-Label-Normierung, weil bei jedem $j>1/2$ das lokale Gewicht $2j+1$ strikt größer als zwei ist. Die globale Singulettprojektion ändert in diesem Modell den führenden Exponenten der vollen Irrep-Zählung nicht. Sie kann daher die Differenz zu r63 nicht allein erklären. Die Rechnung behandelt keine native Horizonttheorie mit zusätzlichen Randbedingungen oder endlichem Niveau.

### Umfeldkapazität bei Erhaltung eines Flächenfensters

Erkundung. Ersetze die Forderung nach Erhaltung des exakten Flächeneigenwerts durch Erhaltung des Fensters $[N,N+\delta_N]$ mit geradem $N$, $\delta_N\to0$ und $N\delta_N\to\infty$. Ein reiner Minimalspinausgang in diesem Fenster hat für große $N$ genau $N$ Punkte, weil ihre dimensionslose Fläche ganzzahlig ist. Sowohl seine magnetisch neutrale Zwei-Label-Dimension als auch seine volle Singulettdimension wachsen wie $2^{N+o(N)}$. Der Eingangsexponent ist in den beiden vorigen Modellzählungen dagegen $s/\ln2$ Bit pro Flächeneinheit.

Für einen abstrakten deterministischen Kanal auf dem jeweiligen Fensterträger gilt daher $\dim\mathcal H_{\rm Umfeld}\ge\lceil D_{\rm in}/D_{\rm out}\rceil$. Eine beliebige isometrische Einbettung erreicht diese Dimensionsgrenze, wenn keine weitere Dynamik oder Unterscheidung der exakten Flächenwerte verlangt wird. Im vollen Singulettmodell können die Eingangs- und Ausgabeträger als Spin-null-Räume behandelt werden. Die asymptotische Umfeldrate ist $s/\ln2-1$. Mit den r63-Normierungswerten ergeben sich etwa $0{,}86470$ Bit pro Minimalspin-Flächeneinheit für das U(1)-Zwei-Label-Modell und $1{,}15150$ für das volle SU(2)-Modell. Die Zahlen sind dimensionsbedingte Kanalraten unter den deklarierten Zählmaßen, keine zusätzliche BI-Herleitung.

Für das volle Spinmodell ist diese Rate deutlich größer als $0{,}302498$ auf der einzelnen exakten Pell-Faser. Obwohl die Fensterbedingung für den Kanal schwächer ist, umfasst sein Eingangsraum exponentiell mehr Zustände. Falls die Dynamik den exakten Flächenwert statt nur des Fensters bewahrt, kann dieser Kanal die Eingaben mit nichtganzzahligen Flächenquotienten im Allgemeinen nicht auf den Minimalspinausgang abbilden. Der Nachweis eines nativen Fensterinstruments und seines Umfelds bleibt offen.

### Flächenbilanz des Umfelds beim Fensterkanal

Erkundung. Auf dem Eingangsfenster $[N,N+\delta_N]$ mit $0<\delta_N<1$ hat der reine Minimalspinausgang exakt Fläche $N$. Sei das Umfeld anfangs flächenneutral und die gemeinsame Flächenobservable im Ausgang additiv, $A_{\rm out}\otimes I+I\otimes A_E$. Eine isometrische Umsetzung, die den exakten Gesamtflächenoperator verschränkt, muss jeden Eingangssektor der Fläche $N+\epsilon$ in den Umfeld-Eigenraum der Fläche $\epsilon$ abbilden. Für seine Dimension gilt notwendig

$$
D_{\rm in}(N+\epsilon)\le D_{\rm out}(N)\,\dim\ker(A_E-\epsilon I).
$$

Umgekehrt reichen diese Dimensionsbedingungen für eine abstrakte flächenerhaltende Isometrie aus, wenn keine weiteren Symmetrien oder Lokalitätsbedingungen verlangt werden: Jeder Eingangssektor kann separat in sein orthogonales Produktbild eingebettet werden. Auf einem Fenster mit endlich vielen Eigenwerten ist daher die kleinste Umfelddimension bei frei wählbarem Umfeldspektrum $\sum_\epsilon\lceil D_{\rm in}(N+\epsilon)/D_{\rm out}(N)\rceil$. Dies ist stärker als die vorherige Gesamtdimensionsbedingung, die nur das Fenster erhielt.

Hat das Umfeld selbst dasselbe nichtnegative gravitative Flächenspektrum mit kleinster positiver Stufe eins, kann es keinen Rest $0<\epsilon<1$ aufnehmen. Auch eine große interne Multiplizität bei Fläche null hilft dabei nicht. In der untersuchten Fensterfolge gibt es tatsächlich solche nichtganzzahligen Eingangseigenwerte: Der volle Fensterexponent ist größer als der der exakten Faser, und diese Faser ist der einzige ganzzahlige Flächenwert im Fenster. Ein exakter Kanal für die ganze Fensterfaser braucht somit einen Träger mit passenden kleinen Flächendifferenzen, eine andere Kompositionsregel für die Fläche oder einen veränderten sichtbaren Ausgang. Das Argument setzt den flächenneutralen Eingang des Umfelds und die additive Ausgangsfläche voraus. Ein Umfeld mit vorbeladener Fläche oder eine bloß grobe Erhaltung des Fensters liegen außerhalb des Ausschlusses.

### Flächenreserve bei einem vorbeladenen Umfeld

Erkundung. Zerlege jeden exakten Flächenwert in Minimalspineinheiten nach den quadratfreien Radikalen und bezeichne mit $c_3(X)$ den Beitrag aus dem Radikal $\sqrt3$, ausgedrückt in diesen Einheiten. Auf dem additiven gravitativen Spektrum ist $c_3(X)$ eine nichtnegative ganze Zahl mit $c_3(X)\le X$. Für einen scharf präparierten Umfeld-Eingang der Fläche $B$ und einen sichtbaren Minimalspinausgang der Fläche $N$ erzwingt exakte Gesamtflächenerhaltung

$$
c_3(B_{\rm out})=c_3(B)+c_3(A_{\rm in})-N.
$$

Folglich braucht der Vorrat mindestens $N-c_3(A_{\rm in})$ Einheiten der Minimalspinklasse, wenn diese Differenz positiv ist. Andere Radikalklassen können diesen Fehlbetrag wegen linearer Unabhängigkeit nicht ersetzen.

Diese Bedingung kann auf den untersuchten Fensterfolgen extensiv sein. Es gibt von unten approximierende konvergente Brüche $p/q$ für $\alpha=a(1)/a(1/2)=\sqrt{8/3}$ mit $0<q\alpha-p<1/q$. Setze $N=2p$ und wähle $2q$ Spin-1-Punkte. Ihre Fläche liegt bei $N+O(1/N)$ oberhalb von $N$. Damit liegt sie für hinreichend große Glieder in jedem Fenster mit $N\delta_N\to\infty$. Die Belegung lässt wegen gerader Punktzahl ein Singulett zu und hat $c_3(A_{\rm in})=0$. Auf dieser Teilfolge verlangt ein Kanal für das ganze Fenster also $B\ge c_3(B)\ge N$. Eine subextensive scharfe Flächenreserve mit demselben additiven Spektrum genügt nicht.

Umgekehrt ist eine vorbereitete Reserve aus $N$ Minimalspinpunkten formal hinreichend, wenn das Umfeld den vollen ursprünglichen Eingangsträger aufnehmen kann: Ein Registertausch gibt den präparierten Minimalspinzustand sichtbar aus und überträgt den gesamten ursprünglichen Zustand ins Umfeld. Er erhält die additive Gesamtfläche, realisiert aber eine Ersetzung mit vorgegebenem Minimalspinzustand. Die Rechnung setzt scharfe Reserve, gleiche Flächeneinheiten und additive Gesamtfläche voraus. Sie begründet weder eine native Flächenreserve noch eine T-Auswahl durch den Companion.

### Kohärente und katalytische Flächenreserven

Erkundung. Die quadratfreien Komponenten sind auf dem additiven Flächenspektrum eindeutig durch den exakten Gesamtwert bestimmt. Die Minimalspinkomponente des Gesamtsystems ist daher auf diesem Spektrum sowohl eine Funktion der Gesamtfläche als auch die Summe der entsprechenden lokalen Komponenten $C_3$. Eine exakte flächenerhaltende Isometrie erhält deshalb auch die Verteilung dieser Gesamtkomponente. Für einen sichtbaren Eingang aus reinen Spin-1-Punkten ist seine Komponente null; ein garantierter Minimalspinausgang mit Fläche $N$ trägt dagegen exakt die Komponente $N$. Da die Ausgangskomponente des Umfelds nichtnegativ ist, muss das Anfangsumfeld vollständig in Komponenten $c_3\ge N$ getragen sein. Das gilt auch für gemischte oder kohärente Reserven und impliziert bei endlichem Erwartungswert $\langle B\rangle\ge N$. Eine kleine Amplitude auf einer großen Reserve genügt für einen deterministischen Kanal nicht.

Allgemeiner sinkt bei genauem Minimalspinausgang der Erwartungswert der Umfeldkomponente um $N-c_3(A_{\rm in})$ für einen scharfen Eingangseigenwert. Wenn diese Differenz positiv ist, kann das Umfeld nach einem deterministischen Übergang nicht denselben Randzustand zurückerhalten, selbst wenn es mit dem Ausgang korreliert sein darf. Bei reinem Spin-1-Eingang kostet jeder Durchlauf $N$ Einheiten dieser Komponente; wiederholte Verwendung ohne Auffüllung erfordert eine entsprechend größere Anfangsreserve. Bei einem selektiven Kanal mit scharfem Eingang ist die Erfolgswahrscheinlichkeit höchstens das Anfangsgewicht des Umfelds in Komponenten $c_3\ge N-c_3(A_{\rm in})$, sofern auch die Auslesung der Erfolgsflagge die Gesamtkomponente erhält. Die Aussage setzt additive Spektren derselben Radikalklassen und exakte Erhaltung voraus. Ein externes Umfeld mit anderem Spektrum oder eine reine Fenstererhaltung sind andere Modelle.

### Annähernd zurückkehrende Flächenreserve

Erkundung. Beim deterministischen exakten Übergang vom reinen Spin-1-Eingang zum Minimalspinausgang der Fläche $N$ ist die Verteilung der Umfeldkomponente nach dem Übergang die Anfangsverteilung um $N$ nach unten verschoben. Bezeichne mit $C\ge N$ die anfängliche Komponente und mit $\varepsilon$ den Totalvariationsabstand zwischen den Verteilungen von $C$ und $C-N$. Für die Ereignisse $C\ge lN$ gilt dann $\Pr(C\ge lN)-\Pr(C\ge(l+1)N)\le\varepsilon$. Da $\Pr(C\ge N)=1$, folgt $\Pr(C\ge lN)\ge\max(0,1-(l-1)\varepsilon)$. Aufsummieren ergibt

$$
\mathbb E C\ge N\sum_{j\ge0}\max(0,1-j\varepsilon)
\ge \frac{N}{2\varepsilon}.
$$

Die zweite Ungleichung folgt aus dem Integral der fallenden linearen Funktion. Wenn der Spurabstand der beiden Umfeldzustände höchstens $\varepsilon$ ist, gilt dieselbe Schranke, weil die Komponentenmessung den Abstand nicht vergrößert. Der führende Faktor ist auf Verteilungsebene scharf: Gleichverteilung auf $N,2N,\ldots,LN$ hat Abstand $1/L$ nach Verschiebung und Erwartungswert $N(L+1)/2$. Dies belegt weder die Realisierbarkeit des gesamten Kanals mit dieser Verteilung noch Kohärenzerhalt in anderen Freiheitsgraden. Die Schranke betrifft exakte additive Flächenerhaltung und eine garantierte sichtbare Minimalspinausgabe.

### Flächenladder als realisierbare Referenzreserve

Erkundung. Fixiere einen reinen Spin-1-Singulettzustand $|I\rangle$ mit Fläche $N+\epsilon$ und einen reinen Minimalspin-Singulettzustand $|M\rangle$ der Fläche $N$. Verwende im Umfeld $L$ unterscheidbare Blockplätze und definiere $|E_j\rangle$ als Produkt aus $j$ Kopien von $|I\rangle$ auf den ersten Plätzen und $L-j$ Kopien von $|M\rangle$ auf den übrigen, für $0\le j\le L$. Die Zustände sind orthogonal und haben Fläche $LN+j\epsilon$. Die Vorschrift

$$
|I\rangle\otimes|E_j\rangle\longmapsto |M\rangle\otimes|E_{j+1}\rangle,
\qquad 0\le j<L,
$$

erhält exakte Gesamtfläche und Gesamtspin null. Sie lässt sich durch bedingten Tausch mit dem nächsten Minimalspinblock realisieren, oder als Unitäre in jedem gemeinsamen Flächensektor ergänzen. Das Umfeld speichert die Blockreihenfolge. Ein abstrakter Tausch auf den angegebenen Trägern setzt keinen nativen Punktprozess voraus.

Die gleichverteilte Mischung über $E_0,\ldots,E_{L-1}$ geht in die gleichverteilte Mischung über $E_1,\ldots,E_L$ über. Ihr vollständiger Spurabstand ist $1/L$, nicht nur der Abstand der Komponentenstatistik. Die anfängliche mittlere Minimalspinkomponente ist $N(L+1)/2$, womit die vorige Untergrenze im führenden Faktor erreicht wird. Eine reine kohärente Reserve ist ebenfalls möglich: Wähle die normierten Amplituden $a_j=\sqrt{2/(L+1)}\sin[\pi(j+1)/(L+1)]$ auf $E_0,\ldots,E_{L-1}$. Ihr Überlapp mit der um einen Platz verschobenen Reserve ist $\sum_{j=1}^{L-1}a_ja_{j-1}=\cos[\pi/(L+1)]$ aus der Eigenvektorgleichung des Pfadgraphen. Ihr Spurabstand ist daher $\sin[\pi/(L+1)]$, ebenfalls von Ordnung $1/L$. Der Aufbau gilt für einen fixierten Eingangsvektor und gibt einen bereits präparierten Minimalspinzustand aus. Er zeigt keine universelle kohärenzerhaltende Umwandlung der gesamten Fensterfaser und keine native Verfügbarkeit dieser Reserve.

### Rückkehrgrenze bei universeller Ersetzung durch einen festen Zustand

Erkundung. Die Flächenleiter ist auf einen fest vorgegebenen Eingangsvektor zugeschnitten. Eine strengere Aufgabe ist, zwei orthogonale Eingänge $|I_1\rangle,|I_2\rangle$ durch dieselbe gemeinsame Unitäre auf denselben reinen sichtbaren Minimalspinzustand $|M\rangle$ abzubilden, bei derselben anfänglichen Reserve $\sigma$. Die gemeinsamen Eingänge $|I_i\rangle\langle I_i|\otimes\sigma$ sind vollkommen unterscheidbar. Ihre unitären Ausgaben bleiben es. Weil der sichtbare Randzustand rein und in beiden Fällen identisch ist, faktorisiert jede Ausgabe als $|M\rangle\langle M|\otimes\sigma_i'$. Folglich haben die beiden Umfeldzustände Spurabstand eins. Aus der Dreiecksungleichung folgt

$$
\max_i D(\sigma_i',\sigma)\ge\tfrac12.
$$

Diese Grenze gilt unabhängig vom Flächenvorrat und auch für gemischte Reserven. Alle zurückbleibenden Register müssen dabei zum Umfeld gezählt werden. Sie ist mit der kleinen Rückkehrabweichung der Flächenleiter vereinbar, weil diese nur einen Eingang reproduziert. Wenn der sichtbare Ausgang verschiedene Minimalspinzustände tragen darf, kann er einen Teil der Eingangsinformation erhalten; die Konstante $1/2$ folgt dann nicht aus diesem Argument. Für die native OP1-Zählung müssen daher Ersetzung durch einen präparierten Zustand, ein informationshaltiger Minimalspinausgang und ein selektiver Ja-Zweig separat behandelt werden.

### Rückkehrgrenze mit informationshaltigem Minimalspinausgang

Erkundung. Sei $D$ die Eingangsdimension einer Flächenfaser, $d$ die Dimension des erlaubten sichtbaren Minimalspinausgangs und $|e\rangle$ eine reine Anfangsreserve. Die reversible gemeinsame Umsetzung bildet die $D$ orthogonalen Eingänge in den sichtbaren $d$-dimensionalen Raum mal Umfeld ab. Für den gleichverteilten Eingang ist der Gesamtzustand nach dem Übergang ein Rang-$D$-Projektor geteilt durch $D$. Die Wahrscheinlichkeit, die Reserve wieder im Anfangszustand zu finden, ist höchstens $d/D$, denn der entsprechende Projektor $I_{\rm sichtbar}\otimes|e\rangle\langle e|$ hat Rang $d$. Die binäre Messung dieses Projektors liefert für den Spurabstand der mittleren Ausgangsreserve vom Anfangszustand die untere Schranke $1-d/D$. Mindestens ein Eingang aus jeder orthonormalen Eingangsbasis hat daher einen mindestens ebenso großen Rückkehrfehler. Die Rechnung erlaubt beliebige Korrelationen zwischen sichtbarem Ausgang und Umfeld.

Für eine anfänglich gleichverteilte gemischte Reserve auf einem endlichen Rang-$r$-Unterraum gilt dieselbe Schranke: Der gemeinsame Zustand ist ein Rang-$Dr$-Projektor geteilt durch $Dr$, und der Test auf dem ursprünglichen Reserve-Unterraum hat Rang $dr$. Allgemeiner kann man für eine gemischte Reserve mit Eigenwerten $\lambda_i$ die Summe der größten $dr$ Eigenwerte des gemeinsamen Eingangs, also der jeweils $D$-fach auftretenden Werte $\lambda_i/D$, als Rückkehrwahrscheinlichkeits-Obergrenze verwenden. Eine universelle Schranke $1-d/D$ für beliebige ungleich gewichtete gemischte Reserven folgt daraus nicht.

Auf der Faser mit 15 Eingangssinguletts und 14 Minimalspin-Singuletts ist die Rückkehrabweichung bei reiner oder flacher Reserve mindestens $1/15$. Auf den großen Fasern mit exponentiell wachsendem Verhältnis $D/d$ nähert sich die Schranke eins. Das ist eine Informationsgrenze zusätzlich zur Flächenbilanz. Sie setzt deterministische Umwandlung auf dem gesamten Eingangsträger, gemeinsame reversible Entwicklung und die Einbeziehung aller Hilfsregister ins Umfeld voraus.

### Entropiegrenze für beliebig gemischte Reserven

Erkundung. Sei $D$ die Eingangsdimension, $d$ die sichtbare Ausgabedimension und $R$ die gesamte endliche Umfelddimension. Für den gleichverteilten Eingang und eine beliebige Anfangsreserve $\sigma$ hat der gemeinsame Zustand vor und nach der reversiblen Umsetzung Entropie $\log_2 D+S(\sigma)$. Aus der Subadditivität und der sichtbaren Dimension folgt für die Ausgangsreserve $\sigma'$ daher $S(\sigma')-S(\sigma)\ge\log_2(D/d)$.

Sei der Spurabstand $D(\sigma',\sigma)\le\varepsilon\le1/2$ und $R\ge2$. Eine Messung in der Eigenbasis von $\sigma$ liefert zwei Verteilungen $p,q$ mit Totalvariation höchstens $\varepsilon$. Dabei ist $S(\sigma)=H(p)$ und $S(\sigma')\le H(q)$, da die Dephasierung die Entropie nicht verringert. Koppelt man die beiden klassischen Verteilungen so, dass ihre Ziehungen mit Wahrscheinlichkeit gleich ihrem Totalvariationsabstand $t$ verschieden sind, ist die bedingte Entropie der zweiten Ziehung gegeben die erste höchstens $h_2(t)+t\log_2(R-1)$. Das folgt aus dem binären Fehlereignis und den höchstens $R-1$ verbleibenden Möglichkeiten. Die Schranke wächst für $0\le t\le1/2$. Somit gilt notwendig

$$
\log_2(D/d)\le h_2(\varepsilon)+\varepsilon\log_2(R-1).
$$

Wenn jede Eingabe die Reserve mit Fehler höchstens $\varepsilon$ zurückgibt, gilt dies durch Konvexität auch für den gleichverteilten Eingang. Die Schranke erlaubt Korrelationen zwischen sichtbarem Ausgang und Umfeld. Sie zählt alle Hilfsregister in $R$ und ist unabhängig von der Flächenbilanz. Auf der vollständigen exakten Modellfaser mit $\log_2(D/d)=(0{,}302498+o(1))N$ muss daher bei festem Rückkehrfehler $1$ Prozent die Umgebungskapazität mindestens $(30{,}2498+o(1))N$ Bits betragen. Die Abschätzung gibt eine notwendige Kapazität, keine Konstruktion und keine native QAM-Identifikation.

### Gemischte Informationsleiter: Rückkehr im Mittel und pro Eingang

Erkundung. Betrachte den reinen Dimensionsvergleich mit $D=dm$ und ganzzahligem $m\ge2$. Zerlege den Eingang in einen sichtbaren Index $x$ mit $d$ Werten und einen auszulagernden Index $y$ mit $m$ Werten. Das Umfeld besitzt orthogonale Stufen $E_j$ der Dimension $m^j$ für $0\le j\le L$. Auf der Stufe $j<L$ bildet die Isometrie $(x,y,w)\mapsto(x,wy)$ ab, wobei $w$ ein Wort der Länge $j$ und $wy$ das um $y$ ergänzte Wort ist. Sie lässt sich nach Einbettung von Ein- und Ausgängen in einen gemeinsamen Träger reversibel ergänzen. Die Reserve verteilt ihr Gewicht gleichmäßig über die ersten $L$ Stufen und ist innerhalb jeder Stufe maximal gemischt.

Beim gleichverteilten Eingang ist der neue Buchstabe gleichverteilt und unabhängig vom alten Wort. Die Ausgangsreserve ist daher innerhalb jeder Stufe wieder maximal gemischt, mit Stufengewicht auf $1,\ldots,L$ statt $0,\ldots,L-1$. Ihr Spurabstand zur Anfangsreserve ist exakt $1/L$. Zugleich gilt $\log_2 R=L\log_2 m+O(1)$ für $R=\sum_{j=0}^L m^j$. Die Entropieuntergrenze wird also für den gemittelten Eingang im führenden Term erreicht.

Für einen festen Basisbuchstaben $y$ bleiben auf jeder überlappenden Stufe hingegen nur Wörter mit diesem Endbuchstaben belegt. Der Spurabstand beträgt dann $1-(L-1)/(Lm)$ und konvergiert bei großem $L$ gegen $1-1/m$. Eine kleine mittlere Rückkehrabweichung belegt daher keine gleichmäßige Rückkehr für jeden Eingang. Diese Konstruktion behandelt nur Informationsdimensionen. Sie setzt keine zusätzliche Flächenerhaltung voraus. Auf einem einzelnen exakten Flächensektor könnte das Umfeld im Modell als flächenneutraler Informationsträger angesetzt werden; seine native QAM-Verfügbarkeit ist damit nicht begründet.

### Rechte Phase aus den tatsächlichen Punktspins

Erkundung. Ersetze auf einer geraden zyklischen Spinliste die rechten Hilfsdoublets durch dieselben Spins $j_p$, die links die Fläche tragen. Die maximalen Gruppenspins sind dann $a=\sum_{p\ {\rm gerade}}j_p$ und $b=\sum_{p\ {\rm ungerade}}j_p$. Im antiferromagnetischen Zweigruppenmodell entsteht eine eindeutige rechte Singulettlinie genau dann, wenn $a=b$. Eine Punktoperation, die eine solche Liste erhält und die Gruppen bewahrt, wirkt auf der rechten Grundlinie trivial. Eine gruppentauschende Operation wirkt dagegen mit $(-1)^{2a}$: Die maximalen Gruppenträger sind durch ihre höchsten Gewichtszustände kanonisch bis auf eine gemeinsame Phase identifizierbar, und der Tausch im Singulett zweier Spins $a$ hat dieses Vorzeichen. Dieses Kriterium muss je Liste beziehungsweise je Orbit geprüft werden. Die Zahl der Punkte allein bestimmt die Phase nicht.

Auf der exakten Faser mit acht Minimalspin-Flächeneinheiten bleiben nach linker Singulettprojektion nur die reine Acht-Punkt-Belegung und die Belegung aus zwei Spin-$3$-Punkten. Für die reine Belegung ist $a=b=2$. Ihre rechte Phase ist positiv und die linke Diederprojektion liefert drei Zustände. Für die Spin-$3$-Belegung ist $a=b=3$. Sowohl das linke als auch das rechte Paarsingulett sind unter Tausch symmetrisch, weil $(-1)^{2\cdot3}=+1$. Der gemischte Eingangsraum hat damit vier Zustände gegenüber drei reinen Minimalspinausgängen. Mit einem rechten Hilfsdoublet pro Punkt war der rechte Tausch beim Spin-$3$-Paar dagegen negativ, sodass sein linker Singulettzustand aus dem gemeinsamen invarianten Raum fiel.

Damit hängt die Dimensionsgleichheit auf der kleinen Faser direkt am gewählten rechten Träger. Der tatsächliche Spinträger ergibt im Modell wieder einen Bedarf von mindestens zwei Umfeldzuständen. Die derzeitige QAM-Option für Hilfsdoubletts bildet diesen spinabhängigen Charakter nicht ab. Die Rechnung setzt eine zyklische Ordnung, den maximalen Zweigruppen-Grundzustand und die gemeinsame Punktprojektion voraus; sie leitet diese Randstruktur nicht nativ her.

### Asymptotische Kapazität mit tatsächlichen rechten Spins

Erkundung. Die endlichen Zählungen mit spinabhängigem rechtem Charakter sind kleiner als der ungefilterte Eingang. Für den führenden Exponenten kann man dennoch dieselbe untere Schranke konstruieren. Fixiere eine endliche Pell-Spinmenge mit mindestens zwei Arten und die optimalen Listenanteile für ihre abgeschnittene Normierung. Wähle gerade Anzahlen $m_r$ nahe diesen Anteilen und fülle einen beschränkten geraden Flächenrest mit Minimalspinpunkten auf. Verteile jede Spinart mit genau $m_r/2$ Exemplaren auf jede der beiden alternierenden Gruppen. Damit stimmen die rechten maximalen Gruppenspins automatisch überein.

Für Listenlänge $L=\sum_r m_r$ zählt diese Teilfamilie

$$
\left[\frac{(L/2)!}{\prod_r(m_r/2)!}\right]^2
$$

Listen. Ihr Logarithmus unterscheidet sich vom Logarithmus der unbeschränkten Multinomialzahl bei fester Artenzahl nur um $O(\log N)$. Nichtfreie zyklische und Diederorbits bleiben vernachlässigbar, weil selbst ihre unbeschränkten Fixmengen nur den halben Listenexponenten erreichen. Auf einem freien Orbit lässt sich jeder linke Singulettvektor zusammen mit der rechten Grundlinie konsistent fortsetzen; es gibt keinen Stabilisator, der eine zusätzliche Phasenbedingung erzwingt. Die linke Singulett-Untergrenze pro Liste bleibt durch die gerade Anzahl je Spinart unverändert.

Damit erreicht diese balancierte Teilfamilie denselben Eingangs-Exponenten wie die volle Modellfaser, wenn die endliche Spinmenge anschließend vergrößert wird. Die frühere Obergrenze durch die vollen Produktdimensionen gilt weiterhin, da jede zulässige Liste genau eine rechte Grundlinie beiträgt. Im Modell mit tatsächlichen rechten Spins und zyklischer oder Diederprojektion bleibt die asymptotische Umfeldrate somit $-\log_2 z_*-1\approx0{,}302498$ Bit pro Flächeneinheit. Die kleineren endlichen Dimensionen ändern den führenden Exponenten nicht. Das Ergebnis setzt die deklarierte Ordnung und die Auswahl der rechten Grundlinie voraus; weitere native Einschränkungen können die Rate ändern.

### Fensterkanal mit tatsächlicher rechter Spinbalance

Erkundung. Die Fenster-Untergrenze mit voller linker SU(2)-Schließung lässt sich mit der tatsächlichen rechten Spinbalance verbinden. Auf geraden Flächenindizes und bei $N\delta_N\to\infty$ liefert die vorige Flächenkorrektur gerade Anzahlen je Spinart. Verteile jede Art anschließend hälftig auf beide alternierenden Gruppen. Bei fester endlicher Artenzahl ändert dies den Logarithmus der Listenmultiplizität nur um $O(\log N)$. Die linke Singulett-Untergrenze bleibt pro Liste erhalten. Nichtfreie zyklische und Diederorbits sind exponentiell seltener als die balancierten Listen, nach derselben Fixmengenabschätzung wie auf der exakten Faser. Auf freien Orbits können die linken Singuletts mit der rechten Grundlinie unabhängig vom Tauschcharakter fortgesetzt werden. Der volle Fensterexponent bleibt daher $s_{SU(2)}$; die obere Schranke folgt unverändert aus den Produktdimensionen. Da der projizierte reine Minimalspinausgang weiterhin Exponent $\ln2$ pro Punkt hat, beträgt die Umfeldrate für Fenstererhaltung auch in diesem Modell rund $1{,}15150$ Bit pro Flächeneinheit.

Auch der flächenarithmetische Gegenfall für exakte Erhaltung bleibt zulässig. Die homogene Belegung aus $2q$ Spin-1-Punkten hat automatisch gleiche rechte Gruppenspins $q$. Ihre rechte Grundlinie trägt unter Gruppentausch das Zeichen $(-1)^{2q}=1$. Links existiert ein vollständig permutationssymmetrisches Singulett: Im symmetrischen Tensorraum der Spin-1-Vektordarstellung wird es durch die nichtverschwindende Potenz des invarianten quadratischen Polynoms $(x_1^2+x_2^2+x_3^2)^q$ repräsentiert. Dieser Eingang überlebt daher auch die Diederprojektion. Seine Fläche liegt entlang der zuvor konstruierten Teilfolge knapp oberhalb von $N$, und seine Minimalspinkomponente bleibt null. Der Ausschluss für ein flächenneutrales Umfeld mit Mindeststufe eins sowie die extensive Untergrenze für einen Vorrat bleiben für diesen Gegenfall bestehen.

Der Befund gilt für geordnete Listen mit voller linker Singulettschließung, alternierender Zweiteilung und ausgewählter rechter Grundlinie. Er setzt keine native Gültigkeit dieser Randbedingungen voraus.

### Erfolgswahrscheinlichkeit eines Ja-Zweigs mit internem Umfeld

Erkundung. Sei $D$ die Eingangsdimension und $d$ die sichtbare Minimalspin-Ausgabedimension. Ein Ja-Zweig mit höchstens $r$ Krausoperatoren $K_i$ hat Effekt $E=\sum_i K_i^\dagger K_i\le I$. Da jeder $K_i$ Rang höchstens $d$ hat, gilt $\operatorname{rang}E\le rd$. Für den gleichverteilten Eingang folgt $p_{\rm Ja}=\operatorname{tr}E/D\le\min(1,rd/D)$. Die Schranke ist im abstrakten Dimensionsmodell scharf: Teile eine Eingangsbasis in höchstens $r$ disjunkte Gruppen von jeweils höchstens $d$ Vektoren, bilde jede Gruppe isometrisch in den sichtbaren Träger ab und führe ungenutzte Basisvektoren in den Nein-Zweig. Der interne Ja-Index ist dabei ein eigener Umfeldfreiheitsgrad, auch wenn der sichtbare Zeiger nur ein Bit ausgibt.

Für jede fest positive Erfolgswahrscheinlichkeit ist folglich dieselbe führende Umfeldrate nötig wie für deterministischen Erfolg, sofern $D/d$ exponentiell wächst. Dies gilt auch im Modell mit tatsächlicher rechter Balance und Diederprojektion, mit der jeweils zuvor hergeleiteten exakten Faser- oder Fensterrate. Für exakte additive Flächenerhaltung mit einem anfänglich neutralen Umfeld der Mindeststufe eins kommt im schmalen Fenster eine weitere Grenze hinzu: Der Ja-Effekt kann nur auf dem exakten Eingangssektor der Fläche $N$ tragen. Die übrigen Flächenreste haben keinen zulässigen Umfeld-Eigenraum. Unabhängig von $r$ ist der Erfolg bei gleichverteilter Fenstereingabe deshalb höchstens $D_{\rm exakt}(N)/D_{\rm Fenster}(N)$. Im vollen SU(2)-Modell mit tatsächlicher rechter Balance fällt dieser Quotient exponentiell mit Rate $s_{SU(2)}/\ln2+\log_2 z_*\approx0{,}84900$ Bit pro Flächeneinheit.

Diese Aussagen betreffen die gleichverteilten Modellträger und die deklarierten Flächeneinheiten. Auf einem anders präparierten Eingang ist die Besetzung der exakten Faser gesondert anzugeben. Eine bloße Ja-Nein-Ausgabe begründet keinen kleinen internen Hilfsträger und keine native T-Selektionsregel.

### Wechsel des ersten Flächenrests zwischen acht und zehn Einheiten

Erkundung. Im Fenster der Breite $999/1000$ mit Diederprojektion und tatsächlicher rechter Spinbalance liefert die exakte MML-Zählung für die Zielflächen $N=2,4,6,8,10$ die Eingangsdimensionen $1,2,8,48,418$. Bei zwei Einheiten gibt es in diesem Fenster keinen positiven Rest. Bei vier, sechs und acht ist der erste positive Rest $2\sqrt5-4$. Bei zehn sinkt er auf $(2\sqrt6+\sqrt{105}-15)/3\approx0{,}0486434$.

Der erste Sektor bei zehn Einheiten lässt sich unabhängig identifizieren. Seine quadratfreien Beiträge erzwingen einen Spin-1-Punkt und einen Spin-$5/2$-Punkt sowie fünf Minimalspin-Flächeneinheiten aus der Pell-Klasse. Letztere lassen sich entweder mit fünf Minimalspinpunkten oder mit einem Spin-$3$-Punkt und einem Minimalspinpunkt füllen. Die erste Variante hat ungerade Punktzahl und entfällt im balancierten Modell. Die zweite hat die zwei Gruppen $(3,1/2)$ und $(5/2,1)$ mit Spin-Summe $7/2$. Die acht balancierten Anordnungen bilden einen freien Diederorbit. Links haben die beiden Paar-Kopplungen genau zwei gemeinsame Spinwerte, $5/2$ und $7/2$. Somit gibt es zwei linke Singuletts pro Repräsentantenliste und zwei Zustände im projizierten ersten Restsektor. Der Befund zeigt einen konkreten Wechsel der verantwortlichen Belegung, begründet aber kein allgemeines Gesetz für den Abstand zum nächsten Flächenwert.

### Flächenreste der Ordnung 1/N auf allen großen geraden Zielflächen

Erkundung. Definiere positive ganze Zahlen $(x_t,y_t)$ durch $x_0+y_0\sqrt6=2+\sqrt6$ und Multiplikation mit $(5+2\sqrt6)^t$. Dann gilt $x_t^2-6y_t^2=-2$. Setze $P_t=4x_t$, $Q_t=6y_t$. Die Fläche von $Q_t$ Spin-1-Punkten ist in Minimalspineinheiten

$$
Q_t\sqrt{8/3}=P_t+\epsilon_t,\qquad
\epsilon_t=\frac{8}{y_t\sqrt6+x_t}>0.
$$

Die $P_t$ wachsen mit beschränktem Verhältnis aufeinanderfolgender Glieder und $\epsilon_t=O(1/P_t)$. Für jede hinreichend große gerade Zielfläche $N$ wähle das größte $P_t\le N/2$. Dann ist $P_t$ proportional zu $N$ bis auf feste Faktoren. Ergänze die $Q_t$ Spin-1-Punkte um $N-P_t$ Minimalspinpunkte. Beide Anzahlen sind gerade und wachsen linear mit $N$. Die Fläche der Belegung ist genau $N+\epsilon_t$ mit $0<\epsilon_t\le C/N$ für eine feste Konstante $C$.

Verteile jede Spinart hälftig auf beide alternierenden Gruppen. Das erfüllt die tatsächliche rechte Spinbalance. Wegen der geraden Anzahlen hat der linke Tensorträger mindestens ein Singulett, etwa durch Paarung innerhalb jeder Spinart. Die beiden Arten haben Anteile, die gleichmäßig von null und eins entfernt sind. Daher existieren für große $N$ balancierte Listen mit freiem Diederorbit: Die Zahl balancierter Listen hat den vollen binomialen Exponenten, und alle nichttrivialen Fixmengen zusammen haben höchstens den halben Exponenten bis auf polynomiale Faktoren. Auf einem freien Orbit lässt sich ein linker Singulettvektor zusammen mit seiner rechten Grundlinie invariant fortsetzen.

Damit liegt der erste positive Rest im deklarierten Modell für alle hinreichend großen geraden $N$ höchstens bei $C/N$, auch mit tatsächlicher rechter Spinbalance und Diederprojektion. Das ist eine obere Schranke für den Abstand, keine untere Schranke und keine Aussage über die volle Zählrate in Fenstern der Breite $C/N$. Anders als der reine Spin-1-Gegenfall enthält diese ergänzte Belegung bereits Minimalspinfläche; sie liefert hier den Abstandsnachweis. Native Gültigkeit der Randprojektion bleibt offen.

### Bereits Fenster der Ordnung 1/N können den Exponenten erhöhen

Erkundung. Im Modell mit tatsächlicher rechter Balance und Diederprojektion sei $s_P=-\ln z_*$ der exakte Pell-Exponent. Er kann durch eine endliche Pell-Spinmenge mit Exponent $s_F$ beliebig genau von unten angenähert werden. Fixiere zunächst eine kleine positive Zahl $\eta$ und wähle aus der vorigen Pell-Folge das größte $P_t\le\eta N$. Mit einer festen Konstante $R$ für das maximale Verhältnis aufeinanderfolgender $P_t$ liegt $u=P_t/N$ für alle großen geraden $N$ in $[\eta/R,\eta]$. Die $Q_t$ Spin-1-Punkte tragen Fläche $P_t+\epsilon_t$ mit $0<\epsilon_t\le C_\eta/N$. Fülle die übrige Fläche $N-P_t$ mit der endlichen optimalen Pell-Mischung und geraden Anzahlen jeder Art. Rundungsreste werden durch Minimalspinpunkte ergänzt. Damit liegt jede so erzeugte Liste im Fenster $[N,N+C_\eta/N]$.

Sei $\ell_F>0$ die mittlere Punktzahl pro Pell-Flächeneinheit der gewählten endlichen Mischung und $\alpha=a(1)/a(1/2)$. Die Listenzahlen der beiden Teile sind asymptotisch $L_P=\ell_F(1-u)N+O(1)$ und $Q_t=(u/\alpha)N+O(1)$. Ihre frei wählbare Verzahnung liefert zusätzlich den Binomialfaktor $\binom{L_P+Q_t}{Q_t}$. Die linke Singulettdimension der geraden Spin-1-Anzahl ist bis auf polynomiale Faktoren $3^{Q_t}$, nach der früheren Halbierungsabschätzung. Gleichmäßige Verteilung jeder Art auf beide alternierenden Gruppen kostet nur polynomiale Faktoren. Freie Diederorbits erhalten den Exponenten, da Fixmengen gegenüber der balancierten Listenzahl exponentiell kleiner bleiben.

Der resultierende untere Exponent pro Flächeneinheit ist damit

$$
(1-u)s_F+\frac{u}{\alpha}\ln3+
\left[\ell_F(1-u)+\frac{u}{\alpha}\right]
h\!\left(\frac{u/\alpha}{\ell_F(1-u)+u/\alpha}\right).
$$

Der letzte Term ist $(u/\alpha)\ln(1/u)+O(u)$ für kleine $u$. Die Konstante kann für hinreichend große endliche Pell-Mengen einheitlich gewählt werden: Ihre mittlere Fläche pro Punkt bleibt beschränkt, da die Gewichte $d_r z_F^r$ einen gemeinsamen exponentiellen Schwanz besitzen, und somit ist $\ell_F$ von null weg beschränkt. Wähle daher zuerst $\eta$ klein genug, dass der zusätzliche Verzahnungsterm die linearen Verluste im ganzen Intervall $[\eta/R,\eta]$ überwiegt. Wähle danach $s_F$ nahe genug an $s_P$. Damit gibt es feste $C_\eta$ und $\Delta>0$, für die der untere Fensterexponent mindestens $s_P+\Delta$ beträgt. Die Rechnung liefert keinen vollen Fensterexponenten bei Breite $C_\eta/N$ und keine native Fensterauflösung. Sie zeigt jedoch, dass bei dieser Breitenordnung bereits exponentiell relevante neue Zustände auftreten können.

### Annäherung an den vollen Exponenten bei Breite C/N

Erkundung. Fixiere eine endliche Spinmenge $F$ mit Spin $1/2$ und Spin eins und voller lokaler Irrep-Dimension $d_j=2j+1$. Sei $s_F$ durch $\sum_{j\in F}d_j e^{-s_F r_j}=1$ gegeben und $p_j=d_j e^{-s_F r_j}$. Für das Fenster $[N,N+C/N]$ erfordert die frühere dyadische Netzabschätzung der irrationalen Spin-1-Fläche Änderungen um höchstens $O(N/C)$ Punkte. Zusammen mit der ganzzahligen Minimalspinkorrektur erhält man bei großen geraden $N$ eine zulässige gerade Zusammensetzung mit Listenanteilen $q_j=p_j+O_F(1/C)+O_F(1/N)$. Für hinreichend großes festes $C$ bleiben alle Anteile positiv. Rechte Balance, linke Singulettbildung und der Diederquotient kosten bei dieser festen Artenmenge nur polynomiale Faktoren.

Der Exponent pro Flächeneinheit der korrigierten Zusammensetzung lautet

$$
\frac{H(q)+\sum_j q_j\ln d_j}{\sum_j q_j r_j}
=s_F-\frac{D(q\|p)}{\sum_j q_j r_j}.
$$

Für $q$ in einer festen kleinen Umgebung des strikt positiven Vektors $p$ ist $D(q\|p)\le\sum_j(q_j-p_j)^2/p_j$. Das folgt aus $\ln x\le x-1$ und $\sum_j(q_j-p_j)=0$. Der Exponentenverlust ist somit höchstens $O_F(C^{-2})$, im unteren Grenzwert über gerade $N$. Anders als eine lineare Fehlerabschätzung nutzt dies die Optimalität der ursprünglichen Zusammensetzung.

Da sich $s_F$ dem vollen $s_{SU(2)}$ beliebig nähert, folgt: Zu jedem gewünschten Exponentenabstand $\varepsilon>0$ gibt es ein festes endliches $C$, sodass die untere Zählrate im Fenster $C/N$ mindestens $s_{SU(2)}-\varepsilon$ beträgt. Die obere Schranke bleibt $s_{SU(2)}$. Die Konstante der quadratischen Abschätzung hängt von $F$ ab. Für ein vorgegebenes endliches $C$ folgt daraus weder Gleichheit mit dem vollen Exponenten noch eine explizite native Fensterwahl.

### Drei irrationale Spinflächen erschließen den vollen Exponenten bei C/N

Erkundung. In Minimalspin-Flächeneinheiten liefern $j=1/2,1,3/2,9$ die Werte $1,2\sqrt6/3,\sqrt5,2\sqrt{30}$. Daher entspricht jedes Element von $12\mathbb Z[\sqrt6,\sqrt5]$ einer ganzzahligen Änderung durch gerade Punktanzahlen dieser vier Arten. Die Koeffizienten im Basisvektor $(1,\sqrt6,\sqrt5,\sqrt{30})$ bestimmen die vier Änderungen bis auf feste Faktoren.

Für $Q>1$ bilde ein Produkt $u$ aus Potenzen der drei positiven Einheiten $5-2\sqrt6$, $9-4\sqrt5$ und $11-2\sqrt{30}$. Wähle jeden Exponenten so, dass sein Faktor in der ursprünglichen Einbettung zwischen $c_i/Q$ und $1/Q$ liegt, mit festem $c_i>0$. Jede der drei anderen reellen Einbettungen kehrt genau zwei dieser Einheiten um, weil ihre jeweilige Norm eins ist. Somit hat $u$ in der ursprünglichen Einbettung Größe $O(Q^{-3})$, und in den anderen Einbettungen Größe $O(Q)$. Die vier Elemente $12u$ mal die Basisvektoren bilden eine reelle Basis im Raum der vier Einbettungen. Für einen vorgegebenen beschränkten Flächenrest $x$ schreibe $(x,0,0,0)$ in dieser Basis und runde die vier reellen Koeffizienten auf ganze Zahlen. Der resultierende Gittervektor hat in der ursprünglichen Einbettung Fehler $O(Q^{-3})$ und in den übrigen Koordinaten Größe $O(Q)$. Die inverse feste Einbettungsmatrix zeigt, dass seine vier ganzzahligen Koeffizienten in der ursprünglichen Radikalbasis ebenfalls $O(Q)$ sind. Er wird somit durch $O(Q)$ Punktänderungen realisiert.

Für ein Zielfenster $[N,N+\delta_N]$ runde zunächst die optimale Zusammensetzung einer festen endlichen Spinmenge, welche die vier Korrekturspins enthält, auf gerade Anzahlen. Der ursprüngliche Flächenfehler ist beschränkt. Ziele bei der Gitterkorrektur auf die Fenstermitte und wähle $Q$ als hinreichend großes konstantes Vielfaches von $\delta_N^{-1/3}$. Falls $N^3\delta_N\to\infty$, sind die Punktänderungen $o(N)$. Alle vier Korrekturarten haben positive asymptotische Anteile und die Änderungen sind daher zulässig. Rechte Balance, linke Singulettbildung und Diederprojektion kosten wie zuvor nur polynomiale Faktoren. Vergrößern der endlichen Spinmenge ergibt zusammen mit der bekannten oberen Schranke den vollen SU(2)-Listenexponenten auf dieser Fensterfolge.

Insbesondere genügt jetzt jede feste Breite $C/N$ mit $C>0$. Die vorige Annäherung für großes $C$ war eine schwächere Abschätzung, da sie nur eine irrationale Korrekturart verwendete. Die Bedingung $N^3\delta_N\to\infty$ ist hinreichend; sie bestimmt keine scharfe Schwelle. Die Rechnung betrifft den deklarierten geordneten Modellträger und leitet keine native Horizontauflösung her.

### Voller Exponent für jede feste inverse Potenz der Fläche

Erkundung. Die vorige Einheitenkonstruktion verallgemeinert sich auf $K=\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_m})$ mit verschiedenen Primzahlen $p_i\ne3$ und Grad $D=2^m$. Schreibe $a_S=\prod_{i\in S}p_i$ für jede Teilmenge. Für jedes nichtleere $S$ liefert eine positive Pell-Lösung $d_S^2-3a_S r_S^2=1$ einen verfügbaren Spin $(d_S-1)/2$ mit Flächenquotient $r_S\sqrt{a_S}$. Die Minimalspinart liefert die Basisrichtung eins. Somit lässt sich jedes Element eines festen ganzzahligen Vielfachen der Radikalbasis durch gerade Änderungen der entsprechenden Punktanzahlen realisieren.

Für jedes nichtleere $S$ wähle in der quadratischen Teilstruktur eine positive Norm-eins-Einheit $u_S<1$, beispielsweise den Kehrwert einer positiven Pell-Einheit für $a_S$. Für $Q>1$ wähle ihre Potenz so, dass sie in der ursprünglichen Einbettung Größenordnung $Q^{-1}$ hat. Das Produkt aller $D-1$ Potenzen hat dort Größe $O(Q^{-(D-1)})$. Jede andere Einbettung invertiert genau $D/2$ Faktoren und lässt $D/2-1$ Faktoren unverändert, weil ein nichttrivialer Vorzeichencharakter auf genau der Hälfte aller Teilmengen negativ ist. Daher hat das Produkt in jeder anderen Einbettung Größe $O(Q)$. Rundung in der mit diesem Produkt multiplizierten Radikalbasis liefert wie zuvor eine Flächenkorrektur mit Fehler $O(Q^{-(D-1)})$ und $O(Q)$ Punktänderungen.

Für jedes feste $p>0$ wähle $D-1>p$ und ein Fenster $\delta_N=C N^{-p}$ mit festem $C>0$. Dann genügt $Q=O(N^{p/(D-1)})=o(N)$. Die endliche Startmischung muss alle Korrekturspins mit positiven Anteilen enthalten. Sie kann für den Exponenten anschließend um weitere Spinarten erweitert werden. Gerade Anzahlen, rechte Balance, linke Singuletts und freie Diederorbits funktionieren unverändert. Somit erreicht jedes solche Fenster den vollen SU(2)-Exponenten des deklarierten Modells. Auch eine breitere Fensterfolge mit einer festen polynomialen Untergrenze hat denselben Exponenten, sofern ihre Breite beschränkt bleibt. Die Konstruktion verwendet für jedes $p$ eine andere feste endliche Menge von Korrekturspins. Sie entscheidet keine superpolynomial schrumpfenden Fenster und keine native T-Auflösung.

### Superpolynomiale Fenster und notwendiges Wachstum des Spinträgers

Erkundung. Bei festem Spin-Cutoff liegen alle Flächenquotienten in einem festen multiquadratischen Körper $K$ vom Grad $D$. Es gibt einen gemeinsamen ganzzahligen Nenner $M$, sodass $M$ mal jeder Flächenquotient und die Zielfläche algebraisch ganzzahlig sind. Für einen von null verschiedenen Rest $\epsilon=A-N$ einer Liste in $[N,N+1]$ ist die Körpernorm von $M\epsilon$ eine von null verschiedene ganze Zahl. Jede andere Einbettung ändert bei den beteiligten Radikalen nur Vorzeichen. Daher hat dort $M\epsilon$ Betrag höchstens $M(2N+1)$. Aus dem Normprodukt folgt $|\epsilon|\ge c_K N^{-(D-1)}$. Für jedes superpolynomial schrumpfende Fenster bleibt bei festem Cutoff folglich schließlich nur die exakte Faser. Das Argument gilt bereits vor den Punkt- und Singulettprojektionen.

Auf dem unbeschränkten Modellträger existiert dagegen mindestens eine superpolynomial schrumpfende Fensterfolge mit vollem Exponenten. Schreibe $S_N(\delta)=N^{-1}\ln D_N(\delta)$ für die gezählte Dieder-Singulettfaser mit tatsächlicher rechter Balance. Für jedes feste ganze $p\ge1$ wurde $S_N(N^{-p})\to s_{SU(2)}$ auf geraden $N$ gezeigt. Wähle streng wachsende Schwellen $N_p$, sodass für alle geraden $N\ge N_p$ die Rate bei Breite $N^{-p}$ mindestens $s_{SU(2)}-1/p$ beträgt. Definiere $\delta_N=N^{-p}$ für $N_p\le N<N_{p+1}$. Dann geht $p$ gegen unendlich, die Fenster sind schließlich schmaler als jede feste inverse Potenz und ihre Rate konvergiert dennoch gegen $s_{SU(2)}$. Die universelle obere Schranke stammt aus der vollen Listensumme.

Dies ist ein Existenzbeweis ohne effektive Angabe der Schwellen. Er sagt nicht, dass eine vorgegebene superpolynomiale Folge wie $e^{-\sqrt N}$ den vollen Exponenten hat. Zusammen mit der Normschranke zeigt er, dass ein solcher Effekt tatsächlich unbeschränkt wachsende Spinarten benötigt. Die Folgerung betrifft den deklarierten Modellträger und keine native Horizontauflösung.

### Auflösungsskala auf einem festen vollständigen Radikalträger

Erkundung. Fixiere die vier Spinarten $F=\{1/2,1,3/2,9\}$. Ihre Flächenquotienten bilden, bis auf rationale Faktoren, die vollständige Basis von $\mathbb Q(\sqrt6,\sqrt5)$ mit Grad vier. Für alle geraden $N$ und beschränkte Fenster gilt damit eine zweiseitige Einordnung. Wenn $N^3\delta_N\to0$, enthält das Fenster schließlich keinen positiven Flächenrest: Die Normabschätzung gilt gleichmäßig für alle Listen dieses festen Trägers. Auf der exakten Faser bleibt von den vier Arten nur Spin $1/2$, da die drei anderen Radikalkoeffizienten positiv sind und nicht verschwinden können. Mit linker SU(2)-Schließung, rechter Balance und Diederprojektion ist der führende Exponent folglich $\ln2$.

Wenn dagegen $N^3\delta_N\to\infty$, liefert die Einheitenkorrektur mit $Q\asymp\delta_N^{-1/3}$ den vollen Exponenten der vier Arten, $s_F$ mit $\sum_{j\in F}(2j+1)e^{-s_F r_j}=1$. Da alle vier Arten im optimalen Ansatz positive Anteile besitzen, sind die Korrekturen $o(N)$ zulässig. Es gilt $s_F>\ln2$, denn bei $s=\ln2$ trägt die Minimalspinart bereits eins bei und die drei weiteren Beiträge sind positiv. Somit ist die Ordnung $N^{-3}$ für diesen konkreten festen Träger die Skala, die beide bewiesenen Regime trennt. Feste Breiten $C/N^3$ im Übergangsbereich werden durch diese Argumente nicht vollständig klassifiziert.

Allgemeiner gelten dieselben beiden Aussagen mit $D-1$ für eine feste Spinmenge in einem multiquadratischen Körper vom Grad $D$, sofern die Menge genügend Spinflächen für die gesamte Radikalbasis enthält. Die Untergrenze aus der Norm benötigt diese Vollständigkeit nicht. Deshalb kann man aus einem Spin-Cutoff allein die untere Abstandsschranke ableiten, aber für eine passende obere Konstruktion muss die tatsächlich verfügbare Basis geprüft werden. Die Rechnung behandelt die deklarierte Modellauswahl und keine native T-Auflösung.

### Konkrete Grenzen im kritischen Fenster C/N³

Erkundung. Auf dem Vier-Arten-Träger schreibe die Fläche als $A=n_0+x+y+z$, wobei $x,y,z\ge0$ die Beiträge proportional zu $\sqrt6,\sqrt5,\sqrt{30}$ sind. Für $\epsilon=A-N>0$ ist $3\epsilon$ algebraisch ganzzahlig. Die drei übrigen Einbettungen von $\epsilon$ sind $\epsilon-2(x+y)$, $\epsilon-2(x+z)$ und $\epsilon-2(y+z)$. Setze $A\in[N,N+C/N^3]$. Weil $|\epsilon-2t|\le\epsilon+2t$ für $t\ge0$, ist das Produkt der Beträge dieser drei Einbettungen nach dem arithmetisch-geometrischen Mittel höchstens $(\epsilon+4A/3)^3$. Die Norm des von null verschiedenen $3\epsilon$ hat Betrag mindestens eins. Damit folgt

$$
\epsilon\ge\frac{1}{81(\epsilon+4A/3)^3}.
$$

Für festes $C<1/192$ enthält das Fenster $[N,N+C/N^3]$ daher für große $N$ nur die exakte Minimalspinfaser. Bei geraden Anzahlen aller vier Spinarten und geradem $N$ ist sogar $3\epsilon/2$ algebraisch ganzzahlig, und dieselbe Rechnung schließt innerhalb dieser Teilfamilie $C<1/12$ aus. Die zweite Schranke wird nicht auf alle rechts balancierten Listen übertragen, da Balance keine gerade Anzahl jeder Art erzwingt.

In der anderen Richtung liefert die Einheitenkorrektur bei großem festem $C$ mit $Q=O(N C^{-1/3})$ Spinanteile mit Abweichung $O(C^{-1/3})$ vom optimalen Vier-Arten-Vektor. Die relative Entropierechnung aus dem inversen Fenster ergibt deshalb eine untere Exponentenrate $s_F-O(C^{-2/3})$, sofern $C$ groß genug ist, um alle Anzahlen positiv zu halten. Rechte Balance und Diederprojektion kosten weiterhin nur polynomiale Faktoren. Damit sind ein konkretes exaktes Regime bei kleinen Vorfaktoren und eine quantitative Annäherung an den vollen Exponenten bei großen Vorfaktoren gezeigt. Weder die scharfe Vorfaktorschwelle noch die Gleichheit mit $s_F$ bei einem endlichen festen $C$ folgt daraus.

### Fester kritischer Vorfaktor erzwingt einen Exponentenverlust auf einer Teilfolge

Erkundung. Fixiere den Vier-Arten-Träger und $C>0$. Betrachte alle geraden Ziele $N$ in $[X,2X]$ mit Fenstern der Breite $C/N^3$. Für zwei verschiedene Reste $\epsilon,\epsilon'$ in diesen Fenstern ist $3(\epsilon-\epsilon')$ algebraisch ganzzahlig. Jede ihrer drei konjugierten Differenzen hat Betrag $O(X)$, gleichmäßig über die Listen: Konjugierte Flächen haben wegen positiver Originalbeiträge Betrag höchstens die Originalfläche, und die Subtraktion der ganzzahligen Zielfläche kostet höchstens weitere $2X$. Die Norm liefert daher $|\epsilon-\epsilon'|\ge c X^{-3}$ mit festem $c>0$ für alle großen $X$. Da sämtliche Reste im Intervall $[0,C X^{-3}]$ liegen, treten in diesem ganzen Zielblock höchstens $1+\lfloor C/c\rfloor$ verschiedene Reste auf.

Ein fixer Rest legt wegen der linearen Unabhängigkeit von $1,\sqrt6,\sqrt5,\sqrt{30}$ die Anzahl jeder der drei Nichtminimalspinarten eindeutig fest. Nur die Minimalspinanzahl kann sich mit $N$ ändern. Schreibe $\nu_1>0$ für die optimale Anzahl der Spin-1-Punkte pro Flächeneinheit in der Vier-Arten-Zählung. Für eine feste Spin-1-Anzahl $n_1$ kann $|n_1/N-\nu_1|<\eta$ unter $X\le N\le2X$ nur auf einem Intervall der Länge $O(\eta X)$ gelten, mit Konstante abhängig von $\nu_1$. Wähle $\eta>0$ so klein, dass die endlich vielen Intervalle zusammen weniger als die Hälfte des Zielblocks abdecken. Dann gibt es in jedem großen Block einen positiven Anteil gerader Ziele, bei denen jede zugelassene Zusammensetzung um mindestens $\eta$ von der optimalen Spin-1-Dichte abweicht.

Auf diesen Zielen liegt der Exponent der vollen Produktzählung bereits strikt unter $s_F$. Tatsächlich ist die Rate einer Zusammensetzung mit Listenanteilen $q$ gleich $s_F-D(q\|p)/\sum_j q_jr_j$ bis auf $o(1)$; das einzige Maximum liegt bei $q=p$. Auf der kompakten Menge mit Spin-1-Dichteabstand mindestens $\eta$ ist die Differenz daher gleichmäßig positiv. Die Zahl möglicher Zusammensetzungen ist polynomial und ändert diese obere Rate nicht. Linke Singulettschließung, rechte Balance und Diederprojektion können die Zählung nur weiter verringern.

Folglich kann kein festes endliches $C$ beim kritischen Fenster $C/N^3$ den vollen Vier-Arten-Exponenten als Grenzwert über alle geraden Ziele liefern. Eine Teilfolge mit vollem Exponenten wird dadurch nicht ausgeschlossen. Das Resultat gilt für den festen Vier-Arten-Träger; weitere zugelassene Spinarten verändern das Normargument und können die Skala verschieben.

### Größenordnung der Exponentenlücke im kritischen Fenster

Erkundung. Schreibe $\nu_j=p_j/\sum_i p_i r_i$ für die optimale Anzahl der Spinart $j$ pro Flächeneinheit im Vier-Arten-Modell. Nenne eine Liste bei Ziel $N$ nah am Optimum, wenn $|n_j/N-\nu_j|<\eta$ für alle vier Arten. Sei $C$ hinreichend groß, aber fest, und setze $h=aC^{-1/3}$ mit einer kleinen, von $C$ unabhängigen Konstante $a>0$. Teile $[X,2X]$ in volle Teilintervalle der Länge $hX$. Wähle $\eta=\kappa h$ mit einer kleinen konstanten Zahl $\kappa>0$.

Für zwei nahe optimale Listen in demselben Teilintervall unterscheiden sich die Anzahlen jeder Spinart um höchstens $\nu_j hX+4\eta X=O(hX)$. Auch die Zielflächen unterscheiden sich um höchstens $hX$. Deshalb haben die drei nichtursprünglichen Einbettungen der Restdifferenz Betrag höchstens $B hX$ mit einer festen Konstante $B$, wenn $\kappa\le1$. Die ursprüngliche Differenz ist höchstens $CX^{-3}$. Wäre die Restdifferenz ungleich null, hätte die algebraisch ganzzahlige dreifache Restdifferenz Norm mindestens eins. Andererseits ist ihr Normbetrag höchstens $81 B^3 C h^3=81 B^3 a^3<1$ für hinreichend kleines $a$. Damit haben alle nahe optimalen Listen desselben Teilintervalls denselben Rest und folglich dieselbe Spin-1-Anzahl.

Diese feste Anzahl ist nur auf einem Teilstück der Länge $O(\eta X)$ mit der optimalen Spin-1-Dichte verträglich. Für hinreichend kleines festes $\kappa$ lässt dies mindestens die Hälfte der geraden Ziele jedes vollen Teilintervalls ohne nahe optimale Liste, bis auf Rundung an den Enden. Auf diesen Zielen ist die Entropielücke mindestens von Ordnung $\eta^2$: Für Listenanteile $q$ gilt $D(q\|p)\ge\tfrac12\sum_j(q_j-p_j)^2$, denn die Hesse-Matrix von $\sum_j q_j\ln q_j$ hat im Inneren Diagonaleinträge $1/q_j\ge1$, und die Abschätzung setzt sich stetig bis zum Rand fort. Die Abbildung von Listenanteilen auf Flächendichten $q_j/\sum_i q_i r_i$ ist auf dem endlichen Träger gleichmäßig Lipschitz. Der zusätzliche Unterschied zwischen $A$ und $N$ ist vernachlässigbar. Die Ableitung der Rate aus der relativen Entropie ergibt damit einen Verlust mindestens $c C^{-2/3}$ für eine feste Konstante $c>0$, bis auf $o(1)$ für $X\to\infty$. Die polynomial vielen Zusammensetzungen ändern diese Rate nicht.

Zusammen mit der konstruktiven unteren Rate $s_F-O(C^{-2/3})$ für alle großen geraden Ziele hat der Verlust im unteren Grenzwert als Funktion großer fester Vorfaktoren $C$ genau die Ordnung $C^{-2/3}$. Dies bestimmt keine exakte Konstante oder obere Teilfolgenrate. Es gilt für den deklarierten Vier-Arten-Träger und seine Fensterzählung, nicht als native T-Flächenauflösung.

### Kritische Exponentenlücke auf vollständigen multiquadratischen Trägern

Erkundung. Fixiere eine endliche Spinmenge mit Minimalspin, deren Flächenquotienten im multiquadratischen Körper $K$ vom Grad $D>1$ liegen. Setze zusätzlich voraus, dass die Menge für jede Radikalbasisrichtung mindestens eine Spinart mit einem positiven rationalen Vielfachen dieser Richtung enthält. Sei $s_F$ der volle Listenexponent dieser Menge. Im Fenster $C/N^{D-1}$ liefert die Einheitenkorrektur bei großem festem $C$ höchstens $O_F(N C^{-1/(D-1)})$ Änderungen. Damit beträgt der Verlust der unteren Grenzrate höchstens $O_F(C^{-2/(D-1)})$, durch den quadratischen Entropieverlust um den strikt positiven optimalen Listenvektor. Linke Singulettschließung, rechte Balance und Diederprojektion kosten für die konstruierten Listen nur polynomiale Faktoren.

Für die Gegenrichtung zerlege jeden großen Zielblock $[X,2X]$ in Intervalle der Länge $hX$ mit $h=a C^{-1/(D-1)}$. Innerhalb eines Intervalls haben nahe optimale Listen, deren Spinanzahldichten höchstens $\eta=\kappa h$ vom Optimum abweichen, konjugierte Restdifferenzen $O_F(hX)$. Der ursprüngliche Restunterschied ist höchstens $CX^{-(D-1)}$. Nach Multiplikation mit einem festen gemeinsamen Nenner ist das Normprodukt höchstens eine feste Konstante mal $Ch^{D-1}$. Wähle $a$ klein genug, dass dieser Wert kleiner als eins ist. Damit können nahe optimale Listen in demselben Intervall nur einen gemeinsamen Rest haben.

Bei mehreren Spinarten mit demselben Radikal legt der Rest nicht mehr deren einzelne Anzahlen fest. Er legt aber die gewichtete Summe der Anzahlen innerhalb jeder nichttrivialen Radikalklasse fest. Mindestens eine solche Klasse hat im Optimum positive Dichte. Ihre feste gewichtete Summe kann nur auf einem Teilstück der Länge $O_F(\eta X)$ nahe an der optimalen Dichte liegen. Mit kleinem $\kappa$ bleibt auf einem positiven Anteil der Ziele ein Dichteabstand der Ordnung $h$. Die relative Entropie liefert dort einen Verlust mindestens $\Omega_F(h^2)$. Die polynomial vielen Zusammensetzungen ändern den Exponenten nicht.

Damit beträgt der Verlust der unteren Grenzrate im kritischen Fenster auf einem solchen festen Träger $\Theta_F(C^{-2/(D-1)})$ für große feste Vorfaktoren. Die Vollständigkeit der Radikalrichtungen wird für die konstruktive Seite gebraucht. Die obere Begrenzung durch das Normargument benötigt sie nicht. Das Gesetz beschreibt den unteren Grenzwert auf dem deklarierten Modellträger und bestimmt keine native T-Auflösung.
