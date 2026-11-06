# Vorab-Notiz H95: Machbarkeit von I3 mit dynamischem Zweig-Gas (Variante A) auf FRW

**Stand:** 6. November 2026, vor der Rechnung festgelegt. Autor (6.11.): „Ja, H95 rechnen“ (Variante A aus `Vorschlag_Zweigmodell_FRW.md`). **Nicht blind:** Die kosmologischen Eckdaten sind bekannt, und eine analytische Überlegung (unten) lässt eine Widerlegung erwarten. Der Test prüft nur die Machbarkeit.

## Vorwissen geprüft
- `Erkundung_I3_mit_T_Zweig.md`: Mit festen Gewichten ist die Mischung ein Fluid mit konstantem w, an der CMB ausgeschlossen.
- `Vorschlag_Zweigmodell_FRW.md`: Varianten A–C, Empfehlung A.
- k182/k183 (Zweige, Gewichte a·T_M + b·T_T), I4 (Schwelle k = m).
- H76 (Vakuumzerfall, nicht Teil dieses Tests).
- Autorentscheidung „T-Zweig zulassen“.
- Kosmologische Eckwerte aus Vorwissen, nicht nachgeschlagen: Ω_b = 0,049, Ω_r = 9,1·10⁻⁵, Rekombination bei z = 1090, dort ρ_c/ρ_b ≈ 5,4, heute Ω_Λ ≈ 0,69.

## Modell (festgelegt)
Flaches FRW, Skalenfaktor heute 1, Dichten in Einheiten der kritischen Dichte heute. Bestandteile:
- Strahlung Ω_r·a⁻⁴ und Baryonen Ω_b·a⁻³; keine weitere kalte dunkle Materie, kein Λ.
- **Zweig-Gas:** gleiche Teilchenzahl n ∝ a⁻³ in beiden Zweigen, frei strömend.
  - Normaler Zweig (Gewicht 1): k₁ = m·κ₁/a, ω₁ = m√(1 + (κ₁/a)²), ρ = Ω_D·a⁻³·ω₁/m, p = Ω_D·a⁻³·(κ₁/a)²/(3ω₁/m).
  - T-Zweig (Gewicht r = b/a, negative Energie): k₂ = m·a_th/a, ω₂ = m√((a_th/a)² − 1), ρ_T = −r·Ω_D·a⁻³·ω₂/m, p_T = −r·Ω_D·a⁻³·(a_th/a)²/(3ω₂/m).
- Entstehung bei gemeinsamer Rapidität verlangt κ₁ < a_th. Ω_D folgt aus der Flachheit heute (Gesamtdichte 1).
- Parameter: r ∈ [0,1; 5], a_th ∈ (1; 100] (logarithmisch), κ₁/a_th ∈ [0; 0,999].

## Hypothese und Kriterien
- **H95a:** Es gibt Parameter mit (P) Gesamtdichte > 0 für alle a ∈ [10⁻⁸; 1] und Ω_D > 0, (i) (ρ_Gas/ρ_b) bei z = 1090 im Bereich [4,32; 6,48], (ii) w_eff heute (gesamt) im Bereich [−0,8; −0,6], (iii) a_th > 1 (gilt nach Konstruktion).
- **H95b:** Falls ja, ist der Bereich in a_th bei festem r mindestens 10 % breit.
- **Widerlegt**, wenn auf einem Gitter von mindestens 60 × 60 × 40 Punkten kein Punkt (P), (i) und (ii) erfüllt. Ein feineres Gitter wird nur zur Bestätigung eines Treffers genutzt.

## Analytische Erwartung (offengelegt)
Früh ist der T-Zweig negative Strahlung mit ρ_T ≈ −r·Ω_D·a_th·a⁻⁴. Die Positivität (P) verlangt, dass normale Strahlung sie aufhebt: entweder der normale Zweig selbst (κ₁ nahe a_th, dann aber wird er erst nahe a_th kalt, also keine dunkle Materie zur Rekombination) oder die Photonen (dann ist r·Ω_D·a_th ≲ Ω_r, und die heutige Spannung ist von der Ordnung Ω_r, außer a_th liegt extrem nahe bei 1). Erwartung: **H95a widerlegt**.
