# OP5-Neuaufbau: Beobachter, Feldoperation und Portselektion

**6. November 2026. Quellenrekonstruktion; algebraische Folgerungen ausdrücklich nicht blind.** Basis `b6b9846`. Keine neue Rechnung, kein experimenteller Test und keine neue H-Nummer. Selbstprüfung durch Codex; begrenzter Untersuchungsgegenstand ist die operative Bedeutung der Auslesung aus dem Feld-Datenblatt.

## 1. Ergebnis

**Die Gleichsetzung „Portprojektion = passiver Framewechsel desselben vollständigen Zustands“ ist für die dargestellten Operationen nicht tragfähig.** Die Projektion ist rangsenkend und nicht allgemein invertierbar. Die vorhandenen Quellen unterscheiden sie von Dualitätsrotation, Spiegeloperation, Zeitumkehr und Lorentz-Boost.

Eine physikalische Identifikation der M/T/P-Lesarten mit Auslesungen desselben Objekts bleibt damit **unvollständig**: Es fehlt die konkrete gemeinsame Transformation von Zustand, Vergleichsaufbau und Messgröße. Dies widerlegt weder die Projektoralgebra noch jede mögliche physikalische Realisierung. Die ältere T9-/Λ-Interpretation erhält aus den Portformeln allein keine Begründung.

## 2. Quellen und Vorwissen

- `notes/research/v4_9_0_r01_r16/rounds/v490_r02_round.tex`, r02.1–r02.5: Dualitätsweg, Holonomie, J_B und kompensierte Kanäle. Der dort nur angebotene OP5-/HC-Kegel-Vergleich ist ausdrücklich nicht übernommen.
- Gleicher Ordner, `v490_r03_round.tex`, r03.1–r03.4: Zweiarmschema, Portdifferenz, Mittelwert und Produkt als verschiedene Konstruktionen.
- Gleicher Ordner, `v490_r04_round.tex`, r04.1–r04.3: reelle Doppeloperationen und Messauslesung.
- `notes/research/v4_10_0_r26_r31/rounds/v490_r28_round.tex`: Korrektur der Tachyon-Abbildung zu z ↦ iz; Messgerät als zusätzliches Kopplungsmodell.
- `notes/research/v4_10_0_r48_r55/rounds/v490_r51_round.tex`: Zeitumkehr T und Tachyon-Frame sind auseinanderzuhalten; Aussagen betreffen unterschiedliche Träger/Dixon-Sektoren.
- `sources/research/parts/v410-state-mediator-synthesis.tex`, `subsec:v410-oriented-mediator`: Operationen im vollständigen lokalen Feldwörterbuch und Grenzen reduzierter Register.

Einordnung im Gesamtbild: T1 bleibt physikalische Vermutung, T2 liefert den algebraischen Projektor, T9 ist nicht daraus hergeleitet. Auslöserliste I1–I4 geprüft: hier tritt keine neue Zwei-Kegel-Obstruktion oder Skalenrechnung auf. Die Korrektur unterschiedlicher Operationsarten aktiviert keinen String-/Kondensatansatz; W1/W2 bleibt eingefroren.

## 3. Die Operationsliste

| Operation im Quellenmodell | Wirkung | Was damit feststeht | Was nicht feststeht |
|---|---|---|---|
| räumliche Rotation | F ↦ RF | invertierbare räumliche Aktion, G bleibt gleich | aktive Feldrotation oder passive Achsenwahl erst mit Vergleichskonvention entschieden |
| gewöhnlicher Beobachterboost | mischt E/B durch richtungsabhängige Kreuzprodukte | s bleibt im angegebenen Lorentz-Rahmen erhalten; vollständige Felddaten benötigt | keine Gleichsetzung mit einer beliebigen rechten 2×2-Doppeloperation |
| Dualitätsrotation | z ↦ exp(iα)z | invertierbar, s ↦ exp(2iα)s | kein gewöhnlicher Lorentz-Beobachterwechsel; passive interne Konvention nur mit mittransformierten Definitionen/Auslesungen |
| Tachyon-Abbildung in korrigierter Konvention F | z ↦ iz | benannte Vierteldrehung, s ↦ −s | nicht J_B und nicht Zeitumkehr |
| Zeitumkehr, lokale Feldkomponente | z ↦ conjugate(z) | unterscheidbare antilineare Operation | vollständige Raumzeit-/Quellentransformation nicht durch diese Punktformel ersetzt |
| Involution J_B | z ↦ i conjugate(z), E und B vertauscht | reell-linearer involutiver Reflektor; s ↦ −conjugate(s) | keine allgemeine Lorentz-invariante Beobachterumrechnung |
| Kompensator | F ↦ FC₊ | rangsenkende Projektion auf den gewählten Port | weder invertierbarer Framewechsel noch Erhaltung des ganzen Eingangszustands |
| Produkt mit Spiegelbild | z × J_Bz und z · J_Bz | quadratische Auslesung von Fluss-/Energiegrößen im Modell | nicht dasselbe Objekt wie der lineare Mittelwert (z+J_Bz)/2 |

„Aktiv“ oder „passiv“ ist bei einer invertierbaren Formel nicht allein an der Matrix abzulesen. Entscheidend ist, ob ein Zustand bei festem Messaufbau verändert oder derselbe Vergleich vollständig umgeschrieben wird. Für die nichtinvertierbare Einzelportprojektion besteht diese Austauschbarkeit nicht auf dem vollen Feldraum.

## 4. Zustand und Messaufbau gemeinsam verfolgen

Die mathematische Portauslesung ist p_C(ρ) = tr(ρC). Für eine orthogonale interne Basisumrechnung Q gilt aus den bereits benutzten Matrixregeln:

ρ′ = QᵀρQ, C′ = QᵀCQ ⇒ tr(ρ′C′) = tr(ρC).

Dies ist eine elementare algebraische Erläuterung, keine neue Hypothese oder empirische Vorhersage. Sie gilt für diesen orthogonalen internen Basiswechsel, nicht als Ersatz für eine beliebige Lorentz-Transformation der Apparatur.

Wenn dagegen nur ρ verändert und C festgehalten wird, wird ein anderer relativer Zustand des Felds zum Analysator verglichen. Unterschiedliche Portzahlen belegen dann allein keinen Widerspruch und keine neue Substanz. Hält man nur ρ fest und ändert C, ändert man die Messfrage.

Der Interferometerabschnitt r03 enthält genau eine solche zusätzliche Referenz: D(φ) = Im(exp(iφ)s). Die Referenzphase φ gehört zum Aufbau. Ihre Variation ist keine Herleitung des kosmischen Frame-Versatzes β_sym. r03 sagt ausdrücklich, dass kein konkretes Feld mit der symmetrischen Rapidität identifiziert ist.

## 5. Die Projektion bewahrt nicht den vollständigen Zustand

Die Quellen geben E′ = B′ = (E+B)/2 an. Am ausgewählten Port bleibt deshalb die Summe; der Partnerport trägt die Differenz. Nur das Paar der beiden unnormierten Komponenten rekonstruiert den Eingang über F = FC₊ + FC₋. Aus einem einzigen normierten Port allein folgt keine Rekonstruktion.

Drei Ebenen sind auseinanderzuhalten:

1. **Algebraische Zerlegung:** beide unnormierten Komponenten gemeinsam, keine automatische physikalische Messdynamik.
2. **Selektierter Port:** eine Komponente, gegebenenfalls normiert; andere Information wurde nicht mitgeführt.
3. **Messkanal mit verworfenem Ergebnis:** r27/r28 verwenden ein eigenes Mess-/Reservoirmodell. Dessen Bedingungen sind zusätzliche Annahmen, kein passiver Framewechsel.

Deshalb ist die Involution J_B² = I nicht mit einem reversiblen Kompensatordurchlauf gleichzusetzen. Aus zweimaligem Spiegeln folgt keine Umkehrbarkeit einer dazwischen vorgenommenen Portselektion.

## 6. Was für OP5 jetzt anders zu fragen ist

Die unmittelbare, konkrete Aufgabe lautet nicht mehr „Welcher Port ist Materie, Licht oder dunkle Energie?“, sondern:

**Welche Zustandsoperation und welche Referenzoperation werden im behaupteten M/T/P-Vergleich gemeinsam ausgeführt, und welche unabhängig definierte Auslesung wird dabei konstant gehalten oder verglichen?**

Das Ausgangsobjekt kann dabei vorerst das vollständige F sein. Die Portauslesung ist nur ein Kandidat; sie wird nicht zum kosmologischen Energieanteil erklärt. Die Lorentz-Invariante s ist ebenfalls bereits definiert, liefert aber allein keinen bestimmten Wert β_sym oder eine Energiedichte.

Der nächste enge Prüfschritt ist die vorhandene Zuordnung zwischen dem feldabhängigen Rapiditätsparameter η_f, der Port-Sichtbarkeit V = |s|/(2u) und dem projektweiten η_sym beziehungsweise β_sym. r03 markiert diese Identifikation ausdrücklich als nicht hergestellt. Bevor neue Rechnungen vorgeschlagen werden, sind r17–r24, r61 und r67/r68 auf spätere Festlegungen oder Hindernisse zu durchsuchen. Neue Kriterien würden einen eigenen vorab committeten Test erfordern.

## 7. Status

Dies ist eine Arbeitsnotiz, keine neue nummerierte Forschungsschicht. Der neue Inhalt ist die explizite operative Ordnung der vorhandenen Definitionen und ihrer Beweislast. Frühere mathematische und numerische Befunde werden nicht als neue Evidenz ausgegeben. H96 bleibt offen, H97 widerlegt; keine Änderung der Guards oder bestehender Theoreme. Keine externe Apparatur- oder Literaturprüfung wurde hier vorgenommen.
