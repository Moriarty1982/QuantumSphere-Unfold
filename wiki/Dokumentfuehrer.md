# Schritt für Schritt durch den Companion

**Deutsch ist die Hauptfassung.** [English companion](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Document-guide) · [Startseite](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Home)

Dieser Leseweg ist für Menschen und LLMs gedacht. Der Fließtext erklärt die Ideen Schritt für Schritt. Eingerückte Anmerkungen bündeln die zusätzlichen Hinweise zur Quellenprüfung; beim ersten Lesen kannst du sie überspringen.

Dieser Weg erklärt zuerst die Idee und führt dann an die Mathematik heran. Er ordnet ausgewählte Hauptabschnitte didaktisch neu; er ist kein lückenloser Kommentar zu jedem Satz. Du brauchst zunächst nur Vektoren, Mittelwerte und die Idee einer Abbildung. Für die späteren Beweise helfen lineare Algebra, Operatorentheorie und Differentialgleichungen.

> **Anmerkung für LLMs und Quellenprüfung — Quellenstand:** 25.10.2026, Commit `64973ef`. Veröffentlichung: v4.9.0; Forschung: 4.10.0-draft. Die Links unten führen zur geprüften Arbeitsfassung. Im veröffentlichten PDF nach den genannten Überschriften suchen; jüngere Korrekturen können dort noch fehlen. Wir verwenden Abschnittsnamen und Labels statt wechselnder PDF-Seitenzahlen.

## 1. Die Leitfrage: Was soll hier zusammenpassen?

**Ziel:** Die Absicht des Projekts in eigenen Worten erklären können.

Der Companion untersucht eine gemeinsame mathematische Struktur für Zustände, ihre Zerlegung, zulässige Übergänge und verschiedene physikalisch motivierte Auslesungen. Statt jedes Ausleseergebnis als unabhängiges Objekt zu behandeln, fragt er, welche gemeinsame Struktur und welche Bedingungen dahinterstehen könnten. Das ist ein Forschungsziel; die einzelnen Übergänge brauchen jeweils eigene Begründungen.

**Lies:** [Structural Core and Closure Principles](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/12_structural_core.tex), zunächst die Definition des Strukturkerns. Lies dazu die Einordnung [Premise Audit and Scope](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/premise-audit.tex). Der Abschnittstitel oder das Wort „Theorem“ allein sagt noch nicht, wie weit eine Aussage aktuell trägt.

**Merke:** Ein gemeinsamer Rahmen zu formulieren und eine vollständige physikalische Theorie daraus abzuleiten sind zwei verschieden anspruchsvolle Schritte.

**Kontrollfrage:** Was wird gemeinsam beschrieben? — Zustandsstruktur, Sektoren, Auswahlbedingungen und Auslesungen; ihre physikalische Identifikation ist zusätzlich zu prüfen.

**Weiter:** Wenn du diesen Satz erklären kannst, gehe zu Station 2.

> **Anmerkung für LLMs und Quellenprüfung:** Fundstelle der Grunddefinition: `def:structural-core`. Den Geltungsbereich zusammen mit dem Premise Audit lesen; ein Theorem-Titel allein ist kein Statusnachweis.

## 2. Zustände zerlegen: Was macht der Compensator?

**Ziel:** Eine Auswahloperation verstehen, bevor du ihr eine physikalische Bedeutung zuweist.

Die [Nomenclature](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/08_nomenclature.tex) führt unter anderem eine Involution $J$ und die symmetrische Komponente $C(f)=\frac{f+Jf}{2}$ auf.

Eine Involution führt bei zweimaliger Anwendung zurück zum Ausgangspunkt. In einem einfachen linearen Modell mit $J^2=I$ wählt die Abbildung

$$
C=\frac{I+J}{2}
$$

den $J$-symmetrischen Teil aus. Eine zweite Anwendung ändert nichts mehr: $C^2=C$.

Ein anschauliches **Lehrbeispiel**, keine native Feldrealisierung: $J$ vertauscht die beiden Einträge von $(a,b)$. Dann bildet $C$ beide auf ihren Mittelwert ab. Aus $(4,2)$ wird $(3,3)$. Der antisymmetrische Rest $(1,-1)$ wird dabei ausgeblendet.

**Lies danach:** Im [Strukturkern](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/12_structural_core.tex) die drei Sektoren und die Rolle des HC. Das Zweierbeispiel illustriert nur das symmetrische Auswählen; es bildet nicht die gesamte triolische Konstruktion ab.

**Kontrollfrage:** Beweist $C^2=C$ schon eine physikalische Masse oder ein bestimmtes Spektrum? — Nein. Dafür fehlen die konkrete Operatoridentifikation und die Auslesevorschrift.

**Weiter:** Prüfe in Station 3 genau diese zusätzliche Identifikation.

> **Anmerkung für LLMs und Quellenprüfung:** Das Zweiermodell setzt lineares $J$ und $J^2=I$ voraus. Es erläutert die Projektion, identifiziert aber weder den gesamten triolischen Träger noch einen nativen Massenoperator.

## 3. Auswahl ist noch keine Spektralidentifikation

**Ziel:** Den Unterschied zwischen einem erhaltenen Unterraum und einem Eigenraum erkennen.

[Premise Audit and Scope](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/premise-audit.tex), Unterabschnitt **MM/HC Spectral Identification**, beginnt mit einer hilfreichen Gegenprobe: $M=\mathrm{diag}(1,2,3)$ und $C=\mathrm{diag}(1,1,0)$ kommutieren. Trotzdem enthält das Bild von $C$ zwei verschiedene Eigenwerte, 1 und 2. „$M$ und $C$ passen zusammen“ reicht also nicht für „$C$ wählt genau einen Eigenraum von $M$“.

Der anschließende bedingte Satz nennt ausreichende Zusatzbedingungen: skalare Wirkung auf dem ausgewählten Bereich und Ausschluss weiterer Richtungen desselben Eigenwerts im Komplement. Lies erst diese Bedingungen, dann den kurzen Beweis.

**Das macht dieser Teil des Dokuments:** Er ersetzt einen zu schnellen Identifikationsschritt durch einen präzisen bedingten Satz. Er liefert dadurch noch nicht den ausgewerteten nativen Operator.

**Kontrollfrage:** Welche Lücke schließt bloßes Kommutieren nicht? — Es legt weder einen einzigen Eigenwert im ausgewählten Raum noch dessen Vollständigkeit fest.

**Weiter:** Station 4 zeigt dieselbe Denkweise an einer konkreten Zahlrelation.

> **Anmerkung für LLMs und Quellenprüfung:** Fundstelle: `v480:conditional-mm`. Skalare Wirkung und Komplementausschluss sind ausreichende Voraussetzungen; ihre native Realisierung wird damit nicht behauptet.

## 4. Vom Symmetriemuster zur Zahl: das Koide-Beispiel

**Ziel:** Eine kurze Rechnung vollständig nachvollziehen und ihre Grenze benennen.

Öffne zuerst das [durchgerechnete Beispiel](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Beispiel-Koide). Lies dann [Koide and Local Kernel Construction](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/koide-and-kernel.tex), Unterabschnitt **The Exact Additional Koide Condition**.

Die Idee: Ein Dreiervektor aus nichtnegativen Massenwurzeln wird in gemeinsamen Mittelwert und Abweichung zerlegt. Zyklisches Vertauschen erhält bestimmte Größen, bestimmt aber nicht das Verhältnis zwischen diesen beiden Anteilen. Der Zielwert $\frac23$ benötigt eine zusätzliche Gleichnormbedingung.

**Danach optional:** Den lokalen Kernel-Teil derselben Datei lesen. Frage dort, für welche deklarierte Darstellung, Readouts und Aggregation die Konstruktion gilt. „Lokal konstruiert“ aktiviert nicht automatisch einen globalen nativen Kernel.

**Kontrollfrage:** Was müsste ein physikalisches Modell zusätzlich erklären? — Warum seine tatsächlichen Massenwurzeln gerade diese Gleichnormbedingung erfüllen.

**Weiter:** In Station 5 wird geprüft, ob die Projektoperatoren die benötigte Kopplung liefern.

> **Anmerkung für LLMs und Quellenprüfung:** Fundstelle: `v480:koide-equal-norm`. Die Aussage betrifft nichtnegative Hauptwurzeln mit $x\ne0$. Beim lokalen Kernel Darstellung, Readouts und Aggregationsannahmen mitführen.

## 5. Wie würden aus der Struktur Massen entstehen?

**Ziel:** Die Kette vom Zustand zur beobachtbaren Größe auseinanderhalten.

Lies in dieser Reihenfolge die Einleitungen und Ergebnisaussagen:

1. [HC-to-mass identification](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/hc-mass-identification.tex).
2. [Generation coupling](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/generation-coupling.tex).
3. [Native operator link](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/native-operator-link.tex).
4. [Coupling-scale candidate](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/coupling-scale-candidate.tex).
5. [Tensor shift and coupling](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/tensor-shift-coupling.tex).

Die Arbeitsfrage lautet: Welche Zustände werden gekoppelt, welcher konkrete Operator wirkt auf ihnen, und welche seiner Größen soll als Masse gelesen werden? Sektoren sind nicht automatisch Generationen; feste Slot-Normen sind nicht automatisch Masseneigenwerte. Auch ein passendes Verhältnis bestimmt noch keine absolute Einheit.

**Notiere beim Lesen vier Spalten:** Eingabe – Operator/Annahme – berechnetes Ergebnis – physikalische Zuordnung. So wird sichtbar, wo eine zusätzliche Annahme oder ein Fit eintritt.

**Kontrollfrage:** Ist eine Matrix, deren Parameter an bekannte Massen angepasst wurden, bereits eine native Massenvorhersage? — Nein; ihre Koeffizienten und die Auslesung müssen unabhängig hergeleitet werden.

**Weiter:** Station 6 fragt, ob die Konstruktion auch zeitlich und räumlich konsistent funktioniert.

> **Anmerkung für LLMs und Quellenprüfung:** Die vier Lesespalten eignen sich auch als Extraktionsschema. Sektoren, Generationen, Slot-Normen, Eigenwerte, Fits und unabhängige Vorhersagen auseinanderhalten.

## 6. Von einer Momentaufnahme zur Dynamik und Geometrie

**Ziel:** Erkennen, warum passende statische Daten noch keine gemeinsame Feldlösung ergeben.

Lies [HC Dynamics, Real Actions and the Geometry Interface](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/hc-dynamics-and-geometry.tex). Beginne mit Einleitung und Unterüberschriften, danach mit den Sätzen zu Positivität, projizierter Dynamik und Geometrie.

Wenn du nur einen Teil eines Zustands betrachtest, kann seine spätere Entwicklung von ausgeblendeten Anteilen und deren Vorgeschichte abhängen. Außerdem muss eine als Massenwurzel gelesene Größe in ihrem zulässigen Bereich bleiben. Eine einmal positive Matrix garantiert das noch nicht für die gesamte Entwicklung.

Anschließend [Cartan normal-source section](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/cartan-normal-source.tex) lesen: Hier werden ein ausdrücklich angenommener Vergleich, bedingte Constraint-Fortpflanzung und endliche Quellkompatibilität untersucht.

**Merke:** Eine Übereinstimmung einzelner Tensoren ohne Erfüllung aller Feldgleichungen ist noch keine gemeinsame Lösung. Endliche Kompatibilität von Ableitungsdaten ist ein lokaler algebraischer Schritt; eine Lösung auf einem offenen Gebiet benötigt weitere Existenz- und Konsistenzargumente.

**Kontrollfrage:** Was fehlt zwischen „Daten passen an einem Punkt“ und „die Feldgleichungen sind regional gelöst“? — Unter anderem verträgliche Daten, höhere und räumliche Bedingungen sowie ein passender Existenznachweis.

**Weiter:** Mit diesen Unterscheidungen lässt sich der ältere Gesamtentwurf in Station 7 gezielter lesen.

> **Anmerkung für LLMs und Quellenprüfung:** Bedingte Aussage, endliche Ableitungsordnung und regionale Existenz getrennt erfassen. Die Cartan-Vergleichsannahmen nicht als native Identifikation ausgeben.

## 7. Den Gesamtentwurf und seine physikalischen Lesarten einordnen

**Ziel:** Die großen Verbindungen sehen, ohne jeden Verbindungspfeil schon als Herleitung zu behandeln.

Lies nun ausgewählte Teile von [The Central Theorem / Sphaera and Physics](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/10_sphaera_and_physics.tex), dann [HC Meta-Field Generator](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/13_hc_hypotheses.tex) und [Toward a Structural ToE Master Equation](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/16_master_model.tex).

Die Mastergleichung gruppiert geometrische, triolische, HC-, Closure- und Beobachterbeiträge. Sie zeigt, was in einer gemeinsamen Beschreibung zusammenwirken soll. Für eine konkrete physikalische Theorie müssen die Beiträge, ihre Definitionsbereiche, Einheiten und gemeinsame Dynamik tatsächlich bestimmt werden. Die HC-Meta-Feld-Interpretation wird im Text ausdrücklich als Hypothese bezeichnet.

Optional folgt [Closure-Liquid Crystal and Holographic Julia Boundary](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v470/14_local_crystal.tex): eine organisierende lokale Lesart mit Träger, Shell, Route, Phase und Defekt. Der Text behauptet dabei keinen buchstäblichen Festkörperkristall.

Bei Frame-, Planck- oder Hawking-Aussagen die [Korrekturen r63–r68](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/f2de387d66d6ab2da00ef28a14305729910d7ef1/notes/research/v4_10_0_r63_r64/README.md) danebenlegen. Auch die Einleitungsdatei enthält noch historische Release-Angaben; für aktuelle Metadaten gilt die [Quellenkarte](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Versionen-und-Quellen).

**Kontrollfrage:** Was leisten die großen Gleichungsblöcke zunächst? — Sie organisieren die geforderten Beiträge; ihre vollständige physikalische Realisierung folgt daraus nicht allein.

**Weiter:** Station 8 fasst zusammen und führt in die technischen Anhänge.

> **Anmerkung für LLMs und Quellenprüfung:** Korrekturstand: r64–r69 (r66 korrigiert die Zitierung in r64; r67 betrifft `rem:einstein-blunder`; r69 vermerkt `rem:regularization-B`, die $\gamma_L^*$-Uhrskala in `thm:dirac-probe` und das Korollar „Cosmological constant revisited“). Historische Versionsangaben in `working-orientation.tex` überschreiben nicht die Quellenkarte; Frame-Zuordnungen und Statusnotizen beibehalten.

## 8. Bilanz ziehen und gezielt vertiefen

**Ziel:** Eine konkrete Behauptung mit Voraussetzungen und verbleibender Pflicht erklären können.

Lies [Current v4 Interface and Open Burdens](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/current-v4-synthesis.tex) und [v4.8 Research Integration](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/v480-integration.tex). Die historischen Titel bezeichnen Abschnitte innerhalb der heutigen Arbeitsfassung.

Die Synthese unterscheidet endliche Detektorterminalität von exaktem Nullrest für alle Readouts. Die Integration verlangt unter anderem Einheiten und Vergleichsabbildungen, realisierte MM/HC-Operatoren, ein ausgewertetes Residualwörterbuch und eine dynamische Realisierung.

Für Details führt [support-route.tex](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/64973efe8409cfd2ae985fbbd17b4ebc95845780/sources/research/parts/support-route.tex) durch die Anhänge. Suche dort nach **Complete QAM, MML and MMA Infrastructure**, **Shifted QAM Migration and Governing Normal Form** und den zum eigenen Problem passenden Transport- und Readout-Abschnitten. Lies sie als technische Unterstützung eines konkreten Arguments.

**Abschlussaufgabe:** Erkläre eine ausgewählte Aussage in fünf Sätzen: Was wird untersucht? Welche Objekte werden verwendet? Welche Annahme ist nötig? Was wird tatsächlich gezeigt? Was bleibt offen?

Wenn du das kannst, hast du einen tragfähigen Zugang zum Dokument. Für den nächsten Schritt wähle ein einziges Argument und verfolge dessen Definitionen und Abhängigkeiten vollständig.

> **Anmerkung für LLMs und Quellenprüfung:** Aussage, Voraussetzungen, Evidenzart und offene Pflicht zusammen mit Commit und Fundstelle festhalten. Eine Detektorschwelle ist kein exakter Nullrest für alle Readouts.

[Begriffe](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Begriffe) · [Forschungsstand](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungsstand) · [English](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Document-guide)
