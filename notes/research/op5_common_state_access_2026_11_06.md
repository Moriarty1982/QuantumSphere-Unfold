# Erkundung: Ein Zustand, verschiedene Zugriffe auf Spinsektoren?

**6. November 2026. Begrenzte analytische Erkundung, nicht blind.** Basis `21ff987`. Selbstprüfung durch Codex, keine neue empirische Hypothese oder numerische Rechnung. Die Vergleichskonstruktion unten expliziert mögliche Zugriffsarten; sie ist keine aus dem Paper gewonnene native Horizontdynamik.

## 1. Ergebnis

**Die These „derselbe vollständige Zustand, nur invertierbar anders beschrieben“ kann für sich keine Spinbeiträge löschen.** Unterschiedliche zugängliche Mengen sind damit vereinbar, wenn ausdrücklich eine eingeschränkte Auslesung eingeführt wird. Dann bleibt der nicht gelesene Rest Teil des gemeinsamen Zustands und seiner Bilanz.

Eine tatsächliche Beschränkung des Zustands auf die minimale Spinmenge ist dagegen eine Selektion oder Präparationsbedingung. Sie kann sinnvoll definiert werden, folgt aber nicht aus einem passiven Framewechsel und benötigt im Allgemeinen ein Erfolgsgewicht und einen Umgang mit dem Rest.

Für die konkrete M/T-Zähl-Lesart ist das Urteil weiterhin **unvollständig**: Die Quellen geben die zwei Zählregeln an, aber nicht die sie verbindende physikalische Zugriffs- oder Zustandsabbildung.

## 2. Quellen und Vorwissen

- `notes/research/v4_10_0_r63_r64/rounds/v490_r63_round.tex`: verschiedene Spinmengen und offene Herleitung aus den Frames.
- Gleicher Ordner, `v490_r64_round.tex`: gleicher Horizont, gemeinsame Fläche A und Plancklänge; beide Zählungen fixieren jeweils γ über dieselbe Entropie-Flächen-Bedingung. Die Lesart ist ausdrücklich kein Theorem.
- Gleicher Ordner, `v490_r66_round.tex`: weitere Status-/Provenienzpräzisierungen zur Zähl-Lesart.
- Gleicher Ordner, `llm/Nachrechnung_r63_r67.md`: Unsicherheitssättigung als nachträgliche Lesart, nicht als ursprüngliche Herleitung der zitierten Zählung. Externe Quellen hier nicht erneut geprüft.
- `sources/research/parts/v410-state-mediator-synthesis.tex`: gemeinsamer Träger verlangt explizite Vergleichsabbildungen; verschiedene reduzierte Register sind nicht automatisch derselbe Zustand.
- `analysis/OP5_Readout_Protocol_Energy_Result.md`: passiver Vergleich, aktive Messkopplung, Selektion und Apparaturbilanz bereits getrennt.
- Die vorangegangenen Zustands-/Spin-Auswahlerkundungen: Sättigung allein fixiert nicht die Spinmenge und das Register allein nicht die Energieabbildung.

## 3. Eine minimale Vergleichskonstruktion

Betrachte zunächst nur die beiden nichttrivialen Spinlabels j = 1/2 und j = 1 mit jeweils den zwei in r63 betrachteten Extrembasiszuständen. Der Vergleichsraum hat vier orthogonale Zustände:

|1/2,+1/2⟩, |1/2,−1/2⟩, |1,+1⟩, |1,−1⟩.

Π_min projiziert auf die ersten beiden. Für einen normierten positiven Zustandsoperator ϱ sei w = tr(ϱΠ_min).

Diese Konstruktion verwendet nur die fragliche Unterscheidung minimaler und zusätzlicher Sektoren. Sie bildet weder die vollständige Horizontzählung noch deren Flächenconstraints oder Vielteilchenzustände ab. Sie eignet sich als Gegenkontrolle der Behauptung, eine inverse Beschreibung allein könne die Zahl der zugänglichen unabhängigen Beiträge reduzieren.

## 4. Drei verschiedene Bedeutungen von „T zählt nur minimal“

### A. Vollständiger invertierbarer Darstellungswechsel

Bei einer gemeinsamen unitären Umrechnung U werden Zustand und Projektion zusammen transformiert: ϱ′ = UϱU†, Π′ = UΠ_minU†. Dann bleibt tr(ϱ′Π′) = w. Der Rang des ausgewählten Unterraums bleibt 2; der volle Raum hat weiterhin Rang 4.

Ein solcher Wechsel kann Sektoren anders darstellen, aber keine universelle inverse Abbildung des gesamten vierdimensionalen Vergleichsraums auf den zweidimensionalen Minimalraum sein. Das folgt bereits aus der Dimension. Es schließt nicht aus, einen einzelnen speziell präparierten Zustand in einen anderen Unterraum zu drehen; ausgeschlossen ist die behauptete vollständige verlustfreie Reduktion aller Eingaben.

Dieses endliche Vergleichsargument ist keine Behauptung, alle möglichen physikalischen Frameabbildungen müssten unitär sein. Auch eine andere bijektive lineare Koordinatenumrechnung löscht keine Dimension. Eine nichtinvertierbare physikalische Abbildung wäre gesondert als solche zu erklären.

### B. Eingeschränkter Zugriff auf denselben Zustand

Der T-Readout kann nur Observablen im Minimalblock verwenden, während M weitere Blöcke ausliest. Dann bleibt der volle Zustand derselbe, aber beide Readouts tragen nicht dieselbe Information.

Die unnormierte sichtbare Komponente ist Π_minϱΠ_min und hat Gewicht w. Eine auf dieses Teilereignis bedingte Normierung dividiert durch w. Dabei darf die Zahl w nicht stillschweigend durch 1 ersetzt werden. Insbesondere ist w nicht allein durch die Anzahl der zwei minimalen Basiszustände gegeben; es hängt vom Zustand ab.

Sind nur Daten des ausgewählten Blocks bekannt, kann der nicht gelesene Rest trotzdem physikalisch vorhanden sein. „Nicht zugänglich“ ist keine Herleitung von „nicht gravitierend“ oder „Energie null“.

### C. Physikalische Selektion oder Präparation

Für w > 0 ist der selektierte Zustand ϱ_sel = Π_minϱΠ_min/w. Er liegt vollständig im Minimalraum. Dies ist keine bloß andere Beschreibung eines beliebigen vollständigen Eingangs, sondern eine konditionierte Teilmenge beziehungsweise ein neuer präparierter Zustand.

Bei w = 0 ist diese Selektion nicht normierbar. Eine nichtselektive Zweiblockmessung behält dagegen beide Diagonalblöcke; der zusätzliche Spinsektor verschwindet dabei nicht. Diese Unterscheidung verhindert, dass verworfene Messergebnisse als universelles Ausschlussgesetz der Theorie ausgegeben werden.

## 5. Warum Zustandszugriff und Energie zwei Aufgaben bleiben

Für einen ausdrücklich blockdiagonalen positiven Vergleichs-Energieoperator H gilt

tr(ϱH) = tr(Π_minϱΠ_min H) + tr((I−Π_min)ϱ(I−Π_min)H).

Der erste Term allein ist die unnormierte Energie des gewählten Blocks. Die bedingte mittlere Energie des selektierten Zustands dividiert ihn durch w. Der Restterm entfällt nicht durch die Readout-Beschränkung. Bei einem nicht blockdiagonalen H wäre zusätzlich zu prüfen, ob Kohärenz-/Kopplungsterme relevant sind; die obige einfache Aufteilung wird dann nicht behauptet.

Damit wäre sogar bei begründeter Zugriffsmaske noch ein Energie-/Gravitationsgesetz erforderlich. Die hier verwendeten positiven Vergleichsenergien sind kein neuer Vorschlag für den Tachyon-Sektor und keine Rechnung eines kosmologischen Stress-Energie-Tensors.

## 6. Was die vorhandene Zähl-Lesart davon tatsächlich liefert

r64 hält Fläche und Plancklänge fest und bestimmt unter jeder Zählregel ihren γ-Wert. Das ist eine Gegenüberstellung von Zähl-/Kalibrierungsregeln am gemeinsam bezeichneten Horizont. Sie spezifiziert nicht automatisch einen Zustandsoperator ϱ, eine Projektion Π_min, ein Gewicht w oder einen Übergangskanal zwischen beiden Auslesungen.

Die Kalibrierungswerte γ_M und γ_T sind deshalb weder unmittelbar w und 1−w noch die Dimensionen der zugänglichen Unterräume. Auch eine angenommene gemeinsame Population würde erst eine gemeinsame Maß-/Flächenzuordnung und die Readout-Regeln benötigen. Dieselbe makroskopische Fläche allein legt keine mikroskopische Zustandsabbildung fest.

Die Lesart „ein Objekt, verschiedene Zugriffe“ ist somit logisch möglich, aber zusätzliche präzise Struktur. Die Lesart „verschiedene präparierte Zustände“ ist ebenfalls möglich, verfolgt aber ein anderes physikalisches Ziel. Keine der beiden wird durch die numerische Übereinstimmung des γ-Verhältnisses entschieden.

## 7. Fortschritt und nächste engste Aufgabe

Die Suche nach einem Auswahlgesetz ist auf eine konkrete fehlende Abbildung eingegrenzt:

**Was bestimmt die T-Zugriffsmaske auf einem gemeinsamen Träger und ihr Gewicht w — oder, falls eine echte Präparation gemeint ist, was erzeugt diesen Zustand und bilanziert den Rest?**

Der nächste bereits im Paper benannte Kandidat ist die innere Einheit J beziehungsweise der C7-/Chiralitätsprojektor: Es wäre gezielt zu prüfen, ob irgendeine dort wirklich definierte Abbildung auf den Horizont-Spinlabels wirkt und Π_min festlegt. Ein Projektor auf Farbe/Chiralität genügt dafür ohne einen Intertwiner zu den Spin-/Zähldaten nicht. Diese Prüfung soll zuerst Quellen und Typen vergleichen, keine neue Gleichsetzung postulieren.

I2 wird durch den möglichen Projektorbezug als zurückgestellte Idee berührt: der Autorvorschlag „mod HC“/chinesischer Restsatz bleibt ein möglicher separat zu untersuchender Ansatz, falls konkrete gemeinsame ganzzahlige Daten vorliegen; diese Voraussetzungen sind hier nicht geliefert. I1 bleibt durch das γ-Verhältnis berührt. Keine dieser Ideen wird still als Lösung eingesetzt. Keine neue Wirkung oder Reaktivierung von I3/I4. H96 offen, H97 widerlegt, W1/W2 eingefroren; Guards unverändert.
