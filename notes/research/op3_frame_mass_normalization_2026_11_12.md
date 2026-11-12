# OP3: Erst im anderen Frame rechnen, dann positive Massen auslesen?

12. November 2026. Autorenauftrag zur Frame-Prüfung und imaginären
Zwischenbeschreibung. Analytische Erkundung/Selbstprüfung, nicht blind.
Ausgangsrevision 9bece17. Keine neue H-/k-Nummer oder Simulation.
Einordnung Gesamtbild T8/T13; keine Wiederaufnahme der eingefrorenen OP5-Dynamik.

## Urteil und Vorwissen geprüft

Die Quellen enthalten bereits eine konkrete Massenprüfung nach vollständigem
komplexem Boost: r85.1/H82. Unter deren Regeln skaliert die kanonisch
normierte Fermion-Massenmatrix mit einem gemeinsamen positiven Faktor.
Das bestimmt keine Generationenstruktur und ändert keine Massenverhältnisse.
Eine bloß imaginäre Zwischenbeschreibung behebt deshalb weder die H18-
Torusgrenze noch die Rang-eins-Grenze der vorgeschlagenen Gram-Matrix.

Geprüfte Quellen:

- r33-Frame-Tabelle: Slot-Gram-Auslesung ohne äußeren C-Faktor.
- r51.1: äußere Tachyon-Abbildung R:z→iz versus Zeitumkehr T:z→bar(z);
  innere Entsprechung auf span_R(1,e7), Grenzen auf dem Farbtriplet.
- r84.3/r85.1 in `sources/research/parts/v490-post-release-layers.tex`:
  vollständiger komplexer Boost, holomorphe Adjungierte, H82-Massenterme.
- `notes/research/predictions/Ergebnis_H82_Massen_zweite_Lesart.md`,
  zugehörige Vorab-Notiz; `v4_10_0_r85/llm/k197_massen_zweite_lesart.py`.
  Quelltext geprüft, historische Ausgabe nicht als neuer Replay ausgegeben.
- `notes/research/v4_10_0_w1/Erkundung_MT_Luecke.md`, Nachträge 4/5:
  antilinearer Massenpartner nicht einfach mit reinem Tachyonbild gleichsetzen.
- `native-operator-link.tex`, `v480:native-frame-covariance` und
  `v480:native-channel-rank`; vorherige OP3-Operator-/Gram-Notizen.
- Vorwissenssuchen in predictions/, v4_10_0_w1/ und analysis/ nach
  Frame-Massen, imaginären Massen und Adjungierten.

## 1. Welche Rechnung war in welchem Rahmen?

Die bisherige Torusrechnung benutzt reelle Oktonionenkoordinaten,
ein positives euklidisches Skalarprodukt und das zusätzliche H18-Gesetz.
Sie ist kein vollständig durchgeführter M→T→M-Prozess. Die r33-Quelle
nennt ihre Slotlabels frame-unabhängig, weil deren äußere Amplitudenebene
nicht eingeht. Die positiven H18-Massen sind eine nachgeschaltete Lesart.

Eine äußere Drehung z→iz muss nicht als drei innere Slotdrehungen
implementiert werden. Insbesondere würde (a,b,c)→(e7 a,e7 b,e7 c) im
assoziativen farbfesten Unterraum das Produkt abc=1 auf −e7 abbilden.
Es wäre damit kein Selbstabbild des unveränderten r15-Konfigurationsraums.
Gleiche Phasendifferenzen allein beweisen hier keine zulässige Frame-Abbildung.
Bei einer bloßen Darstellung desselben Produkts muss auch die Abbildung
der Produktbedingung mitgeführt werden. Eine solche Abbildung ist keine
neue Konfiguration mit veränderten physikalischen Massen.

## 2. Die vorhandene komplexe Operatorprüfung

r84/r85 verwenden auf Spinorindizes S=diag(−i,i), zusammen mit der
Abbildung des Raumzeitarguments und der festgelegten holomorphen
Adjungierten. Für epsilon=[[0,1],[-1,0]] gilt direkt

$$S^{\mathsf T}\varepsilon S=\varepsilon.$$

Die beiden Faktoren −i und i multiplizieren sich im antisymmetrischen
Massenterm zu +1. Daher bedeutet der imaginäre Spinorboost in dieser
Route nicht, dass der Massenparameter selbst imaginär werden muss.
Das epsilon hier kontrahiert zwei Spinorkomponenten, keine drei Farben
oder Generationenslots. Eine gleiche Bezeichnung ersetzt diese Typtrennung nicht.

In der gewählten zweiten Lesart stehen die Kinetik mit k=a−b und die
Massenterme mit p=a+b. Hier sind k,p skalare Gewichte; p ist kein
Closure-Projektor und k nicht der Koide-Quotient. Für k>0 setzt man
psi_c=sqrt(k) psi. Dann ist für eine vorgegebene Generationsmatrix D

$$D_{\mathrm{eff}}=\frac{p}{k}D.$$

Bei den Materiegewichten der Quelle ist p=1, k=1/gamma, also
D_eff=gamma D. Dies rekonstruiert den H82-Faktor direkt aus der
kanonischen Normierung. Es benötigt weder eine Simulation noch Fits.
Die Quelle prüft so skalare Kopplungsfaktoren; eine native vollständige
Generationsmatrix D wird dadurch nicht ausgewertet.

Wichtige Grenze aus der H82-Ergebnisnotiz: Diese Reduktion der beiden
Lesarten zu einem Feld ist nicht dieselbe Operation wie die historische
M/P-Umrechnung von r19. Die gemeinsame Skalierung ist deshalb kein
allgemeines Gesetz beliebiger Frame-Wechsel.

## 3. Positive Massen und imaginäre Zwischenmatrizen

Für eine gewöhnliche komplexe Dirac-Massenmatrix mit positiver,
kanonischer Kinetik sind die positiven Massengrößen die Singulärwerte:
Die gekoppelten Links-/Rechtsgleichungen ergeben die Produkte D*D bzw.
DD*. Eine allgemeine komplexe Matrix muss keine reellen Eigenwerte haben.
Dies ist eine ausdrücklich bezeichnete effektive Lesart, keine native
Identifikation jedes im Companion Omega genannten Operators.

Wird D durch iD ersetzt, bleibt (iD)*(iD)=D*D. Die positiven Massengrößen
bleiben also gleich. Auch links-/rechtsunitäre Basiswechsel verändern
die Singulärwerte nicht. Der H82-Faktor p/k>0 skaliert sie sämtlich gleich;
der Koide-Quotient bleibt bei nichtverschwindendem Spektrum unverändert.
Ein invertierbarer bloßer Basiswechsel kann ebenfalls keinen Rang erhöhen.
Insbesondere bleibt die zuvor gefundene Rang-eins-Sperre bestehen.

Eine skalare Dispersionsgleichung mit negativem Massenquadrat ist etwas
anderes als eine komplexe Dirac-Kopplungsphase: Beim konjugierten
Dirac-Partner steht |m|², nicht einfach (im)². Tachyonische Moden aus
anderen Vorzeichenregeln müssen mit ihrer Kinetik und Rückübersetzung
separat untersucht werden. Sie liefern hier keine drei Leptonmassen.

## 4. Wo tatsächlich neue Verhältnisse entstehen könnten

Bei positiv definiten, nicht gemeinsam skalaren kinetischen Matrizen
Z_L,Z_R wäre die kanonische Kopplung stattdessen

$$D_c=Z_L^{-1/2}D Z_R^{-1/2}.$$

Nichttriviale relative Gewichte oder zusätzliche Kopplungsterme können
Singulärwertverhältnisse ändern. Das ist eine algebraische Möglichkeit,
kein in den geprüften Quellen ausgewertetes natives Gesetz auf den drei
Leptonzuständen. Wenn solche Matrizen nur aus einem gemeinsamen
Darstellungswechsel stammen, müssen auch D und die Zustände konsistent
transformiert werden; man darf nicht allein die Kinetik umgewichten.

Bei k=0 am Photon-Endpunkt ist die skalare Normierung singulär. Dort
ist D_eff=pD/k nicht definiert; der Ausdruck liefert keine endliche
Massenvorhersage und rechtfertigt keinen Grenzvergleich ohne neue Analyse.

## Ergebnis und verbleibende Pflicht

| Frage | Befund |
|---|---|
| Vollständiger komplexer Boost vorhanden? | Ja, r84/r85 unter erklärter Adjungiertenregel |
| Werden die Fermionmassen dadurch imaginär? | Nicht in dieser Route; antisymmetrische Massenterme bleiben erhalten |
| Ändert die kanonische Rückauslesung die Hierarchie? | Unter gemeinsamen H82-Gewichten nein, nur gemeinsamer Faktor |
| P-Endpunkt als Ausweg? | Normierung dort singulär, kein reguläres alternatives Massenspektrum |
| Native generationsabhängige Rückauslesung? | In den geprüften Quellen nicht ausgewertet |

Nächster enger Quellenauftrag: vorhandene kinetic-/Yukawa-/Triadenblöcke
auf eine festgelegte generationsabhängige relative Wirkung prüfen, die
nicht bloß ein Basiswechsel ist. Ohne konkrete native Z_L,Z_R,D bzw.
Operatorblöcke keine weitere Simulation und keine freie imaginäre Matrix.

QAM-Lese-MCP nicht verfügbar. Lokale read-only Suche `frame` liefert
vorwiegend Beispiel-/Frame-Deklarationen; keine spezifische verifizierte
MMA-Massenbrücke identifiziert. Keine Hash-/Replayprüfung behauptet.
Selbstprüfung der oben ausgeschriebenen Matrixidentitäten; kein neuer
Lean-/MMA-Nachweis. Keine neuen Auslöser zurückgestellter Ideen;
OP1–OP5/C5/C6/T2 und Guards unverändert.
