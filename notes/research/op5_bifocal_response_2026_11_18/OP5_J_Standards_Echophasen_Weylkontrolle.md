# OP5 – Portstandards, Echo-Phasenumlauf und Weyl-Kontrollprofil

21. November 2026. Analytische Erkundungen im Materieframe M. Die [Port-, Referenz- und Spotrechnung](OP5_J_Port_Referenz_Spot.md) benötigt unabhängig bekannte J/A-Richtungen, eine getrennte gemischte Referenzphase und eine gewöhnliche Kontrollantwort für den mit dem massiven Profil entarteten Term. Die folgenden Prüfungen begrenzen die Identifizierbarkeit dieser Größen. Im [Gesamtbild](../../../wiki/Gesamtbild.md) betrifft dies die lokale Auslese. I3 verlangt eine eigenständige kosmologische Bestandsdynamik.

## Welche Portstandards den Kreuzreflexionseintrag bestimmen

Für einen Standard $X$ in der Feldbasis sei $M_X=LXF$ die Gerätematrix. Wenn die Identitätsmessung $N=LF$ invertierbar ist, liefert $Q_X=N^{-1}M_X=F^{-1}XF$. Kalibrierung nur mit $I$ und einem unabhängig bekannten reinen A-Projektor $P_A$ unterscheidet bei exakten Daten die beiden Richtungen in Gerätekoordinaten. Für beide Standards bleiben aber alle Umdefinitionen $G=\operatorname{diag}(g_A,g_J)$ unbeobachtbar, wenn zugleich $F\mapsto GF$, $L\mapsto LG^{-1}$ und $D\mapsto GDG^{-1}$. Der gesuchte Eintrag $D_{AJ}$ ändert sich dann um $g_A/g_J$. Damit bleiben relative Normierung und Phase offen, solange keine unabhängige Fluss- oder J-Kalibrierung diese Freiheit einschränkt. Bei ausschließlich unitär erlaubtem Restwechsel wäre nur die relative Phase offen.

Ein unabhängig kalibrierter kohärenter Standard $C$ mit bekanntem $C_{AJ}\ne0$ setzt dieselbe Richtungsskala wie der gesuchte Eintrag. Für $P=Q_{P_A}$ gilt
$$
P Q_D(I-P)=\frac{D_{AJ}}{C_{AJ}}\,P Q_C(I-P).
$$
Der Quotient zweier gezielter Projektionen in unveränderten Ports liefert damit die relative Kreuzamplitude. Er setzt voraus, dass der Standard dieselben Feldmoden an denselben Referenzebenen anregt. Das ist eine Bedingung an den physischen Standard, nicht lediglich an einen Gerätepfad. Die Konstruktion mit $Q$ benötigt eine belastbare Inversion von $N$. Ohne diese kann eine bereits kalibrierte gerichtete Projektion mit Signalen $m_D=\gamma D_{AJ}+n_D$, $m_C=\gamma C_{AJ}+n_C$ verwendet werden. Mit bekanntem $C_{AJ}$ und $|n_C|$ kleiner als $|\gamma C_{AJ}|$ gilt
$$
\left|C_{AJ}\frac{m_D}{m_C}-D_{AJ}\right|
\le
\frac{|C_{AJ}|\,|n_D|+|D_{AJ}|\,|n_C|}{|\gamma C_{AJ}|-|n_C|}.
$$
Eine Unsicherheit des Standards und eine Änderung des Projektionsgewinns kommen hinzu. Bei normiertem $|\gamma|=1$, $|C_{AJ}|=0{,}01$, $|n_D|\le10^{-7}$, $|n_C|\le10^{-6}$ und $|D_{AJ}|\le10^{-6}$ beträgt das illustrative Verhältnisbudget höchstens $1{,}002\cdot10^{-7}$. Ein ausschließlich optischer A-Standard mit $C_{AJ}=0$ liefert diese Kalibrierung nicht. Die HCl/H-Projektionen könnten nur mit unabhängig belegter J-Kopplung und kontrollierter Anschlusskondition als ein solcher Standard dienen.

## Referenzkontrast und markierter Rücklauf

Schreibe den entfalteten Längenkreuzkontrast als $Y=S+H+E$, mit Nutzkontrast $S$, gemischter Referenzphase $H$ und Mehrwegphase $E$. Gleichzeitige Wiederholungen können Schwankungen beobachten. Eine konstante Umverteilung $S\mapsto S+\lambda$, $H\mapsto H-\lambda$ bleibt dabei exakt unsichtbar. Ein unabhängiger Kontrollkontrast $Z=K+H_{\rm c}+E_{\rm c}$ mit bekanntem $K$ ermöglicht $Y-(Z-K)$. Der verbleibende Fehler enthält $H-H_{\rm c}$ sowie $E-E_{\rm c}$ und die Mess- und Standardfehler. Die zwischen Signal und Kontrolle gemeinsame Phase muss dabei experimentell nachgewiesen oder als Rest begrenzt werden.

Für einen einzeln identifizierten skalaren Echo-Rundlauf $x(z)=D/(1-qz)$ mit $|q|<1$ kann ausschließlich dessen Phase $z$ gezielt verändert werden. Mittelt man die **komplexen** Signale über $m$ gleichmäßig verteilte Phasen, gibt die geometrische Reihe $\overline x=D/(1-q^m)$. Die ersten $m-1$ Rückläufe entfallen exakt. Andere Echos, Änderungen von $D$ beim Schalten und eine Änderung von $q$ zwischen den Phasenstellungen benötigen eigene Grenzen. Ein unbekannter unmodulierter Pfad fällt durch Wiederholung weiterhin nicht auf.

Bei 4 m und 100 MHz bleiben im früheren Modell rund $1{,}5211\cdot10^{-5}$ rad für zusätzliche Beiträge. Eine illustrative Aufteilung von $8\cdot10^{-6}$ rad für Referenz und Kontrolle sowie $6\cdot10^{-6}$ rad für das isolierte Echo lässt rund $1{,}21\cdot10^{-6}$ rad übrig. Für die Referenz entsprechen die $8\cdot10^{-6}$ rad vier Kontroll-Einzelphasen mit je $10^{-6}$ rad, einem Standardrest von $10^{-6}$ rad und einem Transferrest zwischen Kontrolle und Signal von $3\cdot10^{-6}$ rad. Im echoexklusiven symmetrischen Rohbudget aus der Vorarbeit entspricht der Vierphasenzyklus einer zulässigen Rundlaufamplitude von rund $0{,}08508$. Bei der engeren gemeinsamen Aufteilung genügt für ein einzelnes isoliertes Echo und zwei Phasenstellungen bei acht Signal-Rohwerten $8\arcsin(|q|^2)\le6\cdot10^{-6}$. Dies entspricht $|q|\le8{,}6602\cdot10^{-4}$. Die Echoanteile der Kontrolle müssen in deren eigener Fehlergrenze liegen.

## Kontrollprofil und die verbleibende gewöhnliche Entartung

Im [kompensierten Binnenfeldmodell](OP5_J_Binnenfeld_Messweg.md) wähle im flachen Kern eine integrierte Trägerantwort $\overline V_C=P_z c_4 s^4$, $s=(x^2+y^2)/R^2$. Das Querintegral kann im mathematischen Profil durch einen glatten Annuluszusatz außerhalb aller Spots kompensiert werden. Der Zusatz soll den Kernjet und die Anschlüsse unangetastet lassen. Für die transversale Laplace-Operation $D_\perp=\Delta_\perp$ gilt im Kern
$$
D_\perp^2s^4=2304s^2/R^4,\quad
D_\perp^3s^4=36864s/R^6,\quad
D_\perp^4s^4=147456/R^8.
$$
Die massive Gezeitenmatrix ist proportional zur Hesse-Matrix der letzten Größe und verschwindet im ganzen Kern. Der modellierte minimale massive Laufzeitbeitrag kann bestehen bleiben. Er ist im Kern polarisationsgleich und fällt im abgeglichenen radial-/tangentialen Differenzsignal heraus.

In der gewöhnlichen Metrik ist das integrierte Potential bis auf seinen Vorfaktor $(b_0D_\perp^2-b_2D_\perp^3+b_4D_\perp^4)\overline V_C$. Nur der $b_0$-Term erzeugt im Kern eine Weyl-Halbdifferenz. Sie ist, mit dem konstanten Vorfaktor der Binnenfeldrechnung und $P_zc_4$, proportional zu $18432 b_0s/R^6$. Runde Spots mitteln diese $s$-Spalte exakt wie in der Vorarbeit. Die Kontrolle könnte die gewöhnliche Ansprechempfindlichkeit für ein bekanntes $b_0$-Profil bestimmen, falls sie auf die Signalmessung übertragbar ist.

Die Kontrolle bestimmt den entarteten $b_4$-Term des Signalprofils allein nicht. In diesem Modell verwenden der $b_4$-Anteil und der massive Weyl-Anteil dieselbe spurfreie Hesse-Matrix von $D_\perp^4\overline V$. Ein Nullprofil für den massiven Weyl-Anteil schaltet also den $b_4$-Anteil zugleich aus. Um die Koeffizienten zu trennen, braucht es ein unabhängig bestimmtes $b_4$ samt gewöhnlicher Ansprechempfindlichkeit oder eine selektive Messung der gewöhnlichen Gezeiten im Signalprofil. Das gleiche $s^4$-Profil bietet im Modell einen unabhängigen Zugang: Auf der Achse ist das gewöhnliche integrierte Potential bis auf den bekannten Gesamtfaktor proportional zu $147456 b_4/R^8$. Der $b_0$- und der $b_2$-Term verschwinden dort. Eine gewöhnlich-selektive Messung dieser Achsengröße oder eine unabhängige Bestimmung aus der gewöhnlichen Dichte kann daher den benötigten $b_4$-Faktor prüfen. Der minimale massive Anteil ist auf der Achse polarisationsgleich, aber nicht zwingend null. Ein unkalibrierter A/J-Laufzeitvergleich ist daher kein solcher Standard.

Zusätzliche lokale Operatoren und die native effektive Vermittlermetrik bleiben offen. Freie J-Ausbreitung und H96 bleiben offen.

## Rechenkontrolle

Wolfram prüfte die Diagonalfreiheit, den Kreuzstandard, die Verschiebung der Referenzphase, den Vierphasen-Mittelwert und die Laplace-Jets der gewöhnlichen Weyl-Kontrolle. Qiskit wurde bei der Werkzeugwahl erwogen. Die Rechnungen benötigen klassische Übertragungs- und Profilkoeffizienten.

[Wolfram-Skript](op5_j_standards_echophasen_weylkontrolle.wl) · [Tatsächliche Ausgabe](op5_j_standards_echophasen_weylkontrolle.txt) · [Laufmanifest](op5_j_standards_echophasen_weylkontrolle.json)
