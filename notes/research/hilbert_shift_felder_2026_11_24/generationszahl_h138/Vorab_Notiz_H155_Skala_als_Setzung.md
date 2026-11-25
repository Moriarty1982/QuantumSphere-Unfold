# Vorab-Notiz H155: Macht eine gesetzte Skala U′ schwer und legt sie K = ⅔ und δ fest?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „dann probiere die skala“ (nach H154). Damit ist für diesen Zweig die Richtung entschieden: Skala als Setzung.
Fragen: (1) Macht eine Skala die zweite Ebenenrichtung U′ schwer, sodass effektiv nur {1, U} läuft und K = ⅔ startunabhängig wird? (2) Bewegt der jetzt erlaubte Term
sechster Ordnung δ von 0 bzw. π/3 weg zu 2/9? Skalen nur aus Bekanntem, keine neue anpassen; Fit und Herleitung getrennt; Vorzeichen nicht gesetzt (beide gerechnet).
Vergeben: H155, Skripte k338 (Python) und k338b (Wolfram). Qiskit nicht vorgesehen. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H150b (k333): mit Skala ist Koide Minimum für −2λ < κ < 2λ; bei 1 gegen 2 Komponenten wandert θ über die Massenterme (cos 2θ = c_L/f²).
- H149c/d: tauschsymmetrisches Potential ist bei π/4 stationär; δ sieht nur die kubische Norm N(W) = c₀c₁c₂ über cos 3δ; auf θ = π/4 ist
  N = v³(2 cos 3δ − √2)/(24√3); V = αN + βN² braucht α/β ≈ −0,00758 für δ = 2/9 (H149e, dort Anpassung genannt).
- H152: skalenfrei nur φC₃; δ ∈ {0, π/3}. H153/H154: K = ⅔ exakt nur mit Schleife über {1, U}; n_B = 1 nicht erzwungen; Messwert K = 0,6666645 ± 0,0000051.
- k300: bekannte Skalen dieses Fadens: 9,78 GeV (Schleifen-Skala aus W, Z), v = 246,22 GeV, 382 GeV (vier Zusatzbosonen); dazu m_τ, m_Z, m_h; Lepton-Skala Σm_ℓ = 1,8835 GeV.
- Zurückgestellte Idee I4 (Tachyon-Kondensation als Massenquelle) betrifft das Vorzeichen von μ²; hier nicht gesetzt, beide Vorzeichen gerechnet.

## Ansatz
Mit Skala sind alle Z₃ ⋊ Z₂-invarianten Terme bis Grad 4 zulässig, dazu Grad 6 mit 1/Λ². In den Invarianten der Auslesung W (c_k): Tr W = √3 φ, Tr W² = φ² + |y|², N(W).
V = μ_A²A + μ_B²B + λ_A A² + κAB + λ_B B² + ζ·N(W) + N(W)²/Λ²  (A = φ², B = |y|²; ζ Massendimension 1).

## Hypothesen und Kriterien
- **H155a (nicht blind, analytisch):** Baumgraph mit Skala, tauschsymmetrisch (μ_A² = μ_B² = μ² < 0, λ_A = λ_B, −2λ < κ < 2λ), ζ = 0: Minimum exakt bei θ = π/4,
  K = ⅔ für alle solchen Werte; U′ ist dort Goldstone (m = 0). Für μ² > 0 kein Kondensat. *Kriterium:* symbolisch.
- **H155b (gewertet):** U′ schwer machen mit dem einzigen algebraischen Term, der die Ebenen-Drehung bricht, ζN(W). Gitter λ = 0,2, κ/λ ∈ {−1; 1} (κ = ±0,2), μ² = −1,
  ζ ∈ {±0,001; ±0,01; ±0,1; ±0,3}. Gemessen: m²_U′/|μ²| und ΔK = K − ⅔ am Minimum. *Kriterium:* „Skala macht U′ schwer ohne K zu verschieben“, wenn ein Punkt
  m²_U′ ≥ |μ²| und |ΔK| < 1,5·10⁻⁵ hat. Vorhersage: kein Punkt; N(W) ist nicht tauschsymmetrisch, m²_U′ und ΔK wachsen beide linear in ζ.
- **H155c (gewertet):** Entkopplung im Fluss. Start symmetrisch bei Λ (μ² = −1, λ, κ), Lauf mit n_B = 2 (Massen und Quartiken) über das Fenster L = ln(Λ/M_U′), darunter
  n_B = 1; K am Baumgraph-Minimum. Fenster aus bekannten Skalen: ln(382/246,22), ln(246,22/91,19), ln(91,19/9,78), ln(246,22/9,78); λ ∈ {0,05; 0,1; 0,2},
  κ/λ ∈ {−1; −0,5; 0,5; 1}. *Kriterium:* |ΔK| < 1,5·10⁻⁵. Vorhersage: für jedes Fenster > 0 verfehlt; K = ⅔ nur, wenn der symmetrische Start genau bei der Masse von U′
  liegt (Fenster 0). Dazu das größte zulässige Fenster L_max(λ, κ).
- **H155d (gewertet):** δ mit Term sechster Ordnung. Auf θ = π/4: Minimum von ζN + N²/Λ² bei cos 3δ = (√2 − 12√3 R)/2 mit R = ζΛ²/v³; innere Minima (drei verschiedene
  Massen) für |cos 3δ| < 1. δ = 2/9 verlangt genau R* = (√2 − 2 cos(2/3))/(12√3) (Vorhersage ≈ −0,00758, wie H149e). *Kriterium:* Für ζ, Λ aus der Liste bekannter Skalen
  {Σm_ℓ, m_τ, 9,78, m_Z, m_h, v, 382} (beide Vorzeichen von ζ) und v ∈ {246,22; Σm_ℓ}: Anzahl der R innerhalb 1 % von R*; Zufallserwartung aus der log-Verteilung.
  Vorhersage: kein Treffer über der Zufallserwartung; δ = 2/9 bleibt ein Fit mit genau einem Parameter.

## Grenzen
- Eine Schleife; Massen- und Quartik-β aus ½Tr(∂²V)² (MS-artig, ohne Schwellenkorrekturen). Die Entkopplung ist scharf am Fensterende.
- Die Normierung von N(W) folgt r13/k255; R hängt an ihr, die Aussage „ein Parameter“ nicht.
- OP3 offen; Vorzeichen von μ², ζ, κ nicht gesetzt; kein Guard wird berührt.
