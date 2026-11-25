# Vorab-Notiz H140: Sind die drei Sedenion-Kopien Generationen? (gleiche Eichdarstellung, Vertauschung mit der Eichgruppe)

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** k255d hat schon gezeigt, dass die drei Kopienladungen
Q^(k) = ψ^k Q_S ψ^{−k} nicht vertauschen und ihr Mittel ½·𝟙 ist; K28 und H138 zeigen, dass die drei Kopien nur zwei unabhängige Richtungen
aufspannen. Teile c und d sind deshalb **nicht blind** und werden an einer breiteren Familie geprüft. Blind ist Teil a (gemeinsame Farbe) in der
hier verwendeten Form und die Suche in c über die ganze Familie α + βL_x + γR_x. Anlass: Frage des Autors (25.11.2026, 19:50): „wie könnte man
zeigen, dass diese Kopien die Generationen sind?“, Auftrag über den Koordinator (Marc: „ja“, 19:51): Test (1) gleiche Darstellung unter
su(3) × su(2) × u(1), nur Kopienindex verschieden; Test (2) vertauscht S₃ mit der Eichgruppe? Massen, Koide, Mischung bleiben außen vor.

## Vorwissen geprüft
- H138 (Vorab 31732b4), H139 (c41040c): genau drei G₂-stabile Kopien in 𝕊 (Im z³ = 0), Rang 2; Nullteiler = flaches Kopienprofil.
- k255 (`../r13/`): ψ (120°-Drehung in allen Ebenen (e_i, e_{i+8})) permutiert die Kopien; Kopienladungen vertauschen nicht, Mittel ½·𝟙;
  ℂ⊗𝕊 (16 komplex) kann 3 × 8 = 24 Zustände nicht tragen.
- k85: Q8 = ½ − (i/6)L_{e₇} − (i/3)R_{e₇} gibt auf ℂ⊗𝕆 genau eine Generation (Spektrum 0, ⅓³, ⅔³, 1).
- K28: Aut(𝕊) = G₂ × S₃, S₃ vertauscht mit G₂ (exakt); Weg B (𝕆 ⊕ 𝕆 ⊕ 𝕆 mit Trialität) trägt Rang 9.
- k260 (`../drei_kopien_k259/`): Ladungsrichtungen u_k = e₇, −½e₇ ± (√3/2)e₁₅; S₄/A₄ auf drei Plätzen.
- su(2)_L: in ℂ⊗𝕆 (Furey-Form) nicht enthalten; im Projekt kommt sie aus der HS(2)-Stufe (ℍ). Auf einem Träger ℂ⊗ℍ⊗𝕊 wirkt sie auf einen anderen
  Tensorfaktor als S₃ und vertauscht damit **per Konstruktion** (Setzung, nicht gerechnet). Nichttrivial sind nur su(3)_c und u(1).

## Aufbau
Träger ℂ⊗𝕊 (Konvention k253). Kopien C_k = ℂ⊗O_k, O_k = span{1} ⊕ Im 𝕆 ⊗ f_k, f_k bei 0°, 120°, 240°. ψ wie k255.
Je Kopie: Farbe su(3)_k = Stabilisator von u_k = e₇ ⊗ f_k in der blockweisen g₂; Ladung Q_k = ½ − (i/6)L_{u_k} − (i/3)R_{u_k}.
Skript k323 (Python), Gegenprobe k323b (Wolfram, exakt).

## Hypothesen und Kriterien
- **H140a (gemeinsame Farbe, vertauscht mit S₃):** su(3)_0 = su(3)_120 = su(3)_240 als Teilräume (Hauptwinkel < 10⁻¹⁰), jedes Element
  vertauscht mit ψ und mit der Spiegelung ε (Kommutator < 10⁻¹²), und auf jeder Kopie zerfällt C_k unter su(3) in 1 ⊕ 1 ⊕ 3 ⊕ 3̄ (Casimir-Spektrum).
- **H140b (gleiche Darstellung je Kopie):** Q_k bildet C_k in sich ab (Leck < 10⁻¹²) und hat dort das Spektrum einer Generation; die
  Gewichte (Farbe, Ladung) sind für k = 0, 1, 2 gleich, und ψ bildet die Zustände von Kopie k auf die gleich geladenen von Kopie k + 1 ab.
- **H140c (gemeinsame Ladung, nicht blind):** Es gibt **keinen** Operator Q = α + βL_x + γR_x (x ∈ Im 𝕊, α, β, γ ∈ ℂ, (β, γ) ≠ 0), der alle drei
  C_k in sich abbildet und auf jeder Kopie das Generationsspektrum hat. Bestätigt, wenn das Minimum des Lecks über x und (β, γ) (500
  Zufallsstarts) > 10⁻³ ist; widerlegt, wenn eine Lösung mit Leck < 10⁻¹⁰ gefunden wird. Dazu ‖ψQ_0ψ⁻¹ − Q_0‖ berichtet.
- **H140d (Zahl unabhängiger Zustände, nicht blind):** dim_ℂ(C_0 + C_120 + C_240) = 15 < 24.
- **Kontrolle:** Spektrum von Q_0 auf C_0 = (0, ⅓, ⅓, ⅓, ⅔, ⅔, ⅔, 1) (k85); dim su(3)_k = 8.

## Folge, vorab festgelegt
„Die drei Kopien sind drei Generationen“ im Sinn des Auftrags gilt nur, wenn a, b gelten **und** c widerlegt ist (gemeinsame Ladung existiert)
**und** d 24 ergibt. Erwartet ist: a, b bestätigt (Farbe und je-Kopie-Darstellung sind gleich, S₃ vertauscht mit der Farbe), c bestätigt
(keine gemeinsame Ladung in der Multiplikationsfamilie) und d = 15. Dann sind die Kopien in ℂ⊗𝕊 **Etiketten mit gleicher Farbstruktur**, aber
keine drei Generationen mit gemeinsamer elektroschwacher Ladung; der Generationsträger muss außerhalb von ℂ⊗𝕊 liegen (Weg B oder höhere
Stufe). Was in keinem Fall folgt: Massen, Mischung, Vorzeichen. OP3, OP4 offen; kein Guard berührt. Vergeben: H140, k323.
