# Ergebnis H16: Massen aus invarianten Potentialen bis Grad 6 auf dem Tripel-Raum

Vorab-Notiz: Commit d0360b8 (2026-10-22 14:13 UTC), vor der Prüfung. Die Notiz wurde als „H12“ angelegt; diese Nummer
war bereits vergeben (Drei-Frame-Zuordnung). Deshalb wurde die Datei in Commit 6bd2f1b ohne inhaltliche Änderung in
`Vorab_Notiz_H16_Grad6_Tripelraum.md` umbenannt. H12a–c der Notiz heißen hier H16a–c.
Skripte: `k64_test_h16.py` (Test), `k65_sattel_grad6.py` (Nachkontrolle nach dem Urteil). Kriterium unverändert.

## Ergebnisse (M)

Potential V₆ = −S + βS² + γQ − κP + δH (H = Σn⁶, δ > 0).

**H16a (Existenz), feste Verteilung, N = 2000:**

| Muster des globalen Minimums | Anzahl |
|---|---|
| drei gleiche Normen | 1585 |
| ein besetzter Platz | 398 |
| zwei verschiedene Normen, alle ≠ 0 (entartetes Paar) | 17 |
| drei verschiedene, alle ≠ 0 | **0** |

**H16b (Leptonen erreichbar):** Für das Lepton-Tripel (√m/√m_τ = 0,01696; 0,24385; 1) wurde die zweiparametrige
Familie aus Vieta auf dem Gitter 41 × 41 (Skala s, β) abgetastet. An jedem Punkt ist das Tripel kritischer Punkt
(Gradient geprüft). Bei 1139 Punkten ist δ ≤ 0, bei den übrigen 542 ist die Hessematrix nicht positiv definit.
**Kein einziger Punkt ist auch nur ein lokales Minimum.**

**H16c (Vorhersage):** Ohne Minima mit drei verschiedenen Normen gibt es keine K-Verteilung.

## Urteil nach dem festgelegten Kriterium

- H16a **widerlegt** (0 von 2000).
- H16b **widerlegt**: V₆ trägt die Lepton-Hierarchie nicht.
- H16c **widerlegt**, weil die Bedingung (mindestens 50 % mit |K − 2/3| < 0,01) bei null Minima nicht erfüllt ist.

## Strukturbefund: der Grund (M, nach dem Urteil gefunden und exakt geprüft)

Alle Invarianten der Normen bis Grad 6 sind **linear** in e₂ = Σ_{i<j} x_i x_j:

- Q = S² − 2e₂,
- H = S³ − 3S·e₂ + 3P²,
- S·Q = S³ − 2S·e₂.

S, S², S³, P, S·P und P² enthalten e₂ gar nicht. Also hat jedes solche Potential die Form V = A(S, P) + e₂·(b₀ + b₁S).

Bei drei verschiedenen Normen sind (S, e₂, P) gültige lokale Koordinaten (Vandermonde-Determinante ≠ 0). An einem
kritischen Punkt hat die Hessematrix in diesen Koordinaten die Gestalt [[·, b₁, ·], [b₁, 0, 0], [·, 0, ·]]. Ihr
2×2-Hauptminor hat die Determinante −b₁² < 0. Daraus folgt:

- **Jeder kritische Punkt mit drei verschiedenen Normen ist ein Sattelpunkt.**
- Die einzige Ausnahme ist b₁ = b₀ = 0. Dann hängt V nicht von e₂ ab, und die Massen sind unbestimmt.

Für V₆ ist b₁ = −3δ. Die Bedingung ∂V/∂e₂ = 0 ist genau die Vieta-Relation 2γ + 3δS = 0; das ist numerisch
bestätigt.

Exakte Kontrolle mit 40 Stellen: 2000 von 2000 zufälligen kritischen Punkten des allgemeinsten Grad-6-Ansatzes sind
Sattelpunkte. In doppelter Genauigkeit sahen 39 davon nicht wie Sattelpunkte aus, weil der negative Eigenwert bis
auf 5·10⁻¹⁵ des größten schrumpfen kann.

## Neueinordnung

- **H11 / r16 (K32.3):** Die Aussage „Mindestgrad 6“ gilt nur für **kritische Punkte**. Für **Minima** mit drei
  verschiedenen Normen ist Grad 6 nicht ausreichend; nötig ist mindestens **Grad 8**, also e₂², Q² usw. Ob Grad 8
  ausreicht, ist nicht gezeigt.
- Mit Grad 8 kommen bei den reinen Norm-Invarianten mindestens vier neue Koeffizienten dazu (S⁴, S²e₂, e₂², S·P²,
  dazu P-Terme). Die zwei Lepton-Verhältnisse wären auch dann nur anpassbar. Eine Vorhersage von K = 2/3 ist aus
  polynomialen Norm-Potentialen nicht zu erwarten, weil K die Summe Σn_k braucht, die kein Polynom ist.
- Mit der Einschränkung dieses Rahmens (nur Normen und t = P) bleibt die Folgerung: **Die Generationen-S₃ mit
  natürlichen Invarianten erzeugt keine Massenhierarchie.** Eine Hierarchie braucht eine explizite Brechung der S₃
  oder Invarianten jenseits der Normen (etwa Realteile der einzelnen Plätze, die unter G₂ invariant sind).
