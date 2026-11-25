# Ergebnis H141: Die fehlenden 9 Zustände sind ein Quark-Satz (3 ⊕ 3̄, Ladung ⅓ und ⅔) plus drei Singuletts mit Ladung ½; kein abgeschlossener Sektor, keine gemeinsame Ladung

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H141_Vierte_Generation_Rest.md` (Commit 589b1c3, vor der Rechnung; teilweise nicht blind).
Skripte `k324_vierte_generation.py` (`k324_out.txt`), `k324b_gegenprobe.wl` (`k324b_out.txt`, Wolfram exakt). Status: H141a bestätigt,
H141b bestätigt, H141c bestätigt, H141d: keine gemeinsame Ladung (wie erwartet).**

Anlass: Frage des Autors: Was passiert, wenn man eine vierte Generation dazunimmt, die die restlichen Zustände hält?
Werkzeuge: Python (numpy) für Kern, Farbe, ψ, Ladung, Produkt und Nullteiler; Wolfram Language exakt für Kern, Ladungs-Leck und Spektrum.
Qiskit nicht eingesetzt.

## Aufbau in einem Satz
Die drei Kopien als getrennte Träger V = C₀ ⊕ C₁₂₀ ⊕ C₂₄₀ (24 Zustände) werden durch Φ(x₀, x₁, x₂) = x₀ + x₁ + x₂ in ℂ⊗𝕊 abgebildet. Bild 15,
**Kern 9** (die Zustände, die sich in 𝕊 gegenseitig aufheben), Kokern 1 (= e₈). Der Kern ist der Kandidat für die „vierte Generation“.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H141a | dim K = 9, Kokern = e₈; su(3): 1 ⊕ 1 ⊕ 1 ⊕ 3 ⊕ 3̄ (Casimir 0 dreifach, Triplett-Wert sechsfach); su(3)- und ψ-Leck ≤ 3·10⁻¹⁶ | vorab | **bestätigt** |
| H141b | Ladungs-Leck ‖(1 − P_K)Q_⊕P_K‖ = ½ (exakt, drei Richtungen); Produkt-Leck bis 8,9 | > 10⁻³ | **bestätigt** (nicht abgeschlossen) |
| H141c | Komponenten von Kernelementen: smin(L_x) = 1,0000; e₈: smin = 1 | > 10⁻⁶ | **bestätigt** (keine Nullteiler) |
| H141d | [Q_⊕, P_K] = ⅓ ≠ 0 (exakt) | < 10⁻¹⁰ hieße ja | **keine gemeinsame Ladung** |

**Erkundung (gestauchte Ladung auf K, Wolfram exakt):** Spektrum {⅓, ⅓, ⅓, ½, ½, ½, ⅔, ⅔, ⅔}.
- Der Farbteil 3 ⊕ 3̄ (6 Zustände) ist **ladungserhaltend** (Leck 0 in diesen Richtungen) und trägt genau die Quarkladungen ⅓ und ⅔ einer
  Generation. Unter ℤ₃ (ψ) ist er invariant (Spur 6 auf 6 Dimensionen).
- Die drei Singuletts tragen nur den Mittelwert ½ statt 0 und 1 (kein Neutrino, kein Elektron) und lecken unter der Ladung aus dem Kern
  (Leck ½). Unter ℤ₃ tragen sie 1 ⊕ 2 (Spur 0).

## Lesart
- **Antwort auf die Frage:** Eine vierte „Generation“ aus dem Rest hat genau die Farbstruktur einer Generation (plus ein überzähliges Singulett),
  aber nur ihr **Quark-Teil** ist stabil unter der Ladung, mit den richtigen Quarkladungen. Der Lepton-Teil fehlt: Die Singuletts haben die Ladung ½
  und bleiben nicht im Rest. Ein vollwertiges viertes Mitglied entsteht nicht, und die vierte Generation repariert die fehlende gemeinsame Ladung
  aus H140 nicht.
- **Zu den Nullteilern (H139):** Der Rest fällt nicht mit den Nullteiler-Familien zusammen. Seine Komponenten liegen je in einer Kopie und sind
  keine Nullteiler; im Gesamtbild sind es Zustände, die sich in 𝕊 aufheben (Φ = 0), nicht solche, die etwas annihilieren.
- **Nachträglich bemerkt:** Dass gerade die Farbtripletts des Rests ladungsstabil sind und die Singuletts nicht, liegt daran, dass der Realteil
  (e₇·a) in allen drei Kopien gleich ist und sich nur für die Farbrichtungen (a ⊥ e₇) aufhebt. Ob „ein stabiler Quark-Satz ohne Leptonen“ physikalisch
  etwas bedeutet (etwa als Hinweis, dass eine vierte Familie nur farbig vorkommen könnte), ist nicht gezeigt.
- Massen, Mischung, Vorzeichen nicht berührt. OP3, OP4 offen; kein Guard berührt.
