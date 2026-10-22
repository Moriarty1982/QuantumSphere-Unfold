import QSFormal.Doublet
import Mathlib.LinearAlgebra.CrossProduct
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.DotProduct
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Arctan

/-!
# Die Zustandsscheibe des Dubletts

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`:

* Theoremlet v4.9.0-r04.2 (`subsec:v490-r04-state`): Zerlegung von `G = FᵀF`,
  `det G = |E × B|²`, `u² − det G = ¼|s|²`, daraus `|b| ≤ 1` mit Gleichheit genau für
  `E × B = 0`; Eigenwerte `½(1 ± |b|)` von `ρ = ½(1 + b₁σ_z + b₂σ_x)`; Teil (b): die
  Dualitätsdrehung dreht `b` um `2α`, `J_B` spiegelt `b₁`, `T` spiegelt `b₂`.
* Theoremlet v4.9.0-r04.3 (`subsec:v490-r04-measurement`): Energie im Kompensatorport
  `|F C_HC|² = tr(G C_HC) = u + E·B`.
* Theoremlet v4.9.0-r17.1 (`subsec:v490-r17-frame-factor`): `p₊ = 1/(1+β²)`,
  `p₋ = β²/(1+β²)`, `p₋/p₊ = β²` für `β = tanh η`; Hopf-Wert `β = 1/√3` gibt `3/4`, `1/4`
  und `γ_L = 2`. Dazu die Brücke zu r10: `1/(1+tan²α) = cos²α`.

Nicht formalisiert: `|b| = 1/cosh 2η_f` (braucht den Boost in das Frame mit `E ∥ B`, r03.3),
Teil (c) von r04.2 (Boosts) und r17.2 (Entropie, Bures-Abstand).
-/

namespace QSFormal.StateDisk

open Matrix Real QSFormal.Doublet

variable (E B : Fin 3 → ℝ)

/-- `F = [E | B] ∈ ℝ^{3×2}`. -/
def F : Matrix (Fin 3) (Fin 2) ℝ := Matrix.of fun i j => ![E i, B i] j

/-- Die Gram-Matrix `G = FᵀF`. -/
def G : Matrix (Fin 2) (Fin 2) ℝ := (F E B)ᵀ * F E B

/-- `u = ½(E² + B²)`. -/
noncomputable def u : ℝ := (E ⬝ᵥ E + B ⬝ᵥ B) / 2

/-- `Re s = E² − B²`. -/
def sRe : ℝ := E ⬝ᵥ E - B ⬝ᵥ B

/-- `Im s = 2 E·B`. -/
def sIm : ℝ := 2 * (E ⬝ᵥ B)

/-! ## r04.2: Zerlegung, Determinante, Scheibe -/

theorem G_decomp : G E B = u E B • (1 : Matrix (Fin 2) (Fin 2) ℝ)
    + (1/2 : ℝ) • (sRe E B • σz + sIm E B • σx) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [G, F, u, sRe, sIm, σz, σx, mul_apply, dotProduct, Fin.sum_univ_three] <;> ring

theorem det_G : (G E B).det = (E ⨯₃ B) ⬝ᵥ (E ⨯₃ B) := by
  simp [G, F, det_fin_two, mul_apply, crossProduct, dotProduct, Fin.sum_univ_three]; ring

theorem trace_G : (G E B).trace = 2 * u E B := by
  simp [G, F, u, trace, mul_apply, dotProduct, Fin.sum_univ_two, Fin.sum_univ_three]; ring

theorem u_sq_sub_det : u E B ^ 2 - (G E B).det = (sRe E B ^ 2 + sIm E B ^ 2) / 4 := by
  rw [det_G]
  simp [u, sRe, sIm, crossProduct, dotProduct, Fin.sum_univ_three]; ring

/-- `|s|² ≤ 4u²`, also `|b| ≤ 1` für `b = (Re s, Im s)/(2u)`. -/
theorem s_sq_le : sRe E B ^ 2 + sIm E B ^ 2 ≤ 4 * u E B ^ 2 := by
  have h := u_sq_sub_det E B
  have hc : 0 ≤ (E ⨯₃ B) ⬝ᵥ (E ⨯₃ B) :=
    Finset.sum_nonneg fun i _ => mul_self_nonneg _
  rw [det_G] at h
  linarith

/-- Gleichheit `|b| = 1` genau dann, wenn `E × B = 0`. -/
theorem s_sq_eq_iff : sRe E B ^ 2 + sIm E B ^ 2 = 4 * u E B ^ 2 ↔ E ⨯₃ B = 0 := by
  have h := u_sq_sub_det E B
  rw [det_G] at h
  rw [← dotProduct_self_eq_zero]
  constructor <;> intro h' <;> linarith

/-! ## Eigenwerte von `ρ = ½(1 + b₁σ_z + b₂σ_x)` -/

/-- Die Zustandsmatrix zum Bloch-Vektor `(b₁, b₂)`. -/
noncomputable def ρ (b₁ b₂ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  (1/2 : ℝ) • (1 + b₁ • σz + b₂ • σx)

theorem trace_ρ (b₁ b₂ : ℝ) : (ρ b₁ b₂).trace = 1 := by
  simp [ρ, σz, σx, trace, Fin.sum_univ_two]; ring

theorem det_ρ (b₁ b₂ : ℝ) : (ρ b₁ b₂).det = (1 - (b₁ ^ 2 + b₂ ^ 2)) / 4 := by
  simp [ρ, σz, σx, det_fin_two]; ring

/-- `½(1 ± |b|)` sind Eigenwerte: `det(ρ − λ) = 0`. -/
theorem eigenvalues (b₁ b₂ : ℝ) (s : ℝ) (hs : s = 1 ∨ s = -1) :
    (ρ b₁ b₂ - ((1 + s * √(b₁ ^ 2 + b₂ ^ 2)) / 2) • (1 : Matrix (Fin 2) (Fin 2) ℝ)).det = 0 := by
  have hr : √(b₁ ^ 2 + b₂ ^ 2) ^ 2 = b₁ ^ 2 + b₂ ^ 2 := sq_sqrt (by positivity)
  have hs2 : s ^ 2 = 1 := by rcases hs with rfl | rfl <;> norm_num
  simp [ρ, σz, σx, det_fin_two]
  linear_combination (s ^ 2 / 4) * hr + ((b₁ ^ 2 + b₂ ^ 2) / 4) * hs2

/-! ## r04.2 (b): Dualitätsdrehung, `J_B`, `T` auf dem Bloch-Vektor -/

/-- Eine Dualitätsdrehung `F ↦ F R_αᵀ` wirkt auf `G` als `G ↦ R_α G R_αᵀ`. -/
theorem G_rotate (α : ℝ) : (F E B * (R α)ᵀ)ᵀ * (F E B * (R α)ᵀ) = R α * G E B * (R α)ᵀ := by
  simp [G, Matrix.transpose_mul, Matrix.mul_assoc]

/-- … und dreht den spurfreien Anteil, also `b`, um `2α`. -/
theorem rotate_bloch (α b₁ b₂ : ℝ) :
    R α * (b₁ • σz + b₂ • σx) * (R α)ᵀ
      = (b₁ * cos (2 * α) - b₂ * sin (2 * α)) • σz
        + (b₁ * sin (2 * α) + b₂ * cos (2 * α)) • σx := by
  rw [cos_two_mul, sin_two_mul]
  ext i j; fin_cases i <;> fin_cases j <;> simp [R, σz, σx, mul_apply, Fin.sum_univ_two]
  · linear_combination (-b₁) * sin_sq_add_cos_sq α
  · linear_combination (-b₂) * sin_sq_add_cos_sq α
  · linear_combination (-b₂) * sin_sq_add_cos_sq α
  · linear_combination b₁ * sin_sq_add_cos_sq α

/-- `J_B` spiegelt `b₁ ↦ −b₁`. -/
theorem J_B_bloch (b₁ b₂ : ℝ) : σx * (b₁ • σz + b₂ • σx) * σx = (-b₁) • σz + b₂ • σx := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σz, σx, mul_apply, Fin.sum_univ_two]

/-- `T` spiegelt `b₂ ↦ −b₂`. -/
theorem T_bloch (b₁ b₂ : ℝ) : σz * (b₁ • σz + b₂ • σx) * σz = b₁ • σz + (-b₂) • σx := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σz, σx, mul_apply, Fin.sum_univ_two]

/-! ## r04.3: Energie im Kompensatorport -/

theorem port_energy : ((F E B * C)ᵀ * (F E B * C)).trace = u E B + E ⬝ᵥ B := by
  simp [F, C, u, trace, mul_apply, dotProduct, Fin.sum_univ_two, Fin.sum_univ_three]; ring

/-! ## r17.1: Eigenwerte und Rapidität -/

/-- `½(1 + 1/cosh 2η) = 1/(1 + tanh²η)`. -/
theorem p_plus (η : ℝ) : (1 + 1 / cosh (2 * η)) / 2 = 1 / (1 + tanh η ^ 2) := by
  have hc : 0 < cosh η := cosh_pos η
  have h1 : cosh η ^ 2 - sinh η ^ 2 = 1 := cosh_sq_sub_sinh_sq η
  have h2 : 0 < cosh η ^ 2 + sinh η ^ 2 := by positivity
  rw [cosh_two_mul, tanh_eq_sinh_div_cosh]
  field_simp
  linear_combination (-1 : ℝ) * h1

/-- `½(1 − 1/cosh 2η) = tanh²η/(1 + tanh²η)`. -/
theorem p_minus (η : ℝ) : (1 - 1 / cosh (2 * η)) / 2 = tanh η ^ 2 / (1 + tanh η ^ 2) := by
  have hc : 0 < cosh η := cosh_pos η
  have h1 : cosh η ^ 2 - sinh η ^ 2 = 1 := cosh_sq_sub_sinh_sq η
  have h2 : 0 < cosh η ^ 2 + sinh η ^ 2 := by positivity
  rw [cosh_two_mul, tanh_eq_sinh_div_cosh]
  field_simp
  linear_combination h1

/-- `cosh 2η = (1 + β²)/(1 − β²)` mit `β = tanh η`. -/
theorem cosh_two_mul_tanh (η : ℝ) :
    cosh (2 * η) = (1 + tanh η ^ 2) / (1 - tanh η ^ 2) := by
  have hc : cosh η ^ 2 ≠ 0 := pow_ne_zero 2 (cosh_pos η).ne'
  have h1 : cosh η ^ 2 - sinh η ^ 2 = 1 := cosh_sq_sub_sinh_sq η
  rw [cosh_two_mul, tanh_eq_sinh_div_cosh, div_pow,
    show 1 - sinh η ^ 2 / cosh η ^ 2 = 1 / cosh η ^ 2 by field_simp; linarith,
    show 1 + sinh η ^ 2 / cosh η ^ 2 = (cosh η ^ 2 + sinh η ^ 2) / cosh η ^ 2 by field_simp]
  field_simp

/-- Hopf-Wert `β² = 1/3`: Eigenwerte `3/4` und `1/4`, Rahmenfaktor `(1+β²)/(1−β²) = 2`. -/
theorem hopf : 1 / (1 + (1/3 : ℝ)) = 3/4 ∧ (1/3 : ℝ) / (1 + 1/3) = 1/4
    ∧ (1 + (1/3 : ℝ)) / (1 - 1/3) = 2 := by
  norm_num

/-- Brücke r10 ↔ r17: der größere Eigenwert bei `β = tan α` ist der Anteil `cos²α`, den
eine Stufe „drehen, dann kompensieren“ behält. -/
theorem p_plus_tan (α : ℝ) (h : cos α ≠ 0) : 1 / (1 + tan α ^ 2) = cos α ^ 2 := by
  rw [tan_eq_sin_div_cos, div_pow]
  field_simp
  linear_combination (-1 : ℝ) * sin_sq_add_cos_sq α

end QSFormal.StateDisk
