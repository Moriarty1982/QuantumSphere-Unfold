# Vorab-Notiz H51: Cartan-Test des ϑ-geeichten OP5-Symbols

Festgeschrieben vor der Rechnung (3. November 2026). Betrifft nur das OP5-Vergleichsmodell, nicht das QSC-Modell. OP5
bleibt offen.

## Ausgangslage (r71, Erkundung k136)

- Die ϑ-Richtung ist eine exakte Eichsymmetrie, δΨ = f·∂_ϑΨ (Ergebnis H50).
- **Eichung (k136, Erkundung):** Der Eichvektor v = ∂_ϑΨ am Keim ist gemeinsamer Kern aller vier Blöcke von J
  (kleinster Singulärwert 5,5e-15 gegen nächsten 0,13); alle Ω-Blöcke stehen senkrecht auf v (1,6e-14).
  Als Eichbedingung dient die algebraische Bedingung s(Ψ) = S(x) mit s = j² = Ψ†K₂Ψ, einer Komponente des Stroms
  (|ds·v|/|ds| = 0,45, größter Wert unter den Bilinearen Ψ†Ψ, Ψ†K_aΨ, Ψ†Q_aΨ, Ψ†(I⊗β)Ψ). Ψ†(Z⊗β)Ψ ist durch g
  festgelegt und erwartungsgemäß blind (3,7e-16). Weil ds·v ≠ 0 ist, legt die Bedingung f lokal eindeutig fest.
- Auf Symbolebene ist jede transversale algebraische Eichung gleichwertig: g'_p ≅ g_p/(S^p ⊗ v). Das Ergebnis hängt also
  nicht von der Wahl von s ab.
- Gemessen (k136, saubere Lücken ≥ 1,5e-8 gegen ≤ 6,2e-16): g'_p = g_p − C(p+3, 3) für p = 2…7, also
  117, 188, 273, 371, 481, 606; mit den Werten aus der Erkundung folgen 745, 898, 1065 für p = 8, 9, 10.

## Hypothese

Ab p = 6 ist g'_p ein Polynom zweiten Grades, g'_p = 481 + 125(p − 6) + 7(p − 6)(p − 5); bei p = 5 nicht (Polynom 356,
gemessen 371). Ein involutives Symbol der Ordnung q hat ab q eine polynomiale Dimensionsfunktion. Daher:

**H51:** Das ϑ-geeichte, Ω-erweiterte Symbol g' besteht den Cartan-Test erstmals bei p = 6. Es ist nicht involutiv bei
p = 5 und involutiv bei p = 6.

## Rechnung

- g'_p ⊂ S^p(ℝ⁴)* ⊗ ℝ²⁴ aus `matrix(p)` von `balanced_spencer_check.py` (J und θ aus `completion-omega-witness.npz`) plus
  den Eichzeilen w ⊗ x^α für alle |α| = p, w = ds normiert (`k136_eichdaten.npy`).
- In drei zufälligen orthonormalen Koordinatensystemen (Seeds 1, 2, 3) wird
  g'^{(k)}_p = {u ∈ g'_p : ι(e₁)u = … = ι(e_k)u = 0} für k = 0…3 bestimmt, ι(e) = Ableitung in Richtung e.
- Cartan-Test: Es gilt immer dim g'_{p+1} ≤ Σ_{k=0}^{3} dim g'^{(k)}_p. Gleichheit (in generischen Koordinaten)
  bedeutet, dass g'_p involutiv ist.
- Ränge werden an der größten Singulärwertlücke oberhalb von 1e-14 (relativ) abgelesen. Eine Lücke gilt als sauber, wenn
  das Verhältnis ≥ 1e4 ist.

## Kriterium

- **Bestätigt:** Gleichheit bei p = 6 und strikte Ungleichheit bei p = 5, in allen drei Koordinatensystemen.
- **Teilweise:** Gleichheit erst bei p = 7 oder p = 8 (Hilbert-Arithmetik richtig, Involution später).
- **Widerlegt:** Keine Gleichheit bis p = 8, oder Gleichheit schon bei p ≤ 5 (Widerspruch zur gemessenen
  Dimensionsfunktion).
- **Ungültig:** keine saubere Lücke in einem verwendeten Rang, oder die drei Koordinatensysteme widersprechen sich.

## Kontrollen

- Die Ungleichung dim g'_{p+1} ≤ Σ_k dim g'^{(k)}_p muss überall gelten; eine Verletzung macht den Lauf ungültig.
- dim g'^{(0)}_p muss mit den oben genannten Werten übereinstimmen.

## Grenzen

- θ stammt vom älteren Keim (Abweichung etwa 1e-7). Getestet wird nur das Symbol, keine formale Integrabilität: ob das
  geeichte System bis Ordnung 6 ohne weitere Integrabilitätsbedingungen auskommt (H^{5,2} nach Eichung), bleibt eine
  eigene Frage.
- Auch ein bestätigtes H51 ist kein Existenzsatz für das QSC-Modell.
