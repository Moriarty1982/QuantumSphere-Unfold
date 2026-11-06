# Erkundung: Die beiden Drehsinne am Urknall-Übergang sind exakt konjugiert: |C₊| = |C₋| und die Produktregel aus H86 folgen

**6. November 2026. Status: Erkundung, analytisch hergeleitet, numerisch kontrolliert (`k211_symmetrie_drehsinne.py`, Ausgabe `k211_out.txt`), ohne Kriterium.** Der Autor sagte „erst weiterrechnen“; es ging um den offenen Punkt „exakte Herleitung von |r(λ̄)| = |r(λ)|“ (H92c) bzw. |C₊| = |C₋| (H91, nachträglich).

## Vorwissen geprüft
- H86: |C| ist für beide Drehsinne gleich. |D₊| ≠ |D₋|, aber √(|D₊||D₋|) = √(b/a) adiabatisch auf 10⁻¹³ und ≈ D₀ bei langen Wellen (auf 0,2–0,5 %). Das ist ohne Herleitung geblieben.
- H91 (|C₊| = |C₋| auf 10⁻¹⁰, nachträglich), H92c (|r(λ̄)| = |r(λ)| auf 8·10⁻¹¹), H94 (Norm N±, Drehsinne asymmetrisch).
- Keine Notiz enthält eine Herleitung.

## Herleitung
Die Gleichung ist (w y')' + k² w y = 0 mit w = e^{L s(t)}, s = ½(1 + tanh(t/Δ)), L = ln(a/b) ∓ iπ, also L₋ = L̄₊. Transfermatrix M(L) in der Basis (e^{ikt}, e^{−ikt}): Die erste Spalte ist der Ausgang für den Eingang e^{ikt}, also (D, C); die zweite der für e^{−ikt}, also (b, d).
1. **Wronski-Determinante:** W = w(y₁y₂' − y₂y₁') ist konstant, w ist links 1 und rechts e^L, also det M = e^{−L}.
2. **Dualität:** v = w y' löst (w^{−1}v')' + k² w^{−1}v = 0, also die Gleichung mit −L, wobei rechts der konstante Faktor e^L hinzukommt. Daraus folgt M(−L) = e^L·J M(L) J mit J = diag(1, −1).
3. **Spiegelung und Konjugation:** Mit s(−t) = 1 − s(t) löst f(t) = conj y(−t) die Gleichung mit −L̄ (bis auf einen konstanten Faktor von w). Links hat f die konjugierten rechten Koeffizienten von y, rechts die linken. Daraus folgt M(−L̄) = conj(M(L))^{−1}.
4. **Zusammen:** M(L̄) = e^{−L̄} J conj(M(L))^{−1} J = [[d̄, b̄], [c̄, ā]] für M(L) = [[a, b], [c, d]].

## Folgen
- **C(L̄) = conj C(L).** Also gilt |C₊| = |C₋| exakt, für jedes kΔ und jedes Profil, das s(−t) = 1 − s(t) erfüllt.
- **D₋ = conj(d₊)** und aus det M = e^{−L}: **D₊·conj(D₋) − b₊C₊ = e^{−L₊}**. Adiabatisch (b, C → 0) folgt |D₊||D₋| = e^{−Re L} = b/a: Das ist die Produktregel aus H86, jetzt exakt mit Korrekturterm b₊C₊.
- **Lokales Problem (H92):** Dort ist M = [[1, 0], [r, 1]] exakt. Die Lösung e^{−iσ} ist unterhalb der Singularität subdominant und lässt sich weit nach unten verschieben, wo die Gleichung frei wird; daher b = 0 und d = 1, mit det = 1 dann a = 1. Daraus folgt **r(λ̄) = conj r(λ)**, also H92c exakt.

## Numerische Kontrolle (k211, tanh, Δ = 2, kΔ = 0,01, 0,3, 1, 2, 5)
| Identität | größte relative Abweichung |
|---|---|
| det M = e^{−L} | 1·10⁻¹² |
| M(L̄) = [[d̄, b̄], [c̄, ā]] | 6·10⁻¹³ |
| C₋ = conj C₊ | 3·10⁻¹⁰ |
| D₊ conj(D₋) − b₊C₊ = e^{−L} | 1·10⁻¹² |

Das lokale Problem gibt zusätzlich a = d = 1 auf 10⁻¹⁰, b ≈ 10⁻¹⁷, und c(λ̄) = conj c(λ) bei kΔ = 2 und 10.

Nebenbei beobachtet: |b₊| = |C₊| an allen fünf Punkten. Plausibel ist, dass das aus der Spiegelung t → −t allein folgt. Geprüft ist das nicht.

## Lesart
Die beiden Drehsinne des komplexen Übergangs sind einander exakt konjugiert. Die Asymmetrie der |D±| (H86d) und der Norm N± (H94) ist reell und folgt aus der Determinante e^{−L}, deren Phase vom Drehsinn abhängt. Die Beimischung C, also die physikalisch maßgebliche Größe, hängt nicht vom Drehsinn ab. Damit ist der letzte offene Punkt aus H86, H91 und H92 geschlossen.
