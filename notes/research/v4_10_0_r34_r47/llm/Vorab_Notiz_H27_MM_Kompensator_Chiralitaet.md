# Vorab-Notiz H27: Ein Heisenberg-Kompensator der Millennium-Matrix als Chiralitätsprojektor

Festgelegt am 2026-10-23, **vor** der Rechnung. Autorhinweis (2026-10-23): Für die fehlende Singulett-Hälfte war die MM-Matrix gedacht,
die verschiedene HC in sich tragen sollte. Bezug: `sec:millennium-hc` (𝓜₁₆, 16 × 16; globale HC-Lesart erweitert C = ½(id + J) auf alle
Schichten), `thm:hc-spectral-projector` (C = Spektralprojektor von 𝓜), `def:v470-r01-sided-mm-hc-channel-split`, H20/r35 (innere Einheit
J_in = L_{e₇}, äußere i, P_± = ½(1 ∓ i J_in)), H26/r41 (Aufteilung D: nur Dubletts, Singuletts fehlen).

## Rahmen

Aufteilung D aus r41 auf ℂ⊗ℍ⊗𝕆 ≅ ℂ³² (ℂ-Faktor als Skalar i). Zusätzlich der Kompensator
  **C_ch := ½(1 + J), J := i·L_{e₇}** (auf 𝕆, gehoben auf ℂ⊗ℍ⊗𝕆); J² = 1, also C_ch ein Projektor in der Form ½(id + J).
Wirksame schwache SU(2): T_a′ := C_ch T_a (T_a = −(i/2)R_a von rechts). Hyperladung: Y/2 := Q − ½ + (1 − C_ch)T₃.
Elektrische Ladung wie in r41: Q_em := T₃ + Q − ½ (= T₃′ + Y/2).

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

C_ch = P₋ aus H20c; sein Bild sind die Q-Sektoren {0, 2/3}. Auf dem Bild bleibt alles wie in r41 (Dubletts (ν, e), (u, d)); auf dem Kern
(Sektoren 1/3, 1) wird die schwache Wirkung null, und Y/2 = Q − ½ + T₃ ergibt dort −1/6 ± 1/2 = 1/3, −2/3 und 1/2 ± 1/2 = 1, 0: die
Hyperladungen von d^c, u^c, e^c, ν^c. Das ist genau der linkshändige Inhalt einer Generation des Standardmodells mit ν_R. **Das Muster ist
also vorab gesehen, nicht vorhergesagt**; die Rechnung prüft es an den Matrizen. Die Wahl von J = i·L_{e₇} und die Form von Y/2 sind durch
dieses Ziel motiviert. Nicht vorab ausgerechnet: die Anomalie-Spuren (H27c) und die Frame-Wirkung (H27d).

## Hypothesen

- **H27a (Kompensator):** C_ch ist hermitesch und idempotent, von der Form ½(id + J) mit J² = 1; es vertauscht mit Farbe, Lorentz, der
  schwachen SU(2) (R_q) und Q; sein Bild ist genau die Summe der Q-Sektoren 0 und 2/3 (komplexe Dimension 16 von 32).
- **H27b (Quantenzahlen):** Unter (Farbe, schwache SU(2)′, Y/2) zerfällt ℂ³² genau in (3, 2, 1/6), (1, 2, −1/2), (3̄, 1, −2/3), (3̄, 1, 1/3),
  (1, 1, 1), (1, 1, 0), jeweils zweifach (Lorentz-Index), zusammen 16 Weyl-Zustände × 2. Q_em = T₃′ + Y/2 überall; Y/2 vertauscht mit
  SU(2)′, Farbe und Lorentz.
- **H27c (Anomalien):** Über die 16 Zustände (ein Lorentz-Index) verschwinden Tr(Y/2), Tr(Y/2)³, Tr_{Dubletts}(Y/2) und Tr_{Tripletts}(Y/2)
  (gravitative, kubische, SU(2)²U(1)- und SU(3)²U(1)-Anomalie; Tripletts und konjugierte Tripletts gleich gewichtet).
- **H27d (Chiralität und Frame):** SU(2)′ wirkt nur auf dem Bild von C_ch (16 von 32), auf dem Kern trivial. T C_ch T⁻¹ = 1 − C_ch: Im
  T-Frame wirkt die schwache SU(2) auf der anderen Hälfte.
- **H27e (MM-Lesart, Kontrolle):** 𝓜 := λ₀ C_ch + λ₁(1 − C_ch) mit λ₀ ≠ λ₁ hat C_ch als Spektralprojektor zum Eigenwert λ₀ und vertauscht
  mit C_ch (Bedingung von `thm:hc-spectral-projector`). Trivial; Lesart: ein Kompensator der MM-Matrix trennt die Chiralitäten.

## Entscheidungskriterium (verbindlich)

Jede Hypothese bestätigt oder widerlegt nach der wörtlichen Aussage (Toleranz 10⁻⁹). Einordnung vorab:
- H27a, b bestätigt ⇒ Ein Kompensator der Form ½(id + J), mit J aus innerer und äußerer Einheit, ergänzt D zum vollständigen
  linkshändigen Inhalt einer Generation mit den richtigen Quantenzahlen. Das ist eine **Konstruktion unter Wahlen**, keine Herleitung; sie
  zeigt, dass die Companion-Bausteine (HC, zwei Einheiten, zwei Seiten, Triality) dafür ausreichen.
- H27c ist eine Folge des Inhalts (das Standardmodell ist anomaliefrei), keine unabhängige Bestätigung.
- Ob 𝓜₁₆ mit genau diesen 16 Zuständen gemeint war, bleibt eine Lesart; die Zahl 16 wird festgehalten, nicht gedeutet.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
