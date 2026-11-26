# Vorab-Notiz H181: Zwei Lesarten des M-Zustands (b/a = β_sym oder b/a = β_sym²)

**Stand:** 2026-11-26, vor der Rechnung k383 festgeschrieben. Auftrag des Autors (26.11.2026, 21:52 UTC): „kannst du beides mal nachrechnen“,
auf die Weggabelung nach r70: Entweder war der Treffer κ = (γ_L + 1/γ_L)/2 → m_h = 124,8 GeV (k303) Zufall, oder für den HC gilt doch die
Lesart b/a = β_sym².

**Blindheit, offen gesagt:** Teil 1 ist **nicht blind**. Alle Größen dort sind geschlossene Formeln; ihre Werte stehen im Kopf oder im Bestand
schon fest (unter Lesart A gäbe das Wörterbuch D etwa m_W ≈ 70 GeV). Festgeschrieben werden trotzdem Wörterbuch, Messwerte und Kriterien,
damit nichts nach dem Sehen gewählt wird. **Blind ist nur Teil 2** (Maskenscan bei zwei neuen Werten von ε; Ausgabe nicht bekannt).

## Vorwissen geprüft
- r70 (`notes/research/v4_10_0_r70_portgewichte_hc/`, k382): Lesart W (Gewichte, b/a = β_sym, Rapidität η_W = artanh β_sym = 0,617530) gegen
  Lesart A (Amplituden, b/a = β_sym², Rapidität η_A = artanh β_sym² = 0,311553). cosh 2η_W = γ_L, cosh 2η_A = (γ_L + 1/γ_L)/2, e^{2η_A} = γ_L.
- k303 (`feldgleichung/Rueckwaertssuche_kappa_k303.md`): Ziel κ* = 1,2039 (1,202 bis 1,206), Fenster der Zahlensuche 1,08 bis 1,32,
  Genauigkeit der Ein-Schleifen-Formel einige Prozent, Treffer auf Zufallsniveau; r64.4 ebenso.
- k358 (`op1_herkunft_beta_sym_h165/Nachrechnung_k358_Empfindlichkeit.md`): Messwerte und Formeln der Stellen, die an β_sym hängen
  (H15 m_W, H96 Ω_M, H9 sin²θ₁₂, Maske H45/H46 mit Fenster η ∈ [0,611; 0,647] aus r61).
- Zufallsabschätzung (Wiki Forschungsstand, „Zufallsabschätzung“): Ω_M = β², |U_e2|² = β², cot θ_W = γ_L sind einzeln gesetzte
  Gleichsetzungen, kein gemeinsames Wörterbuch. H112 (Überbestimmung) verlangt nur Gleichheit der zwei Ablesungen von β².
- Suche nach „H181“ und „k383“ im Repo: frei. Vergeben hiermit: **H181, k383**.

## Hypothese
H181: **Der M-Zustand des HC ist der mit b/a = β_sym² (Lesart A), und er ist derselbe Zustand, an dem die übrigen Ablesungen hängen.**
Gegenstück: Lesart W (b/a = β_sym, r70).

## Teil 1 (nicht blind): ein Wörterbuch, zwei Zustände
Wörterbuch D, festgelegt aus der Geometrie von r70.1 (Zustand mit Rapidität η, tanh η = b/a), gleich für beide Lesarten:

| Nr. | Größe | Formel in D | Messwert |
|---|---|---|---|
| Q1 | m_W | m_Z·c/√(1 + c²), c = cot θ_W = cosh 2η (Verhältnis Links- zu Rechtsladung, 1/b_C) | PDG 2026 80,3625 ± 0,0077 GeV, dazu 1,8 MeV aus m_Z |
| Q2 | Ω_M | tanh² η | DESI DR2 0,2975 ± 0,0086; Planck 2018 0,315 ± 0,007 |
| Q3 | sin²θ₁₂ | tanh² η/(1 − s₁₃), s₁₃ = 0,02215 | JUNO 2026 0,3036 ± 0,0064 |
| Q4 | Maske | ε = η | Fenster 0,611 bis 0,647 (r61) |
| Q5 | m_h | κ = cosh 2η, m_h = 125,20 GeV·√((16κ² − 2,77)/20,42) (Anteile aus k303) | 125,20 GeV, Formel auf etwa 5 % genau |

Kriterien je Größe: |z| < 2 „trägt“, |z| > 3 „widerlegt“, dazwischen „offen“; Q4: im Fenster oder nicht; Q5: innerhalb 5 % „trägt“
(kein Beleg, Zufallsniveau nach k303), über 10 % „widerlegt“.

**Urteil H181 (Teil 1):** bestätigt, wenn Lesart A in D mindestens Q1 bis Q4 trägt; **widerlegt**, wenn A in D mindestens zwei von Q1 bis Q4
verfehlt. Dann kann der κ-Treffer nicht am selben Zustand hängen wie die übrigen Ablesungen: Er ist Zufall, oder es gibt einen zweiten Zustand.
Erwartung (offengelegt): widerlegt.

## Teil 1b (Erkundung, kein Kriterium): Lässt sich A mit einem zweiten Wörterbuch retten, und trennt κ überhaupt?
- Wörterbuch D′ für A: cot θ_W = Achsenverhältnis e^{2η}, Ω_M = tanh η (Amplituden- statt Gewichtsverhältnis), Maske ε = 2η, κ = cosh 2η.
  Prüfen, welche Zahlen gleich bleiben und welche Setzung von Konvention F (x als Gewichtsverhältnis, r22 bis r24) dabei bricht.
- Für **beide** Lesarten dieselbe feste Liste einfacher Funktionen von η als κ einsetzen (tanh, coth, sinh, cosh, e^{±}, je mit η und 2η, dazu
  Kehrwerte): Wie viele liegen innerhalb 5 % von κ*? Gibt W ebenso viele Treffer wie A, trennt der κ-Treffer die Lesarten nicht.

## Teil 2 (blind): Maskenscan
Der unveränderte Code `notes/research/v4_10_0_r63_r64/llm/k105_h46_exakt.py` mit ε = η_W = 0,617530, ε = η_A = 0,311553 und ε = 2η_A = ln γ_L = 0,623105.
Festgehalten werden Trefferzahl und das Fenster von sin²θ₂₃ und |sin δ| je Wert.
- Kriterium: Gibt ε = η_A keine Treffer, ist Q4 für A in D verfehlt (Bestätigung der Fensterangabe aus r61 am Scan).
- Unterscheiden sich die sin²θ₂₃-Fenster von ε = η_W und ε = 2η_A um mehr als 0,005 in der Mitte, ist sin²θ₂₃ eine Größe, die W mit D von A mit D′
  trennt; sonst trennt die Maske sie mit heutigen Daten nicht. Welche Messgenauigkeit nötig wäre, wird angegeben.

## Werkzeuge
Python (mpmath/numpy) für die Zahlen, Wolfram Language als unabhängige Gegenprobe der geschlossenen Formeln (exakte Identitäten cosh 2η_A,
e^{2η_A}). Qiskit passt nicht (keine Schaltung, keine Messsimulation). Kein RUN_TAPE betroffen, kein HDL-Vergleich.

## Grenzen
β_sym ist das Postulat r67 (OP1 offen). Die Messwerte sind die im Bestand geführten. Das Wörterbuch D ist eine Setzung dieser Notiz;
im Bestand sind Q1 bis Q3 einzelne Gleichsetzungen. Kein Guard wird berührt; OP1 bis OP5 bleiben offen.
