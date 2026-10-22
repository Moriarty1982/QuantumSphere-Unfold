import QSFormal.StateDisk
import QSFormal.ClockBound
import QSFormal.Entropy
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# Konvention F

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`, Stand `main` am 2026-10-22:
Konvention F (`subsec:v490-r22-rule`), Theoremlet v4.9.0-r22.1 und die Ergänzungen
(F5)–(F7) aus v4.9.0-r24.

* Skalar: `x ↦ 1/x` vertauscht `p₊` und `p₋` und kehrt das Vorzeichen von `γ` um; jede
  symmetrische Funktion von `(p₊, p₋)` ist frame-frei, das Verhältnis `p₋/p₊` nicht.
* Matrizen: `J_B = σ_x` dreht `b₁ ↦ −b₁` (Materie ↔ Tachyon) und vertauscht die
  `σ_z`-Eigenkanäle, lässt aber Kompensator- und Partnerport fest (`σ_x C σ_x = C`); die Ports
  vertauscht `T = σ_z`. `A R_α A = cos α · A`.
* r24: `C: z ↦ −z` lässt `s` fest (24.1), `tanh(z + iπ/2) = coth z` (24.2),
  `|b_R|/|b_M| = cosh 2η` mit `R` als reinem Zustand der Entropie `0` (24.3).
-/

namespace QSFormal.Frames

open Matrix Real QSFormal.Doublet QSFormal.StateDisk

/-! ## Konvention F skalar: `x ↦ 1/x` -/

section scalar

open QSFormal.ClockBound

variable {x : ℝ}

theorem pPlus_inv (hx : 0 < x) : pPlus (1 / x) = pMinus x := by
  simp only [pPlus, pMinus]; field_simp; ring

theorem pMinus_inv (hx : 0 < x) : pMinus (1 / x) = pPlus x := by
  simp only [pPlus, pMinus]; field_simp; ring

theorem γ_inv (hx : 0 < x) (hx1 : x ≠ 1) : γ (1 / x) = -γ x := by
  have h1 : 1 - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hx1)
  have h2 : x - 1 ≠ 0 := sub_ne_zero.mpr hx1
  simp only [γ]; field_simp; ring

/-- (F1): eine Größe, die nur von den ungeordneten Eigenwerten abhängt, ist frame-frei. -/
theorem symmetric_frame_free (f : ℝ → ℝ → ℝ) (hf : ∀ a b, f a b = f b a) (hx : 0 < x) :
    f (pPlus (1 / x)) (pMinus (1 / x)) = f (pPlus x) (pMinus x) := by
  rw [pPlus_inv hx, pMinus_inv hx, hf]

/-- Das Verhältnis `p₋/p₊` ist `x` in M und `1/x` in T, also nur Materie (`Ω_M`). -/
theorem ratio (hx : 0 < x) : pMinus x / pPlus x = x ∧ pMinus (1 / x) / pPlus (1 / x) = 1 / x := by
  constructor <;> simp only [pPlus, pMinus] <;> field_simp

end scalar

/-! ## Konvention F auf dem Dublett -/

theorem J_B_fixes_C : σx * C * σx = C := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, C, mul_apply, Fin.sum_univ_two]

theorem J_B_fixes_A : σx * A * σx = A := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, A, mul_apply, Fin.sum_univ_two]

theorem T_swaps_ports : σz * C * σz = A := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σz, C, A, mul_apply, Fin.sum_univ_two] <;> norm_num

theorem ρ_eq (b₁ b₂ : ℝ) : ρ b₁ b₂ = !![(1 + b₁) / 2, b₂ / 2; b₂ / 2, (1 - b₁) / 2] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [ρ, σz, σx] <;> ring

/-- Inhalt des Kompensatorports: `tr(ρ C_HC) = ½(1 + b₂)`, die `σ_x`-Komponente. -/
theorem port_C (b₁ b₂ : ℝ) : (ρ b₁ b₂ * C).trace = (1 + b₂) / 2 := by
  simp [ρ, σz, σx, C, trace, mul_apply, Fin.sum_univ_two]; ring

theorem port_A (b₁ b₂ : ℝ) : (ρ b₁ b₂ * A).trace = (1 - b₂) / 2 := by
  simp [ρ, σz, σx, A, trace, mul_apply, Fin.sum_univ_two]; ring

/-- `J_B` bildet `ρ(b₁, b₂)` auf `ρ(−b₁, b₂)` ab. -/
theorem J_B_ρ (b₁ b₂ : ℝ) : σx * ρ b₁ b₂ * σx = ρ (-b₁) b₂ := by
  rw [ρ_eq, ρ_eq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, mul_apply, Fin.sum_univ_two]
  ring

theorem T_ρ (b₁ b₂ : ℝ) : σz * ρ b₁ b₂ * σz = ρ b₁ (-b₂) := by
  rw [ρ_eq, ρ_eq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [σz, mul_apply, Fin.sum_univ_two] <;> ring

/-- `J_B` ändert den Inhalt von Kompensator- und Partnerport nicht. -/
theorem J_B_port (b₁ b₂ : ℝ) :
    (ρ (-b₁) b₂ * C).trace = (ρ b₁ b₂ * C).trace ∧ (ρ (-b₁) b₂ * A).trace = (ρ b₁ b₂ * A).trace := by
  simp [port_C, port_A]

/-- `T` vertauscht die Inhalte von Kompensator- und Partnerport. -/
theorem T_port (b₁ b₂ : ℝ) : (ρ b₁ (-b₂) * C).trace = (ρ b₁ b₂ * A).trace := by
  rw [port_C, port_A]; ring

/-- `J_B` vertauscht die Gewichte der `σ_z`-Eigenkanäle `½(1 ± b₁)`, also Materie und Tachyon. -/
theorem J_B_channels (b₁ b₂ : ℝ) : ρ (-b₁) b₂ 0 0 = ρ b₁ b₂ 1 1 ∧ ρ (-b₁) b₂ 1 1 = ρ b₁ b₂ 0 0 := by
  simp [ρ_eq]; ring

/-- Spur und Determinante, also das ungeordnete Spektrum, sind unter `J_B` und `T` fest. -/
theorem spectrum_fixed (b₁ b₂ : ℝ) :
    (ρ (-b₁) b₂).det = (ρ b₁ b₂).det ∧ (ρ b₁ (-b₂)).det = (ρ b₁ b₂).det := by
  simp [det_ρ]

/-! ### Portachse je Frame

Ein Portpaar ist ein Paar komplementärer Projektionen `½(1 ± n₁σ_z ± n₂σ_x)` mit `|n| = 1`,
also `ρ n₁ n₂` und `ρ (−n₁) (−n₂)`. `C_HC` und `A` sind das Paar zur Achse `n = (0, 1)`, die
Kanäle `½(1 ± b₁)` das Paar zur Achse `(1, 0)`. Ob `J_B` ein Portpaar vertauscht oder festlässt,
hängt allein an der Achse. -/

/-- `J_B` vertauscht die Ports der Achse `n` genau dann, wenn `n₂ = 0` (Achse `σ_z`). -/
theorem J_B_swaps_iff (n₁ n₂ : ℝ) : σx * ρ n₁ n₂ * σx = ρ (-n₁) (-n₂) ↔ n₂ = 0 := by
  rw [J_B_ρ]
  constructor
  · intro h
    have := congrArg (· 0 1) h
    simp [ρ_eq] at this
    linarith
  · rintro rfl; simp

/-- `J_B` lässt die Ports der Achse `n` genau dann fest, wenn `n₁ = 0` (Achse `σ_x`). -/
theorem J_B_fixes_iff (n₁ n₂ : ℝ) : σx * ρ n₁ n₂ * σx = ρ n₁ n₂ ↔ n₁ = 0 := by
  rw [J_B_ρ]
  constructor
  · intro h
    have := congrArg (· 0 0) h
    simp [ρ_eq] at this
    linarith
  · rintro rfl; simp

/-- `C_HC` ist das Portpaar zur Achse `σ_x`. -/
theorem C_axis : ρ 0 1 = C ∧ ρ 0 (-1) = A := by
  constructor <;> rw [ρ_eq] <;> ext i j <;> fin_cases i <;> fin_cases j <;> simp [C, A]

/-- `A R_α A = cos α · A`, wie `C_HC R_α C_HC = cos α · C_HC`. -/
theorem A_R_A (α : ℝ) : A * R α * A = cos α • A := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A, R, mul_apply, Fin.sum_univ_two] <;> ring

/-! ## r24 -/

/-- r24.1: `C: z ↦ −z` lässt `s` fest; die Sektoren hängen am Vorzeichen von `s`, nicht an
der Orientierung. -/
theorem C_conj (E B : Fin 3 → ℝ) : sRe (-E) (-B) = sRe E B ∧ sIm (-E) (-B) = sIm E B := by
  simp [sRe, sIm]

/-- r24.2: `tanh(z + iπ/2) = coth z`; mit `z = −η` also `tanh(−η + iπ/2) = −coth η`. -/
theorem tanh_add_pi_div_two_I (z : ℂ) :
    Complex.tanh (z + (π / 2 : ℂ) * Complex.I) = Complex.cosh z / Complex.sinh z := by
  rw [Complex.tanh_eq_sinh_div_cosh, Complex.sinh_add, Complex.cosh_add, Complex.sinh_mul_I,
    Complex.cosh_mul_I, Complex.sin_pi_div_two, Complex.cos_pi_div_two]
  simp [mul_div_mul_right _ _ Complex.I_ne_zero]

/-- r24.3: der Umrechnungsfaktor von M nach R ist `|b_R|/|b_M| = 1/sech 2η = cosh 2η`; R selbst
(`η = 0`) ist der reine Zustand `|b| = 1` mit Entropie `0`. -/
theorem reference_frame (η : ℝ) :
    1 / (1 / cosh (2 * η)) = cosh (2 * η) ∧ 1 / cosh (2 * 0) = 1 ∧ QSFormal.Entropy.S 0 = 0 := by
  refine ⟨by rw [one_div_one_div], by simp, QSFormal.Entropy.S_zero⟩

end QSFormal.Frames
