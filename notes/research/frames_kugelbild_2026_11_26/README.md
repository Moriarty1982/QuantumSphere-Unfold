# Frames der Konvention F als Bild auf der Zustandskugel (Erkundung, nicht blind, 26.11.2026)

Auftrag des Autors (26.11.2026): die Frames und was in ihnen vorliegt als gewöhnliche 3D-Grafik, bei Bedarf in Teilbildern.
Keine H- und keine k-Nummer, keine Runde, kein Guard berührt. β_sym ist eingesetzt (OP1 offen).

## Was gezeichnet ist
- **A** Halbkugel der Feldzustände mit R, M, P, T, dem Schub-Meridian und den drei Abbildungen D, J_B, ϑ.
- **B** Schnitt durch die Meridianebene mit Rapiditätsmarken und Portgewichten.
- **C** Je Frame: Feldvektoren eines Vertreters mit E·B = 0, Schwingungsellipse (Lesart k297), Portgewichte.

Dateien: `frames_A_kugel_*`, `frames_B_schnitt_*`, `frames_C_je_frame_*`, `frames_gesamt_*` (je `de` und `en`, PDF und PNG).
Aufruf: `python frames_kugelbild.py --lang de|en [--out ORDNER]`. Ausgabe der Kontrollrechnung: `kontrolle_out.txt`.

## Worauf die Lage der Punkte beruht
Physik-Artikel Abschnitt 3 (Gl. A-gram, A-disk): b = (Re s, Im s)/(2u) füllt eine **Scheibe**, weil G reell symmetrisch ist.
Aus |b|² = 1 − det G/u² und det G = |E×B|² folgt b₁² + b₂² + b₃² = 1 mit b₃ = |E×B|/u ≥ 0 (Kontrolle 1). Jeder Feldzustand
ist damit ein Punkt einer Halbkugel, und die Scheibe der Konvention F ist ihr Schatten. b₃ ist der Anteil des Energieflusses.

- R: b₁ = 1, b₃ = 0 (Pol). P: b = 0, b₃ = 1 (auf dem Äquator b₁ = 0, lichtartig).
- Ein Schub der Rapidität η quer zum Feld führt R auf b₁ = sech 2η, b₃ = tanh 2η (Kontrolle 2). Bei η = ε = artanh β_sym ist
  b₁ = 1/γ_L und p₊ = 1/(1 + x): das ist M (Kontrolle 3; r24.3, H164, r66). Winkel vom Pol 57,57° (= 2α aus H164).
  Im Vertreter „reines E-Feld“ ist dann |B|/|E| = β_sym.
- T = D(M): b ↦ −b bei gleichem b₃, also die halbe Drehung um die b₃-Achse. J_B kehrt b₁ um, ϑ kehrt b₂ um (Prop. A-maps).
  Auf dem gezeichneten Meridian (b₂ = 0) wirken D und J_B gleich.

Abweichung vom ersten Vorschlag im Projektchat: Die Punkte liegen nicht auf einer vollen Poincaré-Kugel, sondern auf einer
Halbkugel, und M und T liegen auf demselben Meridian wie R und P.

## Offene Stelle (nicht aufgelöst)
r69.4 nennt für M zugleich die Portgewichte 1 : x (76,8 %) und die Ellipse aus k297 mit b/a = μ = x (Achsen γ_L : 1). Liest man
a und b als Amplituden zweier Ports, dann trüge der größere Port 1/(1 + x²) = 91,65 % (so steht es in k297) und der Stokes-Anteil
wäre 0,8330 statt 1/γ_L = 0,5363 (Kontrolle 4). Beides passt nur zusammen, wenn die Ellipse als **Form** gelesen wird:
kleine/große Achse = (1 − x)/(1 + x) = 1/γ_L = b₁(M). So ist sie in Teilbild C gezeichnet. Ob die Ports der Konvention F und
die zwei gegenläufigen Anteile aus k297 dasselbe sind, ist damit nicht entschieden.

## Grenzen
Lesart und Darstellung, kein neuer Befund mit Kriterium. Die Gleichsetzung „Portgewichte = Anteile von E² und B²“ gilt für den
gezeichneten Vertreter (E·B = 0, Eigenbasis von ρ). Die HS-Stufen sind nicht dargestellt. Werkzeug: sympy (exakt);
Wolfram und Qiskit nicht eingesetzt (vier kurze Identitäten, keine Schaltung). OP1 bis OP5 bleiben offen.
