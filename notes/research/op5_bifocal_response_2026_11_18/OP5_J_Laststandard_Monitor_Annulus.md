# OP5 – Selektive J-Last, Direktpfadmonitor und glatter Annulus

21. November 2026. Analytische Erkundungen im Materieframe M. Aufbauend auf der [J-Terminierung, Echokontrolle und Ringrechnung](OP5_J_Terminierung_Echo_Radialraster.md) werden die erreichbare J-Last, die Beobachtbarkeit eines ungeschalteten Rücklaufs und die Dichtevariation der gewöhnlichen Kontrolle geprüft. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur lokalen Auslese. I3 braucht eine eigenständige kosmologische Bestandsdynamik.

## Zwei elektrische Antriebe ergeben noch keine selektive J-Last

Der [H/HCl-Nullport](OP5_J_Optischer_Nullport_Echo_Achsensaeule.md) addiert zwei gesteuerte Quellvektoren. Eine passive Last bildet dagegen eine einfallende Welle auf eine auslaufende ab. Im linear additiven Vergleich auf einer gemeinsamen Ebene liefert ein materieller Kontakt mit reeller normierter Richtung $v_i=(1,r_i)^{\mathsf T}/\sqrt{1+r_i^2}$ eine Rang-eins-Antwort $c_i v_i v_i^{\mathsf T}$. Die komplexen $c_i$ tragen den jeweils kalibrierten Antwortfaktor. Die Rechnung setzt dieselbe $A,J$-Flussbasis, festes Material und vernachlässigbare Mehrfachkopplung zwischen den Kontakten voraus.

Mit zwei verschiedenen $r_i$ müssen für eine reine J-Last zugleich $\sum c_i/(1+r_i^2)=0$ und $\sum c_i r_i/(1+r_i^2)=0$ gelten. Das lineare System hat nur die Nullantwort. Das gilt auch für komplexe Antwortfaktoren. Die A-Auslöschung einer gesteuerten Quelle beweist deshalb keine entsprechende J-selektive Terminierung durch dieselben zwei Kontakte.

Mit drei verschiedenen reellen Richtungen in diesem Modell erhält man $\gamma P_J$, wenn
$$
c_i=\gamma\,\frac{1+r_i^2}{(r_i-r_j)(r_i-r_k)},
\qquad\{i,j,k\}=\{0,1,2\}.
$$
Die ersten beiden Momente verschwinden, der quadratische Moment ist $\gamma$. Diese Koeffizienten brauchen abgestimmte komplexe Antworten mit geeigneten relativen Vorzeichen. Die algebraische Konstruktion beweist ihre gleichzeitige passive Realisierbarkeit nicht. Schon mit der sehr großzügigen Einzelgrenze $|c_i|\le1$ fällt der erreichbare J-Lastbetrag quadratisch mit dem Winkelabstand der Kontakte.

Für den idealen A-Standard $r_0=0$ und die beiden illustrativen H/HCl-Fälle bei $|g_J/e|=10^{-3}$ ergibt die Obergrenze für $|\gamma|$ die beiden Werte $1{,}5354\cdot10^{-6}$ und $2{,}5316\cdot10^{-6}$. Das ist um mehrere Größenordnungen kleiner als die illustrative Last $0{,}5$ der vorangegangenen kohärenten Terminierungsrechnung. Für $|t|=0{,}003$ und ein Prozent komplexen Einwegfehler liegt die maximal verfügbare additive A-Reflexionsgenauigkeit je Lastzustand im Bereich weniger $10^{-13}$, selbst ohne zusätzliche Systematik. Die Rechnung folgt aus der Division durch $\gamma$ in der antisymmetrischen Messung. Ein nichtlinear gekoppelter Konverter, ein aktiv abgeglichener Port oder weit auseinanderliegende physische Feldrichtungen würden eine andere Konstruktion erfordern. Eine gemessene kalibrierte J-Last oder native Kopplung folgt aus diesem Modell nicht.

## Was der Direktpfadmonitor über den ungeschalteten Rest aussagt

Bei einem schaltbaren Rücklauf $W$ und festem Rücklauf $V$ faktorisiert die vorige Extrapolation mit $L=(I-V)^{-1}$ als $H_a=C(I-aLW)^{-1}LD$. Die Extrapolation schätzt $B_V=CLD$ mit absolutem Fehler $\epsilon_E$. Ein separat kalibrierter kohärenter Monitor für den nackten Direktpfad $B_0=CD$ schätzt diesen mit Fehler $\epsilon_M$ in denselben Phasen- und Amplitudeneinheiten. Für skalare Daten gilt dann
$$
\frac{|B_V-B_0|}{|B_0|}
\le
\frac{|\widehat E-\widehat M|+\epsilon_E+\epsilon_M}
     {|\widehat M|-\epsilon_M}
$$
bei positivem Nenner. Der Monitor muss $V$ tatsächlich ausschließen oder dessen Einfluss unabhängig kennen. Gleichzeitige Wiederholung desselben Projektionspfads kann einen unbeobachteten konstanten Faktor nicht begrenzen.

Für das frühere Achtphasenbudget $6\cdot10^{-6}$ rad ist der zulässige gesamte Feldrest je Rohwert $\sin(6\cdot10^{-6}/8)$. Sind die Extrapolationsfehler in denselben $|B_0|$-Einheiten durch $3{,}33466\cdot10^{-7}$ begrenzt, bleiben etwa $4{,}16534\cdot10^{-7}$ für den sichtbaren festen Rücklauf. Bei $|\widehat M|=1$, $\epsilon_M\le5\cdot10^{-8}$ und entsprechendem absolutem Extrapolationsfehler genügt als Anzeigegrenze für die getrennte Restprüfung $|\widehat E-\widehat M|\le3{,}3068\cdot10^{-8}$. Soll ausschließlich der korrigierte Feldwert $\widehat E$ gegen $B_0$ abgesichert werden, ist die direkte Schranke $|\widehat E-\widehat M|+\epsilon_M$ anwendbar. Der Extrapolationsfehler darf dann nicht nochmals budgetiert werden.

Die skalare Prüfung erfasst einen projizierten Eintrag. Beispielsweise bleibt $V=\operatorname{diag}(0,v)$ für $C=(1,0)$ und $D=(1,0)^{\mathsf T}$ unsichtbar. Bei vollständigen kalibrierten invertierbaren Ports liefert dagegen $Z=C^{-1}(B_V-B_0)D^{-1}=L-I$. Für $\|Z\|<1$ folgt $\|V\|\le\|Z\|/(1-\|Z\|)$. Schlechte Portkondition verstärkt die Messunsicherheit in $Z$. Für das skalare Rohphasenbudget genügt die tatsächlich verwendete Projektion; eine volle Normzertifizierung braucht zusätzliche Information.

## Ein kompensierter Übergangsring mit zertifizierten Ableitungen

Setze $u=r^2/R_c^2$, $H=u\partial_u^2+\partial_u$ und $D_\perp=4H/R_c^2$. Als explizite gewöhnliche Kontrolle der [Achsensäule](OP5_J_Optischer_Nullport_Echo_Achsensaeule.md) kann in $\bar V_C=P_zc_4 f(u)$ der Ansatz
$$
f(u)=\tfrac15\partial_u\bigl(u^5\chi(u)\bigr)
$$
verwendet werden. Er liefert $f=u^4$ im Kern und Null-Quermoment, sobald $\chi$ vor der Außenreferenz verschwindet. Im Übergang auf $u\in[1/4,3/4]$ sei $x=2u-1/2$ und
$$
\chi(u)=\sum_{j=0}^{12}\binom{25}{j}x^j(1-x)^{25-j}.
$$
Der Ansatz wird davor mit eins und danach mit null fortgesetzt. Die ersten zwölf Ableitungen des Übergangspolynoms verschwinden an beiden Enden. Damit ist $f$ mindestens $C^{11}$, was für den betrachteten Dichte-Lipschitzfehler ausreicht. Für eine beliebig oft differenzierbare Variante kann $\chi$ mit einem glatten nichtnegativen normierten Kern gefaltet werden, sofern Platz für Plateau und Träger bleibt. Die Ableitungsschranken der geglätteten Abschneidefunktion werden durch das Falten nicht vergrößert. Der Nullmomentbeweis bleibt wegen des Ansatzes als Ableitung erhalten; konkrete scharfe Ringgrenzen wären für das geglättete $f$ neu auszuwerten.

Im gewöhnlichen [Binnenfeldmodell](OP5_J_Binnenfeld_Messweg.md) gilt nach Längsintegration
$$
\sigma(u)=-v_{\rm H}\zeta P_zc_4
\left[b_0(4/R_c^2)^3H^3-b_2(4/R_c^2)^4H^4+b_4(4/R_c^2)^5H^5\right] f(u).
$$
Deshalb liefert die Summe der drei Beträge mit $\sup|(H^m f)'|$ eine physikalisch skalierte Lipschitzgrenze. Auf dem Kern sind diese Ableitungen für $m=3,4,5$ genau $576,0,0$. Wolfram begrenzte die Ableitungspolynome im Übergang durch ihre exakten Bernstein-Koeffizienten auf 32 Teilintervallen. Die konservativ aufgerundeten Supremumsgrenzen sind $4{,}77934\cdot10^8$, $1{,}06473\cdot10^{12}$ und $5{,}44565\cdot10^{15}$. Sie sind Schranken für diesen konkreten Entwurf und keine analytischen Untergrenzen für einen beliebigen Übergang. Der Modellträger endet vor $u=1$. Endliche äußere Potentialreferenz und longitudinale Endterme müssen trotzdem aus der tatsächlichen Messung begrenzt werden.

Die globale normierte Ringabschätzung aus der Vorarbeit liefert damit allein keine brauchbare relative $b_4$-Genauigkeit für diesen Entwurf. Schon für den isolierten $b_4$-Anteil wäre die relative Formschranke $(\sup|(H^5f)'|/576)\sum_i B(a_i,b_i)$. Die Ableitung ist im Kern null und im Übergang groß. Eine stückweise Abschätzung $\sum_i L_i B(a_i,b_i)$ mit Ringgrenzen an den Übergangsgrenzen oder ein weniger steiler Entwurf sind die direkten nächsten Prüfwege. Das formale Profil setzt keine physische Ansteuerbarkeit voraus. Freie J-Ausbreitung, reale HCl/H-Anschlüsse, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram kontrollierte die additive Last-Algebra, den sichtbaren Rücklaufrest, die Endjets und die annularen Bernstein-Grenzen. Qiskit wurde für diese klassischen Streu- und Potentialrechnungen erwogen.

[Wolfram-Skript](op5_j_laststandard_monitor_annulus.wl) · [Tatsächliche Ausgabe](op5_j_laststandard_monitor_annulus.txt) · [Laufmanifest](op5_j_laststandard_monitor_annulus.json)
