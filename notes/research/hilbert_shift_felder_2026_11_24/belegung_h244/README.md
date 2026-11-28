# H244 (k461): Folgt die Belegung (2/3, 1/6, 1/6) aus der Kopien-Regel H242?

- `Vorab_H244_Belegung.md`: Vorab-Notiz (b2f0677, vor der Rechnung).
- `k461_test_h244.py` → `k461_out.txt`: Rechnung (Python). Aufruf aus diesem Ordner.
- `k461b_gegenprobe.wl` → `k461b_out.txt`: Gegenprobe (Wolfram, exakt).
- `Ergebnis_H244_Belegung.md`: **trägt teilweise.**
  - Die Belegung folgt nicht aus der Schlussregel g₁+g₂+g₃ ≡ 0: Sie gehört zu „zwei Kopien in gleicher Phase“, und das ist phaseninvariant, der Schluss nicht.
  - Der Baum erreicht sie nur bei δ_ν = π/6 (W₀ = (9+2c²)/(9+12b²+6c²), streng steigend bis 2/3 am Rand).
  - Die θ₁₃-Richtungen sind „zwei Kopien gegenphasig“, das braucht ℤ₆.
