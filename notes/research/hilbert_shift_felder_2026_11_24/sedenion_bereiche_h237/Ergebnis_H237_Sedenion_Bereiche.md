# Ergebnis H237 (k453): Die drei Oktonion-Kopien sind in ganz 𝕊 wellenfähig. Stabile Bereiche der Sedenionen kartiert

**Datum:** 2026-11-28. **Vorab:** `Vorab_H237_Sedenion_Bereiche.md` (Commit 2f68c37, vor der Rechnung). **Urteil: trägt** (Teil A).
**Werkzeuge:**
- Python: `k453_test_h237.py` → `k453_out.txt`.
- Wolfram unabhängig: `k453b_gegenprobe.wl` → `k453b_out.txt`, in drei Aufrufen. Alle gemeinsamen Zahlen stimmen überein.
- Nachtrag: `k453c_kreis.py` → `k453c_out.txt` (nachträglich, nicht gewertet).
- Qiskit ist nicht einschlägig.

Im ersten Python-Lauf zählte `null_space` mit relativer Toleranz bei K ≈ 10⁻¹⁶ das Rauschen als Rang und meldete dim W = 0 für V2 und V3.
Mit absoluter Toleranz ist dim W = 16, passend zu δ = 0. Nur der berichtigte Lauf ist abgelegt.

## Frage
k452 zeigte, dass die Feldgleichung erster Ordnung über **alle** 15 Richtungen von 𝕊 keine Wurzel der Wellengleichung ist. Marc vermutete, dass es in
𝕊 trotzdem Bereiche mit stabilen Feldern gibt. Tragen die wellenfähigen Richtungen die drei Oktonion-Kopien aus H138, und wie sieht die Karte
von 𝕊 aus?

## Ergebnis Teil A (blind)
| Kopie (H138) | Wellendefekt δ(Im V) auf ganz 𝕊 | stabiler Bereich W | mit e₈ (der vierten Wand ℓ) |
|---|---|---|---|
| V1, v = (1, 0) | 0 | ganz 𝕊 (16) | δ = 0: volle Clifford-Menge aus 8 Richtungen |
| V2, v = (−½, +√3/2) | 2·10⁻¹⁶ | ganz 𝕊 (16) | δ = 0, 8 Richtungen |
| V3, v = (−½, −√3/2) | 2·10⁻¹⁶ | ganz 𝕊 (16) | δ = 0, 8 Richtungen |

**Urteil nach Vorab: trägt.**
- Die Feldgleichung jeder der drei Kopien quadriert sich auf ganz 𝕊 zur Wellengleichung, für **jeden** Feldwert in 𝕊.
- Zusammen mit der Richtung ℓ = e₈ bildet jede Kopie eine volle Clifford-Menge aus 8 Richtungen. Das ist das Maximum ρ(16) − 1 = 8, und es sind
  genau die „8 Richtungen“ aus k407/k452.

## Teil B: Karte der Sedenionen (Bericht)
| Bereich | Anzahl | Eigenschaften | stabiler Bereich W seiner Richtungen auf ganz 𝕊 |
|---|---|---|---|
| Basis-Unteralgebren, dim 2 (Kopien von ℂ) | 15 | alle alternativ, normmultiplikativ, nullteilerfrei | — |
| Basis-Unteralgebren, dim 4 (Kopien von ℍ) | 35 | alle alternativ, normmultiplikativ, nullteilerfrei | — |
| Basis-Unteralgebren, dim 8: Oktonionen | 8 | alternativ, normmultiplikativ, nullteilerfrei | **1** davon ganz 𝕊 (die innere {e₀…e₇} = V1), **7** nur die Algebra selbst (W = 8) |
| Basis-Unteralgebren, dim 8: Quasi-Oktonionen | 7 | nicht alternativ, Nullteiler | nur W = span{1, e₈} (2) |
| ganz Im 𝕊 (15 Richtungen) | 1 | — | W = span{1, e₈} = ℂ der vierten Wand (2) |
| größte Clifford-Mengen aus Basiseinheiten | 2: {e₁…e₈}, {e₈…e₁₅} | L² = −1, paarweise antikommutierend; alle maximalen Mengen haben 3 oder 8 Elemente | ganz 𝕊 |
| allgemeine Richtungsräume | — | δ = 0 erzwingt höchstens 8 Richtungen (Hurwitz–Radon, analytisch statt der vorgesehenen Stichprobe B5) | — |

## Nachtrag (nachträglich, nicht gewertet, `k453c`)
Die Wellenbedingung gilt für den ganzen Kreis von Richtungsräumen U_θ = {cos θ·eᵢ + sin θ·e₈₊ᵢ}, nicht nur für die drei Kopien:
- Bei jedem untersuchten θ (0°, 15°, 30°, 37,5°, 45°, 60°, 90°, …) ist δ = 0.
- Eine Unteralgebra (abgeschlossen unter dem Produkt) ist U_θ nur bei θ = 0°, 60°, 120°, 180°, 240°, 300°. Bis auf das Vorzeichen von v sind das
  genau die drei Kopien.
- **Die Feldgleichung wählt die drei Kopien also nicht aus.** Sie lässt einen ganzen Kreis wellenfähiger Richtungsräume zu. Die Dreizahl kommt von
  der Abgeschlossenheit als Algebra (H138), nicht von der Wellenbedingung.

## Was das heißt
- **Marcs Vermutung stimmt:** 𝕊 ist nicht pauschal instabil. Stabile Felder gibt es in drei Arten von Bereichen:
  1. **Nach Richtungen:** Es gibt einen Kreis von 7-dimensionalen Richtungsräumen U_θ. Mit e₈ ergänzt hat jeder davon die volle Zahl von 8
     wellenfähigen Richtungen, und die Feldgleichung quadriert sich auf ganz 𝕊. Drei davon sind zugleich Oktonion-Algebren, nämlich die
     G₂-stabilen Kopien.
  2. **Nach Feldwerten:** Die übrigen sieben Basis-Oktonionen tragen stabile Felder nur innerhalb ihrer selbst (W = 8).
  3. **Kern:** Mit allen 15 Richtungen zugleich bleibt nur das Feld in span{1, e₈}, also die komplexe Ebene der vierten Wand.
- **Die Generationsfrage (H140–H143) bleibt offen.** Neu ist aber: Die drei Kopien sind die einzigen Stellen, an denen in 𝕊 drei Dinge
  zusammenfallen, nämlich Oktonion-Algebra, G₂-Stabilität und volle Wellenfähigkeit auf ganz 𝕊. Zwischen den Kopien liegen wellenfähige, aber
  nicht abgeschlossene Richtungsräume. Die Kopien sind dadurch nicht orthogonal (H138).
- **Zum Abbruch aus k452:** Der Abbruch betrifft die Feldgleichung über alle 15 Richtungen. Beschränkt man die Richtungen auf 8, gibt es in 𝕊 volle
  Wellenfelder. Der Turm hält damit bei den **Richtungen** an (mehr als 8 geht nie, Hurwitz–Radon), nicht bei den **Feldwerten**.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:**
  - δ und W für die drei Kopien, die 15 Basis-Oktonion-Algebren und ganz Im 𝕊 (zwei Werkzeuge).
  - Zählung der Basis-Unteralgebren (15/35/15, davon 8 Oktonionen und 7 Quasi-Oktonionen).
  - Maximale Clifford-Mengen.
  - Obergrenze 8 (Hurwitz–Radon).
- **Gesetzt:** Feldgleichung D = ∂₀ + Σ uₐ∂ₐ mit Richtungen aus einem Teilraum U. Stabilität bedeutet D̄D = Δ (Dirac-Prinzip aus k452). Kopien
  nach H138 (G₂-Stabilität).
- **Nachträglich:**
  - Der Kreis U_θ und die Feststellung, dass die Wellenbedingung die drei nicht auswählt (k453c).
  - Der Kern span{1, e₈}.
  - Abweichung von der Vorab-Notiz: B5 analytisch statt per Stichprobe.

OP1–OP5 bleiben offen; die Kopien sind weiterhin nicht als Generationen gezeigt. Vergeben: H237, k453. Nächste frei: H238, k454.
