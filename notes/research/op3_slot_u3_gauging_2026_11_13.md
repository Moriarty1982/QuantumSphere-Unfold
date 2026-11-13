# Erkundung: Eichung der U(3) auf dem Platzindex

13. November 2026, spät. Autorenauftrag: „Platzindex-U(3) eichen“.
Erkundung, analytisch mit numerischer Selbstprüfung, nicht blind. Kein Test,
keine H-Nummer, kein MMA-Beleg, keine Änderung offener Guards. Einordnung
T5/T7 (Träger), T8 (Massen), OP3. Skript `op3_slot_u3_gauging_2026_11_13.py`,
Ausgabe `..._out.txt`.

## Vorwissen geprüft

- `op3_gram_eigen_readout_2026_11_13.md`: Gram-Matrix S, Eigenwerte
  eichinvariant, Auslesung √m ∝ s ist Annahme.
- `op3_neutrino_phase_candidates_2026_11_13.md`, Nachträge Koide-Spannung,
  c und Familiensymmetrie: keine native Familien-Eichsymmetrie; Platzindex-U(3)
  als einziger stetiger Kandidat; Sumino (arXiv:0812.2103): ℓ_L in 3, e_R in 3̄,
  Familienbosonen M_ij² ∝ m_i + m_j, Aufhebung bei α_F = 4α.
- r13–r16 (diskrete S_3, Trialitätsplätze), r12.2 (Δ(96) in der Farbe),
  `op3_dixon_slot_coupling_2026_11_13.md` (Konjugation am ersten Eintrag),
  `op3_indefinite_form_2026_11_13.md` (bilineare Form im neutralen Sektor).

## Ansatz

Die drei Plätze bilden ein Feld X = [x_1 x_2 x_3] mit Werten in einem
Zustandsraum V; S = X†X. Die Platzindex-U(3) wirkt als X → XU. Geeicht wird
sie mit einem u(3)-Zusammenhang A und D X = ∂X − i g_F X A. Der kinetische
Term tr (DX)†(DX) enthält g_F² tr(A S A); daraus kommen die Massen der neun
Familienbosonen, sobald X einen Erwartungswert hat.

Das ist ein neues Strukturelement: Der Companion hat kein Feld und keinen
Zusammenhang auf dem Platzindex. Geprüft wird nur, ob ein solcher Ansatz zu
Suminos Mechanismus passt.

## Ergebnis

1. **Invarianz.** Die Gram-Eigenwerte sind invariant unter X → XU und unter
   unitären Wirkungen auf V (numerisch 10⁻¹⁴). Die Massenauslesung bleibt
   eichinvariant.
2. **Bosonenmassen.** In der Eigenbasis von S = diag(s_1, s_2, s_3) gilt
   (g_F = 1): drei Bosonen mit M² = s_i und je zwei mit M² = (s_i + s_j)/2
   (numerisch 10⁻¹⁴). Alle neun sind massiv, auch die diagonalen. Das ist
   genau die Struktur, die Sumino braucht: Die diagonalen Bosonen setzen die
   Schwellen ln M_ii², aus denen die generationsabhängige Korrektur kommt.
3. **Gegenprobe.** Trüge S selbst die Ladung (adjungiert, S → U†SU), blieben
   drei Bosonen masselos; dann fehlten die diagonalen Schwellen. Das
   geladene Feld muss X sein, nicht S.
4. **Auslesung entscheidet über die Kopplungsbedingung.**

   | Auslesung | Bosonen | ln M_ii² | Aufhebung bei |
   |---|---|---|---|
   | A: √m ∝ s (Gram, wie H99) | M_ii² ∝ √m_i | ½ ln m_i | α_F = 8α |
   | B: m ∝ s (√m ∝ Singulärwerte von X) | M_ii² ∝ m_i | ln m_i | α_F = 4α (wie Sumino) |

   Annahme: Suminos Form der Korrektur (Koeffizient mal ln M_ii²) überträgt
   sich. In Auslesung B ist X genau Suminos Φ.
5. **Ladungen der Fermionen.** Mit Suminos Zuordnung (ℓ_L in 3, e_R in 3̄)
   ist ein invarianter Massenterm ψ̄_L M e_R nur mit M → U M Uᵀ möglich. Aus X
   gebaut ist das die **bilineare** Matrix Xᵀ X (bei passender Konvention der
   Wirkung), nicht die hermitesche X†X. Für reelles X (bis auf eine gemeinsame
   Phase) fallen beide zusammen. Der Neutrino-Term ℓ_L ℓ_L braucht entsprechend
   (Xᵀ X)*. Die bilineare Form ist im Companion nativ (indefinite Form,
   neutraler Sektor); ob X in einem neutralen Raum liegt, ist offen.
6. **Neutrinos.** Der Exponent c bleibt 1, unabhängig von α_F: Er misst das
   Verhältnis der Familienkorrektur auf der Neutrinoseite zur QED-Korrektur
   der geladenen Leptonen, und diese ist durch die Aufhebungsbedingung
   festgelegt.

## Bewertung

- Die Eichung ist widerspruchsfrei anzusetzen und liefert die richtige
  Bosonenstruktur: alle neun Familienbosonen massiv, Massen aus den
  Platzüberlappungen, diagonale Schwellen pro Generation.
- Sie erzwingt eine Wahl:
  - Auslesung A behält die Gram-Lesart von Koide (ρ² = 1/2, Bogen, π/12) und
    verlangt α_F = 8α.
  - Auslesung B ist Suminos Modell (α_F = 4α), verliert aber die
    Überlappungs-Lesart: Koide spricht dann über die Singulärwerte von X,
    nicht über die Eigenwerte von S, und H99 müsste neu formuliert werden.
- Nicht hergeleitet: das Feld X selbst, sein Potential (warum ρ² = 1/2), die
  Kopplung α_F (4α oder 8α) und deren Vereinigung mit SU(2)_L. Die bilineare
  Massenmatrix in Punkt 5 ist eine Folgerung aus Suminos Ladungen, keine
  Eigenschaft des Companion.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.

## Nächste Fragen

- Welche Auslesung (A oder B) ist im Companion begründbar? A ist die bisher
  verwendete; B wäre die direkte Übernahme von Sumino.
- Gibt es ein natives Potential für X, das ρ² = 1/2 (A) oder die Koide-
  Bedingung der Singulärwerte (B) auswählt? Bei Sumino leistet das ein
  eigenes Potential mit zusätzlichen Feldern.
- Wie hängt die Platzindex-U(3) mit SU(2)_L im Quaternionenfaktor zusammen
  (Vereinigung, die α_F festlegt)?

## Nachtrag: Auslesung A oder B (13.11., Autor)

Vorwissen: r16 (H11) legt √m_k ∝ |Platz k| fest, also √m linear in der
Amplitude (B-artig, Diagonal-Labels); die Gram-Notiz und H99 benutzen
√m ∝ Eigenwerte von S (A). H2 (r12): Neutrinos erreichen K = 2/3 nur mit
einer negativen Wurzel; mit nur positiven Wurzeln höchstens K = 0,585.

**Kriterien**

| Kriterium | A: √m ∝ s | B: m ∝ s |
|---|---|---|
| Bogen \|θ\| ≤ π/12 | ja | ja (der Bogen ist nur „alle Wurzeln ≥ 0“, numerisch geprüft) |
| Koide als Überlappung ρ² = 1/2 | ja | nein |
| negative Wurzel (Neutrinos, H2) | ja, über die indefinite Form (Eigenwert < 0) | nein: Singulärwerte sind nie negativ; dann K_ν ≤ 0,585, Koide für Neutrinos ausgeschlossen |
| √m linear im Feld (wie bei Koide- und Sumino-Modellen, r16) | nein, wenn X das Feld ist | ja |
| Sumino-Bedingung α_F = 4α | nur mit passendem Feld (siehe unten) | ja, mit X |

**Feldtyp und Kopplungsbedingung** (Skript, Abschnitt „Auslesung A oder B“):

| Feld, das die Familienbosonen massiv macht | masselose Bosonen | A | B |
|---|---|---|---|
| X fundamental (X → XU) | 0 | α_F = 8α | α_F = 4α |
| S adjungiert (S → U†SU) | 3 | – | – |
| Φ mit Singulärwerten s, Φ → UΦ | 0 | **α_F = 4α** | α_F = 2α |
| Massenmatrix M = S, M → U M Uᵀ (Suminos Ladungen) | 0 | **α_F = 4α** | α_F = 2α |

Die Sumino-Bedingung hängt also nicht an der Auslesung allein, sondern am
Paar (Auslesung, Feld): Entscheidend ist, dass die diagonalen
Bosonenschwellen M_ii² proportional zu m_i sind. In A gilt das, wenn das
Feld die Überlappungen s selbst als Singulärwerte trägt, also S als Feld
mit einer Wirkung von einer Seite oder als symmetrische Massenmatrix.

**Entscheidung: A.**
- Nur A trägt die Neutrinoseite. B schließt negative Wurzeln aus, und
  nach H2 ist Koide für die gemessenen Neutrinos dann nicht erreichbar;
  H99, die Fassung bei einer Skala und der Sumino-Weg für Neutrinos
  fielen weg.
- Nur A gibt Koide eine geometrische Bedeutung (mittlere quadratische
  Überlappung 1/2) und verbindet die indefinite Form mit der Signatur.
- Der Preis: Das Feld, das die Familienbosonen massiv macht, ist dann
  nicht X, sondern ein Objekt mit Singulärwerten s, am natürlichsten die
  Überlappungsmatrix selbst in der Darstellung, die Suminos Ladungen
  verlangen (M → U M Uᵀ). Dann gilt α_F = 4α wie bei Sumino. Mit X als
  Feld wäre α_F = 8α.
- Offen: Warum ist die Überlappungsmatrix selbst ein Feld (und nicht nur
  aus X gebildet)? Bei Gram-Bildung aus einem Tripel transformiert sie
  adjungiert (masselose Bosonen); als M → U M Uᵀ braucht sie Überlappungen
  zwischen zwei verschieden geladenen Tripeln (etwa links und rechts,
  passend zu ℓ_L in 3, e_R in 3̄). Das ist nicht nativ.
- B bleibt als direkte Sumino-Übernahme widerspruchsfrei, aber nur für
  geladene Leptonen.

## Nachtrag: zwei Tripel L/R und das Zwei-Sonden-System (13.11., Autor: „die zwei Tripel gibt es als Idee schon, die Sonden machen am Ende nichts anderes“)

Vorwissen geprüft: prop:triadic-two-probe (v470/10, Abschnitt Sondensektor;
Statusbemerkung: Feldarchitektur, keine Herleitung), lem:two-probe-compatibility
(r20-Arbeitsquelle: zwei Sonden „aufeinander gerichtet“, aus demselben
normierten Körper), generation-coupling.tex (Generationsplätze als
Sondenplätze, geschlossene Seeds S = P T G^(−1/2), Gram-Matrix als
Massenauslesung), op3_inner_operator_terms_2026_11_11.md.

**1. Überlappungen zweier Tripel** (Skript, Abschnitt „Zwei Tripel“). L-Tripel
X → XU (3, wie ℓ_L), R-Tripel Y → YU* (3̄, wie e_R). Als eigenes Feld gelesen:

| Überlappung | masselose Familienbosonen |
|---|---|
| X†X, Y†Y (L mit L, R mit R, hermitesch) | 3 (adjungiert) |
| Xᵀ X (L mit L, bilinear) | 0 |
| X† Y (L mit R, hermitesch) | **0** |
| Xᵀ Y (L mit R, bilinear) | 1 |
| X† X* (R = konjugiertes L) = (Xᵀ X)* | **0** |

Die gemischte hermitesche Überlappung von L und R hat genau Suminos
Darstellung (C → U† C U*, Konjugierte von M → U M Uᵀ). Ist das R-Tripel das
konjugierte L-Tripel, wird sie zur konjugierten bilinearen Gram-Matrix; für
reelle Plätze ist sie die gewöhnliche Gram-Matrix S.

**2. Das Zwei-Sonden-System trägt genau das.** In prop:triadic-two-probe ist

    Ω_△ = [[Ω_1, g_Y T_12, 0], [g_Y T_21, Ω_2, 0], [0, 0, Ω_⊥]] + χ (Kopplung an Ψ_⊥).

Zuordnung (Lesart, nicht im Text festgelegt):
- Ψ_1 ↔ L-Tripel, Ψ_2 ↔ R-Tripel; nach lem:two-probe-compatibility stammen
  beide aus demselben normierten Körper und sind aufeinander gerichtet,
  passend zu „R = konjugiertes L“.
- g_Y T_12 ↔ die Überlappung C, also der Massenblock (g_Y ist die
  Yokamono-Kopplung, im Text als Yukawa-artig geführt).
- Ψ_⊥ mit χ ↔ der dritte Platz h der Dixon-Platzkopplung F_b(x, y, h).

Numerisch (reelle Einheitsvektoren, Ω_1 = Ω_2 = 0): Der Block
[[0, C], [C†, 0]] hat die Eigenwerte ± s_k mit s_k den Eigenwerten der
Gram-Matrix S. Die Zwei-Sonden-Masse ist also genau die Auslesung A, als
Dirac-Paar ±s.

**3. T_12 als Feld gibt Suminos Bedingung.** Trägt T_12 einen Vakuumwert mit
Singulärwerten s ∝ √m (Auslesung A) und transformiert als U† T_12 U*, sind
alle neun Familienbosonen massiv, und die diagonalen Schwellen erfüllen
ln M_ii² = 1,00 · ln m_i + const, also **α_F = 4α** wie bei Sumino.

**Bewertung.**
- Der Hinweis des Autors trägt: Das Zwei-Sonden-System liefert die beiden
  Tripel, ihre Kopplung als Massenblock und einen dritten Kanal. Mit
  T_12 als Kopplungsfeld passt Auslesung A zu Suminos α_F = 4α; der Preis
  aus dem vorigen Nachtrag („nicht nativ“) entfällt damit in der Struktur.
- Die Dirac-Form ±s erklärt nebenbei, warum geladene Leptonen positive
  Wurzeln haben (Singulärwerte) und innerhalb des Bogens liegen.
- Weiter offen: Im Text ist T_12 ein fester Operator, kein Feld mit
  eigener Dynamik; die Transformation der Sonden unter einer Familien-U(3)
  und deren Eichung sind nicht angelegt. Der Neutrino-Fall braucht den
  symmetrischen L-L-Block (Majorana) mit indefiniter Form; das
  Zwei-Sonden-System hat dafür keinen eigenen Block. Ω_1, Ω_2 und χ sind
  unbestimmt. prop:triadic-two-probe hat den Status einer
  Feldarchitektur, keiner Herleitung.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.

## Nachtrag: Neutrino-Block L-L (13.11., Autor)

Vorwissen geprüft: r44.1(d) (der einzige eichinvariante Verbinder ohne
Higgs ist ein Majorana-Term für ν^c), r55 (Dirac-Kopplungen zirkulant,
Z_3; Majorana mit eigener Untergruppe, Z_2 gibt TM2), H2 (negative Wurzel),
`op3_indefinite_form_2026_11_13.md` (bilineare Form nur im neutralen Sektor
ungleich null; Signatur (2,1) außerhalb des Bogens).

**Platz im Zwei-Sonden-System.** Die Diagonalblöcke Ω_1 (L mit L) und Ω_2
(R mit R) sind die Majorana-Blöcke; sie gibt es nur im neutralen Sektor,
weil die bilineare Form auf geladenen Zuständen verschwindet. Ω_2 ist
nativ (r44.1(d), ν^c ohne Higgs); Ω_1 braucht zwei Higgs-Einsetzungen
(Weinberg) oder entsteht über Ω_2 als Seesaw. Der neutrale Block ist dann
[[Ω_1, g T_12], [g T_21, Ω_2]]. Das Feld X der Plätze muss neutral sein
(sonst verschwände die bilineare Überlappung); die Leptonen sind die
Sondenfelder Ψ_1, Ψ_2.

**Rechnungen** (Skript, Abschnitt „Neutrino-Block L-L“):

| Prüfung | Ergebnis |
|---|---|
| (a) Ω_1 ∝ Xᵀ η X, transformiert U ᵀ N U | als Feld alle Familienbosonen massiv; Korrektur mit demselben Vorzeichen wie bei geladenen Leptonen, also c = 1 |
| (b) Vorzeichen bei η mit Signatur (2,1) | drei raumartige η-Einheitsvektoren geben in 716 von 716 Fällen genau einen negativen Eigenwert: die negative Wurzel von H2 ist dort zwingend |
| (c) Seesaw mit Ω_2 ∝ 1 und Dirac-Block mit geladener Struktur | R = 0,00354, −58σ: ausgeschlossen (leichte Massen ∝ m_e, m_μ, m_τ) |
| (d) Neutrino-Tripel als Tensorprodukt aus geladenem und Rand-Tripel | ρ_ν² = 1/4, K_ν = 1/2: kein Koide |

**Die eigentliche Bedingung.** ν_L und e_L sitzen im selben Dublett, also
im selben linken Tripel X. Dann ist der geladene Block T_12 ∝ (Xᵀ X)*
(R-Tripel = konjugiertes L-Tripel) und der Neutrino-Block Ω_1 ∝ Xᵀ η X.
Mit η = 1 hätten beide dasselbe Spektrum, was die Daten ausschließen.
Der ganze Unterschied zwischen den Sektoren muss also in η liegen, der
Form im neutralen Sektor. H99 (und die Fassung bei einer Skala) verlangen
von η genau zwei Dinge:
1. dieselbe mittlere quadratische Überlappung ρ² (Koide in beiden Sektoren),
2. eine Phasenverschiebung um den Bogenrand θ_b (π/12 bei ρ² = 1/2), also
   aus der Signatur (3,0) in die Signatur (2,1).

Teil 2 passt qualitativ: Ein indefinites η erzwingt die negative Wurzel,
also eine Phase außerhalb des Bogens. Dass die Verschiebung genau θ_b
beträgt und ρ² erhalten bleibt, folgt aus keinem der geprüften Ansätze.
r55 passt dazu, dass η die zyklische Z_3 der Dirac-Kopplungen teilweise
bricht (Majorana-Auslesung mit Z_2).

**Bewertung.** Der L-L-Block hat im Zwei-Sonden-System einen natürlichen
Platz (Ω_1, neutraler Sektor), die richtige Familiendarstellung (c = 1)
und mit indefiniter Form zwingend eine negative Wurzel. Die einfachen
Wege, ihn aus dem geladenen Block zu gewinnen (Seesaw mit gleicher
Struktur, Tensorprodukt), scheiden aus. Offen ist eine native Form η im
neutralen Sektor, die ρ² erhält und die Phase um θ_b verschiebt; das ist
die präzise Fassung der Frage nach dem Ursprung von H99.
OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert.
