# Erkundung: Wählen Feldalgebra und Register bereits Zustand und Energieanteil aus?

**6. November 2026. Analytische Erkundung, ausdrücklich nicht blind.** Ausgangsstand `674487c`. Autorauftrag: Untersuchung der Zustandsauswahl und Messabbildung bei ausgesetzter historischer Λ-Auslöschung. Keine neue H-Nummer, keine numerische Rechnung und kein empirischer Test. Die folgenden Aussagen sind endliche direkte Algebra; keine neuen experimentellen Kriterien werden eingeführt. Selbstprüfung durch Codex.

## 1. Genaues Ziel

Geprüft wird die begrenzte Behauptung: Die bereits rekonstruierte lokale Feld-/Projektoralgebra mit normiertem Gram-Register bestimme allein einen ausgezeichneten Registerwert q und dessen physikalische Interpretation als Materieanteil.

**Urteil für diese Behauptung: widerlegt durch explizite Vergleichsdaten.** Das betrifft die unten angegebenen Minimalvoraussetzungen, nicht ein zusätzliches, hier noch nicht hergeleitetes natives Auswahlgesetz. Für die vollständige physikalische Brücke bleibt das Urteil unvollständig.

## 2. Vorwissen geprüft

- `sources/research/parts/v410-state-mediator-synthesis.tex`: vollständiges reales Feld, Gram-Auslesung und verlorene Skala/Orientierung.
- `notes/research/v4_9_0_r17_r19/rounds/v490_r17_round.tex`: q als Eigenwertverhältnis und Rapiditätsparametrisierung.
- `notes/research/v4_10_0_r26_r31/rounds/v490_r27_round.tex`: frei deklarierter Rotations-/Messschritt, Kontraktion zum neutralen Register; ein bestimmter endlicher Winkel ist kein hergeleiteter universeller Auswahlmechanismus.
- `analysis/OP5_Readout_Protocol_Energy_Result.md`, besonders Ergebnis und Abschnitte 1–3: Protokoll-/Apparaturabhängigkeit und energetische Bilanz waren bereits bekannt. Die vorliegende Notiz wiederholt das nicht als neue Entdeckung.
- `analysis/OP5_Neutral_Pair_Dynamics.md`: vorgeschriebene neutrale Vergleichsdynamik und offene mikroskopische Herkunft/Energiezuordnung.
- `analysis/OP5_Lambda_Neutral_Reassessment.md`: normierte Anteile erfordern zusätzliche Energiegewichte und Entwicklung.
- `notes/research/v4_10_0_r63_r64/rounds/v490_r63_round.tex`: Auswahl der Zählregeln und Spiegel-Floor nicht durch beliebige Felder begründet.
- `notes/research/op5_denominator_audit_2026_11_06.md`: Fluss-/Register-/Dichteverhältnisse verschieden; r31 setzt q ein.

Der neue Arbeitsbeitrag sind die explizite konstante-Skala-Familie und die eng quantifizierte Energiewichtungsformel, die die bereits benannte Unterbestimmtheit direkt sichtbar machen. Keine Behauptung neuer allgemeiner Physik oder mathematischer Neuheit.

## 3. Minimalvoraussetzungen

Es gelten nur: F = [E|B] reell, G = FᵀF positiv, Normierung tr G = 1, die bereits definierten Projektoren C± und die Registerauslesung. Es werden kein unbekanntes Feldgesetz, keine spezielle Energiegewichtung, keine kosmische Epoche und keine Identifikation mit einem bestimmten Zählmodell hinzugefügt.

Alle Felder unten sind lokale algebraische Zustände im Feld-/Gram-Modell. Sie werden nicht als global realisierte elektromagnetische oder kosmologische Lösungen ausgegeben. Das ist wichtig: Ein zusätzliches physikalisches Auswahlgesetz könnte die Familie einschränken, ist aber gerade nicht Teil dieser Minimalvoraussetzungen.

## 4. Explizite Zustandsfamilie bei gleicher Skala und Orientierung

Für jedes q mit 0 < q < 1 setze

E_q = (1/sqrt(1+q), 0, 0),

B_q = (0, sqrt(q/(1+q)), 0).

Dann ist

G_q = ρ_q = diag(1/(1+q), q/(1+q)),

tr G_q = 1, E_q·B_q = 0 und s_q = (1−q)/(1+q) > 0.

Die beiden Spalten sind unabhängig, die rekonstruierte Orientierung O ist die Einheitsmatrix, und beide Zustände bleiben in derselben positiven reellen Sektorklasse. Das Verhältnis des kleineren zum größeren Eigenwert ist genau q.

Zwei genaue Instanzen:

| q | G = ρ | s | tr G |
|---|---|---|---|
| 1/3 | diag(3/4,1/4) | 1/2 | 1 |
| 1/2 | diag(2/3,1/3) | 1/3 | 1 |

**Folgerung:** Positivität, feste Gesamtskala, feste Orientierung, Sektorzeichen und dieselbe Projektoralgebra wählen keinen einzigen q-Wert aus. Ein beliebiger Zielwert lässt sich in dieser Familie einsetzen, aber das wäre eine Präparation, keine Ableitung.

**Weitere konkrete Trennung:** Im unveränderten σ_x-Analysator haben alle diese Register p₊ = p₋ = 1/2, weil E·B = 0. Verschiedene Eigenwertverhältnisse können also denselben festen Portkontrast liefern. Für eine Eigenwert-Auslesung ist die Wahl des Analysators mitzunennen.

## 5. Ein festes q bestimmt ohne Energiezuordnung keinen Energieanteil

Nun sei ein einzelner q-Wert fest. Das Register hat normierte Eigengewichte λ₊ = 1/(1+q), λ₋ = q/(1+q).

Als rein mathematische, positive Energiezuordnungen zu diesen beiden Gewichten betrachte

e₊ = A w₊ λ₊, e₋ = A w₋ λ₋ mit A > 0 und w± > 0.

Der Anteil des Minusbudgets am Gesamtbudget lautet dann

f₋ = e₋/(e₊+e₋) = w₋ q/(w₊+w₋q).

Bei denselben Registerdaten liefern w₊ = w₋ = 1 den Anteil q/(1+q), während w₊ = 1 und w₋ = 2 den Anteil 2q/(1+2q) liefern. Diese Werte unterscheiden sich für 0 < q < 1. Beide Zuordnungen erfüllen die hier einzigen zusätzlichen Budgetforderungen Positivität und Summenbildung.

Das sind verschiedene zusätzliche Modelle, keine bloßen Einheitenwechsel oder zwei korrekte Auswertungen derselben bereits kalibrierten Apparatur. Es wird insbesondere keine Freiheit behauptet, nachträglich in einem festgelegten Experiment beliebige Energiegewichte zu verändern.

Für die konkrete Forderung f₋ = q muss bei 0 < q < 1 gelten:

w₋/w₊ = 1/(1−q).

Ein solches Gewicht müsste unabhängig begründet sein. Es allein so zu wählen, dass das Zielverhältnis wieder erscheint, wäre keine Erklärung. Hier wird es weder vorgeschlagen noch auf Daten angepasst.

**Grenze des Arguments:** Positives Zweibudget ist noch kein vollständiges kosmologisches Materie-/Λ-Modell. Druck, Erhaltung, Expansion und Normierung zur kritischen Dichte fehlen. Das Gegenbeispiel zeigt nur, dass das Register allein die Energieanteile noch weniger eindeutig bestimmt als eine solche vollständige Theorie es verlangen würde.

## 6. Warum vorhandene Auswahlkandidaten diese beiden Lücken nicht schon schließen

- **Kaskadenstationarität:** r31 ist bei vorgegebenem q stationär lösbar. Sie liefert deshalb kein zusätzliches Auswahlkriterium für q.
- **Bloße Symmetrie/Neutralität:** Neutrales Register I/2 hat q = 1. Es ist nicht der in H96 verwendete innere Wert; Symmetrie allein wählt diesen nicht aus.
- **Reiner Referenzzustand:** hat q = 0. Auch dies ist ein anderer Zustand, keine Herleitung des gewünschten inneren Werts.
- **r27-Messdynamik:** Der konkrete Kanal kontrahiert zum neutralen Register. Ein ausgewählter endlicher Schritt/Winkel oder ein nachgelieferter Reservoirzustand ist eine weitere Präparations-/Dynamikannahme. Die bisherigen Resultate werden nicht als unbekannte Lücke erneut vorgeschlagen.
- **Zählregeln r63:** können nach Festlegung ihrer Regeln eine Zahl liefern; die Auswahl der Regeln aus den Frames und die Energieabbildung bleiben separate Verpflichtungen. Einsetzen dieser Zahl in F_q konstruiert eine passende Registerinstanz, identifiziert aber noch keinen unabhängig realisierten kosmologischen Zustand.

## 7. Belastbarer Fortschritt und nächster Angriffspunkt

Die weitere Untersuchung muss zwei unabhängige Aufgaben bearbeiten:

1. **Auswahl:** Was schränkt die bei gleicher Skala, Orientierung und Sektorklasse verbleibende q-Familie physikalisch ein?
2. **Messabbildung:** Welche aus dem vorhandenen Modell begründeten Energie-/Messgewichte verbinden das ausgewählte Register mit der behaupteten Beobachtungsgröße?

Ein Beweis nur der ersten Aufgabe würde die zweite nicht erledigen. Umgekehrt kann eine Energiegewichtung einen beliebigen q-Wert in viele Anteile übersetzen, ohne seine Auswahl zu erklären.

Der nächste gezielte Quellen-/Ableitungsschritt ist deshalb die r63-Auswahlregel selbst: Erzwingt die Unsicherheitssättigung tatsächlich die spezielle minimale Spinmenge für T und die volle Gewicht-2-Menge für M, oder bleibt mindestens eine dieser Einschränkungen frei? Die r63-Formel zeigt schon, dass Extremzustände m = ±j bei jedem Spin sättigen. Die zusätzliche Einschränkung auf j = 1/2 ist daher gesondert zu untersuchen, nicht still aus Sättigung zu folgern.

I1-Auslöser 3 ist durch das Zählverhältnis weiterhin berührt: String-/LQG-Verbindung bleibt als separat zu begründende Autoridee möglich. Hier wird kein neuer Stringmechanismus oder neues Reservoir aktiviert. I3/I4 bleiben in den geprüften Formen gescheitert. W1/W2 eingefroren, H96 offen, H97 widerlegt; Guards unverändert.
