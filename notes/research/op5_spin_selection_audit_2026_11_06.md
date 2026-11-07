# Erkundung: Was wählt die Unsicherheitssättigung tatsächlich aus?

**6. November 2026. Analytische Selbstprüfung, nicht blind; keine neue empirische Hypothese.** Basis `e5d9b55`. Ziel ist der konkrete Schluss in der Lesart von r63, ein gemeinsames Sättigungsprinzip liefere sowohl die minimale T-Zählung als auch die volle Gewicht-2-Zählung für M. Keine neue H-/k-Nummer und keine numerische Rechnung. Bestehende Resultate werden als solche verwendet.

## 1. Urteil

**Der Schluss „Unsicherheitssättigung allein erzwingt j = 1/2 für T“ ist durch ein einfaches Gegenbeispiel widerlegt.** Die Sättigungsformel aus r63 selbst ist davon nicht widerlegt; sie gilt in ihrem angegebenen Bereich und zeigt gerade die zusätzliche Freiheit.

Die stärkere physikalische Lesart „T nimmt das absolute Minimum, M das Minimum bei jedem Spin“ ist **bedingt auf zwei zusätzliche Auswahlregeln**. Die Quellen liefern hier keine Dynamik, die diese verschiedenen Regeln den beiden Frames zwingend zuordnet. r63 hält am Ende selbst genau diese Herkunft als offene OP1-Aufgabe fest.

## 2. Vorwissen und Quellen

- `notes/research/v4_10_0_r63_r64/rounds/v490_r63_round.tex`, r63.1–r63.4 und Lesart: Zählgleichung, Sättigung, Energie-Floor und offene Auswahlfrage.
- Gleicher Ordner, `v490_r68_round.tex`, r68.1: dokumentierte Nachprüfung der Sättigung und Zählwerte. Externe LQG-Quellen wurden hier nicht erneut geprüft.
- `formal/QSFormal/Zaehlung.lean`, `perp_sub_abs`, `robertson_eq_iff`, `saturating_iff`, `spin_half_sd`: vorhandene formalisierte Arithmetik. Die Datei wurde gelesen, nicht in diesem Arbeitsgang neu kompiliert; sie formalisiert laut eigenem Kopf nicht die vollständigen Drehimpulsoperatoren oder einen physikalischen Auswahlmechanismus.
- `notes/research/op5_state_selection_exploration_2026_11_06.md`: q-Familie und getrennte Energiegewichte.
- `notes/research/predictions/Vorab_Notiz_H96_Omega_M_beta2.md`: konkrete Zählannahmen der offenen empirischen Hypothese bleiben bestehen.

## 3. Genaue Voraussetzungen der Sättigung

Betrachtet werden die in r63 verwendeten magnetischen Basiszustände |j,m⟩ mit ħ = 1, |m| ≤ j und den dort angegebenen Operatorerwartungen. Für diese Zustände lautet die Bedingung

ΔJ_x ΔJ_y = [j(j+1)−m²]/2 ≥ |m|/2.

Der Abstand zur Schranke faktorisiert als

j(j+1)−m²−|m| = (j−|m|)(j+|m|+1).

Für zulässige nichtnegative j ist Sättigung deshalb genau |m| = j. Bei nichtverschwindendem Spin sind das zwei Basiszustände pro j. Diese Aussage ist keine Klassifikation aller möglichen Superpositionen bei beliebiger Achsenwahl. „Zwei Zustände“ bezieht sich auf die gewählte magnetische Basis, nicht auf eine basisunabhängige Zählung sämtlicher reiner Zustände.

## 4. Kleinstes Gegenbeispiel zur Spinauswahl

| Basiszustand | Unsicherheitsprodukt | Robertson-Schranke | Sättigung |
|---|---|---|---|
| j = 1/2, m = 1/2 | 1/4 | 1/4 | ja |
| j = 1, m = 1 | 1/2 | 1/2 | ja |
| j = 3/2, m = 3/2 | 3/4 | 3/4 | ja |

Insbesondere erfüllt |1,1⟩ dasselbe Sättigungsprinzip wie |1/2,1/2⟩. Damit folgt die Beschränkung auf j = 1/2 nicht aus Sättigung allein. Ein vollständiger numerischer Scan ist dafür nicht nötig.

Dies ist eine direkte Auswertung der bekannten r63-Formel, keine neue Entdeckung der Sättigungszustände. Neu präzisiert wird die Reichweite des daraus beanspruchten Auswahlschlusses.

## 5. Absolute Minimierung wäre eine andere Forderung

Auf den Extremzuständen gilt ΔJ_x ΔJ_y = j/2 und ΔJ_x = ΔJ_y = sqrt(j/2). Unter der **zusätzlichen** Einschränkung auf j = 1/2, 1, 3/2, … minimiert deshalb j = 1/2 die absolute Unsicherheit. Der Schluss ist mathematisch nachvollziehbar, aber seine Voraussetzung ist eine Optimierungsregel über verschiedene Spinsektoren, nicht die Sättigung einer Schranke innerhalb eines Sektors.

Würde j = 0 zugelassen, wäre das absolute Minimum bereits dort null. Die Einschränkung auf nichttriviale Spin-/Flächenbeiträge ist daher ebenfalls zu nennen, statt den Wert 1/2 voraussetzungslos als globales Minimum auszugeben.

Für M, das alle j mit m = ±j zählt, braucht man umgekehrt eine Regel, die alle nichttrivialen Spinsektoren berücksichtigt und dort nur die beiden Extremzustände nimmt. „Absolutes Minimum über j“ und „Extremzustände bei jedem j vollständig zählen“ sind verschiedene Vorschriften. Sättigung ist mit beiden verträglich, entscheidet aber nicht zwischen ihnen.

## 6. Warum der Energie-Floor noch keine Spinrelaxation liefert

r63.3 verwendet E(v;μ) = μ/sqrt(v²−1) bei festem μ > 0. Für jeden solchen μ gilt E → 0 bei v → ∞. In dieser Formel kommt j nicht vor.

Selbst wenn später eine Zuordnung μ = μ(j) > 0 ergänzt würde, liefe diese Energie bei jedem zugelassenen j gegen null. Daraus folgt ohne weiteres Gesetz kein Übergang zwischen Spinsektoren und kein Endzustand j = 1/2.

Es fehlen insbesondere eine begründete Relation zwischen μ, Spin/Flächenbeitrag und Zustandsenergie sowie ein erlaubter Übergangsmechanismus, der j verändert. Einen solchen Mechanismus aus dem bloßen Wort „Relaxation“ zu folgern wäre derselbe vorgelagerte Fehler wie bei der früheren Auslöschungspflicht: Eine physikalische Zielrichtung würde vorausgesetzt, bevor ihr Gesetz angegeben ist.

Das ist kein allgemeiner Satz gegen eine mögliche Spinrelaxation. Es zeigt nur, dass die tatsächlich zitierte feste-μ-Kinematik diese Auswahl nicht leistet.

## 7. Auswirkung auf die Zählzahl

Die r63-Gleichung ist S_J(γ) = Σ_{j∈J} 2 exp(−2πγ sqrt(j(j+1))) = 1, wenn nur die beiden Extrembasiszustände jedes zugelassenen Spins gezählt werden.

Bereits die zwei endlichen Mengen J₁ = {1/2} und J₂ = {1/2,1} erfüllen diese Sättigungsauswahl. Ihre Summen sind für γ > 0 streng fallend. Am positiven Lösungswert der ersten Gleichung ist die zweite Summe wegen ihres zusätzlichen positiven Terms größer als 1. Die zweite Lösung liegt daher strikt höher. Existenz folgt hier direkt aus S_J(0) > 1 und S_J(γ) → 0 für diese endlichen Mengen.

Damit bestimmt selbst die Kombination „Sättigung plus die angegebene Zählgleichung“ keinen universellen γ-Wert, solange die zulässige Spinmenge J nicht unabhängig feststeht. Diese Demonstration verändert nicht die Zählregeln von H96 und behauptet nicht, dass beliebige endliche Mengen eine vollständige Horizonttheorie wären. Es sind Gegenmodelle zur Hinlänglichkeit des behaupteten Minimalprinzips.

## 8. Was als tatsächlich neues Auswahlgesetz erforderlich wäre

Die offene Brücke kann jetzt genauer benannt werden:

1. Ein physikalisch begründeter zulässiger Spinbereich für jeden Träger.
2. Ein Grund, weshalb T über diesen Bereich absolut minimiert, M dagegen Beiträge aller Spins zählt.
3. Falls Dynamik beansprucht wird: zulässige Übergänge, Erhaltungsgrößen und ein Generator, aus denen diese Auswahl folgt.
4. Eine gemeinsame, unabhängig bestimmte Mess-/Energieabbildung; die Spinauswahl allein würde die zweite Lücke aus dem vorherigen Arbeitsblock nicht schließen.

Eine Rückkehr zu einer frei gewählten Wirkung oder einem neuen Reservoir erfolgt hier nicht. Stattdessen ist der nächste enge Prüfschritt die **Kompatibilität mit der eigenen „ein Objekt, verschiedene Auslesungen“-Lesart**: Sind die unterschiedlichen Spinmengen Eigenschaften verschiedener physischer Zustände oder unterschiedliche Zugriffsmengen auf denselben Zustand? Die erste Lesart braucht einen Zustandswechsel, die zweite eine explizite eingeschränkte Ausleseabbildung und darf verworfene Beiträge nicht automatisch als fehlende Energie behandeln.

I1-Auslöser 3 bleibt durch die Herkunft von γ_BI/γ_string berührt; die String-/LQG-Idee ist ein möglicher gesondert zu begründender Weg, keine hier aktivierte Lösung. Keine Reaktivierung der gescheiterten I3-/I4-Varianten. H96 offen, H97 widerlegt, W1/W2 eingefroren; Guards unverändert. Keine nummerierte Schicht und keine Änderung vorhandener Beweise.
