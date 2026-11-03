# Ergebnis H62: widerlegt. Das Symbol hat außer der Skalierung keine Raumzeit-Symmetrie

Grundlage ist die Vorab-Notiz H62 (Commit ad66a1b, vor der Rechnung). Gerechnet hat `k162_symmetrien.py`.

Bei einem ersten Lauf wurde die Gram-Matrix als Differenz Y^TY − Z^TZ gebildet. Dabei löschten sich Stellen aus, und die Lücke ließ sich nicht ablesen. Der Lauf wurde abgebrochen und nicht gewertet. Gewertet wird die Rechnung mit M = (1 − Π)XQ ohne Auslöschung.

## Werte
| p | dim 𝔰_p | Lücke (Verhältnis) | dim π_A | innere (A = 0) | Schnitt mit so(Q) |
|---|---|---|---|---|---|
| 6 | 50 | 2.2e-16 \| 1.7e-7 (7e8) | 1 | 49 | 0 |
| 7 | 50 | 1.1e-16 \| 2.0e-7 (2e9) | 1 | 49 | 0 |
| 8 | 50 | 1.5e-17 \| 2.2e-7 (1e10) | 1 | 49 | 0 |

so(Q) ist sauber 6-dimensional; die Lücke im Singulärwertspektrum liegt bei 3.7e-2 gegen 1e-16.

## Prüfung der Kriterien
- Die Lücken betragen ≥ 7e8.
- dim 𝔰_p ist für alle drei p gleich.

Der Test ist gültig. Der Schnitt ist 0 und nicht 6, **H62 ist widerlegt.**

π_A(𝔰_p) besteht nur aus der Skalierung A ∝ 1. Kein A ∉ R·1 lässt sich durch ein B so ergänzen, dass g''_p erhalten bleibt: keine Drehung, kein Boost, keine sonstige lineare Koordinatentransformation.

## Erkundung danach (k162b, nicht vorregistriert): die innere Algebra
- Die innere Algebra (A = 0) hat Dimension 49 und ist unter Kommutatoren abgeschlossen (Rest 4e-11).
- Das Zentrum hat Dimension 1 (die Skalierung), die abgeleitete Algebra Dimension 47.
- Die Killing-Form hat Signatur (3 positiv, 1 negativ, 45 null). Die Algebra ist also überwiegend auflösbar oder nilpotent. Ein generisches Element hat bis auf zwei Eigenwerte nur Nullen.
- Ein kompakter halbeinfacher Anteil, etwa su(2) oder su(3) als Eichgruppe, ist nicht zu sehen.

## Lesart
- Am Keim ist das Symbol des erweiterten Systems mit Ω, θ, Eichung und vier Bedingungen nicht lorentzkovariant.
- Der Lichtkegel ist zwar die charakteristische Menge, aber die Polarisationsstruktur auf ihm hängt anisotrop von der Richtung ab.
- Den 6 masselosen Moden lässt sich deshalb im Modell kein Spin zuordnen. Teil (b) von H62 entfällt.
- Ob die Brechung vom Hintergrund kommt (Ψ am Keim, Koframe aus den Blöcken 1 und 2) oder von einem der Zusatzbausteine (Ω, θ, Eichung, die vier Bedingungen), ist offen. Das lässt sich klären, indem man denselben Test für das Symbol von J allein und dann schrittweise erweitert wiederholt.
