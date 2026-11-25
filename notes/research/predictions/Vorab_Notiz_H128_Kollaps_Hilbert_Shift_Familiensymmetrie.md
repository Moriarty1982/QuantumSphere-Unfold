# Vorab-Notiz H128: Erzeugt der Strukturverlust beim Hilbert-Shift HS(4) die Familiensymmetrie und ihre Brechung?

**Stand:** 2026-11-25, vor der Rechnung festgelegt. **Teilweise nicht blind** (die analytisch feststehenden Teile stehen unten unter
„Vorab offengelegt“ und sind kein Teil der Vorhersage). Anlass: Autor, 25.11.2026, 09:41 UTC: „das dürfte wahrscheinlich der hilbershift sein,
der könnte paradoxerweise mehr dimensionen schaffen aber dabei ein kollabs der internen struktruk sein aus dem sich dann die symetriegruppen
ergeben“, und 09:44 UTC: „rechne das mal parallel“. Skripte ab **k283** (Python numpy; Wolfram Language exakt zur Kontrolle der Massenform).
Qiskit nicht vorgesehen (keine Schaltung, keine Messung). Bezug OP3 (#131), Thesen T5/T7 im Gesamtbild (Zuordnung der Generationen bleibt Vermutung).

## Vorwissen geprüft
- **k253** (#279): Cayley–Dickson-Turm A_n als Regel für HS(n); dim Der(A_n) = 0, 0, 3, 14, 14, 14.
- **k254** (#280): Ab 𝕊 = A₄ brechen Alternativität, Moufang und Normmultiplikativität; Aut(𝕊) = G₂ × S₃; 𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2); Nullteiler als Lecks.
- **k275** (#290): H₃(𝕆), Der = f₄ (52); Kommutant von su(3)_c ist su(3)′ (8), Kommutant von g₂ ist die Familien-so(3) (X ↦ RXRᵀ); Rest unter der Ladung A₄.
- **k281** (#294): Ein Feld im spurfreien Teil von H₃(ℂ) hat ein SU(3)-invariantes Potential, keine Restgruppe. Gebraucht wird ein Term, der unter
  SO(3) invariant ist, aber nicht unter SU(3), am einfachsten μ₁² ≠ μ₂² für Spin 1 und Spin 2.
- **k282** (Nachbarfaden, 25.11., noch nicht im Repo): setzt die Terme Tr(W∘σW) und Tr((CW)∘(CW)) von Hand und tabelliert die Restgruppe je Vorzeichen.
  Diese Tabelle lag vor dieser Notiz fest; ich habe sie vor der Rechnung nicht gelesen. Offen blieb dort, ob der Turm die Vorzeichen festlegt.
- `op3_dixon_times_sedenions_2026_11_16/`, `op3_dixon_copies_2026_11_16/`: Sedenionen als Träger, keine Albert-Algebra über 𝕊.
- Im Repo gibt es **keine** Rechnung zu H₃(𝕊) (Suche nach „Albert“ zusammen mit „Sedenion“, 25.11.). Literatur zu Der(H₃(𝕊)) ist mir nicht bekannt
  (aus Vorwissen, ungeprüft).

## Aufbau
- H₃(A_n): hermitesche 3×3-Matrizen über A_n (n = 0 … 5, also ℝ, ℂ, ℍ, 𝕆, 𝕊, A₅), Produkt X∘Y = ½(XY + YX), Dimension 3 + 3·2ⁿ = 6, 9, 15, 27, 51, 99.
  Cayley–Dickson-Konvention wie k253. Spurform ⟨X, Y⟩ = Re Tr(X∘Y), Orthonormalbasis Φ_b dieser Form.
- **Der(H₃(A_n))** als Nullraum der Bedingung D(X∘Y) = DX∘Y + X∘DY (numerisch, Singulärwerte; danach Probe auf allen Basispaaren).
- **Feld:** W spurfrei in H₃(ℂ_u), ℂ_u = span(1, u). Spin-2-Teil: reell symmetrisch spurfrei (Einheitsvektor S). Spin-1-Teil: u·(reell antisymmetrisch) (Einheitsvektor V).
- **Massenform** (die kanonische quadratische Form, die die *ganze* Algebra und nicht nur H₃(ℂ_u) sieht):
  K(W) = Σ_b ‖[L_{Φ_b}, L_W]‖²_F, L_X die Multiplikation mit X auf H₃(A_n). K ist unter Aut(H₃(A_n)) invariant.
  Verhältnis **r_n(u) = K(V)/K(S)**, also μ₁²/μ₂² dieser Form.
- Richtungen bei n = 4: u = e₇ (Ladungsrichtung aus r42, in der ersten Oktonion-Hälfte) und u = e₈ (Verdopplungseinheit, die G₂-neutrale Richtung von 𝕊).

## Vorab offengelegt (analytisch, kein Teil der Vorhersage)
1. Für jedes n sind X ↦ [A, X] mit A reell antisymmetrisch und die eintragsweise Wirkung von Der(A_n) Derivationen von H₃(A_n). Also dim Der(H₃(A_n)) ≥ 3 + dim Der(A_n);
   für n = 4, 5 heißt das **≥ 17**. Die Familien-SO(3) kann durch keinen Turmschritt gebrochen werden. **SO(3) → A₄ kann der Turm allein deshalb nicht liefern**; dafür
   bleibt die Ladung (k275).
2. Für n ≤ 3 ist dim Der = 3, 8, 21, 52 (Literatur). Für n = 3 ist der spurfreie Teil unter F₄ irreduzibel, also r₃ = 1.
3. Für eine kanonische Einheit u gilt auch in 𝕊: u(ux) = −x, (ux)u = u(xu), und xu = −ux für x ⊥ 1, u. Damit ist die Wirkung von L_W (W ∈ H₃(ℂ_u)) auf H₃(𝕊) dieselbe
   Modulstruktur wie in H₃(𝕆), nur mit 7 statt 3 Kopien. **Tr(L_W^k) bleibt deshalb SU(3)-invariant** (insbesondere Verhältnis 1 für k = 2). Das ist Kontrolle, keine Vorhersage.
4. K ist SO(3)-invariant, und Spin 1 und Spin 2 sind verschiedene irreduzible Darstellungen. Also K(W) = μ₂²|s|² + μ₁²|v|² ohne Mischterm.

## Hypothesen und Kriterien
- **H128a (Kollaps auf genau die Familiensymmetrie):** dim Der(H₃(𝕊)) = **17**, also g₂ ⊕ so(3): Von den 52 Dimensionen der f₄ überlebt beim Schritt 𝕆 → 𝕊 neben g₂
  nur die Familien-so(3) aus k275.
  - **Bestätigt:** Nullraum genau 17-dimensional (Singulärwertlücke ≥ 10⁶), und jede Derivation ist Summe aus g₂-Anteil und reeller Drehung (Rest < 10⁻⁹).
  - **Widerlegt:** Dimension > 17. (Dimension < 17 wäre ein Rechenfehler, siehe Offenlegung 1.)
- **H128b (der Kollaps trennt Spin 1 und Spin 2):** r₄(u) ≠ 1.
  - **Bestätigt für u:** |r₄(u) − 1| > 10⁻⁶. **Widerlegt für u:** |r₄(u) − 1| < 10⁻⁹. Entschieden wird getrennt für u = e₇ und u = e₈.
  - Das Vorzeichen von r₄ − 1 wird berichtet und erst **nach** der Rechnung gegen die Tabelle aus k282 gelesen.
- **Kontrollen:** (i) n = 0 … 3: dim Der = 3, 8, 21, 52. (ii) |r₃ − 1| < 10⁻¹¹. (iii) n = 4, u = e₇, e₈: Verhältnis von Tr(L_W²) zwischen V und S weicht um < 10⁻¹¹ von 1 ab.
  (iv) Mischterm K(S, V) und Abhängigkeit von K von der Wahl von S bzw. V innerhalb des Spin-Raums < 10⁻¹¹ (relativ). (v) Wolfram exakt rechnet r₃ und r₄ unabhängig nach.
  Schlägt eine Kontrolle fehl, ist der Lauf ungültig.

## Erkundung daneben (ohne Kriterium, als Erkundung geführt)
dim Der(H₃(A₅)) (erwartet 17), r₄ für eine schiefe Einheit u = (e₁ + e₁₀)/√2 (Nullteiler-Richtung), r₅, und die Zahl der Würfeldrehungen, die in H₃(𝕊) mit der Ladung
je Platz vertauschen (erwartet 12 wie in k275).

## Folge, vorab festgelegt
- **a und b bestätigt:** Die Idee des Autors trägt für den Schritt SU(3) → SO(3): Der Strukturverlust bei HS(4) lässt von der Symmetrie der Albert-Algebra genau G₂ und die
  Familien-SO(3) übrig, und er erzeugt den Massenunterschied, den k281 verlangt und k282 von Hand setzt. Das Vorzeichen wird dann zur Eingabe für die Tabelle aus k282.
  Es folgt **nicht**, dass die drei Plätze Generationen sind, dass H₃(𝕊) im Turm entsteht (es ist eine Konstruktion auf drei Kopien) oder dass K das physikalische
  Potential ist; K ist eine gesetzte, wenn auch kanonische Form.
- **a bestätigt, b widerlegt:** Die Symmetrie der ganzen Algebra kollabiert, aber das neutrale Feld merkt es in zweiter Ordnung nicht; die SU(3) ist dort zufällig. Offen
  bliebe dann eine höhere Ordnung.
- **a widerlegt:** Es überlebt mehr als die Familiensymmetrie; die zusätzlichen Derivationen werden bestimmt, die Lesart „Kollaps gibt die Gruppe“ gilt dann nicht in dieser Form.
- In jedem Fall: SO(3) → A₄ kommt nicht aus dem Turm (Offenlegung 1). OP3/OP4 bleiben offen, kein Guard wird berührt.
