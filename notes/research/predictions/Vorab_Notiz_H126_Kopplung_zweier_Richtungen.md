# Vorab-Notiz H126: PMNS-Mischung aus der nicht-assoziativen Kopplung zweier Oktonion-Richtungen

**Status:** Festgelegt am 24.11.2026, **vor** jeder Rechnung von Stufe A und B. Freigabe des Autors: „dann mach mal“ (24.11.2026, 10:54 UTC).
Erst nach diesem Commit laufen die Skripte (k257 ff.).

**Blindheit, offen gesagt:** Stufe A ist eine Strukturprüfung. Ihr Ausgang ist teilweise vorhersehbar (Grenzfall χ = 0 liegt in einer
quaternionischen, also assoziativen Unteralgebra). Sie zählt deshalb nicht als Test. Stufe B ist blind: Die Matrix M(χ, δ_ν) wurde für kein
χ ≠ 0 berechnet, und die Lage des verträglichen Bereichs ist unbekannt. Geschätzt ist nur, dass die S₃-Restsymmetrie allein nichts Neues gibt
(k256). Der Test fragt, ob die Brechung durch χ die Daten trifft.

## Vorwissen geprüft
- k253–k256 (`notes/research/hilbert_shift_felder_2026_11_24/`): Kopienbasis g_k = 1/√3 + √(2/3)·w⊗f_k, Koide genau für Ψ = exp(uπ/4)
  (k255), ψ = Phase nur in der Eigenbasis; S₃ als Restsymmetrie gibt nur 𝟙, trimaximal, θ₁₃ = 0, TM1 oder TM2 (k256); TM1-Spalte = imaginäre
  Kopienachse, gehalten von Konjugation ∘ Kopienspiegelung.
- H4 (TM1 stark bevorzugt), H5 (Hopf-Winkel), H8 (μ-τ-Spiegelung, θ₂₃ = 45°, δ_CP = 270°, Spannung χ² = 8,8), H10 (Assoziator),
  H34 (Maske widerlegt), H37 (Trialität widerlegt), H39 (A₄-Untergruppen); r13-Notizen (Ladungsachse e₈ als komplexe Struktur).
- Innerhalb eines einzigen V_w ist alles quaternionisch (assoziativ). Nicht-Assoziativität braucht zwei verschiedene Richtungen w_e ≠ w_ν.
  Ihr Winkel χ ist bis auf G₂ die einzige Invariante des Paares (G₂ transitiv auf S⁶, SU(3) transitiv auf S⁵).
- Zurückgestellte Ideen I1–I7: kein Auslöser trifft zu.

## Hypothese
**H126:** Die PMNS-Mischung entsteht aus der Wirkung des Neutrino-Zustands Ψ_ν auf die Generationszustände der geladenen Leptonen. Der Weg
führt über zwei Linksmultiplikationen in 𝕊, die nicht assoziativ sind. Ein Winkel χ zwischen Elektron- und Neutrino-Richtung und ein Koide-Winkel
δ_ν genügen, um sin²θ₁₂, sin²θ₁₃, sin²θ₂₃ und δ_CP gemeinsam zu treffen.

## Konstruktion (verbindlich)
1. 𝕆 = erste Hälfte von 𝕊, Cayley–Dickson-Konvention wie k253: (a,b)(c,d) = (ac − d*b, da + bc*). Für X ∈ Im 𝕆 und f = (cos θ, sin θ) ist
   X⊗f := cos θ·(X, 0) + sin θ·(0, X). Kopienwinkel θ_k = 2πk/3, k = 0, 1, 2.
2. w_e = e₁, w_ν = cos χ·e₁ + sin χ·e₂ (G₂ erlaubt diese Wahl ohne Verlust).
3. Generationszustände der geladenen Leptonen: g_k = 1/√3 + √(2/3)·w_e⊗f_k.
4. Neutrino-Zustand: Ψ_ν = (1 + w_ν⊗n(δ_ν))/√2 mit n(δ) = (cos δ, sin δ) (Koide-Form aus k255).
5. Komplexe Struktur aus r13 (e₈ = i): ⟨x, y⟩_ℂ := (x*y)₀ + i·(x*y)₈.
6. Massenmatrix der Neutrinos in der Flavourbasis: **M_jk = ⟨g_j, Ψ_ν(Ψ_ν g_k)⟩_ℂ** (zwei Linksmultiplikationen nacheinander, nicht (Ψ_νΨ_ν)g_k).
   Die Eigenvektoren von H = MM† nach aufsteigendem Eigenwert sind ν₁, ν₂, ν₃ (normale Ordnung, H2).
7. Zuordnung der Zeilen: Kopie k ↦ geladenes Lepton nach aufsteigender Koide-Amplitude c_k = 1 + √2 cos(δ_e − θ_k). δ_e wird aus den
   PDG-2024-Massen (m_e = 0,51099895, m_μ = 105,6583755, m_τ = 1776,93 MeV) mit √m_k ∝ c_k angepasst. Beide Orientierungen (θ_k ↦ −θ_k) werden
   gerechnet, die bessere zählt (eine diskrete Wahl, offen ausgewiesen).
8. U = Matrix der Eigenvektoren in dieser Zeilenordnung; Winkel aus |U|², δ_CP aus der Jarlskog-Invariante und |U|² (Konvention PDG), beide
   Vorzeichenzweige.

## Stufe A: Strukturprüfung (nicht blind, wird in jedem Fall berichtet)
- A1: Ist H für allgemeine (χ, δ_ν) nicht entartet? Anteil der entarteten Gitterpunkte (Eigenwertabstand < 10⁻⁹).
- A2: Grenzfall χ = 0 und χ = 180°: Ergebnis U angeben (Erwartung: Permutation oder DFT nach k256).
- A3: Beitrag der Nicht-Assoziativität: ‖M − M_assoz‖/‖M‖ mit M_assoz,jk = ⟨g_j, (Ψ_νΨ_ν)g_k⟩_ℂ. Ist er überall < 10⁻⁹, ist H126 gegenstandslos.
- Gilt A1 überall entartet oder A3 null, wird Stufe B nicht gewertet, und H126 ist „nicht prüfbar“.

## Stufe B: Datenvergleich (blind)
- **Daten:** NuFIT 6.0 (arXiv:2410.05380), Tabelle 1, IC24 + SK, normale Ordnung, wie H4: sin²θ₁₂ = 0,308 (+0,012/−0,011); sin²θ₁₃ = 0,02215
  (+0,00056/−0,00058); sin²θ₂₃ = 0,470 (+0,017/−0,013); δ_CP = 212° (+26/−41). Gauß-Näherung mit asymmetrischen Fehlern.
- **Gitter:** χ ∈ [0°, 180°], δ_ν ∈ [0°, 360°), je 0,5°; danach lokale Verfeinerung um das Minimum.
- **χ²** aus vier Größen, zwei Parameter, also 2 Freiheitsgrade.
- **Kriterium:** χ²_min ≤ 5,99 → **trägt**; 5,99 < χ²_min ≤ 9,21 → **Spannung**; χ²_min > 9,21 → **widerlegt**.
- **Schärfe (Nebenkriterium):** Liegt mehr als 20 % der (χ, δ_ν)-Fläche bei χ² ≤ 5,99, gilt das Ergebnis als „nicht scharf“, als Anpassung, nicht als
  Vorhersage.
- **Ausgewiesen werden außerdem:** χ und δ_ν im Bestfall, ob χ in die Nähe ausgezeichneter Werte fällt (Vielfache von 30°, magischer Winkel 54,74°,
  Hopf-Winkel 66,64°; nur berichtet, kein Kriterium) und der Beitrag von δ_CP allein.

## Werkzeuge
Python (numpy) für Gitter und Diagonalisierung (k257). Wolfram exakt als unabhängige Kontrolle von M an drei festen Punkten (k257b). Kein
Qiskit, kein HDL (kein endlicher Auswahlablauf).

## Grenzen
- Die Konstruktion setzt viel: e₈ als i (r13), Ψ_ν in Koide-Form, den Weg Ψ_ν(Ψ_ν g) und MM† als Massenoperator. Diese Setzungen werden
  vor der Rechnung festgelegt und danach nicht geändert. Eine Änderung braucht eine neue H-Nummer.
- Selbst „trägt“ wäre bei zwei Parametern für vier Größen nur ein schwacher Befund, es sei denn χ und δ_ν fallen auf ausgezeichnete Werte.
- OP3/OP4 offen; kein Guard berührt.
