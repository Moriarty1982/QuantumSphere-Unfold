# OP5 – Abgleich des Matrix-Nullpfads

20. November 2026. Analytische Erkundung im Materieframe M. Gesucht ist die nötige Übereinstimmung von Mess- und Nullpfad für die differentielle Laufzeit. Die betrachtete Einwegstrecke hat zwei propagierende Moden. Ihr Kontrast $U(\omega)$ ist im Modell unitär. Alle Normen sind Operatornormen zur 2-Norm in der gemeinsamen kanonischen Feldbasis.

## Vorwissen geprüft

Das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) liefert die Spektral- und Phasenhülle eines ideal abgeglichenen Kontrollpfads und die aus einem Laufzeitziel rückwärts bestimmte Zahl $r_*$ des zulässigen Eigenwertabstands. Die [HCl/H-Anschlusskondition](OP5_J_HCl_Anschlusskondition.md) bestimmt die Empfindlichkeit der Anschlüsse. Die [skalare Endpunktdrift](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Endpunktdrift.md) verwendet eine unabhängige Kontrolle mit bekanntem Streckenkontrast. Die lokale Suche nach Nullpfad, Kontrollpfad und Kalibrierung ergab für den Matrixpfad bisher den exakt gemeinsamen Anschlussfall. Die neue Rechnung bestimmt, welche relativen Anschlussfehler dessen Eigenphasen tatsächlich verschieben. Die Einordnung folgt dem lokalen Auslesezweig im [Gesamtbild](../../../wiki/Gesamtbild.md). Die für I3 nötige Bestandsdynamik bleibt eine spätere Forschungsfrage.

## Welche Anschlussabweichung im Spektrum erscheint

Schreibe die Nullmessung $C=LF$ und die Messung mit Kontrast $M=LSURF$. Die Matrizen $L,F$ sind die invertierbaren Anschlüsse des Kontrollpfads. $S=I+X$ und $R=I+Y$ sind die relativen Abweichungen auf der Empfangs- beziehungsweise Sendeseite des Messpfads. Für invertierbares $S$ ist $C^{-1}M$ ähnlich zu
$$
U W,\qquad W=RS.
$$
Denn $C^{-1}M=F^{-1}SURF$ und $S^{-1}(SUR)S=URS$. Im idealen Spektrum zählt das geordnete Produkt $W$. Sind die beiden Abweichungen reziprok, also $R=S^{-1}$, bleiben beide Eigenwerte exakt erhalten. Ist $W=cI$ mit $c\ne0$, erhalten beide Eigenwerte denselben komplexen Faktor. Er verschiebt nur die gemeinsame Phase, auch wenn $c$ von der Frequenz abhängt. Die entfaltete Phasendifferenz und ihre Sekante bleiben erhalten. Diese Aussagen setzen eine gemeinsame kohärente Basis und eine konsistente Phasenentfaltung voraus.

Ohne Information über die Fehlerstruktur gilt
$$
\|UW-U\|=\|W-I\|\le \|X\|+\|Y\|+\|X\|\,\|Y\|.
$$
Für das bisherige Beispiel $r_*=3{,}92699\cdot10^{-5}$ und gleichen Endbudgets $\|X\|,\|Y\|\le\eta$ genügt bei verschwindendem additivem Fehler
$$
\eta<\sqrt{1+r_*}-1\simeq1{,}96348\cdot10^{-5}.
$$
Das sind knapp 20 Millionstel pro Ende in der normierten Feldmatrix. Der Wert ist eine hinreichende Toleranz für beliebig gerichtete Abweichungen, keine Vermessung räumlicher Justierfehler.

## Direkter Phasenfehler und Vermischung

Sei $E=U(W-I)$ in der orthonormalen Eigenbasis von $U$. Setze $g=|\lambda_1-\lambda_2|$, $d=\max_j|E_{jj}|$ und $m=\max(|E_{12}|,|E_{21}|)$. Aus $\|E\|\le d+m<g/2$ folgt die eindeutige Zuordnung der gestörten Eigenwerte $\mu_j$ zu $\lambda_j$. Für $k\ne j$ ergibt die charakteristische Gleichung
$$
(\mu_j-\lambda_j-E_{jj})(\mu_j-\lambda_k-E_{kk})=E_{jk}E_{kj}.
$$
Da $|\mu_j-\lambda_j|\le d+m$, folgt
$$
|\mu_j-\lambda_j|\le d+\frac{|E_{jk}E_{kj}|}{g-2d-m}.
$$
Die Diagonalkomponente geht linear ein. Vermischung ohne Diagonalkomponente wirkt erst über das Produkt beider Mischrichtungen. Ist nur eine der beiden Mischrichtungen vorhanden, ist die Matrix dreieckig und hat bei verschwindender Diagonalkorrektur exakt die ursprünglichen Eigenwerte. Für $d=0$ und $m<g/2$ genügt $m^2/(g-m)<r_*$. Bei einem Phasenabstand von mindestens $0{,}1$ rad ist $g\ge2\sin(0{,}05)\simeq0{,}0999583$. Das bisherige Beispielbudget lässt dann $m<0{,}00196171$ zu. Das entspricht knapp $0{,}2\,\%$ in den Auf- und Abmischungseinträgen des gesamten Restfehlers. Diese Reserve gilt nur bei geprüfter verschwindender oder separat budgetierter Diagonalkomponente in der Eigenbasis. Nahe einer Phasenentartung verliert die quadratische Schranke ihre Anwendbarkeit.

## Additive Fehler und unabhängige Nullstellung

Bei $\widehat C=L(I+N_C)F$ und $\widehat M=L(SUR+N_M)F$ seien $n_i$ obere Schranken für $\|N_i\|$, zum Beispiel $\epsilon_i/[\sigma_{\min}(L)\sigma_{\min}(F)]$ für additive Gerätefehler $\epsilon_i$. Konjugation mit $S$ gibt in der Feldbasis die Form
$$
(I+S^{-1}N_C S)^{-1}\bigl(UW+S^{-1}N_M S\bigr).
$$
Für $\kappa(S)n_C<1$ genügt somit die konservative Hülle
$$
r=\frac{\|W-I\|+\kappa(S)(n_C+n_M)}{1-\kappa(S)n_C}.
$$
Der Fehlerradius des A/B-Budgets muss sowohl den Rest des Pfadabgleichs als auch die additiven Fehler aufnehmen. Für einen strukturierten Spektraltest kann stattdessen der gesamte Rest in der Eigenbasis als $E$ eingeschätzt werden. Die Näherung einer reinen Vermischung darf erst nach Prüfung der Diagonale benutzt werden.

Ein weiterer Weg ist eine **unabhängig bekannte Nullstellung im Messzweig selbst**. Wenn der Eingriff $U\mapsto I$ nur den Streckenkontrast ändert und die relativen Anschlüsse $S,R$ sowie $L,F$ beibehält, liefert diese Nullstellung $M_0=LSRF$. Dann ist
$$
M_0^{-1}M=F^{-1}R^{-1}URF.
$$
Der Pfadunterschied zum parallelen Kontrollweg fällt in diesem idealen Quotienten exakt heraus, auch für nichtkommutierende Anschlussmatrizen. Das ist ein klares Kriterium an die Kalibrierung: Die Nullstellung muss eine unabhängig begründete Änderung der Strecke sein und dabei dieselben Endpunktüberlappungen und Phasen teilen. Eine Schaltung, die zugleich die Anschlüsse ändert, lässt einen Rest in Form von $W$ zurück. Eine gemessene Differenzphase allein bestimmt die unbekannte Diagonalabweichung weiterhin nicht.

## Rechenkontrolle

[Wolfram-Skript](op5_j_nullpfad_abgleich.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_nullpfad_abgleich.txt) · [Laufmanifest](op5_j_nullpfad_abgleich.json)

Wolfram liefert exakte Nullreste für die zyklische Ähnlichkeit, reziproke Anschlussabweichungen, die Kalibrierung in derselben Messstrecke und die charakteristische Produktform. Zwei numerische Kontrollen desselben komplexen Mischungsmusters bei 45-stelliger Eingabe ergeben bei zehnfach kleinerer Mischungsamplitude einen rund hundertfach kleineren Eigenwertfehler. Die numerischen Beispiele ersetzen die allgemeine Schranke nicht. Das Skript ist im Notizordner mit `wolframscript -file op5_j_nullpfad_abgleich.wl` reproduzierbar. Der Lauf erfolgte im Wolfram-Connector. Qiskit wurde erwogen. Die zu prüfenden Fehler sind relative Übertragungsmatrizen einschließlich möglicher Verluste und können hier exakt algebraisch kontrolliert werden.

Offen bleiben eine physisch realisierte Nullstellung, die Kalibrierung ihrer Endpunktabweichungen, freie J-Ausbreitung im betreffenden Band, native Kopplung und H96.
