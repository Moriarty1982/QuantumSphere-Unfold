# Vorab-Notiz H127: Spin-Inhalt der Ladungsbrechung und Leckordnung in die Quarks

Festgelegt am 2026-11-24, **vor** der Rechnung. Auftrag: Autor „weiter“ auf den Vorschlag des Koordinators, die Brechung SO(3) → A₄ aus
k275 in eine Massenmatrix zu übersetzen, und „weiter“ auf den Entwurf dieser Notiz (24.11.2026). Skripte ab **k276** (Python numpy;
Wolfram Language exakt zur Kontrolle von Stufe A). Qiskit nicht vorgesehen (keine Schaltung). Bezug OP3 (#131).

## Vorwissen geprüft
- **k275** (#290, `notes/research/hilbert_shift_felder_2026_11_24/rueckwaerts/trialitaet/`): Kommutant von G₂ in f₄ = so(3) mit X ↦ RXRᵀ, Vektor auf
  den Plätzen; auf den Farbtripletts [so(3), L_e₇] = 0 exakt, auf den Farbsinguletts 2; Rest A₄ (12 von 24), die ungeraden Elemente konjugieren
  (L_e₇ → −R_e₇).
- **H39 / r55** (A₄-Untergruppen als Lesarten: ℤ₃ für Dirac-Sektoren, ℤ₂ für Neutrinos → TM2; θ₁₂ scharf, JUNO 3,6 σ darunter; H39d: V_CKM = 1 in
  führender Ordnung).
- **k256** (Kopien-S₃: alle Muster vorab fest, kein blinder Test; K∘S₀ hält TM1). **H8** (Cayley–Dickson-Involution als CP → TM1, θ₂₃ maximal,
  δ_CP = 270°). **H4** (TM1 bevorzugt, TM2 χ² = 14,7).
- **H37** (Kopplung aus der Triality-Form, nur verschiedene Plätze, widerlegt). **r33** (A₄ als Slot-Symmetrie gesetzt).
- **r42/r43** (Projektor ½(1 + iL_e₇), Anomalie wählt Linksmultiplikation). **H125** (relatives CP-Vorzeichen: Leptonen det −1, Quarks det +1).
- **H126** (Kopplung zweier Richtungen, nicht prüfbar, k257). **k273** (Spin ½ gegen Spin 1, J·εε ab N = 3).
- Literatur (nicht neu): Die Tetraedergruppe hat ihr erstes nichttriviales Invariantes bei l = 3 (xyz), die Oktaedergruppe bei l = 4; A₄-Flavon-Modelle
  (Ma–Rajasekaran 2001, Altarelli–Feruglio 2005).

## Gegenstand und Konventionen
- H₃(𝕆) mit Jordan-Produkt, Koordinaten und Oktonionen wie k275. Metrik ist die Spurform ⟨X, Y⟩ = Tr(X∘Y). Alle Rechnungen in einer
  Orthonormalbasis dieser Form, damit ρ(R) orthogonal ist.
- C := L_e₇ je Platz (x_i ↦ e₇x_i auf den drei Oktonion-Einträgen, Diagonale 0), wie `slot_op` in k275.
- P_s: Projektor auf die Farbsinguletts (Diagonale, Re- und e₇-Anteile, 9 Dim., = H₃(ℂ) mit ℂ = span(1, e₇)); P_t: auf die Farbtripletts (e₁ … e₆, 18).
- Spin-Zerlegung eines Operators A: Casimir der adjungierten Wirkung A ↦ [T_a, A] der so(3) aus k275, Projektion auf die Eigenräume l(l+1).

## Vorab offengelegt (analytisch, kein Teil der Vorhersage)
Auf H₃(ℂ) gilt L_e₇ = R_e₇ (ℂ ist kommutativ). Die ungeraden Elemente von S₄ führen C dort also in −C über. Damit ist P_s C P_s **S₄-ungerade
und A₄-invariant**. Komponenten ungleich 0 sind nur bei l möglich, deren Einschränkung auf die Oktaedergruppe die Darstellung A₂ enthält, also
l ∈ {3, 6, 7, 9, 10, …}. Insbesondere ist die l = 0-Komponente 0, und das ist keine Vorhersage. Offen ist, ob l = 3 tatsächlich besetzt ist und
wie stark (P_s C P_s liegt in End(1 ⊕ 3 ⊕ 5), dort ist l ≤ 10).

## Stufe A: Spin-Inhalt der Brechung
A₀ := P_s C P_s, Komponenten A₀,l, Anteile w_l = ‖A₀,l‖² / ‖A₀‖².
**Vorhersage:** w₃ > 0, und die Spin-3-Komponente ist die führende (w₃ = max_l w_l).
- **Bestätigt:** w₃ ≥ 10⁻⁸ und w₃ ≥ w_l für alle l.
- **Teilweise:** w₃ ≥ 10⁻⁸, aber eine höhere Komponente (l ≥ 6) ist größer.
- **Widerlegt:** w₃ < 10⁻¹⁰ (die Brechung sitzt erst bei l ≥ 6).
- **Kontrolle:** w_l < 10⁻¹⁰ für alle l ∉ {3, 6, 7, 9, 10}, sonst Fehler in Rechnung oder k275. Wolfram exakt rechnet w_l unabhängig nach.

## Stufe B: Leckordnung in die Quarks
K(A) := Σ_a L_{Y_a} A L_{Y_a}, Y_a eine Orthonormalbasis der Spurform, L_Y die Jordan-Multiplikation. K vertauscht mit der Wirkung jedes
Automorphismus, also auch mit SO(3), und bringt deshalb keine eigene Brechung mit. A_n := K(A_{n−1}), C_eff⁽ⁿ⁾ := P_t A_n P_t (n = 1, 2, 3);
Kontrolle n = 0: P_t C P_t. Brechungsmaß b_n = max über 20 Zufalls-R ∈ SO(3) von ‖ρ(R) C_eff⁽ⁿ⁾ ρ(R)ᵀ − C_eff⁽ⁿ⁾‖ / ‖C_eff⁽ⁿ⁾‖ (b_n := 0, wenn
‖C_eff⁽ⁿ⁾‖ < 10⁻¹²). Leckordnung n_q := kleinstes n ≥ 1 mit b_n > 10⁻⁸.
**Vorhersage:** **n_q = 1** (eine Kopplung hin und zurück, zweite Ordnung in L_Y), und im SO(3)-brechenden Teil von C_eff⁽¹⁾ ist l = 3 die
führende Komponente.
- **Bestätigt:** b₀ < 10⁻¹⁰ (Kontrolle, k275), b₁ > 10⁻⁸, und unter den Komponenten l > 0 von C_eff⁽¹⁾ ist l = 3 die größte.
- **Teilweise:** n_q = 1, aber eine andere Komponente führt; oder n_q ∈ {2, 3}.
- **Widerlegt:** b_n < 10⁻¹⁰ für alle n ≤ 3. Das hieße, dass die Quarks die Familien-SO(3) auch effektiv exakt tragen. Das wäre ein eigener Befund,
  denn die CKM-Mischung müsste dann aus einer anderen Quelle kommen.

## Nicht Teil des Kriteriums (nachträgliche Einordnung, nicht blind)
Spurion-Lesart M_ij = m₀ δ_ij + ε t_ijk v_k mit t_ijk = |ε_ijk| und Flavon v (gesetzt, Literatur). Mischung ~ ε^Ordnung, ε aus θ₁₃. CKM und PMNS sind
bekannt, deshalb kommt das nur als Einordnung in die Ergebnis-Notiz.

## Grenzen
Vorausgesetzt bleiben: die drei Plätze sind Generationen (k275, offen); K als Kopplung. K ist die kanonische, ohne Zusatz F₄-äquivariante
Wahl aus Jordan-Multiplikationen, aber eine Wahl. Kein Guard berührt, OP3 bleibt offen.
