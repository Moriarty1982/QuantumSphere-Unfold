# Hopf-Lücke als Nullpunkt der Fläche (Erkundung, nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** Setzt man in der Zählgleichung beider Frames statt der Flächeneigenwerte √(j(j+1)) das um den Nullpunkt
verschobene Spektrum j + ½ ein (Heisenberg als ħ/2), dann ist γ_L = γ_M/γ_T **exakt 2** und β_sym **exakt 1/√3**, also der Hopf-Wert aus
`rem:bsym-hopf-gap`. Die „Hopf-Lücke“ (1/√3 gegen 0,5494) ist in dieser Lesart der Unterschied zwischen dem halbklassischen Flächenspektrum
j + ½ und dem exakten √(j(j+1)). Die Daten (m_W, Ω_M) trifft nur das exakte Spektrum.

Auftrag des Autors (Chat 23.11.2026): „was passiert wenn du statt 1/2 mal die heisenberg undschärfe einsetzt?“, dann „halte das fest und überlege
dann was das heißen würde physikalisch“. Erkundung, **nicht blind**: Die Rechnung lief vor dieser Notiz, und die Zielwerte (Hopf-Wert, H98-Fenster)
waren bekannt. Deshalb keine Vorab-Notiz und keine H-Nummer; **H125 bleibt frei**. Vergeben: Skript **k245**. Keine Runde (eine spätere Runde
v4.10.0-r59 nur auf Entscheidung des Autors).

Werkzeuge: Wolfram Language (exakt; geschlossene Formen der geometrischen Reihen) und Python (unabhängige numerische Kontrolle aller Varianten).
Qiskit nicht eingesetzt: keine Schaltung, kein Zustand zu simulieren. Kein HDL-Vergleich (kein endlicher Auswahlablauf).

## Vorwissen geprüft
- `thm:symmetric-frame`, `thm:frame-offset`, `rem:bsym-hopf-gap` (`sources/research/parts/v470/10_sphaera_and_physics.tex`): β_sym aus γ_BI/γ_string;
  Hopf-Wert 1/√3 mit γ_L = 2 aus der ℤ/3-Bahn auf der runden S³.
- v4.8.0-r03, F11/F11a (`sources/research/parts/v480-post-release-layers.tex`): γ_string = ln 2/(π√3) ist der ABCK-Wert (nur j = ½), γ_BI = 0,2375 der
  DL/Meissner-Wert; beide sind Literaturwerte desselben Parameters.
- r63.1–r63.4 und v4.10.0-r09 (`notes/research/v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md`): Heisenberg schon als Robertson-Sättigung
  ΔJ_x ΔJ_y ≥ ½|m| (Prinzip P1, begründet das Gewicht 2), nicht als Flächenverschiebung.
- H98 (Sonderstellung des Regelpaars, Fenster Leptonen, m_W, Ω_M) und **H104** (`notes/research/predictions/Ergebnis_H104_Zaehlregel_Flaechenspektren.md`):
  Spektren √(j(j+1)), j + ½, j über 253 Regelpaare durchgezählt; die Zahl γ_L = 2 für das Paar „j + ½, beide wie heute“ war dort als einer von vielen
  Rasterpunkten enthalten, aber nicht mit dem Hopf-Wert in Verbindung gebracht.
- H123 (Projektdateien, noch nicht im Repo): andere Auslese, gleiche Zählgleichung; Kontrolle γ_M = 0,2375329580.

## Rechnung
Zählgleichung Σ_j g(j) e^{−2πγ a(j)} = 1; M: alle j ≥ ½ mit g = 2; T: nur j = ½ mit g = 2. Mit y = e^{−πγ}:

| Spektrum a(j) | M (alle j) | T (j = ½) | γ_L | β | β² |
|---|---|---|---|---|---|
| √(j(j+1)) (heute) | γ_M = 0,237533 (numerisch) | ln 2/(π√3) = 0,127384 | 1,864700 | 0,549406 | 0,301847 |
| j + ½ | 2y²/(1−y) = 1, y = ½, γ_M = ln 2/π | ln 2/(2π) | **2** | **1/√3** | **⅓** |
| j | 2y/(1−y) = 1, y = ⅓, γ_M = ln 3/π | ln 2/π | log₂ 3 = 1,584963 | 0,475704 | 0,226294 |

Weitere Lesarten (k245, nur Python): √j (nur der Unschärfeanteil) gibt 2,349 bzw. 1,523, wenn nur T wechselt; j/2 (Robertson-Schranke) gibt
dasselbe wie j, wenn beide Frames wechseln. Wechselt nur T und bleibt γ_M fest: j + ½ gibt 2,153, j gibt 1,077. Ausgaben: `k245_out.txt`,
`k245_hopf_gap_wolfram_out.txt`.

Abstand der Spektren: j + ½ − √(j(j+1)) = 1/(8j) − 1/(16j²) + …; bei j = ½ gleich 1 − √3/2 = 0,1340, also 13 % der kleinsten Fläche.

## Physikalische Lesart (ungeprüft)
1. **Drei Stufen derselben Fläche.** j ist die Länge des klassischen Drehimpulsvektors (keine Schwankung). j + ½ ist der halbklassische Wert mit
   Nullpunkt, wie n + ½ beim Oszillator (Bohr–Sommerfeld mit Maslov- bzw. Langer-Korrektur). √(j(j+1)) ist der exakte Quantenwert: j(j+1) = j² + j,
   und der Zusatz j ist die Querunschärfe ΔJ_x² + ΔJ_y² = j des Zustands m = ±j. γ_L wächst mit dem Spektrum: 1,585 < 1,865 < 2.
2. **Hopf = halbklassisch.** Die Hopf-Rechnung setzt einen Punkt auf der runden S³ in gleichen Winkelabständen, also eine klassische
   Spinorgeometrie. Dass sie mit dem halbklassischen Spektrum j + ½ exakt übereinstimmt, liest die Hopf-Lücke als **Quantenkorrektur**: Die
   Geometrie gibt 1/√3, die Quantenschwankung der kleinsten Punktierung (Spin ½) zieht β auf 0,549. Die Korrektur sitzt fast ganz bei T, weil T
   nur j = ½ zählt, wo der Abstand am größten ist.
3. **Warum genau 2.** Mit Nullpunkt bildet M einen Oszillatorturm (geometrische Reihe, Gewicht halbiert sich je Stufe, y = ½), T einen einzigen
   Zweizustand (ein Bit). Beide Frames tragen ln 2 je Schritt; M löst aber Flächenschritte ½ auf, T nur die ganze erste Stufe 1. γ_L = 2 ist das
   Verhältnis dieser kleinsten Schritte. Ohne Nullpunkt (Spektrum j) wird daraus log₂ 3: M zählt dann Trits (y = ⅓), T Bits.
4. **Heisenberg als Faktor fällt heraus.** Wechseln beide Frames, hängt γ_L nur von der Form des Spektrums ab, nicht von seinem Maßstab
   (j und j/2 geben dasselbe). Wirkung hat die Unschärfe nur als additiver Nullpunkt.

## Grenzen
- Nicht blind, nachträglich: Der Hopf-Wert war bekannt; die Übereinstimmung ist exakt, aber gesucht.
- Mit j + ½ in beiden Frames sind die Daten verfehlt: β² = ⅓ gegen Ω_M ≈ 0,30, γ_L = 2 gegen das m_W-Fenster bei 1,8647 (etwa ± 0,003). Die
  Lesart erklärt die Lücke, ersetzt aber nicht das exakte Spektrum.
- Der Kern von OP1 bleibt: warum M alle Spins und T nur j = ½ zählt. Ebenso ungeprüft: dass die Hopf-Konstruktion genau dem halbklassischen
  Grenzfall der LQG-Fläche entspricht (bisher nur Zahlengleichheit).
- Kein Guard berührt; OP1 offen. H15, H46, H96, H102 unverändert.

## Mögliche nächste Schritte (nur auf Entscheidung)
- Prüfen, ob die Hopf-Bahn (ℤ/3 auf S³) als halbklassischer Grenzfall des Flächenoperators herleitbar ist; dann wäre die Lücke eine Folge, keine
  Zahlengleichheit.
- Eine blinde Folgerung suchen, die j + ½ und √(j(j+1)) an anderer Stelle unterscheidet (dann H125 mit Vorab-Notiz).
