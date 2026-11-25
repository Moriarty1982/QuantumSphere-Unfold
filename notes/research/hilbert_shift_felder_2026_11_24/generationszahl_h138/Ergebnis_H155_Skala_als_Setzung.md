# Ergebnis H155: Mit gesetzter Skala hält die Tauschsymmetrie K = ⅔ ohne schweres U′; das Laufen stört erst in zweiter Ordnung; δ = 2/9 bleibt ein Parameter

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H155_Skala_als_Setzung.md` (Commit 9d6b6ca; a nicht blind). Skripte `k338_skala.py` (`k338_out.txt`), `k338b_gegenprobe.wl`
(`k338b_out.txt`, Wolfram). Status: H155a, b bestätigt; H155c widerlegt (zugunsten von Koide); H155d nach Wortlaut widerlegt (ein Treffer über der Zufallserwartung, der in δ aber
63σ danebenliegt). Ein nachträglicher Zusatz ist als Erkundung markiert.**

Anlass: Autor „dann probiere die skala“. Für diesen Zweig ist damit entschieden: Skala als Setzung. Werkzeuge: Python (sympy für N(W), β-Funktionen mit Massentermen und die
Aufhebung erster Ordnung; scipy für Minima und Fluss), Wolfram unabhängig (dieselben symbolischen Reste, zwei Fenster, ein Minimum mit ζ, der Zusatz mit WorkingPrecision 30).
Alle gemeinsamen Werte stimmen überein. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H155a | μ_A² = μ_B² = μ² < 0, λ_A = λ_B: Minimum A = B = −μ²/(2λ + κ), also θ = π/4, K = ⅔; Massenquadrate 0 (U′, Goldstone), −4μ², 4μ²(κ − 2λ)/(κ + 2λ) | symbolisch | **bestätigt** (nicht blind) |
| H155b | ζN(W) gibt U′ Masse, verschiebt aber K: (K − ⅔)/m²_U′ = 0,058 (κ = −λ) bzw. 0,52 (κ = +λ); bei m²_U′ = 0,90\|μ²\| ist K − ⅔ = 0,046; 0 von 16 Punkten mit m²_U′ ≥ \|μ²\| und \|ΔK\| < 1,5·10⁻⁵ | 0 Punkte | **bestätigt** |
| H155c | Fenster mit n_B = 2: 22 von 48 Fällen innerhalb 3σ; erste Ordnung in L hebt sich exakt auf (Massen- gegen Quartiklauf); L_max von 0,33 (λ = 0,2, κ = λ) bis 11,5 (λ = 0,05, κ = −λ) | Vorhersage: jedes Fenster > 0 verfehlt | **widerlegt** |
| H155d | Term sechster Ordnung erlaubt innere δ für R ∈ [−0,0282; 0,164]; δ = 2/9 genau bei R* = −0,0075807; bekannte Skalen: 1 Treffer in 196 (ζ = −Σm_ℓ, Λ = v: R = −Σm_ℓ/v, +0,89 %), Zufallserwartung 0,06; dieses R gibt δ = 0,221844, 63σ neben 0,222225 | kein Treffer über Zufall | **nach Wortlaut widerlegt**; als Herleitung kein Treffer |

## Lesart
- **Mit Skala braucht K = ⅔ kein schweres U′.** Sind Massen- und Quartikterme tauschsymmetrisch, liegt das Minimum bei θ = π/4 für jedes μ² < 0 und −2λ < κ < 2λ.
  U′ bleibt dabei ein Goldstone. Die gesetzte Größe ist die Tauschsymmetrie selbst (μ_A² = μ_B², λ_A = λ_B), nicht mehr ein Startwert im Fluss.
- **U′ schwer machen kostet K.** Der einzige algebraische Term, der die Ebenen-Drehung bricht, ist die kubische Norm ζN(W). Sie ist nicht tauschsymmetrisch, und Masse
  von U′ und Verschiebung von K wachsen gemeinsam. Ein U′ so schwer wie die Skala würde K um einige Prozent verschieben.
- **Das 1:2-Problem schrumpft von erster auf zweite Ordnung (nicht vorhergesagt).** Läuft der Fluss mit zwei Ebenenrichtungen, laufen Massenterm und Quartik so, dass sich
  ihre Wirkung auf θ in erster Ordnung exakt aufhebt (symbolischer Nullrest, Python und Wolfram). Übrig bleibt ein Effekt der Ordnung (λL/16π²)². Für kleine Kopplungen
  bleibt K je nach Kopplung über Fenster bis zu einem Faktor 1,4 bis 10⁵ in der Skala innerhalb 3σ. Skalenfrei (H150) war die Verschiebung dagegen 0,005 und mehr. Das gilt für das
  logarithmische Laufen. Mit harter Abschneidung (H150b) oder Schwellenkorrekturen schwerer Felder verschiebt sich θ dagegen schon in erster Ordnung.
- **δ: der Term sechster Ordnung hilft, legt 2/9 aber nicht fest.** Auf θ = π/4 hängt das Minimum von ζN + N²/Λ² nur an R = ζΛ²/v³. Für |cos 3δ| < 1 gibt es drei
  verschiedene Massen. δ = 2/9 verlangt R* = −0,0075807 (wie H149e), also genau einen Parameter, und das ist ein Fit. Unter den bekannten Skalen liegt R = −Σm_ℓ/v 0,89 %
  daneben, bei Zufallserwartung 0,06 Treffern. In δ sind das aber 63σ, also kein Treffer im Sinne einer Herleitung. Dass gerade die Summe der Leptonmassen auftaucht,
  ist zudem nicht unabhängig vom Ziel.

## Nachträglich (Erkundung, nicht in der Vorab-Notiz)
Mit dem Fit-Wert R* (Λ = v) wurde das volle Potential minimiert. Ergebnis: K bleibt ⅔ (Wolfram |ΔK| < 10⁻¹⁵), und δ = 2/9. Grund: Liegt δ im Inneren, gilt ∂V/∂N = 0, und die
kubische Norm drückt θ nicht mehr weg. Das Minimum ist zweifach entartet: δ = 2/9 mit Σc > 0 und δ = 0,29713 mit Σc < 0 (dort tritt N mit umgekehrtem Vorzeichen auf).
Mit Skala reproduziert der Ansatz also alle drei Leptonmassen aus der gesetzten Tauschsymmetrie, der Skala und einem angepassten Parameter. Das sind so viele Eingaben wie
Koide plus Brannen-Phase. Neu ist nur, dass beide Größen aus einem Potential kommen, das sie zugleich stabil hält.

## Bilanz der Setzungen (H150 bis H155)
- Skalenfrei (H150 bis H154): K hängt am Startwert; K = ⅔ nur mit n_B = 1, und das erzwingt die Algebra nicht.
- Mit Skala (H155): K = ⅔ folgt aus der Tauschsymmetrie des Baumgraph-Potentials und überlebt das Laufen bis zur zweiten Ordnung. Gesetzt sind die Skala und die
  Tauschsymmetrie der Terme. δ ist ein angepasster Parameter (R*).
- Die offene Wahl ist damit von „Startwert“ zu „Tauschsymmetrie der Massenterme“ gewandert. Ob die Algebra die Gleichheit μ_A² = μ_B² verlangt, ist die nächste Frage.

## Grenzen
- Eine Schleife, logarithmisches Laufen ohne Schwellenkorrekturen; die Entkopplung ist scharf am Fensterende. H150b (harte Abschneidung) bleibt als Gegenbefund stehen.
- Die Normierung von N(W) folgt r13/k255; R hängt an ihr.
- Bekannte Skalen wie in der Vorab-Notiz; v = 246,22 GeV setzt voraus, dass Ψ das elektroschwache Feld ist (Lesart).
- OP3 offen; die Vorzeichen von μ², ζ, κ sind nicht gesetzt (beide gerechnet; Kondensat nur für μ² < 0); kein Guard berührt.
- Vergeben: H155, k338. Nächste frei: H156, k339.
