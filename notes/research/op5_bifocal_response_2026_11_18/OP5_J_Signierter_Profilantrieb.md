# OP5 – Einseitige Antriebe und eine vorzeichenfähige Profilquelle

20. November 2026. Analytische Erkundung im Materieframe M. Das [Nullprofil im selben Messweg](OP5_J_Gleicher_Messweg_Nullprofil.md) setzt einen passend geformten äußeren Antrieb voraus. Hier wird rückwärts geprüft, ob ein überall gleichgerichteter Antrieb genügt und welche zusätzliche lokale Kraft einen vorzeichenwechselnden Antrieb im reduzierten Modell erzeugen könnte.

## Vorwissen geprüft

Der [kompakte luminale Vergleich](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Luminaler_Einstein_Kanal.md) liefert die statische Antriebsform und ihre positive Parameterwahl. Die [Antriebswirkung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Lokale_Antriebswirkung.md) setzt die Kraft $J$ von außen ein und lässt ihren materiellen Ursprung offen. Die [kompakte Ansteuerung mit Rückwirkung](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Rueckwirkung_und_Charakteristiken.md) trennt die präparierte Lösung von allgemeinen Störungen. Die lokale Suche nach Quellform, Stellgrößen und radialer Kompensation ergab im jüngsten Zweig das geformte Zielprofil. Hier werden dessen Vorzeichen- und Kontrollbedingungen abgeleitet. Im [Gesamtbild](../../../wiki/Gesamtbild.md) ist das eine vorgelagerte Frage der lokalen Auslese. Für I3 fehlt weiterhin eine eigene kosmologische Bestandsdynamik.

## Ein überall gleichgerichteter Antrieb hinterlässt einen Ausläufer

Sei $q=|\mathbf k|^2$, $a=|\mathbf k_\perp|^2$, $\alpha=Zc_h^2+3g_0^2/2>0$ und $\Omega_0>0$ die skalare Frequenzlücke. Auf dem statischen Plateau des langsameren massiven Vergleichs gilt für den präparierten Verlauf
$$
J=\frac{P_0(q,a)}{m^2}H,\qquad
P_0(q,a)=(Z\Omega_0^2+\alpha q)(m^2+r_m q)-\frac23g_m^2a^2 .
$$
Transversale Integration entspricht $a=0$. Sei $\bar J(z)=\int J(x,y,z)\,dx\,dy$ und analog $\bar h(z)$. Die stationäre Gleichung entlang dieses Fourieranteils ist
$$
(Z\Omega_0^2-\alpha\partial_z^2)\bar h=\bar J.
$$
Der massive gerichtete Zähler fällt hier weg. Für abklingende Randbedingungen ist der Kern dieser Gleichung $e^{-k_s|z|}/(2\alpha k_s)$ mit $k_s=\sqrt{Z\Omega_0^2/\alpha}$. Bei $\bar J\ge0$ und $\bar J\not\equiv0$ ist $\bar h(z)>0$ für jedes endliche $z$. Eine kompakte Quelle mit überall demselben Vorzeichen kann also in diesem Vergleich auch bei frei gewählter Form den gesamten Skalarhintergrund nicht kompakt halten. Die Aussage betrifft den integrierten Skalar, nicht unmittelbar die Phase eines einzelnen Detektors.

Liegt der Antrieb im Inneren von $[0,L]$ und $Q=\int_0^L\bar J\,dz>0$, so gilt für die beiden Endausläufer
$$
\bar h(0)\bar h(L)
=\frac{e^{-k_s L}}{4\alpha^2 k_s^2}
\left(\int e^{-k_s z}\bar J(z)\,dz\right)
\left(\int e^{k_s z}\bar J(z)\,dz\right)
\ge \frac{e^{-k_s L}Q^2}{4\alpha^2 k_s^2}.
$$
Die Ungleichung ist Cauchy–Schwarz mit dem positiven Maß $\bar J(z)\,dz$. Mindestens eines der beiden Endfelder erreicht somit $Q e^{-k_sL/2}/(2\alpha k_s)$. Eine symmetrisch auf die Mitte konzentrierte Quelle nähert im Grenzfall diese Schranke. Die Höhe einer daraus entstehenden Phasendrift hängt von der kalibrierten Antwort der Anschlüsse ab.

Für den konkreten kompakten Antrieb $P_0H/m^2$ sind zusätzlich
$$
\int e^{\pm k_s z}\bar J(z)\,dz=0,\qquad
\int e^{\pm k_m z}\bar J(z)\,dz=0,\qquad k_m=m/\sqrt{r_m}.
$$
Das folgt durch partielle Integration und die zwei Faktoren von $P_0(q,0)$ an $q=-k_s^2,-k_m^2$. Der zweite Momentensatz kennzeichnet die gewählte polynomielle Konstruktion. Er ist hier keine allgemeine Notwendigkeit für den Skalar allein. Bei gleichen Skalen fallen die beiden angezeigten Tests zusammen. Eine Quellendifferenz mit verschwindendem Querintegral bei jedem $z$ erfüllt sie identisch. Die Tests sehen nur den transversalen Nullmodus. Sie beweisen für eine beliebige Ersatzquelle keine vollständige Außenfeldkompensation.

Zwei einzeln nichtnegative Quellstellungen dürfen durchaus gleiche Ausläufer haben. Für eine glatte kompakte Zieldifferenz $\delta J=P_0\delta H/m^2$ lässt sich ein gemeinsamer positiver Sockel $J_{\mathrm b}\ge|\delta J|$ auf ihrem Träger wählen. Dann sind $J_A=J_{\mathrm b}$ und $J_B=J_{\mathrm b}+\delta J$ nichtnegativ, und die lineare **Differenz** der präparierten Felder ist kompakt. Die Ausläufer der beiden absoluten Felder sind gemeinsam und im Allgemeinen vorhanden. Ob der Sockel eine unabhängig bekannte Nullstellung für die Ausbreitung ergibt, ist separat zu prüfen. Ein einziger globaler Verstärkungsregler an einem festen einseitigen Profil erzeugt die kompakte Schaltdifferenz nicht.

## Beispiel einer lokalen Kraft mit beiden Vorzeichen

Sei $\xi$ die Auslenkung eines lokalen linearen Aktors mit positiver Trägheit $\mu_\xi$ und Steifigkeit $k_\xi$. Eine definierte nichtverschwindende Kopplung $g_\xi$ zum OP5-Skalar hätte den Ansatz
$$
\mathcal L_{\xi}=\tfrac12\mu_\xi\dot\xi^2-\tfrac12k_\xi\xi^2+g_\xi h\xi+f\xi .
$$
Hier ist $f$ eine äußere, vorzeichenfähige generalisierte Kraft. Sie erzeugt $J=g_\xi\xi$ im Skalar. Für ein Zielpaar $(h_*,J_*)$ der bisherigen gekoppelten Gleichungen setze in einer Umgebung des gemeinsamen Trägers
$$
\xi_*=\frac{J_*}{g_\xi},\qquad
f_*=(\mu_\xi\partial_t^2+k_\xi)\frac{J_*}{g_\xi}-g_\xi h_*.
$$
Damit erfüllt das Zielpaar auch die Aktorgleichung. Bei glatten kompakten Zielverläufen, verschwindenden Ausgangsdaten und konstantem $g_\xi$ in dieser Umgebung ist auch diese Kraft kompakt. Außerhalb der Zielträger können die von ihr vorgeschriebenen Verläufe zu null fortgesetzt werden. Wegen Linearität würden zwei unabhängig gewichtete, räumlich geformte Kraftprofile für Grundstellung und Änderung ausreichen. Ein gemeinsamer Verstärkungsfehler an einer bereits exakt präparierten Form skaliert deren Antwort. Ein Fehler der räumlichen Form kann dagegen Außenfelder erzeugen.

Sei $k_s^{\mathrm{stat}}>0$ eine untere Schranke der effektiven statischen Skalarsteifigkeit nach dem statischen Schur-Abgleich der übrigen Modellfelder. Die neue Potentialkopplung ist positiv kontrollierbar, wenn $g_\xi^2/k_\xi<k_s^{\mathrm{stat}}$ gilt. Das folgt aus dem Quadrat $k_\xi(\xi-g_\xi h/k_\xi)^2/2$ und der verbleibenden Skalarsteifigkeit. Die Aktorträgheit ist positiv. Diese Prüfung betrifft die quadratische Vergleichswirkung. Sie bestimmt weder den materiellen Energie-Impuls-Tensor der Ansteuerung noch die zulässige physische Größe der Kraft. Für kleineres $|g_\xi|$ wächst bei festem Zielantrieb die erforderliche Auslenkung $|J_*/g_\xi|$.

Damit ist ein vorzeichenfähiger Aktor ein bedingter Mechanismus im reduzierten Modell. Eine konkrete Kopplung $g_\xi h\xi$ aus W1/W2, die räumliche Erzeugung der beiden Kraftprofile und das Übersprechen auf die Apparatur sind weiterhin unbelegt. Für die Messung wäre der tatsächlich erzeugte Antriebsrest anhand seiner Quellform und der Endpunktantwort gegen das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) zu prüfen. Freie J-Ausbreitung im Messband, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_signierter_profilantrieb.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_signierter_profilantrieb.txt) · [Laufmanifest](op5_j_signierter_profilantrieb.json)

Wolfram prüfte die axiale Faktorisierung, Green-Normierung, die Zweiquellenidentität zur Ausläuferschranke sowie Kraft- und Energieidentitäten des Aktors symbolisch. Die stetige Schranke folgt aus dem angegebenen analytischen Argument. Das Skript ist im Notizordner mit `wolframscript -file op5_j_signierter_profilantrieb.wl` reproduzierbar. Der tatsächliche Lauf erfolgte im Connector. Qiskit wurde erwogen. Die Rechnung betrifft klassische statische Feldantwort und lokale Kraftbilanz.
