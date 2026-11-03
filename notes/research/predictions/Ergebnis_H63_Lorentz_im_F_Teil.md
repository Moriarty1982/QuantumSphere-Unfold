# Ergebnis H63: (a) widerlegt, (b) bestätigt. Schon F ist bei festem Hintergrund nicht lorentzsymmetrisch

Grundlage ist die Vorab-Notiz H63 (Commit 2853a5b, vor der Rechnung). Gerechnet hat `k163_lorentz_F.py` mit J aus `completion-omega-witness.npz`.

## Werte
| Zeilen | dim Stab | Lücke (Verhältnis) | dim π_A | Schnitt mit so(Q) | Hauptwinkel-Kosinusse |
|---|---|---|---|---|---|
| F (24) | 176 | 2.2e-2 \| 3.6e-15 (6e12) | 7 | **0** | 0.9998, 0.9975, 0.9957, 0.947, 0.938, 0.742 |
| F+G (28) | 63 | 1.2e-6 \| 3.4e-16 (4e9) | 1 | 0 | 0.150 |
| F+G+dg (32) | 86 | 1.2e-6 \| 5.3e-16 (2e9) | 1 | 0 | 0.129 |

so(Q) ist 6-dimensional (Lücke 3.7e-2 gegen 1e-16). Q ist tatsächlich ein charakteristischer Kegel von F: Auf Q = 0 hat F(ξ) einen Rangabfall von 13, generisch von 4 (k163b).

## Prüfung der Kriterien
- Alle Lücken liegen über 1e6, der Test ist gültig.
- (a): Der Schnitt ist 0 statt 6, also widerlegt.
- (b): Der Schnitt ist ≤ 1, also bestätigt.
- **H63 ist als Ganzes widerlegt**, weil (a) scheitert.

## Erkundung danach (k163b, nicht vorregistriert)
- F hat eine 7-dimensionale Raumzeit-Symmetrie aus Skalierung und 6 weiteren Richtungen. Diese 6 liegen nahe an so(Q) (Kosinusse 0.74 bis 0.9998), aber nicht darin.
- Sie bilden auch keine so(Q') für irgendeine andere quadratische Form Q': Die Bedingung hat keinen Kern (kleinster Singulärwert 0.13), und das Residuum beträgt 0.28.
- Der G-Teil reduziert die Raumzeit-Symmetrie auf die bloße Skalierung.

## Lesart
- Die Erwartung, F hänge vom Hintergrund nur über das Vierbein ab, ist falsch.
- Wenn Ψ am Keim ausdrücklich im Hauptsymbol steht, etwa über einen aus Ψ gebauten Koframe oder Zusammenhang in D_μ, dann ist das Symbol nur unter der Stabilisatorgruppe von Ψ invariant. Für einen generischen Spinor ist diese Gruppe trivial (Takabayasi).
- Tests der Invarianz bei festem Hintergrund (H62, H63) unterscheiden deshalb kein kovariantes von einem nicht kovarianten Modell.
- Das leistet nur der Kovarianztest: Der Lorentz-transformierte Keim (S(Λ)Ψ, Λx) muss das transformierte Symbol ergeben. Das wäre H64.
- Auf Symbolebene ist das billig, wenn das Symbol als Funktion des Keims neu aufgebaut werden kann (k127 kann J aus dem Keim konstruieren).
