# Kernkarte Quantum Sphaera — v2.6

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
Λ_bare ∼ γ₁².

**Vermutung (V), präzisiert:** Materie/Tachyon/Photon als ein Objekt in Dualitätsrahmen (r07);
Raumzeit als Projektion einer Spinor-/Informationsebene (K2); Einstein-Lesart der Spurformel (r05).

**Offen (P):** OP1, OP2, Rolle von t, Transport K̂(L_n) = L_{n−1}, Kopplungen der Master-Gleichung,
definierte Wirkung, Λ-Typ, physikalischer Status des Dualitätswinkels, **ein dynamisches Prinzip für
Lesart B**, das |c|/t und die Koide-Phase festlegt (r10).

**Strukturbefund (M, r10):** Die Koide-Form der Leptonmassen ist exakt Skalar + symmetrische Triole;
K = 2/3 ⇔ |c| = t.

**Vorab-Tests:** H1 δ = K/3 (r11) — widerlegt für Quarks und laufende Leptonmassen. H2 Neutrinos mit r = 1
(K14) — verträglich, Vorhersage normale Ordnung, Σm_ν = 0,0592 eV (schwach trennend). H3 Vorzeichen als
Majorana-Parität (K15) — verträglich, m_ββ ≤ 3,5 meV, nicht prüfbar. Regel: Jede neue
Vorhersage zuerst als Vorab-Notiz committen, dann rechnen.

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

---

## 9. Bewusst nicht enthalten

- **Torus:** Im Corpus nicht ausgeschrieben; nach Auskunft des Autors bewusst weggelassen, weil er aus der
  Hopf-Faserung selbst entsteht. Inzwischen in K3.6 als Hopf-Urbild ergänzt.
- Solve-Log r03–r94 und v4.8.0-r01–r03 (Guard-Ledger-Details), C4/C5-Kollar-Rekursion, OP-Routen.
