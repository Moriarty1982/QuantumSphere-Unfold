# Vorab H241 (k457): Liegt der Klartext-Block eines Nullteilers in einer Kopie? Ist eine Kopie das XOR der anderen?

**Datum:** 2026-11-28, vor der Rechnung committet. **Anlass:** Marc (20:14): „ja bitte, es könnte nämlich auch eine art xor der anderen sein“. Das
schließt an H240 an.

## Vorwissen geprüft
- **H240/k456:** Für einen Nullteiler x = (a, b) ist L_x blockdiagonal und auf B_x = ℍ_x ⊕ ℍ_x·e₈ invertierbar, mit ℍ_x = span{1, a, b, ab}.
- **H138/H237/H238:** Die drei G₂-Kopien V_k = span{1} ⊕ {(v₀q, v₁q) : q ∈ Im 𝕆} haben v_k = (1, 0) und (−½, ±√3/2). Die Basis-Unteralgebren der
  Dimension 8 sind 15 (8 Oktonionen, 7 Quasi-Oktonionen), die der Dimension 4 sind 35.
- **Standard (nicht nachgeprüft):** In Cayley–Dickson-Algebren gilt e_i e_j = ± e_{i⊕j} (Index-XOR).

## Rechnung vorab (nicht blind)
- (B_x ∩ V_k): Elemente c + (v₀q, v₁q) mit q ∈ Im ℍ_x. Erwartet ist dim 4, ein Quaternion-Teil der Kopie, für jedes k. B_x enthält e₈, keine Kopie tut das,
  also liegt B_x in keiner Kopie.
- B_x ist unter dem Produkt abgeschlossen und ist die Cayley–Dickson-Verdopplung von ℍ_x. Erwartet wird deshalb eine Oktonion-Algebra.
- v₁ + v₂ + v₃ = 0, also gilt für jedes q: u₁(q) + u₂(q) + u₃(q) = 0 mit u_k(q) = (v_k,₀ q, v_k,₁ q). Die Imaginärteile jeder Kopie sind die negative
  Summe der beiden anderen, wie bei einer RAID5-Parität über ℝ. Weil v ↦ −v dieselbe Kopie gibt, spielt das Vorzeichen keine Rolle (wie in Charakteristik 2).
- Für Basis-Unteralgebren (Indexmengen sind Untergruppen von (ℤ₂)⁴): Drei Hyperebenen eines Büschels (gemeinsame 4er-Untergruppe) erfüllen
  1_{H₁} + 1_{H₂} + 1_{H₃} = 1 (mod 2). Also H₁ Δ H₂ = Komplement von H₃, und jede ist durch die beiden anderen bestimmt.

## Teil A: Lage des Klartext-Blocks
Für Z1 (84 Basis-Nullteiler) und Z2 (200 allgemeine, wie H239/H240):
- dim(B_x ∩ V_k) für k = 1, 2, 3.
- Liegt B_x in einer Kopie oder ist er gleich einer? (Erwartet: nein, nicht blind.)
- Ist B_x eine Unteralgebra, alternativ und normmultiplikativ (also oktonionisch)? (Nicht blind.)
- **A-blind:** Für Z1: Welche der 15 Basis-Unteralgebren ist B_x, und welcher Typ nach H237 (Oktonion oder Quasi-Oktonion)?

## Teil B: XOR
- **B1 (nicht blind):** e_i e_j = ± e_{i⊕j} für alle 256 Paare.
- **B2:** Die 35 Büschel aus je drei 8-dim. Basis-Unteralgebren. Die XOR-Relation selbst ist nicht blind. **Blind:** welche Typenkombinationen (Oktonion,
  Quasi-Oktonion) in den Büscheln vorkommen und ob ein Büschel aus drei Oktonionen besteht.
- **B3 (nicht blind):** u₁ + u₂ + u₃ = 0 für die drei G₂-Kopien. **Zufallskontrolle:** 10 000 zufällige Winkel-Tripel; der Anteil, für den es Vorzeichen
  mit |±v₁ ± v₂ ± v₃| < 10⁻⁶ gibt.
- **B4 (blind):** Ist die XOR-Relation mit dem Produkt verträglich? Geprüft wird, ob die Abbildung u₁(q) ↦ u₂(q) die Multiplikation trägt, also
  u₁(p)u₁(q) ↦ u₂(p)u₂(q) bis auf den Realteil. Ebenso, ob die Parität im Block B_x gilt: B_x ∩ V₃ ⊂ (B_x ∩ V₁) + (B_x ∩ V₂).

## Urteil
- **Frage 1 (Block in Kopie):** „liegt in Kopie“, wenn B_x ⊂ V_k für ein k bei allen Nullteilern. Sonst „schneidet“ (mit Dimension).
- **Frage 2 (XOR):** trägt, wenn B3 exakt gilt, die Zufallskontrolle es nicht reproduziert (Anteil < 10⁻³) und B4 für die Parität im Block gilt. Teilweise
  trägt sie, wenn nur die lineare Relation gilt, ohne Verträglichkeit mit dem Produkt (B4 verfehlt). Widerlegt ist sie, wenn B3 nicht gilt.
- Weil B3 und die Büschel-Relation vorab feststehen, wird ein „trägt“ ausdrücklich als nicht blind geführt.

## Werkzeuge
Python k457, Wolfram k457b (exakt: B_x ∩ V_k, Oktonion-Eigenschaft von B_x, u₁ + u₂ + u₃ = 0). Qiskit nicht einschlägig.
