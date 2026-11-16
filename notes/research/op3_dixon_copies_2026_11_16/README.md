# OP3: Zwei und vier Dixon-Kopien (Tensor-Shift HS(7), HS(8)); die vierte Kopie als Normale der drei

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind** (die Rechnungen sind Darstellungstheorie und stehen analytisch fest), ohne
Kriterium, keine H-Nummer. Idee und Auftrag des Autors: „Dixon reicht mit 64 Dimensionen nicht“, „HS(7) trägt zwei, HS(8) vier
Algebren; die vierte speichert die Normalen der drei anderen zueinander“, „2 × HS(7) passen in HS(8), 2 × HS(6) in HS(7), Partitionieren
durch Halbierung“, dann „prüfe das“. Skript `dixon_copies.py`, Ausgabe `run/dixon_copies_stdout.txt`. OP3 bleibt offen.

## Vorwissen geprüft
- **Atlas (v470/32, „HS(6) Dixon carrier and 64-bit activation code“):** Der Tensor-Shift HS(n) hat 2ⁿ Kanäle und 2^(2ⁿ) Masken; HS(5) ist
  die zweiseitige Verdopplung, HS(6) der Dixon-Träger C⊗H⊗O mit 64 Bit. **HS(7) und HS(8) sind im Atlas nicht definiert**, weder
  zugelassen noch ausgeschlossen.
- **v4.10.0-r19 (`../op3_frame_bridge_2026_11_15/`):** Der Kommutant von Eich- und Lorentzgruppe auf einer Generation ist C⁶ (eine Phase je
  Multiplett); kein Generations-Qubit; mit n Kopien M_n(C), die Kopien müssen vorher da sein, und die Frame-Abbildungen wirken auf ihnen
  nicht.
- **v4.10.0-r15.4 (Komplementarität):** Ein vollständiger Satz unverzerrter Basen in Dimension d gibt d + 1 Zustände mit K = 2/(d + 1);
  nur d = 2 gibt drei Zustände und K = 2/3.
- **v4.10.0-r14:** det G = (√2 cos φ − 1)/2 trennt den flachen Oktanten (φ = π/4, det G = 0, eine Masse null) von drei positiven Massen.
- **Spin-1-Dreieck (`../op3_spin1_triangle_2026_11_15/`, r15.3):** drei kohärente Spin-1-Zustände mit Überlappung ½: K = 2/3, Phase
  0,679042, det G = 0,0503, Wurzel-Verhältnisse 1 : 16,24 : 65,93; bis zur Lepton-Phase 2/3 fehlen 0,012376.
- **Zeitzyklus (`../op3_time_cycle_2026_11_15/`, r16.9):** nötige Gewichte p_k = √m_k/Σ√m (Leptonen: τ 0,7931, μ 0,1934, e 0,01345); kein
  nativer Wert.
- **v4.10.0-r13:** Weg A (Sedenionen, 128) gibt 2T und den Bezug, aber zwei Generationen; Weg B (O³, Trialität) drei Generationen, aber
  S₃ und K = 1/2. Ein Drei-Generationen-Träger mit neutralem Levi-Civita-Tripel fehlt (r13.6, r14.3–r14.4).
- Literatur zu Erweiterungen (Albert-Algebra J₃(O), Sedenionen nach Gresnigt): im Repo nicht vorhanden, hier nicht nachgelesen.

## Ergebnisse
1. **Kommutant auf n Kopien.** Eine Generation (16 Weyl-Komponenten × 2 Spinorkomponenten = 32 komplex = 64 reell) hat den Kommutanten C⁶
   (nachgerechnet, wie r19). Auf n Kopien zerfällt jeder Kommutant blockweise in n² Blöcke: dim = 6 n², für n = 2 nachgerechnet (24), für
   n = 4 aus der Blockstruktur (96). Der Kopienanteil ist **M_n(C)**; die Eichgruppe wirkt auf dem Kopienindex trivial. Jeder Zustand auf
   dem Kopienindex hat deshalb **bestimmte Ladung**; das Hindernis aus r16.1 (keine bestimmte Ladung auf C⊗O) entfällt dort.
2. **HS(7): zwei Kopien, ein Qubit, flacher Oktant.** Die drei unverzerrten Zustände +x, +y, +z des Kopien-Qubits haben Überlappung ½,
   K = 2/3, Phase π/4 und **det G = 0**: das ist der flache Oktant mit einer masselosen Generation, also effektiv zwei massive. Das passt zum
   Befund von Weg A in r13 (128 Dimensionen, zwei Generationen); eine Lesart, kein Nachweis, dass beide dasselbe meinen.
3. **HS(8): vier Kopien = zwei Qubits = Triplett + Singulett.** Der Kopienindex C⁴ = C² ⊗ C² zerfällt in den symmetrischen Teil (Spin 1,
   drei Zustände) und den antisymmetrischen Teil (Spin 0, ein Zustand, der Levi-Civita-Tensor ε_ab). Das Spin-1-Dreieck liegt ganz im
   Triplett (Singulettanteil 10⁻¹⁷) und ist **gebogen**: K = 2/3, Phase 0,679042, det G = 0,050253, drei positive Massen.
4. **Die vierte Kopie speichert die Normale der drei, kanonisch.** Die einzige SU(2)-äquivariante Abbildung von drei Triplett-Vektoren
   auf das Singulett ist ihr Spatprodukt det V = v₁ · (v₂ × v₃): die Kreuzprodukte sind die „Normalenvektoren“, das Spatprodukt das
   orientierte Volumen. Nachgerechnet: det V = −0,224171 i, **|det V|² = det G = 0,050253**, unverändert unter gemeinsamer SU(2)-Drehung;
   das Singulett ist invariant und ladungsneutral. Damit gilt:

   | Fall | Phase φ | det G = \|det V\|² | Singulett trägt |
   |---|---|---|---|
   | flacher Oktant (HS(7)) | π/4 | 0 | nichts |
   | Spin-1-Dreieck (HS(8)) | 0,679042 | 0,050253 | die Biegung |
   | Leptonen | 2/3 | 0,055706 | die Biegung |

   Die vierte Algebra ist genau dann besetzt, wenn die drei Generationen gebogen sind, also alle drei Massen positiv. Das ist der
   gesuchte **neutrale Levi-Civita-Träger** aus r13.6, hier auf dem Kopienindex.
5. **Halbierung (Vermutung des Autors bestätigt).** HS(8) = HS(7) ⊕ HS(7) und HS(7) = HS(6) ⊕ HS(6): Das erste Kopien-Bit halbiert HS(8),
   das zweite jede Hälfte; die vier Kästen |00⟩, |01⟩, |10⟩, |11⟩ sind die vier Dixon-Algebren. **Triplett und Singulett liegen quer zur
   Halbierung:** Das Singulett (|01⟩ − |10⟩)/√2 hat in jeder Hälfte Gewicht ½. Es gibt also zwei Zerlegungen desselben Trägers, die
   Halbierung in Kästen und die Symmetrie in 3 + 1. Die Generationen sind nicht die Kästen, sondern über sie verteilt.
6. **Nachträglicher Befund: Die Kästen tragen die Massenhierarchie.** Jede der drei Generationen verteilt sich gleich über die Kästen:
   |00⟩ 0,7927, |01⟩ und |10⟩ je 0,0976 (zusammen 0,1952), |11⟩ 0,0120. Das sind die Wurzel-Gewichte des Spin-1-Dreiecks (1 : 16,24 : 65,93),
   wie es die Fourier-Struktur verlangt; neu ist nur die Lesart über die Kästen. Gegen die Leptonen (τ 0,7931, μ 0,1934, e 0,01345):
   τ auf 0,05 %, μ auf 0,9 %, e auf 11 % getroffen. Die Abweichung ist die bekannte Restbiegung (Phase 0,679 gegen 2/3). Nachträglich
   gefunden, nicht blind.

## Was damit erreicht ist
- **Die Zwei als Eingabe statt der Drei.** Der binäre Shift liefert Kopienzahlen 2ⁿ. Zwei Kopien geben ein Qubit und daraus drei Auslesungen
  mit K = 2/3 (flach); vier Kopien geben Triplett plus Singulett, gebogen, mit dem Volumen im Singulett. Drei Generationen müssen nicht als
  drei Kopien gesetzt werden.
- **Die offene Größe bekommt einen Ort.** Die Biegung (Kerngröße γ_M) ist eine Eigenschaft der Beziehung der drei Generationen, nicht einer
  einzelnen. In HS(8) hat sie einen eigenen, neutralen Platz.

## Was offen bleibt
- **HS(7) und HS(8) sind im Atlas nicht definiert.** Ob die Regeln von HS(4) (Leck-Tor) und HS(5) (schuldenfreie Zweiseitigkeit) eine siebte
  und achte Stufe zulassen, ist nicht geprüft; es wäre eine Erweiterung des Atlas.
- **Gesetzt bleibt,** dass die Generationen im Triplett als kohärente Spin-1-Zustände mit Überlappung ½ ausgelesen werden (r15.4, Spin-1-
  Dreieck). Warum gerade diese drei Zustände, bleibt die Kernfrage von Koide.
- **Der Rest 0,012376** zur Lepton-Phase ist nicht erklärt; das Singulett speichert die Biegung, legt ihren Wert aber nicht fest.
- **Frame-Abbildungen** wirken auf dem Kopienindex nicht (r19); die Lesart „eine Generation je Frame-Abbildung“ (r15.5) trägt hier nicht.
- Kein Test. OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
