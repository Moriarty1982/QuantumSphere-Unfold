# Vorab-Notiz H180: Können die Daten zwischen K_ν = ⅔ und freiem K_ν unterscheiden?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, Entscheidungskarte „Beide Lesarten als Test prüfen“ (Weggabelung aus k380: Neutrinos
in der Ebene {1, U}, K_ν = ⅔ durch J gedeckt, oder in der zweiten farblosen Ebene, K_ν frei). Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3.
Vergeben: H180, k381 (geprüft: frei).

## Vorwissen geprüft
- H99/H100 (`../../predictions/`): Neutrino-Verhältnis R mit K_ν = ⅔. H173, k369, H174, H175, k372, k373, H176 (`../mischung_h173/` bis `../mischung_h176/`):
  Ein-Feld-Form N̂, Baumwert tribimaximal, kleine Drehung der geladenen Leptonen, Ein-Zahl-Kandidat x = 0,04478 (χ² = 2,86 bei vier Messgrößen).
- k369: Der Winkel der Drehung im geladenen Sektor hängt nicht von ρ_e ab. Für ρ_ν ist das nicht gerechnet.
- k380 (`../hs_stufe_k380/`): J legt K nur für die Ebene {1, U} fest.

## Aufbau (unverändert aus k371/k373 übernommen, nur ρ_ν kommt dazu)
Neutrinos: λ_k = 1 + √2·ρ_ν·cos(δ_ν + 2πk/3), Massen ∝ λ_k², Ein-Feld-Form N̂ = [[1, b, c], [b, 1, −b], [c, −b, 1]] mit diesen Eigenwerten
(c = λ_min − 1, b² = ((λ₁ − λ₂)² − c²)/8). K_ν = (1 + ρ_ν²)/3. Geladene Leptonen: Ĉ(ρ, δ) + i·κ·(K₁ + K₂)/√2, Massen exakt.
Messgrößen: R, sin²θ₁₃, sin²θ₁₂, sin²θ₂₃ (Werte und Fehler wie k373).

## Hypothesen und Kriterien
- **H180a (blind): Profil über K_ν mit kleiner Drehung.** Für festes ρ_ν werden δ_ν und κ frei angepasst (zwei Parameter, vier Messgrößen), χ²_min(ρ_ν)
  über ρ_ν ∈ [0,6; 1,5]. Bereich mit Δχ² < 4 gegen das globale Minimum:
  - enthält ρ_ν = 1 nicht: **Daten bevorzugen freies K_ν**;
  - enthält ρ_ν = 1 und ist breiter als ±0,1 in ρ_ν: **Daten unterscheiden nicht**;
  - enthält ρ_ν = 1 und ist schmaler: **Daten stützen K_ν ≈ ⅔**.
  Existiert für ein ρ_ν keine reelle Form (b² < 0), wird das berichtet und der Punkt ausgelassen.
- **H180b (blind): Ersetzt freies K_ν die kleine Drehung?** κ = 0, frei sind ρ_ν und δ_ν (zwei Parameter, vier Messgrößen).
  **Trägt**, wenn χ²_min < 9,2 (99 % bei zwei Freiheitsgraden); sonst **widerlegt**.
- **Bericht:** Massensumme Σm (normale Ordnung, mit Δm²₂₁ = 7,53·10⁻⁵ eV²) und δ_CP entlang des erlaubten Bereichs aus a; die Variante mit der Kopplung
  κ = tan x und δ_ν = π/6 − x (eine Zahl wie H176) bei freiem ρ_ν.
- Der Kandidat H176 wird nicht geändert. Ergibt a „unterscheiden nicht“, bekommt H176 nur den Vermerk, dass K_ν = ⅔ dort eine Setzung ist, die die
  heutigen Daten nicht prüfen.

## Werkzeugwahl
Python (numpy/scipy; Funktionen aus k370/k371 unverändert geladen) und Wolfram Language als unabhängige Kontrolle an zwei Punkten (Spektrum, R, Mischung
am Baumwert). Qiskit nicht geeignet.

## Grenzen (vorab)
Ein-Feld-Form, Richtung (K₁ + K₂)/√2 und normale Ordnung sind Setzungen aus H173 bis H176. Keine Übertragung in den Materie-Frame (Maske), wie in H176.
Kein Vorzeichen gesetzt; OP3/OP4 bleiben offen.
