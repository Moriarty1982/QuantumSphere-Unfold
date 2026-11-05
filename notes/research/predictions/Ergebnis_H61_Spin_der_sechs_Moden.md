# Ergebnis H61: widerlegt. Die 6 Moden sind keine Weyl-Moden in der naiven Spin-Zuordnung

Grundlage ist die Vorab-Notiz H61 (Commit 036cf7a, vor der Rechnung). Gerechnet hat `k161_spin.py` mit 200 Nullrichtungen in g''_8; die Kontrolle ergab 6 Polarisationen in jeder Richtung.

## Werte (Median, maximal möglich wäre 1)
| Größe | Wert |
|---|---|
| r_J | 1.0 |
| r_γ5 | 0.99 |
| r_h | 0.5 |
| Eigenwerte von γ₅ auf P | −0.99 … +0.98, gemischt, Streuung 0.6 |
| Eigenwerte von h auf P | −0.49 … +0.48, Streuung 0.3 |

P ist also weder unter J noch unter γ₅ noch unter h invariant. **H61 ist widerlegt.**

## Erkundung danach (nicht vorregistriert; k161b, k161c)
- **Majorana-Form?** dim(P + JP) = 12, aber P ist nicht total reell: der größte Kosinus zwischen P und JP liegt bei 0.99. P + JP ist auch nicht der Kern von ξ̂_a γ^a für drei masselose Dirac-Spinoren. Der Kern hat zwar ebenfalls Dimension 12, aber der kleinste Hauptkosinus ist 0.33 bzw. 0.0. Eine Majorana-Lesart in derselben Zuordnung trägt damit auch nicht.
- **Verteilung auf die drei Blöcke von Ψ:** Die Spur des Projektors je Block ist 1.64, 1.05 und 3.24 (Summe 6), und P hat auf jedem Block vollen Rang. Die Moden sind nicht nach Blöcken getrennt. Das größte Gewicht trägt der dritte Block, der in den Koframe Q_a = S₃ ⊗ (1, α_a) gar nicht eingeht.

## Lesart
Die 6 masselosen Moden sind keine freien Spinor-Moden, wenn man die Lorentz-Wirkung naiv als I₃ ⊗ Spin½ im rekonstruierten Koframe ansetzt.

Diese Zuordnung ist vermutlich falsch:
- Der Koframe entsteht nur aus den Blöcken 1 und 2 (über S₃).
- Der dritte Block trägt das meiste Gewicht.

Die Lorentz-Wirkung des Modells muss deshalb aus seinen eigenen Symmetrien bestimmt werden, also aus der Stabilisatorgruppe des Symbols g''_8 in GL(4) × GL(24), bevor sich ein Spin ablesen lässt. Bis dahin bleibt offen, welche Felder die 6 Moden sind.
