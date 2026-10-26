# OP5: trägt die native Dynamik ein Paarpotential und einen absoluten Vakuumwert?

Datum: 26. Oktober 2026. Basisrevision: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Begrenzter Audit vorhandener Definitionen und ihrer Folgerungen. Keine Änderungen
an Paper, Indizes, Issues oder Git. Keine neue physikalische Potentialfunktion
wird an die vorhandenen Parameter angepasst.

## Ergebnis

Die geprüften nativen Definitionen enthalten explizite positive
Closure-/Matching-Strafen und vorgeschlagene kompensatorische Kanäle. Sie enthalten
aber noch keine hergeleitete gravitative effektive Wirkung für einen dynamischen
Paarabstand chi oder eine Paarmischung, welche zugleich dessen Minimum und den
absoluten konstanten Vakuumanteil festlegt. Ein dynamisch stabiler neutraler
Paarzustand würde dieses zweite Problem nicht automatisch lösen.

Die kleinste zusätzliche Pflicht ist nicht eine passend gewählte Konstante in
einem Modellpotential. Sie ist eine native Wirkungs-/Maßvorschrift oder ein
bewiesener Schutz-/Matching-Satz, der den gemeinsamen konstanten Volumenterm
festlegt. Die vorhandenen normierten Zustände, Projektorclosure,
Kanalgleichgewichte und Markov-Gesetze leisten das derzeit nicht.

## 1. Tatsächlich vorhandene Eingaben

| Quelle / Locator | Inhalt | Was daraus nicht folgt |
| --- | --- | --- |
| `sources/research/parts/v470/10_sphaera_and_physics.tex:2187–2215`, `thm:variational-form` | Probe, geordnete Verbindung, Resonanz-Krümmung und die Strafen `U_C7=lambdaC||(1-P)Psi||²`, `U_HC=lambdaH||H-Lambda_cl[M,P]||²`. | Keine hier ausgeschriebene gemeinsame Einstein-Hilbert-Wirkung mit metrikabhängigem Paarpotential, absoluter Dichtenormierung und festgelegtem Quantenmaß. |
| dieselbe Datei `:2257–2284`, `Explicit closure functional` | `Lambda_cl=rho[M,P]^dagger[M,P]+sigma R_C^dagger R_C`, rho,sigma nichtnegativ. | `Lambda_cl` ist eine operatorwertige Closure-Abweichung, nicht die kosmologische Konstante. Die Buchstaben rho/sigma sind hier keine Vakuumdichten. |
| dieselbe Datei `:2327–2339` | Exakte Projektorclosure ergibt den verschwindenden minimalen Kompensator H_C. | Kein Schluss auf den gesamten Vakuumstress sämtlicher Felder und ihrer Fluktuationen. |
| `sources/research/parts/hc-dynamics-and-geometry.tex:211–269` | Reale Vergleichswirkung, explizite A-/H-Variationen, Target-Reaktion und Ward-Bedingungen. | Diese explizit andere reale Vergleichswirkung darf nicht unbemerkt als identische Quantisierung der geordneten nativen Wirkung eingesetzt werden. |
| `sources/research/parts/v490-post-release-layers.tex:3823–3940`, r27 | Rotation plus Messung; selektive Überlebensrate und unitaler Fluss zum gemischten Zustand. Im Text als vorgeschlagenes Modell bezeichnet. | Keine Herleitung des Messgeräts, Kopplungswerts, Sekundenmaßstabs oder gravitativer Potentialhöhe. |
| dieselbe Datei `:3979–4035`, r28 | Korrekte Trennung von J_B und der Dualitätsrotation z->iz; kontrollierte Messung und Partial-Swap-Modell. | Ein Kanal oder ein gegebener Austausch­winkel ist noch keine Energie-/Potentialfunktion für den Paarzustand. |
| dieselbe Datei `:4135–4178`, r29 | Vakuumpaare als vorgeschlagene erneuerte Reservoirquelle. | Rate, Kohärenz, Energiebilanz und Einfluss der Quelle auf die gravitative Wirkung bleiben zusätzliche Pflichten. |
| dieselbe Datei `:4394–4419`, r31.1 | Mit Rückkehrrate r>0 eindeutige stationäre Markov-Verteilung; stabile Abgangsfraktionen q und 1-q mit q=beta². | Die Rückkehrrate ist offen; Flussfraktionen definieren weder einen Hamiltonoperator noch den Nullpunkt einer Energiedichte. |
| dieselbe Datei `:8370–8399`, r67 | Unterschiede zwischen Materieanteil q und Lambda-Anteil 1-q sowie fehlende Brücke von Horizontzählung zu Energieanteil ausdrücklich genannt. | Kein Schluss von der dimensionslosen Zählrelation auf absolute Lambda-Skala oder eine epochengültige Vakuumgleichung. |

Die im alten Feldpaket vorkommende chi-Kopplung (`10_sphaera_and_physics.tex:2176`)
ist ein effektiver triadischer Mischkoeffizient. Sie ist nicht ohne Definition
dieselbe Größe wie ein neu eingeführter Paarabstand oder eine relative Rapidität.
Ein Symbolgleichklang liefert hier keinen nativen Potentialansatz.

## 2. Was die positiven Strafen tatsächlich fixieren

Für lambdaH>0 fixiert die ausdrücklich definierte Strafe bei sonst festem
Target ihr Minimum bei H=Lambda_cl; ihr Wert ist dort null. Zusammen mit exakter
Closure kann das den dargestellten klassischen Matching-Beitrag auf null setzen.
Das ist ein wirklicher Befund für diesen definierten Beitrag.

Zwei Grenzen sind wesentlich:

1. Der Target `Lambda_cl[M,P]` selbst ist nicht als Potential für zwei dynamische
   Framezustände und ihren Abstand hergeleitet. Die Feld-/Targetvariationen und
   die harten versus weichen Constraints müssen gemeinsam behandelt werden.
2. Die Festlegung einer einzelnen Strafe als Normquadrat schließt einen
   zusätzlichen unabhängigen konstanten Volumenterm nicht aus. Man darf den
   Literaltext der Definition nicht nachträglich verändern und dennoch sagen,
   es sei dieselbe vollständig definierte Theorie. Aber die bisher geprüften
   nichtgravitativen Gleichungen allein unterscheiden die entsprechenden
   gravitativen Vervollständigungen nicht.

Insbesondere ist „kein C in der gedruckten Minimalform“ eine Wahl des
klassischen Ansatzes. Ein Satz, dass native Symmetrien, Quantisierung und
Renormierung einen zusätzlichen konstanten Beitrag verbieten, ist dadurch
nicht bewiesen.

## 3. Der konstante Verschiebungs-Test

Sei hypothetisch eine gemeinsame Wirkung mit klar definierten dynamischen
Variablen Phi und konstantem gravitativen Koeffizienten A>0 gegeben:

\[
S_C[g,\Phi]=\int d^4x\sqrt{|g|}\,[A R-\mathcal K(\Phi,g)-V(\Phi)-C].
\]

Hier ist C eine einzige gemeinsame physikalische Dichte, kein pro Frame
nachträglich angepasster Bezug. Für Variationen nach Phi gilt

\[
\frac{\delta S_C}{\delta\Phi}=\frac{\delta S_0}{\delta\Phi},
\qquad d(V+C)=dV,\qquad d^2(V+C)=d^2V.
\]

Die Lage eines stationären neutralen Paarzustands, sein constrained Hessian
und seine lokalen Stabilitätseigenwerte werden vom konstanten C nicht festgelegt.
Auch wenn V'(chi*)=0 und V''(chi*)>0 bewiesen wären, wäre V(chi*)+C noch offen.

Für die Konvention Signatur (-,+,+,+) und
T_mu_nu=-2/sqrt|g| delta S_m/delta g^mu_nu liefert derselbe Zusatz

\[
T^{(C)}_{\mu\nu}=-C g_{\mu\nu},\qquad
\Delta\Lambda_{\rm cos}=\frac{C}{2A}.
\]

Er verändert also die gravitative Gleichung, obwohl die genannten
Materie-/Neutralitätsgleichungen gleich bleiben. Dies ist ein analytischer
Unbestimmtheitsnachweis für die Schlussregel „stabil neutral => Lambda fest“;
kein Beweis, dass jede vollständige künftige native Theorie ein freies C haben
muss.

Ein solcher Volumenterm ist mit gewöhnlicher Diffeomorphismusinvarianz und
internen Frame-/Austausch-/Projektorsymmetrien verträglich. Seine zusätzliche
Stressantwort ist kovariant konserviert. Daher verbieten die entsprechenden
Ward- oder Normierungsbedingungen ihn allein nicht. Eine weitere Symmetrie,
globale Nebenbedingung oder Renormierungs-/Matchingvorschrift könnte das ändern;
ein solcher nativer Satz wurde in den geprüften Blöcken nicht gefunden.

Normierung eines Zustands fixiert seinen Energie-Nullpunkt ebenfalls nicht.
Zum Beispiel bleibt für einen endlichen Gibbszustand
exp[-b(H+C I)]/Tr exp[-b(H+C I)] derselbe normierte Zustand wie für H,
während eine Kopplung des physikalischen Dichtenullpunkts an die Metrik eine
separate Frage ist. Ein normierter Markovkanal fixiert erst recht keine
gravitativ gekoppelte absolute Energie.

## 4. Vorhandene Potential- und Flussanalysen schließen diese Lücke nicht

r26 untersucht vorregistrierte Potentiale in drei Slotnormen bis Grad sechs
(`v490-post-release-layers.tex:3740–3779`). Der Text zeigt unter den genannten
Invarianten eine Sattel-/Flachrichtungsobstruktion für drei verschiedene
Nichtnullnormen. r32 untersucht erweiterte Realteil-Invarianten und weist
weitere Sattelbedingungen nach (`:4502–4541`). Das sind tatsächlich berechnete
Potentialaussagen, aber für einen anderen Objektbereich als eine hergeleitete
Paar-Rapidität samt gravitativer Vakuumdichte. Auch ein dort gefundenes Minimum
würde seinen eigenen konstanten Shift nicht aus seinen ersten und zweiten
Ableitungen bestimmen.

r27/r28 liefern kontrahierende Kanäle. Eine monotone Lyapunovfunktion eines
Kanals ist ohne Wirkungs-/Hamiltonbrücke noch kein physikalisches Potential.
Eine von mehreren Lyapunovfunktionen kann zudem um Konstanten verschoben
werden. Stationarität und Kanalnormierung beseitigen die gravitative Frage
daher nicht. Die Reservoirquelle und ihre Reaktion dürfen bei einer Energiebilanz
nicht nachträglich als kostenfrei behandelt werden.

r31 hat q und r als Eingaben und bestimmt die stationären Wahrscheinlichkeiten.
Die stabile Flussaufteilung ist keine Herleitung von q aus einem minimierten
Paarpotential und kein Fixpunkt einer absoluten Vakuumwirkung. r67 nennt die
fehlende Energiebrücke ausdrücklich. Die spätere r68-Nachrechnung berichtigt
Zähl- und Interpretationsaussagen, fügt dieser Kette keine gemeinsame
metrikabhängige Potentialfunktion oder Renormierungsbedingung hinzu.

## 5. Die vorhandene HC-Hessiananalyse benennt einen konkreten Engpass

`HC_Closure_Fluctuation_Hessian.md:9–65` zeigt für die gedruckte minimale
Closurefunktion am exakt geschlossenen Hintergrund delta Lambda_cl=0;
Lambda_cl beginnt quadratisch in den off-closure Variationen. Das ist nicht
delta Lambda_cos=0. Es betrifft eine andere Größe.

Bei hart eingesetztem H=Lambda_cl gibt es dort kein unabhängiges lineares
Gaussian-H-Feld. Bei weicher unabhängiger H-Integration ist die Matchingstrafe
eine andere Fluktuationstheorie. Diese Möglichkeiten dürfen nicht zugleich
zur Erhaltung der Closure und zum Zählen zusätzlicher Determinanten benutzt
werden.

Die vollständige angegebene Euclidean-Vergleichshessian besitzt zudem eine
fehlende Ableitungsrichtung und eine nicht auf gewöhnliche vierdimensionale
skalare Partner reduzierbare Spektralstruktur (`:129–156`). Ein positiver
Matchingkoeffizient beseitigt das nicht. Für die native Auswertung fehlen
damit insbesondere die reale Wirkungsform, die tatsächlich unabhängigen
Integrationsvariablen und Constraints, ein kontrollierter spektraler Operator
sowie Maß, Gauge-/Ghostbehandlung und Subtraktionsvorschrift (`:190–198`).

## 6. Bilineares Vorzeichen ist kein entgegengesetztes Determinantengewicht

H25 trennt die beiden Vergleiche ausdrücklich:
`notes/research/v4_10_0_r34_r47/llm/Ergebnis_H25_Zweiseitige_Kontraktion_Frames.md:11–29`.
Die Dualitätsrotation z->iz kehrt den bilinearen quadratischen Ausdruck q um,
während der hermitesche Ausdruck h unverändert bleibt. r28 korrigiert die
Abbildung auf dem Doublet entsprechend. Daraus folgen zwei unterschiedliche
Kontrollfälle, keine automatische Vakuumkompensation.

**Hermitescher/unitärer Vergleich.** Sind zwei positive Operatoren lediglich
unitär äquivalent, L2=U L1 U^{-1}, dann sind ihre mit demselben Maß und derselben
Regularisierung gebildeten Heat-Traces gleich. Bei gleichen statistischen
Determinantengewichten addieren sie sich. Eine relative Phase erzeugt kein
Minuszeichen des Integrationsmaßes.

**Bilineares q als Massenquadrat interpretieren.** Das ist eine zusätzliche
physikalische Identifikation, nicht bereits H25. Nimmt man sie testweise an,
ergeben gleiche Gewichte für q und -q im flachen Heat-Faktor

\[
e^{-s q}+e^{+s q}=2\cosh(sq),\qquad s>0.
\]

Das ist keine Aufhebung. Für q>0 führt L=-partial²-q in unendlichem flachen
Euclidean-Raum außerdem negative Moden bei k²<q ein; der proper-time-Anteil
wächst im Infraroten. Eine endliche IR-Abschneidung, ein anders stabilisiertes
Potential oder ein anderer kausaler Operator wäre ein eigener Ansatz.
Das Vorzeichen des bilinearen QAM-Readouts darf also nicht mit dem Vorzeichen
eines wohldefinierten physikalischen Vakuumdeterminanten verwechselt werden.

Entgegengesetzte bosonische/fermionische Gewichte haben eine andere Herkunft:
den Feldinhalt und die Integrationsstatistik. Ihre native Zuordnung müsste
separat bewiesen werden. H25, J-Projektion, ein Tachyonetikett oder positive
Closure-Tags liefern diese Gewichte nicht.

## 7. Reale bedingte Alternative: selektive sektorielle Kompensation

`HC_Induced_Gravity_Heat_Kernel.md:208–265` berechnet eine wohldefinierte
Vergleichsbedingung für gewöhnliche zusätzliche skalare Felder:

\[
W_0(s)=4\sum_f e^{-s m_f^2}-\sum_b e^{-s q_b}=0,
\qquad A>0.
\]

Für ein endliches Spektrum mit festen Gewichten muss für jedes verschiedene
Massenquadrat die passende Modenzahl stimmen. Vier reale skalare Moden pro
komplexem Dirac-Modus mit demselben Massenquadrat ergeben in diesem Vergleich
die flache Vakuumaufhebung. Die Krümmungskoeffizienten können dabei positiv
bleiben, wenn die ebenfalls deklarierte skalare Krümmungskopplung passt.

Das ist ein ernsthafter Mechanismus, aber zusätzliche Feld-/Maßdaten und keine
Folgerung aus der Paarneutralität. Er fixiert auch nicht automatisch einen
unabhängigen nackten kosmologischen Gegenterm, weitere Schleifen oder die
vollständige gekrümmte Vakuumwirkung. Die native Identifikation der Moden und
eine schützende Relation sind weiterhin offen.

## 8. Referenzabzug versus lokaler Gegenterm

Bei festem Referenzhintergrund g0 gilt

\[
\frac\delta{\delta g}[\Gamma[g]-\Gamma[g_0]]
=\frac{\delta\Gamma[g]}{\delta g}.
\]

Der Abzug des Referenzwerts entfernt daher keinen lokalen Vakuumstress.
Wird g0 dynamisch oder metrikabhängig aus einem Paar konstruiert, entstehen
zusätzliche Kettenregelterme; sie müssen aus einer gemeinsamen Wirkung mit
den Paar-/Referenzgleichungen berechnet werden. Das ist nicht mehr der
Abzug einer festen Konstanten.

Der Abzug `C int sqrt|g|` verändert den Stress und ist genau ein lokaler
kosmologischer Gegenterm. Ohne unabhängige native Bedingung wäre sein Wert
eine Festlegung, keine Herleitung. Das folgt bereits in der vorhandenen
Analyse `HC_Induced_Gravity_Heat_Kernel.md:301–311`.

## Schluss und konkrete nächste Pflicht

Für einen nativen Fortschritt müssen die Variablen der Paarrelation und
deren Abbildung aus Psi,P,M,H,n zunächst ausdrücklich festgelegt werden.
Danach braucht man den tatsächlich auf diese Variablen reduzierten
Wirkungs-/Energieoperator, seine Nebenbedingungen und kinetische Form. Nur
aus dieser gemeinsamen Struktur lassen sich stationärer Paarzustand,
zulässige Hessian, Reservoirreaktion und gravitativer Volumenkoeffizient
zusammen bewerten.

Derzeit erlaubter Schluss: Die vorhandenen Daten können einen relationalen
neutralen Vergleich und bestimmte stabile Modellkanäle tragen. Ein aus ihnen
hergeleitetes natives Paarpotential mit fixierter absoluter Vakuumhöhe wurde
in den geprüften Quellen nicht gefunden. Eine gesetzte Normquadratstrafe
und ein stabiler neutraler Zustand schließen die C-Frage nicht.

## Provenienz

Quellen gelesen und die dargestellten Constant-Shift-/Heat-Faktor-Kontrollen
analytisch rekonstruiert. Kein neuer numerischer Lauf, kein externer
Theoremnachweis oder neuer numerischer Fit. Die Aussagen der vorhandenen
Forschungsnotizen wurden nach ihrem jeweils angegebenen bedingten Umfang
verwendet, nicht als native Theorieerfolge übernommen.

SHA256 der Kernquellen:

```text
v470/10_sphaera_and_physics.tex 7D72C58B1159F5462C6BE395961FCD8882028FC3E8C8495E7F2A3B10055C1A32
hc-dynamics-and-geometry.tex 472297781D9EB837BC4E5F6ECAC59D9E4ABE792A03BC8DF7EACD4247FDA3546F
v490-post-release-layers.tex 232BDD631BAC34259BE48B6D326FBF6EAF38F084EE4BEC1A621658B3C964424E
HC_Closure_Fluctuation_Hessian.md 38E8F1FB91709A524D26D704ED8EF14D380B52B31CF8C52543CB4DE566033370
HC_Induced_Gravity_Heat_Kernel.md 3910A1FEE31AD4B27FAC0445FDC2BB53ED5FF6C8442D52556C76651426C1A340
HC_Two_Frame_Action_Bridge.md BD5649A5D5BC219B7F2878085A059B5D5344F5705BEDB3EA63C59F874355725D
Ergebnis_H25_Zweiseitige_Kontraktion_Frames.md E458442005B1F9CDD69B577DA5D3E12DF1453166F56A2FA3EA59D44F14EA6163
```
