# Vorab-Notiz H177: Halbiert sich die Phase δ von Sektor zu Sektor bei einer gemeinsamen Skala?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026 („nötige Konfigurationen suchen … wie die zusammenhängen könnten … auf welcher HS-Stufe die
Teilchen sitzen“). Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3. Vergeben: H177, k375 (geprüft: frei).

**Blindheit:** Die Beobachtung selbst (δ ≈ 0,480 / 0,222 / 0,100 / 0,052 für ν / e / d / u) ist **nachträglich** aus k374 abgelesen. Blind ist nur die
Frage dieser Notiz: wie sich δ_d und δ_u unter dem Laufen der Massen oberhalb von M_Z verschieben. Das ist bisher im Projekt nicht gerechnet.

## Vorwissen geprüft
- H1/k14 und H172/k367 (`../delta_h172/`): δ_d = 0,100129 ± 0,000953, δ_u = 0,051806 ± 0,000483 bei M_Z; bei den „Standardskalen“ 0,1101 und 0,0746.
  Die Standardskalen sind je Quark verschieden und deshalb kein gemeinsamer Punkt. H172 (Regel χ = |Q|π/4) ist widerlegt.
- k374 (`../konfigurationen_k374/`): Tabelle je Sektor, Halbierung als ungetestete Beobachtung.
- Suche nach früheren Rechnungen zum Laufen der Massenverhältnisse (Stichworte RGE, laufende Masse) in `notes/research/`: keine zu den Brannen-Phasen der Quarks.

## Suchrichtung (rückwärts)
Notwendige Bedingung statt weiterer Kandidaten: Unter der QCD laufen alle Quarkmassen bei gemeinsamer Skala mit demselben Faktor, K und δ ändern sich
dadurch nicht. Oberhalb von M_Z ändert in führender Ordnung nur die Top-Yukawa-Kopplung die Verhältnisse, und zwar über **eine** Zahl
I(μ) = ∫ (3/2)·y_t²/(16π²) d ln μ (von M_Z bis μ): m_u/m_t und m_c/m_t ∝ e^(−I), m_d/m_b und m_s/m_b ∝ e^(+I); m_u/m_c, m_d/m_s und die Leptonverhältnisse
bleiben. Damit hängen δ_d und δ_u nur von I ab, und die Frage wird ein-parametrig.

## Hypothese und Kriterien
Zwei vorab festgelegte Fassungen der Halbierung:
- **V1 (Verhältnis):** δ_d = δ_e/2 = 0,111111 und δ_u = δ_e/4 = 0,055556.
- **V2 (Baumwerte):** δ_d = π/24 = 0,130900 und δ_u = π/48 = 0,065450.

Bereich: I von 0 (M_Z) bis I(M_Planck = 1,22·10¹⁹ GeV), mit Ein-Schleifen-Laufen des Standardmodells (g₁, g₂, g₃, y_t).
Fehler: Massenfehler bei M_Z per Monte Carlo (10⁵ Ziehungen, Seed 20261126), wie k367.

- **H177a trägt** (für eine Fassung), wenn es ein I im Bereich gibt, bei dem δ_d **und** δ_u beide innerhalb von 3σ am Zielwert liegen.
- **Nicht gemeinsam**, wenn jede der beiden Phasen ihren Zielwert im Bereich erreicht, aber bei I-Werten, die um mehr als 3σ auseinanderliegen.
- **Widerlegt**, wenn mindestens eine Phase ihren Zielwert im Bereich nicht innerhalb von 3σ erreicht.
- Weil zwei Fassungen geprüft werden, zählt ein Treffer erst ab 3σ-Verträglichkeit beider Phasen und wird mit dem Faktor 2 (zwei Fassungen) berichtet.
- **H177b (Bericht, kein Kriterium):** K_d(I) und K_u(I) über den Bereich; ob K_d oder K_u irgendwo ⅔ erreicht; die Variante mit negativer leichtester
  Wurzel; die I-Werte, bei denen δ_d/δ_u = 2 gilt.

## Werkzeugwahl
Python (numpy/scipy) für das Laufen und die Monte-Carlo-Fehler; Wolfram Language als unabhängige Kontrolle der Zentralwerte (exakte Brannen-Zerlegung und
NDSolve für I). Qiskit nicht geeignet (keine Schaltung).

## Grenzen (vorab)
Ein-Schleifen-Näherung mit Top-Dominanz; Schwellen und Zwei-Schleifen-Terme nicht enthalten; nur Standardmodell-Teilcheninhalt. Die Zuordnung der Sektoren
zu HS-Stufen wird hier nicht gesetzt; ein Treffer wäre eine Zahlenbeziehung, keine Herleitung. Kein Vorzeichen wird gesetzt. OP3/OP4 bleiben offen.
