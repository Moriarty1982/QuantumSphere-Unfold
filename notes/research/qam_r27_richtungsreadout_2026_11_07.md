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

## Wirkung der doppelten Rapidität auf das volle Feld

Analytische Fortsetzung nach dem Merge. Betrachte ein nichtnullartiges Feld mit nichtverschwindendem Laborfluss. Im flussfreien Zwischenprofil seien $E_0=e\,a$ und $B_0=b\,a$, mit gemeinsamer Einheitsachse $a$. Die Boostachse $k$ steht senkrecht zu $a$. Die beiden äußeren Beobachter liegen bei entgegengesetzten Rapiditäten relativ zu diesem Zwischenprofil. Ihre Felder lauten in parallel ausgerichteten kartesischen Achsen

$$
E_\pm=\gamma_0(e\,a\pm\beta_0 b\,k\times a),
\qquad B_\pm=\gamma_0(b\,a\mp\beta_0 e\,k\times a).
$$

Eine räumliche Drehung um $\pi$ um $a$ fixiert die $a$-Anteile und kehrt die $k\times a$-Anteile um. Sie bildet somit das gesamte Feldpaar $(E_+,B_+)$ auf $(E_-,B_-)$ ab. Insbesondere stimmen alle vier HC-Normen überein. Der Energiefluss dreht sich mit und wechselt sein Vorzeichen entlang der festgehaltenen Boostachse. Die Feldwirkung dieser Drehung und des doppelten Beobachterboosts fällt für diesen Eingang zusammen. Die Operationen bleiben als Abbildungen verschieden, insbesondere bezüglich der Beobachteruhr.

Beim früheren Paar $(2e_x,\pm e_y)$ ist $a=e_x$. Für allgemein nichtorthogonale Laborfelder bleibt die Aussage mit der im Zwischenprofil bestimmten Achse gültig. Die normierten Gram-Daten bestimmen diese räumliche Achse nicht. Der Vergleich benötigt die deklarierte Ausrichtung der Achsen.

## Abgleich mit F1 und F2 aus r08

[r08](v4_10_0_r08/Annahmenliste_Companion.md) trennt die Zählregel Z1, die Zuordnung des Zählverhältnisses zum Frame-Versatz (F1) und die Halb-Rapiditätsformel (F2). Setze $G=\gamma_{\rm BI}/\gamma_{\rm string}$ und nenne den gewöhnlichen Lorentzfaktor zwischen den äußeren HC-Beobachtern $\gamma_{\rm außen}=n/|s|$. Unter der zusätzlichen Identifikation $G=\gamma_{\rm außen}$ ergibt F2 genau den Betrag des Boosts zum flussfreien Mittelpunkt:

$$
\beta_{\rm sym}^2=\frac{G-1}{G+1}
=\frac{n-|s|}{n+|s|}
=\frac{v_{\rm ref}^2}{c^2}.
$$

Die Feldkonstruktion realisiert damit die Geometrie von F2. Sie lässt $G$ frei. Für jedes $G\ge1$ erhält man etwa mit $E=e_x$ und $B=\sqrt{(G-1)/(G+1)}\,e_y$ die Identität $n/|s|=G$. Multiplikation beider Vektoren mit einer gemeinsamen positiven Skala und ihre gemeinsame räumliche Drehung lassen dieses Verhältnis bestehen. Aus dem Zählverhältnis folgt daher im Feldmodell weder ein bevorzugter Feldzustand noch eine Boostachse. Umgekehrt liefert die Feldrechnung keine Auswahl der Zählregel.

Die beiden äußeren Beobachter gehören zur selben realen Lorentzbahn des Feldes und haben dasselbe komplexe $s$. F1 benennt dagegen eine T–M-Zuordnung. Eine Anwendung braucht eine Abbildung der beiden QSC-Profile auf die beiden realen HC-Beobachter und einen Nachweis, dass deren Registerwert gerade $|s|/n=1/G$ ist. Eine aktive Dualität kann das Vorzeichen von reellem $s$ wechseln. Ein solcher Schritt wäre ausdrücklich getrennt zu führen. Die [r09-Erkundung zu Prinzip P](v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md) beschreibt für ihren T-Boden eine komplexe Rapidität und lässt die Brücke zur Horizontenergie offen. Die reale HC-Konstruktion liefert diese Brücke nicht. Einordnung T6/T14, analytische Erkundung ohne neue H-Nummer.

## Kandidat mit getrenntem Beobachter- und Sektorschritt

Auf dem reellen Feldträger definiere $D(E,B)=(-B,E)$, also $E+iB\mapsto i(E+iB)$. Direkt gilt $s(D F)=-s(F)$, $n(D F)=n(F)$ und $\mathbf P(D F)=\mathbf P(F)$. Die Dualität kommutiert mit dem gewöhnlichen Lorentzboost der Feldlesart. Für den am Eingabefeld konstruierten äußeren Boost $L_F$ folgt damit

$$
(s,n,\mathbf P)(D L_F F)=(-s,n,-\mathbf P).
$$

Die Dualität ändert weder die Beobachtergeschwindigkeit noch die Uhr. Der Lorentzfaktor zwischen den Beobachtern stammt allein aus $L_F$ und beträgt $n/|s|$. Für $(E,B)=(2e_x,e_y)$ ergibt der Boost mit $4c/5$ zunächst $(2e_x,-e_y)$. Die anschließende Dualität liefert $(e_y,2e_x)$ mit $s=-3$, $n=5$ und $\mathbf P=-2e_z$.

Das Vorzeichen von $s$ und die Flussrichtung prüfen somit verschiedene Teile dieser Konstruktion. Bei reellem $s\ne0$ wechselt sie die algebraische Sektormarkierung. Die beiden Feldausgaben können in QAM mit einer Beobachtermap und einer separaten aktiven Feldmap verbunden werden. Für F1 fehlt weiterhin der Nachweis, dass die QSC-Profile genau diese Zuordnung und den Zählwert $n/|s|=\gamma_{\rm BI}/\gamma_{\rm string}$ realisieren. Insbesondere ist die aktive Dualität hier eine gewählte Feldoperation. Der Vergleich mit der komplexen r09-Rapidität verlangt eine eigene Abbildung, bevor man beide Konstruktionen gleichsetzt.

## Vergleich des zusammengesetzten Übergangs mit der HC-Involution

Die im Companion verwendete Involution $J_Bw=i\bar w$ vertauscht die reellen Felder: $J_B(E,B)=(B,E)$. Ihre Wirkung auf die Auslesungen ist $(s,n,\mathbf P)\mapsto(-\bar s,n,-\mathbf P)$. Der zusammengesetzte Übergang $D L_F$ liefert dagegen $(-s,n,-\mathbf P)$. Für nichtreelles $s$ sind bereits die komplexen Feldinvarianten verschieden.

Für reelles $s\ne0$ gilt $E\cdot B=0$. Bei nichtverschwindendem Fluss ist der äußere Boost entlang $k=(E\times B)/|E\times B|$ durch $\beta=2|E||B|/n$ gegeben. Wegen $k\times B=-|B|E/|E|$ und $k\times E=|E|B/|B|$ ergibt das Boostgesetz

$$
L_F(E,B)=(\operatorname{sgn}(s)E,-\operatorname{sgn}(s)B),
\qquad D L_F(E,B)=\operatorname{sgn}(s)\,J_B(E,B).
$$

Bei verschwindendem Fluss und reellem $s\ne0$ ist eines der Felder null. Mit $L_F=\mathrm{id}$ gilt dieselbe Formel. Auf dem elektrisch dominierten Teil stimmt der zusammengesetzte Übergang auf den Feldvektoren exakt mit $J_B$ überein. Auf dem magnetisch dominierten Teil entsteht das negative Feld. Das Vorzeichen unterscheidet die vollständigen Felder. Die quadratischen Auslesungen aus Normen und Fluss sind gegenüber diesem Gesamtvorzeichen unempfindlich.

Wendet man dieselbe Vorschrift $D L_F$ auf die jeweilige neue Eingabe erneut an, kehrt der Fluss beim ersten Schritt um und das Sektorvorzeichen wechselt. Auf dem reellen nichtnullartigen Bereich ergibt die zweimalige Anwendung daher $-F$, während $J_B^2F=F$ gilt. Auf den quadratischen Auslesungen wirkt die zweimalige Anwendung als Identität. Das liefert einen konkreten Rückwegtest dafür, ob QAM vollständige Felder oder nur diese Auslesungen gleichsetzt. Selbst bei übereinstimmendem Feldwert enthält der zusammengesetzte Übergang eine eigene Beobachterabbildung.

## Gerichteter Rückweg mit inverser Dualität

Für reelles $s\ne0$ setze $\epsilon=\operatorname{sgn}(s)$ und wähle die aktive Vierteldrehung abhängig vom Eingangssektor. Die Abbildung sei $K(F)=D^\epsilon L_FF$. Da $D^{-1}=-D$ auf dem Feldträger, folgt aus dem vorigen Abschnitt $K(F)=J_BF$ für beide Sektoren. Auf dem Rückweg ist $\epsilon$ gewechselt. Die aktive Vierteldrehung läuft deshalb in inverser Richtung. Zugleich hat sich der Fluss umgekehrt, sodass der am neuen Feld rekonstruierte äußere Boost in den kollinear ausgerichteten Achsen den ersten Boost invertiert. Auf dem vollständigen Feld und auf dem Beobachter ergibt sich damit ein geschlossener Rückweg.

Im Zahlenbeispiel ist der Hinweg $(2e_x,e_y)\mapsto(2e_x,-e_y)\mapsto(e_y,2e_x)$. Der Rückboost liefert $(-e_y,2e_x)$. Darauf ergibt $D^{-1}(E,B)=(B,-E)$ wieder $(2e_x,e_y)$. Mit erneutem $D$ würde stattdessen $(-2e_x,-e_y)$ entstehen. Die lineare Labor-Auslesung $E\cdot e_x$ unterscheidet die Rückwegwerte $2$ und $-2$, während die quadratischen Normen und der Fluss in beiden Fällen gleich sind.

Für QAM benötigt diese Konstruktion die Vorzeichenentscheidung des reellen $s$ im Eingangsprofil oder eine explizite Richtungsmarke mit der zugehörigen inversen Map. Die Regel ist auf den reellen nichtnullartigen Sektor beschränkt. Sie realisiert dort die lokale HC-Involution als zusammengesetzten Übergang. Die Zuordnung zu nativen M/T-Profilen und zum Zählverhältnis bleibt eine separate Beweispflicht.

## Gerichteter HC-Rückweg für komplexes s

Für jedes nichtnullartige Feld $w=E+iB$ setze $\zeta(s)=i\bar s/|s|$ und definiere die aktive Dualität durch Multiplikation mit $\zeta(s)$. Sei $B_\eta$ der Boost vom Labor zum flussfreien Zwischenprofil entlang der festgehaltenen Laborflussachse, sodass der äußere Boost $L_F=B_{2\eta}$ ist. Dort gilt $w_0=B_\eta w=q a$ mit reeller Einheitsachse $a$, komplexem $q$ und $q^2=s$. Deshalb ist $J_Bw_0=i\bar q a=\zeta(s)w_0$.

Für dieselbe feste Boostachse gilt $J_B B_\eta=B_{-\eta}J_B$. Dies folgt aus dem Boostgesetz, weil komplexe Konjugation den imaginären transversalen Mischungsterm umkehrt. Die aktive Dualität kommutiert mit dem Boost. Aus $w=B_{-\eta}w_0$ ergibt sich somit

$$
J_Bw=B_\eta J_Bw_0=\zeta(s)B_{2\eta}w.
$$

Bei verschwindendem Fluss gilt die Rechnung mit $\eta=0$. Unter dem ersten Übergang wird $s$ zu $-\bar s$. Die zweite Phase ist dann $\zeta(-\bar s)=\overline{\zeta(s)}$, also die inverse aktive Dualität. Der Fluss kehrt beim ersten Übergang um, und der zweite äußere Boost invertiert den ersten. Auf reellem $s$ ergibt sich wieder die Vierteldrehung mit sektorgebundenem Vorzeichen.

Beispiel: Im Zwischenprofil wähle $E_0=2e_x$, $B_0=e_x$. Dann ist $s=3+4i$ und $\zeta=(4+3i)/5$. Es gilt $\zeta(2+i)=1+2i$, wie für die Vertauschung der beiden Felder erforderlich. Das Beispiel benötigt keine Wahl eines Zweigs für $\arg s$. Die Normauslesungen können die Phase aus dem vollständigen komplexen $s$ bestimmen, während der gerichtete Fluss die Boostachse bestimmt. Die Konstruktion verwendet den reellen elektromagnetischen Feldträger bei $s\ne0$ und liefert keine native M/T-Zulassung.

## Nullartiger Rand der HC-Zerlegung

Für ein nichtverschwindendes nullartiges Feld gilt $n=2|\mathbf P|>0$. Ein endlicher kollinearer Boost in Flussrichtung liefert $n(\eta)=n e^{-2\eta}$ und $P_\parallel(\eta)=n e^{-2\eta}/2>0$. Aktive Dualität erhält den Fluss. Daher kann keine Folge aus einem endlichen kollinearen Beobachterboost und aktiver Dualität auf diesem Träger die Flussumkehr von $J_B$ realisieren. Beim Annähern an ein festes nichtverschwindendes nullartiges Feld divergiert die äußere Rapidität $\operatorname{arcosh}(n/|s|)$.

Auch die Phase hat keinen eindeutigen Grenzwert. Gegen dasselbe Nullfeld $(E,B)=(e_x,e_y)$ konvergieren die Familien $(E,B)=((1+\epsilon)e_x,e_y)$ und $(e_x,e_y+\epsilon e_x)$. Für $\epsilon\to0^+$ liefert die erste $s=2\epsilon+\epsilon^2$ und $\zeta=i$. Die zweite liefert $s=-\epsilon^2+2i\epsilon$ und $\zeta\to1$. Das zusammengesetzte Feldbild besitzt dennoch den eindeutigen Grenzwert $J_BF$, da es auf jedem nichtnullartigen Eingabefeld exakt mit der stetigen reell-linearen Involution übereinstimmt.

Am Nullfeldrand gibt es eine andere explizite Feldrealisierung. Bei $s=0$ und $n>0$ sind $E$ und $B$ orthogonal und gleich lang. Die räumliche Halbdrehung um die Achse $E+B$ vertauscht beide Vektoren und kehrt den Fluss um. Sie realisiert das Feldbild von $J_B$ im selben Beobachterprofil. Beim Nullfeld $F=0$ ist $J_BF=0$. In QAM hat die Involution daher einen größeren Definitionsbereich als ihre Zerlegung in den kollinearen Boost und die aus $s$ bestimmte Phase.

## Wann eine räumliche Drehung allein die HC-Vertauschung realisiert

Eine gemeinsame räumliche Drehung $R\in SO(3)$ mit $(RE,RB)=(B,E)$ existiert genau dann, wenn $|E|=|B|$, also $\operatorname{Re}s=0$. Die Notwendigkeit folgt aus der Normerhaltung. Für $A=E+B\ne0$ folgt aus der Normgleichheit $A\cdot D=0$ mit $D=E-B$. Die Halbdrehung um $A$ fixiert $A$ und sendet $D$ auf $-D$. Daher vertauscht sie $E$ und $B$. Bei $A=0$ und $E\ne0$ wirkt eine Halbdrehung um jede zu $E$ senkrechte Achse als Vertauschung. Beim Nullfeld reicht die Identität.

Das Kriterium umfasst nichtverschwindende nullartige Felder und nichtnullartige Felder mit rein imaginärem $s$. Beispielsweise liefern $E=e_x$ und $B=(3e_x+4e_y)/5$ den Wert $s=6i/5$. Eine Halbdrehung um $E+B$ realisiert auch hier $J_B$ innerhalb des Labors. Zugleich ist der nichtnullartige äußere Beobachterboost mit aktiver Dualität definiert und liefert in ausgerichteten Achsen dieselben Feldkomponenten. Die beiden Realisierungen führen zu verschiedenen Beobachterdaten.

Auf dem Teilbereich $|E|=|B|$, $E+B\ne0$ hängt die Drehmatrix $2AA^{\mathsf T}/|A|^2-I$ stetig von den Feldern ab. Sie gibt insbesondere entlang dieses Teilbereichs eine endliche Realisierung durch den nullartigen Rand. Auf einer vollen Umgebung eines Nullfelds mit Eingaben unterschiedlicher elektrischer und magnetischer Norm kann eine räumliche Drehung allein die Vertauschung nicht realisieren. Die drei HC-Normdaten prüfen die Gleichnormbedingung über $N_E=N_++N_-$, enthalten aber die Richtung von $A$ im Allgemeinen nicht.

## HC-Realisierung im Labor durch Drehung und Dualität

Für $s\ne0$ setze $M=EE^{\mathsf T}+BB^{\mathsf T}$. Seine beiden möglichen nichtverschwindenden Eigenwerte sind $(n+|s|)/2$ und $(n-|s|)/2$, da sie mit denen der Gram-Matrix des Feldpaares übereinstimmen. Der größte Eigenwert ist einfach. Sein Eigenprojektor $P_a$ bestimmt die Hauptachse ohne Vorzeichenwahl. In der Darstellung der beiden äußeren Profile ist diese Achse genau die gemeinsame Feldachse des flussfreien Zwischenprofils. Dort liegen die $a$-Komponenten der Laborfelder bei einem gemeinsamen Faktor $\gamma_0$ und die dazu senkrechten Komponenten bei $\gamma_0|\beta_0|$, sodass $M$ auf diesen Achsen diagonal ist und die $a$-Richtung den größeren Eigenwert trägt.

Die Halbdrehung $R_a=2P_a-I$ hat auf dem Laborfeld dieselbe Feldausgabe wie der äußere Boost. Daher gilt

$$
J_Bw=\zeta(s)R_a w,\qquad \zeta(s)=i\bar s/|s|.
$$

Das ist eine vollständig aktive Realisierung im Laborprofil. Sie benötigt die volle räumliche Hauptachse, aber keine Beobachtergeschwindigkeit. Normdaten liefern die beiden Eigenwerte und die Phase, während der Eigenprojektor aus ihnen allein im Allgemeinen nicht folgt.

Bei $s=0$, $n>0$ fallen die beiden positiven Eigenwerte zusammen. Die Hauptachse ist dann nicht eindeutig und die Phase aus dieser Vorschrift undefiniert. Die oben angegebene Halbdrehung um $E+B$ realisiert dort direkt $J_B$. Über das nichtverschwindende Nullfeld hinweg lässt sich keine stetige Wahl der Dualitätsphase für eine solche Zerlegung auf einer ganzen Umgebung treffen. Jede räumliche Drehung erhält $s$, sodass für die Phase $\lambda$ notwendig $\lambda^2=-\bar s/s$ gilt. Die beiden bereits beschriebenen Annäherungen mit Grenzargumenten $0$ und $\pi/2$ erzwingen verschiedene Grenzwerte für $\lambda^2$. Die gesamte HC-Feldabbildung bleibt stetig.

## Dieselbe HC-Feldausgabe für eine Familie von Beobachtern

Sei $B_\eta$ der Boost vom Labor in das flussfreie Zwischenprofil, mit Richtung $k$ und $E_0=e\,a$, $B_0=b\,a$, $k\perp a$. Ein Boost $C_\xi$ mit Rapidität $\xi$ entlang $a$ fixiert beide Zwischenfelder. Deshalb gilt für die geordnete Folge der Profilwechsel

$$
B_\eta C_\xi B_\eta w=B_{2\eta}w,\qquad
\zeta(s)B_\eta C_\xi B_\eta w=J_Bw.
$$

Hier bezeichnet das linke $B_\eta$ einen Boost entlang der entsprechend mitgeführten $k$-Achse nach dem Zwischenschritt. Die Feldkomponenten werden in den durch diese Folge definierten Achsen verglichen. Die Gleichung für das Feld setzt keine Gleichheit der Lorentzabbildungen auf anderen Objekten voraus.

Für die Zeitkomponente der zusammengesetzten Lorentzmatrix folgt, mit $\gamma_0=\cosh\eta$ und $\beta_0=\tanh\eta$,

$$
\gamma_{\rm Ziel}(\xi)=\gamma_0^2(\cosh\xi+\beta_0^2)
=\cosh(2\eta)+\gamma_0^2(\cosh\xi-1).
$$

Dazu genügt die Wirkung auf den Zeitbasisvektor. Der erste Boost erzeugt Zeit- und $k$-Komponente. Der Zwischenschritt multipliziert die Zeitkomponente mit $\cosh\xi$, fügt eine $a$-Komponente hinzu und lässt die $k$-Komponente stehen. Der letzte Boost mischt Zeit und $k$ erneut.

Für das komplexe Beispiel aus [hc-return.tex](../../qam/examples/hc-return.tex) gilt $\beta_0=3/5$ und $\gamma_0=5/4$. Die gleiche HC-Feldausgabe hat bei $\xi=0$ den Faktor $17/8$ und bei $\cosh\xi=5/4$ den Faktor $161/64$. Der Wert $n/|s|$ ist innerhalb dieser Familie der minimale Uhrfaktor. Ein höherer Faktor bestimmt $|\xi|$, aber nicht die Richtung entlang $a$. Die bereits konstruierte aktive Laborabbildung mit Faktor $1$ verwendet eine andere Operationsfolge. Somit kann die Feldausgabe allein weder die Art der Abbildung noch den Uhrfaktor innerhalb dieser Boostfamilie auswählen.

## Auswahl des direkten äußeren Boosts

In der oben definierten Familie $B_\eta C_\xi B_\eta$ hat der transformierte Zeitbasisvektor, in der Vorzeichenkonvention mit positiven Boostkomponenten, die Komponenten

$$
U^0=\gamma_0^2(\cosh\xi+\beta_0^2),\qquad
U_k=\gamma_0^2\beta_0(\cosh\xi+1),\qquad
U_a=\gamma_0\sinh\xi.
$$

Die Formel folgt durch Multiplikation der drei Boostmatrizen auf dem Zeitbasisvektor. Die Richtung der räumlichen Komponenten setzt die deklarierte Vorzeichenkonvention voraus. Die Bedingung $U_a=0$ wählt exakt $\xi=0$, also den direkten kollinearen Weg. Ein Uhrvergleich allein bestimmt $\cosh\xi$ und lässt das Vorzeichen offen. Die gerichtete Querkomponente bestimmt $\xi$ dagegen direkt als $\operatorname{arsinh}(U_a/\gamma_0)$. Diese Auslesung betrifft die Lorentzabbildung in den deklarierten Achsen und setzt die gewählte Familie voraus.

Für das komplexe Beispiel mit $\gamma_0=5/4$ und $\cosh\xi=5/4$ ist $U_a=\pm15/16$ und $U^0=161/64$. Die beiden Fälle liefern gleiche Feldausgaben und denselben Uhrfaktor, aber entgegengesetzte gerichtete Komponenten. Beim direkten Weg ist $U_a=0$ und $U^0=17/8$.

Für einen Vergleich mit F1 ist die Kollinearität damit eine explizite Auswahlbedingung innerhalb der konstruierten Familie. Ein als Uhrfaktor vorgegebenes $G$ ist in ihr genau dann erreichbar, wenn $G\ge n/|s|$. Gleichheit wählt den direkten Weg, strikte Ungleichheit bestimmt zwei Vorzeichen von $\xi$. Dieser Vergleich gilt bei festem Eingangsfeld. Er liefert weder eine Auswahl des Eingangs aus der Zählregel noch eine Identifikation der Familie mit nativen M/T-Übergängen.

## F1-Zählfaktor als Verträglichkeitsbedingung

Die [Annahmenliste in r08](v4_10_0_r08/Annahmenliste_Companion.md) nennt $G=1{,}8647$ für die gewählte Zählung und etwa $2{,}15$ für ihre SU(2)-Gegenrechnung. Für ein festes Feld und die oben deklarierte Boostfamilie gilt

$$
G\text{ erreichbar}\iff r\ge 1/G,\qquad
\cosh\xi=1+\frac{G-1/r}{(1+r)/(2r)} .
$$

Für die gewählte Zählung ist die Mindestlänge $1/G\approx0{,}5363$. Der Beispielwert $r=1/2$ aus r27 verlangt mindestens $G=2$. Dasselbe gilt noch stärker für das komplexe Feld aus dem HC-Beispiel, dessen $r=8/17$ den Mindestfaktor $17/8$ verlangt. Beim Feld $(2e_x,e_y)$ mit $r=3/5$ ist $G=1{,}8647$ erreichbar. Es erfordert $\cosh\xi\approx1{,}1485$ und erlaubt zwei Bewegungsrichtungen. Der direkte Weg hätte $G=5/3$. Der SU(2)-Vergleichswert $2{,}15$ wäre in allen drei Fällen erreichbar, allerdings jeweils mit einem zusätzlichen Feldachsenboost.

Für ein unabhängiges Messintervall $r\in[r_-,r_+]$ schließt $r_+<1/G$ diese Zuordnung aus. Bei $r_-\ge 1/G$ ist sie für jeden damit vereinbaren Feldwert erreichbar. Die direkte kollineare Zuordnung verlangt genauer $r=1/G$. Das ist ein modellinterner Abgleich mit einem vorgegebenen Zählfaktor und kein Auswahltest für die Zählregeln. Ohne unabhängig festgelegtes Feldprofil kann man stets $r$ passend wählen. Ohne Zulassung der hier benutzten Familie bleibt auch die native F1-Zuordnung offen. Analytische Erkundung, keine neue H-Nummer.

## Wann ein Feldintervall die beiden r08-Faktoren trennt

Für die nominalen r08-Werte $G_1=1{,}8647$ und $G_2=2{,}15$ gilt $G_1<G_2$. Innerhalb der festgelegten äußeren Boostfamilie sind die Bereiche

$$
\begin{array}{c|c}
r<1/G_2 & \text{beide Faktoren ausgeschlossen}\\
1/G_2\le r<1/G_1 & \text{nur }G_2\text{ erreichbar}\\
r\ge1/G_1 & \text{beide Faktoren erreichbar}.
\end{array}
$$

Der umgekehrte Trennfall ist in dieser Familie unmöglich, weil die erreichbaren Uhrfaktoren bei festem $r$ ein oberhalb von $1/r$ beginnendes Intervall bilden. Ein unabhängig bestimmtes Feldintervall trennt die Faktoren für alle damit verträglichen Eingaben genau dann zugunsten von $G_2$, wenn seine Untergrenze mindestens $1/G_2$ und seine Obergrenze kleiner als $1/G_1$ ist. Als gewähltes Rechenbeispiel liegt $[0{,}48,0{,}52]$ vollständig zwischen den nominalen Grenzen $0{,}4651$ und $0{,}5363$.

Für den streng kollinearen Weg ändert sich die Logik. Dort sind die Faktoren nur bei $r=1/G_1$ beziehungsweise $r=1/G_2$ erreichbar. Das gewählte Intervall schließt daher **beide** kollinearen Zuordnungen aus. Die Erreichbarkeit von $G_2$ im breiteren Modell erfordert einen zusätzlichen Feldachsenboost und eine entsprechende Bewegungsauslesung. Die Zahlen sind eine analytische Erkundung und verwenden kein gemessenes Feld. Die native F1-Zulassung und die Auswahl einer Zählregel bleiben gesonderte Fragen.

## Zweite Vorhersage bei vorgegebenem Uhrfaktor

Für das festgelegte Feldregister $r=1/2$ und den nominalen Vergleichsfaktor $G_2=43/20$ gilt in der erweiterten äußeren Boostfamilie $\gamma_0^2=3/2$ und $\cosh\xi=11/10$. Die in den deklarierten Achsen gemessene Geschwindigkeitskomponente entlang der Feldachse ergibt sich aus $U_a/U^0$:

$$
\frac{v_a}{c}=\pm\frac{\gamma_0\sqrt{\cosh^2\xi-1}}{G_2}
=\pm\frac{3\sqrt{14}}{43}\approx\pm0{,}2611.
$$

Der Uhrfaktor lässt beide Vorzeichen zu, sagt aber den Betrag voraus. Eine unabhängige Bewegungsauslesung mit $|v_a|<0{,}26c$ würde in diesem exakten Zahlenmodell auch die erweiterte $G_2$-Zuordnung ausschließen. Für Messdaten mit Fehlern müssen die Intervalle für $r$ und $G$ mitgeführt werden. Allgemein lautet die zusätzliche Bedingung

$$
G^2(v_a/c)^2=2(G-1/r)+\frac{2r}{1+r}(G-1/r)^2,\qquad G\ge 1/r.
$$

Sie folgt aus $U_a^2=\gamma_0^2(\cosh^2\xi-1)$ und ist unabhängig vom Vorzeichen der Achsenbewegung. Die Größen sind in der für die Boostfolge deklarierten Achsenkonvention auszulesen. So lässt sich ein Faktor innerhalb der Familie nicht nur an die Uhr anpassen, sondern auch gegen eine zweite Beobachterauslesung prüfen. Der nominale Zahlenwert ist eine Modellrechnung und keine Beobachtung.

## Bewegungsschranke bei unsicherem Feldwert

Für festes $G$ und erreichbares $r$ schreibe $\Delta=G-1/r\ge0$. Dann ist

$$
\frac{|v_a|}{c}
=\frac1G\sqrt{2\Delta+\frac{2r}{1+r}\Delta^2}.
$$

Sowohl $\Delta$ als auch $2r/(1+r)$ wachsen mit $r$. Die rechte Seite ist auf dem zulässigen Bereich daher monoton. Für ein Feldintervall wird zunächst $r\ge1/G$ geschnitten. Ist die Schnittmenge leer, ist der Uhrfaktor bereits ausgeschlossen. Andernfalls liefern ihre beiden Endpunkte die scharfen Grenzen der vorhergesagten Beträge innerhalb der Boostfamilie.

Für das gewählte Intervall $[0{,}48,0{,}52]$ und den festen nominalen Faktor $G=2{,}15$ ergibt sich $|v_a|/c\in[0{,}17166\ldots,0{,}32527\ldots]$. Eine unabhängige Obergrenze $|v_a|\le0{,}17c$ schließt den Faktor daher für das gesamte Feldintervall in dieser Familie aus. Umgekehrt bestätigt ein Wert innerhalb des Bereichs zunächst nur die Vereinbarkeit mit den Intervallen. Diese Rechnung propagiert ein gegebenes Intervall für $r$ und setzt $G$ exakt auf den nominalen Vergleichswert. Sie verwendet keine erhobenen Messdaten.

## Gemeinsame Unsicherheit von Feldwert und Uhrfaktor

Bei festem $r$ setze $A=(1+r)/(2r)$ und $b=(1-r)/(1+r)$. Aus der Boostformel folgt

$$
(v_a/c)^2=\frac1A-\frac{2b}{G}+\frac{A(b^2-1)}{G^2}.
$$

Der Ausdruck wächst für $G\ge1/r$, da $b\ge0$ und $b^2-1<0$ für $r>0$. Zusammen mit der Monotonie in $r$ ergibt sich eine genaue Intervallregel für unabhängige Intervalle $[r_-,r_+]$ und $[G_-,G_+]$. Ist $G_+r_+<1$, ist kein Paar zulässig. Ist $G_-r_-\ge1$, liegen Minimum und Maximum an den unteren beziehungsweise oberen Ecken. Andernfalls enthält das zulässige Rechteckstück den Rand $Gr=1$, sodass das Minimum null ist. Das Maximum liegt weiterhin an der oberen Ecke.

Für $r\in[0{,}48,0{,}52]$ und das zusätzlich gewählte Uhrintervall $G\in[2{,}14,2{,}16]$ ergibt sich $|v_a|/c\in[0{,}158752\ldots,0{,}331351\ldots]$. Die frühere Obergrenze $0{,}17$ reicht nun nicht zum Ausschluss. Eine unabhängige Obergrenze $0{,}158$ würde ihn in diesem Modell weiterhin liefern. Die Rechnung verwendet frei gewählte Intervallgrenzen. Bei gekoppelten Fehlern ist statt des Rechtecks der gemeinsame zulässige Bereich zu verwenden.

## Feldwert aus Uhr und Bewegung zurückrechnen

Die Beobachtergleichung lässt sich auch ohne Felddaten auswerten. Setze $q=(v_a/c)^2$, $G=U^0$ und $h=1/A=2r/(1+r)$. Mit $b=1-h$ wird die Gleichung des vorigen Abschnitts linear in $h$:

$$
G^2q=h(G+1)^2-2(G+1),\qquad
h=\frac{G^2q+2(G+1)}{(G+1)^2},\qquad
r_{\rm Beobachter}=\frac{h}{2-h}.
$$

Damit kann ein unabhängig aus den vier Normen bestimmtes $r_{\rm Feld}$ gegen $r_{\rm Beobachter}$ geprüft werden. Für exakte Werte mit $G\ge1$ existiert ein normiertes Feldprofil in der betrachteten Familie genau dann, wenn $0\le q\le1-G^{-2}$. Diese Bedingung erzwingt $1/G\le r_{\rm Beobachter}\le1$. Bei $r=1$ ist das Labor bereits flussfrei. Für die Konstruktion eines Feldachsenboosts wird in diesem Fall eine Feldachse im Labor deklariert. Das Vorzeichen von $v_a$ unterscheidet die beiden Richtungen, geht aber nicht in die Rekonstruktion von $r$ ein.

Für $G=43/20$ und $|v_a|/c=3\sqrt{14}/43$ ergibt sich $h=2/3$ und somit $r_{\rm Beobachter}=1/2$. Wird dagegen bei demselben Uhrfaktor $v_a=0$ gemessen, folgt $r_{\rm Beobachter}=20/43\approx0{,}4651$. Das zuvor gewählte unabhängige Feldintervall $[0{,}48,0{,}52]$ wäre damit unvereinbar. Der Vergleich prüft die gewählte Boostfamilie. Andere Transformationsfamilien und die native Zuordnung der QSC-Profile verlangen eigene Annahmen.

## Längskomponente als weiterer Abgleich der Boostfolge

In der deklarierten Konvention für den transformierten Zeitbasisvektor gilt $U_k=\gamma_0^2\beta_0(\cosh\xi+1)$ und $G=\gamma_0^2(\cosh\xi+\beta_0^2)$. Weil $\gamma_0^2(1-\beta_0^2)=1$, folgt

$$
\frac{v_k}{c}=\frac{U_k}{G}
=\beta_0(1+1/G),\qquad
\beta_0=\sqrt{\frac{1-r}{1+r}}.
$$

Die Komponente senkrecht zur von $a$ und $k$ aufgespannten Ebene muss null sein. Für $0<r<1$ ist die Längsrichtung durch die deklarierte Flussachse festgelegt. Die beiden Vorzeichen der Bewegung entlang $a$ haben dieselbe Längskomponente. Eine gerichtete Messung von $v_k$ prüft deshalb zusätzlich, ob die Bewegung in der vorgesehenen Richtung verläuft. Bei $r=1$ ist $\beta_0=0$ und nur die deklarierte Feldachse für den möglichen Zwischenschritt relevant.

Für $r=1/2$ und $G=43/20$ sind die Vorhersagen $v_k/c=21\sqrt3/43$ und $v_a/c=\pm3\sqrt{14}/43$. Ihre Quadratsumme ist $1-G^{-2}$. Eine Beobachterbewegung mit umgekehrter Längskomponente hätte denselben Uhrfaktor und dasselbe $v_a$. Sie würde die Rückrechnung aus den letzten beiden Werten passieren, aber die deklarierte Boostfolge verletzen. Die Längskomponente liefert zudem einen zweiten Rückrechenweg mit $\beta_0=Gv_k/[c(G+1)]$ und $r=(1-\beta_0^2)/(1+\beta_0^2)$, sofern $0\le\beta_0<1$ in der festgelegten Richtung. Diese Prüfung betrifft die Beobachterbewegung. Die Orientierung räumlicher Achsen bleibt als Teil der Profilabbildung separat deklariert.

## Beobachtergeschwindigkeit und räumliche Achsen getrennt prüfen

Zwei eigentliche orthochrone Lorentzabbildungen, die denselben Zeitbasisvektor auf dieselbe Vierergeschwindigkeit abbilden, unterscheiden sich auf der Zielseite durch eine räumliche Drehung im Ruhesystem dieses Beobachters. Halte nun zusätzlich die aktive Dualitätsphase fest und vergleiche die vollständigen gerichteten Feldkomponenten. Wenn beide Abbildungen dieselben Zielfelder $E',B'$ liefern, muss diese relative Drehung beide Vektoren fixieren. Bei $E'\times B'\ne0$ fixiert sie auch das Kreuzprodukt. Diese drei Richtungen spannen den Raum auf. Die Drehung ist dann die Identität.

Damit bestimmen die vollständige Beobachtergeschwindigkeit und die vollständigen Feldkomponenten bei vorgegebener aktiver Dualität die Lorentzabbildung eindeutig, sofern der Zielfluss nicht verschwindet. Bei flussfreien, nichtverschwindenden Zielfeldern bleibt dagegen jede räumliche Drehung um die gemeinsame Feldachse möglich. Beim Nullfeld bleibt jede räumliche Drehung möglich. Normen oder ungerichtete Feldwerte ersetzen den vollständigen Komponentenvergleich in diesem Argument nicht.

Im komplexen HC-Beispiel sind die Zielfelder $B,E$ linear unabhängig. Die gerichtete Längs- und Feldachsenbewegung sowie die verschwindende dritte Geschwindigkeitskomponente fixieren den Beobachter. Stimmen zudem die vollständigen Zielfeldkomponenten nach der deklarierten Dualitätsphase überein, bleibt keine weitere Achsendrehung offen. Im flussfreien Zwischenprofil mit $E_0=2e_x$, $B_0=e_x$ lässt sich die Ausrichtung der beiden senkrechten Achsen durch diese Felder nicht prüfen. Hierfür wäre ein zusätzlicher Richtungsbezug erforderlich.

## Gemeinsame Mehrdeutigkeit von Dualitätsphase und Achsen

Halte die Beobachtergeschwindigkeit fest und lasse sowohl die räumliche Ausrichtung als auch die aktive Dualitätsphase frei. Zwei Paare aus Drehung und Phase mit derselben gerichteten Feldausgabe unterscheiden sich durch eine relative Drehung $R$ und eine relative Einheitsphase $\lambda$, die zusammen das Feld fixieren. Da $R$ den komplexen Skalar $s$ erhält, gilt für $s\ne0$ zwingend $\lambda^2=1$.

Bei linear unabhängigen $E,B$ ergibt $\lambda=1$ nur die Identität. Die zweite Möglichkeit $\lambda=-1$ wird genau durch die Halbdrehung um $E\times B$ kompensiert, weil diese beide Feldvektoren negiert. Damit bestimmen selbst vollständige Feldausgabe und Beobachtergeschwindigkeit die beiden Operationsanteile nur bis zu einer Zweideutigkeit. Im komplexen Beispiel liefern die Phase $(4+3i)/5$ mit den deklarierten Achsen und die negative Phase mit einer zusätzlichen Halbdrehung um die Ziel-Flussachse denselben Feldbericht. Eine deklarierte Phase oder ein unabhängiger räumlicher Richtungsbezug in der Feldebene trennt sie.

Im flussfreien Fall mit nichtverschwindenden parallelen Feldern bleiben für $\lambda=1$ die Drehungen um die Feldachse. Für $\lambda=-1$ kommen die Drehungen hinzu, die diese Achse umkehren. Am nichtverschwindenden nullartigen Feld gibt es sogar eine kontinuierliche Kopplung. Schreibe $E=e\,a$, $B=e\,b$ mit orthonormalen $a,b$. Eine Dualitätsphase $e^{i\theta}$ wird durch eine räumliche Drehung um $a\times b$ mit Winkel $\theta$ kompensiert. Diese Aussage betrifft den lokalen Vergleich bei fester Beobachtergeschwindigkeit. Am Nullfeld sind die Felddaten gegenüber jeder Drehung und Phase unempfindlich.

## Eine geschlossene Feldfolge ohne stetig gerichtete Hauptachse

Sei $w_0=2e_x+i e_y$ und $R_z(\theta)$ eine aktive räumliche Drehung. Die gewählte Feldfolge

$$
w(\theta)=e^{i\theta}R_z(\theta)w_0,\qquad 0\le\theta\le\pi,
$$

ist geschlossen, weil bei $\theta=\pi$ beide Faktoren auf dem transversalen Feld das Vorzeichen wechseln. Es gilt $s(\theta)=3e^{2i\theta}$ und $n=5$. Die Folge bleibt durchgehend nichtnullartig und von Rang zwei. Die aktive Dualität lässt $M=EE^{\mathsf T}+BB^{\mathsf T}$ fest, während die räumliche Drehung $M$ konjugiert. Seine größte Eigenlinie ist daher $\mathbb R R_z(\theta)e_x$.

Jede stetige gerichtete Einheitsachse auf diesem Parameterintervall hat die Form $a(\theta)=\epsilon R_z(\theta)e_x$ mit festem $\epsilon\in\{\pm1\}$. Damit ist $a(\pi)=-a(0)$, obwohl das vollständige Feld am Ende wieder gleich ist. Auf diesem geschlossenen Weg lässt sich die Hauptachse also nicht als eindeutige stetige gerichtete Funktion des Felds wählen. Der Projektor $aa^{\mathsf T}$ kehrt dagegen zu seinem Ausgangswert zurück. Auch die komplexe Phase $\zeta(s)=i e^{-2i\theta}$ und die Halbdrehung $2aa^{\mathsf T}-I$ kehren zurück.

Für QAM genügt bei der aktiven HC-Halbdrehung die ungerichtete Eigenlinie als Nutzdatum. Eine vorzeichenbehaftete Bewegung entlang dieser Achse braucht einen zusätzlichen Richtungsbezug oder einen explizit entlang der Route fortgeführten Richtungswert. Ein festes Vorzeichen kann nicht allein durch eine stetige Auswahl aus dem vollständigen Feld auf diesem Kreis gewonnen werden. Der Befund betrifft die Eigenachse des lokalen Feldmodells, ohne eine Zuordnung zu M/T/P vorauszusetzen.

## Umlaufzahl von s entscheidet die Achsenrückkehr

Sei $w(t)$ ein stetiger geschlossener Weg mit $s(t)=w(t)\cdot w(t)\ne0$. Wähle entlang des Intervalls eine stetige Quadratwurzel $q(t)$ von $s(t)$ und schreibe $w/q=X+iY$. Dann gilt $X\cdot Y=0$ und $|X|^2-|Y|^2=1$. Insbesondere ist $X$ nie null. Außerdem gilt $EE^{\mathsf T}+BB^{\mathsf T}=|s|(XX^{\mathsf T}+YY^{\mathsf T})$. Daher ist $a=X/|X|$ eine stetige gerichtete Hauptachse, und jede andere stetige Wahl unterscheidet sich nur um ein konstantes Vorzeichen.

Schreibe $s(t)=|s(t)|e^{i\phi(t)}$ mit stetig fortgeführtem Winkel. Wenn $s$ den Ursprung $m$-mal umläuft, ist $\phi(1)-\phi(0)=2\pi m$ und die Wurzel erfüllt $q(1)=(-1)^m q(0)$. Weil das volle Feld zurückkehrt, folgt

$$
a(1)=(-1)^m a(0).
$$

Der vorherige Weg hat $m=1$. Bei gerader Umlaufzahl kehrt die gerichtete Achse zurück. Der Projektor und die aktive HC-Feldausgabe kehren bei jeder Umlaufzahl zurück. Für QAM genügt zur Vorhersage des Endvorzeichens neben der Anfangsorientierung die Parität der Umlaufzahl. Sie gehört zur Route und lässt sich aus den beiden Endwerten von $s$ allein nicht gewinnen. Die Regel betrifft die lokale Feldhauptachse und setzt $s\ne0$ entlang des gesamten Weges voraus.

## Umlaufparität aus endlich vielen Messwerten

Sei $s(t)$ ein geschlossener Feldverlauf und $P(t)$ die geschlossene Polygoninterpolation der komplexen Messwerte $\widehat s_j$. Die beiden Endwerte des Polygons sollen übereinstimmen. Angenommen, $s$ hat eine bekannte Lipschitz-Schranke $L$, jeder Messfehler hat Betrag höchstens $\delta$ und die maximale Abtastlücke ist $\Delta$. Dann gilt

$$
\sup_t|s(t)-P(t)|\le\delta+L\Delta/2.
$$

Auf einem Teilintervall mit relativer Position $\lambda$ folgt dies durch den Vergleich mit der linearen Interpolation der exakten Endwerte. Ihr Abstand zu $s(t)$ ist höchstens $2\lambda(1-\lambda)L\Delta$. Die Messfehler der Endwerte tragen zur Interpolation höchstens $\delta$ bei.

Hat das Polygon einen Mindestabstand $d$ vom Nullpunkt mit $d>\delta+L\Delta/2$, dann meidet auch die geradlinige Verformung vom Polygon zu $s$ den Nullpunkt. Beide Kurven haben dieselbe Umlaufzahl und damit dieselbe Achsenparität. Die Regel setzt eine Schranke für den Verlauf zwischen den Abtastungen voraus. Ohne diese kann ein zusätzlicher Umlauf zwischen zwei Messpunkten verborgen bleiben.

Für den gewählten Feldkreis $s(t)=3e^{2\pi i t}$ liefern acht gleichmäßig verteilte Messwerte ein regelmäßiges Achteck mit $d=3\cos(\pi/8)\approx2{,}772$. Bei einer Messfehlergrenze $\delta=0{,}1$ und $L=6\pi$ genügt sogar derselbe Nachweis für jedes Polygon mit diesen Abtastfehlern. Sein Abstand ist mindestens $3\cos(\pi/8)-0{,}1\approx2{,}672$, während die Kurvenabweichung höchstens $0{,}1+3\pi/8\approx1{,}278$ ist. Das gemessene Polygon hat damit wie das exakte Achteck Umlaufzahl eins. Die Achse kehrt mit negativem Vorzeichen zurück. Dies ist eine analytische Robustheitsrechnung für gewählte Eingaben, keine Auswertung erhobener Daten.

## Umlaufparität bei wechselnder positiver Verstärkung

An jedem Abtastpunkt liefert die Viernorm-Differenzauslesung $Z_j=g_j s_j+e_j$, mit gemeinsamem Gain $g_j>0$ innerhalb der vier Messungen dieses Punkts. Der Gain darf sich zwischen den Punkten ändern. Der gemeinsame additive Offset fällt heraus. Im exakten Fall ist die Phase von $Z_j$ die Phase von $s_j$.

Sei $|e_j|\le d_j<|Z_j|$. Aus der Fehlerscheibe um $Z_j$ folgt eine Schranke $\alpha_j=\arcsin(d_j/|Z_j|)$ für die Abweichung seiner Phase von der wahren Phase. Liegt für jedes Abtastintervall eine Schranke $V_j$ für die Änderung des stetig fortgeführten wahren Winkels vor, genügt

$$
V_j+\alpha_j+\alpha_{j+1}<\pi
$$

zur eindeutigen Wahl des Phasenschritts. Dann ist der Hauptwert von $\arg(Z_{j+1}/Z_j)$ gleich dem wahren fortgeführten Phasenschritt plus der Differenz der beiden kleinen Messwinkelabweichungen. Für den geschlossenen Weg verwenden wir am Ende wieder denselben Messwert wie am Anfang. Die Fehlerdifferenzen heben sich in der Summe auf. Die Summe der Hauptwerte ist folglich $2\pi$ mal die wahre Umlaufzahl. Eine hinreichende Vorgabe für $V_j$ ist eine Schranke für die Winkelgeschwindigkeit mal Intervalllänge. Die Regel setzt einen nichtnullartigen Verlauf und garantierte Schranken voraus.

Im Kreisbeispiel ist bei acht Schritten $V_j=\pi/4$. Sind die Restfehler höchstens ein Zehntel des jeweiligen gemessenen Betrags, gilt $\alpha_j\le\arcsin(0{,}1)$ und die Bedingung ist erfüllt. Das gilt auch bei verschiedenen unbekannten positiven Verstärkungen an den acht Punkten. QAM kann damit die Umlaufparität aus Phasenschritten führen, ohne die absoluten Feldskalen der Abtastpunkte miteinander zu vergleichen.

## Zwei Wege zwischen denselben reellen Sektorwerten

Ein stetiger Weg von $s>0$ zu $s<0$, der auf der reellen Achse bleibt, muss $s=0$ durchlaufen. Im nichtnullartigen komplexen Bereich gibt es dagegen Wege mit denselben vollständigen Endfeldern und unterschiedlicher Achsenrückkehr. Für $w_0=2e_x+i e_y$ wähle

$$
w_{\rm oben}(t)=e^{i\pi t/2}w_0,\qquad
w_{\rm unten}(t)=e^{-i\pi t/2}R_z(\pi t)w_0,\qquad 0\le t\le1 .
$$

Beide beginnen bei $w_0$ und enden bei $i w_0$. Der obere Weg hat $s(t)=3e^{i\pi t}$, der untere $s(t)=3e^{-i\pi t}$. Auf dem oberen Weg bleibt die gerichtete Hauptachse $e_x$ fest. Auf dem unteren folgt sie stetig $R_z(\pi t)e_x$ und endet bei $-e_x$. Auch $n$ und der gerichtete Fluss sind auf beiden Wegen gleich, weil die Dualität beide Größen erhält und die räumliche Drehung um die Flussachse erfolgt.

Der obere Weg mit dem invers durchlaufenen unteren Weg bildet einen geschlossenen Weg mit Umlaufzahl eins. Das erklärt die entgegengesetzten Achsenvorzeichen am gemeinsamen Ziel. Die Wahl einer reellen oder komplexen Route und die Fortführung der Orientierung sind deshalb zusätzliche QAM-Daten. Die Wege sind aktive Feldoperationen im Laborprofil. Sie realisieren einen Vergleich algebraischer Sektoren, ohne diese mit den nativen M/T-Profilen gleichzusetzen.

## Wie sich das Achsenvorzeichen auf Teilwegen zusammensetzt

Wähle an Quelle und Ziel je eine gerichtete Referenz auf der Hauptlinie. Ein Weg $\Gamma$ erhält einen Faktor $\epsilon_\Gamma\in\{+1,-1\}$, indem man die Quellreferenz stetig fortführt und mit der Zielreferenz vergleicht. Die Fortführung ist gegenüber dem Vorzeichen der Eingangswahl linear. Daher multiplizieren sich die Faktoren auf aufeinanderfolgenden Wegen, wenn am Zwischenpunkt dieselbe Referenz verwendet wird. Umkehr eines Weges liefert den inversen Faktor, hier denselben Faktor. Kehrt man eine Zwischenreferenz um, ändern sich beide benachbarten Faktoren, ihr Produkt bleibt gleich.

Für die beiden Sektorwege oben und unten gelten bei Referenz $e_x$ an beiden Enden die Faktoren $+1$ und $-1$. Geht man auf demselben Weg zurück, liefert das Produkt $+1$. Die beiden gemischten Rückwege liefern $-1$. In allen vier Fällen kehrt das vollständige elektromagnetische Feld zurück. Das zusätzliche Vorzeichen unterscheidet die Rückkehr der mitgeführten gerichteten Achse. Für einen geschlossenen Weg ist der Gesamtfaktor unabhängig von der Wahl der Referenz und stimmt mit $(-1)^m$ überein.

Die zusammensetzbare QAM-Auslesung kann deshalb das Feld gemeinsam mit einer orientierten Hauptachse führen. Eine einzelne Wegmarke hängt von den beiden Referenzen ab. Geschlossene Produkte oder relative Vergleiche von Wegen mit denselben Endpunkten sind referenzunabhängig. Diese Regel setzt nichtnullartige Teilwege voraus und betrifft die lokale Feldhauptachse.

## Orientierung im symmetrisierten Quelle–Rückweg

Erweitere den lokalen Träger um die mitgeführte Einheitsachse $a$. Für den geschlossenen Rückweg mit identischer Route ergibt sich $(w_0,a_0)$. Der gemischte Rückweg liefert $(w_0,-a_0)$. Auf dem Feldträger sind beide Ergebnisse identisch. Auf dem erweiterten Träger sind sie verschieden.

Im ursprünglichen Laborprofil sei $j(a)=a\cdot a_0$. Werden beide Rückwegvarianten gleich gewichtet, ist der symmetrische Wert $\bar j=(1+(-1))/2=0$, während $j^2=1$ auf beiden Zweigen bleibt. Das Mittel ist keine gerichtete Einheitsachse. Es beschreibt hier die Auslöschung zweier entgegengesetzter Orientierungsberichte. Die Quelle hat $j=1$.

Die Erhaltungsaussage in [Teil 22](../../sources/research/parts/v470/22_op_transport_arguments.tex) setzt gleiche Klassenwerte für beide gerichteten Transporte voraus. Soll $j$ durch die Klasse faktorisieren, dann kann der gemischte Rückweg in diesem erweiterten Modell nicht zugleich als klassenwahrend gelten. Alternativ kann die Klasse die ungerichtete Achse $aa^{\mathsf T}$ oder das ursprüngliche Feld führen. Beide Größen bleiben auf beiden Rückwegen erhalten. Die Parität selbst ist ein Datum des geschlossenen Weges und lässt sich nicht als Funktion des ungehobenen Endfeldes darstellen, da die beiden Wege dasselbe Endfeld und verschiedene Parität haben.

Damit ergeben sich zwei unterschiedliche Anforderungen an einen nativen Abgleich. Erhält die native Klasse nur feldbezogene ungerichtete Daten, ist der lokale gemischte Rückweg damit verträglich. Soll sie die gerichtete Achse erhalten, braucht sie einen Nachweis gerader Umlaufzahl für die zugelassenen geschlossenen Wege oder eine Klassenrelation, die den Orientierungswechsel ausdrücklich berücksichtigt. Welche Variante nativ gemeint ist, wird durch die lokale Rechnung nicht festgelegt.

## Parität aus den einzelnen Transporten

Betrachte einen stetigen nichtnullartigen Feldweg aus gewöhnlichen Lorentztransporten und aktiven Dualitätsdrehungen. Lorentzstücke lassen $s$ fest. Ein Dualitätsstück mit stetig fortgeführtem Winkelzuwachs $\Delta\alpha$ ändert den fortgeführten Winkel von $s$ um $2\Delta\alpha$. Für einen geschlossenen Feldweg folgt daher

$$
m=\frac{1}{\pi}\sum_j\Delta\alpha_j,\qquad
a_{\rm Ende}=(-1)^m a_{\rm Anfang}.
$$

Die Summe ist beim geschlossenen Weg ein ganzzahliges Vielfaches von $\pi$. Für die Orientierungserhaltung muss sie ein Vielfaches von $2\pi$ sein. Bei den gemischten Sektorwegen beträgt sie $\pm\pi$. Der räumliche Anteil kann dabei das volle Feld schließen, ohne den Phasenbeitrag zu ändern. Ein echter Rückweg entlang der invers durchlaufenen Route hebt die Winkelzuwächse paarweise auf.

Eine zweite hinreichende Bedingung ist ein gemeinsamer zulässiger Phasenbereich, auf dem $s$ eine stetige einwertige Winkelwahl besitzt. Beispielsweise reicht eine feste aufgeschnittene komplexe Ebene, wenn kein zugelassener Weg den Schnitt berührt. Dann hat jeder geschlossene Weg darin Umlaufzahl null. Die Annahme $s\ne0$ allein reicht hierfür nicht.

Die Prüfung gilt für die beschriebenen kontinuierlichen Bausteine. Für eine weitere native Operation muss QAM angeben, wie ihr zulässiger Pfad auf $s$ wirkt. Eine bloße Endpunktformel für $s$ kann einen Umlauf zwischen den Endpunkten verdecken. Insbesondere ersetzt eine deklarierte diskrete Involution ohne gewählten Zwischenweg die Prüfung nicht.

## Quellenabgleich zur nativen Phasenbindung

Die [native Routenbeschreibung](../../sources/research/parts/v470/22_op_transport_arguments.tex) fordert Klassenerhaltung für die gerichteten Transporte. Die OP3-Schalenbedingung fordert sie für zulässige Verfeinerungen. Beide Bedingungen betreffen die Klasse am Eingang und am Ergebnis. In den geprüften Definitionen liefern sie keinen kontinuierlichen Pfad für die elektromagnetische Invariante $s$.

Die naheliegende historische Phasenbindung betrifft andere Größen. Der OP1-Epsilon-Korridor in Teil 09 kontrolliert eine positive kanonische Brückennormierung. Der historische OP3-Antiphasenkorridor kontrolliert den sichtbaren Schalenquotienten $\zeta_{\rm sh}$, den Teil 22 als Diagnose verwendet. Weder die Gleichsetzung dieses Quotienten mit $s$ noch eine durchgehende Beziehung seiner Phase zu der von $s$ wird in diesen Korridorbedingungen geliefert.

Ein konkreter ausreichender Anschluss wäre ein stetiger Quotient $\zeta_{\rm sh}(t)$ mit $|\zeta_{\rm sh}(t)+1|\le\rho<1$ entlang eines geschlossenen zulässigen Weges und eine geschlossene stetige Beziehung $s(t)=h(t)\zeta_{\rm sh}(t)$ mit $h(t)>0$. Die Scheibe um $-1$ schließt null aus und hat eine einwertige Winkelwahl. Der positive Faktor verändert den Winkel nicht. Damit wäre die Umlaufzahl null und die Orientierung erhalten. Eine Endpunktbindung allein reicht nicht: Die beiden lokalen Sektorwege geben ein Gegenbeispiel zu genau diesem Schluss. Die vorgeschlagene Beziehung ist eine hinreichende Nachweispflicht, kein im Companion bereits belegtes Wörterbuch.

## Schwächere Brücke: gerade Umlaufzahl genügt

Seien $s(t)$ und der Schalenquotient $\zeta_{\rm sh}(t)$ geschlossene stetige Kurven ohne Null. Liegt der Quotient auf dem ganzen Weg im Antiphasenkorridor $|\zeta_{\rm sh}+1|\le\rho<1$, hat er Umlaufzahl null. Für $h=s/\zeta_{\rm sh}$ gilt wegen der Addition fortgeführter Phasen $\operatorname{wind}(s)=\operatorname{wind}(h)$. Die gerichtete Achse kehrt also genau dann zurück, wenn $h$ gerade Umlaufzahl hat. Gleichwertig ist die Existenz einer stetigen **geschlossenen** Quadratwurzel von $h$. Eine auf einem offenen Parameterintervall fortgeführte Wurzel allein genügt nicht, weil sie am Ende das Vorzeichen wechseln kann.

Eine konkret nachweisbare hinreichende Brücke wäre damit $s(t)=\zeta_{\rm sh}(t)q(t)^2$, wobei ein unabhängig aus der Route konstruiertes $q$ stetig, nie null und am Ende gleich seinem Anfangswert ist. Dann kann $s$ durchaus umlaufen, aber nur mit gerader Umlaufzahl. Ein Beispiel ist $\zeta_{\rm sh}=-1$ und $s(t)=-e^{4\pi i t}$ mit $q(t)=e^{2\pi i t}$. Das negative Gegenbeispiel $s(t)=-e^{2\pi i t}$ hat denselben Schalenquotienten und dieselben Endwerte, aber keine geschlossene Wurzel von $h$.

Die frühere Forderung $h>0$ ist also stärker als nötig. Der Antiphasenkorridor kontrolliert die Phase des Quotienten. Für die Orientierung fehlt die Parität der verbleibenden Phase. Ein bloß als Quadratwurzel von $s/\zeta_{\rm sh}$ entlang des Intervalls gewähltes $q$ würde die offene Endpunktbedingung lediglich umbenennen. Eine native Konstruktion von $q$ ist hier nicht gegeben.

## Prüfung der historischen Routengrößen als Kandidaten für q

Im [historischen Schalenbeweis](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6170) sind die beiden linearen Gewinne $\Gamma_{\rm ph}=A_{\rm sh}a_{\rm sh}$ und $\Gamma_{\rm exp}=B_{\rm sh}b_{\rm sh}$. Die Schalenkonjugation liefert $b_{\rm sh}=-a_{\rm sh}+\varepsilon_{\rm conj}$. Das ist eine Vorzeichenbeziehung zweier Projektionen desselben Schalentangenten. Im exakten balancierten Fall wird $\Gamma_{\rm exp}=-\Gamma_{\rm ph}$ und ihr Quotient ist $-1$. Daraus folgt keine Beziehung zur komplexen Konjugation der Feldinvariante.

Selbst wenn $\Gamma_{\rm ph}$ auf einer konkreten Route stetig, geschlossen und ohne Null wäre, könnte es nur dann als $q$ dienen, wenn unabhängig $s=\zeta_{\rm sh}\Gamma_{\rm ph}^2$ in passenden Einheiten und auf der ganzen Route hergeleitet wird. Die historische Antiphasenrechnung enthält keine solche Gleichung. Der Quotient erfasst auch keine absolute Amplitude. Ein gemeinsamer Faktor in beiden Gewinnen ändert deren Verhältnis nicht. Im exakten Korridor könnten daher bei gleichbleibendem Quotienten sowohl das gerade als auch das ungerade Feldbeispiel aus dem vorigen Abschnitt eingesetzt werden, solange kein zusätzliches Feldwörterbuch gefordert ist.

Die historischen Gewinne geben somit konkrete Größen für eine mögliche Kopplung vor. Für die Achsenrückkehr fehlt die Zuordnung eines Schalentangenten zu einem Feldzustand, die das Quadratgesetz und die geschlossene Rückkehr seines Faktors begründet. Das ist ein Quellenbefund zur geprüften Schalenrechnung, keine globale Nichtexistenzaussage.

## Explizites Feldwörterbuch als lokale Modellrealisierung

Seien $\zeta=\zeta_{\rm sh}$ und $q$ geschlossene stetige Routengrößen ohne Null, wobei $q$ die Einheit eines Feldes trägt. Wähle zwei feste orthonormale Laborachsen $e_1,e_2$ und einen dimensionslosen Parameter $\ell>0$. Die komplexen Vektoren $u_\pm=(e_1\pm i e_2)/\sqrt2$ erfüllen $u_\pm\cdot u_\pm=0$ und $u_+\cdot u_-=1$. Die gewählte Abbildung

$$
w=q\left(\ell u_+ + \frac{\zeta}{2\ell}u_-\right)
$$

liefert reelle Felder $E=\operatorname{Re}w$, $B=\operatorname{Im}w$ und exakt $s=w\cdot w=\zeta q^2$. Die Abbildung ist eindeutig und stetig für feste Achsen und $\ell$. Wenn $\zeta$ im Antiphasenkorridor liegt, kehrt die gerichtete Achse für jede geschlossene Route der Eingabedaten zurück. Beispiel: $\zeta=-1$, $q(t)=q_0 e^{2\pi i t}$ liefert $s=-q_0^2 e^{4\pi i t}$ mit Umlaufzahl zwei. Die Feldroute ist dabei von null verschieden und geschlossen.

Das Modell zeigt auch die verbleibende Freiheit. Es gilt $n=|q|^2(\ell^2+|\zeta|^2/(4\ell^2))$. Bei $\zeta=-1$ und festem $q$ liefern $\ell=1/\sqrt2$ und $\ell=1$ dieselbe Feldinvariante, aber $n=|q|^2$ beziehungsweise $5|q|^2/4$. Selbst das Quadratgesetz bestimmt also den r27-Registerwert $r=|s|/n$ nicht. Hierfür wäre eine zusätzliche Skalenvorschrift erforderlich. Achsen und $\ell$ sind gewählte Daten des Vergleichsmodells. Ihre Identifikation mit nativem Schalentangententransport ist eine separate Nachweispflicht.

## Der freie Parameter des Feldwörterbuchs ist ein kollinearer Boost

Setze $k=e_1\times e_2$. Beim gewöhnlichen Beobachterboost mit Rapidität $\eta$ entlang $k$ gilt für transversale komplexe Felder $w'=\cosh(\eta)w-i\sinh(\eta)\,k\times w$. Da $k\times u_\pm=\mp i u_\pm$, werden $u_+$ und $u_-$ mit $e^{-\eta}$ beziehungsweise $e^\eta$ multipliziert. Daher gilt für das oben gewählte Feldwörterbuch

$$
B_\eta w(q,\zeta,\ell)=w(q,\zeta,e^{-\eta}\ell).
$$

Bei festen $q,\zeta$ und festen ausgerichteten Achsen sind alle positiven $\ell$ somit auf derselben gewöhnlichen Lorentzbahn. Für $\ell_*=\sqrt{|\zeta|/2}$ haben beide Nullkomponenten gleiche Stärke. Mit $\tau=\log(\ell/\ell_*)$ gilt

$$
n=|s|\cosh(2\tau),\qquad
\mathbf P=\tfrac{|s|}{2}\sinh(2\tau)\,k,\qquad
r=\operatorname{sech}(2\tau).
$$

Die Wahl $\ell_*$ fixiert ein flussfreies Profil dieser Modellfamilie. Die äußeren Profile mit entgegengesetztem Fluss haben Parameter $\ell$ und $\ell_*^2/\ell$. Für $\zeta=-1$ ist beispielsweise $\ell=1/\sqrt2$ flussfrei und $\ell=1$ durch einen Boost mit Rapiditätsbetrag $\log\sqrt2$ verbunden. Die zuvor erhaltenen Werte $r=1$ und $r=4/5$ gehören also zu verschiedenen Beobachterprofilen derselben Feldbahn.

Das präzisiert die offene Auswahl im konstruierten Wörterbuch. Bei festem $q,\zeta$ fehlt eine Vorschrift für die Beobachterrapidität, um $r$ festzulegen. Eine Wahl des Zählfaktors würde den Betrag $|\tau|$ bestimmen. Das Vorzeichen und die native M/T-Zuordnung wären weiterhin zusätzlich festzulegen.

## HC-Involution auf den Eingabedaten des Feldwörterbuchs

Bei festen Laborachsen und $\zeta\ne0$ vertauscht komplexe Konjugation die Nullvektoren $u_+$ und $u_-$. Einsetzen in $J_Bw=i\bar w$ liefert exakt

$$
J_B w(q,\zeta,\ell)
=w\left(i\frac{\bar\zeta}{|\zeta|}\bar q,\ \zeta,\ \frac{|\zeta|}{2\ell}\right).
$$

Zur Kontrolle ist der neue $u_+$-Koeffizient $i\bar q\,\bar\zeta/(2\ell)$ und der neue $u_-$-Koeffizient $i\bar q\,\ell$. Der Quotient $\zeta$ bleibt dabei fest. Der neue Faktor $q'=i\bar\zeta\,\bar q/|\zeta|$ hat denselben Betrag und ergibt $s'=\zeta(q')^2=-\bar s$. Die Beobachterkoordinate wird $\tau'=-\tau$. Zweimalige Anwendung gibt $q''=q$ und $\ell''=\ell$. Der flussfreie Wert $\ell_*$ ist der Fixpunkt der Parameterumkehr, während die Feldphase auch dort verändert werden kann.

Bei $\zeta=-1$ und $q=1$ ist $q'=-i$. Für $\ell=1$ ist $\ell'=1/2$. So gehen $s=-1$ und $s'=+1$ ineinander über, bei gleicher Feldskala $n=5/4$ und entgegengesetztem Fluss. Das Modell erlaubt damit einen Vorzeichenwechsel von reellem $s$, während der Schalenquotient genau im Antiphasenwert bleibt. Der Wechsel steckt in $q$, nicht in der Schalenphase. Diese Gleichung ist eine exakte Verträglichkeit des gewählten Wörterbuchs mit der HC-Involution. Die historische Schalenrechnung müsste separat zeigen, dass ihre Routendaten genau diese Transformation tragen.

## Grenze einer linearen Identifikation mit den Schalengewinnen

Im exakt balancierten historischen Schalenmodell gilt $\Gamma_{\rm exp}=-\Gamma_{\rm ph}$. Betrachte als möglichen Anschluss die Vertauschung der beiden Gewinne bei festem $\zeta=-1$. Das Gewinnpaar $(\Gamma_{\rm ph},\Gamma_{\rm exp})=(g,-g)$ geht dabei in $(-g,g)$ über. Jede feste lineare Auslesung dieses Paars, auch mit komplexen Koeffizienten, liefert daher $q'=-q$. Im Wörterbuch folgt $s'=\zeta(q')^2=s$. Auf dem reellen nichtnullartigen Sektor verlangt die HC-Abbildung jedoch $s'=-s$. Eine feste lineare Kombination der beiden Gewinne unter dieser Vertauschung kann den Sektorwechsel also nicht realisieren. Die Vertauschung ist hier eine geprüfte Kandidatenannahme, keine aus der historischen Antiphasengleichung abgeleitete native Map.

Allgemeiner gilt dieselbe Schranke für jede ungerade Auslesung des Gewinnpaars. Für eine komplexe Kopplung mit positivem reellem Gewinn kann man die fehlende Information sichtbar machen. Setze auf zwei getrennt deklarierten Sektoren beispielsweise $q_-(g)=g$ und $q_+(g)=ig$ für reelles $g\ne0$. Wechselt das Gewinnvorzeichen, dann gilt $q_+(-g)=-ig=-i\overline{q_-(g)}$ und $q_-(-g)=-g=-i\overline{q_+(g)}$. Diese gewählte Zuordnung reproduziert die HC-Transformation von $q$ bei $\zeta=-1$. Sie führt eine relative Viertelphase zwischen den beiden Profilen als neue Eingabe ein. Die historische Vorzeichenbeziehung bestimmt diese Phase nicht.

Das Beispiel trennt damit zwei Nachweispflichten. Der reelle Schalengewinn kann eine Amplitude liefern. Für den HC-Sektorwechsel braucht die Kopplung zusätzlich eine begründete komplexe Phasenzuordnung oder eine andere Feldabbildung. Die Beobachterkoordinate $\ell$ bleibt davon getrennt.

## Zwei reelle Komponenten für den komplexen Feldfaktor

Bei $\zeta=-1$ schreibe $q=x+iy$. Die HC-Regel $q'=-i\bar q$ ist dann die reell-lineare Abbildung $(x,y)\mapsto(-y,-x)$. Sie hat eine feste Linie $x=-y$ und eine vorzeichenwechselnde Linie $x=y$. Dagegen wirkt die Vertauschung des exakt antiphasierten historischen Gewinnpaars $(g,-g)$ auf dessen einziger freier reeller Koordinate als $g\mapsto-g$.

Jede feste reell-lineare Abbildung dieser eindimensionalen Koordinate nach $\mathbb C$, die mit beiden Involutionen verträglich ist, muss daher die Form $q=\lambda(1+i)g$ mit reellem $\lambda$ haben. Ihr Bild liegt auf der vorzeichenwechselnden Linie. Dort ist $s=-2i\lambda^2g^2$ rein imaginär und unter HC invariant. Damit kann die eindimensionale exakte Gewinnlinie selbst bei zulässiger komplexer Ausgabe keinen Wechsel zwischen reellen nichtnullartigen $s$-Sektoren tragen.

Eine gewählte zweikomponentige Erweiterung zeigt, welche Struktur ausreichen würde. Zwei unabhängige reelle Amplituden $u,v$ mit Übergang $(u,v)\mapsto(u,-v)$ ergeben

$$
q=u(1-i)+v(1+i),\qquad
s=-4uv+2i(u^2-v^2).
$$

Auf den reellen nichtnullartigen Sektoren gilt $u^2=v^2>0$. Das Umkehren von $v$ kehrt das Vorzeichen von $s$ um. Die zweite Amplitude muss entlang der Route unabhängig definiert und ihre Übergangsregel begründet werden. Aus dem exakten Gewinnpaar allein folgt sie nicht. Die Konstruktion betrifft den Feldfaktor bei festem Schalenquotienten und legt weiterhin keine Beobachterrapidität fest.

## Nichtlineare Kopplung aus einem einzigen reellen Gewinn

Die Schranke für eine reell-lineare Kopplung lässt einen nichtlinearen Anschluss zu. Auf dem eingeschränkten Bereich $g\in\mathbb R\setminus\{0\}$ wähle $u=|g|$ und $v=g$. Die Gewinnvertauschung $g\mapsto-g$ lässt $u$ fest und kehrt $v$ um. Bei $\zeta=-1$ erhält man damit

$$
q(g)=|g|(1-i)+g(1+i),\qquad q(-g)=-i\overline{q(g)},
\qquad s(g)=-4|g|g.
$$

Für $g=1$ ist $q=2$ und $s=-4$. Für $g=-1$ ist $q=-2i$ und $s=4$. Der frühere Befund zur linearen Kopplung bleibt bestehen. Für diese beiden reellen Halbstrahlen braucht das gewählte nichtlineare Wörterbuch jedoch keine zweite unabhängige Amplitude. Die Bedingung $u^2=v^2$ ist hier bereits eingebaut. Eine dimensionsbehaftete Kalibrierung von $g$ als Feldamplitude und die Gültigkeit der Kopplung in der nativen Route müssen separat begründet werden.

Der Definitionsbereich $g\ne0$ hat zwei Zusammenhangskomponenten. Eine stetige reelle Gewinnroute zwischen ihnen durchläuft $g=0$ und damit im gewählten Wörterbuch $q=s=0$. Das Modell realisiert den diskreten HC-Sektorwechsel. Es liefert keinen stetigen nichtnullartigen Zwischenweg zwischen den beiden Sektoren. Dafür wäre ein zusätzlicher komplexer Pfad oder ein entsprechend erweiterter Träger nötig. Die Umkehr $\ell\mapsto|\zeta|/(2\ell)$ bleibt eine eigene Beobachterzuordnung.

## Stetige komplexe Fortsetzung der Gewinnkopplung

Erweitere den Modellgewinn auf $g\in\mathbb C\setminus\{0\}$ und behalte die Vertauschung $g\mapsto-g$. Bei $\zeta=-1$ ist

$$
q(g)=2|g|\exp\!\left[-\frac{i\pi}{4}
 \left(1-\frac{\operatorname{Re}g}{|g|}\right)\right]
$$

eine stetige gewählte Fortsetzung der reellen Kopplung. Für reelles positives $g$ ist $q=2g$, für reelles negatives $g$ ist $q=-2i|g|$. Direkt gilt $q(-g)=-i\overline{q(g)}$. Auf einem Halbkreis von $g_0>0$ nach $-g_0$ bleibt $|q|=2g_0$. Daher wechselt $s=-q^2$ den reellen Sektor, ohne null zu werden. Beide Halbkreise im Gewinnraum liefern in dieser speziellen Fortsetzung dieselbe Feldphasenkurve, weil $q$ vom Winkel nur über seinen Kosinus abhängt. Die Konstruktion verwendet den Imaginärteil des Gewinns als erlaubte Route und setzt diese komplexe Erweiterung als neue Modelldaten voraus.

Die Rückkehr ist stärker beschränkt als durch das Quadratgesetz allein. Für jede stetige nullfreie Funktion $q(g)$ auf dem punktierten komplexen Gewinnraum mit $q(-g)=-i\overline{q(g)}$ hat $q$ auf jedem Ursprungskreis Umlaufzahl null. Eine Drehung des Eingabekreises um $\pi$ ändert die Umlaufzahl nicht. Komplexe Konjugation der Ausgabe kehrt sie um. Aus der Verträglichkeit folgt daher $m_q=-m_q$. Das gilt auch für alle geschlossenen Gewinnwege im punktierten Raum, weil jeder zu einer entsprechenden Zahl von Kreisumläufen deformierbar ist. Bei festem $\zeta=-1$ hat dann auch $s$ Umlaufzahl null.

Die Einschränkung gilt für eine einwertige stetige Kopplung mit genau dieser Vertauschung. Das allgemeine Feldwörterbuch mit unabhängigem $q$ erlaubt weiterhin gerade, von null verschiedene Umlaufzahlen. Die historische reelle Gewinnrechnung liefert weder den komplexen Gewinnraum noch eine solche Fortsetzung.

## Regularität der komplexen Gewinnkopplung

Auf einem zusammenhängenden offenen Gewinnbereich, der unter $g\mapsto-g$ abgeschlossen ist, kann eine holomorphe Kopplung $q$ mit $q(-g)=-i\overline{q(g)}$ nur konstant sein. Die linke Seite ist holomorph, die rechte antiholomorph. Eine Funktion mit beiden Eigenschaften ist konstant. Damit gibt es auf dem punktierten Gewinnraum keine holomorphe Fortsetzung, die zugleich beide reellen Sektorwerte $q(1)=2$, $q(-1)=-2i$ erfüllt. Die konstruierte Fortsetzung ist dort reell-glatt und hängt von Betrag und Realteil des Gewinns ab.

Die Annahme über die Wirkung auf den Eingaberaum ist entscheidend. Für die alternative Eingabeabbildung $g\mapsto-i\bar g$ wäre etwa die holomorphe Wahl $q(g)=g$ mit der HC-Regel verträglich. Diese Eingabeabbildung schickt die positive reelle Achse auf die negative imaginäre Achse. Sie setzt damit eine andere Darstellung der beiden Schalensektoren voraus als die historische reelle Gewinnvertauschung.

Für eine native Kopplung sind daher die Transformation des erweiterten Gewinnträgers und die geforderte Regularität gemeinsam festzulegen. Der Ausschluss gilt für den deklarierten komplexen Träger mit Vorzeichenvertauschung. Er liefert keine Aussage gegen anders typisierte oder reell-glatte Modelle.

## Der symmetrische Gewinn nahe exakter Antiphase

Für reelle Gewinne $p=\Gamma_{\rm ph}$ und $e=\Gamma_{\rm exp}$ setze $U=(p+e)/2$ und $V=(p-e)/2$. Ihre Vertauschung fixiert $U$ und negiert $V$. Damit ist $q=aU(1-i)+bV(1+i)$ mit festen reellen Kalibrierkoeffizienten $a,b$ eine reell-lineare HC-verträgliche Kopplung im Vergleichsmodell mit Feldquotient $\zeta=-1$. Der historische Gewinnquotient $\chi=e/p$ bleibt davon getrennt. Liegt er bei $p\ne0$ im Korridor $|\chi+1|\le\rho<1$, folgt

$$
\left|\frac{U}{V}\right|
=\left|\frac{1+\chi}{1-\chi}\right|
\le\frac{\rho}{2-\rho}.
$$

Für ein reelles nichtnullartiges $s$ verlangt diese Kopplung $|aU|=|bV|>0$. Bei $b\ne0$ ist daher $|a/b|\ge(2-\rho)/\rho$ notwendig, wenn $\rho>0$. Bei exakter Antiphase verschwindet $U$, und kein endliches festes $a/b$ genügt. Bei der gewählten Beispielschranke $\rho=0{,}1$ müsste der symmetrische Anteil mindestens um den Faktor $19$ relativ zum antisymmetrischen Anteil verstärkt werden. Dies ist eine notwendige Bedingung. Der tatsächliche Quotient kann noch näher an $-1$ liegen und einen größeren Faktor erfordern.

Damit gibt es im unbalancierten Gewinnpaar zwar einen natürlichen geraden Anteil, doch eine feste lineare Kalibrierung kann mit ihm keine reelle nichtnullartige Zuordnung beliebig nahe an der exakten Antiphase aufrechterhalten. Die nichtlineare Wahl aus dem vorigen Abschnitt verwendet stattdessen den Gewinnbetrag und gehört zu einem anderen Wörterbuch. Die Rechnung prüft die als Kandidat gewählte Gewinnvertauschung und identifiziert den historischen Gewinnquotienten nicht mit dem Feldquotienten.

## Phasenschranke bei begrenzter linearer Kalibrierung

Verwende die vorige lineare Kopplung und setze $u=aU$, $v=bV$. Nehme $b\ne0$ und eine unabhängige Obergrenze $|a/b|\le K$ an. Dann gilt $|u/v|\le d=K\rho/(2-\rho)$. Für $d<1$ ergeben $s=-4uv+2i(u^2-v^2)$ und $|s|=2(u^2+v^2)$ die Schranken

$$
\frac{|\operatorname{Im}s|}{|s|}\ge\frac{1-d^2}{1+d^2},
\qquad
\frac{|\operatorname{Re}s|}{|s|}\le\frac{2d}{1+d^2}.
$$

Die erste Funktion fällt und die zweite steigt mit $|u/v|$ bis eins. Die Grenzen sind im gewählten Modell scharf. Der Rand $\chi=-1+\rho$ und $|a/b|=K$ realisiert $|u/v|=d$. Bei gleicher Kalibrierstärke $K=1$ und $\rho=0{,}1$ folgt $d=1/19$. Der imaginäre Anteil beträgt dann mindestens $180/181$, der reelle höchstens $19/181$ des Betrags von $s$.

Damit ist bei begrenzter linearer Verstärkung eine Umgebung des reellen Sektors ausgeschlossen, solange der Gewinnquotient hinreichend eng um Antiphase gebunden ist. Die Schranken betreffen ausschließlich diese gewählte lineare Kopplung bei Feldquotient $\zeta=-1$. Sie gelten unabhängig von der beobachterabhängigen Skala $\ell$. Die Kalibriergrenze $K$ ist eine zusätzliche Modellannahme und stammt nicht aus der historischen Schalenrechnung.

## Phasenschranke mit variablem Feldquotienten

Behalte die lineare Auslesung $q=u(1-i)+v(1+i)$ und die Schranke $|u/v|\le d<1$ aus dem historischen Gewinnkorridor. Erlaube separat einen Feldquotienten mit $|\zeta+1|\le\sigma<1$. Für $\zeta=-1$ liegt $s=-q^2$ höchstens im Winkelabstand $2\arctan d$ zur negativen imaginären Achse. Das folgt aus $q/v=(1+i)+(u/v)(1-i)$, dessen Richtung höchstens um $\arctan d$ von $1+i$ abweicht. Das Quadrieren verdoppelt den Winkel. Die Scheibe des Feldquotienten erlaubt zusätzlich eine Abweichung von der negativen reellen Achse von höchstens $\arcsin\sigma$. Deshalb ist der Winkelabstand von $s=\zeta q^2$ zur negativen imaginären Achse höchstens

$$
\Theta=2\arctan d+\arcsin\sigma.
$$

Für $\Theta<\pi/2$ bleibt die reelle Achse ausgeschlossen und $|\operatorname{Im}s|/|s|\ge\cos\Theta$. Bei unabhängig wählbaren Grenzen kann die reelle Achse erst erreicht werden, wenn $\sigma\ge\cos(2\arctan d)=(1-d^2)/(1+d^2)$. Diese Grenze ist für das gewählte Modell scharf. Bei gleicher Kalibrierung und historischem Gewinnradius $\rho=0{,}1$ ist $d=1/19$. Damit müsste der Feldquotientenradius mindestens $180/181$ betragen. Eine zusätzliche Feldquotientenabweichung von nur $\sigma=0{,}1$ lässt weiterhin $|\operatorname{Im}s|/|s|\gtrsim0{,}979$.

Die Rechnung verwendet die feste lineare Auslesung aus dem exakt antiphasierten Modell und variiert danach den Feldquotienten. Für nichtreelles $\zeta$ ist die HC-Verträglichkeit dieser festen Kopplung eine separate Bedingung, da die HC-Regel für $q$ von $\zeta$ abhängt. Die Phasenschranke setzt diese Verträglichkeit nicht voraus.

## HC-verträgliche lineare Kopplung bei komplexem Feldquotienten

Schreibe $\zeta=-|\zeta|e^{i\delta}$ mit stetig gewähltem $\delta$ im Korridor $|\zeta+1|<1$. Beim Gewinnwechsel bleibt der Feldquotient fest. Die HC-Regel lautet dann $q'= -i e^{-i\delta}\bar q$. Die an diese Regel angepasste reell-lineare Auslesung ist

$$
q=e^{-i\delta/2}\bigl(aU(1-i)+bV(1+i)\bigr),\qquad a,b\in\mathbb R.
$$

Sie erfüllt die HC-Regel unter $(U,V)\mapsto(U,-V)$. Umgekehrt ist bei festem $\zeta$ jede reell-lineare Kopplung aus diesen beiden Gewinnkomponenten, die mit der Vertauschung verträglich ist, von dieser Form. Der $U$-Koeffizient muss auf der festen reellen Eigenlinie der HC-Abbildung liegen und der $V$-Koeffizient auf ihrer vorzeichenwechselnden Eigenlinie. Beide sind die um $-\delta/2$ gedrehten Linien des Falls $\zeta=-1$.

Beim Bilden von $s=\zeta q^2$ kürzt sich die Feldquotientenphase exakt heraus:

$$
s=-|\zeta|\bigl(aU(1-i)+bV(1+i)\bigr)^2.
$$

Damit gilt die frühere Schranke $|\operatorname{Im}s|/|s|\ge(1-d^2)/(1+d^2)$ für $d=K\rho/(2-\rho)<1$ unverändert, sofern $b\ne0$ und $|a/b|\le K$. Die zusätzliche Winkelabweichung aus dem vorigen Abschnitt galt für eine festgehaltene, nicht an die komplexe HC-Regel angepasste Kopplung. Hier kann eine Änderung der Phase von $\zeta$ den reellen Sektor bei begrenzter Verstärkung nicht öffnen. Die Aussage betrifft die gewählte Gewinnvertauschung mit festem Feldquotienten. Eine native Abbildung, die den Feldquotienten selbst ändert, ist ein anderer Fall.

## Darf die HC-Involution den Feldquotienten ändern?

Halte die Laborachsen im Wörterbuch fest und erlaube zunächst beliebige neue Eingaben $(q',\zeta',\ell')$ mit $\ell'>0$. Für $q,\zeta\ne0$ haben beide Nullkomponenten einen von null verschiedenen Koeffizienten. Vor HC ist ihr Quotient (Minus- durch Pluskomponente) $\zeta/(2\ell^2)$. Nach $J_Bw=i\bar w$ lautet er $2\ell^2/\bar\zeta$. Folglich muss gelten

$$
\frac{\zeta'}{2(\ell')^2}=\frac{2\ell^2}{\bar\zeta}.
$$

Da beide Skalen positiv sind, hat $\zeta'$ dieselbe Phase wie $\zeta$. Jede Darstellung der HC-Ausgabe im selben Wörterbuch hat daher die Form

$$
\zeta'=\lambda\zeta,\qquad
\ell'=\sqrt\lambda\,\frac{|\zeta|}{2\ell},\qquad
q'=\lambda^{-1/2}i\frac{\bar\zeta}{|\zeta|}\bar q,\qquad \lambda>0.
$$

Die Freiheit in $\lambda$ ist eine Umparametrisierung. Allgemein lässt $(q,\zeta,\ell)\mapsto(q/\sqrt\lambda,\lambda\zeta,\sqrt\lambda\,\ell)$ beide komplexen Feldkoeffizienten unverändert. Auch $\ell/\sqrt{|\zeta|/2}$ bleibt gleich. Wird dagegen der historische Quotientenbetrag als eigenes beobachtbares Datum identifiziert, muss seine Entwicklung separat begründet werden. Das Feld allein bestimmt sie nicht.

Damit kann eine Änderung der Feldquotientenphase bei HC auf diesem festen Wörterbuch nicht als Ausweg dienen. Eine solche Änderung würde eine andere Achsenzuordnung oder eine andere Feldabbildung voraussetzen. Insbesondere darf eine native Veränderung des Schalenquotienten nicht ohne deklariertes Wörterbuch als Änderung der Feldphase gelesen werden.

## Feldquotient bei gedrehten Darstellungsachsen

Drehe das orthonormale Basispaar $(e_1,e_2)$ um $\theta$ um $k=e_1\times e_2$, während das geometrische Feld festgehalten wird. Die neuen Nullbasisvektoren sind $u'_+=e^{-i\theta}u_+$ und $u'_-=e^{i\theta}u_-$. Dasselbe Feld hat dann die Eingabedaten

$$
q'=e^{i\theta}q,\qquad
\zeta'=e^{-2i\theta}\zeta,\qquad
\ell'=\ell.
$$

Einsetzen zeigt $w'=w$ als geometrischen Vektor und $\zeta'(q')^2=\zeta q^2=s$. Auch Feldskala und Fluss bleiben geometrisch unverändert. So kann die Phase des Feldquotienten durch die Darstellungsachsen verändert werden, obwohl sie bei der HC-Feldabbildung mit festgehaltenen Achsen erhalten bleibt. Nach zusätzlicher positiver Umparametrisierung lässt sich punktweise $\zeta=-1$ wählen.

Entlang eines geschlossenen Weges mit $\zeta\ne0$ benötigt eine stetige Achsenwahl, die $\zeta$ auf der negativen reellen Achse hält, den halben fortgeführten Quotientenwinkel. Bei Umlaufzahl $m_\zeta$ ist die nötige Achsendrehung am Ende $\pi m_\zeta$ relativ zum Anfang. Die gerichteten Achsen kehren daher nur bei geradem $m_\zeta$ zurück. Im durchgehend eingehaltenen Antiphasenkorridor ist $m_\zeta=0$. Diese Aussage setzt feste transversale Bezugsebene und stetige Achsenwahl voraus.

Für einen Vergleich mit dem historischen Schalenquotienten braucht es deshalb neben der Feldabbildung auch eine deklarierte Achsenkonvention oder ein entsprechendes Transformationsgesetz für den Quotienten. Ein bloßer Vergleich der Phasen in unterschiedlich orientierten Darstellungen kann eine physikalische Phasenänderung vortäuschen.

## Umlaufparität unter geschlossenen Achsenwechseln

Für eine geschlossene Darstellung mit $q,\zeta\ne0$ gilt aus $s=\zeta q^2$

$$
m_s=m_\zeta+2m_q.
$$

Eine geschlossene stetige Drehung der Darstellungsachsen mit Gesamtwinkel $2\pi k$ verändert die beiden Beiträge zu $m_q'=m_q+k$ und $m_\zeta'=m_\zeta-2k$. Damit bleiben $m_s$ und die Parität von $m_\zeta$ unverändert. Insbesondere kann eine geschlossene Achsenwahl einen Quotienten mit ungerader Umlaufzahl nicht auf eine konstante Phase bringen. Bei gerader Umlaufzahl ist die Halbwinkelwahl aus dem vorigen Abschnitt geschlossen.

Erlaubt man für eine Route stattdessen, dass beide Darstellungsachsen am Ende umkehren, kann man auch bei ungerader Umlaufzahl $\zeta$ durchgehend auf der negativen Achse halten. Dann ist der neue Faktor $q'$ am Ende das Negative seines Anfangswerts. Diese Umkehr wird durch die beiden negierten Nullbasisvektoren ausgeglichen, sodass das geometrische Feld schließt. Die ungerade Parität steckt in dieser Darstellung im Übergang der Achsen und des Feldfaktors statt in der sichtbaren Quotientenphase.

Ein Beispiel liefert der geschlossene Feldkreis $w(t)=e^{i\pi t}R_z(\pi t)w_0$ mit $w_0=2e_x+i e_y$. In der festen Nullbasis kann man $\ell=\sqrt{3/2}$, $q=\sqrt3$ und $\zeta=e^{2\pi it}$ wählen. In der mitrotierenden Basis mit $\theta=\pi t$ bleibt $\zeta'=1$, aber $q'=\sqrt3 e^{i\pi t}$ und beide Basisachsen kehren ihr Vorzeichen um. Eine zusätzliche konstante Achsendrehung setzt die Quotientenphase auf $-1$ und ändert die Endvorzeichen nicht.

Für die native Phasenbrücke ist daher wichtig, dass die konstante Quotientenphase und die geschlossene Achsendarstellung gemeinsam belegt werden. Eine Antiphasennormierung, die erst durch unterwegs mitgedrehte Achsen entsteht, liefert die Paritätsaussage allein nicht.

## Parität aus Übergängen zwischen lokalen Antiphasendarstellungen

Zerlege einen geschlossenen nichtnullartigen Feldweg in Teilstücke. Auf jedem Stück wähle eine stetige transversale Darstellung mit $\zeta=-1$, einschließlich der positiven Umparametrisierung des Betrags. Benachbarte Darstellungen sollen am gemeinsamen Feldpunkt dieselbe orientierte Ebenennormale verwenden. Da beide Quotienten auf $-1$ normiert sind, kann der Unterschied der beiden transversalen Basen dort nur eine Drehung um null oder $\pi$ sein. Bezeichne ihr Vorzeichen mit $\epsilon_j=\pm1$. Für den Feldfaktor gilt an der Naht ebenfalls $q_{\rm neu}=\epsilon_j q_{\rm alt}$. Die Naht zwischen letztem und erstem Teilstück zählt mit.

Auf jedem Teilstück ist $iq$ eine stetige Quadratwurzel von $s=-q^2$. Verfolgt man eine einzige Wurzel über alle Teilstücke, muss man an jeder Naht gegebenenfalls das Vorzeichen der lokalen Wurzel korrigieren. Damit gilt für den geschlossenen Weg

$$
(-1)^{m_s}=\prod_j\epsilon_j .
$$

Eine Umkehr beider Basisachsen auf einem ganzen Teilstück verändert die Vorzeichen an seinen beiden Grenzen. Ihr Produkt bleibt gleich. Das Ergebnis ist daher unabhängig von diesen lokalen Referenzwahlen. Beim bekannten Feldkreis kann man die durchgehend mitrotierende Antiphasendarstellung als ein einziges Stück verwenden. Der Schließübergang hat dann Vorzeichen $-1$. Eine feinere Zerlegung verteilt das Vorzeichen auf mehrere Nähte, ohne das Gesamtprodukt zu ändern.

Für QAM ist das eine Alternative zur direkten Umlaufrechnung. Lokale Quotienten können überall auf $-1$ stehen und dennoch globale Orientierungsinformation tragen. Dafür braucht der Export an jeder Naht die gerichtete Achsenzuordnung oder ihr Vorzeichen. Die Konstruktion setzt das hier gewählte transversale Wörterbuch voraus. Ein historischer Schalenkorridor ohne entsprechendes Achsenwörterbuch liefert diese Nahtdaten nicht automatisch.

## Orientierungsprüfung für ein verzweigtes Routennetz

Modelliere eine endliche zusammenhängende Sammlung zulässiger nichtnullartiger Teilwege als Graph. Die Knoten bezeichnen vollständige Zustände mit jeweils einer gewählten gerichteten Referenz auf der Hauptachse. Jede Kante trägt das Vorzeichen der stetigen Orientierung von Quelle zu Ziel relativ zu diesen Referenzen. Die inverse Kante trägt denselben Faktor. Verschiedene Teilwege mit denselben Endpunkten bleiben als parallele Kanten getrennt.

Wähle einen Spannbaum und eine Orientierung an seiner Wurzel. Die Kantenfaktoren des Baums legen dann die Orientierung an jedem Knoten fest. In dieser Wahl haben alle Baumkanten Faktor $+1$. Jede übrige Kante schließt zusammen mit dem zugehörigen Baumweg einen Grundkreis. Ihr verbleibender Faktor ist genau das Vorzeichenprodukt dieses Kreises. Eine einheitliche, auf allen Teilwegen erhaltene Orientierung existiert deshalb genau dann, wenn jeder dieser Grundkreise Produkt $+1$ hat. Es genügen $|E|-|V|+1$ Prüfungen für einen zusammenhängenden Graphen mit Kantenmenge $E$ und Knotenmenge $V$.

Die beiden Sektorwege bilden bereits einen Graphen aus zwei Knoten und zwei parallelen Kanten. Wählt man den oberen Weg als Baumkante, ist der untere die einzige zusätzliche Kante und der Grundkreis hat Produkt $-1$. Ein Umbenennen der Zielrichtung kann den Konflikt nur zwischen den Kanten verschieben. Der ungerichtete Projektor kann auf beiden Teilwegen dennoch konsistent geführt werden.

Für einen nativen QAM-Abgleich wäre damit ein konkretes Routeninventar verwendbar. Pro Teilweg braucht es die Endzustände und ein aus dem Pfad oder seinen lokalen Übergängen belegtes Vorzeichen. Die Spannbaumprüfung ersetzt die Kontrolle aller geschlossenen Wege durch Grundkreise. Das setzt voraus, dass die betrachteten nativen Routen tatsächlich durch den gewählten Graphen und seine zulässigen Zusammensetzungen erfasst werden. Der lokale Graph enthält noch keine native Zulassungsentscheidung.

## Orientierter Zustandsträger für verzweigte Wege

Zu jedem Feldknoten $x$ mit gewählter Hauptachsenreferenz gehören zwei erweiterte Zustände $(x,\sigma)$ mit $\sigma=\pm1$. Ein Teilweg $e:x\to y$ mit belegtem Vorzeichen $\epsilon_e$ wird zur Abbildung

$$
(x,\sigma)\longmapsto (y,\epsilon_e\sigma).
$$

Die Orientierung ist auf diesem erweiterten Träger eindeutig fortführbar. Ein geschlossener Feldweg mit negativem Kreisprodukt wechselt zwischen den beiden Orientierungen. Erst seine zweimalige Anwendung schließt auch den erweiterten Zustand. Die Referenzumkehr an einem Knoten vertauscht dort nur die Namen seiner beiden Zustände und ändert keinen geometrischen Übergang.

Ist der ursprüngliche Routengraph zusammenhängend und sind inverse Wege zugelassen, gibt es zwei Fälle. Sind alle Kreisprodukte positiv, zerfällt der erweiterte Graph in zwei getrennte Kopien des ursprünglichen Netzes. Gibt es einen negativen Kreis, ist der erweiterte Graph zusammenhängend. Der negative Kreis erlaubt am Ausgangsknoten den Orientierungswechsel. Über die übrigen Wege erreicht man dann beide Orientierungen jedes Knotens.

Im lokalen Sektorbeispiel verbindet der obere Weg gleiche und der untere entgegengesetzte Referenzvorzeichen. Der gemischte Rückweg führt von $(w_0,+1)$ zu $(w_0,-1)$. Ein einziges zusätzliches Bit pro aktuellem Zustand genügt zur Vorhersage aller gerichteten Folgewerte, sofern die Kantenfaktoren feststehen. Auf einer Route mit erreichbarem negativem Kreis ist dieses Bit für eine Auslesung notwendig, die beide Achsenrichtungen unterscheidet. Das vollständige Feld allein hat dort zwei mögliche gerichtete Fortsetzungen.

Für QAM ergibt sich die Wahl zwischen dem ursprünglichen Feldträger für ungerichtete Auslesungen und dem erweiterten Träger für gerichtete Auslesungen. Der erweiterte Träger macht den Wechsel sichtbar. Er erklärt einen negativen Rückweg nicht zu einer Rückkehr desselben orientierten Zustands. Die native Anwendung setzt weiterhin das Routeninventar und die belegten Kantenfaktoren voraus.

## Wann eine Routenverfeinerung die Orientierung erhält

Seien $e:x\to y$ ein grober Teilweg und $p=e_k\cdots e_1$ seine vorgeschlagene Verfeinerung mit denselben vollständigen Endfeldern. Beide Wege mögen stetig und nichtnullartig sein. Mit gemeinsamen gerichteten Endreferenzen stimmen ihre Abbildungen auf dem orientierten Träger genau dann überein, wenn

$$
\epsilon_e=\prod_{i=1}^k\epsilon_{e_i}.
$$

Gleichwertig muss der geschlossene Vergleichsweg aus $p$ und dem inversen $e$ positive Parität haben. Es genügt nicht, dass jeder Teilweg für sich eine wohldefinierte Orientierung fortführt. Für eine Folge mehrerer Ersetzungen multiplizieren sich die Vergleichsvorzeichen. Die Bedingung ist unabhängig von den an den Zwischenknoten gewählten Vorzeichen.

Eine einfach prüfbare hinreichende Voraussetzung ist eine stetige Verformung von $p$ zu $e$ bei festen Endfeldern, auf der $s$ nirgends null wird. Die fortgeführten Phasen können dann keine Umlaufzahl ändern. Diese Voraussetzung ist stärker als nötig. Auch Wege, deren geschlossener Vergleich eine von null verschiedene gerade Umlaufzahl hat, tragen dieselbe Zielorientierung.

Im Sektorbeispiel kann man den unteren Weg als Ersatz für den oberen betrachten. Die Endfelder stimmen überein, aber der Vergleichskreis hat ungerade Umlaufzahl. Die Ersetzung ist deshalb für die ungerichtete Feldauslesung verträglich und verändert den gerichteten Rückweg. Für die native OP3-Schalenverfeinerung liefert dies eine konkrete zusätzliche Prüffrage, falls die Klasse Orientierung tragen soll. Die vorhandene Klassenbedingung allein liefert weder die Feldpfade noch deren Vergleichsparität.

## Ein Abstandsvergleich für die Orientierung bei Verfeinerung

Seien $s_{\rm grob}(t)$ und $s_{\rm fein}(t)$ die komplexen Invarianten zweier nichtnullartiger Feldwege mit denselben Endfeldern, parametrisiert auf demselben Intervall. Gilt für alle $t$

$$
|s_{\rm fein}(t)-s_{\rm grob}(t)|<|s_{\rm grob}(t)|,
$$

dann liegt der Quotient $s_{\rm fein}/s_{\rm grob}$ in der offenen Einheitskreisscheibe um $1$. Der Quotient beginnt und endet bei $1$ und hat Umlaufzahl null. Der verfeinerte Weg hat somit dieselbe relative Umlaufzahl und Orientierung wie der grobe Weg. Die Aussage benötigt nur eine Verformung der komplexen Auslesungen und behauptet keine Verformung durch zulässige native Feldwege.

Bei abgetasteten Daten kann man beide Wege durch ihre Messpolygone $P_{\rm grob},P_{\rm fein}$ ersetzen. Seien $D_{\rm grob},D_{\rm fein}$ garantierte gleichmäßige Abweichungsgrenzen zwischen Messpolygon und jeweiligem wahrem Verlauf. Eine hinreichende Bedingung ist

$$
\sup_t|P_{\rm fein}(t)-P_{\rm grob}(t)|+
D_{\rm fein}+2D_{\rm grob}<\inf_t|P_{\rm grob}(t)|.
$$

Dies folgt durch die Dreiecksungleichung im Zähler und die untere Schranke $|s_{\rm grob}|\ge|P_{\rm grob}|-D_{\rm grob}$. Beim früheren Feldkreis mit acht exakten Eckpunkten ist die minimale Polygonnorm $3\cos(\pi/8)$. Für zwei Messpolygone mit demselben Zeitraster und maximaler Punktabweichung $0{,}1$ von diesen Eckpunkten ist ihre Differenz höchstens $0{,}2$. Die grobe Polygonnorm ist mindestens $3\cos(\pi/8)-0{,}1$. Nimmt man für die wahren Kurven eine direkte Fehlergrenze $D_{\rm grob}=D_{\rm fein}=0{,}5$ an, ist die Ungleichung erfüllt. Diese Grenze ist eine zusätzliche Modellvorgabe für das Beispiel und wird nicht aus der früheren Lipschitz-Schranke abgeleitet.

Diese Prüfung ist hinreichend. Verletzt ein Paar die Schranke, kann die Vergleichsparität trotzdem gerade sein. Dann muss die Parität separat bestimmt oder die Synchronisierung der beiden Pfade genauer begründet werden.

## Phasenvergleich ohne gemeinsame Amplitudenkalibrierung

Für zwei synchronisierte nichtnullartige Wege mit denselben Endfeldern genügt es, wenn ihr Phasenquotient

$$
R(t)=\frac{s_{\rm fein}(t)}{|s_{\rm fein}(t)|}
     \frac{\overline{s_{\rm grob}(t)}}{|s_{\rm grob}(t)|}
$$

niemals $-1$ erreicht. Dann hat er einen stetigen Hauptwinkel in $(-\pi,\pi)$ und beginnt und endet bei $1$. Seine Umlaufzahl ist null. Die Beträge können unabhängig variieren, und getrennte positive Verstärkungen in den beiden Auslesungen fallen heraus. Die Bedingung ist hinreichend. Auch ein Verhältnis, das die negative reelle Richtung zeitweise erreicht, kann gerade Umlaufzahl haben.

Für Abtastwerte sei $\widehat R_j$ der aus zwei gemessenen komplexen Werten berechnete Phasenquotient. Sei $d_j$ sein Winkelabstand von $-1$, $\alpha_j$ eine Schranke für den kombinierten Winkelfehler beider Messungen und $V_j$ eine Schranke für die gesamte Änderung des fortgeführten relativen Winkels vom Abtastpunkt bis zu einem beliebigen Punkt des folgenden Intervalls. Gilt $d_j>\alpha_j+V_j$ an jedem linken Intervallende, kann der wahre Quotient auf keinem Intervall $-1$ erreichen. Die Winkelfehler können aus den separat begrenzten Restfehlern der Viernorm-Auslesungen wie zuvor berechnet und addiert werden.

Im lokalen Beispiel sei der grobe Weg $w_{\rm grob}(t)=w_0$ und der feine $w_{\rm fein}(t)=\sqrt{1+9\sin^2(\pi t)}\,w_0$. Die Endfelder stimmen überein. Der Quotient $s_{\rm fein}/s_{\rm grob}$ erreicht im Inneren den Wert $10$, sodass der frühere Abstandsvergleich scheitert. Der Phasenquotient ist aber konstant $1$ und die Achsenorientierung bleibt gleich. Die Verfeinerung ist eine gewählte Modellroute und keine behauptete native Schalenoperation.

## Der historische Schalenquotient ist reell

Die historische Definition bei Zeile 5722 setzt $\zeta_{\rm sh}=e_{\rm sh}/p_{\rm sh}$ aus zwei vorzeichenbehafteten reellen Beiträgen erster Ordnung zusammen. Sie unterscheidet positive und negative Quotienten. Der Quotient ist damit im geprüften historischen Modell keine komplexe Phase. Im Antiphasenkorridor bleibt er auf der negativen reellen Achse. Die komplexe Scheibe aus den Vergleichsmodellen ist eine Erweiterung, keine Eigenschaft dieser Definition.

Das liefert einen engeren möglichen Anschluss. Falls eine stetige und nullfreie Feldinvariante $s$ durch eine einwertige stetige Funktion allein des reellen Beitragspaars $(p_{\rm sh},e_{\rm sh})$ auf einer ganzen Antiphase-Komponente gegeben ist, hat jeder geschlossene Weg des Paars Umlaufzahl null in $s$. Für $0\le\rho<1$ ist die Komponente mit $p_{\rm sh}>0$ durch $-1-\rho\le e_{\rm sh}/p_{\rm sh}\le-1+\rho$ und $p_{\rm sh}>0$ beschrieben. Sie ist konvex. Dasselbe gilt für die Komponente mit $p_{\rm sh}<0$. Jeder geschlossene Weg lässt sich dort auf einen Punkt zusammenziehen, und die nullfreie Feldabbildung überträgt diese Verformung auf $s$.

Die Voraussetzung ist stärker als eine Feldzuordnung an den Endpunkten. Die Abbildung muss auf der gesamten Komponente definiert und nullfrei sein. Eine nur auf dem beobachteten Weg definierte Auslesung oder zusätzliche unabhängige komplexe Routendaten können Umläufe zulassen. Auch müssen die Beiträge selbst zurückkehren. Der Quotient allein belegt dies nicht. Die historische Definition liefert die reellen Eingaben, aber keine solche Feldabbildung. Für einen stetigen Wechsel zwischen den beiden Antiphase-Komponenten müsste die Route den Bereich mit $p_{\rm sh}\ne0$ verlassen.

## Schalenbeiträge sind Abweichungen vom exakten Schalenpunkt

In der [historischen Schalenrechnung](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L5505) misst $\delta_{\rm obs}$ die Phasenverschiebung der sichtbaren gegenüber der exakten Transportschale. $\eta_{\rm exp}$ misst ihre Abstandsdrift. Die Beiträge $p_{\rm sh}=A_{\rm sh}\delta_{\rm obs}$ und $e_{\rm sh}=B_{\rm sh}\eta_{\rm exp}$ stammen aus einer Taylorentwicklung der skalaren sichtbaren Restamplitude. Sie verschwinden beide am exakten Schalenpunkt. Der Quotient $e_{\rm sh}/p_{\rm sh}$ ist dort undefiniert, auch wenn er entlang eines antiphasierten Wegs gegen $-1$ läuft.

Das trennt zwei mögliche Feldwörterbücher. Eine homogene Kopplung $q$ vom Grad eins aus diesen Beiträgen, etwa die betrachtete lineare Kopplung oder die Wahl über $|g|$, lässt $q$ am exakten Schalenpunkt verschwinden. Bei beschränktem Feldquotienten erzwingt sie damit $s=0$. In unserem Wörterbuch mit festem positivem $\ell$ verschwindet dann sogar das gesamte Feld. Die historische Schalenrechnung sagt dagegen, dass die **Abweichung** von der exakten Schale verschwindet. Sie liefert keine Aussage über das Verschwinden eines elektromagnetischen Hintergrundfelds.

Falls die exakte Schale einem nichtnullartigen Hintergrund mit Invariante $s_0\ne0$ entsprechen soll, braucht die Feldzuordnung dort einen Hintergrundterm. Eine mögliche lokale Nachweispflicht wäre $|s(p,e)-s_0|\le C(|p|+|e|)$. Für $C(|p|+|e|)<|s_0|$ liegt der ganze Feldverlauf in einer Scheibe, die null ausschließt. Geschlossene Wege darin haben Umlaufzahl null. Die Schranke setzt eine eigenständig begründete Feldkopplung voraus. Sie kann nicht aus der Taylorentwicklung der sichtbaren Restamplitude übernommen werden.

## Kann die exakte Schale einen gemeinsamen HC-festen Hintergrund tragen?

Die historische Rechnung legt am exakten Schalenpunkt den Rest auf null fest, aber kein elektromagnetisches Hintergrundfeld. Prüfe daher als zusätzliche Modellannahme, dass ein einziger Hintergrund $w_0$ von $J_B$ festgehalten wird. Dann gilt $E_0=B_0$. Für ein nichtverschwindendes Hintergrundfeld folgt $s_0=2i|E_0|^2$ und $|s_0|=n_0>0$. Auf der Ebene der Invariante folgt bereits aus $s_0=-\bar s_0$, dass sie rein imaginär sein muss. Die stärkere Feldgleichung $J_Bw_0=w_0$ legt zusätzlich die positive imaginäre Richtung fest.

Eine Feldstörung $\Delta w$ erfüllt mit der hermiteschen Vektornorm

$$
|s(w_0+\Delta w)-s_0|
\le 2\|w_0\|\|\Delta w\|+\|\Delta w\|^2.
$$

Für diesen HC-festen Hintergrund genügt $\|\Delta w\|<(\sqrt2-1)\|w_0\|$, um die Abweichung strikt kleiner als $|s_0|$ zu halten. Dann meidet $s$ nicht nur null, sondern die gesamte reelle Achse. Geschlossene Wege in diesem Bereich erhalten die Orientierung, können aber keine reellen nichtnullartigen Sektoren als Endpunkte verbinden.

Soll ein nichtnullartiger reeller Hintergrund selbst den Sektorwechsel tragen, braucht das Modell stattdessen zwei durch $J_B$ gepaarte Hintergrundfelder. Ihre Invarianten sind $s_0$ und $-s_0$. Ein gemeinsamer HC-fester Hintergrund ist damit ein möglicher Ausgang für lokale Orientierungserhaltung, aber kein gemeinsamer reeller Sektorwert. Welche Hintergrundzuordnung der exakten Schale zukommt, bleibt in der historischen Quelle offen.

## Zwei HC-gepaarte Hintergrundprofile

Wähle $w_+=2e_x+i e_y$ und $w_-=J_Bw_+=e_y+2i e_x$. Die beiden exakten Modellschalen haben damit $s_+=3$ und $s_-=-3$, während ihre Schalenabweichungen null sind. Sei $V$ ein fester Feldvektor mit passender Kalibriereinheit. Eine affine Kopplung der reellen Schalenbeiträge $p,e$ ist

$$
W_+(p,e)=w_+ +pV+eJ_BV,\qquad
W_-(p,e)=w_- +pV+eJ_BV.
$$

Wegen der reellen Linearität von $J_B$ gilt $J_BW_+(p,e)=W_-(e,p)$ und umgekehrt. Die Gewinnvertauschung allein erzwingt diese Hintergrundzuordnung nicht. Hier wird der Profilwechsel ausdrücklich mitgeführt. Anders als bei der homogenen Kopplung entspricht $p=e=0$ einem nichtverschwindenden Feld.

Da $J_B$ die hermitesche Norm erhält, ist $\|\Delta w\|\le (|p|+|e|)\|V\|$. Gilt diese Schranke strikt kleiner als $\sqrt8-\sqrt5$, dann liegt $s(W_\pm)$ jeweils in einer offenen Scheibe mit Radius $3$ um $\pm3$. Innerhalb eines Profils haben geschlossene Wege Umlaufzahl null. Ein stetiger Feldweg vom einen zum anderen Hintergrund kann nicht vollständig in der Vereinigung der beiden disjunkten offenen Scheiben bleiben. Der deklarierte diskrete HC-Wechsel ist dagegen auch am exakten Schalenpunkt wohldefiniert.

Die Konstruktion liefert ein explizites Wörterbuch mit endlicher Störungsschranke. Die beiden Hintergründe und $V$ sind gewählte Modelldaten. Eine native Zuordnung müsste sie aus der exakten Transportschale und ihren Abweichungsrichtungen begründen. Die Rechnung liefert keinen nativen Nachweis für die Profilwahl oder einen kontinuierlichen Zwischenweg.

## Reeller Sektor unter affinen Schalenabweichungen

In der affinen Modellkopplung $W_\pm=w_\pm+pV+eJ_BV$ sei $V=X+iY\ne0$. Dann ist

$$
V\cdot J_BV=i\|V\|^2.
$$

Der gemischte Term in $\operatorname{Im}s(W_\pm)$ ist folglich $2pe\|V\|^2$. Die Imaginärteil-Auslesung ist ein quadratisches Polynom in den reellen Beiträgen $p,e$. Sie kann auf keinem offenen zweidimensionalen Bereich identisch null sein, sofern $V\ne0$. Die HC-Verträglichkeit des affinen Wörterbuchs allein hält also $s$ nicht reell.

Auf der exakten Antiphasenlinie $e=-p$ ist die Störung $p(V-J_BV)$. Sie hat entgegengesetzte elektrische und magnetische Anteile, sodass ihre bilineare Quadratform $-i\|V-J_BV\|^2$ ist. Soll $\operatorname{Im}s$ auf einem ganzen Intervall dieser Linie verschwinden, muss der quadratische Koeffizient null sein. Das erzwingt $V=J_BV$. In diesem Fall verschwindet die Störung auf der Antiphasenlinie vollständig und $s$ bleibt beim Hintergrundwert.

Damit kann das affine Modell kleine nichtnullartige Störungen tragen, aber keine nichttriviale reelle Variation entlang exakter Antiphase. Für diese stärkere Sektorbedingung wäre eine eingeschränkte Route oder eine nichtlineare Feldkopplung nötig. Der Befund betrifft das gewählte affine Wörterbuch mit demselben $V$ auf beiden Profilen.

## Reelle Variation mit profilabhängiger affiner Kopplung

Die vorige Schranke benutzt dieselbe Störungsabbildung in beiden Profilen. Erlaubt man eigene, durch HC miteinander verknüpfte Koeffizienten, genügt weiterhin eine affine Kopplung. In fest gewählten Feld- und Beitragseinheiten setze

$$
W_+(p,e)=(2+p)e_x+i(1+e)e_y,\qquad
W_-(p,e)=J_B W_+(e,p)=(1+p)e_y+i(2+e)e_x.
$$

Damit gilt $J_BW_+(p,e)=W_-(e,p)$ und umgekehrt. In beiden Profilen sind die elektrischen und magnetischen Vektoren orthogonal, daher bleiben beide Invarianten für reelle Beiträge reell. Auf der exakten Antiphasenlinie folgt

$$
s(W_+(p,-p))=3+6p,\qquad
s(W_-(p,-p))=-3+6p.
$$

Für $|p|<1/2$ bleiben die Sektoren getrennt und ihre Werte ändern sich nichttrivial. Beim HC-Wechsel wird zusätzlich $p$ mit $-p$ vertauscht. Deshalb ist der Zielwert exakt das Negative des Quellwerts. Auf dem offenen Rechteck $|p|,|e|<1/2$ bleiben die Vorzeichen ebenfalls erhalten, weil der große Feldbetrag stets über und der kleine unter $3/2$ liegt.

Die Konstruktion zeigt, welche Zusatzwahl gegenüber dem vorigen Modell ausreicht. Die beiden Schalenbeiträge werden in jedem Profil unterschiedlichen gerichteten Feldkomponenten zugeordnet. Die Zuordnung wird per HC zwischen den Profilen ausgetauscht. Die native Quelle müsste diese beiden Richtungen und die Profilabhängigkeit der Kalibrierung begründen. Das Modell setzt diese Daten ausdrücklich ein und verwendet keinen kontinuierlichen Sektorwechsel innerhalb der reellen nichtnullartigen Felder.

## Uhrfaktor entlang der exakten Antiphasenlinie

Im positiven affinen Profil gilt entlang $e=-p$ und $|p|<1/2$

$$
n=5+2p+2p^2,\qquad
r=\frac{3+6p}{5+2p+2p^2},\qquad
\beta_{\rm ref}=\frac{1-p}{2+p}.
$$

Für die HC-gepaarte Eingabe im negativen Profil sind $n$ und $r$ gleich. Der äußere kollineare Uhrfaktor ist $G=1/r=(1+\beta_{\rm ref}^2)/(1-\beta_{\rm ref}^2)$. Er nimmt mit $p$ strikt ab, da $\beta_{\rm ref}$ positiv ist und strikt abnimmt. Beim exakten Schalenpunkt $p=e=0$ liefert der gewählte Hintergrund $G=5/3$. Bei exakt antiphasierten Abweichungen mit $p\ne0$ ändert sich der Faktor, obwohl $e/p=-1$ bleibt.

Ein vorgegebenes $G$ im Wertebereich dieser lokalen Route bestimmt umgekehrt genau ein $p$. Aus $\beta=\sqrt{(G-1)/(G+1)}$ folgt $p=(1-2\beta)/(1+\beta)$. Für den nominalen r08-Wert $G=1{,}8647$ erhält man $p\approx-0{,}064$ in den gewählten Beitragseinheiten. Dies ist eine Anpassung an den vorgegebenen Faktor. Ein unabhängig bestimmter Schalenbeitrag würde stattdessen eine Vorhersage für $G$ liefern. Die Hintergrundfelder, ihre Kalibrierung und die Eingabe $p$ bleiben Modellannahmen.

## Kann der Schalenrest den Uhrfaktor auswählen?

Das [historische Schalenmodell](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L5517) zerlegt die sichtbare Restamplitude in $p+e$ und einen nach oben beschränkten Rest höherer Ordnung. Auf $e=-p$ ist $p+e=0$ für jeden $p$. Eine obere Restschranke allein wählt keinen Punkt der Antiphasenlinie aus. Sie erlaubt beispielsweise sowohl identisch verschwindenden Rest als auch einen quadratischen Rest.

Für eine konkrete glatte Route in den Beitragskoordinaten wäre ein separat berechneter Ausdruck $R(p,-p)=\kappa p^2+o(p^2)$ mit $\kappa\ne0$ ein neuer Nachweis. Dann gilt lokal $|R(p,-p)|\ge|\kappa|p^2/2$. Exakte Restnull würde lokal $p=0$ erzwingen und im gewählten affinen Feldmodell den Hintergrundwert $G=5/3$ liefern. Eine Restschwelle $|R|\le\varepsilon$ würde lokal $|p|\le\sqrt{2\varepsilon/|\kappa|}$ ergeben. Über die monotone Funktion $G(p)$ lässt sich daraus ein Uhrfaktorintervall bestimmen. Die historische Taylor-Schranke liefert weder $\kappa$ noch eine untere Schranke dieser Art.

Falls die Restfunktion unter Vertauschung der beiden Beiträge invariant ist, ist sie auf der Antiphasenlinie gerade in $p$. Dann können selbst exakte Restwerte $p$ und $-p$ nicht trennen. Bei festgehaltenem positiven Feldprofil liefern diese beiden Eingaben aber verschiedene $G(p)$. Eine vorzeichenbehaftete Beitragsauslesung oder eine zusätzliche Auswahlregel wäre dann nötig. Die Vertauschungsinvarianz ist hier eine bedingte Modellprüfung, keine aus der historischen Restabschätzung abgeleitete Eigenschaft.

## Quadratischer Schalenkoeffizient und gekrümmte Nullkurve

Die historische Quelle setzt eine glatte sichtbare Restamplitude $f(\delta,\eta)$ voraus und identifiziert ihre ersten Ableitungen $A,B$ am exakten Schalenpunkt. Für festgehaltenes Beobachterprofil und $AB\ne0$ sind die Beitragskoordinaten $p=A\delta$, $e=B\eta$. Der quadratische Koeffizient auf der exakten Antiphasenlinie ist

$$
\kappa=\tfrac12\left(\frac{f_{\delta\delta}}{A^2}
-\frac{2f_{\delta\eta}}{AB}+\frac{f_{\eta\eta}}{B^2}\right)_{(0,0)}.
$$

Der historische Beweis liefert eine Taylor-Schranke, aber keine Werte der drei zweiten Ableitungen in dieser Kombination. Beispielsweise besitzen $p+e$, $p+e+p^2$ und $p+e-p^2$ dieselbe lineare Auslesung und jeweils einen quadratisch beschränkten Rest. Sie realisieren $\kappa=0,+1,-1$.

Zudem ist zwischen exakter Antiphase und exakter sichtbarer Null zu unterscheiden. Mit $F(p,e)=f(p/A,e/B)$ gilt $\partial_eF(0,0)=1$. Der Satz über implizite Funktionen liefert daher nahe null eine exakte Nullkurve

$$
e(p)=-p-\kappa p^2+o(p^2).
$$

Selbst ein nachgewiesenes $\kappa\ne0$ würde also nur unter einer **unabhängig erzwungenen exakten Antiphasenlinie** $e=-p$ den Punkt $p=0$ auswählen. In einem Korridor um Antiphase liegt die gekrümmte Nullkurve für kleine $p\ne0$ weiterhin im Korridor, denn $e(p)/p\to-1$. Die sichtbare Restnull allein legt dann den Uhrfaktor nicht fest. Für diesen Schluss sind eine glatte zweidimensionale Auslesung und beide von null verschiedenen linearen Koeffizienten vorausgesetzt. Ob die gekrümmte Kurve auf einer konkreten nativen Route erreichbar ist, verlangt zusätzliche Zulassungsdaten.

## Quadratischer Rest auf einer Ein-Schalenkoordinaten-Route

Die [historische Ein-Schalenkoordinaten-Regel](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6006) koppelt beide Abweichungen an dieselbe Größe $\xi$. Bei festem Profil gibt sie $\delta=a\xi+O(\xi^2)$ und $\eta=b\xi+O(\xi^2)$ an. Exakte Balance der **linearen Gewinne** bedeutet $Aa=-Bb=g\ne0$. Das legt die Tangente der Beitragsroute fest, aber nicht deren Krümmung.

Falls die Route einen zweiten Jet besitzt, schreibe $p=g\xi+p_2\xi^2+o(\xi^2)$ und $e=-g\xi+e_2\xi^2+o(\xi^2)$. Mit dem zuvor definierten $\kappa$ folgt

$$
F(p(\xi),e(\xi))=(p_2+e_2+\kappa g^2)\xi^2+o(\xi^2).
$$

In der Koordinate $p$ ist also $\lambda=(p_2+e_2)/g^2$ die Krümmung der zugelassenen Route relativ zur geraden Antiphasenlinie. Der entscheidende Koeffizient lautet $\kappa+\lambda$, nicht $\kappa$ allein. Die exakte Nullkurve hat $\lambda=-\kappa$. Bei $\kappa+\lambda\ne0$ ist der exakte Schalenpunkt auf dieser Route lokal die einzige Restnull. Bei $\kappa+\lambda=0$ entscheidet die zweite Ordnung die Frage nicht.

Als Vergleichsmodelle seien $F=p+e+p^2$ und $g=1$ fest. Die Routen $(p,e)=(\xi,-\xi)$ und $(p,e)=(\xi,-\xi-\xi^2)$ haben dieselbe lineare Balance und erfüllen die historischen quadratischen Obergrenzen. Die erste liefert Rest $\xi^2$, die zweite exakte Restnull für jedes $\xi$. Die historische Ein-Schalenkoordinaten-Regel legt weder die Summe $p_2+e_2$ noch ihre Beziehung zu $\kappa$ fest. Die Modelle sind analytische Gegenbeispiele zur Ableitung einer eindeutigen Restnull aus der ersten Ordnung allein.

## Auch exakte Vertauschungssymmetrie lässt die Krümmung offen

Prüfe die stärkere Modellannahme $p(-\xi)=e(\xi)$ und $e(-\xi)=p(\xi)$ entlang der ganzen Route. Dann ist $U=(p+e)/2$ gerade in $\xi$ und $V=(p-e)/2$ ungerade. Der quadratische Term in $U$ darf trotzdem ungleich null sein. Bei einer zusätzlich vertauschungsinvarianten Restfunktion gilt $F(U,V)=F(U,-V)$. Auch das lässt einen Term proportional zu $V^2$ zu.

Als exaktes Gegenpaar setze $F(U,V)=2U+V^2$. Die beiden Routen

$$
(U,V)=(0,\xi)
\qquad\text{und}\qquad
(U,V)=(-\xi^2/2,\xi)
$$

erfüllen dieselbe exakte Vertauschungsregel und dieselbe lineare Antiphase. Die erste ergibt $F=\xi^2$. Die zweite ergibt $F=0$ für alle $\xi$. Die Krümmung des symmetrischen Gewinnanteils ist in der zweiten Route gerade so groß, dass sie den quadratischen Rest ausgleicht.

Die historische Vorzeichenbeziehung auf den Schalentangenten ist schwächer als diese exakte Symmetrieannahme. Selbst ihr stärkeres Gegenstück würde die Auswahl der Restnull daher nicht entscheiden. Dazu müsste die native Rechnung den geraden Anteil $U$ in zweiter Ordnung festlegen oder eine andere unabhängige Bedingung an die zugelassene Route liefern. Die Beispiele sind gewählte lokale Modelle.

## Welche quadratische Größe unabhängig von den Beitragskoordinaten ist

Schreibe die lokale Beitragsroute als $e=-p+\lambda p^2+o(p^2)$ und die Restfunktion auf der geraden Antiphasenlinie als $F(p,-p)=\kappa p^2+o(p^2)$. Betrachte bei unveränderter physikalischer Auslesung die Umparametrisierung $p'=p$, $e'=e+c p^2$. Sie ist lokal invertierbar und hat am Ursprung dieselbe erste Ordnung.

In den neuen Koordinaten hat die Route den Koeffizienten $\lambda'=\lambda+c$. Die neue Restfunktion lautet $F'(p',e')=F(p',e'-c(p')^2)$. Weil $\partial_e F(0,0)=1$, ergibt sich auf $e'=-p'$ der Koeffizient $\kappa'=\kappa-c$. Somit bleibt

$$
\kappa'+\lambda'=\kappa+\lambda.
$$

Mit $c=-\lambda$ lässt sich die zugelassene Route bis zur zweiten Ordnung gerade schreiben. Mit $c=\kappa$ lässt sich stattdessen die Nullkurve bis zur zweiten Ordnung gerade schreiben. Beide Geraden gleichzeitig zu erhalten ist genau bei $\kappa+\lambda=0$ möglich. Die einzeln angegebenen Koeffizienten hängen damit von der Beitragsdarstellung ab. Ihr gemeinsamer Koeffizient beschreibt den Kontakt der tatsächlichen Route mit der Nullkurve in der gewählten, hier unveränderten Koordinate $p$. Eine zusätzliche Umparametrisierung von $p$ skaliert seinen Zahlenwert quadratisch, lässt aber sein Verschwinden unverändert.

Für QAM sollte der Quellenvergleich deshalb die Auslesung auf der deklarierten Route mitsamt ihren Koordinaten prüfen. Eine unabhängig physikalisch definierte Bedingung $p+e=0$ muss beim Koordinatenwechsel mittransformiert werden. Sie darf nicht in beiden Darstellungen ohne Begründung als dieselbe Gerade eingesetzt werden.

## Quadratischen Rest direkt auf der Route auslesen

Sei $f(p)=F(p,e(p))$ die sichtbare Restamplitude entlang der deklarierten Route, mit $f(0)=f'(0)=0$. Für den gemeinsamen Koeffizienten $K=\kappa+\lambda=f''(0)/2$ genügt ein symmetrischer Vergleich:

$$
K_h=\frac{f(h)+f(-h)-2f(0)}{2h^2}.
$$

Falls $|f^{(4)}|\le M_4$ auf $[-h,h]$ gilt, folgt aus Taylorentwicklung $|K_h-K|\le M_4h^2/24$. Die ungeraden Terme fallen heraus. Haben die drei Restwerte garantierte Fehler $\delta_+,\delta_-,\delta_0$, ist für den aus gemessenen Werten berechneten Koeffizienten die gesamte Fehlerschranke

$$
|\widehat K_h-K|\le\frac{M_4 h^2}{24}
 +\frac{\delta_++\delta_-+2\delta_0}{2h^2}.
$$

Ein Intervall um $\widehat K_h$, das null ausschließt, belegt somit eine Trennung von Route und Restnull in zweiter Ordnung. Enthält es null, bleibt die Trennung mit diesen Daten offen. Die Methode erfordert Zugriff auf beide Seiten derselben zugelassenen Route und eine unabhängig begründete Glattheitsgrenze. Die historische quadratische Obergrenze für den Rest liefert keine Schranke für die vierte Ableitung.

Für die bisherigen exakten Vergleichsmodelle $F=2U+V^2$ mit $p=U+V$ kann man stattdessen die dort unmittelbar gegebene Routenkoordinate $\xi=V$ verwenden. Dann sind die Restprofile $\xi^2$ und $0$. Bei der gewählten Schrittweite $h=0{,}1$ liefern sie exakt $K_h=1$ und $K_h=0$ in dieser Koordinate. Mit je $10^{-4}$ Restfehler und $M_4=0$ ist die Koeffizientenschranke $0{,}02$. Das sind Modelldaten. Der Nachweis des Verschwindens oder Nichtverschwindens ist auch nach regulärem Wechsel der Routenkoordinate sinnvoll, während der Zahlenwert mit ihrer Kalibrierung skaliert.

## Von der Krümmungsschranke zur isolierten Restnull

Sei $f(0)=f'(0)=0$ exakt und liefere der symmetrische Vergleich eine abgesicherte Untergrenze $|K|\ge k_*>0$ für $K=f''(0)/2$. Ist $|f'''|\le M_3$ auf einem zugelassenen Intervall $[-R,R]$, gilt

$$
|f(p)|\ge p^2(k_*-M_3|p|/6).
$$

Für $|p|\le R_*=\min(R,3k_*/M_3)$ folgt $|f(p)|\ge k_*p^2/2$. Bei $M_3=0$ wird $R_*=R$ verwendet. In diesem Bereich ist der exakte Schalenpunkt die einzige Restnull. Für eine Restschwelle $|f(p)|\le\varepsilon$ gilt zusätzlich $|p|\le\sqrt{2\varepsilon/k_*}$. Die Aussage setzt voraus, dass der betreffende Zustand bereits im kontrollierten Routenintervall liegt.

Im exakten Vergleichsmodell $f(p)=p^2$ mit der vorigen Koeffizientenfehlerschranke $0{,}02$ liefert ein zentraler Schätzwert $1$ den zertifizierten Wert $k_*=0{,}98$. Mit der gewählten Restschwelle $\varepsilon=10^{-4}$ erhält man $|p|\le1/70$, sofern das betrachtete Intervall diesen Bereich enthält und $M_3=0$. Im gewählten affinen HC-Feldprofil ergibt die monotone Auslesung $G(p)=(5+2p+2p^2)/(3+6p)$ daraus das Intervall $[G(1/70),G(-1/70)]$. Die tatsächliche exakte Null dieses Modells liefert $G=5/3$. Die Schranke ist bewusst konservativ und die verwendeten Daten sind Modellwerte. Der native Schritt verlangt eine konkrete zulässige Restfunktion, einen von null getrennten Koeffizienten und eine eigene Ableitungsschranke.

## Was die historischen Restschranken tatsächlich entscheiden

Die geprüften historischen Abschnitte geben die sichtbare Auslesung nur durch ihre erste Taylorordnung und eine Restschranke an. Auch die Ein-Schalenkoordinaten-Regel beschränkt die Abweichungen von der linearen Route nur nach oben. In dieser Quellenkette ist daher kein Wert des gemeinsamen quadratischen Koeffizienten ausrechenbar. Aus den vorhandenen Schranken ergibt sich aber eine erste Ausschlussregel abseits exakter Gewinnbalance.

Bei festem Profil schreibe $\delta=a\xi+r_\delta$, $\eta=b\xi+r_\eta$ mit $|r_\delta|+|r_\eta|\le C_\xi|\xi|^2$. Setze $D=Aa+Bb$ und $L=|a|+|b|+C_\xi R$ auf $|\xi|\le R$. Die historische Auslesung $f=A\delta+B\eta+R_{\ge2}$ erfüllt dann

$$
|f(\xi)-D\xi|\le C_*|\xi|^2,\qquad
C_*=\max(|A|,|B|)C_\xi+C_{\rm sh}L^2.
$$

Für $D\ne0$ folgt $|f(\xi)|\ge |D||\xi|/2$ auf dem Teilintervall $C_*|\xi|\le |D|/2$. Dort ist $\xi=0$ die einzige Restnull. Diese Prüfung verwendet nur die bereits angegebene Struktur der historischen Obergrenzen und einen unabhängig nachgewiesenen von null verschiedenen Gewinnüberschuss. Sie verlangt keine Hesse-Matrix. Bei exakter Gewinnbalance $D=0$ fällt die untere Schranke weg, und die beiden schon konstruierten quadratischen Gegenmodelle bleiben möglich.

Damit hat das historische Material einen bedingten lokalen Ausschluss für nicht exakt balancierte Routen. Die quantitative Anwendung verlangt konkrete Werte oder garantierte Schranken für die Gains und Restkonstanten im selben Profil. Die Quelle liefert diese Daten in der geprüften Passage als Parameter, nicht als ausgewertete native Route.

## Einseitige Auslesung des quadratischen Rests

Ist nur der Weg $0\le\xi\le2h$ zugelassen, verwende

$$
K_h^{+}=\frac{f(2h)-2f(h)+f(0)}{2h^2}.
$$

Konstante und lineare Terme fallen heraus. Für $f\in C^3$ mit $|f'''|\le M_3$ gilt $|K_h^+-f''(0)/2|\le M_3h/2$. Dazu schreibt man die zweite Differenz als $\int_0^h\int_0^h f''(u+v)\,du\,dv$. Der Abstand von $f''(u+v)$ zu $f''(0)$ beträgt höchstens $M_3(u+v)$. Die zusätzliche Fehlerschranke für drei gemessene Restwerte ist $(\delta_2+2\delta_1+\delta_0)/(2h^2)$.

Für die zwei bisherigen Vergleichsrouten mit $f(\xi)=\xi^2$ beziehungsweise $f(\xi)=0$ liefert $h=1/10$ wieder die Werte $1$ und $0$. Bei $M_3=0$ und Einzelfehlern bis $10^{-4}$ ist die Fehlergrenze $0{,}02$. Ein von null getrennter Koeffizient isoliert den exakten Schalenpunkt auf der einseitigen Route nur zusammen mit der Bedingung $f'(0)=0$ und der Kontrolle höherer Ordnung. Die zweite Differenz selbst prüft die lineare Balance nicht.

## Linearer Gewinnüberschuss aus denselben einseitigen Daten

Aus denselben drei Werten bei $0,h,2h$ schätzt

$$
\widehat D_h^+=\frac{-3\widehat f(0)+4\widehat f(h)-\widehat f(2h)}{2h}
$$

den linearen Gewinnüberschuss $D=f'(0)$. Die Formel ist die Ableitung des quadratischen Interpolationspolynoms am linken Rand. Bei $|f'''|\le M_3$ und den zuvor benannten Einzelfehlern gilt

$$
|\widehat D_h^+-D|\le \frac{M_3h^2}{3}+
\frac{3\delta_0+4\delta_1+\delta_2}{2h}.
$$

Für exakte Werte erhält man die erste Schranke aus der Taylorformel mit Integralrest. Der Fehlerkern ist $-t+3t^2/(4h)$ für $0\le t\le h$ und $-(2h-t)^2/(4h)$ für $h\le t\le2h$. Er ist überall nichtpositiv und sein Betragsintegral beträgt $h^2/3$.

Für $h=1/10$, $M_3=0$ und Einzelfehler höchstens $10^{-4}$ beträgt die Fehlerschranke für $D$ höchstens $0{,}004$, gleichzeitig für $K$ höchstens $0{,}02$. Die gewählte Vergleichsroute $f(\xi)=0{,}01\xi+\xi^2$ liefert die zentralen Werte $D=0{,}01$ und $K=1$. Die beiden Intervalle schließen null aus. Bei $f(\xi)=\xi^2$ schließt nur das Krümmungsintervall null aus. Das lineare Intervall ist mit exakter Balance vereinbar, beweist sie aber nicht.

Damit können dieselben einseitigen Auslesungen einen linearen Überschuss belegen oder ihn unentschieden lassen. Für einen rein quadratischen Nullnachweis braucht man bei einem linearen Intervall um null weiterhin einen unabhängigen Nachweis exakter Balance oder eine gemeinsame Vorzeichenabschätzung für den Rest auf der zugelassenen Seite.

## Welche Restnull die einseitigen Daten offenlassen

Sei $f(0)=0$ exakt, $D\in[D_-,D_+]$, $K\ge k_*>0$ und $|f'''|\le M_3$ auf der zugelassenen Seite. Für $\xi>0$ folgt

$$
f(\xi)\ge \xi\bigl(D_-+k_*\xi-M_3\xi^2/6\bigr).
$$

Bei $D_-\ge0$ ist der Ursprung im Bereich $M_3\xi\le3k_*$ die einzige Restnull. Damit reicht auf dieser Seite ein abgesichertes nichtnegatives lineares Vorzeichen. Exakte Balance ist ein Spezialfall. Bei $D_-<0$ folgt im selben Bereich lediglich der Ausschluss weiterer Nullstellen für $\xi>2|D_-|/k_*$. Eine zusätzliche Null näher am Ursprung bleibt möglich.

Das zeigt ein konkretes Paar für die bisherigen Abtastwerte bei $0,1/10,1/5$. Die gemeldeten Werte seien $(0,1/100,1/25)$ mit Fehlergrenze $10^{-4}$. Sowohl $f_1(\xi)=\xi^2$ als auch

$$
f_2(\xi)=-\xi/1000+(201/200)\xi^2
$$

sind damit vereinbar. Beide stimmen am Ursprung und bei $1/5$ exakt mit dem Bericht überein. Bei $1/10$ weicht $f_2$ um $-1/20000$ ab. Beide Krümmungen sind positiv und beide dritten Ableitungen verschwinden. Dennoch hat $f_2$ zusätzlich die positive Nullstelle $2/2010=1/1005$. Ein positives Krümmungsintervall allein kann also selbst bei diesen drei gemeinsamen Rohwerten die zusätzliche Null nicht ausschließen.

Die Schranke nutzt nur die getrennten Koeffizientenintervalle und kann daher konservativ sein. Das Gegenbeispiel verwendet dagegen die ursprünglichen drei Datenintervalle direkt. Es zeigt, warum QAM für einen eindeutigen Nullnachweis ein abgesichertes lineares Vorzeichen oder einen unabhängigen Balancenachweis mitführen muss.

## Scharfer Nullstellenbereich aus gemeinsamen Rohdaten

Beschränke die Rechnung auf exakt quadratische Restfunktionen $f(\xi)=D\xi+K\xi^2$ mit exakt bekanntem $f(0)=0$. Setze $y_1=f(h)$ und $y_2=f(2h)$. Aus beiden Rohwerten folgt

$$
D=\frac{4y_1-y_2}{2h},\qquad K=\frac{y_2-2y_1}{2h^2}.
$$

Für die bisherigen Intervalle $y_1\in[0{,}0099,0{,}0101]$, $y_2\in[0{,}0399,0{,}0401]$ ist $K>0$ auf dem ganzen Rechteck. Eine zweite positive Null existiert genau bei $y_2>4y_1$ und liegt dann bei

$$
\xi_*=-D/K=h\,\frac{y_2-4y_1}{y_2-2y_1}.
$$

Für positive $y_1,y_2$ und positiven Nenner wächst dieser Ausdruck mit $y_2$ und fällt mit $y_1$. Der maximale Wert liegt daher bei $y_1=0{,}0099$ und $y_2=0{,}0401$. Mit $h=1/10$ ergibt sich $\xi_*^{\max}=1/406$. Diese Ecke liefert $D=-1/400$ und $K=203/200$ und erreicht die Grenze tatsächlich. Im Rechteck sind auch $D=0$ und $D>0$ möglich. Durch Stetigkeit zwischen der Maximalecke und einem Punkt mit $D=0$ ist jeder Wert in $(0,1/406]$ erreichbar.

Damit sind für diese Rohdaten im exakt quadratischen Modell weitere positive Nullstellen oberhalb von $1/406$ ausgeschlossen. Der Bereich nutzt die Kopplung der aus denselben Messungen abgeleiteten Koeffizienten. Für allgemeine glatte Reste mit höherer Ordnung gilt diese scharfe Grenze erst nach einer erneuten Fehlerfortpflanzung. Die Intervallwerte sind gewählte Modelldaten.

## Zweite Restnull mit beschränkter höherer Ordnung

Sei $f(0)=0$ exakt und $f\in C^3[0,2h]$ mit $|f'''|\le M_3$. Für $0<\xi<h$ lautet das Interpolationspolynom durch die exakten Werte $y_1,y_2$:

$$
P_2(\xi)=\frac{\xi(2h-\xi)}{h^2}y_1+
         \frac{\xi(\xi-h)}{2h^2}y_2.
$$

Auf diesem Intervall ist der erste Koeffizient positiv, der zweite negativ. Die kleinste zulässige Polynomkurve verwendet also die untere Grenze für $y_1$ und die obere für $y_2$. Der Interpolationsrest ist durch $M_3\,\xi(h-\xi)(2h-\xi)/6$ beschränkt. Mit den bisherigen Intervallen und $h=1/10$ folgt

$$
f(\xi)\ge \xi\left[-0{,}0025+1{,}015\xi
 -\frac{M_3}{6}(0{,}1-\xi)(0{,}2-\xi)\right].
$$

Die Klammer wächst strikt auf $[0,h]$. Für die zusätzliche Modellannahme $M_3=0{,}1$ liegt ihre einzige Null bei etwa $0{,}002777904$. Damit gibt es zwischen dieser Grenze und dem ersten Abtastpunkt keine weitere Null. Die Grenze ist für diese Datenklasse scharf: Das Polynom der extremalen Ecke minus $(M_3/6)\xi(\xi-h)(\xi-2h)$ hat dieselben Knotenwerte, erreicht die untere Schranke auf $[0,h]$ und hat dritte Ableitung $-M_3$.

Auf $[h,2h]$ sind beide Interpolationsgewichte nichtnegativ und ihre Summe ist mindestens eins. Der Polynomwert beträgt daher mindestens $0{,}0099$. Der Rest ist auf diesem Intervall kleiner als oder gleich $(M_3/6)2h^3$. Mit dem gewählten $M_3$ bleibt $f$ somit auch dort strikt positiv. Für $M_3=0$ liefert die Rechnung die frühere Grenze $1/406$. Die Abschätzung setzt eine unabhängig begründete Ableitungsschranke auf der ganzen Strecke voraus und benutzt weiterhin gewählte Modelldaten.

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
