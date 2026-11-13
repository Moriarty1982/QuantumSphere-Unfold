# Vorab-Notiz H103: Gibt eine native Struktur den Bezugszustand unter dem magischen Winkel im neutralen Qubit N?

**Stand:** 13. November 2026, abends, vor der Rechnung festgelegt. Autorenauftrag: „Erst Bezug suchen“. Es gibt keinen
Datenvergleich. Die Zielgröße (cos θ = ±1/√3) ist bekannt. Die Werte der Kandidaten wurden vor dem Commit dieser
Notiz **nicht** gerechnet; das Ergebnis ist also offen. Skript `k225_test_h103.py`.

## Vorwissen geprüft
- `op3_sedenion_charge_2026_11_13.md`:
  - Mit Q_* = 1/2 − (i/2) L_e8 (farbneutraler Block) ist N = ker Q_* = span(v_1, v_ω) mit v_1 = 1 + i e_8 und
    v_ω = e_7 − i e_15 ein farb- und ladungsneutrales Qubit. Dort gilt ψ = diag(1, ω).
  - Projektionen reeller Elemente mit rationalen Koeffizienten geben rationale cos θ. Die Diagonale (e_7+e_8+e_15)/√3
    gibt −1/3, die Hurwitz-Einheiten geben 0.
- `op3_sedenion_reference_2026_11_13.md`: Q_S = 1/2 − (i/6) L_e7 − (i/3) R_e7 ist die Fortsetzung über e_7. Der
  symmetrische Punkt a = exp(2π e_7/3) stammt aus r15.
- `op3_neutral_su2_octant_2026_11_13.md`, `op3_selection_principle_2026_11_13.md`:
  - Das Oktanten-Tripel verlangt |⟨r|ψr⟩|² = 1/2, also cos θ = ±1/√3 zur ψ-Achse.
  - Der Abstand vom Oktanten ist π/12 − θ_e.
- Suchrichtung (rückwärts): Für einen Bezug r gilt |⟨v_1|r⟩|² : |⟨v_ω|r⟩|² = (2 ± √3) : 1. Die Phase zwischen den
  Komponenten ist dabei gleichgültig, weil ψ diagonal wirkt. Ein Operator X legt einen Bezug als Eigenzustand seiner
  Kompression P_N X P_N fest. Er trifft genau dann, wenn deren Bloch-Vektor den Winkel arccos(1/√3) zur ψ-Achse hat
  (tan θ = √2).

## Verfahren
- N und ψ wie in `op3_sedenion_charge_2026_11_13.py` (Q_* mit L_e8).
- Für einen hermiteschen Operator X: B = P_N X P_N als 2×2-Matrix in der Basis (v_1, v_ω), mit dem Bloch-Vektor n
  ihres spurfreien Teils und c(X) = |n_z|/|n|. Ist n = 0, ist X auf N skalar und gibt **keinen** Bezug.
- Für ein Element x ∈ S: c(x) = |w_1 − w_ω|/(w_1 + w_ω) mit w = |⟨v|x⟩|². Ist die Projektion 0, gibt x keinen Bezug.
- **Treffer:** |c − 1/√3| ≤ 10⁻¹⁰.

**Kandidat A (Hauptkandidat): die Ladung des Companion.** X = Q_S, die über e_7 fortgesetzte Ladung (auf O gleich Q8).
Lesart: Der Bezug ist ein Eigenzustand der e_7-Ladung im e_8-neutralen Qubit. Seine ψ-Bahn bestünde dann aus den
Eigenzuständen der drei Generationsladungen ψ^k Q_S ψ^{−k}.

**Liste B (Nebensuche, fest), zusammen 47 Operatoren und 49 Elemente:**
- **B1:** i L_u und i R_u für die 15 imaginären Einheiten u = e_1 … e_15 (30 Operatoren).
- **B2 (17 Operatoren):**
  - L_e7 R_e7, reell symmetrisch;
  - die vier Spektralprojektoren von Q_S (q = 0, 1/3, 2/3, 1);
  - ε (a + b e_8 ↦ a − b e_8);
  - (C_a + C_a†)/2 und i(C_a − C_a†)/2, mit C_a der Konjugation mit dem r15-Punkt a = −1/2 + (√3/2) e_7;
  - i L_{Im x} und i R_{Im x} für x ∈ {a, ψa, ψ²a};
  - i L_f und i R_f mit f = (e_7 + e_8 + e_15)/√3;
  - Q_S + Q_*.
- **B3 (Elemente):** alle Produkte x·y mit x, y aus {1, e_7, e_8, e_15, a, ψa, ψ²a} (49 Produkte, sedenionisch).

## Entscheidungskriterium
- **H103a:** Q_S gibt einen Treffer. Dann ist H103 bestätigt, sonst widerlegt.
- **H103b (Nebensuche, berichtet, nicht entscheidend):** Anzahl der Treffer in Liste B. Jeder Treffer dort ist eine
  Suchtreffer-Aussage und muss eigens vorab geprüft werden.
- **Kontrolle:** Die Kompression von ψ selbst muss c = 1 geben (Achse), Q_* muss auf N skalar sein (n = 0), und die
  von Hand gesetzte Magie-Mischung muss ρ² = 1/2 und die Phase π/4 geben (Fehler ≤ 10⁻¹⁰).

## Bei Bestätigung / Widerlegung
- **H103a bestätigt:** Der Bezug wäre nativ: die Companion-Ladung (e_7) im e_8-neutralen Qubit. Das Oktanten-Tripel
  wäre dann die Bahn der drei Generationsladungen. Offen blieben die Wahl von e_8 und warum nur Neutrinos den Träger
  sehen.
- **H103a widerlegt:** Die Companion-Ladung legt den Bezug nicht fest. Der Bezug bleibt offen, außer bei einem Treffer
  in B. Ein solcher Treffer wäre nur ein Hinweis auf einen Suchtreffer und würde eine eigene Vorab-Notiz verlangen.

## Offenlegung
Die Zielgröße ist bekannt, die Kandidatenwerte sind es nicht. Liste B ist eine Suche mit 96 Einträgen, deshalb wird nur
A gewertet. Die Wahl von e_8 als Ladungsachse für N bleibt eine Annahme aus der Erkundung.
