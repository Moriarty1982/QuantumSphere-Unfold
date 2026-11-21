# OP5 – Vorzeichenfeste Modenzuordnung und mittlere Krümmungskopplungen

21. November 2026. Analytische Erkundung im Materieframe M. Beibehalten werden die kommutierende Einwegstrecke, zwei feste Feldmoden J und A und das statische Ring-Kalibrierprofil. Die Rechnung untersucht, welche zusätzlichen kohärenten Daten die Moden markieren und die vier Krümmungskopplungen identifizieren.

## Vorwissen geprüft

Die [Zweilauf-Kalibrierung](OP5_J_Zweilauf_Kalibrierung.md) trennt bei passenden Gewichten zwei Kopplungsdifferenzen, setzt aber eine vorzeichenfeste Modenzuordnung voraus. Das [Matrixfehlerbudget](OP5_J_AB_Fehlerbudget.md) liefert die Normschranke in Feldkoordinaten. Die [Binnenfeldrechnung](OP5_J_Binnenfeld_Messweg.md) gibt die radialen Signalpolynome. Die Suche nach Modenmarkierung, Phasenreferenz und mittleren Kopplungen ergab im lokalen OP5-Zweig bisher keine solche Auswertung am entarteten Punkt. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 setzt eine eigenständige kosmologische Bestandsdynamik voraus.

## Modenmarkierung im Feldraum

Für eine etablierte kohärente Nullreferenz sei $M_0=LF$. Die Profilübertragung sei $M_\ell=L U_\ell F$ mit $U_\ell=\operatorname{diag}(z_{\ell J},z_{\ell A})$ und $|z_{\ell I}|=1$. Füge in einer Referenzmessung zwischen den Anschlussabbildungen eine physisch identifizierte Markierung $T=\operatorname{diag}(1,-1)$ ein, deren Pluszeichen fest J zugeordnet ist. Die Markierungsmessung ist $M_T=LTF$. Dann gelten im Gerätekoordinatensystem
$$
Q_\ell=M_0^{-1}M_\ell,\qquad A_T=M_0^{-1}M_T,\qquad
z_{\ell J,A}=\tfrac12\operatorname{tr}[(1\pm A_T)Q_\ell].
$$
Die gemeinsame Ähnlichkeit mit $F$ fällt in der Spur weg. Die beiden markierten komplexen Werte bleiben definiert, wenn $z_{\ell J}=z_{\ell A}$. Eine kontrollierte Phasenumkehr in Gerätekoordinaten vor $F$ hätte lediglich $M_T=M_0 T_{\rm Gerät}$ zur Folge. Aus diesem Quotienten folgt die Zuordnung zum Feldraum nur mit separat kalibrierter Abbildung $F$. Für gewöhnliche Polarisation illustrieren interferometrische Jones-Messungen die Art der benötigten komplexen Daten. Eine J-selektive Markierung ist damit weiterhin eine Apparaturannahme. [Interferometrische Jones-Messung](https://opg.optica.org/viewmedia.cfm?seq=0&uri=ol-29-21-2512)

## Fehlergrenze ohne Eigenwertabstand

Seien $r_Q,r_T$ konservative Normgrenzen für die beiden Quotientenfehler in der wahren Feldbasis. Beide können mit dem gewichteten Rest des bisherigen Matrixbudgets berechnet werden. Bei einer Referenz- und Zielmessung mit Gerätefehlern $\epsilon_0,\epsilon_X$, gemeinsamer Anschlussgrenze $p=\sigma_{\min}(L)\sigma_{\min}(F)>\epsilon_0$ und eingeschlossener profil- oder markierungsgebundener Anschlussdrift $d_X$ genügt
$$
\|E_X\|\le r_X:=\frac{\epsilon_0+\epsilon_X+p\,d_X}{p-\epsilon_0},
\qquad X=Q,T .
$$
Hier bezeichnet die rechte Seite jeweils die verfügbare obere Schranke. Ein Fehler der Markierung selbst wird im Zielrest der Markierung mitgeführt. Mit wahren Feldprojektoren $P_\pm=(1\pm T)/2$ ist
$$
\widehat z_\pm-z_\pm=\operatorname{tr}(P_\pm E_Q)
 \ \pm\ \tfrac12\operatorname{tr}[E_T(U_\ell+E_Q)].
$$
Der erste Term ist durch $r_Q$ beschränkt, der zweite durch $r_T(1+r_Q)$, weil die Dimension zwei ist. Somit genügt $e_z=r_Q+r_T(1+r_Q)$ als komplexer Fehlerradius je markiertem Wert. Für $e_z<1$ ist sein Winkelfehler höchstens $\arcsin e_z$. Das benötigt keinen Abstand zwischen den Eigenphasen. Die entfaltete differentielle Phasensekante über $\Delta\omega>0$ hat damit Fehler höchstens $2(\arcsin e_{z,1}+\arcsin e_{z,2})/\Delta\omega$. Die bekannten Zuordnungen und Phasenfortsetzungen müssen über die Frequenzen erhalten bleiben. Ein von null verschiedenes Vorzeichen ist abgesichert, sobald der Betrag der entfalteten Differenz ihre Fehlergrenze übersteigt. Nahe null bleibt also die Beschriftung stabil, während das Vorzeichen eines zu kleinen Messwerts offen bleibt.

Eine unbekannte profilgebundene Änderung am Sender kann auch bei perfekter Markierung eine veränderte Strecke vortäuschen. Für jedes alternative $U'_\ell$ liefert der Senderzusatz $U_\ell^{-1}U'_\ell$ dieselbe Profilmatrix wie die Strecke $U'_\ell$. Daher braucht der markierte Phasenwert weiterhin die angegebene Schranke für Anschlussdrift oder eine passende zeitgleiche Nullkontrolle.

## Einzelphasen mit unabhängiger Zeitreferenz

Eine unabhängige stabile Phasenreferenz bestimmt die gemeinsame Phasensekante jedes Laufs. Nach Abzug der je Modus berechneten gewöhnlichen minimalen Laufzeit seien $y_{\ell I}$ die referenzierten Einzelsekanten. Im Ring-Kalibrierprofil ist der OP5-Kontrast für alle Kernstrahlen null, und der gewöhnliche Gezeitenkontrast ist $g_C$. Dann gilt je Modus
$$
y_{CI}=g_C\lambda^G_I,\qquad
y_{SI}=O_{SI}\lambda^O_I+G_{SI}\lambda^G_I .
$$
Damit sind bei $g_C O_{SI}\ne0$ beide Kopplungen je Modus bestimmt. Die Summe und die Differenz über die Moden geben die gesuchten mittleren und differentiellen Kopplungen. Die Modengewichte dürfen in dieser Rechnung ungleich sein, sofern ihre jeweiligen Kurvenmittel bekannt sind. Eine unbekannte gemeinsame Laufzeit je Lauf lässt zwei Freiheitsgrade in den vier Einzelsekanten und stellt die bisherige Unterbestimmtheit wieder her. Die Markierung allein liefert diese gemeinsame Zeitreferenz nicht.

Für bekannte Koeffizienten und Fehlergrenzen $\eta_{SI},\eta_{CI}$ der Einzelsekanten gilt
$$
|\delta\lambda^G_I|\leq\eta_{CI}/|g_C|,\qquad
|\delta\lambda^O_I|\leq
 \frac{\eta_{SI}+|G_{SI}/g_C|\eta_{CI}}{|O_{SI}|}.
$$
Die $\eta$ umfassen den markierten Phasenfehler, die Referenzdrift und die Unsicherheit der jeweiligen Wegkorrektur. Ungewisse Koeffizienten werden mit den Quotientenschranken der Zweilauf-Rechnung weitergegeben.

## Vier differentielle Messungen ohne gemeinsame Zeitreferenz

Alternativ lassen sich bei abgeglichener Basis pro Lauf, bekannten radialen Gewichten und über alle Läufe konstanten Kopplungen vier differentielle Daten verwenden. Erstens liefert der übliche Ring-Kalibrierlauf nach Wegkorrektur $\lambda_G^-$. Zweitens liefert ein Signallauf mit gleichen Modengewichten und $O_S^+\ne0$ nach Abzug des bekannten gewöhnlichen Anteils $\lambda_O^-$. In zwei weiteren Signalläufen variiere die Modengewichte gezielt. Nach Abzug der bereits bestimmten Differenzkopplungen bleiben in diesen Zeilen ausschließlich die mittleren Kopplungen, mit den Koeffizienten $(O_S^-,G_S^-)$.

Eine explizite unabhängige Wahl erhält man im Grenzfall schmaler radialer Gewichte bei $s=r_\perp^2/R^2$. In beiden Läufen liege A nahe der Achse, J jeweils bei $s_1$ bzw. $s_2$ im flachen Kern. Schreibe $O(s)=O_0+O_1s$ und $G(s)=g_0+g_1s+g_2s^2+g_3s^3$. Dann ist die Determinante der letzten zwei Zeilen
$$
O_1s_1s_2(s_2-s_1)[g_2+g_3(s_1+s_2)] .
$$
Bis auf den gemeinsamen nichtverschwindenden Faktor $4\pi G v_{\rm H}\zeta A_HaP_z$ sind $g_2=b_0+144\kappa b_2/R^2$ und $g_3=-4\kappa b_0$. Für $b_0,b_2,\kappa>0$ und $0<s_1<s_2<1/(36\kappa)$ bleibt die eckige Klammer bis auf diesen Faktor positiv. Mit $O_1=-36\kappa O_0\ne0$ sind damit alle vier Kopplungen identifizierbar. Hinreichend enge glatte Gewichte um die angegebenen Radien erhalten die Rangbedingung durch Stetigkeit. Werden beide Radien gemeinsam zur Achse gezogen, fällt die Determinante kubisch in der Skala von $s$ bei festem Verhältnis. Dann werden die beiden letzten Zeilen fast parallel. Für eine numerische Toleranz ist die kleinste Singulärzahl der gemessenen Koeffizientenmatrix zu kontrollieren, nach Festlegen der Einheiten und Gewichtung der Messfehler.

Die beiden Wege setzen entweder eine stabile gemeinsame Zeitreferenz oder kontrolliert veränderliche Modengewichte voraus. In beiden Fällen bleiben eine tatsächlich feldselektive Markierung oder unabhängige Modenzuordnung, stabile Anschlüsse, weitere gewöhnliche Operatoren und die native Higgs–OP5-Kopplung offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_modenzuordnung.wl) · [Tatsächliche Ausgabe](op5_j_modenzuordnung.txt) · [Laufmanifest](op5_j_modenzuordnung.json)

Wolfram prüfte die Spurauslese mit nichtdiagonalen Anschlüssen bei freiem und verschwindendem Phasenabstand, die Fehlerentwicklung und beide Rangdeterminanten samt gewöhnlichen radialen Koeffizienten. Die Normschranken und die Fortsetzung auf glatte Gewichte werden analytisch hergeleitet. Reproduzierbar mit **wolframscript -file op5_j_modenzuordnung.wl**.
