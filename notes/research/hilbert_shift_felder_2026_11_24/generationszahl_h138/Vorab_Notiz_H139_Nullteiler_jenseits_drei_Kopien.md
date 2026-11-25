# Vorab-Notiz H139: Liegen die Anordnungen jenseits der drei Kopien in den Nullteilern?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind, nachträglich motiviert:** Dass es auf HS(5) neben den
oktonionischen Kopien sechs weitere abgeschlossene, nicht alternative G₂-stabile Unteralgebren gibt, ist aus k321/k321b (Test H138) schon
bekannt (Lauf vor dieser Notiz). Unbekannt ist, ob sie Nullteiler enthalten. Die Form der Sedenion-Nullteiler (H139c) ist aus der Literatur
bekannt (Moreno 1998; de Marrais, Box-Kites), aber im Projekt nicht in der Kopien-Sprache gerechnet; Teil c ist deshalb **nicht blind**.
Anlass: Vermutung des Autors (25.11.2026, 19:34): „wenn man versucht, mehr als drei Generationen damit darzustellen, könnte es sein, dass die
restlichen Anordnungen nur noch durch die Nullteiler dargestellt sein könnten oder durch Familien von Nullteilern.“

## Vorwissen geprüft
- k254 (`../hs4/`): Nullteiler (e₁ + e₁₀)(e₄ − e₁₅) = 0; L_a für a = (e₁ + e₁₀)/√2 hat vierdimensionalen Kern; G₂-Bahn 11-dimensional (Moreno).
- k255 (`../r13/`, Punkt 7): Elemente w ⊗ n vom Rang 1 sind nie Nullteiler; Nullteiler sind „verschränkt“ (Rang 2 in 7 ⊗ ℝ²), die Lecks
  liegen zwischen den Kopien.
- H138 (diese Mappe, Vorab 31732b4): Kopienzahl; k321/k321b: HS(4) genau drei Kopien (Bedingung t₂(3t₁² − t₂²) = 0), HS(5) 15 abgeschlossene
  O_v, davon 9 oktonionisch und 6 nicht alternativ.
- Atlas r27.2 und HS(4)-Meta-Septum: Leckregister statt freier Sedenionen.

## Aufbau
Konvention wie k253. Kopien-Sprache: A_n = ℝ^m ⊕ 7 ⊗ ℝ^m (m = 2^{n−3}); ein Element x des 7 ⊗ ℝ^m-Teils ist eine 7 × m-Matrix M(x).
Kopienprofil p_x(v) = |M(x) v|² für Einheitsvektoren v (Gewicht von x in Kopienrichtung v). Nullteiler: x ≠ 0 mit xy = 0 für ein y ≠ 0
(kleinster Singulärwert von L_x gleich 0).
Skript k322 (Python), Gegenprobe k322b (Wolfram, exakt an den Basis-Nullteilern und einem symbolischen Profil).

## Hypothesen und Kriterien
- **H139a (Überschuss-Anordnungen sind Nullteiler-Träger, HS(5)):** Jede der 6 nicht alternativen abgeschlossenen O_v enthält einen inneren
  Nullteiler (x, y ∈ O_v, |x| = |y| = 1, |xy| < 10⁻¹⁰, gefunden durch Minimierung des kleinsten Singulärwerts von L_x auf O_v über x).
  Gegenstück: Keine der 9 oktonionischen Kopien enthält einen Nullteiler von A₅ (kleinster Singulärwert von L_x auf ganz A₅ über
  1000 Zufallselemente und Minimierung > 10⁻⁶). Bestätigt, wenn beides gilt.
- **H139b (Nullteiler haben kein Kopienprofil, HS(4)):** Jeder Nullteiler von 𝕊 liegt ganz im 7 ⊗ ℝ²-Teil und hat ein flaches Profil,
  M(x)ᵀM(x) = (|x|²/2)·𝟙, also gleiches Gewicht ½ in jeder Kopienrichtung, insbesondere gleich auf allen drei Kopien. Geprüft an allen
  Basis-Diagonalen e_i ± e_j, die Nullteiler sind (vollständige Suche über i < j), und an 500 Nullteilern aus Kernen von L_x zufälliger
  G₂-Bilder. Bestätigt, wenn die Abweichung vom flachen Profil überall < 10⁻¹⁰ ist.
- **H139c (Umkehrung, nicht blind):** Jedes Element mit flachem Profil (M = [a b], a ⊥ b, |a| = |b|) ist ein Nullteiler (kleinster
  Singulärwert von L_x < 10⁻¹⁰ in 500 Zufallsfällen), und jedes Element mit nicht flachem Profil ist keiner (> 10⁻⁶ in 500 Fällen).
- **Kontrollen:** (e₁ + e₁₀)(e₄ − e₁₅) = 0 reproduziert; Zahl der Basis-Diagonalen-Nullteiler wird berichtet (Literatur: 84 bzw. 168 mit
  Vorzeichen; nicht als Kriterium).

## Folge, vorab festgelegt
- H139a–c bestätigt: Marcs Vermutung hat eine präzise Form. Auf HS(4) gibt es genau drei Kopien; ein Element, das keiner Richtung zugeordnet
  ist (gleich verteilt über alle Kopienrichtungen), ist genau ein Nullteiler. Auf HS(5) sind die über die 3 × 3 oktonionischen hinaus
  zusätzlichen Anordnungen Nullteiler-Träger. Weitere „Generationen“ wären dann keine normierten Träger, sondern Leck-Zustände.
- Widerlegt in einem Teil: Die Vermutung gilt in dieser Form nicht; welcher Teil scheitert, wird benannt.
- Was in keinem Fall folgt: dass Nullteiler physikalisch eine vierte Generation verbieten oder darstellen. Vorzeichen bleiben offen bis zur
  Feldgleichung. OP3, OP4 offen; kein Guard berührt.
- Vergeben: H139, k322.
