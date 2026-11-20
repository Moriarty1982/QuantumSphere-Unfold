# OP5 – Nullprofil und Krümmungsschaltung im selben Messweg

20. November 2026. Analytische Erkundung im Materieframe M. Gesucht sind zwei kontrollierte Quellenstellungen bei gleichbleibender Messachse und gleichen lokalen Hintergrundfeldern an den Enden. Die Rechnung benutzt das lineare, extern angetriebene OP5-Vergleichsmodell auf einem statischen Plateau und die geometrische Optik in erster Ordnung. Die Quelle ist im Modell frei formbar.

## Vorwissen geprüft

Der [Nullpfad-Abgleich](OP5_J_Nullpfad_Abgleich.md) zeigt, wie eine unabhängig begründete Nullstellung im gleichen Messzweig feste Anschlussfaktoren kürzt. Die [doppelte Laufzeitdifferenz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Doppelte_Laufzeitdifferenz.md) liefert die planare Yukawa-Faltung. Die [kompakte Tensorantwort](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Luminaler_Einstein_Kanal.md) beschreibt den polynomialen Antrieb eines frei gewählten glatten Profils $H$. Die [Lesart mit sichtbarem Krümmungsterm](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/832e98f0c5c9958986d22620c5e94dfae75e41be/notes/research/op5_bifocal_response_2026_11_18/OP5_J_Sichtbarer_Kruemmungsterm.md) benutzt als geometrische Kontrolle einen seitlich vollständig verschobenen Träger. Hier liegen A und B im selben Zylinder. Geändert wird nur ein querausgeglichener Profilanteil mit bestimmtem Achsenjet. Die [Randbedingungen im Gesamtbild](../../../wiki/Gesamtbild.md) ordnen die Frage der lokalen OP5-Auslese zu. I3 erfordert darüber hinaus eine kosmologische Bestandsdynamik.

## Grenze des planaren Profils

Sei $\delta\rho$ die kompakt im Inneren von $[0,L]$ getragene Dichtedifferenz im planaren statischen Vergleich, und $f=K_m*\delta\rho$ mit $K_m(z)=m e^{-m|z|}/2$. Es gilt $\int_{\mathbb R} f=\int_{\mathbb R}\delta\rho$. Links von $0$ gilt $f(z)=f(0)e^{mz}$ und rechts von $L$ gilt $f(z)=f(L)e^{-m(z-L)}$. Deshalb ist exakt
$$
\int_0^L f(z)\,dz=\int_0^L \delta\rho(z)\,dz-\frac{f(0)+f(L)}{m}.
$$
Bei gleicher gesamter D-Säule und gleichen statischen Vermittlerfeldern an beiden Enden verschwindet der führende planare Laufzeitkontrast. Eine reine axiale Umverteilung bei dieser Doppelbedingung kann ihn im linearen planaren Modell nicht schalten. Eine Änderung der Gesamtsäule oder eine andere Auslesung, etwa die transversale Krümmung, ist erforderlich.

## Querprofil mit gemeinsamem Träger

Wähle $p(z)\ge0$ glatt, kompakt in $d<z<L-d$ und mit positivem Integral. Mit $s=(x^2+y^2)/R^2$ sei $\chi(s)\ge0$ ein glatter Zuschnitt, der für $0\le s\le s_0$ identisch eins ist, danach bis $s_1>s_0$ abfällt und außerhalb verschwindet. Definiere
$$
\kappa=\frac{\int_0^\infty s^2\chi(s)\,ds}{\int_0^\infty s^3\chi(s)\,ds},\qquad
\psi(s)=\chi(s)(s^2-\kappa s^3),
$$
$$
H_A=-A_Hp(z)\chi(s),\qquad H_B=-A_Hp(z)[\chi(s)+a\,\psi(s)]
$$
mit $A_H>0$ und $a\ne0$. Bei hinreichend kleinem $|a|$ bleiben die beiden radialen Profile nichtnegativ, da das Polynom auf dem gemeinsamen kompakten Träger beschränkt ist. Beide Stellungen benutzen dieselbe Achse, denselben Längsschnitt und dieselbe Endgeometrie. Ihr Querintegral $\pi R^2\int H_i(s,z)\,ds$ stimmt für jedes $z$ überein. Bei einem lokalen linearen Antrieb mit konstanten Koeffizienten verschwindet auch das Querintegral der Antriebsdifferenz. Querableitungen integrieren sich wegen des kompakten Trägers weg, und reine Längs- und Zeitableitungen wirken auf das verschwindende Querintegral. Das ist ein Abgleich von Profil- und Antriebsintegralen. Energie und physische D-Masse sind damit unbestimmt.

Für das lineare gekoppelte Modell ist die Konstruktion zulässig, wenn beide Stellungen mit ihren jeweiligen polynomialen Antrieben erzeugt werden. Eine gemeinsame glatte zeitliche Aktivierung lässt sich vorsehen, und die Auslese erfolgt auf den statischen Plateaus. Die massive Antwort bleibt durch die vorausgesetzte inverse Quellkonstruktion auf den kompakten Bereich mit seinem Ableitungsträger beschränkt. Die konforme Einstein-Krümmung des Vergleichs ist ebenfalls kompakt. Die direkten Hintergrundbeiträge an beiden Enden verschwinden so in beiden Stellungen einschließlich aller lokalen Ableitungen. Das setzt die genaue polynomielle Ansteuerung des reduzierten Modells und die zugehörigen retardierten Anfangsdaten voraus.

## Nullstellung und Signal

Im zentralen flachen Teil der A-Stellung gilt $\Delta_\perp H_A=0$. Der für die vorherige Gezeitenrechnung maßgebliche massive Eintrag $f_A=\Delta_\perp H_A/m^2$ verschwindet dort. Die longitudinale Antwort hat keine lineare Krümmung und der axiale konforme Gezeitenbeitrag ist eine integrierte Randableitung. A ist daher im betrachteten axialen RFF- und Dirac-Schwellenmodell nach Abzug der festen Grundübertragung eine bekannte Nullstellung in erster Ordnung. Das gilt auch für gerade, zur Achse parallele Teststrahlen, die im flachen Kern bleiben. Der RFF-Term bezeichnet hier die Kopplung von linearer Krümmung an zwei Feldstärken.

B hat auf der Achse weiterhin denselben Profilwert und dasselbe $\Delta_\perp H$ wie A. Die Änderung beginnt quer in vierter Ordnung. Für jede transversale Einheitsrichtung $e$ gilt auf der Achse $\partial_e^2\Delta_\perp\psi=32/R^4$. Somit erhält der Krümmungsteil pro transversaler Polarisation den Kontrast
$$
\Delta\mathcal I
= -\frac12\int\partial_e^2(f_B-f_A)\,dz
=\frac{16 A_H a}{m^2 R^4}\int p(z)\,dz.
$$
Dieser Ausdruck ist ungleich null. Für den reinen Riemann-Vergleich wird die differentielle Laufzeit mit der dortigen Kopplungsdifferenz multipliziert. Im auf der Achse rotationssymmetrischen Dirac-Schwellenvergleich wird der Kontrast mit der dortigen festen Ladungsmatrix und ihrem Koeffizienten multipliziert. Beide sind gesetzte Vergleichskopplungen. Ein Auslesesignal verlangt die entsprechende nichtverschwindende Modendifferenz. Der Achsenbefund erstreckt sich nicht automatisch auf den vollständigen Dirac-Schwellenoperator außerhalb der Achse.

Bei einem rotationssymmetrisch gewichteten Bündel paralleler Teststrahlen, das vollständig in $s\le s_0$ liegt, lässt sich für den reinen Riemann-Kontrast das azimutale Mittel direkt bilden. Für eine feste transversale Polarisation gilt dort
$$
\big\langle\partial_e^2\Delta_\perp\psi\big\rangle_{\rm az}
=\frac{32}{R^4}(1-9\kappa s).
$$
Bei konstantem Strahlquerschnitt in der Gezeitenregion wird der vorstehende Kontrast in der linearen Querschnittsmittelung mit $1-9\kappa\langle s\rangle$ multipliziert. Dies macht die zusätzliche Annahme eines hinreichend schmalen Bündels prüfbar. Bei Strahlanteilen am Rand des flachen Kerns, Beugung, Rückstreuung oder longitudinal veränderlichem Modenüberlapp reicht diese Formel für die gemessene Übertragungsmatrix nicht aus.

Die Nullstellung eliminiert im Modell den direkten lokalen Hintergrundwechsel an den Anschlüssen. Eine reale Quelle müsste außerdem zeigen, dass ihr Schalten die Anschlussantworten nicht über sichtbare Hilfsfelder, Mechanik, Beugung oder Rückstreuung verändert. Solche Beiträge und Terme höherer Ordnung gehören in das [A/B-Fehlerbudget](OP5_J_AB_Fehlerbudget.md). Die Konstruktion liefert eine bekannte Null im angesetzten linearen Modell. Eine native Realisierung der Quellform, eine kalibrierte Apparatur, freie J-Ausbreitung im Messband und H96 bleiben offen.

## Rechenkontrolle

[Wolfram-Skript](op5_j_gleicher_messweg_nullprofil.wl) · [Tatsächliche Print-Ausgabe und Rückgabewert](op5_j_gleicher_messweg_nullprofil.txt) · [Laufmanifest](op5_j_gleicher_messweg_nullprofil.json)

Wolfram prüfte die planare Faltung, die Momentenkompensation, den Achsenjet und das azimutale Mittel symbolisch. Die scharfe Scheibe im Skript dient ausschließlich als algebraische Momentenprobe. Die Konstruktion verwendet einen glatten Zuschnitt. Das Skript ist im Notizordner mit `wolframscript -file op5_j_gleicher_messweg_nullprofil.wl` reproduzierbar. Der tatsächliche Lauf erfolgte im Connector. Qiskit wurde erwogen. Die tragenden Aussagen sind klassische Differential- und Integralidentitäten ohne definierten Schaltkreis.
