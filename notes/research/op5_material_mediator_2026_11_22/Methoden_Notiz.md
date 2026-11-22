# Methoden-Notiz: Die optische Mode des Materials als Vermittler des OP5-Falls (Weg A; Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Die Struktur der Antwort ist zum Teil analytisch absehbar. Keine H-Nummer. Auftrag des
Autors: „Weg A: Material“, nach Runde v4.10.0-r34 und der Rückwärtssuche vom selben Tag.

## Vorwissen geprüft
- r32.0: Antriebsoperator des Vergleichsmodells mit Vermittlerterm −g_m² N_m / d_m, d_m = m² + r_m q − x, N_m = ⅔(x² − a_⊥x + a_⊥²);
  gesetzt Z = 1, r_m = c_h² = ½, g₀² = g_m² = 3/100. r32.4: gerichteter Kontrast 16𝒜P/(m²R⁴) aus f = Δ_⊥H/m².
- r33: Ist das Vergleichsfeld der Higgs-Radialmodus von W2, gilt 2(∂_t² − Δ)η + 4μ²η = 𝒥_h, also c_h = 1, Z = 2, g₀ = 0.
- r34.2: optische Mode zweier Kontinua mit Paarfeder, ω₀² = k(ρ₁+ρ₂)/(ρ₁ρ₂); Kopplung an 𝒥_h genau bei Y₁/ρ₁ ≠ Y₂/ρ₂.
- Rückwärtssuche (22.11.): r_m ≠ 1 und die Paarung bei gemeinsamer Rapidität brauchen ein ausgezeichnetes Bezugssystem; die
  Gleichsetzung von Materie- und Tachyon-Rapidität ist nicht boostinvariant (Wolfram: Δq² = 4m² cosh(2η+ξ) sinh ξ).
- Zurückgestellte Ideen: I1 Auslöser 4 getroffen und dem Autor vorgelegt; Autor wählt Weg A.

## Ansatz
Wirkung im Materie-Frame M (c = 1): Higgs-Radialmodus η von W2 (Z_W = 2, c_h = 1, m_H) plus zwei elastische Kontinua mit Paarfeder k aus
r32.2, gekoppelt über die Massendichte, L ⊃ η (Y₁ ∇·u + Y₂ ∇·w) mit Y_a = Σ y n₀ der Komponente a (aus r32.1). Die Materialgrade werden
ausintegriert; das Ergebnis ist ein effektiver Operator für η, der mit der Form von r32.0 Koeffizient für Koeffizient verglichen wird.

## Fragen und Rechnung (Wolfram, exakt; Skript `material_mediator.wl`, Ausgabe `run/material_mediator.txt`)
1. **Isotropes Material:** effektiver η-Operator, Zerlegung in akustischen und optischen Pol, Residuen. Identifikation m² ↔ ω₀²,
   r_m ↔ v_opt², g_m²-Gegenstück. Zähler des optischen Terms gegen N_m.
2. **Abhängigkeit des Kontrasts von r_m:** Reihe von g_m² N_m / d_m auf dem statischen Plateau (x = 0) in q/m²; trägt r_m zum führenden
   Glied bei, aus dem r32.4 den Kontrast gewinnt?
3. **Gerichtete Präparation:** einachsiges Material (Kopplung nur über die Querdivergenz ∇_⊥·u_⊥, Steifigkeiten quer und längs
   verschieden). Entsteht ein Term, der von a_⊥ und nicht nur von q abhängt? Welche Potenz von a_⊥ steht im Zähler?
4. **Kopplungsbedingung physikalisch:** Y_a = f_a ρ_a / v mit dem Higgs-Anteil f_a der Ruhemasse; die Bedingung Y₁/ρ₁ ≠ Y₂/ρ₂ wird zu
   f₁ ≠ f₂. Nur symbolisch; Zahlen für f_a werden nicht eingesetzt.

## Raster (vorab)
- **trägt:** Das Material liefert einen gerichteten Vermittlerterm von der Form −g_m² N_m / d_m, und die Werte, von denen der führende
  Kontrast abhängt, sind für ein Material erreichbar.
- **trägt teilweise:** Ein gerichteter Vermittlerterm entsteht (einachsige Präparation), aber Form oder Werte weichen von r32.0 ab
  (etwa eine andere Potenz von a_⊥ im Zähler oder r_m nicht erreichbar, sofern r_m im führenden Glied steht).
- **trägt nicht:** Auch einachsig entsteht kein von a_⊥ abhängiger Vermittlerterm.

Frames: alles im Materie-Frame M; keine Größe eines anderen Frames. OP5 bleibt in jedem Fall offen.
