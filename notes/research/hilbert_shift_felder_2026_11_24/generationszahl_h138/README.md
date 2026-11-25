# Generationszahl aus den Sedenionen (H138–H145; 25.11.2026)

Frage des Autors (25.11.2026): Lässt sich aus den Sedenionen erklären, warum für die Generationen nur 3–4 Kopien entstehen? Ergänzende
Vermutung des Autors: Darüber hinaus gäbe es nur noch Anordnungen aus Nullteilern oder Familien von Nullteilern.

**Kurzfassung.**
- In 𝕊 gibt es genau drei G₂-stabile Oktonion-Kopien, weil ihre Abschlussbedingung Im(z³) = 0 ist (z = Kopienrichtung). „3 statt 4“ ist
  innerhalb einer Verdopplung erzwungen (H138, Wolfram exakt). Die drei sind aber linear abhängig (zwei unabhängige Richtungen).
- Höhere Stufen: HS(5) 15 abgeschlossene Kopien, davon 9 = 3 × 3 oktonionisch; HS(6) mindestens 207, davon mindestens 79 oktonionisch.
  H138a und H138b (Vorhersage 3^k bzw. höchstens drei orthogonale) widerlegt.
- Orthogonale, also unabhängige Kopien sind nie oktonionisch. Zwischen den Kopien gilt exakt: Nullteiler von 𝕊 sind genau die Elemente mit
  gleichem Gewicht in allen Kopienrichtungen (det L_x = (c − s)⁴(c + s)⁴(c² + s²)⁴). Die Überschuss-Algebren auf HS(5) und HS(6) haben
  Imaginärteile aus lauter Nullteilern (H139b, c bestätigt; H139a nach Wortlaut widerlegt, weil die Nullteiler nach außen, nicht innen wirken).
- **H140** (Vorab 94694e6): Alle drei Kopien haben dieselbe Farbe su(3) (S₃-symmetrisch) und je eine Generation mit gleichem Spektrum,
  aber jede ihre eigene Ladung; eine gemeinsame Ladung α + βL_x + γR_x gibt es exakt nicht (Leck ≥ 3|x|²), und es gibt nur 15 statt 24 Zustände.
  In ℂ⊗𝕊 sind die Kopien keine drei Generationen, sondern drei gleichwertige Lesarten einer.
- **H141** (Vorab 589b1c3): Die fehlenden 9 Zustände (Kern von C₀ ⊕ C₁₂₀ ⊕ C₂₄₀ → ℂ⊗𝕊) sind 1 ⊕ 1 ⊕ 1 ⊕ 3 ⊕ 3̄. Ihr Farbteil ist
  ladungsstabil mit den Quarkladungen ⅓, ⅔; die drei Singuletts haben Ladung ½ und lecken. Kein abgeschlossener Sektor, keine gemeinsame Ladung,
  keine Nullteiler.
- **H142** (Vorab 1bc8fb4, Nachtrag f578bff): Vier Kopien auf HS(5). In 9 von 126 Auswahlen (Wechselrelation v₁ − v₂ + v₃ − v₄ = 0) ist der Rest
  eine vollständige, ladungsstabile Generation (0, ⅓³, ⅔³, 1; 1 ⊕ 1 ⊕ 3 ⊕ 3̄) plus zwei leckende Singuletts. b widerlegt; keine gemeinsame Ladung.
- **H143** (Vorab 5a68040): Fünf Kopien auf HS(5). Höchstens eine vollständige Rest-Generation (45 von 126 Auswahlen), und jede stammt aus einer
  der 9 Vierer-Relationen von H142. Regel exakt bestätigt: Zahl der Rest-Generationen = Zahl der Relationen Σ c_k v_k = 0 mit Σ c_k = 0 (alle
  126 × 16 Orientierungen). Die fünfte Kopie bringt nur einen weiteren Quark-Satz oder Leck (½, irrationale Ladungen); keine Nullteiler, keine
  gemeinsame Ladung.
- **H144** (Vorab 54682ea): Trägt die Rest-Generation die anderen Sektoren? Nein, unter der Sektorregel (ℂ als C-Faktor der Frames) hat sie
  dieselbe Signatur wie eine Kopien-Generation: Quarks s = 0, Leptonen |s| = ½ (Wolfram exakt). Frame-Abbildungen wirken trägerweise und
  verbinden Kopien und Rest nicht; z ↦ z̄ bildet den Rest auf sich ab mit q ↦ 1 − q, das ist der globale Vorzeichenwechsel der Orientierung.
  Die Signatur folgt der Ladung, nicht dem Leck. c widerlegt; d trivial erfüllt.
- **H145** (Vorab 6e5a6b5): Ist der Rest wieder ein HS(0)? Nicht als Algebra (nicht abgeschlossen, kein Produkt auf der Linie bei gleich
  orientierten Kopien). Aber K = (D⁰ ⊗ e₀) ⊕ (R ⊗ Im𝕆) exakt, und die Rest-Generation ist R⁰ ⊗ ℂ𝕆: eine ganze Oktonion-Kopie über einer reellen,
  ladungsfreien, zeitumkehrfesten Linie (HS(0)-Merkmale). Die Rest-Leptonen entstehen dort, wo die aufgehobenen reellen Einheiten (HS(0) der
  Kopien) mit einer Relation zusammenfallen. Gemischte Vorzeichen = gespiegelte Kopien (Anti-Isomorphismus); c nach Wortlaut widerlegt.
- Status: „3 je Verdopplung“ gezeigt (bedingt auf G₂-Stabilität); „Kopien = Generationen“ offen; Generationszahl bleibt Eingabe.

Dateien: Vorab- und Ergebnis-Notizen H138–H145; Skripte k321–k328 (je mit b-Gegenprobe in Wolfram, teils c, d) mit Ausgaben. Aufruf aus diesem Ordner.
Werkzeuge: Python, Wolfram (exakt bis HS(5)); Qiskit nicht eingesetzt.
