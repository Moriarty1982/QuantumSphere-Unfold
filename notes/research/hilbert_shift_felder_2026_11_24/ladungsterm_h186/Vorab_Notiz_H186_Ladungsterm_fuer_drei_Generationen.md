# Vorab-Notiz H186: Legt ein einzelner Ladungsterm fest, wie sich Up und Down über die drei Generationen unterscheiden?

**Stand:** 26.11.2026, vor der Rechnung. Anlass: Autor, 26.11.2026, „weiter“ nach H185 (nächster Schritt dort). Einordnung: `wiki/Gesamtbild.md`,
T8/T13, OP3/OP4, Strang 2 (Feldgleichung). Vergeben: H186, k389 (geprüft: frei).

## Vorwissen geprüft
- H185 (`../updown_h185/`): komplexes Feld ℂ ⊗ H₃(𝕆); je Ladung eine hermitesche Zirkulante; Up ≠ Down braucht einen Term mit dem Ladungsoperator
  (i·L_U); Spuren ohne ihn trennen nicht. Drei ladungsungerade Formen sind erlaubt (Unterschied in α, Re β, Im β).
- H184 (`../schwingungen_h184/`): Jede Farbmode gehört zu einem Paar (i, j) von Eigenrichtungen des Vakuums (Eigenwerte l_i, l_j, dritter l_k).
- H182 (`../ladung_h182/`): eine ladungsungerade hermitesche Invariante für ein Feld, h = Ψ†(Q₀ − ½)Ψ; C/B = −0,070 (angepasst).
- k376 (`../quarks_k376/`): Massen bei M_Z (als Yukawa-Größen): d (1,54·10⁻⁵; 3,06·10⁻⁴; 1,630·10⁻²), u (7,04·10⁻⁶; 3,56·10⁻³; 0,967), mit Fehlern.
- H179: Georgi-Jarlskog-Faktoren verknüpfen Down mit den Leptonen auf 0,3 bis 5 %, nach Kriterium widerlegt.
- Nicht gefunden: Invarianten mit dem Ladungsoperator auf H₃ und ihre Wirkung je Generation.

## Suchrichtung (rückwärts)
Ziel: der Unterschied ΔX_k = X_k(Up) − X_k(Down) der drei Generationen. Die Daten geben für jede Lesart X ∈ {√m, m, m²} einen Vektor (ΔX₁, ΔX₂, ΔX₃);
seine Richtung (zwei Verhältnisse) ist das Ziel. Notwendig für eine Vorhersage: Die erlaubten ladungsungeraden Terme spannen weniger als drei
Richtungen auf, oder ein einzelner Term wird ausgezeichnet. Zuerst wird der Rang bestimmt, dann werden Einzelterme verglichen.

## Setzungen dieser Notiz
- Feld, Vakuum (reelle Zirkulante, K = ⅔, δ = 2/9, Eingabe), Farbe und P wie H185. Ladungsmischende Terme werden weggelassen (Farbphase als Symmetrie).
- Operator D auf W: (Q₀ − ½) = −(i/6)L_U − (i/3)R_U auf den drei Einträgen neben der Diagonale (x_a, x_b, x_c), null auf der Diagonale.
- Kandidaten (alle bis Grad 4 mit genau einem D, die mir einfallen; Liste vorab fest):
  c1 Re Tr(W̄ ∘ DW); c2, c3 Re, Im Tr((W̄ ∘ DW) ∘ W_U); c4 Re Tr((W̄ ∘ DW) ∘ (W_U ∘ W̄_U)); c5, c6 Re, Im Tr((W̄ ∘ DW) ∘ (W_U ∘ W_U));
  c7, c8 Re, Im Tr((W̄ ∘ W_U) ∘ (DW ∘ W̄_U)); c9, c10 Re, Im Tr((W̄ ∘ W̄_U) ∘ (DW ∘ W_U)); c11 Re Tr((W̄ ∘ DW) ∘ (W ∘ W̄)).
- Zuordnung der Generationen (**Setzung**): Farbmode zum Paar (i, j), geordnet nach l_i + l_j: (e, μ) ↔ 1. Generation, (e, τ) ↔ 2., (μ, τ) ↔ 3.
  Andere Zuordnungen werden nur als nachträglich berichtet.
- Lesarten Frequenzquadrat ↔ Masse: X = √m, m, m² (keine ist hergeleitet). Daten bei M_Z aus k376.

## Hypothesen und Kriterien
- **H186a (Ausgang erwartet, nicht gerechnet):** Die Kandidaten spannen im Raum der ladungsungeraden Verschiebungen (ΔX₁, ΔX₂, ΔX₃) alle drei Richtungen
  auf. Kriterium: Rang 3 (kleinster Singulärwert relativ > 10⁻⁶): **bestätigt** (dann legen Symmetrie und Grad allein nichts fest); Rang < 3:
  **widerlegt** (dann gibt es eine Vorhersage, die gegen die Daten geht).
- **H186b (Ausgang offen):** Ein einzelner Kandidat trifft die Richtung der Daten. Je Kandidat und Lesart zwei Verhältnisse r₁ = ΔX₁/ΔX₃, r₂ = ΔX₂/ΔX₃.
  Kriterium: beide innerhalb von 3σ der Daten (Fehler aus den Massenfehlern, Monte-Carlo) für mindestens ein Paar (Kandidat, Lesart):
  **bestätigt**, mit dem Vermerk, dass 33 Paare verglichen wurden und der Treffer eine eigene Vorab-Prüfung braucht; für kein Paar: **widerlegt**.
- **Bericht:** Richtung der Daten je Lesart; je Kandidat die Verschiebung als Funktion der l (Anpassung an symmetrische Funktionen wie in H184);
  kleinster Abstand in σ.

## Werkzeugwahl
Python (numpy, scipy): wie k388, zweite Variation der Kandidaten auf den 36 Farbrichtungen, ladungserhaltender Anteil, Eigenwerte je Ladung und je
Paar (Zuordnung über eine Referenzform mit Eigenwert 2(l_i + l_j)). Wolfram Language für die exakte Form der Verschiebung eines Kandidaten im
reduzierten Modell. Qiskit nicht geeignet. Ausgaben neben den Skripten.

## Grenzen (vorab)
Kandidatenliste nicht vollständig; Zuordnung der Generationen und Lesart Frequenz ↔ Masse sind Setzungen; Massen bei M_Z ohne Laufen; der
ladungsgerade Anteil bleibt frei und wird nicht geprüft; Grad ≤ 4, ohne Ableitungsterme. Kein Vorzeichen gesetzt. OP3, OP4 bleiben offen.
