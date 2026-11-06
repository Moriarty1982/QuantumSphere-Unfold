# Erkundung: I3 mit zugelassenem T-Zweig auf FRW. Mit festen Gewichten ist die Mischung ein einziges Fluid mit konstantem w = −b/(3a) und an der CMB ausgeschlossen; die Mischung bei gemeinsamer Rapidität bleibt unter Rotverschiebung nicht erhalten

**6. November 2026. Status: Erkundung, analytisch mit einer Abschätzung, ohne Kriterium.** Autorentscheidung (6.11.): T-Zweig als eigene Freiheitsgrade zugelassen (`Bestandsaufnahme_Wirkungsansaetze.md`). Ziel: Bevor das Gewicht b/a festgelegt wird, prüfen, ob I3 in der Form von k182/k183 auf einem expandierenden Universum überhaupt tragen kann.

## Vorwissen geprüft
- k182: M-Lesart gibt Staub (p = 0), T-Lesart reine Spannung (ρ = 0, p_T = −ρ₀/3, so dass bei a = b gilt ρ + 3p = 0).
- k183: Die Gravitation sieht a·T_M + b·T_T, also w = −b/(3a). Zerlegung in Staub und Λ: Ω_Λ = b/(3a); die Daten verlangen b/a ≈ 2,07.
- `Zurueckgestellte_Ideen.md`, I3: Die Spannung zu den Daten war schon vermerkt („ein rein ausrollendes Universum mit ρ + 3p = 0 gilt als ausgeschlossen“).
- H70: Versatz und Expansion.
- Vorwissen Kosmologie, nicht nachgeschlagen: Ω_b ≈ 0,05, Ω_c ≈ 0,26, Rekombination bei z ≈ 1090, dort Ω_c/Ω_b ≈ 5,4 nötig für die akustischen Spitzen.

## Befunde
1. **Feste Gewichte geben ein einziges Fluid, keinen Staub plus Λ.** T_M und T_T sind zwei Lesarten derselben Mischung mit derselben Dichte ρ₀. Beide skalieren also gleich mit der Expansion. Die Zerlegung „Ω_m + Ω_Λ“ aus k183 ist nur heute gültig; als Funktion der Zeit ist die Summe ein Fluid mit **konstantem w = −b/(3a)**. Sein „Λ-Anteil“ verdünnt sich mit derselben Rate wie der Staub-Anteil, ist also keine kosmologische Konstante.
2. **An der CMB ausgeschlossen (Abschätzung).** Soll dieses Fluid die ganze dunkle Komponente sein (Ω ≈ 0,95), so ist ρ_dunkel/ρ_b bei z = 1090 gleich (0,95/0,05)·(1091)^{3w}:

| b/a | w | Ω_Λ heute | dunkel/Baryonen bei z = 1090 |
|---|---|---|---|
| 1 | −⅓ | ⅓ | 1,7·10⁻² |
| 2 | −⅔ | ⅔ | 1,6·10⁻⁵ |
| 2,07 | −0,69 | 0,69 | 1,0·10⁻⁵ |

Nötig wären etwa 5,4. Für jedes b/a, das heute Λ erklären soll, fehlt die dunkle Materie zur Rekombination um Größenordnungen. **I3 mit festen Gewichten ist ausgeschlossen**, unabhängig davon, welche Begründung b/a hat.
3. **Die Mischung bei gemeinsamer Rapidität ist auf FRW nicht definiert.** In k182 trägt der normale Zweig k₁ = m sinh η und der tachyonische Zweig k₂ = m cosh η. Unter Rotverschiebung fallen beide Impulse wie 1/a. Ihr Verhältnis k₁/k₂ = tanh η bliebe dann fest, aber jedes einzelne k müsste sich mit η ändern. Das widerspricht sich: Die Mischung wird durch die Expansion zerstört. Der tachyonische Zweig erreicht bei k₂ → m die Schwelle (I4). Ein dynamisches Modell, wie sich Gewichte und Zweige mit der Expansion ändern, fehlt.

## Folge
- **I3 trägt nur, wenn die Gewichte oder die Zusammensetzung sich mit der Expansion ändern:** früh Staub (w ≈ 0), spät Spannung. Mit festen Gewichten (k183) ist I3 ausgeschlossen (Befund 2). Das gilt unabhängig von der Begründung des Gewichts b/a.
- Ein Test wäre erst sinnvoll mit einem **vorab festgelegten dynamischen Modell**: wie sich η (bzw. die beiden Zweige) unter Rotverschiebung entwickelt und wie die Gravitation die Zweige gewichtet. Daraus ergäbe sich w(z), und das wäre mit der Expansionsgeschichte zu vergleichen. Der naheliegende Kandidat ist I4-artig: Der T-Zweig läuft mit k₂ → m zur Schwelle, sein Druck ändert sich dabei. Unter H76 braucht der T-Zweig zudem einen Rahmen-Cutoff.
- Der Preis der Autorentscheidung (negative Energien, H76) steht, ohne dass I3 in der bisherigen Form einen Gewinn bringt.
