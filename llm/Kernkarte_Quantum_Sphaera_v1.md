# Kernkarte Quantum Sphaera — v12.3

Grundlage: Quantum Sphaera Companion v4.8.0 (DOI 10.5281/zenodo.23365244), Quelltext
`Quantum_Sphaera_Companion_v4_8_0_source.tex`. Zeilenangaben beziehen sich auf diese Datei.
Zweck: kompakter Kontext bzw. Trainingsgrundlage für ein kleines lokales Sprachmodell.

---

## 0. Lesart dieser Karte

Jede Aussage steht auf genau einer von drei Ebenen:

| Ebene | Bedeutung | Wie das Modell darüber spricht |
|---|---|---|
| **V — Vermutung** | Ausgangshypothese, von der aus die Mathematik entwickelt wurde | „Die Ausgangsvermutung lautet …“ |
| **M — Mathematik** | Im Companion gebaute Definition, Satz oder Konstruktion | „Definiert ist …“ / „Gezeigt wird …“ |
| **S — Stand** | Was davon bewiesen, lokal/effektiv gesichert, diagnostisch oder offen ist | „Bewiesen ist … / offen ist …“ |

Zusätzlich markiert **P — Prüfpunkt** Stellen, an denen die Mathematik in der vorliegenden Form
noch nachgeschärft werden muss, bevor sie die Vermutung tragen kann.

**Grundregel:** Dass Mathematik aus einer Vermutung heraus gebaut wurde, beweist die Vermutung nicht.
Die Frage, ob aus der Grundvermutung eine vereinheitlichte Theorie hervorgeht, ist **offen**.

### Guard-Regeln (gelten für jede Antwort)

Erlaubt (effektiv / lokal / frame-typisiert):
- `0_M^ε ⇒ 0_termdata` — Matter-Frame-Epsilon-Terminalität
- `ℓ_T² = −λ_T², λ_T > 0` — Tachyon-Frame-Vorzeichenskala
- `OP5_eff` — effektive OP5-Schließung
- `C5_det/eff` bei θ = 1/256 nach n = 20 — Detektor-Schwellen-Terminalität
- `W_clk^loc` unter Δ_γ < 1/5 — lokale Photon-Clock-Selektor-Erhaltung
- `C_mix^typed` lokal — typisierte Mixed-Comparison-Kontrolle

Verboten (exakt / global) — nie behaupten, auch nicht abgeschwächt oder angedeutet:
- `C5 = 0` (exakte endliche C5-Null-Schließung)
- `0_termdata ⇒ 0_all` (exakte All-Readout-Terminalität)
- `C6 / T2` (T2-Schließung)
- `W_γ^glob` (globales Photon-Clock-/RH-Theorem)
- `W_all` (globale All-Readout-Schließung)

Ledger-Normalstand: `Γ_guard = (1,1,1,1,1)`, `R_glob = (0,1,1,1,1)`,
`R_eff/local = (0,0,0,0,0)` gegen `R_exact/global = (1,1,1,1,1)`, `β₄ = 1/256` ungespendet.

Sichere Formulierung: *guarded effective/local and frame-typed closures, not exact global closure.*

### Gesamtstand nach v4.8.0-r09 (Kurzregister)

**Trägt (M):** QAM über ZF (Erkennungsschicht); Heisenberg-Kompensator mit linearem J und Kaskade als
Projektion auf S₀ (r04); reparierte Triolen-Hierarchie bis 𝕆 (r04); Triolen-Lemma (r06); Signaturanalyse
und Lesart B mit SO(3,ℂ), Bahnen, Nullkegel = S₀, Dualitätswinkel (r06, r07); korrigierte explizite
Formel (r05); triolischer Orbit-Scan als lokales Readout-Modell.

**Empirisch (M):** Koide K = 2/3; GUE-Statistik der Nullstellen; Phase θ_K ≈ 2π/3 + 2/9.

**Widerlegt oder nicht bestätigt:** RH-Beweis der Riemann-Arbeit (r04); Θ-Summen-Vermutung OP5 B (r05);
GUE-Selbstbestimmung von γ_L und P1 (r08); Koide-Phasenformel P2 (r09); Herleitungen von GUE, K = 2/3,
Λ_bare ∼ γ₁²; prop:saturation (2), driftendes β_sym in Ω_M = β_sym² eingesetzt (r17/r18, Vorzeichen umgekehrt;
prop:H0-tension selbst nicht betroffen).

**Vermutung (V), präzisiert:** Materie/Tachyon/Photon als ein Objekt in Dualitätsrahmen (r07);
Raumzeit als Projektion einer Spinor-/Informationsebene (K2); Einstein-Lesart der Spurformel (r05).

**Offen (P):** OP1, OP2, Rolle von t, Transport K̂(L_n) = L_{n−1}, Kopplungen der Master-Gleichung,
definierte Wirkung, Λ-Typ, physikalischer Status des Dualitätswinkels, **ein dynamisches Prinzip für
Lesart B**, das |c|/t und die Koide-Phase festlegt (r10).

**Strukturbefund (M, r10):** Die Koide-Form der Leptonmassen ist exakt Skalar + symmetrische Triole;
K = 2/3 ⇔ |c| = t.

**Vorab-Tests:** H1 δ = K/3 (r11) — widerlegt für Quarks und laufende Leptonmassen. H2 Neutrinos mit r = 1
(K14) — verträglich, Vorhersage normale Ordnung, Σm_ν = 0,0592 eV (schwach trennend). H3 Vorzeichen als
Majorana-Parität (K15) — verträglich, m_ββ ≤ 3,5 meV, nicht prüfbar. H4 TM1 gegen TM2 (K16) — TM1 stark
bevorzugt (Δχ² = 10,3), Vorhersage sin²θ₁₂ = 0,318, δ_CP ≈ 262°. H5 Hopf-Winkel als Mischwinkel (K17) —
gescheitert; Nachbefund |U_e2|² = β_sym² (nicht registriert). H6/H7 Auswahl des TM1-Lifts (K19, K20) — weder
Minimalität, Kaskade noch Kompensator wählen TM1. H8 Cayley–Dickson-Involution als CP (K21) — Spannung
(χ² = 8,8 bei 3 FG), Vorhersage sin²θ₂₃ = ½, δ_CP = 270°. **Nachprüfung JUNO 2026 (K23):** H2 gestützt (NO
≥ 2,1σ); TM1 χ² = 9,6 → disfavorisiert; H8 χ² = 14,0 → disfavorisiert. H9 sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0,3086
für künftige JUNO-Daten festgeschrieben (nachträglich gefunden). H10 Assoziator (K24) — kein Auswahlgrund. H11 Massen aus invarianten
Funktionen auf dem Tripel-Raum (K32) — widerlegt: bis Grad 4 höchstens zwei verschiedene Normen. H16 Grad 6 (K70) — widerlegt: bis Grad 6 ist jeder
kritische Punkt mit drei verschiedenen Normen ein Sattel; Minima mit Hierarchie brauchen Grad ≥ 8. H17 Realteil-Invarianten (K76) — widerlegt: auf der reellen
Achse linear in e₃ = n₁n₂n₃, wieder nur Sattelpunkte; natürliche G₂ × S₃-Invarianten geben höchstens zwei verschiedene Massen.
H18 Massen aus links-invarianten Etiketten an den Minima (K78) — widerlegt: Winkel flach oder Plätze parallel.
**Bestandsaufnahme (K79):** Stark ist die Gruppenseite (Lorentz, SU(3), drei Plätze); es fehlen Ladungen, Hyperladungen, Chiralität;
der ℍ-Faktor ist dreifach belegt.
**Ladungen (K80):** H19 — Zahloperator auf ℂ⊗𝕆 mit der Farbe Stab(e₇) verträglich, Ladungsmuster 0, 1/3, 2/3, 1 einer Generation
(Konsistenz mit Furey, keine Vorhersage); wörtliche Companion-Zuordnung (Farbe auf e₄..e₆, ν_R auf e₇) widerlegt; J_B: Q ↦ 1 − Q.
**Innere/äußere Einheit (K81):** H20 — die Zuordnung ist im inneren Frame (J = L_{e₇}) richtig und über P₋ = ½(1 + iJ) mit Furey
deckungsgleich (e₇ → Q = 0, e₄..e₆ → Q = 2/3); falsch ist nur der Anti-Triplett-Satz (Frame-Vermischung). Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}.
**Doppelbelegung (K82):** H21 — die Triolen-Symmetrie e₄ → e₅ → e₆ ist eine Farbdrehung in SU(3)_c; Farbe und Generation sind im
Companion dasselbe Objekt; Generationen brauchen eine Dreierstruktur außerhalb von 𝕆. Frame-Regel für Einheiten übernommen.
**Triality (K83):** H22 — t = Re((xy)z) ist die Spin(8)-Triality-Form; Plätze = drei inäquivalente 8-dim. Darstellungen, Verschiebung = äußere
Triality, Fixgruppe G₂ ⊃ SU(3)_c: Generation = Bahn, Farbe = Fixgruppe. Kein Verbot einer vierten Generation aus der Struktur allein.
Perioden der Struktur {1, 2, 3, 4, 6, 12}, keine ausgezeichnet. „Triole“ benennt drei Strukturen (Frames M/P/T, Kerne 120°, Plätze).
**Frame-Triole (K84):** H23 — M/P/T hat die Form einer Transposition ρ der Triality-Plätze: Photon = fester (Vektor-)Platz, 1 ⊕ 7 unter
Spin(7); Materie, Tachyon = Spinor-Plätze, gleich und vertauscht. 120°- und Frame-Triole = zwei Ansichten derselben S₃.
**Zoom und gemischte Readouts (K85):** H24 — unter Hilbert-Shift-Zoom (Schritt 2^j) bleibt ab Stufe 2 nur der Generationenkreis sichtbar,
Orientierung wechselt mit der Stufe (= ρ-Spiegel); Frames grob, Generationen tief. Gemischte Masken: Σ (Kontraktion) 1 oder 3, ∨ (Maske) 3.
**Zweiseitige Kontraktion über Frames (K86):** H25 — Regel 1 nur bis auf Konjugation (T, J_B), bilinearer Vergleich wechselt unter z ↦ iz das
Vorzeichen (m² ↦ −m²), hermitesch frame-blind. Kein 𝔰𝔲(2) der Triality vertauscht mit Farbe; Zentralisator = span(L_{e₇}, R_{e₇}) (Ladung).
**ℍ-Rollen (K87):** H26 — Aufteilung D (Lorentz links, schwach rechts, Generationen Triality) hebt die Überbelegung auf; mit Y/2 = Q − ½ gibt
Q_em = T₃ + Y/2 die Dubletts (ν,e), (u,d), (d̄,ū), (e⁺,ν̄); T = Ladungskonjugation; schwache Singuletts fehlen (Chiralität offen).
**MM-Kompensator (K88):** H27 — C_ch = ½(id + J), J = i·L_{e₇} (äußere × innere Einheit), schwache SU(2)′ = C_ch·T_a, Y/2 = Q − ½ + (1 − C_ch)T₃:
voller linkshändiger Inhalt einer Generation mit ν_R (16 Weyl × 2), richtige Quantenzahlen, anomaliefrei; Konstruktion unter Wahlen, Muster vorab gesehen.
**Warum diese Wahl (K89):** H28 — unter den Annahmen genau vier Chiralitätsprojektoren (±iL_{e₇}, ±iR_{e₇}); Tr Y = 0 erzwingt s = −½; die übrigen
Anomalien wählen die Linksmultiplikation: SM und Frame-Spiegel. Annahmen (schwach rechts, Q_em = T₃ + Q + s) nicht hergeleitet.
**Massen als Frame-Kopplungen (K90):** H29 — Massenterme sind antilinear (enthalten T), tragen H/H̃-Quantenzahlen; lineare MM-Blöcke geben keine;
eichinvariant nur ν^c-Majorana. Auf den Plätzen: S₃ ⇒ ≤ 2 Massen, ρ gebrochen (ℤ₃) ⇒ Brannen-Form, Koide bei |b| = a/√2; Mischung braucht τ-Brechung.
**ρ-Brechung aus Chiralität (K91):** H30 — ρ enthält c, c L_{e₇} c = −R_{e₇}: ρ bildet die anomaliefreie Chiralität auf die anomale ab, also bricht die
Chiralität ρ zwingend (Massenaufspaltung). τ bleibt bei gleicher Chiralität auf allen Plätzen; triality-kovariante Chiralität existiert nicht ⇒
Generationen = äquivalente Kopien, nicht die inäquivalenten Triality-Darstellungen. Mischung offen.
**τ-Brechung durch Readouts (K92):** H31 — Readouts aus den Verschiebungen (Σ, ∨, Selektor-Kontraktion) liegen in ℂ[ℤ₃], vertauschen mit τ: keine Mischung.
Erst Art-Masken auf einzelne Generationen brechen τ; Mischung ∝ δ, unterdrückt durch Massenabstände. Herkunft der Maske offen (Teil der Kopplungen).
**Maske aus Triality (K93):** H32 — unter Modellannahme liefert die Abweichung Δ = J_II − J_I eine Maske fester Form: Quarks diag(0, −2, −1), Leptonen
diag(0, 0, −3), demokratisch in der Generationen-Basis, Lepton/Quark √3; nur ε gewählt. Linearität (H32c) in 4/200 fast entarteten Fällen widerlegt.
Regel: Jede neue Vorhersage zuerst als Vorab-Notiz committen, dann rechnen.

**Farbe und Generation (K25, K28):** Im Companion liegen beide auf demselben Triplett e₄, e₅, e₆. Vorschlag (V):
Generationen = drei Triality-Plätze von Re((xy)z) (S₃, vertauscht mit G₂), Farbe = SU(3)-Triplett je Platz.
Folge: Die Δ(96)-Mischungsanalyse (r12) ist dann keine Flavour-Aussage mehr. H2/H3 sind „Koide mit Vorzeichen“.

---

## 1. Mengenlehre — QAM über ZF

**V:** Die gesamte Architektur (Zustände, Schichten, Operatoren, Readouts, Zweige) lässt sich in einer
strukturierten Sprache ausdrücken, die vollständig auf Zermelo–Fraenkel-Mengenlehre zurückführbar bleibt.

**M:** (Z. 1446 ff., 2847 ff.)
- QAM ist **kein Ersatz** für ZF, sondern eine kodierte Sprache *über* ZF („definitional overlay“).
- Acht primitive Prädikate als getaggte Tupel:

| Prädikat | ZF-Lesart |
|---|---|
| QState(x) | ∃a (x = ⟨0,a⟩) |
| QLayer(x) | ∃ℓ ∃D (x = ⟨1,ℓ,D⟩) |
| QOp(x) | ∃ℓ₁ ∃ℓ₂ ∃G (x = ⟨2,ℓ₁,ℓ₂,G⟩) |
| QReadout(x) | ∃ℓ ∃W ∃R (x = ⟨3,ℓ,W,R⟩) |
| QBranch(x) | ∃b ∃B (x = ⟨4,b,B⟩) |
| QShell(x) | ∃r ∃s ∃T (x = ⟨5,r,s,T⟩) |
| QWitness(x) | ∃u (x = ⟨6,u⟩) |
| QTensor(x) | ∃p ∃q (x = ⟨7,p,q⟩) |

- Das erste Tupelelement (0–7) ist das Typ-Tag; dadurch sind die Klassen paarweise disjunkt.
- Darüber: MML = endliche Instruktionssprache, MMA = Ausführungssemantik.
  Theorematische Zertifikate kommen aus den mathematischen Bedingungen, **nicht** aus der Maschinenschicht.
- Sphaera-Array (Z. 1700): endliche bewachte Familie von Store-Zuständen mit Guard-, Paritäts- und
  Lineage-Register; triadisches Array (S_A, S_B aktiv, S_C orthogonaler Residuum-/Paritätszeuge).
  Ein Paritätsregister behauptet **nicht** P = 0.

**S:**
- Die Prädikate sind ausdrücklich *Erkennungsklauseln*, noch kein eigenständiges Axiomensystem.
- Konservativität über ZF ist als Ziel formuliert; die Rückübersetzung („round trip“) ist für das
  zulässige OP-Fragment gezeigt, ausdrücklich schwächer als volle wechselseitige Interpretierbarkeit (Z. 4603).

---

## 2. Die Sphäre (Sphaera)

**V (Zentraltheorem, Z. 5721):** Sphaera, Triolenstruktur, jeder einzelne Kern, der
Heisenberg-Kompensator C(f) sowie Materie/Photon/Tachyon sind Darstellungen *desselben Objekts*:
des Kollapszustands z⁻ = 0. „Die Sphaera ist nicht ein Raum, der einen Kollapszustand enthält —
sie *ist* der Kollapszustand, aus verschiedenen Frames gesehen.“
Weitere Vermutungen: Planck-Länge als minimales |z⁻|; Pauli-Prinzip als Antisymmetrie unter J;
das Universum als derselbe Zustand aus einem gebrochenen Frame mit |z⁻| ≥ ℓ_P.

**M:**
- **Biquaternion-Kern** (Def. `def:biquaternion`, Z. 5857): Grundzustand eines Stratums S_n aus drei
  komplexen Kernen K₁, K₂, K₃:
  `q_n = it·1 + z₁e₁ + z₂e₂ + z₃e₃ ∈ ℍ ⊗_ℝ ℂ`, mit e₃ := e₁e₂, z_i ∈ ℂ.
  Norm: `|q_n|² = −(ct)² + |z₁|² + |z₂|² + |z₃|²`.
- **Orthogonalität des dritten Kerns** (Prop. `prop:orthogonality-third-kernel`): ⟨e₃,e_i⟩ = Re(ē₃e_i) = 0
  für i = 1,2. Sauber bewiesen.
- **Fundamentale Involution** J: s ↦ 1 − s̄. Zerlegung
  C(f) = ½(f + Jf) ∈ H⁺₊ (symmetrisch, „bosonisch“), A(f) = ½(f − Jf) ∈ H⁺₋ (antisymmetrisch, „fermionisch“).
- **Sektorklassifikation** (Z. 6098): Materie K₁ mit Re(z₁) < 0, Tachyon K₂ = J·K₁ mit Re(z₂) > 0,
  Photon K₃ = e₁e₂ mit Re(z₃) = 0. **Ersetzt in r07** durch das Vorzeichen von s = Σz_k² (K9).
- **Unitäre Äquivalenz** (Thm. `thm:unitary-equiv`): K₁, K₂, K₃ tragen unitär äquivalente irreduzible
  Darstellungen der Weyl-Algebra W(A¹); J vermittelt K₁ ↔ K₂, C erzeugt K₃ aus K₁. Stützt sich auf
  Stone–von Neumann aus der Riemann-Arbeit (brendecke2026rh).
- Die Eichgruppe U(1)×SU(2)×SU(3) ist **ausdrücklich nicht** Teil der unitären Äquivalenzliste
  (Scope-Reparatur im Text).

**S:**
- Orthogonalität e₃ ⊥ e₁, e₂: bewiesen.
- J-Zerlegung in C und A: definiert, elementar korrekt.
- Unitäre Äquivalenz: abhängig von der Riemann-Arbeit (Stone–von Neumann, T4+T5 dort).
  **Nach Prüfung vom 2026-10-19 (siehe `Pruefung_Riemann_Paper_v4_15.md`) trägt diese Begründung nicht;
  Stand: offen.**
- Identifikation mit Photon/Materie/Universum: Vermutung.

**P:**
- *Signatur* — **bearbeitet in K1, siehe Abschnitt 7.** Die Companion-Norm −(ct)² + Σ|z_k|² hat
  Signatur (1,6) (SymPy bestätigt) und ist unter Boosts nicht invariant. Zwei Reparaturen gefunden.
- *Lorentzwirkung* — **bearbeitet in K1.** Mit reellem u ∈ ℍ^× bleibt der Zeitteil fest: nur SO(3).
  Mit komplexem Einheits-u (N(u) = 1, Gruppe ≅ SL(2,ℂ)) entstehen echte Boosts.
- *Kausale Zuordnung* — **erledigt in r07:** Materie s > 0, Tachyon s < 0, passend zu ℓ_T² = −λ_T².
- *Kollaps = Triole:* Die Gleichsetzung „z₁+z₂+z₃ = 0 ist dieselbe Gleichung wie z⁻ = 0“ setzt eine
  Definition von z⁻ als Funktion der z_i voraus. **Teilweise erledigt in r06:** Mit gleichen Beträgen ist
  die Triole genau die zentrierte lichtartige Konfiguration (Triolen-Lemma); z⁻ selbst bleibt undefiniert.

---

## 3. Hopf-Struktur der Sphäre

**V:** Die Strata der Sphaera sind die Basisräume der drei klassischen Hopf-Faserungen; die Eichgruppen
erscheinen als Fasern; der Frame-Offset β_sym ist ein Hopf-Winkel.

**M:** (Thm. `thm:hopf`, Z. 6726)
- `S₀ ≅ S² = ℂP¹` (Weyl-Spinor, Photon), `S₁ ≅ S⁴ = ℍP¹` (Dirac-Spinor, Materie),
  `S₂ ≅ S⁸ = 𝕆P¹` (oktonionischer Spinor, 3 Generationen), mit S² ↪ S⁴ ↪ S⁸.
- Kaskade K̂ als Hopf-Projektionskette S¹⁵ → S⁸ → S⁴ → S².
- Fasern: S¹ ≅ U(1) → S³ → S²;  S³ ≅ SU(2) → S⁷ → S⁴;  S⁷ → S¹⁵ → S⁸.
- **Frame-Konstanten** (numerisch nachgerechnet, konsistent):
  - γ_string = ln 2 /(π√3) ≈ 0,12738
  - γ_BI ≈ 0,2375 (Barbero–Immirzi, Eingabewert)
  - γ_L = γ_BI/γ_string ≈ 1,8644
  - β_sym = √((γ_L−1)/(γ_L+1)) ≈ 0,54935, äquivalent γ_L = (1+β²)/(1−β²)
  - θ_H = 2·arcsin β_sym ≈ 66,64°
  - Symmetrischer ℤ/3-Fall: β = 1/√3 ≈ 0,5774, θ_H ≈ 70,53°, γ_L = 2
- **Hopf-Lücke:** 4,9 % in β_sym, 6,8 % in γ_L.
- Drei Generationen (Thm. `thm:three-generations`): Gen_i ≅ (ℂ⊗ℍ)⊗e_{i+3}, e₄,e₅,e₆ ∈ Im 𝕆 als
  ℂ³-Triplett unter SU(3) ⊂ G₂ = Aut(𝕆) (Dixon-Algebra ℂ⊗ℍ⊗𝕆).
  **[P, K25]** Der Beweis gibt jeder Generation „one color index“: Farbe und Generation liegen auf demselben
  Triplett. Für Quarks (3 Farben × 3 Generationen) reicht das nicht; die Zuordnung muss getrennt werden.
  **[V, K28]** Vorschlag: Generationen = die drei Triality-Plätze von Re((xy)z) auf 𝕆 ⊕ 𝕆 ⊕ 𝕆 (S₃, vertauscht mit
  G₂), Farbe = SU(3)-Triplett e₄, e₅, e₆ in jedem Platz; 9 unabhängige farbige Zustände (nachgerechnet).

**S:**
- Die Hopf-Faserungen selbst sind klassische, gesicherte Mathematik.
- Ihre Identifikation mit Photon/Materie/Generationen: Vermutung.
- β_sym wird aus γ_BI und γ_string **eingesetzt**, nicht hergeleitet. γ_L ist das Verhältnis zweier
  veröffentlichter Barbero–Immirzi-Werte (r03 F11); kein GUE-Fixpunkt (r08). Die β-Formel P3 ist eine
  Koinzidenz mit nachträglich gewähltem Exponenten (r09, K11).
- **OP1 (offen):** β_sym direkt aus der Kaskadendynamik als Fixpunkt herleiten.
  Voraussetzung: **OP2 (offen)** Dirac-Operator auf H⁺₋.

**P:**
- „S⁷ ⊃ G₂ ⊃ SU(3)“: S⁷ ist keine Gruppe. Korrekt wäre etwa S⁷ ≅ Spin(7)/G₂, bzw. G₂ als
  Stabilisator; die Rolle von SU(3) sollte über diese Relation formuliert werden.
- Die Kette S¹⁵ → S⁸ → S⁴ → S² ist keine Komposition von Hopf-Abbildungen: Die klassischen Hopf-Maps
  sind S³ → S², S⁷ → S⁴, S¹⁵ → S⁸; Abbildungen S⁸ → S⁴ und S⁴ → S² gehören nicht dazu.
  Die Kaskade K̂ müsste als eigene Abbildung zwischen den Basen definiert werden (z. B. über die
  äquatorialen Inklusionen S² ↪ S⁴ ↪ S⁸ in umgekehrter Richtung).

---

## 4. Triolen

**V:** Die Grundstruktur ist dreigliedrig: drei Kerne mit z₁ + z₂ + z₃ = 0, um 120° phasenverschoben;
diese ℤ/3-Struktur bleibt durch die ganze Kaskade erhalten.

**M:**
- *Algebraisch:* Drei gleich lange, um 120° gedrehte komplexe Zahlen summieren sich zu null
  (Kubikwurzeln der Eins: 1 + ω + ω² = 0).
- *Geometrisch — Triolischer Orbit-Scan* (Abschnitt `sec:alternating-triolic-orbit-scan`, Z. 542; strikte Form Z. 727 ff.):
  - Bewachter Scanraum X_K = X \ B_ε(K); zulässige Orbits γ: S¹ → X_K, also d(γ(s),K) ≥ ε.
  - Linsen-Triole 𝒯_lens = (F₋, K, F₊), Teilchen-Triole 𝒯_n = (P_n, K, Q_n).
  - *Core-sighted:* K = (1−λ)P + λQ, λ ∈ [0,1]; *zentral balanciert* nur bei λ = ½.
    Getrennt halten: Sicht durch K ⇏ K ist Mittelpunkt.
  - Bifokaler Defekt 𝓔_F(x) = |d(x,F₋) + d(x,F₊) − 2a|; η-bifokal bei sup 𝓔_F ≤ η (Ellipse: η = 0).
  - Shift-Selektor Σ^i_j = δ^i_{j+1}, (Σ^k)^i_j = δ^i_{j+k}; Paritätsprojektoren Π₀, Π₁.
    Σ tauscht die Regime 𝒜 ↔ ℬ, Σ² erhält sie.
  - Periapsis-Hülle Σ_K aus ρ_min(θ,φ) = min_s d(γ(s),K) > 0.
- Hopf-Vergleich: Im idealen Hopf-Bild füllen Fasern S³ lückenlos; im bewachten Bild X = S³ \ B_ε(K)
  ist ein verbleibender Kern **kein** Hopf-Defekt, sondern das ausgeschlossene, bewachte Objekt selbst.

**S:**
- Orbit-Scan: sauber definiert, als **lokales Readout-Modell**. Ausdrücklich keine physische
  Trajektorie durch den Kern.
- Strikter Orbit-Scan-Satz (`thm:strict-alternating-triolic-orbit-scan`) und Existenz der Scanfläche
  (`prop:existence-guardedness-scan-surface`): bewiesen im gesetzten Rahmen.
- Hochstufung der lokalen Flächendaten in die globale HC/MM-Chart-Brücke: offen (Promotion Guard).

---

## 5. Fraktal

**V:** Die Selbstdurchquerung der Sphaera ist fraktal: dieselbe Null-Achsen-Struktur kehrt auf jeder
Stufe wieder und erscheint physikalisch als Lichtachse.

**M:**
- Null-Achse eines Stratums: L_n := {q_n ∈ S_n : |q_n|² = 0} (Z. 6010). **Seit r06** in Lesart B
  invariant als s = 0 definiert; ihre Richtungen sind genau S₀ = ℂP¹.
- **Satz** (`thm:fractal`): K̂(L_n) = L_{n−1}; globale Null-Achse L = ⋂_{n≥0} L_n = S₀.
- ℤ/3-Struktur z₁+z₂+z₃ = 0 bleibt auf der Null-Achse erhalten.
- **Kristall–Fraktal-Probe** (Z. 46941): Ringzentren K̂_ℓ, Kristall-Kohärenzresiduum 𝒞_crys,
  Mehrskalen-Residuenmenge ℛ_multi, Box-Counting log N(δ) ≈ D_res·log(1/δ) + b.
  Endliche Diagnostik: 𝒞_crys^max ≈ 8,7·10⁻¹⁷, 30.216 Residuenpunkte, **D_res ≈ 2,435**.
- *Readout-Guard:* Kristall-Aussage nur über Kohärenz der Zentren; Fraktal-Aussage nur über die
  Skalierung der Residuenmengen über erklärte Skalen.

**S:**
- „Fraktal“ im Satz bedeutet *selbstähnlicher Transport derselben Struktur*, nicht fraktale Dimension.
- D_res ≈ 2,435 ist eine **diagnostische Zahl**, kein Beweis einer Hausdorff-Dimension.
- Keine Hochstufung zu einem globalen Schließungssatz.

**P:**
- Der Beweis von K̂(L_n) = L_{n−1} ist prosaisch („by the general MM-tools“), nicht ausgerechnet.
  Er sollte explizit über die Wirkung von K̂ auf q_n geführt werden.
- Bei aufsteigender Kette S₀ ⊂ S₁ ⊂ S₂ gilt ⋂L_n ⊆ L₀; die Gleichheit mit S₀ verlangt L₀ = S₀,
  also dass S₀ ganz aus Nullvektoren besteht. Das sollte als eigene Aussage stehen.

---

## 6. Weg zur vereinheitlichten Theorie

**V:** Aus der Grundvermutung folgt eine strukturelle Master-Gleichung (Z. 17696):

    𝔊[Ψ,g] + 𝔗_tri[Ψ] + ℌ_HC[Ψ] + 𝔔_cl[Ψ] + 𝔅_β[Ψ] = 0

(Geometrie, Triolen-Dynamik, Heisenberg-Kompensator, Schließungsterm, Frame-Phasenterm), halbkonkret:

    R[Ψ] + Σ_a D_aΨ_a + Σ_{a≠b} Λ_ab Ψ_b + λ_HC(I−C)Ψ + λ_cl ℛ_cl[Ψ] + λ_β(Ψ − U_βΨ) = 0

Master-Strukturlinie (`thm:master-structural`): Triolenquelle → Träger → 𝓜₁₆ → 𝓗₁₆ →
schließungsstabiler Sektor → Gruppensymmetrie → Null-Achse → Photon-Fixsektor → Residuen-Lokalisierung
→ Materie/Tachyon/Photon → Higgs-Vermittlung → Feldgleichungen.

**S:**
- Die Master-Gleichung ist eine **strukturelle Kompression**, die halbkonkrete Form ausdrücklich nur
  als Lesart; Kopplungen λ_HC, λ_cl, λ_β sind nicht bestimmt.
- MM/HC-Feldgleichungs-Refaktor: offen (v4.8.0-Linie).
- Gesichert sind lokale/effektive, frame-typisierte Schließungen — **keine** globale Schließung (T2, W_all).

**Was eine Vereinheitlichung konkret bräuchte (offene Prüfsteine):**
1. OP1: β_sym als Fixpunkt der Kaskade, ohne γ_BI und γ_string als Eingabe.
2. OP2: Dirac-Operator auf H⁺₋.
3. ~~Signatur und Lorentzwirkung~~ geklärt (K1); **Lesart B ist Arbeitslesart** (r06), Sektoren über s (r07).
4. Bestimmung der Kopplungen der Master-Gleichung aus der Struktur statt durch Wahl.
5. Mindestens eine quantitative Vorhersage, die nicht schon als Eingabe verwendet wurde und an
   Messdaten scheitern *könnte*. **Stand nach r09:** Keine der Vorhersagen P1–P6 ist bestätigt; P1 nicht
   bestätigt, P2 durch Daten ausgeschlossen, P3 Koinzidenz (Register in r09, Abschnitt K11).
6. Eine Feldgleichungs-Wirkung, die definiert ist (r05: ∫Σ dτ existiert nicht).

Ob die Grundvermutung zu einer zutreffenden vereinheitlichten Theorie führt, ist **offen**.

---

## 7. Arbeitsergebnisse

### K1 — Signatur und Lorentzwirkung des Biquaternion-Kerns (2026-10-19)

Skript: `llm/k1_signatur.py` (SymPy/NumPy, reproduzierbar). Ebene aller Punkte: **M** (gerechnet),
die physikalische Deutung in K1.5 ist **V**.

**K1.1 Befund.** Für q = it·1 + z₁e₁ + z₂e₂ + z₃e₃ mit z_k = x_k + iy_k:
- Companion-Norm −t² + Σ|z_k|²: Signatur **(1,6)**; unter komplexen Einheits-Konjugationen nicht
  invariant (Testwert 2,56 → 32,6).
- Natürliche Norm der Biquaternionen ist die komplex-bilineare **N(q) = q q̄ = −t² + Σ z_k²**
  (Quaternionenkonjugation, *ohne* komplexe Konjugation). Re N = −t² + |x|² − |y|², Im N = 2 x·y.

**K1.2 Lesart A — Vierervektor.** Auf dem reellen Schnitt {q : q† = −q} (z_k reell, q† = Quaternionen- und
komplexe Konjugation) ist N(q) = −t² + x₁² + x₂² + x₃²: exakt **Minkowski (1,3)**.
Die Wirkung q ↦ u q u†, N(u) = 1, erhält N und den Schnitt und ändert die Zeitkomponente: echte Boosts.
*Preis:* Die z_k sind reell — die 120°-Phasen der Triole haben hier keinen Platz.

**K1.3 Lesart B — komplexer Dreiervektor.** z = (z₁,z₂,z₃) ∈ ℂ³ mit der Wirkung q ↦ u q u⁻¹, u komplexe
Einheits-Biquaternion. Der Skalarteil it bleibt fest, Σ z_k² ist invariant: die Gruppe wirkt als
**SO(3,ℂ) ≅ SO⁺(1,3)** (eigentliche orthochrone Lorentzgruppe). Die Companion-Formel u q u⁻¹ ist in dieser
Lesart korrekt, sobald u komplex statt reell gewählt wird. Lorentz-Invariante ist Σ z_k² (komplex),
nicht Σ|z_k|². t ist hier ein invarianter Parameter, keine Zeitkoordinate eines Vierervektors.

**K1.4 Triolen-Lemma (bewiesen).** Für (z₁,z₂,z₃) ∈ ℂ³ gilt:

    z₁ + z₂ + z₃ = 0  und  z₁² + z₂² + z₃² = 0   ⇔   (z₁,z₂,z₃) = c·(1, ω, ω²)  bis auf Reihenfolge,

mit ω = e^{2πi/3}, c ∈ ℂ. Beweis: p₂ = e₁² − 2e₂, also e₁ = p₂ = 0 ⇒ e₂ = 0; die z_k sind dann die
Nullstellen von λ³ − e₃, also die drei Kubikwurzeln von e₃. Rückrichtung: 1 + ω + ω² = 0 und
1 + ω² + ω⁴ = 1 + ω² + ω = 0.
*Folgerung:* Die symmetrische 120°-Triole ist genau der zentrierte Fall, der in Lesart B **lichtartig**
(Σ z² = 0) ist. Die Triolenbedingung mit gleichen Beträgen ist damit nicht nur eine Phasenbedingung,
sondern zusätzlich eine Lorentz-invariante Nullbedingung.

**K1.5 Physikalisches Gegenstück (V).** Lesart B ist formal die Riemann–Silberstein-Darstellung
F = E + iB des elektromagnetischen Feldes: Σ z² ↔ E² − B² + 2i E·B, die beiden Feldinvarianten
(numerisch bestätigt). Σ z² = 0 heißt E² = B² und E ⊥ B — ein *Nullfeld*, also Strahlung.
Die Ausgangsvermutung „Photon-Sektor = symmetrische Triole“ bekommt damit eine präzise mathematische
Form, die man prüfen kann. Bewiesen ist die Physik dadurch nicht.

**K1.6 Folgen für andere Teile (neue Prüfpunkte).**
- Die Sektorklassifikation über das Vorzeichen von Re z_k (Materie/Tachyon/Photon) ist in Lesart B
  **nicht Lorentz-invariant**; invariante Kandidaten wären Re/Im von Σ z² bzw. N(q).
- Die Null-Achse L_n = {|q_n|² = 0} (Abschnitt 5) muss auf die neue Norm umgestellt werden:
  mit N(q) wird sie zu zwei reellen Gleichungen (−t² + |x|² − |y|² = 0, x·y = 0).
- Lesart A und B schließen sich nicht aus: ℍ⊗ℂ trägt beides (Vierervektor-Schnitt bzw. Skalar ⊕ ℂ³).
  Welche Lesart die Kerne K₁, K₂, K₃ tragen sollen, ist eine **Modellentscheidung**, die der Corpus
  bisher nicht trifft.

**Stand nach K1:** Prüfpunkt „Signatur/Lorentz“ ist mathematisch geklärt (zwei saubere Reparaturen);
die Modellentscheidung A vs. B ist **offen**. Guard- und Ledger-Vektoren unverändert.

### K2 — Lesart B: Sektoren, Informationsebene, Punkte aus dem Riemann-Taktgeber (2026-10-19)

Skript: `llm/k2_punkte.py`. Nutzer-Entscheidung: Arbeit in **Lesart B** fortsetzen.

**K2.0 Grundvermutung (V, vom Autor bestätigt).** Raumzeit ist nicht fundamental, sondern eine
**Projektion aus der Informationsebene**. Die Raumzeit-*Punkte* sollen über den **Riemann-Taktgeber**
gewonnen werden.

**K2.1 Invariante Sektoren (M).** Die Bahnen von SO(3,ℂ) auf ℂ³ sind durch s = Σ z_k² bestimmt
(für s ≠ 0 eine Bahn pro Wert; s = 0: Nullkegel ∪ {0}). Kandidat für eine Lorentz-invariante
Sektoreinteilung, die die frame-abhängige Re-z-Einteilung ersetzt:
- s = 0: Nullsektor (Photon-artig; enthält die symmetrische Triole, K1.4)
- s > 0 reell: „elektrisch dominiert“; s < 0 reell: „magnetisch dominiert“
- Dualitätsdrehung z ↦ i z bildet s ↦ −s ab (tauscht die beiden massiven Sektoren), lässt s = 0 fest.
Passt strukturell zu „Tachyon = J-Dual der Materie“ und „Photon = Fixsektor“. Die Zuordnung
elektrisch ↔ Materie, magnetisch ↔ Tachyon ist eine **offene Modellentscheidung** (V).
Ebenfalls offen: Bedeutung komplexer s mit Im s ≠ 0, und Rolle von t (aus N(q) = 0 folgt s = t²).

**K2.2 Informationsebene = Spinoren (M).** Ein Spinor ψ ∈ ℂ² (normiert: ein Qubit, Zustandsraum ℂP¹)
liefert
- den lichtartigen Vierervektor k(ψ) = (|ψ|², ψ†σψ); seine Raumrichtung ist die **Hopf-Abbildung**
  S³ → S² (= Bloch-Vektor),
- den Nullvektor z(ψ) = (ψ₁² − ψ₂², i(ψ₁² + ψ₂²), −2ψ₁ψ₂) ∈ ℂ³ in Lesart B.
Die projektivierten Nullrichtungen bilden genau ℂP¹ = S² = S₀ aus dem Hopf-Satz. Die symmetrische Triole
(1, ω, ω²) hat einen Spinor, z. B. ψ ≈ (0,974+0,128i, 0,310+0,404i).
Lesart der Stratenkette (V): S₀ = ℂP¹ — ein Spinor, lichtartig (Photon); S₁ = ℍP¹ — ein Spinorpaar,
dessen Summe zweier Nullvektoren zeitartig ist (Materie; vgl. Dirac = zwei Weyl-Spinoren).

**K2.3 Punkte aus Spinoren und Takten (M, numerisch geprüft).**
- Jeder zukunftsgerichtete zeitartige Vektor x ist Summe zweier zukunftsgerichteter Nullvektoren:
  x = k(ψ_a) + k(ψ_b). Konstruktion: Eigenzeit m = √(−⟨x,x⟩), raumartiges e mit ⟨e,x⟩ = 0, ⟨e,e⟩ = 1,
  k± = (x ± m e)/2; Spinoren aus k± rekonstruierbar (Rekonstruktion exakt).
- Der **Takt steckt in der Spinornorm**: |ψ|² = Zeitkomponente von k(ψ). Normierter Anteil = Richtung
  (Qubit), Norm = Takt. Ein Ereignis = zwei unnormierte Spinoren = zwei Qubits + zwei Takte.
- Mit Takten aus den ersten N Zeta-Nullstellen-Ordinaten γ_n (numerisch bekannt: 14,1347; 21,0220;
  25,0109; …) und zwei festen Qubits entsteht eine endliche, diskrete Ereignismenge mit Eigenzeiten
  2√(γ_a γ_b).

**K2.4 Grenzen und Prüfpunkte (P).**
- *Nicht eindeutig:* Ein Ereignis hat eine ganze 2-Sphäre von Spinorpaaren (Wahl von e). Das ist eine
  Eichfreiheit — strukturell ähnlich der Twistor-Inzidenz (Punkt ↔ Familie im Twistorraum), muss aber
  als solche definiert werden.
- *Nur Zukunftskegel:* Summen erreichen nur zeitartige/lichtartige Zukunftsvektoren. Raumartige
  Abstände brauchen Differenzen oder eine zweite Konstruktion.
- *Der Takt ist bisher ein Parameter*, keine Herleitung: Warum gerade Zeta-Ordinaten Takte sind, folgt
  aus der Konstruktion nicht — das ist der Kern der Vermutung.
- *Guard:* Endliche, numerisch verifizierte Nullstellenlisten setzen RH **nicht** voraus. Erlaubt ist
  nur der lokale, endliche Taktgeber (vgl. r13: „probe, not identification“; `W_clk^loc` unter
  Δ_γ < 1/5). Ein globaler Taktgeber über alle Nullstellen wäre `W_γ^glob` — **verboten**.
  Die Schranke Δ_γ < 1/5 hat im vorliegenden Quelltext weiterhin **keine Herleitung** (r65-Volltext fehlt).
- *Stand im Corpus:* Der Riemann-Taktgeber existiert als Diagnostik (r13–r15: Handoff-Clock 𝒯_γ,
  Phasen-Mismatch 𝓔_zero, Clock-Funktion 𝒞_γ(τ) = 1 + η|Σ w_m e^{iγ_m τ}|²/(Σ|w_m|)²). Eine Verbindung
  zu Raumzeit-Punkten ist dort **nicht** hergestellt — K2.3 ist der erste Vorschlag dafür.

**Literaturanker:** Penrose-Twistortheorie (Raumzeit aus Spinor-/Twistorraum), Riemann–Silberstein-Vektor,
Montgomery–Odlyzko (GUE-Statistik der Zeta-Nullstellen).

**Stand nach K2:** Lesart B trägt Sektoren, Photon-Sektor und Hopf-Basis konsistent; ein konkreter
Mechanismus „Ereignis = zwei Qubits + zwei Takte“ ist gebaut und geprüft. Offen: Eindeutigkeit,
raumartige Punkte, und warum der Takt riemannsch ist. Guard- und Ledger-Vektoren unverändert.

### K3 — Primzahlen, Zeta und Photonen; Torus (2026-10-19)

Skript: `llm/k3_primzahlen_photonen.py`.

**K3.0 Grundvermutung (V, vom Autor).** Der Riemann-Takt ist gerechtfertigt, weil es einen
Zusammenhang zwischen Primzahlverteilung, ζ und Photonen gibt. Der Autor geht davon aus, dass dieser
Zusammenhang im Corpus schon angelegt ist.

**K3.1 Was im Corpus bereits steht (M, Fundstellen).**
- Primgitter in Log-Koordinaten: **Γ_P = {log p : p prim}** (Companion Z. 19263, 19682, 21934);
  in der Riemann-Arbeit multiplikativ als Γ_ℙ = ⟨p⟩ ⊂ ℚ⁺ — dieselbe Struktur über den Logarithmus.
- **Dilatationsgenerator L₀ = −i(x d/dx + ½)** „encodes the prime lattice geometry in log-coordinates“
  (Z. 7255). Geprüft: L₀ x^{−½+iE} = E·x^{−½+iE}; in τ = log x ist L₀ = −i(d/dτ + ½), also der
  Erzeuger von Translationen in τ — **die Takt-Variable ist im Corpus schon τ = log x**.
- Spurformel Σ(τ) = Tr(e^{−iτL₀}) = 1 − Θ(τ) + R(τ) über die **Guinand–Weil-Explizitformel**
  (Riemann-Arbeit Thm. `thm:EF`, Companion Z. 7255 ff.).
- Erster Nullstellen-Takt im Frame-Regime: γ₁ = 14,135 ↦ γ_L = 1,8637, β_sym = 0,5492
  („Physical (prime lattice)“, Z. 21738) zwischen Hopf-Grenze (2; 1/√3) und Tribonacci-Grenze (𝕋 ≈ 1,839).
- Λ_bare ∼ γ₁² (Z. 24546): γ₁ als „natürliche Energieskala des Primgitters“.
- **Nicht** im Corpus (auch nicht in den 841 älteren Ständen): Primon-Gas, Bose-/Fermi-Statistik über
  Primzahlmoden, quadratfreie Zustände, Möbius-Index.

**K3.2 Die Brücke: Primon-Gas (M, gesicherte Mathematik; Julia 1990, Spector 1990).**
Eine Mode pro Primzahl p mit Energie log p; Vielteilchenzustände ↔ natürliche Zahlen n = ∏ p^{k_p}.
Drei Statistiken, numerisch bis n = 2·10⁵ bestätigt (s = 2, 3):

| Statistik | Zustände | Zustandssumme |
|---|---|---|
| bosonisch | alle n | Z_B(s) = ζ(s) = ∏(1 − p^{−s})^{−1} |
| fermionisch (Pauli) | quadratfreie n | Z_F(s) = ζ(s)/ζ(2s) = ∏(1 + p^{−s}) |
| Index (−1)^F | alle n, Gewicht μ(n) | W(s) = 1/ζ(s) |

**K3.3 Lesart für die Sphaera (V).** Bosonischer Sektor (Photon) ↔ ζ(s); fermionischer Sektor (Materie,
Pauli „höchstens ein Fermion pro Stufe“) ↔ ζ(s)/ζ(2s); Möbius-Vorzeichen (−1)^F ↔ J-Antisymmetrie
A(f). Die Nullstellen von ζ sind dann die Stellen, an denen die bosonische Zustandssumme bei komplexer
inverser Temperatur s = ½ + iγ verschwindet, und zugleich die Frequenzen des Takts in τ = log x
(Explizitformel). Die physikalische Identifikation „Photonen = Primzahlmoden“ ist **nicht bewiesen**.

**K3.4 Linear vs. logarithmisch — kein Widerspruch (M).** Die Materie-Stufen |z⁻|_n = n·ℓ_P sind die
multiplikative Koordinate x = n; τ = log n ist die Takt-Koordinate; L₀ verbindet beide. Primitive
Stufen p·ℓ_P ↔ Moden-Energien log p sind dieselbe Information in zwei Koordinaten. Die Takt-Phase eines
Zustands ist γ·log n, d. h. (|z⁻|/ℓ_P)^{iγ}.

**K3.5 Prüfpunkt (P).** Der Companion (Thm. `thm:origin` (iii)) erlaubt *jede* Stufe n mit höchstens
einem Fermion. Im fermionischen Primon-Gas sind dagegen die **Primzahlen die Einteilchen-Moden** und
nur **quadratfreie n** zulässige Vielteilchenzustände. Beide Lesarten unterscheiden sich darin, was eine
„Stufe“ ist (Einteilchen-Niveau vs. Vielteilchenzustand). Modellentscheidung offen.

**K3.6 Torus (M, vom Autor bestätigt: entsteht aus der Hopf-Faserung).**
Für die Hopf-Abbildung S³ → S² gilt: Urbild eines Punktes = Kreis (Faser); Urbild eines Breitenkreises
θ = Torus {(cos(θ/2)e^{iu}, sin(θ/2)e^{iv})} ≅ S¹ × S¹ (Clifford-Torus bei θ = π/2); an den Polen
entartet der Torus zum Kreis. Numerisch bestätigt. S³ ist damit eine Schar ineinander geschachtelter
Tori, auf denen die Fasern als verkettete Kreise (Hopf-Link) liegen — das ist das „Ringfüllungsbild“
aus `prop:hopf-completion-vs-guarded-core-remainder`. In K2-Sprache: Alle Qubits mit gleichem
Bloch-Breitengrad bilden einen Torus; der Breitengrad ist das Verhältnis |ψ₁|/|ψ₂|.

**Stand nach K3:** Der Riemann-Takt hat im Corpus bereits eine mathematische Heimat (Γ_P = {log p},
L₀, Guinand–Weil). Neu ist die Primon-Brücke mit einer natürlichen Boson/Fermion-Aufteilung, die zur
Photon/Materie-Trennung passt. Offen: physikalische Identifikation; Prüfpunkt K3.5. Guard- und
Ledger-Vektoren unverändert; RH wird nirgends vorausgesetzt.

### K4 — Jede Primzahlmode ein Qubit (2026-10-19)

Skript: `llm/k4_primzahl_qubits.py`.

**K4.1 Konstruktion (M, exakt).** Das fermionische Primon-Gas *ist* ein Qubit-Register: ein Qubit pro
Primzahl p, |0⟩_p = leer, |1⟩_p = besetzt, H = Σ_p log p · n_p. Basiszustände ↔ quadratfreie n
(geprüft: 4 Qubits {2,3,5,7} ↔ die 16 Teiler von 210). Tr e^{−sH} = ∏(1 + p^{−s}) = ζ(s)/ζ(2s).
Damit verbinden sich K2 und K3: **Informationsebene = Register von Primzahl-Qubits**, jedes mit eigener
Bloch-Kugel und Hopf-Faser.

**K4.2 Primzahl-Uhr (M, exakt).** Unter e^{−iHτ} präzediert jedes Qubit p auf seiner Bloch-Kugel um die
z-Achse mit Frequenz log p (geprüft für p = 5). Die Bewegung läuft entlang der Hopf-Faser-Phase, der
Breitengrad (= Besetzungsgewicht) bleibt fest — jedes Qubit läuft auf seinem Torus (K3.6).

**K4.3 Rückkehramplitude (M, exakt für σ > 1).** Für den thermischen Produktzustand mit
|β_p|²/|α_p|² = p^{−σ}:

    A(τ) = ⟨Ψ|e^{−iHτ}|Ψ⟩ = Z_F(σ + iτ) / Z_F(σ),   Z_F = ζ(s)/ζ(2s).

Bei σ = 2 stimmen Register (alle p < 10⁵) und analytische Formel auf 6 Stellen überein.

**K4.4 Ticks an den Nullstellen (M, mit Vorbehalt).**
- *Exakt und unbedingt:* Auf der kritischen Linie gilt Z_F(½ + iτ) = 0 ⇔ ζ(½ + iτ) = 0, weil
  ζ(1 + 2iτ) ≠ 0 (Primzahlsatz). Numerisch: Minima von |Z_F(½+iτ)| genau bei 14,135; 21,02; 25,01;
  30,425; 32,935. Kein RH nötig — die Aussage gilt für jede Nullstelle *auf* der Linie.
- *Lesart (V):* Ein Nullstellen-Tick ist ein Zeitpunkt, an dem das Register einen zum Start
  **orthogonalen**, also perfekt unterscheidbaren Zustand erreicht. Das ist der quanteninformations-
  theoretische Begriff eines Uhrtakts (vgl. Mandelstam–Tamm, Margolus–Levitin).

**K4.5 Die harte Grenze (P).**
- ∏(1 + p^{−σ}) konvergiert nur für σ > 1. Für σ ≤ 1 ist der Registerzustand **nicht normierbar**;
  auf der kritischen Linie ist A(τ) keine echte Amplitude (Z_F(½) = ζ(½)/ζ(1) = 0 wegen des Pols bei 1).
  Für normierbare Zustände (σ > 1) hat Z_F keine Nullstellen — dort gibt es keine Ticks.
- Endliche Register: Mit 25 Qubits liegen die 5 tiefsten Minima nahe den Nullstellen
  (14,07; 21,09; 25,28; 30,80; 32,94). Mit mehr Qubits wird es **schlechter**, nicht besser
  (1.229 Qubits: Störminimum bei 13,47; 78.498 Qubits: fast nur Störminima um 11–14,5), weil das
  abgeschnittene Euler-Produkt auf der kritischen Linie nicht konvergiert.
- Folgerung: Die Ticks existieren nur in der analytischen Fortsetzung, nicht als Zustand eines
  physikalischen Registers. Das ist dieselbe Hürde, an der die Hilbert–Pólya-Programme hängen.

**K4.6 Nächste Kandidaten.**
- Bost–Connes-System (1995): quantenstatistisches System mit Zustandssumme ζ(β) und Phasenübergang
  bei β = 1 — genau die Grenze aus K4.5. Natürlicher Rahmen, um den Übergang σ > 1 → σ = ½ zu fassen.
- Geglättete Euler-Produkte (Gonek–Hughes–Keating: ζ ≈ Euler-Produkt bis X × Produkt über Nullstellen):
  Kandidat für eine Regularisierung, unter der endliche Register stabile Ticks zeigen.
- Bosonischer Sektor: Photon-Moden sind Oszillatoren, keine Qubits; über die Schwinger-Darstellung
  (zwei Oszillatoren → SU(2)-Spinor) ließe sich der Spinor aus K2 bosonisch bauen.

**Stand nach K4:** „Jede Primzahlmode ein Qubit“ ist exakt realisiert (fermionischer Sektor), mit
Primzahl-Uhr und Rückkehramplitude Z_F. Die Nullstellen sind genau die Orthogonalitätszeiten der
analytisch fortgesetzten Amplitude. Offen und zentral: die Normierbarkeit auf der kritischen Linie.
Guard- und Ledger-Vektoren unverändert; RH nicht vorausgesetzt; kein globaler Taktgeber (`W_γ^glob`).

### K5 — Bost–Connes-System und Prüfung des Riemann-Papers (2026-10-19)

Skripte: `llm/k5_bost_connes.py`, `llm/rh_review_checks.py`; Gutachten: `llm/Pruefung_Riemann_Paper_v4_15.md`.

**K5.1 Einbettung (M).** Das Bost–Connes-System (1995) hat den Hilbertraum ℓ²(ℕ*) mit H ε_n = log n · ε_n
und Zustandssumme Tr e^{−βH} = ζ(β). Das bosonische Primzahl-Register aus K3 *ist* dieser Raum
(Rückkehramplitude ζ(β+iτ)/ζ(β), bei β = 2 numerisch bestätigt); das fermionische Register aus K4 ist
der Unterraum der quadratfreien n.

**K5.2 Phasenübergang bei β = 1 (M, Bost–Connes).**
- β > 1: Gibbs-Zustände mit Dichtematrix; die Symmetrie Ẑ^× ≅ Gal(ℚ^ab/ℚ) ist **spontan gebrochen**
  (viele extremale KMS-Zustände).
- β ≤ 1: genau ein KMS-Zustand, symmetrisch, **ohne Dichtematrix** — er existiert nur als Zustand auf
  der Algebra. Am Übergang divergiert ζ(β) (β = 1,001: ζ ≈ 1000,6).
- Hochtemperatur-Zustand auf den Phasen e(a/b) (Formel nach Bost–Connes / Connes–Marcolli, zitiert):
  φ_β(e(a/b)) = b^{−β} ∏_{p|b} (1 − p^{β−1})/(1 − p^{−1}); bei β = 1 verschwinden alle nichttrivialen
  Phasen.

**K5.3 Was das für K4.5 bedeutet (M/P).** Bost–Connes löst die Normierbarkeitsgrenze *teilweise*: Für
alle reellen β ≤ 1 gibt es einen echten Zustand, auch ohne Dichtematrix. Die Nullstellen liegen aber bei
**komplexem** β = ½ + iγ — das ist keine Temperatur, und auch Bost–Connes liefert dort keinen Zustand.
Der nächste Schritt dafür ist Connes' Adelklassenraum (1999), wo die Nullstellen als
Absorptionsspektrum erscheinen. Dort ist aber gerade die Gültigkeit der Spurformel **äquivalent zu RH**.

**K5.4 Lesart für die Sphaera (V).** Unterhalb β = 1 (heiß): ein einziger symmetrischer Zustand ↔
ungebrochener Kollapszustand z⁻ = 0. Oberhalb β = 1 (kalt): spontane Symmetriebrechung in viele
gleichwertige Zustände ↔ „Universum als gebrochener Frame“ (Thm. `thm:origin`). Strukturell passt das;
eine Herleitung des Übergangs aus der Sphaera-Kaskade fehlt.

**K5.5 Befund Riemann-Paper (Kurzfassung).** Kombinatorik L1–L11, Euler-Produkt und Funktionalgleichung
korrekt. Die Beweiskette für RH trägt nicht:
- explizite Formel falsch angegeben (nachgerechnet: 2,159 vs. 0,520; die korrekte Λ-Form stimmt auf
  6 Stellen),
- J verlässt den Hardy-Raum; in der einzig wohldefinierten Lesart ist ℋ⁺₊ = {0},
- T4+T5 zeigt keine wesentliche Selbstadjungiertheit (und L₀ ist auf L²(ℝ⁺) ohnehin s.a. mit
  kontinuierlichem Spektrum),
- T6 benutzt Connes' Spurformel, die zu RH äquivalent ist (zirkulär); zudem Laplace[Σ] ≠ log ζ.
Folgen für den Companion: `thm:unitary-equiv` und die Äquivalenz-Begründung von `thm:unity` werden
**offen**; Σ = 1 − Θ + R in den Feldgleichungen muss auf die korrigierte Formel umgestellt werden.
Die Guard-Regel „`W_γ^glob` verboten“ ist bestätigt.
- *Nachtrag „Beweis aus der Menge selbst“ (Gutachten B8):* Derselbe Kern (ℙ, log p) gehört zu ζ und zu
  L(s, χ₋₄), deren erste Nullstellen verschieden sind (14,1347 vs. 6,0209); die Davenport–Heilbronn-
  Funktion erfüllt eine Funktionalgleichung und hat eine Nullstelle bei 0,8085 + 85,6993 i. Die Lage der
  Nullstellen steckt also nicht in (ℙ, log p) allein, sondern in der Faktorisierungsstruktur
  (Euler-Produkt) — Anschlusspunkt: Primon-Gas/Bost–Connes (K3–K5).

### K6 — Das Sphären-Modell als eigenständige Grundlage (2026-10-19)

Skript: `llm/k6_triolen_algebra.py` (explizite Cayley–Dickson-Arithmetik, Konvention des Riemann-Papers).

**K6.0 Einordnung (V, vom Autor).** Das Riemann-Paper war Startpunkt; der Companion übernimmt daraus vor
allem den **Heisenberg-Kompensator** und das **Sphären-Modell**, also die grundlegenden Transformationen
(J-Spiegelung, Kaskade, Triolen-Hierarchie ℍ → 𝕆 → Sedenionen). Ziel: diese Teile vom RH-Beweisanspruch
entkoppeln und eigenständig sauber machen.

**K6.1 Was trägt (M).**
- Heisenberg-Kompensator C = ½(1 + J) mit **linearer** unitärer Involution J (J² = 1): echter orthogonaler
  Projektor, C(Jf) = C(f), Lagrangian-Invarianz gilt. Braucht keinerlei RH-Aussage.
- Kaskade K̂ als Komposition orthogonaler Projektionen auf absteigende abgeschlossene Teilräume:
  wohldefiniert.
- J_B (e₁-Spiegelung) als lineare Involution auf ℂ⊗ℍ: wohldefiniert; auf ℍ ist sie ein
  Anti-Automorphismus.
- T1 = (e₁,e₂,e₃) und T3 = (e₃,e₄,e₇) sind quaternionische Unteralgebren.

**K6.2 Was repariert werden muss (P, nachgerechnet).**
- **T2 = (e₄,e₅,e₆) ist keine quaternionische Unteralgebra:** e₄e₅ = e₁ ∉ T2 — das steht sogar in der
  Rechnung des Papers selbst.
- Korrekte Struktur: Die 7 quaternionischen Linien (Fano-Ebene) in dieser Konvention sind
  (1,2,3), (1,4,5), (1,6,7), (2,4,6), (2,5,7), (3,4,7), (3,5,6). Drei Triolen überdecken alle sieben
  Einheiten **genau dann, wenn sie durch einen gemeinsamen Punkt gehen** — z. B. durch e₄ = ℓ:
  (1,4,5), (2,4,6), (3,4,7). Es gibt 7 solche Konfigurationen, eine pro Punkt der Fano-Ebene.
  *Lesart (V):* Die drei Triolen teilen sich eine gemeinsame Achse — passend zu „drei Kerne um einen
  gemeinsamen Kollapspunkt“.
- R_{e₁} (nur e₁ negiert) ist **kein** Automorphismus von 𝕆. Es gibt 8 Vorzeichen-Automorphismen; die
  e₁ negierenden negieren immer **vier** Einheiten, z. B. {1,2,4,7}, und lassen eine quaternionische
  Linie fest (hier (3,5,6)). Wenn J eine Symmetrie der Algebra sein soll, muss es diese Form haben.
- Sedenionen: O₂ = (f₈,…,f₁₄) ist nicht abgeschlossen (f₈f₉ = f₁); Nullteiler existieren
  ((e₃+e₁₀)(e₆−e₁₅) = 0). Die Hierarchie bleibt oberhalb von 𝕆 nur algebraisch, nicht geometrisch —
  das Paper räumt das für die Hopf-Struktur selbst ein.
- Maximale Totalität: in ZF nur als eingeschränkte Menge formulierbar; K̂ darf nicht auf Elemente
  außerhalb seines Definitionsbereichs angewendet werden.

**Stand nach K6:** Heisenberg-Kompensator und Kaskade sind eigenständig tragfähig. Die
Triolen-Hierarchie ist auf ℍ → 𝕆 tragfähig, sobald T2 durch die korrekte konkurrente Konfiguration
ersetzt wird. Vorschlag: Entkopplungsrunde v4.8.0-r04 im Companion. Guard- und Ledger-Vektoren unverändert.

**Stand nach K5:** Das Primzahl-Register sitzt exakt im Bost–Connes-System; dessen Phasenübergang bei
β = 1 ist ein natürlicher Kandidat für den „Bruch des Kollapszustands“. Die Ticks bei komplexem β bleiben
offen und führen direkt auf das Hilbert–Pólya-/Connes-Problem — das auch das Riemann-Paper nicht
gelöst hat. Guard- und Ledger-Vektoren unverändert.

---

### K7 — Korrigierte explizite Formel, Θ-Summen-Vermutung entschieden (2026-10-19)

Skripte: `llm/k7_theta_summe.py`, `llm/zeros_gen.py` (2000 Nullstellen, parallel). Im Companion als
Runde **v4.8.0-r05** (`sec:v480-r05-corrected-explicit-formula`).

**K7.1 Korrigierte Zerlegung (M, bewiesen/klassisch).** Für τ > 0 distributionell:
Σ(τ) = Σ_ρ e^{iγτ} = **e^{τ/2}** (Pol) − **e^{−τ/2} Σ Λ(n) δ(τ − log n)** (Primzahlen) −
**e^{−τ/2}/(e^{2τ} − 1)** (triviale Nullstellen). Die Dreiteilung Pol / Primzahlen / triviale Nullstellen
bleibt, alle Funktionsformen ändern sich.

**K7.2 Einstein-Lesart (V).** M ↔ Λ, P ↔ T_μν, Z ↔ G_μν bleibt als strukturelle Vermutung. Das Integral
∫Σ dτ existiert nicht (M wächst, Z ∼ 1/(2τ)); Tr e^{−iτL₀} ist kein Wärmeleitungskern. Λ_bare ∼ γ₁² ist
nicht herleitbar (der Polterm enthält keine Nullstelle).

**K7.3 Θ-Summen-Vermutung (OP5 Step B) — widerlegt (M, nachgerechnet).**
𝒯(T) = 2 Σ sin(Tγ_n/γ_L)/(γ_n/γ_L), T = γ_L^{−3/2}. Exakt über ψ₀(eᵃ) = 0 für eᵃ < 2:
**𝒯(T) = −0,1097 ± 0,0009**, vermutet war 0,8934. Erforderlich wäre β_sym² ≈ 6,80. Die Differenz ist fast
genau 1 (1,003) — Hinweis auf einen falsch behandelten Konstantterm in der Regularisierung.
Der Companion-Wert −0,146 für N = 50 wird reproduziert (−0,145).

**K7.4 GUE (M, empirisch).** 1899 normierte Abstände (Nullstellen 101–2000): KS-Abstand GUE 0,041,
GOE 0,108, Poisson 0,315. GUE gilt empirisch; die Herleitung in `thm:gue` trägt nicht (ein antiunitäres J,
das mit L₀ vertauscht, würde sogar auf GOE zeigen).

**Stand nach K7:** Die Feldgleichungsschicht hat jetzt die richtige Formel. Die Θ-Summen-Vermutung und
mit ihr die Balance-Bedingung von OP5 Step B sind in der bisherigen Form widerlegt. Guards unverändert.

### K8 — Lesart B im Companion (2026-10-19)

Skript: `llm/k9_lesart_b.py`. Im Companion als Runde **v4.8.0-r06** (`sec:v480-r06-complex-vector-reading`).

**K8.1 Übernommen (M).** Signatur (1,6) der alten Norm; natürliche Norm N(q) = q q̄ = −t² + Σz_k²
(multiplikativ); Lesart A (Vierervektor, reeller Schnitt) und Lesart B (ℂ³ mit SO(3,ℂ) ≅ SO⁺(1,3)).
**Lesart B ist Arbeitslesart** (Entscheidung des Autors). `thm:lorentz` zeigte nur J-Invarianz; die
Lorentzwirkung kommt jetzt aus Lesart B.

**K8.2 Neu bewiesen bzw. geprüft (M).**
- Triolen-Lemma: Σz = 0 ∧ Σz² = 0 ⇔ z = c(1, ω, ω²).
- Bahnen von SO(3,ℂ) auf ℂ³: Niveaumengen von s (s ≠ 0), punktierter Nullkegel, {0}; konstruktiv geprüft.
- Veronese: z(ψ) = (ψ₁² − ψ₂², i(ψ₁² + ψ₂²), −2ψ₁ψ₂); jeder Nullvektor hat genau ±ψ als Urbild;
  projektivierter Nullkegel ≅ ℂP¹ = S₀; SL(2,ℂ)-äquivariant.
- Null-Achse in Lesart B invariant als s = 0 definiert; ihre Richtungen sind genau S₀.

**K8.3 Offen.** Zuordnung elektrisch ↔ Materie / magnetisch ↔ Tachyon; Bedeutung nicht-reeller s;
Rolle von t; Transportaussage K̂(L_n) = L_{n−1}.

### K9 — Sektor-Zuordnung und Dualitätswinkel (2026-10-19)

Skript: `llm/k10_dualitaet.py`. Im Companion als Runde **v4.8.0-r07** (`sec:v480-r07-sector-assignment`).

**K9.1 Arbeitszuordnung (vom Autor übernommen).** s > 0 Materie, s < 0 Tachyon, s = 0 Photon. Begründung:
Das Vorzeichen von s trägt genau die Intervall-Signatur der r82-Tachyonskala ℓ_T² = −λ_T² (nicht den
Orientierungscode aus r01). Die alte Einteilung (Photon = rein imaginäres z) wird ersetzt — rein
imaginäres z ist in Lesart B tachyonartig.

**K9.2 Dualitätswinkel (M, bewiesen/geprüft).** Jedes z mit s ≠ 0 ist eindeutig z = e^{iα} z_m mit
s(z_m) = |s| > 0 und α = ½ arg s (mod π). Materie: α = 0; Tachyon: α = π/2. Unter SO(3,ℂ) × U(1)_dual
sind die Bahnen die Schalen {|s| = r} und der Nullkegel.

**K9.3 Lesart (V).** Nicht-reelles s ist kein eigener Sektor, sondern Materie im gedrehten Dualitätsrahmen.
Materie und Tachyon = ein Objekt in zwei Dualitätsrahmen; das Photon ist der einzige dualitätsinvariante
Sektor — die präzise Form der Grundvermutung in Lesart B. Ob α physikalisch oder Eichfreiheit ist: offen.

**K9.4 Rolle von t (Beobachtung).** Auf N(q) = 0 gilt s = t²: reelles t ≠ 0 erzwingt den Materie-Rahmen
mit t = √|s|; t = 0 das Photon; tachyonartig nur mit t² < 0. Kandidat, nicht übernommen.

### K10 — Test der Vorhersage P1 (2026-10-20)

Skript: `llm/k11_p1_entfaltung.py`. Im Companion als Runde **v4.8.0-r08** (`sec:v480-r08-p1-test`).

**K10.1 Vorhersage (V, Companion).** Photon-Frame-Entfaltung mit ρ_μ(t) = log(t/(2πμ))/(2πμ) hat ein
eindeutiges KS-Minimum bei μ = γ_L = 1,864 und verbessert χ² um ~21 % (`thm:gue-selfdet`, `cor:odlyzko`).

**K10.2 Ergebnis (M, gerechnet, Nullstellen 1–2000).**
- Roh (wie definiert): Minimum bei **μ = 1,00** (Standard); bei μ = γ_L mittlerer Abstand 0,42–0,47,
  KS 0,63–0,70 statt 0,04–0,07.
- Normiert auf Mittelwert 1: μ fast wirkungslos (KS 0,039–0,042 für Nullstellen 101–2000), Minimum bei
  2,85 bzw. 2,25; χ² +5,4 % (1–100) bzw. −9,9 % (101–2000).
- Asymptotisch: ρ_μ/ρ₁ = μ⁻¹(1 − log μ / log(t/2π)); nach Normierung bleibt ein Effekt ~1/log γ,
  bei γ ~ 10²² etwa 1 % — 21 % sind ausgeschlossen.
- Die im Companion genannten 75,8 % (100 Nullstellen) sind nicht reproduzierbar; das Originalskript
  `gue_frame_correction.py` fehlt.

**Stand nach K10:** P1 nach eigenem Kriterium nicht bestätigt; γ_L ist kein „GUE-Fixpunkt“, sondern
bleibt Eingabe (OP1). Guards unverändert.

### K11 — P2, P3 und Neueinordnung (2026-10-20)

Skript: `llm/k12_p2_p3.py`. Im Companion als Runde **v4.8.0-r09** (`sec:v480-r09-p2-p3-reclassification`).

**K11.1 P2 Koide-Phase — durch Daten ausgeschlossen (M).** Vorhersage θ_K = π − √2·arcsin β_sym =
132,8751°. Gemessen (m_τ = 1776,93 ± 0,09 MeV): 132,7325° ± 0,0004°. Abweichung +0,142° ≈ 300–400 σ.
Die „0,111 %“ sind klein relativ zum Winkel, aber groß relativ zum Messfehler. Gemessen θ_K = 2π/3 + 0,22223
(≈ 2/9, bekannter empirischer Befund). Die Herleitung von K = 2/3 über Cauchy–Schwarz trägt nicht
(liefert nur K ≥ 1/3).

**K11.2 P3 β-Formel — Koinzidenz (M).** (1/√3)·exp(−γ₁/(4πγ_L⁵)) = 0,549233 gegen β_sym = 0,549348
(−0,021 %); exakt erfüllt bei γ_L = 1,86366. Beziehung zwischen den Eingaben, keine unabhängige Vorhersage.
Exponent nachträglich von γ_L² auf γ_L⁵ geändert. Unter 56 gleich einfachen Formeln liegen 27 innerhalb
±5 %; Zufallswahrscheinlichkeit für einen Treffer in ±0,02 % ≈ 11 %.

**K11.3 Neueinordnung.** Register aller Vorhersagen P1–P6 und der Hauptsätze mit aktuellem Status steht
in r09 und als Kurzregister am Anfang dieser Karte. Ergebnis: Keine Vorhersage ist bestätigt; was trägt,
sind die strukturellen Ergebnisse.

### K12 — Koide-Struktur in Lesart B (2026-10-20)

Skript: `llm/k13_koide_lesart_b.py`. Im Companion als Runde **v4.8.0-r10** (`sec:v480-r10-koide-reading-b`).

**K12.1 Die Koide-Form ist eine Triole (M).** √m_k = A(1 + √2 cos(θ + 2πk/3)) ist exakt
v = t·(1,1,1) + √2·Re(c(1, ω, ω²)) mit t = A, c = |c|e^{iθ}. Allgemein K = (1 + |c|²/t²)/3,
also **K = 2/3 ⇔ |c| = t**. Gemessen: |c|/t = 0,999997, θ mod 2π/3 = 0,222225.

**K12.2 Lesart B legt nichts fest (M).** Für jede Triole s = 0 und N(q) = −t²; weder |c|/t noch arg c sind
bestimmt. Die Struktur liefert die richtige Form, keine Zahlen.

**K12.3 Kandidat für K = 2/3 (V).** |c| = t ⇔ jeder Kern einzeln lichtartig in der alten Pro-Kern-Norm
(−t² + |z_k|² = 0). Hängt am Faktor √2 der Brannen-Form (Konvention) — Kandidat, keine Herleitung.

**K12.4 Phase (M).** Kein vorab festgelegter kanonischer Winkel der Struktur (jπ/12, Hopf-Winkel, arcsin β,
arctan β, Tetraeder-/magischer Winkel …) ergibt 0,222225; am nächsten die ausgeschlossene P2-Formel.
2/9 ist kein rationales Vielfaches von π.

**K12.5 Dynamik fehlt (M/V).** Einzige quadratische Lorentz-Invarianten: Re(e^{−iφ}s) = cos φ(E² − B²) +
sin φ·2E·B (Maxwell + θ-Term); Dualitätsdrehung verschiebt φ um 2α. Die einfachste Dynamik von Lesart B
ist Elektromagnetik; der Dualitätswinkel erscheint als Vakuumwinkel (V). Für Massen braucht es ein
zusätzliches Prinzip, das |c|/t und arg c festlegt — **vor** dem Datenvergleich formuliert.

### K13 — Erster vorab festgelegter Test: δ = K/3 (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H1_Koide_Phase.md` (Commit 81f38d3, **vor** der Rechnung); Ergebnis
`llm/Ergebnis_H1_Koide_Phase.md`; Skript `llm/k14_test_h1.py`. Im Companion als **v4.8.0-r11**.

**K13.1 Hypothese (V, Autor).** 2/9 · 3/2 = 1/3, gelesen als δ = K · (1/3): Phase = Koide-Zahl durch Kernzahl
(oder · β²_Hopf; für Dreiergruppen gleich). Gegenhypothese H1′: δ = 2/9 fest.

**K13.2 Ergebnis (M).** Primärdaten (laufende Yukawas bei M_Z, Antusch/Hinze/Saad 2025):
Up-Quarks δ = 0,0518 vs. K/3 = 0,2959 (z = −322); Down-Quarks δ = 0,1001 vs. 0,2493 (z = −115);
Leptonen bei M_Z δ = 0,2211 vs. 0,2226 (z = −49). Nur Leptonen mit Polmassen verträglich (Kalibrierung).
**H1 und H1′ widerlegt.**

**K13.3 Einordnung.** δ ≈ K/3 ≈ 2/9 ist an die Polmassen der geladenen Leptonen gebunden, wie Koide selbst,
und kein Gesetz der Dreiergruppen. Das Verfahren (Vorab-Notiz, Commit, dann Rechnung) bleibt Standard
für jede künftige Vorhersage.

### K14 — Zweiter vorab festgelegter Test: Neutrinos als lichtartige Triole (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H2_Neutrino_Triole.md` (Commit 434c5a8, **vor** der Rechnung); Ergebnis
`llm/Ergebnis_H2_Neutrino_Triole.md`; Skript `llm/k15_test_h2.py`.

**K14.1 Hypothese (V).** r = 1 (K = 2/3) gilt für alle Leptonen, also auch für Neutrinos:
m_k = t²(1 + √2 cos(δ + 2πk/3))², Vorzeichen der v_k frei. Vorab offengelegt: Mit nur positiven Wurzeln ist
K ≤ 0,585 (NO) bzw. 0,500 (IO), H2 braucht ein negatives Vorzeichen. Nicht neu (Brannen 2006).

**K14.2 Ergebnis (M).** NuFIT 6.0 (IC24 + SK-atm). Je Ordnung genau eine Lösung, das leichteste v_k ist negativ.
NO: m = (0,36; 8,66; 50,1) meV, Σ = 0,0592 ± 0,0002 eV. IO: m = (2,9; 49,2; 49,9) meV, Σ = 0,102 eV.
Gegen Σ < 0,0642 eV (DESI DR2 + CMB): **NO verträglich, IO disfavorisiert.**

**K14.3 Einordnung.** H2 ist verträglich, aber schwach trennend: Σ liegt nur 0,4 meV über dem NO-Minimum (m₁ = 0).
Widerlegbar durch eine gemessene invertierte Ordnung (JUNO, DUNE) oder Σ ≳ 0,07 eV. Offen: Bedeutung des
negativen Vorzeichens (bei geladenen Leptonen sind alle v_k positiv).
**[Neueinordnung K26]** H2 ist „Koide mit Vorzeichen“: Mit nicht-negativen Wurzeln (v4.9-Konvention für das
physikalische K) ergeben die H2-Massen K = 0,525. JUNO 2026 stützt die NO-Vorhersage (K23).

**K14.4 Bedeutung des Vorzeichens (M, S; Skript `llm/k16_vorzeichen.py`).**
(a) Höchstens eine Komponente kann negativ sein. Das Vorzeichen ist das der kubischen Invariante
e₃ = v₀v₁v₂ = t³(1 − 3r²/2 + r³ cos 3δ/√2), für r = 1: t³(cos 3δ/√2 − 1/2). Negativ ⇔ δ jenseits der
Grenzphase π/12 (dort ist eine Masse exakt null). Auf dem r = 1-Kreis haben 75 % der Phasen eine negative
Komponente; „alle positiv“ ist der Sonderfall.
(b) Alle geladenen Dreiergruppen liegen knapp **innerhalb** des positiven Bogens (Leptonen 0,222 vs. 0,262;
Down 0,100 vs. 0,163; Up 0,052 vs. 0,057), daher das jeweils fast masselose leichteste Teilchen. Die Neutrinos
(0,479) liegen **jenseits** der Grenze. Das ist ein Ordnungsbefund, keine Erklärung.
(c) Lesart B gibt dem Vorzeichen keine Bedeutung: Die SO(3)-Invarianten von (v, (1,1,1)) sind |v| und der
45°-Winkel, für alle δ gleich. e₃ braucht den festen Generationen-Rahmen (S₃), also Flavour-Struktur, die das
Modell nicht liefert.
(d) Physikalisch ist das Vorzeichen von √m nicht beobachtbar: m = v² ist immer positiv; ein Massenvorzeichen
lässt sich chiral wegdrehen; die messbaren Majorana-Phasen betreffen das Vorzeichen von m, nicht von √m.
Bedeutung hätte es nur, wenn v selbst die fundamentale Größe ist (m als Quadrat einer Amplitude, z. B.
Seesaw m_ν ∝ m_D², Yukawaon-Modelle). [P] Eine Deutung (etwa Dirac ↔ Majorana oder θ = π im Triolenkern)
wäre eine neue Hypothese und braucht eine Vorab-Notiz.

### K15 — Dritter vorab festgelegter Test: Vorzeichen als Majorana-CP-Parität (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H3_Vorzeichen_Majorana.md` (Commit e3b140e, **vor** der Rechnung); Ergebnis
`llm/Ergebnis_H3_Vorzeichen_Majorana.md`; Skript `llm/k17_test_h3.py`.

**K15.1 Hypothese (V).** e₃ < 0 ⇔ Majorana; die Triolen-Vorzeichen sind die CP-Paritäten (η = −1, +1, +1),
keine weiteren Majorana-Phasen.

**K15.2 Ergebnis (M).** NuFIT 6.0 (IC24 + SK-atm, NO). m_ββ = 2,74 ± 0,70 meV (MC), 1,25–3,47 meV über den
vollen δ_CP-Bereich, 95 %-Obergrenze 3,50 meV. Mit η₁ = +1 wäre m_ββ rund 0,5 meV größer. m_β = 8,85 meV.

**K15.3 Einordnung.** Verträglich (KamLAND-Zen 28–122 meV), auf absehbare Zeit nicht prüfbar; das Vorzeichen
selbst wirkt weniger als die δ_CP-Unsicherheit. Widerlegt durch ein 0νββ-Signal über 3,5 meV oder durch
Dirac-Neutrinos. Ausbleibende Signale bei LEGEND-1000/nEXO bestätigen nichts.

### K16 — Vierter vorab festgelegter Test: TM1 gegen TM2, 1:1 (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H4_TM1_gegen_TM2.md` (Commit 00d297e); Ergebnis `llm/Ergebnis_H4_TM1_gegen_TM2.md`;
Skript `llm/k18_test_h4.py`.

**K16.1 Ausgangspunkt (M).** Die Triolen-Form ist das Spektrum einer hermiteschen zyklischen Matrix; deren
Eigenvektoren sind feste Fourier-Vektoren. Die naive Mischung daraus ist ausgeschlossen (θ₁₃ ≈ 35°).
Minimalvarianten: TM2 erhält (1,1,1)/√3 (Skalar-Richtung), TM1 erhält (2,−1,−1)/√6 (Triolen-Ebene).
Beide mit gleichem Vorab-Gewicht, ohne freie Parameter über θ₁₃, θ₂₃ hinaus. Offengelegt: θ₁₂-Teil nicht blind.

**K16.2 Ergebnis (M).** NuFIT 6.0, NO, Gauß-Näherung: χ²(TM1) = 4,4, χ²(TM2) = 14,7 (2 FG), Δχ² = 10,3
(etwa 170 : 1). Blinder Teil δ_CP allein: Δχ² = 2,8 für TM1. **TM1 stark bevorzugt, TM2 disfavorisiert.**

**K16.3 Einordnung.** Die naheliegende Skalar-Richtung verliert. Warum die Triolen-Ebene eine Spalte
auszeichnet, ist offen. Festgeschrieben für TM1: sin²θ₁₂ = 0,318 (JUNO prüft bald auf etwa 0,5 %; bei
Mittelwert 0,308 wäre auch TM1 ausgeschlossen), δ_CP = 259–267° (DUNE, Hyper-K).

**K16.4 Überlagerung von TM1 und TM2 (M; Skript `llm/k19_tm_ueberlagerung.py`, reine Strukturrechnung).**
(a) Beide Spalten exakt erhalten erzwingt durch Unitarität die dritte: tribimaximal, |U_e3|² = 0 —
ausgeschlossen (gemessen 0,022). (b) Überlagerung = erhalten bleibt w = cos a · (1,1,1)/√3 − sin a · e^{ib}
(2,−1,−1)/√6 (a = 0: TM2, a = 90°: TM1). Gleichgewicht 1:1 (a = 45°): |U_e|² von w ist 0,029 (b = 0),
0,500 (b = 90°) oder 0,971 (b = 180°); keiner passt zu ν₁ (0,677) oder ν₂ (0,301) — ausgeschlossen.
(c) Mit freiem Gewicht passt θ₁₂ immer, und zwar bei a = 90,6° (fast reines TM1) oder a = 2,0° (fast reines
TM2); θ₁₂ ist dann Eingabe, kein Test. Die Daten verlangen also keine echte Überlagerung, sondern fast reine
Endpunkte. Zwischen „TM1“ und „TM2 + 2° Beimischung“ entscheidet erst δ_CP.

### K17 — Fünfter vorab festgelegter Test: Hopf-Winkel als Mischwinkel (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H5_Hopf_Mischwinkel.md` (Commit 16eff15); Ergebnis `llm/Ergebnis_H5_Hopf_Mischwinkel.md`;
Skript `llm/k20_test_h5.py`.

**K17.1 Zuordnung (M).** Die erhaltene Spalte w = cos a · c₂ − sin a · e^{ib} · c₁ ist ein Punkt auf S³; die
Hopf-Abbildung gibt den S²-Punkt mit Polwinkel 2a, Azimut b. TM2 = Nordpol, TM1 = Südpol, 1:1 = Äquator.

**K17.2 Hypothese (V) und Ergebnis.** Polwinkel = Hopf-Winkel des Companion (66,64° oder 70,53°, auch gespiegelt).
(i) kanonische Azimute: 0 von 32 verträglich (bestes χ² = 92; Zufallserwartung 0,6) — **widerlegt**.
(ii) freier Azimut: χ² = 3,74, δ_CP = 262°, aber für alle Polwinkel identisch — **entartet, kein Test**.

**K17.3 Strukturbefund (M).** Für jede Spalte in span(c₁, c₂) gilt |w_μ| = |w_τ| und |w_e|² = sin²(γ/2), γ =
Abstand auf der Hopf-Sphäre zum Punkt E (Polwinkel arccos(1/3) = 70,53°, b = 0; dort ist w_e = 0). Die ganze
Familie hängt physikalisch nur von γ ab.

**K17.4 Nachbefund (nicht vorab registriert, wie P3).** Als ν₂ verlangen die Daten γ = 66,57°; der Companion-Winkel
θ_H = 66,64°. Gleichwertig |U_e2|² = β_sym², sin²θ₁₂ = 0,3086 (gemessen 0,308). Kein Beleg (nachträglich,
β_sym eingesetzt, viele Konstanten). Trennt aber bei JUNO klar von TM1 (0,318); wäre vor JUNO als eigene
Vorab-Notiz festzuschreiben.

### K18 — Rückwärtsanalyse: Was müsste sich ändern, damit Bekanntes herauskommt? (2026-10-20)

Regel: Jede Änderung kostet Stellschrauben; sie lohnt nur, wenn sie mehr Messwerte erklärt, als sie Schrauben
hinzufügt.

| Lücke | minimale Änderung | Kosten | Gewinn |
|---|---|---|---|
| Lepton-Phase δ = 2/9 | Mechanismus für die Phase (nur Leptonen, H1 widerlegt allgemein) | 0, falls hergeleitet | Elektron/Myon-Verhältnis |
| Quarks r = 1,115 / 1,290 | r als Funktion von Ladung/Farbe | 1 Formel für 2 Zahlen | nur bei einer Formel für beide |
| Mischung TM1 | Restsymmetrie Z₂ für Neutrinos, Z₃ (Triole) für geladene Leptonen, aus S₄ | Gruppe + Brechungsmuster | θ₁₂, δ_CP-Relation |
| Massenskala t | Dynamik (Higgs/Yukawa) | offen | absolute Massen |
| β_sym | Herleitung (OP1) statt Barbero–Immirzi | 0 | ganze Frame-Kette |

**K18.1 Befund (M, nachgerechnet).** GL(3,2) (= Symmetrie der Fano-Ebene) hat Ordnung 168; der Stabilisator eines
Punkts hat Ordnung 24 und dieselbe Ordnungsstatistik wie S₄ (1, 9, 8, 6 Elemente der Ordnung 1, 2, 3, 4).
**K18.2 Weg (V).** S₄ ist die übliche Flavour-Gruppe für TBM/TM1. Die Fano-Ebene ist im Companion bereits
vorhanden (Oktonionen-Multiplikation, Triolen-Satz über konkurrente Fano-Linien, r04). Eine Flavour-Symmetrie
aus dem Punkt-Stabilisator der Fano-Ebene wäre also keine von außen geholte Zutat. Offen: Brechungsmuster
herleiten, dann TM1 oder TM2 vorhersagen — vor dem Datenvergleich festzulegen.

**K18.3 Wie die Fano-Symmetrie bricht (M; Skript `llm/k21_fano_brechung.py`, ohne Datenvergleich).**
Ein fester Punkt P und eine Linie L nicht durch P zerlegen die 7 Punkte in {P} ∪ L ∪ R (R = 3 Punkte, nicht auf
einer Linie). Das Dreier-Element von Stab(P) ≅ S₄ fixiert P und L und vertauscht L und R zyklisch. Die neun
Involutionen zerfallen nach Fano-Geometrie in drei Klassen zu je 3; ihre erhaltene Spalte (in der Eigenbasis des
Dreier-Elements):
- Zentrum = P (S₄-Doppeltranspositionen): (1/3, 1/3, 1/3) → **TM2**;
- Achse durch P, Zentrum auf L: (0, 1/2, 1/2) → dritte TBM-Spalte (erzwingt θ₁₃ = 0, ausgeschlossen);
- Achse durch P, Zentrum in R: 2/3 auf der Eigenwert-1-Richtung, 1/6, 1/6 → **TM1**.
Die drei TBM-Spalten entsprechen also genau den drei Lagen des Zentrums.

**K18.4 Übersetzung in den Companion (M, Konventionen aus r04).** Linien (1,2,3), (1,4,5), (1,6,7), (2,4,6),
(2,5,7), (3,4,7), (3,5,6). Mit P = e₇ (SU(3)-Singulett) und L = {e₁,e₂,e₃} (Anti-Triplett) ist R = {e₄,e₅,e₆},
das Generationen-Triplett; die Companion-Zyklik e₄→e₅→e₆ ist ein Fano-Automorphismus dieses Typs (nachgeprüft).
Damit: TM2 = Restsymmetrie mit Zentrum im Singulett e₇; TM1 = Restsymmetrie mit Zentrum in einer
Generationen-Einheit e₄, e₅ oder e₆; die ausgeschlossene Variante = Zentrum im Anti-Triplett.
[S] Annahmen: Elektron = Eigenwert-1-Richtung des Dreier-Elements (Standardkonvention); die 3-dim. Darstellung
stammt aus der Wirkung auf die 4 Linien nicht durch P. Ob die G₂-Wirkung auf das Triplett (mit den Vorzeichen
der Gruppe 2³·GL(3,2)) dieselbe Darstellung liefert, ist **ungeprüft**. [V] Welche Klasse das Modell auswählt,
ist offen; beide Kandidaten (e₇ oder Generationen-Einheit) sind modellintern naheliegend.
**→ Die Zuordnung in K18.3–4 ist durch K18.5 überholt** (sie galt nur für die Ersatz-Darstellung, nicht für die
echte Oktonionen-Wirkung).

**K18.5 Echte G₂-Wirkung auf das Triplett (M; Skript `llm/k22_oktonion_triplett.py`).** Oktonionen nach
Companion-Konvention (Fano-Linien aus der Multiplikation reproduziert). Die Automorphismen, die e₁…e₇ bis aufs
Vorzeichen permutieren, bilden eine Gruppe der Ordnung 1344 (2³·GL(3,2)). Ihr Stabilisator von +e₇ (Teil von
SU(3) ⊂ G₂) hat Ordnung 96, wirkt unitär mit Determinante 1 und irreduzibel auf ℂ³ = span(e₄,e₅,e₆) und hat
dieselbe Ordnungsstatistik und Klassenzahl (10) wie **Δ(96)**, eine bekannte Flavour-Gruppe. Die 15 Involutionen
(Dreier-Element = Companion-Zyklik e₄→e₅→e₆, Elektron = Eigenwert-1-Richtung):

| Fano-Zentrum | Anzahl | erhaltene Spalte | Muster |
|---|---|---|---|
| keins (reine Vorzeichenwechsel, z. B. e₄, e₅ → −, e₆ fest) | 3 | (1/3, 1/3, 1/3) | TM2 |
| e₁, e₂, e₃ (erster Lift) | 3 | (2/3, 1/6, 1/6) | **TM1** |
| e₁, e₂, e₃ (zweiter Lift) | 3 | (0, 1/2, 1/2) | θ₁₃ = 0, ausgeschlossen |
| e₄, e₅, e₆ | 6 | (1/3, (2−√3)/6, (2+√3)/6) | Δ(96)-Spalte |
| e₇ | — | nur Lifts der Ordnung 4, keine Involution | — |

Befund: TM1 und die ausgeschlossene Variante haben dieselbe Fano-Lage (Zentrum im Anti-Triplett); sie
unterscheiden sich **nur durch die Oktonionen-Vorzeichen**. Die Fano-Geometrie allein trennt sie nicht; die
Vorzeichenstruktur der Oktonionen tut es. TM2 entsteht aus reinen Vorzeichenwechseln, die eine Generation
festhalten. Die Δ(96)-Spalte hätte mit dieser Konvention als ν₂ einen der Einträge |U_μ2|², |U_τ2|² bei 0,045;
gemessen sind beide etwa 0,2 oder größer (3σ-Bereiche); sie scheidet für ν₂ aus (grobe Prüfung, kein Fit). [V] Offen bleibt, welcher Lift ausgewählt wird.

### K19 — Sechster vorab festgelegter Test: Kriterien für die Auswahl des Lifts (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H6_Lift_Kriterien.md` (Commit e1e2393); Ergebnis `llm/Ergebnis_H6_Lift_Kriterien.md`;
Skript `llm/k23_test_h6.py`.

**K19.1 Ergebnis (M).** Die Triole e₄→e₅→e₆ hat 4 Lifts der Ordnung 3, einer vorzeichenfrei; alle Befunde sind
für alle Lifts gleich. Hauptkriterium A (h g₃ h = g₃⁻¹, Diedergruppe S₃) gilt für die θ₁₃ = 0-Lifts, nicht für
TM1: **Hauptkriterium spricht gegen TM1.** Nebenkriterium C trennt umgekehrt: ⟨g₃, h_TM1⟩ hat Ordnung 24 mit
S₄-Ordnungsstatistik, ⟨g₃, h_θ₁₃=0⟩ ist S₃. B, D–G trennen nicht; H fällt mit A zusammen.

**K19.2 Einordnung (S).** Minimalität (S₃) gibt θ₁₃ = 0 und ist empirisch widerlegt; TM1 entspricht
Vollständigkeit (Triole und Restspiegelung erzeugen den ganzen Fano-Punkt-Stabilisator S₄). Dieses Prinzip ist
nachträglich gefunden und zählt nur, wenn es sich unabhängig begründen lässt. **→ Deutung korrigiert in K19.3.**

**K19.3 Prüfung: Erzwingt die Kaskade Vollständigkeit? (M; Skript `llm/k24_kaskade_vollstaendigkeit.py`)**
(a) *Korrektur:* ⟨g₃, h_TM1⟩ (Ordnung 24) hat als Fano-Bild nur S₃ (6 Elemente, dasselbe wie ⟨g₃, h_θ₁₃=0⟩)
und enthält den ganzen Vorzeichen-Kern V (4 Elemente): 24 = 4 · 6. Es ist **nicht** der Fano-Punkt-Stabilisator.
Den vollen Fano-Stabilisator erreicht nur die Δ(96)-Spiegelung (erzeugt ganz Stab(+e₇)). Richtig: TM1 ⇔ die
Gruppe enthält die Oktonionen-Vorzeichen-Symmetrien; θ₁₃ = 0 ⇔ sie enthält keine.
(b) *Vorzeichen-Kern:* Jedes Kern-Element ist auf einer der drei quaternionischen Linien durch e₇ die Identität
und auf den beiden anderen die e₇-Konjugation (Drehung um π um e₇).
(c) *Kaskade:* Die Projektionen auf span(1, L) für L durch e₇ und auf span(1, e₇) kommutieren mit allen
Kern-Elementen. TM1-Lift und θ₁₃ = 0-Lift über demselben Fano-Bild unterscheiden sich genau um ein Kern-Element
und wirken auf alle Kaskaden-Projektionen gleich. **Die Kaskade sieht den Unterschied nicht und kann
Vollständigkeit nicht erzwingen. Vermutung widerlegt.**
(d) *Offen (V):* Ein Auswahlgrund müsste aus der Multiplikation selbst kommen, nicht aus Projektionen. Im
Companion treten Vorzeichen-Automorphismen bisher nur bei der reparierten J-Spiegelung auf (K6.2: muss vier
Einheiten negieren und eine Linie festhalten); ob das hier hilft, ist ungeprüft. → geprüft in K20.

### K20 — Siebter vorab festgelegter Test: Heisenberg-Kompensator als Auswahlkriterium (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H7_Heisenberg_Kompensator.md` (Commit e6da7db); Ergebnis
`llm/Ergebnis_H7_Heisenberg_Kompensator.md`; Skript `llm/k25_test_h7.py`.

**K20.1 Ergebnis (M).** J als Vorzeichen-Automorphismus (alle 7 Kandidaten, Haupt: negiert e₁, hält e₇ — Linien
(2,5,7), (3,4,7)). Für alle J und alle vier Triolen-Lifts gilt: Kommutieren mit h (K1), J-Eigenvektor (K2) und
J-gerade Spalte (K3) verhalten sich für TM1- und θ₁₃ = 0-Lift gleich. **Kein Auswahlgrund aus dem Kompensator.**
Grund (vorab offengelegt, bestätigt): Die beiden Lifts unterscheiden sich um ein Element der abelschen
Vorzeichengruppe.

**K20.2 Nebenbefunde (M).** (a) Die Haupt-Kandidaten für J kommutieren nicht mit der Triole. (b) Einziger
Vorzeichen-Automorphismus, der mit der Triole kommutiert: feste Linie (1,2,3), negiert e₄…e₇ = Cayley–Dickson-
Involution p + qℓ ↦ p − qℓ. Sie kommutiert mit allen Triolen-Lifts und allen sechs TM1-/θ₁₃ = 0-Involutionen
(24 von 96 Elementen von Stab(+e₇)), negiert e₇ und wirkt auf dem Triplett antilinear (CP-artig).
[V] Als verallgemeinerte CP-Symmetrie könnte sie CP-Phasen festlegen; das wäre eine neue Hypothese (H8) mit
eigener Vorab-Notiz. → geprüft in K21.

### K21 — Achter vorab festgelegter Test: Cayley–Dickson-Involution als CP-Symmetrie (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H8_CP_Cayley_Dickson.md` (Commit f6734ab); Ergebnis `llm/Ergebnis_H8_CP_Cayley_Dickson.md`;
Skript `llm/k26_test_h8.py`.

**K21.1 Struktur (M).** Auf dem Triplett wirkt die Involution als z ↦ −z̄ (X = −1) in der Basis, in der die Triole
die reine zyklische Vertauschung ist. Massenmatrix hᵀ m h = m, Xᵀ m X = m* ⇒ m reell, Lösungsraum Dimension 4.
In der Massenbasis der geladenen Leptonen wird daraus die μ-τ-Spiegelung: **sin²θ₂₃ = ½ und δ_CP ∈ {90°, 270°}
exakt** (2000 Stichproben je Typ; gilt für TM1- und TM2-Spiegelungen). Mit TM1: sin²θ₁₂ = 0,318.

**K21.2 Datenvergleich (M).** NuFIT 6.0 NO, ein Winkel angepasst: χ²_min = 8,82 bei 3 FG (θ₁₂ 0,73; θ₂₃ 3,11;
δ_CP 4,98 mit δ = 270°). Nach Kriterium: **Spannung** (zwischen 95 % und 99 %).

**K21.3 Einordnung.** Erste Stelle, an der eine schon vorhandene Struktur des Modells (Cayley–Dickson-Verdopplung)
ohne Zusatzannahme scharfe, bald prüfbare Werte liefert: θ₂₃ = 45°, δ_CP = 270°. Die μ-τ-Spiegelung selbst ist
bekannt; die Wahl 270° statt 90° trifft der Datenvergleich. Gauß-Näherung überzeichnet die Spannung eher.
m_ββ (H2-Massen, reelle Paritäten): 3,56 meV für (−1, +1, +1), 1,34–4,05 meV insgesamt.

### K22 — Companion-Runde v4.8.0-r12 und Neueinordnung der alten PMNS-Aussagen (2026-10-20)

Runde `sec:v480-r12-neutrino-flavour` (Snippet `llm/v480_r12_round.tex`): Theoremlets r12.1 (Triolen-Produkt und
Vorzeichen, zyklische Matrix), r12.2 (Stab(+e₇) mit Δ(96)-Invarianten), r12.3 (Involutionen-Tabelle), r12.4
(Cayley–Dickson-CP ⇒ θ₂₃ = 45°, δ_CP ∈ {90°, 270°}); Tabelle H2–H8 mit Commits.

**Neueinordnung (S).**
- `prop:pmns-z3`: arctan√2 = 54,74° ist **nicht** der maximale Mischungswinkel (der ist 45°). Der verschobene Wert
  52,1° gibt sin²θ₂₃ = 0,622 gegen 0,470 (NO, θ₂₃ = 43,3°): etwa 9σ, gegen IO (0,550) etwa 6σ.
  → **widerlegt**, ebenso die θ₂₃-Zeile der Vorhersagetabelle. Ersatz: r12.4 mit offener Auswahlfrage.
- `thm:op1op4-unified`: CKM- und PMNS-Zeile hängen an der δ_CL-Vermutung, deren β-Formel in r09 als Koinzidenz
  eingestuft ist. CKM-Zeile erbt diesen Status; PMNS-Zeile widerlegt. CKM-Phase (π/3 gegen ≈ 70°) unberührt, offen.
- Ledger: R_mix^{r12} = (0,0,1); Guards unverändert, β₄ = 1/256 unverbraucht.

### K23 — Nachprüfung mit JUNO 2026 und Vorab-Notiz H9 (2026-10-20)

Daten: JUNO, arXiv:2609.37895 (29.09.2026, 207,2 Tage): sin²θ₁₂ = 0,3036 ± 0,0064, Δm²₂₁ = 7,388(78)·10⁻⁵ eV²,
Δm²₃₁ = +2,509·10⁻³ eV² (NO), NO bevorzugt mit ≥ 2,1σ. Lag beim Festschreiben von H2–H8 vor, war aber nicht
bekannt (Datenbasis NuFIT 6.0) → unabhängige Nachprüfung. Dokument `llm/Nachpruefung_JUNO_2026.md`.
Kombiniert mit NuFIT 6.0: sin²θ₁₂ = 0,3046 ± 0,0056.

**K23.1 Ergebnisse (M).** H2: Σ = 0,0591 eV (NO), NO-Vorhersage gestützt. H4: χ²(TM1) = 9,6, χ²(TM2) = 49,1 —
TM1 weit vor TM2, aber für sich **disfavorisiert**. H8: χ² = 14,0 bei 3 FG — **disfavorisiert**. Ursache:
TM1 verlangt sin²θ₁₂ = 0,3182, gemessen 0,3046 (2,4σ).

**K23.2 H9 (V, Vorab-Notiz b75170d).** sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0,30862 ± 0,00018 (γ_BI = 0,2375 eingesetzt).
Nachträglich gefunden (K17.4); heutiger Abstand zu JUNO 0,8σ zählt nicht. Getestet wird die nächste
JUNO-Veröffentlichung mit σ ≤ 0,004: |z| < 2 verträglich, ≥ 3 widerlegt.

### K24 — Neunter vorab festgelegter Test: Assoziator als Auswahlkriterium (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H10_Assoziator.md` (Commit a6b5bcb); Ergebnis `llm/Ergebnis_H10_Assoziator.md`;
Skript `llm/k27_test_h10.py`.

**K24.1 Strukturbefund (M).** [e₄,e₅,e₆] = −2e₇: Der Assoziator des Generationen-Tripels zeigt auf das
SU(3)-Singulett (Kaskaden-Ende, komplexe Struktur der Lesart B). Fano-Linien haben Assoziator 0, Nicht-Linien
Norm 2. Jedes Element von Stab(+e₇) erhält ihn.

**K24.2 Ergebnis (M).** Kriterien S1 (Haupt: [x, h(x), e₇] = 0), S2, S3, S4 trennen für keinen der vier
Triolen-Lifts zwischen TM1- und θ₁₃ = 0-Lift. **Kein Auswahlgrund.** Damit wählen weder Minimalität (H6),
Kaskade (K19.3), Kompensator (H7) noch Assoziator (H10) den TM1-Lift; nach JUNO 2026 ist TM1 ohnehin
disfavorisiert (K23).

### K25 — Prüfung: Quark-Werte aus der Oktonionen-Struktur? (2026-10-20)

Dokument `llm/Pruefung_Quarks_Oktonionen.md`. Kein Datenvergleich, keine Vorhersage.

**K25.1 Zielwerte schemaabhängig (M).** r_u = 1,2895 (M_Z) bzw. 1,2435 (PDG-Standardskalen), r_d = 1,1151 bzw.
1,0926: Spanne 3,6 % bzw. 2,0 %, rund hundertmal größer als der statistische Fehler. Koide gilt bei Leptonen nur
für Polmassen; Quarks haben keine sauberen Polmassen. In x = r² − 1 treffen zufällige Konstanten die Bänder mit
etwa 12 % bzw. 5 %. Strukturtreffer wären Zufall; **es wird nicht gefittet.**

**K25.2 Farbe = Generation im Companion (S).** `thm:three-generations` legt die Generationen auf e₄, e₅, e₆, das
Triplett unter SU(3) ⊂ G₂, und gibt jeder Generation einen Farbindex. In der Dixon-Lesart ist dieses SU(3) die
Farbgruppe. Folgen: (a) Quarks brauchen 3 × 3 Zustände, ein Triplett reicht nicht. (b) Die r12-Flavour-Analyse
(Δ(96), TM1/TM2, Cayley–Dickson-CP) ist mathematisch richtig, setzt physikalisch aber „Triplett = Generationen“
voraus; als Farbe gelesen würde eine gebrochene Flavour-Symmetrie in SU(3)_c die Farbe brechen.
**Ergebnis:** Quark-Werte aus der jetzigen Struktur nicht ableitbar; zuerst müssen Farbe und Generation getrennt
werden.

### K26 — Abgleich mit der GitHub-Linie v4.9.0-Kandidat (2026-10-20)

Dokument `llm/Abgleich_v49_Linie.md`; GitHub `main` 651b624, `sources/research/parts/`.

**K26.1 Übereinstimmungen (S).** Koide als Gleich-Norm-Bedingung ohne Herleitung (v4.9 `v480:koide-equal-norm` =
r10); **Phasenkammern |θ − 2πj/3| ≤ π/12 unabhängig gleich gefunden** (v4.9 `v480:generation-phase-chambers` =
K14.4, inkl. leichtem Teilchen nahe der Grenze); Phasen-Ansatz π − √2 arcsin β verworfen (= r09/r11);
Riemann/GUE nicht als Satz (= r04/r05); β_sym = 0,5493482 mit γ_BI = 0,2375 (= H9).

**K26.2 Spannungen (S).** (a) v4.9 lässt für das physikalische K nur nicht-negative Wurzeln zu; H2/H3 testen
„Koide mit Vorzeichen“ außerhalb dieses Bereichs (nicht-negatives K der H2-Massen: 0,525). Kein mathematischer
Widerspruch, aber H2/H3 sind so zu benennen. (b) Beide Linien legen Farbe und Generation auf dasselbe Triplett
(K25.2 betrifft auch v4.9). (c) Die Θ-Summe führt v4.9 als offen; r05 hat die Vermutung widerlegt.

**K26.3 Empfehlungen.** v4.9: r04/r05 und K25.2 übernehmen. Lokal: H2/H3 umbenennen, v4.9-Kammern als
unabhängige Bestätigung zitieren. Zusammenführung über Entwurf-PR #19 (berührt keine v4.9-Datei).

### K27 — Companion-Runde v4.8.0-r13 (2026-10-20)

Runde `sec:v480-r13-juno-associator-colour` (Snippet `llm/v480_r13_round.tex`) hält K23–K26 fest: Nachprüfung mit
JUNO 2026 (Tabelle H2/H4/H8), H9 (b75170d), Theoremlet r13.1 [e₄,e₅,e₆] = −2e₇ mit Beweis aus der Multiplikation,
H10 (a6b5bcb), Farbe/Generation (Folgen für r12 und für Quarks, Schemaabhängigkeit), Abgleich mit v4.9 (H2/H3 als
Koide mit Vorzeichen neu eingeordnet). Ledger R_mix^{r13} = (0,0,1,1); Guards unverändert, β₄ unverbraucht.

### K28 — Trennung von Farbe und Generation (2026-10-20)

Dokument `llm/Trennung_Farbe_Generation.md`; Skript `llm/k28_sedenion_generationen.py`. Modellbau, kein Datenvergleich.

**K28.1 Weg A, Sedenionen (M).** Aut(𝕊) = G₂ × S₃ (Gillard–Gresnigt) in der Companion-Konvention bestätigt: ψ
(120°-Drehung in den sieben Ebenen (eᵢ, eᵢ₊₈)) und ε (a + b·e₈ ↦ a − b·e₈) erzeugen S₃ und vertauschen mit ganz
G₂; Farbalgebra Stab(e₇) hat Dimension 8. Triolen-Relation 1 + ψ + ψ² = 0 auf 14 Richtungen. Aber
𝕊 = 1 ⊕ sgn ⊕ 7·(Dublett): farbige Zustände tragen nur das S₃-Dublett; die 9 Zustände ψᵏ(e_c) haben Rang 6.
**Nur zwei unabhängige farbige Generationen**; die Triolen-Relation selbst erzwingt die Abhängigkeit.

**K28.2 Weg B, Triality (M).** t(x,y,z) = Re((xy)z) auf 𝕆 ⊕ 𝕆 ⊕ 𝕆 ist zyklisch invariant (ℤ₃-Triole), invariant
unter (x,y,z) → (x̄,z̄,ȳ) (zusammen S₃) und unter diagonalem G₂ (vertauscht mit S₃). 3 Farben × 3 Generationen:
**Rang 9**. Passt zu Abschnitt 3 (S₂ = 𝕆P¹ ↔ drei Generationen; G₂ = Triality-Fixgruppe in Spin(8)).

**K28.3 Empfehlung (V).** Weg B: Generationenindex = Triality-Platz, Farbindex = SU(3)-Triplett je Platz.

**K28.4 Folgen (S).** Δ(96) ⊂ SU(3) liegt danach in der Farbgruppe, ist also keine Flavour-Symmetrie:
r12.2–r12.4 bleiben Mathematik, verlieren ihre Mischungs-Lesart (H4/H8 ohnehin disfavorisiert, K23). Reine
Generationen-S₃ mit ℤ₃ (Triole) und Transposition gibt die Spalte (0, ½, ½), also θ₁₃ = 0 (= H6-Minimalität);
Mischung braucht weitere Brechung. Die Triolen-Form ist die S₃-Zerlegung Singulett ⊕ Dublett; K = 2/3 bleibt
Gleich-Norm-Bedingung ohne Herleitung.

### K29 — Companion-Runde v4.8.0-r14 (2026-10-20)

Runde `sec:v480-r14-colour-generation` (Snippet `llm/v480_r14_round.tex`) hält K28 fest: Anforderungen (a)–(c),
Theoremlet r14.1 (Sedenionen, G₂ × S₃, 𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2), Rang 6), Theoremlet r14.2 (Triality-Form,
Beweis über Re-Teil des Assoziators, Rang 9), vorgeschlagene Zuordnung (V), Folgen für r12/r13. Dass
Aut(𝕊) genau G₂ × S₃ ist, wird aus der Literatur übernommen, nicht neu bewiesen. Ledger R_cg^{r14} = (0,1,1);
Guards unverändert, β₄ unverbraucht.

### K30 — Träger der Triality-Plätze: die oktonionische Hopf-Faserung (2026-10-20)

Dokument `llm/Traeger_Triality_Hopf.md`; Skript `llm/k29_hopf_triality_traeger.py`. Modellbau, kein Datenvergleich.

**K30.1 (M).** Die Hopf-Abbildung h(x,y) = (|x|² − |y|², 2xȳ) aus `thm:hopf` ist das Triality-Produkt. Die
Einheits-Tripel {(a,b,c) : (ab)c = 1} sind zyklisch (Triole) und unter (a,b,c) → (ā,c̄,b̄) abgeschlossen (S₃),
Dimension 14, G₂-diagonal invariant. Über dem Äquator von 𝕆P¹ ist (√2·x, √2·ȳ, v̄) mit v = 2xȳ ein Einheits-
Tripel; die Faser über v ist {(a, ā·v)} ≅ S⁷. Die drei Plätze sind die beiden Totalraum-Komponenten und der Basispunkt.

**K30.2 (M).** Symmetrischer Punkt a = b = c ⇔ a³ = 1, a = exp(2πu/3). Für u = e₇ ist a = ω in span(1, e₇); sein
Stabilisator in G₂ hat Dimension 8 = SU(3), die Farbgruppe. Generationen-Symmetriepunkt und Farbgruppe hängen über
e₇ zusammen.

**K30.3 Probe (M).** In span(1, e₇) wird (ab)c = 1 zu α₁ + α₂ + α₃ ≡ 0. Koide-Phasen δ + 2πk/3 verlangen dann
3δ ≡ 0; gemessen 3δ = 0,667 → direkte Lesart scheitert. (3δ ≈ 2/3 ist die bekannte 2/9-Zahl, in r11 als nicht
allgemein widerlegt; zählt nicht.) **Offen:** Massenhierarchie aus Abweichungen vom symmetrischen Tripel.

### K31 — Companion-Runde v4.8.0-r15 (2026-10-20)

Runde `sec:v480-r15-hopf-triality-carrier` (Snippet `llm/v480_r15_round.tex`) hält K30 fest: Theoremlet r15.1
(Einheits-Tripel 𝒯, Hopf-Abbildung, Äquator-Faser), Theoremlet r15.2 (symmetrischer Punkt, Stabilisator SU(3)),
Probe der Koide-Phasen (scheitert). Ledger R_cg^{r15} = (0,0,1); Guards unverändert, β₄ unverbraucht.
Build 3 Läufe, Audit gegen r14 ohne harte Abweichung.

### K32 — Elfter vorab festgelegter Test H11: Massen aus dem Tripel-Raum (2026-10-20)

Vorab-Notiz `llm/Vorab_Notiz_H11_Massen_Tripelraum.md` (Commit 8e5eaa9), Ergebnis `llm/Ergebnis_H11_Massen_Tripelraum.md`,
Skript `llm/k30_test_h11.py`. Ablesung (verbindlich): √m_k ∝ n_k = |Platz k|.

**K32.1 H11a (M).** Die Triality-Form t = Re((ab)c) hat bei fester Gesamtnorm ihre Extrema bei gleichen Normen
(K = 1/3, t = ±1); die übrigen kritischen Punkte haben zwei leere Plätze (K = 1).

**K32.2 H11b (M).** Für V = αS + βS² + γQ − κt (allgemeinstes G₂ × S₃-invariantes Potential bis Grad 4) erfüllt
x_k = n_k² an jedem kritischen Punkt mit n_k ≠ 0 dieselbe quadratische Gleichung (2α + 4βS)x + 4γx² = κP. Also höchstens
zwei verschiedene Normen. Gitter (210 Punkte): 180 × gleiche Normen, 25 × ein besetzter Platz, 5 × flach, 0 × drei
verschiedene.

**K32.3 Urteil (S).** H11a und H11b **widerlegt** nach dem festgelegten Kriterium. Toleranz für „verschieden“ von 10⁻⁶ auf
10⁻⁴ geändert (offengelegt; das Urteil folgt analytisch, unabhängig davon). Mindestgrad für drei verschiedene Normen: 6
[Neu eingeordnet durch K70: gilt für kritische Punkte; für Minima ist Grad 6 nicht ausreichend, nötig ist Grad ≥ 8.]
(notwendig, nicht als hinreichend gezeigt). Jede Erweiterung bringt ≥ 2 neue Parameter, also Anpassung statt Vorhersage.

**K32.4 Neueinordnung.** K30.3 „offen: Hierarchie aus Abweichungen vom symmetrischen Tripel“ ist für natürliche
Invarianten bis Grad 4 negativ beantwortet. Der Massenmechanismus bleibt offen (P); die Triole liefert weiterhin die
Form (K12), nicht die Dynamik.

### K33 — Companion-Runde v4.8.0-r16 (2026-10-20)

Runde `sec:v480-r16-triple-space-masses` (Snippet `llm/v480_r16_round.tex`) hält K32 fest: Rahmen und Hypothesen
H11a/H11b mit festem Kriterium, Theoremlet r16.1 (dieselbe quadratische Gleichung für alle x_k, höchstens zwei
Normen), Gitterbefund, offengelegte Toleranz-Abweichung, Urteil (widerlegt, Mindestgrad 6). Ledger R_cg^{r16} = (0,0,1);
Guards unverändert, β₄ unverbraucht. Build 3 Läufe (1084 Seiten), Audit gegen r15 ohne harte Abweichung.

### K34 — Zeitrichtung der kosmologischen Anteile (2026-10-21)

Konsistenzprüfung, keine neue Vorhersage, daher ohne Vorab-Notiz. Skript `llm/k31_kosmologie_vorzeichen.py`.

**K34.1 Die drei Aussagen (M).** thm:dark-energy: Ω_Λ = 1 − β_sym², Ω_M = β_sym². prop:H0-tension: β_sym steigt von
0,527 (z = 1100) auf 0,5493 (heute). prop:saturation („konsistente Fortsetzung“): β_sym → 1, Ω_M → 1, Universum wird
materiedominiert, Expansion stoppt. Beide Propositionen wenden thm:dark-energy zu allen Zeiten an; bis r16 waren sie
in keiner Runde geprüft und nicht im Register.

**K34.2 Abgleich (M).** Mit ΛCDM (Planck 2018) verlangt die Zuordnung β_sym = √(1 − Ω_Λ(z)): 1,000 bei z = 1100,
0,885 bei z = 1, 0,558 heute, 0,231 bei z = −0,5, Grenze 0. Also dβ_sym/dt < 0. prop:H0-tension gibt
Ω_Λ(1100) = 0,722 statt 1,3 · 10⁻⁹ (Faktor 5,8 · 10⁸).

**K34.3 Urteil (S).** Die drei Aussagen sind zusammen nicht haltbar: sie beschreiben ein Universum, das Λ-dominiert
beginnt und materiedominiert endet, umgekehrt zur beobachteten Geschichte. Der heutige Wert (1,4 % gegen Planck)
bleibt unberührt. Auswege, nicht gewählt: (a) thm:dark-energy nur heute gültig; (b) β_sym läuft abwärts, frühes
Universum an der Tachyon-Grenze; (c) zeitabhängige Brücke zwischen Kaskaden- und kosmologischen Anteilen.

**K34.4 Korrektur.** Eine vermutete Nähe zu DESI (veränderliche dunkle Energie) besteht nicht: DESI betrifft die
Dichte, prop:H0-tension den Anteil, und der Anteil steigt mit der Zeit für jedes w < 0.

**K34.5 Eingrenzung durch K36.** Der Konflikt sitzt nur in prop:saturation (2); prop:H0-tension nutzt die Drift über
den Frame-Faktor und erwähnt Ω nicht. Das Datensatz-Urteil „H0-Spannung in der vorliegenden Form nein“ war zu stark.

### K35 — Companion-Runde v4.8.0-r17 (2026-10-21)

Runde `sec:v480-r17-cosmological-time-direction` (Snippet `llm/v480_r17_round.tex`) hält K34 fest: drei Aussagen,
Tabelle β_sym(z), Theoremlet r17.1 (dβ_sym/dt < 0 verlangt, > 0 angenommen), Auswege (a)–(c), Register-Nachtrag für
thm:dark-energy, prop:H0-tension, prop:saturation. Ledger R_cos^{r17} = (0,0,1); Guards unverändert, β₄
unverbraucht. Build 3 Läufe unter MiKTeX 25.12 (1087 Seiten), Audit gegen r16 ohne harte Abweichung.

### K36 — Drei-Frame-Typisierung des Versatzes und Eingrenzung von r17 (2026-10-21)

Skript `llm/k32_bsym_rollen.py` (Rollen aller 261 \bsym-Stellen im Hauptkorpus; Kreuzterme). Keine neue Vorhersage.

**K36.1 Eingrenzung von r17 (S).** prop:H0-tension erwähnt Ω nicht; die Drift wirkt über den Frame-Faktor
(rekonstruiert: (γ_L(0)/γ_L(1100))^{3/2} = 1,082 gegen 1,083, Exponent nicht im Text). Ω_Λ(1100) = 0,722 entsteht nur, wenn
man das driftende β_sym in thm:dark-energy einsetzt — das tut nur prop:saturation (2). r17.1 bleibt (konditional).
„Permanent“ in thm:dark-offset heißt „nie null“, kein Widerspruch zu langsamer Drift.

**K36.2 Kreuzterme (M).** Materie +, Photon 0, Tachyon − bei Rapiditäten +η, 0, −η mit η = artanh β_sym = 0,6174.
Kreuzterme η_a − η_b: Nachbar (+0, 0−) β = 0,5493, γ = 1,197; Gegenüber (+−) β = 0,844, γ = cosh 2η = 1,864 = γ_L.
Unter J-Symmetrie genau zwei Beträge (Theoremlet r18.1).

**K36.3 Befunde (M).** (a) Konstantenumrechnung Materie → Photon (Definition k, thm:frame-offset) benutzt γ_L, den
Gegenüber-Term; der Nachbarfaktor wäre 1,197; cosh 2η ≠ (cosh η)^n, also nicht in k verschiebbar. (b) z₋ = β/2 = 0,422
in thm:frame-offset ist eine Halbierung in der Geschwindigkeit; in der Rapidität ergibt sie β_sym = 0,5493. (c) Ω_M = tanh²η,
Ω_Λ = sech²η, Summe identisch 1; offen, warum eine Kaskade aus S⁸ den +0-Term benutzt.

**K36.4 Lesart (V, nicht übernommen).** Driftet der Materie-Frame und bleibt der Tachyon-Frame strukturell fest, bricht
die J-Symmetrie, drei verschiedene Kreuzterme. Strukturelles und beobachtetes β fallen genau am symmetrischen Punkt
zusammen; thm:spring hat diesen Punkt als Gleichgewicht (Nettokraft null nur für z_T = −z_M), aber ungedämpft. Der
Abstand 0,5493 (γ_L) zu 0,5578 (Planck) wäre dann Symmetrieabweichung statt δ_CL. Zuordnung der Messwerte zu
Kreuztermen ist eine Vorhersage — nur mit Vorab-Notiz.

### K37 — Companion-Runde v4.8.0-r18 (2026-10-21)

Runde `sec:v480-r18-three-frame-typing` (Snippet `llm/v480_r18_round.tex`) hält K36 fest: Eingrenzung von r17,
Kreuzterm-Tabelle, Theoremlet r18.1, Befunde (a)–(c), Symmetrie-Lesart als Option, Register-Nachtrag.
Ledger R_fr^{r18} = (0,0,1); Guards unverändert, β₄ unverbraucht. Build 3 Läufe unter MiKTeX 25.12 (1090 Seiten),
Audit gegen r17 ohne harte Abweichung.

### K38 — Zwölfter vorab festgelegter Test H12: Zuordnung zu den Kreuztermen (2026-10-21)

Vorab-Notiz `llm/Vorab_Notiz_H12_Drei_Frame_Zuordnung.md` (Commit a593f5d), Ergebnis `llm/Ergebnis_H12_Drei_Frame_Zuordnung.md`,
Skript `llm/k33_test_h12.py`. Regeln: cosh(η₊ + η_s) = γ_L; Ω_M = tanh²η_s (Planck 2018 mit BAO); sin²θ₁₂ = tanh²η₊/cos²θ₁₃.

**K38.1 Werte (M).** η_s = 0,6296 (β_s = 0,5578), η₊ = 0,6053 (β₊ = 0,5408); Vorhersage sin²θ₁₂ = 0,2991 ± 0,0057
gegen H9 0,3086. Unsicherheit fast ganz aus Ω_M (σ_P ≈ σ_Ω). JUNO 2026 (zählt nicht): beide verträglich, Δχ² = 0,34.

**K38.2 Urteil (S).** Nach dem festgelegten Kriterium **nicht trennbar**: |P₁₂ − H9|/σ = 1,36 < 2 bei σ_x = 0,004. Die
Grenze setzt Ω_M, nicht JUNO (auch bei fehlerfreiem θ₁₂ nur 1,67σ). Kein Test, als Ergebnis festgehalten. Ein Messwert
nahe 0,299 wäre eine Spannung für H9 nach dessen eigenem Kriterium, keine Stütze für H12. H9 unverändert.

### K39 — Rückwärtsanalyse: 3×3×3 mit Auslese-Index (2026-10-21)

Wie K18: zählt nicht als Test. Skript `llm/k34_rueckwaerts_3x3x3.py`. T_abc = Versatz von a gegen b, gelesen aus c.
Starteinstellung: Hopf-Kontinuum β = 1/√3 (η_H = 0,6585), J-symmetrisch.

**K39.1 Kinematik (M).** Ein Boost in c verschiebt alle Rapiditäten gleich; T_abc = η_a − η_b hängt nicht von c ab.
Der dritte Index trägt nur Information, wenn die Auslesung auf das System wirkt.

**K39.2 Daten (M).** Planck Ω_M als T−0+: η = 0,6296 ± 0,0073 (−4,4 % gg. Hopf); JUNO θ₁₂ über die nachträgliche
H9-Relation als T+0+: η = 0,6111 ± 0,0082 (−7,2 %); LQG γ_L/2 = 0,6175 (Theorie, kein Messwert, −6,2 %). Die beiden
Messungen unterscheiden sich nur um 1,7σ.

**K39.3 Ansätze (M).** M0 nur Kinematik χ² = 49 (2 FG). M1 Auslesung zieht das gelesene Objekt zum lesenden Frame,
χ² = 34 (1 FG); M2 κ·ε_abc χ² = 34: beide verschwinden bei Selbstlesung (JUNO: Materie aus Materie), gerade dort ist
die Absenkung am größten. M1′ mit lichtartigem Neutrino (H2) χ² = 14. **M3 Auslesefaktor T_abc = (η_a − η_b)·f(c):
1 Parameter, χ² = 2,9 (1 FG), f(+) = 0,944 ± 0,008**; LQG-Kontrolle 0,6 % daneben. M4 freier Faktor je Kontext:
0 FG, erklärt nichts.

**K39.4 Was man lernt (S).** Die nötige Anregung ist nicht abstandsabhängig, sondern ein gleicher Faktor auf alles,
was aus dem Materie-Frame gelesen wird. In β ist das 0,956 ± 0,007 — zahlenmäßig die bekannte Hopf-Lücke
(δ_CL = 0,951, conj:cl-correction; P3 seit r09 Koinzidenz). Kein neuer Wert, nur eine andere Deutung: Auslesefaktor
statt Gitterkorrektur. Zugänglich ist nur f(+), weil jede Messung aus dem Materie-Frame erfolgt; f(0), f(−) sind
nicht beobachtbar, der dritte Index ist empirisch eine einzige Zahl.

**K39.5 Grenzen (P).** JUNO geht über eine nachträglich gefundene Relation ein; Planck und JUNO trennen sich nur
mit 1,7σ; LQG ist kein Messwert. Ein Test bräuchte f(+) ohne JUNO festgelegt und eine Vorab-Notiz vor der Rechnung.

### K40 — Würfel pro Frame, Übergangsgruppe, Holonomie (2026-10-21)

**K40.1 Würfelfamilie (M).** Ein Auslesewürfel T^(d)_abc pro Frame d mit festen Übergängen Λ(d′←d) trägt die
Information eines Würfels plus des Übergangsgesetzes, also keinen zusätzlichen Parameter. Neu ist nur, ob die
Übergänge auf einem geschlossenen Weg zur Identität zusammensetzen; der Rest ist die Holonomie, der Teil, den keine
Wahl des lesenden Frames entfernt. Vertauschen die Übergänge, ist sie trivial.

**K40.2 Zwei Übergangsgruppen (M).** Alte Lesart (thm:symmetric-frame): kollineare Boosts, vertauschbar, Holonomie
trivial. Lesart B (r06, Riemann–Silberstein z = E + iB): SO(3,ℂ) erhält s = E² − B² + 2iE·B. Kein Lorentz-Übergang
verbindet Materie (s > 0, elektrisch) mit Tachyon (s < 0, magnetisch) oder mit dem Photon (Nullfeld); Materie ↔ Tachyon
geht nur über die Dualitätsdrehung α = π/2 (E → −B, B → E). γ_L als Lorentzfaktor zwischen Materie und Tachyon hat in
Lesart B kein Gegenstück (r19.1).

**K40.3 Z₂-Holonomie (M).** s → e^{2iα}s: α von 0 bis π umläuft s = 0 einmal, z kehrt als −z zurück (r19.2). Das
Photon ist Verzweigungspunkt von z über s. Kann nur ±1 beitragen, keinen Faktor wie 0,944.

**K40.4 Alte Lesart als photonzentrierte Sicht (M + V).** Die reelle s-Achse reproduziert die Sektorstruktur von
thm:symmetric-frame (r19.3). Lesart (nicht übernommen): Das Photon wählt keine Bezugsrichtung aus; die alte Lesart ist
die Sicht vom Photon aus mit der reellen Achse als gewählter Referenz (Dualitätswinkel als Eichung fixiert). Dort führt
der gerade Weg Materie → Tachyon durch den Verzweigungspunkt, in Lesart B läuft er um das Photon herum. Die Sicht
sieht die Z₂-Holonomie nicht und liefert zusätzlich eine Metrik (Abstand als Boost mit γ_L), die Lesart B nicht hat.
Eichung oder physikalisch: offen seit r07.

**K40.5 Folge (P).** Eine kontinuierliche Holonomie braucht geschlossene Wege in einer SO(3,ℂ)-Bahn und eine
Transportregel (Zusammenhang); das Dokument liefert keines. Kandidat: Wigner-Rotation aus nicht kollinearen Boosts in
Triolen-Richtungen — Modellwahl, Vergleich mit f(+) nur mit Vorab-Notiz.

### K41 — Companion-Runde v4.8.0-r19 (2026-10-21)

Runde `sec:v480-r19-frame-cubes-holonomy` (Snippet `llm/v480_r19_round.tex`): H12 und K39 festgehalten, Würfelfamilie,
Theoremlets r19.1 (keine Lorentz-Verbindung zwischen den Sektoren), r19.2 (Z₂-Holonomie), r19.3 (reelle s-Achse),
photonzentrierte Lesart als Option, Register-Nachtrag. Ledger R_hol^{r19} = (0,0,1); Guards unverändert, β₄
unverbraucht. Build 3 Läufe MiKTeX (1093 Seiten), Audit gegen r18 ohne harte Abweichung.

### K42 — Dreizehnter vorab festgelegter Test H13: Wigner-Holonomie als Auslesefaktor (2026-10-21)

Vorab-Notiz `llm/Vorab_Notiz_H13_Wigner_Holonomie.md` (Commit 645295f), Ergebnis `llm/Ergebnis_H13_Wigner_Holonomie.md`,
Skript `llm/k35_test_h13.py`. Konstruktion: drei Materie-Frames mit Rapidität η_H in Triolen-Richtungen, reine Boosts
v₀ → v₁ → v₂ → v₀, Vergleichsgröße cos δ.

**K42.1 Werte (M).** Holonomie reine Rotation (Boostanteil 10⁻¹⁶), δ = 0,4985 rad = 28,56°, gleich dem Winkeldefekt
des gleichseitigen hyperbolischen Dreiecks (Gegenprobe). cos δ = 0,878 gegen f(+) = 0,944 ± 0,008: z = −7,9.

**K42.2 Urteil (S).** **Widerlegt** für diese Konstruktion; die Holonomie-Route mit Triolen-Boosts ist für f(+)
geschlossen. Andere Konstruktionen nicht gerechnet, bräuchten eigene Notiz. Da f(+) nur eine Anpassung ist (K39),
fällt eine Erklärung des Faktors weg, nicht der Faktor.

**K42.3 Nachbefund (nicht registriert, zählt nicht).** cos²(δ/2) = (1 + cos δ)/2 = 0,939 trifft f(+) mit z = −0,5; einer
von vier naheliegenden Kandidaten (cos δ −7,9; cos(δ/2) +3,1; 1 − δ/2π −2,8). Herkunft: halber Winkel aus r06.4
erzwungen, wenn der Spinor ψ (K2.2) ausgelesen wird; Quadrat = Born-Regel (Deutung, wie tanh²η, sech²η in r18 (c));
Ausrichtung des Spinors in der Ebene = Wahl. Strukturbefund (M): Das Triolen-Photon c(1,ω,ω²) breitet sich entlang
(1,1,1) aus, der Drehachse — es erhält nur die Phase δ/2 = 14,28°, keine Abschwächung; cos²(δ/2) gilt für Spinoren in
der Ebene (Helizität eines Materie-Frames). Lesart (V): Materie-Lesungen um cos²(δ/2) abgeschwächt, Photon nur
Phase. Hopf-Start → β = 0,5500, γ_L = 1,8675 (0,12 % / 0,16 %), Kategorie wie P3. Eine Photonphase δ/2 wäre
vorab festzulegen.

### K43 — Der Tachyon-Frame unter Holonomie und Spinorstruktur (2026-10-21)

Strukturrechnung ohne Datenvergleich, Skript `llm/k36_tachyon_frame.py`.

**K43.1 Gleiche Holonomie (M).** Die Dualität z ↦ iz vertauscht mit jeder SO(3,ℂ)-Wirkung (numerisch exakt). Jede
Schleife hat im Tachyon-Sektor dieselbe Holonomie wie ihr Materie-Bild; für die Triole δ = 28,56°.

**K43.2 Gleiche Hauptspinoren (M).** z und iz haben dieselben zwei Hauptnullrichtungen; Materie und Tachyon mit
z_T = i z_M unterscheiden sich nur in der Gesamtphase des Spinorprodukts. Im Auslesebild von K42.3 werden Materie- und
Tachyon-Lesungen gleich abgeschwächt; nur das Photon (auf der Drehachse) unterscheidet sich.

**K43.3 Überlichtrapidität (M).** Für v > 1 ist artanh v = artanh(1/v) + iπ/2. Bei v = 1/β_sym = 1,8203: Realteil
η_sym = 0,6174, Imaginärteil π/2. u(η + iπ/2) = i·w mit w = (sinh η, cosh η) raumartig: Die reelle Vierergeschwindigkeit
kippt von zeitartig zu raumartig, der Faktor i trägt die Phase — dieselbe Struktur wie z_T = i z_M mit s → −s, und
derselbe Faktor i wie in der erlaubten Aussage ℓ_T² = −λ_T² (r82). Für Tachyonen tauschen cosh und sinh die Rollen.

**K43.4 Kreuzterme mit komplexer Tachyon-Rapidität (M).** Tachyon bei −η + iπ/2: Photon–Tachyon cosh = −i·sinh η
(|·| = 0,657), Materie–Tachyon cosh = −i·sinh 2η (|·| = 1,574 = β·γ des Paars statt γ_L = 1,864). Der reelle Faktor
γ_L entsteht nur, wenn der Imaginärteil fallen gelassen wird — passt zu r19.1 und r19.3.

**K43.5 Tribonacci (M).** thm:tribonacci μ = 1/β_sym(μ) ist in Rapiditäten cosh 2η = coth η = tanh(η + iπ/2): Der
Lorentzfaktor des Gegenüber-Terms ist gleich der Geschwindigkeit eines Tachyons mit reeller Rapidität η. Umformulierung,
kein neuer Wert.

### K44 — Companion-Runde v4.8.0-r20 (2026-10-21)

Runde `sec:v480-r20-tachyon-complex-rapidity` (Snippet `llm/v480_r20_round.tex`): H13 widerlegt (K42), Halbwinkel-
Nachbefund als nicht registriert gekennzeichnet (K42.3), Theoremlets r20.1 (Dualität vertauscht mit SO(3,ℂ): gleiche
Holonomie und Hauptspinoren im Tachyon-Sektor) und r20.2 (artanh v = artanh(1/v) + iπ/2, Imaginärteil = Dualitätswinkel),
Parallele zu z_T = i z_M und ℓ_T² = −λ_T² (r82, ohne Zusatz), Kreuzterm-Tabelle mit komplexer Tachyon-Rapidität,
Tribonacci als cosh 2η = coth η, Register-Nachtrag. Ledger R_tach^{r20} = (0,0,1); Guards unverändert, β₄ unverbraucht.
Build 3 Läufe MiKTeX (1096 Seiten), Audit gegen r19 ohne harte Abweichung.

### K45 — Companion-Runde v4.9.0-r01: Photon-Frame als neutrale Achse, Konstantenumrechnung (2026-10-21)

Erste Runde nach dem 4.9.0-Release (`sec:v490-r01-neutral-axis-conversion`, Snippet `llm/v490_r01_round.tex`, Skript
`llm/k37_gl_umrechnungen.py`). Kein Datenvergleich.

**K45.1 Herkunft (M, Archiv).** v2.28.0–v2.29.0: „γ_L = γ_BI/γ_string ≈ 1,197“, bei schon geführtem 1/β_sym ≈ 1,820.
1,197 = (1 − β_sym²)^{−1/2} = cosh η (Nachbarterm Materie–Photon). v2.29.1: auf 1,864 geändert, als Rechenfehler
verbucht; die Notiz in cor:gue-frame nennt 1,197 fälschlich γ_BI. Autor (2026-10-21): Photon-Frame als neutral
vermutet, zuerst auf der neutralen Achse arbeiten — im Archiv nicht vermerkt.

**K45.2 Strukturbefunde (M).** r01.1: 1,197 = cosh η = √((1+γ_L)/2), 1,864 = cosh 2η = γ_L, beide aus γ_BI/γ_string.
Neutralannahme in Lesart B gestützt (Photon dualitätsfest, Verzweigungspunkt, Mitte der reellen s-Achse). r01.2: Das
Lorentzfaktor-Potenzgesetz komponiert über drei Frames nicht ((cosh η)^{2k} gegen γ_L^k; k = 6: 8,6 gegen 42); ein
Doppler-Gesetz e^{−kη} komponiert exakt. Ein Paar zugleich ist konsistent — passt zu „erst eine Achse“.
**r01.3: cosh 2η = e^η genau bei e^η = 𝕋 (Tribonacci)**, dort cosh 2η = e^η = coth η = 1,83929, β = 0,54369;
thm:tribonacci ist die Bedingung „Lorentzfaktor Materie–Tachyon = Doppler-Faktor Materie–Photon“. Im Kontinuum ist
die γ_L-Wahl für den Schritt zur neutralen Achse also genau der Faktor eines komponierbaren Gesetzes; gemessen
(γ_L 1,37 % über 𝕋) 0,55 % Abstand.

**K45.3 Hawking (M).** prop:hawking-gBI-tachyon (i)/(ii): reziproke Faktoren setzen Photon und Tachyon auf
entgegengesetzte Seiten der Materie; die Achse von thm:symmetric-frame hat das Photon zwischen Materie und Tachyon.

**K45.4 Wege (offen).** (A) γ_L behalten, Umrechnungen als über die neutrale Achse lesen; (B) Nachbarfaktor 1,197
(Wert vor v2.29.1); (C) komponierbares Doppler-Gesetz, 1,854 je Nachbarschritt. Tabelle (Arithmetik): ℓ_P-Verhältnis
2,546 / 1,309 / 2,525; Vakuum γ⁶ 42,0 / 2,94 / 40,6; m_ν γ⁴ 12,08 / 2,05 / 11,82. Datenvergleiche (cor:falsifiable,
prop:muon-g2) nicht neu bewertet — nur mit Vorab-Notiz. Ledger R_conv = (0,0,1); Guards unverändert. Build MiKTeX
1099 Seiten, Audit gegen r20 ohne harte Abweichung.

### K46 — Companion-Runde v4.9.0-r02: Rundlauf um das Photon und Umkehrwalze (2026-10-21)

`sec:v490-r02-round-trip-umkehrwalze`, Snippet `llm/v490_r02_round.tex`, Skript `llm/k38_umkehrwalze.py`. Kein
Datenvergleich. Anlass (Autor): Umkehrwalze war für den Rundlauf M→P→T→P→M gedacht, als Paralleltransport über die Sphäre.

**K46.1 Zwei Seiten (M).** Ein Durchgang Materie→Tachyon bei festem |s| läuft oben oder unten um s = 0 (z → ±iz).
Seite = sign Im s = sign(E·B): Lorentz-invariant, P- und T-ungerade, C-gerade (Dichte des θ-Terms FF̃). Rundlauf auf
derselben Seite zurück: z → z; Seitenwechsel (gleicher Drehsinn): z → −z. Spinor ψ → ±iψ, zwei Rundläufe ψ → −ψ.
Der „doppelte Tunnelpunkt“ ist ein Punkt mit zwei Seiten.

**K46.2 Rundlauf-Umkehrwalze = C (M).** z → −z ist auf den Feldstärken Ladungskonjugation C = PT = Dualität um π;
zentral, also kein Kandidat für das J des Projektors ½(1+J) (der wäre null).

**K46.3 Involutive Umkehrwalze ist antilinear (M).** Keine C-lineare Involution mit s → −s (det M² = −1). Antilineare
mit s → −s̄: J z = iR z̄, R ∈ O(3,ℂ), R R̄ = 1. Vertreter J_B = i z̄: E ↔ B = Dualität(π/2) nach T; passt zur
zeitumgekehrten Innensicht von thm:core. Nicht Lorentz-invariant (J_B Λ = Λ̄ J_B). Eigenkanäle E = ±B auf den beiden
imaginären Halbachsen, je einer pro Seite; ½(1+J_B) bildet auf Re s = 0, Im s ≥ 0 ab, nie auf den Nullkegel ⇒
thm:core „Photon bei β = 0“ gilt nur für Re s. Enigma-Komposit: R_{π/2}⁻¹ J_B R_{π/2} = −J_B = C·J_B.

**K46.4 OP5 (M + Lesart).** Leckdiagnosen von def:working-shared-matrix-leakage mit J_B: null nur für reelle Drehungen
(Boost η = 0,6174: 0,985 / 0,526; Dualität α = 0,4: 0,779 / 0,389). Entsprechung Wendepunkt ↔ Rückweg auf gleicher
Seite, Durchgang ↔ Seitenwechsel notiert, nicht übernommen (ρ_r, ρ_h, K, Tunnelselektor ohne Gegenstück).
Ledger R_uw = (0,0,1); Guards unverändert.

### K47 — Companion-Runde v4.9.0-r03: Kompensator als Zweiarm-Interferometer (2026-10-21)

`sec:v490-r03-compensator-interferometer`, Snippet `llm/v490_r03_round.tex`, Skript `llm/k39_kompensator.py`. Kein
Datenvergleich. Anlass (Autor): Michelson–Morley mit halbdurchlässigem Spiegel; Tachyonenspiegel als Periskop.

**K47.1 Ausgänge (M).** C = ½(1+J) und A = ½(1−J) sind die beiden Ausgänge eines Zweiarm-Interferometers mit J in
einem Arm; Energie verlustfrei aufgeteilt. Mit antilinearem J nur reell-linear, A(f) = −i C(if): Boson/Fermion-
Aufteilung des Pauli-Punkts (sec:central) wird Real-/Imaginärteil-Aufteilung.

**K47.2 Ladung und Licht (M).** Coulombfeld → J_B: Feld einer magnetischen Ladung; C, A: Dyonen (q/2, ±q/2).
Lichtwelle: J_B = Umkehr der Ausbreitung + 90°-Polarisationsdrehung (phasenkonjugierender Spiegel + Rotator, existiert);
C(Licht) hat E ∥ B, kein Licht. Fehlender Tachyonenspiegel = fehlende magnetische Ladung (unter r07-Zuordnung).

**K47.3 Auslese (M).** Dualitätsphase φ im Referenzarm: D(φ) = Im(e^{iφ} s); Amplitude |s|, Phase arg s; D(0) = 2E·B
(Seite des Photons). Materie und Tachyon um eine halbe Periode versetzt, Licht ohne Streifen (Nullresultat).
Sichtbarkeit V = |s|/|z|² = √(1 − (|E×B|/u)²) = 1/cosh 2η_f, η_f Rapidität des Systems mit E ∥ B; Energie läuft mit
tanh 2η_f. Arithmetik bei η_sym: V = 1/γ_L = 0,536, 0,844 — nicht identifiziert, nur mit Vorab-Notiz.

**K47.4 Summe und Produkt (M).** prop:compensator „orthogonal zu beiden Eingängen“ gilt nicht für den Mittelwert
(Re⟨f, Cf⟩ = |Cf|²), wohl für das Produkt: z × J_B z = 2 E×B, z · J_B z = 2iu; lichtartig genau für Licht.
Welche Lesart gemeint ist, offen. Ledger R_comp = (0,0,1); Guards unverändert.

### K48 — Companion-Runde v4.9.0-r04: Kompensator als Matrix auf dem (E, B)-Dublett (2026-10-21)

`sec:v490-r04-doublet-matrix`, Snippet `llm/v490_r04_round.tex`, Skript `llm/k40_dublett_matrix.py`. Kein
Datenvergleich. Anlass (Autor): Kompensator besser als Matrix?

**K48.1 Dublett (M).** F = [E | B] ∈ ℝ^{3×2}. Dualität, J_B, T, C wirken von rechts als reelle 2×2-Matrizen
(R_α, σ_x, σ_z, −1) und erzeugen O(2); Antilinearität = σ_x ist Spiegelung. Drehungen von links (vertauschen),
Boosts faktorisieren nicht. C_HC = ½(1+σ_x) gewöhnlicher Projektor; Enigma-Komposit = R σ_x R⁻¹ = −σ_x.

**K48.2 Zustandsmatrix (M).** G = FᵀF = u·1 + ½(Re s σ_z + Im s σ_x), det G = |E×B|², u² − det G = |s|²/4.
Bloch-Vektor b = (Re s, Im s)/2u in der Einheitsscheibe: |b| = 1/cosh 2η_f, Licht in der Mitte, Materie/Tachyon
gegenüber, Seite = sign b₂. Dualität dreht b um 2α; Boost: s fest, u ändert sich, |b| = 1 im System E ∥ B, → 0 bei
großem Boost. Stokes-Formalismus für (E, B); kein σ_y-Anteil (Scheibe statt Kugel, dritte Achse offen).

**K48.3 Messung (M).** Ausgang 1: tr(G C_HC) = u + E·B; D(φ) = 2u b·(sin φ, cos φ): Interferometer misst b längs
einer Richtung. Summenlesart = Projektor, Produktlesart = Spur/Determinante (+ Spaltenkreuzprodukt für die Richtung).
app:hc-tools: Dublett liefert konkrete X^±; Identifikation mit der Millennium-Matrix nicht gemacht. R_mat = (0,0,1);
Guards unverändert.

### K49 — Companion-Runde v4.9.0-r05: Millennium-Matrix auf dem Dublett, dritte Achse/Kerr, Photon aus Materie + Tachyon (2026-10-21)

`sec:v490-r05-layer-transport-kerr-photon`, Snippet `llm/v490_r05_round.tex`, Skript
`llm/k41_schichttransport_kerr_photon.py`. Kein Datenvergleich.

**K49.1 Millennium-Matrix (M).** (T4) [M, J] = [M, C] = 0 erzwingt auf dem Dublett M = λ₊C_HC + λ₋A
(Portgewichtung); C_HC ist dann Spektralprojektor (thm:hc-spectral-projector). Erfüllt von Drehungen, J_B, C;
verletzt von Boosts, allgemeinen Dualitätsdrehungen, T. det-1-Glieder e^{tσ_x} = e^t C + e^{−t} A erhalten Re s; bei
t = η_sym Doppler-Gewichte (Arithmetik). Volles M_16 (Vierschichtzerlegung, Index 16) nicht identifiziert.
**Umbenennung (Autorwunsch):** M_16 = „layer-transport matrix“ (Schichttransportmatrix), Dublett-Einschränkung =
„port-weighting matrix“ (Portgewichtungsmatrix); ab r05 als Lesename, frühere Wortlaute/PDF-Keywords unverändert.

**K49.2 Dritte Achse (M).** An einem Punkt E, B reell ⇒ nie σ_y. Komplexe Amplituden: Ĝ hermitesch, σ_y-Anteil
−2 Im(Ê*·B̂) = Helizität (zirkular ±1, linear 0); Scheibe → Kugel, Licht auf der Helizitätsachse. Kerr:
Ψ₂ = −M/(r − ia cos θ)³ komplex, Im Ψ₂² (Pontrjagin-Anteil) Halbkugeln mit entgegengesetztem Vorzeichen, Äquator 0;
Schwarzschild reell. Kopplung an Helizität / Helizitätsungleichgewicht der Kerr-Hawking-Strahlung offen, nur mit
Vorab-Notiz.

**K49.3 Photon aus Materie + Tachyon (M).** s(z_M + z_T) = 2 z_M·z_T bei s_T = −s_M; Nullfeld genau bei
Orthogonalität (E ⊥ B gleich stark), Energiefluss längs E×B senkrecht zu beiden; Winkel ϑ: b = (0, cos ϑ),
parallel = Dyon. Rücklaufendes Photon kommt d(1 + 1/v) nach dem Abflug an, in jedem System zukunftsartig ⇒ kann
das Tachyon nicht erzeugen; Tachyon-Reihenfolge rahmenabhängig (Umdeutung). Zyklus mit Periode d(1 + 1/v); Rückkehr
auf der anderen Seite ⇒ C-konjugiertes Tachyon. Sog nicht ableitbar (keine Dynamik, r10). R_lt = (0,0,1); Guards
unverändert.

### K50 — Companion-Runde v4.9.0-r06: Tachyon-Trefferkette, Beschleunigung, Higgs-Feld (2026-10-21)

`sec:v490-r06-hit-chain-higgs`, Snippet `llm/v490_r06_round.tex`, Skript `llm/k42_tachyon_trefferkette.py`. Kein
Datenvergleich. Anlass (Autor): Tachyon läuft doch schon rückwärts; Higgs-Feld erzeugt entlang einer Linie Materie,
jeder Treffer des Tachyons ein gleiches Photon.

**K50.1 Kreisschluss (M).** Photon braucht d, Tachyon nimmt höchstens d/v zurück ⇒ Lücke d(1 − 1/v) = 0,451 d.
Ein Photon- + ein Tachyonbein schließen nie; zwei Tachyonbeine in relativ bewegten Frames (Tolman) schon. Bei
v = 1/β_sym, u = β_sym exakt zurück zum Start = dieselbe raumartige Linie (r02.1 Fall a). r05.3(c) steht.

**K50.2 Trefferkette (M).** Feste v: Huygens-Kegel cos ϑ = 1/v ⇒ 56,68° bei v = 1/β_sym; Beobachter mit u = 1/v
= β_sym (Materie-Frame) sieht alle Treffer gleichzeitig; Boost nimmt η aus η + iπ/2, übrig iπ/2 (reine Phase);
Aberration der Senkrechten gibt wieder 56,68°. Tachyon: E = μ sinh η, p = μ cosh η = 1,197 μ.

**K50.3 Beschleunigung (M).** Konstante Eigenbeschleunigung t = R cosh σ, x = R sinh σ: v und dv/dt divergieren bei
(R, 0), Eigenbeschleunigung bleibt 1/R, Trefferrate divergiert (Blitz), dahinter Paarereignis, Emission ↔ Absorption.
Energieabgabe an Treffer: nach E₀/ε Treffern E = 0, v = ∞, p = μ; Kegel öffnet 56,68° → 90°.

**K50.4 Higgs (M + Lesart).** Elektroschwache Massenmatrix auf (W³, B) hat Rang 1 = Portgewichtung mit masselosem
Photonport; bei θ_W = 45° genau 0·C_HC + m_Z²·A; gemessenes θ_W ≠ 45° ⇒ gedrehter Kompensator (formal, anderes
Dublett). Higgs bei φ = 0 tachyonisch (m² < 0), Masse durch Kondensation. Tachyonische Felder: Instabilität, keine
Überlichtsignale ⇒ Trefferkette braucht vorkorrelierte Auslöser. Kondensiertes Vakuum liefert keine Energie: Energie
vom Tachyon (K50.3) oder vom noch abrollenden Feld (Symmetriebrechung). R_chain = (0,0,1); Guards unverändert.

### K51 — Vorab-Test H14: Kegelwinkel = 2 θ_W (2026-10-21)

Vorab-Notiz `llm/Vorab_Notiz_H14_Kegelwinkel_Weinberg.md` (Commit 5911161), Ergebnis
`llm/Ergebnis_H14_Kegelwinkel_Weinberg.md`, Skript `llm/k43_test_h14.py`. Daten PDG 2024/2025.

**K51.1 (D).** Vorhersage sin²θ_W = (1 − β_sym)/2 = 0,22533; on-shell aus m_W, m_Z: 0,22321 ± 0,00026 ⇒ z = +8,2:
**exakt widerlegt.** Band On-shell…MS-bar [0,22243; 0,23140] enthält die Vorhersage ⇒ als Baumgraphen-Beziehung
**nicht entscheidbar**. ϑ_c = 56,68° gegen 2θ_W = 56,39° (on-shell) / 57,48° (MS-bar). Nachträgliche Hypothese,
Look-elsewhere 2 % je Beziehung, 9 % für fünf: **kein Beleg**. Route ruht ohne Schema-/Skalenvorschrift.

### K52 — Companion-Runde v4.9.0-r07 und Vorab-Notiz H15: Kegelwinkel, Weinberg-Winkel, W-Masse (2026-10-21)

`sec:v490-r07-cone-weak-mixing`, Snippet `llm/v490_r07_round.tex`; Erkundungsprotokoll
`llm/Erkundungsprotokoll_Weinberg_Kegel.md` (8 gezählte Versuche); Skripte k43–k46.

**K52.1 (M).** cos 2θ = tanh η ⇔ tan θ = e^{−η} ⇔ sin²θ = 1/(1 + e^{2η}) ⇔ 2θ = Π(η) (Parallelitätswinkel);
Kegel ϑ_c = Π(η). Portgewichtung bei t = η: Gewichtsverhältnis e^{2η} = cot²θ. H14 ist ein Kopplungsverhältnis
g/g′ = e^η; MS-bar-Minimum ≈ 0,231 bei μ = M_W ⇒ keine Skala erreicht 0,22533.

**K52.2 (D, Beobachtung).** cot θ_W on-shell = 1,86550 ± 0,00140; γ_L = 1,86444 (z = −0,8), e^η (z = −8,1),
1/β_sym (z = −32). Daten bei Weg (A) aus r01, Kegel benutzte Weg (C). Nachträglich, Look-elsewhere ≈ 0,17, kein Beleg.
Reale Teilcheneffekte (bekannt oder dunkel) können die H14-Lücke höchstens zu etwa einem Viertel füllen (m_W-Schranke).

**K52.3 H15 (vorab festgelegt, Commit 62c505d).** cot θ_W (on-shell) = γ_L, γ_BI aus der Meissner-Zählgleichung
= 0,237532957966 ⇒ **m_W = 80,3615 ± 0,0018 GeV**. Vergleich mit der ersten m_W-Weltmittelung nach 2026-10-21;
gestützt nur bei SM-Ausschluss mit 3σ (SM 80,359 ± 0,006). Ergebnis ausstehend (`llm/Ergebnis_H15_W_Masse_gamma_L.md`).
R_ew = (0,0,1); Guards unverändert.

### K53 — Companion-Runde v4.9.0-r08: Frame-Drift, Atomuhren, Hubble-Spannung (2026-10-21)

`sec:v490-r08-drift-clocks-hubble`, Snippet `llm/v490_r08_round.tex`; Erkundungsprotokoll E10–E13; Skripte k47, k48.

**K53.1 Feste Größen (S).** Photon-Frame-Werte und k = 0 (c, γ_BI) fest; Materie-Frame-Werte driften mit
γ_L^(local)(t)^k; strukturelles γ_L = γ_BI/γ_string fest (Trennung wie r18).

**K53.2 α-Vorzeichen gelöst (S).** P5, prop:muon-g2 und α-Korollar nutzen k(α) = +1 für α; nur die Tabellenzeile
nennt α⁻¹ ⇒ k = 1 gehört zu α (schließt r03 F2), keine Zahl des Hauptkorpus ändert sich.

**K53.3 Drift gegen Atomuhren (D).** Drift aus prop:H0-tension über den lokalen Faktor: |d ln α/dt| = 3,9e-12 (γ_L),
1,3e-12 (cosh η), 2,3e-12 (e^η) pro Jahr gegen 1,0(1,1)e-18 (Yb⁺, Lange 2021) ⇒ ~6 Größenordnungen; lesartunabhängig
k(α)/k(H₀) < 5,5e-7 nötig. Statische Typisierung (k(H₀) = 1 ⇒ 1,864) und Frühzeit-Änderung (m_e, α falsche Richtung)
tragen nicht ⇒ prop:H0-tension ohne tragfähigen Mechanismus.

**K53.4 Compton-Uhr (M).** m_e c²/ħ hat k = 0 ⇒ frame-invariante Uhr; Verhältnis zur Atomuhr (k = 2) liest
γ_L^(local)^{±2} direkt. H15 sagt konstantes θ_W voraus (strukturelles γ_L). R_drift = (0,0,1); Guards unverändert.

### K54 — Companion-Runde v4.9.0-r09: Was der lokale Frame-Faktor sein kann (2026-10-21)

`sec:v490-r09-local-frame-factor`, Snippet `llm/v490_r09_round.tex`; Erkundungsprotokoll E14/E15; Skript k49.

**K54.1 (S).** Vier Einflüsse laut Quelle (Beobachter thm:frame-offset, Zeit prop:H0-tension, Erdbahn α-Korollar,
Potential P5 mit 1e-10 δΦ/c²), kein Feldgesetz. Zwei Widersprüche thm:frame-offset ↔ thm:k-values (γ_BI
beobachterabhängig vs k = 0; ein Faktor für alle vs k(c) = 0, k(G) = 2), aufgelöst durch strukturelle Lesart.

**K54.2 (D).** Geschwindigkeitslesart ausgeschlossen (1,6e-4 jährlich, ~1e13 über Uhrenschranke); Potentiallesart
überlebt (1,6e-20), treibt aber nur ~1e-15 kosmische Drift; Dichtelesart ohne Form. Muster β_X = k(X) κ:
Compton-Uhr 0, α κ, Atomuhr und G_N 2κ.

**K54.3 (M).** P5 korrigiert: (δα/α)/(δG/G) = k(α)/k(G_N) = 1/2 (statischer Faktor gehört nicht hinein; P5s Ausdruck
ergäbe 0,268, geschrieben 0,537). R_loc = (0,0,1); Guards unverändert.

### K55 — Companion-Runde v4.9.0-r10: Deutung des C5-Faktors 3/4, Zeugenklasse für Form (iii) (2026-10-22)

`sec:v490-r10-c5-factor-shape-three`, Snippet `llm/v490_r10_round.tex`; `llm/Erkundungsprotokoll_Kern.md` (K1–K4);
Skripte k50, k51.

**K55.1 (M + Deutung).** C_HC R_α C_HC = cos α C_HC: „drehen, dann kompensieren“ hält cos²α, nicht idempotent. α = π/6
gibt 3/4, 9/16, 27/64, 81/256 (Ledger r04–r08) und n = 20. π/6 triolisch (Vierteldrehung Materie→Tachyon in drei
Schritten, 27/64 = ein Durchgang) oder Hopf (tan = 1/√3; mit β_sym Stufe 22). Zeno-Muster.

**K55.2 (M, bedingt auf die Deutung).** Form (iii): isometrische Zeugen verlagern C → A (verletzt δ), Boosts haben den
Boden E² + B² ≥ |s|, Nullfelder nur Grenzwert ⇒ keine Zeugen aus der Transportgruppe von Lesart B; nötig wäre
Dynamik (s ändern). Keine Aussage über C5 = 0. R_core = (0,0,1); Guards unverändert.

### K56 — Companion-Runden v4.9.0-r11/r12: gekickte Dualitätsdynamik, Rekonstruktion von Δ_γ < 1/5 (2026-10-22)

**K56.1 r11 (Modellvorschlag).** Gekickte Dualitätsdrehung: z → e^{iωt} z zwischen Kicks, C_HC bei t_n = nτ, A-Anteil ins
Reservoir. Stufenfaktor cos²ωτ, 3/4 eindeutig bei π/6; 3/6/12/24 Stufen = Vierteldrehung / z → −z / 2π / Spinor; Kick
ändert s; kein endlicher Abschluss (Export); Skala offen. Analogie: Zeno-Schleifen (Kwiat et al. 1995) mit N = 3.

**K56.2 r12 (M unter Prämissen).** r65 verloren (Autor). Δ_γ < 1/5 strikt aus P1 r14-Daten, P2 strikte r23-Bedingung,
P3 multiplikativer Verlust (r11), P4 Uhrenfenster-Charts von R_A; bindend V3 (einzige Chart mit κ(N − 1) = 1, S = 2N,
1 − 4/N). Unter P3: Drift tan α < 1/2; C5-Stufe außerhalb, r05-Toleranzzeile innerhalb; r05-Nullzeilen = Verlagerung
nach A_4/U_6. Provenienz offen, Ableitung unter Prämissen geschlossen. Guards unverändert.

### K57 — Companion-Runde v4.9.0-r13: Zeitskala der gekickten Dualitätsdynamik (2026-10-22)

**K57.1 (M).** r15-Tick cos²((τ−τ_V)/σ_V) = C-Port-Energie zwischen Kicks ⇒ ω = 1/σ_V, τ_k = (π/6)σ_V. Zwei-Term-Sonde:
σ = 2/Δγ, Schwebung T_b = 2π/Δγ ⇒ τ_k = T_b/6 für jedes Paar; 3/6/12/20/24 Stufen = ½/1/2/10/3/4 Schwebungen. Mit
γ₁, γ₂: τ_k = 0,15205 Uhreneinheiten; keine Sekunden (Quelle verweigert die Identifikation; global = W_γ^glob).

**K57.2.** Fenster in Grad: V3 39,23°, V5 50,77° (R_A) fassen eine C5-Stufe, V8 28,13° (R_B) nicht ⇒ zweiter Grund für
r12-P4. Stufenwinkel Hopf 30° (3/4) gegen Gitter 28,78° (0,7683). R_time = (0,0,1); Guards unverändert.

### K58 — Companion-Runde v4.9.0-r14: Auslese-Richtungen aus Triole und Umkehrwalze (2026-10-22)

**K58.1 (Deutung).** Kick = Durchgang von arg s durch Triole ∪ J_B(Triole) (s → −s̄) = Sechseck 0°…300° (enthält Materie
und Tachyon) ⇒ 30° Dualität, q = 3/4; Triole allein 1/4, Viertelraster 1/2. Ein Umlauf von s um das Photon = sechs
Kicks = z → −z (r02) = eine Schwebung (r13). Annahme: Triole auf arg s gelegt (Quelle: Komponentenbedingung). A₂/SU(3)
nur Bemerkung. R_kick = (0,0,1); Guards unverändert.

### K59 — Companion-Runde v4.9.0-r15: Sammelregister v4.9.0-r01–r14, r17-Auswege nach r08 (2026-10-22)

**K59.1 (S).** r17-Weg (b) (β läuft von ~1 abwärts) durch die Uhrenschranke von r08 ausgeschlossen; (a) und (c) bleiben,
beide mit festem β ⇒ thm:dark-energy ist eine Aussage über die heutige Epoche. prop:saturation (1) (m_ν ∝ γ_L(t)⁴)
ebenfalls ausgeschlossen ⇒ Proposition ohne Grundlage.

**K59.2.** Register aller Statusänderungen r01–r14 in einer Tabelle; Liste der sechs Autorentscheidungen
(thm:frame-offset strukturell? C5 = Drehen/Kompensieren? Triole auf arg s / diskrete Auslese? W_clk^loc auf R_A?
Wege A–C? dark-energy (a) oder (c)?). Guards unverändert.

### K60 — Companion-Runde v4.9.0-r16: Autorentscheidungen (2026-10-22)

**K60.1 (Autor).** thm:frame-offset ist eine Aussage über den festen strukturellen Faktor γ_L = γ_BI/γ_string ⇒ die
r09-Widersprüche zur k-Tabelle sind gelöst. Die C5-Rekursion als gekickte Dualitätsdrehung mit Auslese an
Triole ∪ J_B(Triole) ist die ursprünglich gemeinte Lesart des Autors (Status: Autorlesart, keine Herleitung aus dem
früheren Text); r10.2 gilt unter ihr. Offen (Autor): Wege A–C der Umrechnung; thm:dark-energy Weg (a) oder (c).

### K61 — Companion-Runde v4.9.0-r17: Entropie zwischen den Frames, Photon als Informationssingularität, Skalen-Dimension (2026-10-22)

`sec:v490-r17-entropy-scale`, Snippet `llm/v490_r17_round.tex`, Skript `llm/k56_entropie_skala.py`. Fragen des Autors:
Fallen Strukturen zusammen, um den Photon-Frame zu erzeugen? Photon als Informationssingularität? Neuer Freiheitsgrad zum
Parken der Umrechnungen?

**K61.1 (M).** |b| = sech 2η; Eigenwerte p± = (1 ± 1/cosh 2η)/2 = 1/(1+β²), β²/(1+β²), Verhältnis β². γ_L = 1/|b|. Hopf: 3/4, 1/4
(= C5-Faktor und Export); gemessen 0,768/0,232 (= Gitterwert r13).

**K61.2 (M).** Entropie S von 0 (E ∥ B) über 0,781 Bit (η_sym), 0,811 Bit (Hopf) bis 1 Bit (Licht). Photon = maximal gemischt;
Bures-Abstand Ruhe→η = ½ gd(2η), Licht bei π/4 (endlich), Rest ½ Π(2η). Informationssingularität = undefinierte Richtung
(r² dθ² → 0), Metrik regulär; nur im Grenzwert erreichbar. Photon-Frame = Punkt, an dem p₊ = p₋ und Materie/Tachyon
zusammenfallen (stützt die Autorvermutung); endliches γ_L entspricht |b| = 1/γ_L, nicht b = 0.

**K61.3 (M).** Skalen-Dimension σ: komponierbar nur als Rapidität ⇒ Doppler-Gesetz (Weg C); Weg A nur am Tribonacci-Punkt;
Gewicht-0-Kombinationen σ-invariant. Spannung zur r07-Beobachtung (Weg A), Entscheidung beim Autor. R_info = (0,0,1).

### K62 — Companion-Runde v4.9.0-r18: die alten Umrechnungen auf der Skalenlinie, Wege A und C zugleich (2026-10-22)

`sec:v490-r18-scale-line-a-and-c`, Snippet `llm/v490_r18_round.tex`, Skript `llm/k57_a_und_c.py`. Frage 1 des Autors: Was
ändert sich an den alten Umrechnungen mit den Frames einzeln, und was muss gelten, damit Weg A und Weg C zugleich gelten?

**K62.1 (M).** Drei Lesarten desselben Abstands: coth η = 1/β = √(p₊/p₋) (1,820), e^η (Doppler, 1,854), cosh 2η = 1/|b| (γ_L,
1,864). Gleich genau am Tribonacci-Punkt (alle 1,83929). Gemessener Abstand 1,37 % darüber in γ_L; für Zahlengleichheit müsste
die Gitterkorrektur als eigene Verschiebung geführt werden.

**K62.2 (M).** Klassentrennung auf der σ-Linie: Skalengrößen (Frequenz, Länge, Masse, Energie) X = e^{kσ}X₀ (Weg C);
Auslesegrößen (Sichtbarkeit, Kontrast, Eigenwertverhältnisse, Mischungen) als Zustandsfunktion f(σ) mit Faktor cosh 2σ (Weg A),
komponiert über Rapiditätsaddition (sech 2(σ₁+σ₂) = 0,311 statt Produkt 0,452). Bedingungen: Klassenzuordnung, Frames als
Rapiditäten addieren, für Zahlengleichheit zusätzlich Tribonacci-Punkt.

**K62.3 (D).** Hauptkorpus-Umrechnungen (§phase-constants) sind Skalengrößen; unter C ändern sie sich um −0,55 % (Takt, Hawking),
−0,82 % (ℓ_P), −2,18 % (m_ν), −2,72 % (Matter-Fehler, Vakuum k = 5). γ_L bleibt bei Auslesegrößen: 1/γ_L, Ω_M = β², cot θ_W ≈ γ_L
(r07), γ_BI/γ_string. Spannung r07 ↔ r17 aufgelöst (verschiedene Klassen). Angebotene Lesart; Entscheidung 5 von r15 beim Autor.
R_conv = (0,0,1).

### K63 — Companion-Runde v4.9.0-r19: Klassentrennung auf den Hauptkorpus angewandt (2026-10-22)

`sec:v490-r19-class-split-applied`, Snippet `llm/v490_r19_round.tex`, Skript `llm/k58_klassentrennung.py`.

**K63.1 (M).** Regel: Monom in k-gewichteten Konstanten → Skala, e^{kη} (Weg C); Zustandsfunktion → Auslese, γ_L (Weg A).
Klasse allein aus der Form, vor dem Ablesen der Vergleichswerte. α ist trotz Dimensionslosigkeit Skala (k = 1). Je
z₋-Einfügung ein Doppler-Faktor; Gewichte additiv, auch k(ℓ_P) = 3/2.

**K63.2 (D).** Skalenstellen ändern sich um 0,55–2,7 %, keine Aussage kippt: ℓ_P^ph 6,40·10⁻³⁶ m, Vakuum 21,92, Matter-Rest
10^−120,7, Neutrino 11,82, hvp-Faktor 0,539, Λ_bare^ph 58,1, rem:open 2,37·10⁻⁴, γ₁^ph 7,623, β_eff 3,708.

**K63.3 (M).** Wo es zählt: P5 = k(α)/k(G_N) = 1/2 exakt (r09-Korrektur folgt aus der Regel); P3 verliert den Treffer
(0,54847, −0,15 %; selbstkonsistent −0,19 %), passt zur r09-Einstufung „Koinzidenz“; P6: γ_BI = T_Sphaera/T_H^tachyon nur noch
auf −0,55 % (γ_string e^η = 0,23619), exakt nur am Tribonacci-Punkt. Unverändert (Auslese): P2, H15, Ω_M, thm:frame-offset.
R_split = (0,0,1).

### K64 — Companion-Runde v4.9.0-r20: Herkunftshypothese für Δ_γ < 1/5 (2026-10-22)

`sec:v490-r20-delta-gamma-provenance`, Snippet `llm/v490_r20_round.tex`, Skript `llm/k59_herkunft_delta_gamma.py`. Anlass:
Autorhinweis, der Wert sei bei einer Photon-Frame-Rechnung entstanden und müsse nicht allgemein stimmen.

**K64.1 (M).** r14 nennt G den Gewinn der Photon-Frame-Uhr. Am Hopf-Punkt β² = 1/3: γ_L = 2 = G(V3), p₋ = 1/4 = κ(V3),
N = 1 + 1/p₋ = 2 + 1/β² = 5 (Balance κ(N−1) = 1), p₊ = 3/4 = κ(Uhrsaat). Damit 1 − 16/(G S) = 1/5 exakt. Kollarzeile 5/6 und
C5-Faktor 3/4 am selben Punkt.

**K64.2 (H).** Hypothese: Δ_γ < 1/5 entstand mit Photon-Frame-Uhrgewinn = γ_L am Hopf-Punkt (Kontinuum ohne δ_CL) bzw.
γ_L = 1,864 aufs Halbgitter gerundet. Gewicht: vier Treffer an einem Punkt plus Balance; dagegen Viertel-/Halbgitter, V5/V8
ohne entsprechende Lesart, 16 rahmenfrei.

**K64.3 (M).** Beim gemessenen Abstand mit Kartenform fest: 0,142 (G = γ_L), 0,137 (G = e^η), 0,110/0,105 (κ = p₋), 0,1925
(balanciert); alle unter 1/5, also 1/5 dort nicht konservativ. Alternative tan α < 1/γ_L gibt 0,223. r12.2(b): Kollarzeile
(1/6) nur am Hopf-Punkt innen. Guard: Schranke frame-typisiert, enger = weniger behauptet, kein Guard verbraucht.
R_prov = (0,0,1).

### K65 — Companion-Runde v4.9.0-r21: Uhrschranke je Frame, Herleitung der 1/5 (2026-10-22)

`sec:v490-r21-clock-bound-per-frame`, Snippet `llm/v490_r21_round.tex`, Skript `llm/k60_delta_gamma_je_frame.py`.

**K65.1 (M).** Prämissen: D1 G = 1/|b| = |γ| (Uhr hebt Sichtbarkeit auf 1, Auslese); D2 κ = Partnerport (Materie p₋, Tachyon p₊
durch J_B); D3 Balance κ(N−1) = 1; D4 N frame-invariant; D5 Tachyon = Uhrsaat (5, 3/4, 1). Reserven
Δ_M = (10x²−5x+1)/((1+x)(1+2x)), Δ_T = (1+3x−14x²)/((1+x)(1+2x)), x = β². Frame-Konsistenz G_M S_M = G_T S_T ⇒ x = 1/3 eindeutig,
N = 5, Δ = 1/5 in beiden Frames. Ohne D3 (N = 5): 4p₋² − 9p₋ + 2 = 0 ⇒ p₋ = 1/4.

**K65.2 (M).** Je Frame gemessen: Materie 0,1925 (1/5 um 0,0075 zu großzügig; Kollarzeile innen, C5-Stufe außen); Tachyon kein
Fenster nötig (S = 22,9 ≥ 16), Reserve 0,302; Photon entartet (Scheibe: G → ∞; σ-Linie: blockiert) = Informationssingularität
in der Uhrenschicht. Frame-frei nur am Hopf-Punkt. Uhrsaat = J_B-Bild von V3. r20-Folge 3 (Kollarzeile außen) unter D3 aufgehoben.

**K65.3 (D).** Regel für Frame-Unterscheidung: Tachyon = J_B-Bild (x → 1/x, p± getauscht, γ negativ), Photon = entarteter
Fixpunkt p± = 1/2. Anwendung auf andere Schichten offen. R_frame = (0,0,1).

### K66 — Companion-Runde v4.9.0-r22: Frame-Regel als stehende Konvention (2026-10-22)

`sec:v490-r22-frame-rule`, Snippet `llm/v490_r22_round.tex`, Skript `llm/k61_frame_regel.py`.

**K66.1 (D).** Konvention F: M = Dublettzustand bei x = β²; T = J_B-Bild (x → 1/x, p± getauscht, γ → −γ); P = Fixpunkt b = 0.
F1 frame-frei ⇔ M = T; F2 P eigens, Entartung ist keine globale Aussage; F3 Tachyon-Umrechnung: Betrag nach Klasse (r19),
Phase (−1)^k; F4 ab r22 Pflichtabschnitt `subsec:v490-rNN-frames`, vom Guard-Linter geprüft.

**K66.2 (M).** Frame-frei (M = T): Sichtbarkeit, Entropie, sin²θ_W (H15), Kick-Lesart 3/4, P5, k = 0-Größen. Nur Materie:
Eigenwert-Lesart 3/4, Ω_M (T: 3,31), Koide-Phase (T: undefiniert), Uhrschranke. P: portsensitive Größen entartet.

**K66.3 (M).** Vorzeichenskala r82 ℓ_T² = −λ_T² folgt aus F3 ((−1)^{3/2} = ∓i, Quadrat −1), nicht aus dem Doppler-Faktor bei
η + iπ/2 (e^{3iπ/4}, Quadrat −i). Klassentrennung und erlaubte Tachyon-Skala damit verträglich. R_F = (0,0,1).

### K67 — Companion-Runde v4.9.0-r23: Konvention F auf den Hauptkorpus angewandt (2026-10-22)

`sec:v490-r23-convention-f-main-body`, Snippet `llm/v490_r23_round.tex`, Skript `llm/k62_frame_regel_hauptkorpus.py`.

**K67.1 (D).** 113 von 2234 Aussage-Umgebungen des Hauptkorpus hängen von einem Frame ab: F 7 (Strukturkonstanten,
k-Tabelle, Tribonacci in |γ|, Guinand–Weil), M 29 (Kosmologie, Koide, OP1/OP2, Hopf-Winkel, Quasikonformität), C 12
(Konstantenumrechnungen, Hypothesen), S 9 (Λ = 0 und Θ–R-Bilanz im Photon-Frame), P 3 (Horizont, Sättigung), D 13, N 40
(OP1-Arbeitsschicht, OP5-Grammatik).

**K67.2 (M).** (a) Tachyon des Hauptkorpus (−β, thm:symmetric-frame) ≠ Tachyon von F (1/β); 18 Aussagen (12 M, 6 S) wären
unter −β frame-frei. (b) Photon-Frame des Hauptkorpus (β = 0, σ = 0) ist unter F der reine Zustand |b| = 1, nicht P; die
S-Aussagen übertragen sich nicht. (c) β → 1 (Horizont, Sättigung) = Photon-Fixpunkt von F. (d) Quasikonform: Tachyon |μ| > 1,
K = −γ_L, orientierungsumkehrend. (e) Ungerade Gewichte wechseln im Tachyon-Frame das Vorzeichen (T_H, α, Vakuum k = 5).
(f) N-Aussagen samt lokaler OP5-Schließung ohne Frame-Größe, unverändert lokal. Vorzeichen-Widerspruch Sektordefinition
(Materie β < 0) gegen thm:symmetric-frame (+β) vermerkt, durch v4.8.0-r07 (Vorzeichen von s) überholt. R_F = (0,0,1),
Wahl der Tachyon-Lage für die geraden Aussagen beim Autor.

### K68 — Companion-Runde v4.9.0-r24: Korrektur der drei r23-Widersprüche als Ein-Frame-Artefakte (2026-10-22)

`sec:v490-r24-single-frame-correction`, Snippet `llm/v490_r24_round.tex`, Skript `llm/k63_widersprueche_ein_frame.py`.
Autorhinweis: der Hauptkorpus arbeitete nur in einem Frame.

**K68.1 (M).** Vorzeichen: β in Sektordefinition und thm:symmetric-frame ist Orientierungscode (v4.8.0-r01); die zwei
Konventionen unterscheiden sich um z → −z = C, das s erhält; Sektor nach Vorzeichen von s (v4.8.0-r07). Notation, nicht Physik.

**K68.2 (M).** Tachyon: Rapidität −η + iπ/2, tanh = −1/β; reelle Projektion auf die Achse des Bezugsframes = −β (Hauptkorpus,
T|_R), im eigenen Frame β_T² = 1/β² (F). Die 18 geraden Aussagen sind frame-frei zwischen M und T|_R, im Tachyon-Eigenframe
bei 1/β² (Ω_M → 3,31).

**K68.3 (M).** Photon: der „Photon-Frame“ des Hauptkorpus (β = 0) ist der reine Zustand R, |b| = 1, Entropie 0; Umrechnungs-
faktor |b_R|/|b_M| = cosh 2η = γ_L. Zum echten Photon P (b = 0) wäre er unendlich. S-Aussagen (Λ = 0, Rahmenterm 0) gelten in
R; in P sind Rahmenterm und p₋/p₊ maximal.

**K68.4 (D).** Konvention F ergänzt: F5 Bezugsframe R, Umrechnung M → R; F6 Projektion T|_R bei −β; F7 Vorzeichen von β =
Orientierungscode. R_F = (0,0,0): beide Tachyon-Lagen mit Typisierung behalten.

### K69 — Companion-Runde v4.9.0-r25: Überarbeitung des Hauptkorpus (2026-10-22)

`sec:v490-r25-main-body-revision`, Snippet `llm/v490_r25_round.tex`, Skript `llm/aufraeumen_v490.py`, Sicherungstag
`vor-aufraeumen-v490-r24`. Autorauftrag: alte Arbeit nicht verlieren, Sackgassen nicht stehen lassen.

**K69.1 (D).** Regel: (A) Sackgasse → Original wortgleich in Archiv-Anhang `sec:v490-archive`, an alter Stelle gleiche
Umgebung, gleiche Nummer, gleiches Label, Status, Verweis; (B) bekannter Fehler → im Text korrigiert, `\qsstatus` mit altem
Wortlaut; (C) umgedeutet/offen → `\qsstatus`. Runden, Vorab-Notizen, Tests nie archiviert.

**K69.2 (D).** Archiviert (15): Koide-Phasenformel (K = 2/3 bleibt), GUE-Herleitung (GUE empirisch bleibt), thm:gue-selfdet,
cor:odlyzko (P1), P3-Komplex (conj:cl-correction, prop:exponent-5, thm:self-consistent-gL, cor:op1-resolved), prop:pmns-z3,
prop:H0-tension, prop:saturation, prop:bare-lambda, Θ-Summen-Vermutung samt Restabschätzung, RH-Zeile in thm:toe.
Korrigiert: γ_L⁶ → γ_L⁵ (Vakuum, Matter-Fehler, P4), P5 → 1/2, k = 1 für α, Kompensator-Orthogonalität (Produkt).
Statusvermerke an 20 Stellen (Sektordefinition, §phase-constants = Bezugsframe R, thm:symmetric-frame u. a.).

**K69.3 (D).** Build 1176 Seiten / 3635 Labels, Overfull 58, harte Werte 0. Auf GitHub liegt der Hauptkorpus in eingefrorenen
Fragmenten; Übernahme (premise-audit oder neue Basis) ist Autorentscheidung. R_rev = (0,0,0).

### K70 — Vorab festgelegter Test H16 und Companion-Runde v4.9.0-r26: Grad-6-Potentiale auf dem Tripel-Raum (2026-10-22)

`sec:v490-r26-degree-six-triple-space`, Snippet `llm/v490_r26_round.tex`. Vorab-Notiz `llm/Vorab_Notiz_H16_Grad6_Tripelraum.md`
(Commit d0360b8, als „H12“ angelegt, Nummer war vergeben; Umbenennung ohne Inhaltsänderung 6bd2f1b). Ergebnis
`llm/Ergebnis_H16_Grad6_Tripelraum.md`, Skripte `llm/k64_test_h16.py`, `llm/k65_sattel_grad6.py`.

**K70.1 (M).** V₆ = −S + βS² + γQ − κP + δH (δ > 0). Feste Verteilung N = 2000: globale Minima 1585 × gleiche Normen,
398 × ein Platz, 17 × entartetes Paar, 0 × drei verschiedene. Lepton-Tripel: auf der Vieta-Familie überall kritischer
Punkt, auf dem Gitter 41 × 41 nirgends lokales Minimum (1139 × δ ≤ 0, 542 × Hessematrix indefinit).

**K70.2 Urteil (S).** H16a, H16b, H16c **widerlegt** nach dem festgelegten Kriterium.

**K70.3 Theoremlet r26.1 (M, nach dem Urteil gefunden).** Alle Norm-Invarianten bis Grad 6 sind linear in
e₂ = Σ_{i<j} x_ix_j (Q = S² − 2e₂, H = S³ − 3Se₂ + 3P², SQ = S³ − 2Se₂), also V = A(S,P) + e₂(b₀ + b₁S). Bei drei
verschiedenen Normen ist die Hessematrix in (S, e₂, P) [[·, b₁, ·], [b₁, 0, 0], [·, 0, ·]], Hauptminor −b₁² < 0:
Sattelpunkt, oder flach (b₀ = b₁ = 0). Exakt geprüft (40 Stellen, 2000 von 2000); in doppelter Genauigkeit kann der
negative Eigenwert bis 5·10⁻¹⁵ des größten schrumpfen.

**K70.4 Neueinordnung.** K32.3 „Mindestgrad 6“ gilt für kritische Punkte; Minima mit drei verschiedenen Normen brauchen
Grad ≥ 8 (hinreichend nicht gezeigt, ≥ 4 neue Koeffizienten, also Anpassung). K = 2/3 braucht Σn_k, kein polynomiales
Invariant. Im Rahmen „Normen und t = P“ erzeugt die Generationen-S₃ keine Massenhierarchie; nötig wären explizite
S₃-Brechung oder Invarianten jenseits der Normen (Realteile der Plätze sind G₂-invariant). Frames: Urteil und r26.1
frame-frei; Massen-Lesart nur Materie. R_cg^{r26} = (0,0,1); Guards unverändert, β₄ unverbraucht.

### K71 — Companion-Runde v4.9.0-r27: Dynamik der gekickten Dualitätsdrehung (2026-10-22)

`sec:v490-r27-kick-measurement-dynamics`, Snippet `llm/v490_r27_round.tex`, Skript `llm/k64_dynamik_kick_messung.py`.

**K71.1 (M).** Modell: Dualitätsdrehung U_α = exp(−iασ_y), dann Messung {C_HC, A}. Selektiv: Überleben cos²α, 3/4 bei π/6, n = 20
bis unter 1/256 (C5-Rekursion). Nicht-selektiv: ein π/6-Kick aus R (|b| = 1) gibt den Hopf-Zustand (|b| = 1/2, γ_L = 2,
Eigenwerte 3/4, 1/4); gemessener Abstand ⇔ Kickwinkel 28,78°, Überleben 0,768 (r13-Gitterwert). Fluss aller Zustände zu b = 0
(Photon als Attraktor), Entropie monoton. Spur fest, |s| schrumpft: außerhalb der Transportgruppe von Lesart B (wie r10.2
verlangt). Dichte Kicks: Γ = 2ω²τ → 0 (Zeno), kontinuierlich Dephasierung in der Kompensatorbasis.

**K71.2 (M).** Grenzen: (cos²α)^n > 0 für jedes endliche n (kein endlicher Score-Nullpunkt, nur C5_det/eff); leer erst bei α = π/2
(Vierteldrehung, durch C4/C6 blockiert, r12.2(c)); α = π/4 erreicht b = 0 in einem Schritt, Score dort 1/2. Offen: Uhr-Einheit,
κ, messender Agent. Form (iii) offen. R_dyn = (0,0,1).

### K72 — Companion-Runde v4.9.0-r28: Wer misst? Tachyon als Messgerät, Selbststabilisierung, Korrektur der Tachyon-Abbildung (2026-10-22)

`sec:v490-r28-who-measures`, Snippet `llm/v490_r28_round.tex`, Skript `llm/k65_messgeraet_tachyon_feld.py` (sechs Varianten vorab
festgelegt, eine Prüfung nachträglich).

**K72.1 (D).** Korrektur: C_HC = ½(1 + J_B), J_B lässt die Kompensator-Ports fest und kehrt nur b_z = Re s/2u um. Die in r21, r22
(Konvention F) und r27 als „J_B-Bild“ bezeichnete Tachyon-Abbildung (b → −b, Ports getauscht, x → 1/x) ist die Dualitätsdrehung
z → iz (v4.8.0-r07.2), ρ → σ_y ρ σ_y. Ergebnisse unverändert. Beide Abbildungen kehren Re s um; J_B behält die Seite sgn(E·B), z → iz wechselt sie.

**K72.2 (M).** Tachyon als Messgerät: ideal (D = 0) aus seinem Bezugszustand mit Kopplung über T = σ_z; über J_B oder C keine Messung
(D = 1); als Bild des Systems teilweise (0,50 / 0,87). Tausch mit dem eigenen Tachyonbild: b → cos 2θ b, radialer Schritt von r27,
π/6 aus R gibt Hopf; Fluss zum Photon (Selbstmessung ohne äußeres Gerät).

**K72.3 (M).** Feld allein: zwei Frequenzen |D|² = 3/4 nach einem Kickabstand (derselbe Winkel wie r13), volle Wiederkehr nach 6 →
reversibel; 40 Frequenzen Kohärenz ≈ N^(−1/2) mit Teil-Wiederkehr → nur näherungsweise. Mit nachgefülltem Tachyon-Reservoir:
eindeutiger Attraktor |b| = sin²θ/(1 − cos²θ cos 2α) auf der Partnerport-Achse (selbststabilisiert, offenes System). Nachträglich:
sin²θ = β² selbstkonsistent genau bei β² = 1/3 (Hopf), gemessen 0,4825 gegen 0,5364. R_meas = (0,0,1).

### K73 — Companion-Runde v4.9.0-r29: Woher das Tachyon-Reservoir kommen könnte (2026-10-22)

`sec:v490-r29-reservoir-source`, Snippet `llm/v490_r29_round.tex`, Skript `llm/k66_tachyon_reservoir_quelle.py` (Kandidaten und
Kriterien vorab: nachliefern, Bezugszustand b_T = (−1, 0), kohärenter Austausch, keine verbotene Aussage).

**K73.1 (M).** Vakuum = Bezugsframe R (r24); sein Bild unter z → iz ist genau der Tachyon-Bezugszustand → Paarerzeugung aus dem
Vakuum liefert passende Tachyonen (K2). Horizont liegt am Photon-Fixpunkt, b_T = 0, Attraktor 0 (K1 scheidet aus); übrige Moden nur
Dephasierung (K4 scheidet aus); thermisches Bad nur teilweise (|b| = 0,500 / 0,193 / 0 bei |b_T| = 1 / 0,5 / 0), T → 0 = Vakuum (K5);
Trefferkette verteilt statt nachzuliefern, Paarereignis = K2 (K6).

**K73.2 (M).** Kaskade K3: Austauschstärke β² nur kohärent selbstkonsistent (Hopf, |b| = 1/2); als Markov-Ersetzung 0,378, schräg
(41°), selbstkonsistent erst bei p = 0,3865 (kein benannter Punkt). Bilanz: gebrauchter Tachyon (−0,750, 0,144), ein frisches
Vakuumpaar je Kick nötig. Offen: Paarerzeugungsrate, Kohärenz des Austauschs, Verbleib der gebrauchten Tachyonen. R_res = (0,0,1).

### K74 — Companion-Runde v4.9.0-r30: Der Kompensator umgeht die klassische 1/2 (2026-10-22)

`sec:v490-r30-compensator-coherence`, Snippet `llm/v490_r30_round.tex`, Skript `llm/k67_kompensator_kohaerenz.py`. Autorhinweis:
Der Heisenberg-Kompensator wurde eingeführt, um die klassische Aufenthaltswahrscheinlichkeit 1/2 zu umgehen.

**K74.1 (M).** Klassische Mischung von Zustand und Tachyonbild gibt im Kompensatorport immer 1/2; kohärente Kombination hängt von der
relativen Phase ab, bei zwei Phasen 0 bzw. 1 (eindeutiger Port). Die Hauptkorpus-Bemerkung „Light as the Heisenberg compensator of
the universe“ (C(β) = ½(β − β) = 0) ist nur amplitudenweise möglich; Wahrscheinlichkeiten gäben β² = 0,302.

**K74.2 (M).** C = ½(1 + J) ist Projektor nur für eine Involution: J_B ja, z → iz nein (C² = J/2). J_B = R_{π/2} ∘ T: der
Kompensator-Partner ist der Tachyon, durch die Zeitumkehr gesehen; gleiche Aussage wie r28.1(a) (ideale Messung über T).

**K74.3 (M).** Austausch über den Kompensator ist kohärent per Konstruktion → offene Frage aus r29 beantwortet; Markov-Lesart ist die
klassische Mischung, die der Kompensator vermeiden soll. Bei Stärke 1/2: kohärent |b| = 2/3, Gewichte 1/6 / 5/6, 0,32 Bit; Markov
0,577, 1/4 / 3/4, 0,74 Bit. Wortlaut „Markov“ in thm:dark-energy: β² als Einschritt-Gewicht lesbar; Statusvermerk möglich, Autor
entscheidet. R_coh = (0,0,0).

### K75 — Companion-Runde v4.9.0-r31: Markov-Kaskade als Selbststabilisierungstest, Statusvermerk zu thm:dark-energy (2026-10-22)

`sec:v490-r31-markov-self-stabilisation`, Snippet `llm/v490_r31_round.tex`, Skript `llm/k68_markov_kaskade_stabil.py`; Vermerk über
`llm/apply_patches.py` mit `llm/revision_spec_v490_r31.py` (auch für GitHub). Autorabsicht: Die Markov-Kette sollte die
Wahrscheinlichkeiten besser vorhersagen und prüfen, ob sich die Kaskade selbst stabilisiert.

**K75.1 (M).** Kette des Beweises: nach drei Schritten alles in S² (Photon), einziger stationärer Zustand (1, 0, 0) — keine
Selbststabilisierung. Mit Rückweg S² → S⁸ (Rate r): eindeutig stationär (1, β²r, r)/(1 + r + β²r), gedämpft oszillierende Annäherung
(Nebeneigenwerte 0,41 bei β² = 1/3, r = 1/2); Flussanteile aus S⁸ genau β², 1 − β² für jedes r. Gleiches Muster wie r27/r28 auf dem
Dublett: geschlossen → Photon, nachgefüllt → stabil. Rückweg vorgeschlagen: Vakuumpaare (r29). Statusvermerk erweitert (Regel C).
R_Mk = (0,0,1).

### K76 — Vorab festgelegter Test H17 und Companion-Runde v4.9.0-r32: Realteil-Invarianten auf dem Tripel-Raum (2026-10-23)

`sec:v490-r32-real-part-triple-space`, Snippet `llm/v490_r32_round.tex`. Vorab-Notiz `llm/Vorab_Notiz_H17_Realteile_Tripelraum.md`
(im Container festgelegt 2026-10-22 21:11, Rechner nicht erreichbar, dem Autor vor der Rechnung geschickt; lokal mit
ursprünglichem Zeitstempel als 1a39d6f). Ergebnis `llm/Ergebnis_H17_Realteile_Tripelraum.md`, Skripte `llm/k69_test_h17.py`,
`llm/k70_achse_e3.py` (im Container als k66/k67 gerechnet, Namen waren vergeben, Code unverändert).

**K76.1 (M).** V_R = −S + βS² + γQ − κt − μL − νR₂ − λL² (L = ΣRe a_k, R₂ = Σ(Re a_k)², G₂-invariant je Platz), Minimierung
über alle 24 Koordinaten. N = 2000: 1483 × gleiche Normen, 517 × entartetes Paar, 0 × drei verschiedene; 1629 Minima auf der
reellen Achse (G₂ ungebrochen). Lepton-Tripel (Vieta-Gitter 21 × 4 × 7 × 3): 696 unbeschränkt, 1061 indefinit, 7 lokal nicht
global, 0 global.

**K76.2 Urteil (S).** H17a, H17b, H17c **widerlegt**.

**K76.3 Theoremlet r32.1 (M, nach dem Urteil).** Auf der Achse t = e₃, R₂ = S, L = e₁ und V_R = A(e₁,e₂) + e₃(4γe₁ − κ),
weil Q = e₁⁴ − 4e₁²e₂ + 2e₂² + 4e₁e₃. Hessematrix in (e₁,e₂,e₃): H₃₃ = 0, H₁₃ = 4γ → Sattel. Allgemein: symmetrische Polynome
in n vom Grad ≤ 5 sind linear in e₃. Die 7 „lokalen Minima“ haben exakt (50 Stellen) einen negativen Eigenwert, relativ ≈ 10⁻⁹,
unter der festgelegten Toleranz 10⁻⁸.

**K76.4 Einordnung.** Realteile verschieben das Hindernis von e₂ (r26.1) nach e₃, heben es nicht auf. Auf der Achse generisch
Grad ≥ 6 nötig, ohne Realteile Grad ≥ 8; jeweils Anpassung. Abseits der Achse kein Satz, numerisch kein Gegenbeispiel. H11, H16,
H17: natürliche G₂ × S₃-Invarianten geben höchstens zwei verschiedene Massen. Nächster prüfbarer Weg: explizite S₃-Brechung.
Frames: Urteil und r32.1 frame-frei, Massen-Lesart nur Materie. R_cg^{r32} = (0,0,1); Guards unverändert, β₄ unverbraucht.

### K77 — Prüfung: Dixon-Ablage, Hilbert-Shift-Leiter, gemischte Readouts (2026-10-23)

Dokument `llm/Pruefung_Dixon_Ablage.md`, Skript `llm/k71_dixon_ablage.py`. Konsistenzprüfung, keine Vorhersage.
Autorhinweis: Die Dixon-Algebra war als Objekt gedacht, in dem alle Konfigurationen abgelegt werden; gemischte Readouts
sind angelegt, aber nie benutzt.

**K77.1 (D).** Leiter HS(n): Träger C_n = 2^n Kanäle, 2^{C_n} Masken; HS(3) = 8 (Fano/Oktonion), HS(6) = 64 = Dixon
ℂ⊗ℍ⊗𝕆, Kanalindex (a, b, c) ∈ 2 × 4 × 8, Route → Maske χ_Dix ∈ {0,1}⁶⁴ oder blocked/leak/debt. Als Register stimmig.

**K77.2 (S).** Gemischte Readouts (Z. 1811–2142, Masken-Registry 2^j, doppelter Hilbert-Shift 2^k, Normalform) werden nur im
eigenen Block referenziert; später nur strukturell (Kanten-Zulässigkeit `sec:v410r18-…`, Kontraktionsregel χ_mn der
Tensornotation, r93). **Nie** mit konkreten Komponenten und Aggregation ausgewertet. Masken sind konservativ: keine Größe.

**K77.3 (M).** (Im ℍ)⊗𝕆 = i⊗𝕆 ⊕ j⊗𝕆 ⊕ k⊗𝕆 ≅ 𝕆³: Das Tripel aus r14/r15 liegt verlustfrei in der Ablage (24 von 64 Bits),
die 3 × 3 farbigen Zustände als 9-Bit-Teilmaske; G₂ (auf 𝕆) und Aut(ℍ) = SO(3) vertauschen → Farbe und Generation getrennt.

**K77.4 (M).** Von den 24 Vorzeichen-Permutationen in SO(3) lassen nur 12 die Triality-Form invariant (gerade Permutationen,
gerade Zahl von Vorzeichen) ≅ A₄. Die Triality-Vertauschungen brauchen Oktonion-Konjugation (Anti-Automorphismus).
Gemeinsame Symmetrie von Ablage und Triality-Form: A₄. Konflikt: `thm:three-generations` nutzt ℂ⊗ℍ als Lorentz-Spinor;
Generationen in Im ℍ und Spinor in ℍ zugleich geht nicht.

**K77.5 Einordnung.** A₄ ist struktureller Befund, keine Vorhersage (A₄ als Flavour-Gruppe bekannt; tribimaximal durch θ₁₃ ≠ 0
ausgeschlossen). Gemischte Readouts mit festgelegter Aggregation μ über die Platz-Bits wären eine explizite S₃-/A₄-Brechung:
der passende Ort für den nächsten Vorab-Test. `thm:three-generations` ohne `\qsstatus` (Kandidat Regel C, Autorentscheidung).

**K77.6 Frames (Autorhinweis).** Die Dixon-Grammatik ist mit Bezug auf den Photon-Frame geschrieben; r23 ordnet sie als N ein
(Name ohne Frame-Größe), nach r24.3 ist das der Bezugsframe R, nicht P. K77.3/K77.4 sind algebraisch, gezeigt in R; für M/T fehlt
die Wirkung von J_B auf der Ablage [korrigiert in K77.8: ℂ-Konjugation ist T, nicht J_B]. Namensfalle:
„gemischter Readout“ (QAM) ≠ „gemischter Zustand“ (P maximal gemischt). Port-gewichtete Aggregation wäre frame-abhängig
(M (0,768; 0,232), T vertauscht, P ohne Brechung); eine Vorab-Notiz muss den Frame der Massen-Ablesung festlegen.

**K77.7 Lean (`formal/QSFormal/Dixon.lean`, ohne Mathlib, Lean 4.35.0).** Bewiesen: Konjugation ist Anti-Automorphismus, kein
Automorphismus; Triality-Form zyklisch und unter (x̄,z̄,ȳ) invariant; unter den 24 Vorzeichen-Permutationen in SO(3) sind genau
die 12 aus `a4` (gerade Permutation, gerade Vorzeichenzahl) Symmetrien (`inv_iff`); 64 Dixon-Kanäle, Tripel-Maske 24 Bits,
Farbmaske 9 Bits als Teilmaske; Polynom-Kerne von r26.1 (linear in e₂) und r32.1 (auf der Achse linear in e₃), Hauptminor −b² < 0;
unter Annahme J_B = ℂ-Konjugation: Masken erhalten. Nicht formalisiert: abstrakter Isomorphismus zu A₄, Schritt Hauptminor ⇒ Sattel
(Analysis). Nur Standard-Axiome (propext, Classical.choice, Quot.sound), kein sorry, kein native_decide.

**K77.8 J_B auf der Ablage (Lean, `Dixon.lean`).** Nach v4.9.0-r30.2(b) ist J_B = R_{π/2} ∘ T (T: z ↦ z̄, R: z ↦ iz). Unter der
Annahme (A_ℂ), dass der ℂ-Faktor der Ablage (Index a) die Amplitudenebene z ist: J_B vertauscht die beiden a-Hälften (σ_x, ohne
Vorzeichen, Involution); R² = −1; T lässt jede Maske fest. Tripel-Maske (a = 0) → Kopie in a = 1, disjunkt, 24 Bits; Farbmaske ebenso.
Platznormen (Massen-Lesart √m ∝ n_k) unter T, R, J_B fest → **frame-frei**. Triality-Form: T: t ↦ t̄; R: t ↦ −i t; J_B: t ↦ −i t̄,
also (Re, Im) ↦ (−Im, −Re), Betrag fest; für ein reelles Tripel verschwindet der Realteil-Readout im Tachyon. Lesart: das a-Bit ist das
M/T-Sektorbit (wie die σ_z-Kanäle des Dubletts, `Frames.J_B_channels`), P = gleiches Gewicht beider Hälften. **Korrektur K77.6:** die
dort genannte „natürliche Wahl ℂ-Konjugation“ ist T (Zeitumkehr), nicht J_B. Python-Gegenprobe exakt. (A_ℂ) ist Autorentscheidung.

**K77.9 Readout-abhängige Lesarten (Autoridee; Lean `Lesarten.lean`).** ℂ-Faktor zugleich Dualitätsebene (J_B = z ↦ i z̄),
quantenmechanisches i (C = z̄), Lorentz-Komplexifizierung (R = z ↦ iz, Drehung → Boost) und Uhrphase (z ↦ wz). Bewiesen: C = T auf dem
ℂ-Faktor; J_B R_w J_B = R_{w̄} (Uhr läuft im Tachyon rückwärts, vgl. r23 orientierungsumkehrend); C, J_B antikommutieren auf Amplituden,
vertauschen auf quadratischen Readouts. **Korrektur:** Das a-Etikett erhalten nur die 8 Elemente von D₄, nicht ganz O(2); die Uhr ist mit
M/T nur in Viertelschritten verträglich, Triolen-Phasen ω^k gehören nicht auf den ℂ-Faktor (Ort: span(1, e₇), r15). ℍ: L und R vertauschen;
A₄ = Konjugation mit 2T (binäre Tetraedergruppe); Rechtswirkung von 2T irreduzibel; Linksmultiplikation verteilt Platznormen um,
invariant ist conj(qx)(qy) = |q|²conj(x)y. Lage: Mit Lorentz von links ist √m ∝ Platznorm nicht Lorentz-invariant; Rettung = Massen aus
links-invarianten Größen ablesen, Generationen-Etiketten auf der rechten Seite finden. Nicht widerlegt, nicht konstruiert.

**K77.10 Links-invariante Etiketten (Modellbau; `k72_links_invariant.py`, Lean `Lesarten.lean`).** Tripel als 8 Quaternionen h_c;
G_cd = conj(h_c)h_d links-invariant (Drehungen; komplex-bilinear auch Boosts). Re G = Σ x_b x_bᵀ (platzsymmetrisch); Im G = drei Komponenten
A⁽ⁱ⁾, A⁽ʲ⁾, A⁽ᵏ⁾ = drei links-invariante Etiketten **auf der rechten Seite**; für reines Tripel A⁽ⁱ⁾ = −x_j ∧ x_k,
μ_i = 2(|x_j|²|x_k|² − ⟨x_j,x_k⟩²). Rechts-2T vertauscht die μ nur zyklisch (ℤ₃ der Triole). Orthogonale Plätze: √(μ_i/2) = P/n_i,
Reihenfolge umgekehrt (vgl. x ↦ 1/x der Konvention F; nur Beobachtung). Damit hat der Weg aus K77.9 eine konkrete Form; eine
Massen-Lesart über μ ist neue Vermutung, braucht Vorab-Notiz; kein Massenvergleich gerechnet. μ sind G₂-invariant (Summen über Spalten).

### K78 — Vorab festgelegter Test H18 und Companion-Runde v4.9.0-r33: links-invariante Etiketten (2026-10-23)

`sec:v490-r33-left-invariant-labels`, Snippet `llm/v490_r33_round.tex`. Vorab-Notiz `llm/Vorab_Notiz_H18_Links_invariante_Massen.md`
(Commit 6130814), Ergebnis `llm/Ergebnis_H18_Links_invariante_Massen.md`, Skripte `llm/k73_test_h18.py`, `llm/k74_nachkontrolle_h18.py`.

**K78.1 (M).** Lesart m_k ∝ √μ_k an den globalen Minima der geprüften Potentiale. Familie A (H11, 205 Punkte): alle unbestimmt.
Familie B (H17, 500 Punkte): 428 unbestimmt, 51 gleich, 21 zweierlei. Drei bestimmte, verschiedene μ: keine.

**K78.2 Urteil (S).** H18a, H18b **widerlegt**.

**K78.3 Nachkontrolle (M).** A: Der Winkel zwischen zwei Plätzen ist eine echte flache Richtung (μ_max/S² zwischen 0,15 und 0,22 bei
gleicher Tiefe), weil V die Winkel nur über t sieht. B: Die unbestimmten Fälle haben μ ≈ 0 (parallele Plätze auf der reellen Achse).

**K78.4 Einordnung.** Die Runde r33 hält K77 (Dixon-Ablage, A₄ = 2T-Konjugation, J_B auf der Ablage, D₄, links-invariante Etiketten)
und H18 fest. Die Etiketten lösen den Lorentz-Konflikt für die Etiketten, nicht für Massen; sie erben das Auswahlproblem. Nötig wäre ein
Prinzip, das die Winkel zwischen den Plätzen festlegt. Vierter widerlegter Test desselben Ansatzes (H11, H16, H17, H18). Build 1197 Seiten,
Audit gegen r32 ohne harte Abweichung. R_cg^{r33} = (0,0,1); Guards unverändert, β₄ unverbraucht.

### K79 — Bestandsaufnahme: Was folgt aus der Struktur, was ist eingesetzt? (2026-10-23)

Lebendes Dokument `llm/Bestandsaufnahme_Struktur_Standardmodell.md` (nach jeder Runde nachführen). Autorabsicht: Erklären, warum das
Standardmodell diese Struktur hat; eine Erklärung zählt nur, wenn die Struktur Alternativen ausschließt. Stufen A (folgt, verbietet),
B (darstellbar, eingesetzt/umformuliert), C (widerlegt), D (fehlt).

**K79.1 (S).** A: Lorentz (Biquaternionen), SU(3) als Stabilisator von e₇ und von ω, drei Plätze mit S₃/A₄ (unter Lesart). B: Trennung
Farbe/Generation, schwache SU(2) und U(1), Koide-Form, Quarks/Leptonen, Mischungsexistenz, α/θ_W, β_sym, Higgs. C: Mischungswinkel,
Massenhierarchie aus natürlichen Potentialen. D: Ladungen und Hyperladungen, Chiralität, globale Form der Eichgruppe.

**K79.2 (M).** `thm:SM` und `prop:biquaternion-u1su2` (ohne `\qsstatus`): ℂ⊗ℍ enthält auch SL(2,ℂ); kompakte Untergruppe U(2) = (U(1)×SU(2))/ℤ₂;
das U(1) heißt dort „Elektromagnetismus“, im Standardmodell ist das ungebrochene U(1) die Hyperladung. Der ℍ-Faktor ist dreifach belegt
(Lorentz-Spinor in thm:three-generations, schwache SU(2) in thm:SM, Generationen in r33). Kandidat für Regel C (Autorentscheidung).

**K79.3 Vorschlag (P).** Abzähl-Tests mit Vorab-Notiz: (1) Ladungen einer Generation aus der Dixon-Ablage (Zahloperator auf ℂ⊗𝕆);
(2) genau drei Generationen: Ist Re((xy)z) die Spin(8)-Triality (drei 8-dim. Darstellungen, Out = S₃), schließt sie eine vierte aus?
(3) eine dritte, verträgliche, chirale SU(2) in der Ablage; (4) U(1) als Hyperladung mit Q = T₃ + Y/2.

### K80 — Vorab festgelegter Test H19 und Companion-Runde v4.9.0-r34: Ladungen aus der Dixon-Ablage (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H19_Ladungen_Dixon.md` (Commit 1e60410, vor der Rechnung), Skript `llm/k75_test_h19.py`, Ausgabe
`llm/k75_out.txt`, Ergebnis `llm/Ergebnis_H19_Ladungen_Dixon.md`, Runde `sec:v490-r34-charges-dixon`. Test 1 aus K79.3.

**K80.1 (M).** α_a = ½(L_{e_a} + i·L_{e₇e_a}), a = 4, 5, 6, i = ℂ-Faktor der Ablage; N = Σα_a†α_a, Q = N/3. Fermion-Relationen exakt;
Eigenwerte 0, 1, 2, 3 mit Vielfachheiten 1, 3, 3, 1 algebraisch erzwungen (keine Vorhersage).
**K80.2 (M).** H19a bestätigt: Stab(e₇) ⊂ G₂ (Dimension 8 von 14) vertauscht mit Q. H19b bestätigt: Q = 0, 1 Singuletts 1 ± i·e₇;
Q = 1/3, 2/3 irreduzible, zueinander konjugierte, nicht selbstkonjugierte Tripletts in span_ℂ(e₁..e₆). In Fureys Lesart ν, d̄, u, e⁺.
**K80.3 (M).** H19c widerlegt: Der reelle Spann von e₄, e₅, e₆ ist kein Q-Eigenraum, e₇ kein Eigenvektor; Eigenzustände e_a ± i·e₇e_a.
`thm:octonion-SU3` und `thm:three-generations` (Gen_i ↔ e_{i+3}, e₇ ↔ ν_R) sind in der Zuordnung falsch. Kandidat für Statusvermerk.
*Umgestuft durch K81:* Im inneren Frame J = L_{e₇} ist die Zuordnung richtig; falsch bleibt nur der Anti-Triplett-Satz.
**K80.4 (M).** H19d bestätigt: T Q T⁻¹ = 1 − Q, J_B Q J_B⁻¹ = 1 − Q, R Q R⁻¹ = Q. Frame-frei sind Spektrum und Farbstruktur, nicht die
Zuordnung Zustand ↔ Ladung; die Wirkung kommt vom Zeitumkehr-Anteil T. Stützt den Autorhinweis, `thm:SM` sei in einem Frame entwickelt:
Die U(1)-Zeile muss ihren Frame nennen. H19e (gleiches Q auf allen drei Plätzen) folgt aus der Tensorstruktur.
**K80.5 (S).** Bestandsaufnahme: Ladungen D → A unter Lesart (ℂ-Faktor als quantenmechanisches i); wörtliche Companion-Zuordnung C.
Offen: Hyperladung, Chiralität (Tests 3, 4). Kein Guard verbraucht; R_ch = (0,0,1).

### K81 — Vorab festgelegter Test H20 und Companion-Runde v4.9.0-r35: innere und äußere komplexe Einheit (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H20_Frame_Zuordnung.md` (Commit 7d95feb), Skript `llm/k76_test_h20.py`, Ausgabe `llm/k76_out.txt`,
Ergebnis `llm/Ergebnis_H20_Frame_Zuordnung.md`, Runde `sec:v490-r35-inner-outer-unit`. Anlass: Autorhinweis „vielleicht wieder nur der
feste Frame“ zu K80.3.

**K81.1 (M).** Innerer Frame J = L_{e₇}: Stab(e₇) J-linear; (𝕆, J) = span(1, e₇) ⊕ e₇^⊥, e₇^⊥ irreduzibles komplexes Triplett mit
komplexer Basis e₄, e₅, e₆ (J e₄ = −e₃, J e₅ = −e₂, J e₆ = e₁). `thm:octonion-SU3` gilt dort (H20a bestätigt).
**K81.2 (M).** span(e₁, e₂, e₃) = J·span(e₄, e₅, e₆) ist weder J-, Stab- noch Q-invariant: der Anti-Triplett-Satz im Beweis von
`thm:three-generations` ist falsch (H20b widerlegt), eine Vermischung beider Frames.
**K81.3 (M).** P_± = ½(1 ∓ iJ): äquivariant, injektiv, P_±J = ±iP_±. P₋: e₇^⊥ → Q = 2/3, span(1, e₇) → Q = 0; P₊: 1/3 und 1; T vertauscht
P₊ und P₋ (H20c bestätigt). Mit P₋ deckt sich die Companion-Zuordnung mit Fureys Lesart (ν auf e₇, u auf e₄..e₆).
**K81.4 (M).** Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇} exakt (H20d): Die Ladung braucht beide Einheiten und Links- wie Rechtsmultiplikation;
der Skalar it von `thm:SM` allein ist eine globale Phase, kein Elektromagnetismus.
**K81.5 (S).** Lesart von K80.3 / r34.1(c) korrigiert: Aussage bleibt, aber die Zuordnung ist ein Frame-Unterschied, kein Fehler.
Bleibt: Doppelbelegung Farbe/Generation (kein Frame-Effekt). Regelvorschlag zu Konvention F: Farb- und Ladungsaussagen nennen ihre
Einheit (innen J, ohne Ladung; außen i, mit Q) und das Vorzeichen P_±. Kein Guard verbraucht.

### K82 — Frame-Regel für Einheiten, Statusvermerke, Vorab-Test H21 und Runde v4.9.0-r36: Herkunft der Doppelbelegung (2026-10-23)

Autorentscheidung 2026-10-23: Die Frame-Regel aus K81.5 wird Teil von Konvention F (CLAUDE.md, Rundenformat Punkt 7). Statusvermerke
zu `thm:three-generations` und `thm:SM` über `llm/revision_spec_v490_r36.py` (Regel C). Vorab-Notiz
`llm/Vorab_Notiz_H21_Herkunft_Doppelbelegung.md` (Commit 516ab15), Skript `llm/k77_test_h21.py`, Ausgabe `llm/k77_out.txt`, Ergebnis
`llm/Ergebnis_H21_Herkunft_Doppelbelegung.md`, Runde `sec:v490-r36-unit-rule-double-use`.

**K82.1 (M).** σ: e₄ → e₅ → e₆ → e₄, e₇ fest, e₁ → −e₃, e₂ → −e₁, e₃ → e₂ ist ein Automorphismus der Ordnung 3, unter den 48
Vorzeichen-Fortsetzungen der einzige; also σ ∈ Stab(e₇) = SU(3)_c (H21a).
**K82.2 (M).** Auf ℂ³ = (e₇^⊥, J) ist σ die zyklische Permutationsmatrix (det 1, Eigenwerte 1, ω, ω̄, nicht zentral), vertauscht mit Q,
T, R, J_B (H21b): frame-frei, kein Frame-Effekt.
**K82.3 (M).** Die 120°-Triole Σ ω^k e_{k+4} (z₁ + z₂ + z₃ = 0) erfüllt σv = ω̄v; P₋v liegt im Triplett Q = 2/3 (H21c). Die triolische
Grundstruktur (drei Kerne, 120°) ist in 𝕆 ein Farbzustand, ihre zyklische Symmetrie eine Farbdrehung.
**K82.4 (M).** Die Untergruppe von Stab(e₇), die span_ℝ(e₄, e₅, e₆) erhält, ist SO(3) (Dimension 3), σ liegt darin (H21d). Flavour-Gruppen
auf dem reellen Spann (r12: A₄, Δ(96)) sind Untergruppen der Farbe. Generationen-ℤ₃ auf Im ℍ vertauscht mit Stab(e₇) (H21e).
**K82.5 (S).** Herkunft der Doppelbelegung: eine Dreierstruktur, zwei Rollen (Kerne = Farben in thm:octonion-SU3, dieselbe Zyklik =
Generationen in thm:three-generations). Innerhalb von 𝕆 mit festem e₇ ist jede ℤ₃-Symmetrie Farbe; die Trennung ist nötig, ihr Träger
(Triality-Plätze r14 oder Im ℍ r33) offen. Offen (Autor): ob die Triole ursprünglich Farbe oder Generation meinte. Kein Guard verbraucht.

### K83 — Vorab festgelegter Test H22 und Companion-Runde v4.9.0-r37: Triality als Selbstdurchwanderung (2026-10-23)

Autorabsicht (2026-10-23): Die Triole sollte eine andere Darstellung der Sphäre sein; die fraktale Selbstdurchwanderung transformiert
zwischen den Gestalten (Triole, Sphäre, Umgebung), die Selbstähnlichkeit wählt bei jedem Zoom eine Gestalt; nicht auf Periode 3
festlegen; ein Zeitkristall-Ansatz „müsste im Paper stehen“. Textbefund: Der Begriff kommt in Companion, Original v3.1.4, Riemann-Paper,
Archiven und Notizen nicht vor; strukturell verwandt sind der alternierende Orbit-Scan (Σ, Periode 2), die Kristall–Fraktal-Probe und
die Bahntheorie des Riemann-Papers (beliebige Perioden). In der Originalarbeit (`thm:spring`) ist die Triole Materie–Photon–Tachyon.
Vorab-Notiz `llm/Vorab_Notiz_H22_Triality_Selbstdurchwanderung.md` (Commit ed74608), Skript `llm/k78_test_h22.py`, Ausgabe
`llm/k78_out.txt`, Ergebnis `llm/Ergebnis_H22_Triality_Selbstdurchwanderung.md`, Runde `sec:v490-r37-triality-self-traversal`.

**K83.1 (M).** Symmetrie-Algebra 𝔤 ⊂ so(8)³ von t: dim 28, alle Projektionen bijektiv, Platz-Darstellungen irreduzibel und paarweise
inäquivalent (H22a): t ist die Spin(8)-Triality-Form. τ ist der äußere Triality-Automorphismus (H22b).
**K83.2 (M).** τ-feste Elemente (A, A, A) = Der(𝕆) = 𝔤₂ (dim 14), mit A e₇ = 0: 𝔰𝔲(3) (H22c). Lesart: Generation = was die Durchwanderung
vertauscht, Farbe = was sie festlässt; löst die Identifikation aus K82 auf. Physikalische Zuordnung der Plätze offen. *Umgestuft durch K91:* Mit Chiralität nur als äquivalente Kopien; die Inäquivalenz der Plätze ist mit einer
anomaliefreien Chiralität nicht verträglich.
**K83.3 (M).** Vier Plätze: zwei Klassen von Klammerungen ({((xy)z)w, (xy)(zw), x(y(zw))} und {(x(yz))w, x((yz)w)}), die zyklische
Verschiebung tauscht sie, ihre Summe ist invariant (Nachkontrolle). H22d bestätigt, aber ohne Verbot. „Genau drei“ ruht auf der Klassifikation
(drei 8-dim. Irreps von Spin(8), Out = S₃): verbietet einen vierten *neuen* Platz, keine Wiederholung.
**K83.4 (M).** τ, ρ, T, R erzeugen S₃ × D₄ (Ordnung 48), Perioden {1, 2, 3, 4, 6, 12} (H22e). Keine ausgezeichnete Periode.
**K83.5 (S).** Drei Triolen im Korpus: Frame-Triole M/P/T (ℤ₂ mit Fixpunkt, 1 : 1 : 3), Kern-Triole (ℤ₃, 120°, in 𝕆 Farbe), Platz-Triole
(Triality). Die Doppelbelegungen (r13, r34–r36) entstehen beim Gleichsetzen. Kein Guard verbraucht.

### K84 — Vorab festgelegter Test H23 und Companion-Runde v4.9.0-r38: Frame-Triole als Spiegelseite der Triality (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H23_Frame_Triole_Triality.md` (Commit 55043f8), Skript `llm/k79_test_h23.py`, Ausgabe `llm/k79_out.txt`,
Ergebnis `llm/Ergebnis_H23_Frame_Triole_Triality.md`, Runde `sec:v490-r38-frame-triole-triality`.

**K84.1 (M).** ρ(x, y, z) = (x̄, z̄, ȳ) ist ein äußerer Automorphismus von 𝔤 der Ordnung 2: Platz 1 behält seine Klasse, 2 und 3 tauschen (H23a).
**K84.2 (M).** ρ-fest: 𝔰𝔬(7) (dim 21); Platz 1 = 1 ⊕ 7 (invariante Gerade ℝ·1), Platz 2, 3 je irreduzibel 8 und äquivalent (H23b). Vorzeichen
mit s₁s₂s₃ = 1 (ℤ₂ × ℤ₂), (1, −1, −1) trivial auf Platz 1 (H23c, trivial). S₃ auf den Plätzen (H23d). 𝔤₂ ⊂ 𝔰𝔬(7), Farbe fest unter ganz S₃ (H23e).
**K84.3 (S).** Lesart: Photon = Vektor-Platz, Materie/Tachyon = Spinor-Plätze (Chiralitätspaar); welcher Platz Photon ist, ist die Wahl einer der
drei Transpositionen (Konvention F: Photon = entarteter Fixpunkt). Offen: Frames und Generationen können nicht auf derselben Ebene auf den
Plätzen liegen (zwei Zoomstufen nötig). Spur für Test 3: M ↔ T als Chiralitätswechsel. Kein Guard verbraucht.

### K85 — Vorab festgelegter Test H24 und Companion-Runde v4.9.0-r39: Ketten verschiedener Länge unter Zoom und gemischten Readouts (2026-10-23)

Autoridee (2026-10-23): Die gemischten Readouts waren gedacht, damit die Generationen bei oft genug wiederholtem Zoom einen Kreis bilden;
verschiedene Moduln (Kettenlängen) sollten verschiedene Lesarten geben. Die neue Kontraktion (`def:two-sided-admissible-contractions`)
wurde eingeführt, damit klassische Tensorrechnung weiter funktioniert und gemischte Kanäle kontrahiert werden können; kaum benutzt; das
Paper ist aus Sicht eines Frames geschrieben. Vorab-Notiz `llm/Vorab_Notiz_H24_Ketten_Module_Readouts.md` (Commit 8c89481), Skript
`llm/k80_test_h24.py`, Ausgabe `llm/k80_out.txt`, Ergebnis `llm/Ergebnis_H24_Ketten_Module_Readouts.md`, Runde `sec:v490-r39-chains-zoom-mixed`.

**K85.1 (M).** Modell: Kette ⟨g⟩ der Länge m; Stufe j sieht ⟨g^{2^j}⟩ (Bit β_j = 2^j); Maske S, k = Σ 2^j, Lesart Σ ⟨g^k⟩ oder ∨ ⟨g^{2^j}: j ∈ S⟩.
**K85.2 (M).** Ungerade Ketten behalten ihre Länge; τ^{2^j} = τ^{(−1)^j}, τ⁻¹ = ρτρ (H24a). Ketten 2^a verschwinden ab Stufe a; in G = S₃ × D₄
sichtbar: Stufe 0 {1,2,3,4,6,12}, Stufe 1 {1,2,3,6}, ab Stufe 2 {1,3} ⊂ ⟨τ⟩ (H24b, H24e). Masken (m = 3, 6 Bits): Σ sieht bei 21 von 63 Masken eine
Generation, ∨ immer drei (H24c); allgemein Σ: m/gcd(m,k), ∨: m/gcd(m, 2^{min S}), ungerader Anteil unter ∨ erhalten (H24d). Elementar.
**K85.3 (S).** Lesart: Generationenkreis = einziges, was tiefen Zoom überlebt; Frames grob, Generationen tief (löst K84-Spannung im Modell);
jede zweite Stufe im ρ-gespiegelten Frame. Textlesart: Selektor-Kontraktion χ_mn R^m S^n komponiert verträgliche Moden = Σ; Boolesche Maske = ∨;
gerade mit ungerader Stufe kontrahiert gibt τ³ = 1 (blind für den Kreis). Vordere Indizes = Frame, im Hauptteil nie variiert (Ein-Frame-Problem).
Kein Guard verbraucht.

### K86 — Vorab festgelegter Test H25 und Companion-Runde v4.9.0-r40: zweiseitige Kontraktion über Frames, schwache SU(2) (2026-10-23)

Autorhinweis (2026-10-23): Die neue Kontraktion ist noch nie benutzt oder getestet worden; es wird nicht erwartet, dass sie sofort
funktioniert. Vorab-Notiz `llm/Vorab_Notiz_H25_Zweiseitige_Kontraktion_Frames.md` (Commit d1aba48), Skript `llm/k81_test_h25.py`,
Ausgabe `llm/k81_out.txt`, Ergebnis `llm/Ergebnis_H25_Zweiseitige_Kontraktion_Frames.md`, Runde `sec:v490-r40-two-sided-frames`.

**K86.1 (M).** Vorderseite = ℂ-Faktor mit R (linear), T, J_B (antilinear). Regel 1 ω_α X^α: R-invariant, unter T, J_B konjugiert (H25b).
Regel 2 bilinear q: R ↦ −q, T ↦ q̄, J_B ↦ −q̄; hermitesch h D₄-invariant (H25c). Vorne/hinten vertauschen auf W (H25a, Kontrolle).
**K86.2 (M).** Zentralisator von 𝔰𝔲(3)_c in der Triality-Algebra: dim 2, abelsch (H25d); *Nachkontrolle:* = span(L_{e₇}, R_{e₇}) auf jedem Platz,
die Erzeuger von Q. Auf W: L_q, R_q zwei 𝔰𝔲(2), vertauschen mit Farbe und D₄. Kein Element wirkt nur auf einem Spinor-Platz (H25e).
**K86.3 (S).** Notation ist frame-kovariant, nicht frame-invariant; bilinearer Vergleich trägt das tachyonische Vorzeichen, hermitescher ist
frame-blind (inhaltliche Wahl). Triality-Ebene trägt Farbe und Ladung, keine schwache Wechselwirkung; schwache SU(2) nur im ℍ-Faktor
(links oder rechts); Lesart „schwache SU(2) = eine Seite“, nicht gezeigt; ℍ-Überbelegung bleibt. Vorschlag Frame-Klausel für Regel 1/2
(Autorentscheidung). Kein Guard verbraucht.

### K87 — Vorab festgelegter Test H26 und Companion-Runde v4.9.0-r41: Verteilung der Rollen des ℍ-Faktors (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H26_Verteilung_H_Faktor.md` (Commit 1876b55; Ladungsmuster vorab analytisch offengelegt), Skript
`llm/k82_test_h26.py`, Ausgabe `llm/k82_out.txt`, Ergebnis `llm/Ergebnis_H26_Verteilung_H_Faktor.md`, Runde `sec:v490-r41-quaternion-roles`.

**K87.1 (M).** Aufteilung D: Lorentz L_q, i·L_q (links), schwach R_q mit T₃ = −(i/2)R_k (rechts), Farbe auf 𝕆, Frames auf ℂ, Generationen auf den
Triality-Plätzen. Schwach vertauscht mit Lorentz, Farbe, Q; T fixiert Drehungen, kehrt Boosts um (H26a); Generationen-ℤ₃ vertauscht mit allem (H26e).
**K87.2 (M).** Y/2 := Q − ½, Q_em := T₃ + Y/2: Sektor 0 → (0, −1), 2/3 → (2/3, −1/3), 1/3 → (1/3, −2/3), 1 → (1, 0), Farbe Singulett/Triplett/
konj. Triplett/Singulett (H26b). T Q_em T⁻¹ = −Q_em, T (Y/2) T⁻¹ = −Y/2 (H26c). Keine schwachen Singuletts, T² = 3/4 überall (H26d).
**K87.3 (S).** Überbelegung von ℍ in D aufgehoben (Seiten + Triality); Test 4 unter der Wahl Y/2 = Q − ½ positiv (Muster der linkshändigen Dubletts
und Konjugierten), Wahl nicht erzwungen; Sektor-Zuordnung nach Furey, ähnliche Muster in der Literatur. Frame T = Ladungskonjugation C
(der Versatz in Q ↦ 1 − Q ist der Hyperladungs-Versatz ½). D unvollständig: rechtshändige Singuletts fehlen, Chiralität offen. Kein Guard verbraucht.

### K88 — Vorab festgelegter Test H27 und Companion-Runde v4.9.0-r42: Kompensator der MM-Matrix als Chiralitätsprojektor (2026-10-23)

Autorhinweis (2026-10-23): Für die fehlende Singulett-Hälfte war die MM-Matrix gedacht, die verschiedene HC in sich tragen sollte. Vorab-Notiz
`llm/Vorab_Notiz_H27_MM_Kompensator_Chiralitaet.md` (Commit 614ac3e; Muster vorab analytisch offengelegt), Skript `llm/k83_test_h27.py`, Ausgaben
`llm/k83_out.txt` und `llm/k83_out_erstlauf.txt`, Ergebnis `llm/Ergebnis_H27_MM_Kompensator_Chiralitaet.md`, Runde `sec:v490-r42-mm-compensator-chirality`.
Erstlauf meldete H27b widerlegt wegen eines Rundungsfehlers im Skript (Y-Werte auf 9 Stellen, Nullraum-Toleranz 10⁻¹⁰); nur die Rundung korrigiert.

**K88.1 (M).** C_ch = ½(id + J), J = i·L_{e₇}: hermitescher Projektor vom Rang 16, vertauscht mit Farbe, Lorentz, R_q, Q; Bild = Q-Sektoren 0 und 2/3 (= P₋ aus K81).
**K88.2 (M).** Mit T_a′ = C_ch T_a, Y/2 = Q − ½ + (1 − C_ch)T₃, Q_em = T₃ + Q − ½: (3,2,1/6) 12, (1,2,−1/2) 4, (3̄,1,−2/3) 6, (3̄,1,1/3) 6, (1,1,1) 2,
(1,1,0) 2 — eine Generation mit ν_R (16 Weyl × 2 Lorentz); Y vertauscht mit SU(2)′, Farbe, Lorentz (H27b). Anomalie-Spuren null (H27c).
SU(2)′ nur auf dem Bild; T C_ch T⁻¹ = 1 − C_ch (H27d). 𝓜 = λ₀C_ch + λ₁(1 − C_ch) mit C_ch als Spektralprojektor (H27e, Kontrolle).
**K88.3 (S).** Lesart: Ein Kompensator der MM-Matrix trennt die Chiralitäten; im Modell ist das die Chiralität. T vertauscht die chiralen Hälften: M- und
T-Frame = Teilchen und Antiteilchen mit gespiegelter Chiralität (Lesart). 𝓜₁₆ ist 16 × 16, eine Generation mit ν_R hat 16 Weyl-Zustände (festgehalten,
nicht gedeutet). Konstruktion unter Wahlen (J, Y-Formel), keine Herleitung; ähnliche Konstruktionen in der Literatur (ℂ⊗ℍ⊗𝕆). Kein Guard verbraucht.

### K89 — Vorab festgelegter Test H28 und Companion-Runde v4.9.0-r43: Wahl des Chiralitätsprojektors durch Anomaliefreiheit (2026-10-23)

Autorfrage (2026-10-23): wieso genau diese Wahl. Vorab-Notiz `llm/Vorab_Notiz_H28_Warum_diese_Wahl.md` (Commit 9b8b360; Sektor-Zuordnung, Fall iR_{e₇}
und Tr Q = 4 vorab von Hand, offengelegt), Skript `llm/k84_test_h28.py`, Ausgabe `llm/k84_out.txt`, Ergebnis `llm/Ergebnis_H28_Warum_diese_Wahl.md`,
Runde `sec:v490-r43-choice-anomalies`.

**K89.1 (M).** Kommutant von Farbe und Q auf ℂ⊗𝕆 = die vier Sektor-Projektoren; genau vier Chiralitätsprojektoren (Bild Singulett + Triplett):
J = iL_{e₇} {0, 2/3}, −iL_{e₇} {1/3, 1}, iR_{e₇} {0, 1/3}, −iR_{e₇} {2/3, 1} (H28a). Tr Y = 0 genau für s = −½ (H28b).
**K89.2 (M).** Bei s = −½ anomaliefrei nur J = ±iL_{e₇}; J = ±iR_{e₇}: Tr Y³ = ±3/2, SU(2)²U(1) = ∓2 (über beide Dublett-Zustände) (H28c).
T(iL_{e₇})T⁻¹ = −iL_{e₇} (H28d).
**K89.3 (S).** Die Wahl aus r42 ist unter den Annahmen bis auf den Frame erzwungen (Farbe, Ladungserhaltung, Anomalien); die Auswahl trifft wieder
links gegen rechts. Annahmen bleiben: schwache SU(2) rechts auf ℍ, Q_em = T₃ + Q + s, Projektor auf ℂ⊗𝕆. Keine Vorhersage (SM ist bekannt
anomaliefrei). Kein Guard verbraucht.

### K90 — Vorab festgelegter Test H29 und Companion-Runde v4.9.0-r44: Massenterme als Frame-Kopplungen, Brechungsstufen (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H29_Brechung_Massen_Mischung.md` (Commit 85d065a; bekannte Teile offengelegt), Skript `llm/k85_test_h29.py`, Ausgabe
`llm/k85_out.txt`, Ergebnis `llm/Ergebnis_H29_Brechung_Massen_Mischung.md`, Runde `sec:v490-r44-mass-frame-couplings`.

**K90.1 (M).** Verbinder (vertauschen mit Farbe und L_q): 24-dim. linear wie antilinear (H29a). Antilinear Bild ← Kern: 8-dim. (Lepton 4, Quark 4),
genau Dubletts Y/2 = ±½ (H, H̃) (H29b). Linear Bild ← Kern: 4-dim., nur Lepton, Y/2 ∈ {−½, −3/2} (H29c). Eichinvariant: keiner Bild ← Kern, genau
einer Kern ← Kern, nur auf ν^c (H29d).
**K90.2 (M).** Plätze: S₃-symmetrisch ⇒ höchstens zwei Eigenwerte; ℤ₃ ⇒ a + 2|b|cos(θ + 2πk/3) (Brannen), K = 2/3 ⇔ |b| = a/√2; up und down beide
ℤ₃ ⇒ |V| Permutation (H29e).
**K90.3 (S).** Massenterme = antilineare Frame-Kopplungen (M ↔ T), wie die Feder Materie–Tachyon in `thm:spring`; benötigte Brechung = Dublett Y/2 = ½,
Ursache offen; See-Saw-Lesart für ν (nicht gerechnet). Brechungsstufen: Masse ⇐ Frame-Kopplung, Aufspaltung ⇐ ρ-Brechung (erklärt die Widerlegungen
H11, H16–H18), Mischung ⇐ τ-Brechung. Koide-Form (r10) = Massenform einer ℤ₃-symmetrischen, ρ-gebrochenen Kopplung; |b|/a, θ offen. Kein Guard verbraucht.

### K91 — Vorab festgelegter Test H30 und Companion-Runde v4.9.0-r45: Chiralität bricht die Spiegelung der Triality-Form (2026-10-23)

Autor (2026-10-23): „prüfe mal, ob es sich aus der Struktur begründen lässt“. Vorab-Notiz `llm/Vorab_Notiz_H30_Brechung_aus_Chiralitaet.md`
(Commit d755a08; c L_{e₇} c = −R_{e₇} vorab offengelegt), Skript `llm/k86_test_h30.py`, Ausgabe `llm/k86_out.txt`, Ergebnis
`llm/Ergebnis_H30_Brechung_aus_Chiralitaet.md`, Runde `sec:v490-r45-chirality-breaks-reflection`.

**K91.1 (M).** c L_{e₇} c = −R_{e₇}, c R_{e₇} c = −L_{e₇}; reines Vertauschen (x, z, y) keine Symmetrie von t (H30a). Modell I (gleiche Chiralität): von den
sechs Symmetrien erhalten 1, τ, τ² die Chiralität, ρ, τρ, τ²ρ bilden sie auf ½(1 − iR_{e₇}) (anomal) ab (H30b). Im T-Frame ebenso (−iL ↦ +iR).
**K91.2 (M).** (L, L, L) ∉ 𝔤; Fortsetzung von A = L_{e₇}: (L_{e₇}, R_{e₇}, −L_{e₇} − R_{e₇}), nicht τ-invariant (H30c); Platz 2 iR_{e₇} (anomal), Platz 3 keine
Involution (H30d).
**K91.3 (S).** ρ-Brechung folgt aus der Struktur (Transposition enthält c, c tauscht links/rechts, Anomaliefreiheit wählte links) ⇒ Bedingung für
Massenaufspaltung (r44) erfüllt; erklärt die Widerlegungen H11, H16–H18 (Potentiale ohne Chiralität). Stärke der Brechung (θ, |b|/a) offen. τ bleibt
in Modell I; Generationen = äquivalente Kopien (Umstufung von K83). Mischung braucht eine andere Quelle der τ-Brechung. Kein Guard verbraucht.

### K92 — Vorab festgelegter Test H31 und Companion-Runde v4.9.0-r46: gemischte Readouts und die Brechung der Triality (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H31_Tau_Brechung_Readouts.md` (Commit ea74447; H31a aus Kommutativität, H31c Störungstheorie offengelegt), Skript
`llm/k87_test_h31.py`, Ausgabe `llm/k87_out.txt`, Ergebnis `llm/Ergebnis_H31_Tau_Brechung_Readouts.md`, Runde `sec:v490-r46-readouts-triality-breaking`.

**K92.1 (M).** Verschiebungs-Readouts (Produkte von P^{2^j}, Untergruppen-Mittel, Selektor-Kontraktionen) vertauschen mit τ; |V| bleibt Permutation (H31a, 200 Fälle).
**K92.2 (M).** Art-Masken D_S (Generationen als Auslesearten) vertauschen nicht mit τ; δ > 0 ⇒ Mischung, auch bei gleicher Maske für up und down (H31b).
Mischung linear in δ, ≤ δ(1/Lücke_u + 1/Lücke_d)/3 (H31c). Masken reell, frame-frei (H31d).
**K92.3 (S).** Die gemischten Readouts aus dem Hilbert-Shift erzeugen keine Mischung (Verbot); erst generationen-selektive Masken. Qualitativ: kleine Mischung
bei großer Hierarchie (CKM), größere bei dichten Massen (Neutrinos); keine Zahlen. Spannung: Mischung ist messbar, also muss die Maske Teil der Kopplungen
sein, nicht des Beobachters; Herkunft offen. Kein Guard verbraucht.

### K93 — Vorab festgelegter Test H32 und Companion-Runde v4.9.0-r47: Generationen-Maske aus der triality-kovarianten Chiralität (2026-10-23)

Vorab-Notiz `llm/Vorab_Notiz_H32_Maske_aus_Triality.md` (Commit 65c5b44; Gewichte und T Δ T⁻¹ = −Δ vorab offengelegt), Skript `llm/k88_test_h32.py`,
Ausgabe `llm/k88_out.txt` (mit Nachkontrolle), Ergebnis `llm/Ergebnis_H32_Maske_aus_Triality.md`, Runde `sec:v490-r47-mask-from-triality`.
Modellannahme (nicht hergeleitet): Δ wirkt als schwache Störung, M ↦ M + ε(WM + MW); Partner im T-Frame gelesen.

**K93.1 (M).** Δ skalar auf den Q-Sektoren: 0 (0, 0, −3), 1/3 (0, 2, 1), 2/3 (0, −2, −1), 1 (0, 0, 3) (H32a). T Δ T⁻¹ = −Δ, antisymmetrisch unter q ↔ 1 − q;
W_q = diag(0, −2, −1) (up und down), W_l = diag(0, 0, −3) (H32b). Fourier-Basis: alle Nebendiagonalen gleich, |W_q| = 1/√3, |W_l| = 1, Verhältnis √3 (H32d).
**K93.2 (M).** H32c widerlegt: Mischung in allen 200 Fällen ≠ 0, aber linear in ε nur in 196/200 bei ε = 10⁻³, 10⁻⁴; Nachkontrolle: die 4 Fälle fast entartet
(relative Lücke ≤ 3·10⁻³, Median 7·10⁻²); bei ε = 10⁻⁶, 10⁻⁷ alle linear.
**K93.3 (S).** Unter der Annahme kommt die Generationen-Maske aus der Struktur, Form fest, nur ε gewählt; up und down gleiche Maske, Mischung trotzdem (r46).
Demokratisch in der Generationen-Basis, Leptonen √3 stärker: Richtung große PMNS-, kleine CKM-Winkel (qualitativ). τ-Brechung aus der Wahl eines
Referenzplatzes (Platz 1: Gewicht 0). Annahme, ε, Zirkulanten-Parameter und Zahlen offen. Kein Guard verbraucht.

### K94 — Companion-Runde v4.9.0-r48: Ladungs-Sektoren aus der Oktonionen-Multiplikation in Lean (2026-10-24)

Lean-Modul `formal/QSFormal/Sektoren.lean` (nur Lean-Kern, Standard-Axiome), Runde `sec:v490-r48-sectors-formal`. Keine neue Vorhersage, daher keine
Vorab-Notiz; sichert r34, r35, r42, r43, r47. Komplexe Einheit überall die äußere i (ℂ-Faktor der Ablage), T = Konjugation dieses Faktors.

**K94.1 (M).** (iL)² = (iR)² = 1, iL iR = iR iL für alle x ∈ ℂ⊗𝕆. P_s = ¼(1 + ℓ iL)(1 + r iR) sind Projektoren, paarweise orthogonal, Summe 1,
auf dem Bild iL = ℓ, iR = r. Spuren: Sp L = Sp R = 0, Sp(LR) = 4, Sp P_s = 1, 3, 3, 1 (Farbdimension). Auf P_s: 6Q = 3 − ℓ − 2r, Δ₂ = r − ℓ, Δ₃ = −2ℓ − r
(Gewichte von K93.1). T iL = −iL T, T P_(ℓ,r) = P_(−ℓ,−r) T (Ladungskonjugation). σ vertauscht auf der Basis mit iL, iR, P_s.
**K94.2 (S).** Die Tabellen `sectors`, `colourDim`, `q6`, `weights` aus `Ladungen.lean` sind damit Eigenschaften von O.mul statt Setzungen; die
Vorzeichenkonvention der Numerik (k75, k84) stimmt mit der formalen überein. Nicht formalisiert: Rang = Spur eines Projektors, Fortsetzung von σ
von der Basis auf alle x (Linearität), die physikalischen Lesarten und alle Zahlen. Kein Guard verbraucht.

### K95 — Vorab festgelegter Test H33 und Companion-Runde v4.9.0-r49: Die Achse e₇ trägt B − L, nicht die elektrische Ladung (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H33_Photon_Achse_e7.md` (Commit ec06de3; Ergebnis vorab analytisch gesehen, offengelegt), Skript `llm/k89_test_h33.py`,
Ausgabe `llm/k89_out.txt`, Ergebnis `llm/Ergebnis_H33_Photon_Achse_e7.md`, Runde `sec:v490-r49-e7-axis-b-minus-l`, Lean `b_minus_l`,
`qem_not_sector_function` in `formal/QSFormal/Sektoren.lean`. Geprüft: Deutung „Ladung = Kopplung an e₇, e₇ = Photon-Achse“ (Besprechung nach r48).

**K95.1 (M).** span_ℂ(1, e₇) = Sektoren Q = 0 ⊕ Q = 1, dort L_{e₇} = R_{e₇} (H33a). Auf einer Generation 2(Q − ½) = B − L, Y/2 = (B − L)/2 + T₃^R,
Q_em = T₃^L + T₃^R + (B − L)/2 (H33b). Kein a + b iL + c iR + d iL iR ist Q_em, beste Abweichung ½ (H33c). Alle bestätigt.
**K95.2 (S).** Deutung in der gestellten Form widerlegt: e₇ ist die Achse von B − L (und mit iL der Chiralität); das Photon ist die Mischung
der e₇-Achse mit T₃ aus ℍ. Ladungsformel links-rechts-symmetrisch (Pati-Salam-Form). Textbefund: span(1, e₇) ist im Companion Photon-Kern K₃
(Kompensator-Bild), Träger von ν_R und Ebene von ω: Doppelbelegung wie r36, Kandidat für einen Statusvermerk. Offen: e₇ als Bezugsachse
der Frames. Kein Guard verbraucht.

### K96 — Vorab festgelegter Test H34 und Companion-Runde v4.9.0-r50: Die Maske aus r47 erklärt die Mischung nicht (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H34_Mischung_aus_Maske.md` (Commit 8d8b761), Skript `llm/k90_test_h34.py`, Ausgabe `llm/k90_out.txt` (Erstlauf
`k90_out_erstlauf.txt`: Abbruch in einer Diagnose-Ausgabe nach H34a; korrigiert nur diese und m₁ = 0), Ergebnis `llm/Ergebnis_H34_Mischung_aus_Maske.md`,
Runde `sec:v490-r50-mixing-test`. Daten: Massen bei M_Z (Huang, Zhou 2021), NuFIT 6.0 (NO), PDG 2024.

**K96.1 (M).** Lösungen mit den gemessenen Massen nur bis ε ≈ 0.06 (up), 0.125 (down), 0.13 (e), 0.025–0.23 (ν). H34a widerlegt: 0 von 7488
(ε, Zweigpaar) treffen |V_us|, |V_cb|, |V_ub| zugleich auf ±20 %, nächster Fall 96 % daneben. H34b widerlegt (kein ε aus H34a), H34c zählt nicht.
Nachkontrolle: Leptonen allein mit eigenem ε erreichen die 3σ-Bereiche nie (nächster Fall bis 71 % daneben).
**K96.2 (S).** Modellannahme von r47 (Maske als schwache Störung zirkulanter Kopplungen) für die Mischung widerlegt. Grund: ε² W C W erzeugt
Massen ≈ (2/3) ε² m_t bzw. 2 ε² m_τ, die Hierarchie erzwingt kleine ε, dort ist die Maske zu demokratisch. **Umgestuft:** K93.3 (Richtung große
PMNS-, kleine CKM-Winkel) als quantitative Aussage zurückgezogen; K93.1 (Form, Frame, Fourier, √3) unberührt. Herkunft der Mischung offen.
Kein Guard verbraucht.

### K97 — Vorab festgelegter Test H35 und Companion-Runde v4.9.0-r51: e₇ und die Frames (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H35_e7_als_Frame_Achse.md` (Commit 42e4fcc; Ergebnis vorab analytisch gesehen, offengelegt), Skript `llm/k91_test_h35.py`,
Ausgabe `llm/k91_out.txt`, Ergebnis `llm/Ergebnis_H35_e7_als_Frame_Achse.md`, Runde `sec:v490-r51-e7-frames`, Lean `R_iL`, `R_iR`, `R_P4`.
Unter A_ℂ (K77.8): Tachyon-Abbildung z ↦ iz = R (σ_y), Zeitumkehr T = z ↦ z̄ (σ_z, Porttausch), J_B = R ∘ T (σ_x).

**K97.1 (M).** R vertauscht mit iL, iR, Q, B − L, su(3) und allen P_s; T und J_B: P_(ℓ,r) ↦ P_(−ℓ,−r) (H35a). L_{e₇} vertauscht mit Stab(e₇); farbverträgliche
J-antilineare K bilden einen 2-dimensionalen Raum und verschwinden auf e₇^⊥ (H35b). φ(x + iy) = x + y e₇ übersetzt iz, z̄, i z̄ in L_{e₇}, Konjugation, Produkt (H35c).
**K97.2 (S).** e₇ ist Bezugsachse der Frames nur teilweise: für die Tachyon-Abbildung auf ganz 𝕆, für alle drei auf span(1, e₇) (Frame-Ebene = Ebene des
Photon-Kerns). Ladungen, B − L, Chiralität sind zwischen Materie und Tachyon frame-frei; Ladungskonjugation ist die Zeitumkehr T (Porttausch).
**Umgestuft/korrigiert:** In K87.3, K89 (r43.1(d)), K93 (r47 „Partner im T-Frame“), K94.1 und K95 sowie in den Frame-Zeilen von r41, r43, r47–r49 ist mit „T“
die Zeitumkehr gemeint, nicht der Tachyon-Frame; in der Spalte M/T sind diese Ergebnisse gleich. Lean `frameT` = Zeitumkehr. Kein Guard verbraucht.

### K98 — Vorab festgelegter Test H36 und Companion-Runde v4.9.0-r52: exakte Kopplungsformen der Maske (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H36_Kopplungsform.md` (Commit 66c12ab; Froggatt-Nielsen-Erwartung offengelegt), Skript `llm/k92_test_h36.py`, Ausgabe
`llm/k92_out.txt` (Erstlauf ohne Zählung in der Nachkontrolle), Ergebnis `llm/Ergebnis_H36_Kopplungsform.md`, Runde `sec:v490-r52-coupling-forms`.
Form K: M = D C D (Partner über T), Form S: M = D C D⁻¹ (Partner über die Tachyon-Abbildung, Gewicht −W), D = exp(εW), C zirkulant, ein ε.

**K98.1 (M).** Zweige bis ε ≈ 3.5 (up), 2.3 (down). H36a widerlegt: 0 von 98 064 (K) innerhalb ±20 %, nächster Fall 36 % daneben (ε = 1.26: 0.144, 0.036, 0.0050).
H36c widerlegt: 0 von 102 528 (S), nächster 40 %. H36b, d widerlegt. Nachkontrolle: Leptonen allein K 0 von 163 398, S 12 von 125 922 (Zufallstreffer bei ε ≈ 0.5).
**K98.2 (S).** Beide exakten Formen näher als die lineare (36 % statt 96 %), Reihenfolge |V_us| ≫ |V_cb| ≫ |V_ub| reproduziert, Hierarchie begrenzt ε nicht mehr.
Fehlende Zutat offene Wahl: nicht zirkulante C oder ein ε je Sektor (dann keine Erklärung mehr). Kein Guard verbraucht.

### K99 — Vorab festgelegter Test H37 und Companion-Runde v4.9.0-r53: Kopplungen aus der Triality-Form (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H37_Kopplung_aus_Triality.md` (Commit e1ee9ec; Spurfreiheit und m₁* ≈ 0.035 eV vorab offengelegt), Skript `llm/k93_test_h37.py`,
Ausgabe `llm/k93_out.txt` (Erstlauf ohne Nachkontrolle, gleiche Kriteriumswerte), Ergebnis `llm/Ergebnis_H37_Kopplung_aus_Triality.md`, Runde
`sec:v490-r53-triality-couplings`. Kosmologie: Σm_ν < 0.0642 eV (DESI DR2 + CMB).

**K99.1 (M).** Reine Triality-Kopplung T(v) (nur verschiedene Plätze) ist spurfrei, auch D T(v) D: m₃ = m₁ + m₂ nötig; u, d, e verfehlen um 99.6/98.0/94.1 %;
Dirac-ν nur bei m₁* = 0.028 eV, Σm = 0.115 eV > 0.0642 eV → H37a widerlegt. Norm + Triality α·1 + T(v) ohne Maske: Quarks 0 Treffer (nächster 82 %, dicht
80 %), Leptonen 264 von 1.37·10⁷ nur bei m₁ = 0.05/0.1 eV (Σm 0.17/0.31 eV, kosmologisch ausgeschlossen) → H37b formal Teilbefund, physikalisch keiner.
H/H̃-Lesart (u, ν und d, e in verschiedenen Formen K/S): 0 Treffer, nächster 37 %/40 % → H37c widerlegt.
**K99.2 (S).** Verbot aus der Struktur: Massen brauchen eine Kopplung innerhalb eines Platzes; die Triality-Form allein kann keine Massen tragen. Keine aus der
Struktur nahe liegende Kopplung erklärt die Mischung; am nächsten bleibt K98 (D C D, zirkulant, 36 %). Herkunft der Mischung offen. Kein Guard verbraucht.

### K100 — Vorab festgelegter Test H38 und Companion-Runde v4.9.0-r54: ein ε je Sektor (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H38_Ein_eps_je_Sektor.md` (Commit d3555bf), Skript `llm/k94_test_h38.py`, Ausgabe `llm/k94_out.txt` (Erstlauf ohne Nachkontrolle,
gleiche Kriteriumswerte), Ergebnis `llm/Ergebnis_H38_Ein_eps_je_Sektor.md`, Runde `sec:v490-r54-eps-per-sector`. Formen K, S wie K98, ε_u, ε_d, ε_e, ε_ν
unabhängig; m₁ ∈ {0, 0.001, 0.003} eV (DESI). **Korrektur K98.2:** je Familie zwei ε für drei Winkel, eine Vorhersage bleibt (nicht „so viele Parameter wie Größen“).

**K100.1 (M).** Form K: Quarks 0 von 2.9·10⁷ (nächster 20.2 %), Leptonen 0.003 %. Form S: Quarks 294 von 3.2·10⁷ (0.0009 %), Region ε_u ∈ [1.36, 1.63],
ε_d ∈ [1.42, 1.47], bester Fall 7 % (0.2225, 0.0448, 0.0040); Leptonen 0.009 %, ε_e ∈ [0.44, 0.82], ε_ν ∈ [0.27, 0.55], alle zulässigen m₁. Regionen je Zweigpaar
zusammenhängend. Nachkontrolle: bei passendem |V_us|, |V_cb| liegt |V_ub| in [0.0034, 0.029], Median 0.018, nur 0.9 % passen; sin²θ₁₃ bei passendem θ₁₂, θ₂₃
in [0, 0.99], 0.8 % passen.
**K100.2 (S).** H38a widerlegt, H38b–d bestätigt: Form S mit vier ε nach Kriterium Kandidat. Inhaltlich schwach: die verbleibende Vorhersage ist nicht scharf,
Treffer im Ausläufer; eher Anpassung als Erklärung. ε_u ≈ ε_d, aber kein Treffer auf der Diagonale (H36c). Herkunft der ε-Werte offen. Kein Guard verbraucht.

### K101 — Vorab festgelegter Test H39 und Companion-Runde v4.9.0-r55: Lesart je Teilchenart als Untergruppe der A₄ (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H39_Restsymmetrie_Lesarten.md` (Commit 5c916b8; Klein- und TM2-Erwartung offengelegt; Ankündigung „tribimaximal“ korrigiert, braucht S₄),
Skript `llm/k95_test_h39.py`, Ausgabe `llm/k95_out.txt` (Erstlauf ohne Nachkontrolle, gleiche Kriteriumswerte), Ergebnis `llm/Ergebnis_H39_Restsymmetrie_Lesarten.md`,
Runde `sec:v490-r55-residual-readouts`. Autorfrage: jede Teilchenart eine eigene Lesart. Regel: Dirac (u, d, e) lesen mit ⟨τ⟩ ≅ ℤ₃ (zirkulant, r44), Neutrinos
(Majorana möglich, r44) mit G_M ⊂ A₄ (K77.4).

**K101.1 (M).** Untergruppen von A₄: Ordnungen 1, 2, 3, 4, 12 (1, 3, 4, 1, 1). Klein: alle |U_ij|² = 1/3, kein Treffer; andere ℤ₃: kein Treffer. ℤ₂: Treffer genau
bei fester Spalte ν₂ (TM2): sin²θ₁₂ = 1/(3 cos²θ₁₃) ∈ [0.3402, 0.3414] scharf, sin²θ₂₃ ∈ [0.399, 0.601] frei. Gleiche Lesart für u, d ⇒ V_CKM = 1 in führender Ordnung.
Nach Wortlaut (Spannweiten über alle Zuordnungen) Anpassung mit einem Winkel. Nachkontrolle: JUNO 2025 sin²θ₁₂ = 0.3092 ± 0.0087 ⇒ TM2 3.6 σ darüber.
**K101.2 (S).** Erste Lesart, die CKM klein und PMNS groß ordnet (H34–H38 nicht). Quantitativ die bekannte TM2-Mischung der A₄-Literatur; θ₁₂ unter Druck durch JUNO,
θ₂₃ und CKM-Winkel offen (Korrekturen, etwa aus der Maske). Kein Guard verbraucht.

### K102 — Vorab festgelegter Test H40 und Companion-Runde v4.9.0-r56: Kalibrierung der Ausleseschicht (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H40_Kalibrierung_Ausleseschicht.md` (Commit fdb27ae), Skript `llm/k96_test_h40.py`, Ausgabe `llm/k96_out.txt`, Ergebnis
`llm/Ergebnis_H40_Kalibrierung_Ausleseschicht.md`, Runde `sec:v490-r56-readout-calibration`. Autoridee: Kern + Ausleseschicht; Schicht so einstellen, dass sie
reale Werte liefert, und aus den Einstellungen die Herkunft lernen. Schicht: je Sektor Brannen-C (a, |b|, θ), ε, Form S; 16 Einstellungen (+ m₁) für 17 Größen.

**K102.1 (M).** Kalibriert (H38-Kombinationen): ε_u [1.36, 1.63], ε_d [1.42, 1.47], ε_e [0.44, 0.82], ε_ν [0.27, 0.55]; |b|/|a| u [0.95, 1.03], d [0.99, 1.08],
e [1.2, 6.4], ν [0.45, 1.57]; θ fast der ganze Bereich. 14 Kandidaten (1/3, …, β_sym, γ_L) treffen 76-mal, Zufall im Mittel 65.3, p = 0.019 → H40a widerlegt
(Schwelle 0.01); H40b (ε-Verhältnis mit 1) zählt nicht. |b|/|a| ≈ 1 der Quarks folgt aus der Hierarchie (λ ≈ (0, 0, 1) ⇒ C ≈ ⅓(1 + P + P²)).
**K102.2 (S).** Keine Struktur in den Einstellungen über Zufall hinaus, weil die Daten sie kaum festlegen (Kompression fehlt). Der Weg braucht weniger Einstellungen
(Regel für die Brannen-Größen, Lesarten aus Untergruppen wie K101) oder schärfere Daten. Lesarten ohne Kriterium: Master-Gleichung γ ↔ ε, β/m₀ ↔ |b|/a; Beltrami
|μ| = (K − 1)/(K + 1) ≈ 0.88–0.93 (u), 0.89–0.90 (d), 0.58–0.84 (e), 0.38–0.68 (ν). Teichmüller steht im Korpus auf der RH-/Closure-Seite, nicht in den
Feldgleichungen. Kein Guard verbraucht.

### K103 — Vorab festgelegter Test H41 und Companion-Runde v4.9.0-r57: TM2 mit der Maske als Korrektur (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H41_TM2_mit_Maskenkorrektur.md` (Commit 74bd018), Skript `llm/k97_test_h41.py`, Ausgabe `llm/k97_out.txt`, Ergebnis
`llm/Ergebnis_H41_TM2_mit_Maskenkorrektur.md`, Runde `sec:v490-r57-tm2-correction`. Leptonen: geladene zirkulant (ℤ₃) mit Form-S-Korrektur ε_e; Neutrinos Majorana,
ℤ₂-invariant (alle drei ℤ₂), Winkel φ, Form-K-Korrektur; A: ε_ν = 0, B: ε_ν = ε_e; je zwei Einstellungen für drei Winkel. JUNO 2025 als 2σ-Bereich für θ₁₂.

**K103.1 (M).** A: 776 von 4.0·10⁶ Fällen mit θ₁₂ (JUNO 2σ), θ₁₃, θ₂₃ (NuFIT 3σ), ε_e 0.03–0.64. B: 3 808 von 2.1·10⁷, ε ≈ 0.04–0.06 und 0.62–0.64. H41a, b bestätigt.
Bei passendem θ₁₂, θ₁₃: sin²θ₂₃ ∈ [0.309, 0.537] (A), [0.314, 0.515] (B) → H41c (Breite < 0.05) widerlegt.
**K103.2 (S).** Die TM2-Spannung mit JUNO (K101) ist durch die Maske als Korrektur auflösbar; die Lesart aus r55 bleibt. Anpassung mit zwei Einstellungen, θ₂₃ nicht
vorhergesagt. Nachträglich bemerkt: sin²θ₂₃ ≲ 0.54 in beiden Varianten (oberer Oktant spräche dagegen), müsste vorab festgelegt werden. Kein Guard verbraucht.

### K104 — Vorab festgelegte Vorhersage H42: sin²θ₂₃ ≤ 0.54 (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H42_Grenze_theta23.md` (Commit 1c7f3e1). Aus K101/K103 (TM2-Lesart mit Maskenkorrektur): sin²θ₂₃ ≤ 0.54 in normaler Ordnung. Nachträglich
bemerkt, daher Vorhersage erst ab dieser Notiz; NuFIT 6.0 (0.561 ohne, 0.470 mit SK-atm) prüft nicht. Prüfung: erste globale Auswertung oder DUNE/Hyper-K nach dem
2026-10-24; widerlegt bei 2σ-Intervall ganz über 0.54, bestätigt ganz darunter, sonst offen. Eine Bestätigung prüft nur die Grenze, nicht die Lesart. **Ausstehend.**

### K105 — Vorab festgelegter Test H43 und Companion-Runde v4.9.0-r58: CP-Phase der korrigierten TM2-Lesart (2026-10-24)

Vorab-Notiz `llm/Vorab_Notiz_H43_CP_Phase_aus_TM2.md` (Commit 59d8d04), Skript `llm/k98_test_h43.py`, Ausgabe `llm/k98_out.txt`, Ergebnis
`llm/Ergebnis_H43_CP_Phase_aus_TM2.md`, Runde `sec:v490-r58-cp-phase`. δ aus Jarlskog-Invariante und |U_μ1|² für alle Treffer von K103.

**K105.1 (M).** A: |sin δ| ∈ [0.174, 0.999], cos δ ∈ [−0.980, 0.985]; B: [0.172, 0.999], [−0.981, 0.985]. Breite > 0.3 → H43a, b widerlegt; keine Vorhersage H44.
**K105.2 (S).** δ durch die Lesart nicht festgelegt, nur |sin δ| < 0.17 tritt nicht auf (schwach, gitterabhängig). Die korrigierte TM2-Lesart bleibt Anpassung mit zwei
Einstellungen; schärfer nur, wenn die Korrektur selbst aus der Struktur folgt. Kein Guard verbraucht.

---

## 8. Änderungsprotokoll

- v1 (2026-10-19): Erstfassung der Kernkarte.
- v1.1 (2026-10-19): K1 Signatur/Lorentz; Triolen-Lemma; Prüfpunkte in Abschnitt 2 aktualisiert.
- v1.2 (2026-10-19): K2 Lesart B — invariante Sektoren, Spinoren als Informationsebene,
  Punkte aus Spinoren + Riemann-Takten.
- v1.3 (2026-10-19): K3 Primzahlen/ζ/Photonen (Corpus-Fundstellen, Primon-Gas, Prüfpunkt Stufenbegriff);
  Torus als Hopf-Urbild ergänzt.
- v1.4 (2026-10-19): K4 Primzahl-Qubit-Register, Primzahl-Uhr, Nullstellen als Orthogonalitätszeiten;
  Normierbarkeitsgrenze σ > 1.
- v1.5 (2026-10-19): K5 Bost–Connes-Einbettung, Phasenübergang β = 1; Prüfung des Riemann-Papers v4.15
  (unitäre Äquivalenz in Abschnitt 2 auf „offen“ gesetzt).
- v1.6 (2026-10-19): Nachtrag B8 (Mengen-Argument); K6 Sphären-Modell und Triolen-Hierarchie geprüft.
- v1.7 (2026-10-19): K6 im Companion umgesetzt als Runde **v4.8.0-r04** (`sec:v480-r04-riemann-decoupling`):
  Audit A1–A5, eigenständiger Heisenberg-Kompensator (lineares J), Kaskade = Projektion auf S₀,
  Triolen-Satz (konkurrente Fano-Linien), Abhängigkeitskarte; `R_dec = (0,0,0,1,1,1)`, Guards unverändert.
- v1.8 (2026-10-19): K7 korrigierte explizite Formel, Θ-Summen-Vermutung widerlegt (−0,1097 statt 0,893),
  GUE empirisch bestätigt; im Companion als v4.8.0-r05.
- v1.9 (2026-10-19): K8 Lesart B als v4.8.0-r06 in den Companion übernommen (Signatur, N(q), SO(3,ℂ),
  Triolen-Lemma, invariante Sektoren, Nullkegel = S₀).
- v2.0 (2026-10-19): K9 Sektor-Zuordnung (s > 0 Materie, s < 0 Tachyon), Dualitätswinkel, Rolle von t;
  im Companion als v4.8.0-r07. Guard-Linter unter `llm/training/guard_linter.py`.
- v2.1 (2026-10-20): K10 Test von P1 (Photon-Frame-Entfaltung) — nicht bestätigt; im Companion als v4.8.0-r08.
- v2.2 (2026-10-20): K11 P2 ausgeschlossen, P3 Koinzidenz; Kurzregister „Gesamtstand“ am Anfang;
  Grundabschnitte 2, 3, 5, 6 mit Statusvermerken neu eingeordnet; im Companion als v4.8.0-r09.
- v2.3 (2026-10-20): K12 Koide-Form als Triole, Lesart B ist Kinematik, Dynamik fehlt; im Companion als v4.8.0-r10.
- v2.4 (2026-10-20): K13 erster vorab festgelegter Test (δ = K/3) — widerlegt; im Companion als v4.8.0-r11.
- v2.5 (2026-10-20): K14 zweiter vorab festgelegter Test (Neutrinos, r = 1) — verträglich, Vorhersage NO,
  Σm_ν = 0,0592 eV festgeschrieben; K14.4 Bedeutung des Vorzeichens (kubische Invariante, nicht beobachtbar).
- v2.6 (2026-10-20): K15 dritter vorab festgelegter Test (Vorzeichen als Majorana-CP-Parität) — verträglich,
  nicht prüfbar; m_ββ ≤ 3,5 meV festgeschrieben. k15-MC-Fenster korrigiert (Werte unverändert).
- v2.7 (2026-10-20): K16 vierter vorab festgelegter Test (TM1 gegen TM2, 1:1) — TM1 stark bevorzugt
  (Δχ² = 10,3), TM2 disfavorisiert; Vorhersagen sin²θ₁₂ = 0,318, δ_CP ≈ 262° festgeschrieben.
  K16.4 Überlagerung: beide exakt ⇒ tribimaximal (ausgeschlossen); 1:1 ausgeschlossen; freies Gewicht ohne Test.
- v2.8 (2026-10-20): K17 fünfter vorab festgelegter Test (Hopf-Winkel als Mischwinkel) — gescheitert
  ((i) 0/32, (ii) entartet); Strukturbefund |w_e|² = sin²(γ/2); Nachbefund |U_e2|² = β_sym² (nur Kandidat).
- v2.9 (2026-10-20): K18 Rückwärtsanalyse (Lücken, minimale Änderungen, Kosten); Fano-Punkt-Stabilisator ≅ S₄
  (Ordnungsstatistik) als modellinterner Weg zu einer Flavour-Symmetrie. K18.3–4: Brechung der Fano-Symmetrie;
  TM2 ↔ Zentrum e₇, TM1 ↔ Zentrum in e₄,e₅,e₆, ausgeschlossene Variante ↔ Zentrum in e₁,e₂,e₃.
- v3.0 (2026-10-20): K18.5 echte Oktonionen-Wirkung: Stab(+e₇) ≅ Δ(96) (Ordnungsstatistik, 10 Klassen), Triplett
  irreduzibel. **Korrektur von K18.3–4:** TM1 = Lift mit Zentrum im Anti-Triplett e₁,e₂,e₃ (zweiter Lift dort
  gibt θ₁₃ = 0); TM2 = reine Vorzeichenwechsel; Zentrum e₇ liefert keine Involution; e₄,e₅,e₆ gibt die
  Δ(96)-Spalte.
- v3.1 (2026-10-20): K19 sechster vorab festgelegter Test (Kriterienliste für den Lift) — Hauptkriterium (S₃ mit
  der Triole) spricht gegen TM1; Hinweis: TM1 ⇔ Triole und Restspiegelung erzeugen S₄.
- v3.2 (2026-10-20): K19.3 Kaskade erzwingt Vollständigkeit nicht (sieht die Vorzeichen-Symmetrien nicht);
  Korrektur: ⟨Triole, h_TM1⟩ = Vorzeichen-Kern ⋊ S₃, nicht der Fano-Punkt-Stabilisator.
- v3.3 (2026-10-20): K20 siebter vorab festgelegter Test (Heisenberg-Kompensator) — kein Auswahlgrund;
  Nebenbefund: Cayley–Dickson-Involution kommutiert mit Triole und Lifts, wirkt CP-artig (Kandidat für H8).
- v3.4 (2026-10-20): K21 achter vorab festgelegter Test (Cayley–Dickson-CP) — μ-τ-Spiegelung exakt, sin²θ₂₃ = ½,
  δ_CP = 270°; gegen NuFIT Spannung (χ² = 8,8 bei 3 FG); Kurzregister ergänzt.
- v3.5 (2026-10-20): K22 Companion-Runde v4.8.0-r12 (H2–H8, Δ(96), Cayley–Dickson-CP); `prop:pmns-z3` und die
  θ₂₃-Zeile von `thm:op1op4-unified` als widerlegt eingeordnet.
- v3.6 (2026-10-20): K23 Nachprüfung mit JUNO 2026 (H2 gestützt, TM1 und H8 disfavorisiert); Vorab-Notiz H9
  (sin²θ₁₂ = 0,3086 für künftige JUNO-Daten).
- v3.7 (2026-10-20): K24 neunter vorab festgelegter Test (Assoziator) — kein Auswahlgrund; Strukturbefund
  [e₄,e₅,e₆] = −2e₇.
- v3.8 (2026-10-20): K25 Quark-Prüfung — Zielwerte schemaabhängig (2–4 %), Farbe und Generation im Companion auf
  demselben Triplett; r12-Flavour-Analyse gilt nur unter „Triplett = Generationen“; Vermerk in Abschnitt 3.
- v3.9 (2026-10-20): K26 Abgleich mit v4.9 (Phasenkammern unabhängig bestätigt; H2/H3 als „Koide mit Vorzeichen“
  neu eingeordnet; Farbe/Generation betrifft beide Linien).
- v4.0 (2026-10-20): K27 Companion-Runde v4.8.0-r13 (K23–K26 im Paper).
- v4.1 (2026-10-20): K28 Trennung von Farbe und Generation (Sedenionen: nur 2 farbige Generationen; Triality:
  3 × 3 unabhängig, empfohlen); Δ(96)-Mischungs-Lesart entfällt; Vermerk in Abschnitt 3.
- v4.2 (2026-10-20): K29 Companion-Runde v4.8.0-r14 (Trennung von Farbe und Generation im Paper).
- v4.3 (2026-10-20): K30 Hopf-Faserung als Träger der Triality-Plätze; symmetrischer Punkt ω ↔ Farbgruppe SU(3).
- v4.4 (2026-10-20): K31 Companion-Runde v4.8.0-r15.
- v4.5 (2026-10-20): K32 elfter vorab festgelegter Test (H11, Massen aus dem Tripel-Raum) — widerlegt; Mindestgrad 6.
- v4.6 (2026-10-20): K33 Companion-Runde v4.8.0-r16.
- v4.7 (2026-10-21): K34 Zeitrichtung der kosmologischen Anteile — thm:dark-energy mit prop:H0-tension und
  prop:saturation nicht vereinbar (Vorzeichen von dβ_sym/dt umgekehrt); DESI-Nähe zurückgenommen.
- v4.8 (2026-10-21): K35 Companion-Runde v4.8.0-r17.
- v4.9 (2026-10-21): K36 Drei-Frame-Typisierung (Kreuzterme, Befunde a–c, Symmetrie-Lesart); Eingrenzung von r17 auf
  prop:saturation (2), K34.5.
- v5.0 (2026-10-21): K37 Companion-Runde v4.8.0-r18.
- v5.1 (2026-10-21): K38 zwölfter vorab festgelegter Test (H12, Drei-Frame-Zuordnung) — nicht trennbar von H9, kein Test.
- v5.2 (2026-10-21): K39 Rückwärtsanalyse 3×3×3 mit Auslese-Index — einziger tragfähiger Ansatz ist ein Auslesefaktor
  f(+) ≈ 0,944, zahlenmäßig die bekannte Hopf-Lücke.
- v5.3 (2026-10-21): K40 Würfelfamilie mit Übergängen, Übergangsgruppen beider Lesarten, Z₂-Holonomie, alte Lesart
  als photonzentrierte Sicht.
- v5.4 (2026-10-21): K41 Companion-Runde v4.8.0-r19.
- v5.5 (2026-10-21): K42 dreizehnter vorab festgelegter Test (H13, Wigner-Holonomie) — widerlegt, z = −7,9.
- v5.6 (2026-10-21): K42.3 Nachbefund Halbwinkel (nicht registriert): Spinor-Herkunft, Triolen-Photon auf der Drehachse.
- v5.7 (2026-10-21): K43 Tachyon-Frame: gleiche Holonomie und Hauptspinoren wie Materie, Überlichtrapidität mit iπ/2,
  Kreuzterme imaginär, Tribonacci als cosh 2η = coth η.
- v5.8 (2026-10-21): K44 Companion-Runde v4.8.0-r20.
- v5.9 (2026-10-21): K45 Companion-Runde v4.9.0-r01 (neutrale Achse, Konstantenumrechnung, Tribonacci = Gleichheit
  von Lorentz- und Doppler-Faktor).
- v6.0 (2026-10-21): K46 Companion-Runde v4.9.0-r02 (Rundlauf um das Photon, Umkehrwalze = C, involutive
  Umkehrwalze antilinear E ↔ B).
- v6.1 (2026-10-21): K47 Companion-Runde v4.9.0-r03 (Kompensator als Interferometer, Dyon, Sichtbarkeit
  1/cosh 2η_f, Produktlesart).
- v6.2 (2026-10-21): K48 Companion-Runde v4.9.0-r04 (Kompensator als 2×2-Matrix auf (E, B), Zustandsscheibe).
- v6.3 (2026-10-21): K49 Companion-Runde v4.9.0-r05 (Portgewichtung, Umbenennung, Helizitätsachse/Kerr,
  Photon aus Materie + Tachyon).
- v6.4 (2026-10-21): K50 Companion-Runde v4.9.0-r06 (Trefferkette, Kegel 56,68°, Beschleunigung, Higgs als
  Portgewichtung).
- v6.5 (2026-10-21): K51 Vorab-Test H14 (Kegelwinkel = 2θ_W exakt widerlegt, als Näherung nicht entscheidbar).
- v6.6 (2026-10-21): K52 Companion-Runde v4.9.0-r07, Vorab-Notiz H15 (m_W = 80,3615 GeV vorhergesagt).
- v6.7 (2026-10-21): K53 Companion-Runde v4.9.0-r08 (Drift gegen Atomuhren, α-Vorzeichen, Compton-Uhr).
- v6.8 (2026-10-21): K54 Companion-Runde v4.9.0-r09 (lokaler Faktor: nur Potentiallesart, P5 = 1/2).
- v6.9 (2026-10-22): K55 Companion-Runde v4.9.0-r10 (C5-Faktor als Drehen/Kompensieren, Zeugenklasse Form (iii)).
- v7.0 (2026-10-22): K56 Companion-Runden v4.9.0-r11 (gekickte Dualitätsdynamik) und r12 (Δ_γ < 1/5 rekonstruiert).
- v7.1 (2026-10-22): K57 Companion-Runde v4.9.0-r13 (Zeitskala: τ_k = T_b/6).
- v7.2 (2026-10-22): K58 Companion-Runde v4.9.0-r14 (Kick-Richtungen Triole ∪ J_B(Triole)).
- v7.3 (2026-10-22): K59 Companion-Runde v4.9.0-r15 (Sammelregister, r17-Weg (b) ausgeschlossen).
- v7.4 (2026-10-22): K60 Companion-Runde v4.9.0-r16 (Autorentscheidungen).
- v7.5 (2026-10-22): K61 Companion-Runde v4.9.0-r17 (Entropie, Informationssingularität, Skalen-Dimension).
- v7.6 (2026-10-22): K62 Companion-Runde v4.9.0-r18 (Wege A und C zugleich: Klassentrennung Skala/Auslese).
- v7.7 (2026-10-22): K63 Companion-Runde v4.9.0-r19 (Klassentrennung angewandt: P5 = 1/2 automatisch, P3 verloren, P6 nur genähert).
- v7.8 (2026-10-22): K64 Companion-Runde v4.9.0-r20 (Herkunftshypothese Δ_γ < 1/5: Photon-Frame-Uhrgewinn am Hopf-Punkt).
- v7.9 (2026-10-22): K65 Companion-Runde v4.9.0-r21 (Uhrschranke je Frame, 1/5 aus Frame-Konsistenz hergeleitet).
- v8.0 (2026-10-22): K66 Companion-Runde v4.9.0-r22 (Frame-Regel als Konvention F, Pflichtabschnitt, Linter-Prüfung).
- v8.1 (2026-10-22): K67 Companion-Runde v4.9.0-r23 (Konvention F auf 113 Hauptkorpus-Aussagen angewandt).
- v8.2 (2026-10-22): K68 Companion-Runde v4.9.0-r24 (r23-Widersprüche als Ein-Frame-Artefakte korrigiert; F5–F7).
- v8.3 (2026-10-22): K69 Companion-Runde v4.9.0-r25 (Überarbeitung des Hauptkorpus: Archiv, Korrekturen, Statusvermerke).
- v8.4 (2026-10-22): K70 Vorab-Test H16 (Grad-6-Potentiale auf dem Tripel-Raum) widerlegt; Theoremlet r26.1 (bis Grad 6 nur Sattelpunkte); Companion-Runde v4.9.0-r26; K32.3 neu eingeordnet.

- v8.5 (2026-10-22): K71 Companion-Runde v4.9.0-r27 (Dynamik: Drehung plus Kompensator-Messung).

- v8.6 (2026-10-22): K72 Companion-Runde v4.9.0-r28 (Tachyon als Messgerät, Selbststabilisierung, Tachyon-Abbildung z → iz).

- v8.7 (2026-10-22): K73 Companion-Runde v4.9.0-r29 (Quelle des Tachyon-Reservoirs: Paarerzeugung aus dem Vakuum).

- v8.8 (2026-10-22): K74 Companion-Runde v4.9.0-r30 (Kompensator umgeht die klassische 1/2; Partner = Tachyon durch T; Austausch kohärent).

- v8.9 (2026-10-22): K75 Companion-Runde v4.9.0-r31 (Markov-Kaskade: geschlossen keine Stabilisierung, mit Rückweg stabile Flussanteile β²; Statusvermerk thm:dark-energy).
- v9.0 (2026-10-23): K76 Vorab-Test H17 (Realteil-Invarianten auf dem Tripel-Raum) widerlegt; Theoremlet r32.1 (auf der Achse linear in e₃, Sattelpunkte); Companion-Runde v4.9.0-r32.
- v9.1 (2026-10-23): K77 Prüfung Dixon-Ablage (Tripel = (Im ℍ)⊗𝕆, gemeinsame Symmetrie A₄, Lorentz-Konflikt) und Bestandsaufnahme gemischte Readouts (angelegt, nie ausgewertet).
- v9.2 (2026-10-23): K77.6 Frame-Einordnung der Dixon-Prüfung (Grammatik = Bezugsframe R; M/T offen bis J_B auf der Ablage festgelegt; Namensfalle gemischter Readout/Zustand; port-gewichtete Brechung frame-abhängig).
- v9.3 (2026-10-23): K77.7 Lean-Modul `formal/QSFormal/Dixon.lean` (Triality-Symmetrien, A₄-Charakterisierung, Dixon-Masken, Kerne von r26.1/r32.1).
- v9.4 (2026-10-23): K77.8 J_B = R ∘ T auf der Dixon-Ablage in Lean (σ_x der a-Hälften, Normen frame-frei, t ↦ −i t̄); K77.6 korrigiert (ℂ-Konjugation = T).
- v9.5 (2026-10-23): K77.9 Readout-abhängige Lesarten des ℂ-Faktors (Lean `Lesarten.lean`); Korrektur: nur D₄ erhält das a-Etikett; ℍ: A₄ = Konjugation mit 2T, Lage des Lorentz-Konflikts präzisiert.
- v9.6 (2026-10-23): K77.10 Links-invariante Etiketten: Im-Komponenten der quaternionischen Gram-Größe, μ_i = Fläche der anderen beiden Plätze, Rechts-2T zyklisch, umgekehrte Reihenfolge.
- v9.7 (2026-10-23): K78 Vorab-Test H18 (links-invariante Etiketten an den Minima) widerlegt; Companion-Runde v4.9.0-r33.
- v9.8 (2026-10-23): K79 Bestandsaufnahme Struktur gegen Standardmodell (A/B/C/D), thm:SM-Befund, Abzähl-Tests vorgeschlagen.
- v9.9 (2026-10-23): K80 Vorab-Test H19 (Ladungen aus der Dixon-Ablage) und Runde v4.9.0-r34: H19a/b/d/e bestätigt, H19c widerlegt.
- v10.0 (2026-10-23): K81 Vorab-Test H20 und Runde v4.9.0-r35: innere gegen äußere Einheit; H20a/c/d bestätigt, H20b widerlegt; Lesart K80.3 korrigiert.
- v10.1 (2026-10-23): K82 Frame-Regel für Einheiten übernommen, Statusvermerke thm:three-generations/thm:SM, Vorab-Test H21 und Runde v4.9.0-r36 (Herkunft der Doppelbelegung), alle bestätigt.
- v10.2 (2026-10-23): K83 Vorab-Test H22 und Runde v4.9.0-r37: Triality-Form = Spin(8)-Triality, Farbe in der Fixgruppe, Perioden {1,…,12}; H22d ohne Verbot.
- v10.3 (2026-10-23): K84 Vorab-Test H23 und Runde v4.9.0-r38: Frame-Triole M/P/T als Transposition der Triality-Plätze, alle bestätigt.
- v10.4 (2026-10-23): K85 Vorab-Test H24 und Runde v4.9.0-r39: Ketten unter Zoom und gemischten Readouts, alle bestätigt; Autorhinweis zur neuen Kontraktion.
- v10.5 (2026-10-23): K86 Vorab-Test H25 und Runde v4.9.0-r40: zweiseitige Kontraktion über Frames kovariant, nicht invariant; keine schwache SU(2) in der Triality.
- v10.6 (2026-10-23): K87 Vorab-Test H26 und Runde v4.9.0-r41: Aufteilung D der ℍ-Rollen, Q = T₃ + Y/2 mit Y/2 = Q − ½, T = C, Singuletts fehlen.
- v10.7 (2026-10-23): K88 Vorab-Test H27 und Runde v4.9.0-r42: MM-Kompensator als Chiralitätsprojektor, Inhalt einer Generation konstruiert.
- v10.8 (2026-10-23): K89 Vorab-Test H28 und Runde v4.9.0-r43: Chiralitätsprojektor und Versatz durch Anomaliefreiheit bis auf den Frame erzwungen.
- v10.9 (2026-10-23): K90 Vorab-Test H29 und Runde v4.9.0-r44: Massenterme als Frame-Kopplungen mit Higgs-Quantenzahlen, Brechungsstufen für Aufspaltung und Mischung.
- v11.0 (2026-10-23): K91 Vorab-Test H30 und Runde v4.9.0-r45: Chiralität bricht ρ zwingend; triality-kovariante Chiralität existiert nicht; K83 umgestuft.
- v11.1 (2026-10-23): K92 Vorab-Test H31 und Runde v4.9.0-r46: Verschiebungs-Readouts erzeugen keine Mischung, Art-Masken schon.
- v11.2 (2026-10-23): K93 Vorab-Test H32 und Runde v4.9.0-r47: Maske fester Form aus der Abweichung der triality-kovarianten Chiralität; H32c (Linearität) widerlegt.
- v11.3 (2026-10-23): Lean-Modul `formal/QSFormal/Ladungen.lean` (nur Lean-Kern): σ einziger Automorphismus unter 48 Fortsetzungen (r36), c L_{e₇} c = −R_{e₇} für alle x (r45), 6Q, Inhalt einer Generation, Anomalie-Spuren und Tr Y = 0 ⇔ s = −½ (r42, r43), Masken-Gewichte und Eisenstein-Normen (r47), 2^j mod 3 (r39); geprüft mit Lean 4.35.0, nur Standard-Axiome.
- v11.4 (2026-10-24): K94 Companion-Runde v4.9.0-r48 und Lean-Modul `formal/QSFormal/Sektoren.lean`: Ladungs-Sektoren, Farbdimensionen 1, 3, 3, 1, Ladungen und Masken-Gewichte aus O.mul hergeleitet; T als Ladungskonjugation; σ bleibt im Sektor.
- v11.5 (2026-10-24): K95 Vorab-Test H33 und Runde v4.9.0-r49 (e₇ trägt B − L, Photon braucht ℍ; Q_em = T₃^L + T₃^R + (B − L)/2), K96 Vorab-Test H34 und Runde v4.9.0-r50 (Maske aus r47 erklärt CKM und PMNS nicht; ε durch die Hierarchie begrenzt); K93.3 umgestuft.
- v11.6 (2026-10-24): K97 Vorab-Test H35 und Runde v4.9.0-r51 (Tachyon-Abbildung lässt die Sektoren fest; e₇ Frame-Achse nur teilweise; „T“ in r41–r49 = Zeitumkehr, korrigiert), K98 Vorab-Test H36 und Runde v4.9.0-r52 (Kongruenz- und Ähnlichkeitsform der Maske widerlegt, nächster Fall 36 %).
- v11.7 (2026-10-24): K99 Vorab-Test H37 und Runde v4.9.0-r53 (reine Triality-Kopplung verboten: m₃ = m₁ + m₂, für ν Σm = 0.115 eV ausgeschlossen; Norm + Triality und H/H̃-Lesart erklären die Mischung nicht).
- v11.8 (2026-10-24): K100 Vorab-Test H38 und Runde v4.9.0-r54 (ein ε je Sektor: Form S trifft CKM und PMNS, aber im Ausläufer; Form K verfehlt die Quarks knapp); Zählung in K98.2 korrigiert.
- v11.9 (2026-10-24): K101 Vorab-Test H39 und Runde v4.9.0-r55 (Lesart je Teilchenart: Dirac ℤ₃, Majorana ℤ₂ aus A₄ ⇒ CKM = 1 in führender Ordnung, PMNS = TM2; sin²θ₁₂ ≈ 0.341, 3.6 σ über JUNO).
- v12.0 (2026-10-24): K102 Vorab-Test H40 und Runde v4.9.0-r56 (Kalibrierung der Ausleseschicht: Einstellungen festgehalten, keine Struktur über Zufall, p = 0.019; Kompression fehlt).
- v12.1 (2026-10-24): K103 Vorab-Test H41 und Runde v4.9.0-r57 (Maske als Korrektur löst die TM2-Spannung mit JUNO; θ₂₃ nicht festgelegt, nachträglich sin²θ₂₃ ≲ 0.54).
- v12.2 (2026-10-24): K104 Vorhersage H42 (sin²θ₂₃ ≤ 0.54) vorab festgelegt, ausstehend.
- v12.3 (2026-10-24): K105 Vorab-Test H43 und Runde v4.9.0-r58 (CP-Phase δ durch die korrigierte TM2-Lesart nicht festgelegt; keine H44).

---

## 9. Bewusst nicht enthalten

- **Torus:** Im Corpus nicht ausgeschrieben; nach Auskunft des Autors bewusst weggelassen, weil er aus der
  Hopf-Faserung selbst entsteht. Inzwischen in K3.6 als Hopf-Urbild ergänzt.
- Solve-Log r03–r94 und v4.8.0-r01–r03 (Guard-Ledger-Details), C4/C5-Kollar-Rekursion, OP-Routen.
