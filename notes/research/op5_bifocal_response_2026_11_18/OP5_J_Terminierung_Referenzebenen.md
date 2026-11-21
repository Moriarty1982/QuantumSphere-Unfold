# OP5 – Feste J-Terminierung, Referenzebenen und Elektronenschwelle

21. November 2026. Analytische Erkundungen im Materieframe M. Untersucht werden die skalare A-Kalibrierung bei fester J-Last, die Freiwegstabilität bei 4 m und eine mögliche unabhängige Geometrieprüfung des Elektronenbeitrags. Bezug sind [passive Lasten und Dispersion](OP5_J_Passive_Last_Dispersion.md), der [Schicht-Rücklauf](OP5_J_Ruecklauf_Toleranzen.md) und der [Dirac-Schwellenvergleich](OP5_J_Dirac_Schwellenabgleich.md). Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Wann eine feste J-Terminierung genügt

Bei Variation der A-Last und fester passiver J-Terminierung $\gamma_J$ lautet der Interzeptrest
$$
b_J=\frac{R_{AJ}\gamma_J u_J}{1-\gamma_J R_{JJ}}.
$$
Die beiden A-Laststellungen bestimmen den effektiven Interzept $t+b_J$. Die effektive A-Reflexion ist bei passivem Streuer und passiver J-Terminierung weiterhin eine Kontraktion. Bei abgeschaltetem Linkseingang kann die auslaufende J-Leistung die einfallende J-Leistung nicht unterschreiten. Damit bleibt die auslaufende A-Leistung höchstens gleich der einfallenden A-Leistung. Das bisherige skalare Fehlerbudget für die zwei A-Laststellungen bleibt anwendbar.

An der homogenen Musterlage mit gleichen Außenmedien gilt durch Spiegelung der vorherige Reflexionsgrenze auch von rechts. Die skalare Referenz $R_0$ ist diagonal. Für den Kreuzreflexionskoeffizienten genügt daher die Summe der drei Störungsterme,
$$
|R_{AJ}|\le \|R-R_0\|\le
4{,}573\cdot10^{-9}+2{,}624\cdot10^{-9}+3{,}140\cdot10^{-8}
=3{,}8597\cdot10^{-8}.
$$
Mit $|u_J|\le0{,}00317$, $|R_{JJ}|\le3{,}512\cdot10^{-6}$ und $|\gamma_J|\le 1$ ist $|b_J|<1{,}224\cdot10^{-10}$. Werden diese und die früheren Fehlerschranken in **allen vier** Marker-/Schalterzuständen eingehalten, bleibt die komplexe Logabweichung unter $4{,}814\cdot10^{-7}$. Enthalten sind der Zweilastfehler $2{,}001\cdot10^{-8}$ je Zustand und die separat budgetierten $4\cdot10^{-7}$ für die Referenzebenen. Vorausgesetzt ist der bisherige Durchgangsbetrag $|t_{ms}|\ge0{,}99$.

Würde nur die volle Reflexionsnorm als Grenze für $|R_{AJ}|$ verwendet, läge der Fehler mit beliebiger passiver J-Last bei bis zu $5{,}259\cdot10^{-7}$. Für genau diese gröbere Information genügte $|\gamma_J|\le0{,}4257$. Bei einheitlicher Vollreflexionsgrenze und $|\gamma_J|\le1$ reicht als gezielte Messgröße $|R_{AJ}|\le1{,}495\cdot10^{-6}$. Die kleine Schichtkreuzreflexion gilt an den homogenen Modell-Referenzebenen. Zusätzliche Modenumwandlung an realen Anschlüssen oder im Schalter muss separat erfasst werden. Die A-Kalibrierung mit fester Terminierung benötigt unter dieser Bedingung keine Erzeugung des Zweikanal-Lastdreiecks. Die vollständige Zweikanalauslese ist ein eigener Nachweis.

## Referenzebenen und Dämpfung bei 4 m

Für die Bandenden seien $L_{A,\pm}=d+c_\pm$ und $L_{J,\pm}=d+c_\pm+\ell_\pm$. $c$ beschreibt den gemeinsamen Wegfehler und $\ell$ den relativen J/A-Versatz. Mit $g=k_J-k_A$ ist der Geometrierest der Differenz beider Endphasen exakt
$$
\bar c\,\Delta g+\Delta c\,\bar g+\bar\ell\,\Delta k_J+\Delta\ell\,\bar k_J .
$$
Balken bezeichnet den Mittelwert, $\Delta$ den oberen minus unteren Bandwert. Bei $d=4$ m beträgt das Modelltrennsignal $S=8{,}38422\cdot10^{-4}$ rad. Nach der bisherigen Fehlerhülle bleibt eine zusätzliche Reserve von $1{,}52109\cdot10^{-5}$ rad je Zweibandkontrast, damit die Fehlerintervalle beider Modelle getrennt bleiben. Die folgende Tabelle setzt jeden Beitrag einzeln dieser Reserve gleich. Die Beträge teilen sich die Reserve, und für Abschlüsse gegen einen unbekannten konstanten Versatz müssen die Koeffizienten über das Ankerintervall für beide Modelle begrenzt werden.

| Geometriefehler | Einzelwert im nominalen Modell |
| --- | ---: |
| Mittlerer gemeinsamer Wegfehler | $7{,}26$ cm |
| Änderung des gemeinsamen Wegs zwischen Bandenden | $83{,}3$ nm |
| Mittlerer relativer J/A-Versatz | $7{,}26$ µm |
| Änderung des relativen J/A-Versatzes zwischen Bandenden | $8{,}33$ pm |

Bei unabhängig vermessener, gemeinsamer und frequenzunabhängiger Länge kann die tatsächliche Länge direkt in den Modellkontrast eingesetzt werden. Dafür gilt weiterhin die vorangegangene Mindestlänge von rund 3,855 m. Die ausgesprochene Empfindlichkeit auf den relativen Versatz entsteht durch die optische Wellenzahl im letzten Term.

Mit gemeinsam gültiger Geometriegrenze $B_g$, einem relativen additiven Fehler $\rho$ je komplexem Messwert und A-Phasenfehler $\delta_A$ je Paar lautet die robuste Bedingung $B_g+4\arcsin(\rho)+2\delta_A<S/2$. Ohne zusätzliche Geometrieanteile ergibt sie bei $\delta_A=2\cdot10^{-6}$ rad höchstens $\rho\simeq1{,}0380\cdot10^{-4}$. Die bisherige Grenze $10^{-4}$ lässt wenig Mehrwegreserve. Für wahre Direktamplitude $A_0e^{-\alpha d}$ und aggregierten absoluten Additivfehler $\eta$ genügt $\eta\le[\rho/(1+\rho)]A_0e^{-\alpha d}$. Bei $\eta/A_0=10^{-5}$ ist im reinen Dämpfungsbeispiel $\alpha$ bis etwa $0{,}585\ {\rm m}^{-1}$ zulässig, wenn die volle relative Reserve verwendet wird. Mehrwege, Geometrie und Referenzfehler sind im realen Aufbau gemeinsam zu budgetieren.

## Was Polarisationsmessungen an der Elektronenschwelle prüfen

Im Elektronenvergleich sei $G_e=q_e q_e^{\mathsf T}/m_e^2$, $K$ die flache positive Kinetik und $I_R=\int R_{\rm eff}(n,e,n,e)\,dz$. Die axiale Eigenwertlücke der normalisierten Elektronenkorrektur ist
$$
s=\frac{11|I_R|}{720\pi^2} \operatorname{tr}(K^{-1}G_e).
$$
Ein zusätzliches normalisiertes lokales Matrixglied mit Abstand höchstens $\varepsilon$ von einer skalaren Matrix lässt mindestens $s-2\varepsilon$ an Lücke. Ein unabhängiger Operator derselben Tensor- und Feldstruktur kann den Elektronenbeitrag exakt kompensieren. Die fehlende gemeinsame effektive Vermittlermetrik lässt zudem $I_R$ offen. Ladung und Masse allein liefern daher keine native Untergrenze.

Eine geometrisch unabhängige Prüfung ergibt sich mit zwei orthogonalen transversalen Polarisationen auf abgeglichenen Strahlen derselben effektiven Metrik. In vier Dimensionen gilt $R(n,e_i,n,e_i)=C_i+R_{nn}/2$ und $C_1+C_2=0$. Der Ricci-Faktor ist im Mittel der beiden Polarisationsantworten $11/360$ vor $G_e/(4\pi^2)$. Die halbe Differenz hat vor demselben Faktor den Weyl-Koeffizienten $-1/90$ mal $C_1$. Der Quotient der auf die jeweilige Krümmung separat normierten Koeffizienten beträgt somit $-4/11$. Der Achsengrenzfall reproduziert den bisherigen axialen Wert. Diese Prüfung kann die Ricci-/Weyl-Struktur testen, sobald die effektiven Krümmungen separat bekannt sind. Unabhängige lokale Beiträge mit denselben Strukturen bleiben zu begrenzen. Freie J-Ausbreitung, HCl/H-Portkondition, native Kopplung und H96 bleiben offen. [Effektive Photonenwirkung](https://arxiv.org/abs/gr-qc/0205042) · [Polarisationssummenregel](https://arxiv.org/abs/gr-qc/9504041)

## Rechenkontrolle

Wolfram bestätigte die Interzeptidentität, die Geometriezerlegung und die Krümmungskoeffizienten exakt und wertete die Fehlerbudgets numerisch aus. Qiskit wurde für diese klassischen Streu-, Phasen- und Tensorrechnungen erwogen.

[Wolfram-Skript](op5_j_terminierung_referenzebenen.wl) · [Tatsächliche Ausgabe](op5_j_terminierung_referenzebenen.txt) · [Laufmanifest](op5_j_terminierung_referenzebenen.json)
