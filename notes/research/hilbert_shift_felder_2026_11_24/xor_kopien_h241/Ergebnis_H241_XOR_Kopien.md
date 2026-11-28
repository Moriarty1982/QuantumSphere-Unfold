# Ergebnis H241 (k457): Klartext-Block und Kopien; die Kopien als XOR

**Datum:** 2026-11-28. **Vorab:** `Vorab_H241_XOR_Kopien.md`, Commit e8d4fe3, vor der Rechnung. **Rechnung:** `k457_test_h241.py` → `k457_out.txt`;
Gegenprobe `k457b_gegenprobe.wl` → `k457b_out.txt` (symbolisch/exakt); Nachtrag `k457c_kreuzprodukt.py` → `k457c_out.txt`.

**Frage 1 (Block in Kopie): nein, er schneidet jede Kopie in einem Quaternion-Teil (dim 4).**
**Frage 2 (XOR): trägt, nicht blind.** Die drei Kopien bilden eine exakte Parität. Nachträglich zeigt sich mehr: Das Produkt zweier Kopien landet in der
dritten, nach dem Gesetz k₁ + k₂ + k₃ ≡ 0 (mod 3).

## Teil A: Lage des Klartext-Blocks B_x = ℍ_x ⊕ ℍ_x·e₈
- Für alle 84 Basis- und 200 allgemeinen Nullteiler gilt dim(B_x ∩ V_k) = 4 für k = 1, 2, 3 (Wolfram exakt). B_x liegt in keiner Kopie, denn er enthält e₈.
- B_x ist eine Oktonion-Algebra: abgeschlossen, alternativ, normmultiplikativ. Sie enthält x und e₈. In ihr ist x invertierbar, in 𝕊 ein Nullteiler.
- **A-blind:** Für die Basis-Nullteiler ist B_x jedesmal eine der 7 Basis-Oktonionen, die e₈ enthalten. Das sind die 7 Oktonionen außer der inneren
  (H237: 8 Oktonionen = innere 𝕆 + 7 mit e₈; 7 Quasi-Oktonionen).
- Lesart: Der ungeschützte Block eines Nullteilers ist eine eigene Oktonion-Algebra quer zu den Kopien. Er enthält aus jeder Kopie genau einen
  Quaternion-Teil span{1} ⊕ u_k(Im ℍ_x) und dazu e₈.

## Teil B: XOR
- **B1 (nicht blind):** e_i e_j = ±e_{i⊕j} für alle 256 Paare. Die Multiplikation der Basis ist ein Index-XOR mit Vorzeichen.
- **B2:** Die 15 achtdimensionalen Basis-Unteralgebren bilden 35 Büschel aus je dreien. In jedem gilt H₁ Δ H₂ = Komplement von H₃, also eine Paritätsrelation
  über 𝔽₂ (nicht blind). **Blind:** Typenkombinationen 7 × (O, O, O), 7 × (O, O, Q), 21 × (O, Q, Q). Die 7 reinen Oktonion-Büschel sind die 7 Geraden einer Fano-Ebene auf den 7 Oktonionen mit e₈; die innere 𝕆 liegt in keinem von ihnen (ihre Büschel sind die 7 × (O, O, Q)).
- **B3 (nicht blind):** u₁(q) + u₂(q) + u₃(q) = 0 für jedes q, exakt (v₁ + v₂ + v₃ = 0). Zufallskontrolle: 0 von 10 000 zufälligen Winkel-Tripeln.
  Jede Kopie ist also die negative Summe der beiden anderen, wie eine RAID5-Parität über ℝ. Weil v und −v dieselbe Kopie geben, spielt das Vorzeichen
  keine Rolle, wie in Charakteristik 2.
- **B4 (blind):** q ↦ u_k(q) ist für jede Kopie ein Isomorphismus von 𝕆 (u_k(p)u_k(q) = −p·q + u_k(p × q), Abweichung 2·10⁻¹⁶). Die Parität gilt auch im
  Block: B_x ∩ V₃ ⊂ (B_x ∩ V₁) + (B_x ∩ V₂) für alle 200 Nullteiler. Damit ist das Kriterium „trägt“ erfüllt.

## Nachträglich (k457c, symbolisch bewiesen in k457b): die Produktregel auf dem Kreis
Für Richtungen u_α(p) = (cos α·p, sin α·p) gilt exakt:

u_α(p)·u_β(q) = −(p·q)·[cos(β−α) + sin(β−α)·e₈] + u_{−(α+β)}(p × q).

- Für die Kopien (α, β ∈ {0°, 120°, 240°}) ist −(α + β) wieder eine Kopie: für zwei verschiedene die dritte, für gleiche dieselbe. Das Produkt der Kopien
  folgt also dem Gesetz k₁ + k₂ + k₃ ≡ 0 (mod 3), so wie die Basis dem Gesetz i ⊕ j ⊕ k = 0 in (ℤ₂)⁴ folgt. Marcs „XOR der anderen“ ist damit
  ein ℤ₃-XOR.
- Tabelle: V₁V₁ → V₁, V₁V₂ → V₃, V₁V₃ → V₂, V₂V₂ → V₂, V₂V₃ → V₁, V₃V₃ → V₃. Die Skalarteile landen in span{1, e₈}; für verschiedene Kopien gibt
  es einen e₈-Anteil −(p·q)·sin(±120°).
- **Folge für H238:** Die Formel erklärt die Leck-Energie. Ein Produkt im Raum U_θ landet in U_{−2θ}. Der Anteil außerhalb ist sin²3θ, und es gibt
  42 = 7·6 geordnete Paare verschiedener Einheiten. Also folgt L(θ) = 42·sin²3θ jetzt analytisch, und die Zahl 42 ist erklärt.

## Hergeleitet, gesetzt, offen
- **Hergeleitet:** die Produktregel (symbolisch), daraus die ℤ₃-Parität der Kopien, die Isomorphie der Kopien, die Lage von B_x (Schnitt 4, eine Oktonion-Algebra
  mit e₈) und H238 analytisch.
- **Gesetzt:** die Lesart „XOR“ für lineare Parität (B3) und für das Produktgesetz; die Übersetzung in RAID-Begriffe aus H239/H240.
- **Nicht blind:** B1, B3 und die Büschelrelation in B2 standen vorab fest. B4 war vorab als blind geführt, folgt aber, wie sich beim Rechnen zeigte,
  aus derselben Produktregel.
- **Offen:** ob das ℤ₃-Gesetz der Kopien physikalisch etwas bedeutet. Es hätte die Form einer Generationenregel, das ist aber nicht gezeigt. Offen bleibt
  auch, welche Rolle der e₈-Anteil beim Produkt verschiedener Kopien spielt.

## Werkzeuge und Grenzen
Python (Stichproben, Basis-Unteralgebren, Zufallskontrolle) und Wolfram (symbolischer Beweis der Produktregel, exakte Schnitte). Qiskit nicht einschlägig.
