# Vorab-Notiz H56: Cartan-Test des um die vier Bedingungen erweiterten Symbols

Festgeschrieben vor der Rechnung (3. November 2026). Betrifft nur das OP5-Vergleichsmodell. OP5 bleibt offen.

## Ausgangslage

- H51: Das ϑ-geeichte Symbol g' (J, θ, Eichung) ist ab p = 6 involutiv; dim g'_6 = 481.
- H55 und Erkundung `Erkundung_vier_Bedingungen_6Jets.md`: Es gibt vier versteckte Gleichungen sechster Ordnung. Auf g'_6
  haben sie Rang 4; das vollständige Symbol bei Ordnung 6 hat 477 Dimensionen.

## Objekt

- σ_k (k = 1…4): der c₆-Anteil der Vektoren in `k144_bedingungen_p1.npy`, als Kovektoren auf S⁶ ⊗ ℝ²⁴ in ausgeglichenen
  Koordinaten (gleiche Konvention wie `balanced_spencer_check.py`), umsortiert auf die Reihenfolge `idx(6)`.
- g''_p = {u ∈ g'_p : σ_k(∂^γ u) = 0 für alle |γ| = p − 6, k = 1…4}, g'_p wie in H51 (`k137_cartan_test.py`).
- Cartan-Test wie in H51: drei zufällige orthonormale Koordinatensysteme (Seeds 1, 2, 3), Vergleich von
  dim g''_{p+1} mit Σ_{k=0}^{3} dim g''^{(k)}_p, für p = 6, 7, 8.

## Hypothese H56

Das erweiterte Symbol wird bis spätestens p = 8 involutiv. Berichtet wird die erste Ordnung, bei der der Test besteht.

## Kriterium

- **Bestätigt:** Gleichheit bei einem p ∈ {6, 7, 8}, in allen drei Koordinatensystemen.
- **Widerlegt:** Bei p = 6, 7, 8 überall strikte Ungleichheit.
- **Ungültig, wenn:**
  - dim g''_6 ≠ 477 (die Bedingungen passen dann nicht zum gespeicherten Symbol);
  - oder der größte Hauptwinkel-Sinus zwischen der Faser G₆ des echten Keims (`k144`, Dimension 481) und g'_6 aus dem
    gespeicherten Symbol über 1e-5 liegt;
  - oder ein verwendeter Rang keine Lücke ≥ 1e4 hat, oder die drei Koordinatensysteme sich widersprechen, oder die
    Ungleichung dim g''_{p+1} ≤ Σ verletzt ist.

## Grenzen

- Nur das Symbol. Ob das erweiterte System formal integrabel ist, ist eine eigene Frage (nächster Test).
- σ_k stammen vom ersten Grundpunkt; ihr Symbolteil hängt nur vom Jet bis Grad 3 ab.
- θ vom älteren Keim (1e-7).
