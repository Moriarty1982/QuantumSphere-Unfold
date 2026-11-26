# Vorab-Notiz H173: Legt die Algebra den freien Drehwinkel der Mischung fest? Ein-Feld-Form mit gleicher Diagonale

**Stand:** 26.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** a ist von Hand hergeleitet; für b ist der Wert ohne Maske vor der Festlegung
überschlagen (sin²θ₁₃ ≈ 0,014, also voraussichtlich widerlegt). **Blind** sind c (Frame-Übertragung mit der Maske) und d (gemeinsame Anpassung). Anlass: Autor,
26.11.2026, „ja mach das“ zum Wechsel auf Strang 3 (legt die Algebra den freien Drehwinkel fest). Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4.
Vergeben: H173, k368 (geprüft: frei).

## Vorwissen geprüft
- **k262** (`../setzungen_k262/README.md`): Majorana-Neutrinos auf dem Realteil s; ℤ₃ = ⟨T⟩ und ungerade ℤ₂ = ⟨A⟩ geben TM1 mit θ₂₃ = 45°, |sin δ| = 1; allgemeine
  A-invariante reelle Form m = {{f, b, c}, {b, d, −b}, {c, −b, f}} mit vier Parametern: drei Massen und **ein freier Winkel** (θ₁₃). Das ist der freie Drehwinkel.
- **H131** (`../mischung_h131/`), **H134** (`../frame_h134/`, `../../predictions/Ergebnis_H134_…`): Maske D = exp(εW_l), W_l = diag(0, 0, −3), ε = artanh β_sym als
  erklärte Frame-Abbildung für die Mischung; mit freiem φ verträglich mit JUNO 2026 nur in Variante B, keine Vorhersage. Regel des Autors (25.11.): vor „von Daten
  disfavorisiert“ die Übertragung in den Materie-Frame prüfen.
- **H39, H8, H4, k256, k280**: TM1/TM2-Lesarten; k280: Kopplung wählt (2/3, 1/6, 1/6) oder (0, 1/2, 1/2).
- **k278** (`../rueckwaerts/k278/README.md`): Ein-Feld-Prinzip, ein Flavon = ein Element; **H158**: Brannen-Form W = a·𝟙 + Nebendiagonale, Diagonale auf allen
  Plätzen gleich. **H99, H168** (`../delta_h168/`): Neutrino-Spektrum in Brannen-Form mit δ_ν = π/6 − x, x = 0,0395773407; x_ν(Daten) = 0,04336 ± 0,00213.
  **H169**: neutral = kein Anteil in der Ladungsrichtung (c = 0), passt zu Lesart B.
- Suche nach „gleiche Diagonale“, „f = d“, „Winkel aus dem Spektrum“ zusammen mit „TM1“ in `notes/`, `wiki/`: kein Vorbefund (k280 erwähnt gleiche Diagonale nur
  für einen 2×2-Block).

**Suchrichtung:** rückwärts: Ziel θ₁₃; notwendig ist eine vierte Bedingung an m. Die Ein-Feld-Form liefert sie ohne neuen Parameter. **Werkzeugwahl:** Wolfram
für die exakte Herleitung (a), Python (numpy, scipy; Funktionen `charged`, `angles`, `delta_of` unverändert aus `../frame_h134/k263_test_h134.py`) für b bis e.
Qiskit nicht geeignet.

## Aufbau (k368, `k368_test_h173.py`; `k368b_exakt.wl`)
Platzbasis, T und A wie k262b. **Neue Bedingung (die Hypothese):** Das neutrale Feld hat die Ein-Feld-Form N = a·𝟙 + X(s) mit reellem Triplett s, also gleiche
Diagonale, f = d = a. Mit A-Invarianz: N = {{a, b, c}, {b, a, −b}, {c, −b, a}}, drei Parameter. **Spektrum:** Brannen-Form, λ_k = 1 + √2 cos(δ_ν + 2πk/3)
(Feldebene, Massen ∝ λ²; die Massenmatrix N² hat dieselben Eigenvektoren). Zuordnung: feste Spalte w = ν₁ (kleinstes |λ|), normale Ordnung.
Daten: sin²θ₁₃ = 0,02248 ± 0,00056, sin²θ₂₃ = 0,470 (+0,017/−0,014), sin²θ₁₂ = 0,3088 ± 0,0067 (NuFIT 6.1, NO) und 0,3036 ± 0,0064 (JUNO 2026);
R_obs = 0,030016 ± 0,000457.

## Hypothesen und Kriterien
- **H173a (exakt, nicht blind): Der Winkel folgt aus dem Spektrum.** Mit ψ = δ_ν + 2π/3 gilt tan² 2φ = 3 tan² ψ − 1 und sin²θ₁₃ = sin²φ/3,
  sin²θ₁₂ = cos²φ/(3 − sin²φ), θ₂₃ = 45°, |sin δ_CP| = 1. Am Baumwert δ_ν = π/6 ist φ = 0: θ₁₃ = 0, tribimaximal. Reelle Lösungen gibt es nur für δ_ν ≤ π/6
  (gefaltet), also nur für den Versatz nach unten. Kriterium: symbolische Nullreste (Wolfram), Zahlenprobe (Python) auf 10⁻¹².
- **H173b (Test ohne Maske, Erwartung widerlegt):** Mit δ_ν = π/6 − x, x aus den Leptonen, liegt sin²θ₁₃ beim Messwert. Bestätigt bei |z| < 2, widerlegt bei
  |z| > 3. Zusätzlich berichtet: derselbe Vergleich mit x_ν aus den Neutrino-Daten (Fehler fortgepflanzt).
- **H173c (blind): Frame-Übertragung.** Variante A wie H134: U_e mit der Maske bei ε = artanh β_sym (alle Zweige aus `charged`), Neutrino-Seite unverändert
  mit dem festen φ aus a; alle sechs A (p, Vorzeichen), beide Vorzeichen von φ, Zuordnung fest (w = ν₁, dann nach |λ|). Kriterium: **bestätigt**, wenn es einen
  Fall mit sin²θ₁₃ innerhalb 2σ, sin²θ₂₃ innerhalb 3σ ([0,430; 0,596] wie k263) und sin²θ₁₂ im JUNO-2σ-Bereich [0,2908; 0,3164] gibt; **widerlegt**, wenn in
  keinem Fall sin²θ₁₃ innerhalb 3σ liegt; sonst unentschieden. Zufallserwartung wird berichtet (Zahl der Fälle). Kontrolle: bei ε = 0 gleich b auf 10⁻⁹.
  Variante B (ε_ν = ε_e, M_ν = D N² D ohne Nachanpassung) nur als Bericht, mit dem dann entstehenden R.
- **H173d (blind): gemeinsame Anpassung ohne Maske.** x frei, zwei Messgrößen (R_obs und sin²θ₁₃), ein Parameter. Verträglich, wenn χ²_min < 3,84 (p > 0,05,
  ein Freiheitsgrad); sonst nicht verträglich.
- **H173e (Bericht):** Variante „gleiche Diagonale auf der Massenebene“ (Eigenwerte λ²) und die beiden anderen Zuordnungen der festen Spalte. Ohne Kriterium.

## Folge, vorab festgelegt
- a bestätigt: Antwort auf die Frage des Strangs: Mit der Ein-Feld-Form ist der Drehwinkel **nicht mehr frei**, er folgt aus δ_ν; am Baumwert gibt es
  tribimaximale Mischung, und derselbe Versatz x, der das Massenverhältnis R einstellt, erzeugt θ₁₃. Die Ein-Feld-Form bleibt eine Setzung.
- b widerlegt und c widerlegt: Die Zahl stimmt nicht; die Struktur (ein Versatz für R und θ₁₃) bleibt als qualitative Lesart, mehr nicht.
- c bestätigt: verträglich im Materie-Frame; dann ist zu berichten, wie viele diskrete Wahlen eingingen, und ein Folgetest mit schärferer Vorhersage nötig.
- Kein Vorzeichen wird gesetzt; kein Guard berührt; OP3 und OP4 bleiben offen.
