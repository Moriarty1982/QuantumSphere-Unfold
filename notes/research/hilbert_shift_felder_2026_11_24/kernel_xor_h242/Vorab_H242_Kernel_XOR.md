# Vorab H242 (k458): Ist die alte Kernel-Definition K₃ = K₁K₂ dieselbe Struktur wie die drei Kopien? Folgt eine Generationenregel?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (20:26): „naja wir hatten k3 mal ganz am anfang so definiert, dass er senkrecht auf
normalen der anderen beiden stehen soll, geometrisch ist das ein xor“.

## Vorwissen geprüft (Fundstellen der alten Definition)
- **Companion, Definition „Biquaternion kernel“** (`sources/parts/03_core_sphaera_and_physics_baseline.tex`, label def:biquaternion; gleichlautend in
  v4.7.0 bis v4.11.0):
  - Der Grundzustand einer Schicht besteht aus drei komplexen Sphären K₁, K₂, K₃ mit q_n = it·1 + z₁e₁ + z₂e₂ + z₃e₃ ∈ ℍ ⊗ ℂ.
  - Es gilt **e₃ := e₁e₂**, „hence automatically orthogonal to both e₁ and e₂“ (Proposition „Orthogonality of the third kernel“).
  - Die Koordinaten z_k ∈ ℂ sind komplex.
- **Sektorzuordnung** (Definition „Sector classification from biquaternion“):
  - Materie K₁: Re z₁ < 0.
  - Tachyon K₂ = J·K₁: Re z₂ > 0.
  - Photon K₃ = e₁e₂: Re z₃ = 0.
  - Der Vorzeichen-Code wurde in v4.9.0 als Orientierungscode markiert.
- **Proposition „Compensator“ (korrigiert in v4.9.0-r03.4):** Orthogonal zu beiden Eingängen ist das Produkt z × J_B z = 2E × B, nicht der Mittelwert.
- **AGENTS.md:** Die Tachyon-Abbildung ist z ↦ iz, die Zeitumkehr ist z ↦ z̄.
- **H241/k457 (symbolisch bewiesen):** u_α(p)·u_β(q) = −(p·q)[cos(β−α) + sin(β−α)e₈] + u_{−(α+β)}(p × q), mit u_α(p) = (cos α·p, sin α·p).
  Die Kopien liegen bei 0°, 120° und 240° und folgen dem Produktgesetz k₁ + k₂ + k₃ ≡ 0 (mod 3). Außerdem gilt e_i e_j = ±e_{i⊕j}.

## Einbettung (gesetzt)
ℍ ⊗ ℂ ⊂ 𝕆 ⊗ ℂ wird nach 𝕊 abgebildet durch z·e_k ↦ u_{arg z}(|z|·e_k) = (Re z·e_k, Im z·e_k). Die imaginäre Einheit i der Koordinaten wird also zur Wand
e₈. Das ist natürlich, weil die Rechtsmultiplikation mit e₈ den Vektor (p, 0) auf (0, p) abbildet. Für die Basis werden e₁, e₂ und e₃ = e₁e₂ aus 𝕆 gewählt.

## Vorhersagen aus H241 (nicht blind)
- **N1:** K₃ := K₁K₂ steht für alle Phasen senkrecht auf K₁ und K₂, und seine Phase ist α₃ = −(α₁ + α₂). Die alte Definition übersetzt sich also
  in „Phasen addieren sich zu null“.
- **N2:** span{1, K₁, K₂, K₃} ist genau dann eine Quaternion-Unteralgebra von 𝕊, wenn α₁ + α₂ + α₃ ≡ 0 (mod π).
- **N3:** Bei gemeinsamer Phase α schließt das Tripel genau dann, wenn 3α ≡ 0 (mod π). Das sind genau die drei Kopien.
- **N4 (Generationenregel, Kandidat):** Liegen alle drei Phasen auf den Kopien (g_k ∈ ℤ₃), dann schließt das Tripel genau dann, wenn
  g₁ + g₂ + g₃ ≡ 0 (mod 3). Das sind 9 von 27 Belegungen: 3 mit allen Kernen in derselben Kopie und 6 mit je einem Kern in jeder Kopie.

## Rechnung
- **A:** Für 2000 zufällige Phasentripel wird der Schlussrest von span{1, K₁, K₂, K₃} berechnet (Anteil der Produkte außerhalb), zusammen mit
  |sin(α₁ + α₂ + α₃)|. Geprüft wird, ob der Rest genau dann verschwindet, wenn die Summenregel gilt. Dazu Stichproben auf der Regel (α₃ = −α₁ − α₂).
- **B:** Die 27 Kopien-Belegungen: welche schließen?
- **C:** Orthogonalität K₃ ⟂ K₁, K₂ für alle Phasen.
- **Zufallskontrolle:** Anteil zufälliger Phasentripel mit Schlussrest < 10⁻⁶.
- **Nur Bericht:**
  - Mit K₂ = J·K₁, J = i (α₂ = α₁ + 90°): für welche α₁ ist das Photon-Kriterium Re z₃ = 0 erfüllt?
  - Die Brannen-Phasen δ + 2πk/3: Summe und Schluss.

## Urteil
- **Frage 1 (gleiche Struktur):** trägt, wenn N1 bis N3 exakt gelten und die Zufallskontrolle unter 10⁻³ bleibt. Weil N1 bis N3 aus H241 folgen, wird ein
  „trägt“ als nicht blind geführt.
- **Frage 2 (Generationenregel):** „Regel folgt“, wenn genau die 9 Belegungen mit g₁ + g₂ + g₃ ≡ 0 schließen. Ob das physikalische Generationen sind, wird
  **nicht** gewertet. Dazu fehlen Massen und Mischung.
- **widerlegt:** Der Schluss hängt nicht an der Phasensumme, oder die Kopien-Belegungen schließen anders.

## Werkzeuge
Python k458, Wolfram k458b (symbolisch: Produkt K₁K₂ und Schluss der Quaternion-Tafel unter der Summenregel). Qiskit nicht einschlägig.
