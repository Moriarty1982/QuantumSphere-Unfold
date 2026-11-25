# Vorab-Notiz H138: Wie viele Oktonion-Kopien erzeugt der Turm, und wie viele davon sind unabhängig?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** Für HS(4) (Sedenionen) ist das Ergebnis bekannt
(drei Kopien O_0, O_120, O_240, k254, k259 exakt); es dient nur als Kontrolle. **Blind** sind die Zählungen auf HS(5) (32 Dimensionen)
und HS(6) (64 Dimensionen). Anlass: Frage des Autors (25.11.2026, 18:52): „kannst du mal bei den Sedenionen nachsehen, ob wir evtl.
erklären können, wieso für die Generationen nur 3–4 Kopien erzeugt werden können?“

## Vorwissen geprüft
- k253 (`../README.md`): Der(A_n) = g₂ für n ≥ 3; ab HS(4) keine neue stetige Symmetrie.
- k254 (`../hs4/`): Aut(𝕊) = G₂ × S₃, drei Oktonion-Kopien mit paarweisem Schnitt ℝ; nach Eakin–Sathaye bringt jede weitere Verdopplung
  ein weiteres S₃ (Literatur, im Projekt nicht nachgerechnet). Radon–Hurwitz-Achsen 8, 9, 11 für n = 4, 5, 6.
- k255 (`../r13/`): O_θ = span{1, cos θ e_i + sin θ e_{i+8}} ist nur für θ = 0°, 60°, 120° eine Unteralgebra; die drei Kopien sind ein
  straffer Rahmen (Hauptwinkel 60°), ihre Ladungen vertauschen nicht; ℂ⊗𝕊 trägt keine drei Generationen.
- k259/k260 (`../drei_kopien_k259/`): unter su(3)_c genau fünf abgeschlossene Teilräume, davon drei oktonionisch (exakt, Reduce).
- H130 (`../ladungsrichtung_h130/`): oktonionische Träger nur mit u₈ = 0; B_± nicht alternativ.
- K28 (`notes/research/v4_8_0_r03_r12/llm/Trennung_Farbe_Generation.md`): 𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2) unter G₂ × S₃; die drei Kopien
  eines Farbzustands haben Rang 6, nicht 9 (Gillard–Gresnigt, arXiv:2306.13098, lineare Abhängigkeit): **zwei** unabhängige Generationen.
- k273 (Projektordner `rueckwaerts-felder/generationen/`): Clifford-Achsen e₈, e₁₆, e₃₂ wirken als Dublett; drei Generationen als
  Familie verlangen ein Im ℍ als Vektor; eine vierte Generation ist nicht verboten, aber kein Mitglied derselben Familie.
- Nicht gefunden: eine Zählung der Kopien auf HS(5) oder HS(6). Das ist die neue Rechnung.

## Aufbau
- Cayley–Dickson-Konvention des Projekts (k253): (a,b)(c,d) = (ac − d̄b, da + bc̄). A_n, Dimension 2ⁿ, m = 2^{n−3} Blöcke zu je 8.
- G₂ wirkt blockweise gleich (D ⊕ D ⊕ …, die 14 Derivationen von 𝕆; vorher geprüft, dass sie Derivationen von A_n sind).
  Dann ist A_n = ℝ^m (Singuletts e_{8k}) ⊕ 7 ⊗ ℝ^m.
- **Gesetzt:** Eine Kopie ist eine unitale, G₂-stabile, achtdimensionale Unteralgebra. G₂-Stabilität und Unitalität zwingen die Form
  O_v = span{1} ⊕ {a ⊗ v : a ∈ Im 𝕆} mit v ∈ S^{m−1} (bis auf ±v). Gesucht sind alle v mit abgeschlossenem O_v.
- Python k321: Abschlussdefekt d(v) = Norm des Anteils von (a⊗v)(b⊗v) außerhalb O_v über alle a, b; Minimierung mit 2000 Zufallsstarts
  je Stufe, Cluster der Lösungen (bis auf ±v), Prüfung der Hesse-Matrix auf flache Richtungen (Schar oder isoliert),
  Alternativität und Normmultiplikativität jeder Lösung, paarweise Winkel, Rang des Spanns der Imaginärteile.
- Wolfram k321b: Abschlussbedingung als Polynomsystem in v (n = 4, 5 exakt mit Reduce/Solve über ℝ; n = 6, falls exakt nicht machbar,
  NSolve oder Grad-Abschätzung), unabhängig von Python.

## Hypothesen und Kriterien
Bezeichnungen: N_n = Zahl der Kopien (Klassen ±v), r_n = (Rang des Spanns aller Imaginärteile)/7 (Zahl unabhängiger Kopien),
o_n = größte Zahl paarweise orthogonaler Kopien (v_i · v_j = 0).
- **H138a (Kopienzahl wächst multiplikativ):** N_5 = 9 und N_6 = 27, also N_n = 3^{n−3}: jede Verdopplung ab 𝕊 verdreifacht die Kopien.
  Bestätigt, wenn beide Zahlen exakt so herauskommen und keine Lösung flache Richtungen hat (kleinster Hesse-Eigenwert auf der Sphäre
  > 10⁻⁶). Widerlegt sonst (andere endliche Zahl oder Schar).
- **H138b (keine vier unabhängigen Träger):** o_5 ≤ 3 und o_6 ≤ 3, d. h. auf keiner Stufe gibt es vier paarweise orthogonale
  Oktonion-Kopien. Bestätigt, wenn die exakte größte Clique im Orthogonalitätsgraphen (Schranke |v_i·v_j| < 10⁻⁹) höchstens 3 hat.
  Widerlegt bei o ≥ 4 auf einer der Stufen.
- **Kontrolle:** n = 4 gibt genau N_4 = 3 (θ = 0°, 60°, 120°), r_4 = 2, o_4 = 1; Derivationsdefekt der blockweisen G₂ < 10⁻¹¹;
  Abschlussdefekt der Lösungen < 10⁻¹¹.
- **Erkundung ohne Kriterium (offen ausgewiesen):** die analytische Form der Bedingung bei n = 4 (Vermutung: sin 3θ = 0, also eine
  Dreizähligkeit aus Konjugation und Quadrat im Verdopplungsprodukt) und, falls lösbar, das Bildungsgesetz auf HS(5), HS(6).

## Folge, vorab festgelegt
- H138a bestätigt: Die Zahl 3 ist die Kopienzahl **einer** Verdopplung über 𝕆; höhere Stufen geben 3^k Kopien, aber nicht mehr
  unabhängige Träger als 2^{n−3}. Die „3“ wäre dann im Turm erzwungen (nicht gesetzt), aber nur für die Stufe HS(4).
- H138b bestätigt: Mehr als drei gleichzeitig unabhängige (orthogonale) Oktonion-Träger erzeugt der Turm bis HS(6) nicht; eine vierte
  Generation als vollwertige Kopie wäre dort ausgeschlossen. H138b widerlegt: der Turm erlaubt vier (oder mehr) orthogonale Kopien,
  und „3 statt 4“ bleibt eine Eingabe.
- Was in keinem Fall folgt: dass die Kopien Generationen *sind* (k255: Ladungen vertauschen nicht; K28: Rang 6), Massen, Mischung oder
  Vorzeichen. Vorzeichen bleiben offen bis zur Feldgleichung. OP3, OP4 offen; kein Guard berührt.
- Skripte: k321 (Python), k321b (Wolfram). Vergeben: H138, k321.
