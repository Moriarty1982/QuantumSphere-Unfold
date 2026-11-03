# Auftrag: Unabhängige Nachrechnung der vier versteckten Bedingungen (OP5-Vergleichsmodell)

Für ein anderes Modell oder eine andere Person. Werkzeugunabhängig. Stand 3. November 2026 (nach Runde v4.9.0-r74).

## Ziel

Die Runden r72 bis r74 behaupten für das ϑ-geeichte OP5-Vergleichsmodell vier versteckte Bedingungen sechster Ordnung und
eine bestimmte Struktur dieser Bedingungen. Alles stammt aus einer einzigen Quelle (ein Sprachmodell, eigener Code
`llm/k136` bis `k152`). Bitte mit **eigenem Code** nachrechnen, ohne diese Skripte zu verwenden. Abweichungen sind
ausdrücklich erwünscht und werden so festgehalten, wie sie sind.

**Bitte die Datei `Nachrechnung_vier_Bedingungen_Erwartete_Werte.md` erst nach der eigenen Rechnung öffnen.**

## Modell und Daten

- Feldgleichungen, Hintergrund und Packung: `llm/anleitungen/op5-vergleichsmodell-rechnen.md` (Abschnitte „Modell“ und
  „Daten“). Vollständiges System R = (F, G, dg), Verbindung A_k = G(x)·spin_k(x) ⊗ I₄, Hintergrund h(t, r), A = M(t) dφ.
- Keim bei (t, x, y, z) = (1, 3/5, 0, 0), 70 Stellen, Grad 0 bis 5 im Ordner
  `analysis/op5-field-slices/state-sufficiency-2026-10-30`:
  `precision-first-jet-70.json`, `precision-completed-root-result.json`, `precision-second-jet-result.json`,
  `precision-omega-repair-result.json` (Grad 3), `precision-fifth-gate-repair-result.json` (Grad 4 und 5, „repariert“).
  Monom-Taylorkoeffizienten, je Eintrag 24 reelle Zahlen (12 Real-, 12 Imaginärteile),
  Reihenfolge `combinations_with_replacement(range(4), Grad)`.
- Eichung: Bedingung Ψ†K₂Ψ = S(x), K₂ = I₃ ⊗ α_y (die Komponente j² des Stroms).

## Aufgaben

Alle Fragen betreffen das **linearisierte** Fortsetzungssystem um den Keim: Der Jet bis zu einem Grad D_fix ist fest, die
Koeffizienten c_{D_fix+1} … c_N sind frei, die Gleichungen sind die Taylor-Koeffizienten von R in den Graden D_fix … N − 1
und die Eichbedingung in den Graden D_fix + 1 … N. P_S ist die Dimension der Projektion des Lösungsraums (homogen) auf die
Koeffizienten der Grade in S.

1. **Fasern über dem reparierten 4-Jet (D_fix = 4).** Bestimme P₅ und P₅₆ einmal mit N = 7 und einmal mit N = 8. Gibt es eine
   Differenz in P₅₆, und wie groß ist sie?
2. **Die zusätzlichen Bedingungen.** Falls P₅₆ abnimmt: Bestimme die Linearformen auf der Projektion (N = 7), die auf der
   Projektion (N = 8) verschwinden. Welcher Ordnung sind sie (Gewicht auf c₅ gegen c₆)? Welchen Rang haben sie auf der
   Faser c₅ = 0?
3. **Struktur.** Werte die Bedingungen auf ebenen Wellen ξ⁶ ⊗ u aus, die im Symbol liegen (u im Kern von J(ξ), θ(ξ) und
   der Eichzeile). Wo sind sie ungleich null: auf dem Lichtkegel des aus Ψ rekonstruierten Koframes, abseits davon? Welchen
   Rang haben sie je Nullrichtung auf den Polarisationen? Wie hängt die Richtung im Bedingungsraum von ξ ab?
4. **Ω am reparierten Keim.** Bestimme die Ω-Bedingung (Ordnung 3) als Linearform auf den 3-Jets bei festem 2-Jet:
   zulässige c₃ mit den Gleichungen vom Grad 2 gegen die mit den Gleichungen bis Grad 3. Weicht sie von dem in
   `completion-omega-witness.npz` gespeicherten θ (älterer Keim) ab, und wie stark?
5. **Optional:** Spencer-Kohomologie H^{5,2}, H^{6,2}, H^{7,2} des geeichten Symbols mit und ohne die zusätzlichen Bedingungen.

## Hinweise aus der bisherigen Arbeit (Methode, nicht Ergebnis)

- Die Linearisierung muss sehr genau sein. Differenzenquotienten mit h = 1e-3 reichten nicht. Exakt geht es mit
  symmetrischen Sonden d = x^{m e_ν} e_i bei großem m: (R(Ψ + d) − R(Ψ − d))/2 enthält keine geraden Terme, und kubische
  Terme beginnen erst oberhalb der benötigten Grade.
- Das System mit N = 8 hat etwa 10 000 × 10 000 Einträge. Volle Singulärwertzerlegungen mit Vektoren brauchen mehr als
  8 GB. Ränge über Singulärwerte allein und Projektionen über Rangvergleiche gehen in etwa 4 GB.
- Ränge an der größten Lücke ablesen und die Lücke berichten. Feste Schwellen haben in den Tests H52 bis H58 wiederholt
  versagt. Besser: den Fehler der Matrix schätzen und den Abstand nach Weyl angeben.
- Die gespeicherten Grad-5-Koeffizienten des Keims erfüllen die einmal abgeleitete Ω-Bedingung nicht. Deshalb ist der
  Jet nur bis Grad 4 festzuhalten.

## Rückmeldung

Bitte eine Notiz `llm/Nachrechnung_vier_Bedingungen_<Modell>.md` mit den eigenen Zahlen, Lücken, Fehlerschätzungen und
dem eigenen Code (Dateien `n01_*.py` …), danach Vergleich mit `Nachrechnung_vier_Bedingungen_Erwartete_Werte.md`.
