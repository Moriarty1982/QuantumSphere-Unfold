# Ergebnis H125: Relatives Vorzeichen der CP-Verletzung zwischen Leptonen und Quarks

Vorab-Notiz: `Vorab_Notiz_H125_Relatives_CP_Vorzeichen.md`, Commit 76f7a6c (24.11.2026, vor der Rechnung). Freigabe des Autors: „mach weiter“.
Skripte und Ausgaben: `../h125_relatives_cp_2026_11_24/` (k252).

## Stufe A (Strukturprüfung, nicht blind): bestätigt

| Prüfung | Leptonen (H_n, Rang 2) | Quarks (farbig, Rang 6) |
|---|---|---|
| A1: [R_e7, R_e8] = λ R_e15 | λ = −2 (Rest 0) | λ = +2 (Rest 0) |
| A3: B = Tr(P₇P₈P₁₅)/Rang | 1/4 − i/4 | 1/4 + i/4 |
| A3: Zuordnungen mit vollem Rang | 24, alle det −1, alle Im B < 0 | 24, alle det +1, alle Im B > 0 |
| A2: B_Leptonen = conj(B_Quarks) | ja | |

Referenz: Die Linkswirkung von H (Lorentz-Spin) hat [L_i, L_j] = 2L_k und B = 1/4 + i/4. Die Familien-su(2) der Leptonen ist also relativ zum
Lorentz-Spin das komplex konjugierte Dublett, die der Quarks nicht. Ursache: Die Sedenion-Rechtsmultiplikation ist nicht assoziativ, deshalb
ist [R_a, R_b] auf den beiden Blöcken ±2R_c. Wolfram exakt: Für [J_x, J_y] = i s J_z gilt B = 1/4 + i s/4, und s ↦ −s konjugiert B.

Kein Abbruch: A1 und A3 halten in allen 24 + 24 Zuordnungen.

**Abweichung vom Verfahren:** In der Vorab-Notiz stand „Wolfram exakt“ für Stufe A. Die Blockrechnung lief in Python (numpy) auf der
bestehenden Infrastruktur von `op3_cs_dixon_map_2026_11_15/search.py`, weil die Sedenion- und Dixon-Tafeln dort liegen; die Reste sind 0 bis
auf Gleitkommagenauigkeit. Wolfram prüft exakt den algebraischen Kern (B als Funktion des Strukturvorzeichens). Qiskit nicht eingesetzt
(kein Schaltkreis; die Bargmann-Schaltung für 1/4 + i/4 liegt aus H123/k244 vor).

## Stufe B (Datenvergleich, blind gegen künftige Daten): offen
Vorhersage unter S1: sign(J_PMNS) = −sign(J_CKM), also sin δ_PMNS < 0. Entschieden wird mit der ersten globalen Analyse, die das
Vorzeichen auf ≥ 3σ festlegt; Frist 31.12.2035. Heutiger Stand (vorab genannt): J_CKM > 0, NuFIT-Bestwert bei normaler Ordnung mit sin δ < 0,
nicht entscheidend.

## Einordnung
- Stufe A zeigt: Die Struktur legt ein **relatives** Vorzeichen zwischen Leptonen und Quarks fest; es ist frei von der Konvention i ↦ −i,
  weil diese beide Sektoren gleichzeitig konjugiert. Das ist der erste Befund in der Drehsinn-Reihe (k245–k252), der ein Vorzeichen nicht setzt.
- Die Brücke zur CP-Phase bleibt Setzung S1 (CP entsteht in beiden Sektoren gleich aus der Familienstruktur). Der absolute Drehsinn bleibt
  eine Konvention.
- Grenzen: CT-003 und r33.2 (Lesart) gelten; nur zwei Generationen (Dublett). OP3 und OP4 offen; kein Guard berührt.
