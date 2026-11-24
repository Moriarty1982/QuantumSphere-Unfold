# Was verlangen drei Generationen rückwärts vom Turm? (Erkundung k273, nicht blind, 24.11.2026)

**Ergebnis in einem Satz:** Die beobachtete CP-Verletzung mit genau einer Phase verlangt eine Generationsebene mit einem
invarianten ε_ijk. Ein echtes Kreuzprodukt gibt es im Turm nur auf Im ℍ (3) und Im 𝕆 (7), und ε_ijk gibt es nur auf Im ℍ. Die
Generationen müssen deshalb eine **zusätzliche HS(2)-Stufe** sein, die **als Vektor** wirkt, also über ihre Automorphismen SO(3) und
nicht über die Multiplikation. Der Turm selbst liefert über der Farbstufe nur Clifford-Achsen (e₈, e₁₆, e₃₂). Diese tragen
Ladungsuniversalität, wirken aber als Spin ½, also als Dublett mit zwei Generationen. Das ist die Spannung aus dem Bestand
(Spin ½ gegen Spin 1, „Rollentausch“) aus der Rückwärtsrichtung gesehen.

Auftrag (Autor, 24.11.2026, über den Koordinator): nach der Rückwärtsrechnung k270–k272 als Nächstes die Frage, was drei Generationen
verlangen. **Erkundung, nicht blind:** Kobayashi–Maskawa (Phasenzahl), Jarlskog (J·εε), Kreuzprodukte nur in 3 und 7 Dimensionen
(Eckmann/Massey) und die Clifford-Darstellung sind Lehrbuch. Neu ist nur die Einordnung in den Turm. Skripte **k273, k273b**.

Werkzeuge: Python (numpy, scipy) für alle Teile (k273); Wolfram Language exakt für J, die 2×2-Aussage und die εε-Identität in der
Standardparametrisierung (k273b). Qiskit nicht eingesetzt.

## Vorwissen geprüft
- r12/r13, k255 (Kopienbasis, Koide aus exp(uπ/4), Kopienladungen vertauschen nicht), k256 (Mischmuster aus S₃ nur bekannt),
  H126 (#282, nicht prüfbar), H37 (Triality-Kopplung verboten), H19e (Ladung auf drei Plätzen von (Im ℍ)⊗ℂ⊗𝕆 gleich, K77.3),
  Forschungsstand „Rollentausch“ (r33-Generationstripel = Vektor Im ℍ unter Konjugation, H_n = Spin-½-Dublett; Levi-Civita-Tripel auf
  Im ℍ bricht dort die Ladung), op3-Notiz zu ℂ⊗𝕊 (zwei Generationen), Gesamtbild T5/T7 (kein Verbot einer vierten Generation).
- k270: N_c = 3 bei 𝕆; k254: Radon–Hurwitz-Achsen.

## Ergebnisse (k273, k273b)
1. **Warum mindestens drei.** Physikalische CP-Phasen: (N − 1)(N − 2)/2 = 0, 1, 3, 6 für N = 2 … 5. Für N = 2 ist
   Im(V₁₁V₂₂V₁₂*V₂₁*) identisch null (200 Zufallsmatrizen ≤ 2·10⁻¹⁶; Wolfram exakt 0). Der Grund ist die Vollständigkeit: Zwei
   Projektoren ergänzen sich zu 𝟙. Für N = 3 gilt exakt Im(V_ij V_kl V*_il V*_kj) = J·Σ ε_ikm ε_jln (Abweichung 10⁻¹⁶; Wolfram für alle 81
   Indizes: 0) mit J = c₁₂c₁₃²c₂₃s₁₂s₁₃s₂₃ sin δ. **Die einzige CP-Phase wird von ε_ijk getragen.** Für N = 4 sind die Quartette nicht mehr
   von der Form J·εε (9 linear unabhängige Werte über die Stichprobe).
2. **CP als Holonomie.** J = Im Tr(P_i Q_j P_k Q_l) ist ein Bargmann-Viereck aus Flavour- und Massenprojektoren (|Im B| = |J| exakt).
   Analog zu k253 (HS(1) hat keine Holonomie, HS(2) die erste) hat der Flavourraum bei N = 2 keine Phase, bei N = 3 die erste.
   Drei Generationen sind die **kleinste Zahl mit Flavour-Holonomie**.
3. **Wo der Turm ein ε hat.** x × y = Im(xy) erfüllt |x×y|² = |x|²|y|² − (x·y)² auf Im ℍ und Im 𝕆 (≤ 6·10⁻¹⁴), auf den Sedenionen nicht
   (3,4·10²). Ein dreidimensionales ε gibt es nur auf Im ℍ. Im 𝕆 hätte sieben Richtungen und 15 Phasen, und die Z-Breite schließt
   sieben leichte Neutrinos aus. **Rückwärts: Die Generationsebene ist ein Im ℍ, also eine HS(2)-Stufe.** Das ist eine Lesart unter
   der Setzung, dass auch der Generationsraum aus dem Turm stammt. Ein ε hat jeder dreidimensionale komplexe Raum über die
   Determinante. Neu im Turm ist nur, dass Im ℍ es als eigenes Kreuzprodukt mitbringt.
4. **Vektor, nicht Dublett.** Unter den Automorphismen x ↦ qxq* ist Im ℍ der Vektor von SO(3) (RᵀR = 𝟙, det +1). Das Tripelprodukt
   Re(x(yz)) = −det[x, y, z] ist invariant: Das ist das ε. Unter der Multiplikation L_q ist ℍ dagegen ein Spin-½-Dublett (Casimir −3/4).
   **Drei Generationen als Familie verlangen die adjungierte Wirkung.** Die reelle Eins von ℍ = 1 ⊕ 3 ist dabei Singulett. Eine vierte
   Generation wäre deshalb **kein Mitglied derselben Familie**. Das ist kein Verbot einer vierten Generation, wohl aber ein Grund,
   warum die Familie drei Mitglieder hat.
5. **Was der Turm über der Farbe tatsächlich liefert (k273 D).** Über dem Block e₁ … e₇ gibt es antikommutierende Basisachsen e₈ (n = 4),
   e₈, e₁₆ (n = 5) und e₈, e₁₆, e₃₂ (n = 6). Das sind genau die neuen Einheiten der Verdopplungen (exakte Cliquensuche über
   Basis-Einheiten; Radon–Hurwitz erlaubt bei n = 6 elf Achsen, die elfte liegt nicht in der Basis und wurde nicht gesucht). Sie
   vertauschen mit allen Bilinearen des Blocks (Abweichung 0) und damit mit Farbe und Ladung: **Universalität ist automatisch.**
   Ihre so(3) wirkt aber mit Casimir −3/4, also als Dublett: **zwei Generationen**, wie ℂ⊗𝕊 im Bestand.

## Bewertung
- Rückwärts verlangt die Beobachtung (eine CP-Phase, drei leichte Neutrinos) eine dritte Rolle von ℍ: neben dem Spin bzw. Isospin
  (Multiplikation, Spin ½) ein Im ℍ als Vektor (Automorphismen, Spin 1). Die bisherigen Träger erfüllen jeweils nur eine Hälfte:
  - Die Clifford-Achsen des Turms (k273 D, ℂ⊗𝕊) geben Universalität, aber ein Dublett.
  - Die Slots (Im ℍ)⊗ℂ⊗𝕆 (K77.3, H19e) geben das Triplett mit gleicher Ladung, sind aber als Tensorfaktor gesetzt und nicht aus dem Turm erzeugt.
  - Die S₃-Kopien (k255) geben ein Etikett mit 120°-Zyklus, aber keine gemeinsamen Ladungen.
- **Präzisierte offene Frage:** Gibt es im Turm eine Stufe, auf der eine HS(2)-Struktur über ihre Automorphismen (adjungiert) auf die
  Materie wirkt? Kandidat wäre die Trialität bei HS(3). Dort ist G₂ der Fixpunkt, und die drei 8er-Darstellungen werden vertauscht.
  Das ist nicht gerechnet, und H37 verbietet nur die reine Triality-*Kopplung*, nicht die Triality als Etikett.
- Keine Vorhersage. OP3/OP4 offen, kein Guard berührt.

## Dateien
`../k273_generationen_rueckwaerts.py` (`../k273_out.txt`), `../k273b_jarlskog.wl` (`../k273b_out.txt`, Wolfram).
