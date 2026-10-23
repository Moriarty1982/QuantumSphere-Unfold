# Prüfung: Dixon-Ablage, Hilbert-Shift-Leiter und gemischte Readouts

Stand 2026-10-23. Konsistenzprüfung, keine Vorhersage, kein Datenvergleich. Skript `k71_dixon_ablage.py`.
Anlass: Autorhinweis, die Dixon-Algebra sei als Objekt gedacht gewesen, in dem sich alle Konfigurationen ablegen
lassen, und die gemischten Readouts seien angelegt, aber nie benutzt worden.

## 1. Was im Companion steht (Fundstellen)

| Stelle | Inhalt |
|---|---|
| `def:qam-hilbert-shift-plan` (Z. 1818) | H(⟨i, x…⟩) = ⟨i+1, x…⟩, Tag 0 wird frei für „keine aktive Art“ |
| `def:binary-mask-registry-mixed-readouts` (Z. 1855) | Readout-Art j → Bit 2^j; gemischter Readout = ODER aktiver Bits |
| `def:v3360-r16-double-hilbert-shift-route-mask-convention` (Z. 2261) | H₀(k) = k+1, H_mask(k) = 2^k, Rückübersetzung `back` |
| `def:r03-guarded-mixed-readout-normal-form`, `def:r03-boolean-selector-mask-grammar` (Z. 2029 ff.) | Normalform (I, R_i, Γ, χ, μ, J), Masken-Grammatik ∨, ∧, ⊕, ¬_Ω |
| Delta-Schicht „Dixon-Carrier Coding“ (Z. 45017 ff.) | Leiter HS(n): Träger C_n = 2^n Kanäle, 2^{C_n} Masken; HS(3) = 8 Fano/Oktonion, HS(6) = 64 Dixon ℂ⊗ℍ⊗𝕆 |
| `thm:three-generations` (Z. 6841) | Gen_i ≅ (ℂ⊗ℍ)⊗e_{i+3} in der Dixon-Algebra; kein `\qsstatus`-Vermerk |

Die Dixon-Ablage indiziert jeden Kanal mit α = (a, b, c), a ∈ {0,1} (ℂ), b ∈ {0..3} (ℍ), c ∈ {0..7} (𝕆). Jede zulässige
Route bekommt eine Maske χ_Dix ∈ {0,1}⁶⁴ (Karte, Selektorwort, Seite, Fano-/Oktonion-Kanal). Blockierte, leckende und
verschuldete Routen werden gesondert markiert. Das passt zur Absicht „ein Objekt, in dem alle Konfigurationen abgelegt
werden“.

## 2. Gemischte Readouts: angelegt, nie gefüllt (bestätigt)

- Die Definitionen (Z. 1811–2142) werden nur innerhalb desselben Blocks referenziert. `def:binary-mask-registry-mixed-readouts`,
  `prop:mixed-readout-factorization`, `def:guarded-mixed-qam-readout`, `def:qam-hilbert-shift-plan` und
  `def:r03-boolean-selector-mask-grammar` haben **keinen einzigen** Verweis.
- Spätere Verwendung nur **strukturell**: als Zulässigkeitsbedingung an Kanten (`sec:v410r18-mixed-readout-edge-compatibility`, Z. 41645 ff.: HC/MML,
  Selektor/QAM …) und als Kontraktionsregel der Tensornotation (Z. 51537; r93, Z. 64770 ff.: gleichartige Indizes nur
  über ein benanntes G_αβ oder χ_mn).
- **Kein** gemischter Readout wird irgendwo mit konkreten Komponenten, Aggregation μ und Zahlenwert ausgewertet. Die
  Tensornotation χ_mn R^m S^n könnte das ausdrücken, wurde aber nie so verwendet.
- Die Konservativitätssätze (`prop:r03-mask-filter-conservativity`, `lem:v3360-r16-double-shift-conservativity`)
  sagen: Masken wählen und kodieren, ändern aber keine Nutzdaten. Allein aus Masken folgt also keine Größe wie eine Masse.

## 3. Das Generationen-Tripel in der Dixon-Ablage (M)

- ℍ⊗𝕆 = 𝕆 ⊕ (Im ℍ)⊗𝕆, und (Im ℍ)⊗𝕆 = i⊗𝕆 ⊕ j⊗𝕆 ⊕ k⊗𝕆 hat die 24 Dimensionen von 𝕆³. Das Tripel aus r14/r15 lässt
  sich also verlustfrei ablegen: Maske {a = 0, b ∈ {i, j, k}, c beliebig}, 24 von 64 Bits.
- Die 3 × 3 farbigen Zustände (c ∈ {e₄, e₅, e₆} im Rahmen u = e₇) sind eine Teilmaske mit 9 Bits.
- G₂ wirkt auf den 𝕆-Faktor, Aut(ℍ) = SO(3) auf den ℍ-Faktor. Beide vertauschen, und Farbe und Generation sind damit
  getrennt, wie r14 verlangt.

## 4. Wo es nicht ganz passt (M)

- Die Triality-Form Re((xy)z) ist invariant unter der zyklischen Vertauschung und unter (x,y,z) → (x̄,z̄,ȳ).
- Von den 24 Vorzeichen-Permutationen der Plätze in SO(3) = Aut(ℍ) lassen nur **12** die Form invariant: die
  zyklischen Permutationen mit einer geraden Zahl von Vorzeichenwechseln. Die Gruppe ist abgeschlossen und ≅ **A₄**
  (Drehgruppe des Tetraeders).
- Die Vertauschungen der Triality-S₃ brauchen die Oktonion-Konjugation. Die ist auf 𝕆 ein Anti-Automorphismus,
  (xy)* = y*x*, also keine Symmetrie der Ablage im Sinn von Aut(ℍ) × G₂.
- Gemeinsame Symmetrie von Ablage und Triality-Form ist also A₄ (bzw. ihr zyklischer Teil ℤ₃), nicht die volle S₃.
- Konflikt mit `thm:three-generations`: Dort trägt ℂ⊗ℍ = M(2,ℂ) den Lorentz-Spinor. Legt man die Generationen in Im ℍ
  ab, steht der ℍ-Faktor dafür nicht mehr zur Verfügung. Beides gleichzeitig geht in einer einzigen Dixon-Algebra nicht.

## 5. Einordnung

- Die Dixon-Ablage ist als Register in sich stimmig und kann das Generationen-Tripel und die Farbe getrennt tragen.
- Dass als gemeinsame Symmetrie A₄ herauskommt, ist ein struktureller Befund, keine Vorhersage. In der Literatur ist A₄
  eine bekannte Flavour-Gruppe für die Leptonmischung; ihr bekanntestes Muster, die tribimaximale Mischung, ist durch
  θ₁₃ ≠ 0 ausgeschlossen. Ob sich daraus etwas Prüfbares ergibt, wäre eine eigene Vorab-Notiz.
- Die gemischten Readouts wären das passende Werkzeug, um die Ablage zu *benutzen*: Ein Readout, der die drei
  Platz-Bits mit einer festgelegten Aggregation μ zusammenführt, ist genau eine explizite Brechung der S₃ (bzw. A₄).
  Mit Masken allein entsteht keine Größe; μ und J_mix müssen als neue Vermutung angegeben werden.
- Offene Autorentscheidung: `thm:three-generations` hat noch keinen `\qsstatus`-Vermerk, obwohl r13/r14 Farbe und
  Generation darin als Doppelbelegung festgestellt haben (Kandidat für Regel C).

## 6. Frames (Autorhinweis: die Dixon-Grammatik wurde mit Bezug auf den Photon-Frame geschrieben)

- v4.9.0-r23 ordnet die OP5-Halo-/Kollar-/Tunnel-/Dixon-Grammatik in Klasse **N** ein: Sie trägt den Namen „photon frame“,
  aber keine Frame-Größe (kein β, γ_L, z₋). Nach r24.3 ist „photon frame“ des Hauptkorpus der **Bezugsframe R**
  (reiner Zustand, |b| = 1), nicht der Photon P der Konvention F (maximal gemischt).
- Die Befunde 3 und 4 sind algebraisch und enthalten keine Frame-Größe. Gezeigt sind sie in R, wie die Ablage geschrieben ist.
- Für M und T fehlt eine Festlegung, wie J_B auf der Dixon-Ablage wirkt. [Korrigiert in Abschnitt 8: Die hier zuerst
  genannte Konjugation auf dem ℂ-Faktor ist nach r30.2(b) die Zeitumkehr T, nicht J_B.] Erste Fassung:
  Konjugation auf dem ℂ-Faktor (Index a). Sie ändert nur Vorzeichen, nicht die Menge der aktiven Kanäle. Masken und das
  Tripel bei a = 0 wären dann frame-frei. Das ist eine Annahme, kein Befund.
- Namensfalle: „gemischter Readout“ (QAM: Zusammenfassung mehrerer Readout-Arten) ist nicht „gemischter Zustand“
  (Dichtematrix; P ist der maximal gemischte Zustand). Beides nicht verwechseln.
- Folge für einen Test mit gemischten Readouts: Gewichtet die Aggregation μ die Platz-Bits mit den Port-Gewichten p± des
  Dubletts, ist die Brechung frame-abhängig: in M (0,768; 0,232), in T vertauscht, in P beide ½, also ohne Brechung (F2).
  Eine Vorab-Notiz muss den Frame der Massen-Ablesung festlegen (wie bei der Koide-Phase: nur Materie).

| Befund | M / T / P (und R) |
|---|---|
| Tripel = (Im ℍ)⊗𝕆, Farbe als Teilmaske, A₄ | algebraisch, in R gezeigt; M/T frame-frei unter der Annahme J_B = ℂ-Konjugation; P nicht ausgewertet |
| gemischte Readouts nie ausgewertet | Bestandsaufnahme, frame-unabhängig |
| port-gewichtete Aggregation (künftig) | M und T vertauscht, P ohne Brechung |

## 7. Lean

Die Befunde 3 und 4 sind in `formal/QSFormal/Dixon.lean` bewiesen (Lean 4.35.0, ohne Mathlib, nur Standard-Axiome), dazu die
Polynom-Kerne von r26.1 und r32.1. Nicht formalisiert: der abstrakte Isomorphismus zu A₄ und der Schritt vom negativen
Hauptminor zum Sattelpunkt.

## 8. J_B auf der Ablage (Lean, `formal/QSFormal/Dixon.lean`)

Nach v4.9.0-r30.2(b) gilt J_B = R_{π/2} ∘ T mit T: z ↦ z̄ und R: z ↦ iz. Annahme (A_ℂ): Der ℂ-Faktor der Ablage ist die
Amplitudenebene z. Bewiesen sind dann die Folgerungen in der Tabelle.

| | T (Zeitumkehr) | R (z ↦ iz) | J_B = R ∘ T |
|---|---|---|---|
| auf den a-Hälften | Vorzeichen bei a = 1 | (x, y) ↦ (−y, x), R² = −1 | Vertauschung (σ_x), Involution |
| Tripel-Maske | fest | — | wandert nach a = 1 (disjunkt, 24 Bits) |
| Platznormen (Massen-Lesart) | fest | fest | fest |
| Triality-Form t | t̄ | −i t | −i t̄: (Re, Im) ↦ (−Im, −Re), Betrag fest |

Lesart: Das a-Bit wird zum Bit für den Materie- oder Tachyon-Sektor, wie die σ_z-Kanäle des Dubletts. P hat gleiches
Gewicht auf beiden Hälften. Unter (A_ℂ) ist die Massen-Lesart über Normen frame-frei. Frame-abhängig sind der
Realteil-Readout der Triality-Form und jede port-gewichtete Aggregation. Die im ersten Entwurf genannte
ℂ-Konjugation ist T, nicht J_B. (A_ℂ) selbst ist eine Autorentscheidung.
