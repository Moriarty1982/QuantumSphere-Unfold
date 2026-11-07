# Erste OP5-Route: Rekonstruktion und fehlende Instanz

**6. November 2026. Status: Quellenrekonstruktion und begrenzte Selbstprüfung, keine neue Hypothese, keine Rechnung.** Basis: `325c165` auf `codex/op5-question-rebuild`. Gegenstand ist das Quelle–Rückweg-Paket in den Teilen 21/22 einschließlich seiner nächstliegenden QAM- und Atlas-Verweise. Kein vollständiger Audit aller Realisierungen im Companion.

## 1. Ergebnis

**Urteil über die gesuchte konkrete Instanz: unvollständig.** Der bedingte Erhaltungssatz lässt sich vollständig als Schema rekonstruieren. In der untersuchten Abhängigkeitskette wird aber keine konkrete native Route mit auswertbaren A₂, A₃, A₄, Klassentest und physikalisch definierter Auslesung geliefert. Daraus folgt nicht, dass nirgends im Werk eine solche Konstruktion existieren könnte; hier ist die engste gefundene Lücke festgehalten.

Der bedingte Satz wird damit nicht als falsch eingestuft. Für seinen abstrakten Schluss genügen die angegebenen Annahmen. Seine Anwendung auf einen physikalischen Träger ist eine zusätzliche, noch nicht durch das bloße Schema erfüllte Verpflichtung.

## 2. Das rekonstruierte Datenblatt

| Bestandteil | Tatsächliche Angabe im Text | Status für eine konkrete Anwendung |
|---|---|---|
| Träger | zulässiger Sektor A_cl innerhalb C | abstrakt bezeichnet; Elemente und Zulassungstest hier nicht auswertbar instanziiert |
| Ausgangszustand | c_Γ in A_cl | beliebiger zulässiger Träger, kein bestimmter Zustand |
| Route | T_Γ = A₄ ∘ A₃ ∘ A₂ | Komposition angegeben; die drei Operationen hier nicht konkret definiert |
| Gegenrichtung | T_Γ̄: A_cl → C | als Transport bezeichnet; keine konkrete Umkehrvorschrift und keine Forderung T_Γ̄ = T_Γ⁻¹ |
| Auslesung | ρ_θ: C → W | Abbildungsfamilie angegeben, kein bestimmtes Messverfahren |
| Klasse | K_ncl: A_cl → A_cl / ∼_ncl | qualitative Beschreibung durch HC-Transport, Frame-Versatz und Verfeinerung; kein konkreter Klassentest im Paket |
| Invariante | I: W → Λ mit I(ρ_θ(c)) = J_cls(K_ncl(c)) | Faktorisierung ausdrücklich angenommen; Zielraum und Wert nicht konkret physikalisch identifiziert |
| Mittelung | OP5_sym = (OP5_fwd + OP5_bwd)/2 | Mittelung und Linearität auf dem Rücksektor vorausgesetzt |
| Physikalische Größe | keine im Satz festgelegt | insbesondere weder Λ noch Ω_M noch Energie-/Drucktensor |

Quelle: `sources/research/parts/v470/21_inflow_and_transport_statement.tex`, Abschnitt `sec:compressed-op-branch-shell`; `22_op_transport_arguments.tex`, erster Unterabschnitt und `thm:op15-closure`.

**Notation:** Das Λ im Typ I: W → Λ bezeichnet hier einen Zielraum; es ist keine Identifikation mit der kosmologischen Konstante. Die im Original als J bezeichnete Klassenabbildung heißt hier J_cls, um sie nicht mit der Involution des algebraischen Kerns gleichzusetzen. Eine solche Gleichsetzung wird nicht hergestellt.

## 3. Was genau als „Rückweg“ verglichen wird

Das Original definiert:

- OP1 = ρ_in(c_Γ),
- OP5_fwd = ρ_fwd(T_Γ c_Γ),
- OP5_bwd = ρ_bwd(T_Γ̄ c_Γ).

Beide gerichteten Transporte starten in diesen Formeln bei c_Γ. Der Satz berechnet **nicht** den zusammengesetzten Durchlauf T_Γ̄(T_Γ c_Γ). Die Bezeichnung Quelle–Rückweg darf deshalb ohne zusätzliche Realisierungsdaten weder als inverse Dynamik noch als physische Rückkehr des vollständigen Zustands gelesen werden.

Die genaue Aussage betrifft den Mittelwert zweier gerichteter Auslesungen und die ausgewählte Invariante. Das ist ein nachvollziehbares mathematisches Schema, aber ein engeres Resultat als eine konkret realisierte Hin-und-zurück-Dynamik.

## 4. Welche Annahmen die Gleichheit tragen

1. Beide Transporte bleiben in A_cl.
2. Beide erhalten K_ncl(c).
3. I nach der Auslesung hängt nur von K_ncl(c) ab und nicht vom Frameparameter.
4. I ist auf dem zugelassenen Rücksektor linear.

Damit haben beide gerichteten Auslesungen denselben I-Wert wie die Quelle; Linearität überträgt dies auf ihren Mittelwert. **Der Beweis propagiert die vorausgesetzte Erhaltung, er leitet sie nicht aus konkreten Transportgleichungen her.** Das ist keine automatische Zirkularität: Als bedingter Satz ist diese Form sinnvoll. Für einen Realisierungsnachweis muss jedoch gerade die Erhaltung vorab am Modell gezeigt werden.

Außerdem beweist der Satz keine Trennschärfe der Invariante. Dass Quelle und Rückseite denselben I-Wert haben, identifiziert ohne weitere Voraussetzung weder ihre vollständigen Zustände noch alle physikalischen Messwerte. Nicht-Trivialität und physikalische Bedeutung der konkret gewählten Invariante gehören deshalb ins Datenblatt einer Anwendung.

## 5. Die nächsten Verweise schließen die Lücke nicht automatisch

| Verweis | Was er hinzufügt | Was weiterhin fehlt |
|---|---|---|
| QAM, `def:qam-kernel-bridge-datum`, `thm:qam-kernel-bridge` | explizite Bedingungen für Realisierung, Klassenreflexion und Faktorisierung | Existenz dieser Brückendaten ist ausdrücklich nicht bewiesen |
| QAM, `thm:qam-direct-kernel-constructor` | Payload von ⟨0,a⟩ als Kandidat für den Kernel | Klassenerhaltung/Normalform und Readout-Faktorisierung werden weiterhin vorausgesetzt; Tag entfernen allein erfüllt sie nicht |
| Atlas, „What would be needed to close OP5“ | konkretere Faktorisierungsform T_Γ^∨ ∘ J_HC^cone ∘ T_Γ und acht Nachweispflichten | im gelesenen Block ausdrücklich offene Abdeckung, Obstruktionsfreiheit und Identifikation mit OP5 |
| r27, konkreter Doppelzustand mit Rotation und Messung | tatsächlich angegebene lokale Operatoren U_α, C_HC und Messkanal | keine dort nachgewiesene Instanziierung des obigen K_ncl-Pakets; die Messung ändert laut r27.1(d) die betreffende Größe s und liegt außerhalb der dortigen Transportgruppe |

Quellen: `sources/research/parts/v470/07_qam_infrastructure.tex`, etwa Zeilen 1409–1515; `32_atlas_and_op_promotion.tex`, Abschnitt „What would be needed to close OP5“; `notes/research/v4_10_0_r26_r31/rounds/v490_r27_round.tex`, r27.1/r27.2. Spätere Atlas-Abschlussbehauptungen wurden in diesem begrenzten Arbeitsgang nicht vollständig auditiert; die hier zitierte Kandidatenpassage wird nicht als letzter Gesamtstatus ausgegeben.

## 6. Reichweite für die neu aufgebaute Frage

Der erste Schritt liefert noch keine physikalische Messgröße. Er lokalisiert aber die nächste überprüfbare Aufgabe: eine bereits explizite Auslesung samt den tatsächlich verfügbaren Zustandsdaten auswählen und prüfen, welche Information sie erhält oder verwirft. Erst danach kann sie mit einem Transport und einer unabhängigen Messgröße verbunden werden.

Der engste vorhandene Kandidat ist der reale elektromagnetische Doppelzustand F = [E|B] mit Gram-Auslesung G = FᵀF und normiertem Register ρ = G/tr G. Der bereits vorhandene Abschnitt `v410-state-mediator-synthesis.tex` zeigt, dass ρ Orientierung und Skala nicht enthält und unter allgemeinen Beobachterwechseln nicht autonom fortgeschrieben werden kann. Dieser bekannte Befund darf nicht als neue Entdeckung wiederholt werden. Er gibt für den nächsten Schritt eine konkrete Arbeitsrichtung: vollständiges lokales Auslesedatum einschließlich Orientierung und Skala aus dem bestehenden Text rekonstruieren, bevor eine kosmologische Bedeutung zugeschrieben wird.

Das wäre eine Prüfung des vorhandenen Datenwörterbuchs, kein Ersatzmodell für die fehlende native OP-Route. Weder ein neuer Vakuumterm noch ein neuer Abschlussstatus folgt daraus. Die Guards, H96/H97 und das eingefrorene W1/W2-Programm bleiben unverändert. Die Auslöserliste I1–I4 wurde gegen diesen Befund geprüft; es wird kein neuer Zwei-Kegel-, Skalen- oder Kondensatansatz aktiviert.

## 7. Nachvollziehbarkeit

Suchen: feste Zeichenfolgen T_{Γ}, A₂ und ∼_ncl über `sources/research/parts/` sowie Kernel-/Atlas-Verweise. Die Ergebnisse für A₂ betreffen die Kompositionsformel in Teil 21 und den Zwischenzustand in Teil 22; dies ist ein Befund über diese Schreibweise und Suchbasis, kein Beweis der Nichtexistenz aller semantisch äquivalenten Konstruktionen.

Selbstprüfung durch Codex am oben bezeichneten Stand; keine neue externe Quellenprüfung, keine neue numerische Evidenz. Keine Änderung bestehender Theoreme oder nummerierter Runden.
