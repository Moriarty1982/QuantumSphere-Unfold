# OP3: r38 neu gelesen, und eine Generation je Frame-Abbildung

15. November 2026, Claude Opus. **Erkundung, nicht blind** (Koide 2/3, die Zahl drei und die Phase π/4 des Oktanten waren
bekannt). Auftrag des Autors: „prüfe r38 nochmal, könnte noch auf alten annahmen basieren“, nach dem Vorschlag, die
Generationen als Eigenzustände der Frame-Abbildungen zu lesen. Keine H-Nummer, kein CT-Eintrag, Guards unverändert.
Skript `frame_map_states.py`, Ausgabe `run/frame_map_states_stdout.txt`.

## Vorwissen geprüft
- **r38** (`sources/research/parts/v490-post-release-layers.tex`, ab Zeile 5220, Test H23): Frame-Triole als Transposition
  ρ der drei Triality-Slots von O³; Lesart Photon = Vektor-Slot (fest), Materie und Tachyon = die beiden Spinor-Slots.
  Offener Punkt 5: Auf einer Ebene können dieselben drei Slots nicht Frames und Generationen (r37) zugleich tragen.
  Punkt 6: M ↔ T wäre ein Chiralitätswechsel (Spur, nicht gerechnet).
- **r39** trennt beide Rollen nach Zoomstufen, **r41** (H26) übernimmt das („the zoom levels separate frames from
  generations“), **H29** (r44) liest die Massenaufspaltung als Brechung von ρ, „the frame triole of v4.9.0-r38“.
- **r51** (H35): Die drei Involutionen des Dubletts wirken über den C-Faktor des Dixon-Speichers, Tachyon-Abbildung
  z ↦ iz (σ_y, berichtigt in r28), Zeitumkehr z ↦ z̄ (σ_z, Tausch von Kompensator- und Partnerport), J_B = R∘T (σ_x).
  r51.1(a): Die Tachyon-Abbildung lässt jeden Sektor fest, also auch Ladung und Chiralität; die Ports und damit die
  Chiralitäten tauscht die Zeitumkehr. r51 berichtigt deshalb die Frame-Zeilen von r41, r43 und r47–r49, **nicht aber r38**.
- **r03/r04, r17–r19:** Die Frames liegen auf der Stokes-Kugel des Dubletts (E, B): Materie und Tachyon sind die beiden
  voll polarisierten Enden einer Achse, das Photon ist die unpolarisierte Mitte (p₊ = p₋ = ½).
- **v4.10.0-r14.4(d)** (eigene Runde) zitiert r38 weiter: „the frame triole is a transposition“.

## Teil A: Worauf r38 beruht
| Annahme in r38 | Späterer Stand | Folge |
|---|---|---|
| Rechnung reell oktonisch, „without the C factor“ | r51 legt die Frame-Abbildungen gerade in den C-Faktor | r38 sieht die Frame-Abbildungen nicht |
| Frames = Triality-Slots (Photon Vektor-, M und T Spinor-Slots) | Frames = Punkte bzw. Abbildungen des Dubletts (r04, r19, r51) | Lesart (2) von r38 ist ein älteres Bild |
| M ↔ T tauscht die Spinor-Slots, also die Chiralität (Punkt 6, Register) | Die Tachyon-Abbildung lässt die Chiralität fest; der Tausch ist die Zeitumkehr (r51.1(a)) | **Widerspruch**, von r51 nicht mit berichtigt |
| Generationen = Z₃-Bahn der Slots (r37) | Generationen am Platz des Spins (r14.4) bzw. in Im H (r33) | auch die zweite Rolle ist weitergewandert |

**Was gültig bleibt:** Theoremlet r38.1(a)–(e) ist reine Algebra auf so(8)³ (ρ äußerer Automorphismus der Ordnung 2,
Fixalgebra so(7), S₃ aus τ und ρ, g₂ ρ-fest). Daran ändert sich nichts. Betroffen ist nur die Zuordnung von Frames zu Slots.

**Folgen für spätere Lesarten (nicht für deren Mathematik):**
- Der offene Punkt 5 von r38 entsteht nur, wenn Frames und Generationen auf denselben Slots sitzen. Wirken die Frames über
  den C-Faktor, liegen beide Rollen auf **verschiedenen Tensorfaktoren** von C ⊗ H ⊗ O. Der Konflikt entfällt in seiner
  ursprünglichen Form; die Zoomtrennung von r39 wird dafür nicht gebraucht (bleibt als Modellbefund bestehen).
- H29: „Massenaufspaltung = Brechung der Frame-Spiegelung ρ“. Die Brannen-Form aus τ-symmetrischer, ρ-gebrochener
  Kopplung bleibt richtig; nur der Name „Frame“-Spiegelung für ρ ist nicht mehr gedeckt.
- r38 Punkt 6 und die Registerzeile „chirality: M ↔ T as exchange of the two spinor slots“ widersprechen r51.1(a).
  Nach Append-only braucht das eine **Berichtigung in einer neuen Runde** (Vorschlag: v4.10.0-r15), wie r51 sie für
  r41–r49 gemacht hat.

## Teil B: Eine Generation je Frame-Abbildung
Da r38 nicht mehr im Weg steht, lässt sich die Lesart prüfen: **Jede Generation ist ein Eigenzustand je einer der drei
Frame-Abbildungen T, J_B, R des Dubletts.** Ergebnisse (exakt):
1. Die Eigenbasen von T (σ_z), J_B (σ_x) und R sind paarweise unverzerrt, |⟨u|v⟩|² = ½. R ist reell eine Drehung mit
   R² = −1 und hat die Eigenwerte ±i; seine Eigenlinien sind die von σ_y, also komplex (Teil der Lesart: der C-Faktor
   wird gebraucht).
2. Jede der 8 Wahlen gibt K = 2/3 und Phase ±π/4. Das Vorzeichen ist die Orientierung des Tripels auf der Stokes-Kugel
   (det der Bloch-Vektoren = ±1).
3. **Frame-Wechsel M ↔ T (R, unitär):** R hält seinen eigenen Eigenzustand fest und schickt die beiden anderen auf ihre
   Partner; das Tripel dreht sich um π um die R-Achse, Phase **+π/4 bleibt**, K bleibt. Koide und die Orientierung sind
   frame-unabhängig zwischen M und T, wie die Ladungen in r51.
4. **Antiunitäre Konjugation** (z ↦ z̄ als komplexe Konjugation des Zustands) kippt nur den R-Eigenzustand und
   **dreht das Vorzeichen der Phase** auf −π/4. Das Vorzeichen der Koide-Phase gehört also zur Zeitumkehr, nicht zum
   Frame-Wechsel.

## Einordnung
- Die Lesart vereint die zwei gesetzten Prinzipien der Komplementaritätsnotiz
  (`../op3_koide_complementarity_2026_11_15/README.md`): „ein Zustand je Basis“ = eine Generation je Frame-Abbildung;
  „vollständiger Satz“ = alle drei Involutionen des Dubletts. Die Zahl drei der Generationen wäre die Zahl dieser Abbildungen.
- Sie passt zum Stokes-Bild von r04/r19: Die Frames M, T sind die Pole *einer* Achse (Überlappung 0), die Generationen je
  ein Pol aus *drei* Achsen (Überlappung ½); das Photon ist die Mitte.
- Neue Doppelbelegung? Frames und Generationen leben jetzt beide auf dem Dublett, aber in verschiedenen Rollen: die Frames
  als Abbildungen bzw. Pole, die Generationen als Eigenzustände über alle drei Achsen. Ob das physikalisch trägt, also ob
  der Generationsindex wirklich auf dem Frame-Dublett sitzt und nicht auf einer Kopie, ist **nicht gezeigt**.

## Annahmen und Grenzen
- **Nicht blind;** keine neue Zahl. Die Lesart setzt r33 (C-Faktor = Amplitudenebene) und r51 voraus.
- Die Biegung zu den echten Massen (φ = 2/3 statt π/4) bleibt beim Kern (γ_M, OP1); hier entsteht nur der flache Oktant.
- Ob die Zeitumkehr auf dem Generationsdublett linear (σ_z) oder antilinear wirkt, entscheidet über das Vorzeichen der
  Phase; r02 verlangt für eine involutive M ↔ T-Abbildung in drei komplexen Dimensionen Antilinearität. Offen.
- Ladungsneutralität weiter unter CT-003.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: Sitzt der Generationsindex auf dem Frame-Dublett? Nein, nicht auf C ⊗ O
Auftrag des Autors: „weiter“. Geprüft wird der offene Punkt aus Teil B mit den Operatoren von r51 selbst
(`notes/research/v4_10_0_r48_r55/llm/k91_test_h35.py`): R ist dort die C-lineare Multiplikation mit i, T die komplexe
Konjugation (antilinear), J_B = R∘T. Skript `on_c_tensor_o.py`, Ausgabe `run/on_c_tensor_o_stdout.txt`.

1. **R ist auf C ⊗ O ein Skalar.** Jeder Zustand ist R-Eigenzustand; R zeichnet keine Basis aus.
2. **T und J_B haben dieselben Eigenstrahlen.** Für ein antilineares K ist Kv = λv genau für v = Phase · reell, bei T wie
   bei J_B (200 von 200 Stichproben). Ihre Überlappung ist 1, nicht ½.
3. **Kein T- oder J_B-Eigenzustand hat eine bestimmte Ladung oder Chiralität.** T bildet P_(l,r) auf P_(−l,−r) ab
   (r51.1(a)); ein reeller Zustand hat deshalb in beiden Sektoren gleiches Gewicht, und ⟨Q⟩ = ½ für alle (Abweichung
   höchstens 2·10⁻¹⁶).
4. Die drei gegenseitig unverzerrten Basen gibt es nur auf der **komplexifizierten Amplitudenebene z** (dem reellen
   2-dimensionalen Faktor), nicht unter den Materiezuständen von C ⊗ O. Die Ports (Eigenräume von iL_e7, je Dimension 4)
   werden von der Konjugation vertauscht; auf ihnen ist R ebenfalls skalar.

**Folge für r15.5:** Die Lesart „eine Generation je Frame-Abbildung“ trägt auf den Zuständen des Bestands nicht. Zwei der
drei „Generationen“ hätten keine bestimmte Ladung (Ladung und Ladungskonjugat gemischt), und T und J_B lieferten gar keine
verschiedenen Basen. Sie lässt sich nur auf einer **zusätzlichen Kopie** der Amplitudenebene halten, und damit fällt sie auf
r15.4 zurück: ein gesetztes Qubit mit seinen drei Basen, ohne Quelle im Bestand. Die beiden Prinzipien der
Komplementarität bleiben gesetzt. Die Mathematik von r15.5(a)–(c) ist richtig, aber nur auf der Ebene z.

Das ist eine Einschränkung der Lesart, nicht eine Berichtigung einer Rechnung. Sie gehört in die nächste Runde (Append-only).
