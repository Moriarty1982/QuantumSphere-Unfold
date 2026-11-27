# Ergebnis H204 (k414): Keine einzelne „Elter"-F₄-Darstellung bindet D/B — **nein**

**Datum:** 2026-11-27. **Werkzeuge:** Python (numpy) für die Farbblock-Operatoralgebra und die Idempotente, sympy für die Grad-Zerlegung, **Wolfram Language** (exakt) als unabhängige Gegenkontrolle. Beide einig.
**Vorab:** `Vorab_H204_Elter_Darstellung.md` (vor der Rechnung committet). **Teilweise nicht blind** (siehe unten).

## Frage
Sind B (ladungsgerades l_k²) und D (ladungsungerades l_k²) zwei Zweige **einer** höheren F₄-Darstellung, deren Verzweigung D/B darstellungstheoretisch festlegt?

## Befund: nein (Kriterium K2)

**(A) Die Ladungs-kovariante l_k²-Operatoralgebra auf dem 36-dim Farbblock ist 2-dimensional.**
Erzeugt von {1, iL_U} mit (iL_U)² = 1 exakt (Wolfram: L_U² = −1). Sie hat **genau zwei** minimale Idempotente (irreduzible Komponenten, „einzelne Darstellungen"): P_up = ½(1+iL_U) und P_dn = ½(1−iL_U), beide mit Spur 18, orthogonal und vollständig (P_up + P_dn = 1). Jede **einzelne** Komponente erzwingt D/B nur in der **diskreten** Menge:

| Operator O (l_k²-Koeffizient) | (B, D) | D/B |
|---|---|---|
| 1 (ladungsblind, F₄-invariant) | (1, 0) | 0 |
| iL_U (J-Form Q₀−½) | (0, 1) | ∞ (B = 0) |
| P_up (chiral, irred. +) | (½, ½) | +1 |
| P_dn (irred. −) | (½, −½) | −1 |

Ein **allgemeiner** Massenoperator a·P_up + b·P_dn braucht **zwei** Koeffizienten (b_up, b_down) = **zwei** Komponenten. D/B = 1 gilt nur bei **rein** P_up (b_down = 0 exakt).

**(B) B und D leben in verschiedenen F₄-Feldgraden.**
B (gerades l_k²) tritt zuerst bei Feldgrad **5** auf, D (ungerades l_k², H186-Formen) bei Grad **4** (sympy, deckt H201). Eine **irreduzible** F₄-Darstellung lebt in **einem** homogenen Tensorgrad (Symⁿ des 26): B sitzt in Sym⁵, D in Sym⁴. **Keine einzelne F₄-Irrep kann beide Beine tragen.**

**(C) Abgleich mit dem scharfen Datenwert.**
D/B = 1,0085 ± 0,0010 (4-Parameter-Fit H197/H202). Nächster diskreter Verzweigungswert: **+1 (chiral P_up), 8,5σ entfernt**; die übrigen {0, −1, ∞} liegen bei ~1000σ / ∞. Der Datenwert liegt **zwischen** den Werten einer einzelnen Darstellung ⇒ eine **zweite**, unabhängige Komponente ist nötig.

## Deutung
D/B ist eine **freie relative Normierung** zwischen zwei unabhängigen Invarianten **verschiedenen Grades** (Sym⁵ für B, Sym⁴ für D), **kein** Clebsch–Gordan-Verhältnis einer einzigen Darstellung. Die ~0,9 % Abweichung von der reinen Chiralität (D/B = 1) ist genau die Beimischung der zweiten Komponente (b_down ≠ 0). Das **bestätigt H202** (Abbildung Kopplungen → (A,B,C,D) Rang 4, Kopplungen frei) und **schließt die Elter-Route**.

## Ehrlichkeit (teilweise nicht blind)
Der analytisch feste Teil — B Grad 5, D Grad 4 (verschiedene Grade) — war aus H201 bekannt, die Unabhängigkeit (Rang 4) aus H202. **Neu** an H204 ist die ausdrückliche Elter-/Branching-Lesart: die Ladungs-kovariante Operatoralgebra als exakt 2-dimensionale kommutative Algebra mit genau zwei minimalen Idempotenten, deren einzelne „Darstellungen" nur die diskreten Werte D/B ∈ {0, +1, −1, ∞} erzwingen, und der **quantitative Abgleich** dieser diskreten Werte (8,5σ zum nächsten) mit dem scharfen Datenwert. Die Grad-Trennung ist als bekannt markiert; der Idempotent-/Branching-Teil ist der prüfende.

## Stand Quark-Kopplungen
Weder Grad (H201), Symmetrie (H197), Laufeffekt (H199), Holomorphie (H200), minimale Invariant-Zahl (H202), Lepton-Sektor (H203) **noch eine einzelne Elter-F₄-Darstellung (H204)** fixiert die vier Quark-Kopplungen A, B, C, D. Die Quark-Massenhierarchie ist in diesem Rahmen **nicht herleitbar**; die Kopplungen sind freie Eingaben. OP3/OP4 bleiben offen.

**Verbleibende Weggabeln:** Mischung-Strang (freier Drehwinkel) oder den Quark-Massenstrang ruhen lassen (wie β_sym nach 37 Versuchen).

## Dateien
- `Vorab_H204_Elter_Darstellung.md` — Vorab-Notiz (vor der Rechnung).
- `k414_test_h204.py`, `k414_out.txt` — numpy/sympy-Rechnung und Ausgabe.
- `k414b_kontrolle.wl`, `k414b_out.txt` — Wolfram-Gegenkontrolle (exakt).
