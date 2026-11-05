# Ergebnis H78: T als zweite Lesart desselben Feldes – stabil und ohne Zerfall, aber für Fermionen richtungsabhängig

Vorab-Notiz `Vorab_Notiz_H78_T_als_zweite_Lesart.md`, Commit `ef3e1e0` (nicht blind). Skript `k194_zweite_lesart.py`, Ausgabe `k194_out.json`.

## Ergebnisse
- **H78a bestätigt (Skalar):** a·L_M + b·L_T = (a − b)·½X − (a + b)·V, exakt. δ fällt heraus (Probe: Wirkung des Bildes mit und ohne Verschiebung gleich, relative Abweichung 4·10⁻¹⁶). Für a > b ist die Energie nach unten beschränkt, die wirksame Masse ist m_eff² = (a + b)/(a − b)·m² = γ·m² bei Materie-Gewichten (γ = 1,8645). Bei Photon-Gewichten fehlt die Kinetik ganz.
- **H78b bestätigt (Weyl):** Der wirksame Operator ist (a − b)(σ̄^t∂_t + σ̄^z∂_z) + (a + b)(σ̄^x∂_x + σ̄^y∂_y), unabhängig von δ. Der Spinor-Faktor −iσ_z dreht σ̄ mit R = diag(1, −1, −1, 1); mit dem F3-Vorzeichen bleiben t und z mit a − b, x und y mit a + b. Dispersion ω² = k_z² + q²·k_⊥², q = (a + b)/(a − b) (sympy, Rest 0). Der Hamilton-Operator ist hermitesch, das Spektrum reell (±). Bei Materie-Gewichten ist q = γ = 1,8645, bei Photon-Gewichten gibt es keine Zeitableitung.
- **H78c bestätigt:** Die reduzierte Theorie ist eine Theorie in Φ bzw. ψ allein, mit den Freiheitsgraden von M. Es gibt keine unabhängigen T-Quanten negativer Energie, also keinen Zerfallskanal wie in H76.

## Offenlegung
Lauf 1 der δ-Probe ergab 26 % Abweichung. Ursache war das Testfeld (sin(x + 0,3t) ist auf dem Gitter nicht periodisch, die Verschiebung dort keine Symmetrie), nicht die Aussage. Lauf 2 mit periodischem Feld (sin(x + 2t)): 4·10⁻¹⁶. Das Skript enthält die Korrektur mit Kommentar.

## Folge (nach der Vorab-Notiz)
- **Fermionen:** In der Form von k174 sagt Variante 2 quer zur Achse n die γ-fache Lichtgeschwindigkeit voraus, eine Lorentz-Verletzung von 86 %. Laborgrenzen für Elektronen liegen bei 10⁻¹³ bis 10⁻¹⁵ (Altschul, *Laboratory bounds on electron Lorentz violation*, arXiv:1005.2994; LEP-Synchrotronverluste, Überleben von TeV-Photonen). **Variante 2 ist in dieser Form für Fermionen ausgeschlossen**, um rund 13 Größenordnungen. Bei Photon-Gewichten hätten Fermionen keine Zeitentwicklung.
- **Skalare:** stabil, ohne Zerfall aus H76, Masse um √γ vergrößert.
- **Nebenbefund:** Mit der reellen Wirkung fällt der Versatz δ im flachen Raum heraus. Die δ-Abhängigkeit aus H69 und H70 stammt aus der komplexen Lesart K (Strombilanz), nicht aus der reellen Wirkung.

## Was offen bleibt
- Eine andere Form der zweiten Lesart, die auch die Koordinaten abbildet, ψ_T(x) = S·ψ(Λx + δ), würde die Isotropie erhalten. Λ(iπ) = diag(−1, 1, 1, −1) kehrt aber t um. Das ist genau die Verwechslung von Tachyon-Abbildung und Zeitumkehr, vor der r51 und r81 warnen. Sie wäre nur mit eigener Begründung zulässig.
- Variante 1 (T als eigenes Feld) mit Rahmen-Cutoff ≲ 14 MeV.
