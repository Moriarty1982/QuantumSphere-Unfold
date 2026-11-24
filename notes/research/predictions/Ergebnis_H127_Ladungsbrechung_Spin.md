# Ergebnis H127: Die Ladungsbrechung ist reiner Spin 3; die Leckordnung bleibt offen, weil die gewählte Kopplung sie nicht sehen kann

Vorab-Notiz: `Vorab_Notiz_H127_Ladungsbrechung_Spin.md`, Commit ba473c5 (2026-11-24 15:59 UTC), vor der Rechnung. Skripte
`k276_test_h127.py` (Python numpy, Ausgabe `k276_out.txt`; Erstlauf `k276_out_erstlauf.txt` mit denselben Kriteriumswerten, danach wurde
nur die Nachkontrolle angehängt) und `k276b_spin_exakt.wl` (Wolfram Language exakt, Ausgabe `k276b_out.txt`). Ablage:
`notes/research/hilbert_shift_felder_2026_11_24/rueckwaerts/h127/`. Verfahren und Kriterium unverändert. Qiskit nicht eingesetzt (keine Schaltung).

## Ergebnisse

| Stufe | Kriterium | Befund | Urteil |
|---|---|---|---|
| A: Spin-Inhalt von P_s C P_s | w₃ ≥ 10⁻⁸ und führend | **w₃ = 1 exakt**, alle anderen w_l = 0 (Wolfram exakt; Python 4·10⁻³¹) | **bestätigt** |
| A, Kontrolle | w_l < 10⁻¹⁰ für l ∉ {3, 6, 7, 9, 10} | max 4·10⁻³¹ | erfüllt |
| B: Leckordnung | b₀ < 10⁻¹⁰, b₁ > 10⁻⁸ | b₀ = 4·10⁻¹⁵, aber C_eff⁽ⁿ⁾ = 0 für n = 1, 2, 3 (‖A₁‖ = 10⁻¹⁶) | **widerlegt nach Wortlaut** |

**Stufe A im Einzelnen.** End(H₃(ℂ)) = End(1 ⊕ 3 ⊕ 5) zerfällt in 3 × l0, 6 × l1, 6 × l2, 3 × l3, 1 × l4 (Casimir-Multiplizitäten 3, 18, 30, 21, 9;
Wolfram). C = L_e₇ je Platz liegt **ganz** im Spin-3-Teil (‖C‖² = 6), ist A₄-invariant und wechselt unter den ungeraden Elementen das Vorzeichen
(beides exakt). Mehr als die Vorhersage: Nicht nur führt l = 3, es gibt **keine** andere Komponente. Die Ladungsbrechung der Familien-SO(3)
ist also genau ein Spin-3-Objekt, die Tetraeder-Pseudoskalare der Oktaedergruppe.

## Nachkontrolle (nach der Auswertung, kein Kriterium)
Warum ist C_eff⁽ⁿ⁾ = 0? Die Kopplung K(A) = Σ_a L_{Y_a} A L_{Y_a} ist auf den antisymmetrischen Operatoren nicht trivial (Zufallstest ‖K‖ ≈ 20), hat dort
aber **Rang 52**. Nach Schur (Λ²27 = 52 ⊕ 273 unter F₄) ist K dort (3/2) mal der Projektor auf f₄ (geprüft: K(T) = 1,5 T für T ∈ so(3), Rest 4·10⁻¹⁶).
C = L_e₇ je Platz ist kein Derivationsgenerator und steht senkrecht auf f₄, also K(C) = 0 und alle A_n = 0.

**Lesart:** Das Ergebnis von Stufe B folgt aus der Wahl von K, nicht aus den Quarks. Die in der Vorab-Notiz für diesen Fall genannte Lesart
(„Quarks tragen SO(3) effektiv exakt“) ist damit **nicht gedeckt**. K kann eine Brechung außerhalb von f₄ gar nicht weitergeben. Das hätte vor
der Rechnung auffallen können (Schur auf Λ²). Es wird hier als Mangel der Vorab-Notiz festgehalten und nicht nachträglich umgedeutet.

## Einordnung
1. **Neu und belastbar (Stufe A):** Die Brechung SO(3) → A₄ ist kein Gemisch, sondern ein einziger irreduzibler Spin-3-Tensor (xyz-Typ).
   In der Spurion-Sprache ist das genau das Objekt t_ijk = |ε_ijk|, das A₄-Flavon-Modelle (Ma–Rajasekaran, Altarelli–Feruglio) **ansetzen**.
   Hier folgt es aus der Ladungsstruktur der Albert-Algebra. Eine Massenmatrix (Bilinearform, l ≤ 2) kann es erst zusammen mit einem
   Vektor erreichen, etwa M_ij ∝ t_ijk v_k. Das ist die Struktur des Vorschlags und bleibt eine Setzung.
2. **Offen (Stufe B):** Ob und in welcher Ordnung die Quarks die Brechung spüren, ist nicht beantwortet. Ein Folgetest braucht eine Kopplung,
   die nicht durch f₄ faktorisiert, zum Beispiel die symmetrische Kopplung über L_Y ohne Paarung oder das Jordan-Produkt mit einem
   Flavon-Element. Das ist eine neue Wahl und bräuchte eine neue Vorab-Notiz.
3. Kein Datenvergleich (die Vorab-Notiz sah ihn nur als nicht blinde Einordnung vor, und ohne Leckordnung gibt es nichts einzuordnen).
   Vorausgesetzt bleibt „drei Plätze = Generationen“. Kein Guard berührt, OP3 bleibt offen.
