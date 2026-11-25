# Test H131: S₄ mit der Ladung als verallgemeinerter CP (25.11.2026)

Vorab-Notiz `../../predictions/Vorab_Notiz_H131_S4_Ladung_CP_Mischung.md` (875e6d4, vor der Rechnung), Ergebnis
`../../predictions/Ergebnis_H131_S4_Ladung_CP_Mischung.md`.

- **H131a bestätigt:** Alle 48 zulässigen, nicht entarteten Kombinationen (T, S, X) fallen in eine Klasse.
- **H131b widerlegt:** Diese Klasse hat J = 0. Die CP aus der Ladung gibt δ = 0 oder 180°, nicht ±90°, und θ₂₃ ist nicht maximal.
- Nachträglich (k261c): TM2 mit sin²θ₁₂ = 0,341 und sin²θ₂₃ = 0,395 oder 0,605 bei sin²θ₁₃ = 0,022.

Dateien: `k261_test_h131.py` (`k261_out.txt`), `k261b_exakt.wl` (`k261b_out.txt`, Wolfram), `k261c_theta23.py` (`k261c_out.txt`, nachträglich).
Aufruf aus diesem Ordner: `python3 k261_test_h131.py` (etwa eine Minute; liest `../kollaps_h128/`).
