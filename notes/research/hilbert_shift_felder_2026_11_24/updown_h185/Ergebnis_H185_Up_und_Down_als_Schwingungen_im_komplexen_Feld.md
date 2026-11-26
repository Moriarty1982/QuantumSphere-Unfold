# Ergebnis H185: Das komplexe Feld erlaubt Up und Down, trennt sie aber nicht von selbst

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H185_Up_und_Down_als_Schwingungen_im_komplexen_Feld.md` (Commit df685ba, vor der Rechnung). Skripte
`k388_test_h185.py` (`k388_out.txt`) und `k388b_gegenprobe.wl` (`k388b_out.txt`).

Werkzeuge: Python (numpy, scipy) mit expliziten Oktonionen und komplexem Jordan-Produkt auf ℂ ⊗ H₃(𝕆); invariante Formen als Nullraum der
Stabilisatorbedingungen; zweite Variation von 43 Spurinvarianten auf den 36 Farbrichtungen (endliche Differenzen mit Richardson, für Grad ≤ 4 exakt
bis auf Rundung). Wolfram Language exakt für die Zählung im reduzierten Raum (nach Schur genügt je Farbkomponente die Struktur L_U) und für die
Spektren je Ladung. Qiskit nicht eingesetzt (keine Schaltung). Warnungen in Wolfram: nur Hinweise der Auswerteumgebung, keine Rechenwarnung.

**Ergebnis in einem Satz:** Um das Leptonvakuum hat das komplexe Feld zwei Sätze von Farbschwingungen (Ladung ⅓ und ⅔, je drei Generationen); die
Symmetrie erlaubt sechs ladungserhaltende und sechs ladungsmischende Massenterme, und kein Potential aus Jordan-Spuren ohne ausdrücklichen
Ladungsoperator gibt Up und Down verschiedene Frequenzen.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H185a (nicht blind) | Formen: nur Farbe 36, mit P 12; Vielfachheiten (6,6,6,6,6,6) in 25 von 25 Proben; alle vertauschen mit dem Platztausch | 12 und sechsmal 6 | **bestätigt** |
| H185b (nicht blind) | 6 vertauschen mit i (je eine Zirkulante für ⅓ und ⅔), 6 antivertauschen (mischen ⅓ und ⅔) | 6 + 6 | **bestätigt** |
| H185c | mit C: 3 ladungserhaltende Formen, Spektren für ⅓ und ⅔ gleich (≤ 3,3·10⁻¹⁵; Wolfram: Differenz der char. Polynome 0) | gleich in allen Proben | **bestätigt** |
| H185d | 43 Spurinvarianten bei δ = 2/9: Unterschied der Spektren für ⅓ und ⅔ höchstens 1,2·10⁻¹⁵ (bei δ = 0: 1,3·10⁻¹⁵) | > 10⁻⁶ bei δ = 2/9 | **widerlegt** |
| Bericht | freie Größen: 12; ladungserhaltend 6 (für sechs Massen); mit C 3; ladungserhaltend mit τ 4 (Vielfachheiten 6, 6, 12, 12) | Bericht | – |

Kontrollen: R_U = −L_U auf dem Farbblock; Ladungen ⅓ und ⅔ je 18-fach; C Q C = 1 − Q; P und τ vertauschen mit Q; Invarianz der zweiten Variationen
unter Farbe und P bis 2·10⁻¹³.

## Lesart
- **Zwei Quarktypen, je drei Generationen.** Die 36 Farbrichtungen zerfallen nach der Ladung in zweimal 18. Ladungserhaltend gibt es je Ladung eine
  hermitesche Zirkulante (α, β wie in H184), zusammen sechs freie Größen für sechs Massen. Keine Vorhersage.
- **Ladungsmischende Terme sind erlaubt.** Das reelle Leptonvakuum ist kein Ladungseigenzustand (die reelle 1 mischt Q = 0 und Q = 1). Deshalb gibt es
  sechs weitere Formen, die eine Schwingung der Ladung ⅓ mit einer der Ladung ⅔ verbinden; mit ihnen sind die Eigenrichtungen keine
  Ladungseigenzustände mehr (Beispiel: Erwartungswerte 0,334 bis 0,666). Sie verschwinden genau dann, wenn die Phase e^{iθ} auf den Farbrichtungen
  allein eine Symmetrie ist. Das ist eine Erhaltung der Farbzahl (so viele W wie W̄ im Farbanteil jedes Terms), in üblicher Sprache Baryonenzahl.
  In den Spurinvarianten: Re und Im von Tr W², Tr W³, Tr W² ∘ W_U² und ähnliche sind rein ladungsmischend; Tr W W̄, Tr (W W̄) W_U,
  Tr (W W̄) ∘ W_U² sind rein ladungserhaltend; Tr W² W̄, Tr (W W̄)² sind gemischt (Anteile 0,28 bis 0,5).
- **Up ≠ Down verlangt die Brechung von C.** Mit der ℂ-Konjugation sind die Spektren für ⅓ und ⅔ gleich (wie H182 für ein Feld).
- **Spuren allein brechen C nicht (H185d widerlegt).** Die Vermutung, die Leptonphase δ ≠ 0 erzeuge den Unterschied, trägt nicht. Grund für das
  reelle Vakuum (nachträglich): Alle Strukturkonstanten und W₀ sind reell, also ist der Koeffizient von δW δW̄ in jeder Spur reell; Realteile sind
  C-gerade, Imaginärteile haben keinen ladungserhaltenden Anteil. Der Unterschied braucht einen Term mit dem Ladungsoperator selbst
  (i·L_U, wie die eine ladungsungerade Invariante aus H182).

## Zusatz (nachträglich, Erkundung): nicht reelles Vakuum
Zwei Varianten des Vakuums (Einträge neben der Diagonale mal e^{0,3i}; Einträge plus 0,3·iU), zehn Invarianten mit ladungserhaltendem Anteil: Die
Imaginärteile tragen jetzt bei, aber die Spektren für ⅓ und ⅔ bleiben gleich (≤ 8,7·10⁻¹⁵). Der Grund ist hier nicht hergeleitet; der Befund gilt
für die geprüfte Familie. Verglichen sind Spektren; ein Unterschied nur im Vorzeichen der Phase von β zwischen den Ladungen bliebe so unsichtbar,
ändert aber auch keine Frequenz.

## Bilanz der Setzungen
| | gesetzt | hergeleitet | offene Wahl wandert nach |
|---|---|---|---|
| Träger | W ∈ ℂ ⊗ H₃(𝕆) | zwei Farbsätze nach Ladung | – |
| Vakuum | reelle Zirkulante, K = ⅔, δ = 2/9 (Messwerte) | bricht die Ladung Q₀ | ob das Vakuum die Ladung erhalten muss |
| Symmetrie | Farbe, P; wahlweise Farbphase, C, τ | 12 = 6 + 6 Formen; mit C gleiche Spektren | Grund für die Farbphase (Baryonenzahl) |
| Up ≠ Down | – | braucht C-Brechung; Spuren liefern sie nicht | Koeffizient des Terms mit i·L_U (H182: C/B) |
| Massen | keine Zuordnung Frequenz ↔ Masse | – | α, β je Ladung (angepasst) |

## Grenzen
Grad ≤ 4, statisch und homogen, ohne Ableitungsterme; Vakuum als Eingabe; J auf H₃ nicht gefordert; die Spurfamilie ist nicht vollständig, H185d
gilt für die 43 geprüften Invarianten (für reelles Vakuum durch das Argument oben gestützt). Q₀ wirkt nur auf Einträge neben der Diagonale. Die
Lesart „Farbphase = Baryonenzahl“ ist eine Benennung, keine Herleitung. Kein Vorzeichen gesetzt. OP3 und OP4 bleiben offen.

## Nächster Schritt (Vorschlag)
Den Term mit dem Ladungsoperator im Albert-Rahmen ausschreiben (Fortsetzung der Invariante aus H182 auf drei Generationen) und prüfen, ob er α oder β
verschiebt, also ob er K oder δ der Quarks trennt; dazu die Daten (K_d 0,7478, K_u 0,8876). Mit Vorab-Notiz. Vergeben: H185, k388. Nächste frei:
H186, k389.
