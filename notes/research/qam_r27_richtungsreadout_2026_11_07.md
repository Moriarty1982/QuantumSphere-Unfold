# r27 in QAM: Rotation, Richtungsmittel und Messung

7.11.2026. Analytische Erkundung, T14/T15. Vorwissen: [r27.1](v4_10_0_r26_r31/rounds/v490_r27_round.tex), [Rückweg-Auslesung](qam_quelle_rueckweg_auslesung_2026_11_07.md), [Routeninventar](op5_route_inventory_2026_11_06.md), [C5-Detektor](../../analysis/OP5_QAM_Nulluebergang.md). Die Prüfung betrifft das vorhandene lokale Register und seine Auslesungen. Die zurückgestellten Ideen I1–I4 liefern dafür keine benötigten Daten.

## Rechenwege im selben Profil

Für $\rho=(I+x\sigma_x+z\sigma_z)/2$ mit $x^2+z^2\le1$ benutzen beide Richtungen dieselbe Bloch-Auslesung $(x,z)$ und dieselbe Kompensatorachse. Setze $c=\cos 2\alpha$, $t=\sin 2\alpha$. Aus $U_\alpha=e^{-i\alpha\sigma_y}$ und der Konjugation $U\rho U^\dagger$ folgen

$$
f=(cx+tz,cz-tx),\qquad b=(cx-tz,cz+tx),\qquad
m=c(x,z),\qquad d=t(z,-x).
$$

Beide Rotationen erhalten die Bloch-Länge. Bei festgehaltener Feldskala $2u$ erhalten sie somit $|s|=2u\sqrt{x^2+z^2}$ im r27-Modell. Das Richtungsmittel hat dagegen die Länge $|c|\sqrt{x^2+z^2}$. Für $c\ne0$ bestimmt das **volle** gemittelte Register die Richtungsausgaben über $(x,z)=m/c$. Bei $c=0$ geht diese Eindeutigkeit verloren. Die lineare Mittelung erhält die nichtlineare Norm im Allgemeinen nicht. Eine lineare, klassenkompatible OP1–OP5-Invariante oder eine Identifikation mit der nativen Klasse ist damit nicht nachgewiesen.

## Konkrete Kollision bei der Portauslesung

Die r27-Portauslesung ist $p(x,z)=(1+x)/2$. Für die beiden Richtungen gilt $p_\pm=(1+cx\pm tz)/2$. Wähle $\alpha=\pi/6$ aus r27 und die beiden zulässigen reinen Eingaben $(0,1)$ und $(0,-1)$. Beide haben vorab $p=1/2$ und dasselbe gemittelte Portsignal $1/2$. Ihre geordneten Richtungssignale sind

$$
\left(\frac{2+\sqrt3}{4},\frac{2-\sqrt3}{4}\right)
\quad\text{und}\quad
\left(\frac{2-\sqrt3}{4},\frac{2+\sqrt3}{4}\right).
$$

Die gerichtete Portauslesung faktorisiert also nicht durch den einzelnen Ausgangsportwert oder den gemittelten Portwert. Der Zusatz $z$ zum Ausgangsportwert genügt. Alternativ genügt die vorzeichenbehaftete halbe Portdifferenz $tz/2$ zum Portmittel.

## Messschritt separat

Die nichtselektive Messung ist $D:(X,Z)\mapsto(X,0)$. Sie lässt das jeweilige Portsignal unverändert. Bei den Eingaben $(0,\pm1)$ bleiben die beiden Richtungsausgaben nach der Messung verschieden, weil ihr Unterschied auf der $x$-Achse liegt. Bei der Kompensator-Eingabe $(1,0)$ sieht man den anderen Fall. Vor der Messung sind die beiden Rotationen $(1/2,\mp\sqrt3/2)$, danach liefern beide $(1/2,0)$. Die Messung entfernt hier die gesamte Richtungsdifferenz und senkt die Bloch-Länge von $1$ auf $1/2$. Die Richtungsinformation fehlt somit je nach Eingabe an verschiedenen Abbildungen.

Die QAM-Zuordnung für diese Erkundung führt Rotation, Portauslesung, Richtungsmittel und nichtselektive Messung als getrennte Operationen im selben r27-Profil. Die Labels $+$ und $-$ bezeichnen Rotationsrichtungen. Ein Wechsel zwischen M, T und P wird daraus nicht abgeleitet.

## Quadratisches Register für die Quelle–Rückweg-Invariante

Analytische Fortsetzung. Wähle für $v=(x,z)^{\mathsf T}$ das zweite Moment $Q(v)=vv^{\mathsf T}$. Das gerichtete Register transformiert unter den r27-Drehmatrizen $R_\pm$ als $Q(R_\pm v)=R_\pm Q(v)R_\pm^{\mathsf T}$. Die Spur ist auf symmetrischen Matrizen linear und liefert $\operatorname{tr}Q(v)=|v|^2$. Sie unterscheidet die Bahnklassen der vollen kontinuierlichen r27-Rotationsfamilie. Diese Klassenwahl gehört zum lokalen Modell.

Mit $f=m+d$ und $b=m-d$ gilt

$$
\frac{Q(f)+Q(b)}2=Q(m)+Q(d).
$$

Damit stimmt die Spur des gemittelten **quadratischen** Registers mit der Quellspur überein. Wer zuerst die Richtungen im Bloch-Register mittelt und danach quadriert, erhält nur $|m|^2$. Der Unterschied ist exakt $|d|^2=\sin^2(2\alpha)|v|^2$. Für $v=(1,0)$ und $\alpha=\pi/6$ ergibt sich vor der Mittelung im quadratischen Register die Spur $1$, beim Quadrieren des Mittels dagegen $1/4$. Die fehlenden $3/4$ sind die quadrierte Richtungsdifferenz.

Das lokale Modell erfüllt die Erhaltungsannahmen des Quelle–Rückweg-Schemas für die beiden reinen Rotationen. Der zulässige Träger ist die Bloch-Scheibe, beide Transporte halten die Bahnklasse fest, die Spur faktorisiert durch diese Klasse und ist im Zielraum der symmetrischen Matrizen linear. Die r27-Messung $D=\operatorname{diag}(1,0)$ wirkt im quadratischen Register als $Q\mapsto DQD^{\mathsf T}$. Für einen gerichteten Zustand $(X,Z)$ sinkt die Spur um $Z^2$. Ihre Erhaltung verlangt also $Z=0$ am jeweiligen Messeingang. Das quadratische Register identifiziert $v$ und $-v$. Wer zusätzlich gerichtete Portwerte braucht, behält die linearen Koordinaten oder die getrennten Portwahrscheinlichkeiten. Die native Klassenidentifikation der OP1–OP5-Route bleibt offen.

## Lineare Observable auf zwei Kopien

Für zwei unabhängig und gleich präparierte r27-Kopien ist der Träger $\rho\otimes\rho$. Wähle die Observable $H=\sigma_x\otimes\sigma_x+\sigma_z\otimes\sigma_z$. Wegen der Produktpräparation gilt $\operatorname{tr}[H(\rho\otimes\rho)]=x^2+z^2$. Die gleichzeitige Rotation beider Kopien erhält $H$, weil sie die beiden Achsen orthogonal mischt und sich die Kreuzterme aufheben. Die dazugehörige lineare Auslesung gilt auch auf dem Mittel der beiden gemeinsam rotierten Zweikopienzustände. Das Produkt zweier einzeln gemittelter Kopien enthält dagegen auch entgegengesetzt rotierte Paare und liefert $c^2(x^2+z^2)$.

Im Heisenberg-Bild sendet die nichtselektive Kompensatormessung $\sigma_x$ auf $\sigma_x$ und $\sigma_z$ auf null. Auf beiden Kopien zusammen ersetzt sie $H$ daher durch $\sigma_x\otimes\sigma_x$. Die Differenz ist die explizite Observable $\sigma_z\otimes\sigma_z$, deren Erwartung auf zwei identischen gedrehten Eingaben $Z^2$ ist. Im Beispiel $(1,0)$ bei $\alpha=\pi/6$ sind Quellwert, Wert nach gemeinsamer Rotation und Messwert $1,1,1/4$. Die Produktannahme ist wesentlich. Für beliebige korrelierte Zweikopienzustände misst $H$ die Summe der beiden Korrelationen.

Die normierte Zweikopienauslesung bestimmt bei bekannter Feldskala $2u$ den Betrag $|s|=2u\sqrt{\langle H\rangle}$. Für ein vorzeichenbehaftetes $s$ braucht das Profil zusätzlich eine Sektorzuordnung. Die r27-Rotationen und die lokalen Portwahrscheinlichkeiten allein liefern diese Zuordnung nicht.

## Teilweise gekoppelte Drehrichtungen

Die Richtungen $\epsilon_1,\epsilon_2\in\{+1,-1\}$ seien einzeln gleichverteilt. Ihr gemeinsamer Zustand wird durch $k=\mathbb E[\epsilon_1\epsilon_2]$ bestimmt. Die Wahrscheinlichkeit gleicher Richtungen beträgt $(1+k)/2$. Schreibe $v_i=m+\epsilon_i d$ mit $m=cv$ und $d=t(z,-x)$. Der Erwartungswert der Zweikopien-Observable ist

$$
\mathbb E[v_1\cdot v_2]=|m|^2+k|d|^2=(c^2+kt^2)|v|^2.
$$

Nach der Kompensatormessung auf beiden Kopien ist der Erwartungswert $c^2x^2+kt^2z^2$. Bei bekannter Quelllänge und $t^2|v|^2>0$ bestimmt die ungemessene Zweikopien-Auslesung $k$ eindeutig. Nach der Messung gilt das für diese Auslesung genau dann, wenn $tz\ne0$ und die Quellkoordinaten bekannt sind. Bei $z=0$ verschwindet ihre gesamte Abhängigkeit von $k$. Bei $x=0$ bleibt die gesamte $k$-abhängige Komponente erhalten. Für eine nichttriviale Richtungsdifferenz ist die Quellspur vor der Messung genau bei $k=1$ erhalten.

Bei $\alpha=\pi/6$ und $|v|=1$ ergibt sich vor der Messung $(1+3k)/4$. Für $v=(1,0)$ zeigt die Messung stets $1/4$. Für $v=(0,1)$ zeigt sie $3k/4$. Der negative Wert bei $k=-1$ ist ein Erwartungswert auf einem Paar mit entgegengesetzten Richtungen. Die Interpretation als quadrierte Länge gilt für identisch präparierte Produktkopien und für die hier betrachtete gemeinsame Rotation vor der Messung. Die Kopplung $k$ ist eine gewählte Erweiterung des r27-Protokolls.

## Unbekannte Präparation und Trennbarkeit der Kopplung

Nach der Kompensatormessung seien $Y_1,Y_2\in\{\pm1\}$ die beiden Portausgänge. Im Modell mit fairen Richtungen und bedingt unabhängigen Produktkopien gilt $\mu=\mathbb E[Y_i]=cx$ und $C=\mathbb E[Y_1Y_2]-\mu^2=kt^2z^2$. Die gesamte Portverteilung ist durch diese beiden Größen bestimmt, denn $P(Y_1=a,Y_2=b)=[1+(a+b)\mu+ab(\mu^2+C)]/4$. Bei derselben Messachse bestimmt eine Variation des Kickwinkels weiterhin nur $x$ und $kz^2$. Beispielsweise liefern $(x,z,k)=(0,1/2,1)$ und $(0,1,1/4)$ für jeden Winkel dieselbe Portverteilung.

Ein zweiter Durchlauf mit einer bekannten gemeinsamen Vorrotation $U_{\pi/4}$ sendet $(x,z)$ auf $(z,-x)$. Bei gleicher Präparation und demselben Richtungsprotokoll sind seine beiden Momente $\mu'=cz$ und $C'=kt^2x^2$. Für $ct\ne0$ liefern die Mittelwerte $x=\mu/c$ und $z=\mu'/c$. Für jeden nichtverschwindenden Eingang ist dann

$$
k=\frac{C+C'}{t^2(x^2+z^2)}.
$$

Bei $\alpha=\pi/6$ ergibt das für den ersten Beispielträger $\mu'=1/4$, für den zweiten $\mu'=1/2$. Beide haben $C=3/16$ und $C'=0$. Beim vollständig gemischten Eingang verschwinden beide Kovarianzen für jedes $k$. Das zusätzliche Protokoll setzt eine reproduzierbare Präparation, eine bekannte Vorrotation und dieselbe Kopplung in beiden Reihen voraus. In QAM ist die Vorrotation ein eigener Schritt am Zustand und gehört zur Definition der zweiten Auslesung.

## Was bleibt bei einer reinen Korrelationsauslesung?

Bei $\alpha=\pi/6$ liefern $(x,z,k)=(0,1,1/3)$ und $(1,0,1)$ nach der Messung beide $\mathbb E[Y_1Y_2]=1/4$. Ihre Einzelportmittel sind verschieden. Die folgende Frage betrifft ausschließlich den gespeicherten Zweikopienwert, ohne Einzelportmittel.

Sei $R$ eine bekannte gemeinsame Vorrotation in der Bloch-Ebene und $w=(X,Z)=Rv$. Der gespeicherte Wert ist $aX^2+bZ^2$ mit $a=c^2$ und $b=kt^2$. Betrachte nun einen zweiten Eingang $v'=\lambda Jv$, wobei $J$ eine Vierteldrehung in der Ebene ist. Weil $JR=RJ$, sind seine quadrierten Komponenten nach jeder Vorrotation $(\lambda^2 Z^2,\lambda^2 X^2)$. Für $a,b>0$ wähle $\lambda^2=b/a$ und $b'=a^2/b$. Dann stimmen beide Zweikopienwerte für jede Vorrotation überein, solange beide Eingaben und beide Kopplungen zulässig sind.

Ein exaktes Paar bei $\alpha=\pi/6$ ist

$$
(v,k)=((1/2,0),1),\qquad (v',k')=((0,\sqrt3/2),1/9).
$$

Für eine Vorrotation um den Bloch-Winkel $\beta$ liefern beide $(\cos^2\beta+3\sin^2\beta)/16$. Beide Zustände liegen in der Scheibe und beide Kopplungen in $[-1,1]$. Die Gleichheit betrifft die komplette Winkelkurve der skalaren Korrelationsauslesung. Ein zusätzlich gespeichertes Einzelportmittel trennt dieses Paar bereits bei $\beta=0$. Das Rekonstruktionsprotokoll mit zwei Mittelwerten und Kovarianzen aus dem vorherigen Abschnitt bleibt auf dem dort angegebenen Bereich eindeutig.

## Drei Werte zur Rekonstruktion, ein vierter zum Modellabgleich

Für $ct\ne0$ liefern die beiden Mittelwerte $\mu$ und $\mu'$ bereits $x$ und $z$. Bei einem nichtverschwindenden Eingang genügt danach eine geeignet ausgewählte Kovarianz. Falls $|z|\ge |x|$, verwende $k=C/(t^2z^2)$. Andernfalls verwende $k=C'/(t^2x^2)$. Damit wählt man immer den größeren der beiden möglichen Nenner. Eine vorab festgelegte Kovarianz hat dagegen auf einer der beiden Achsen keine Trennwirkung. Das ist eine Reduktion auf drei gespeicherte Skalare mit adaptiver Auswahl, keine Aussage über die minimale Zahl experimenteller Wiederholungen.

Wer beide Kovarianzen behält, kann zusätzlich prüfen, ob die zwei Reihen mit derselben Kopplung vereinbar sind. Für exakte Erwartungswerte lauten die Bedingungen

$$
x^2+z^2\le1,\qquad x^2C=z^2C',\qquad
|C+C'|\le t^2(x^2+z^2).
$$

Für $x^2+z^2>0$ sind sie notwendig und hinreichend. Die mittlere Gleichung macht $(C,C')$ proportional zu $(z^2,x^2)$, die letzte beschränkt den gemeinsamen Faktor auf das Intervall für $k$. Bei $x=z=0$ verlangt das Modell separat $C=C'=0$. Bei empirischen Schätzungen braucht der Vergleich eine Behandlung der Stichprobenunsicherheit.

Beispiel bei $\alpha=\pi/6$. Für $(x,z)=(3/5,4/5)$ und $k=1/2$ lauten die Mittelwerte $(3/10,2/5)$ und die Kovarianzen $(6/25,27/200)$. Die erste Kovarianz liefert bereits $k=1/2$. Ersetze nur die zweite durch $1/10$. Die Rekonstruktion aus drei Werten bleibt gleich, aber die vier Daten zusammen verletzen $x^2C=z^2C'$. Der Abgleich prüft die gemeinsame Modellbeschreibung. Er kann aus einer Verletzung allein keine bestimmte Ursache zuordnen.

## Abgleich mit der nativen Klasse

Erkundung im selben deklarierten Laborprofil der realen Feldlesart. Vorwissen: [Feldinvarianten und Sektoren](qsc_back_to_basic_idea_2026_11_06.md), [lokaler Feldvermittler](../../sources/research/parts/v410-state-mediator-synthesis.tex), [Routeninventar](op5_route_inventory_2026_11_06.md). Setze $n=|E|^2+|B|^2=2u$ und $s=(E+iB)\cdot(E+iB)$. Die Gram-Auslesung liefert $s/n=z+ix$ und $r=|s|/n$. Die Vergleichspaare liegen im Rang-zwei-Bereich.

| Feld $(E,B)$ | $n$ | $s$ | $r$ |
|---|---:|---:|---:|
| $(2e_x,e_y)$ | 5 | 3 | $3/5$ |
| $(4e_x,2e_y)$ | 20 | 12 | $3/5$ |
| $(-e_y,2e_x)$ | 5 | $-3$ | $3/5$ |

Die ersten beiden Felder haben sogar dasselbe vollständige normierte Gram-Register. Sie sind durch keine Komposition gewöhnlicher Lorentztransformationen und reeller Dualitätsrotationen verbunden, weil beide Operationen $|s|$ erhalten. Damit ist die normierte r27-Bahnklasse gröber als die Bahnrelation dieser konkreten Feldtransporte. Für den Unterschied genügt die Zusatzgröße $n$, denn $nr=|s|$.

Das erste und dritte Feld haben entgegengesetzte reelle $s$-Vorzeichen. Bei gewöhnlichen Lorentztransformationen sind sie getrennt, weil $s$ selbst invariant ist. Die aktive Dualität $E+iB\mapsto i(E+iB)$ verbindet sie dagegen explizit. Deshalb ist das Vorzeichen nur relativ zur gewählten Transportrelation ein Trennmerkmal. Das Vorzeichen ist aus dem vollen normierten Gram-Register bei reellem $s$ bereits über $z$ ablesbar. Aus Radius oder Spur des quadratischen Registers allein folgt es nicht.

Die native OP1–OP5-Klasse ist in Teil 22 durch zulässige HC-Transporte, Frame-Versätze und Verfeinerungen beschrieben. Das Paket legt weder einen auswertbaren Zulassungstest für diese Felder noch die Erhaltung von $|s|$ für alle seine Klassenerzeuger fest. Somit ist das Skalenpaar ein belegtes Gegenbeispiel für die konkrete Lorentz-/Dualitätsbahn, aber nur ein bedingter Trenner für die native Klasse. Für diese Folgerung wären die Zulassung beider Felder und die Faktorisierung von $|s|$ durch $K_{\rm ncl}$ zu zeigen. Die Feldrechnung erfordert keine neue Skalenherleitung und aktiviert keine der zurückgestellten Ideen.

## HC-Projektion und die native Zulassung

Die geprüften Teile 21/22, die QAM-Kernel-Brücke und das Routeninventar liefern keinen auswertbaren Zulassungstest für das Skalenpaar. „HC-confined“ bezeichnet in Teil 22 die Abgeschlossenheit des angenommenen Sektors unter den beiden Transporten. Die Schalen- und Zweigbedingungen verlangen Klassenerhaltung, geben hier aber keinen unabhängigen Feldtest dafür.

Für die konkrete Feldinvolution $J_Bw=i\bar w$ gilt beim ausgewählten Port $C_+(E+iB)=(1+i)(E+B)/2$ und daher $s(C_+w)=i|E+B|^2/2$. Auf dem Skalenpaar gehen somit $|s|=3,12$ in $5/2,10$ über. Falls diese einzelne Projektion als zulässiger Klassenschritt für eines der Felder aufgenommen wird, kann $|s|$ auf der betreffenden Klasse nicht konstant sein. Diese Rechnung entscheidet nicht, ob die native Route den Projektionsschritt tatsächlich zulässt.

Die beiden Ports gemeinsam erlauben eine engere Aussage. Mit $A=E+B$ und $D=E-B$ erhält man $s=A\cdot D+i(|A|^2-|D|^2)/2$. Der gemischte Term ist erforderlich. Beispielsweise haben $(A,D)=(e_x,e_y)$ und $(e_x,(3e_x+4e_y)/5)$ dieselben beiden Portnormen, aber $s=0$ bzw. $s=3/5$. Eine HC-Schnittstelle kann $s$ durch Mitführen beider Vektoren oder der drei reellen Auslesewerte $|A|^2,|D|^2,A\cdot D$ rekonstruieren. Diese Rekonstruktion ist ein lokales Ergebnis und setzt für die native Anwendung weiterhin eine konkrete Route und deren Zulassung voraus.

## Konkreter HC-Rückweg und dritte Normauslesung

Im selben Laborprofil ist die Zweiportroute $F=(E,B)\mapsto(A,D)=(E+B,E-B)$ linear und invertierbar. Der Rückweg ist $(E,B)=((A+D)/2,(A-D)/2)$. Damit ist der vollständige Feldrückweg auf dem reellen lokalen Feldträger definiert. Für die engere Aufgabe, nur $s$ zurückzugewinnen, genügen drei unnormierte quadratische Auslesungen

$$
N_+=|A|^2,\qquad N_-=|D|^2,\qquad N_E=|A+D|^2.
$$

Polarisation ergibt $A\cdot D=(N_E-N_+-N_-)/2$, sodass

$$
s=\tfrac12(N_E-N_+-N_-)+\tfrac i2(N_+-N_-).
$$

Die dritte Auslesung ist die Norm des kohärent addierten reellen Portvektors, äquivalent zu $4|E|^2$ im Laborprofil. Sie setzt Zugriff auf die gemeinsame Orientierung der Portvektoren oder direkten Zugriff auf die elektrische Feldnorm voraus. Zwei separat gespeicherte Portnormen ermöglichen diese Addition im Allgemeinen nicht. Für die Skaleneingaben sind die Tripel $(5,5,16)$ und $(20,20,64)$ und liefern $s=3$ bzw. $12$. Beim Paar mit gleichen Portnormen sind die Tripel $(1,1,2)$ und $(1,1,16/5)$ und liefern $s=0$ bzw. $3/5$.

Die lineare Auslesung des Normtripels liefert auch einen lokalen Rückweg auf der Ebene der Invariante. Für entgegengesetzte gewöhnliche Lorentz-Boosts können die drei Normen nach jeder Richtung separat ermittelt und dann gemittelt werden. Da jede Richtung $s$ erhält und die Auslesung im Normtripel linear ist, liest das Mittel dasselbe $s$ aus. Das ist eine konkrete Feldinstanz für die gewählte Klasse „gleiches $s$“ und gewöhnliche Lorentztransporte. Aktive Dualität ändert im Allgemeinen die Phase von $s$ und gehört nicht zu dieser Klassenwahl. Für gerichtete Feldrekonstruktion werden weiterhin die beiden vollständigen Portvektoren benötigt. Die Identifikation mit der nativen OP1–OP5-Klasse verlangt weiterhin deren Zulassungstest.

## Lorentz- und Dualitätsrückweg mit unnormierter Invariante

Aus dem HC-Normtripel bilde $w=(\operatorname{Re}s,\operatorname{Im}s)^{\mathsf T}$ durch die obige lineare Auslesung. Gewöhnliche Lorentztransporte lassen $w$ unverändert. Eine aktive Dualitätsdrehung $E+iB\mapsto e^{i\alpha}(E+iB)$ rotiert $w$ um $2\alpha$. Das unnormierte zweite Moment $Q_s=ww^{\mathsf T}$ transformiert daher durch orthogonale Konjugation und $\operatorname{tr}Q_s=|s|^2$ bleibt erhalten. Die Rechnung gilt auch für beliebige Kompositionen beider Transportarten und für die symmetrische Mittelung der beiden gerichteten $Q_s$-Werte.

Für einen expliziten Rückweg starte mit $(E,B)=(2e_x,e_y)$ und damit $s=3$. Bei $\alpha=\pm\pi/4$ entstehen die gerichteten Werte $s_\pm=\pm3i$. Die Normtripel sind $(8,2,10)$ beziehungsweise $(2,8,10)$. Das Mittel $(5,5,10)$ liest sich als $s=0$. Auf dem vollen Feld hat jedoch jeder Zweig $|s|=3$. Bildet man $Q_s$ vor dem Mitteln, liefern beide Zweige $\operatorname{diag}(0,9)$ und die Quelle $\operatorname{diag}(9,0)$. Die Spur bleibt $9$. Der Nullwert der komplexen Mittelung kennzeichnet eine Auslöschung im Readout. Er zertifiziert keinen nullartigen gerichteten Feldzustand.

Das ergibt eine lokale Instanz des Quelle–Rückweg-Schemas für die gewählte Klasse „gleiches $|s|$“ auf dem reellen Feldträger. Der unnormierte Aufbau trennt das Skalenpaar durch die Spuren $9$ und $144$. Er behauptet keine Vollständigkeit als Klassifikator aller Feldbahnen. Für die native OP1–OP5-Klasse bleibt die Zulassung und Erhaltung unter weiteren Klassenerzeugern zu zeigen.

## Nullprüfung für gewichtete Rückwege

Für endlich viele gerichtete Feldwerte $s_j$ und normierte Gewichte $p_j\ge0$ setze $\bar s=\sum_j p_js_j$ und $M_2=\sum_j p_j|s_j|^2$. Dann gilt

$$
M_2=|\bar s|^2+\sum_j p_j|s_j-\bar s|^2.
$$

Damit ist $M_2=0$ äquivalent zu $s_j=0$ für jeden Zweig mit positivem Gewicht. Zweige mit Gewicht null liegen außerhalb dieser Aussage. Für $M_2\le\varepsilon^2$ gilt auf einem Zweig mit $p_j>0$ nur $|s_j|\le\varepsilon/\sqrt{p_j}$. Im symmetrischen Zweigpaar ist die Schranke $\sqrt2\,\varepsilon$. Sie wird erreicht, wenn nur einer der beiden Werte ungleich null ist. Für das Dualitätspaar $s_\pm=\pm3i$ ist das Mittel null, während die gesamte Spur $9$ in der Abweichung vom Mittel liegt.

Die Aussage $s_j=0$ lässt auf dem reellen Feldträger das Nullfeld zu. Erfasse deshalb zusätzlich $n_j=|E_j|^2+|B_j|^2$ im deklarierten Beobachterprofil. Es gilt $n_j=0$ genau für das Nullfeld. Bei $M_2=0$ und $\bar n=\sum_jp_jn_j>0$ existiert mindestens ein nichtverschwindender nullartiger Zweig. Für diese Aussage auf **jedem** Zweig braucht man $n_j>0$ auf jedem Zweig mit positivem Gewicht oder eine Route, die Nichtverschwindung aus einem nichtverschwindenden Eingang erhält. Gewöhnliche Lorentztransporte und aktive Dualität sind invertierbar und erfüllen diese letzte Voraussetzung. $\bar n$ allein kann sie für eine beliebige Route nicht ersetzen.

Die Ausleseregel unterscheidet damit Auslöschung im Mittel, branchweise Nullartigkeit und Nichtverschwindung des Feldes. Sie setzt exakte Zweigwerte voraus. Eine Detektorschwelle für $M_2$ liefert nur die angegebene Schranke. Die physikalische Zuordnung zu einem Photon und die native OP1–OP5-Zulassung sind separate Bedingungen.

## Nullprüfung für die beiden HC-Projektionsausgänge

Für $w=E+iB$ und $J_Bw=i\bar w$ liefern die zwei Einzelport-Projektionen $w_+=(1+i)A/2$ und $w_-=(1-i)D/2$ mit $A=E+B$ und $D=E-B$. Ihre Feldinvarianten sind $s_+=i|A|^2/2$ und $s_-=-i|D|^2/2$. Jeder nichtverschwindende Port ist daher nichtnullartig. Für eine gleichgewichtete Auswertung der beiden projizierten Feldwerte gilt

$$
\bar s_{\rm HC}=\frac i4(|A|^2-|D|^2),\qquad
M_{2,\rm HC}=\frac{|A|^4+|D|^4}{8}
=\frac{n^2}{4}+\frac{(\operatorname{Im}s)^2}{4}\ge\frac{n^2}{4},
\qquad n=|E|^2+|B|^2.
$$

Für jedes nichtverschwindende Eingangsfeld ist das zweite Moment strikt positiv. Das komplexe Mittel kann trotzdem null sein, sobald $E\cdot B=0$. Beim bisherigen Eingang $(2e_x,e_y)$ sind die beiden Werte $\pm5i/2$, das Mittel ist null und das zweite Moment ist $25/4$. Auch ein nichtverschwindender nullartiger Eingang liefert hier zwei nichtnullartige Portfelder, etwa $(e_x,e_y)$ mit $s=0$ und $s_\pm=\pm i$.

Diese Mittelung betrifft die Auslesungen zweier projizierter reeller Feldträger bei festen gleichen Gewichten. Sie ist weder die kohärente Rekonstruktion $w=w_++w_-$ noch die r27-Messung auf Dichtematrizen mit ihren Portwahrscheinlichkeiten. Bei der kohärenten Rekonstruktion trägt der Kreuzterm $2w_+\cdot w_-=A\cdot D$ zur Feldinvariante bei. Die Einzelport-Nullprüfung setzt keine native OP1–OP5-Zulassung voraus.

## Was die beiden HC-Portnormen über das Eingangsfeld entscheiden

Halte $N_+=|A|^2$ und $N_-=|D|^2$ fest. Dann hat die Invariante des kohärent rekonstruierten Eingangs genau den Wertebereich

$$
s\in [-\sqrt{N_+N_-},\sqrt{N_+N_-}]
 +\frac{i}{2}(N_+-N_-).
$$

Cauchy–Schwarz gibt die Grenzen. Jeden Zwischenwert realisieren zwei reelle Portvektoren mit dem entsprechenden Winkel. Falls eine Norm null ist, kollabiert das Intervall auf einen Punkt. Verschiedene Portnormen schließen $s=0$ aus. Bei gleichen positiven Normen ist ein nichtverschwindendes nullartiges Eingangsfeld möglich, und es ist genau dann nullartig, wenn $A\cdot D=0$. Sind beide Normen null, liegt das Nullfeld vor.

Das frühere Paar $(E,B)=(2e_x,e_y)$ und $(E,B)=(\sqrt{5/2}\,e_x,\sqrt{5/2}\,e_y)$ zeigt die verbleibende Mehrdeutigkeit. Beide haben $N_+=N_-=5$, dieselben Einzelportinvarianten und dasselbe Portmoment $25/4$. Der kohärente Eingang hat aber $s=3$ beziehungsweise $s=0$. Die Zusatznorm $N_E=|A+D|^2$ liefert $16$ beziehungsweise $10$. Bei gleichen Portnormen ist der genaue Nulltest also $N_E=2N_+$. Das zweite Moment der projizierten Felder und die Nullprüfung des rekonstruierten Feldes haben verschiedene Zielobjekte.

## HC-Eingangstest mit Messintervallen

Für gemessene Normquadrate $\widehat N_+,\widehat N_-,\widehat N_E$ und garantierte absolute Fehler $\delta_+,\delta_-,\delta_E$ berechne $\widehat s$ mit derselben linearen Formel wie für exakte Daten. Dann gelten

$$
|\operatorname{Re}(s-\widehat s)|\le a=\tfrac12(\delta_E+\delta_++\delta_-),
\qquad
|\operatorname{Im}(s-\widehat s)|\le b=\tfrac12(\delta_++\delta_-).
$$

Das liefert die garantierte Schranke $|s|\le\sqrt{(|\operatorname{Re}\widehat s|+a)^2+(|\operatorname{Im}\widehat s|+b)^2}$. Schon disjunkte Intervalle für $N_+$ und $N_-$ schließen Nullartigkeit ohne dritte Messung aus.

Für einen **exakten Vereinbarkeitstest** mit den Messintervallen $I_+,I_-,I_E$ gilt

$$
J=I_+\cap I_-\cap\tfrac12 I_E\cap[0,\infty).
$$

Ein nichtverschwindendes nullartiges Feld ist genau dann mit den Intervallen vereinbar, wenn $J$ einen positiven Wert $q$ enthält. Die Notwendigkeit folgt aus $(N_+,N_-,N_E)=(q,q,2q)$. Für die Hinrichtung realisiert $(E,B)=(\sqrt{q/2}\,e_x,\sqrt{q/2}\,e_y)$ jedes solche Tripel. Das Nullfeld ist genau dann vereinbar, wenn $0\in J$. Diese Äquivalenz setzt voraus, dass die Messfehler ausschließlich durch die angegebenen Intervalle beschränkt werden. Bei zusätzlichen gemeinsamen Fehlerbedingungen kann sich die Menge verkleinern.

Bei den bisherigen Tripeln $(5,5,16)$ und $(5,5,10)$ mit jeweils absoluter Fehlerschranke $0{,}1$ ergibt sich im ersten Fall $J=\varnothing$. Im zweiten ist $J=[4{,}95,5{,}05]$. Dort ist ein nichtverschwindendes nullartiges Feld möglich. Für eine scharfe Schranke maximieren wir den Betrag der linearen Auslesung auf dem Intervallquader. Wegen Konvexität genügt der Vergleich seiner acht Eckpunkte. Bei gleichen Vorzeichen der beiden Portfehler ist der Betrag höchstens $0{,}15$. Bei entgegengesetzten Vorzeichen ist er höchstens $\sqrt{5}/20$. Das Maximum $0{,}15$ wird beim Tripel $(5{,}1,5{,}1,9{,}9)$ mit $s=-0{,}15$ erreicht. Dieses Tripel ist realisierbar, weil der gemischte Term betragsmäßig kleiner als $5{,}1$ ist.

## Gemeinsame Kalibrierfehler im HC-Nulltest

Die lineare HC-Auslesung sei $L(N)=s$. Bei einem gemeinsamen positiven Verstärkungsfaktor $g$ und einem gemeinsamen additiven Offset $b$ gilt für die gemessenen Normquadrate $\widehat N=gN+b(1,1,1)$. Da $L(1,1,1)=-1/2$, folgt

$$
\widehat s=g s-b/2,\qquad s=(\widehat s+b/2)/g.
$$

Ein gemeinsamer positiver Verstärkungsfehler erhält die Nullartigkeit. Ein gemeinsamer Offset verschiebt den Realteil und lässt die Aussage, ob der Imaginärteil null ist, unverändert. Bei gemessenen gleichen Portnormen kann ein nichtverschwindendes nullartiges Feld genau dann zu einem zulässigen Offset passen, wenn $b=2\widehat N_+-\widehat N_E$ zulässig ist und $\widehat N_+-b>0$. Denn dann ist das wahre Tripel $(q,q,2q)$ mit $q=(\widehat N_+-b)/g>0$.

Für die bisherigen Messdaten $(5,5,16)$ wäre $b=-6$ erforderlich. Mit $|b|\le0{,}1$ ist Nullartigkeit ausgeschlossen. Für $(5,5,10)$ ist exakt $b=0$ erforderlich. Bei $g=1$ und $|b|\le0{,}1$ folgt für dieses Tripel die scharfe Schranke $|s|\le0{,}05$. Die beiden Randwerte sind realisierbar, da die zugehörigen positiven Portnormen den erforderlichen gemischten Term zulassen. Mit drei separat begrenzten Fehlern war die scharfe Schranke $0{,}15$. Die stärkere Schranke beruht auf der gemeinsamen Offsetannahme. Sie gilt für dieses Messmodell, in dem alle drei Normquadrate dieselbe additive Verschiebung haben.

## Offsetfreie HC-Auslesung mit einer vierten Norm

Ergänze $N_B=|A-D|^2=4|B|^2$. Dann gilt

$$
s=\frac{N_E-N_B}{4}+\frac{i}{2}(N_+-N_-),\qquad
N_E+N_B=2(N_++N_-).
$$

Bei derselben affinen Kalibrierung $\widehat N_j=gN_j+b$ für alle vier Normen beseitigen die Differenzen den Offset. Der komplexe Wert aus den Differenzen ist $g s$. Auch bei unbekanntem positivem $g$ ist Nullartigkeit im exakten gemeinsamen Kalibriermodell somit entscheidbar. Das Parallelogrammgesetz identifiziert den Offset separat als $b=[2(\widehat N_++\widehat N_-)-(\widehat N_E+\widehat N_B)]/2$. Ein unbekannter Gain bleibt aus diesen vier Daten allein unbestimmt.

Beispiel mit $g=1$, $b=0{,}1$. Ein nullartiges Feld mit wahrem Tripel $(5,5,10)$ hat $N_B=10$. Die alte Dreierauslesung der gemessenen Werte ergibt $-0{,}05$. Die Differenzauslesung aus $(5{,}1,5{,}1,10{,}1,10{,}1)$ ergibt exakt null und die Parallelogrammformel rekonstruiert $b=0{,}1$. Für die Aussage, dass dieses Feld von null verschieden ist, genügt eine positive korrigierte Portnorm. Die Rechnung verwendet dieselbe affine Kalibrierung bei allen vier Messungen. Getrennte Restfehler erfordern zusätzliche Fehlerschranken.

## Die normierte Nullnähe beim Beobachterwechsel

Die vier Normen liefern bei gemeinsamer affiner Kalibrierung $r=|s|/n$ im deklarierten Beobachterprofil. Der gemeinsame positive Gain kürzt sich heraus. Ein Lorentz-Boost lässt $s$ unverändert, kann aber $n=|E|^2+|B|^2$ ändern. Für ein nichtverschwindendes Feld und zwei ausdrücklich per Boost verbundene Beobachter gilt deshalb $r'=r\,n/n'$. Die exakte Nullentscheidung bleibt erhalten, während eine positive Schwelle auf $r$ an das jeweilige Profil gebunden ist.

Für $E=2e_x$, $B=e_y$ und den in [gram-boost.tex](../../qam/examples/gram-boost.tex) deklarierten Boost entlang $z$ ist bei $c=1$

$$
n(v)=\frac{(2-v)^2+(1-2v)^2}{1-v^2}
     =\frac{5-8v+5v^2}{1-v^2},\qquad s(v)=3.
$$

Im Labor, bei $v=1/4$ und bei $v=-1/4$ ergeben sich $r=3/5$, $45/53$ beziehungsweise $5/13$. Eine beispielhaft gewählte Schwelle $r\le1/2$ wird nur beim dritten Beobachter unterschritten. Für $v\to-1$ wächst die Feldskala ohne Grenze und $r$ nähert sich null, obwohl $s=3$ bleibt. Die Folge besteht aus gewöhnlichen Beobachterboosts desselben Feldes. Sie ist keine dynamische Annäherung eines Feldes an $s=0$.

Beim Vergleich zweier Messprofile mit unabhängig unbekanntem Gain lassen sich die skalierten Feldnormen $gn$ nicht direkt als $n/n'$ vergleichen. Die Relation $r'=r\,n/n'$ verlangt eine erklärte Boostabbildung mit den nötigen Felddaten oder einen kalibrierten Vergleich der Feldnormen. Die lokale relative Fehlerschranke allein liefert diese Abbildung nicht.

## Kleinste Feldskala über Lorentz-Beobachter

Setze $P=|E\times B|$. Direkt aus dem Skalar- und Kreuzprodukt folgt $n^2-|s|^2=4P^2$. Daher gilt für jeden Beobachter $n\ge |s|$. Für $s\ne0$ wird die Untergrenze erreicht. Bei $P=0$ gilt die Gleichheit bereits. Sonst wähle einen gewöhnlichen Boost entlang $E\times B$ mit Geschwindigkeit $v=2P/(n+|s|)$ in Einheiten $c=1$. Für diese Richtung ergibt das Boostgesetz

$$
n(v)=\frac{(1+v^2)n-4vP}{1-v^2},
\qquad
P_{\parallel}(v)=\frac{(1+v^2)P-vn}{1-v^2}.
$$

Einsetzen liefert $P_{\parallel}(v)=0$ und $n(v)=|s|$. Beide transformierten Felder bleiben transversal, sodass auch der volle Energiefluss verschwindet. Der Boost definiert einen Referenzbeobachter ausgehend vom deklarierten Labor. Weitere Boosts entlang der dann parallelen Felder können ebenfalls die Untergrenze erreichen.

Für $(E,B)=(2e_x,e_y)$ ist $v=1/2$. In diesem Profil gilt $B'=0$, $|E'|^2=3$ und $r'=1$. Für ein nichtverschwindendes nullartiges Feld dagegen gilt $2P=n>0$. Der formale Minimierer hätte $v=1$. Entlang des Flusses ist $n(v)=n(1-v)/(1+v)$ und nähert sich null, ohne sie bei einem endlichen Boost zu erreichen. Damit ist $\inf n=|s|$ in beiden Fällen, aber nur für $s\ne0$ oder das Nullfeld wird das Infimum erreicht.

Diese Wahl liefert die invariante absolute Skala $|s|$ im nichtnullartigen Sektor. Sie macht den normierten Quotienten im Referenzprofil konstant eins und liefert daher keine feinere invariante Rangfolge der Nullnähe. Die vier Normen liefern bei unbekanntem Gain die absolute Skala weiterhin nur bis auf diesen Gain. Zur Konstruktion der Boostachse braucht man zudem die Richtung von $E\times B$, nicht nur die normierten Registerwerte.

## Referenzboost aus kalibrierungsfreien Daten

Für ein nichtverschwindendes Feld im deklarierten Laborprofil ist $r=|s|/n$. Bei $r>0$ ergibt $n^2-|s|^2=4|E\times B|^2$ für den flussparallelen Referenzboost

$$
\frac{v_{\rm ref}}{c}=\sqrt{\frac{1-r}{1+r}},
\qquad
\eta_{\rm ref}=\tfrac12\operatorname{arcosh}(1/r).
$$

Die Viernorm-Auslesung bestimmt damit den Betrag der benötigten Geschwindigkeit ohne absoluten Gain. Bei $r=1$ ist die Geschwindigkeit null. Für $0<r<1$ wird zur räumlichen Abbildung zusätzlich der Einheitsvektor in Richtung $E\times B$ benötigt. Die Felder $(2e_x,e_y)$ und $(2e_x,-e_y)$ haben dieselben vier Normen $(5,5,16,4)$, aber entgegengesetzte Flussrichtungen. Beide erfordern den Geschwindigkeitsbetrag $c/2$. Die Boostvektoren sind entgegengesetzt.

Ist aus Messfehlern nur $0\le r\le R<1$ bekannt, gilt für jeden vereinbaren nichtnullartigen Eingang $v_{\rm ref}/c\ge\sqrt{(1-R)/(1+R)}$. Enthält die zulässige Menge auch nullartige Eingänge, garantieren die Daten keinen endlichen Referenzboost. Für die Beispielschranke $R=\sqrt5/96$ liegt die Untergrenze bei etwa $0{,}977c$. Das ist eine bedingte Aussage über vereinbare nichtnullartige Felder, keine Rekonstruktion der Richtung und kein Nachweis der Existenz des Referenzprofils für das tatsächlich gemessene Feld.

## Flussrichtung aus paarweisen Boost-Auslesungen

In Einheiten $c=1$ sei $\mathbf P=E\times B$ und $a$ eine bekannte Labor-Einheitsachse. Zwei gewöhnliche Beobachterboosts mit Geschwindigkeiten $\pm v a$, $0<v<1$, liefern die Feldskalen $n(\pm va)$. Die parallelen Feldkomponenten bleiben gleich. Die quadrierten transversalen Komponenten liefern im Unterschied

$$
n(-va)-n(+va)=8\gamma^2v\,a\cdot\mathbf P.
$$

Der gerade Anteil, einschließlich der achsenabhängigen parallelen Feldenergie, fällt heraus. Damit gewinnen drei solcher Paare entlang orthonormaler Laborachsen die gerichtete Flussinformation. Wird für alle Boost-Auslesungen derselbe positive Gain $g$ verwendet, ergibt der Vektor der drei normierten Differenzen $g\mathbf P$. Gemeinsame additive Offsets fallen paarweise heraus. Das gilt auch bei einem eigenen, aber innerhalb jedes Paars gleichen Offset. Ein gemeinsamer Gain über die drei Achsen genügt zur Richtung. Bei verschiedenen unbekannten Achsengewinnen sind die Komponentenvorzeichen zugänglich, die Raumrichtung ist im Allgemeinen mehrdeutig.

Im Beispiel $E=2e_x$, $B=\pm e_y$ und $v=1/4$ sind die Differenzen entlang $x$ und $y$ null. Entlang $z$ liefern sie $\pm64/15$. Zusammen mit der kalibrierungsfreien Normauslesung $r=3/5$ ergibt sich daraus der Referenzboost $\pm e_z/2$. Die Vergleichsboosts sind bekannte Eingaben. Die Methode benötigt daher Zugriff auf die Feldskalen in den drei Paaren von Beobachterprofilen. Die vier ursprünglichen Labornormen allein reichen weiterhin nicht für die Richtung.

## Zwei Boostachsen lassen eine Spiegelmehrdeutigkeit

Selbst bei bekanntem Flussbetrag liefern zwei unabhängige Boostachsen nur die Projektion von $\mathbf P$ in ihre Ebene. Ist $a_\perp$ ein Einheitsnormalenvektor dieser Ebene und $\mathbf P_\parallel$ die bestimmte Projektion, bleiben die Möglichkeiten

$$
\mathbf P=\mathbf P_\parallel\pm
 \sqrt{|\mathbf P|^2-|\mathbf P_\parallel|^2}\,a_\perp.
$$

Sie fallen zusammen, wenn der Fluss in der Messebene liegt. Bei der Messebene $xy$ realisieren die Felder $(2e_x,\pm e_y)$ die beiden Möglichkeiten mit identischen Labornormen und identischen Boostdifferenzen entlang $x$ und $y$. Der benötigte Referenzboost ist dennoch $\pm e_z/2$. Allgemein realisiert eine gemeinsame räumliche Drehung dieses Paars das Gegenbeispiel für jede vorab gewählte Messebene. Somit können zwei feste Boostachsen die Richtung auf dem gesamten Feldträger nicht bestimmen, selbst bei bekannter Flussstärke und idealer Kalibrierung.

Bei bekanntem Betrag und kalibrierten Ebenenkomponenten genügt für den dritten Schritt das Vorzeichen der Differenz entlang der Normalen. Alternativ kann eine separat begründete Information über die Flusshalbkugel dieses Vorzeichen liefern. Liegt der Fluss in der Messebene, entfällt dieser dritte Schritt. Drei unabhängige Boostachsen liefern eine Auslesung ohne diese Fallunterscheidung. Die Aussage zur nötigen Zahl gilt für diese Familie paarweiser linearer Flussauslesungen.

## Kontrolle im rekonstruierten Referenzprofil

Nach Anwendung des aus Laborwerten rekonstruierten Boosts ist die Vorhersage im Zielprofil $\mathbf P'=E'\times B'=0$. Ein neuer Satz von drei entgegengesetzten Kontrollboosts entlang unabhängiger räumlicher Zielachsen $a_j$ liefert dort $\Delta_j=n'(-u a_j)-n'(+u a_j)=8\gamma_u^2u\,a_j\cdot\mathbf P'$, mit bekanntem $0<u<1$. Alle drei Differenzen verschwinden genau dann, wenn der Zielbeobachter keinen Energiefluss misst. Ein gemeinsamer Offset innerhalb jedes Kontrollpaars kürzt sich heraus. Für den exakten Nullabgleich darf der positive Gain zwischen den Achsen variieren, weil jede Differenz separat auf null geprüft wird. Die Kontrollwerte können als neue Auslesungen erhoben werden. Eine Berechnung aus denselben Labordaten prüft dagegen nur die algebraische Konsistenz.

Für $E=2e_x$, $B=e_y$ führt der ermittelte Boost $v=1/2$ zu $B'=0$ und $n'=3$. Bei Kontrollgeschwindigkeit $u=1/4$ ist entlang der elektrischen Achse $n'(\pm u e_x)=3$. Entlang $y$ und $z$ gilt $n'(\pm u e_j)=17/5$. Somit verschwinden alle Differenzen, obwohl die absoluten Kontrollskalen achsenabhängig sind. Beim Vergleichsfall mit falschem Boostvorzeichen $v=-1/2$ ist $P'_z=20/3$. Das Kontrollpaar entlang $z$ liefert dann $\Delta_z=128/9$. Damit prüft die Kontrollauslesung insbesondere das Vorzeichen des rekonstruierten Boosts.

Hat jeder gemessene Unterschied höchstens Fehler $d_j$ und ist der jeweilige Gain $g_j$ nach unten positiv beschränkt, dann folgt $|a_j\cdot\mathbf P'|\le (|\widehat\Delta_j|+d_j)/(8g_j\gamma_u^2u)$, wobei für $g_j$ seine untere Schranke eingesetzt werden darf. Dies ist eine Aussage über den Restfluss im Zielprofil. Die QAM-Kette führt Laborrekonstruktion, ausgeführten Beobachterwechsel und Kontrollauslesung als getrennte Schritte.

## Restfluss als Maß für den Korrekturboost

Im tatsächlich erreichten Profil sei $s\ne0$. Aus $n'^2-|s|^2=4|\mathbf P'|^2$ folgt für den flussparallelen Korrekturboost

$$
\eta_{\rm korr}
 =\frac12\operatorname{arsinh}\!\left(\frac{2|\mathbf P'|}{|s|}\right),
\qquad
\frac{v_{\rm korr}}{c}=\tanh\eta_{\rm korr}.
$$

Seine Richtung ist die des Restflusses. Diese Rapidität ist die kleinste unter den Boosts vom erreichten Profil in ein Profil ohne Fluss. Um das zu sehen, starte in einem flussfreien Profil. Dort sind $E$ und $B$ parallel. Ein Boost mit Betrag $\beta$ und Winkel $\theta$ zur gemeinsamen Feldachse liefert $n'=|s|(1+2\gamma^2\beta^2\sin^2\theta)\le |s|\cosh(2\eta)$ mit $\eta=\operatorname{artanh}\beta$. Jeder Boost in ein flussfreies Profil muss die daraus folgende untere Rapiditätsschranke erfüllen. Der flussparallele Boost erreicht sie.

Für den früheren falschen Boost $v=-c/2$ bei $(E,B)=(2e_x,e_y)$ ist $|\mathbf P'|=20/3$ und $|s|=3$. Der Korrekturboost hat Geschwindigkeit $4c/5$ entlang $+z$. Mit der relativistischen Geschwindigkeitsaddition ergibt das wieder den richtigen Laborboost $+c/2$.

Sind nur $|\mathbf P'|\le P_{\max}$ und $|s|\ge s_{\min}>0$ bekannt, folgt $\eta_{\rm korr}\le \tfrac12\operatorname{arsinh}(2P_{\max}/s_{\min})$. Die beiden Größen müssen im selben Skalensystem vorliegen. Ohne positive Untergrenze für $|s|$ garantiert eine absolute Restflussschranke allein keine obere Schranke für die Korrekturrapidität. Liegt die Feldskala aus demselben Zielprofil vor, kann die relative Auslesung alternativ direkt die Korrekturgeschwindigkeit liefern.

## Was die Flusskontrolle am Zielprofil festlegt

Der Nulltest $\mathbf P'=0$ überprüft die Zugehörigkeit zur Familie flussfreier Beobachter. Er identifiziert im Allgemeinen keinen einzelnen Beobachter. In einem flussfreien Profil sind $E'$ und $B'$ parallel, wobei auch eines der Felder null sein kann. Sei $a$ die gemeinsame Feldachse, die bei einem nichtverschwindenden Eingang durch mindestens eines der Felder bestimmt ist. Für einen weiteren Boost mit Geschwindigkeit $\beta$ im Winkel $\theta$ zu $a$ gilt

$$
n''=|s|\bigl(1+2\gamma^2\beta^2\sin^2\theta\bigr).
$$

Für $s\ne0$ ist $n''=|s|$ genau dann, wenn der weitere Boost null oder parallel zur Feldachse ist. Wegen $n''^2-|s|^2=4|\mathbf P''|^2$ charakterisiert das alle flussfreien Beobachter relativ zu einem bereits flussfreien Profil. Räumliche Koordinatendrehungen ändern den Beobachter dabei nicht.

Beim Beispiel $(2e_x,e_y)$ erreicht der Laborboost $+e_z/2$ das Profil $E'=\sqrt3 e_x$, $B'=0$. Ein weiterer Boost mit Geschwindigkeit $1/4$ entlang $e_x$ lässt diese Felder und sämtliche Nullentscheidungen der Kontrollpaare unverändert, ändert aber die Beobachtergeschwindigkeit. Ein weiterer Boost mit demselben Betrag entlang $e_y$ ergibt dagegen $n''=17/5$ und $|\mathbf P''|=4/5$. Die Kontrollauslesung erkennt die zweite Abweichung, während sie die erste als flussfreies Profil akzeptiert.

In QAM sind daher zwei Aussagen getrennt zu führen. Die Feldkontrolle zertifiziert die Eigenschaft „flussfrei“. Die Auswahl des konkreten Zielbeobachters verlangt eine deklarierte Abbildung, etwa den flussparallelen Boost minimaler Rapidität relativ zum Labor. Soll ein Experiment genau diese Wahl verifizieren, braucht es zusätzlich eine Beobachterauslesung, beispielsweise die relative Geschwindigkeit zum Labor.

## Beobachterabgleich innerhalb der flussfreien Familie

Sei $s\ne0$ und der minimale Referenzbeobachter per Boost entlang des Laborflusses festgelegt. Im Referenzprofil steht die gemeinsame Feldachse senkrecht zur Richtung dieses Boosts. Bei bereits flussfreiem Labor gilt die folgende Rechnung mit $\gamma_{\rm ref}=1$. Jeder weitere flussfreie Beobachter entsteht durch einen Boost mit vorzeichenbehafteter Rapidität $\xi$ entlang der Feldachse. Die Lorentzfaktoren relativ zum Labor erfüllen

$$
\gamma_{\rm Ziel}=\gamma_{\rm ref}\cosh\xi,\qquad
\gamma_{\rm ref}=\sqrt{\frac{1+r}{2r}}.
$$

Der erste Ausdruck folgt durch Zusammensetzen senkrechter Boosts auf der Vierergeschwindigkeit. Damit identifiziert eine einzige zusätzliche skalare Uhr- oder Geschwindigkeitsmessung den minimalen Beobachter innerhalb der flussfreien Familie genau dann, wenn sie $\gamma_{\rm Ziel}=\gamma_{\rm ref}$ ergibt. Bei größerem $\gamma_{\rm Ziel}$ bestimmt sie $|\xi|=\operatorname{arcosh}(\gamma_{\rm Ziel}/\gamma_{\rm ref})$. Zur Unterscheidung der beiden Richtungen entlang der Feldachse braucht man zusätzlich das Vorzeichen der entsprechenden Geschwindigkeitskomponente. Der Uhrvergleich bestimmt die Beobachtergeschwindigkeit und legt keine räumlichen Koordinatenachsen fest.

Im Beispiel hat der minimale Laborboost $+e_z/2$ den Faktor $2/\sqrt3$. Ein zusätzlicher Boost mit $v=\pm1/4$ entlang der Feldachse $e_x$ ergibt in beiden Fällen $\gamma_{\rm Ziel}=8/\sqrt{45}>2/\sqrt3$. Die Flusskontrolle akzeptiert alle drei Beobachter, der Uhrvergleich unterscheidet den minimalen von den beiden anderen. Für Messintervalle mit $\gamma_{\rm Ziel}\le G$ und $\gamma_{\rm ref}\ge L>0$ folgt unter der Annahme eines flussfreien Zielprofils $|\xi|\le\operatorname{arcosh}(G/L)$, sofern $G/L\ge1$. Bei $G/L<1$ sind die Intervalle mit diesem Modell unvereinbar.

## Vergleich mit dem Faktor aus r27

In der Feldlesart ist die normierte Bloch-Länge $r=|s|/n$. r27.1(b) verwendet nach seiner nichtselektiven Messung den Registerfaktor $\gamma_{\rm L}=1/r$. Werten wir diese Formel und die Referenzboostformel auf **denselben** nichtnullartigen Felddaten aus, gilt

$$
\gamma_{\rm L}=\frac1r
 =\cosh(2\eta_{\rm ref})
 =2\gamma_{\rm ref}^2-1,\qquad
\gamma_{\rm ref}=\sqrt{\frac{1+r}{2r}}.
$$

Für den r27-Registerwert $r=1/2$ sind die Faktoren $2$ und $\sqrt{3/2}$. Der minimale Laborboost hat dabei $v_{\rm ref}/c=1/\sqrt3$. Würde man $2$ als gewöhnlichen Lorentzfaktor lesen, entspräche er der doppelten Rapidität und einem Geschwindigkeitsbetrag $\sqrt3/2$. Die Faktoren stimmen nur bei $r=1$ überein.

Der Vergleich setzt voraus, dass $r$ in beiden Formeln dieselbe Feldlesart und dasselbe Ausgangsprofil bezeichnet. Die r27-Messung verändert das Register. Die Referenzabbildung setzt am jeweils vorliegenden Feld an und erhält $s$ unter dem Boost. Die Identität liefert daher eine algebraische Zuordnung der Parameter und keine physikalische Identifikation des r27-Schritts mit einem gewöhnlichen Beobachterwechsel oder einem M/T/P-Wechsel.

## Die doppelte Rapidität verbindet zwei Beobachter mit entgegengesetztem Fluss

Für ein nichtnullartiges Feld mit nichtverschwindendem Laborfluss orientiere die Achse entlang $\mathbf P=E\times B$. Schreibe $\eta_0=\eta_{\rm ref}$. Die Boostformeln liefern für einen Beobachter bei Rapidität $\eta$ relativ zum Labor

$$
n(\eta)=|s|\cosh\bigl(2(\eta_0-\eta)\bigr),\qquad
P_\parallel(\eta)=\tfrac{|s|}{2}\sinh\bigl(2(\eta_0-\eta)\bigr).
$$

Daher haben Labor und Beobachter bei $2\eta_0$ dieselbe Feldskala und entgegengesetzte Flüsse in den gemeinsam ausgerichteten Boostachsen. Das flussfreie Profil liegt bei $\eta_0$ in der Mitte der beiden Rapiditäten. Der Faktor $1/r=\cosh(2\eta_0)$ ist folglich der gewöhnliche Lorentzfaktor zwischen diesen beiden Profilen, wenn der zweite Beobachter durch diese kollineare Konstruktion definiert wird. Bei verschwindendem Laborfluss fallen die Profile zusammen. Für nichtverschwindende nullartige Felder existiert diese endliche Konstruktion nicht.

Im Beispiel $E=2e_x$, $B=e_y$ ist der Boost zum flussfreien Profil $v=1/2$. Der Boost mit doppelter Rapidität hat $v=4/5$ und liefert $E'=2e_x$, $B'=-e_y$. Beide Profile haben $n=5$, $s=3$ und dieselben vier HC-Normen. Die gerichtete Flussauslesung trennt sie. Die Übereinstimmung des Faktors mit r27 ergibt sich für dasselbe Eingangsregister. Die r27-Messung wird dadurch nicht zur Abbildung zwischen diesen Beobachtern.

## Auslesung der Spur aus getrennten Messreihen

Auf zwei gleich präparierten Eingaben definiere die Portausgänge als $\pm1$, mit Mittelwerten $q_\pm=2p_\pm-1=cx\pm tz$. Für $ct\ne0$ gilt

$$
\operatorname{tr}Q
=\frac{(q_++q_-)^2}{4c^2}+\frac{(q_+-q_-)^2}{4t^2}.
$$

Die Kompensatormessung lässt diese Portstatistiken bestehen, obwohl sie den Zustand jeder einzelnen Kopie ändert. Somit lässt sich die Quellspur aus zwei getrennten Reihen bestimmen. Aus dem zusammengeworfenen Portmittel allein bleibt bei $c\ne0$ nur $x$ bestimmbar. Bei r27s $\alpha=\pi/6$ sind die Koeffizienten in der Formel $1$ und $1/3$.

Ein balancierter Vergleichswinkel ist $\alpha=\pi/8$ mit $c=t=1/\sqrt2$. Dann gilt $\operatorname{tr}Q=q_+^2+q_-^2$. Für einen unverzerrten Schätzer kann man je Richtung Paare unabhängiger Portausgänge auf gleich präparierten Kopien verwenden. Das Produkt zweier Ausgänge derselben Richtung hat Erwartung $q_\pm^2$. Die Summe der gemittelten Produkte schätzt damit die Spur. Das Quadrieren eines endlichen empirischen Mittelwerts enthält dagegen zusätzlich dessen Varianz.

Im Beispiel $v=(1,0)$ und $\alpha=\pi/6$ liefern beide Reihen $p_\pm=3/4$ und die Formel rekonstruiert die Quellspur $1$. Die Spur des einzelnen Zustands nach der Kompensatormessung beträgt $1/4$. Das sind zwei verschiedene Zielgrößen im selben Modell. In QAM trägt die erste Auslesung den Präparationsbezug und beide Richtungskontexte, die zweite den Zustand nach der Messung.

## Lineare Invariante und Rekonstruktion aus zwei Portwerten

Eine affine Auslesung auf der normierten Scheibe hat die Form $L(x,z)=a x+b z+k$. Erhaltung durch $U_{+\alpha}$ auf der ganzen Scheibe verlangt, dass $(a,b)$ ein linker Fixvektor der Drehmatrix ist. Die Determinante der Drehmatrix minus Identität ist $2(1-c)$. Für jede nichttriviale Drehung ist sie positiv, also $a=b=0$. Auf den unnormierten reellen symmetrischen Matrizen bleibt damit als lineare Invariante nur ein Vielfaches der Spur. Die Bloch-Länge klassifiziert die Bahnen der gesamten kontinuierlichen Rotationsfamilie auf der Scheibe, ist aber nicht affin. Die Aussage betrifft das bestehende Register mit seiner üblichen linearen Struktur. Ein anderes Register kann andere lineare Invarianten tragen.

Für zwei getrennte Portwahrscheinlichkeiten gilt exakt

$$
x=\frac{p_++p_--1}{c},\qquad z=\frac{p_+-p_-}{t}.
$$

Für $ct\ne0$ bestimmen sie den gesamten normierten r27-Zustand. Bei $\alpha=\pi/6$ sind dies $x=2(p_++p_--1)$ und $z=2(p_+-p_-)/\sqrt3$. Bei $c=0$ fehlt $x$, bei $t=0$ fehlt $z$. Die zwei Werte werden für gleich präparierte Eingaben in zwei getrennten Versuchsreihen bestimmt. Sie sind keine Wiederherstellung einer einzelnen bereits gemessenen Kopie. Jede nichtselektive Kompensatormessung lässt ihre jeweilige Portwahrscheinlichkeit unverändert. Beide Messrichtungen zusammen erhalten daher in diesem Sinn genug Daten für die Rekonstruktion.

Für die QAM-Buchführung ist das ein konkretes Paar verschiedener Ausleseverträge. Das Portmittel trägt bei $c\ne0$ die Komponente $x$. Das geordnete Paar trägt bei $ct\ne0$ die gesamte normierte Scheibe. Die Rotationen erhalten eine nichtlineare Bahninvariante, während die lineare Invariante im vorhandenen Register nur die Normierung erfasst. Damit liefert r27 eine lokale Rekonstruktionsroute mit expliziten Abbildungen und zugleich eine Grenze für eine nichttriviale direkte Instanz des Quelle–Rückweg-Satzes auf diesem Register.
