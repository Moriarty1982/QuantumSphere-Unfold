# OP5, kosmologische Konstante und ein relationaler neutraler Bezug

Checkpoint: `OP5-LAMBDA-NEUTRAL-2026-10-25`.
Quellbasis: `f2de387d66d6ab2da00ef28a14305729910d7ef1`.
Status: Forschungsneueinordnung mit exakten Vergleichskonstruktionen und
begrenzten Rechenkontrollen. Keine Integration ins Paper, keine neue
Frame-Konvention, kein neuer DOI und keine OP5-Schließung.

## Auftrag und Ergebnis

Ausgehend von der früheren Annahme „Photon-Frame = neutral“ wurde die
OP5-Kette bis zur behaupteten kosmologischen Konstante zurückverfolgt.
Untersucht wurde, ob Neutralität stattdessen aus mindestens zwei verglichenen
Frames/Zuständen entstehen kann.

**Ergebnis:** Ein relationaler neutraler Bezug ist konstruierbar. Innerhalb
des aktuellen realen Zustandsdisks lässt sich sogar der symmetrische Zustand
I/2 aus zwei entgegengesetzten Zuständen erzeugen. Das ist aber eine Mischung,
nicht dasselbe wie der Mittelpunkt zweier Skalenframes oder ein flussfreier
Raumzeitbeobachter. Die drei Begriffe dürfen nicht identifiziert werden.

Die historisch behauptete Folgerung „Offset im neutralen Frame null, deshalb
fundamentales Lambda null“ trägt nicht. Ein verschwindender erster Moment
beseitigt weder einen quadratischen Rest noch die konstante Dichte einer
vollständigen Wirkung. Die erste fehlende physikalische Brücke liegt bereits
zwischen Spektralspur und metrikabhängiger Wirkung.

Eine tragfähigere Arbeitsrichtung ist:

```text
zwei native Zustände + begründete Vergleichs-/Mischregel
    -> relationaler neutraler Bezug N und relatives Datum chi
    -> dimensionsloser Readout q_rel
    -> gemeinsame metrikabhängige Wirkung [noch herzuleiten]
    -> konstante Dichte rho und Einstein-Koeffizient A
    -> Lambda_cos = rho/(2A) [unter der angegebenen Konvention].
```

## 1. Die Herkunft der früheren Lambda-Aussage

Die vollständigen Belege und Quellenfingerabdrücke stehen im
[Abhängigkeitsaudit](OP5_Lambda_Dependency_Audit.md).

| Pfeil der alten Herleitung | Befund |
| --- | --- |
| Dilationoperator und Nullstellenspektrum -> Tr exp(-it L0) | Eine spektrale Modellzuordnung; vierdimensionale Metrikabhängigkeit, Operatorbereich und Spurregularisierung fehlen für die gravitative Anwendung. |
| Spur -> ungewichtete Wirkung int Sigma(t)dt | Als Wirkung nicht definiert; unitäre Spur und Wärmekern wurden verwechselt. In r05 bereits zurückgestuft. |
| Drei Spuranteile -> Lambda, Materiestress und Einstein-Tensor | Strukturelle Zuordnung, keine ausgerechnete Metrikvariation. Die ursprüngliche Spurzerlegung wurde korrigiert. |
| Erster Nullstellenwert -> nacktes Lambda ~ gamma_1² | Als Herleitung zurückgezogen; folgt nicht aus dem korrigierten Polterm. |
| L_frame=beta²<f,f> -> beta² g_mu_nu | Eine definierte interne Größe; die behauptete Variation benötigt Maß, Normierung, unabhängige Felder und Metrikabhängigkeit. |
| beta=0 -> gesamte kosmologische Konstante null | Nur der so definierte Offsetterm verschwindet. Der Schluss auf alle Vakuum-/Wirkungsbeiträge folgt nicht. |
| beta²/ellP² -> beobachtetes Lambda | Einheiten passend, Zahlenwert bei historischen Eingaben um etwa 10^121 zu groß. Ein anderer Bezugspunkt entfernt diese dimensionslose Hierarchie nicht. |

Die Quelle nennt schon in `thm:lambda-zero` als Grund für beta=0 die
Definition des damaligen Photon-Frames. Damit wird ein Nullpunkt gesetzt,
nicht die vollständige gravitative Vakuumwirkung berechnet.

## 2. Drei genaue Bedeutungen von Neutralität

### 2.1 Relationaler Mittelpunkt auf der realen Skalenlinie

Für zwei endliche reelle Skalenkoordinaten eta_1 und eta_2 auf derselben
orientierten Linie sei

\[
\eta_N=\frac{\eta_1+\eta_2}{2},\qquad
\delta=\frac{\eta_1-\eta_2}{2}.
\]

Beide Zustände haben gegenüber N die Offsets +delta und -delta; die
Skalenfaktoren exp(k delta) und exp(-k delta) sind reziprok. Bei einem
gemeinsamen Shift eta_i -> eta_i+a verschiebt sich N mit, delta bleibt fest.
Das äquivalente positive Referenzmaß ist das geometrische Mittel der beiden
Skalen. Für diese Konstruktion muss keiner der Eingangsframes photonartig sein.

Die Wahl gleicher Rapiditätsabstände ist eine zusätzliche Symmetrieregel.
Austauschsymmetrie und Shift-Kovarianz allein bestimmen den Mittelpunkt noch
nicht eindeutig; Gewichte, nichtkollineare Fälle und die Metrik der Skalenlinie
müssen gegebenenfalls zusätzlich festgelegt werden. Ein gewöhnlicher
zeitartiger Lorentz-Beobachter ist damit noch nicht aus den internen Daten
hergeleitet. Insbesondere ist die native komplexe Tachyonrapidität nicht
stillschweigend eine zweite reelle Beobachterrapidität.

### 2.2 Symmetrische Mischung auf dem realen Zustandsdisk

Auf dem im Projekt verwendeten realen Disk gilt

\[
\rho(b_z,b_x)=\tfrac12(I+b_z\sigma_z+b_x\sigma_x).
\]

Die korrigierte native Tachyon-/Dualitätsabbildung r28 liefert dort

\[
\rho_T=\sigma_y\rho\sigma_y=\rho(-b_z,-b_x),\qquad
\frac{\rho+\rho_T}{2}=\frac I2.
\]

Damit wird die Idee eines erst aus zwei Zuständen entstehenden symmetrischen
Gesamtzustands **konkret realisiert**, unter der Voraussetzung gleicher Gewichte
und der richtigen Abbildung. Bei Gewicht w statt 1/2 bleibt der Bloch-Vektor
(2w-1)b. Gleichgewichtige Mischung ist daher eine zu begründende Operation.

Die frühere Abbildung J_B=sigma_x reicht allgemein nicht: Sie ergibt
rho(-b_z,b_x), und ihre Mischung mit rho behält b_x. Bei b=(0.3,0.4)
bleibt beispielsweise der Kompensatorport mit 0.7 gegenüber 0.3 besetzt.
Das ist nicht I/2. Auf einem allgemeinen dreidimensionalen Bloch-Ball würde
auch sigma_y die y-Komponente nicht umkehren; die Disk-Einschränkung ist nötig.

Eine inkohärente Mischung oder ein reduzierter Zustand ist kein invertierbarer
Frame-Wechsel. Eine kohärente Überlagerung würde zusätzliche Phasen-/Präparations-
daten benötigen. Der neutrale Mischzustand I/2 hat das P-Etikett der aktuellen
Convention F; der historische Referenzframe R ist dagegen rein. Diese
verschiedenen Ausgaben können nicht durch das gemeinsame Wort neutral
gleichgesetzt werden.

### 2.3 Gemeinsamer flussfreier Raumzeitbeobachter

Zwei positive, nicht parallele kausale Beiträge können einen timelike
Schwerpunkt- oder lokalen Energieframe auswählen. Das kann aus zwei
Lichtbeiträgen möglich sein, obwohl ein einzelner Lichtstrahl keinen Ruhframe
hat. Die Gewichte und die Frage „endliche Pakete oder lokale Energiedichten?“
sind entscheidend. Die getrennte [Kandidatennotiz](OP5_Neutral_Frame_Candidates.md)
leitet beide Fälle her und unterscheidet sie exakt.

Zwei gleich starke gegenläufige Nullströme haben im lokalen flussfreien Frame

\[
T^{\mu\nu}=\operatorname{diag}(\rho,\rho,0,0),\quad \rho>0,
\]

bei Signatur (-,+,+,+). Energie und anisotroper Druck bleiben erhalten.
Das ist nicht der Vakuumtensor diag(rho,-rho,-rho,-rho). Bei parallelen
Strahlen oder nur einem Beitrag fehlt der timelike Ruhframe. Die Konstruktion
mit positiven kausalen Strömen lässt sich nicht ohne Zusatzannahme auf einen
spacelike Tachyonvektor übertragen.

## 3. Relativen Readout statt absoluten Frame-Offsets behalten

Eine ausdrücklich **vorgeschlagene, nicht adoptierte** Neueinordnung auf der
reellen Vergleichslinie wäre

\[
\chi=\eta_1-\eta_2,\qquad
q_{\rm rel}=\tanh^2(\chi/2).
\]

Diese Größe ist unter gemeinsamem Shift und Austausch der Eingänge invariant.
Bei symmetrischen Positionen +eta und -eta gilt

\[
q_{\rm rel}=\tanh^2\eta
=\frac{\cosh(2\eta)-1}{\cosh(2\eta)+1}.
\]

Das ist genau die Form der historisch verwendeten Zahl beta_sym², wenn
gamma_L=cosh(2 eta) als Paarvergleich angenommen wird. Die Zahl müsste somit
nicht verworfen werden: Sie könnte zunächst die **relative Trennung** der
beiden Eingaben charakterisieren, statt einen absoluten Fehler eines
Materiebeobachters gegenüber einem vorab neutral genannten Photon zu bedeuten.

Das ist eine konsistente mathematische Übersetzung des Parameters. Dass die
native M/T-Abbildung diesen reellen Vergleich physikalisch realisiert, bleibt
eine eigene Brücke; auch bedeutet q_rel noch keine Energiedichte.

Im neutralen Mittelpunkt gilt zwar der mittlere vorzeichenbehaftete Offset null,
aber

\[
\frac{\tanh^2\delta+\tanh^2(-\delta)}2=\tanh^2\delta>0
\quad(\delta\ne0).
\]

Allgemein ist E[z²]=(E[z])²+Var(z). Die Energie des gemittelten Zustands
darf nicht mit der gemittelten Energie verwechselt werden. Für eine feste
lineare Energieauswertung Tr(rho H) mitteln die Erwartungswerte linear;
eine Mischung positiver Energien löscht sie nicht. Eine nichtlineare
Kontrastfunktion hat nochmals eine andere Mittelungsregel.

## 4. Wann daraus überhaupt ein Lambda-Term entstehen könnte

Mit c=hbar=1 und der ausdrücklich zusätzlich angenommenen Wirkung

\[
S=\int d^4x\sqrt{-g}\,[A R-\rho_{\rm vac}+\mathcal L_m]
\]

für konstante A>0 und rho_vac ergibt die Metrikvariation

\[
G_{\mu\nu}+\frac{\rho_{\rm vac}}{2A}g_{\mu\nu}
=\frac1{2A}T_{\mu\nu}.
\]

Ein möglicher relativer Beitrag wäre also zunächst eine noch herzuleitende
Wirkungsdichte rho_rel(q_rel), nicht q_rel selbst als Lambda.
Bei der üblichen gravitativen Normierung und rho als Energiedichte lautet die
SI-Konversion Lambda=8 pi G rho/c^4. Eine dimensionslose Zahl bestimmt weder
rho noch A oder eine physikalische Massenskala.

Ein konkreter negativer Kontrollversuch zeigt, was zusätzlich fehlt:
Man nehme chi als neues dimensionsloses Skalarfeld mit kinetischem Term
-f² g^{mu nu}(partial_mu chi)(partial_nu chi)/2, f>0, und
V(chi)=M^4 tanh²(chi/2), M>0. Das kanonisch normierte Feld wäre phi=f chi.
Diese Zusatztheorie ist nicht aus der QAM hergeleitet. Ihr Potential hängt
nur von der relativen Koordinate ab. Für einen konstanten Feldzustand müsste
jedoch zusätzlich V'(chi)=0 gelten. Es ist

\[
V'(\chi)=M^4\tanh(\chi/2)\operatorname{sech}^2(\chi/2).
\]

Die Ableitung ist hier nach chi; für die Ableitung nach phi kommt 1/f hinzu.
Die einzige endliche stationäre Stelle ist chi=0. Bei den historischen
Parametern ist (dV/dchi)/M^4 etwa 0.38356, also nicht null. Ein einfaches Ersetzen
des alten Offsetterms durch dieselbe relative Funktion erklärt deshalb keinen
statischen Vakuumzustand bei der bisherigen Trennung. Ein bewegtes Feld wäre
eine andere, dynamische Dunkle-Energie-Hypothese; w wäre nicht automatisch -1.
Zusätzliche Kopplungen oder ein konstant vorgegebener Parameter ändern dieses
Problem, wären aber neue, unabhängig zu rechtfertigende Eingaben.

Falls die relativen Größen stattdessen aus g und dynamischen Vektorfeldern
gebildet werden, ist ihre eigene Metrikvariation mitzunehmen. Die Formel
T=-Vg folgt dann nicht durch bloßes Einsetzen eines numerischen V. Das ist ein
weiterer Grund, internen Zustandskontrast und Raumzeit-Vakuumstress zu trennen.

## 5. Kosmologische Brücke und die absolute Skala

Die alternative Lesart aus r03, Omega_Lambda=1-beta², ist zunächst eine
Hypothese über einen dimensionslosen Dichteanteil. Aus Markov-Wahrscheinlichkeiten
folgen Energiedichteanteile nicht ohne Energiegewichte, Entwicklung und
kosmologische Dynamik. Wird die Hypothese trotzdem ausdrücklich angenommen,
gilt unter der gewöhnlichen GR-/Friedmann-Interpretation

\[
\Lambda=3\Omega_\Lambda H_0^2/c^2.
\]

Mit den historischen Parametern beta²=0.3017835 und **eingesetztem**
H0=67.4 km/s/Mpc erhält man Lambda ungefähr 1.112e-52 m^-2.
Die Größenordnung kommt hier aus dem eingesetzten H0, nicht aus einer
neu hergeleiteten neutralen Frame-Kombination. Das ist keine unabhängige
Vorhersage, keine aktuelle Datenanpassung und keine Lösung der Vakuumhierarchie.

Hingegen würde beta²/ellP² bei ellP=1.616255e-35m etwa 1.155e69m^-2 ergeben.
Die Vergleichszahl Lambda=1.1e-52m^-2 liefert Lambda ellP² etwa 2.874e-122.
Dieser Unterschied bleibt bei bloßen Einheitenwechseln bestehen.

Ein echter lokaler Vakuumtensor T_vac=-rho_vac g hat außerdem keinen bevorzugten
timelike Landau-Beobachter: Jeder normierte zeitartige Beobachter misst dieselbe
Dichte. Ein physikalischer flussfreier Frame wird daher gegebenenfalls durch
andere Sektoren ausgewählt. Zwei Beschreibungen desselben T sind nicht zwei
unabhängige Quellen, deren Energien man zur Kompensation addieren darf.

## 6. Vergleich mit vorhandenen Forschungswegen

Die vorhandene [Heat-Kernel-Analyse](HC_Induced_Gravity_Heat_Kernel.md) besitzt
bereits eine präzisere bedingte Verbindung von metrikabhängigem Operator,
regulierter Wirkung und den Koeffizienten rho und A. Ihr rein fermionischer
Vergleich erzeugt einen nicht unterdrückten Vakuumterm. Das ist keine native
Raumzeit-Herleitung.

Ihre zusätzliche skalare/fermionische Paarung kann den flachen konstanten
Koeffizienten aufheben und einen Einstein-Koeffizienten behalten. Das ist eine
echte Änderung des Feldinhalts und eine spektrale Matching-Bedingung, keine
Frame-Wahl. Die native Identifikation der Partner, Wechselwirkungen und
Schutzmechanismen bleiben offen. Bloß zwei unitär äquivalente Darstellungen
desselben Spektrums haben dieselben Determinanten, nicht entgegengesetzte
Vakuumbeiträge.

Ebenso verlangt die [gemeinsame Zwei-Frame-Wirkung](HC_Two_Frame_Action_Bridge.md)
explizite Nebenbedingungen und Rückwirkung. Ihr Multiplikator kann eine
Metrikvariation ausgleichen; daraus folgt nicht automatisch eine unabhängige
Einstein-Gleichung. Diese Ergebnisse bleiben Einschränkungen für jede
neutrale Zwei-Frame-Interpretation.

## 7. Quellenprüfung, Durchführung und Review

Originalquellen, genaue Fundstellen und Fingerabdrücke:
[Lambda-Kette](OP5_Lambda_Dependency_Audit.md),
[drei neutrale Konstruktionen](OP5_Neutral_Frame_Candidates.md).
Die r28-Korrektur der nativen Tachyon-Abbildung wurde berücksichtigt;
der bloße J_B-Porttausch wurde nicht als allgemeine Inversion übernommen.

Primäre externe Definitionen geprüft am 25.10.2026:

- Sean M. Carroll, *The Cosmological Constant*, astro-ph/0004075 (2000),
  [Autortext bei NED](https://ned.ipac.caltech.edu/level5/Carroll2/Carroll.html),
  Gl.12–15: Vakuumtensor, Druck, Lambda-Konversion und Einstein-Hilbert-Wirkung;
  Gl.21–22: kritische Dichte und dimensionslose Anteile.
- D.H. Weinberg und M. White, PDG *Dark Energy*, Revision August 2025,
  [Verlagstext](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-dark-energy.pdf),
  Abschn.28.1 und 28.2.1: w=-1 und Abgrenzung zu dynamischen Skalarfeldern.

Beide vollständigen Web-/PDF-Texte wurden geöffnet und die einschlägigen
Passagen gelesen. Kein vollständiger Text lokal behalten, daher kein lokaler
Quellhash. Diese Quellen definieren die physikalische Zielaussage; sie belegen
keine QAM-Identifikation und keine Vorhersage des Projekts.

Neu ausgeführt:
[Rechenvertrag](OP5_Neutral_Frame_Check.contract.json),
[Skript](OP5_Neutral_Frame_Check.py),
[Ergebnis](op5-neutral-frame-run-2026-10-25/result.json),
[Manifest](op5-neutral-frame-run-2026-10-25/manifest.json).
Exakte symbolische Kontrollen: Mittelpunkt-/Shift- und Varianzidentität,
Ableitung und stationäre Stelle des Vergleichspotentials, Lorentz-Kovarianz
eines Vakuumtensors, spurfrei bleibende Nullströme, partielle/vollständige
Disk-Mischung. Vier gemeinsame Shifts und drei skalare kinetische Beispiele
mit 45 Dezimalstellen geprüft. Manifeststatus `completed`, mit aktuellem
Projektwurzelpfad validiert. Keine Zufallsstichprobe.

Die getrennte [rationale Kontrolle](OP5_Neutral_Frame_Candidates_Check.py)
prüft zusätzlich nichtkommutierende räumlich verschiedene Boosts und den
Unterschied zwischen Paket-Schwerpunkt- und lokalem Landau-Frame. Ergebnisse
und Grenzen werden in der Kandidatennotiz dokumentiert.

Review: Zwei getrennte Ableitungen in Subagenten (native Abhängigkeiten und
neutrale Konstruktionen), danach Koordinatorabgleich mit den Rohquellen und
eigenen symbolischen/numerischen Kontrollen. Ein zusätzlicher Gegencheck der
Abschnitte 2–4 hat die benötigte Feldnormierung f für die dimensionslose
Rapidität chi sowie A>0 und M>0 ausdrücklich gemacht. Dies ist kein externer Peer Review,
keine vollständig unabhängige Validierung des gesamten Frameworks und kein
Beweis einer nativen physikalischen Wirkung.

## 8. Ergebnisstatus und Fortsetzung

| Route | Ergebnis | Status / genaue Fortsetzung |
| --- | --- | --- |
| Alte Lambda-/OP5-Kette rückwärts | Wirkungs- und Skalenlücken liegen vor der Frame-Wahl; Null des Offsetterms ist definitionsbedingt. | Audit abgeschlossen im angegebenen Umfang; historische Hypothesen nicht weiter hochstufen. |
| Neutralität aus zwei Skalenframes | Relationaler Mittelpunkt und shift-invariante Trennung konstruierbar. | Exakt im reellen Vergleich; native Paar-/Gewichtsregel und Raumzeitbrücke offen. |
| Neutralität aus zwei Disk-Zuständen | Richtige native Gegenabbildung plus gleiche Mischung ergibt I/2. | Exakt auf realem Disk; Präparation/Gewichte, Energiefluss und Mischdynamik offen. |
| Neutralität als flussfreier Beobachter | Positive nichtparallele Ströme wählen einen COM-/Landau-Bezug. | Bedingt auf gewöhnliche kausale Raumzeitquellen; liefert kein Vakuum-w=-1. |
| Relativer Ersatz des Offsetterms | q_rel kann die alte Zahl konsistent als Trennung erhalten. Einfaches kanonisches tanh²-Potential hat dort keine nichttriviale konstante Lösung. | Neuer Vergleichsvorschlag, nicht adoptierte Theorie. Native Wirkung/Hessian und Stabilisierung offen. |
| Lambda aus dimensionslosem Anteil | Dimensionsrichtige Umrechnung mit eingesetztem H0 möglich. | Phänomenologische Hypothese; absolute Skala und Zustands-/Dichtemapping nicht erklärt. |

Die beauftragte Neueinordnung wurde ausgeführt. Eine native physikalische
Lambda-Erklärung bleibt offen. Der konkrete nächste Entscheid ist, ob das
gesuchte neutrale Objekt **Vergleichsframe N**, **Mischzustand I/2** oder
**dynamisch flussfreier Beobachter** sein soll und welche native Operation es
erzeugt. Danach muss genau dieses Objekt in die metrikabhängige Wirkung
eingehen. Ohne diese Eingabe wäre eine spezifische neue Lambda-Gleichung
erfunden. Die drei Konstruktionen samt Voraussetzungen bleiben als
Fortsetzungsoptionen erhalten; keine davon wird als unmöglich archiviert.
