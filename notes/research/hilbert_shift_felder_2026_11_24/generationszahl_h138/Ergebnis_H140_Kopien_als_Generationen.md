# Ergebnis H140: Die drei Kopien haben dieselbe Farbe und je eine Generation, aber keine gemeinsame Ladung; in ℂ⊗𝕊 sind sie keine drei Generationen

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H140_Kopien_als_Generationen.md` (Commit 94694e6, vor der Rechnung; teilweise nicht blind).
Skripte `k323_kopien_generationen.py` (`k323_out.txt`), `k323b_gegenprobe.wl` (`k323b_out.txt`, Wolfram exakt). Status: H140a bestätigt,
H140b bestätigt, H140c bestätigt (keine gemeinsame Ladung, exakt), H140d = 15 wie erwartet. Nach der vorab festgelegten Folge sind die Kopien
in ℂ⊗𝕊 damit keine drei Generationen.**

Werkzeuge: Python (numpy, scipy) für Farbe, Ladung, Suche über die Familie α + βL_x + γR_x (500 Starts); Wolfram Language exakt für das Leck mit
symbolischem x, für ψQ₀ψ⁻¹ ≠ Q₀ und die Dimension. Qiskit nicht eingesetzt (keine Schaltung). su(2)_L nicht gerechnet: Auf einem Träger ℂ⊗ℍ⊗𝕊
wirkt sie auf einen anderen Tensorfaktor als S₃ und vertauscht per Konstruktion (Setzung).

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| ψ, ε Automorphismen; ψ: Kopie k → k + 1, u_k → u_{k+1} | 9·10⁻¹⁵; ≤ 8·10⁻¹⁶ | < 10⁻¹² | erfüllt |
| dim su(3)_k | 8, 8, 8 | 8 | erfüllt |
| Spektrum Q₀ auf C₀ (k85) | 0, ⅓³, ⅔³, 1 | vorab | erfüllt |

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H140a | su(3)_0 = su(3)_120 = su(3)_240 (Hauptwinkel-cos 1,000000000000); [su(3), ψ], [su(3), ε] ≤ 6·10⁻¹⁶; je Kopie Casimir 0 (2×), −⅔ (6×), kein Leck | < 10⁻¹⁰ / 10⁻¹² | **bestätigt** |
| H140b | Q_k bildet C_k in sich ab (Leck ≤ 2·10⁻¹⁶), Spektrum je eine Generation, [Q_k, su(3)] = 0 auf C_k, ψQ_kψ⁻¹ = Q_{k+1} (≤ 4·10⁻¹⁶) | < 10⁻¹² | **bestätigt** |
| H140c | min Leck² = 3,0000 (500 Starts); exakt: Leck(βL_x + γR_x) = (12\|β\|² + 12\|γ\|² − 18 Re β̄γ)(\|x\|² + x₈²) ≥ 3\|x\|² | > 10⁻³ | **bestätigt** (keine gemeinsame Ladung) |
| H140d | dim(C₀ + C₁₂₀ + C₂₄₀) = 15 | 15 < 24 | wie erwartet (nicht blind) |
| Zusatz | ‖ψQ₀ψ⁻¹ − Q₀‖ = 0,75; ‖[Q₀, Q₁]‖ = 0,24; Q₀ leckt aus C₁₂₀ (0,375) | berichtet | |

## Warum es scheitert
- **Farbe ist gemeinsam.** Die Ladungsrichtungen u_k = e₇ ⊗ f_k liegen alle im selben G₂-Vektor e₇, nur in verschiedenen Kopienrichtungen. G₂
  wirkt blockweise gleich, also ist der Stabilisator su(3) für alle drei derselbe, und S₃ vertauscht mit ihm (S₃ wirkt nur auf den Kopienindex).
  Test (2) des Auftrags trägt für die Farbe vollständig.
- **Ladung ist je Kopie verschieden.** Jede Kopie hat ihre eigene Ladung Q_k, mit identischer Darstellung (Test (1) trägt je Kopie), aber
  ψ verschiebt Q_k nach Q_{k+1}; S₃ vertauscht also nicht mit der Ladung. Eine Ladung, die alle drei Kopien zugleich erhält, gibt es in der
  ganzen Familie α + βL_x + γR_x nicht: Das Leck ist exakt eine positive quadratische Form in x, mit Minimum 3|x|² > 0. Grund: Jedes
  imaginäre x liegt in höchstens einer Kopie (paarweiser Schnitt ℝ), und L_x, R_x erhalten nur Unteralgebren, die x enthalten.
- **Zu wenig Platz.** Die drei Kopien überdecken zusammen nur 15 komplexe Dimensionen statt 24 (Rang 2 der Imaginärteile, H138).

## Lesart
- **Was gezeigt ist:** Jede Kopie trägt für sich genau eine Generation mit gleicher Farbe und gleichem Ladungsspektrum, und die Farbe ist für
  alle drei dieselbe und S₃-symmetrisch. Das ist mehr als ein bloßes Etikett: Die Kopien sind **drei gleichwertige Lesarten einer Generation**.
- **Was nicht geht:** Gleichzeitig drei Generationen mit einer gemeinsamen elektroschwachen Ladung in ℂ⊗𝕊. Die Kopienvertauschung bricht die
  u(1) (genau wie k255d), und die Zustände reichen nicht.
- **Wie man es doch zeigen könnte (Vorschlag, nicht gerechnet):** Die drei Kopien als *getrennte* Träger nehmen (ℂ⊗(O₀ ⊕ O₁₂₀ ⊕ O₂₄₀), extern,
  24 Zustände) und die Ladung je Kopie mit ihrer eigenen Richtung u_k definieren. Dann ist die Ladung über die Isomorphie gleich, aber erst eine
  Wechselwirkung (Kopplung zwischen den Kopien, etwa das Produkt O₀ · O₁₂₀ → O₂₄₀ aus k255) entscheidet, ob das Standardmodell-artig ist. Das
  ist der Weg B der Trialität (K28), hier mit den Sedenion-Kopien als Etikett. Prüfbar wäre: Ist die Kopplung zwischen den Kopien mit der je
  Kopie definierten Ladung verträglich (Ladungserhaltung im Produkt)? Das braucht eine neue Vorab-Notiz.
- Massen, Koide, Mischung und Vorzeichen nicht berührt. OP3, OP4 offen; kein Guard berührt.
