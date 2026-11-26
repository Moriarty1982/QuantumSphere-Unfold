# Vorab-Notiz H158: Die offenen Zellen der Träger-Tabelle für die Albert-Algebra: Zyklus, magischer Winkel, K = ⅔ und δ

**26.11.2026, vor der Rechnung committet.** Anlass: Autor („dann gehen wir mal die 2/9 an“, mit Verweis auf die Träger-Tabelle des Companion/Physik-Papers,
Abschnitt Teilchen): Für die Albert-Algebra H₃(𝕆) mit exakter A₄ (r60) stehen dort „order-3 cycle on a neutral qubit“, „reference at the magic angle“ als
*not examined* und „K = 2/3“ als *not addressed*; bei den Dixon-Kopien Zyklus und Mischung. Auftrag: diese Zellen gezielt untersuchen, im Rahmen des Postulats
(Tausch J als Symmetrie, H156/H157), und schauen, ob eine Phase δ = 2/9 herauskommt. Vergeben: H158, Skripte k341 (Python), k341b (Wolfram). Qiskit nicht
vorgesehen. Kein Vorzeichen wird gesetzt.

## Vorwissen geprüft
- r60, k275–k282 (`../rueckwaerts/`): Familien-SO(3) → A₄ unter der Ladung C; spurfreier Teil von H₃(ℂ) = Diagonale d ⊕ reelle Nebendiagonale s ⊕ imaginäre
  Nebendiagonale v; Tr(W∘σW) = |d|² + 2[(1 − c²)(|s|² − |v|²) − 4c s·v]; Vakuum je Vorzeichen ℤ₃, V₄ oder flach (k282). Dort wurde δ nicht ausgelesen.
- H149–H157: Drei-Felder-Modell (φ, y₁, y₂); mit J K = ⅔; unter der Ebenen-Lesart ist cos 3δ erst ab Ordnung 6, cos² 3δ erst ab Ordnung 12 erlaubt (H157b,
  Rechnung liegt vor, Ergebnis-Notiz in Arbeit).
- r14.5, r16.9: zirkulante Gram-Matrix, Brannen-Form, det G = ½(√2 cos φ − 1); 143 Kandidatenrichtungen ohne Treffer (r28.2).
- H140–H146: Dixon-Kopien: Zyklus als S₃ der Kopien, Massen nicht aus Kopien, Mischung nicht hergeleitet. Die Dixon-Zellen werden hier nur eingeordnet, nicht neu gerechnet.

## Vorüberlegung (vor der Rechnung; damit sind a und b nicht blind)
Der Platztausch P (Ordnung 3, in A₄) wirkt auf H₃ durch Konjugation. P-invariante Elemente sind Zirkulanten W = a·1 + b S + b̄ S² (in H₃(𝕆): x₁ = x₂ = x₃ = x,
und x erzeugt mit 1 eine komplexe Unteralgebra, also H₃(ℂ_x)). Eigenwerte: a + 2|b| cos(arg b + 2πk/3). Das ist die Brannen-Form mit δ = arg b:
**δ ist die Phase der Nebendiagonale, tan δ = v/s.** Tr W² = 3a² + 6|b|², also K = ⅔ ⇔ 3a² = 6|b|²: Spuranteil und Nebendiagonalanteil haben gleiche Norm.
Das ist genau der Tausch φ ↔ r. Die Eigenvektoren von P sind die Fourier-Vektoren; (1,1,1)/√3 steht zu jeder Platzachse im magischen Winkel arccos(1/√3).
Neu gegenüber H157: die Zirkulante kennt neben dem Z₃-Term det (cos 3δ) auch Re b² (cos 2δ, aus σ) und |b|² Re b (cos δ), weil A₄ auf der Nebendiagonale
nur Vorzeichenpaare wechselt.

## Hypothesen und Kriterien
- **H158a (nicht blind):** Zyklus, magischer Winkel und Brannen-Form wie oben, exakt. *Kriterium:* symbolische Nullreste (Wolfram), numerisch in H₃(𝕆) mit
  x₁ = x₂ = x₃ für 20 zufällige Oktonionen x (Eigenwerte über die komplexe Unteralgebra, Vergleich mit Tr, Tr W², det der Albert-Algebra aus k276).
- **H158b (nicht blind):** K = ⅔ ⇔ gleiche Norm von Spur- und Nebendiagonalanteil, d. h. unter dem Postulat (J: a√3 ↔ |b|√6 bei fester Phase) ist K = ⅔ der
  Fixpunkt. *Kriterium:* symbolisch.
- **H158c (gewertet):** A₄-invariante, J-erlaubte Polynome auf dem Zirkulantensektor (a, s, v), aufgezählt bis Ordnung 8 nach Harmonischer cos nδ / sin nδ.
  Vorhersage: niedrigster δ-abhängiger Term ist Ordnung 4 (φ²r² cos 2δ, mit sin 2δ nur ohne σ-Symmetrie); cos δ und cos 3δ zuerst bei Ordnung 6; cos 4δ bei
  Ordnung 8. Folge: innere δ (drei verschiedene Massen) schon aus Ordnung 4 + 6, nicht erst Ordnung 12 wie in H157. *Kriterium:* Aufzählung auf zwei Wegen
  (Python über Monome in b_k, b̄_k mit V₄-Parität; Wolfram über allgemeine Polynome mit direkter Invarianzforderung) stimmt überein und trifft die Vorhersage.
- **H158d (gewertet, Kandidatensuche):** Kommt 2/9 ohne Fit heraus? Mit σ als Symmetrie und den natürlichen Invarianten I₄ = (Tr W)²·[Tr(W∘σW)]_δ,
  I₆ = (Tr W)³·det W und I₆′ = (Tr W)³·Re Σ_zykl b₁b₂b̄₃, in Einheiten v² = Tr W² = 1 (Λ = v), ist V_δ = α I₄ + β I₆ (bzw. β′ I₆′) bei K = ⅔.
  Kandidaten für β/α (und β′/α), vorab festgelegt: ±(p/q)·w mit p, q ∈ {1,…,6}, w ∈ {1, √2, √3, 1/√2, 1/√3}. *Kriterium:* Treffer, wenn das Minimum-δ
  (modulo der Symmetrien der Brannen-Form) innerhalb 3σ des Messwerts liegt (δ aus PDG-Massen, σ aus m_τ = 1776,93 ± 0,09 MeV); dazu Zufallserwartung.
  Vorhersage: kein Treffer über Zufall. Nicht blind in einem Punkt: der nötige Wert für das Paar (cos 2δ, cos 3δ) in der Form A cos 2δ + B cos 3δ ist
  B/A = −2 sin 2δ/(3 sin 3δ) ≈ −0,46 (vorab im Kopf überschlagen).
- **H158e (Lesart):** Was die Ladungsmischung c tut: w_k = (1 + ic)(s_k + iv_k), also arg b = arctan c + atan2(v, s). Vorhersage: c ist auf dem Zirkulantensektor
  eine Umparametrisierung der Phase und legt δ nicht fest; der σ-Term ist |b|² cos(2 arg b). *Kriterium:* symbolischer Nullrest gegen die k282-Formel.

## Grenzen
- Zirkulantensektor (P-invariantes Vakuum); Stabilität gegen nicht zirkulante Richtungen wird nicht gerechnet (k282 gibt ℤ₃-Vakua für vier von acht Vorzeichenfällen).
- Ebenen-Lesart des Postulats wie H157. Baumniveau. Dixon-Zellen nur eingeordnet.
- OP3, OP4 offen; kein Vorzeichen gesetzt; kein Guard berührt.
