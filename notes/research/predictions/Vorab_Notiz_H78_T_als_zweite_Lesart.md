# Vorab-Notiz H78: Der T-Anteil als zweite Lesart desselben Feldes – Dynamik der reduzierten Theorie

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Erwartungen folgen analytisch aus der Translationsinvarianz der Wirkung im flachen Raum; die Rechnung (sympy) macht sie nachprüfbar. Autorentscheidung 5.11.: Variante 2 (dasselbe Feld, versetzt gelesen) zuerst prüfen.

## Vorwissen geprüft
- `notes/research/v4_10_0_w1/Erkundung_MT_Luecke.md` (k174): T-Anteil als dasselbe Feld, ψ_T(x) = −iσ_n ψ_M(x + δ); Λ(iπ) = diag(−1, 1, 1, −1) für n = z; Λ(iπ) = −R_n(π); j_T = Λ(iπ) j_M; Isotropie durch n gebrochen (Preis 2).
- H69, H70 (Paar aus demselben Feld mit Versatz neutral; Versatz in konformer Zeit fest).
- H77 / r83.3: Tachyonbild einer Wirkung nach Lesart B (Kinematik fortgesetzt, Potentiale bleiben). H76: Zerfall über Paare unabhängiger T-Quanten.
- `llm/Erkundung_Geistkondensat_Skala.md`: Frage „eigenes Feld oder zweite Lesart“, Autor wählt Variante 2.
- Gesamtbild T1 („ein Objekt in drei Frames“, Vermutung).

## Aufbau
Flacher Raum, Gewichte a (M) und b (T) mit a, b > 0 (Materie-Gewichte a = p₊, b = p₋, a − b = 1/γ, a + b = 1; Photon-Gewichte a = b). Wirkung S = a·S_M[Φ] + b·S_T[Φ_T] mit Φ_T(x) = Bild von Φ, ausgewertet bei x + δ (nur das Argument verschoben, keine Koordinatenabbildung, wie k174).
- **Skalar:** L_M = ½X − V(φ), L_T = −½X − V (Lesart B), φ_T(x) = φ(x + δ).
- **Weyl:** L_M = ψ†σ̄^μ i∂_μψ, L_T = −ψ_T†σ̄^μ i∂_μψ_T (F3), ψ_T(x) = −iσ_zψ(x + δ).

## Hypothesen und Entscheidungskriterien
- **H78a (Skalar):** S = ∫[(a − b)·½X − (a + b)·V] exakt, unabhängig von δ. Die Energie ist für a > b und nach unten beschränktes V nach unten beschränkt; bei a = b fehlt die Kinetik (keine Dynamik). Bei Materie-Gewichten ist die wirksame Masse m_eff² = γ·m². **Bestätigt**, wenn die symbolische Rechnung die Koeffizienten exakt liefert.
- **H78b (Weyl):** Der wirksame Operator ist (a − b)(σ̄^t∂_t + σ̄^z∂_z) + (a + b)(σ̄^x∂_x + σ̄^y∂_y), unabhängig von δ. Die Dispersion ist ω² = k_z² + q²·k_⊥² mit q = (a + b)/(a − b); bei Materie-Gewichten q = γ ≈ 1,864, bei Photon-Gewichten keine Zeitableitung. Das Spektrum ist reell, die Energie nach Füllen des Dirac-Sees nach unten beschränkt. **Bestätigt**, wenn Operator und Dispersion exakt so herauskommen.
- **H78c (Freiheitsgrade):** Die reduzierte Theorie hat genau die Freiheitsgrade von M allein. Es gibt keine unabhängigen T-Quanten negativer Energie, also keinen Zerfallskanal wie in H76. (Strukturell; bestätigt, wenn H78a und H78b eine Wirkung in Φ bzw. ψ allein ergeben.)

## Folge, vorab festgelegt
- Gilt H78b, sagt Variante 2 in der Form von k174 für Fermionen eine richtungsabhängige Lichtgeschwindigkeit der Ordnung 1 voraus (quer zur Achse n das γ-fache). Messungen schließen Lorentz-Verletzung für Elektronen auf weit unter 10⁻¹⁰ aus (Zahl aus Vorwissen, im Ergebnis nachzuschlagen). Variante 2 wäre in dieser Form für Fermionen ausgeschlossen. Bei Photon-Gewichten hätten Fermionen keine Zeitentwicklung. Dann bleibt zu prüfen, ob eine andere Form der zweiten Lesart (zum Beispiel mit Abbildung auch der Koordinaten) die Isotropie erhält.
- Gilt H78a und H78c, ist Variante 2 für Skalare stabil und ohne Zerfall aus H76.

Skript: `llm/k194_zweite_lesart.py` (nach dem Commit dieser Notiz).
