# Forschungsstand

**Quellenstand: 4.11.2026, GitHub `main` bei cf48496 plus Runden r70 bis r80.** Diese Seite fasst den aktuellen Stand zusammen; sie ist kein neuer Beweisaudit. Was im Companion insgesamt steht, beschreibt die [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt); die Ergebnisse aller Runden nach Themen die [Forschungslinie](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungslinie). [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

## Bedingte Ergebnisse

Die v4.9.0-Linie enthält unter anderem bedingte Cartan-Vergleiche, endliche Normal-Inversen und Quellgesetze, Koide-bezogene Gleichnormbedingungen sowie Untersuchungen zur HC-Massenidentifikation und Generationenkopplung. Voraussetzungen und Einschränkungen stehen in den jeweiligen Abschnitten und Analysen. Ein endlicher Inversen- oder Kompatibilitätssatz liefert für sich weder regionale PDE-Existenz noch native physikalische Identifikation.

## Jüngste Korrekturen auf der 4.10-Basis

Die [Basisrevision](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_base/README.md) archiviert zurückgezogene Aussagen, korrigiert bekannte Fehler und kennzeichnet offene bzw. umgedeutete Aussagen. Historischer Text ist zusammen mit seinem aktuellen Status zu interpretieren.

Die [Layer r63–r68](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r63_r64/README.md) unterscheiden Zählregeln und prüfen deren Frame-Deutung. Dokumentiert wird insbesondere:

- `thm:k-values` mit $k(\gamma_{\mathrm{BI}})=0$ widerspricht `thm:frame-offset`. Dieser Widerspruch ist nicht neu: v4.9.0-r09 hat ihn bereits festgestellt und aufgelöst, indem `thm:frame-offset` nur vom strukturellen Faktor $\gamma_L$ spricht. r66 korrigiert die fehlende Zitierung in r64 und erweitert die Statusnotiz.
- In der Zähllesart liegt der Frame-Unterschied in $\gamma$; die Zuordnungen für $\hbar$ und $G$ benötigen eine andere Begründung.
- Die Photon-Planck-Skalierung $\gamma_L^{-3/2}$ und der Vakuumquotient $\gamma_L^5$ werden durch diese Lesart nicht gestützt.
- Im Hawking-Abschnitt wird eine Tachyonzählung dem austretenden Photon zugeordnet. r65 ergänzt hierzu Statusnotizen im Haupttext.
- In der Zähllesart ist der strukturelle Faktor eine feste Zahl; die beiden Zählregeln sind diskret und liefern keinen stetig driftenden lokalen Frame-Faktor (r66). Die Drift-Lesarten aus r08/r09 sind ohnehin durch Atomuhren ausgeschlossen.
- Zu Einsteins „größtem Fehler“ (`rem:einstein-blunder`, r67): Die Bemerkung und die Feldgleichung in `rem:omega-bsym` setzen $\beta_{\mathrm{sym}}^2$ auf $\Lambda$, `thm:dark-energy` setzt denselben Wert auf die Materie ($\Omega_M=\beta_{\mathrm{sym}}^2$). In der Zähllesart ist $\Lambda$ als Krümmung frame-unabhängig; erklärbar wäre höchstens der Anteil $\Omega_\Lambda=2\gamma_T/(\gamma_M+\gamma_T)\approx0{,}698$, und nur für die heutige Epoche. Offen bleibt, warum ein Zählanteil einem Energieanteil entsprechen soll.
- Unabhängige Nachrechnung (r68): Die Zahlen von H47 und r63–r67 bestätigen sich. Einschränkung: Die Zähllesart funktioniert nur mit der U(1)-Behandlung der Horizontzustände ($\gamma\approx0{,}2375$). Die als besser begründet geltende SU(2)-Behandlung ergibt $\gamma\approx0{,}274$ und $\beta_{\mathrm{sym}}\approx0{,}604$, außerhalb des Leptonfensters. Die registrierte Vorhersage H46 bleibt mit dem ungerundeten Wert gültig.

Das sind Einschränkungen bestimmter Argumente, keine allgemeine Widerlegung jeder möglichen Gravitationstheorie.

## OP5: Vakuumterm, Frames und Neutralität (r69)

Der Autor hat vom 25. bis 27. Oktober mit einem weiteren Sprachmodell an OP5 gearbeitet; die Notizen liegen unter `analysis/` (Prefix `OP5_`). [Layer r69](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/b12adf5fc0a69d32e0405b78dfb505c3b9bbea44/notes/research/v4_10_0_r69/README.md) bindet sie ein. Alle Prüfskripte ließen sich reproduzieren, neun Aussagen wurden mit eigenem Code nachgerechnet. Jede positive Aussage der Serie ist bedingt (Vergleichsmodell, gewählter Zeuge oder zwei Stichpunkte). Festgehalten wird:

- Ein passiver, invertierbarer Frame-Wechsel skaliert einen Bilanzdefekt nur; er kann ihn nicht beseitigen. Die Ersetzung von $\gamma_L$ durch $e^\eta$ schließt die historische Bilanz nicht.
- „Neutral“ hat drei verschiedene Bedeutungen: Mittelpunkt zweier Skalenframes; gleichgewichtige Mischung eines Zustands mit seinem Tachyonbild ($I/2$, Etikett P); flussfreier Beobachter zweier Nullströme (Stress $\mathrm{diag}(\rho,\rho,0,0)$, kein Vakuumtensor). Sie dürfen nicht gleichgesetzt werden.
- Keine der geprüften Routen legt den absoluten Vakuumterm fest. Ein gemeinsamer Energieversatz ist bei festem Hintergrund unbeobachtbar; im alternativen affinen Vergleichsmodell löst ein Zweig die Feldgleichungen für jede Konstante.
- Der Lichtkegel der Sondengleichung kommt aus der Clifford-Struktur, nicht aus Masse-, $M_{16}$-, triadischen oder HC-Termen. Kegeldaten legen weder eine absolute Skala noch das Gewicht eines Vakuumterms fest.
- Mit der verbundenen Querauslese $E=\tfrac12 Dj$ gilt $T=\tfrac12 Rj$. Torsionsfrei und mit gewöhnlicher Einstein-Vakuumgleichung folgt $\Lambda_{\mathrm{geom}}=0$, wo $j\neq0$: ein Ausschluss unter diesen Voraussetzungen, keine Aufhebung von Vakuumenergie.
- Drei Fehler im Hauptkorpus wurden gefunden: `rem:regularization-B` (Reihenentwicklung und Vorzeichen des Gegenterms falsch; der Wert 0,940 stimmt nicht), `thm:dirac-probe` und `prop:three-compatible-readings` stützen die Uhrskala auf das archivierte `thm:gue-selfdet`, und das Korollar „Cosmological constant revisited“ gibt für dieselbe Größe null und $\gamma_L^5$ an. Alle drei sind seit der 4.10-Konsolidierung korrigiert bzw. mit Statusvermerk versehen (siehe unten). Der in r69 genannte richtige Wert 1,689 war selbst falsch; richtig ist 1,686953 (r70).

OP5 bleibt in der exakten Form offen; die lokale Detektorschließung $\mathrm{OP5}_{\mathrm{eff}}$ ist davon nicht berührt.

## 4.10-Konsolidierung, H48 und Λ als Mischung (r70)

Am 29. und 30. Oktober hat das zweite Sprachmodell den Forschungskandidaten direkt weitergeschrieben; Runde r70 übernimmt das in die lokale Gesamtquelle und verbucht es.

- **Korrekturen im Hauptkorpus.**
  - Die Regularisierung lautet jetzt $R(\tau) = -1/\tau + 1 - \tfrac{11}{24}\tau + \dots$ mit Gegenterm $-\log(\varepsilon/\mu)$. Der endliche Teil bei $T = 0{,}393$, $\mu = 1$ ist 1,686953 und hängt von der gewählten Skala $\mu$ ab. Das alte Ziel 0,893 ist zurückgezogen.
  - Statusvermerke stehen jetzt an der Dirac-Sonde, an den drei Lesarten der fermionischen Sonde, am Λ-Korollar, an der Verschränkung als gemeinsamer Eigenzeit (eine gemeinsame Uhr beweist allein keine Verschränkung) und an der alten Vorhersageliste.
  - Die Faser $S^7$ war als Gruppe „$\supset G_2 \supset SU(3)$“ beschriftet. Das ist falsch und entfernt: $G_2$ ist die Automorphismengruppe der Oktonionen, $SU(3)$ der Stabilisator einer imaginären Einheit.
- **Neuer Abschnitt „States, Mediators and Clock Comparisons“.**
  - **Vermittler:** Quanten- und Relativitätsauslesung eines gemeinsamen Trägers werden nur über einen Vermittler mit ausdrücklichen Beweispflichten verbunden.
  - **Feld-Dublett:** Das reale Dublett $[E\,|\,B]$ lässt sich lokal aus seiner Gram-Matrix und drei Orientierungsparametern vollständig zurückgewinnen. Der normierte Zustand allein verliert Skala und Flussrichtung.
  - **Uhren:** Zwei Uhren mit festen Raten stimmen nach einer Kalibrierung $\tau = at_a = bt_b$ überein; dafür braucht es keine zweite Quantenzeit.
  - **Numerik:** Die numerische Verträglichkeit der Feldgleichungen erreicht an drei Punkten die vierte Ableitungsordnung. Das ist keine Lösung auf einem Gebiet.
- **H48 (Vorab-Test, widerlegt).** Getestet wurde, ob $\beta_{\mathrm{sym}}$ als eingefrorene Länge des Materie/Tachyon-Zustands aus einer Dynamik folgt.
  - Der eingefrorene Wert hängt an Expansion und Dichte, nicht nur an einem Ratenverhältnis.
  - Ein Einstein–Cartan-Spinterm koppelt nicht, weil der Zustand in der dichten Phase senkrecht zur Chiralitätsachse liegt.
- **Λ als Mischung über Sektor-Kreuzungen (Erkundung).** Keine der 26 Lesarten trifft besser als Zufall. $\Omega_M = \beta_{\mathrm{sym}}^2 \approx 0{,}302$ bleibt die beste Zahl (Planck 2018 −1,9σ, DESI DR2 +0,5σ).
  - Festgehalten wird eine Identität: $\beta^2$ ist das Verhältnis der beiden Eigenwerte des Materie/Tachyon-Zustands.

Nichts davon schließt OP5 oder ändert die Guards.

## OP5: Struktur des Vergleichssystems und eine exakte Eichsymmetrie (r71)

Am 2. November hat der Autor die OP5-Arbeit dort fortgesetzt, wo das zweite Sprachmodell aufgehört hatte (Commit `cf48496`): ein auf 70 Stellen genauer Feldkeim bis zur fünften Ordnung im festen Vergleichsmodell, die zusätzliche Bedingung $\Omega$ an die dritten Ableitungen und eine Zählung bei Grad 5, die je nach Schwelle 1, 0 oder −1 ergab. Runde r71 hält fest:

- **Der Keim ist unabhängig bestätigt.** Zwei eigene Implementierungen ohne gemeinsamen Code mit dem anderen Modell zeigen, dass der Keim das vollständige System $R = (F, G, dg)$ bis Grad 3 erfüllt. Dazu gehört auch der Teil $G$, der vorher nur vom anderen Modell geprüft war.
- **Die −1 ist ein Rechenartefakt.** Mitgezählt wurde eine Richtung, die die Grundregel „der Rand eines Randes ist null“ verletzt. Sauber gezählt kommen mit dem gespeicherten $\Omega$ bei Grad 5 vier neue Klassen heraus, nicht 0 oder 1.
- **Die Struktur dahinter.**
  - Das System lässt eine freie Funktion von vier Variablen unbestimmt.
  - $\Omega$ ist für diese freie Richtung blind und bringt neue Information nur für Wellen auf dem Lichtkegel der rekonstruierten Geometrie oder in zwei besonderen Ebenen.
- **Die freie Funktion ist eine exakte Eichsymmetrie.** Sie verschiebt das Feld entlang des Polarwinkels $\vartheta$. Der Hintergrund des Modells hängt nur von $t$, $r$ und $\varphi$ ab: Die Masse ist $h(t, r)$, die Verbindung ist $A = M(t)\,d\varphi$. Deshalb ändert keine $\vartheta$-Umparametrisierung die Gleichungen.
- **H49 (Vorab-Test, widerlegt).** Vermutet war, dass abseits des Äquators schon bei den zweiten Ableitungen eine versteckte Bedingung auftaucht. Das trifft nicht zu. Die Prämisse, ein Term $\propto z/\rho^2$ breche die Freiheit, war falsch.
- **H50 (Vorab-Test, widerlegt).** Gefragt war, ob $\Omega$ über die $\vartheta$-Richtung auf $\Psi$ zurückwirkt (Frage des Autors). Das tut es nicht: $\Omega$ ist eichinvariant und ändert sich unter allen geprüften Verschiebungen um höchstens $10^{-10}$.

Folgerung: Vor einem Existenzsatz nach Cartan–Kuranishi muss die $\vartheta$-Eichung festgelegt werden. Die Symmetrie gehört zum gewählten Hintergrund; ein Hintergrund, der von $\vartheta$ abhängt, würde sie brechen. OP5 bleibt offen, die Guards sind unverändert.

## OP5: Die ϑ-Eichung, ein Cartan-Test und vier versteckte Bedingungen (r72)

Am 3. November hat der Autor den nächsten Schritt aus r71 angestoßen: die $\vartheta$-Freiheit festlegen und dann prüfen, ob das System vollständig ist. [Layer r72](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r72/README.md) hält fest:

- **Die Eichung.** Als Bedingung dient, dass eine Komponente des Stroms, $\Psi^\dagger K_2\Psi$, eine vorgegebene Funktion des Ortes ist. Sie reagiert auf die $\vartheta$-Verschiebung und legt diese damit eindeutig fest. Auf der Ebene des Symbols ist jede solche Wahl gleichwertig. Die Eichung nimmt genau die freie Funktion heraus und sonst nichts.
- **H51 (Vorab-Test, bestätigt).** Der Cartan-Test prüft, ob die Gleichungen höherer Ordnung nichts Neues mehr erzwingen (Involutivität). Für das geeichte Symbol ist das ab Ordnung 6 der Fall, bei Ordnung 4 und 5 noch nicht – genau wie vorab aus dem Wachstum der Dimensionen vorhergesagt. Danach bleibt keine freie Funktion von vier Variablen mehr übrig; formal hängen die Lösungen von 14 Funktionen von drei Variablen ab, also von Anfangsdaten auf einer Fläche.
- **Formale Integrabilität: drei Tests ungültig (H52–H54).** Ein involutives Symbol reicht nicht; zusätzlich dürfen beim Fortsetzen der Taylorreihe keine neuen Bedingungen auftauchen. Alle drei Tests dazu sind nach ihren eigenen Kriterien ungültig, jedes Mal wegen eines Fehlers in der Testplanung. Was sie trotzdem zeigen:
  - Die gespeicherten Koeffizienten fünfter Ordnung des Keims lassen sich nicht fortsetzen; sie erfüllen die einmal abgeleitete $\Omega$-Bedingung nicht. Für Prüfungen muss die fünfte Ordnung frei bleiben.
  - Über dem reparierten Keim bis Ordnung 4 ist mit den Gleichungen bis Grad 6 alles sauber: Die Freiheitsgrade stimmen genau mit dem geeichten Symbol überein.
  - Mit den Gleichungen vom Grad 7 kommen **vier zusätzliche Bedingungen an die sechsten Ableitungen** hinzu (848 statt 852 Freiheitsgrade).
- **Warum genau vier (Erkundung).** Die Spencer-Kohomologie des Symbols gibt an, wie viele versteckte Bedingungen höchstens möglich sind. Für das geeichte Symbol ist bei Ordnung 5 Platz für genau vier, bei Ordnung 4 für keine. Eine Fehlerschranke (Satz von Weyl) zeigt, dass die gemessenen 848 nicht durch Rechenfehler entstanden sein können. Inhaltlich sind es damit genau vier; formal bestätigt ist das nicht.

Folgerung: Das geeichte Symbol ist involutiv, das geeichte System aber nach allem Anschein bei Ordnung 6 nicht formal integrabel. Nächster Schritt: an einem zweiten Grundpunkt vorab prüfen (H55), dann die vier Bedingungen ausdrücklich bestimmen, ins System aufnehmen und den Cartan-Test wiederholen. OP5 bleibt offen, die Guards sind unverändert.

## OP5: Die vier versteckten Bedingungen bestimmt (r73)

[Layer r73](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r73/README.md) bestätigt und bestimmt die vier Bedingungen aus r72:

- **H55 (Vorab-Test, bestätigt).** Auch an einem zweiten Ausgangspunkt (Ableitungen vierter Ordnung um 50 % geändert) kommen mit den Gleichungen vom Grad 7 genau vier Bedingungen an die sechsten Ableitungen hinzu. Das geeichte System ist bei Ordnung 6 also nicht formal integrabel. Einschränkung: Ein Teil der Rechnung hängt nur von den Ableitungen bis Ordnung 2 ab und ist an beiden Punkten gleich.
- **Was die vier Bedingungen sind (Erkundung).**
  - Echte Gleichungen sechster Ordnung; mit ihnen hat das vollständige Symbol bei Ordnung 6 477 statt 481 Dimensionen.
  - Sie betreffen nur lichtartige Wellen, also Wellen, deren Richtung auf dem Lichtkegel der rekonstruierten Geometrie liegt. Für jede solche Richtung legen sie genau eine von sieben möglichen Polarisationen fest.
  - Welche der vier Bedingungen dabei greift, hängt quadratisch von der Wellenrichtung ab, und zwar über genau die vier Quadriken, die auf den beiden besonderen Ebenen aus r71 verschwinden.
  - Lesart: Es sind die „Krümmungsreste“ der vier Beziehungen $q\,d_k\,\Omega$ aus r71. Auf der Ebene des Symbols sind diese Beziehungen Identitäten; mit den Termen niederer Ordnung bleibt von jeder eine Bedingung sechster Ordnung übrig. Das passt zur Spencer-Zahl $H^{5,2} = 4$.
- **Cartan-Test des erweiterten Symbols: zwei Tests ungültig (H56, H57).** Bis Ordnung 7 ist das Ergebnis sauber: 477 und 594 Dimensionen, bei Ordnung 6 nicht involutiv. Ab Ordnung 8 reicht die Rechengenauigkeit nicht: Ein einzelner sehr kleiner Wert entscheidet, ob das Symbol bei Ordnung 7 oder 8 involutiv wird. Ursache ist, dass $\Omega$ von einem älteren Keim stammt (Abweichung etwa $10^{-7}$), die vier Bedingungen vom reparierten.

Nächster Schritt: ein konsistenter Datensatz am reparierten Keim ($\Omega$ und die vier Bedingungen) mit höherer Genauigkeit, dann den Cartan-Test wiederholen. OP5 bleibt offen, die Guards sind unverändert.

## OP5: Konsistente Daten und eine Genauigkeitsgrenze (r74)

[Layer r74](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r74/README.md):

- **Konsistente Daten (H58, ungültig nach Kriterium).** $\Omega$ wurde am reparierten Keim neu bestimmt, mit derselben Methode wie die vier Bedingungen. Mit diesen konsistenten Daten ergibt sich: Das um die vier Bedingungen erweiterte Symbol wird erstmals bei Ordnung 8 involutiv; formal bleiben 12 Funktionen von drei Variablen. Der Wert 724 aus H57 war ein Artefakt. Weil fünf Rangentscheidungen knapp unter der festgelegten Schwelle lagen, ist der Test formal ungültig.
- **Obergrenze für weitere Bedingungen (Erkundung).** Die Spencer-Kohomologie des erweiterten Symbols lässt Raum für bis zu vier weitere versteckte Bedingungen an siebten und drei an achten Ableitungen. Ob sie auftreten, ist offen.
- **Warum die Rechnung hier an eine Grenze stößt (Methodenprüfung).** Das Symbol aus den Grundgleichungen allein ist numerisch gut gestellt. $\Omega$ und die vier Bedingungen wirken aber nur auf lichtartige Wellen und sind als Gleichungen fast Folgen der Grundgleichungen; ihr eigener Anteil hat nur ein Gewicht von etwa $10^{-8}$. In normaler Rechengenauigkeit lassen sich ein bis zwei solcher Stufen trennen, nicht drei. Eine stufenweise Elimination spart Speicher, löst das aber nicht.
- **Ebene Wellen (Erkundung).** Der Versuch, die Symbolräume aus ebenen Wellen auf dem Lichtkegel aufzubauen, trägt nicht: Die Wellen erreichen die bekannten Dimensionen nicht ganz; der Symbolmodul hat Vielfachheiten.

Nächster Schritt: entweder die ganze Rechenkette mit höherer Genauigkeit oder eine Umformulierung, die die Vielfachheiten berücksichtigt. OP5 bleibt offen, die Guards sind unverändert.

Nachtrag (3. November, Erkundung): Ein erster Lauf auf parallelen GitHub-Runnern hat die Symbolräume des eingefrorenen Symbols bis Ordnung 12 gerechnet. Alle bekannten Werte kamen genau wieder heraus; neu sind $\dim g'_{10}, g'_{11}, g'_{12} = 1065, 1246, 1441$, mit konstanten zweiten Differenzen 14 wie nach H51 erwartet. Einzelheiten unter [Parallele Rechnungen](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Parallele-Rechnungen).

## OP5: Hohe Genauigkeit, formale Integrabilität am Keim und Kovarianz (r77)

[Layer r77](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r77/README.md): Am 3. und 4. November wurde die ganze Rechenkette in hoher Genauigkeit wiederholt (160 bzw. 70 Stellen). Die entscheidenden Eliminationen liefen parallel auf GitHub-Runnern. Danach ging es um Anknüpfungen an die Physik.

- **Genau vier versteckte Bedingungen (Erkundung).** Die Lücke zwischen echten Werten und Rauschen beträgt $10^{58}$. Das erweiterte Symbol hat die Dimensionen 477, 594, 723, 865 bei Ordnung 6 bis 9. Es ist erstmals bei Ordnung 8 involutiv, mit den Charakteren 723, 130, 12, 0.
- **Keine weiteren versteckten Bedingungen (H59, bestätigt).** Die Fasern der 7- und 8-Jets sind 594 und 723, also genau so groß wie das Symbol; die Gegenprobe bei 6-Jets ergibt 477. Damit ist das System am Keim formal integrabel. Seine allgemeine formale Lösung hängt von 12 Funktionen dreier Variablen ab.
- **Sechs masselose Moden (H60, bestätigt).** Je Lichtrichtung gibt es genau 6 reelle Polarisationen, außerhalb des Lichtkegels keine. Die 12 Anfangsdaten sind also 6 masselose Moden.
- **Kein Weyl- oder Majorana-Typ (H61, widerlegt).** Liest man Ψ als drei Dirac-Spinoren mit der üblichen Spin-Wirkung, haben die Moden keine feste Händigkeit und keine feste Helizität.
- **Keine Symmetrie bei festem Hintergrund (H62 und H63, widerlegt).** Das Symbol ist nur unter Skalierung invariant. Schon der dynamische Teil F hat keine Lorentz-Symmetrie. Das ist strukturell zu erwarten: Ψ am Keim steht selbst im Hauptsymbol. Die Sonderebenen Π₀, Π₁ entstehen im G-Teil (r71).
- **Die Konstruktion ist kovariant (H64, bestätigt; zweiter Lauf, nicht blind).** Transformiert man Jets und Hintergrund mit, bleibt R auf Symbolebene unverändert. Das gilt unter beliebigen linearen Koordinatenänderungen und unter inneren Lorentz-Transformationen von Ψ; die Residuen liegen bei höchstens $4\cdot10^{-10}$. Hält man den Hintergrund fest, bricht die Kovarianz mit 0,26. Die Lorentz-Brechung kommt also vom Hintergrund (Ψ am Keim, die Felder A und h), nicht von einem Baustein des Modells.

Nächster Schritt: prüfen, ob auch Ω, θ, die Eichung Ψ†K₂Ψ = S und die vier Bedingungen kovariant sind, und klären, woher der Hintergrund A, h kommt. OP5 bleibt offen, die Guards sind unverändert.

## OP5: Kovarianz auf Werteebene und die Eichung (r78)

[Layer r78](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r78/README.md):
- **R ist vollständig kovariant (H66, bestätigt; nicht blind).** Auch mit allen Termen niedrigerer Ordnung und außerhalb der Lösungsmenge bleibt R unter linearen Koordinatenänderungen und inneren Lorentz-Transformationen unverändert. Die Residuen liegen bei höchstens $2\cdot10^{-11}$. Hält man den Hintergrund fest, steigen sie auf 57 bzw. 1200. Damit ist auch Ω kovariant, denn es wird allein aus R abgeleitet.
- **Die Eichung zeichnet eine Richtung aus (H65, ungültig nach Kriterium).** Wie vorhergesagt bleibt Ψ†K₂Ψ = S nur unter so(1,2) erhalten, also unter der Drehung um y und den Boosts entlang x und z. Teil (a) von H65 wurde ungültig, weil die Kontrollschranke zu streng gewählt war; H66 holt ihn nach.
- **Folge:** Die vier versteckten Bedingungen stammen aus R zusammen mit der Eichung. Sie sind deshalb höchstens unter so(1,2) kovariant. Offen ist, ob ihre Zahl und ihre Lage auf dem Lichtkegel von der Wahl der Eichung abhängen.

OP5 bleibt offen, die Guards sind unverändert.

## OP5: Die vier Bedingungen sind eichunabhängig (r79)

[Layer r79](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r79/README.md):
- **Gleiche Bedingungen in fünf Eichungen (H67, bestätigt).** Die hochgenaue Rechnung der 6-Jet-Faser wurde für fünf Eichungen wiederholt. Neben der bisherigen Eichung (y-Strom) waren das die Dichte Ψ†Ψ, der z-Strom, Ψ†Q₃Ψ und der Lorentz-Skalar Ψ̄Ψ. Jede Eichung lief als eigener Job auf einem GitHub-Runner.
- In allen fünf Fällen hat die Faser die Dimension 477 (20 Ω-Folgerungen und 4 Bedingungen). Auf dem Lichtkegel gibt es 6 Polarisationen, außerhalb keine. Die Lücken liegen bei mindestens $4\cdot10^{56}$.
- **Folge:** Zahl und Lage der vier Bedingungen hängen nicht von der Eichung ab, auch nicht bei der kovarianten Eichung Ψ̄Ψ. Mit r78 gehören sie damit zum kovarianten Inhalt des Systems. Die Lorentz-Brechung kommt nur noch vom vorgegebenen Hintergrund (Ψ am Keim, A, h).

Nächster Schritt: eine eigene Dynamik für den Hintergrund. OP5 bleibt offen, die Guards sind unverändert.

## OP5: Der Hintergrund kommt nicht aus den Spinoren; Abschluss des Zweigs (r80)

[Layer r80](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_r80/README.md):
- **Fierz-Erkundung.** Am Keim liegen alle drei Spinorblöcke im regulären Dirac-Sektor (Yvon–Takabayasi-Winkel ≤ 0,07°). Die Blöcke 0 und 1 strömen mit v = +x/t, Block 2 entgegen (γ = 1,25); alle Spins zeigen entlang der Azimutrichtung, die auch Eichung und Hintergrund auszeichnen.
- **H68 widerlegt.** Geprüft wurde in der Metrik des Modell-Koframes, ob A = M(t) dφ Yang–Mills auf span(λ₂, λ₄, λ₆) mit dem Farbstrom als Quelle erfüllt und h Klein–Gordon mit der Yukawa-Quelle Ψ̄(Y⊗1)Ψ, jeweils mit einer Kopplung. Residuen: Yang–Mills 0,955, Klein–Gordon masselos 0,995, massiv 0,826; schon der Wert am Keim scheitert. Die Quellen sind rund 10³-mal zu klein, die Spinorströme liegen fast ganz in anderen Farbrichtungen. Kontrollen (Bianchi-Identität, exaktes □h, Keimresiduum) gültig. In der flachen Metrik scheitert es ebenso.
- **Abschluss (Autorentscheidung 4.11.).** Das Vergleichssystem hat damit keine innere Quelle für seine Lorentz-Brechung; sie kommt von einem Hintergrund, den es nicht selbst erzeugt. Der Zweig r71–r80 ist geschlossen; seine Ergebnisse bleiben gültige lokale Aussagen über diese Konstruktion, nicht über das QSC-Modell.

Nächster Schritt eine Ebene höher: Bestandsaufnahme der bisherigen Wirkungsansätze und der Mindestanforderungen an eine gemeinsame Dynamik. OP5 bleibt offen, die Guards sind unverändert.

## Nach r80: eine gemeinsame Wirkung W1 (Notizen, noch keine Runde)

[Notizen](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/main/notes/research/v4_10_0_w1/README.md): Nach dem Abschluss des Vergleichsmodells hat der Autor fünf Grundsatzfragen entschieden. Der Koframe ist ein eigenes Feld, gerechnet wird eine reelle Wirkung im Materie-Frame mit der komplexen Lesart parallel, die Gravitation ist Einstein–Cartan ohne kosmologische Konstante, Träger ist die Dixon-Ablage mit dem U(1) aus der inneren Einheit, und der Schließungsprojektor P_C7 bleibt vorerst offen.
- **Komplexe Lesart:** Bei symmetrischer Kinetik ist die Wirkung von selbst reell, die komplexe Lesart fügt nichts hinzu. Ohne Symmetrisierung erzwingt sie mit unabhängiger Verbindung einen verschwindenden Strom und damit, in einem Frame, verschwindende Spinoren. Offen und vom Autor gewollt: ob Anteile mit negativer Dichte im Tachyon-Frame das umgehen.
- **M–T-Lücke (k174):** Mit einem Tachyon-Anteil nach Konvention F trägt dessen Strom gegenüber M eine negative Dichte. Die komplexe Lesart verlangt dann nur, dass sich Materie- und Tachyonstrom aufheben: Materie darf nur entlang der M–T-Achse strömen, quer dazu nichts. Die übrigen Gleichungen sind dann erfüllt, und die Torsion verschwindet. Der Preis: Der Tachyon-Anteil hat gegenüber M eine Kinetik mit umgekehrtem Vorzeichen, und die Achse ist eine Eingabe.
- **H69 bestätigt:** Im flachen Raum hat ein Paar aus zwei gegenläufigen Materiewellen und ihrem um δ versetzten Tachyonbild weder Nettostrom noch Nettoenergie, wenn der Frequenzabstand Δω = π/δ ist (ungerade Vielfache). Der Versatz legt also eine Schwebungsfrequenz fest, und das Paar trägt klassisch nicht zur Vakuumenergie bei. Der nächste Test (H70) koppelt den Versatz an die kosmische Expansion.
- **Torsion:** Die Spinoren koppeln nur über den total antisymmetrischen Teil; nach Elimination bleibt die bekannte Vier-Fermionen-Kopplung −(3/16)κ j² mit dem Gesamtstrom (Kontrolle: Hehl–Datta). Sie sieht die U(1)-Ladung nicht. W1 erzeugt keinen Vakuumterm; dafür braucht es den Skalarsektor.
- **Quellenprüfung:** „mod HC“ in der Meta-Septum-Bedingung ist nirgends definiert; Kompensator und P_C7 sind verschiedene Projektoren. Zwei Ideen des Autors sind mit Auslösern zurückgestellt: mehrere LQG-Systeme mit einem String als Brücke (I1) und „mod HC“ als chinesischer Restsatz über Primzahl-Plätze (I2).

## Umbenennung: Kompensatormatrix (r75)

Die 16×16-Matrix $\mathcal M_{16}$ hieß bisher „Millennium-Matrix“. Der Name ließ an die Millennium-Probleme denken, die der Companion nicht behandelt. Auf Entscheidung des Autors heißt sie seit Runde r75 **Kompensatormatrix**: Sie trägt mehrere Heisenberg-Kompensatoren und überträgt die Regel $C=\tfrac12(\mathrm{id}+J)$ auf alle Schichten. Symbol, Labels und das Kürzel MM (etwa in „MM/HC“) bleiben; ältere Runden und Anhänge behalten den alten Wortlaut. Mathematisch ändert sich nichts. Korrektur (r76): Schon Runde r05 hatte die Matrix „layer-transport matrix“ genannt, ohne den Haupttext zu ändern; das hatte r75 übersehen. Der Autor hat Kompensatormatrix als gültigen Namen bestätigt. Die Einschränkung auf das (E, B)-Dublett heißt weiter „port-weighting matrix“ (Portgewichtung).

## Offene Pflichten und Aussagegrenzen

Die bedingten Cartan- und Kopplungsanalysen liefern keine pauschalen Nachweise regionaler gekoppelter Existenz, vollständiger Gauge-Klassifikation, nativer Massenkoeffizienten oder globaler physikalischer Closure. Für ein bestimmtes Problem die konkrete Quelle und spätere Layer prüfen; dieses Wiki schließt keine OPs. Eine ausführliche Darstellung, woran die Arbeit hängt, steht unter [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme); alle Vorab-Tests unter [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests).

Die 4.10-Basis hält fest: $R_{\mathrm{glob}}=(0,1,1,1,1)$, $\Gamma_{\mathrm{guard}}=(1,1,1,1,1)$, $\beta_4=\frac{1}{256}$ unverbraucht. Die jüngsten Layer melden unveränderte Guard-Vektoren. Dies sind dokumentierte Projektregister, kein vom Wiki unabhängig geprüftes Zertifikat. $C_5=0$, $C_6/T_2$, globaler Photon-Clock/RH-Satz und globale All-Readout-Closure werden dadurch nicht hergeleitet.

Organisatorische Nachverfolgung: [GitHub Issues](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues). Ein geschlossenes Issue ist für sich kein mathematischer Beweis.
