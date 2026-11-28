# Vorab H243 (k460): Ordnet die ℤ₃-Regel der Kopien die Mischung? Ist θ₁₃ eine ℤ₃-Brechung?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (20:36): „ja“ zum Vorschlag, die ℤ₃-Ladung aus H242 an der Mischung zu prüfen
(TM1-Spalte v₀, θ₁₃-Richtung K₂, δ_ν = π/6).

## Vorwissen geprüft
- **k262:** Träger s, ℤ₃, ungerade ℤ₂, Majorana → TM1, θ₂₃ = 45°, |sin δ| = 1.
- **H173:** N̂ = [[1, b, c], [b, 1, −b], [c, −b, 1]]. Bei δ_ν = π/6 ist b = 0 und die Mischung exakt tribimaximal; der Versatz x erzeugt θ₁₃.
- **H205:** v₀ = (1, 0, 1)/√2 ist Eigenvektor für jedes b, c; die Achsen von K₁, K₂ stehen senkrecht auf v₀.
- **H206:** In der zirkulanten Eigenbasis (T-Eigenwerte 1, ω, ω²) gilt diag(K₂) = 0 (massenerhaltend) und diag(K₁) = (0, −1/√3, +1/√3).
- **Maschinerie k370/k371** (unverändert übernommen): T = [[0, 0, 1], [−1, 0, 0], [0, −1, 0]], C(ρ, δ) = 1 + ρ/√2·(e^{iδ}T + e^{−iδ}T²),
  Nhat(δ_ν), K₁ = i(E₀₂ − E₂₀), K₂ = i(−E₀₁ + E₁₀ + E₁₂ − E₂₁)/√2, dazu die übrigen DIRS-Richtungen.
- **H242:** Kopien-Ladungen g ∈ ℤ₃. Ein Produkt schließt genau bei g₁ + g₂ + g₃ ≡ 0 (mod 3).
- **k459:** φ ist keine kleine ℤ₃-Brechung.

## Größen (gesetzt)
- Ladungsbasis: Eigenvektoren t_k von T mit Eigenwert ω^k (k = 0, 1, 2). Das ist die Eigenbasis der geladenen Leptonen, denn C ist ein Polynom in T.
  Ladung eines Zustands = k (Lesart: Kern in Kopie k, H242).
- **Majorana-Form (neutral, Regel aus H242 ohne Konjugation):** M'_{ij} = t_iᵀ N t_j trägt die Klasse (i + j) mod 3. Ein Vakuum („Spurion“) in Kopie g
  erlaubt nach H242 genau die Einträge mit i + j + g ≡ 0.
- **Dirac-Form (geladen):** D'_{ij} = t_i† D t_j trägt die Klasse (j − i) mod 3.
- Gewicht W₀ = Anteil (Frobenius) der Klasse 0, also der ℤ₃-geschlossene Teil mit Vakuum in Kopie 0. Weil die Matrizen reell bzw. hermitesch sind,
  haben die Klassen 1 und 2 stets gleiches Gewicht. Gerechnet wird daher W₀ gegen W₊₋ = 1 − W₀.

## Hypothese
θ₁₃ ist eine ℤ₃-Brechung: Der Baum (TM1, θ₁₃ = 0) ist ℤ₃-geschlossen, und die θ₁₃ erzeugenden Stücke sind rein ℤ₃-geladen.

## Kriterien
- **A1 (blind):** W₀ von N̂(π/6), dem Baum. Er gilt als geschlossen, wenn W₀ ≥ 1 − 10⁻¹².
- **A2 (blind):** W₀ von ∂N̂/∂δ_ν bei π/6, der neutralen Versatzrichtung. Sie gilt als rein geladen, wenn W₀ ≤ 10⁻¹².
- **A3 (nicht blind, H206):** W₀(K₂) = 0. **Blind:** W₀(K₁) und W₀ der übrigen DIRS-Richtungen (nur Bericht).
- **Zufallskontrolle:** 10 000 zufällige reelle symmetrische 3×3-Matrizen (Majorana-Regel) und 10 000 reelle antisymmetrische (Dirac-Regel, als iK).
  Gezählt werden der Anteil mit W₀ ≥ 1 − 10⁻⁶ bzw. ≤ 10⁻⁶ und das mittlere W₀.
- **Urteil:**
  - **trägt:** A1 geschlossen und A2 rein geladen (A3 gilt ohnehin). Die Zufallskontrolle bleibt dabei unter 10⁻³.
  - **trägt teilweise:** nur eines von A1, A2.
  - **widerlegt:** weder A1 noch A2.
- **Nur Bericht:**
  - Welche Mischung entsteht, wenn N̂ auf seinen Klasse-0-Teil projiziert wird?
  - Die Klassen der Spalte v₀.
  - Die Gegenprobe mit der Konjugations-Regel (i − j statt i + j) für die Majorana-Form.

## Werkzeuge
Python k460, Wolfram k460b (exakt: t_k, Klassen von N̂(π/6), ∂N̂/∂δ_ν, K₁, K₂). Qiskit nicht einschlägig.
