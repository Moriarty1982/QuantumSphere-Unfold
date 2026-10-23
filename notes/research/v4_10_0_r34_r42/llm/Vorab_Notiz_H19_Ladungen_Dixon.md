# Vorab-Notiz H19: Ladungen einer Generation aus der Dixon-Ablage

Festgelegt am 2026-10-23, **vor** der Rechnung. Bezug: Bestandsaufnahme K79 (Test 1), K77 (Dixon-Ablage), `thm:octonion-SU3`,
`thm:three-generations`, `thm:SM`; Literatur: C. Furey, „Charge quantization from a number operator“ (Phys. Lett. B, 2015).

## Rahmen (verbindlich)

- Oktonionen nach der Cayley–Dickson-Formel von `k22_oktonion_triplett.py`. L_a = Linksmultiplikation mit e_a (reelle 8×8-Matrix).
  Die L_a erfüllen L_aL_b + L_bL_a = −2δ_ab und erzeugen auf ℂ⊗𝕆 ≅ ℂ⁸ die Algebra ℂℓ(6).
- Komplexe Einheit i = der ℂ-Faktor der Dixon-Ablage (Index a), vertauscht mit allen L_a.
- Farbe wie im Companion: SU(3) = Stabilisator von e₇ in G₂ = Aut(𝕆), wirkend durch g·ψ. Vorab geprüfte Konvention (kein
  Ergebnis): e₇·e₄ = −e₃, e₇·e₅ = −e₂, e₇·e₆ = +e₁, also ist ℂ³ = span(e₄, e₅, e₆) mit e₇ als komplexer Struktur auf e₇^⊥.
- Leiteroperatoren für die drei Farbrichtungen a ∈ {4, 5, 6}: α_a = ½(L_{e_a} + i·L_{e₇e_a}). Zahloperator N = Σ α_a†α_a,
  Ladung Q = N/3.
- Frame-Abbildungen auf dem ℂ-Faktor wie in K77.8 (v4.9.0-r30.2(b)): T (z ↦ z̄), R (z ↦ iz), J_B = R ∘ T.

## Offenlegung (Vorüberlegung vor der Notiz, nur analytisch)

- Aus α_a² = 0 und {α_a, α_b†} = δ_ab (folgt aus den Clifford-Relationen) ist N ein Fock-Zahloperator mit drei Moden. Die
  Eigenwerte 0, 1, 2, 3 mit Vielfachheiten 1, 3, 3, 1, also Q ∈ {0, 1/3, 2/3, 1}, sind damit **algebraisch erzwungen und
  keine Vorhersage**.
- Nicht erzwungen und damit riskant ist, ob die Farbgruppe des Companion (Stab(e₇) ⊂ G₂) mit Q vertauscht und die
  Ladungssektoren als Farb-Singuletts bzw. -Tripletts trägt. In der Literatur gilt das für Fureys Konvention; ob es für die
  Konvention des Companion gilt, ist hier der Test.
- Erwartung zur wörtlichen Zuordnung des Companion: Die Ladungs-Eigenzustände sind komplexe Kombinationen e_a ± i·e₇e_a, die
  e₄, e₅, e₆ mit e₁, e₂, e₃ mischen. Der *reelle* Spann von e₄, e₅, e₆ ist dann kein Ladungs-Eigenraum.
- Erwartung zu den Frames: T macht aus α_a etwa −α_a†, also N ↦ 3 − N und Q ↦ 1 − Q (ladungskonjugiertes Multiplett). R ist
  komplex-linear und lässt Q fest. J_B = R ∘ T gäbe dann Q ↦ 1 − Q. Das ist nicht gerechnet.

## Hypothesen (V)

- **H19a (Verträglichkeit):** Jedes Element von Stab(e₇) ⊂ G₂ vertauscht mit Q (geprüft an einer Basis der Lie-Algebra und an
  zufälligen Gruppenelementen).
- **H19b (Sektoren):** Q = 0 und Q = 1 sind Farb-Singuletts in span_ℂ(1, e₇); Q = 1/3 und Q = 2/3 sind Farb-Tripletts in
  span_ℂ(e₁, …, e₆), und zwar zueinander konjugierte Darstellungen von Stab(e₇).
- **H19c (wörtliche Companion-Zuordnung):** Der reelle Spann von e₄, e₅, e₆ (`thm:octonion-SU3`, `thm:three-generations`) ist
  ein Ladungs-Eigenraum, und e₇ allein ist ein Ladungs-Eigenzustand (Zuordnung e₇ ↔ ν_R).
- **H19d (Frames):** Unter J_B gilt Q ↦ 1 − Q; unter T ebenso; unter R bleibt Q fest.
- **H19e (Generationen):** In der Ablage (Im ℍ)⊗ℂ⊗𝕆 (K77.3) ist Q auf allen drei Plätzen gleich (Ladungsuniversalität).

## Verfahren (verbindlich)

Numerisch mit exakter Ganzzahl- bzw. Matrixrechnung (Toleranz 10⁻¹² für Vertauschung und Eigenwerte). Stab(e₇):
Derivationen von 𝕆 (Lösungsraum der linearen Bedingung D(xy) = D(x)y + xD(y), Dimension 14), davon die mit D(e₇) = 0
(erwartet Dimension 8), dazu Exponentiale zufälliger Elemente. T, R, J_B auf ℂ⊗𝕆 als reelle 16×16-Matrizen.
Q ↦ 1 − Q heißt: W Q W⁻¹ = 1 − Q.

## Entscheidungskriterium (verbindlich)

- H19a **bestätigt**, wenn alle geprüften Elemente mit Q vertauschen; sonst **widerlegt** (dann passen Farbe und Ladung in der
  Konvention des Companion nicht zusammen).
- H19b **bestätigt**, wenn alle vier Sektoren wie angegeben liegen und sich wie angegeben transformieren; sonst **widerlegt**.
- H19c, H19d, H19e: jeweils bestätigt oder widerlegt nach der wörtlichen Aussage.

Einordnung vorab: H19a und H19b wären eine Konsistenzprüfung gegen ein bekanntes Ergebnis, keine Vorhersage über die Natur.
Eine Widerlegung wäre dagegen aussagekräftig.

Offene Frage, kein Teil des Tests (Autorhinweis): `thm:SM` könnte nur in einem Frame entwickelt sein. Der Satz nennt das U(1)
„Elektromagnetismus“ (gebrochene Phase) und lässt SU(2) ungebrochen (symmetrische Phase).

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
