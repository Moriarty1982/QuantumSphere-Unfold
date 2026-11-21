# OP5 – Durchgangsreferenz und Kriterien für J-Ausbreitung und Kopplung

21. November 2026. Analytische Erkundungen im Materieframe M. Die drei Prüfungen greifen die [Einwegfrage](OP5_J_Einweg_Ruecklauf.md) und die dort abgeleiteten Parallelspuren auf. Der [gekreuzte Vergleich](OP5_J_Gekreuzte_Schaltkontrolle.md) liefert das illustrative Budget von $5\cdot10^{-7}$ für den gemischten komplexen Anschlussrest. Die Einordnung folgt der lokalen Auslese im [Gesamtbild](../../../wiki/Gesamtbild.md). I3 benötigt weiterhin eine eigenständige kosmologische Bestandsdynamik.

## A-Durchgang bei zwei Laststellungen

Die A-Wellen werden an zwei bekannten kanonischen Referenzebenen kohärent gemessen, von links einfallend $a_L$, von rechts einfallend $a_R$ und nach rechts auslaufend $b_R$. Bei festem Marker- und Schaltzustand gilt im linearen skalaren Zweitor
$$
y=t+r x,\qquad x=a_R/a_L,\quad y=b_R/a_L,\quad t=S_{21},\quad r=S_{22}.
$$
Die beiden Laststellungen müssen dieselbe Streumatrix sehen. Sie ändern die einfallende Rückwelle $x$. Ihre Beträge und Phasen werden am Port gemessen. Das erlaubt die direkte Bestimmung des links-rechts-Durchgangs auch bei verbleibender Rückwelle:
$$
\widehat t=\frac{\widehat x_2\widehat y_1-\widehat x_1\widehat y_2}{\widehat x_2-\widehat x_1}.
$$
Die Faktoren $t$ und $r$ können unabhängig von der Gegenrichtung sein. Mit $|\widehat x_i-x_i|\le\epsilon_x$, $|\widehat y_i-y_i|\le\epsilon_y$ folgt
$$
|\widehat t-t|\le
\frac{(|\widehat x_1|+|\widehat x_2|)(\epsilon_y+|r|\epsilon_x)}
     {|\widehat x_2-\widehat x_1|}.
$$
Der Nenner ist die tatsächlich erreichte Trennung der Lastzustände. Ein einzelner Durchgang bei unbekannter Rückwelle enthält den Term $r x$. Eine Laständerung, die zusätzlich den Marker, die Sende- oder Empfangsmoden oder den gesamten Schaltzustand verändert, braucht einen separaten Modellrest. Die Rechnung setzt die kontrollierte skalare A-Projektion voraus. Offene oder ungemessene J-Rückwellen gehen zusätzlich in den Rest.

An jeder Bandgrenze wird $t$ für alle vier Marker-/Schalterzustände wiederholt. Der Kreuzquotient der vier lokalen $t_{ms}$ gibt den wirklichen Durchgangskontrast an diesen Ebenen. Mit unabhängig bekannter Durchgangsnormalisierung kann sein Vergleich mit dem äußeren Signal- oder Monitorquotienten den gemischten Anschlussrest bestimmen. Dazu müssen die lokalen Richtkoppler und ihre Phasenreferenzen getrennt kalibriert sein. Ein unbekannter vierzustandsabhängiger Gain der lokalen Koppler würde denselben gemischten Rest erneut einführen. Die zwei Lasten entfernen den Term der einfallenden Gegenwelle.

Im Zahlenbeispiel gelten $x_1=-0{,}02$, $x_2=+0{,}02$, $\epsilon_x=\epsilon_y=10^{-8}$, $|r|\le1$ und $|t_{ms}|\ge0{,}99$. Der Betrag des Durchgangsfehlers ist je Zustand höchstens $2{,}001\cdot10^{-8}$. Der Logfehler des Kreuzquotienten beträgt höchstens $8{,}081\cdot10^{-8}$, indem für jeden der vier Werte $-\log(1-|\widehat t-t|/|t|)$ summiert wird. Mit einer **separat belegten** Grenze von $4\cdot10^{-7}$ für alle übrigen Abgleichfehler an den Referenzebenen bliebe der Gesamtwert unter $4{,}809\cdot10^{-7}$. Das erfüllt das illustrative Ziel. Die Genauigkeit der Richtkoppler und der übrige Abgleich sind Anforderungen an den Aufbau.

## J-Ausbreitung aus mehreren Streckenlängen

Für eine isolierte Mode mit festen, separat abgeglichenen Anschlüssen ist an einer Frequenz $s_n=B\exp[(-\alpha+ik)(L_0+nd)]$ zu erwarten. Drei gleichmäßig gestaffelte freie Längen testen die Gleichheit der zwei komplexen Quotienten $s_{n+1}/s_n$, äquivalent zu $s_0s_2=s_1^2$ bei von null verschiedenen Signalen. Der Betrag liest die Dämpfung und die kohärent entfaltete Phase liest $kd$. Der Phasenzweig braucht einen unabhängigen Anker oder eine zusätzliche Distanz mit bekannter Fehlerhülle. Bei relativem komplexem Messfehler $\epsilon<1$ pro Wert kommen höchstens $-2\log(1-\epsilon)$ je Logquotient und $-4\log(1-\epsilon)$ zur Logabweichung des Abschlusses hinzu. Anschlussdrift und Mehrweganteile brauchen eigene Grenzen.

Eine positive entfaltete Längenphase schließt einen einzelnen rein evaneszenten Ast im verlustfreien freien Vergleich aus. Sie genügt bei mehreren Beiträgen nicht. Schon $s_n=2^{-n}-i4^{-n}$ enthält nur zwei rein abklingende Beiträge und erzeugt komplexe Quotienten. Im Beispiel verletzen sie den Drei-Längen-Abschluss. Umgekehrt kann eine Überlagerung genügend vieler evaneszenter Beiträge mit beliebigen komplexen Amplituden jede endliche Folge bei gleichmäßig gestaffelten Längen reproduzieren, weil die zugehörige Vandermonde-Matrix invertierbar ist. Der Abschluss dient als Konsistenztest, zusammen mit A-Ausblendung, Mehrwegkontrolle und Anschlussabgleich. Für die freie massive Vergleichsdispersion muss über mehrere Frequenzen derselbe Wert von $E^2-(\hbar c k)^2$ folgen. A-Durchschlag muss dabei unabhängig ausgeschlossen oder begrenzt werden. [Sende- und Empfangsports](OP5_J_Sende_Empfangsports.md)

Bei invertierbaren Zweikanalports und festem $M_n=L D^n R$ kann $M_0^{-1}M_1=R^{-1}DR$ die beiden Längenfaktoren auch ohne vorab reine J-Projektion lesen. $M_2=M_1M_0^{-1}M_1$ ist dann der Matrixabschluss. Ein bekannter A-Zweig hilft bei der Zuordnung. Die HCl/H-Anschlusskondition bleibt für die Inversion erforderlich.

## Basisunabhängiges Kriterium für die native Laufphase

Im homogenen, isotropen, verlustfreien und masselosen Zweikanal-Hauptteil seien $K_E$ und $K_B$ die positiv definiten elektrischen und magnetischen Kinetikmatrizen. Die quadrierten Geschwindigkeiten sind die Eigenwerte von $K_E^{-1/2}K_B K_E^{-1/2}$. Ihre quadrierte Differenz ist
$$
(v_+^2-v_-^2)^2=\bigl[\operatorname{tr}(K_E^{-1}K_B)\bigr]^2-4\det(K_E^{-1}K_B).
$$
Simultane Feldumdefinitionen ändern diese Größe nicht. Sie verschwindet genau für $K_B=\lambda K_E$, $\lambda>0$. Ein gemeinsamer skalarer Faktor lässt beide Hauptsymbolkegel zusammenfallen. Um eine gemeinsame Referenzkinetik $K$ ist der spurfreie Teil von $\frac12 K^{-1/2}(\delta K_E-\delta K_B)K^{-1/2}$ das lokale Kriterium für die Indexaufspaltung erster Ordnung. Der [Wellenvergleich](OP5_J_Wellenauslese.md) und der [Tensorvergleich](OP5_J_Tensorkopplung.md) liefern entsprechend einen gemeinsamen beziehungsweise einen unterschiedlichen elektrischen und magnetischen Beitrag. Im Tensorvergleich wird der Koeffizient vorgegeben. Für einen nativen Nachweis ist er samt A-Referenz aus der tatsächlichen Wirkung abzuleiten.

Für messbare getrennte Zweige müssen die kanonischen Sende- und Empfangsvektoren nichtverschwindende Produkte über den jeweiligen Modenprojektor haben. Eine lokale Aufspaltung allein garantiert keine integrierte Laufphase bei räumlich wechselndem Kontrast. Masse, höhere Dispersion, Verluste und Grenzflächen liegen außerhalb dieses Hauptsymbolkriteriums. Freie J-Ausbreitung und native Kopplung bleiben offen.

## Rechenkontrolle

Wolfram prüfte den Durchgangsinterzept und seine Fehleridentität exakt und wertete das illustrative Kalibrierbudget aus. Der Längenabschluss, das evaneszente Gegenbeispiel und die invarianten Kinetikfälle wurden ebenfalls kontrolliert. Die Rechnungen betreffen klassische Übertragungskoeffizienten und Hauptsymbole. Qiskit wurde erwogen; eine Quantenschaltung ist hier nicht Teil des Modells.

[Wolfram-Skript](op5_j_durchgang_parallelpruefung.wl) · [Tatsächliche Ausgabe](op5_j_durchgang_parallelpruefung.txt) · [Laufmanifest](op5_j_durchgang_parallelpruefung.json)
