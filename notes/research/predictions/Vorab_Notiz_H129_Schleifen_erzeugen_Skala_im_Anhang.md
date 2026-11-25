# Vorab-Notiz H129: Erzeugt der skalenfreie Ansatz bei einer Schleife von selbst eine Skala im Anhang, mit festem Vorzeichen?

**Stand:** 2026-11-25, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 25.11.2026: „ich vermute mal, dass vorzeichen werden wir erst aus unserer finalen feldgleichung herleiten können“, und nach k295
(„erzeugen Schleifen μ² selbst und mit welchem Vorzeichen?“) am 25.11.2026, 10:46 UTC: „versuche es“. Skripte **k296** (Python sympy/scipy) und
**k296b** (Wolfram Language, unabhängige Gegenprobe der β-Funktionen und der Klassifikation). Qiskit nicht vorgesehen (keine Schaltung, keine Messung).
Kein HDL/MMA-Vergleich (kein RUN_TAPE-Bezug). Bezug OP3/OP4 nur mittelbar, kein Guard wird berührt.

## Vorwissen geprüft
- **k290** (#296): Rekursion L_{n+1} = L_n + Δ_n, Zusatzterme K₁ (Fläche) und K₂ (Kommutator), Variante aus D_μψ oder aus Strömen.
- **k291, k292** (#296): keine Masse auf HS(0), HS(1); HC legt die Form fest, nicht die Amplitude.
- **k293, k294** (#298): Zusatzterme bevorzugen den Anhang klassisch nicht; Schwelle mit gesetztem Potential.
- **k295** (#302): zulässige Terme im Anhang B, A·B, B²; einzige Skala μ² (Koeffizient von B), Vorzeichen frei.
- **k282** und Bilanz (#295): σ-Term, Vorzeichen offen.
- Suche im Repo nach „Coleman“, „Einschleif“, „Renormierungsgruppe“, „Gildener“ (25.11.): nur die eigenen Notizen k290, k295 und ein OP5-Text ohne Bezug.
  Es gibt keine Schleifenrechnung zum Turm im Repo.
- Literatur aus Vorwissen (ungeprüft, nicht nachgeschlagen): Coleman–Weinberg und Gildener–Weinberg (Skala aus Schleifen in skalenfreien Theorien).

## Aufbau
- Felder: ψ = ψ₁ + χ·j, vier reelle Komponenten x₀ … x₃, A = x₀² + x₁², B = x₂² + x₃².
- Skalenfreier Ansatz: V = λ_A·A² + κ·A·B + λ_B·B², **μ² = 0** (auch im Anhang), kinetisch ½(∂ψ)². Ohne Eichfelder.
- **Stufe A:** Einschleifen-β-Funktionen aus 16π²·dV/d ln μ = ½·Tr[(∂²V)²] (vierter Ordnung), symbolisch.
- **Stufe B:** Fluss ins Infrarote, τ = ln(μ₀/μ)/(16π²) von 0 bis 10⁴, auf dem festen Gitter λ_A, λ_B ∈ {0,05; 0,10; …; 0,50},
  κ ∈ {−0,95; −0,90; …; 1,50} ohne κ = 0 und ohne Punkte, die am Start κ > −2√(λ_Aλ_B) verletzen. Klassen nach dem ersten Ereignis:
  (i) keines (keine Skala), (ii) λ_B = 0 zuerst (flache Richtung im Anhang), (iii) λ_A = 0 zuerst (flache Richtung in der Vorstufe),
  (iv) κ = −2√(λ_Aλ_B) zuerst (flache Richtung mit beiden Anteilen). Wo eine flache Richtung erreicht wird, erzeugt die Schleife dort nach
  Gildener–Weinberg die Skala, wenn die Summe der vierten Potenzen der Massen positiv ist (wird je Klasse geprüft).
- **Stufe C:** Einfluss der Zusatzterme auf die Richtung: Einschleifen-Korrektur der kinetischen Normierung Z je Komponente aus c₁K₁ und c₂K₂
  (Variante D_μψ, c₁, c₂ > 0, euklidisch, Impuls-Abschneidung, ⟨∂_μx_a ∂_νx_b⟩ = δ_ab δ_μν J mit J > 0).

## Hypothese H129
Der skalenfreie Ansatz erzeugt bei einer Schleife von selbst eine Skala, und zwar im Anhang (χ bekommt die feste Amplitude), ohne dass ein Vorzeichen gesetzt wird.

## Entscheidungskriterien
- **K-a (Skala):** Anteil der Gitterpunkte, die nicht in Klasse (i) fallen. Bestätigt ab 95 %, widerlegt bis 50 %, dazwischen „trägt teilweise“.
- **K-b (Richtung aus dem Potential):** Anteil (ii) unter den Punkten mit Skala. Bestätigt ab 95 %, widerlegt bis 50 %.
- **K-c (Richtung aus den Zusatztermen):** Bestätigt, wenn δZ die beiden Komponenten des Anhangs gegenüber **beiden** Komponenten der Vorstufe
  auszeichnet (δZ(x₂) = δZ(x₃) ≠ δZ(x₀) und ≠ δZ(x₁)). Widerlegt, wenn mindestens eine Komponente der Vorstufe dieselbe Korrektur hat wie der Anhang
  oder wenn alle gleich sind.
- **Gesamturteil:** H129 bestätigt nur, wenn K-a bestätigt ist und K-b oder K-c bestätigt ist. Sonst widerlegt oder „trägt teilweise“ (Skala ja, Richtung nein).

## Vorab offengelegt (kein Teil der Vorhersage)
- **Tauschsymmetrie:** V und der kinetische Term sind unter ψ₁ ↔ χ (Rechtsmultiplikation mit j) zusammen mit λ_A ↔ λ_B invariant. Auf dem symmetrischen Gitter
  sind die Klassen (ii) und (iii) daher gleich groß. K-b kann also höchstens 50 % plus die Hälfte der Gleichstände erreichen und steht als **widerlegt** fest.
  K-b wird nur zur Vollständigkeit ausgezählt.
- **Dimensionale Regularisierung:** Im masselosen Fall sind die Beiträge zu Stufe C skalenlose Integrale und null. Ein Ergebnis von Stufe C gilt daher
  nur für die Abschneidung und wird als regulatorabhängig geführt.
- **Überschlag vor der Rechnung (im Kopf, mit β-Koeffizienten aus dem Gedächtnis):** Für λ_A = λ_B = λ erwarte ich r = κ/λ mit dr/dτ = λ·r·(r − 2)²,
  also: 0 < κ ≤ 2λ fließt zum O(4)-symmetrischen Punkt κ = 2λ ohne Skala, κ > 2λ erreicht λ = 0, κ < 0 erreicht die Stabilitätsgrenze.
  Für K₂ erwarte ich δZ > 0 für alle drei imaginären Komponenten x₁, x₂, x₃ (K₂ sieht nur Imaginärteile), für K₁ dieselbe Korrektur für alle vier.

## Vorhersage
- K-a: **trägt teilweise** (ein Fenster 0 < κ ≲ 2√(λ_Aλ_B) ohne Skala; Anteil auf dem Gitter unbekannt, das entscheidet die Rechnung).
- K-b: widerlegt (offengelegt). K-c: **widerlegt** (x₁ aus der Vorstufe hat dieselbe Korrektur wie der Anhang).
- Gesamt: **H129 trägt teilweise oder ist widerlegt**: Schleifen können die Skala erzeugen, legen aber nicht fest, dass sie im Anhang entsteht.
- Offen vor der Rechnung: die genauen β-Koeffizienten, die Gitteranteile, Vorzeichen und Größe von δZ, und ob die Gildener–Weinberg-Bedingung in allen Klassen erfüllt ist.

## Grenzen (vorab)
Eine Schleife, ohne Eichfelder, nur der Schritt ℂ → ℍ, nur die Links- und Rechtsdrehung um i als Symmetrie (ohne die zwei Zusatzterme aus k295, die nur
linksinvariant sind). Das Gitter ist eine Wahl; die Anteile sind keine Wahrscheinlichkeiten. τ bis 10⁴ ist formal (keine physikalische Skala).
