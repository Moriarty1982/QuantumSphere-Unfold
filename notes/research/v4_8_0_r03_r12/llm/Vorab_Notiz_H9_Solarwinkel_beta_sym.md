# Vorab-Notiz H9: Solarer Mischungswinkel aus β_sym (Vorhersage für künftige JUNO-Daten)

Festgelegt am 2026-10-20. Bezug: K17.4 (Nachbefund aus H5), K22.

## Hypothese (V)

**H9:** |U_e2|² = β_sym², also sin²θ₁₂ = β_sym² / cos²θ₁₃.
Mit den Companion-Konstanten γ_string = ln2/(π√3) = 0,127384, γ_BI = 0,2375 (Eingabewert, unverändert),
γ_L = γ_BI/γ_string = 1,86444, β_sym = √((γ_L−1)/(γ_L+1)) = 0,549348:
**sin²θ₁₂ = 0,30862 ± 0,00018** (Fehler nur aus sin²θ₁₃ = 0,02215 ± 0,00057, NuFIT 6.0).

## Offenlegung (vor dem Festschreiben bekannt)

1. Die Relation wurde **nachträglich** gefunden (K17.4): Sie fiel bei der Auswertung von H5 auf und war nicht
   vorab registriert. β_sym ist eingesetzt, nicht hergeleitet (OP1 offen); der Companion hat rund zehn
   vergleichbare Konstanten. Ein Treffer auf dem heutigen Datenstand ist daher kein Beleg.
2. Vor dieser Notiz gelesen: **JUNO 2026** (arXiv:2609.37895, 207,2 Messtage): sin²θ₁₂ = 0,3036 ± 0,0064.
   H9 liegt 0,8σ darüber; kombiniert mit NuFIT 6.0 (0,3046 ± 0,0056) 0,7σ. Dieser Vergleich **zählt nicht**
   als Test.
3. Zum Vergleich, ebenfalls bereits bekannt: TM1 (sin²θ₁₂ = 0,3182, aus H4/H8) liegt 2,3σ über JUNO 2026,
   TM2 5,8σ.

## Was getestet wird (verbindlich)

Die **nächste** JUNO-Veröffentlichung von sin²θ₁₂, deren 1σ-Fehler höchstens 0,004 beträgt (deutlich genauer als
heute). Ersatzweise ein globaler Fit, der diese Daten enthält. Ältere Daten zählen nicht.

## Entscheidungskriterium (verbindlich)

Pull z = (0,30862 − x)/σ_x mit dem neuen Messwert x:
- |z| < 2: **verträglich**,
- 2 ≤ |z| < 3: **Spannung**,
- |z| ≥ 3: **widerlegt**.

Wird H9 widerlegt, fällt die Verbindung „β_sym ↔ solarer Winkel“ weg; β_sym selbst bleibt davon unberührt.
Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
