# Ergebnis H87: Wolfram bestätigt H86 unabhängig; die Steigung nähert sich π, aber langsamer als vorab angenommen

Vorab-Notiz `Vorab_Notiz_H87_Wolfram_Gegenprobe_Abfall.md`, Commit `61b7132` (nicht blind). Rechnungen über den Wolfram-Connector; Code in `k202_wolfram_gegenprobe.wl`.

## Ergebnisse
- **H87c bestätigt:** Wolfram liefert symbolisch C₀ = (a + b)/(2a), D₀ = (a − b)/(2a), α = (1 + x)/(2√x), β = (1 − x)/(2√x), |α|² − |β|² = 1; numerisch β/α = 0,53634, n = 0,40382.
- **H87a bestätigt:** Direkte Integration (WorkingPrecision 30) gegen k201 (scipy): relative Abweichungen 2,6·10⁻¹³, 7·10⁻¹¹, 5·10⁻⁹, 5·10⁻⁷ bei kΔ = 2, 4, 6, 8, alle unter 10⁻⁵. Der scipy-Wert bei kΔ = 8 ist der ungenaueste (5·10⁻⁷).
- **H87b widerlegt (wie formuliert):** Für große kΔ wurde entlang der Linie τ = x + ih (h = 0,9 bzw. 0,95 · πΔ/2, unterhalb der Singularität von sech² bei iπΔ/2) integriert. Die Randwerte bei Re τ → ±∞ sind dieselben, das Problem ist aber gut konditioniert. Gegenproben: kΔ = 4 und 8 wie auf der reellen Achse (3·10⁻¹⁰ bzw. 2·10⁻¹⁰), beide Linien stimmen auf ≤ 1,5·10⁻⁸ überein.

| kΔ | 10 | 15 | 20 | 25 | 30 |
|---|---|---|---|---|---|
| |C| | 4,230·10⁻¹² | 1,879·10⁻¹⁸ | 8,942·10⁻²⁵ | 3,765·10⁻³¹ | 1,304·10⁻³⁷ |

Lokale Steigungen 2,925; 2,912; 2,936; 2,975. Zwischen kΔ = 20 und 30: 2,956, also 5,9 % unter π (Kriterium 3 %).

## Nachträglich (nicht vorregistriert)
- Die lokale Steigung steigt im Bereich 15–30 langsam an. Ein Fit ln|C| = c₀ + p·ln(kΔ) − s·kΔ gibt s = 3,150 (exakt durch die Punkte 20, 25, 30; 0,3 % über π) mit p ≈ 4,8 bzw. s = 3,077 (kleinste Quadrate 15–30; 2 % unter π) mit p ≈ 3,0. Das ist mit einem Abfall e^{−πkΔ} und einem großen Potenzvorfaktor (kΔ)^p verträglich; die Lage der Singularität bei iπΔ/2 legt den Exponenten fest, der Vorfaktor hängt an der Stärke L = ln(a/b) − iπ und ist nicht störungstheoretisch (die erste Bornsche Näherung lag bei kΔ = 8 um den Faktor 2,2 daneben).
- Eine Bestätigung bräuchte einen neuen Vorab-Test, etwa mit vorab festgelegtem Fit-Modell und Bereich bis kΔ ≈ 60.

## Folge
- Die Zahlen aus H86 sind von einem zweiten, unabhängigen System bestätigt.
- Der Abfall der Beimischung ist exponentiell mit einer Rate nahe π je Einheit kΔ; die Abschneideskala ist damit etwa 1/(πΔ), mit einem Potenzvorfaktor, der den Übergang zum asymptotischen Verhalten bis über kΔ ≈ 30 hinauszieht. Δ bleibt frei.
