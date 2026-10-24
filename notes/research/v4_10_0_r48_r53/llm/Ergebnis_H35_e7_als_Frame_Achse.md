# Ergebnis H35: e₇ ist Bezugsachse nur für die Tachyon-Abbildung; Ladungen sind zwischen Materie und Tachyon frame-frei

Vorab-Notiz: `Vorab_Notiz_H35_e7_als_Frame_Achse.md`, Commit 42e4fcc (2026-10-24 03:51 MESZ), vor der Rechnung. Vorab offengelegt: R ist ℂ-linear,
T und J_B antilinear; auf dem Triplett gibt es keine farbverträgliche J-antilineare Abbildung. Skript `k91_test_h35.py`, Ausgabe `k91_out.txt`;
Lean `R_iL`, `R_iR`, `R_P4` in `formal/QSFormal/Sektoren.lean`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H35a Frames auf ℂ⊗𝕆 | **bestätigt** | R (z ↦ iz) vertauscht mit iL, iR, Q, B − L, su(3) und allen P_s; T und J_B bilden P_(ℓ,r) auf P_(−ℓ,−r) ab |
| H35b innere Einheit | **bestätigt** | L_{e₇} vertauscht mit su(3) = Stab(e₇) (dim 8 in g₂, dim 14); die farbverträglichen K mit K L_{e₇} = −L_{e₇} K bilden einen 2-dimensionalen Raum und verschwinden auf e₇^⊥ |
| H35c Frame-Ebene | **bestätigt** | φ(x + iy) = x + y e₇ übersetzt z ↦ iz in L_{e₇}, z ↦ z̄ in die Oktonion-Konjugation, z ↦ i z̄ in ihr Produkt |

## Einordnung

1. **e₇ ist Bezugsachse der Frames nur teilweise.** Die Tachyon-Abbildung z ↦ iz hat mit L_{e₇} ein inneres, farbverträgliches Gegenstück auf ganz 𝕆.
   Auf der Singulett-Ebene span(1, e₇) haben es alle drei Frame-Abbildungen: Dort ist die Frame-Ebene die Ebene des Photon-Kerns. Zeitumkehr T und
   J_B brauchen auf dem Farb-Triplett die äußere Einheit, weil 3 und 3̄ nicht äquivalent sind.
2. **Ladungen sind zwischen Materie und Tachyon frame-frei.** Die Tachyon-Abbildung von Konvention F (z ↦ iz, K72.1) lässt jeden Sektor fest: Ladung,
   B − L und Chiralität sind im Materie- und im Tachyon-Frame gleich. Die Ladungskonjugation Q ↦ 1 − Q ist der Zeitumkehr-Anteil T (auf dem Dublett σ_z,
   der Tausch von Kompensator- und Partnerport), nicht die Tachyon-Abbildung (σ_y).
3. **Korrektur der Frame-Zeilen (nachgetragen, nichts umgeschrieben).** Wo r41, r43, r47, r48 und r49 vom „Frame T“ als Ladungskonjugation sprechen, ist
   die Zeitumkehr T gemeint, also der Porttausch, nicht der Tachyon-Frame der Spalte M/T/P. In der Spalte gilt für diese Ergebnisse: gleich in M und T.
   Die Lean-Namen `frameT`, `frameT_swaps_left` (Ladungen.lean) bezeichnen ebenfalls die Zeitumkehr. Das deckt sich mit K80.4 (R Q R⁻¹ = Q, „die Wirkung
   kommt vom Zeitumkehr-Anteil T“) und mit r47 („Partner im T-Frame gelesen“ = über den Partnerport).
4. **Lesart:** Der Kompensator ½(1 + iL_{e₇}) aus r42 ist der Kompensatorport, 1 − C der Partnerport; T tauscht die Ports und damit die Chiralitäten, R lässt
   beide fest. Chiralität iL_{e₇} = (äußeres z ↦ iz) ∘ (inneres z ↦ e₇z): linkshändig sind die Zustände, auf denen beide Tachyon-Abbildungen bis aufs
   Vorzeichen übereinstimmen.
