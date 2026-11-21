# OP5 – A-Leistungsbilanz, Fourier-Echokanäle und radiale Ringmessung

21. November 2026. Analytische Erkundungen im Materieframe M. Aus dem [optischen Nullport und dem Säulenvergleich](OP5_J_Optischer_Nullport_Echo_Achsensaeule.md) bleiben die absolute J-Skala, gerade und unmarkierte Echos sowie die diskrete Dichteerfassung offen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betreffen alle drei Rechnungen die lokale Auslese. I3 erfordert eine eigenständige kosmologische Bestandsdynamik.

## Wie viel eine A-Leistungsbilanz über J bestimmt

Seien $S_{AA}$ und $S_{JA}$ die auslaufenden A- und J-Feldamplituden in Abhängigkeit von den einfallenden A-Amplituden. Beide Richtungen und Seiten werden in einer gemeinsamen physikalischen Flussnorm gezählt. Bei Passivität gilt
$$
I-S_{AA}^\dagger S_{AA}=S_{JA}^\dagger S_{JA}+\Lambda,\qquad\Lambda\ge0 .
$$
$\Lambda$ enthält Absorption und weitere ungemessene Ausgänge außerhalb der bilanzierten J-Ports. Selbst mit kohärenter vollständiger A-Matrix liefern die A-Daten ohne unabhängige Verlustgrenze nur die Summe auf der rechten Seite. Bei nachgewiesener Verlustfreiheit liefert die A-Messung die Gram-Matrix der J-Ausgänge. Unitäre Mischung der ungemessenen Ausgänge ändert diese Gram-Matrix nicht. Die Phase und die Zuordnung zu einem bestimmten J-Ausgang bleiben daher offen. Ein separat abgeglichener Zustand mit nur einem möglichen J-Ausgang lässt dessen Amplitudenbetrag zu.

Bezeichne $\widehat p$ als gemessene Differenz zwischen einfallender und auslaufender A-Leistung bei normiertem Eingang. Sei $\delta_p$ ihr absoluter Fehler, $\lambda_{\max}$ die unabhängige Obergrenze für sonstige Verlustleistung und $P_{\rm sonst,J}$ die Grenze für alle J-Ausgänge außer dem Zielport. Für dessen normierte Amplitude $t_J$ gilt
$$
\max(0,\widehat p-\delta_p-\lambda_{\max}-P_{\rm sonst,J})
\le |t_J|^2\le\widehat p+\delta_p .
$$
Wird der Zielbetrag von einer bekannten Modellmitte aus mit ein Prozent relativer Genauigkeit gesucht, ist für die symmetrische Leistungsunsicherheit das engere Intervall $|t_J|^2-(0{,}99|t_J|)^2$ maßgeblich. Es beträgt für $|t_J|=0{,}003$ rund $1{,}791\cdot10^{-7}$ und für $|t_J|=10^{-6}$ nur $1{,}99\cdot10^{-14}$. Hinzu kommen unabhängige Unsicherheiten des Verlust- und Portabgleichs; sie teilen sich dieselbe Leistungshülle. Der reine A-Verlust des passiven Markers darf dabei nicht als J-Leistung behandelt werden. Eine unter geeigneten Bedingungen nachgewiesene Reziprozität könnte einen kalibrierten Betrag in die Gegenrichtung übertragen. Ein komplexer A/J-Kreuzstandard braucht weiterhin eine kohärente J-Phasenreferenz. Der optische H/HCl-Nullabgleich allein bietet weder diese Referenz noch die Verlusttrennung.

## Gerade Echokanäle im Phasengitter

Für die zwei markierten Rücklaufpfade schreibe die konvergente Reihe $G(z,w)=\sum_{i,j\ge0}G_{ij}z^i w^j$. Bei $m$ beziehungsweise $n$ unabhängigen Einheitswurzelphasen liefert die zweidimensionale diskrete Fourier-Auswertung
$$
\widehat G_{pq}=\sum_{u,v\ge0}G_{p+um,q+vn},\qquad 0\le p<m,\quad 0\le q<n .
$$
Sie trennt die Anzahlen markierter Durchläufe einschließlich gerader Werte. Die Wörter mit gleicher Anzahl bleiben im selben Koeffizienten. Beim $3\times3$-Gitter sind die quadratischen Kanäle $(2,0)$ und $(0,2)$ vom Nullkanal getrennt. Mit $a=\|LA\|$, $b=\|LB\|$, $L=(I-U)^{-1}$ und $a+b<1$ gilt
$$
\|\widehat G_{pq}-G_{pq}\|
\le \|C\|\|LD\|\frac{(a+b)^{p+q+\min(m,n)}}{1-a-b}.
$$
Die Ungleichung zählt alle Terme ab der ersten möglichen Aliasordnung. Der deterministische DFT-Messfehler ist zusätzlich durch den größten Einzelmessfehler begrenzt. Erst ein Koeffizient oberhalb der Summe aus Alias-, Geräte- und Phasenfehlern zertifiziert einen von null verschiedenen Kanal.

Bei symmetrischen Rundläufen $a=b=q$ und einem $3\times3$-Gitter ist die genaue skalare Nullkanal-Majorante ab dem Direktglied $(8q^3/(1-8q^3)-2q^3/(1+q^3))/3$. Für acht Rohphasen mit insgesamt $6\cdot10^{-6}$ rad und $\|C\|\|LD\|/|CLD|=1$ ergibt sich eine Schwelle bei $q\simeq0{,}00721124$. Die Aliasschranke für den Kanal $G_{20}$ ist dort rund $6{,}33\cdot10^{-10}$ mal $\|C\|\|LD\|$. Diese Werte nehmen ideale Phasenstellungen und stationäre Direktkopplung an.

Ein unmarkierter Rücklauf bleibt auch mit kontinuierlicher Phasenabtastung strukturell unbestimmt, solange der nackte Direktweg unbekannt ist. Denn $(U,A,B,D)\mapsto(0,LA,LB,LD)$ ergibt für alle $z,w$ dieselbe Antwort. Der Direktwert ohne Rückläufe ist im Allgemeinen verschieden. Zur unabhängigen Kontrolle ist ein schaltbarer unmarkierter Pfad, ein bekannter Direktstandard oder eine zusätzliche Normgrenze nötig. Für unabhängig bekanntes $\|U\|\le u_0<1$ ist $\|CLD-CD\|\le\|C\|\|D\|u_0/(1-u_0)$.

## Diskrete Säulendichte und Lückenbudget

Setze $u=r^2/R_c^2$ und $\widetilde\sigma(u)=\sigma(R_c\sqrt u)$. In dieser Flächenkoordinate lautet der Potentialterm des [Achsensäulenvergleichs](OP5_J_Optischer_Nullport_Echo_Achsensaeule.md)
$$
\bar\Phi(0)-\bar\Phi(R_c)
=-\pi G R_c^2\int_0^1\widetilde\sigma(u)(-\log u)\,du .
$$
Definiere $F(u)=u(1-\log u)$ und $F(0)=0$. Für einen Ring $[a_i,b_i]$ mit gemessenem Flächenmittel $\bar\sigma_i$ setzt die diskrete Rekonstruktion den Beitrag $\bar\sigma_i W_i$ mit $W_i=F(b_i)-F(a_i)$ an. Ein absoluter Messfehler $\epsilon_i$ im Ringmittel trägt höchstens $\epsilon_i W_i$ zum normierten Integral bei. Eine vollständig unbeobachtete Lücke mit $|\widetilde\sigma|\le B_i$ trägt höchstens $B_i W_i$ bei.

Bei bekanntem Ringmittel und $|\widetilde\sigma-\bar\sigma_i|\le B_i$ ist der verbleibende Fehler wegen des verschwindenden Mittels der Abweichung höchstens
$$
B_i[2F((a_i+b_i)/2)-F(a_i)-F(b_i)] .
$$
Die Grenze folgt durch Subtraktion des Medianwerts des logarithmischen Gewichts und wird bei entgegengesetzten Extremabweichungen auf beiden Ringhälften erreicht. Im unveränderten Gewicht tragen die innersten zehn Prozent des Radius zusammen $5{,}605\%$ und die äußersten zehn Prozent $1{,}932\%$ der Gewichtsnorm. Das sagt ohne eigene Dichteschranke nichts über die tatsächliche Größe des fehlenden Potentialbeitrags.

Ein unabhängig bestätigtes Null-Quermoment kann bei vollständiger Abdeckung einen gemeinsamen additiven Messbias entfernen, indem man $-\log u-1$ statt $-\log u$ gewichtet. Die absolute Gewichtsnorm ist dann $2/e$. Für unabhängig beschränkte Fehler je Messwert minimiert der konstante Shift $\log 2$ die Gewichtsnorm auf $\log 2$. Er kürzt einen gemeinsamen konstanten Bias nur teilweise. Bei einer einzigen Lücke kann das Null-Quermoment ihr Flächenmittel erzwingen, lässt aber den Halbringfehler offen. Fehler der äußeren Potentialreferenz und Längsendterme kommen hinzu. Das rekonstruierte Potential geht mit der bereits hergeleiteten Transfergrenze in den gewöhnlichen $b_4$-Abzug ein. Freie J-Ausbreitung, HCl/H-Portkondition, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte die Leistungsbilanz, die Freiheit der ungemessenen Ausgangsrichtungen, Fourier-Aliase und den Ringkern. Qiskit wurde erwogen. Die Rechnung verwendet klassische Streumatrizen und Dichtegewichte.

[Wolfram-Skript](op5_j_leistungsbilanz_fourier_ringmessung.wl) · [Tatsächliche Ausgabe](op5_j_leistungsbilanz_fourier_ringmessung.txt) · [Laufmanifest](op5_j_leistungsbilanz_fourier_ringmessung.json)
