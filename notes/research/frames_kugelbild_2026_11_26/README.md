# Frames der Konvention F und der HC als Bild auf der Zustandskugel (Erkundung, nicht blind, 26.11.2026)

Aufträge des Autors (26.11.2026): die Frames als gewöhnliche 3D-Grafik in Teilbildern; danach klären, warum die Portgewichte
abweichen, und was der HC in diesem Bild macht. Keine H- und keine k-Nummer, keine Runde, kein Guard berührt.
β_sym ist eingesetzt (OP1 offen).

## Teilbilder
- **A** Halbkugel der Feldzustände mit R, M, P, T, Schub-Meridian und den drei Abbildungen D, ϑ, J_B.
- **B** Schnitt durch die Meridianebene mit Rapiditätsmarken, HC-Achse und Portgewichten.
- **C** Je Frame: Feldvektoren (Vertreter mit |E| = |B|), Schwingungsellipse, Portgewichte.
- **D** Der HC: Achse der Kugel, Schatten auf der Achse, Sprung in einen Port; zwei Wege von R auf dieselbe Höhe.

Dateien `frames_{A,B,C,D,gesamt}_*` je `de` und `en`, PDF und PNG. Aufruf: `python frames_kugelbild.py --lang de|en [--out ORDNER]`.
Ausgabe der Kontrollrechnung (sympy, exakt): `kontrolle_out.txt`.

## Koordinaten
ρ = G/tr G = ½(1 + b_S σ_z + b_C σ_x) mit b_S = (|E|² − |B|²)/(2u) (im Artikel b₁) und b_C = E·B/u (im Artikel b₂).
Mit b₃ = |E×B|/u ≥ 0 gilt b_S² + b_C² + b₃² = 1 (Kontrolle 1): Jeder Feldzustand ist ein Punkt einer Halbkugel, und die
Zustandsscheibe der Konvention F ist ihr Schatten. b₃ ist der Anteil des Energieflusses.

## Der HC im Bild
Im Feld-Dublett ist J_B = σ_x und C_HC = ½(1 + σ_x) (r04.1, r27: „compensator axis along x“). Die Achse des HC ist also b_C.
- Energie im Kompensator-Port: u + E·B (r04.3), als Anteil p₊ = (1 + b_C)/2 = |E + B|²/(4u). Der HC sieht nur die Höhe b_C.
- Was er durchlässt, hat E′ = B′ = (E + B)/2 und liegt am Pol b_C = 1; der Partner A liegt am Gegenpol (Kontrolle 4; r23.2).
- Nicht selektiv (beide Ports behalten, Kohärenz verworfen): b ↦ (b_C, 0), der Schatten auf der Achse (r27).
- Die Frames der Konvention F („compensator port holding p₊“) liegen auf dieser Achse bzw. auf dem Meridian darüber:
  R am Pol (E = B), M bei b_C = 1/γ_L (Winkel zwischen E und B 57,57°), P auf dem Äquator (E ⊥ B), T bei −1/γ_L.
- Zwei Wege von R auf die Höhe von M: der Schub ε = artanh β_sym (Kontrolle 2, 3; r24.3, H164) und die Dualitätsdrehung um
  α mit tan α = β_sym gefolgt vom HC (Kontrolle 5; r27.1(b), p₊ = cos²α = 0,7681). Der HC unterscheidet sie nicht.
- D (b ↦ −b) und ϑ (b_C ↦ −b_C) tauschen M und T; J_B (b_S ↦ −b_S) lässt alle vier Frames fest, wie es für die Involution
  des Projektors sein muss.

**Berichtigung zum ersten Stand dieser Notiz:** Dort war die Port-Achse als b₁ = (|E|² − |B|²)/(2u) beschriftet
und J_B als Spiegelung am Äquator angegeben. Mit C_HC = ½(1 + σ_x) ist die Port-Achse b_C = E·B/u.

## Warum die Portgewichte abweichen (76,8 : 23,2 gegen 91,65 : 8,35)
Dieselbe Zahl x = β_sym² steht an zwei Stellen in verschiedener Rolle (Kontrolle 6):
- Konvention F (r17, r22): x ist das Verhältnis der **Gewichte** (Energien), p₋/p₊ = x. Das ist durch den Schub gedeckt
  (r24.3, H164) und wird überall benutzt (Ω_M = p₋/p₊, |b| = 1/γ_L).
- k292/k297: x ist das Verhältnis der **Amplituden** der zwei Kreisanteile, b/a = μ = x. Die Gewichte sind dann 1 : x² =
  91,65 : 8,35, die Höhe ist 0,8330 (33,59° vom Pol). Das ist der Zustand nach einem Schub mit Geschwindigkeit β_sym², nicht M.
- Die Vermischung steht schon in `thm:hc-quasiconformal`: Der Beweis nennt μ „the ratio of the eigenvalues“ (ein Verhältnis
  von Gewichten) und setzt es in K = (1 + μ)/(1 − μ) ein, wo ein Amplitudenverhältnis stehen müsste.
Hält man die Gewichte der Konvention F fest und liest die Ports als die zwei Kreisanteile (k253), dann ist b/a = β_sym,
die Ellipse hat die Achsen e^{2ε} : 1 = 3,439 : 1, und γ_L = cosh 2ε ist nicht ihr Achsenverhältnis, sondern 1/b_C.
So ist Teilbild C gezeichnet; die Ellipse aus k297 (γ_L : 1) steht gestrichelt daneben.
**Ausgeführt in Runde v4.10.0-r70** (`notes/research/v4_10_0_r70_portgewichte_hc/`, Nachrechnung k382).

## Offene Stelle
Die Sektorregel (Materie Re s > 0, also b_S > 0; r04.2(a)) und die Lage der Frames auf der HC-Achse (b_S = 0, s rein
imaginär) benutzen verschiedene Achsen der Scheibe. Sie gehen durch eine Dualitätsdrehung um 45° ineinander über
(Prop. A-orbits (c)); welche Achse gemeint ist, sagt Konvention F nur über die Worte „compensator port“.

## Grenzen
Lesart und Darstellung, kein Befund mit Kriterium. HS-Stufen nicht dargestellt. Werkzeug: sympy (exakt); Wolfram und Qiskit
nicht eingesetzt (kurze Identitäten, keine Schaltung). Kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf). OP1 bis OP5 bleiben offen.
