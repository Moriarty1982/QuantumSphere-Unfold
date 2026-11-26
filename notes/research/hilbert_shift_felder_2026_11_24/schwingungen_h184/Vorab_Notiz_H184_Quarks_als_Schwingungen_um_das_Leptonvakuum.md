# Vorab-Notiz H184: Welches Muster haben die Farbschwingungen um ein zirkulantes Leptonvakuum in der Albert-Algebra?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, Entscheidungskarte nach H183: „Ein Vakuum, Sektoren schwingen“. Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H184, k387 (geprüft: frei).

## Vorwissen geprüft
- H183 (`../feldgleichung_h183/`): Lepton- und Quarkzustand sind nicht zugleich stabil; um den Leptonzustand eines einzelnen Feldes in ℂ ⊗ 𝕆 haben die
  Schwingungen die Vielfachheiten 6, 6, 1, 1, 1. Dort ohne Generationen.
- H158 (`../generationszahl_h138/`): Träger der drei Generationen ist die Albert-Algebra H₃(𝕆). Ein unter dem Platztausch P invariantes Vakuum ist eine
  Zirkulante W₀ = a·1 + bS + b̄S², Eigenwerte a + 2|b|cos(δ + 2πk/3) (Brannen-Form), K = ⅔ ⇔ |b|² = a²/2, δ = Phase von b in der Ebene {1, U}.
  Grenze dort: „Stabilität gegen nicht zirkulante Richtungen nicht gerechnet.“
- H157: unter J nur gerade Ordnungen. Hier wird J auf H₃(𝕆) nicht gefordert (siehe Setzungen); die Aussagen unten folgen aus weniger Symmetrie.
- k374, k376 (`../konfigurationen_k374/`, `../quarks_k376/`): Brannen-Form je Sektor; CKM-Baumwert 𝟙 bei zirkulanter Form je Sektor; die ganze
  CKM-Matrix braucht eine ℤ₃-Brechung von 0,157 bis 0,166.
- k378: Farbtriplett hat keinen Anteil entlang 1 oder U.
- k282 (`../rueckwaerts/`): σ und C des Verdopplungsschritts, ℤ₃-Vakua in vier von acht Vorzeichenfällen.
- Nicht gefunden: die zweite Variation eines Potentials auf H₃(𝕆) um ein zirkulantes Vakuum, nach Farbe zerlegt.

## Suchrichtung (rückwärts)
Ziel: drei Generationen von Farbtripletts mit drei verschiedenen Massen als Schwingungen um das Leptonvakuum. Notwendig: Die zweite Variation auf den
Farbrichtungen muss drei verschiedene Eigenwerte haben. Was die Symmetrie des Vakuums davon erlaubt, folgt aus seinem Stabilisator und wird geprüft,
bevor Potentiale angepasst werden.

## Setzungen dieser Notiz
- Feld W ∈ H₃(𝕆) (27 reelle Komponenten: drei Diagonalwerte, drei Oktonionen x₁, x₂, x₃). Die Farbe SU(3)_c wirkt auf alle Einträge zugleich.
- Vakuum W₀: Zirkulante mit b in der Ebene {1, U}, K = ⅔ und δ = 2/9 als **Eingabe** (Messwerte der geladenen Leptonen), nicht hergeleitet.
- Potential V: Polynom bis Grad 4, invariant unter SU(3)_c und dem Platztausch P. Zwei Fassungen: mit und ohne die Spiegelung τ (Tausch zweier
  Plätze zusammen mit der Konjugation der Einträge; τ lässt W₀ fest). Koeffizienten zufällig, mit der Bedingung, dass W₀ stationär ist.
- Farbschwingungen: die 18 Richtungen, in denen x₁, x₂, x₃ einen Farbanteil bekommen (drei Plätze mal 3 ⊕ 3̄). Das ist **ein** Quarktyp mit drei
  Generationen; die Trennung in Up und Down (H182, komplexes Feld) ist hier nicht enthalten.
- Keine Zuordnung Frequenz ↔ Masse wird benutzt; verglichen werden nur Vielfachheiten und Eigenrichtungen.

## Hypothesen und Kriterien
- **H184a (nicht blind; folgt aus dem Stabilisator SU(3)_c × ℤ₃):** Die zweite Variation auf den Farbrichtungen ist eine hermitesche Zirkulante mal
  Einheit der Farbe: drei Frequenzquadrate mit Vielfachheit je 6, und die Eigenrichtungen im Platzindex sind die Fourier-Vektoren, unabhängig von den
  Koeffizienten. Kriterium: mindestens 20 zufällige Potentiale, Vielfachheiten (6, 6, 6) und Überlapp der Eigenräume mit den Fourier-Räumen
  > 1 − 10⁻⁶: **bestätigt**; sonst **widerlegt**.
- **H184b (Ausgang offen):** In der Fassung mit τ sind zwei der drei Frequenzquadrate gleich (Vielfachheiten 6 und 12). Kriterium: in allen Proben
  entartet (relativer Abstand < 10⁻⁶): **bestätigt** (dann braucht ein Spektrum mit drei verschiedenen Quarkmassen die Brechung von τ); in keiner
  Probe entartet: **widerlegt**; gemischt: berichtet, ohne Urteil.
- **H184c (Ausgang offen):** Die farblosen Schwingungen (9 Richtungen minus Symmetrierichtungen) haben keine erzwungenen Nullrichtungen außer denen,
  die aus der Symmetrie des Potentials folgen. Kriterium: Zahl der Eigenwerte mit Betrag < 10⁻⁸ in allen Proben gleich der Dimension der Bahn von W₀
  unter der Symmetrie des Potentials: **bestätigt**; mehr Nullrichtungen: **widerlegt** (zufällige Flachheit bis Grad 4).
- **Bericht:** Zahl der freien Größen der Farb-Zirkulante (erwartet 3: α, |β|, φ) gegen drei Massen; ob es Proben gibt, in denen W₀ stabil ist
  (alle Frequenzquadrate > 0); Folge für die Mischung (gleiche Eigenrichtungen für alle Zirkulanten, vgl. k374).

## Werkzeugwahl
Python (numpy): explizite Oktonionen und Jordan-Produkt, Invarianten aus Spuren von Jordan-Potenzen von W und seines Anteils in H₃(ℂ_U),
zweite Variation exakt aus den Polynomen (endliche Differenzen mit Richardson, für Grad 4 exakt bis auf Rundung). Wolfram Language für die
Darstellungsaussage in einem expliziten Beispiel (exakte Arithmetik). Qiskit nicht geeignet (keine Schaltung). Ausgaben neben den Skripten.

## Grenzen (vorab)
Reelles Feld (ein Quarktyp), Grad ≤ 4, statisch und homogen, J nicht gefordert, Vakuum als Eingabe. Die verwendeten Invarianten spannen nicht
notwendig alle Invarianten auf; Aussagen über Vielfachheiten gelten dann für die geprüfte Familie und werden durch das Stabilisator-Argument gestützt.
Kein Vorzeichen wird gesetzt. OP3 und OP4 bleiben offen.
