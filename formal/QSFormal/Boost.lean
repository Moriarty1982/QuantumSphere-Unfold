import QSFormal.StateDisk

/-!
# Boosts des Dubletts

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`:

* Theoremlet v4.9.0-r04.2 (c): ein Boost lässt `s` unverändert und ändert `u`, also
  bewegt sich `b = (Re s, Im s)/(2u)` entlang seiner eigenen Richtung.
* Theoremlet v4.9.0-r03.3: das Frame mit `E ∥ B` bewegt sich entlang `E × B` mit
  `v/(1+v²) = |E × B|/(2u)`; mit `v = tanh η_f` ist das `tanh 2η_f = |E × B|/u`, und die
  Sichtbarkeit ist `|b| = 1/cosh 2η_f`.

Der Boost ist der Standardboost entlang der x-Achse mit `c = 1`; die Lorentzbedingung steht
als Hypothese `γ²(1 − v²) = 1`. Für andere Richtungen kommt die Drehinvarianz von `s` und `u`
dazu (`dot_rot`). Dass zu jedem nichtnullen Feld ein solches `η_f` existiert, wird hier nicht
gezeigt; die Sätze setzen es voraus.
-/

namespace QSFormal.Boost

open Matrix Real QSFormal.StateDisk

variable (v γ : ℝ) (E B : Fin 3 → ℝ)

/-- `E'` unter einem Boost entlang x. -/
def boostE : Fin 3 → ℝ := ![E 0, γ * (E 1 - v * B 2), γ * (E 2 + v * B 1)]

/-- `B'` unter einem Boost entlang x. -/
def boostB : Fin 3 → ℝ := ![B 0, γ * (B 1 + v * E 2), γ * (B 2 - v * E 1)]

variable {v γ}

/-! ## r04.2 (c): `s` ist invariant, `b` bewegt sich radial -/

theorem sRe_boost (hγ : γ ^ 2 * (1 - v ^ 2) = 1) :
    sRe (boostE v γ E B) (boostB v γ E B) = sRe E B := by
  simp [sRe, boostE, boostB, dotProduct, Fin.sum_univ_three]
  linear_combination (E 1 ^ 2 + E 2 ^ 2 - B 1 ^ 2 - B 2 ^ 2) * hγ

theorem sIm_boost (hγ : γ ^ 2 * (1 - v ^ 2) = 1) :
    sIm (boostE v γ E B) (boostB v γ E B) = sIm E B := by
  simp [sIm, boostE, boostB, dotProduct, Fin.sum_univ_three]
  linear_combination (E 1 * B 1 + E 2 * B 2) * hγ

/-- Der Bloch-Vektor nach dem Boost ist der alte, gestreckt um `u/u'`. -/
theorem bloch_boost (hγ : γ ^ 2 * (1 - v ^ 2) = 1) (hu : u E B ≠ 0) :
    let u' := u (boostE v γ E B) (boostB v γ E B)
    sRe (boostE v γ E B) (boostB v γ E B) / (2 * u') = (u E B / u') * (sRe E B / (2 * u E B)) ∧
    sIm (boostE v γ E B) (boostB v γ E B) / (2 * u') = (u E B / u') * (sIm E B / (2 * u E B)) := by
  intro u'
  rw [sRe_boost E B hγ, sIm_boost E B hγ]
  constructor <;> field_simp

/-! ## Drehungen erhalten `s` und `u` -/

theorem dot_rot {Q : Matrix (Fin 3) (Fin 3) ℝ} (hQ : Qᵀ * Q = 1) (x y : Fin 3 → ℝ) :
    (Q *ᵥ x) ⬝ᵥ (Q *ᵥ y) = x ⬝ᵥ y := by
  rw [dotProduct_mulVec, ← vecMul_transpose, vecMul_vecMul, hQ, vecMul_one]

theorem s_rot {Q : Matrix (Fin 3) (Fin 3) ℝ} (hQ : Qᵀ * Q = 1) :
    sRe (Q *ᵥ E) (Q *ᵥ B) = sRe E B ∧ sIm (Q *ᵥ E) (Q *ᵥ B) = sIm E B ∧
      u (Q *ᵥ E) (Q *ᵥ B) = u E B := by
  simp [sRe, sIm, u, dot_rot hQ]

/-! ## r03.3: das Frame mit `E ∥ B` -/

/-- Liegen `E` und `B` senkrecht zur Boostrichtung (dann zeigt `E × B` entlang x) und erfüllt
`v` die Bedingung `v (E² + B²) = (1 + v²) (E × B)ₓ`, so ist nach dem Boost `E' × B' = 0`.
Der Lorentzfaktor geht nur als Gesamtfaktor `γ²` ein und wird nicht gebraucht. -/
theorem parallel_frame (hE : E 0 = 0) (hB : B 0 = 0)
    (hv : v * (E ⬝ᵥ E + B ⬝ᵥ B) = (1 + v ^ 2) * (E ⨯₃ B) 0) :
    boostE v γ E B ⨯₃ boostB v γ E B = 0 := by
  simp [crossProduct, dotProduct, Fin.sum_univ_three, hE, hB] at hv
  ext i; fin_cases i <;> simp [crossProduct, boostE, boostB, hE, hB]
  linear_combination (-γ ^ 2) * hv

/-- `v/(1 + v²) = ½ tanh 2η` für `v = tanh η`: die Bedingung von `parallel_frame` ist
`tanh 2η_f = |E × B|/u`. -/
theorem tanh_two_mul' (η : ℝ) : tanh η / (1 + tanh η ^ 2) = tanh (2 * η) / 2 := by
  have hc : cosh η ≠ 0 := (cosh_pos η).ne'
  have h2 : cosh (2 * η) ≠ 0 := (cosh_pos _).ne'
  have h3 : cosh η ^ 2 + sinh η ^ 2 ≠ 0 := by positivity
  rw [tanh_eq_sinh_div_cosh, tanh_eq_sinh_div_cosh, sinh_two_mul, cosh_two_mul]
  field_simp

/-- Sichtbarkeit `|b| = 1/cosh 2η_f`, quadriert: aus `tanh² 2η_f = |E × B|²/u²` folgt
`|s|²/(4u²) = 1/cosh² 2η_f`. -/
theorem visibility (η : ℝ) (hu : u E B ≠ 0)
    (h : tanh (2 * η) ^ 2 = ((E ⨯₃ B) ⬝ᵥ (E ⨯₃ B)) / u E B ^ 2) :
    (sRe E B ^ 2 + sIm E B ^ 2) / (4 * u E B ^ 2) = 1 / cosh (2 * η) ^ 2 := by
  have hs := u_sq_sub_det E B
  rw [det_G] at hs
  have hc : cosh (2 * η) ≠ 0 := (cosh_pos _).ne'
  have h1 : 1 - tanh (2 * η) ^ 2 = 1 / cosh (2 * η) ^ 2 := by
    rw [tanh_eq_sinh_div_cosh]
    field_simp
    linear_combination (cosh_sq (2 * η))
  rw [← h1, h]
  field_simp
  linear_combination (-4) * hs

end QSFormal.Boost
