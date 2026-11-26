# Ergebnis H158: Die Albert-Algebra füllt die offenen Zellen (Zyklus, magischer Winkel, K = ⅔ unter dem Postulat); δ ist die Phase der Nebendiagonale, 2/9 kommt nicht ohne Fit

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H158_Albert_Zyklus_und_delta.md` (Commit f2e5862; a, b, e nicht blind). Skripte `k341_albert_zyklus_delta.py`
(`k341_out.txt`), `k341b_gegenprobe.wl` (`k341b_out.txt`, Wolfram). Status: H158a, b, c, e bestätigt; H158d bestätigt (kein Treffer).**

Anlass: Autor, mit Verweis auf die Träger-Tabelle (Physik-Paper, Abschnitt Teilchen; Companion r60): Für die Albert-Algebra H₃(𝕆) stehen „order-3 cycle“ und
„reference at the magic angle“ als *not examined*, „K = 2/3“ als *not addressed*. Werkzeuge: Python (sympy, numpy mit Cayley–Dickson-Oktonionen), Wolfram unabhängig
(reelle Monome in (φ, s_k, v_k) mit expliziten V₄-Vorzeichen, Fourier-Zerlegung). Die Ausgaben stimmen überein. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H158a | P-invariante Elemente sind Zirkulanten W = a·1 + bS + b̄S²; Eigenwerte a + 2\|b\| cos(arg b + 2πk/3) (charakteristisches Polynom: Nullrest); Eigenvektoren von P sind die Fourier-Vektoren, (1,1,1)/√3 steht zu jeder Platzachse im Winkel 54,7356°; in H₃(𝕆) mit x₁ = x₂ = x₃ stimmen Tr, Tr W², det mit H₃(ℂ_x) überein (20 Proben, 6·10⁻¹⁴) | symbolisch, numerisch | **bestätigt** (nicht blind) |
| H158b | K = Tr W²/(Tr W)² = (a² + 2r²)/(3a²); K = ⅔ ⇔ r² = a²/2 ⇔ 3a² = 6r² (gleiche Norm von Spur- und Nebendiagonalanteil) | symbolisch | **bestätigt** (nicht blind) |
| H158c | J-erlaubte Dimension je Ordnung 0, 2, 4, 6, 8: 1, 1, 4, 8, 13 (Python und Wolfram gleich); ungerade Ordnungen leer; δ-abhängig zuerst Ordnung 4 (cos 2δ, sin 2δ), cos δ und cos 3δ ab Ordnung 6, cos 4δ ab Ordnung 8 | Vorhersage vorab | **bestätigt** |
| H158d | δ_exp = 0,2222217 ± 7,8·10⁻⁷ (2/9 liegt 0,66σ daneben); 720 Kandidaten je Paar, 174 verschiedene innere Minima; Treffer 0 und 0; Zufallserwartung 0,0008; nächster Kandidat β/α = −3√3 (nötig −5,186, Abstand 0,19 %; δ = 0,221935, 368σ) | Treffer innerhalb 3σ | **bestätigt**: kein Treffer |
| H158e | Re(w²) − [(1 − c²)(s² − v²) − 4c s·v] = 0; arg w = arctan c + atan2(v, s) | symbolisch | **bestätigt** (nicht blind): c verschiebt nur die Phase |

## Lesart
- **Die drei Zellen lassen sich füllen.** Der Zyklus der Ordnung 3 ist der Platztausch P, der in A₄ liegt. Seine Eigenvektoren sind die Fourier-Vektoren; der
  symmetrische steht im magischen Winkel zu den drei Plätzen. Ein P-invariantes Vakuum ist eine Zirkulante, und ihre Eigenwerte haben genau die Brannen-Form.
  Im Träger H₃(𝕆) liegt ein solches Vakuum immer in einem H₃(ℂ).
- **δ bekommt eine Bedeutung: es ist die Phase der Nebendiagonale,** tan δ = v/s, also das Verhältnis von imaginärem zu reellem Nebendiagonalanteil
  (Spin 1 zu Spin 2 der Familien-SO(3), k278–k282). 2/9 heißt v/s = tan(2/9) = 0,2260.
- **K = ⅔ ist gleiche Norm von Spur und Nebendiagonale.** Das ist der Tausch φ ↔ r aus H155–H157. Unter dem Postulat ist K = ⅔ der Fixpunkt; ohne Postulat ist
  es eine Bedingung an die Koeffizienten. Die Zelle „K = 2/3“ ist damit „unter Postulat“, nicht „hergeleitet“.
- **Neu gegenüber H157:** A₄ wechselt auf der Nebendiagonale nur Vorzeichenpaare. Deshalb sind neben cos 3δ (det) auch cos 2δ (aus der Konjugation σ, k282) und
  cos δ erlaubt. Innere δ, also drei verschiedene Massen, entstehen schon aus Ordnung 4 und 6 statt erst aus Ordnung 12.
- **2/9 kommt nicht ohne Fit heraus.** Mit σ als Symmetrie braucht 2/9 ein Koeffizientenverhältnis (β/α = −5,186 in Einheiten Λ = v, auf dem Zweig δ = 2π/3 − 2/9).
  Unter 720 vorab festgelegten einfachen Werten trifft keiner. −3√3 liegt 0,19 % daneben; das sind 368σ in δ und kein Treffer.
- **Die Ladungsmischung c legt δ nicht fest.** Sie dreht nur die Phase um arctan c. Der σ-Term ist |b|² cos(2 arg b).

## Offen gelegt
- Der Überschlag der Vorab-Notiz (B/A ≈ −0,46) gehört zu einem stationären Punkt bei δ = +2/9, der kein globales Minimum ist. Das globale Minimum mit Brannen-Phase
  2/9 liegt auf dem Zweig 2π/3 − 2/9 mit B/A = −0,611 (β/α = −5,186).
- Nachträglich (nicht in der Vorab-Notiz): Allein mit dem Ordnung-4-Term und σ liegt δ bei 0 oder π/2. δ = π/2 gibt schon drei verschiedene Massen,
  Verhältnisse 1 : 0,202 : 0,0102, also nicht die Leptonen (1 : 0,0595 : 0,00029).
- δ_exp ist hier aus √m_e/Σ√m unter der Annahme K = ⅔ bestimmt; der Fehler kommt nur aus m_τ.

## Dixon-Zellen (nur eingeordnet)
„Order-3 cycle“ und „mixing“ bei den Dixon-Kopien: H140–H146 haben gezeigt, dass die Kopien eine S₃ tragen, die Massen aber nicht aus den Kopien folgen (H146) und
eine Mischung nicht hergeleitet ist. Dort gibt es keinen Ort für eine Phase δ. Nicht neu gerechnet.

## Grenzen
- Nur der Zirkulantensektor; Stabilität gegen nicht zirkulante Richtungen nicht gerechnet (k282: ℤ₃-Vakua in vier von acht Vorzeichenfällen).
- Ebenen-Lesart des Postulats wie H157; Baumniveau; Λ = v ist eine Wahl.
- Offen bleibt: Was legt v/s fest? Das Verhältnis Spin 1 zu Spin 2 ist die Stelle, an der eine Herleitung ansetzen müsste.
- OP3, OP4 offen; kein Vorzeichen gesetzt; kein Guard berührt.
