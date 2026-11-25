# Vorab-Notiz H141: Eine vierte „Generation“ aus den fehlenden Zuständen (24 − 15 = 9)

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Dimensionen (Kern 9, Kokern 1) folgen aus H140d; die
su(3)-Zerlegung des Kerns und das Verhalten unter der Kopienladung habe ich vor der Rechnung grob überschlagen (unten als Erwartung genannt).
Anlass: Frage des Autors (25.11.2026, 19:56): „was passiert, wenn du eine 4. Generation dazu nimmst, die die restlichen Zustände hält?“

## Vorwissen geprüft
- H140 (94694e6, k323): drei Kopien C_k = ℂ⊗O_k, gleiche Farbe su(3), je Kopie Ladung Q_k (Generationsspektrum), keine gemeinsame Ladung,
  dim(C₀ + C₁₂₀ + C₂₄₀) = 15 in ℂ⊗𝕊.
- H139 (c41040c, k322): Nullteiler von 𝕊 = flaches Kopienprofil; Rang-1-Elemente (eine Kopienrichtung) nie Nullteiler.
- H138: Imaginärteile der drei Kopien linear abhängig (f₀ + f₁₂₀ + f₂₄₀ = 0).
- k255: Produkt Kopie 0 × Kopie 120 fällt zu 0,87 in die dritte Kopie.

## Aufbau
Getrennte Träger V = C₀ ⊕ C₁₂₀ ⊕ C₂₄₀ (24 komplex) mit der Summenabbildung Φ: V → ℂ⊗𝕊, Φ(x₀, x₁, x₂) = x₀ + x₁ + x₂.
„Rest“ = Kern K = ker Φ (die Zustände, die in 𝕊 nicht sichtbar sind) und Kokern (ℂ⊗𝕊 ⊖ Bild Φ). Auf V wirken su(3) (gemeinsam, je Summand),
die Kopienladung Q_⊕ = Q₀ ⊕ Q₁ ⊕ Q₂, ψ (Kopie k → k + 1) und das komponentenweise Produkt (x_k)(y_k) = (x_k y_k).
Skript k324 (Python), Gegenprobe k324b (Wolfram, exakt).

## Hypothesen und Kriterien
- **H141a (Kern = Generation plus ein Singulett):** dim K = 9, Kokern = span(e₈) (dim 1); unter su(3) zerfällt K in 1 ⊕ 1 ⊕ 1 ⊕ 3 ⊕ 3̄
  (Casimir 0 dreifach, −⅔ sechsfach); K ist su(3)- und ψ-invariant (Leck < 10⁻¹²).
- **H141b (Rest ist kein abgeschlossener Sektor):** K ist **nicht** invariant unter Q_⊕ (Leck ‖(1 − P_K) Q_⊕ P_K‖ > 10⁻³) und **nicht**
  abgeschlossen unter dem komponentenweisen Produkt (Leck > 10⁻³). Erwartung vorab: beides verletzt, weil der Realteil e₇·a in allen drei
  Kopien gleich ist und sich nicht aufhebt.
- **H141c (Rest ≠ Nullteiler-Familien):** Kein Komponentenvektor eines Kernelements ist ein Nullteiler von 𝕊 (kleinster Singulärwert von
  L_{x_k} > 10⁻⁶ für 500 zufällige Kernelemente, alle k); und das Bild Φ(K) = 0 enthält definitionsgemäß keine. Der Kokern e₈ ist kein
  Nullteiler (smin = 1).
- **H141d (gemeinsame Ladung mit vierter Generation):** Auf V gibt es dann eine gemeinsame erhaltene Ladung, wenn Q_⊕ die Zerlegung
  V = K^⊥ ⊕ K erhält; dann wäre Φ Q_⊕ Φ⁺ eine wohldefinierte gemeinsame Ladung auf dem Bild. Kriterium wie H141b: Leck < 10⁻¹⁰ heißt ja.
  Erwartung: nein (folgt aus b).
- **Erkundung ohne Kriterium:** Spektrum der auf K gestauchten Ladung P_K Q_⊕ P_K und ihre Zuordnung zu den su(3)-Teilen; S₃-Darstellung auf K.

## Folge, vorab festgelegt
- a bestätigt, b bestätigt: Die fehlenden Zustände haben die Farbstruktur einer Generation plus ein Singulett, bilden aber keinen
  ladungserhaltenden oder abgeschlossenen Sektor. Eine vierte Generation „aus dem Rest“ wäre dann kein gleichwertiges Mitglied.
- d widerlegt-Erwartung (keine gemeinsame Ladung): Die vierte Generation repariert H140c nicht.
- Was in keinem Fall folgt: Massen, Mischung, Vorzeichen; ein physikalisches Verbot einer vierten Generation. OP3, OP4 offen; kein Guard berührt.
- Vergeben: H141, k324. (Der in H140 vorgeschlagene Test „Ladungserhaltung im Kopienprodukt“ ist hier nicht enthalten, weil die k85-Ladung
  schon innerhalb einer Kopie keine Derivation ist; das wäre erst mit einer anderen Ladungsdefinition sinnvoll.)
