# OP5 – Quadrupolkompensation bei erhaltenem Achsenkontrast

20. November 2026. Analytische Erkundung im Materieframe M, nach Merge von [PR #209](https://github.com/Moriarty1982/QuantumSphere-Unfold/pull/209). Gesucht ist ein schaltbares Querprofil, dessen direkter gewöhnlicher W2-Restmassenbeitrag den Achsenkontrast ohne äußeren Newton-Multipol begleitet. Verwendet werden der statische, konstantkoeffizientige OP5-Antriebsoperator und die direkte W2-Dichtevariation bei festem Higgsradius $v$.

## Vorwissen geprüft

Das [Nullprofil](OP5_J_Gleicher_Messweg_Nullprofil.md) hält mit einer quer kompensierten Änderung das Querintegral und die direkten OP5-Hintergrundfelder an den Enden fest. Der [W2-Dichteantrieb](OP5_J_W2_Dichteantrieb.md) zeigt, dass sein bisheriges Profil trotzdem einen direkten gewöhnlichen Quadrupol erzeugt. Die [signierte Profilquelle](OP5_J_Signierter_Profilantrieb.md) gibt den statischen Operator $P_0/m^2$ an. Im [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md) ist eine verbleibende Änderung von Sender oder Empfänger separat zu kalibrieren. Diese Erkundung gehört weiterhin zur lokalen Auslese im [Gesamtbild](../../../wiki/Gesamtbild.md). Sie bestimmt keine Populationsdynamik für I3 und keinen neuen Messwert für H96.

## Kompaktes Laplace-Profil

Rückwärts genügt für den direkten gewöhnlichen Dichtebeitrag die Quellenform $\delta\rho=\Delta B$ mit glattem kompaktem $B$. Dann löst $4\pi G B$ die statische Poisson-Gleichung $\Delta\delta\Phi=4\pi G\,\delta\rho$ mit verschwindendem Potential am räumlichen Unendlichen. Die abklingende Lösung ist eindeutig. Man braucht deshalb keine Folge einzelner Multipolkompensationen.

Sei $s=(x^2+y^2)/R^2$. Wähle eine glatte nichtnegative radiale Abschneidefunktion $\chi(s)$, die um die Achse identisch eins ist und außerhalb eines endlichen Radius verschwindet. Mit $M_j=\int_0^\infty s^j\chi(s)\,ds$ setze
$$
\kappa=\frac{M_3}{M_4},\qquad
V=-\frac{A_H a R^2}{36}\,p(z)\chi(s)(s^3-\kappa s^4),\qquad
\delta H=\Delta V.
$$
Dabei ist $p$ glatt und kompakt in der Streckenmitte, mit positivem Integral. Die transversale Integration von $V$ ergibt in jeder Querebene null. Für $\delta H$ gilt dasselbe, weil das transversale Integral von $\Delta_\perp V$ verschwindet und $\partial_z^2$ auf das verschwindende Integral von $V$ wirkt. Das frühere Abgleichkriterium bleibt erfüllt. Die Änderung kann im Inneren des Trägers der Grundstellung platziert werden. Bei hinreichend kleinem $|a|$ bleiben beide Profilstellungen dort von demselben Vorzeichen, wenn die Grundstellung auf dem Träger der Änderung strikt von null getrennt ist. Die Konstruktion verwendet ein kompakt getragenes Potential $V$, keinen unendlichen transversalen Ausläufer.

Der statische Antriebsoperator $\mathcal P=P_0/m^2$ ist ein Polynom in räumlichen Ableitungen mit konstanten Koeffizienten. Daher
$$
\delta J=\mathcal P\,\Delta V=\Delta(\mathcal P V),\qquad
\delta\rho_{\rm direkt}=\delta\epsilon_{\rm mat}|_v=-v\,\delta J .
$$
Unter der bedingten Identifikation des Zielantriebs mit der direkten radialen W2-Quelle erhält man in natürlichen Einheiten für den direkten Newton-Beitrag
$$
\delta\Phi_{\rm direkt}=-4\pi Gv\,\mathcal P V .
$$
Außerhalb des kompakten Trägers verschwindet dieses Potential einschließlich seiner Ableitungen. Äquivalent liefert partielle Integration $\int Y\,\delta\rho_{\rm direkt}=0$ für jedes harmonische Polynom $Y$. Neben Monopol, Dipol und Quadrupol verschwinden damit alle äußeren Newton-Multipole des direkten Beitrags. Die Dichtedifferenz kann beide Vorzeichen tragen. Bei kleiner Änderung um einen ausreichend positiven materiellen Referenzzustand können die absoluten Dichten in beiden Stellungen positiv bleiben.

## Achsenkontrast und endlicher Querschnitt

Im Bereich $\chi=1$ gilt $\Delta_\perp s^3=36s^2/R^2$ und $\Delta_\perp s^4=64s^3/R^2$. Darum beginnt das neue Profil auf der Achse mit
$$
\delta H=-A_Ha\,p(z)s^2+O(s^3).
$$
Der Beitrag von $\partial_z^2 V$ beginnt erst bei $s^3$. Die Änderungen des Achsenwerts und von $\Delta_\perp H$ auf der Achse sind null. Zugleich bleibt für jede transversale Einheitsrichtung $e$ der lineare Gezeitenkontrast
$$
-\frac{1}{2m^2}\int\partial_e^2\Delta_\perp\delta H(0,z)\,dz
=\frac{16 A_H a}{m^2R^4}\int p(z)\,dz
$$
gleich dem früheren Resultat. Die Nullstellung mit flachem Querprofil bleibt im angesetzten linearen Vergleich erhalten. Ein tatsächlich differentielles Signal setzt wie zuvor eine nichtverschwindende Modendifferenz der effektiven Kopplungsmatrix voraus.

Für ein rotationssymmetrisch gewichtetes Bündel paralleler Teststrahlen innerhalb des flachen Zuschnitts, mit konstantem Querschnitt über die aktive Länge, kommt im reinen Riemann-Vergleich der Mittelungsfaktor $1-16\kappa\langle s\rangle$ hinzu. Der Anteil mit $p''(z)$ integriert sich dabei zu null. Der Faktor gilt für die lineare Strahlmittelung. Beugung, Änderungen der Modenüberlappung und die volle Wirkung außerhalb der Achse bleiben gesonderte Aufgaben.

## Reichweite der Kompensation

Das Ergebnis bezieht sich auf den **direkten statischen Restmassenbeitrag bei festem $v$**. Die Halterungen, weitere Zustands- und Stressvariationen und die Einschaltstrahlung sind eigene Quellen. Für einen zusätzlichen skalaren Newton-Quellterm derselben Form $Q(\partial)\delta H$ mit lokalem konstantkoeffizientigen Operator $Q$ gilt die gleiche Kompaktheitsrechnung. Ein solcher Zusammenhang müsste für die tatsächliche Halterung erst hergeleitet werden. Die Identifikation von Higgsradius und gerichtetem OP5-Profilfeld bleibt ein offener Guard. Native Kopplung, freie J-Ausbreitung und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_quadrupol_kompensation.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_quadrupol_kompensation.txt) · [Laufmanifest](op5_j_quadrupol_kompensation.json)

Wolfram prüfte Achsenprofil, Azimutalmittel, Momentenkompensation, die Kommutation der beiden Operatoren sowie zwei harmonische Momente. Die Aussage für alle äußeren Multipole folgt aus der analytischen Poisson-Identität. Das Polynom mit endlicher Glattheit im Skript ist eine Momentenprobe. Die Konstruktion benutzt einen glatten Zuschnitt. Lokal reproduzierbar im Notizordner mit `wolframscript -file op5_j_quadrupol_kompensation.wl`. Ausgeführt wurde der Wolfram-Kernel über den Connector. Qiskit wurde erwogen. Die statischen Differentialoperatoren definieren hier keine Quantenschaltung.
