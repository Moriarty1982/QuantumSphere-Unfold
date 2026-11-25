# Vorab-Notiz H146: Massen aus der Kopien-Struktur (Gram-Auslesung)

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Messwerte sind bekannt, und H146a, b folgen analytisch
(Begründung unten). Gewertet ist H146c. Anlass: Autor (25.11.2026, 20:40): „was passiert, wenn wir damit versuchen, mal die Massen
auszurechnen?“ Vorgaben (über den Koordinator): Eingabe und Ausgabe trennen; Skala frei; keine Masse auf HS(0)/HS(1) im strengeren Sinn;
Vorzeichen nicht setzen; vor „von Daten disfavorisiert“ die Übertragung in den Materie-Frame prüfen (Maske ε = artanh β_sym).

## Vorwissen geprüft
- **Auslesung A (r14–r16, `../../op3_koide_complementarity_2026_11_15/`, H101):** Die Massenwurzeln sind die Eigenwerte der Gram-Matrix G
  der Generationszustände, m_k ∝ λ_k²; K = Tr G²/(Tr G)². Für drei normierte Zustände mit Überlappungen a_ij gilt
  K = (3 + 2 Σ|a_ij|²)/9. K = 2/3 verlangt mittlere Überlappung² ½ (Qubit-Oktant), dann hat ein Zustand die Masse null (flacher Oktant);
  die Brannen-Phase ist arg(a₁₂a₂₃a₃₁)/3.
- **r13, Gesamtbild T5:** Der S₃-symmetrische Trialitätsträger 𝕆³ gibt drei Generationen mit K = ½. H101: Die Maske in Form K hebt das
  masselose Elektron nicht (Sylvester), in Form S (geladene Leptonen, M_e = D C D⁻¹) ändert sie keine Eigenwerte.
- **H138–H145 (dieser Ordner):** Kopien O_v, v = a ⊗ b auf HS(5), Überlappungen v·v′ ∈ {1, −½, ¼}; Rest-Generation = R⁰ ⊗ ℂ𝕆 mit
  c = (−1, −1, 1, 1), also Σ c_k ι_k(y) = 0 für jedes y.
- Messwerte (Polmassen, wie H101): m_e = 0,51099895, m_μ = 105,6583755, m_τ = 1776,93 MeV; K_ℓ = 0,666661.

## Aufbau (Setzung offengelegt)
Generationszustand der Kopie k zur Ladung q: ι_k(y_q) mit dem Ladungseigenzustand y_q der Oktonion-Kopie (Lepton q = 0: (e₀ + i e₇)/√2;
Farbzustand q = ⅓ bzw. ⅔: ein fester Farbvektor, für alle Kopien gleich, H140). Überlappung ⟨ι_k y, ι_l y⟩: Leptonen ½(1 + v_k·v_l),
Farbzustände v_k·v_l (bei transportierter Orientierung). Gram-Auslesung wie oben; die Skala bleibt frei.

## Hypothesen und Kriterien
- **H146a (nicht blind, analytisch):** Mit drei Kopien auf HS(5) ist K ≤ 0,594 (Leptonen, Überlappungen aus {¼, ⅝}) bzw. ≤ ½ (Farbe,
  Überlappungen aus {−½, ¼}); K = 2/3 ist nicht erreichbar. Die drei Sedenion-Kopien geben Leptonen K = 3/8 mit zwei gleichen Massen,
  Farbe K = ½ mit (0, 3/2, 3/2). Prüfung: alle 84 Dreierauswahlen, exakt.
- **H146b (nicht blind, analytisch):** Mit vier Kopien und einer H142-Relation hat die 4×4-Gram-Matrix in jedem Ladungssektor genau einen
  Eigenwert 0 mit Eigenvektor c: Die Rest-Generation ist in der Gram-Auslesung **masselos**, die übrigen drei Eigenwerte sind positiv.
- **H146c (gewertet):** Für diese drei massiven Zustände gilt: K weicht von 2/3 um mehr als 0,01 ab, und es gibt keine Hierarchie
  (m_max/m_min < 100, Leptonen und Farbe, in allen 9 Auswahlen). Bestätigt, wenn beides gilt; sonst widerlegt (dann Werte berichten).
- **Frame-Prüfung (vorab):** Für geladene Leptonen ist die Maske eine Ähnlichkeitstransformation (Form S, r57): Eigenwerte und K bleiben.
  Ein Urteil „von Daten disfavorisiert“ ist daher frame-unabhängig. Für Form K (Neutrinos) wird nichts behauptet.

## Folge, vorab festgelegt
- c bestätigt: Die Kopien-Struktur liefert die Phase 2π/3 (Z₃) und eine masselose Rest-Generation, aber weder K = 2/3 noch die Hierarchie;
  Massen bleiben Eingabe. c widerlegt: Werte berichten und als Kandidat mit neuer Vorab-Notiz prüfen.
- Eingabe: die Gram-Auslesung selbst (Setzung aus r14–r16), die Wahl der Kopien, die Orientierung, die Skala. Ausgabe: nur die Verhältnisse.
- OP3 offen; kein Guard berührt. Werkzeuge: Python (numpy), Wolfram exakt für die Eigenwerte einer Auswahl je Klasse; Qiskit nicht eingesetzt.
- Vergeben: H146, k329.
