# Licht als Vermittler, Zeit aus Stringbewegung (Erkundung, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Ein Gedankenexperiment des Autors ordnet Urknall und Zeit in den Hilbert-Shift-Turm ein: HS(0) schwingt ohne
umlaufene Fläche (zeitlos, stabil), HS(1) bringt den HC und die erste Ebene, HS(2) die erste Restdrehung (Holonomie) als Urknall. Das Bild ist
in sich stimmig, aber der **Drehsinn ist an keiner Stelle hergeleitet**. Herleitbar wären nur Schwelle und Betrag, und auch die nur mit einem
bestimmten Außenfeld. Zwei Rechnungen dazu: Ein Lichtsignal legt die Zeitrichtung τ in M fest und gibt T unter der Tachyon-Abbildung
(holomorphe Adjungierte) den Gegensinn (k247). Licht P erfüllt das Vermittler-Profil r30.7 nicht (scheitert an A4, A5).

Auftrag des Autors (Chat 24.11.2026): „können wir uns nochmal eine der frühesten ideen ansehen …, das licht als vermittler zwischen den beiden
sektoren“, danach das Gedankenexperiment in Schritten, „mach das mal alles“ (Anschlüsse) und „schreibe das mal so“. **Erkundung, nicht blind**:
Die Ergebnisse der Rechnungen standen vorher analytisch fest oder sind Standardphysik. Deshalb keine Vorab-Notiz und keine H-Nummer;
**H125 bleibt frei** (zuerst als Test zum Lichtsignal geplant, beim Entwurf als nicht blind erkannt). Vergeben: Skripte **k247–k249**.
Keine Runde (nur auf Entscheidung des Autors). Die Holonomie-Frage ΔΦ = γ_M·A (Anschluss c) läuft getrennt (k246).

Werkzeuge: Wolfram Language (exakt) für k247; Python (scipy, numpy) für k248 und k249. Qiskit nicht eingesetzt: Die Bargmann-Kontrolle als
Schaltung liegt aus H123/k244 vor, hier gibt es keinen neuen Zustand oder Messablauf. Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher
Auswahlablauf).

## Vorwissen geprüft
- **Die frühe Idee:** `v470/10_sphaera_and_physics.tex` um Z. 1289 (Federmodell: das Photon als masseloser Knoten, der zwischen Materie
  z⁻ = +β und Tachyon z⁻ = −β vermittelt; „c konstant als Gleichgewichtsknoten“; `thm:light-equil`); T3 (s > 0, s < 0, s = 0); v4.9.0-r19
  (P als Punkt p₊ = p₋ = ½, „supports the author's conjecture“); `v470/16_master_model.tex` (Higgs vermittelt zwischen Photon-Fixsektor und Masse).
- **Was daraus wurde:** r21/r22 (z⁻ = 0 ist meist R, P liegt am Horizont), r23 (keine endliche Kaskade führt zu P), Rückgang vom 6.11.
  (`qsc_back_to_basic_idea_2026_11_06.md`: Dualität verbindet M und T direkt, nicht über den Nullsektor), T9 großteils nicht tragfähig,
  H33 (e₇ ist B − L, nicht Photon-Achse), r30.7 (Vermittler-Profil; P nie geprüft).
- **OP1, Q1, Hopf-Lücke:** U1-Notiz `op1_u1_check_2026_11_16/` (M-Zählung = Helizitätsladung ±j entlang der Dualitätsachse), r24.4 (T zählt
  Querungen), H123 (Projektdateien; Oktantvorzeichen = Relation τε, Herkunft von τ offen), `hopf_gap_2026_11_23/` (k245).
- **Kreismodell:** `op3_string_length_exploration_2026_11_12.md`, `op3_string_relaxation_backward_2026_11_12.md` (nur Längen ℓ_i, keine
  Winkel; Attraktor nur bei wachsendem L).
- **Urknall:** `v4_10_0_r03/Erkundung_Randbedingung_Urknall.md` (G2, φ̇ = 0, T als Zeitspiegel), I1, I4.
- **Hilbert-Shift:** `v470/07_qam_infrastructure.tex` (def:qam-hilbert-shift-plan, first boundary shift, ass:v3360-r16-hc-activation-first-boundary),
  `v470/32_atlas_and_op_promotion.tex` (HS(0)–HS(6)).
- **Julia und zwei Sonden:** `op5_pairing_readout_2026_11_18/Julia_Frames.md`, `prop:triadic-two-probe`, bifokaler Monitor `v470/05`.
- Zurückgestellte Ideen: I1 (Auslöser 3, β_sym als Verhältnis zweier Zählungen) berührt; dem Autor bereits mit H123 vorgelegt.

## 1. Das Gedankenexperiment (Lesart, nicht gerechnet, außer wo vermerkt)
1. **Zeit als Holonomie.** Kehrt eine Schwingung nach n Schritten exakt ins Ausgangsbild zurück, ist keine Zeit vergangen. Zeit ist, was als
   Restdrehung bleibt. Mechanisches Gegenstück: geometrische Phase deformierbarer Körper (Shapere–Wilczek), Restdrehung ∝ umlaufene Fläche im
   Formraum. Das passt zur Form ΔΦ = γ_M·A der I1-Brücke vom 14.11. Umlaufsinn = Zeitrichtung.
2. **Restdrehung im Kreismodell.** Das Längenmodell vom 12.11. hatte keine Winkel. Eine bleibende Drehung δ ist die Brannen-Phase: drei gleich
   verteilte Punkte, gedreht und auf eine feste Achse projiziert; K = ⅔ für jedes δ. Die Ungleichheit der Massen kommt dann aus der Lage zur
   Achse, nicht aus ungleichen Strings.
3. **Hilbert-Shift-Turm.** Nach def:qam-hilbert-shift-plan verschiebt der Shift nur das Tag, nicht den mathematischen Inhalt (QAM über ZF). Lesart
   des Autors: HS(0) = Zustand vor dem Urknall, HS(1) erzeugt den HC (first boundary shift 0 → 1, Randwert ½), HS(2) = Urknall. Geometrisch:
   Ein Kanal erlaubt keine Fläche (zeitlos, stabil), zwei Kanäle die erste Ebene (der antisymmetrische Teil des HC ist dort der Drehgenerator ε),
   echte Holonomie aus reiner Formänderung braucht mindestens drei Dimensionen, also HS(2) (4 Kanäle, im Atlas „stabilisierter Orbit“).
4. **Auslöser.** Vakuumfluktuationen; selten ein tangentialer (ungerader) Stoß über die Lichtachse. Radiale Streckung ist gerade und dreht nie.
5. **Einfang (k249).** Julia-Abbildung F_c(w) = 1/conj(w² + c), c = −1 + iγ: Bei γ = 0 läuft der Zyklus −1 → ∞ → 0 auf der Achse (Fläche 0). Bei
   γ ≠ 0 gibt es einen anziehenden 3-Zyklus mit Fläche vom Vorzeichen von γ (±9,902754 bei γ = ±0,05; +1,717962 bei γ = 0,237533). Alle Startpunkte
   des Rasters (301 × 301 innen, 2000 bei |w| ≈ 1000) enden dort; eine Welle von außen wird eingefangen und übernimmt den Drehsinn.
6. **Strömungsbild.** Selbsterhaltend heißt Euler oder Suprafluid. Bester Kandidat: Kirchhoff-Ellipse (starr rotierend, bifokal); der
   Rankine-Kreis rotiert unsichtbar (≈ HS(0) → HS(1)). Mechanismus aus zufälligen Wellen: inverse Kaskade in 2D. Drehsinn = Netto-Zirkulation.
   In 3D Helizität = Drehsinn × Achsrichtung; mit Achse = Zeitrichtung ist das die Relation τε aus H123.
7. **Ansaugen.** Achsströmung nur mit Grenze (Bödewadt/Ekman) oder äußerer Streckung (Burgers); Kernunterdruck ∝ ρv², vorzeichenblind.
   EM-Analogie (Biot–Savart, Maxwells Ätherwirbel, Bjerknes) mit teils umgekehrten Vorzeichen; gleichsinnige Wirbel verschmelzen.
8. **Gegenwirbel.** Das Außenfeld (HS(0)) hat keine Netto-Zirkulation; nach Kelvin gehört zu +Γ ein −Γ. Das passt zu z⁻ = ±β, r21 und G2
   (T vor dem Urknall als Zeitspiegel von M). **Achtung:** Unter der Tachyon-Abbildung w ↦ iw (eine Drehung) hat T im Julia-Bild *denselben*
   Drehsinn; den Gegenwirbel liefert nur die Zeitumkehr z ↦ z̄ (r51/r81).
9. **Schwelle (k248).** Drei-Mulden-Modell I θ'' = −3K sin 3θ − η θ' + τ: Schwelle ω_c = 2√(K/I) (numerisch 2,0000000000), Verhältnis zur
   Pendelfrequenz ⅔ = 2/n bei n = 3 Mulden (Geometrie, nicht Koide). Rückhalt-Drehmoment nach Stewart–McCumber 4/(πQ) (0,0213 gegen 0,0212;
   0,0424 gegen 0,0424; 0,0868 gegen 0,0849 bei kleinem Q). Keine Zahl aus γ_M, γ_BI, γ_string oder β. Die Schwelle legen Eigenschaften des
   Außenfeldes fest: Muldentiefe K, Trägheit I, Dämpfung η, Fluktuationsspektrum, Netto-Drehmoment τ (Vorzeichen = Drehsinn), Dauer und Phase des Stoßes.
10. **Energiebilanz.** Bremsen allein treibt nicht an (Lenz; ein Induktionsmotor braucht ein rotierendes Feld, HS(0) hat keines). Tragfähig ist
    ein Durchfluss: Einstrom streckt den Wirbel (Burgers) und verstärkt die vorhandene Drehung; vorbeilaufende Wellen werden verstärkt und tragen
    Rotationsenergie nach außen (Superradianz, Penrose), das ist die „Rekuperation“ des Autors. Stationär entsteht eine Maschine zwischen Einstrom
    und Abstrahlung, kein Perpetuum mobile. Besseres Motorbild: Scheibendynamo (Bullard), Vorzeichen vom Saatfeld, Umkehrungen möglich. Im Bestand
    ist die Bilanz „M nimmt auf, T gibt ab“ strukturell angelegt (r21: C5_M + C5_T = 1; Maxwell-Abbildung energieerhaltend; L_T = −½X − V, H78/H79),
    für diesen Kreislauf aber nicht gerechnet.

## 2. Zeitrichtung τ über ein Lichtsignal (k247)
Setzung: Die drei Fenster der Oktant-Auslese (S123) werden von einem Lichtsignal mit Nullvektor k ausgelöst; τ := sign(k⁰).
- Unter eigentlichen orthochronen Lorentz-Transformationen ist τ invariant (Standard). In M ist τ damit frame-unabhängig festgelegt.
- Λ(iπ) auf k: (1, n) ↦ (−1, −n_x, n_y, n_z), τ kippt. Auf Spinoren: unitär S K S† gibt (1, n_x, −n_y, −n_z) (Drehung, τ bleibt), holomorph
  S K S gibt (−1, −n_x, n_y, n_z) wie Λ(iπ). Mit der holomorphen Adjungierten des Companion (H79) gilt τ_T = −τ_M.
- Die Bargmann-Invariante des Oktant-Tripels ist unter einer gemeinsamen unitären Abbildung fest (1/4 + i/4), umgekehrte Reihenfolge konjugiert sie.
  Mit τ_T = −τ_M liest T das entgegengesetzte Oktantvorzeichen.

Lesart: Das Licht legt τ fest und gibt T den Gegensinn, also das Gegenwirbel-Paar aus der Kinematik. ε wählt es nicht; das Vorzeichen des
Oktantschritts bleibt die Relation τε, jetzt mit physikalisch festgemachtem τ. Gesetzt bleibt, dass die Auslese von einem Lichtsignal ausgelöst wird.

## 3. P gegen das Vermittler-Profil r30.7
| Kriterium | P (b = 0, ρ = I/2) | Fundstelle |
|---|---|---|
| A1 eine Zahl | nur ½ bzw. γ_L = 2 über j + ½, nicht 1,8647 | r19, k245 |
| A2 eigener Zustand | erfüllt (kein endlicher Boost erreicht P); die Feldalgebra verbindet M und T aber direkt über die Dualität | r19.1, r21, Rückgang 6.11. |
| A3 stabil | verträglich (H74), legt γ_L nicht fest | r30.7 |
| A4 fünf Übersetzungen | nicht erfüllt: bei P ist β = 0, die Übersetzungen werden trivial; P fixiert die Bargmann-Phase nicht | r30.6, r30.9 (H114) |
| A5 Skala | nicht erfüllt (masselos) | – |

Ergebnis: kein Vermittler im Sinn von r30.7. Neu: Als Taktgeber der Zeitrichtung (Abschnitt 2) hat P eine Rolle, die das Profil nicht abfragt.

## Grenzen
- Alles Erkundung, nicht blind; Gedankenexperiment und Strömungsbezüge sind Lesarten aus Vorwissen, nicht gerechnet (außer k247–k249).
- Der Drehsinn (Vorzeichen von γ, Netto-Zirkulation, Helizität, ε) ist überall gesetzt. Die HS-Zuordnung ist eine Lesart (Spannung zwischen
  QAM-Definition „nur Tag“ und Atlas „Träger 2ⁿ“).
- Julia-Iteration ist keine Wellenausbreitung; die Zuordnung Iterationsschritt ↔ Zeit ist offen.
- OP1, OP3, OP5, Q1a offen; kein Guard berührt; H15, H46, H96, H102 unverändert.

## Mögliche nächste Schritte (nur auf Entscheidung)
- Holonomie ΔΦ = γ_M·A an einem konkreten Formzyklus (eigener Faden, k246).
- Bilanz „M nimmt auf, T gibt ab“ als Rechnung am Kirchhoff-/Burgers-Modell mit L_T = −½X − V.
- Ein blinder Test zur Lichtsignal-Auslese bräuchte eine Folgerung, deren Ausgang nicht vorher feststeht (dann H125 mit Vorab-Notiz).

## Dateien
`k247_tau_lichtsignal.wl` (Ausgabe `k247_out.txt`), `k248_drei_mulden_schwelle.py` (`k248_out.txt`), `k249_julia_zyklus.py` (`k249_out.txt`).
