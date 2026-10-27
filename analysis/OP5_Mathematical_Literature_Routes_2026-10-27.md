# OP5: mathematische Literaturwege
Stand: 27. Oktober 2026. Recherche mit Firecrawl-Papiersuche und Websuche; Quellen sind Primärarbeiten bzw. Vorlesungsnotizen des Autors. Keine Behauptung einer vollständigen Suche durch sämtliche Mathematik. Keine der gefundenen Arbeiten liefert bereits einen unmittelbar anwendbaren OP5-Lösungssatz.

## Ausgangslage
Grundlage: Repository-Checkpoint 5913abb und anschließender lokaler Test OP5_Constraint_Set_And_Ensemble_Result.md. Im Vergleichsmodell ließ sich der Dirac-Zeitvektor an zwei Punkten erst mit erweiterten Boost- und chiralen Richtungen vollständig darstellen. Die bislang vorgeschriebene Menge mit verschwindenden räumlichen Gesamtströmen und axialem Gesamtstrom ist unter dieser Dynamik nicht invariant. Eine lokale Zweiermischung beseitigte axialen, aber nicht radialen Drift. Neu berechnete Coframes blieben invertierbar und lorentzsch; ihre Rückkopplung in den kinetischen Operator fehlt. Diese Befunde betreffen den untersuchten Ansatz, nicht ein allgemeines Unmöglichkeitstheorem für OP5.

## 1. Clifford-Algebra und polare Spinoren: unmittelbar beginnen
Luca Fabbri, General Dynamics of Spinors, arXiv:1707.03270v3 (5.12.2018), insbesondere Gleichungen (10), (11), (30) und die vollständigen polaren Dirac-Gleichungen.
https://arxiv.org/abs/1707.03270v3

Geprüfte Textpassagen geben Theta=2 phi² sin(beta), Phi=2 phi² cos(beta). Im regulären Sektor Phi²+Theta²>0 beschreibt der Yvon–Takabayasi-Winkel das Verhältnis von Pseudoskalar und Skalar. Unser zusätzlicher chiraler Parameter gehört zu diesem bekannten Freiheitsgrad. Bei kompatiblen Gamma-Konventionen entspricht exp(+i chi gamma5/2) der dortigen exp(-i beta gamma5/2) mit beta=-chi. Signaturen und Definitionen müssen explizit übersetzt werden. Singularspinoren sind separat zu behandeln.

Konkreter Test: Jede Spezies mit vollständigen polaren Variablen einschließlich eigener Winkelentwicklung parametrisieren; sämtliche Dirac-Komponenten prüfen. Nicht lediglich Stromerhaltung oder abgeleitete skalare Gleichungen erfüllen. Erfolg wäre eine lokale Feldentwicklung einschließlich räumlicher Ableitungen; ein Zweipunkt-Tangentenfit genügt nicht.
Bewertung: Quelleninhalt geprüft; Übertragung auf die triadische Kopplung bedingt.

Shaun Inglis und Peter Jarvis, Fierz bilinear formulation of the Maxwell-Dirac equations and symmetry reductions, arXiv:1405.6762v1 (27.5.2014), Gleichungen (10–14), (30–32).
https://arxiv.org/abs/1405.6762v1

Fierz-Identitäten und Rekonstruktion verbinden bilineare Größen mit tatsächlichen Spinoren. Der Nenner sigma²-omega² in deren Konvention entspricht bei reellem Pseudoskalar sigma²+p5². Regularität ist erforderlich. Die U(1)-Maxwell-Dirac-Rekonstruktion ist kein fertiger Satz für unseren internen Verbindungsraum. Test: algebraische Fierz-Bedingungen UND vollständige Differentialbedingungen verlangen, damit passende Ströme keine nichtrekonstruierbaren Scheinkandidaten erzeugen.

## 2. Symplektische Geometrie: zulässige Zustandsmenge systematisch bestimmen
Gracia, Martin, Roman-Roy, Constraint algorithm for k-presymplectic Hamiltonian systems. Application to singular field theories, arXiv:0903.1791v1, Abschnitt 3.2.
https://arxiv.org/abs/0903.1791v1

Das Verfahren sucht zunächst Punkte, an denen die Bewegungsgleichung lösbar ist, dann solche, an denen ihre Lösungsrichtungen tangential zur bisherigen Nebenbedingungsmenge liegen. Iteration kann eine stabile Menge oder Unverträglichkeit ergeben. Die betrachteten Mengen müssen reguläre Untermannigfaltigkeiten sein; bei Feldtheorien ist zusätzlich die Integrabilität der Mehrfachrichtungen zu prüfen.

OP5-Test: Native Bedingungen von freiwilligen Ansatzbedingungen trennen. Aus C=0 die Erhaltungsbedingungen ableiten und weiterführen. Verschwindender räumlicher Strom und E=I dürfen nicht ohne Herleitung als universelle Forderungen eingehen. Multiplikatoren aus dem gemeinsamen System bestimmen, nicht durch nachträgliche Projektion.
Bewertung: Algorithmus geprüft; Anwendung verlangt zuvor einen geeigneten gemeinsamen variationalen Aufbau.

## 3. Differentialgeometrie/PDE: formale Integrabilität vor weiteren Fits
J. M. Landsberg, Exterior differential systems: a geometric approach to PDE, arXiv:dg-ga/9708005, Vorlesungen zu Pfaff-Systemen, Cartan-Test und Prolongation.
https://arxiv.org/abs/dg-ga/9708005

Geprüft wurden Definitionen, Kompatibilitätsbeispiele und der Weg über Tableau/Prolongation. Ein punktweise lösbares Ableitungssystem muss noch kein Feld sein: gemischte Ableitungen und weitere differenzierte Bedingungen können widersprechen. Cartan–Kähler ist ein analytischer Existenzweg mit Regularitäts-/Involutionsvoraussetzungen, kein allgemeiner glatter Existenzsatz; hier wurde kein vollständiger Anwendungssatz für OP5 nachgewiesen.

Test: Dirac-Gleichung, Coframe-Definition und Verbindungsbedingungen gemeinsam als Jet-System formulieren; Symbol, versteckte Bedingungen und nächste Ableitungsordnung prüfen. EDS-Torsion bezeichnet dabei einen Kompatibilitätsterm und ist nicht automatisch physikalische Raumzeit-Torsion.

## 4. Variationsrechnung: gemeinsame Wirkung prüfen
Igor Khavkine, Presymplectic current and the inverse problem of the calculus of variations, arXiv:1210.0802, Theorem 3.
https://arxiv.org/abs/1210.0802

Geprüfter Satz: Ein geeigneter horizontal und vertikal geschlossener presymplektischer Strom kann unter Regularitäts- und lokalen Kohomologievoraussetzungen eine Lagrange-Dichte erzeugen. Entscheidende Grenze: Die alten Lösungen sind Lösungen des konstruierten Euler–Lagrange-Systems; Gleichheit beider Lösungsmengen folgt nicht automatisch.

Test: Variationale Verträglichkeit der Kopplungen/Noether-Identitäten prüfen. Eine eingeführte Multiplikatorwirkung ist noch keine Herleitung der nativen Kopplung und kann zusätzliche Lösungen zulassen.

## 5. Hyperbolische PDE und Funktionalanalysis: selbstkonsistente Rückkopplung
Peng Zhao und Xiaoning Wu, On the local existence for the characteristic initial value problem for the Einstein-Dirac system, arXiv:2509.04167v1, Theorem 2, Abschnitt 4.2.
https://arxiv.org/abs/2509.04167v1

Geprüft: lokaler glatter Existenz-/Eindeutigkeitsweg für reguläre charakteristische Daten auf zwei sich schneidenden Nullflächen mit kontrollierten Normen. Zusätzliche Spinorableitungen schließen das gekoppelte Abschätzungssystem. Das ist Standard-Einstein–Dirac, nicht die zusammengesetzte Coframe-Definition von OP5. Die dortige Spinornotation Lambda=-R/24 darf nicht mit unserer kosmologischen Konstante verwechselt werden.

Test: E, Verbindung, Spinoren und erforderliche Ableitungen zunächst gemeinsam als Unbekannte führen, Coframe-Definition als Bedingung einbauen; Eichung, Hauptsymbol und Erhaltung prüfen. Erst dann lokale Existenz anstreben.

Baldi und Haus, A Nash-Moser-Hörmander implicit function theorem with applications to control and Cauchy problems for PDEs, arXiv:1609.00213, Theorem 2.1.
https://arxiv.org/abs/1609.00213
Geprüft wurden der Beginn des Satzes und Glättungsabschätzungen, nicht alle Beweisdetails. Möglicher späterer Weg bei Ableitungsverlust; passende Skalen, Abschätzungen und ein kontrollierter Rechtsinverser bleiben nachzuweisen. Punktweiser Rang genügt nicht.

## 6. Maßtheorie und Optimierung: die Mengenroute ernsthaft formulieren
Adolfo Arroyo-Rabasa, Characterization of generalized Young measures generated by A-free measures, arXiv:1908.03186, Abschnitt 1.3.
https://arxiv.org/abs/1908.03186

Geprüfte Voraussetzungen: homogener linearer Differentialoperator mit konstanten Koeffizienten und konstantem Symbolrang, geeigneter beschränkter Grundbereich. Die Theorie berücksichtigt, dass nicht jede gewünschte nichtlineare Mittelung durch differentialverträgliche Felder erzeugt werden kann. Keine unmittelbare Anwendung auf das volle nichtlineare gekrümmte Dirac-System.

Semidefinite Approximations of Invariant Measures for Polynomial Systems, arXiv:1807.00754, Abschnitte 2–4.
https://arxiv.org/abs/1807.00754

Geprüft: polynomiale endlichdimensionale Dynamik, kompakte semialgebraische Zustandsmenge, positive Wahrscheinlichkeitsmaße und Momenthierarchien; Konvergenzaussagen haben zusätzliche Voraussetzungen.

Test: Erst eine begründete endliche Reduktion und gemeinsame Dynamik festlegen. Dann positive Gewichte bzw. Verteilungen unter sämtlichen relevanten Erhaltungsbedingungen suchen. Ein stationäres Ensemble ist eine stärkere Sonderwahl; allgemeine zeitabhängige Ensembles brauchen ihre Transportgleichung. Ein einzelner verschwindender Mittelwert beweist beides nicht. Zertifizierte Unzulässigkeit kann eine Reduktion ausschließen; eine endliche zulässige Momentrelaxation beweist keine Kontinuumslösung.

## 7. Numerik und weitere gesichtete Gebiete
- Geometrische Integration: McLachlan, Modin, Verdier, Wilkins, Geometric Generalisations of SHAKE and RATTLE, arXiv:1207.3367. Geprüfte Textstellen verlangen Nichtentartung und Coisotropie. Für konsistente Nebenbedingungen hilfreich; kein Reparaturverfahren für widersprüchliche Physik. https://arxiv.org/abs/1207.3367
- Kinetik/Wigner-Funktionen: arXiv:1912.01169 und 2004.07510, nur Abstract-Sichtung. Mögliche Spin-Transportbeschreibung, aber Näherungsordnung und Schließung sind zusätzliche Annahmen.
- Topologie/h-Prinzip: arXiv:2210.07746, Abstract-Sichtung. Offene ample Differentialrelationen; diese Eigenschaft ist für unsere Gleichungsbedingungen nicht belegt. Keine allgemeine Existenzabkürzung.
- Spektralgeometrie: Chamseddine/Connes, The Spectral Action Principle, hep-th/9606001; Vassilevich, Heat kernel expansion: user's manual, hep-th/0306138. Spektrale Wirkung als möglicher Rückweg zum ursprünglichen Vakuumproblem. Identität/Abstract bzw. einzelne Textstellen geprüft, keine OP5-Koeffizienten hergeleitet. Zuerst nativen Operator, Definitionsbereich, Regularisierung und Lorentz-/euklidische Übersetzung festlegen. https://arxiv.org/abs/hep-th/9606001 ; https://arxiv.org/abs/hep-th/0306138

## 8. Die kosmologische Konstante bleibt eine eigene Beweisstufe
Green und Wald, A new framework for analyzing effects of small scale inhomogeneities in cosmology, arXiv:1011.4920, Voraussetzungen (i–iv), Theoreme 1 und 2.
https://arxiv.org/abs/1011.4920
Geprüft: Unter ihren speziellen Einstein-Familien-, Kleinheits-, schwachen Grenzwert- und Energiebedingungen ist der effektive Rückwirkungstensor spurfrei. Damit kann er dort keinen nichtverschwindenden reinen Lambda-Term ersetzen. Kein universelles Verbot sämtlicher Mittelungsverfahren! Unsere Coframe-Varianz ist bislang ohnehin kein hergeleiteter Energietensor.

Kaloper, Padilla, Stefanyszyn, Zahariade, A Manifestly Local Theory of Vacuum Energy Sequestering, arXiv:1505.01492; PRL 116, 051302 (2016).
https://arxiv.org/abs/1505.01492
Geprüfte Schlussabschnitte: Vierformfelder erlauben einen Mechanismus zur radiativen Stabilisierung; der verbleibende endliche Wert wird nicht automatisch vorhergesagt. Zusätzliche Wirkungsstruktur muss begründet werden. Interessanter Vergleich für den absoluten Anteil, kein fertiger OP5-Beweis.

## Empfohlene Reihenfolge
1. Vollständige polare/Fierz-Variablen und Konventionsübersetzung.
2. Native Bedingungen von zu engen Ansatzbedingungen trennen.
3. Gekoppelte Dynamik mit Coframe-Rückkopplung und systematischer Kompatibilitätsprüfung.
4. Lokale PDE-Lösung statt isolierter Punktfits.
5. Ensemblezweig getrennt mit positiver Verteilung und gemeinsamer Transportdynamik.
6. Erst aus einer konsistenten Wirkung den absoluten Volumenterm untersuchen.

Ergebnis: Die aussichtsreichste unmittelbare Verbindung ist polare Spinordynamik plus Nebenbedingungs-/Integrabilitätsanalyse. Sie adressiert unsere beobachtete Lücke konkret. Ob sie OP5 löst, bleibt offen.

## Rechercheprovenienz und Grenzen
18 thematische Firecrawl-Papiersuchen plus ergänzende Websuche; Suchlisten und Ergebnis-Metadaten im begleitenden JSON. Körpertext-Passagen zu den oben als geprüft bezeichneten Aussagen wurden gelesen, nicht sämtliche Beweise sämtlicher Arbeiten. Nur ausdrücklich genannte Versionen wurden an der offiziellen Versionsgeschichte festgemacht. Unversionierte Links können künftig neuere Fassungen zeigen. Kein Volltextarchiv, keine Hash-basierte Versionsfixierung; keine urheberrechtlichen Volltexte gespeichert. Kein Neuheits- oder Vollständigkeitsanspruch. Die Recherche wurde anschließend auf Nutzerwunsch zusammen mit den Mengenprüfungen als Repository-Checkpoint gesichert.
