# Test H128: Kollaps beim Hilbert-Shift HS(4) und die Familiensymmetrie (25.11.2026)

Vorab-Notiz `../../predictions/Vorab_Notiz_H128_Kollaps_Hilbert_Shift_Familiensymmetrie.md` (2b53bbd, vor der Rechnung), Ergebnis
`../../predictions/Ergebnis_H128_Kollaps_Hilbert_Shift_Familiensymmetrie.md`.

- **H128a widerlegt:** dim Der(H₃(𝕊)) = 22, nicht 17. Es überlebt g₂ ⊕ **su(3)**. Die su(3) ist die Symmetrie von H₃(ℂ) über der Verdopplungseinheit e₈.
- **H128b bestätigt für u = e₇ (r = 9/10 exakt), widerlegt für u = e₈ (r = 1).** Allgemein r(u) = 1 − (1 − u₈²)/10.
- Nachträglich (k283c): Der Stabilisator der Ladungsebene H₃(ℂ_e₇) wirkt darauf nur noch als so(3). Bei HS(5) dasselbe Muster mit e₁₆ (dim Der = 22, r = 29/36).

Dateien: `k283_test_h128.py` (`k283_out.txt` für n ≤ 4, `k283_out_n5.txt` mit n = 5), `k283b_exakt.wl` (`k283b_out.txt`, Wolfram),
`k283c_struktur.py` (`k283c_out.txt`, nachträgliche Erkundung). Aufruf aus diesem Ordner: `python3 k283_test_h128.py [5]`, `python3 k283c_struktur.py`.
n = 5 braucht etwa 4 GB Arbeitsspeicher und einige Minuten.
