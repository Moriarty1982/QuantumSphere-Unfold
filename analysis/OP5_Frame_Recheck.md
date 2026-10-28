# OP5: erneute Prüfung des Frame-Übergangs

Datum: 25. Oktober 2026. Ausgangsrevision: `f2de387d66d6ab2da00ef28a14305729910d7ef1`.
Separater Forschungsversuch; keine Änderung am Paper, kein Release, keine OP-Schließung.

## Ergebnis

Der Verdacht eines unvollständig definierten Frame-Übergangs ist sachlich begründet.
Die alte OP5-Vorschrift mischt die spektrale Frequenzumrechnung, einen unabhängig
skalierten Planck-Cutoff und einen nicht entsprechend transportierten Zielwert.
Zusätzlich ist ihre gedruckte Regularisierung am Ursprung falsch.

Eine vollständige, invertierbare Umrechnung desselben wohldefinierten Observablen
kann einen vorhandenen Bilanzdefekt aber nicht verschwinden lassen. Die konkret
vorgeschlagene Ersetzung von gamma_L durch exp(eta) schließt auch die alte
Zahlengleichung nicht. Eine neue physikalische Bilanz ist mit den vorhandenen
Angaben nicht eindeutig bestimmt.

## Prüfumfang und Quellen

- Ursprüngliche OP5-Bilanz: `sources/research/parts/v470/23_physical_readouts.tex`,
  `def:tr-balance`, `rem:regularization-B`, `def:theta-sum-B`.
- Korrekturschicht: `sources/research/parts/v480-post-release-layers.tex`, r05.
- Neuere Frame-Konvention: `sources/research/parts/v490-post-release-layers.tex`,
  r18, r24 und r61.
- Getrennte Ableitung: [Frame-Kovarianz](OP5_Frame_Covariance_Independent.md).
- Rechnung: [Skript](OP5_Frame_Recheck.py), [Rechenvertrag](OP5_Frame_Recheck.contract.json),
  [Endergebnis](op5-frame-run-2026-10-25-final/result.json),
  [Provenienz](op5-frame-run-2026-10-25-final/manifest.json).

Dieser Versuch behandelt die historische Theta-Bilanz. Er setzt sie nicht mit
dem C5-Fit-Score oder dem HC/MM-Kartenzertifikat gleich.

## 1. Konsistenter passiver Frame-Übergang

Für einen positiven endlichen Frequenzfaktor a fordert die unveränderte Phase

\[
\omega'=a\omega,\quad t'=t/a,\quad L'=L/a,\quad dt'=dt/a.
\]

Mit einem zusätzlich ausdrücklich deklarierten Amplitudenfaktor b gilt

\[
\Sigma'(t')=b\Sigma(at'),\quad I'=\frac ba I.
\]

Die rechte Seite einer Bilanz muss denselben Faktor erhalten. Daher gilt für
den Defekt Delta=I-B: Delta'=(b/a)Delta. Bei endlichem a und b ungleich null
bleibt die Aussage Delta=0 invariant. Das ist eine algebraische Folgerung,
kein Ergebnis aus einer endlichen Stichprobe.

Bei B=qL² erfordert dies q'=abq. Ein unverändert eingesetzter dimensionsloser
Readout beta² ist nicht automatisch ein solcher Koeffizient.

Die historische Wahl omega'=omega/g bei gleichzeitigem L'=g^(-3/2)L ist
nicht allein die passive Umrechnung einer konjugierten Zeitkoordinate.
Eine eigene physikalische Cutoff-Regel kann andere Gewichte haben. Dann müssen
die Bedeutung von t, die Umrechnung von Länge in Zeit, c und die verwendeten
Einheiten angegeben werden. Das ist eine zusätzliche Modellvorgabe.

## 2. Konkreter Regularisierungsfehler

Die definierte alte Funktion hat die Entwicklung

\[
R(t)=-\frac{e^{-t/2}}{e^t-1}
=-\frac1t+1-\frac{11}{24}t+\frac18t^2+O(t^3).
\]

Der Integrand 1+R divergiert also wie -1/t. Sein Integral von epsilon bis L
enthält +log(epsilon). Die gedruckte Addition eines weiteren +log(epsilon)
verdoppelt die Divergenz. Korrekt wäre hier die Subtraktion von log(epsilon/mu)
bei ausdrücklich festgelegtem Maßstab mu. Auch die alte gedruckte Reihe passt
nicht zur definierten Funktion.

Für die korrigierte Dichte M-Z unterhalb log(2) gilt hingegen

\[
M(t)-Z(t)=-\frac1{2t}+\frac74+\frac{t}{48}+\frac9{32}t^2+O(t^3).
\]

Das benötigt bereits einen anderen Gegen­term. Ein fester statt
mittransformierter Subtraktionsmaßstab erzeugt zusätzliche logarithmische
Terme. Diese sind kein frei einsetzbarer Frame-Ausgleich. Eine physikalische
Vorschrift müsste ihren endlichen Anteil unabhängig festlegen.

## 3. Neu berechneter diagnostischer Zahlenvergleich

Feste Eingaben: gBI=0.2375, gstring=log(2)/(pi sqrt(3)),
g=1.86444103541314, beta²=(g-1)/(g+1)=0.301783497976057,
eta=atanh(beta), h=exp(eta)=1.85418896036717.
Der Readout beta² wird beim Faktorvergleich nicht nachträglich angepasst.

| Vorschrift für Frequenz / Cutoff | Spektrale linke Seite | Alte rechte Seite | Defekt links minus rechts |
| --- | ---: | ---: | ---: |
| beide mit g | -0.109650597 | 0.893440886 | -1.003091483 |
| nur Frequenz mit h | -0.110343077 | 0.893440886 | -1.003783963 |
| nur Cutoff mit h | -0.111596388 | 0.889179598 | -1.000775986 |
| beide mit h | -0.112245936 | 0.889179598 | -1.001425535 |

Diese Tabelle testet Ersetzungen in der historischen Gleichung. Sie ist
ausdrücklich keine neue, kovariant hergeleitete physikalische Bilanz, und ihre
alte rechte Seite ist durch die fehlerhafte Regularisierung nicht legitimiert.

Die Zahlen verwenden eine zusätzlich hergeleitete geschlossene Darstellung
des spektralen Ausdrucks, bedingt auf das kritische-Linie-Spektrum und die
symmetrische spektrale Summationskonvention. Für 0<x<log(2) ist

\[
S(x)=2\sum_{\gamma>0}\frac{\sin(x\gamma)}\gamma
=J_1(x)-\frac{\log(2\pi)+\gamma_E}{2},
\]

mit u=exp(x/2) und

\[
J_1(x)=2u-2/u+\tfrac12\log\frac{u+1}{u-1}
-\arctan u-\log2+\pi/4.
\]

J_1 ist der ausdrücklich gewählte finite Anteil mit Gegen­term
-log(epsilon)/2. Der konstante Unterschied zu S ist durch die symmetrische
spektrale Normierung festgelegt, kein frei gewählter Fitparameter.
Die Herleitung und die externen Voraussetzungen stehen in der getrennten Notiz.
Für die wirklichen Zeta-Nullstellen ist die reine Ordinatendarstellung für alle
Nullstellen eine RH-abhängige Voraussetzung; allgemein steht dort die gewichtete
Spur sum exp((rho-1/2)t). Dieser Versuch beweist keine RH.

Als Gegenkontrolle wurde auch der Skalenfaktor völlig freigegeben, bei festem
beta² und historisch mitverändertem Cutoff. Numerisch findet sich dann eine
Nullstelle bei etwa 3.501051. Das ist eine Anpassung eines anderen Cutoffs mit
untransportiertem Zielwert, keine aus der Frame-Konvention abgeleitete Lösung.
Es wäre falsch, aus der Tabelle die Unmöglichkeit jeder beliebigen Ersetzung
abzuleiten; ausgeschlossen ist die Rettung durch die geprüfte vorgegebene
Ersetzung bzw. durch einen vollständigen passiven Wechsel desselben Observablen.

## 4. Referenzframe R ist nicht der Photonengrenzfall P

Nach r24.3 bezeichnet der historische endliche „Photon-Frame“ den Referenzframe
R. Der Photonenzustand P der neueren Convention F ist ein anderer Grenzfall.
Die Aussage zur Invarianz des Nullstatus gilt für endliche invertierbare
Übergänge. Für P braucht man einen eigenen Grenzzustand und ein konvergierendes,
physikalisch normiertes Observable. Das bloße Verschwinden einer unnormierten
Zahl in einem singulären Maßstabswechsel wäre kein physikalischer Abschluss.

## 5. Kontrollen, Provenienz und verbleibende Aufgabe

- 128 Nullstellen mit mpmath unabhängig erzeugt; endlicher Kovarianztest an vier
  positiven Faktoren. Fehler nach Rücktransformation kleiner als 1e-30.
- Beschleunigte Summen mit 64/128 Nullstellen als Diagnose. Keine behauptete
  rigorose Schwanzabschätzung aus einer asymptotischen Nullstellendichte.
- Stammfunktion symbolisch differenziert; die beiden Endpunktresiduen
  symbolisch geprüft. Geschlossene Darstellung gegen unabhängige Quadratur
  geprüft, Differenz kleiner als 1e-24 in den getesteten Fällen.
- Geschlossene spektrale Darstellung mit 35 und 55 Dezimalstellen verglichen;
  Abweichung für die historische Zeile etwa 3.1e-36. Das ist numerische Stabilität,
  keine Aussage über die Wahrheit der spektralen oder physikalischen Prämissen.
- Ein Paarungstest auf dem kompakten primfreien Intervall [0.08,0.2] prüft
  den Jacobian unabhängig von der Endpunktregularisierung. Die verwendete
  endliche Polynom-Testfunktion dient hier nur der Quadraturkontrolle, nicht
  als Beweis für sämtliche Voraussetzungen einer expliziten Formel.
- Finaler Rechenlauf mit Manifeststatus `completed`; Manifest mit aktuellem
  Projektwurzelpfad validiert. Ältere Läufe dokumentieren ältere Skriptstände.
- Getrennte strukturelle Ableitung in einem Subagenten; abschließender
  Selbstcheck durch den koordinierenden Agenten. Kein externer Peer Review.

Die physikalische Neuformulierung benötigt weiterhin: die Identifikation des
Spektrums, eine regulierte Testfunktion mit definierter Metrikabhängigkeit,
Cutoff und Einheiten, eine unabhängig fixierte Subtraktion sowie eine begründete
Abbildung des Resultats auf Lambda. Diese Daten lassen sich nicht eindeutig
aus der alten Bilanz oder den QAM-Tags rekonstruieren.

Der nächste sinnvolle Schritt ist deshalb ein Vertrag für genau dieses
Observable und seinen R- oder P-Frame. Eine ausgiebigere Suche nach passenden
Umrechnungsfaktoren würde die fehlende Definition nicht ersetzen.

## Externe Quellenprüfung

Geprüft am 25.10.2026: Jeffrey C. Lagarias, *The Riemann Hypothesis: Arithmetic
and Geometry*, Clay Mathematics Proceedings 6 (2006), S.127–141, insbesondere
Theorem 3.1, S.132, und gepaarte Hadamard-Faktorisierung, S.133,
[Verlagsexemplar](https://www.claymath.org/library/proceedings/cmip06.pdf#page=148).
Die Quelle wurde als vollständiges PDF geöffnet und die betreffenden Abschnitte
gelesen. Sie liefert die explizite Formel für geeignete Testfunktionen und das
gepaarte Produkt; sie beweist keine physikalische OP5-Identifikation.
Die Übersetzung in eine reine Frequenzspur ist hier ausdrücklich bedingt.
Ergänzend: [NIST DLMF 25.4](https://dlmf.nist.gov/25.4) für xi-Konventionen.
Kein lokal behaltenes vollständiges PDF, daher kein lokaler Quellhash.

Die auffindbaren Ausschnitte von Conrey (AMS 2003) wurden nur zur Orientierung
verwendet; der direkte PDF-Abruf wurde abgewiesen und gilt nicht als selbständig
authentifizierter Volltext. Keine Neuheitsbehauptung.
