# Vorab-Notiz H92: Der Vorfaktor der Urknall-Beimischung ist eine universelle Funktion r(λ) des lokalen Problems an der Singularität, λ = L·kΔ/2

**Stand:** 6. November 2026, vor der Rechnung festgelegt. Autor (6.11.): „Vorfaktor analytisch“ (Option a nach H91). **Teilweise nicht blind:** Die Daten C(kΔ) aus H91 sind bekannt (`k206_out.json`). Die lokale Funktion r(λ) ist noch nicht gerechnet, und ihr Vergleich mit C ist offen.

## Vorwissen geprüft
- `Ergebnis_H85…`, `Ergebnis_H86…` (k201): Gleichung (w y')' + k² w y = 0, w = e^{L s}, s = ½(1 + tanh(t/Δ)), L = ln(a/b) ∓ iπ.
- `Ergebnis_H87…` (k202): Erste Bornsche Näherung bei kΔ = 8 um den Faktor 2,2 daneben, Vorfaktor „nicht störungstheoretisch“.
- `Ergebnis_H91…` (k206): |C| bis kΔ = 60 auf 10⁻¹⁰, lokale Steigung wellig, glatte Fits (Potenz, √x) tragen nicht; |C₊| = |C₋| auf 10⁻¹⁰ (nachträglich, ohne Herleitung). Der Hinweis dort, „lokales Problem am Pol, Stokes-Konstante“, ist der Ansatz hier.
- Suche nach „Born“, „Stokes“, „Pokrovskii“, „Überbarriere“ in `llm/*.md`: sonst kein Vorbefund (die Stokes-Treffer in der Kernkarte betreffen die Polarisation).

## Herleitung (vor der Rechnung)
Die nächste Singularität von s in der oberen Halbebene liegt bei t₀ = iπΔ/2. Dort gilt s ≈ ½ + Δ/(2τ) mit τ = t − t₀, also w ≈ e^{L/2}·e^{β/τ}, β = LΔ/2. Das ist eine **wesentliche Singularität** von w, nicht nur ein Pol von w'/w. Das lokale Problem ist y'' − (β/τ²)y' + k²y = 0. Mit σ = kτ wird daraus
  y_σσ − (λ/σ²) y_σ + y = 0,  λ = βk = L·kΔ/2,
mit **einem** komplexen Parameter λ. Die reelle t-Achse liegt bei Im σ = −πkΔ/2, also unterhalb der Singularität σ = 0. Läuft von links e^{iσ} ein und wird unterhalb von σ = 0 nach rechts fortgesetzt, so entsteht y → e^{iσ} + r(λ) e^{−iσ}. Wegen e^{±iσ} = e^{±ikt}e^{∓ikt₀} folgt
  **C ≈ r(λ)·e^{2ikt₀} = r(L kΔ/2)·e^{−πkΔ}.**
Der Exponent π folgt aus der Lage der Singularität. Der ganze Vorfaktor ist |r(λ)|, eine Funktion des Produkts L·kΔ allein. Die Korrekturen kommen von der Näherung s ≈ ½ + Δ/(2τ). Sie sind von relativer Ordnung (|L|/kΔ)^{1/2}, gehen also langsam gegen 0. Für kleines λ gibt die erste Bornsche Näherung r ≈ 2πλ, in Übereinstimmung mit der Bornschen Näherung des vollen Problems (C ≈ πL kΔ e^{−πkΔ}).

## Rechnung
`llm/k207_lokales_problem.py` (Python/scipy). Integration der lokalen Gleichung entlang σ = s − ih, h > 0, von s = −S bis S. Anfangs- und Auswertewerte kommen aus der asymptotischen Reihe y = e^{±iσ}(1 + Σ aₙσ^{−n}), aₙ rekursiv aus der Gleichung, damit die langsamen 1/σ-Ausläufer keinen Fehler geben. Kontrolle: zwei verschiedene h und zwei verschiedene S stimmen überein. Vergleich mit den k206-Werten C(kΔ) für kΔ = 10, 12,5, …, 60, beide Drehsinne.

## Hypothesen und Kriterien
- **H92a (Universalität):** R(kΔ) := |C(kΔ)|·e^{πkΔ}/|r(L kΔ/2)| geht gegen 1. Kriterium: Ein Fit ln R = a₀ + a₁(kΔ)^{−1/2} + a₂(kΔ)^{−1} auf [20, 60] gibt |a₀| ≤ 0,05 (beide Drehsinne).
- **H92b (Wellen erklärt):** Der Rest dieses Fits hat rms ≤ 5·10⁻³ (die glatten Fits in H91 hatten 2·10⁻²). Die Wellen der lokalen Steigung stecken also in r(λ).
- **H92c (Drehsinne):** |r(λ̄)| = |r(λ)| relativ auf ≤ 10⁻⁸ für die λ beider Drehsinne (Herleitung der H91-Beobachtung |C₊| = |C₋|, soweit sie aus dem lokalen Problem folgt).
- **H92d (Born-Grenzfall):** |r(λ)/(2πλ) − 1| ≤ 10⁻² für |λ| = 10⁻³ (Kontrolle der Normierung).
- Gültigkeit: Konturen- und S-Kontrolle stimmen relativ auf ≤ 10⁻⁶; sonst gelten a–d als ungültig.

## Umgang mit Abweichungen
Wenn a verfehlt wird, b aber erfüllt ist, stimmt die Form, die Normierung aber nicht (Kandidat: Faktor aus der Konstante e^{L/2} oder aus der zweiten Singularität bei −iπΔ/2). Das wird offengelegt und nicht nachträglich angepasst. Die Asymptotik von r(λ) für großes λ (WKB, Umkehrpunkte des Pols vierter Ordnung, Term ∝ √λ) ist hier nicht Teil des Tests. Sie folgt als Erkundung.
