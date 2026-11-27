# H208 (k418): θ₁₂/TM1-Problem — ist sin²θ₁₂ ≈ 0,318 erzwungen oder senkbar?

**Frage:** Senkt eine struktur-erhaltende Deformation sin²θ₁₂ von 0,3195 (+2,5σ) auf die gemessenen 0,3036, ohne θ₁₃, Massen-Erhaltung und maximale CP-Verletzung zu brechen?

**Verdikt: TEILWEISE.** Die feste Spalte v₀ (|U_e1|²=⅔) ist exakt (Wolfram, für alle b,c). sin²θ₁₂ ist aber nicht starr: ein erlaubter Zusatzterm (S+d) senkt bei erhaltenen Massen + maximaler CP auf 0,3155 (**+1,9σ**) — nicht auf den Zentralwert. Tiefer geht nur gegen die maximale CP-Verletzung: **die Struktur handelt θ₁₂ gegen |sin δ|** (massenerhaltender Boden springt von 0,234 bei |sin δ|≈0,65 auf 0,3155 bei |sin δ|≥0,8). Neue, von JUNO (θ₁₂) + DUNE/T2K (δ) testbare Korrelation: entweder θ₁₂ hoch (≳0,315) + maximale CP, oder θ₁₂ zentral + submaximale CP.

**Werkzeuge:** numpy (8-dim Richtungs-Scan, 290 Kandidaten), Wolfram exakt (v₀-Eigenvektor, TM1-Formel).

**Dateien:** `Vorab_H208_Theta12_TM1.md` · `k418_test_h208.py` / `k418_out.txt` · `k418b_kontrolle.wl` / `k418b_out.txt` · `Ergebnis_H208_Theta12_TM1.md`.
