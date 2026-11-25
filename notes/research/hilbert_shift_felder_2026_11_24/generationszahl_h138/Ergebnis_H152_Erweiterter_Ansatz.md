# Ergebnis H152: Der vollständige skalenfreie Ansatz legt weder K noch δ fest; die kubische Norm wählt δ = 0 oder π/3, also zwei gleiche Massen

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H152_Erweiterter_Ansatz.md` (Commit c76928c). Skripte `k335_erweiterter_ansatz.py` (`k335_out.txt`), `k335b_gegenprobe.wl`
(`k335b_out.txt`, Wolfram). Status: H152a–e bestätigt (alle wie vorhergesagt).**

Anlass: Autor „probiere erst den abgeschnittenen ansatz“. Gelesen als: Der skalenfreie Fluss aus H150/H151 war nach dem einen Kopplungsterm κ abgeschnitten; hier stehen
alle zulässigen Terme vierter Ordnung und die Rückwirkung von HS(3). Werkzeuge: Python (sympy: Invariantentheorie und β-Funktionen; scipy: Fluss und Minimum auf der
Kugel), Wolfram unabhängig (β-Funktionen über SolveAlways, δ-Abhängigkeit, Massen). Alle sieben β-Funktionen stimmen überein. Qiskit nicht eingesetzt.

## Der Ansatz
Felder: φ (HS(0)-Einheit), y = (y₁, y₂) (Kopien-Ebene), C (4 Komponenten, Rückwirkung von HS(3) wie H133). Symmetrie: Z₃ ⋊ Z₂ der drei Kopien und O(4) auf C.
V = λ_A φ⁴ + κ φ²B + λ_B B² + **ξ φ C₃** + κ_C φ²|C|² + κ_BC B|C|² + λ_C |C|⁴, mit B = |y|², C₃ = y₁³ − 3y₁y₂².

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H152a | Z₃⋊Z₂-invariante Quartiken in (φ, y): Dimension 4 = {φ⁴, φ²B, B², φC₃}; ½Tr(∂²V)² liegt in der Basis (Nullrest); β_ξ = 24ξ(κ + 2λ_B), ξ erzeugt Beiträge 9ξ² zu β_κ und β_B | Nullrest | **bestätigt** |
| H152b | 144 Startpunkte, alle mit Gildener–Weinberg-Punkt; K von 0,6615 bis 0,8182, Streuung 0,042 | Streuung < 10⁻³ für „fester Punkt“ | **startabhängig** (bestätigt) |
| H152c | δ am GW-Punkt: 73-mal 0, 71-mal π/3; drei verschiedene Massen in 0 von 144 Fällen | 0 Treffer bei 2/9 | **bestätigt** |
| H152d | K innerhalb 3σ von 0,666661: 0 von 144; ⅔ liegt aber im erreichten Bereich | 0 Punkte | **bestätigt**; ⅔ nur über gewählte Startwerte (Fit) erreichbar |
| H152e | \|θ − π/4\| < 0,01 in 20 von 144 Fällen; θ − π/4 von −0,004 bis +0,093 | weniger nahe π/4 als H150d | **bestätigt** |

Kontrolle: Mit ξ = 0 und κ_C = 0 gibt der Ansatz H150 genau zurück (τ = 0,134145, K = 0,671941). Kein Gitterpunkt kondensiert in C.

## Lesart
- **Der vollständige Ansatz hat genau einen neuen Term**, ξ φ C₃, die skalenfreie Form der kubischen Norm. Auf der Kugel geht er wie ξ cos θ sin³θ cos 3δ (Wolfram exakt).
  Sein Minimum liegt deshalb immer bei cos 3δ = ±1, also δ = 0 oder π/3. Dort sind zwei der drei Massen gleich. Das ist der Befund aus H149 (kubische Norm) und H11/H16
  (keine drei verschiedenen Normen), jetzt mit Fluss: **Der Fluss wählt die Brannen-Phase, aber die falsche.**
- **K wird nicht festgelegt.** Der ξ-Term schiebt θ zusätzlich (er ist ungerade in φ), die HS(3)-Rückwirkung κ_C schiebt K nach unten. Zusammen überdecken sie einen Bereich,
  der ⅔ enthält. Den Messwert trifft man aber nur, wenn man die Startkopplungen passend wählt; das ist eine Anpassung, keine Herleitung.
- **π/4 bleibt kein Fixpunkt.** Ohne Tausch-Symmetrie (1 gegen 2 Komponenten) und mit dem in φ ungeraden ξ-Term liegt θ am GW-Punkt meist über π/4.
- Das Abschneiden nach κ war also nicht der Grund für die Verschiebung. Die Verschiebung kommt aus der Komponentenzahl (H151), und die Erweiterung macht die Lage für δ
  schlechter, nicht besser.

## Grenzen
- Eine Schleife, ohne Eichfelder und ohne die Zusatzterme K₁–K₄ (verschwinden für homogene Felder). Die Ankopplung von C nur über φ²|C|² am Start ist eine Lesart von H133;
  κ_BC entsteht im Fluss von selbst.
- Gitter grob (144 Punkte); die Aussage „startabhängig“ ist davon unabhängig.
- Ein Term sechster Ordnung (cos 6δ, nötig für ein Minimum zwischen 0 und π/3 nach H149) ist nicht skalenfrei und deshalb nicht enthalten. Er wäre der nächste Schritt, falls
  der Autor die Skala als Setzung zulässt.
- OP3 offen; kein Vorzeichen gesetzt (ξ und κ_C über beide Vorzeichen); kein Guard berührt.
- Vergeben: H152, k335. Nächste frei: H153, k336.
