# H196: Ladungsterm (H182) und der Up/Down-Zähler-Split

Test, **teilweise**. Verschiebt der Ladungsterm das Quintik-Glied (l_k²) für Up anders als Down?

- `Vorab_Notiz_H196_Ladungsterm_und_Up_Down_Zaehler.md` — Vorab (Kopie), Commit 8cfd9c5.
- `k404_test_h196.py` / `k404_out.txt` — fester Kandidat (3 Param), volle Ladungsstruktur (4 Param), Kontrolle.
- `k404b_out.txt` — Wolfram-Gegenprobe der ladungsungeraden Krümmungen (bestätigt sympy).
- `Ergebnis_H196_Ladungsterm_und_Up_Down_Zaehler.md` — Befund.

**Kurz:** Strukturell **ja** — die volle Ladungsstruktur m_s = [A l_k + B l_k² + s(C l_k + D l_k²)]/(l_i+l_j)² trifft (χ² 7,9), das
ladungsungerade l_k² (D = 3,32·10⁻²) ist nötig, Vorzeichen +, und D ≈ B, also b_up = B+D stark, b_down = B−D ≈ 0: die Ladung macht
Up quadratisch und Down linear. **Aber keine Vorhersage:** 4 Parameter = H194 umparametrisiert; kein einzelner H186-Kandidat (3
Param) trägt (Up 237σ); D ≈ B ist gefittet, nicht erzwungen. Der H195-Nenner behebt H186 hier nicht. Aufruf:
`python k404_test_h196.py > k404_out.txt`.
