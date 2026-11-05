# Vorab-Notiz H82: Massen und Kopplungen unter der zweiten Lesart, verglichen mit den Gewichten aus r19

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen sind analytisch vorgerechnet (kanonische Normierung). Autor 21:41: Massenterme zuerst; unterschiedliches Wachstum (Fermionen γ, Skalare √γ) „könnte unter Umständen gleichzeitig richtig sein“.

## Vorwissen geprüft
- H79/r84.3 und Autorentscheidungen: zweite Lesart, vollständiger komplexer Boost, holomorphe Adjungierte; Terme mit Ableitungen bekommen das Gewicht K = a − b, Terme ohne Ableitungen P = a + b (Lesart B, H77). Materie-Gewichte: K = 1/γ, P = 1, γ = 1,8645.
- r19 (v4.9.0): Skalengrößen konvertieren mit e^{kη} bzw. γ_L^{±k}; Tabelle und P5: k(α) = 1, k(α_s) = 1, k(G_N) = 2 (k(α)/k(G_N) = ½), k(ℓ_P) = 3/2; Auslesegrößen unverändert, darunter cot θ_W ≈ γ_L (r07) und Ω_M = β_sym².
- H71 (Masse macht das Bild tachyonisch, für das Bild allein), r82.4 (ν^c-Majorana-Kanal), H78a (Skalar m_eff² = γm²).
- Mit S = −iσ_z gilt Sᵀ ε S = det(S)·ε = ε: Majorana- und Dirac-Massenterme sind unter dem Boost invariant und haben keine Ableitung, gehen also mit P ein.

## Modell
Spielzeug-Standardmodell in der zweiten Lesart: reeller Higgs-Skalar mit V = −μ²φ²/2 + λφ⁴/4, Weyl-Fermionen mit Yukawa y·φψψ (bzw. Majorana-Masse m), U(1)-Eichfeld mit Kopplung g in D = ∂ − igA, Gravitation mit (1/2κ)·e·R (κ = 8πG). Ableitungsterme (|Dφ|², ψ̄σ̄Dψ, F², e·R) mit K, alle übrigen mit P. Kanonische Normierung: φ, ψ, A ↦ √K·(…).

## Hypothesen
- **H82a (Rechnung):** g_eff = g/√K, α_eff = α/K; y_eff = P·y/K^{3/2}; μ²_eff = P·μ²/K; λ_eff = P·λ/K²; v_eff = v·√K/... (v²_eff = v²·K/P); Fermionmasse m_f,eff = (P/K)·m_f; Majorana-Masse (P/K)·m; m_H² ↦ (P/K)·m_H²; m_W unverändert; G_eff = G/K. Bei Materie-Gewichten also: Fermionen γ, Higgs √γ, W 1, α γ, G γ, ℓ_P √γ, θ_W unverändert. **Bestätigt**, wenn sympy die Exponenten exakt liefert.
- **H82b (Vergleich mit r19):** Für jede Größe mit Gewicht aus r19 ist der Betrag des γ-Exponenten gleich |k|. **Erwartung:** α (1) und α_s (1) passen, θ_W (Auslesegröße, 0) passt; G_N (γ¹ statt k = 2) und ℓ_P (γ^{1/2} statt k = 3/2) passen **nicht**. H82b gilt also als **widerlegt**, sobald eine der Größen abweicht; welche abweichen, wird angegeben.
- Ausdrücklich: Die Umrechnung von r19 (zwischen Frames M und P) und die Reduktion hier (M und T zu einem Feld) sind nicht dieselbe Operation. Eine Übereinstimmung wäre ein Hinweis, keine Herleitung; eine Abweichung schließt die zweite Lesart nicht aus.

## Folge, vorab festgelegt
- Alle Faktoren lassen sich in umdefinierte Parameter aufnehmen. Beobachtbar wird das unterschiedliche Wachstum nur, wo die Struktur nackte Werte oder Gewichte festlegt. r19 ist eine solche Stelle.
- Passen die Eichkopplungen und nicht die Gravitation, liegt die Abweichung in der Behandlung des Gravitationsterms. Zu prüfen wäre dann, ob e·R unter dem Boost anders zu gewichten ist (zwei Ableitungen, aber Koframe zweimal), bevor man r19 oder die zweite Lesart verwirft.

Skript: `llm/k197_massen_zweite_lesart.py` (nach dem Commit dieser Notiz).
