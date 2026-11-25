# Vorab-Notiz H150: Folgt das Vorzeichen von 2a − b aus der Feldgleichung?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „ja“ auf den Vorschlag nach H149, das Vorzeichen von 2a − b aus der Feldgleichung zu bestimmen.
Marcs Regel: Das Vorzeichen soll aus der Feldgleichung folgen und nicht gesetzt werden; wenn nicht, ehrlich sagen, woran es hängt. Seine Richtungsentscheidung
„skalenfrei oder Skala als Setzung“ ist offen, deshalb werden beide Fälle gerechnet. Vergeben: H150, Skripte k333 (Python: sympy, scipy) und k333b (Wolfram,
unabhängige Gegenprobe). Qiskit nicht vorgesehen (keine Schaltung). Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf).

## Vorwissen geprüft
- H149 (k332): ∂_θV|π/4 = −(2a − 2c + μ₀² − μ₁²)/2; mit Tausch Krümmung 2(2a − b) bei π/4, −2(2a − b) bei 0; V = konst. + (2a − b)/8·cos 4θ (μ = 0).
- k290 (U(1) geeicht ⇒ V = V(N)), k291 (μ₀ = μ₁ = 0), k295 (zulässige Terme A², A·B, B² mit A = Norm der Vorstufe, B = Norm des Anhangs; μ²-Vorzeichen frei),
  k297 (HC als Potential η(B − μ²A)², κ = −2ημ² < 0, flache Richtung B = μ²A; Tausch = μ → 1/μ).
- H129 (k296): β-Funktionen für V = λ_A A² + κAB + λ_B B² bei ℂ → ℍ (je zwei Komponenten), 16π²·dr/dt = −4λr(r − 2)² mit r = κ/λ; Klassen (i) keine Skala,
  (ii)/(iii) flache Richtung in einem Teil, (iv) κ < 0, flache Richtung mit beiden Teilen, A/B = √(λ_B/λ_A); Gildener–Weinberg erfüllt. Mit Abschneidung
  δμ² ∝ (4λ + κ)Λ²/16π².
- H133/k302–k305 (κ ≈ 1,2): das ist die Kopplung κ·A·C an die Higgs-Richtung bei HS(3), eine andere Größe; wird hier nicht übertragen.
- H132, H136 (geeichte SU(2): keine Invariante hängt am Winkel).
- Zurückgestellte Ideen: I4 (Tachyon-Moden über die Schwelle, Kondensation als Massenquelle) wird berührt, falls der Koide-Punkt nur über eine Kondensation
  mit κ < 0 erreicht wird; dann wird I4 dem Autor als möglicher Ausweg genannt.

## Zuordnung (vor der Rechnung festgelegt)
Mit φ = ReΨ (Vorstufe, HS(0)) und χ = |ImΨ| (Kopienrichtung, Anhang) ist A = φ², B = χ², also a = λ_A, b = κ, c = λ_B. Auf dem Tausch (λ_A = λ_B = λ) ist
2a − b = λ(2 − r). Auf der Kugel N = A + B = 1 ist A = cos²θ, B = sin²θ; an einer flachen Richtung der Klasse (iv) gilt tan²θ = √(λ_A/λ_B) und K = (1 + tan²θ)/3.

## Hypothesen und Kriterien
- **H150a (nicht blind, analytisch):** Bei geeichter U(1) bzw. dem Potential der vollen Norm ist r = 2, also 2a − b = 0 exakt, und das bleibt unter der Symmetrie in
  jeder Ordnung so; θ ist flach. *Kriterium:* symbolisch. Bestätigt, wenn 2a − b ≡ 0 für V(N) und β_κ − 2β_λ = 0 bei r = 2.
- **H150b (Skala als Setzung, gewertet):** Baumgraph V = μ²N + λ(A² + B²) + κAB mit μ² < 0 (Skala gesetzt): Minimum bei θ = π/4 genau für −2λ < κ < 2λ,
  bei θ ∈ {0, π/2} für κ > 2λ; für κ ≤ −2λ unbeschränkt. Die Abschneidung gibt beiden Teilen dasselbe δμ² und verschiebt das nicht. Das Vorzeichen von 2a − b
  wird also nicht festgelegt, nur auf das Fenster von κ abgebildet. *Kriterium:* exakte Klassifikation der Minima. Bestätigt, wenn genau diese Fenster herauskommen.
- **H150c (skalenfrei, gewertet):** Auf der Tausch-Linie (λ_A = λ_B, je n Komponenten, n = 1 und n = 2) endet der Fluss ins Infrarote für r < 0 in Klasse (iv) mit
  A = B, also θ = π/4 und K = ⅔ exakt; für 0 < r < 2 ohne Skala mit r → 2 (Krümmung → 0⁺); für r > 2 in einem Teil (θ ∈ {0, π/2}). *Kriterium:* Integration auf
  einem Gitter λ ∈ {0,05; …; 0,5}, r ∈ (−2, 4). Bestätigt, wenn alle Gitterpunkte so ausgehen.
- **H150d (gewertet, offen):** Der Tausch ist nur dann eine Symmetrie des Flusses, wenn Vorstufe und Anhang gleich viele Komponenten haben. In der Lage aus H149
  steht eine reelle Einheit (n_A = 1) gegen die Kopien-Ebene (n_B = 2). Frage: Wo landet der Fluss, wenn er auf der Tausch-Linie λ_A = λ_B mit κ < 0 startet?
  *Kriterium:* K am Gildener–Weinberg-Punkt. „Koide überlebt“, wenn für mindestens 90 % der Startpunkte |K − ⅔| < 1 % gilt; „Koide verschoben“ sonst.
  Vorhersage: verschoben (die β-Funktionen von λ_A und λ_B unterscheiden sich um die Komponentenzahl). Unsicher.
- **H150e (gewertet, offen):** Abseits der Tausch-Linie, gleiche Komponentenzahl (n = 2, Gitter wie H129): Wird |ln(λ_A/λ_B)| zum Gildener–Weinberg-Punkt hin
  kleiner (Tausch infrarot anziehend)? *Kriterium:* Anteil der Klasse-(iv)-Punkte mit kleinerem |ln(λ_A/λ_B)| am Ende als am Start. „Anziehend“ bei ≥ 90 %,
  „abstoßend“ bei ≤ 10 %, sonst gemischt. Dazu der Anteil mit |K − ⅔| < 1 %. Vorhersage: anziehend, aber Koide-Anteil unter 50 %.
- **H150f (nicht blind, analytisch):** Für jedes Potential der HC-Form η(B − μ²A)² verlangt die Beschränktheit η > 0, also κ = −2ημ² < 0 und 2a − b > 0 bei μ = 1.
  Das Minimum liegt bei tan θ = μ; Koide nur bei μ = 1. *Kriterium:* symbolisch.

## Grenzen
- Eine Schleife, ohne Eichfelder; die Zusatzterme K₁–K₄ verschwinden für homogene Felder und fehlen hier.
- Die Zuordnung A = Vorstufe, B = Kopienrichtung ist eine Lesart der Auslesung aus r13/k255.
- OP3, OP4 offen; kein Guard wird berührt. Kein Vorzeichen wird gesetzt: wo eines nötig ist, stehen beide Fälle.
