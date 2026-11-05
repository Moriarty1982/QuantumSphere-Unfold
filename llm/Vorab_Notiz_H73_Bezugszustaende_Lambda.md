# Vorab-Notiz H73: Legen die Bezugszustände der Frames und ihre Gewichte die Zustandsgleichung des Vakuumterms fest?

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert. Das Ergebnis w_eff ist vorab nicht berechnet.**

## Vorwissen geprüft
- H72 (`Ergebnis_H72_Vakuumterm_Tachyongas.md`): Ein Λ-artiger Term braucht tachyonische Moden mit beiden Normvorzeichen und zwei Impulsschalen; das Mischungsverhältnis ist frei.
- H69: Das versetzte M–T-Paar verlangt Δω·δ = π. H70: Der Versatz ist in konformer Zeit fest.
- H71: Das Tachyonbild mit Masse hat ω² = k² − m²; die normale Masse (V1) hat ω² = k² + m².
- r20 (v4.8.0) und r22: Der Tachyon-Frame ist die überlichtschnelle Rapidität η + iπ/2; bei η = 0 ist das die Rapidität iπ/2, also unendliche Geschwindigkeit. r28: Der Tachyon hat einen Bezugszustand auf seiner Kompensatorachse. Konvention F: Materie-Gewicht p₊ = 1/(1+x), Tachyon-Gewicht p₋ = x/(1+x), x = β_sym².
- Beobachtung (Vorwissen, nicht nachgeschlagen): Für die dunkle Energie ist w ≈ −1, mit Hinweisen auf Abweichungen bis etwa −0,7 (DESI).

## Festlegung (vorab, keine freien Parameter außer der Normierungskonvention)
- **Schale B, Bezugszustand von M:** normale Masse (V1, s = +1) in Ruhe, k = 0, ω = m. Gewicht p₊.
- **Schale A, Bezugszustand von T:** Tachyonbild (V2, s = −1) an der Schwelle, |k| = m, ω = 0. Gewicht p₋. Isotrop gemittelt über ±x, ±y, ±z. Von den beiden λ wird die Mode mit negativem Druck (Spannung) genommen; haben beide positiven Druck, ist H73 widerlegt.
- Folge ohne Test: Δω = ω_B − ω_A = m, also nach H69 δ = π/m.
- Normierung: Feldnorm |ψ|² + |χ|² = 1 je Mode (wie k180). Als Empfindlichkeit ohne Kriterium wird zusätzlich die Normierung |ψ|² = 1 berichtet.
- x = 0,5493² (β_sym aus dem Companion, nicht angepasst).

## Hypothese H73
Die gemittelte Mischung p₊·T_B + p₋·T_A hat eine isotrope Zustandsgleichung w_eff = p/ρ mit **|w_eff + 1| ≤ 0,05**, trifft also den Λ-Wert.

Zusätzlich berichtet:
- das Gewichtsverhältnis r*, das exakt w = −1 gäbe, und sein Vergleich mit p₊/p₋ = 1/x;
- das Vorzeichen von ρ.

## Kontrollen
- Feldgleichungen der beiden Moden ≤ 1e-12.
- Isotropie: gemitteltes T_ij ∝ δ_ij auf ≤ 1e-12; T_0i = 0.
- Die Ruhemode B ist allein reine Dichte (T_ij = 0); die Schwellenmode A allein reiner Druck (T_tt = 0).

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| bestätigt | |w_eff + 1| ≤ 0,05 in der festgelegten Normierung |
| widerlegt | |w_eff + 1| > 0,05, oder kein negativer Druck in A, oder ρ ≤ 0 |
| ungültig | eine Kontrolle verfehlt |

## Grenzen (vorab)
- Klassisch und statisch, im flachen Raum. Die Normierung ist eine Konvention, die das Ergebnis beeinflussen kann; deshalb wird die Alternative berichtet.
- Die Höhe ρ skaliert weiter mit der Gesamtamplitude; getestet wird nur die Zustandsgleichung.
- Die Rotverschiebung massiver Moden mit der Expansion (Drift von w) ist nicht Teil des Tests.
