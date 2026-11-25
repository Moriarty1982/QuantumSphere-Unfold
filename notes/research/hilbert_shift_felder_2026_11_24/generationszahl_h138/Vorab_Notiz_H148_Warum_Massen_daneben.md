# Vorab-Notiz H148: Warum liegen die Massenwerte aus H146 daneben?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Diagnose in der Gram-Auslesung (a) und die Koide-Formel der
Amplituden-Auslesung (c) folgen analytisch aus r13/k255 und H146; Messwerte bekannt. Gewertet: b, c, d. Anlass: Autor (25.11.2026, 20:50):
„prüfe doch mal, wieso die Werte danebenliegen?“ Vorgaben (über den Koordinator): Ursache eingrenzen (Auslesung, Kopienwahl, Frame-Boost,
freier Mischwinkel e₀/e₇ aus H147), Anpassung und Ableitung trennen, Vorzeichen nicht setzen.

## Vorwissen geprüft
- **H146:** Gram-Auslesung, K = (3 + 2Σ|a_ij|²)/9; Kopien-Überlappungen ¼, ⅝ (Leptonen), −½, ¼ (Farbe); max K = 19/32 bzw. ½ (alle 84 Tripel);
  Frame-Maske für geladene Leptonen Form S (keine Wirkung auf Eigenwerte).
- **r13 neu gelesen (k255, `../r13/README.md`):** Amplituden-Auslesung: orthonormale Kopienbasis g_k = 1/√3 + √(2/3)·w⊗f_k (magischer Winkel zur
  Eins); ein Zustand Ψ = α·1 + β·w⊗n(δ) hat Amplituden c_k = (α + √2β cos(δ − 2πk/3))/√3, K = (α² + β²)/(3α²); K = ⅔ genau bei β = α, also
  Ψ = exp(uπ/4) (Achteldrehung von der Eins weg, Oktant-Phase π/4, H123). δ nur in 120°-Schritten durch die Symmetrie erlaubt, Koide-δ ≈ 2/9 nicht
  hergeleitet.
- **H147:** zwei Skalare im Rest, e₀ (reelle Einheit, HS(0)) und e₇ (Ladungsachse); Mischwinkel θ unter der Ladungsdrehung frei.
- **H138:** Im z³ = 0 erzwingt die 120°-Lage der drei Kopien.

## Hypothesen und Kriterien
- **H148a (nicht blind):** In der Gram-Auslesung braucht K = ⅔ die mittlere Überlappung² ½ (Kopien im Überlappungsabstand π/4); die 120°-Lage
  aus Im z³ = 0 gibt ¼ (Farbe) bzw. 1/16 (Leptonen, Sedenion-Tripel). Weder Kopienwahl (erschöpfend, H146) noch Frame-Boost (Form S) ändern das.
  Nachrechnung der Zahlen genügt.
- **H148b (gewertet, Gram-Auslesung mit Mischwinkel):** Mit dem Generationszustand cos θ·e₀ + sin θ·e₇ je Sedenion-Kopie gibt es genau einen Winkel
  θ* in (0, π/2) mit K = ⅔, sin²θ* = ⅔(1 − 1/√2), θ* ≈ 26,2°. Dort sind zwei Massen gleich (reelle Überlappungen, Brannen-Phase 0), also keine
  Hierarchie. Und θ* stimmt mit keiner Projektgröße überein (β_sym, artanh β_sym, π/4, π/12, halber magischer Winkel, arcsin(1/√3), Hopf-Winkel;
  Toleranz 10⁻³). Bestätigt, wenn alle drei Aussagen gelten.
- **H148c (gewertet, Amplituden-Auslesung):** Mit Ψ_θ = cos θ·1 + sin θ·w⊗n(δ) in der Basis g_k gilt K = 1/(3cos²θ) unabhängig von δ, also K = ⅔
  genau bei θ = π/4, dem im Projekt schon ausgezeichneten Winkel (exp(uπ/4), Oktant). Die Massenverhältnisse hängen dann nur noch an δ; δ = 2/9
  (eingesetzt, Brannen) gibt m_μ/m_e und m_τ/m_μ innerhalb 1 %. Bestätigt, wenn K(π/4) = ⅔ exakt und die Verhältnisse bei δ = 2/9 innerhalb 1 %.
- **H148d (gewertet):** Der komplexe Ladungseigenzustand (e₀ + i e₇)/√2 (gleich schwer, aber mit i) gibt in der Amplituden-Auslesung **nicht**
  K = ⅔ (für kein δ auf einem 1°-Raster, |K − ⅔| > 10⁻³). Der Koide-Zustand ist also der reelle, zeitumkehrfeste Mischzustand.

## Folge, vorab festgelegt
- Alle bestätigt: Die Werte liegen daneben, weil die Gram-Auslesung feste Kopienzustände mit der 120°-Überlappung vergleicht. Koide verlangt
  dagegen einen Zustand, der die reelle Einheit (HS(0)) und die imaginäre Kopienrichtung gleich stark mischt: den freien Mischwinkel aus H147 bei
  π/4. Herleitung: K = ⅔ bei θ = π/4 (Amplituden-Auslesung). Anpassung: δ = 2/9 und die Skala. Ungeklärt: warum θ = π/4 (Potential bzw.
  Feldgleichung) und woher δ.
- Was nicht folgt: δ, Skala, Quarkmassen. OP3 offen; Vorzeichen offen; kein Guard berührt.
- Werkzeuge: Python (numpy), Wolfram exakt für θ* und K(θ). Qiskit nicht eingesetzt. Vergeben: H148, k331.
