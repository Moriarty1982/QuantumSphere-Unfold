# Erkundung: Die vier versteckten Bedingungen an 6-Jets, ausdrücklich bestimmt

Stand: 3. November 2026. Erkundung ohne Vorab-Notiz, nach H55. Skripte `k144_vier_bedingungen.py` (Bestimmung) und
`k145_charakteristik.py` (Einordnung); die vier Bedingungen am Keim liegen in `k144_bedingungen_p1.npy` (Linearformen
auf (c₅, c₆) in ausgeglichenen Koordinaten b_α = c_α·√α!, als Vektoren in K₇). Betrifft nur das OP5-Vergleichsmodell.

## Bestimmung

Über dem festen reparierten 4-Jet: K₇ = Projektion des Kerns von F₇ auf (c₅, c₆), Dimension 852; K₈ dasselbe für F₈,
Dimension 848 (ohne volle SVD: Kern von (I − QQᵀ)E₅₆ mit Q = Bild von E₇₈). K₈ ⊂ K₇ (Rest 3e-6). Die vier Bedingungen
sind die Linearformen auf K₇, die auf K₈ verschwinden; eindeutig bis auf bekannte Bedingungen.

## Befunde

1. **Echte Gleichungen sechster Ordnung.** 99 % ihres Gewichts liegt auf c₆. Auf der Symbolfaser g'₆ (c₅ = 0 in K₇,
   Dimension 481) haben sie vollen Rang 4 (Singulärwerte 0,95; 0,60; 0,16; 0,09). Das vollständige Symbol bei Ordnung 6
   hat also 477 Dimensionen, nicht 481. Der Cartan-Test von H51 betraf ein unvollständiges Symbol.
2. **Sie wirken nur auf lichtartige Wellen.** Ebene Wellen ξ⁶ ⊗ u im Symbol gibt es nur auf der charakteristischen
   Menge. Generisch gibt es keine (Eichung). Auf dem Lichtkegel q(ξ) = 0 gibt es 7 Polarisationen je Richtung, und dort
   sind die Bedingungen nicht null. Abseits des Kegels (gefundene charakteristische Richtung) verschwinden sie (9e-15).
3. **Je Nullrichtung genau eine Polarisation.** Auf jeder lichtartigen Richtung haben die vier Bedingungen Rang 1 auf
   den 7 Polarisationen (nächster Singulärwert ≤ 3e-9 relativ, 16 Richtungen). Sie legen also je Nullrichtung eine
   skalare Kombination s(ξ, u) fest.
4. **Die Richtung im Bedingungsraum ist quadratisch in ξ, und zwar durch die beiden Ebenen bestimmt.**
   - Eine lineare Abhängigkeit n(ξ) ∝ Lξ passt nicht (Abweichungen 0,1–0,9).
   - n(ξ) ∝ M·(ξ ⊗ ξ) passt an 20 zurückgehaltenen Nullrichtungen auf ≤ 1,6e-9. M ist auf dem Kegel nur bis auf
     Vielfache von q bestimmt.
   - Die beiden Ebenen Π₀, Π₁ wurden unabhängig bestimmt (J(ξ) mit zweitem Kernvektor abseits des Kegels; 21 bzw.
     2 Fundpunkte, an Zufallskombinationen bestätigt ~1e-16). Die vier Quadriken l_a·m_b, die auf Π₀ ∪ Π₁ verschwinden,
     liegen im Raum span(M, q): Rang [M; q] = Rang [M; q; D] = 5 (Lücke 0,2 gegen 1,5e-13).

## Lesart

Auf dem Lichtkegel haben die vier Bedingungen die Form σ_k(ξ, u) = d_k(ξ)·s(ξ, u), bis auf eine feste
Umkombination. Dabei sind d_k die vier Quadriken der Ebenen Π₀, Π₁, und s ist eine einzige skalare Polarisationsform.
Das sind genau die Faktoren der vier Grad-7-Beziehungen q·d_k·Ω ∈ ⟨J⟩ aus r71.3. Die versteckten Bedingungen sind also
die Krümmung dieser vier Beziehungen: Auf Symbolebene sind sie Identitäten, die Terme niederer Ordnung lassen je eine
Bedingung sechster Ordnung übrig. Das passt zu H^{5,2}(g') = 4.

## Grenzen und offen

- Nur am ersten Grundpunkt bestimmt. Der Symbolteil hängt nur vom Jet bis Grad 3 ab und wäre am zweiten Punkt gleich;
  der c₅-Anteil nicht. Nicht nachgerechnet.
- Die Polarisationsform s ist nicht gedeutet.
- θ stammt vom älteren Keim (1e-7). Die Strukturaussagen (Rang 1, Quadriken) halten auf 1e-9 bis 1e-13.
- Nächster Schritt: die vier Bedingungen (fortgesetzt) ins Symbol aufnehmen und den Cartan-Test wiederholen; vorher als
  Test festschreiben.
