# OP5 – Endpunktphase, belastete Wellenstandards und Materialhub

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Endpunkt- und Momentkernrechnung](OP5_J_Bandendpunkte_Pilot_Momentkerne.md) wird für komplexe Resonanzphase, Lastfeedback in der Referenzkalibrierung und gewöhnliche mechanische Anforderungen fortgesetzt. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört dies zur lokalen Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Phase und Verlust an einem kalibrierten Resonanzpunkt

Setze $\lambda_i=\kappa_i+\alpha_i$, $Z_i=\lambda_i-i\delta_i$ und $D=Z_AZ_J+g^2$ im Zweimodenmodell. Für nachgewiesene gemeinsame Port- und Kopplungsphase gilt für den normierten relativen Transmissionswinkel gegenüber dem Resonanzwert
$$
\arg[T(\delta_A,\delta_J)/T(0,0)]
=\operatorname{atan2}(\lambda_A\delta_J+\lambda_J\delta_A,\,
\lambda_A\lambda_J+g^2-\delta_A\delta_J).
$$
Im verlustfreien symmetrischen Beispiel erzeugt die bisher zulässige gemeinsame Verstimmung von rund $36{,}97$ kHz bereits eine Transmissionsphase von rund $4{,}24\cdot10^{-3}$ rad. Die direkte Reflexion ist bei gemeinsamer Verstimmung nur quadratisch empfindlich. Im asymmetrischen verlustbehafteten Beispiel bei $0{,}64$ Hz beträgt die entsprechende Phase rund $9{,}18\cdot10^{-6}$ rad. Der Reflexionsbetrag allein legt die komplexe Kalibrierphase daher nicht fest. Für eine Lastabbildung durch einen Spiegel wird die Einwegphase zweimal gelesen.

Bei A-Anregung schließt die Leistungsbilanz des Zweimodenmodells mit
$$
1-|S_{AA}|^2-|T|^2=
\frac{4\kappa_A[\alpha_A|Z_J|^2+\alpha_Jg^2]}{|D|^2}.
$$
Eine unabhängige Verlustgrenze oder eine kalibrierte Messung auch des J-Ausgangs ist nötig, um eine Reflexionsnull der Konversion zuzuordnen. Bei bekanntem Messwert $\widehat T$ und komplexer Fehlergrenze $\epsilon_T$ folgt $|T|^2\ge\max(0,|\widehat T|-\epsilon_T)^2$. Ohne den J-Messwert und ohne getrennte Verlustinformation bleibt nur die Summe aus Ausgangsleistung und Verlust aus der A-Bilanz. Weitere ungemessene Kanäle müssen zusätzlich bilanziert werden.

Die kritische A-Anpassung bei $\alpha_J=0$ hat bei Konversionsleistung $\eta$ die J-Reflexion $r_J=-(1-\eta)$. Bei $99\%$ ist der Resonator daher am J-Eingang nicht reflexionsfrei. Schaltet ein A-Spiegel an diesem Konverter im Zentrum zwischen $\pm\gamma$, ist die abgebildete J-Last $r_J\pm x$ mit $x=\gamma T^2$, weil die A-Reflexion am Spiegelport verschwindet. In einem zusätzlichen kalibrierten Probe-Zweitor mit J-Reflexion $r$ und Einwegprodukt $P$ liefert die gegenphasige Differenz geteilt durch $2x$ daher
$$
\frac{P}{(1-r r_J)^2-(rx)^2}.
$$
Die feste Rückreflexion des Konverters ist in der Normierung mitzunehmen. Für $\eta=0{,}99$, $|\gamma|=0{,}5$, $|r|\le0{,}1$, $|P|=9\cdot10^{-6}$ und additive A-Messfehler bis $5\cdot10^{-8}$ beträgt die kombinierte Grenze im Beispiel rund $1{,}413\cdot10^{-7}$, sofern $x$ bereits komplex kalibriert ist. Das liegt unter dem früheren Ein-Prozent-Produktbudget von $1{,}791\cdot10^{-7}$. Die Differenz lässt nur wenig Platz für die bislang ungemessene Lastphase, Verluste und Zustandsdrift. Ein physischer J-Port folgt aus dieser Rechnung nicht.

## Wellenstandards trotz Quellenreflexion

An einer festen kalibrierten Ebene sei $a^+=s+r_S a^-$ und $a^-=\Gamma a^+$. Dann ist die tatsächliche Standardspalte $s(1,\Gamma)^{\mathsf T}/(1-r_S\Gamma)$. Bei nominell gleichem Antrieb vernachlässigt ein Standard mit angenommenem konstantem $a^+=s$ genau diesen Rücklauf. Für $|r_S|\le1{,}04\cdot10^{-4}$ und $|\Gamma|=0{,}5$ kann der relative Vorwärtsfehler bereits $5{,}20\cdot10^{-5}$ betragen.

Mit drei kalibrierten Lasten $0,+\gamma,-\gamma$, gleichbleibendem komplexem Quellwert $s$ und unabhängig vom Lastzustand festem Empfängerblock $K$ gilt für die gemessenen Rohvektoren
$$
X_++X_--2X_0=r_S\gamma(X_+-X_-).
$$
Der Vektor $B=\gamma(X_+-X_-)$ bestimmt die Kondition der komplexen Projektion. Für maximale Rohfehler $\epsilon$ pro Standard ist die Fehlergrenze von $r_S$ höchstens $(4+2|r_S\gamma|)\epsilon/\|\widehat B\|$. Danach ist $sKe_A=X_0$ und die zweite Spalte folgt aus $[(1-r_S\gamma)X_+-X_0]/\gamma$. Der Dreilastabgleich bestimmt damit den Empfängerblock mal Quellamplitude. Eine relative Quellskala zwischen Leerkörper und Marker oder zwischen Frequenzen braucht einen unabhängigen Standard. Zusätzlich muss die Lastvariation tatsächlich nur den modellierten Rücklauf verändern.

Für $|s|=1$, $\sigma_{\min}(K)\ge0{,}99$, $|\gamma|=0{,}5$ und Rohfehler $\epsilon\le10^{-11}$ liegt $\|\widehat B\|$ über $0{,}4949999986$, und der Fehler von $r_S$ bleibt unter $8{,}082\cdot10^{-11}$. Mit absoluten Quell- und Lastkalibrierfehlern von jeweils höchstens $9\cdot10^{-11}$ ergibt sich für die zwei Wellenstandardspalten insgesamt eine Frobenius-Fehlergrenze unter $2{,}868\cdot10^{-10}$. Dies reicht im vorherigen Rechenbeispiel für die Grenze von $3\cdot10^{-10}$. Solche absoluten und komplex relativen Fehler sind an den gewählten Referenzebenen beizulegen. Eine nominell identische Quelle ersetzt diese Prüfung nicht.

## Mechanische Mindestanforderungen für das gewöhnliche Momentprofil

Im [longitudinalen Zweikomponentenmodell](OP5_J_Halterung_Spannungsbilanz.md) sei $u=\nabla\varphi$ die Verschiebung der ersten Komponente und $-u/c$ die der zweiten. Mit $D_\rho=\rho_1-\rho_2/c\ne0$ gilt $\delta\rho=-D_\rho\operatorname{div}u$ und bei kompaktem Potential $\Phi=-4\pi G D_\rho\varphi$. Somit ist $\int u_r\,dz=\bar a_r/(4\pi G D_\rho)$. Für isoliertes gewöhnliches $b_4$-Potential $\bar\Phi=\Phi_0 P(r^2/R_c^2)$ und Längsträger $\ell_z$ folgt aus der vorigen Untergrenze $\operatorname{TV}(P)>95915{,}31$ eine Mindestanforderung an die gewöhnliche Geometrie. Verwende $a=1/4,b=3/4$, $r_a=R_c\sqrt a$ und $r_b=R_c\sqrt b$.

Aus $\int_{r_a}^{r_b}|\bar a_r|\,dr=|\Phi_0|\operatorname{TV}(P)$ folgen die Hub- und Umfangsdehnungsgrenzen durch $\int |u_r|dz\le\ell_z\sup|u_r|$ beziehungsweise $|u_r|\le r\sup|\epsilon_{\theta\theta}|$. Für die Säulendichte $\sigma=\int\delta\rho\,dz$ im reinen $b_4$-Beitrag gilt nach radialer Poisson-Gleichung und verschwindendem Fluss an beiden Grenzen
$$
|\bar\Phi'(r)|\le
2\pi G\|\sigma\|_\infty\,\frac{\min(r^2-r_a^2,r_b^2-r^2)}{r}.
$$
Das integrierte Gewicht ist $\pi G R_c^2 I$, $I=-a\log((a+b)/(2a))+b\log(2b/(a+b))$. Da $\sigma$ an beiden Rändern null ist, gilt außerdem $\sup|\partial_r\sigma|\ge2\|\sigma\|_\infty/(r_b-r_a)$. In der linearen isotropen elastischen Halterung mit Lamé-Koeffizienten $\lambda,\mu$ ist die integrierte radiale Stützkraftdichte bis auf das Vorzeichen proportional zu $(\lambda+2\mu)\partial_r\sigma/D_\rho$.

| Isolierte Anforderung | Notwendige Untergrenze, abgerundet |
| --- | ---: |
| Radialhub $\sup|u_r|$ | $2{,}0852\cdot10^4|\Phi_0|/(G|D_\rho|\ell_zR_c)$ |
| Umfangsdehnung $\sup|\epsilon_{\theta\theta}|$ | $3{,}0530\cdot10^4|\Phi_0|/(G|D_\rho|\ell_zR_c^2)$ |
| Säulendichte $\|\sigma\|_\infty$ | $2{,}3339\cdot10^5|\Phi_0|/(G R_c^2)$ |
| Integrierte radiale Stützkraftdichte | $1{,}2752\cdot10^6(\lambda+2\mu)|\Phi_0|/(G|D_\rho|R_c^3)$ |

Hier ist $\Phi_0=\bar\Phi(0)$ ein Linienpotential in $\mathrm{m^3/s^2}$; die vier Größen haben SI-Einheiten $\mathrm m$, eins, $\mathrm{kg/m^2}$ und $\mathrm{N/m^2}$. Andere gewöhnliche Anteile können kompensieren. Die Tabelle ist deshalb eine notwendige Modellanforderung für den isolierten Kanal oder separat begrenzte Beiträge. Die Stützkraftgrenze gehört zur elastischen Route. Eine kompatible spannungsfreie Endlage hat denselben geometrischen Hub, kann aber statisch ohne diese elastische Stützkraft auskommen. Werkstoffgrenzen, zeitabhängige Ansteuerung und gewöhnliche Selektivität sind noch nicht belegt. Freie J-Ausbreitung, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte die komplexe Resonanzphase, die sichtbare Leistungsbilanz, die belastete Dreilastidentität und die normierten mechanischen Anforderungen. Qiskit wurde für diese klassischen Streu- und Materialrechnungen erwogen.

[Wolfram-Skript](op5_j_endpunktphase_laststandard_materialhub.wl) · [Tatsächliche Ausgabe](op5_j_endpunktphase_laststandard_materialhub.txt) · [Laufmanifest](op5_j_endpunktphase_laststandard_materialhub.json)
