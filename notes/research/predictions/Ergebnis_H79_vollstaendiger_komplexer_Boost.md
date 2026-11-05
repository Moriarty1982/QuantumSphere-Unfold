# Ergebnis H79: Mit vollständigem komplexem Boost und holomorpher Adjungierter ist die zweite Lesart isotrop und stabil

Vorab-Notiz `Vorab_Notiz_H79_vollstaendiger_komplexer_Boost.md`, Commit `701f1ca` (nicht blind). Skript `k195_komplexer_boost.py`, Ausgabe `k195_out.json`.

## Ergebnisse
- **Konvention:** S(θ) = exp(−θσ_z/2) erfüllt S σ̄^μ S = Λ(θ)^μ_ν σ̄^ν für reelles θ (sympy). Bei θ = iπ ist S = −iσ_z, genau die Abbildung aus k174, und Λ(iπ) = diag(−1, 1, 1, −1).
- **H79a bestätigt (holomorph, ψ† ↦ ψ†S):** Der Bildterm ist in allen vier Richtungen −L_M. Die Wirkung ist (a − b)·S_M, isotrop (det ∝ (a − b)²(ω² − k²)). Das Bild trägt entgegengesetzte Energie (K3 erfüllt). Für a > b ist die Energie nach dem Dirac-See nach unten beschränkt. Es gibt keine T-Quanten.
- **H79b bestätigt (hermitesch, ψ† ↦ ψ†S†):** Der Bildterm ist +L_M, die Wirkung (a + b)·S_M, isotrop, aber das Bild hat das Vorzeichen der Materie (K3 verletzt).
- **H79c bestätigt (Skalar):** Λ(iπ) erhält die Metrik, X ist invariant; (a − b)·½X − (a + b)·V wie in H78a. Probe mit gespiegeltem und verschobenem Argument: relative Abweichung 3·10⁻¹⁶.

## Folge
- Die Anisotropie aus H78 kam allein daher, dass k174 den Boost nur auf den Spinor und nicht auf das Argument angewendet hat. Mit dem vollständigen Boost und der holomorphen Abbildung der Adjungierten ist Variante 2 **isotrop, stabil (a > b) und ohne Zerfall aus H76**. Fermionen und Skalare haben dieselbe Kinetik-Gewichtung a − b = 1/γ (Materie-Gewichte).
- **Festlegung für den Autor:** „holomorph“ ist die Fortsetzung der Boost-Identität ins Komplexe und passt zur komplexen Lesart K. Es ist eine Entscheidung zur offenen Frage „welche Adjungierte“ der Bestandsaufnahme.
- **Im flachen Raum ist die reduzierte Theorie die Materie-Theorie mit umnormierter Kinetik.** Kinetik a − b, Potential a + b. Skalare bekommen m_eff² = γ·m². Λ wird nicht aufgehoben (Potential mit a + b). Beobachtbare Spuren des T-Anteils gibt es im flachen Raum außer dieser Umnormierung nicht.

## Nachträglich bemerkt, nicht geprüft
Λ(iπ) kehrt im Argument die Zeit um. Im flachen Raum fällt das aus dem Integral heraus, auf einem expandierenden Hintergrund nicht: Dort sieht der T-Anteil den Hintergrund zeitgespiegelt, also die Expansion als Kontraktion. Das ist die Frage des Autors vom 5.11. („Müsste sich die Expansion bei Tachyonen anders auswirken? Wäre das für die nicht eher eine Kompression?“, Herkunft von I4). Ein Test auf FRW wäre der nächste Schritt; vor der Rechnung ist festzulegen, wie die Spiegelung um welchen Zeitpunkt und der Versatz δ in konformer Zeit (H70) zusammengehen.
