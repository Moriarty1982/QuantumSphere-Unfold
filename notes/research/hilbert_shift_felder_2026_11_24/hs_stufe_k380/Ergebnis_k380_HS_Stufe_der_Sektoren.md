# Erkundung k380: Erst HS(4) bietet vier Sektoren, und J legt genau einen davon fest

**Stand:** 26.11.2026. **Erkundung, nicht blind** (Strukturrechnung ohne Entscheidungskriterium). Anlass: Autor, 26.11.2026 („erst … was die normale
Physik erwarten würde, dann das andere“; das andere ist die HS-Stufe der Sektoren). Skripte k380 (Python: Derivationen, Stabilisator, J, invariante Formen)
und k380b (Wolfram: J² exakt, eigene Multiplikation). Qiskit nicht eingesetzt.

## Vorwissen geprüft
k253 (Turmregel; dim Der und Stabilisator bleiben ab HS(4) bei 14 und 8), H138 bis H148 (`../generationszahl_h138/`: Sedenion-Kopien als Generationen,
dort verworfen), H178, k378 (J und Farbe auf 𝕆). Neu hier: die Zerlegung von 𝕊 unter der Farbe zusammen mit J und die Zählung der invarianten Formen.

## Ergebnis
| | HS(3) = 𝕆 | HS(4) = 𝕊 |
|---|---|---|
| Farbsymmetrie (Stabilisator von U = e₇) | su(3), Dimension 8 | su(3), Dimension 8 |
| farblose Richtungen | 2: {1, e₇} | 4: {1, e₇} und {e₈, e₁₅} |
| Farbrichtungen | 6 (ein Triplett mit Antitriplett) | 12 (zwei Tripletts mit Antitripletts: in 𝕆 und in 𝕆·ℓ) |
| J² = +1 | auf {1, e₇} | auf {1, e₇} |
| J² = −1 | auf den 6 Farbrichtungen | auf allen übrigen 14 Richtungen, auch auf {e₈, e₁₅} |
| invariante quadratische Formen (Farbe, Konjugation, J) | 2 | 4: je eine für jede farblose Ebene und für jeden Farbblock, keine gemischte |

- **HS(3) reicht nicht.** Dort gibt es eine farblose Ebene und einen Farbblock, also Platz für ein Lepton und einen Quarktyp.
- **HS(4) hat genau vier Sektoren:** zwei farblose Ebenen und zwei Farbblöcke. Das ist die Zahl der Sektoren einer Generation (ν, e, d, u). Jeder Sektor
  hat seinen eigenen Massenterm; die beiden Farbblöcke sind durch keine der benutzten Symmetrien verknüpft. Die zwei freien Zahlen der Quarks aus k378
  (ρ_d, ρ_u) haben damit einen Platz, aber keinen Wert.
- **J legt genau einen der vier Sektoren fest.** Der Winkel θ zwischen der Einheit 1 und der Kopienrichtung hat nur dann den Fixpunkt 45°, wenn die
  Kopienrichtung U selbst ist. Für die zweite farblose Ebene {e₈, e₁₅} ist J eine Vierteldrehung wie auf der Farbe.

## Lesart
- **Passt zur Messlage.** Von den vier Sektoren ist genau einer bei K = ⅔ gemessen (geladene Leptonen), zwei liegen daneben (Quarks), und für den vierten
  (Neutrinos) ist K nicht gemessen.
- **Folge für die Neutrinos (wichtig, betrifft eine Setzung).** Wenn die Neutrinos die zweite farblose Ebene besetzen, ist K_ν = ⅔ durch J **nicht**
  gedeckt. K_ν = ⅔ ist in H99/H100, H173 bis H176 gesetzt. Diese Setzung hätte dann keinen Grund aus J und müsste als freie Stellgröße geführt werden.
  Das ist eine Weggabelung für den Autor: (a) Neutrinos in derselben Ebene {1, U} wie die geladenen Leptonen (Real- und Imaginärteil, Lesart seit H99;
  dann bleibt K_ν = ⅔ gedeckt und HS(4) wird für die Leptonen nicht gebraucht), oder (b) Neutrinos in der zweiten Ebene (dann ist K_ν frei).
- **Up als Prüfstein:** Die Struktur sagt nicht, welcher Farbblock Up und welcher Down ist, und gibt keine Zahl. Mit H179 zusammen wäre die Lesart:
  Der Block in 𝕆 ist Down (hängt über die Farbzahl an den Leptonen), der Block in 𝕆·ℓ ist Up (ohne Beziehung). Das ist nachträglich und nicht geprüft.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H179 | Georgi-Jarlskog als Zahlenrelation | Eichladungen ändern K nicht | Up frei |
| k380 | U = e₇; Turmregel (Cayley-Dickson) | vier Sektoren erst auf HS(4); J legt einen fest | Zuordnung der Sektoren zu den Blöcken; K_ν; Koeffizienten der zwei Farbblöcke |

## Grenzen
Nur quadratische Formen gezählt; Grad 4 nicht. 𝕊 ist nicht alternativ; J ist dort weiterhin orthogonal mit J² = ±1 auf den Einheiten (geprüft), die
Schlüsse zu Kreisbahnen aus k253 gelten aber nicht. Die Automorphismen von 𝕊 jenseits der Derivationen (endliche Gruppe) sind nicht einbezogen; sie
könnten die Blöcke verknüpfen. Die Normierung der Casimir-Werte hängt von der Basis ab. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen.
Vergeben: k380. Nächste frei: H180, k381.
