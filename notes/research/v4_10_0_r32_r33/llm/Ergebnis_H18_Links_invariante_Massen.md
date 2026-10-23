# Ergebnis H18: Massen aus links-invarianten Etiketten an den Minima der geprüften Potentiale

Vorab-Notiz: `Vorab_Notiz_H18_Links_invariante_Massen.md`, Commit 6130814 (2026-10-23 03:59 MESZ), vor der Prüfung.
Skripte: `k73_test_h18.py` (Test), `k74_nachkontrolle_h18.py` (Nachkontrolle nach dem Urteil). Kriterium unverändert.

## Ergebnisse (M)

Lesart m_k ∝ √μ_k mit μ_k = 2(|x_i|²|x_j|² − ⟨x_i,x_j⟩²) am globalen Minimum, 20 Startpunkte je Parameterpunkt.

| Familie | Punkte | Ergebnis |
|---|---|---|
| A (H11, V₄) | 205 | 205 unbestimmt |
| B (H17, V_R) | 500 | 428 unbestimmt; bestimmt: 51 gleich, 8 zwei verschieden (eins null), 13 zwei verschieden |

**Drei bestimmte, verschiedene μ: in keinem Fall.**

## Urteil nach dem festgelegten Kriterium

H18a und H18b sind **widerlegt**. Für H18b gab es keine Kandidaten.

## Nachkontrolle: warum „unbestimmt“ (M, nach dem Urteil)

- **Familie A:** Alle Startpunkte erreichen dieselbe Tiefe mit denselben Normen, aber μ_max/S² streut zwischen 0,15 und
  0,22. V₄ hängt nur von den Normen und von t = Re((ab)c) ab. Bei festem t bleibt der Winkel zwischen zwei Plätzen frei,
  das dritte Oktonion stellt sich darauf ein. Die μ wandern also entlang einer echten flachen Richtung. Der Höchstwert
  2/9 = 0,222 entspricht gleichen Normen bei orthogonalen Plätzen.
- **Familie B:** Unter den ersten 150 Punkten sind alle 131 „unbestimmten“ Fälle solche mit μ ≈ 0. Die Plätze liegen
  parallel auf der reellen Achse (vgl. H17: dort lagen die meisten Minima). Rauschen um null hat die relative Toleranz
  ausgelöst. In der Sache sind die μ dort null, nicht unbestimmt.
- Beides spricht noch deutlicher gegen die Hypothese: Die geprüften Potentiale legen die Winkel entweder gar nicht fest
  oder legen alle Plätze parallel.

## Einordnung

- Die links-invarianten Etiketten (K77.10) lösen den Lorentz-Konflikt, aber sie *erben* das Auswahlproblem. An den
  Minima der natürlichen Potentiale sind sie gleich, null oder unbestimmt.
- Um aus ihnen Massen zu machen, bräuchte es ein Prinzip, das die *Winkel* zwischen den Plätzen festlegt, nicht nur die
  Normen. Die bisherigen Potentiale enthalten die Winkel nur über t = Re((ab)c). Das ist eine Bedingung, wo drei nötig wären.
- Damit stehen vier widerlegte Tests desselben Ansatzes: H11, H16, H17 und H18. Natürliche Invarianten auf dem
  Tripel-Raum erzeugen keine Hierarchie, weder über Normen noch über links-invariante Flächen.
