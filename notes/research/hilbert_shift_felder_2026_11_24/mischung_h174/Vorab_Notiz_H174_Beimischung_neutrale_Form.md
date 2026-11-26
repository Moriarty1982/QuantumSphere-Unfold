# Vorab-Notiz H174: Kleine Drehung der geladenen Leptonen aus einer Beimischung der neutralen Form

**Stand:** 26.11.2026, vor der Rechnung festgelegt. Anlass: Autor, 26.11.2026, „dann probieren wir erst ein kleine drehung“ (Kandidat d aus k369).
Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3 (Mischung). Vergeben: H174, k370 (geprüft: frei).
**Blind** sind b und c: Die Mischungswinkel dieser Konstruktionen sind nicht gerechnet. **Nicht blind** ist a (Umrechnung eines bekannten Ergebnisses).
Vor der Festlegung bekannt: die nötige Drehung aus k369 (0,044 bis 0,052) und die Größenabschätzung unten.

## Vorwissen geprüft
- **k369** (`../mischung_h173/k369/`): Eine e–μ-Drehung der geladenen Leptonen um 0,0516 (x) bzw. 0,0451 (x_R) mit freier Phase trifft θ₁₃ und θ₁₂ (χ² = 2,3 bzw. 2,4);
  kleinster Winkel für θ₁₃: 0,0440 bzw. 0,0365; √(m_e/m_μ) = 0,0695 passt nicht. Die Phase aus k369 hängt an der Phasenwahl der Eigenvektoren und ist so nicht verwendbar.
- **H173** (`../mischung_h173/`): Ein-Feld-Form N = {{a, b, c}, {b, a, −b}, {c, −b, a}} mit Brannen-Spektrum; am Baumwert δ_ν = π/6 exakt tribimaximal (b = 0).
- **k262** (`../setzungen_k262/`): Neutrinos auf dem Realteil s, geladene Leptonen auf z = s + iv in der ℤ₃-Basis von T. Die geladenen Leptonen sind zirkulant;
  eine zirkulante Matrix dreht für keine Phase.
- **H45/H134** (`../frame_h134/`): Die Maske exp(εW_l) ist der bisher einzige Term im Projekt, der ℤ₃ bei den geladenen Leptonen bricht. Mit ε = artanh β_sym
  widerlegt (H173c); ein freies ε ≈ 0,02 bis 0,03 würde passen (k369), hat aber keinen Platz im Rahmen.
- **H170** (`../delta_h170/`): Neutraler und geladener Term sind Real- und Imaginärteil einer holomorphen Form G = −(s + iv)²; jede reelle Mischung ist eine
  Phasenlage, 2F_χ − (s² + v²) = Re[e^{−2iχ}G]. **H171:** Am Baumpunkt hat ein Zweig den Eigenwert 0 (Oktant). **H168:** gemeinsamer Versatz x beider Sektoren, Herkunft offen.
- Suche nach „Beimischung“, „Gatto“, „ℤ₃ gebrochen“, „Drehung der geladenen Leptonen“ in `notes/`, `wiki/`, `analysis/`: kein Vorbefund zu dieser Konstruktion.

**Suchrichtung:** rückwärts. Ziel: e–μ-Drehung 0,044 bis 0,052. Notwendig: ein Term bei den geladenen Leptonen, der nicht zirkulant ist. Der einzige nicht
zirkulante Baustein, den der Aufbau ohne neue Größe schon enthält, ist die neutrale Form N selbst. Kandidat: Die Phasenlage des geladenen Terms ist nicht exakt
der Imaginärteil, sondern enthält einen kleinen Anteil des Realteils (H170c). **Werkzeugwahl:** Python (numpy, scipy) für die Rechnung, Wolfram für eine
unabhängige Nachrechnung der Hauptfälle. Qiskit nicht geeignet.

## Aufbau (k370, `k370_test_h174.py`; `k370b_kontrolle.wl`)
Platzbasis, T = {{0,0,1},{−1,0,0},{0,−1,0}}, A = {{0,0,−1},{0,1,0},{−1,0,0}} wie k262b. Feldebene (Eigenwerte λ ∝ √m; die Mischung hängt nur an den Eigenvektoren).
- Zirkulanter Teil: Ĉ(ρ, δ) = 𝟙 + (ρ/√2)(e^{iδ}T + e^{−iδ}T²), Eigenwerte 1 + √2ρ cos(δ + 2πk/3).
- Neutrale Form: N̂(δ_ν) mit Diagonale 1 und Brannen-Spektrum (ρ = 1) wie H173.
- **Hypothese:** M_e = a_e·(Ĉ + η·N̂), M_ν ∝ N̂. PMNS = U_e†U_ν, geladene Leptonen nach Masse geordnet, Neutrinos wie H173.
Daten: Polmassen m_e = 0,51099895, m_μ = 105,6583755, m_τ = 1776,93 MeV (± 0,09); sin²θ₁₃ = 0,02248 ± 0,00056, sin²θ₁₂ = 0,3036 ± 0,0064 (JUNO 2026),
sin²θ₂₃ = 0,470 (+0,017/−0,014). x = 0,0395773407, x_R = 0,043359.

## Hypothesen und Kriterien
- **H174a (nicht blind): nötiger Term, unabhängig von Phasenkonventionen.** Die beste Anpassung aus k369 wird in eine Störung δM der zirkulanten Matrix in der
  Platzbasis umgerechnet; berichtet werden Betrag und Phase des e–μ-Elements relativ zu λ_μ − λ_e und die Zerlegung von δM in zirkulanten und nicht zirkulanten
  Anteil. Kriterium: Rekonstruktion der Winkel aus δM auf 10⁻⁸.
- **H174b (blind): Beimischung mit festem η, Massen angepasst.** δ_ν = π/6 − x. η ∈ {± tan x, ± tan 2x} (Feldebene: Winkel x; Formebene: Winkel 2x, weil die
  quadratische Form den Winkel verdoppelt). a_e, ρ, δ werden so angepasst, dass die drei Massen exakt herauskommen (alle Lösungszweige, Start aus den sechs
  Lagen δ = ±δ* + 2πk/3), beide Vorzeichen von b. Kein freier Parameter für die Mischung. **Verträglich**, wenn es für ein η einen Zweig gibt mit sin²θ₁₃ und
  sin²θ₁₂ innerhalb 2σ und sin²θ₂₃ innerhalb 3σ; **widerlegt**, wenn kein Zweig sin²θ₁₃ innerhalb 3σ erreicht; sonst **nicht entschieden**. Berichtet werden alle
  Zweige (Anzahl für den Mehrfachvergleich), dazu ρ, δ des zirkulanten Teils und dieselbe Rechnung mit x_R als Kontrolle.
- **H174c (blind): Baumpunkt plus Beimischung.** Ĉ am Baumpunkt (ρ = 1, δ ∈ {±π/12 + 2πk/3}), N̂ am Baumpunkt (δ_ν = π/6, tribimaximal, b = 0). Am Baumpunkt ist
  m_e = 0 (H171). η wird allein aus m_e/m_μ bestimmt (beide Vorzeichen, alle Lösungen mit |η| < 0,5). Vorhergesagt sind dann m_τ/m_μ und alle Mischungsgrößen.
  **Trägt**, wenn ein Fall m_τ/m_μ auf 10⁻³ relativ trifft und die Winkel wie in b innerhalb 2σ/2σ/3σ liegen; **trägt teilweise**, wenn die Winkel so liegen, die
  Masse aber nicht, oder wenn nur θ₁₃ innerhalb 3σ liegt; **widerlegt**, wenn kein Fall sin²θ₁₃ innerhalb 3σ erreicht. Vorab bekannt: am Baumpunkt ist
  m_μ/m_τ = 0,0718 gegen gemessen 0,0595; die Beimischung müsste auch das verschieben.

**Größenabschätzung vor der Rechnung (bekannt):** Drehung ≈ η·|N̂_eμ|/(λ_μ − λ_e) mit λ_μ − λ_e ≈ 0,54 und |N̂_eμ| von der Ordnung 1; für η = tan 2x also grob 0,1,
für η = tan x grob 0,06. In c: m_e/m_τ verlangt η·N̂_ee ≈ 0,04, die Drehung ist dann grob 0,06·|N̂_eμ/N̂_ee|. Die Größenordnung kann also passen; ob Betrag und
Phase passen, ist offen. Erwartung: unbestimmt.

## Grenzen (vorab)
- Die Beimischung ist eine Setzung. H170c zeigt nur, dass reelle Mischungen der beiden Terme Phasenlagen einer Form sind; dass der Versatz x eine solche
  Beimischung auf Matrixebene ist, ist nicht hergeleitet. Die Wahl η ∈ {tan x, tan 2x} sind zwei Lesarten, vorab festgelegt; weitere werden nicht nachgeschoben.
- Die gleiche Normierung von Ĉ und N̂ (Diagonale 1) ist eine Setzung.
- Mehrfachvergleich: Anzahl der Zweige wird berichtet. Keine Maske (Materie-Frame) in dieser Runde; bei einem positiven Befund ist sie nachzuholen.
- OP3 und OP4 bleiben offen. Kein Vorzeichen wird gesetzt, alle Vorzeichen werden durchlaufen.
