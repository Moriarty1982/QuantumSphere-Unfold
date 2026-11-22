# Vakuumhintergrund als Träger des gerichteten OP5-Vermittlers: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** In einem Lorentz-invarianten Vakuum gibt keine Ableitungskopplung eines neuen Feldes an |Φ|² einen Pol (Proca
und Fierz–Pauli liefern nur Kontaktterme), und die Skalarkopplung X|Φ|² gibt einen ungerichteten Pol. Mit einem Hintergrund aus Rahmen u
und Achse n lässt sich der Zähler N_m = ⅔(x² − a_⊥x + a_⊥²) exakt erreichen: durch ein Spin-2-Feld auf dem Unterraum senkrecht zur Achse
mit positiver Polarisationssumme. Die Summe ist aber nicht eindeutig (zweiparametrige Familie), und Achse wie Rahmen sind gesetzt.
**Nach dem vorab festgelegten Raster: trägt teilweise.**

Auftrag des Autors: „weg b“. Verfahren vorab: `Methoden_Notiz.md` (Commit 9f91c274). Skript `background_mediator.wl`, Ausgabe
`run/background_mediator.txt`, Wolfram exakt. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| (1) Lorentz-invariant | Spin 0 (X\|Φ\|²): Pol mit konstantem Zähler, nicht gerichtet. Spin 1 (X_μ∂^μ\|Φ\|², Proca): Zähler p²(p² − M²)/M², am Pol null; Austausch = Kontaktterm −p²/M². Spin 2 (X_μν∂^μ∂^ν\|Φ\|², Fierz–Pauli): Zähler ⅔(p²)²(p² − M²)²/M⁴, doppelte Nullstelle am Pol. |
| (2) Hintergrund, Spin 1 | Polarisationen nur quer zur Achse: Zähler a_⊥ (wie im Materialweg r35). |
| (2) Hintergrund, Spin 2 | Bausteine: TT → x², B (Zeit–quer) → 2a_⊥x, G (quer spurfrei) → a_⊥²/2, D (quer Spur) → a_⊥²/2, E (TT–Spur-Mischung) → 2a_⊥x. Rein quer: a_⊥²/2 bzw. a_⊥². |
| (2) N_m exakt | α = ⅔, γ = (4 − 3δ)/3, ε = −(1 + 3β)/3. Positiv genau für 0 ≤ β < ⅓ und (1 + 3β)²/3 ≤ δ ≤ 4/3, oder β = ⅓, δ = 4/3. Am Randpunkt γ = 0, ε = −⅔, und der TT–Spur-Block hat Rang eins. |
| (2) Lorentzsch (2+1) | Die Summe mit der Metrik des Unterraums gibt (1 − c)(x − a_⊥)²; N_m − ⅔(x − a_⊥)² = ⅔a_⊥x. |

## Lesart
- Notwendige Bedingung, jetzt gerechnet: Ein gerichteter Pol braucht in jedem Fall einen Hintergrund. Im Lorentz-invarianten Vakuum
  koppeln Ableitungen nur an longitudinale Anteile, deren Pol sich weghebt.
- Mit Hintergrund ist die Form von N_m erreichbar, auch mit der Potenz a_⊥², die dem Materialweg fehlt (r35). Die negative Mischung
  −a_⊥x entsteht aus einer Kopplung zwischen der Zeit-Zeit-Komponente und der Querspur des Feldes.
- Gesetzt bleiben: Rahmen u und Achse n, die Polarisationsstruktur (β, δ in einer Familie) und eine Wirkung, die genau diese Summe erzeugt.
  Als Kandidaten für den Hintergrund nennt der Bestand die Strömung und den Spinvektor des OP5-Keims (k168, Spin entlang φ̂) und das
  raumartige Tachyonbild eines ruhenden Materiezustands (k185); beide sind Lesart, keine Herleitung.
- OP5 und H96 bleiben offen.
