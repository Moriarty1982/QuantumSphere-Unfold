# Ergebnis H73: Die Bezugszustände mit den Gewichten des Materie-Frames geben w = −β_sym²/3, nicht −1

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H73_Bezugszustaende_Lambda.md` (Commit 623a080). Skript `k181_test_h73.py`, Ausgabe `k181_out.json`. Status: H73 widerlegt.**

## Kontrollen (gültig)
Feldgleichungen exakt (0). Die Ruhemode B ist reine Dichte (T_ij = 0). Die Schwellenmode A ist isotrop gemittelt reiner Druck (T_tt = 0, Anisotropie 0, keine Nebendiagonale).

## Ergebnis
- Schwellenmode A: Die Mode λ = +1 hat Druck −⅓ (Spannung), λ = −1 hat +⅓ (Feldnorm, m = 1). Genommen wurde λ = +1.
- Mischung p₊·T_B + p₋·T_A: ρ = p₊·m, p = −p₋·m/3, also **w_eff = −p₋/(3p₊) = −x/3 = −β_sym²/3 = −0,1006**. Das gilt in beiden Normierungen gleich; das Ergebnis hängt nicht von der Konvention ab.
- |w_eff + 1| = 0,90 > 0,05: **widerlegt**. ρ > 0.
- Für exakt w = −1 müsste das Gewichtsverhältnis Materie : Tachyon 1 : 3 sein (r* = ⅓); der Materie-Frame hat 3,31 : 1.
- Folge ohne Test: Δω = m, also δ = π/m.

## Lesart
Mit den Bezugszuständen und den Gewichten des Materie-Frames entsteht eine schwach negative Zustandsgleichung w ≈ −0,1, kein Λ. Die Struktur legt w hier tatsächlich fest, mit w = −β_sym²/3 ohne jeden freien Parameter, aber auf dem falschen Wert.

## Nachträgliche Beobachtungen (nicht vorregistriert, keine Bestätigung)
- **Gewichte vertauscht (Tachyon-Frame):** Liest man dieselbe Mischung im Tachyon-Frame, mit p₊ auf dem Tachyon und p₋ auf der Materie, so folgt w = −1/(3x) = −1,105. Das liegt nahe bei −1 (|w + 1| = 0,105), aber außerhalb der Schranke 0,05 und war nicht vorab festgelegt.
- **Exakt −1** gäbe es genau für x = 3 bzw. 1/x = 3, also β² = 1/3, β = 1/√3 = 0,577, in der Lesart des Tachyon-Frames. Das ist exakte Algebra, aber nachträglich gefunden. Der Companion-Wert β_sym = 0,5493 liegt 5 % darunter; das Leptonfenster aus r61 ist [0,545; 0,570], die Ghosh–Mitra-Zählung aus H47 gab 0,6045.
- Beides darf nur als Anlass für eine neue Vorab-Notiz dienen, nicht als Treffer. Insbesondere wäre vorher zu begründen, warum die Zustandsgleichung des Vakuums im Tachyon-Frame zu lesen ist.
