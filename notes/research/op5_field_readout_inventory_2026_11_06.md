# OP5-Neuaufbau: vollständiges Feld und konkrete Port-Auslesung

**6. November 2026. Quellenordnung und algebraische Rekonstruktion vorhandener Formeln, kein neuer Test.** Ausgangscommit `8c70c70`. Selbstprüfung durch Codex; keine neue numerische oder experimentelle Evidenz. Fortsetzung des Route-Datenblatts, keine Instanziierung einer zuvor fehlenden nativen OP-Route durch bloße Umbenennung.

## 1. Ergebnis und genaue Reichweite

Das Feld-/Gram-Wörterbuch liefert einen expliziten lokalen Träger und berechenbare Auslesungen. **Eine vollständige physikalische OP5-Brücke bleibt unvollständig.** Der kleinste konkrete Kandidat für eine Auslesung ist die relative Aufteilung auf zwei deklarierte Projektorports. Ihre Formel ist im gewählten Feldmodell bestimmt; eine reale Apparatur und ihre Kalibrierung werden dadurch nicht bewiesen.

Die fehlende Information des normierten Registers und seine Nicht-Autonomie unter allgemeinen Beobachterwechseln sind bereits dokumentierte Ergebnisse der Konsolidierung, keine neuen Entdeckungen dieser Notiz.

## 2. Quellen und Vorwissen

- `sources/research/parts/v410-state-mediator-synthesis.tex`, `subsec:v410-readout-types`, `subsec:v410-oriented-mediator`, `subsec:v410-clock-scope`: explizite Rekonstruktion, Orientierungsgegenbeispiele, Typen und Clock-Grenzen.
- `notes/research/v4_9_0_r01_r16/rounds/v490_r04_round.tex`, r04.1–r04.3: reelles Doppel-Feld, Operationen, Gram-Matrix und Port-Auslesung.
- Gleicher Ordner, `v490_r03_round.tex`, r03.1/r03.2: reell-lineare Projektion und Lichtwelle; das Kompensatorbild einer Lichtwelle ist nicht wieder eine Lichtwelle.
- `notes/research/v4_10_0_r26_r31/rounds/v490_r27_round.tex`: Rotation plus Messung als separates Modell; keine automatische native Route oder kosmologische Interpretation.
- `notes/research/op5_neuaufbau_2026_11_06.md` und `op5_route_inventory_2026_11_06.md`: ausgesetzte Auslöschungsgrundlage und offene Realisierung.

Einordnung: T2/T3, T14 und T15; eine lokale Ausleseidentität trägt noch keine kosmologische Aussage T9. Die Auslöserliste I1–I4 ist geprüft: Es wird weder ein Zwei-Kegel-Modell noch eine Skala, ein neuer C7-Projektor oder ein Kondensat benötigt. Keine der zurückgestellten Ideen wird reaktiviert.

## 3. Das explizite Zustandsdatum

Im realen Feldmodell der Quelle ist F = [E|B] eine reelle 3×2-Matrix. Beide Spalten stehen in der gemeinsamen Normierung der Quelle; ihre Formeln dürfen nicht ohne Einheiten- und Kalibrierungsübersetzung direkt auf ungleich dimensionierte SI-Komponenten angewendet werden.

Setze a = E·E, b = B·B, c = E·B und

G = FᵀF = [[a,c],[c,b]], N = tr G = a+b = 2u, ρ = G/N für N > 0.

| Datum | Was erhalten ist | Was fehlt |
|---|---|---|
| F | alle sechs lokalen reellen Feldkomponenten im gewählten räumlichen Bezug | noch keine Ableitungen, Feldentwicklung oder statistischer Quantenzustand |
| G | Spaltenlängen, Skalarprodukt, Skala N und Betrag des Kreuzprodukts | räumliche Orientierung und Richtung des Flusses |
| ρ | normierte interne Form, zwei unabhängige reelle Registerkoordinaten | zusätzlich die Skala N |
| (ρ,N,O) auf der Rang-2-Karte | Rekonstruktion des vollständigen F | Kartenwechsel bei Rangverlust, Dynamik und physikalische Identifikation bleiben separat |

Auf a > 0 und Δ = sqrt(ab−c²) > 0 gibt die Quelle F₀(G) = [[sqrt(a),c/sqrt(a)],[0,Δ/sqrt(a)],[0,0]] und O = [e|q|e×q] an; damit F = O F₀(G). Das ist eine Koordinatendarstellung desselben lokalen Felds, kein zusätzliches fundamentales Feld. Bei Rang 1 braucht man andere Richtungsdaten; beim Nullfeld ist ρ undefiniert.

Der positive AB-Gramzustand zweier Diracspinoren ist trotz ähnlicher Matrixnotation eine andere Auslesung. Die Quelle gibt Gegenbeispiele gegen die Gleichsetzung ihrer physikalischen Inhalte an.

## 4. Bereits definierte, berechenbare Auslesung

Die Quelle deklariert C₊ = (I+σₓ)/2 und C₋ = (I−σₓ)/2. Die beiden quadratischen Portgrößen lauten in ihrer Normierung:

P₊ = ||FC₊||²_F = tr(GC₊) = u+c,

P₋ = ||FC₋||²_F = tr(GC₋) = u−c.

Für N > 0 sind die normierten Anteile daher

p₊ = tr(ρC₊) = 1/2 + c/N, p₋ = tr(ρC₋) = 1/2 − c/N.

Dies ist nur das Ausmultiplizieren der vorhandenen r04.3-Formel und ihres Partnerports. Die Quelle nennt die quadratischen Größen Portenergien; hier wird zunächst ihre mathematische Modellbedeutung festgehalten. Eine Zuordnung zu gemessener Energie oder Leistung benötigt die deklarierte Apparatur samt gemeinsamer Feldnormierung, räumlich/zeitlichem Messfenster und Kalibrierung. Es wird kein experimenteller Nachweis behauptet.

**Was ρ tatsächlich leistet:** Es bestimmt diese normierten Portanteile im festen Messaufbau. Für die absoluten Portgrößen braucht man zusätzlich N. Für allgemeine gerichtete Beobachterwechsel braucht man darüber hinaus die fehlende räumliche Information. Diese drei Anforderungen sind nicht dieselbe Aufgabe.

Die in r04.3 schon definierte Phasen-Auslesung D(φ) = Im(e^{iφ}s) vergleicht Komponenten der internen Form bei festgelegter Referenzphase. Eine solche kontrollierte Modell-Auslesung ist konkreter als die unbestimmte Klasseninvariante I des abstrakten OP-Satzes, aber ohne zusätzliche Brücke nicht mit ihr identifiziert.

## 5. Drei verschiedene „Nullen“

| Aussage | Bedeutung im Feld-/Portmodell | Was daraus nicht folgt |
|---|---|---|
| elektromagnetisch null: s = 0 bei F ≠ 0 | a = b und c = 0, daher ρ = I/2 und p₊ = p₋ = 1/2 | weder Feld noch Portinhalt verschwinden |
| Partnerport leer: FC₋ = 0 | E = B im gewählten Doppelmodell; für F ≠ 0 ist ρ = C₊ und p₊ = 1 | kein nichtverschwindendes nulles elektromagnetisches Feld |
| vollständiges Feld null: F = 0 | G = 0 und beide absoluten Portgrößen null | kein normierter Zustand ρ; N = 0 verbietet die Normierung |

Diese Unterscheidung folgt unmittelbar aus den bereits vorhandenen Formeln und den ausdrücklichen Warnungen der Konsolidierung. Ein verschwundener Port oder eine Null der ausgewählten Invariante darf deshalb nicht ohne Begründung als Photon, vollständige Leere oder kosmologisches Λ = 0 bezeichnet werden.

## 6. Operationen und Beobachter nicht verwechseln

Für die deklarierten rechten Doppeloperationen F′ = FM folgt G′ = MᵀGM. Deshalb kann ihre Wirkung auf G konkret angegeben werden. Die invertierbaren Rotationen/Spiegelungen und die rangsenkende Kompensatorprojektion müssen getrennt behandelt werden; die Projektion liefert keinen allgemeinen inversen Rückweg.

Ein räumlicher Beobachterboost ist laut Quelle keine beliebige rechte 2×2-Doppeloperation. Gleiche ρ können bei demselben gerichteten Boost verschiedene ρ′ ergeben. Orientierung und Skala beizufügen rekonstruiert das lokale Feld; es beweist noch keine native Einbettung der Operationen in die abstrakte OP-Route und keinen gemeinsamen dynamischen Träger.

## 7. Was für den Neuaufbau gewonnen ist

Der erste explizite Gegenstand ist jetzt benannt: **eine lokale relative Port-Auslesung eines deklarierten reellen Feld-Doppels in einem festen Messaufbau**. Ihre zulässigen Eingangsdaten und die benötigten Zusatzdaten lassen sich angeben. Das ist eine konkrete Kandidaten-Auslesung, noch keine neue Vorhersage und keine Aussage über kosmologische Dichten.

Die nächste Quellenprüfung muss die Referenzoperation und den Portaufbau festlegen: Ist die im Paper verwendete Spiegel-/Kompensatoroperation eine passive Umrechnung desselben Zustands, eine aktive Feldänderung oder eine Messselektion? Bereits r03/r04 unterscheiden Spiegelung, Dualitätsrotation und Projektion. Bevor Portanteile als frameabhängige Messwerte desselben Objekts gelesen werden, muss genau diese operative Bedeutung geklärt werden.

Neue Rechnungen oder Tests wurden nicht durchgeführt; keine H-/k-Nummer vergeben. W1/W2 bleibt eingefroren, H96 offen, H97 widerlegt, Guards unverändert. Die historische Λ-Auslöschungsaufgabe wird nicht wieder eingesetzt.
