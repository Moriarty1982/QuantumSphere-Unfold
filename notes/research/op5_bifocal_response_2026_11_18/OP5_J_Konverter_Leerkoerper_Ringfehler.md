# OP5 – Konverterlast, Leerkörpermonitor und lokale Annulusfehler

21. November 2026. Analytische Erkundungen im Materieframe M. Fortgesetzt werden der [additive Laststandard, der Direktmonitor und der kompensierte Annulus](OP5_J_Laststandard_Monitor_Annulus.md). Die Rechnung prüft realisierbare abstrakte Messstrukturen und ihre Restfehler. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft sie die lokale Auslese. I3 erfordert eine eigenständige kosmologische Bestandsdynamik.

## Ein idealer Modenkonverter ersetzt den schwachen additiven Lastansatz

Ein separat kalibrierter, reflexionsfreier, reziproker und verlustloser Zweimodenkonverter mit Vorwärtstransport $U$ hat Rückwärtstransport $U^{\mathsf T}$ in den passenden reziproken Portbasen. Setze an seiner Ausgangsebene nur im A-Kanal einen bekannten Spiegel $\gamma P_A$. Der am Eingang wirkende Lastblock lautet
$$
\Gamma=\gamma U^{\mathsf T}P_A U=\gamma uu^{\mathsf T},\qquad u^{\mathsf T}=e_A^{\mathsf T}U .
$$
Wenn die A-Ausgangszeile genau $e^{i\varphi}e_J^{\mathsf T}$ ist, wirkt am Eingang die J-Last $\gamma e^{2i\varphi}P_J$. Ihr Betrag wird vom Spiegel bestimmt. Das ist eine andere Streustruktur als die additive Summe zweier schwacher H/HCl-Kontakte. Ein reiner A-Spiegel allein setzt keinen J-Laststandard. Der Konverter müsste selbst einen kohärent kalibrierten J-Modenport sowie vernachlässigbare oder bekannte Reflexionen und Verluste nachweisen.

Sei der Leckeintrag $|u_A|\le p$ und $u_J=e^{i\varphi}\sqrt{1-|u_A|^2}$. Nach Abzug der kalibrierten Lastphase beträgt bei reziproker Umwandlung der Fehler der effektiven Einwegamplitude höchstens
$$
d_t=p|t_A|+(1-\sqrt{1-p^2})|t_J|.
$$
Bei tatsächlich bekannter Phase und normierter Zeile gilt auch $\|uu^{\mathsf T}-e^{2i\varphi}P_J\|=|u_A|$. Die Gleichung folgt, indem man beide Phasen durch eine diagonale unitäre Kongruenz entfernt. Die verbleibende reelle symmetrische Differenz hat Eigenwerte $\pm |u_A|$.

Für die antisymmetrische Reflexionsmessung aus der [Terminierungsrechnung](OP5_J_Terminierung_Echo_Radialraster.md) ist bei $|t_J|=m$, $\|R\|\le r$ und bekanntem $|\gamma|r<1$ eine hinreichende Produktfehlergrenze
$$
2m d_t+d_t^2+(m+d_t)^2\,\frac{(|\gamma|r)^2}{1-(|\gamma|r)^2}+\frac{\epsilon}{|\gamma|}.
$$
Hier wird die Norm des gesamten Reflexionsblocks an der Konverterebene verwendet. Nur $R_{JJ}$ zu begrenzen genügt bei gemischter Last nicht. Mit $m=0{,}003$, $|t_A|\le1$, $p=9\cdot10^{-6}$, $r=0{,}1$, $|\gamma|=0{,}5$ und $\epsilon=5\cdot10^{-8}$ bleibt der Produktfehler unter $1{,}768\cdot10^{-7}$. Der frühere Ein-Prozent-Radius der korrekt verankerten Quadratwurzel ist $1{,}791\cdot10^{-7}$. Zusätzliche Last- und Phasenfehler müssen in die geringe verbleibende Reserve passen. Die Rechnung liefert einen konditionalen starken Lastweg. Der bisherige H/HCl-Nullport weist diese Konversion, die Verlustfreiheit und die J-Phase physisch noch nicht nach.

## Kalibriertransfer vom Leerkörper zum Marker

Bezeichne $B_0,B_1$ als nackte Direktwerte des Leerkörpers und des Markers und $M_j=g_jB_j$ als lokale Nebenmonitore. Ist der Leerkörperwert unabhängig ohne den zu prüfenden Rücklauf bekannt und gilt $|g_1/g_0-1|\le d$, liefert
$$
\widehat B_1=\widehat B_0\widehat M_1/\widehat M_0
$$
einen Markerstandard. Für die relativen Fehler $s$ von $\widehat B_0$ und $e_j$ von $\widehat M_j$ ist
$$
|\widehat B_1/B_1-1|\le
\frac{(1+s)(1+d)(1+e_1)-1+e_0}{1-e_0}.
$$
Mit $s=d=e_0=e_1=10^{-8}$ ist die Monitorgrenze rund $4{,}0001\cdot10^{-8}$ relativ zum nackten Markerwert. Nach der [Extrapolationsrechnung](OP5_J_Terminierung_Echo_Radialraster.md) und dem vorigen Achtphasenbudget genügt im selben Rechenbeispiel eine normierte Anzeigedifferenz $|\widehat E/\widehat B_1-1|\le4{,}3068\cdot10^{-8}$ zur getrennten Zertifizierung des für den Messkanal sichtbaren ungeschalteten Rücklaufs. Der Gewinntransfer muss Phasen- und Modenbezug des tatsächlichen Markers einschließlich des Materialwechsels erfassen. Eine zeitlich symmetrische Messfolge allein bestimmt einen festen schaltkorrelierten Übergangsfaktor nicht.

Wenn der Leerkörper selbst nur als gedresster Wert $E_0=B_0(1+\rho_0)$ vorliegt, misst der Kreuzquotient $(E_1/M_1)/(E_0/M_0)$ lediglich $(1+\rho_1)g_0/[(1+\rho_0)g_1]$. Die absolute Markergrenze braucht dann einen eigenständigen Beleg für $\rho_0$ und den Gewinntransfer. Ein gewöhnlicher Leerkörper im selben Aufbau ist deshalb zunächst ein relativer Kontrollzustand.

## Lokale Annulusgrenzen und direkt gewichtete Messung

Sei $f$ das exakt kompensierte $s^4$-Profil der Vorarbeit, $u=r^2/R_c^2$, $H=u\partial_u^2+\partial_u$. Für den reinen $b_4$-Anteil ist der relative Formfehler des Dichteabzugs bei Ringmitteln höchstens
$$
\frac1{576}\sum_i M_i B(a_i,b_i),\qquad
M_i\ge\sup_{[a_i,b_i]}|(H^5 f)'|.
$$
$B$ ist das scharfe Lipschitz-Ringgewicht der [Radialrasterrechnung](OP5_J_Terminierung_Echo_Radialraster.md). Der Nenner $576$ ist der Betrag des gewichteten Gesamtmoments. Denn die gewöhnliche $b_4$-Dichte ist proportional zu $H^5 f$ und $\int_0^1(-\log u)H^5 f\,du=-H^4 f(0)=-576$ bei kompaktem Außenprofil. Im Kern und außerhalb des Annulus verschwindet die $b_4$-Dichte dieses Profils. Der $b_0$- und $b_2$-Anteil braucht bei Unsicherheit in der realen Messung zusätzliche Grenzen.

Mit 32 gleichmäßig in $u$ unterteilten Annulusringen ist die rechnerische globale Formgrenze rund $2{,}113\cdot10^8$, mit lokalen Bernstein-Grenzen rund $3{,}922\cdot10^7$. Bei 128 lokalen Ringen sind es noch rund $1{,}933\cdot10^6$. Diese Zahlen sind Schranken für das Verhältnis zum reinen $b_4$-Zielwert und zeigen, dass diese Zertifizierung für prozentuale Genauigkeit unzureichend bleibt. Sie sind keine Untergrenzen für den tatsächlichen Fehler eines genauer bekannten Profils.

Ein Detektor, der direkt den logarithmisch gewichteten Ringwert $\int_{a_i}^{b_i}(-\log u)\sigma(u)\,du$ liefert, entfernt den Interpolationsfehler aus den Ringmitteln. Unabhängige räumliche Kalibrierfehler treffen aber die großen Beiträge, deren Vorzeichenwechsel das kleine Nettopotential ergeben. Die Bernstein-Abschätzung bei 128 Ringen begrenzt für diesen Entwurf das Verhältnis aus absolut gewichteter und absoluter Netto-$b_4$-Antwort auf $5{,}382\cdot10^9$. Eine hinreichende über diese Hülle angesetzte unabhängige relative Kalibriergrenze für ein Prozent Nettogenauigkeit wäre rund $1{,}858\cdot10^{-12}$. Ein gemeinsamer multiplikativer Kalibrierfaktor wirkt nur auf die Nettogröße. Ein entsprechend entworfenes gemeinsames Messgewicht, ein gewöhnlich-selektiver Gradientenkanal oder ein besser konditioniertes Kontrollprofil sind deshalb vorrangig zu prüfen. Äußere Potentialreferenz, endliche Längsgrenzen, reale J-Ausbreitung, HCl/H-Portkondition, native Metrik und H96 bleiben offen.

## Rechenkontrolle

Wolfram bestätigte Normidentität und Produktbudget der Konverterlast, den Leerkörpertransfer sowie die exakten Bernstein-Koeffizienten der lokalen Annulusgrenzen. Qiskit wurde für diese klassischen Streu- und Potentialaufgaben erwogen.

[Wolfram-Skript](op5_j_konverter_leerkoerper_ringfehler.wl) · [Tatsächliche Ausgabe](op5_j_konverter_leerkoerper_ringfehler.txt) · [Laufmanifest](op5_j_konverter_leerkoerper_ringfehler.json)
