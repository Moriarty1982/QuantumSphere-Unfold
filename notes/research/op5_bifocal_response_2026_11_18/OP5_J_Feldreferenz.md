# OP5 – Rang-eins-Feldreferenz und zeitgleiche Nullkontrolle

21. November 2026. Analytische Erkundung im Materieframe M. Die Vorarbeit zur [Modenzuordnung](OP5_J_Modenzuordnung.md) setzte eine ideale Feldmarkierung voraus. Hier wird geprüft, welche schwächere Referenz genügt, welche Information die HCl/H-Richtungen liefern und wie das Zweilaufbudget auf zwei gleichzeitig benötigte Matrixquotienten verteilt werden kann.

## Vorwissen geprüft

[HCl/H](OP5_J_HCl_Vektoranschluss.md) liefert im Dipolmodell zwei normierbare Richtungen und für jede isolierte Antwort eine Rang-eins-Suszeptibilität. Die [Anschlusskondition](OP5_J_HCl_Anschlusskondition.md) beschreibt die davon verschiedene Frage nach dem kleinsten Signalgewinn der zweispaltigen Anschlüsse. Das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) gibt die Restnorm bei Anschlussdrift. Die [Zweilauf-Kalibrierung](OP5_J_Zweilauf_Kalibrierung.md) gibt das aggregierte Laufzeitbudget. Die Suche nach Feldmarkierung, selektiver Phase und Rang-eins-Referenz ergab keine Auswertung der HCl/H-Gewichte für diese Kombination. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft sie die lokale Auslese. I3 benötigt eine eigene kosmologische Bestandsdynamik.

## Eine schiefe Rang-eins-Markierung genügt

Arbeitshypothese ist eine separat schaltbare, kalibrierte Vorwärtstransmission $T=I+\beta P$, mit $P=vv^\dagger$ für eine normierte Feldrichtung $v$ und bekanntem komplexen $\beta\ne0$. Für die feste kanonische Modenbasis $(J,A)$ seien $w=|v_J|^2$ und $1-w=|v_A|^2$. Nimm den diagonalen Solltransport $U=\operatorname{diag}(z_J,z_A)$ und die kohärent referenzierten Matrizen
$$
N=LF,\qquad M=L U F,\qquad M_T=L T F .
$$
Mit $Q=N^{-1}M$, $Q_T=N^{-1}M_T$ sind die zwei Spuren
$$
a=\operatorname{tr}Q=z_J+z_A,\qquad
b=\beta^{-1}\operatorname{tr}[(Q_T-I)Q]
 = w z_J+(1-w)z_A .
$$
Daraus folgt bei $d=1-2w\ne0$
$$
z_J=\frac{(1-w)a-b}{d},\qquad
z_A=\frac{b-wa}{d}.
$$
Die Markierung darf mit $U$ nicht kommutieren. Die Spur nutzt die Diagonale von $P$, weil $U$ diagonal angenommen ist. Die Rekonstruktion hängt von der Gewichtstrennung $|d|$ und vom komplexen Markierungshub $|\beta|$ ab. Sie ist an einer Koinzidenz von $z_J$ und $z_A$ regulär. Bei nichtdiagonalem Solltransport wären zusätzliche Observablen für die tatsächlichen Moden nötig.

Die gewöhnliche selektive Vorwärtstransmission $T=\operatorname{diag}(1,1+\beta)$ wäre ein Spezialfall mit $w=0$, sofern sie tatsächlich in der Feldbasis zwischen Sender und Empfänger wirkt. Ein Schalter in den Gerätekoordinaten vor $F$ liefert dagegen den Quotienten des bekannten Geräteschalters. Daraus allein folgt keine Feldzuordnung. Auch der Nachweis von Rang eins und der Wert $\beta=\operatorname{tr}(Q_T-I)$ bestimmen $w$ in einer unbekannten Feldbasis noch nicht.

## Was das HCl/H-Modell beiträgt

Im diagonalen Kinetikvergleich der Vorarbeit gilt für eine Dipolrichtung $(r,1)$ bis auf Normierung
$$
w=\frac{|r|^2}{1+|r|^2},\qquad
d=\frac{1-|r|^2}{1+|r|^2}.
$$
Für das dort nur illustrativ angesetzte $|g_J/e|=10^{-3}$ ergeben die H-Richtung und die beiden HCl-Vorzeichenfälle $d$ von rund $0{,}9999980$, $0{,}9999953$ und $0{,}9999750$. Eine einzelne solche Richtung ist für markierte Spuren geometrisch gut getrennt. Die gute Gewichtstrennung hebt die kleine Winkeldifferenz der beiden Anschlussvektoren und die entsprechend kleine Anschluss-Singulärzahl nicht auf.

Bei kontrollierter Änderung einer isolierten Suszeptibilität liefert ihre Rang-eins-Form $P$ als Kandidat für den ersten Term der Vorwärtsantwort **in der Feldstrecke**. Eine gemessene Dipol-Linienstärke bestimmt den vollständigen komplexen Vorwärtshub $\beta$ und die tatsächlich propagierenden Feldprojektionen noch nicht. Der Vergleich setzt gemeinsame Moden, einen auf diese Moden bezogenen Richtungsabgleich und eine gemessene kohärente Vorwärtstransmission voraus. Ein endlicher Hub $|\beta|=2$ wird hier als starker Vergleichswert verwendet. Eine Rang-eins-Suszeptibilität allein garantiert diesen Hub, geringe Reflexion und Erhalt des räumlichen Modenprofils nicht. [Kohärente Schichtantwort in schwacher Anregung, Vergleich zur konventionellen Optik](https://doi.org/10.1103/PhysRevA.104.033702)

## Zeitgleiche Null und ihr Fehler

Schreibe in einem Zeitblock $N(t)=L(t)F(t)$, $M(t)=L(t)UF(t)$ und $M_T(t)=L(t)TF(t)$. In beiden Quotienten tritt dann dieselbe Ähnlichkeit mit $F(t)$ auf. Gemeinsame zeitabhängige Anschlussfaktoren kürzen sich in den Spuren exakt. Entscheidend ist die Gleichheit der Faktoren in den drei Messungen und eine kohärente Phasenreferenz. Ein separater Kontrollweg muss dieselben aktuellen Anschlüsse tatsächlich abbilden. Signalgebundene Abweichungen von der Nullreferenz bleiben im jeweiligen Matrixrest.

Seien $r_Q,r_T$ verfügbare Schranken für die Fehler der Quotienten in der Referenz-Feldbasis. Setze
$$
r_P=\frac{r_T+|\widehat\beta-\beta|}{|\widehat\beta|}
$$
als Schranke für den Fehler des aus $(\widehat Q_T-I)/\widehat\beta$ rekonstruierten Projektors, nach Aufnahme einer Abweichung vom Rang-eins-Modell in den Zielmatrixrest. Bei kalibriertem $\widehat w\in[0,1]$ mit $\widehat d=1-2\widehat w\ne0$ genügt für jeden rekonstruierten komplexen Wert
$$
e_z=
\frac{r_Q+2r_P(1+r_Q)+|\widehat w-w|\,|z_J-z_A|}{|\widehat d|}.
$$
Die Operatoren $(1-\widehat w)I-P$ und $P-\widehat w I$ haben jeweils Spurnorm eins. Die zusätzliche Projektormessung tritt über die Spur eines Produkts zweier $2\times2$-Matrizen ein. Ein Gewichtsfehler allein wirkt mit dem wahren komplexen Modenabstand. Größere Matrixfehler wirken auch am entarteten Punkt. Für $e_z<1$ lässt sich das Phasenbudget mit $\arcsin e_z$ je Modus und Bandende führen wie bei der idealen Markierung.

Für $X=Q,T$ bezeichne $V_X=U,T$ die jeweilige ideale Feldmatrix, und setze $v_X=\|V_X\|_2$. Bei normierten Gerätefehlern $\epsilon_0,\epsilon_X$, dem Anschlussprodukt $p>\epsilon_0$ und einem additiven Feldrest $D_X$ durch nichtgemeinsame Anschlüsse gilt
$$
r_X=\frac{\epsilon_X+v_X\epsilon_0+p\|D_X\|_2}{p-\epsilon_0}.
$$
Wenn die Abweichungen der Anschlüsse in Feldkoordinaten multiplikativ mit Normen höchstens $d_L,d_R$ vorliegen, genügt $\|D_X\|_2\le v_X(d_L+d_R+d_Ld_R)$. Damit lässt sich eine erlaubte Nichtübereinstimmung der jeweils zeitgleichen Null aus einem vorgegebenen $r_X$ berechnen. Gemeinsame Drift darf größer sein, solange $p$ im zertifizierten Bereich bleibt. Diese Aussage setzt schon bestehende und kohärente Zugänge zu Signal, Markierung und Null voraus.

## Zahlenbeispiel aus dem Zweilaufbudget

Bei den bisherigen illustrativen $100$ MHz Bandabstand und $0{,}25$ ps Gesamtfehler, Kalibrierfaktor eins und gleichen Fehlergrenzen je Lauf und Bandende ist der zulässige Radius je markiertem Modalwert $e_z\le1{,}9635\cdot10^{-5}$ für phasenstetig zugeordnete Moden. Bei exakt bekannten $\beta,w$, $d$ nahe eins und $r_Q=r_T=r$ genügt $r+2r(1+r)/|\beta|\le e_z$. Für den starken Vergleich $|\beta|=2$ ergibt sich $r\lesssim9{,}82\cdot10^{-6}$, für $|\beta|=0{,}1$ rund $9{,}35\cdot10^{-7}$. Im starken verlustfreien Vergleich und bei je $10^{-8}$ additivem Fehler pro Matrix, driftfreien Enden und gleichen Anschlussstärken folgt pro Ende eine kleinste Singulärzahl von mindestens etwa $0{,}0451$. Bei der früheren idealisierten Anschlussstärke $0{,}00254$ entspräche dies höchstens rund $3{,}17\cdot10^{-11}$ additivem Fehler je Matrix. Die Rechnung verteilt das gesamte Budget auf die markierte Matrixauslese. Ausrichtungsfehler, Profilrest und ungleiche zeitgleiche Referenzen benötigen davon einen eigenen Anteil.

Ein realer Versuch braucht folglich neben den bisherigen zwei Anschlüssen eine im Feldraum nachgewiesene Vorwärtsreferenz und die gemessene Nichtübereinstimmung ihrer Nullkontrolle. Die HCl/H-Rechnung gibt günstige illustrative Diagonalgewichte, belegt aber weder den erforderlichen komplexen Hub noch freie J-Ausbreitung, native Kopplung oder H96.

## Rechenkontrolle

[Wolfram-Skript](op5_j_feldreferenz.wl) · [Tatsächliche Ausgabe](op5_j_feldreferenz.txt) · [Laufmanifest](op5_j_feldreferenz.json)

Wolfram kontrollierte die Rekonstruktion, den Beitrag eines falschen Richtungsgewichts und die Spuren für eine gemeinsame nichtdiagonale Anschlussänderung. Die Vergleichszahlen wurden aus exakten Eingaben gerundet. Reproduzierbar mit **wolframscript -file op5_j_feldreferenz.wl**.
