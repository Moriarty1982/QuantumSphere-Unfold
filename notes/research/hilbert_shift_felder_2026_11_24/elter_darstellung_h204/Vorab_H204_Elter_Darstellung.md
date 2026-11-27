# Vorab-Notiz H204 (k414): Binden B und D eine einzige „Elter"-F₄-Darstellung?

**Datum:** 2026-11-27. **Strang:** Quark-Massenursprung, nach H202 (Rest D/B frei) und H203 (Lepton-Sektor bindet nicht). **Auslöser:** Weggabel-Karte des Autors, Option B „Elter-F4-Darstellung prüfen" (gewählt 12:18 UTC): „Noch eine Quark-Route: ob B und D Zweige einer einzigen höheren F4-Darstellung sind, deren Verzweigung das Verhältnis bindet."

## Frage
Im Massenmodell m_s(k) = [A·l_k + B·l_k² + s(C·l_k + D·l_k²)]/(l_i+l_j)² (s = ±1 Ladung) sind die vier Kopplungen A, B, C, D nach H202 frei (Rang 4). Die bisher offene Stelle ist der Ladungs-l_k²-Sektor: **B** (ladungs**gerade**) und **D** (ladungs**ungerade**).

**H204:** Gibt es eine einzige höhere („Elter-", engl. *parent*) F₄-Darstellung R, deren Verzweigung unter der Ladungs-U(1) (bzw. F₄ → SU(3)_c) genau B und D als zwei Zweige liefert, sodass ein **darstellungs­theoretischer** (Clebsch-ähnlicher) Koeffizient das Verhältnis D/B festlegt — unabhängig von frei wählbaren Vorfaktoren?

## Was gerechnet wird (k414)
Zwei Teile, mit der Maschinerie aus k408 (H198, Farbblock) und k411 (H201, Grad-Zerlegung).

**Teil A — Ladungs-kovariante Operatoralgebra auf dem Farbblock (36-dim).**
Der l_k²-Koeffizient ist ein Operator O im Ladungsraum. Die unter der Ladung kovarianten Operatoren werden von {1, iL_U} erzeugt (L_U = Linksmult. mit U = e₇; (iL_U)² = 1). Baue diese Algebra explizit, bestimme ihre Dimension und ihre **minimalen Idempotente** (= irreduzible Komponenten = „einzelne Darstellungen" im Ladungs-Branching). Für jedes minimale Idempotent und für die Erzeuger das erzwungene (B, D) = (gerade, ungerade) und D/B ablesen.

**Teil B — F₄-Feldgrad von B und D.**
Reproduziere aus k411 (Wolfram-exakt) den ersten Feldgrad, in dem B (gerades l_k²) und D (ungerades l_k²) auftreten. Eine einzige F₄-irreduzible Darstellung lebt in **einem** homogenen Tensorgrad; kann sie B und D zugleich tragen, nur wenn beide im selben Grad liegen.

**Datenwert:** D/B = 1.0085 ± 0.0010 (scharf, aus dem 4-Parameter-Fit H197/H202; k376-Yukawa bei M_Z).

## Entscheidungskriterien (vorab festgelegt)
- **K1 (eine Elter-Darstellung bindet D/B):** Die Ladungs-kovariante l_k²-Operatoralgebra hat ein **einzelnes** minimales Idempotent (eine irreduzible Komponente), dessen erzwungenes D/B den Datenwert **innerhalb 2σ** trifft, **und** B und D treten im **selben** F₄-Feldgrad auf (eine Darstellung kann beide tragen).
- **K2 (keine einzelne Elter-Darstellung — frei):** Die minimalen Idempotente erzwingen D/B nur in einer **diskreten** Menge, deren nächster Wert vom Datenwert um **≫ 2σ** abweicht (⇒ eine zweite, unabhängige Komponente nötig), **oder** B und D liegen in **verschiedenen** F₄-Feldgraden (⇒ keine einzelne F₄-Irrep kann beide tragen).

## Erwartung und Ehrlichkeit (teilweise nicht blind)
Voraussichtlich **K2 (nein)**. Das Ergebnis ist **teilweise nicht blind**: Die Grad-Trennung (B Grad 5, D Grad 4) ist aus H201 bekannt, und die Unabhängigkeit (Rang 4) aus H202. **Neu** an H204 ist die ausdrückliche Elter-/Branching-Lesart: die Ladungs-kovariante Operatoralgebra als 2-dimensionale kommutative Algebra mit genau zwei orthogonalen Idempotenten (P_up, P_down), deren einzelne „Darstellungen" nur die **diskreten** Werte D/B ∈ {0, +1, −1, ∞} erzwingen, und der quantitative Abgleich dieser diskreten Werte mit dem scharfen Datenwert 1.0085. Der analytisch feste Teil (Grad-Trennung) wird als solcher markiert; der Abgleich mit den diskreten Verzweigungswerten ist der prüfende Teil.

## Erwartete Konsequenz
Trägt K2: Keine einzelne höhere F₄-Darstellung bindet D/B; der ~0,9-%-Rest ist eine freie relative Normierung zwischen zwei unabhängigen Invarianten **verschiedenen Grades**, kein Clebsch–Gordan-Verhältnis. Das schließt auch die Elter-Route und bestätigt H202. Verbleibende Weggabeln für den Quark-Strang: Mischung-Strang oder ruhen lassen (wie β_sym nach 37 Versuchen).

## Vorwissen geprüft
- `grad_selektion_h201/` (H201/k411): B gerades l_k² zuerst Feldgrad 5; D ungerades l_k² Grad 4; C 91σ ≠ 0; D ≈ B gradübergreifend.
- `rest_frei_h202/` (H202/k412): Abbildung 8 Invariant-Kopplungen → (A,B,C,D) Rang 4; jede ≤3-Kopplungs-Basis verworfen; Rest D/B−1 = Eingabewert.
- `pup_projektor_h198/` (H198/k408): P_up = ½(1+iL_U) exakt, (iL_U)² = 1; O = 1 → D/B = 0, O = iL_U → B = 0, O = P_up → D/B = 1.
- `symmetrie_db_h197/` (H197): keine Symmetrie erzwingt D = B; Daten D/B = 1,009 ± 0,001; {0, ⅓, −1} bei Δχ² ≈ 6·10⁴.
- `schwingungen_h184/` (H184), `lepton_kopplung_h203/` (H203): Farb-/farblos-Zerlegung.

## Werkzeuge
Python (numpy) für die Farbblock-Operatoralgebra und die Idempotente; sympy für die Grad-Zerlegung; **Wolfram Language** als unabhängige exakte Gegenkontrolle der Idempotent-Algebra ((iL_U)² = 1, Orthogonalität/Vollständigkeit P_up + P_down = 1, Spuren/Ränge) und der diskreten D/B-Werte.
