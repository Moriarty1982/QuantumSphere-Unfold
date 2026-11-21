# OP5 – Anschlussabgleich, Längenkreuzquotient und Polarisationswege

21. November 2026. Analytische Erkundungen im Materieframe M. Die [feste Terminierung](OP5_J_Terminierung_Referenzebenen.md) liefert die Fehlergrenzen für die homogene Musterschicht, die 4-m-Strecke und den Ricci/Weyl-Vergleich. Hier werden reale Anschlussbeiträge parametrisiert, ein gemeinsamer Längenvergleich geprüft und geeignete Polarisationsgeometrien untersucht. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 braucht eine eigenständige kosmologische Bestandsdynamik.

## Kreuzreflexion an zwei Referenzebenen

Die Reflexion der Markerschicht von rechts heiße $R$. Ein aus Sicht der Schicht linker Anschluss mit effektiver Reflexion $\Lambda_L$ verändert $R$ zu $R'=R+\Delta_L$. Für die Durchgangsblöcke $T_{RL},T_{LR}$ und die linke Schichtreflexion $R_L$ ist
$$
\Delta_L=T_{RL}\Lambda_L(I-R_L\Lambda_L)^{-1}T_{LR}.
$$
Somit genügt $\|\Delta_L\|\le\lambda/(1-r\lambda)$, wenn $\|\Lambda_L\|\le\lambda$, $\|R_L\|\le r$, $r\lambda<1$ und die beiden Durchgänge passiv normiert sind.

Am rechten Anschluss seien $D$ und $A$ die Reflexionen von außen beziehungsweise innen sowie $B$ und $C$ die Durchgänge nach innen beziehungsweise außen. Dann misst man an der äußeren Ebene
$$
R_{\rm ext}=D+C R'(I-A R')^{-1}B.
$$
Eine kalibrierte reflexionsfreie Terminierung an der inneren Ebene liefert direkt $D$. Bei nicht exakt abgeglichener Terminierung mit bekannter Norm $\lambda_0$ liegt ihr Beitrag innerhalb $\|B\|\|C\|\lambda_0/(1-\|A\|\lambda_0)$. Sind auch $B,C$ invertierbar und kalibriert, setze $Z=C^{-1}(R_{\rm ext}-D)B^{-1}$. Dann ist $R'=(I+ZA)^{-1}Z$. Für fehlerhaftes $\widehat Z$ bei bekanntem $A$ gilt exakt
$$
\widehat R'-R'=(I+\widehat ZA)^{-1}(\widehat Z-Z)(I-A R').
$$
Die Differenz zweier Ebenen kann den Anschlussbeitrag daher nur bei kontrolliertem Durchgang und Fehlerverstärkung isolieren. Fehler in $A,B,C$ müssen zusätzlich begrenzt werden. Schlechte Portkondition wird durch den Ebenenwechsel nicht beseitigt.

Für eine direkte Budgetrechnung sind invertierbare Durchgänge nicht erforderlich. Sei $R_0$ die diagonale Schichtreferenz, $\|R-R_0\|\le r_\times$, $\|R_0\|\le r$, $\|R\|\le r$ und $r'=r+\|\Delta_L\|$. Bei passiven Durchgängen und $\|A\|\le a$ ergibt sich
$$
|(R_{\rm ext})_{AJ}|\le
|D_{AJ}|+r_\times+r\left(\|B-B_{\rm diag}\|+\|C-C_{\rm diag}\|\right)
+\|\Delta_L\|+\frac{a(r')^2}{1-ar'}.
$$
Hier stammt der Mischterm aus $C R_0 B-C_{\rm diag} R_0 B_{\rm diag}$ und der letzte Term aus den wiederholten Reflexionen. Diese Form budgetiert sowohl direkte Anschlusskreuzreflexion als auch die Umwandlung der größeren diagonalen Schichtreflexion.

Ein illustratives Ziel für **jeden** Marker-/Schalterzustand ist $|D_{AJ}|\le10^{-6}$, $\|D\|\le10^{-4}$, $a\le0{,}1$, beide Durchgangs-Mischrestnormen höchstens $0{,}01$ und $\lambda\le2\cdot10^{-7}$. Mit $r=3{,}512\cdot10^{-6}$ und $r_\times=3{,}8597\cdot10^{-8}$ ergeben sich außen $|(R_{\rm ext})_{AJ}|<1{,}309\cdot10^{-6}$ sowie $\|R_{\rm ext}\|<1{,}038\cdot10^{-4}$. Ist zusätzlich der äußerlich gemessene $|u_J|\le0{,}0033$, bleibt der Logfehler des A-Vier-Zustands-Vergleichs mit fester passiver J-Terminierung unter $4{,}985\cdot10^{-7}$. Enthalten sind die bisherigen Fehler für die Zweilastmessung und die Referenzebenen. Diese Werte sind gemeinsame Bedingungen, keine gemessenen Anschlussparameter. Insbesondere muss $u_J$ außen neu begrenzt werden.

## Was der Längenkreuzquotient aus der Referenz entfernt

Sei am Längenpunkt $i$ und der Frequenz $f$ die entfaltete Phase des J/A-Quotienten
$$
\phi_{i,f}=h_f+g_f(d_i+c_{i,f})+k_{J,f}\ell_{i,f},\qquad g_f=k_{J,f}-k_{A,f}.
$$
$h_f$ ist der beliebige längenunabhängige Anschlussphasenterm. $c$ ist der gemeinsame Wegfehler und $\ell$ der relative J/A-Versatz. Die doppelte Differenz aus Länge und Frequenz kürzt $h_f$ exakt, auch bei chromatischem $h_f$. Schreibe $C_f=c_{1,f}-c_{0,f}$, $L_f=\ell_{1,f}-\ell_{0,f}$. Nach Abzug des gesuchten Terms $(d_1-d_0)\Delta g$ bleibt
$$
\bar C\,\Delta g+\Delta C\,\bar g+\bar L\,\Delta k_J+\Delta L\,\bar k_J .
$$
Chromatische Referenzfehler kürzen sich damit, sofern sie bei den beiden Längenstellungen gleich bleiben. Zeitgleiche Frequenzen beseitigen einen zeitbedingten Endpunktunterschied in $C,L$, wenn die Wege achromatisch sind. Eine beim Längenwechsel veränderte Chromatik bleibt messrelevant. Das vorherige 4-m-Einzelbudget von $8{,}33$ pm gilt damit für die **Änderung der relativen Versatzdifferenz** $\Delta L$, nicht für einen festen relativen A/J-Abstand. Für achromatisches $\bar L$ beträgt das Einzelbudget etwa $7{,}26$ µm. Diese Einzelbudgets sind nicht gleichzeitig ausschöpfbar.

Ein A-Pilot misst nur den gemeinsamen Referenzweg oder dessen A-Projektion. Eine unbekannte Zusatzänderung ausschließlich im J-Referenzweg bleibt unbeobachtet. Zwei unabhängig kalibrierte Wege bei bekannter Pilotwellenzahl $k_p$ können $p_A=k_p C$ und $p_J=k_p(C+L)$ liefern. Dann ist die Korrektur je Frequenz $(k_J p_J-k_Ap_A)/k_p$. Auch ein einzelner differentieller Pilot genügt, wenn seine Sensitivität proportional zu $(g,k_J)$ auf $(C,L)$ ist. Er muss die Referenzabschnitte erfassen. Eine Messung über die volle unbekannte J-Strecke würde bei der Subtraktion zugleich das Zielsignal ändern. Werden vier unabhängige, bereits als Phasenkorrektur normierte Einzelwerte eingesetzt, genügt im vorigen 4-m-Beispiel je ein Fehler unter $3{,}80\cdot10^{-6}$ rad, wenn sie die gesamte Zusatzreserve beanspruchen.

## Ricci- und Weyl-Projektionen im vorhandenen Nullprofil

Im flachen Kern des [Nullprofils für denselben Messweg](OP5_J_Gleicher_Messweg_Nullprofil.md) hat das relevante transversale Polynom die Form $p=s^2-\kappa s^3$, $s=(x^2+y^2)/R^2<s_0$. Die integrierte Gezeitenmatrix des massiven linearen Vergleichs ist bis auf ihre axiale Normierung $I_0$ durch $R^4\operatorname{Hess}_\perp(\Delta_\perp p)/32$ gegeben. Für einen parallelen Strahl bei $x=b,y=0$ und radiale beziehungsweise tangentiale Polarisation lauten die Eigenwerte
$$
I_r=I_0(1-27\kappa s/2),\qquad I_t=I_0(1-9\kappa s/2).
$$
Ihr Summensignal ist die integrierte Ricci-Projektion, ihre halbe Differenz die Weyl-Projektion. Damit liefert die Achse einen reinen Ricci-Vergleich der modellierten Geometrie. Ein versetzter Strahl liefert die unabhängige Weyl-Differenz. Bei $s=1/(9\kappa)$ und $\kappa>0$ sind $I_r=-I_0/2$ und $I_t=I_0/2$. Dieser reine Weyl-Vergleich liegt im verwendbaren Kern nur bei $1/(9\kappa)<s_0$. Die Trennung über zwei Polarisationen bleibt auch ohne diesen speziellen Ring möglich.

Ein rotationssymmetrisch um die Achse gemittelter Strahl mit fester linearer Polarisation löscht den Weyl-Anteil. Ein runder Spot, der vollständig im Kern liegt und seitlich bei $(b,0)$ zentriert ist, bewahrt bei gleichen transversalen Varianzen und verschwindender Kovarianz die Weyl-Differenz des Strahls bei $b$, da $\langle x^2-y^2\rangle=b^2$. Die Ricci-Projektion enthält dagegen den zweiten radialen Moment des Spots. Die separat konstruierte gewöhnliche Kontrolle des [Binnenfelds](OP5_J_Binnenfeld_Messweg.md) wurde auf der Achse geprüft. Ihre Übertragung auf den seitlich versetzten Polarisationsvergleich erfordert eine eigene Rechnung.


Im mechanisch kompensierten [Binnenfeldprofil](OP5_J_Binnenfeld_Messweg.md) hat die massive Gezeitenantwort stattdessen das Profilpolynom $s^2-4\kappa s^3$. Seine Weyl-Projektion ist proportional zu $s$. Die gewöhnliche Weyl-Projektion ist proportional zu $s\phi''(s)$, wobei $\phi$ das integrierte gewöhnliche Potentialpolynom aus der Binnenfeldrechnung ohne seinen konstanten Vorfaktor ist. Der Koeffizient von $s^2$ in $\phi''$ ist $q=-3b_0\kappa R^2/4$. Der reduzierte Zweiradius-Determinant für gemeinsame unbekannte Skalierungen der beiden Profile lautet
$
s_1 s_2[\phi''(s_2)-\phi''(s_1)].
$
Für $q\ne0$ wähle drei Punkte $s_i=i s_0/4$, $i=1,2,3$. Die Differenzen von $\phi''$ an den benachbarten Punkten unterscheiden sich um $2q(s_0/4)^2$. Mindestens ein benachbartes Paar hat daher einen reduzierten Determinantbetrag von mindestens $2|q|(s_0/4)^4$. Dies trennt algebraisch die beiden deklarierten Weyl-Beiträge, sofern die Skalierungen und die Modengewichte über den Ortswechsel gemeinsam bleiben. Die Größen der Vorfaktoren, die Spotmittelung und die übrigen gewöhnlichen Operatoren bestimmen die physische Kondition.

Damit gibt es im Modell Geometrien für zwei unabhängige Krümmungsprojektionen. Die Zuordnung der Modellkrümmung zur nativen effektiven Vermittlermetrik, die realen Portprojektionen und die übrigen lokalen Ricci-/Weyl-Koeffizienten bleiben offen. Freie J-Ausbreitung und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte den Anschlussabgleich einschließlich nichtkommutierender Blöcke, die beiden Pilotrelationen, die Profil-Hesse-Matrix und den reinen Weyl-Ring. Qiskit wurde für die klassischen Matrix- und Phasenrechnungen erwogen.

[Wolfram-Skript](op5_j_anschluss_pilot_polarisation.wl) · [Tatsächliche Ausgabe](op5_j_anschluss_pilot_polarisation.txt) · [Laufmanifest](op5_j_anschluss_pilot_polarisation.json)
