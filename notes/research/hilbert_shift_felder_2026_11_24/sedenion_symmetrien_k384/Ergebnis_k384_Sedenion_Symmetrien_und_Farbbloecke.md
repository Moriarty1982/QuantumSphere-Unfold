# Erkundung k384: Die endliche Symmetrie S₃ der Sedenionen verknüpft die zwei Farbblöcke als Dublett; eine Zahl für Up folgt daraus nicht

**Stand:** 26.11.2026. **Erkundung, nicht blind** (Strukturrechnung ohne Entscheidungskriterium; das Ergebnis der Teile A bis C folgt aus der
Darstellungstheorie und stand vor der Rechnung im Wesentlichen fest). Anlass: Autor, 26.11.2026 („fangen wir bei 1. an“; Punkt 1 war die in k380
unter „Grenzen“ offen gelassene Frage, ob die endlichen Automorphismen von 𝕊 die Farbblöcke verknüpfen).
Skripte `k384_sedenion_symmetrien.py` (`k384_out.txt`) und `k384b_gegenprobe.wl` (`k384b_out.txt`).

Werkzeuge: Python (numpy, scipy) für Automorphismus-Defekte, Derivationen, Stabilisator und die Zählung invarianter Formen; Wolfram Language exakt
für die Lösungsmenge der Automorphismus-Bedingung, die Bedingungen an die Koeffizienten und die Ladungen. Qiskit nicht eingesetzt (keine
Schaltung, kein Messablauf).

## Vorwissen geprüft
- k380 (`../hs_stufe_k380/`): vier Sektoren auf HS(4), zwei Farbblöcke {e₁..e₆} und {e₉..e₁₄}, durch Farbe, Konjugation und J nicht verknüpft;
  endliche Automorphismen dort ausdrücklich nicht einbezogen.
- H138 bis H140 (`../generationszahl_h138/`): drei Oktonion-Kopien in 𝕊 (Im z³ = 0), die Abbildungen ψ (Drehung 120°) und ε (Vorzeichen von 𝕆·ℓ)
  als Automorphismen (k323); S₃ vertauscht mit der Farbe, aber nicht mit der Ladung Q₀. Dort als Generationenfrage gelesen, nicht als Frage nach
  den Sektoren. Die Ladung Q₀ = ½ − (i/6)L_U − (i/3)R_U (k85-Form) ist von dort übernommen.
- H178, k378 (J und Farbe auf 𝕆), H179 (Georgi-Jarlskog), H180 (Neutrinos am J-Fixpunkt).
- Literatur: Aut(𝕊) = G₂ × S₃ (Brown 1967). Hier nicht neu bewiesen; nachgeprüft ist dim Der(𝕊) = 14 und die vollständige Lösungsmenge in der
  Familie aller Abbildungen, die mit G₂ vertauschen (Teil A).

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| ψ, ε Automorphismen (auf der Basis, bilinear) | 5,6·10⁻¹⁶; 0 | < 10⁻¹² | erfüllt |
| ψ³ = 1, ε² = 1, εψε = ψ⁻¹; sechs Elemente | True (Python und Wolfram exakt) | | erfüllt |
| dim Der(𝕊), Stabilisator von e₇ | 14; 8 | 14; 8 (k380) | erfüllt |
| [G₂, ψ], [G₂, ε] | 5,5·10⁻¹⁶; 8,0·10⁻¹⁶ | < 10⁻¹² | erfüllt |
| Zählung „Farbe + Konjugation + J“ | 4 Formen, keine gemischte | 4 (k380) | erfüllt |

## Ergebnis
**A. Die endliche Gruppe.** In der Familie 1 ⊗ A auf Im 𝕆 ⊗ ℝ² (Paare e_i, e_{i+8}), e₀ fest, e₈ ↦ ±e₈ sind genau sechs Abbildungen
Automorphismen: die Drehungen um 0°, 120°, 240° mit e₈ ↦ +e₈ und drei Spiegelungen mit e₈ ↦ −e₈ (Wolfram exakt: c = 1, s = 0 oder c = −½,
s = ±√3/2; die beiden anderen Zweige haben keine Lösung). Das ist S₃, erzeugt von ψ und ε.

**B. Wirkung auf die Sektoren.**
| Raum | Darstellung von S₃ |
|---|---|
| e₀ | trivial |
| e₈ | Vorzeichen |
| (e₇, e₁₅) | Dublett |
| Farbblock 1 (e₁..e₆) und Farbblock 2 (e₉..e₁₄) | Dublett, je mal (3 ⊕ 3̄) der Farbe |

ε lässt U = e₇ und den Tausch J fest. ψ nicht: ψU = −½e₇ + (√3/2)e₁₅, und ψJψ⁻¹ ≠ J. **Die Wahl der Ladungsrichtung U bricht S₃ auf
ℤ₂ = {1, ε}.**

**C. Invariante quadratische Formen (mögliche Massenterme).**
| geforderte Symmetrie | gesamt | Farbblock 1 | Farbblock 2 | zwischen den Blöcken | farblos |
|---|---|---|---|---|---|
| nur Farbe | 14 | 1 | 1 | 2 | 10 |
| Farbe + ε | 8 | 1 | 1 | 0 | 6 |
| Farbe + S₃ | 4 | 1 (derselbe Koeffizient) | 1 (derselbe) | 0 | 3 |
| Farbe + Konjugation + J (k380) | 4 | 1 | 1 | 0 | 2 |
| Farbe + Konjugation + J + ε | 4 | 1 | 1 | 0 | 2 |
| Farbe + Konjugation + S₃ + alle drei Tausche J_k | **2** | gemeinsam | gemeinsam | 0 | 1 |

Wolfram exakt, für die Form diag(a₀, a₇, a₈, a₁₅; c₁ auf Block 1; c₂ auf Block 2): ψ verlangt a₁₅ = a₇ und **c₂ = c₁**; J verlangt a₇ = a₀
und a₁₅ = a₈; ψ, J und ψJψ⁻¹ zusammen verlangen a₀ = a₇ = a₈ = a₁₅ und c₂ = c₁.

**D. Folge für Up und Down.**
- **Ja, S₃ verknüpft die Blöcke.** Ungebrochen gäbe sie beiden Farbblöcken denselben Massenterm. In der Lesart „Block = Quarktyp“ (k380) hieße das
  K_u = K_d. Gemessen (M_Z): 0,8876 gegen 0,7478. S₃ kann also keine Symmetrie der Massenterme sein.
- **Die Brechung ist schon da:** U = e₇ bricht S₃ auf ℤ₂. Mit ℤ₂ statt S₃ kommen vier Koeffizienten frei dazu (8 statt 4 Formen): der Unterschied
  der zwei Farbblöcke und drei im Farblosen. ε selbst wirkt auf Block 1 als +1 und auf Block 2 als −1 und verbietet nur gemischte Terme.
- **Keine Beziehung für Up.** Zwei Farbblöcke, zwei Koeffizienten (Mittel a und Dublettanteil b). Nur als Bericht, nachträglich: in ρ ist
  a = 1,2025, b = 0,0875, b/a = 0,073; in K ist b/a = 0,086. Diese Zahlen sind Daten, keine Vorhersage.
- **Was dazukommt:** Unter S₃ zusammen mit allen drei Tauschen bleiben nur zwei Massenterme, einer für alle vier farblosen Richtungen und einer
  für alle zwölf Farbrichtungen. Die eine Brechung S₃ → ℤ₂ trennt dann sowohl die farblosen Ebenen als auch die Farbblöcke. Die Stärke im
  Farblosen und in der Farbe ist durch die Symmetrie aber nicht verknüpft (verschiedene Farbdarstellungen, eigene Koeffizienten).

**E. Einwand gegen die Lesart „Block = Quarktyp“ aus k380 (Zusatz, Python und Wolfram exakt).** Die Ladung Q₀ der Kopie 0 hat auf
| Raum | Eigenwerte von Q₀ |
|---|---|
| {e₀, e₇} | 0, 1 |
| Farbblock 1 | ⅓ (dreifach), ⅔ (dreifach) |
| {e₈, e₁₅} | ⅓, ⅔ |
| Farbblock 2 | ⅓ (dreifach), ⅔ (dreifach) |

Q₀ vertauscht mit der Farbe und mit ε und bildet jeden der vier Räume in sich ab. **Die Ladung trennt die zwei Farbblöcke nicht:** Jeder Block
trägt beide Ladungen. Die Ladungen 0 und 1 liegen beide in der Ebene {1, U}; die zweite farblose Ebene trägt ⅓ und ⅔, also keine
Leptonladungen. In der Familie a + bL_U + cR_U ist das für jede Wahl der Koeffizienten so (auf 𝕆·ℓ und auf den Farbrichtungen ist
R_U = −L_U, die Ladungen liegen dort immer als Paar symmetrisch um a).
- Das **stützt** die Lesart aus H99 und H180: neutrale und geladene Leptonen in derselben Ebene {1, U} (Re- und Im-Sektor).
- Das **spricht gegen** die in k380 als „nachträglich und nicht geprüft“ notierte Zuordnung „Block in 𝕆 = Down, Block in 𝕆·ℓ = Up“ und gegen
  „Neutrinos in der zweiten Ebene“. Nach der Ladung enthält jeder Farbblock schon einen Up- und einen Down-artigen Anteil.
- Zählt man hermitesche Formen auf ℂ ⊗ A, die mit Farbe und Ladung vertauschen, hat schon ℂ ⊗ 𝕆 vier (je eine für die Ladungen 0, ⅓, ⅔, 1) und
  ℂ ⊗ 𝕊 acht. Die Aussage aus k380 „erst HS(4) bietet vier Sektoren“ gilt für reelle quadratische Formen ohne Ladung; mit der Ladung als
  Unterscheidung reicht HS(3). k380 wird damit nicht umgeschrieben, aber eingeschränkt.
- Der Tausch J (komplex-linear fortgesetzt) vertauscht auf {e₀, e₇} die Ladungen 0 und 1 (J Q₀ J⁻¹ = 1 − Q₀) und erhält auf den Farbblöcken
  die Ladung. Im Farblosen tauscht er also den neutralen mit dem geladenen Anteil, in der Farbe nicht Up mit Down.

## Lesart
- Die Frage des Auftrags ist beantwortet: Die endlichen Symmetrien verknüpfen die Farbblöcke, aber sie liefern keine Zahl für Up. Sie liefern
  eine Einordnung: Der Unterschied der zwei Blöcke ist die Brechung S₃ → ℤ₂ durch die Ladungsrichtung.
- Wichtiger ist der Einwand E. Es gibt jetzt zwei Lesarten dafür, was Up von Down trennt:
  (1) **Block** (k380): Up und Down sind die zwei Komponenten des S₃-Dubletts. Dann ist der Unterschied eine S₃-Brechung, und jeder Sektor
  enthielte beide Ladungen ⅓ und ⅔, was nicht zur gemessenen Ladung passt.
  (2) **Ladung:** Up und Down sind die zwei Ladungs-Eigenräume innerhalb eines Blocks, schon auf HS(3). Dann ist der Blockindex etwas anderes
  (die Kopienrichtung aus H138 bis H140), und der Unterschied der Massenterme braucht eine ladungsabhängige hermitesche Form. H179 hat gezeigt,
  dass Eichladungen allein K nicht ändern.
  Welche Lesart weiterverfolgt wird, ist eine Weggabelung für den Autor.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| k380 | U = e₇; Turmregel | vier reelle Sektoren erst auf HS(4); J legt einen fest | Zuordnung der Sektoren; Koeffizienten der zwei Farbblöcke |
| H180 | Ein-Feld-Form, Drehrichtung aus H173 bis H176 | Daten stützen K_ν ≈ ⅔ | Neutrinos in {1, U}; zweite Ebene unbesetzt |
| k384 | U = e₇; Ladung Q₀ in der k85-Form; Massenterm als quadratische Form | S₃ verknüpft die Blöcke als Dublett; U bricht S₃ auf ℤ₂; Ladung trennt die Blöcke nicht | Lesart „Block“ oder „Ladung“ für Up gegen Down; Stärke der Brechung (ein Koeffizient je Farbdarstellung) |

Prüfung nach der Regel „Bilanz der Setzungen“: Das Ziel (ein eigener Massenterm je Quarktyp) entsteht in k380 nur in der gewählten Zerlegung
nach reellen Blöcken. In der Zerlegung nach Ladung stellt sich die Frage anders. Diese Weggabelung wird dem Autor vorgelegt.

## Grenzen
Nur Formen vom Grad 2. Die Familie in Teil A enthält alle Abbildungen, die mit G₂ vertauschen; dass es außerhalb von G₂ × S₃ keine weiteren
Automorphismen gibt, ist aus der Literatur übernommen. Die Ladung ist die k85-Form der Kopie 0; andere Ladungsoperatoren außerhalb der Familie
a + bL_U + cR_U sind nicht geprüft. Keine Übertragung in den Materie-Frame nötig (keine Aussage „von Daten disfavorisiert“ außer K_u ≠ K_d, und
K ist eine Verhältnisgröße der Massen je Sektor bei gleicher Skala). Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen.
Vergeben: k384. Nächste frei: H182, k385 (vor Vergabe prüfen).
