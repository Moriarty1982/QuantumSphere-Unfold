# Vorab-Notiz H31: Können gemischte Readouts die Triality τ brechen und so Mischung erzeugen?

Festgelegt am 2026-10-23, **vor** der Rechnung. Autor: „ja prüfe das“. Bezug: r44 (Mischung braucht τ-Brechung, für up und down verschieden),
r45 (Chiralität bricht ρ, nicht τ), r39 (Readouts der Stufe j = Schritt 2^j, Masken Σ und ∨, Selektor-Kontraktion χ_mn R^m S^n),
`def:binary-mask-registry-mixed-readouts` (Bits für Auslesearten, Maske = ODER), `def:guarded-two-sided-mixed-qam-readout`.

## Rahmen

Platzraum ℂ³ (drei Generationen-Plätze), P = τ (zyklische Verschiebung). Kopplungen für up und down: hermitesche ℤ₃-Zirkulanten M_u, M_d
(nach r44/r45 ρ-gebrochen, τ-symmetrisch). Mischung |V| = |U_u†U_d|.
- **Verschiebungs-Readouts:** alle Operatoren, die aus Stufen-Readouts P^{2^j} gebildet werden: Produkte (Lesart Σ), erzeugte Untergruppen
  und ihre Mittel (Lesart ∨), Selektor-Kontraktionen Σ χ_mn P^{2^m}P^{2^n} mit beliebigen komplexen χ_mn.
- **Art-Masken:** Ist die Ausleseart der Platz (Generation), so ist eine Maske ein diagonaler Projektor D_S = Σ_{i∈S} e_i e_iᵀ (S ⊂ {1, 2, 3}).
  Gelesene Kopplung: M + δ·D_S (Gewicht δ ≥ 0).

## Offenlegung

H31a folgt daraus, dass alle Verschiebungs-Readouts im Gruppenring ℂ[ℤ₃] liegen und dieser kommutativ ist; das ist vorab klar. H31c ist
allgemeine Störungstheorie (Mischung ∝ Störung / Massenabstand). Neu ist nur die Zuordnung zu den Readout-Arten des Companion.

## Hypothesen

- **H31a (Verbot):** Jeder Verschiebungs-Readout vertauscht mit τ. Zu M_u, M_d addiert, ergibt er keine Mischung (|V| bleibt eine Permutation).
  Die gemischten Readouts aus Verschiebungen können τ nicht brechen.
- **H31b (Art-Masken brechen τ):** Eine Art-Maske D_S mit S ≠ ∅, {1, 2, 3} vertauscht nicht mit τ. Mit δ > 0 ist |V| für generische M_u, M_d
  keine Permutation, auch wenn up und down dieselbe Maske und dasselbe δ haben.
- **H31c (schwache Brechung, Skalierung):** Für kleines δ wachsen die Nebendiagonal-Einträge von |V| linear in δ; |V_ij|/δ hängt umgekehrt
  vom Abstand der Massen i und j ab (Prüfung: das Verhältnis |V_ij|·|λ_i − λ_j| / δ ist für δ → 0 beschränkt).
- **H31d (Frames):** Art-Masken sind reell; sie vertauschen mit dem Frame-Wechsel T. Die so erzeugte τ-Brechung ist frame-frei.

## Entscheidungskriterium (verbindlich)

H31a, b, d bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹); H31b, c an 200 Zufallsfällen. Einordnung vorab:
- H31a bestätigt ⇒ Die gemischten Readouts, so wie sie aus dem Hilbert-Shift gebildet sind, erzeugen **keine** Mischung.
- H31b, c bestätigt ⇒ Erst ein Readout, der Generationen als eigene Auslesearten unterscheidet, bricht τ. Dann entsteht Mischung, und sie ist
  klein, wenn die Maske schwach gewichtet ist und die Massen weit auseinanderliegen. Die Mischung wäre im Modell ein **Effekt des Auslesens**,
  nicht der Dynamik. Die Zahlenwerte folgen daraus nicht.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
