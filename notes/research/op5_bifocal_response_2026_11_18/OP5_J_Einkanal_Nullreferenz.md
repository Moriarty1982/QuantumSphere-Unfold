# OP5 – Kohärente A-Referenz mit zwei flankierenden Nullmessungen

21. November 2026. Analytische Erkundung im Materieframe M. Für beide Endfrequenzen des 100-MHz-Beispiels wird eine komplexe Einkanalmessung am A-Port betrachtet. Die Rechnung liefert hinreichende Grenzen für Anschlussabweichungen, Zeitdrift und J-Beimischung.

## Vorwissen geprüft

Der [Matrix-Nullpfad](OP5_J_Nullpfad_Abgleich.md) kürzt feste Anschlussfaktoren bei unabhängiger Nullstellung im gleichen Zweig. Die [Endpunktdrift](OP5_J_Endpunktdrift.md) nutzt symmetrische Referenzzeiten für Laufzeitdrift. Hier betrifft der symmetrische Vergleich den komplexen Gain an jeder einzelnen Endfrequenz. Die [komplexe Feldreferenz](OP5_J_Komplexe_Referenz.md) begrenzt die Fehler der Spurauslese. Die [Diagonalrechnung](OP5_J_Diagonalreferenz.md) lässt einen Rest von mindestens $4{,}596\cdot10^{-6}$ nach Rücklauf und skalarem Modellrest. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Was die Nullmessung bestimmt

Seien $f=(f_J,f_A)^{\mathsf T}$ der eingespeiste Feldvektor und $l=(l_J,l_A)$ die Empfangszeile in der kanonischen Flussbasis. Der Nenner der idealen Nullmessung ist $lf$. Für eine unabhängige Identitätsstellung der Strecke und dieselben Anschlüsse beim Signal ergibt die komplexe Division $q=lTf/(lf)$. Ein gemeinsamer Frequenzgang der Anschlüsse kürzt sich bei jeder Frequenz für sich. Ist der Referenztransfer nur als bekannter skalarer Faktor gegeben, muss dieser Faktor vor der Division auf eins normiert werden. Referenzebenen und freie Laufphase müssen zu denjenigen der Modelltransmission passen.

Eine Schaltung, die zugleich einen unbekannten komplexen Gewinn $\chi$ ändert, liefert das Produkt $\chi q$. Dieses Produkt bestimmt $q$ erst mit einem unabhängigen Abgleich von $\chi$. Ein paralleler Nullzweig braucht denselben Abgleich. Eine tatsächliche Rückwirkung ist zusätzlich relativ zu den gewählten Referenzebenen zu bestimmen. Das Beispiel übernimmt den bereits budgetierten Rücklaufrest und verwendet für die Kalibrierung eine Einzelpassreferenz.

## Symmetrische Nullmessung gegen zeitliche Drift

Je Frequenz liegen zwei Nullmessungen bei den Zeiten $-h$ und $h$ sowie die Markermessung bei $0$. Sei $H(t)$ der gemeinsame komplexe Nullgewinn ohne Messfehler, einschließlich der Anschlüsse und der kohärenten Quelle. Auf dem Zeitintervall sei $H(t)\ne0$ und $g(t)=\log H(t)$ eine entlang der Nullphase stetig verfolgte Wahl. Das gemessene Nullsignal bei $\pm h$ ist $H(\pm h)(1+\epsilon_\pm)$ und das Markersignal $M=H(0)q\chi(1+\epsilon_M)$. Die $\epsilon_i$ sind relative komplexe Messfehler gegenüber den jeweiligen fehlerfreien Signalen. Eine dafür verwendete absolute Rauschschranke muss durch eine unabhängig begrenzte Mindestamplitude des jeweiligen Signals geteilt werden.

Die Referenz am Signalzeitpunkt ist die Exponentialfunktion des Mittels der beiden fortgesetzten Null-Logarithmen. Der Schätzer lautet
$$
\widehat q=M\exp[-(\log N_-+\log N_+)/2].
$$
Mit $\sup |g''|\le K$, $|\log\chi|\le d$, $|\epsilon_i|\le e_i<1$ gilt
$$
|\widehat q-q|\le |q|(e^B-1),\qquad
B=d+\frac{Kh^2}{2}-\log(1-e_M)-\tfrac12\log(1-e_-)-\tfrac12\log(1-e_+).
$$
Der Term $Kh^2/2$ ist die Normgrenze des symmetrischen Taylorrests. Ein in der Zeit affiner komplexer Loggewinn kürzt sich exakt, also auch eine linear driftende Phase. Die Logarithmen der relativen Messfehler verwenden den Zweig bei eins. Dafür folgt die Betragsgrenze aus der Potenzreihe von $\log(1+\epsilon)$. Alle Grenzen gelten getrennt an beiden Bandenden.

Die Phasenfortsetzung ist eine beobachtbare Voraussetzung. Zwei isolierte Nullphasoren reichen zur Wahl des Zweiges nicht. Bei $H(t)=\exp(i\pi t/h)$ sind beide Nullwerte $-1$, während $H(0)=1$ gilt. Ein konstanter Gewinn $H=-1$ hätte dieselben Nullwerte, aber einen anderen Mittelwert. Die Zeitmessung braucht daher einen phasenstetigen Monitor oder eine unabhängig abgesicherte Grenze für die entfaltete Phasenänderung, sodass der richtige Phasenunterschied eindeutig ist. Bei gleicher Zeitreferenz für beide Frequenzen kann derselbe Monitor verwendet werden, wenn er diese Bedingung an beiden erfüllt.

## J-Beimischung der Einkanalprojektion

Für $f_A l_A\ne0$ seien $\alpha=l_J/l_A$ und $\beta=f_J/f_A$. Diese Größen werden am Signalzeitpunkt in der Feldbasis bestimmt. Für $|\alpha\beta|<1$ gilt
$$
q-T_{AA}=
\frac{\alpha T_{JA}+\beta T_{AJ}+\alpha\beta(T_{JJ}-T_{AA})}{1+\alpha\beta}.
$$
Bei passiver Einzelpasstransmission ist $|T_{JJ}-T_{AA}|\le2$. Sind beide Kopplungsverhältnisse höchstens $p$ und die beiden Modenumwandlungseinträge höchstens $m$, folgt
$$
|q-T_{AA}|\le \frac{2mp+2p^2}{1-p^2}.
$$
Mit geprüfter Passivität ist $|q|\le1+|q-T_{AA}|$, auch wenn die Empfangszeile und der Sendervektor verschiedene Modenanteile haben. Das berücksichtigt die Verstärkung des zeitlichen Fehlers durch die Projektion.

Das volle Markermodell hat $m\le0{,}00317$. Um den Projektionsfehler unter $2\cdot10^{-6}$ zu halten, genügt $p\le2{,}890\cdot10^{-4}$. Für eine tatsächlich diagonal verifizierte Vergleichsstrecke genügt für denselben Grenzwert $p\le9{,}9999\cdot10^{-4}$. Letztere kann $t_A$ als skalaren Vergleichswert liefern, sofern ihre A-Transmission auf die Referenzebenen und die Bedingungen der Markerschicht abgeglichen ist. Andernfalls muss deren komplexe Differenz als eigener Beitrag erfasst werden. Eine Messung am vollen Marker zielt direkt auf $T_{AA}$. Der bisherige skalare A-Modellrest kann für diese Variante konservativ im Budget stehen bleiben.

## Illustratives Budget je Bandende

Aus dem bisherigen Rest von $4{,}596\cdot10^{-6}$ werden jeweils $2\cdot10^{-6}$ für Zeitdrift samt Schalt- und Messfehlern sowie für Projektionsfehler angesetzt. Es bleiben $5{,}96\cdot10^{-7}$ für weitere Beiträge. Für eine Halbspanne $h=1$ s, alle relativen Messfehler höchstens $2{,}5\cdot10^{-7}$ und $|\log\chi|\le5\cdot10^{-7}$ genügt für den Zeitanteil $K\le1{,}999\cdot10^{-6}\ {\rm s}^{-2}$. Dabei wurde $|q|\le1+2\cdot10^{-6}$ eingesetzt. Diese Werte sind Anforderungen an einen Aufbau und müssen für die beiden tatsächlich gemessenen Frequenzen belegt werden.

Für die Matrixmessung bleibt eine eigene untere Schranke für die kleinste Singulärzahl des HCl/H-Zweikanalanschlusses erforderlich. Freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigt den exakten Projektionsrest, die symmetrische Auslöschung der linearen Drift und das Gegenbeispiel zur Phasenwahl. Beide gerundeten Fehlergrenzen wurden mit den nichtlinear fortgepflanzten Ausdrücken kontrolliert. Qiskit wurde erwogen. Die Rechnung betrifft komplexe klassische Übertragungskoeffizienten und benötigt keine Quantenschaltung.

[Wolfram-Skript](op5_j_einkanal_nullreferenz.wl) · [Tatsächliche Ausgabe](op5_j_einkanal_nullreferenz.txt) · [Laufmanifest](op5_j_einkanal_nullreferenz.json)
