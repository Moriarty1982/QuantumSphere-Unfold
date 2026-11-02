# Erkundung: Λ als Mischung über Kreuzungen der Sektoren (kein Vorab-Test)

Stand 2026-11-02. Autoridee (28.10.): Die kosmologische Konstante hängt vom inneren Messwinkel ab bzw. es gibt ein Λ je Kreuzung der
Sektoren; unser Wert wäre eine Mischung. Der Autor hat einem Test H49 zugestimmt. Beim Aufsetzen zeigte sich: Mit festen
Strukturwerten ist die Klasse der Lesarten endlich und klein genug, um sie vorab im Kopf zu überschlagen. Ein Vorab-Test wäre daher
nicht blind. Deshalb hier offen als Erkundung; die Bezeichnung H49 bleibt frei.
Skript `llm/k108_kreuzungen.py`, Ausgabe `llm/k108_out.txt`, `llm/k108_out.json`.

## Strukturelle Vorüberlegungen (analytisch)

1. **Zerlegungsfreiheit.** Ein gemischter Zustand lässt sich auf viele Arten als Mischung schreiben (M/T über die Eigenwerte, oder
   rein plus Photon P = I/2). „Ein Λ je Kreuzung“ ist nur dann eindeutig, wenn es als Operator auf dem Paarraum definiert ist,
   Λ_obs = Tr[(ρ⊗ρ) Λ̂₂].
2. **Linear trägt nicht.** Λ_obs = Tr(ρ Λ̂) = λ₀ + λ⃗·b mittelt sich unter der Dualitätsdrehung (der Uhr) auf λ₀ heraus und hängt
   dann nicht von der Mischung ab.
3. **Bilinear hängt an |b|.** Ist Λ̂₂ unter Drehung und Tachyon-Abbildung invariant (SU(2)), bleiben nur Singulett und Triplett mit
   Gewichten (1 − |b|²)/4 und (3 + |b|²)/4.
4. **Epoche bleibt.** Jede solche Λ_obs ist konstant, sobald |b| eingefroren ist (H48). Ω_Λ entwickelt sich dann wie in ΛCDM; eine
   Gleichung „Ω = f(|b|)“ gilt nur zu einer Epoche, wie schon in r67. Die Kreuzungs-Lesart löst die Epochenfrage nicht.
5. **Identität.** Mit |b| = 1/γ_L haben die Eigenwerte das Verhältnis λ₋/λ₊ = (γ_L − 1)/(γ_L + 1) = β_sym². β² ist also das
   Gewichtsverhältnis der M/T-Mischung; Ω_M = β² aus thm:dark-energy ist in dieser Sprache Ω_M = λ₋/λ₊.

## Durchmusterung (26 Lesarten)

Drei Gewichtsquellen (Eigenwerte; Zählgewichte aus r63/r67; rein plus P), je linear (2) oder über Kreuzungen 11, 12, 22 mit jeder
nichttrivialen Teilmenge als Vakuum (6), dazu Singulett und Triplett. Daten: Planck 2018 Ω_m = 0,315 ± 0,007; DESI DR2 BAO allein
Ω_m = 0,2975 ± 0,0086 (flach). Treffer: innerhalb 2σ von einem der beiden.

- **Ein Treffer:** Gewichte rein (|b|) und Photon P (1 − |b|), Vakuum = jede Kreuzung, an der P beteiligt ist. Dann
  Ω_M = |b|² = 1/γ_L² = 0,288, Ω_Λ = 0,712. Gegen DESI −1,2σ, gegen Planck −3,9σ.
- **Zufallserwartung:** Der Trefferbereich deckt 0,049 der Einheitsstrecke ab; bei 26 Lesarten erwartet man etwa 1,3 Zufallstreffer.
  Ein einzelner Treffer ist daher kein Hinweis.
- **Zum Vergleich:** Ω_M = β² = 0,302 (thm:dark-energy, bereits im Korpus) liegt bei −1,9σ gegen Planck und +0,5σ gegen DESI und passt
  zu beiden Datensätzen besser als jede Kreuzungs-Lesart.

## Ergebnis

Die Kreuzungs-Lesart liefert keine bessere Zahl als β², und sie löst die Epochenfrage nicht. Als Vorhersage festgeschrieben wird nichts:
Der einzige Treffer ist nachträglich aus 26 Lesarten gewählt und liegt gegen Planck schon bei 3,9σ.

Was bleibt, ist die Identität β² = λ₋/λ₊. Sie legt nahe, β_sym als Mischungsverhältnis der beiden Frames zu lesen statt als Geschwindigkeit
oder Offset. Das passt zur Zähl-Lesart (r63): Zwei Zählungen geben zwei Gewichte. Das ist eine Umformulierung, kein neuer Befund.

Guards unverändert.
