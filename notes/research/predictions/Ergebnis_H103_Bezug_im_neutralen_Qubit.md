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
