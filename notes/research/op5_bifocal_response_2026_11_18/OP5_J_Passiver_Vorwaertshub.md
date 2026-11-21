# OP5 – Passiver Vorwärtshub und gemeinsames Anschlussband

21. November 2026. Analytische Erkundung im Materieframe M. Geprüft wird ein passiver homogener Marker, der eine separat messbare Änderung in der Strecke erzeugt. Das skalare Schichtmodell setzt voraus, dass beide kanonischen Feldmoden im unmarkierten Bereich dieselbe Wellenzahl und Impedanz haben und ein fester Rang-eins-Projektor $P$ den Marker diagonalisiert. Damit behandelt es eine idealisierte Ausbreitungsgrenze. Unterschiedliche freie Wellenzahlen, Impedanz und Modenprofile erfordern eine gekoppelte Streurechnung.

## Vorwissen geprüft

Die [Feldreferenz](OP5_J_Feldreferenz.md) gibt den zulässigen Quotientenfehler für einen bekannten komplexen Hub. Die [HCl-Linie](OP5_J_HCl_Vektoranschluss.md) bestimmt das elektrische Dipolmoment und modelliert die Feldrichtung. Die [Anschlusskondition](OP5_J_HCl_Anschlusskondition.md) liefert das Halbfenster für getrennte H/HCl-Anschlussvolumina. Die Suche nach Vorwärtshub, Reflexion und Halbfenster im Projekt ergab bisher keine gemeinsame passive Phasen- und Verlustrechnung. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft der Schritt die lokale OP5-Auslese. I3 setzt eine eigene kosmologische Bestandsdynamik voraus.

## Einlinienantwort und exakte Schicht

Für Zeitabhängigkeit $e^{-i\omega t}$ setze im isolierten schwach angeregten HCl-Linienmodell
$$
\chi(E)=-\frac{n_{\rm eff}|d_{\rm eff}|^2}{\varepsilon_0(\Delta+i\gamma)},
\qquad \Delta=E-E_0,\quad\gamma>0 .
$$
Hier ist $n_{\rm eff}$ die effektive Teilchendichte einschließlich Besetzungsdifferenz, und $d_{\rm eff}$ ist das auf die helle Mode projizierte Dipolmatrixelement. Falls die gleiche kanonische Normierung wie beim Anschluss gilt, ist $|d_{\rm eff}|^2=|d_A|^2(1+|r_C|^2)$. Die Linie hat in diesem Modell passives Vorzeichen $\operatorname{Im}\chi\ge0$. Elektrischer Untergrund, weitere Übergänge, Dopplerstruktur und Sättigung liegen außerhalb des Einlinienansatzes. Für SI-Einsatz sind $\Delta,\gamma$ in Joule einzusetzen. Ihre Quotienten sind einheitenunabhängig.

Die dunkle Richtung bleibt im Modell frei. Für die helle Richtung sei $\widetilde n=\sqrt{1+\chi}$ auf dem passiven Ast, $k=E/(\hbar c)$, $\rho=(1-\widetilde n)/(1+\widetilde n)$ und $p_{\rm rt}=e^{2ik\widetilde n L}$. Bei Normalinzidenz, Schichtdicke $L$ und identischen Halbräumen auf beiden Seiten lauten Transmission relativ zur freien Strecke und Reflexion an der Eintrittsebene
$$
t=\frac{(1-\rho^2)e^{ik(\widetilde n-1)L}}{1-\rho^2p_{\rm rt}},
\qquad
r_{\rm slab}=\frac{\rho(1-p_{\rm rt})}{1-\rho^2p_{\rm rt}} .
$$
Die Feldmarkierung ist $I+(t-1)P$. Ohne eingespeiste reflektierte Welle liefern $|t|^2$, $|r_{\rm slab}|^2$ und $1-|t|^2-|r_{\rm slab}|^2$ die transmittierten, reflektierten und absorbierten Leistungsanteile. Mit $|p_{\rm rt}|\le1$ und $t_{\rm bulk}=e^{ik(\widetilde n-1)L}$ gilt
$$
|t-t_{\rm bulk}|\le\frac{2|\rho|^2}{1-|\rho|^2},
\qquad
|r_{\rm slab}|\le\frac{2|\rho|}{1-|\rho|^2}.
$$
Damit können Mehrfachreflexionen bei bekannter Geometrie modelliert oder gegen das Restbudget geprüft werden. Wenn allein die weggelassene Mehrfachtransmission höchstens $9{,}82\cdot10^{-6}$ beitragen darf, genügt $|\rho|\lesssim2{,}22\cdot10^{-3}$. In den Empfänger zurückgekoppeltes Licht braucht eine eigene Schranke. [Komplexe Fresnel- und Schichtrechnung](https://arxiv.org/abs/1603.02720)

## Phasenhub, Verlust und Anschlussband

In der verdünnten Näherung $\widetilde n-1\simeq\chi/2$ ergibt sich ohne die Interfacekorrektur $t_{\rm bulk}=e^{-A+i\phi}$ mit
$$
A=C(E)N\frac{\gamma}{\Delta^2+\gamma^2},\qquad
\phi=-C(E)N\frac{\Delta}{\Delta^2+\gamma^2},\qquad
C(E)=\frac{k|d_{\rm eff}|^2}{2\varepsilon_0},\quad N=n_{\rm eff}L .
$$
Der Ansatz erlaubt endliche akkumulierte Phase bei kleinem lokalem $|\chi|$. Wird er anstelle der exakten Schicht für ein Fehlerbudget verwendet, ist auch die im Exponenten akkumulierte Indexnäherung zu begrenzen. Am Linienzentrum verhält sich der Bulk-Marker als reiner Dämpfer mit Hub höchstens eins. Ein $\pi$-Phasenhub bei maximalem Amplitudenverlust $\ell$ verlangt dagegen
$$
|\Delta|/\gamma\ge D_\ell:=\pi/[-\ln(1-\ell)],\qquad
N_\pi=\frac{\pi(\Delta^2+\gamma^2)}{C(E)|\Delta|}.
$$
Dieser Quotient aus Phase und Verlust lässt sich durch Erhöhung der Säule allein nicht verbessern. Für den Referenzvergleich $\ell=0{,}01$ beträgt $D_\ell\simeq312{,}586$. Bei anderer Zielphase oder einem bewusst schwachen Hub ist der entsprechende komplexe Wert $t-1$ zu verwenden. Die Modenauswertung verlangt einen bekannten Hub bei jeder Messfrequenz und lässt insbesondere eine frequenzabhängige Phase zu.

Für die HCl-Anschlüsse aus der Vorarbeit sei $a_i s_i$ die geometrische Obergrenze der kleinsten Singulärzahl am Ende $i$. Liegt die Zielzahl darüber, ist das Anschlussfenster leer, unabhängig vom Marker. Andernfalls sei $B=\min_i b_{0,i}/b_{{\rm req},i}$ im Fall ohne Übersprechen, oder mit den in der Vorarbeit angegebenen erhöhten Zielzahlen für ein hinreichendes Fenster. Für getrennte Marker- und Anschlussvolumina mit **derselben** Linienlage und Halbbreite $\gamma$ gilt dann $|\Delta|\le\gamma\sqrt{B^2-1}$ im gemeinsamen Anschlussfenster. Für ein einseitig detuniertes Band mit halber Energieweite $h_E=h\Delta\nu/2$ und gewünschter Phasenuntergrenze $\phi_{\min}>0$ bleibt im schwach dispersiven Schichtvergleich nur dann ein Platz für das ganze Frequenzband, wenn
$$
\sqrt{B^2-1}\ \ge\
\frac{\phi_{\min}}{-\ln(1-\ell)}+\frac{2h_E}{\gamma}.
$$
Das ist eine notwendige Bedingung für die beiden angegebenen Mindestanforderungen. Bei unterschiedlichen Halbbreiten sind Markeruntergrenze und Anschlussobergrenze jeweils in Energieeinheiten zu bilden. Bei $100$ MHz gilt $h_E=2{,}0678\cdot10^{-7}$ eV. Für den zentralen Vergleich mit $\pi$ und einem Prozent Verlust verlangt bereits der Einzelfrequenzfall $B\gtrsim312{,}59$. Im früheren schwach gekoppelten Beispiel ist $a_i s_i\simeq0{,}00254$ bei $a_i=1$, während der starke Markervergleich aus dem matrixdominierten Zweilaufbudget rund $0{,}0451$ pro Ende fordert. Dieses Beispiel scheitert schon vor der Frage der Detuningreserve. [SI-Konstanten, CODATA 2022](https://physics.nist.gov/cuu/pdf/wall_2022.pdf)

Auch bei passender Bandlage muss **eine** Säule das Band treffen. Für ein Band auf einer Seite der Linie und erlaubte Phasenbeträge $[\phi_{\min},\phi_{\max}]$ schreibe $f=C|\Delta|/(\Delta^2+\gamma^2)$ und $a=C\gamma/(\Delta^2+\gamma^2)$. Der Bulk-Abgleich verlangt
$$
\sup_E\frac{\phi_{\min}}{f(E)}
\ \le N\le\
\min\left(\inf_E\frac{\phi_{\max}}{f(E)},\inf_E\frac{-\ln(1-\ell)}{a(E)}\right).
$$
Diese Schnittbedingung trennt zulässige Wahl der Säule von der rein spektralen Überlappung. Reflektierte Anteile, die nicht im gemessenen Hub erfasst sind, und zeitgleiche Nullfehler gehen wie bisher in $r_T$ bzw. $r_Q$. Beispielsweise addiert eine nicht erfasste Hubänderung $|\delta\beta|$ zum Zähler der Projektorfehlerschranke. In erster Variation des Bulkmodells gilt $|\delta\beta|=e^{-A}|i\delta\phi-\delta A|$. Unterschiedliche Anschlussfaktoren der realen Nullkontrolle bleiben ein separater Beitrag.

## Getrennter H-Marker

Ein separater off-resonanter H-Marker unterliegt nicht dem HCl-Verlustquotienten. In der verlustfreien Coulomb-Referenz der Anschlussnotiz ist die statische Polarisierbarkeit $\alpha_{\rm H}/\varepsilon_0=4\pi a_0^3(9/2)$, sofern die markierte Richtung im diagonalen schwachen Kopplungsvergleich praktisch elektrisch ist. In dieser Näherung verlangt $\pi$ bei $0{,}360329$ eV eine ideale Säule
$$
N_\pi^{\rm H}=\frac{\lambda}{\alpha_{\rm H}/\varepsilon_0}
\simeq4{,}11\cdot10^{23}\ {\rm m}^{-2},\qquad \lambda\simeq3{,}441\,\mu{\rm m}.
$$
Die Zahl bezeichnet eine integrierte Modellpolarisierbarkeit. Reale kohärente Verluste, Reflexion und räumliche Überlappung brauchen getrennte Eingaben. Dieser Weg entfernt den Zwang zur HCl-Verstimmung des **Markers**. Er erhöht die kleinste Singulärzahl der getrennten Zweikanalanschlüsse nicht. Freie gemeinsame J-Ausbreitung, reale Feldreferenz, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_passiver_vorwaertshub.wl) · [Tatsächliche Ausgabe](op5_j_passiver_vorwaertshub.txt) · [Laufmanifest](op5_j_passiver_vorwaertshub.json)

Wolfram prüfte Lorentz-Quotient und Schichtidentitäten und berechnete die Vergleichswerte. Die Band- und Säulenschnittbedingungen folgen im Text analytisch. Reproduzierbar mit **wolframscript -file op5_j_passiver_vorwaertshub.wl**.
