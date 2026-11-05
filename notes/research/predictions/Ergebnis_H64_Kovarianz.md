# Ergebnis H64: bestätigt (Lauf 2, nicht blind). R ist koordinatenkovariant und intern lorentzkovariant

Grundlage ist die Vorab-Notiz H64 (b2471b2) mit ihrem Nachtrag (Lauf 1 ungültig, Lauf 2 mit rcond = 1e-6). Gerechnet hat `k164_kovarianz.py`, das Log ist `k164_log_lauf2.txt`. Der Abgleich von J₀ mit dem gespeicherten J ergibt 1.6e-10.

## Werte (Lauf 2, relatives Residuum min_C ‖J'L − CJ‖/‖J'L‖)
| Fall | F | G | dg |
|---|---|---|---|
| Kontrolle positiv | 1.1e-11 | 1.1e-15 | 1.2e-15 |
| Kontrolle negativ (Hintergrund nicht transformiert) | **0.26** | **0.26** | 8.5e-12 |
| (a) Koordinaten M ∈ GL(4) | 8.3e-11 | 3.3e-10 | 8.5e-12 |
| (b) innere Lorentz S | 5.6e-11 | 2.1e-10 | 1.1e-11 |
| (c) beides | 8.8e-11 | 4.1e-10 | 1.2e-11 |
| Zusatz: nur Drehung / nur Boost | ≤ 7.4e-11 | ≤ 3.3e-10 | ≤ 1.3e-11 |

Zum dg-Block in der negativen Kontrolle: Sein Symbol hängt nur von h ab, deshalb trennt er dort nicht (siehe Nachtrag).

## Prüfung der Kriterien
- Die positive Kontrolle liegt bei ≤ 1e-9.
- Die negative Kontrolle für F und G liegt bei ≥ 1e-3.
- Alle Testwerte liegen bei ≤ 4.1e-10, also unter 1e-7.

**H64 ist bestätigt.**

## Lesart
- Die Konstruktion R ist auf Symbolebene unter linearen Koordinatenänderungen kovariant, wenn Jets und Hintergrund (A, ∂A, ∂h) tensoriell transformiert werden.
- Sie ist außerdem kovariant unter inneren Lorentz-Transformationen von Ψ, und zwar unabhängig von den Koordinaten. Grund ist der Koframe aus Strömen von Ψ: Er trennt den inneren Lorentz-Index vom Koordinatenindex.
- Das Scheitern von H62 und H63 ist damit vollständig erklärt. Es kommt vom festen Hintergrund, also von Ψ am Keim und den Feldern A und h, nicht von einem Baustein der Konstruktion.
- Die Negativkontrolle zeigt das direkt: Wird der Hintergrund nicht mittransformiert, bricht die Kovarianz mit 0.26.

## Grenzen
- Geprüft ist nur das Symbol erster Ordnung von R, also F, G und dg. Ω, θ, die Eichung Ψ†K₂Ψ = S und die vier Bedingungen sind nicht geprüft.
- Die Eichung ist nach dem Nachtrag zu H62 als nicht kovariante Eichfixierung zu erwarten.
- Die physikalische Frage verschiebt sich damit: Was sind A und h, und ist der Hintergrund selbst eine Lösung kovarianter Gleichungen? Die freie ϑ-Richtung (r71.4) und die Felder A und h legen eine Kugel- bzw. Milne-artige Hintergrundgeometrie nahe.
