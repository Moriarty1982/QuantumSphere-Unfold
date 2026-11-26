# Ergebnis H157: Unter dem Postulat J sind nur gerade Ordnungen erlaubt, N(W) ist verboten, und δ bleibt im Drei-Felder-Modell bis Ordnung 10 am Rand

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H157_Postulat_J_und_delta.md` (Commit c5929e4; a, d nicht blind). Skripte `k340_postulat_delta.py` (`k340_out.txt`),
`k340b_gegenprobe.wl` (`k340b_out.txt`, Wolfram), nachträglich `k340c_klassifikation.py` (`k340c_out.txt`) und `k340_zusatz_N2_out.txt`.
Status: H157a, b bestätigt; H157c nach Wortlaut widerlegt, in der Sache bestätigt; H157d Lesart.**

Anlass: Der Autor nimmt vorerst das Postulat an (Tausch J als Symmetrie). Werkzeuge: Python (sympy, scipy), Wolfram unabhängig (allgemeine Polynome in
(φ, y₁, y₂) mit direkter Invarianzforderung statt über Erzeuger). Die Dimensionen stimmen überein. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H157a | H155-Form: Rest P − JP = 0; N(W): Rest ≠ 0, der Koeffizient von φr² ist −√3/6 unabhängig von δ, also keine Ebene mit Rest 0 (Wolfram: False) | symbolisch | **bestätigt** (nicht blind): ζN(W) ist verboten |
| H157b | J-erlaubte Dimension je Ordnung 0…12: 1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 7 (invariant: 1, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 19); k = 1 zuerst Ordnung 6 (nur φ³C₃), k = 2 zuerst Ordnung 12 (nur φ⁶C₃²); Python und Wolfram gleich | (i)–(iii) | **bestätigt** |
| H157c | Bis Ordnung 10: 300 Proben, 275 mit r > 0, davon 59 mit \|sin 3δ\| > 10⁻⁴. Klassifikation (k340c): alle 59 haben φ = 0, dort ist V in δ flach (Spannweite 7·10⁻¹⁶); 216 Minima mit φ ≠ 0, alle am Rand; 210 bei θ = π/4. Mit Ordnung 12: 3 innere δ bei θ = π/4, φ ≠ 0 | „alle Minima am Rand“ | **nach Wortlaut widerlegt, in der Sache bestätigt** |
| H157d | δ = 0: 1 : 0,0147 : 0,0147; δ = π/3: 1 : 1 : 0,0589; Leptonen 1 : 0,0595 : 0,00029 | Lesart | kein Endpunkt hat drei verschiedene Massen |

## Lesart
- **Das Postulat räumt auf.** Erlaubt sind nur Terme gerader Ordnung. Jede kubische Kopplung fällt weg, auch N(W) und nachträglich geprüft N(W)².
  Der Fit aus H155 über ζN(W) + N²/Λ² ist unter dem Postulat nicht zulässig.
- **K = ⅔ ist robust, aber nicht garantiert.** In 210 von 216 Proben mit φ ≠ 0 liegt das Minimum bei θ = π/4. In den übrigen bricht das Vakuum J spontan.
- **δ bleibt am Rand.** Der einzige Term mit cos 3δ bis Ordnung 10 ist linear in cos 3δ. Das Minimum liegt deshalb bei δ = 0 oder π/3, und zwei Massen sind gleich.
  Drei verschiedene Massen brauchen cos² 3δ, also Ordnung 12, und eine Skala Λ ≈ 0,76 v bei Einheitskoeffizienten. δ = 2/9 ist dann ein Verhältnis zweier
  Koeffizienten, ein Fit.

## Offen gelegt
- H157c: Die Vorab-Notiz hat den Fall φ = 0 übersehen. Dort verschwinden alle cos 3δ-Terme (Faktor φ³), δ ist flach und ohne Bedeutung; K ist dort nicht ⅔.
  Die Klassifikation k340c kam nach Sicht der Ausgabe dazu und ist nachträglich.
- Die Nähe 0,0589 (δ = π/3) zu m_μ/m_τ = 0,0595 ist benannt, nicht gewertet; das Spektrum hat dort zwei gleiche schwere Massen.
- Die Ebenen-Lesart des Postulats ist meine Übertragung auf das Drei-Felder-Modell. H158 rechnet dieselbe Frage auf der Nebendiagonale der Albert-Algebra;
  dort sind cos 2δ (Ordnung 4) und cos δ (Ordnung 6) zusätzlich erlaubt.

## Grenzen
- Baumniveau; das Laufen der höheren Kopplungen ist nicht gerechnet. Der beschränkende Term der Stichprobe ist positiv gewählt (Beschränktheit, kein physikalisches Vorzeichen).
- OP3 offen; kein Vorzeichen gesetzt; kein Guard berührt.
