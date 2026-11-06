# Ergebnis H92: Der Vorfaktor ist die Stokes-Funktion r(λ) des lokalen Problems: Wellen erklärt (b), Drehsinne (c), Born-Grenzfall (d); die Normierung verfehlt (a) um einen festen Faktor ≈ 0,54

Vorab-Notiz `Vorab_Notiz_H92_Vorfaktor_lokales_Problem.md`, Commit `c347a92` (teilweise nicht blind). Code `k207_lokales_problem.py` (Python/scipy), Ausgaben `k207_out.json` (Lauf 2), `k207_out_lauf1.json` (Lauf 1) und `k207_erkundung_gross.json`.

## Offenlegung: zwei Läufe
- **Lauf 1 ungültig nach der Gültigkeitsbedingung.** Die Kontrolle (größte relative Änderung von r unter Weg 1,5·h und Rand 2·S) war 3,7·10⁻⁶ bzw. 5,5·10⁻⁶ und lag damit über 10⁻⁶.
- **Ursache:** Allein der Weg mit 1,5-fachem h verliert Stellen, weil der reflektierte Anteil dort um e^{−2h} kleiner ist. Doppeltes S ändert r um ≤ 6·10⁻¹⁰, 0,7-faches h um ≤ 5·10⁻¹¹ (bei kΔ = 20 und 60).
- **Lauf 2** mit der Kontrolle 0,7·h statt 1,5·h (nach Kenntnis von Lauf 1 geändert): Kontrolle ≤ 6·10⁻¹⁰, gültig. Die Werte r selbst sind in beiden Läufen identisch (gleicher Hauptweg), damit auch alle Zahlen unten.

## Ergebnisse (Lauf 2)
- **H92d bestätigt:** r(λ)/(2πλ) = 1 − 1,6·10⁻⁸ bei |λ| = 10⁻³. Die Normierung des lokalen Problems stimmt mit der Bornschen Näherung überein.
- **H92c bestätigt:** |r(λ̄)| = |r(λ)| für die λ beider Drehsinne auf 8·10⁻¹¹ (in ln|r|). Die Gleichheit |C₊| = |C₋| aus H91 folgt damit aus dem lokalen Problem, soweit es trägt. Eine geschlossene Herleitung der Symmetrie von r fehlt weiterhin.
- **H92b bestätigt:** ln R = ln|C| + πkΔ − ln|r(L kΔ/2)| ist glatt. Der Rest des Fits a₀ + a₁(kΔ)^{−1/2} + a₂(kΔ)^{−1} auf [20, 60] hat rms 4,1·10⁻³ (Kriterium 5·10⁻³; die glatten Fits an ln|C| in H91 hatten 2·10⁻²). Die Wellen der lokalen Steigung stecken in r(λ).
- **H92a verfehlt:** a₀ = −0,497 (Kriterium |a₀| ≤ 0,05). R geht nicht gegen 1, sondern bleibt bei ln R ≈ −0,62 (kΔ = 40–60: −0,6196 … −0,6222).

## Nachträglich (nicht vorregistriert)
- **Fehlender Faktor e^{−L/2}.** In der Vorab-Notiz war er als Kandidat genannt, ist aber nicht eingesetzt. Für (w y')' + k²w y = 0 tragen die adiabatischen Wellen die Amplitude w^{−1/2}. Im vollen Problem ist w links 1 und rechts e^L, im lokalen Problem auf beiden Seiten e^{L/2}. Bei der Umrechnung kommt C ≈ r(λ)·e^{−L/2}·e^{−πkΔ} heraus, also ln R → −Re L/2 = −0,599. Die Daten (−0,62 bei 40–60) passen dazu bis auf ≈ 0,02. Je nach Fit-Modell liegt der Grenzwert zwischen −0,53 und −0,63 (Rest ≈ 10⁻³, bei 1/√x-Korrekturen nicht genauer). Das ist eine nachträgliche Erklärung, keine Bestätigung.
- **Erkundung: Wurzelgesetz von r.** Die lokale Funktion allein, bis kΔ = 200 gerechnet (Kontrolle ≤ 10⁻⁸):

| kΔ | 40 | 60 | 80 | 100 | 140 | 200 |
|---|---|---|---|---|---|---|
| ln|r| | 11,43 | 14,03 | 16,20 | 18,10 | 21,42 | 25,59 |

  Ein Fit ln|r| = c√(kΔ) + d gibt c = 1,810, d = −0,005 (rms 7·10⁻³). Mit Logarithmus-Term ergibt sich c = 1,79. Also |r| ≈ e^{1,81√(kΔ)}. Der Kandidat |√L| = 1,834 liegt 1–2 % daneben, entschieden ist er nicht. Damit ist die lokale Steigung π − c/(2√(kΔ)): bei kΔ = 60 gibt das 3,025 (gemessen 3,026), bei 25 gibt es 2,96 (gemessen 2,95).

## Folge
- **Die Frage aus H91 ist strukturell beantwortet:** Der Exponent ist exakt π, aus der Lage der Singularität t₀ = iπΔ/2. Die scheinbar zu kleine Steigung kommt von einem Vorfaktor, der wie e^{≈1,8√(kΔ)} wächst. Er ist die Stokes-Funktion der wesentlichen Singularität von w = e^{Ls} und hängt nur von λ = L kΔ/2 ab, bis auf einen festen Faktor (Kandidat |e^{−L/2}|) und Korrekturen, die mit kΔ abnehmen.
- Für die Physik bleibt es dabei: Die Beimischung verschwindet oberhalb von etwa 1/(πΔ), Δ ist frei. Der Vorfaktor verschiebt die Abschneideskala nur logarithmisch.
- Offen und ein möglicher nächster Vorab-Test: der Grenzwert ln R → −Re L/2 (mit einer Korrektur der lokalen Näherung erster Ordnung) und der Koeffizient c des Wurzelgesetzes aus einer WKB-Rechnung am Pol vierter Ordnung, beides vorab hergeleitet statt gefittet.
