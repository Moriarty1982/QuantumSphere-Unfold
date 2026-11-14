# Ergebnis H103: Die Companion-Ladung Q_S legt im neutralen Qubit keinen magischen Bezug fest (widerlegt)

**13.11.2026, abends.** Vorab-Notiz `Vorab_Notiz_H103_Bezug_im_neutralen_Qubit.md` (Commit 45314b2), Skript
`k225_test_h103.py`, Ausgabe `k225_out.txt`. **Status: H103a widerlegt.**

## Kontrollen
Alle Kontrollen sind bestanden:
- Basis: Q_* v = 0 und ψ = diag(1, ω);
- c(ψ) = 1;
- Q_* ist auf N skalar;
- die Magie-Mischung gibt ρ² = 1/2 und die Phase π/4, beide mit einem Fehler ≤ 10⁻¹⁵.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H103a: Q_S auf N | c = 0 (Bloch-Vektor ⟂ ψ-Achse, 90°) | c = 1/√3 ± 10⁻¹⁰ | widerlegt |
| H103b: Liste B, 47 Operatoren | 1 Treffer: i R_f, f = (e_7+e_8+e_15)/√3 | berichtet | Suchtreffer, nicht gewertet |
| H103b: Liste B3, 49 Produkte | c ∈ {1/2, 5/8, 1} | berichtet | kein Treffer |

## Lesart
- Auf N ist Q_S = 1/2 + (1/3)σ_y. Die e_7-Ladung wirkt also wie ein reeller Zustand senkrecht zur ψ-Achse und gibt
  K = 1/2, nicht den Oktanten.
- **Nachträglich:** Unter den 96 Einträgen der Nebenliste trifft nur die Rechtsmultiplikation mit der Raumdiagonale f
  exakt. Dieser Treffer ist ein Suchtreffer und keine Bestätigung. Er braucht eine eigene Vorab-Notiz, etwa mit der
  Frage, warum R_f und nicht L_f nativ wäre: L_f ist auf N skalar.
- Der Bezug bleibt offen. OP3/OP4 bleiben offen, die Guards sind unverändert.

## Nachtrag 14.11.2026: Der Suchtreffer i R_f ist analytisch erzwungen (Erkundung, nicht blind)
Autorenentscheidung: „Als Erkundung nachtragen“. Es wird keine H-Nummer vergeben. Skript
`../op3_rf_reference_2026_11_14.py`, Ausgabe `..._out.txt`.

- **N ist ein Rechtsmodul über H_n.** H_n = span(1, e_7, e_8, e_15) ist assoziativ, deshalb vertauscht R_u mit L_e8,
  also mit Q_*. Jedes R_u mit u ∈ Im H_n bildet N = ker Q_* in sich ab. L_e7 und L_e15 führen aus N heraus und sind
  auf N null. L_e8 ist auf N konstant −i. Deshalb ist L_f auf N skalar.
- **Pauli-Tripel.** i R_e7, i R_e15 und i R_e8 wirken auf N wie σ_x, σ_y, σ_z. Ihre Quadrate sind 1, sie
  antikommutieren, und i R_e8 ist die ψ-Achse.
- **Folge.** Für jeden Einheitsvektor u ∈ Im H_n gilt c(i R_u) = |⟨u, e_8⟩| (numerisch auf 2·10⁻¹⁶). Alle acht
  Vorzeichen-Diagonalen (±e_7 ± e_8 ± e_15)/√3 geben deshalb den magischen Winkel. Der Treffer folgt aus dem Winkel der
  Diagonale zu e_8; ein unabhängiger Befund ist er nicht. Inhaltlich ist es derselbe Mechanismus wie in
  `op3_sedenion_reference_2026_11_13.md`, Punkt 4, nur jetzt auf dem neutralen Qubit.
- **Was offen bleibt:**
  - warum die Rechtswirkung von H_n physikalisch maßgeblich ist;
  - was die Raumdiagonale unter allen Richtungen in Im H_n auszeichnet. Der Bezug ist damit auf die Wahl einer
    Richtung in Im H_n zurückgeführt, aber nicht hergeleitet.
- OP3/OP4 bleiben offen. H104 bleibt frei.
