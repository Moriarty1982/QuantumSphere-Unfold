# Methoden-Notiz: Lässt sich die Gleichsetzung (40) aus W2 herleiten? (Erkundung, vor der Rechnung festgelegt)

22. November 2026. **Erkundung, nicht blind:** Die Struktur der Antwort ist analytisch weitgehend absehbar. Keine H-Nummer. Auftrag des Autors:
„lass uns annahme 40 untersuchen“ (Gleichsetzung δJ_OP5 = δ𝒥_h im OP5-Fall, Companion r32.0(ii), Preprint (40), Physik-Paper 6.9).

## Rückwärtsfrage
Die Gleichsetzung folgt aus einer Wirkung genau dann, wenn das skalare Vergleichsfeld h des OP5-Modells ein Feld der Wirkung ist, das die
Higgsquelle 𝒥_h = −∂ε_mat/∂h_W als Quelle hat. In W2 ist das der Radialmodus η des Higgs-Dubletts (h_W = v + η). Notwendig ist dann, dass
der skalare Operator des OP5-Modells mit dem Operator von η in W2 übereinstimmt.

## Vorwissen geprüft
- `../v4_10_0_r82/Wirkung_W2_Higgs.md`: W2 = W1 + Higgs, L_H = e[|DΦ|² − V], V = −μ²|Φ|² + λ|Φ|⁴; Yukawa über Konnektoren.
- `../op5_bifocal_response_2026_11_18/W2_Higgsquelle.md`, `OP5_J_W2_Dichteantrieb.md`: 𝒥_h = −Σ y_i n_i; lineare Kopplung η·(Σ y n₀)∇·u.
- `../op5_bifocal_response_2026_11_18/OP5_J_Luminaler_Einstein_Kanal.md`: reduziertes Oszillatormodell, Kern
  𝒦 = Z(x − Ω²) − 3g₀²d/2 + g_m²N_m/d_m mit gesetzten Daten Z = 1, r_m = c_h² = 1/2, g₀² = g_m² = 3/100.
- Companion r32.0 (Annahme), r32.4 (Kontrast über das massive Vergleichsfeld f).

## Rechnung (Wolfram, exakt)
Skript `assumption40_w2.wl`, Ausgabe `run/assumption40_w2.txt`.
1. Radialmodus aus L_H mit h_W = |Φ| in unitärer Eichung, minimal gekoppelt, flacher Hintergrund: Bewegungsgleichung von η mit
   Yukawa-Quelle; Masse m_H² und Normierung (kinetischer Faktor) bestimmen.
2. Lineare Mischung von η mit der Metrik: Spur des linearen Energie-Impuls-Tensors am Minimum, minimal und mit Zusatzterm ξR|Φ|².
3. Koeffizientenvergleich des skalaren OP5-Operators Z(Ω² + c_h²q − x) + (3/2)g₀²(q − x) mit dem W2-Operator von η; Bedingungen an
   (Z, c_h, Ω, g₀) und an g_m.
4. Folge für den gerichteten Kontrast (r32.4): Wovon hängt das massive Vergleichsfeld ab, und hat es in W2 ein Gegenstück?

## Entscheidung (vorab)
- **Herleitbar in W2**, wenn alle Daten des OP5-Modells, die der Kontrast braucht, aus W2 folgen.
- **Teilweise herleitbar**, wenn die Gleichsetzung für den skalaren Kanal folgt, aber Daten des Modells (Geschwindigkeiten, Kopplungen,
  Vermittler) dem widersprechen oder fehlen; dann wird benannt, welche Annahme an die Stelle von (40) tritt.
- **Nicht herleitbar**, wenn schon der skalare Kanal nicht passt.
OP5 bleibt in jedem Fall offen.
