import QSFormal.StateDisk

/-!
# Uhrschranke je Frame und die Herleitung von 1/5

Formalisiert Theoremlet v4.9.0-r21.1 (`subsec:v490-r21-derivation`). Die Runde liegt auf
`main` (Commit `2cc7db8`), noch nicht auf dem Zweig dieses Worktrees; zitiert nach dem Stand
von `main` am 2026-10-22.

Fensterbedingung von r12: `G(1 − Δ_γ)S > 16` mit `S = N + κN(N − 1)`, also Reserve
`Δ^max = 1 − 16/(GS)`. Zustand bei `x = β²`: `γ = (1+x)/(1−x)`, `p₋ = x/(1+x)`,
`p₊ = 1/(1+x)`. Prämissen (D1)–(D5) als Definitionen:

* Materie: `G_M = γ`, `κ_M = p₋` (D1, D2);
* Tachyon: `G_T = 1`, `κ_T = p₊` (D5, D2);
* `N = 1 + 1/p₋` in beiden Frames (D3, D4).

Bewiesen: die beiden Reserveformeln, die Konsistenzbedingung `G_M S_M = G_T S_T` hat für
`0 < x < 1` genau die Lösung `x = 1/3`, dort `N = 5`, `S_M = 10`, `S_T = 20` und
`Δ_M = Δ_T = 1/5`; mit festem `N = 5` statt (D3) ebenfalls genau `x = 1/3`, also `p₋ = 1/4`.
Die Prämissen selbst, vor allem (D4) und (D5), sind Annahmen der Runde und werden hier nur
übernommen.
-/

namespace QSFormal.ClockBound

noncomputable section

variable (x : ℝ)

def γ : ℝ := (1 + x) / (1 - x)
def pMinus : ℝ := x / (1 + x)
def pPlus : ℝ := 1 / (1 + x)

/-- (D3): `N = 1 + 1/p₋`. -/
def N : ℝ := 1 + 1 / pMinus x

/-- `S = N + κN(N − 1)`. -/
def S (κ n : ℝ) : ℝ := n + κ * n * (n - 1)

/-- Überlebensreserve `1 − 16/(GS)`. -/
def reserve (G s : ℝ) : ℝ := 1 - 16 / (G * s)

def SM : ℝ := S (pMinus x) (N x)
def ST : ℝ := S (pPlus x) (N x)
def ΔM : ℝ := reserve (γ x) (SM x)
def ΔT : ℝ := reserve 1 (ST x)

variable {x}

theorem N_eq (hx : 0 < x) : N x = 2 + 1 / x := by
  simp only [N, pMinus]
  field_simp
  ring

/-- (D3) als Balance: `κ_M (N − 1) = 1`. -/
theorem balance (hx : 0 < x) : pMinus x * (N x - 1) = 1 := by
  simp only [N, pMinus]
  field_simp
  ring

theorem SM_eq (hx : 0 < x) : SM x = 2 * (1 + 2 * x) / x := by
  simp only [SM, S, N, pMinus]
  field_simp
  ring

theorem ST_eq (hx : 0 < x) : ST x = (1 + 2 * x) * (1 + x) / x ^ 2 := by
  simp only [ST, S, N, pMinus, pPlus]
  field_simp
  ring

/-- `Δ_M^max = (10x² − 5x + 1)/((1+x)(1+2x))`. -/
theorem ΔM_eq (hx : 0 < x) (hx1 : x < 1) :
    ΔM x = (10 * x ^ 2 - 5 * x + 1) / ((1 + x) * (1 + 2 * x)) := by
  have h1 : 1 - x ≠ 0 := by linarith
  simp only [ΔM, reserve, γ, SM_eq hx]
  field_simp
  ring

/-- `Δ_T^max = (1 + 3x − 14x²)/((1+x)(1+2x))`. -/
theorem ΔT_eq (hx : 0 < x) :
    ΔT x = (1 + 3 * x - 14 * x ^ 2) / ((1 + x) * (1 + 2 * x)) := by
  simp only [ΔT, reserve, ST_eq hx]
  field_simp
  ring

/-- Die Konsistenzbedingung `G_M S_M = G_T S_T` hat für `0 < x < 1` genau die Lösung
`x = 1/3`, den Hopf-Punkt. -/
theorem consistency_iff (hx : 0 < x) (hx1 : x < 1) : γ x * SM x = 1 * ST x ↔ x = 1 / 3 := by
  have h1 : 1 - x ≠ 0 := by linarith
  rw [SM_eq hx, ST_eq hx, γ, one_mul, div_mul_div_comm,
    div_eq_div_iff (by positivity) (by positivity)]
  constructor
  · intro h
    have key : (3 * x - 1) * (x * (1 + x) * (1 + 2 * x)) = 0 := by linear_combination h
    rcases mul_eq_zero.mp key with h3 | h3
    · linarith
    · exfalso; have : 0 < x * (1 + x) * (1 + 2 * x) := by positivity
      linarith
  · rintro rfl; norm_num

/-- Am Hopf-Punkt: `N = 5`, `S_M = 10`, `S_T = 20`, `Δ_M = Δ_T = 1/5`. -/
theorem hopf : N (1/3) = 5 ∧ SM (1/3) = 10 ∧ ST (1/3) = 20 ∧ ΔM (1/3) = 1/5 ∧ ΔT (1/3) = 1/5 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [N_eq (by norm_num)]; norm_num
  · rw [SM_eq (by norm_num)]; norm_num
  · rw [ST_eq (by norm_num)]; norm_num
  · rw [ΔM_eq (by norm_num) (by norm_num)]; norm_num
  · rw [ΔT_eq (by norm_num)]; norm_num

/-- Ohne (D3), mit `N = 5` fest: wieder genau `x = 1/3`. -/
theorem consistency_fixed_N_iff (hx : 0 < x) (hx1 : x < 1) :
    γ x * S (pMinus x) 5 = 1 * S (pPlus x) 5 ↔ x = 1 / 3 := by
  have h1 : 1 - x ≠ 0 := by linarith
  have h2 : 1 + x ≠ 0 := by linarith
  simp only [γ, S, pMinus, pPlus, one_mul]
  constructor
  · intro h
    field_simp at h
    have key : (3 * x - 1) * (x + 2) = 0 := by linear_combination h / 2
    rcases mul_eq_zero.mp key with h3 | h3 <;> linarith
  · rintro rfl; norm_num

/-- Dieselbe Bedingung in `p₋`: `4p₋² − 9p₋ + 2 = 0`, zulässig (`0 ≤ p₋ < ½`) nur `p₋ = 1/4`. -/
theorem quadratic_p (p : ℝ) (hp : 0 ≤ p) (hp1 : p < 1 / 2) :
    4 * p ^ 2 - 9 * p + 2 = 0 ↔ p = 1 / 4 := by
  constructor
  · intro h
    have key : (4 * p - 1) * (p - 2) = 0 := by linear_combination h
    rcases mul_eq_zero.mp key with h3 | h3 <;> linarith
  · rintro rfl; norm_num

theorem pMinus_hopf : pMinus (1/3) = 1 / 4 := by norm_num [pMinus]

end

end QSFormal.ClockBound
