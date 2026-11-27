# Vorab-Notiz H189: Erreichen die Ableitungsterme die Quarkmassen über ein bewegtes Vakuum?

**Stand:** 27.11.2026, vor der Rechnung. Anlass: Autor, 27.11.2026, Entscheidungskarte nach H188: „Bewegtes Vakuum rechnen“. Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H189, k392 (geprüft: frei).

## Vorwissen geprüft
- k253 (`../README.md`): Grundbahn ψ(t) = exp(uωt)ψ₀ mit einer imaginären Einheit u; bis 𝕆 für jedes u geschlossen.
- k290 (`../feldgleichung/README.md`): K₁ Fläche, K₂ Kommutator, K₃ Assoziator (drei Richtungen), K₄ Normdefekt, alle aus X_μ = D_μψ.
- H188 (`../ableitungsterme_h188/`): um ein ruhendes Vakuum beginnen K₁ bis K₄ bei ε⁴. Ordnungsabzählung: mit X_t = B₀ ≠ 0 tragen K₁, K₂, K₄ in
  ε² bei; der Koeffizient von K₁ ist N(B₀)N(∂_xδW) − ⟨B₀, ∂_xδW⟩². Funktionsmenge R (neun Funktionen je Paar) und Vergleichsverfahren von dort.
- H184 bis H187: Frequenzquadrate der Farbschwingungen aus dem Potential (Funktionen aus R, Koeffizienten frei).
- Nicht gefunden: Schwingungen um eine drehende Lösung auf H₃(𝕆), Ausbreitungsgeschwindigkeit je Mode.

## Suchrichtung (rückwärts)
Ziel: träge Masse je Generation und Ladung. Für eine Mode mit Ω² = Ω₀² + c²k² ist die träge Masse m = Ω₀/c² (in Einheiten ħ = 1). Die
Ableitungsterme können also an zwei Stellen wirken: an der Ruhefrequenz Ω₀ (k = 0) oder an c² (Koeffizient des Gradienten). Beides wird getrennt
geprüft, zuerst ohne Daten.

## Setzungen dieser Notiz
- Feld, Vakuumwert W₀ (reelle Zirkulante, K = ⅔, δ = 2/9, Eingabe), Farbe, P, Farbphase wie H185 bis H188.
- **Bewegung des Vakuums:** W(t) = exp(uωt)W₀, räumlich homogen. Variante 1: u = i (Phase des komplexen Felds; verlangt, dass das Potential die
  Phase nicht sieht). Variante 2: u = U auf den Nebendiagonal-Einträgen (δ läuft; nur als Hintergrund gesetzt, keine Lösung behauptet).
- K₂ und K₄ mit dem Matrixprodukt über ℂ ⊗ 𝕆 (komplex-bilinear) und der hermiteschen Norm N(X) = Σ|X_ij|²; K₃ wie k290 mit drei Richtungen.
- Drehrate ω und Koeffizienten c₁, c₂, c₄ frei, für beide Sektoren gleich (es sind Größen der Feldgleichung, nicht der Sektoren).
- Zuordnungen A, B wie H187. Daten bei M_Z aus k376.

## Hypothesen und Kriterien
- **H189a (nicht blind):** Bei rein zeitlich bewegtem, homogenem Vakuum ändern K₁ bis K₄ die Ruhefrequenzen (k = 0) nicht: Für ∂_xδW = 0
  verschwinden K₁, K₂, K₄ identisch, K₃ ist in zweiter Ordnung null. Kriterium: exakt null: **bestätigt**; sonst **widerlegt**.
- **H189b (nicht blind, Überschlag vor der Notiz gemacht):** Der gewöhnliche kinetische Term gibt um das drehende Vakuum (Variante 1) die
  Ruhefrequenzen √(h + ω²) ± ω, für alle Generationen und beide Ladungen mit demselben ω. Das trennt Up und Down nicht und gibt je Generation
  dieselbe Aufspaltung 2ω; die Daten haben keine konstante Differenz (Überschlag: m_u − m_d = −8·10⁻⁶, 3·10⁻³, 0,95). Kriterium: Aufspaltung
  im Skript unabhängig von Generation und Ladung (Abweichung < 10⁻⁸): **bestätigt**, dass die Drehung allein die Massen nicht gibt.
- **H189c (ohne Daten, Ausgang offen):** Die Gradientenformen, die K₁, K₂, K₄ in zweiter Ordnung liefern (g₁, g₂, g₄ je Variante), sind auf den
  Farbrichtungen diagonal in den Moden der Generationen und Funktionen des Paars aus dem Raum der sieben Grundfunktionen (1, l_i + l_j, l_k,
  l_i² + l_j², l_i l_j, l_k(l_i + l_j), l_k²), geprüft an vier Vakua. Kriterium: Rest < 10⁻⁸ und Eigenrest < 10⁻⁸ für alle: **bestätigt**;
  sonst **widerlegt** (dann ist H189d für die betroffene Form nicht prüfbar und wird so berichtet).
- **H189d (Ausgang offen):** Träge Masse m_g = A·√f_g / (1 + κ₂·g₂ + κ₄·g₄) je Sektor, mit f ∈ R je Sektor frei gewählt, A je Sektor frei,
  κ₂ und κ₄ **für beide Sektoren gleich** (g₁ ist auf Farbrichtungen konstant, falls H189c gilt, und geht in A auf; sonst kommt κ₁·g₁ dazu).
  Geprüft werden: nur κ₂ (drei Vorhersagen), nur κ₄ (drei), beide (zwei). Verlangt: Nenner positiv für alle drei Paare; alle vier
  Massenverhältnisse (m₁/m₃, m₂/m₃ für Up und Down) innerhalb von 3σ beim besten κ. Zweite Lesart zur Kontrolle: m_g = A·f_g/(…). Je Variante
  1 und 2, Zuordnung A und B. Zufallskontrolle mit 2000 erfundenen Datensätzen wie H188. Kriterium: Treffer und Zufallsquote < 5 %:
  **bestätigt** (als Kandidat für einen eigenen Vorab-Test); Treffer bei Quote ≥ 5 %: **ohne Urteil**; kein Treffer: **widerlegt**.
- **Bericht:** Funktionen g je Variante, bester Abstand je Fall, Zahl der Vergleiche, Zufallsquoten.

## Werkzeugwahl
Python (numpy, scipy): quadratische Formen exakt durch Polarisation auf den 36 Farbrichtungen, Moden wie k390, Anpassung von κ numerisch.
Wolfram Language: H189a symbolisch, H189b (Ruhefrequenzen) exakt, Stichprobe zu H189c im reduzierten Modell. Qiskit nicht geeignet.

## Grenzen (vorab)
Keine vollständige Lösung der Feldgleichung: ob das drehende Vakuum bei gegebenem Potential existiert und stabil ist, wird nicht geprüft; die
Verschiebung der Ruhefrequenz durch die Drehung (H189b) wird in H189d nicht mitgeführt. Räumlich verdrehte Vakua (∂_xW₀ ≠ 0) und Drehungen in
den Generationen (SU(3) ⊂ F₄) sind nicht gerechnet. Massen bei M_Z ohne Laufen. Kein Vorzeichen gesetzt. OP3, OP4 bleiben offen.
