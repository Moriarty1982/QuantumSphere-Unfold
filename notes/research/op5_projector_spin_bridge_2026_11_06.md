# Erkundung: Können J, Chiralität oder P_C7 die Horizont-Spinmaske liefern?

**6. November 2026. Quellen-/Typenprüfung und begrenzte algebraische Folgerung, nicht blind.** Basis `a486f61`. Selbstprüfung durch Codex, keine neue Rechnung und kein neuer empirischer Test. Die r51- und Lean-Ergebnisse werden als vorhandene Quelle verwendet, nicht neu numerisch oder formal kompiliert.

## 1. Urteil

**Die Identifikation der vorhandenen Projektoren mit einer Horizont-Minimalspinmaske ist unvollständig.** Es fehlt zunächst eine explizite Abbildung zwischen ihren Trägern.

Zusätzlich ist die einfache Behauptung „die korrigierte Tachyon-Abbildung verändert den gegebenen Chiralitätsprojektor und erklärt so verschiedene M/T-Zugriffsmengen“ mit r51 nicht vereinbar: Diese Abbildung kommutiert dort mit dem Chiralitätsoperator und erhält die zugehörigen Sektoren. Das ist ein konkretes Hindernis für genau diesen Kandidaten, kein Unmöglichkeitssatz über alle später konstruierbaren Messabbildungen.

## 2. Quellen und bereits bekannte Korrekturen

- `notes/research/v4_10_0_r34_r47/rounds/v490_r42_round.tex`: C_ch = (I+iL_e7)/2 auf dem gewählten Dixon-Träger; Angaben zu Chiralität und internen Eichsektoren.
- `notes/research/v4_10_0_r48_r55/rounds/v490_r51_round.tex`, r51.1 und Lesart: korrigierte Tachyon-Abbildung R: z ↦ iz erhält die Sektoren; Zeitumkehr und J_B sind davon verschieden.
- `formal/QSFormal/Sektoren.lean`, `R_iL`, `R_iR`, `R_P4`: bereits vorhandene Formalisierung dieser Träger-/Kommutationsaussagen. Hier gelesen, nicht erneut kompiliert.
- `notes/research/v4_10_0_w1/Notiz_mod_HC_und_P_C7.md`: frühere Gleichsetzung P_C7 := C_ch ausdrücklich zurückgenommen; C_ch ist der Kompensator, P_C7 bleibt offen; „mod HC“ nicht als Rechenregel definiert.
- Gleicher Ordner, `Bestandsaufnahme_Wirkungsansaetze.md`: korrigierte Entscheidung 5 und P_C7 vorerst offen.
- `sources/research/parts/native-operator-link.tex`: HC-Projektor C ausdrücklich von P und dem Defekt-Penalty getrennt.
- `sources/research/parts/v470/16_master_model.tex`: abstrakter Schließungsprojektor P_C7 und die Felder des Mastermodells.
- `notes/research/v4_10_0_r63_r64/rounds/v490_r63_round.tex`: eigenständige Horizont-Spinlabels und Zählregeln.

Die bekannten Identifikationsfehler werden hier nicht als Neuentdeckung ausgegeben. Neu ist ihre gezielte Konsequenz für den beauftragten Spinzugriff auf einen gemeinsamen Zustand.

## 3. Typentabelle: Gleich benannt heißt nicht dieselbe Abbildung

| Objekt | Träger / Wirkung laut untersuchten Quellen | Noch nicht gelieferte Verbindung |
|---|---|---|
| J_B = i conjugation | reales elektromagnetisches Doppel-Feld | keine Abbildung auf Horizont-Spinnetzlabels |
| innere Einheit L_e7 / Involution iL_e7 | ausgewählter komplexifizierter Oktonion-/Dixon-Träger | kein Spinbereich j = 1/2,1,… auf diesem Träger identifiziert |
| C_ch = (I+iL_e7)/2 | Chiralitäts-/Kompensatorprojektor im konstruierten Träger | Chiralität ist nicht allein durch die Projektorform eine Horizont-Minimalspinmaske |
| P_C7 | abstrakter zulässiger Schließungssektor des Mastermodells | konkrete Einträge, Trägeridentifikation und Spinmaske offen |
| Π_min aus der Auswahlerkundung | Vergleichsprojektion auf Horizontlabel j = 1/2 | nicht als Bild eines der anderen Projektoren hergeleitet |

Weder die Bezeichnung „Spinor“ noch dieselbe Projektorform (I+J)/2 stellt eine Abbildung zwischen internem Chiralitätsträger und Horizont-Drehimpulsraum bereit. Auch gleiche endliche Ränge wären nur eine Dimensionsbedingung, kein physikalisches Wörterbuch.

## 4. Was die bekannte Tachyon-Abbildung bewahrt

r51 benutzt auf seinem Träger die äußere Multiplikation R mit i. Sie kommutiert mit iL_e7 und damit mit C_ch. r51 beschreibt dies ausdrücklich so, dass M und T dieselben Chiralitäts-/Ladungssektoren tragen. Die sektorvertauschende Operation ist dort die Zeitumkehr, nicht der Tachyon-Framewechsel.

Für einen normierten Zustandsoperator ϱ_D und einen unitären U_D mit [U_D,C_ch] = 0 folgt direkt

tr(U_D ϱ_D U_D† C_ch) = tr(ϱ_D C_ch).

Diese elementare Konsequenz gilt für den bezeichneten Operator und dasselbe Messereignis. Sie sagt nicht, dass jedes aktive Messprotokoll oder jede zusätzlich geänderte Auslesemaske gleiche Werte haben müsste. Sie zeigt aber: Den vorhandenen C_ch unverändert als T-Maske zu verwenden erzeugt durch U_D allein keinen anderen ausgewählten Gewichtsanteil.

## 5. Was auch eine kompatible Brücke erhalten müsste

Als enges Vergleichsschema seien B: H_spin → H_D eine injektive lineare Einbettung und Π ein Projektor auf H_spin. Angenommen,

C_ch B = BΠ und U_D B = B U_spin.

Wenn außerdem C_ch mit U_D kommutiert, folgt durch Einsetzen

BΠU_spin = C_ch U_D B = U_D C_ch B = BU_spinΠ.

Die Injektivität gibt ΠU_spin = U_spinΠ. Unter diesen präzisen Voraussetzungen würde auch die übertragene Spinmaske durch den kompatiblen Transport erhalten, nicht gegen eine andere Maske ausgetauscht.

Das ist ein bedingter algebraischer Kontrollsatz, kein Nachweis, dass B oder ein entsprechender Horizonttransport im Paper existiert. Er grenzt ein, was eine künftig behauptete Brücke leisten könnte: Eine zusätzliche maskenändernde Messregel, eine nicht äquivariante Zuordnung oder ein anderer Träger müsste ausdrücklich benannt werden. Nichts davon wird hier gewählt.

## 6. Chiralität allein unterscheidet keine Spinlabel

Eine zweite einfache Gegenkontrolle ist der deklarierte Vergleichsträger H_spin ⊗ H_internal mit C = I ⊗ C_ch. Für jedes v im Bild von C_ch werden sowohl |1/2,+1/2⟩ ⊗ v als auch |1,+1⟩ ⊗ v ausgewählt. Der interne Projektor wählt deshalb nicht den ersten Spin gegenüber dem zweiten aus.

Diese Faktorzerlegung ist nur ein Vergleich zur unabhängigen Bedeutung der Labels, keine Behauptung einer nativen Faktorisierung. Eine tatsächliche Spin–Chiralitätskorrelation könnte dieses Resultat ändern, müsste aber eigens begründet sein. Eine solche Korrelation würde genau die bisher fehlende Auswahlstruktur ergänzen.

## 7. Warum P_C7 und „mod HC“ die offene Stelle noch nicht füllen

Der Companion verlangt unter anderem P_C7² = P_C7, (I−P_C7)Ψ = 0 und eine Erhaltung unter M16. Diese Bedingungen spezifizieren für sich weder den Minimalspinbereich noch eine Zähl-/Messabbildung.

Die alte Zwischenentscheidung, P_C7 mit C_ch gleichzusetzen, wurde im Projekt bereits korrigiert. Sie als Lösung des jetzigen Spinproblems wiederzuverwenden würde den dokumentierten Fehler wieder einführen.

I2 des Autors, „mod HC“ über Primzahlplätze und den chinesischen Restsatz zu lesen, ist durch diese Prüfung einschlägig. Der Ansatz braucht aber erst konkrete gemeinsame ganzzahlige/rationale Daten und eine Definition, welche Plätze welchen Spin-/Trägersektoren entsprechen. Die untersuchten Quellen liefern diese Zuordnung nicht. Eine Primzahlcodierung allein wäre keine Herleitung der physikalischen Auswahl.

## 8. Arbeitsstand und nächster sinnvoller Schritt

Der zuerst naheliegende vorhandene Projektorkandidat liefert also kein bereits begründetes Auswahlgesetz. Die konkrete Verbindung zu j bleibt offen; außerdem bewahrt die korrigierte Tachyon-Abbildung die bekannten internen Projektorsektoren.

Jetzt lässt sich die konstruktive Alternative eng formulieren: Eine **eingeschränkte Auslesung auf einem gemeinsamen Spinträger** müsste als neue Abbildung samt Gewicht explizit angegeben werden, während der vollständige Zustand erhalten bleibt. Bevor hierfür ein Mechanismus erfunden wird, ist zu prüfen, welche kosmologischen Aussagen selbst bei einer beliebigen solchen Zugriffsbeschränkung überhaupt invariant und messbar wären. Insbesondere kann ein nur zugriffsabhängiges Zählverhältnis nicht ohne zusätzliche Feld-/Gravitationskopplung den beobachterunabhängig behandelten Energiehaushalt festlegen.

Damit ist kein Wiederaufbau von W1/W2 autorisiert oder erfolgt. I1 bleibt durch die Herkunft des Zählverhältnisses berührt; I2 ist als mögliche Autoridee mit fehlenden Eingabedaten vermerkt. I3/I4 in den geprüften Formen gescheitert. H96 offen, H97 widerlegt; Guards unverändert. Keine nummerierte Forschungsschicht und keine Änderungen an bestehenden Beweisen.
