# Vorab-Notiz H131: Legt S₄ mit der Ladung als verallgemeinerter CP die Mischung ohne weitere Wahl fest?

**Stand:** 2026-11-25, vor der Rechnung festgelegt. **Teilweise nicht blind** (Rahmen aus der Literatur, siehe „Vorab offengelegt“). Anlass: Autor, 25.11.2026, 10:33 UTC:
„merge und pushen dann weiter“, auf die in k260 genannte nächste Frage; Nummer H131 nach Abstimmung (H129 gehört dem Feldgleichungs-Faden). Skripte **k261** (Python numpy;
Wolfram Language exakt für die CP-Abbildungen in der Basis der geladenen Leptonen). Qiskit nicht vorgesehen (keine Schaltung). Bezug OP3 (#131), OP4.

## Vorwissen geprüft
- **k260** (#300): Kopie k auf Platz k von H₃(𝕊) lässt die Würfelgruppe S₄ (24 Elemente). 12 vertauschen mit der Ladung (A₄), 12 erhalten sie nur bis auf Vorzeichen und L ↔ R.
- **k275 / r60**: A₄ aus der Ladung; „mit der Konjugation als antiunitärem Teil könnte S₄ als verallgemeinerte CP zurückkehren“, nicht gerechnet.
- **H39 / r55**: ℤ₃ für Dirac-Sektoren, ℤ₂ für Neutrinos gibt TM2 mit sin²θ₁₂ ≈ 0,341, 3,6σ über JUNO 2025. **H43**: CP-Phase aus TM2 nicht festgelegt. **H41**: TM2 mit Maskenkorrektur.
- **H8**: Cayley–Dickson-Involution als CP → TM1, θ₂₃ maximal, δ_CP = 270°. **H4**: TM1 gegen TM2. **k256**: Kopien-S₃, K∘S₀ hält TM1. **k280**: TM1-Spalte je nach Vorzeichen.
- **k278, k282**: Ein Feld im Spin-1-Teil erzwingt ℤ₃; welche Restgruppe das Vakuum hat, hängt an offenen Vorzeichen (Feldgleichung, anderer Faden).
- **H125** Stufe B (sin δ_PMNS < 0 unter Setzung S1, offen).

## Aufbau
- **Gruppe:** Die 24 Elemente aus k260, auf das Triplett der drei Plätze eingeschränkt: komplexe Koordinate z_k = s_k + i·v_k (Realteil und Ladungsrichtung u_k des Eintrags k).
  Die 12 Elemente von A₄ wirken komplex-linear mit den Matrizen ρ(g) (vorzeichenbehaftete gerade Permutationen). Die 12 übrigen wirken antilinear, z ↦ X·z̄.
  Die Matrizen X werden aus k260 abgelesen, nicht gesetzt.
- **Restsymmetrien (wie H39):** geladene Leptonen ℤ₃ = ⟨T⟩ (H_e = M_eM_e† mit T H_e T† = H_e), Neutrinos (Majorana) ℤ₂ = ⟨S⟩ (Sᵀ m_ν S = m_ν) und zusätzlich eine CP-Abbildung X
  (Xᵀ m_ν X = m_ν*). Zulässig ist X, wenn X S = S X und X X* ∈ {1, S}.
- **Aufzählung:** alle T (8 Elemente der Ordnung 3), alle S (3), alle zulässigen X. Je Kombination 200 zufällige H_e und m_ν aus dem Lösungsraum der Bedingungen,
  U = U_e†U_ν. Ausgewertet werden nur Größen, die von Phasen und von der Reihenfolge der Zeilen und Spalten unabhängig sind: eine über die Stichprobe konstante Spalte
  (sortierte |U|²), |J| (Jarlskog), und ob zwei Zeilen von |U|² gleich sind.
- **Klasse** einer Kombination: (konstante Spalte, J ≡ 0 oder nicht, zwei gleiche Zeilen oder nicht).

## Vorab offengelegt (kein Teil der Vorhersage)
1. Ohne CP gibt (ℤ₃, ℤ₂) die trimaximale Spalte (⅓, ⅓, ⅓), also TM2 (H39, Literatur). Das ist Kontrolle. Die Spalte ist nach H39 bereits 3,6σ von JUNO entfernt;
   dieser Test kann daran nichts verbessern und ist kein neuer Datenvergleich.
2. A₄ mit verallgemeinerter CP ist in der Literatur behandelt (Feruglio–Hagedorn–Ziegler 2013; Ding–King–Stuart 2013; aus Vorwissen, ungeprüft). Dort treten je nach X
   Fälle mit sin δ = 0 und mit |sin δ| = 1 bei θ₂₃ = 45° auf. Welche davon die hier abgelesenen X tragen, habe ich nicht gerechnet. Ich erwarte eher zwei Klassen als eine.
3. Zwei gleiche Zeilen in |U|² zusammen mit J ≠ 0 bedeuten θ₂₃ = 45° und |sin δ| = 1 (μτ-Spiegelung, Literatur).
4. Gesetzt bleiben: Kopie k auf Platz k (k260), die Plätze als Generationen, die Zuordnung ℤ₃ zu geladenen Leptonen und ℤ₂ zu Neutrinos, Majorana-Neutrinos.

## Hypothesen und Kriterien
- **H131a (keine weitere Wahl):** Alle zulässigen Kombinationen (T, S, X) fallen in **eine** Klasse.
  - **Bestätigt:** genau eine Klasse. **Widerlegt:** zwei oder mehr Klassen (dann bleibt die Wahl von X offen und wird benannt).
- **H131b (die CP aus der Ladung legt die Phase fest):** Es gibt eine Klasse mit trimaximaler Spalte, J ≢ 0 und zwei gleichen Zeilen, also θ₂₃ = 45° und |sin δ| = 1.
  - **Bestätigt:** Zeilengleichheit < 10⁻⁹ in allen 200 Stichproben einer Kombination und |J| > 10⁻³ in mindestens einer. **Widerlegt:** In jeder Klasse ist J ≡ 0 (< 10⁻¹⁰)
    oder es gibt keine Zeilengleichheit.
- **Kontrollen:** (i) Die 24 Matrizen bilden eine Gruppe im Sinn der gemischt linearen und antilinearen Verknüpfung; 12 linear, 12 antilinear. (ii) Ohne X: konstante Spalte
  (⅓, ⅓, ⅓) auf 10⁻¹⁰. (iii) Die Lösungsräume haben positive Dimension und geben generisch drei verschiedene Massen (sonst wird die Kombination als entartet ausgewiesen und
  nicht gewertet). (iv) Wolfram exakt: X in der Basis der geladenen Leptonen für je einen Vertreter jeder Klasse.

## Folge, vorab festgelegt
- **a und b bestätigt:** Die Struktur aus k260 gibt ohne weitere Wahl TM2 mit θ₂₃ = 45° und |sin δ| = 1. Das Vorzeichen von sin δ legt dieser Test nicht fest (Bezug H125 Stufe B).
  Die Spannung der TM2-Spalte mit JUNO bleibt bestehen.
- **a widerlegt:** Die Wahl von X ist eine weitere offene Eingabe; die Klassen werden aufgelistet. Gilt b, ist |sin δ| = 1 eine der Möglichkeiten, keine Vorhersage.
- **b widerlegt:** Die CP aus der Ladung legt die Phase nicht auf ±90°; berichtet wird, was sie stattdessen festlegt.
- In jedem Fall bleiben OP3 und OP4 offen, kein Guard wird berührt. Die Vorzeichen der Massenterme (Feldgleichung) werden nicht berührt.
