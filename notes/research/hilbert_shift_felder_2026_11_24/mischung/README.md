# Sagt die Kopiengeometrie eine Mischungsmatrix voraus? (Erkundung k256, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Ein blinder Test ist so nicht möglich. Mit der S₃ der Kopien als Restsymmetrie stehen alle
Mischungsmuster schon vor der Rechnung fest: keine Mischung, trimaximal (H39a, widerlegt), θ₁₃ = 0 (ausgeschlossen) oder TM1/TM2, je nachdem,
welches Z₂ man nimmt. Neu ist nur ein **Wörterbuch**: Die TM2-Spalte ist die reelle Eins, die TM1-Spalte ist die imaginäre Achse einer Kopie.
TM1 hält genau die Verknüpfung „Oktonion-Konjugation ∘ Kopienspiegelung“ fest. Das deckt sich mit H8 (Cayley–Dickson-Involution als CP, TM1,
θ₂₃ maximal, δ_CP = 270°) und sagt nichts darüber hinaus. H126 ist für den Folgetest mit dem Winkel χ vorgesehen (Vorab-Notiz zur Freigabe beim Autor).

Auftrag des Autors (24.11.2026, „mach das“): blinden Test entwerfen, ob die Mischgeometrie der Kopien eine Mischungsmatrix vorhersagt, die nicht
schon aus Koide folgt. Bei der Vorbereitung der Vorab-Notiz zeigte die Rückwärtssuche, dass das Ergebnis jeder naheliegenden Konstruktion
analytisch feststeht. Nach der Regel „nicht blind = offen sagen“ steht das hier als Erkundung. Skript **k256**.

Werkzeuge: Python (numpy), lineare Algebra auf dem dreidimensionalen Raum V_w. Wolfram ist nicht nötig: Alle Größen sind exakte Brüche
(1/3, 1/2, 2/3), die die Ausgabe auf 10⁻⁶ zeigt. Qiskit ist nicht eingesetzt.

## Vorwissen geprüft
H4 (TM1 gegen TM2: TM1 stark bevorzugt, TM2 χ² = 14,7), H5 (Hopf-Winkel; Spalte ν₁ gibt δ_CP ≈ 262°), H8 (Cayley–Dickson-Involution →
μ-τ-Spiegelung, θ₂₃ maximal, δ_CP = 270°, in Spannung), H10 (Assoziator), H34 (Maske erklärt weder CKM noch PMNS), H37 (Trialität),
H39 (A₄-Untergruppen: Klein → alle 1/3, ℤ₂ → TM2), k255 (Kopienbasis g_k, Koide aus exp(uπ/4)), H125-Entwurf (det ∓1).

## Ergebnisse (k256)
Flavourbasis der geladenen Leptonen = Kopienbasis g_k. Das ist die Lesart aus k255, in der die Koide-Amplituden c_k diagonal sind.
1. **Beide Sektoren mit ℤ₃ (zirkulant):** U = 𝟙. Das ist die bekannte Eigenschaft zirkulanter Matrizen: Die Eigenbasis ist immer die diskrete
   Fourier-Transformation (DFT).
2. **Leptonen in Kopienbasis, Neutrinos mit ℤ₃:** alle |U_ij|² = 1/3 (trimaximal), widerlegt wie H39a.
3. **Leptonen mit ℤ₃, Neutrinos mit S₃-Spiegelung:** Die erhaltene Spalte hat |U_ei|² = (0, ½, ½), für jeden freien Winkel. Daraus folgt θ₁₃ = 0,
   und das ist ausgeschlossen.
4. **Wörterbuch (Flavour = Kopienbasis):** (1,1,1)/√3 (TM2-Spalte) = reelle Eins; (2,−1,−1)/√6 (TM1-Spalte) = imaginäre Achse w⊗f₀ der Kopie 0;
   (0,1,−1)/√2 = Richtung senkrecht dazu in der Kopienebene.
5. **Welche ℤ₂ welche Spalte erhält:** Die Spiegelung S₀ hält Kopie 0 ganz fest, ihr −1-Raum ist (0,1,−1)/√2 (μ-τ-artig). Die Konjugation x ↦ x*
   hat einen zweidimensionalen −1-Raum. **K∘S₀ hält genau die TM1-Spalte** (−1-Raum eindimensional, = (2,−1,−1)/√6). K ist eine
   Anti-Automorphie und passt zu Majorana-Neutrinos (Teilchen = Antiteilchen). Als CP-artige Restsymmetrie gelesen, gibt das TM1 mit θ₂₃
   maximal und δ_CP = ±90°, also genau H8.

## Bewertung
- Die Kopiengeometrie sagt **keine Mischungsmatrix jenseits bekannter Muster** voraus: Ihre S₃ erzeugt mit zirkulanten oder ℤ₂-Lesarten nur
  𝟙, trimaximal, θ₁₃ = 0, TM2 oder TM1. Das ist bekanntes Terrain (H4, H8, H39).
- Gewonnen ist eine geometrische Lesart der Datenlage: Die Daten bevorzugen die Spalte, die die **imaginäre Kopienachse** erhält (TM1), nicht
  die reelle Eins (TM2). Neutrinos würden dann K∘S₀ achten, also Konjugation mal Kopienspiegelung.
- Ein blinder Test bräuchte eine neue Zutat, die mehr als die Restsymmetrie festlegt, etwa eine Größe, die θ₁₃ oder den Koide-Winkel δ
  bestimmt. Kandidaten: die nicht-assoziative Kopplung zwischen zwei verschiedenen Oktonion-Richtungen w_e ≠ w_ν. Innerhalb eines V_w ist alles
  quaternionisch, also assoziativ, und gibt nichts Neues. Ihr Winkel χ wäre die einzige G₂-invariante Größe. Das wäre eine neue Setzung und
  braucht die Entscheidung des Autors.
- OP3/OP4 offen; kein Guard berührt; H8, H125 unberührt. Folgetest H126 (Winkel χ) nur mit Vorab-Notiz.

## Dateien
`k256_restsymmetrie_mischung.py` (`k256_out.txt`).
