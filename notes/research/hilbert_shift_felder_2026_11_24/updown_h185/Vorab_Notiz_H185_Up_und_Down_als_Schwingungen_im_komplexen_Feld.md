# Vorab-Notiz H185: Trennt das komplexe Feld die Farbschwingungen in Up und Down?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, „weiter“ nach H184 (nächster Schritt dort: komplexes Feld). Einordnung:
`wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H185, k388 (geprüft: frei).

## Vorwissen geprüft
- H184 (`../schwingungen_h184/`): reelles Feld in H₃(𝕆), Farbschwingungen um das zirkulante Leptonvakuum = hermitesche Zirkulante (drei Frequenzen je
  sechsfach, ein Quarktyp). F₄-invariante Potentiale lassen sie masselos.
- H182 (`../ladung_h182/`): Feld in ℂ ⊗ 𝕆, Ladung Q₀ = ½ − (i/6)L_U − (i/3)R_U; auf dem Farbblock ⅓ und ⅔ je dreifach, auf {1, U} 0 und 1.
  ℂ-Konjugation tauscht ⅓ ↔ ⅔; genau eine hermitesche ladungsungerade Invariante, im Farbblock.
- H183 (`../feldgleichung_h183/`): um den Leptonzustand eines Feldes Vielfachheiten 6, 6, 1, 1, 1 (zwei Farbgruppen nach Ladung).
- k374, k376: Brannen-Form je Sektor, CKM-Baumwert 𝟙.
- Nicht gefunden: die zweite Variation auf ℂ ⊗ H₃(𝕆) um das Leptonvakuum, nach Ladung zerlegt.

## Suchrichtung (rückwärts)
Ziel: zwei Quarktypen (Ladung ⅓ und ⅔) mit je drei Generationen und sechs verschiedenen Massen. Notwendig: Die zweite Variation hat einen Anteil,
der die Ladungen trennt, und keinen (oder einen kleinen) Anteil, der sie mischt. Zuerst wird gezählt, was der Stabilisator des Vakuums erlaubt.
Da Farbe und P das Vakuum fest lassen, ist jede unter ihnen invariante quadratische Form die zweite Variation eines invarianten Potentials
(V = q(W − W₀)); die Zählung der Formen ist damit vollständig.

## Setzungen dieser Notiz
- Feld W = A + iB mit A, B ∈ H₃(𝕆) (54 reelle Komponenten). Farbe und Platztausch P wie in H184. i ist die Einheit von ℂ in ℂ ⊗ 𝕆.
- Vakuum W₀: dieselbe reelle Zirkulante wie in H184 (K = ⅔, δ = 2/9, **Eingabe**). Sie ist kein Ladungseigenzustand (die reelle 1 mischt Q = 0 und 1).
- Farbrichtungen: 36 reelle (drei Plätze, 3 ⊕ 3̄, komplex). Ladung dort: Q₀ = ½ + (i/6)L_U (weil R_U = −L_U auf dem Farbblock), also ⅓ und ⅔.
- Symmetrien als Varianten: nur Farbe und P; zusätzlich Phase e^{iθ} auf den Farbrichtungen (Ladungserhaltung im Farbteil); zusätzlich
  ℂ-Konjugation C; zusätzlich τ.
- Keine Zuordnung Frequenz ↔ Masse.

## Hypothesen und Kriterien
- **H185a (nicht blind; Darstellungstheorie):** Unter Farbe und P gibt es 12 invariante quadratische Formen auf den 36 Farbrichtungen; die zweite
  Variation ist blockzirkulant, sechs Frequenzquadrate je sechsfach, Eigenrichtungen im Platzindex sind die Fourier-Vektoren. Kriterium: Zahl 12 und
  Vielfachheiten (6,6,6,6,6,6) in mindestens 20 Proben: **bestätigt**; sonst **widerlegt**.
- **H185b (nicht blind):** Von den 12 Formen vertauschen 6 mit i (erhalten die Ladung: je eine Zirkulante für ⅓ und ⅔) und 6 antivertauschen
  (mischen ⅓ und ⅔). Kriterium: Zählung 6 + 6: **bestätigt**; sonst **widerlegt**. Folge bei Bestätigung: Sechs Massen ohne Mischung der Ladungen
  verlangen eine zusätzliche Symmetrie oder ein Vakuum, das die Ladung erhält.
- **H185c (Ausgang erwartet, nicht gerechnet):** Mit C dazu sind die Spektren für ⅓ und ⅔ gleich. Kriterium: in allen Proben gleich (relativ
  < 10⁻⁸): **bestätigt** (Up ≠ Down verlangt die Brechung von C, wie H182); sonst **widerlegt**.
- **H185d (Ausgang offen):** Potentiale aus Jordan-Spuren von W, W̄ und ihren Anteilen in H₃(ℂ_U), **ohne** expliziten Ladungsoperator, bis Grad 4:
  Der ladungsungerade Anteil der zweiten Variation (Unterschied der Zirkulanten für ⅓ und ⅔) ist bei δ = 2/9 von null verschieden und bei δ = 0
  null. Kriterium: relativer ladungsungerader Anteil > 10⁻⁶ für mindestens eine Invariante bei δ = 2/9 und < 10⁻⁹ für alle bei δ = 0:
  **bestätigt** (dann hängt die Trennung von Up und Down an der Leptonphase); bei δ = 2/9 für alle < 10⁻⁹: **widerlegt** (Trennung braucht den
  Ladungsoperator ausdrücklich); sonst Bericht ohne Urteil.
- **Bericht:** Zahl der freien Größen je Variante gegen sechs Massen; Größe des ladungsmischenden Anteils in den Spurpotentialen.

## Werkzeugwahl
Python (numpy, scipy): explizite Oktonionen, komplexes Jordan-Produkt, invariante Formen als Nullraum der Stabilisatorbedingungen, zweite Variation
der Spurpotentiale auf den 36 Farbrichtungen (endliche Differenzen, für Grad ≤ 4 exakt bis auf Rundung). Wolfram Language für eine exakte Gegenprobe
der Blockstruktur in einem kleinen Beispiel. Qiskit nicht geeignet (keine Schaltung). Ausgaben neben den Skripten.

## Grenzen (vorab)
Grad ≤ 4, statisch und homogen, ohne Ableitungsterme; Vakuum als Eingabe; J auf H₃ nicht gefordert; die Spurfamilie in H185d ist nicht vollständig
(ein Nullbefund gilt für die geprüfte Familie). Q₀ wirkt nur auf die Einträge außerhalb der Diagonale. Kein Vorzeichen gesetzt. OP3, OP4 bleiben offen.
