# Ergebnis H89: Der Energie-Impuls-Tensor von W1 ist hergeleitet; p = ρ gilt, aber mit positivem ρ, und der Vier-Fermionen-Anteil allein hat Λ-Form

Vorab-Notiz `Vorab_Notiz_H89_W1_Einstein_Gleichung.md`, Commit `6355d15` (nicht blind). Code `k204_w1_einstein.wl` (Wolfram-Connector).

## Ergebnisse
- **H89a bestätigt:** Die Vierbein-Variation von e·L_4f bei festen Spinoren gibt T^(4f)_μν = −g_μν L_4f = (3κ/16)·j²·g_μν (Rest Nullmatrix). Für sich genommen hat der Vier-Fermionen-Anteil die Form eines Λ-Terms (p = −ρ), mit einer Höhe ∝ j², die nicht konstant ist.
- **H89b bestätigt:** Zwei Weyl-Felder mit entgegengesetztem Spin, ψ_s = e^{−i(3κn/8)t}χ_s, lösen die Weyl-Gleichung aus H88 exakt (Rest 0), der Gesamtstrom ist (n, 0, 0, 0). Auf dieser Lösung ist L_kin = 3κn²/8, L_gesamt = 3κn²/16, und der ganze Tensor T_μν = T^Bel_μν − g_μν L_gesamt ist diag(3κn²/16, …) mit unteren Indizes: **ρ = p = (3κ/16)·n² > 0**.
- **H89c bestätigt:** Die Vierbein-Variation erster Ordnung um den flachen Raum, mit dem aus de + ω∧e = 0 gelösten (nicht eingesetzten) Spinzusammenhang, ist auf einer Lösung (zwei ebene Wellen, Weyl-Rest 0) exakt das Negative des Belinfante-Tensors (Abweichung 7·10⁻¹⁵ und 5·10⁻¹⁵ an zwei Punkten bei Werten der Größe 30–90) und exakt symmetrisch (antisymmetrischer Teil 0). Das rechtfertigt die Form in H89b.
- **Nicht geprüft:** die volle nichtlineare Einstein-Gleichung und die Bianchi-Identität auf allgemeinen Lösungen.

## Offenlegung
- Der erste Lauf von H89c scheiterte an der Laufzeitgrenze; die Rechnung wurde vereinfacht, indem die festen Spinoren gleich als Lösung eingesetzt und h, ∂h als Symbole geführt wurden (gleiche Größe, kein Inhalt geändert).
- Der zweite Lauf hatte einen Fehler in meinem Code: ConjugateTranspose konjugierte die reellen Symbole dh mit. Korrigiert.
- Der dritte Lauf ergab keine Übereinstimmung (antisymmetrischer Teil ≠ 0). Nach der vorab festgelegten Reihenfolge zuerst Konventionen geprüft: In ω_μab Σ^{ab} hatte ich zusätzliche η-Faktoren angehängt (ω_μ^{ab} statt ω_μab). In H88 war die Kontraktion richtig. Nach der Korrektur stimmt alles. Die Abweichung lag also in meinem Prüfcode, nicht in der W1-Notiz.

## Vergleich mit der W1-Notiz
- „p = ρ“ für den Vier-Fermionen-Einfluss: **richtig**, wenn man den ganzen Energie-Impuls-Tensor auf Lösungen nimmt (H89b).
- „ρ ∝ −κn², Vorzeichen konventionsabhängig“: Für den gerechneten Zustand (Moden positiver Frequenz) ist ρ **positiv**, ρ = (3κ/16)n². Das Vorzeichen hängt am Zustand (Besetzung positiver oder negativer Frequenz), nicht an einer Konvention.
- „nicht wie Λ“: richtig für den ganzen Tensor; der Vier-Fermionen-Term **für sich** hat Λ-Form (H89a), mit nicht konstanter Höhe. Er lässt sich physikalisch nicht vom kinetischen Teil trennen.
- r81 („W1 erzeugt keinen Vakuumterm“) ist davon nicht berührt: Der ganze Tensor des homogenen Zustands ist steife Materie (p = ρ), kein Λ.

## Folge
Die Feldgleichungen von W1 sind jetzt bis auf die volle nichtlineare Einstein-Gleichung unabhängig hergeleitet: Weyl, Ward und Torsion (H88) und der Energie-Impuls-Tensor als Quelle der Einstein-Gleichung in erster Ordnung (H89c), samt seiner Form für homogene Zustände (H89a, b). Die W1-Notiz bekommt einen Nachtrag zum Vorzeichen von ρ und zur Λ-Form des Vier-Fermionen-Anteils.
