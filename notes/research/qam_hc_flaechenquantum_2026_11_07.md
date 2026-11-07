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
