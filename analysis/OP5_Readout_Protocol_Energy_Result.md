# OP5: Reihenfolge, Zeitpunkt und Energie einer Auslesung

Datum: 26. Oktober 2026. Checkpoint: `OP5-READOUT-ENERGY-2026-10-26`.
Git-Basis: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Separate Forschungsfortsetzung; keine Änderung am Paper, kein öffentlicher
Release und keine OP5-Schließung. Die neueren Paardynamik-Notizen sind lokale
Eingaben dieses Checkpoints, nicht bereits durch den Git-Hash allein gepinnt.
Die Rechenmanifeste pinnen die tatsächlich gelesenen Eingaben zusätzlich.

## Auftrag und Ergebnis

Vor einer energetischen Zuordnung wurde geprüft, ob es auf den lesenden
Frame, den Zeitpunkt, die Ausleseoperation und die Reihenfolge ankommt.
Anschließend wurden System, Messgerät, Kopplungsarbeit und Reservoir in
expliziten Vergleichsmodellen bilanziert.

**Ja, ein physisch anderes Readout-Protokoll kann andere Zustände, Wahrscheinlichkeiten,
Energieänderungen und periodische Endzustände erzeugen.** Ein vollständig
passiver Frame-Wechsel desselben Experiments ändert dagegen seine Vorhersagen
nicht. Bei den geprüften aktiven Protokollen wird Energie zwischen System,
Apparatur und Bad ausgetauscht; keine Energie wird durch die Bezeichnung
eines Frames erzeugt. Ein solcher stationärer Betriebszustand ist noch kein
kosmologischer Vakuumzustand.

## 1. Zuerst die Art des Readouts festlegen

Die vorhandene mathematische Relation QRead(r,s,w) liest einen Wert aus einem
gegebenen Zustandscode. Sie stellt für sich keine physische Messkopplung oder
Zustandsänderung bereit. Zwei reine Auswertungen desselben unveränderten
Zustands bekommen nicht durch ihre Aufrufreihenfolge eine neue Dynamik.

Für eine physikalische Frage müssen getrennt angegeben werden:

1. passiver Frame-/Darstellungswechsel desselben Experiments;
2. aktive Kopplung an ein Messgerät mit vollständigem Messinstrument;
3. selektive Auswahl eines Ergebnisses mit seiner Wahrscheinlichkeit;
4. freier Generator, physikalische Uhr und Verzögerung zwischen Eingriffen.

Erst bei 2–4 kann der beobachtete Verlauf durch das Protokoll verändert werden.
Die dabei benötigten Zustandsoperatoren und Instrumente sind zusätzliche
Objekte, nicht bereits durch das QRead-Tag physikalisch begründet.

## 2. Auslesereihenfolge: ein exakter Gegencheck

Für ein Qubit mit Bloch-Vektor b und eine Achse n lautet die vollständige
nichtselektive projektive Auslesung

\[
\mathcal D_n(\rho)=\tfrac12(\rho+\sigma_n\rho\sigma_n),
\qquad b\mapsto nn^{\mathsf T}b.
\]

Zwei solche Kanäle kommutieren für alle Eingaben genau bei parallelen oder
orthogonalen Achsen. Bei anderen Achsen kann die Reihenfolge den Endzustand
ändern. Vollständige selektive Ergebnisfolgen sind eine nochmals getrennte
Frage, auch in manchen Fällen mit gleichem nichtselektivem Endzustand.

Ein parameterfreier Vergleich auf dem realen Disk beginnt mit rho_z=(I+sigma_z)/2.
Gemessen wird einmal entlang x und einmal entlang n=(x+z)/sqrt(2). Danach
wird in beiden Fällen derselbe Kompensatorport x ausgewertet:

| Reihenfolge | Wahrscheinlichkeit für denselben abschließenden Plus-Port |
| --- | ---: |
| x, dann n | 1/2 |
| n, dann x | 3/4 |

Das ist ein anderer physischer Eingriff, kein Widerspruch zwischen korrekten
Beschreibungen desselben Experiments. Die gesamte Rechnung ist in
[Readout-Reihenfolge und Zeit](OP5_Readout_Order_Timing.md) hergeleitet.

### Wichtige native Negativkontrolle

Auf dem realen Disk kehrt die korrigierte native Gegenabbildung sigma_y eine
reale Achse n nur zu -n um. Nichtselektiv gilt D_n=D_-n; Plus- und Minuslabels
tauschen. Die Bezeichnung „Materie liest“ gegenüber „Tachyon liest“ liefert
also allein noch keine zwei inkompatiblen Messkanäle. Selektiert man jeweils
„Plus im eigenen Frame“, behält man unterschiedliche physische Teilmengen.
Die verworfenen Zweige müssen dann mitgerechnet werden.

## 3. Wann gelesen wird: Uhr und freie Entwicklung

Mit dem ausdrücklich gewählten Vergleichsgenerator
H=hbar omega sigma_y/2 bleibt der reale Disk erhalten. Für den Start rho_z
und eine erst nach Wartezeit t erfolgende x-Auslesung ist

\[
p_+^x(t)=\tfrac12[1+\sin(\omega t)].
\]

Eine zusätzliche nichtselektive x-Auslesung ganz am Anfang setzt diesen
Start dagegen auf I/2; dann bleibt die spätere Wahrscheinlichkeit 1/2.
Die Messhistorie gehört damit zu den Daten des Experiments.

Wenn der freie Generator mit dem ausgewerteten Projektor kommutiert, ändern
Verzögerungen diese Wahrscheinlichkeit für keine Eingabe. Ein unveränderter
Wert bei nur einem Zeitpunkt oder Zustand beweist diese allgemeine Aussage
nicht. Zeitabhängige passive Framewechsel brauchen zudem die korrekte
Verbindung im Generator. Mit C(t) lautet er
H'_gen=C H_gen C†+i hbar (dC/dt) C†, während eine physische Energieobservable
als H'_phys=C H_phys C† transformiert wird. Ein scheinbar zusätzlicher
Generatoroffset darf nicht ohne weitere Herleitung als physische Energiedichte
gelesen werden. Bereits C(t)=exp(i alpha t)I verschiebt den dargestellten
Generator um -hbar alpha I, ohne Zustände, Messwahrscheinlichkeiten oder
physische Energie zu verändern. Die vollständige Ableitung einschließlich
Instrumenten an verschiedenen Zeitpunkten steht in der Readout-Notiz.

## 4. Die Energieänderung hat eine Quelle

Für H=h_0 I+h dot sigma beträgt die Systemänderung durch D_n

\[
\Delta E_S=h\cdot(nn^{\mathsf T}-I)b.
\]

Sie kann positiv, negativ oder null sein. Das ist zunächst eine
Systemenergieänderung, noch keine vollständige Aussage über Arbeit oder Wärme.

Die [Kopplungs- und Energienotiz](OP5_Readout_Interaction_Energy.md) baut dazu
ein vollständiges System-/Meter-Gatter. Bei entartetem freiem Meter-Hamiltonian
und ausdrücklich berücksichtigtem Ein-/Ausschalten der Kopplung gilt exakt

\[
W_{\rm Schalten}=\Delta E_S+\Delta E_M.
\]

In einem zeitabhängigen Vergleichsfall mit positivem Energieabstand omega ist

\[
\Delta E_S=\frac\omega8(\sqrt3\cos\phi-1).
\]

Die getesteten Phasen 0, pi/2 und pi liefern +0.091506 omega, -0.125 omega
und -0.341506 omega. Die externe Pulsarbeit liefert bzw. übernimmt genau
diese Beträge. Ein negatives Delta bedeutet Energieabgabe des Systems,
keinen negativen kosmologischen Vakuumbeitrag.

Ein anderer, energieerhaltender Partial Swap zwischen identischen freien
Hamiltonoperatoren überträgt Energie zwischen System und Partner, ohne sie
im geschlossenen Paar zu erzeugen. Ein einzelner weiterentwickelter Partner
zeigt Wiederkehr. Frische Partner oder ein erneuertes Bad sind zusätzliche
Ressourcen, keine kostenlose Wiederholung desselben geschlossenen Vorgangs.
Resetkosten werden ohne konkrete Badtemperatur, Hamiltonoperatoren,
Korrelationszugriff und Rücksetzverfahren nicht pauschal angegeben.

## 5. Ein ganzer wiederholter Readout-Zyklus

Der Koordinator hat zusätzlich ein explizites wiederholtes Protokoll gelöst:

```text
erstes aktives Readout -> freie Wartephase -> zweites aktives Readout
    -> energieerhaltender Kontakt mit frischem thermischem Partner
    -> nächster Zyklus.
```

Die Angaben sind vollständig deklarierte Vergleichseingaben:
Hs=sigma_z/2, gap=hbar=1; Bad mit identischem H und tau=diag(1/4,3/4), also
beta gap=log(3); Partial-Swap cos(theta)=4/5, sin(theta)=3/5.
Readout-Achsen A=(3/5,0,4/5), B=(0,4/5,3/5). Das Modell verwendet den
vollständigen Bloch-Ball; B und die freie Entwicklung sind keine behauptete
native M/T-Zuordnung des ursprünglichen realen Disks.

Der gemeinsame unitäre Partial Swap kommutiert mit Hs+Hbad. Für den
System-Bloch-Vektor hat der Badkontakt die affine Form b->Kb+d mit

\[
K=\begin{pmatrix}16/25&6/25&0\\-6/25&16/25&0\\0&0&16/25\end{pmatrix},
\qquad d=(0,0,-9/50).
\]

Seine euklidische Kontraktionsnorm ist sqrt(292)/25=0.68352...<1.
Auslesungen und freie Rotationen vergrößern Abstände nicht. Deshalb hat
jeder solche Zyklus bei diesen Bad-/Kopplungsparametern einen
eindeutigen attraktiven periodischen Zustand. Gemeint ist der Zustand an
derselben Stelle jedes Zyklus, nicht ein unveränderter Zustand während
des gesamten Zyklus.

Zwei ausgewählte Ergebnisse bei gleicher Wartephase pi/2:

| Reihenfolge | Angeregter Anteil am Zyklusanfang | Readout-Arbeit pro Zyklus | Reservoirenergie ins System |
| --- | ---: | ---: | ---: |
| A, dann B | 0.365354 | +0.064886 | -0.064886 |
| B, dann A | 0.410000 | +0.090000 | -0.090000 |

Energien stehen in Einheiten des vorgegebenen Systemabstands. Der angeregte
Anteil ist die Energie für das äquivalente H_exc=(I+sigma_z)/2. Das Skript
verwendet Hs=sigma_z/2 mit einem um 1/2 verschobenen Nullpunkt; Arbeit und
Reservoirenergieänderungen bleiben gleich. Dies ist keine Rechnung in Joule oder Planck-Einheiten.

In allen acht Fällen gilt symbolisch, nicht nur näherungsweise,

\[
\Delta E_{\rm Zyklus}=0,
\quad W_A+W_B+Q_{\rm Bad\to S}=0,
\quad Q_{\rm Bad\to S}=-\Delta E_{\rm ausgegebenes\ Bad}.
\]

Das stationäre System wird von Readout-Arbeit angetrieben; die ausgegebenen
Badancillas nehmen die Energie auf. Q bezeichnet hier diese operationelle
Energieübertragung. Einige ausgehende Ancillas haben Kohärenz und sind nicht
mehr thermisch; eine eindeutige thermodynamische Zerlegung in Wärme und
Arbeitsfähigkeit wird nicht behauptet. Ein-/Ausschaltarbeit ist berücksichtigt.
Meter-Reset und die Herstellung
frischer Badzustände werden nicht als kostenfrei bezeichnet, aber hier nicht
zusätzlich quantifiziert. Eine andere Geometrie oder Symmetrie kann manche
Reihenfolgen-/Zeiteffekte aufheben; sie folgen nicht aus jedem Frame-Paar.

## 6. Was das für eine kosmologische Einordnung bedeutet

Eine stationäre, durch Arbeit und Reservoir erhaltene Energie kann eine
offene stationäre Dynamik beschreiben. Sie ist nicht allein deshalb
Vakuumenergie mit T_mu_nu=-rho g_mu_nu. Es fehlen weiterhin physischer
Energieabstand, Modendichte, Raumzeit-/Uhrzuordnung, Gesamtstress und seine
Metrikvariation. Die Apparatur oder der Reservoirsektor darf dabei nicht
aus der gravitativen Bilanz entfernt werden.

Ein weiterer, ausdrücklich hypothetischer Kontinuumscheck zeigt die Grenze.
Angenommen, ein isotroper Strahlungssektor mit p_r=rho_r/3 wird in einer
expandierenden FLRW-Beschreibung auf konstanter positiver rho_r gehalten.
Dann braucht er den Zufluss

\[
\dot\rho_r+3H(\rho_r+p_r)=Q,\qquad Q=4H\rho_r.
\]

Schreibt man seine Gleichung künstlich ohne Quelle, erhält man
p_eff=p_r-Q/(3H)=-rho_r. Das sieht wie ein Vakuumzustand aus, ist aber
zunächst eine Umverteilung des Quellenbuchhaltungsterms. Für eine positive
Staubquelle mit p_s=0 und demselben Gegenfluss ist tatsächlich

\[
\dot\rho_s+3H\rho_s=-Q,\qquad
\rho_{\rm ges}+3p_{\rm ges}=\rho_s+2\rho_r>0.
\]

Wenn diese beiden Komponenten den gesamten gravitativen Stress liefern und
kein zusätzlicher nackter Lambda-Term vorliegt, beschleunigt dieses positive
Staub-plus-Strahlungssystem unter gewöhnlichen GR-/FLRW-Annahmen deshalb nicht.
Mit N=log(a/a0) ist

\[
\rho_s(N)=(\rho_{s0}+4\rho_r/3)e^{-3N}-4\rho_r/3.
\]

Die positive Quelle ist bei endlichem
N=log(1+3rho_s0/(4rho_r))/3 erschöpft. Eine längere Fortsetzung mit negativem
rho_s wäre kein erlaubter Beleg für die angenommene positive Quelle.
Diese Kontinuumsdrücke sind separate Hypothesen, nicht aus den Qubits
hergeleitete Druckwerte. Andere Quellsektoren mit eigenem negativem Druck
oder andere Gravitationsgleichungen sind damit nicht ausgeschlossen.

Schließlich bleiben konstante Hamilton-Offsets für normierte Readout-
Wahrscheinlichkeiten, Energieänderungen und Wärmeströme unsichtbar. Das
Protokoll kann Reaktionsenergie bestimmen, legt aber allein den absoluten
gravitativ wirksamen Volumenanteil C noch nicht fest.

## 7. Reproduktion, Quellen und Review

- Instrumente/Reihenfolge: [Notiz](OP5_Readout_Order_Timing.md),
  [exakte Kontrolle](OP5_Readout_Order_Timing_Check.py).
- Apparatur-/Reservoirenergie: [Notiz](OP5_Readout_Interaction_Energy.md),
  [Kontrolle](OP5_Readout_Interaction_Energy_Check.py).
- Gesamtzyklus: [Skript](OP5_Readout_Cycle_Energy_Check.py),
  [Vertrag](OP5_Readout_Cycle_Energy_Check.contract.json),
  [Ergebnis](op5-readout-cycle-run-2026-10-26-reviewed/result.json),
  [Manifest](op5-readout-cycle-run-2026-10-26-reviewed/manifest.json).

Die Instrumente und Zykluszustände wurden exakt mit SymPy geprüft:
Unitarität, Partialspuren, positive normierte Zustände, Fixpunkte,
Kontraktionsnorm, freie Energieerhaltung, Bad-Gegenbilanz und erste
Hauptsatzidentitäten. Acht Protokollfälle wurden vollständig ausgewertet;
keine Zufallssimulation und kein Fit. Dezimalwerte dienen nur der Anzeige.
Die Kontinuums-Gleichungen wurden symbolisch rückeingesetzt.

Der erste Zykluslauf scheiterte an einem unvereinfachten symbolischen
Matrixvergleich für U†U. Nach expliziter algebraischer Vereinfachung bestanden
derselbe Unitaritätstest und alle Folgeprüfungen. Der fehlgeschlagene Lauf
bleibt als solcher dokumentiert; der finale Lauf verwendet das korrigierte
Skript und enthält zusätzlich den Kontinuumscheck. Die früheren Manifeste
pinnten entsprechend ältere Skriptstände. Im abschließenden geprüften Lauf
wurde Q zudem präzise als Ancilla-Energietransfer bezeichnet und im
Kontinuumscheck die Abwesenheit eines zusätzlichen Lambda-Terms festgehalten.

Eine getrennte Rekonstruktion der acht Zyklen mit vollständigen 4x4-Unitaries
bestätigte Fixpunkte und Bilanzen numerisch (Fixpunktfehler höchstens
2.22e-16, Energiebilanzen unter 1e-14). Der zusätzliche Review präzisierte die
Kohärenz der ausgegebenen Badancillas sowie die Gesamtstress-Annahme des
Kontinuumskontrollfalls. Keine Übereinstimmung zwischen Rechnungen wird als
nativer physikalischer Nachweis ausgegeben.

Native Quellen: r27/r28, Compensator- und Frame-Definitionen sowie die in den
Einzelnotizen genauer ausgewiesenen r47/r51-Scope-Korrekturen. Eine QAM-
Grammatikprüfung wird nicht als Nachweis physischer Energie oder nativer
Closure-Klassenerhaltung ausgegeben.

Physikalische Zieldefinitionen: Sean M. Carroll, *The Cosmological Constant*
(2000), [vollständiger Autortext bei NED](https://ned.ipac.caltech.edu/level5/Carroll2/Carroll.html),
Gl.4–6 und 12–15 sowie 24–26. Am 26.10.2026 wurden die Passagen zu
Gesamtstress, Beschleunigung, Vakuumdruck und Energieerhaltung erneut gelesen.
Die Zwei-Fluid-Quellenaufteilung und ihre Lösung wurden hier selbst unter
den angegebenen Zusatzannahmen abgeleitet. Die Quelle liefert keine native
QAM-Zuordnung.

## 8. Forschungsstand und Fortsetzung

Der Nutzerhinweis wurde positiv und negativ getestet: Aktive Readout-Wahl,
Reihenfolge und Uhrzeit können entscheidend sein; native Gegenlabels oder
passives Umbenennen allein reichen nicht. Für den neuen mathematischen
Prüfauftrag ist der vollständige Vergleichszyklus einschließlich Energiequelle
ausgeführt. Die native physikalische Anwendung bleibt offen.

Ein künftiger nativer Protokollvertrag sollte festhalten:

```text
Eingangszustand / gemeinsame Vergleichsschicht
-> welcher Reader mit welchem Instrument und welcher Uhr koppelt
-> freie Entwicklung / Verzögerung
-> zweiter Eingriff einschließlich aller Ergebniszweige
-> Partner-/Reservoirreaktion und externe Steuerarbeit
-> gemeinsamer End-Readout, Energiebilanz und vollständiger Stress.
```

Die nächste tragende Brücke ist damit konkreter: tatsächlicher nativer
Hamiltonoperator und Mess-/Wechselwirkungskanal auf dieser gemeinsamen
Schicht, einschließlich seiner Uhr, Energiegewichte und Reservoirvariablen.
Danach ist die gravitative Variation zu berechnen. Der aktuelle Versuch
belegt eine protokollabhängige offene Reaktionsdynamik, keine neu bestimmte
kosmologische Konstante.
