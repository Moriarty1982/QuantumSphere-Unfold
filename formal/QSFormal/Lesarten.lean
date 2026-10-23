import QSFormal.Dixon

/-!
# Readout-abhängige Lesarten des ℂ-Faktors und der ℍ-Faktor

Autoridee (2026-10-23): Der ℂ-Faktor der Dixon-Ablage ist je nach Readout Dualitätsebene (J_B), quantenmechanisches `i`
(Ladungskonjugation C), Lorentz-Komplexifizierung (Drehung → Boost) oder Uhrphase. Alle vier benutzen Operationen
derselben Ebene: Drehungen `z ↦ wz`, die Vierteldrehung `R : z ↦ iz`, die Spiegelungen `z ↦ z̄` (C, T) und
`J_B = R ∘ T : z ↦ i z̄` (v4.9.0-r30.2(b)).

Bewiesen (über `Int`, ohne Mathlib):
* `jB_clock`: `J_B R_w J_B = R_{w̄}` — im Tachyon-Frame läuft die Uhrphase rückwärts.
* `conj_jB_anti`, `conj_jB_quad`: C (= T auf dem ℂ-Faktor) und J_B antikommutieren auf Amplituden, auf quadratischen
  Readouts vertauschen sie.
* `d4_*`: Unter den ganzzahligen orthogonalen 2×2-Matrizen mit Einträgen in {−1, 0, 1} sind genau die 8 aus `d4`
  orthogonal; sie bilden die Achsen (das a-Etikett Materie/Tachyon) auf Achsen ab. Eine allgemeine Uhrdrehung tut das
  nicht (`clock_mixes`). Damit ist die Aussage „auf ℂ verträglich, weil alles in O(2) liegt“ zu korrigieren: verträglich
  mit dem a-Etikett sind nur Viertelschritte und Spiegelungen.
* ℍ: Links- und Rechtsmultiplikation vertauschen (`LR_comm`). Die Konjugation mit `(1+i+j+k)` bzw. `i` erzeugt die
  beiden Erzeuger der A₄ aus `Dixon.lean` (`conj_cyc`, `conj_i`). Linksmultiplikation (Spinor/Lorentz) bildet Im ℍ aus sich
  heraus ab (`left_leaves_im`) und verteilt Platznormen um (`left_moves_norms`); invariant ist die quaternionische
  Gram-Größe `conj(qx)(qy) = |q|² conj(x) y` (`gram_left`).
* K77.10: Die drei Imaginärkomponenten dieser Gram-Größe sind links-invariante Etiketten auf der rechten Seite. Für ein
  reines Tripel ist die `i`-Komponente das Keilprodukt `x_j ∧ x_k` (`gram_pure`), ihr Quadrat-Integral
  `2(|x_j|²|x_k|² − ⟨x_j,x_k⟩²)` (`lagrange8`); rechts mit `1+i+j+k` werden die Etiketten zyklisch vertauscht (`right_cyc`).
-/

namespace QSFormal.Lesarten
open QSFormal.Dixon

/-! ## Die Ebene des ℂ-Faktors -/

structure Z where
  (x y : Int)
  deriving DecidableEq, Repr

namespace Z
def conj (z : Z) : Z := ⟨z.x, -z.y⟩
def rot (z : Z) : Z := ⟨-z.y, z.x⟩
def jB (z : Z) : Z := rot (conj z)
def neg (z : Z) : Z := ⟨-z.x, -z.y⟩
/-- Drehung (Uhrphase) als Multiplikation mit `w`. -/
def mulW (w z : Z) : Z := ⟨w.x * z.x - w.y * z.y, w.x * z.y + w.y * z.x⟩
/-- Quadratischer Readout: die Einträge von `z zᵀ`. -/
def quad (z : Z) : Int × Int × Int := (z.x * z.x, z.x * z.y, z.y * z.y)
end Z

theorem jB_eq (z : Z) : Z.jB z = ⟨z.y, z.x⟩ := by
  obtain ⟨x, y⟩ := z; simp [Z.jB, Z.rot, Z.conj]

theorem rot_sq (z : Z) : Z.rot (Z.rot z) = Z.neg z := by
  obtain ⟨x, y⟩ := z; simp [Z.rot, Z.neg]

theorem jB_invol (z : Z) : Z.jB (Z.jB z) = z := by
  obtain ⟨x, y⟩ := z; simp [Z.jB, Z.rot, Z.conj]

/-- Aussage 2: `J_B R_w J_B = R_{w̄}`, die Uhrphase läuft im Tachyon-Frame rückwärts. -/
theorem jB_clock (w z : Z) : Z.jB (Z.mulW w (Z.jB z)) = Z.mulW (Z.conj w) z := by
  obtain ⟨a, b⟩ := w; obtain ⟨x, y⟩ := z
  simp only [Z.jB, Z.rot, Z.conj, Z.mulW, Z.mk.injEq]; constructor <;> grind

/-- Aussage 3a: Auf Amplituden antikommutieren C (= `conj`) und J_B. -/
theorem conj_jB_anti (z : Z) : Z.conj (Z.jB z) = Z.neg (Z.jB (Z.conj z)) := by
  obtain ⟨x, y⟩ := z; simp [Z.jB, Z.rot, Z.conj, Z.neg]

theorem conj_jB_ne (z : Z) (hz : z ≠ ⟨0, 0⟩) : Z.conj (Z.jB z) ≠ Z.jB (Z.conj z) := by
  obtain ⟨x, y⟩ := z
  simp only [Z.jB, Z.rot, Z.conj, ne_eq, Z.mk.injEq] at hz ⊢
  omega

/-- Aussage 3b: Auf quadratischen Readouts vertauschen sie. -/
theorem conj_jB_quad (z : Z) : Z.quad (Z.conj (Z.jB z)) = Z.quad (Z.jB (Z.conj z)) := by
  obtain ⟨x, y⟩ := z; simp only [Z.quad, Z.jB, Z.rot, Z.conj, Prod.mk.injEq]; refine ⟨?_, ?_, ?_⟩ <;> grind

/-! ## Welche Operationen erhalten das a-Etikett? -/

/-- 2×2-Matrix `[[a, b], [c, d]]`. -/
structure M2 where
  (a b c d : Int)
  deriving DecidableEq, Repr

def M2.orth (m : M2) : Bool :=
  m.a * m.a + m.c * m.c == 1 && m.b * m.b + m.d * m.d == 1 && m.a * m.b + m.c * m.d == 0
/-- Bildet beide Achsen auf ± Achsen ab. -/
def M2.axial (m : M2) : Bool :=
  ((m.a == 0) != (m.c == 0)) && ((m.b == 0) != (m.d == 0))

def unitEntries : List Int := [-1, 0, 1]
def allM2 : List M2 :=
  unitEntries.flatMap fun a => unitEntries.flatMap fun b => unitEntries.flatMap fun c => unitEntries.map fun d => ⟨a, b, c, d⟩

/-- Die Diedergruppe D₄: Viertelschritte und Spiegelungen. -/
def d4 : List M2 := allM2.filter M2.orth

theorem d4_length : d4.length = 8 := by decide
theorem d4_axial : d4.all M2.axial = true := by decide
/-- Die vier Lesart-Operationen liegen in D₄: `rot`, `conj`, `jB` und `−1`. -/
theorem ops_in_d4 : (⟨0, -1, 1, 0⟩ : M2) ∈ d4 ∧ (⟨1, 0, 0, -1⟩ : M2) ∈ d4 ∧ (⟨0, 1, 1, 0⟩ : M2) ∈ d4
    ∧ (⟨-1, 0, 0, -1⟩ : M2) ∈ d4 := by decide

/-- Eine allgemeine Uhrdrehung (hier `w = 3 + 4i`, also um 53°) mischt die beiden a-Hälften. -/
theorem clock_mixes : Z.mulW ⟨3, 4⟩ ⟨1, 0⟩ = ⟨3, 4⟩ := by decide

/-! ## Der ℍ-Faktor: links (Lorentz/Spinor) gegen rechts, und die A₄ -/

/-- Links- und Rechtsmultiplikation vertauschen (Assoziativität von ℍ). -/
theorem LR_comm (p x r : Q) : Q.mul (Q.mul p x) r = Q.mul p (Q.mul x r) := by
  obtain ⟨a0, a1, a2, a3⟩ := p; obtain ⟨b0, b1, b2, b3⟩ := x; obtain ⟨c0, c1, c2, c3⟩ := r
  simp only [Q.mul, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

def qconj (q x : Q) : Q := Q.mul (Q.mul q x) (Q.conj q)

/-- Konjugation mit `1+i+j+k` (Norm 4) auf Im ℍ: `ai + bj + ck ↦ 4(ci + aj + bk)`, zyklisch. -/
theorem conj_cyc (a b c : Int) : qconj ⟨1, 1, 1, 1⟩ ⟨0, a, b, c⟩ = ⟨0, 4 * c, 4 * a, 4 * b⟩ := by
  simp only [qconj, Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- Konjugation mit `i`: `ai + bj + ck ↦ ai − bj − ck`. -/
theorem conj_i (a b c : Int) : qconj ⟨0, 1, 0, 0⟩ ⟨0, a, b, c⟩ = ⟨0, a, -b, -c⟩ := by
  simp only [qconj, Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- Beide sind Elemente der A₄ aus `Dixon.lean` (neuer Platz `k` = Vorzeichen · alter Platz `π k`). -/
theorem conj_generators_in_a4 : (⟨2, 0, 1, 1, 1, 1⟩ : SP) ∈ a4 ∧ (⟨0, 1, 2, 1, -1, -1⟩ : SP) ∈ a4 := by decide

/-- Linksmultiplikation (Spinor) bildet Im ℍ aus sich heraus ab: `i · i = −1`. -/
theorem left_leaves_im : Q.mul ⟨0, 1, 0, 0⟩ ⟨0, 1, 0, 0⟩ = ⟨-1, 0, 0, 0⟩ := by decide

/-- … und verteilt Platznormen um: `(1+i)·j = j + k`. -/
theorem left_moves_norms : Q.mul ⟨1, 1, 0, 0⟩ ⟨0, 0, 1, 0⟩ = ⟨0, 0, 1, 1⟩ := by decide

/-- Links-invariant ist die quaternionische Gram-Größe: `conj(qx)·(qy) = |q|² · conj(x)·y`. -/
theorem gram_left (q x y : Q) :
    Q.mul (Q.conj (Q.mul q x)) (Q.mul q y)
      = (⟨q.a^2 + q.b^2 + q.c^2 + q.d^2, 0, 0, 0⟩ : Q).mul (Q.mul (Q.conj x) y) := by
  obtain ⟨a0, a1, a2, a3⟩ := q; obtain ⟨b0, b1, b2, b3⟩ := x; obtain ⟨c0, c1, c2, c3⟩ := y
  simp only [Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-! ## Links-invariante Etiketten auf der rechten Seite (K77.10)

Tripel als 8 Quaternionen `h_c` (Spalte `c` = Oktonion-Komponente). Lorentz wirkt von links, `h_c ↦ q h_c`. Die Gram-Größe
`conj(h_c) h_d` ist links-invariant (bis auf `|q|²`); ihre drei Imaginärkomponenten `A⁽ⁱ⁾, A⁽ʲ⁾, A⁽ᵏ⁾` tragen drei Etiketten,
die rechts sitzen. Für ein reines Tripel ist `A⁽ⁱ⁾_cd = −(x_j,c x_k,d − x_k,c x_j,d)`: das Keilprodukt der beiden anderen Plätze,
also `μ_i = Σ_cd (A⁽ⁱ⁾_cd)² = 2(|x_j|²|x_k|² − ⟨x_j,x_k⟩²)`. Die Rechtswirkung von `1+i+j+k` vertauscht die Etiketten zyklisch. -/

/-- Skalar mal Quaternion. -/
theorem scalar_mul (s : Int) (z : Q) : (⟨s, 0, 0, 0⟩ : Q).mul z = ⟨s * z.a, s * z.b, s * z.c, s * z.d⟩ := by
  obtain ⟨a, b, c, d⟩ := z; simp only [Q.mul, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- Links: jede Komponente der Gram-Größe skaliert mit `|q|²` (für Einheitsquaternionen fest). -/
theorem gram_left_comp (q x y : Q) :
    let s := q.a^2 + q.b^2 + q.c^2 + q.d^2
    let G := Q.mul (Q.conj (Q.mul q x)) (Q.mul q y)
    let G0 := Q.mul (Q.conj x) y
    G.a = s * G0.a ∧ G.b = s * G0.b ∧ G.c = s * G0.c ∧ G.d = s * G0.d := by
  intro s G G0
  have h := gram_left q x y
  rw [scalar_mul] at h
  simp [G, G0, s, h]

/-- Rechts: `conj(xr)(yr) = conj(r) (conj(x) y) r`. -/
theorem gram_right (x y r : Q) :
    Q.mul (Q.conj (Q.mul x r)) (Q.mul y r) = Q.mul (Q.mul (Q.conj r) (Q.mul (Q.conj x) y)) r := by
  obtain ⟨a0, a1, a2, a3⟩ := x; obtain ⟨b0, b1, b2, b3⟩ := y; obtain ⟨c0, c1, c2, c3⟩ := r
  simp only [Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- … mit `r = 1+i+j+k`: die drei Imaginärkomponenten werden zyklisch vertauscht (`(s,a,b,c) ↦ 4(s,b,c,a)`). -/
theorem right_cyc (s a b c : Int) :
    Q.mul (Q.mul (Q.conj ⟨1, 1, 1, 1⟩) ⟨s, a, b, c⟩) ⟨1, 1, 1, 1⟩ = ⟨4 * s, 4 * b, 4 * c, 4 * a⟩ := by
  simp only [Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- Reines Tripel: `conj(u) v = (u·v, −(u × v))` für rein imaginäre `u, v`. Die `i`-Komponente ist das Minus des Minors
der beiden anderen Plätze. -/
theorem gram_pure (u1 u2 u3 v1 v2 v3 : Int) :
    Q.mul (Q.conj ⟨0, u1, u2, u3⟩) ⟨0, v1, v2, v3⟩
      = ⟨u1*v1 + u2*v2 + u3*v3, -(u2*v3 - u3*v2), -(u3*v1 - u1*v3), -(u1*v2 - u2*v1)⟩ := by
  simp only [Q.mul, Q.conj, Q.mk.injEq]; refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- Lagrange-Identität in ℝ⁸ (über `Int`): `Σ_cd (x_c y_d − y_c x_d)² = 2(|x|²|y|² − ⟨x,y⟩²)`. -/
theorem lagrange8 (x0 x1 x2 x3 x4 x5 x6 x7 y0 y1 y2 y3 y4 y5 y6 y7 : Int) :
    (x0*y0 - y0*x0)^2 + (x0*y1 - y0*x1)^2 + (x0*y2 - y0*x2)^2 + (x0*y3 - y0*x3)^2 + (x0*y4 - y0*x4)^2 + (x0*y5 - y0*x5)^2 + (x0*y6 - y0*x6)^2 + (x0*y7 - y0*x7)^2 + (x1*y0 - y1*x0)^2 + (x1*y1 - y1*x1)^2 + (x1*y2 - y1*x2)^2 + (x1*y3 - y1*x3)^2 + (x1*y4 - y1*x4)^2 + (x1*y5 - y1*x5)^2 + (x1*y6 - y1*x6)^2 + (x1*y7 - y1*x7)^2 + (x2*y0 - y2*x0)^2 + (x2*y1 - y2*x1)^2 + (x2*y2 - y2*x2)^2 + (x2*y3 - y2*x3)^2 + (x2*y4 - y2*x4)^2 + (x2*y5 - y2*x5)^2 + (x2*y6 - y2*x6)^2 + (x2*y7 - y2*x7)^2 + (x3*y0 - y3*x0)^2 + (x3*y1 - y3*x1)^2 + (x3*y2 - y3*x2)^2 + (x3*y3 - y3*x3)^2 + (x3*y4 - y3*x4)^2 + (x3*y5 - y3*x5)^2 + (x3*y6 - y3*x6)^2 + (x3*y7 - y3*x7)^2 + (x4*y0 - y4*x0)^2 + (x4*y1 - y4*x1)^2 + (x4*y2 - y4*x2)^2 + (x4*y3 - y4*x3)^2 + (x4*y4 - y4*x4)^2 + (x4*y5 - y4*x5)^2 + (x4*y6 - y4*x6)^2 + (x4*y7 - y4*x7)^2 + (x5*y0 - y5*x0)^2 + (x5*y1 - y5*x1)^2 + (x5*y2 - y5*x2)^2 + (x5*y3 - y5*x3)^2 + (x5*y4 - y5*x4)^2 + (x5*y5 - y5*x5)^2 + (x5*y6 - y5*x6)^2 + (x5*y7 - y5*x7)^2 + (x6*y0 - y6*x0)^2 + (x6*y1 - y6*x1)^2 + (x6*y2 - y6*x2)^2 + (x6*y3 - y6*x3)^2 + (x6*y4 - y6*x4)^2 + (x6*y5 - y6*x5)^2 + (x6*y6 - y6*x6)^2 + (x6*y7 - y6*x7)^2 + (x7*y0 - y7*x0)^2 + (x7*y1 - y7*x1)^2 + (x7*y2 - y7*x2)^2 + (x7*y3 - y7*x3)^2 + (x7*y4 - y7*x4)^2 + (x7*y5 - y7*x5)^2 + (x7*y6 - y7*x6)^2 + (x7*y7 - y7*x7)^2
    = 2 * ((x0*x0 + x1*x1 + x2*x2 + x3*x3 + x4*x4 + x5*x5 + x6*x6 + x7*x7) * (y0*y0 + y1*y1 + y2*y2 + y3*y3 + y4*y4 + y5*y5 + y6*y6 + y7*y7) - (x0*y0 + x1*y1 + x2*y2 + x3*y3 + x4*y4 + x5*y5 + x6*y6 + x7*y7)^2) := by
  grind

end QSFormal.Lesarten
