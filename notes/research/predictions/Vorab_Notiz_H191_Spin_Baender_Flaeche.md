# Vorab-Notiz H191: Entsteht in einer Schleife über Bänder verschiedener Spins die Casimir-Fläche √(j(j+1)), ohne dass sie eingegeben wird?

**Stand:** 2026-11-27, vor der Rechnung festgelegt und vor dem ersten Lauf des Test-Bands committet. Auftrag des Autors vom 27.11.2026, 08:12 UTC
(„ja, mach das aber ziehe erst die maschine nach …“). Skript **k397** (Python; die Rechnung läuft auf der Maschine `qam/examples/coprocessor/stufe2/qtape.py`,
Commit 4bc624c und folgender Randfall-Zusatz; Bausteine dort gegen Qiskit geprüft) und **k397b** (Wolfram: Zielprofile exakt, unabhängige Nachrechnung
der stationären Verteilung für einen Gitterpunkt). Werkzeugwahl: Qiskit für die Bausteine (explizite Qubit-Zustände), Wolfram für die exakten
Profile und die Gegenprobe. Kein HDL/MMA-Vergleich: `RUN_TAPE` und die SystemVerilog-Steuerung werden nicht geändert. Kein Guard wird berührt.

## Vorwissen geprüft
- **r67:** Zählregel als Postulat, Σ_{k≥1} 2^(1 − γ a_k) = 1 mit a_k = √(k(k+2)/3), k = 2j. Der Grund für die Casimir-Fläche ist offen.
- **H165 (k356, widerlegt)** und `notes/research/op1_herkunft_beta_sym_h165/Sichtung_Herleitungsversuche.md` (37 Versuche): keine Herleitung.
  Schließungssummen über Überlappe kohärenter Zustände wurden dort geprüft; eine **Dynamik über Bänder mit Clebsch-Gordan-Übergängen** nicht.
- **k245:** mit j + ½ wird γ = 2 exakt. **`op1_readout_frequency`:** der Nebenwert 2^(1−γ_L) = 0,549161 war schon bekannt (in k396 als
  „nachträglich“ erneut gefunden; das war also kein neuer Fund).
- **k395, k396 (27.11.):** Schleife L3 hat den Fixpunkt b = ½; 1/γ_L − ½ ist der mittlere Flächenüberschuss der Spins j ≥ 1; zwei gleiche gekoppelte
  Schleifen bleiben bei ½.
- **r28, r70:** Runde aus Drehung, HC als Messung entlang σ_x, Austausch mit einem Band im Zustand |+⟩.

## Suchrichtung (Rückwärtssuche)
Ziel ist nicht eine Zahl, sondern eine **Form**: In der Zählregel ist das Gewicht von Band k proportional zu 2^(−γ a_k). Für die stationäre
Verteilung p_k einer Schleife heißt das: d_k := ln(p_k/p_{k+1}) = γ ln 2 · (a_{k+1} − a_k). Das Profil r_k := d_k/d_∞ ist frei von γ und von jeder
Skala. Notwendig für „Casimir“: r_k = √3 (√((k+1)(k+3)/3) − √(k(k+2)/3)) = 1,0964; 1,0446; 1,0260; 1,0170 (k = 1..4). Notwendig für die
glatte Fläche j + ½: r_k = 1 für alle k. Eine Schleife, deren Profil von ihren Stellgrößen abhängt, liefert keine Fläche.

## Modell (gesetzt)
Zustand: Bänder k = 0, 1, 2, …; Band k trägt den Spin j = k/2. Eine Runde auf dem Band der Maschine:

    ROT alpha      Drehung um y (Blochwinkel 2 alpha)
    HC             S_x messen, Ergebnis verwerfen
    ADD mu         mit Gewicht mu ein frisches Qubit |+> ankoppeln, Gesamtspin messen: k -> k+1 oder k-1 (Clebsch-Gordan)
    DROP lam       mit Gewicht lam ein Qubit abgeben: k -> k-1

Start: Band 1, Zustand |+⟩. KMAX 60. Stationär heißt: Änderung aller p_k unter 10⁻¹² zwischen N und 2N Runden.
Gesetzt sind damit: die Reihenfolge der vier Schritte, das Bezugsband |+⟩, die kollektive HC-Messung (S_x des ganzen Bands), und dass Auf- und Abbau
je ein Qubit betreffen. Nichts davon ist hergeleitet. Die Fläche a_k wird nirgends eingegeben.

**Gitter (vorab festgelegt):** α ∈ {π/6, π/4, π/3}; (μ, λ) ∈ {(0,25; 0,5), (0,5; 1,0), (0,2; 0,6), (0,4; 0,6)}; zwölf Punkte.
d_∞ := Mittel von d_k über k = 12..16 (falls dort p_k > 10⁻¹³, sonst die letzten fünf Bänder über dieser Schwelle).

## Aussagen und Kriterien
- **H191a (nicht blind, Kontrolle):** Für α = 0 bleibt der Zustand voll entlang x polarisiert; ADD führt dann immer nach oben, und die Verteilung ist
  exakt geometrisch (r_k = 1 für k ≥ 1). Bestätigt, wenn |r_k − 1| < 10⁻⁶ für k = 1..8 an allen vier (μ, λ). Das ist die glatte Fläche j + ½ als
  Vergleichsfall der Maschine.
- **H191b (Test):** Mit Drehung und HC entsteht das Casimir-Profil. **Bestätigt**, wenn an allen zwölf Gitterpunkten |r_k − r_k^Casimir| ≤ 0,015 für
  k = 1, 2, 3, 4. **Teilweise**, wenn das an mindestens einem, aber nicht an allen Gitterpunkten gilt (dann ist die Form eine Frage der Stellgrößen,
  keine Fläche). **Widerlegt**, wenn es an keinem Gitterpunkt gilt.
- **H191c (Test, Gegenstück):** Das Profil bleibt glatt, |r_k − 1| ≤ 0,015 für k = 1..4 an allen zwölf Punkten. Gleiche Abstufung.
- **H191d (ohne Urteil, Bericht):** Existiert überhaupt ein geometrischer Schwanz (d_k konvergiert), und hängt d_∞ von α ab? Berichtet wird das
  volle Profil r_1..r_8 je Gitterpunkt, dazu p_0 und p_1.

Zufallstreffer: Die Fenster ±0,015 um zwei feste Profile über vier k sind eng; ein Treffer an allen zwölf Punkten ist durch Zufall nicht zu
erwarten. Ein Treffer an einem einzelnen Punkt wäre bei zwölf Versuchen nicht aussagekräftig und zählt deshalb nur als „teilweise“.

## Vorab offengelegt
- Meine Erwartung: **H191b und H191c beide widerlegt.** Die Clebsch-Gordan-Wahrscheinlichkeiten enthalten Faktoren wie (j+1)/(2j+1), deren
  Korrekturen mit 1/k abfallen, während das Casimir-Profil mit 1/k² gegen 1 geht. Wahrscheinlich hängt das Profil von α und (μ, λ) ab.
- Die Fläche √(j(j+1)) steht in der Maschine als Eigenwert von S² zur Verfügung (jede Spin-Algebra hat ihn). Der Test fragt, ob die **Dynamik**
  ihn als Gewicht der Bänder benutzt, nicht ob er existiert.
- Kein Bezug zu Messdaten; es wird keine Zahl des Modells geprüft.

## Danach, ohne Urteil (Erkundung k398)
Primzahl-Rauschen (`NOISE alpha prime_gap eps`) auf der Schleife L3 und auf einem Gitterpunkt dieser Schleife, verglichen mit Zufallsrauschen
gleicher Streuung: Verschiebt es Fixpunkt oder Profil? Einordnung der Riemann-Arbeiten und des Vergleichs mit RSA/ElGamal als Notiz.

## Bilanz der Setzungen (vor der Rechnung)
| Größe | Status |
|---|---|
| Rundenschritte, Reihenfolge, Bezugsband |+⟩, kollektiver HC | gesetzt |
| Gitter α, μ, λ; Schwelle 0,015; Bänder für d_∞ | gesetzt, vorab |
| Zielprofile (Casimir, glatt) | aus r67 und k245 |
| Fläche a_k | **nicht** eingegeben; wird aus p_k abgelesen |
