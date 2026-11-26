# Ergebnis H167: Mit der Ladungsmischung c = 1 gibt der Spin-1-Term allein den Oktanten; die Phase legen dimensionslose Terme fest, die Skala wählt den Zweig und hebt das Elektron

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H167_Skala_Setzung_Dipol.md` (Commit c968be9; a, b, c, d2 nicht blind, d1 blind). Skripte `k362_test_h167.py` (`k362_out.txt`),
`k362b_gegenprobe.wl` (`k362b_out.txt`, Wolfram), nachträglich `k362c_nachtrag_ordnung6.py` (`k362c_out.txt`, nur Python).
Status: H167a, b, c, d2 bestätigt (nicht blind); H167d1 bestätigt (kein Treffer).**

Anlass: Autor, 26.11.2026: „zuerst setzen und dann schauen was sich daraus ergibt, vielleicht finden wir dann einen grund wieso es skalenfrei sei muss“.
**Gesetzt sind hier: die Skala, das Postulat J in der Ebenen-Lesart, und c = 1 (Projektor-Lesart aus r42; nach k278 offen).** Werkzeuge: Python (sympy, numpy,
scipy), Wolfram unabhängig; gemeinsame Werte stimmen überein (ρ* auf 10 Stellen). Wolfram meldete nur `Symbol::undefined2` und `N::meprec` beim Vergleich gleicher
Ausdrücke. Qiskit nicht eingesetzt.

## Kontrollen
Volles V(A, B, δ) mit μ² = −1, λ = 1, κ = 0,5, drei Parametersätze: |K − ⅔| ≤ 1,2·10⁻⁹; δ gegen die Formel ≤ 2,4·10⁻⁸ (Schranken 10⁻⁹ und 10⁻⁷; die erste ist
im ersten Satz um 0,2·10⁻⁹ überschritten, Genauigkeit des Minimierers).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H167a | Tr(W∘σW) = 3a² + 6r² cos 2δ; (1 + c²)v² = r² sin²(δ − χ); V_δ = X cos 2δ + Y sin 2δ. α′ = 0: δ ∈ {0, π/6}, π/3 für jedes c. α = 0, c = 1: gefaltet **π/12 und π/4**; det W = −½ + cos 3δ/√2 ist bei π/12 null | Nullreste, Python = Wolfram | **bestätigt** (nicht blind) |
| H167b | r² cos 2δ ist unter A ↔ B nicht invariant, A²r² cos 2δ ist es; bis Ordnung 4 gilt V(−A) = V(A) und V(δ + π) = V(δ); A³B³ cos 3δ ist ungerade. Zweige: Wurzeln (0; 0,634; 2,366) gegen (−0,366; 1,366; 2) | symbolisch; numerisch | **bestätigt** (nicht blind; eine Kontrollschranke knapp überschritten) |
| H167c | Exponent von m_e/m_τ in α/α′: 2,0013; δ − π/12 = −½ arctan(α/α′) | 2,00 ± 0,05 | **bestätigt** (nicht blind) |
| H167d2 | Oktant-Zweig: ρ* = α/α′ = ±tan(π/6 − 2δ*) = ±0,0793204104 | 0,05 < \|ρ*\| < 0,12 | **bestätigt** (nicht blind) |
| H167d1 | 42 Kandidaten gegen 6 Zielverhältnisse (±0,0793204; ±1,4530942; ±2,0998654): 0 Treffer; nächster 1/(4π), relativ 3,2·10⁻³ | kein Treffer vorhergesagt | **bestätigt** |

## Lesart
- **Woher der ungerade Beitrag kommt.** Die Algebra hat zwei Terme, die δ sehen (k282): den Konjugationsterm (cos 2δ) und den Spin-1-Term, der Spin 1 von
  Spin 2 trennt (H128: Verhältnis 9/10). Mit Ladungsmischung c ist der Spin-1-Term um χ = arctan c gegen die Konjugation verdreht: cos 2(δ − χ). Das ist der
  σ-ungerade Dipol aus H166. Er braucht keine neue Zutat, nur c ≠ 0.
- **Mit c = 1 gibt der Spin-1-Term allein den Oktanten.** δ liegt dann bei π/12 oder π/4. δ = π/12 ist der Oktant aus r12: det W = 0, das Elektron ist masselos,
  m_μ/m_τ = 0,0718. Der Oktant war bisher eine Eingabe aus der Spin-½-Geometrie; hier folgt er aus c = 1 und dem Spin-1-Term. Das hängt an c = 1, und das ist gesetzt.
- **Die Phase ist skalenfrei bestimmt.** Unter J ist bei Ordnung 2 nur die Norm erlaubt. Die Terme, die δ festlegen, haben Ordnung 4 und sind dimensionslos.
  Eine gesetzte Skala ändert die Phase in dieser Ordnung nicht.
- **Was die Skala tut.** Bis Ordnung 4 ist das Potential gerade in A. Die Minima δ und δ + π sind exakt entartet, haben aber verschiedene Spektren (Oktant gegen
  einen Zweig mit negativer Wurzel). Erst ein Term sechster Ordnung, also 1/Λ², wählt. Skalenfrei bleibt das Vakuum zweideutig.
- **Die Elektronmasse misst ein kleines Verhältnis.** Mit Konjugationsterm: δ = π/12 − ½ arctan(α/α′), m_e/m_τ ∝ (α/α′)², und die Leptonen verlangen
  α/α′ = 0,0793204. Der Fit R* aus H155 ist damit durch ρ* ersetzt; hergeleitet ist ρ* nicht (kein Treffer in der Liste).

## Nachträglich (Erkundung, nicht in der Vorab-Notiz; k362c, nur Python)
- Der Term sechster Ordnung, der den Zweig wählt, hebt zugleich das Elektron. Mit c = 1, α = 0 und q = β₃v₀²/Λ² liegt das globale Minimum für q/α′ < 0 am
  Oktant-Zweig, verschoben um einen Betrag ∝ q/α′; δ* verlangt q/α′ = −0,0852479. Für q/α′ > 0 liegt es am anderen Zweig.
- Damit gibt es in diesem Aufbau eine Aussage zur Frage des Autors: **Skalenfrei (Λ → ∞, ohne Konjugationsterm) ist das Elektron masselos und der Zweig
  unbestimmt.** Die Elektronmasse wäre dann das Maß für die Skala, m_e/m_τ ∝ (v₀/Λ)⁴. Das spricht in dieser Lesart für eine Skala, nicht gegen sie.
  Offen ist, ob stattdessen der Konjugationsterm das Elektron hebt; die Daten trennen die beiden Wege nicht.
- Der Kontrolllauf mit β₃ = −0,02 gab zufällig δ = 0,22286; das ist kein Befund, der Wert war willkürlich.
- Ohne Konjugationsterm und ohne Ordnung 6 bräuchte δ* die Mischung c* = 0,9238205. cos(π/8) = 0,9238795 liegt nahe (vor der Rechnung gesehen), gibt aber
  δ = 0,2222539, also 3,2·10⁻⁵ daneben bei einer Unsicherheit von 4·10⁻¹⁰. Kein Treffer.
- 1/(4π) liegt 0,32 % neben ρ*; in δ sind das 1,3·10⁻⁴, ebenfalls kein Treffer.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H166 | nichts Neues | Ziel δ*; δ = σ-ungerader Dipol | Dipol gegen Quadrupol |
| H167 | Skala, J (Ebenen-Lesart), c = 1 | Oktant aus dem Spin-1-Term; Phase aus dimensionslosen Termen; Skala wählt den Zweig | (i) warum c = 1; (ii) ein kleines Verhältnis: α/α′ = 0,0793 oder β₃v₀²/(α′Λ²) = −0,0852; (iii) Vorzeichen von α′ und β₃ |

Geprüft: Das Ziel δ* ist eine Messgröße (H166). Die Zerlegung in Konjugations- und Spin-1-Term ist die aus k282; für c = 0 fallen beide zusammen, die Frage
entsteht also erst mit c ≠ 0. Weggabelung für den Autor: Elektronmasse aus dem Konjugationsterm (dimensionslos, Majorana-artig nach k282) oder aus der Skala (Ordnung 6).

## Grenzen
- Nur der Zirkulantensektor; Stabilität gegen nicht zirkulante Richtungen nicht gerechnet. Baumniveau.
- c = 1 ist eine Setzung (Projektor-Lesart); für anderes c liegt das Minimum des Spin-1-Terms bei χ und χ + π/2 statt am Oktanten.
- J in der Ebenen-Lesart wie H157/H158. Bei Ordnung 6 nur cos 3δ gerechnet, cos δ nicht.
- Vorzeichen von α, α′, β₃ nicht gesetzt (beide gerechnet). OP3 und OP4 offen; kein Guard berührt.
- Vergeben: H167, k362. Nächste frei: H168, k363.
