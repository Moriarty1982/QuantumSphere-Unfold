import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.IntervalCases

/-!
# Das (E, B)-Dublett und seine Matrizen

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`:

* Theoremlet v4.9.0-r04.1 (`subsec:v490-r04-doublet`): `σ_x`, `σ_z` sind Spiegelungen,
  `R_α` Drehungen, `J_B R_α = R_{−α} J_B`, `R_{π/2} σ_x R_{π/2}⁻¹ = −σ_x`,
  `C_HC = ½(1+σ_x)` und `A = ½(1−σ_x)` sind orthogonale Projektionen.
* Theoremlet v4.9.0-r10.1 (`subsec:v490-r10-rotate-compensate`):
  `C_HC R_α C_HC = cos α · C_HC`, Energieanteil `cos²α` im Kompensatorport und `sin²α`
  im Partnerport, bei `α = π/6` der Faktor `3/4`, erste Stufe mit `(3/4)ⁿ ≤ 1/256` ist `n = 20`.

Bewiesen wird die Rechnung, nicht die Deutung von r10: dass der C5-Faktor von einer Drehung
um `π/6` herrührt, ist dort ausdrücklich „an interpretation … not a derivation“.
-/

namespace QSFormal.Doublet

open Matrix Real

/-- `σ_x`, im Companion `J_B`. -/
def σx : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1; 1, 0]

/-- `σ_z`, im Companion `T`. -/
def σz : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, -1]

/-- Die Dualitätsdrehung `R_α`. -/
noncomputable def R (α : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![cos α, -sin α; sin α, cos α]

/-- Der Kompensator `C_HC = ½(1 + σ_x)`. -/
noncomputable def C : Matrix (Fin 2) (Fin 2) ℝ := !![1/2, 1/2; 1/2, 1/2]

/-- Der Partner `A = ½(1 − σ_x)`. -/
noncomputable def A : Matrix (Fin 2) (Fin 2) ℝ := !![1/2, -1/2; -1/2, 1/2]

theorem C_eq : C = (1/2 : ℝ) • (1 + σx) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C, σx]

theorem A_eq : A = (1/2 : ℝ) • (1 - σx) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A, σx] <;> norm_num

/-! ## r04.1: die Erzeugenden von O(2) -/

theorem σx_orth : σxᵀ * σx = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, mul_apply, Fin.sum_univ_two]

theorem σz_orth : σzᵀ * σz = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σz, mul_apply, Fin.sum_univ_two]

theorem det_σx : σx.det = -1 := by simp [σx, det_fin_two_of]

theorem det_σz : σz.det = -1 := by simp [σz, det_fin_two_of]

theorem R_orth (α : ℝ) : (R α)ᵀ * R α = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [R, mul_apply, Fin.sum_univ_two] <;> nlinarith [sin_sq_add_cos_sq α]

theorem det_R (α : ℝ) : (R α).det = 1 := by
  simp [R, det_fin_two_of]; nlinarith [sin_sq_add_cos_sq α]

/-- `J_B R_α = R_{−α} J_B` (r02.5): Spiegelung mal Drehung. -/
theorem σx_R (α : ℝ) : σx * R α = R (-α) * σx := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, R, mul_apply, Fin.sum_univ_two]

/-- Das Enigma-Kompositum von r02.5: `R_{π/2} σ_x R_{π/2}⁻¹ = −σ_x`, mit `R_{π/2}⁻¹ = R_{−π/2}`. -/
theorem enigma : R (π/2) * σx * R (-(π/2)) = -σx := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [σx, R, mul_apply, Fin.sum_univ_two]

/-! ## Kompensator und Partner -/

theorem C_symm : Cᵀ = C := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C]

theorem A_symm : Aᵀ = A := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A]

theorem C_idem : C * C = C := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C, mul_apply, Fin.sum_univ_two] <;> norm_num

theorem A_idem : A * A = A := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A, mul_apply, Fin.sum_univ_two] <;> norm_num

theorem C_add_A : C + A = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C, A] <;> norm_num

theorem C_mul_A : C * A = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C, A, mul_apply, Fin.sum_univ_two] <;> norm_num

/-! ## r10.1: drehen, dann kompensieren -/

/-- `C_HC R_α C_HC = cos α · C_HC`. -/
theorem C_R_C (α : ℝ) : C * R α * C = cos α • C := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [C, R, mul_apply, Fin.sum_univ_two] <;> ring

/-- Nach `n` Stufen „drehen, dann kompensieren“ bleibt `cosⁿ α · C_HC`. -/
theorem stages (α : ℝ) (n : ℕ) : (C * R α) ^ n * C = cos α ^ n • C := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, mul_assoc, C_R_C, mul_smul_comm, ih, smul_smul, ← pow_succ']

/-- Ein Vektor im Bild von `C_HC`, unnormiert: `‖u‖² = 2`. -/
def u : Fin 2 → ℝ := ![1, 1]

theorem C_u : C *ᵥ u = u := by
  ext i; fin_cases i <;> simp [C, u, mulVec, dotProduct, Fin.sum_univ_two] <;> norm_num

/-- Energie im Kompensatorport nach einer Drehung: der Anteil `cos² α`. -/
theorem energy_C (α : ℝ) :
    (C *ᵥ (R α *ᵥ u)) ⬝ᵥ (C *ᵥ (R α *ᵥ u)) = cos α ^ 2 * (u ⬝ᵥ u) := by
  simp [C, R, u, mulVec, dotProduct, Fin.sum_univ_two]; ring

/-- Energie im Partnerport: der Anteil `sin² α`. -/
theorem energy_A (α : ℝ) :
    (A *ᵥ (R α *ᵥ u)) ⬝ᵥ (A *ᵥ (R α *ᵥ u)) = sin α ^ 2 * (u ⬝ᵥ u) := by
  simp [A, R, u, mulVec, dotProduct, Fin.sum_univ_two]; ring

/-! ## Der Faktor 3/4 und die Stufe n = 20 -/

theorem cos_sq_pi_div_six : cos (π / 6) ^ 2 = 3 / 4 := by
  rw [cos_pi_div_six, div_pow, sq_sqrt (by norm_num)]; norm_num

/-- Bei `α = π/6` hält jede Stufe `3/4` der Energie. -/
theorem stage_energy_pi_div_six :
    (C *ᵥ (R (π/6) *ᵥ u)) ⬝ᵥ (C *ᵥ (R (π/6) *ᵥ u)) = 3 / 4 * (u ⬝ᵥ u) := by
  rw [energy_C, cos_sq_pi_div_six]

/-- `n = 20` ist die erste Stufe mit `(3/4)ⁿ ≤ 1/256`. -/
theorem first_stage_twenty :
    ((3 : ℚ) / 4) ^ 20 ≤ 1 / 256 ∧ ∀ n < 20, 1 / 256 < ((3 : ℚ) / 4) ^ n := by
  refine ⟨by norm_num, fun n hn => ?_⟩
  interval_cases n <;> norm_num

end QSFormal.Doublet
