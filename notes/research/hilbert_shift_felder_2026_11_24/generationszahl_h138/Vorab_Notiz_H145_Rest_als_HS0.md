# Vorab-Notiz H145: Ist die Rest-Generation wieder ein HS(0)?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Großteils nicht blind:** Die Zerlegung des Rests (H145a, b) folgt analytisch aus der Form
der Summenabbildung Φ und wird nur nachgerechnet. Gewertet sind H145c und H145d. Anlass: Autor (25.11.2026, 20:31): „hört sich blöd an, aber
prüfe mal, ob die Restgeneration evtl. wieder ein HS(0) sein könnte.“ Lesart (über den Koordinator): Trägt der Rest einen eigenen, zu ℝ = HS(0)
isomorphen Anteil (eindimensional, reell, Einheit, Norm), fängt der Turm dort neu an (Cayley–Dickson daraus, Periodizität), und passt das dazu,
dass es auf HS(0) und HS(1) keine Masse im strengeren Sinn gibt?

## Vorwissen geprüft
- **HS(0) im Turm (k253, `../README.md`):** ℝ; Feld auf einer Linie (ψ = 2a cos ωt), Fläche 0, keine Wahl außer ± (S⁰), Der = 0, kein
  Stabilisator; HS(0) ist genau die zeitumkehrinvariante Teilfamilie von HS(1). Keine Masse auf HS(0), HS(1) (Autor 25.11.; k291: Ruhemasse erst
  ab HS(2)). Bott-Periode und S₃ ab HS(4) (k254, r59.7–r59.14).
- **H142, H143:** Rest-Generation genau bei Relationen Σ c_k v_k = 0 mit Σ c_k = 0; Zahl = dim R⁰ (2016/2016). k326c: max dim R⁰ bei 4, 5, 6,
  7, 8, 9 Kopien = 1, 1, 2, 2, 3, 4 (bekannt, also nicht blind für eine „Verdopplung“ der Koeffizienten).
- **H144:** z ↦ z̄ bildet die Rest-Generation auf sich ab (q ↦ 1 − q); Sektorsignatur wie eine Kopie.

## Analytische Vorüberlegung (vor der Rechnung)
Mit dem Transport ι_k: 𝕆 → O_{v_k}, e₀ ↦ e₀, e_i ↦ e_i ⊗ v_k, ist Φ((ι_k(y_k))_k) = (Σ_k y_{k,0}) e₀ + Σ_i e_i ⊗ (Σ_k y_{k,i} v_k).
Der reelle Teil (das HS(0) jeder Kopie, e₀) und der Imaginärteil entkoppeln. Also
**K = (D⁰ ⊗ e₀) ⊕ (R ⊗ Im𝕆)** mit D⁰ = {d : Σ d_k = 0} (dim m − 1) und R = {c : Σ c_k v_k = 0} (Relationen),
dim K = (m − 1) + 7·dim R. Die Ladung mischt e₀ nur mit e₇ (u = e₇ ⊗ v). Daraus:
W = (R⁰ ⊗ span{e₀, e₇}) ⊕ (R ⊗ Farbe₆), R⁰ = R ∩ D⁰; leckend: (D⁰ ⊖ R⁰) ⊗ e₀ und (R ⊖ R⁰) ⊗ e₇.
Die vollständige Rest-Generation ist R⁰ ⊗ ℂ𝕆: eine ganze Oktonion-Kopie über einer reellen Koeffizientenlinie.

## Hypothesen und Kriterien
- **H145a (nicht blind):** Die Zerlegung gilt numerisch in allen Auswahlen von 3, 4, 5 Kopien und allen relativen Orientierungen:
  Abstand der Projektoren auf K, W und den leckenden Teil zu den oben gebildeten Räumen < 10⁻¹⁰. Dazu: ι_k ist ein Algebren-Isomorphismus
  (Produktfehler < 10⁻¹²) und Q wirkt auf c ⊗ y als c ⊗ Q₈ y.
- **H145b (nicht blind):** Die Koeffizientenlinie R⁰ (bei n_gen = 1) hat die HS(0)-Merkmale: reell (unter z ↦ z̄ fest), eindimensional, nur ±c
  als Wahl, ohne Ladung und ohne Farbe (Q und su(3) wirken auf c trivial). Prüfung: numerisch für alle Generationsklassen.
- **H145c (gewertet, „ist es eine Algebra ℝ?“):** Das von der Multiplikation der Träger induzierte Produkt auf der Linie, c ∘ c projiziert auf
  R⁰, ist **null** (Σ c_k³ = 0); die Linie ist also kein ℝ mit Einheit, sondern eine Linie ohne eigenes Produkt. Bestätigt, wenn
  |⟨c ∘ c, c⟩| < 10⁻¹² in allen Generationsklassen (alle Orientierungen mit n_gen ≥ 1).
- **H145d (gewertet, „ist der Rest abgeschlossen?“):** Der Rest K ist unter dem trägerweisen Produkt nicht abgeschlossen: Für zufällige x, y ∈ W ist
  der Anteil von x·y außerhalb K > 10⁻⁶ (relativ). Der Turm fängt im Rest also nicht als Algebra neu an.
- Was ohnehin feststeht (nicht gewertet): Die Koeffizienten verdoppeln sich nicht (1, 1, 2, 2, 3, 4 statt 1, 2, 4, 8).

## Folge, vorab festgelegt
- a, b bestätigt und c, d bestätigt: Der Rest ist kein HS(0) als Algebra. HS(0) steckt aber zweifach in ihm: als reelle, ladungsfreie,
  zeitumkehrfeste Koeffizientenlinie (Vielfachheit der Generation) und als der Raum D⁰ ⊗ e₀ der sich aufhebenden reellen Einheiten der Kopien.
  Die Leptonen (q = 0, 1) des Rests sind genau die Zustände, in denen beides zusammenfällt.
- c widerlegt (Produkt ≠ 0): Die Linie trägt ein eigenes ℝ-Produkt; dann mit neuer Vorab-Notiz prüfen, ob daraus ein Turm wächst.
- d widerlegt (abgeschlossen): Der Rest wäre eine eigene Algebra; dann ihre Stufe bestimmen.
- Masse: nicht berührt; die Lesart „keine Masse auf HS(0)“ wird nur eingeordnet. Vorzeichen offen; OP3, OP4 offen; kein Guard berührt.
- Werkzeuge: Python (numpy) für alle Fälle, Wolfram exakt für Zerlegung und Produkt einer Auswahl. Qiskit nicht eingesetzt.
- Vergeben: H145, k328.
