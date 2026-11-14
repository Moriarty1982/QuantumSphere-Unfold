# OP3: Rückwärtssuche nach einer Quelle für gleiche Kopplungen von Q und R

14. November 2026, Claude Opus. **Erkundung, nicht blind** (Rückwärtssuche): Zielzustand,
K_orb = 2/3 und π/4 waren vorher bekannt. Einordnung T8/T13, OP3. Keine Hypothese vergeben,
kein CT-Eintrag, keine Guard-Änderung. Auftrag des Autors: „Wirkung suchen“, als nächster
begrenzter Ansatzpunkt aus `../op3_reference_energy_selection_2026_11_14/README.md`.

## Ziel und notwendige Bedingungen

Gesucht ist eine vorhandene Wirkung, die auf dem neutralen Slotraum C³ den Term
H = −a(Q + R) mit **gebunden gleichen** Kopplungen liefert. Dabei ist Q = (I + D + D²)/3,
R = (I + τ + τ²)/3. Nach der Codex-Erkundung gilt K_orb = 2/3 genau bei a = b.
Notwendig für eine Quelle ist also:

- (N1) Sie enthält einen Rang-eins-Term aus ⟨D⟩ und einen aus ⟨τ⟩, oder etwas Gleichwertiges.
- (N2) Die beiden Gewichte sind durch eine Symmetrie oder eine Zählregel gleich, nicht durch Wahl.

## Vorwissen geprüft

- Gesamtbild nach r13, beide Übergaben vom 14.11. und die Codex-Notizen vom 14.11.:
  - `../op3_reference_energy_selection_2026_11_14/README.md`;
  - `../op3_fourier_native_gate_2026_11_14.md`;
  - `../op3_triality_slot_phases_2026_11_14/README.md`;
  - `../op3_two_probe_fourier_bridge_2026_11_14.md`.
- Ältere Notizen: `../op3_slot_fourier_2t_2026_11_14.md`, `../op3_tau_doublet_axis_2026_11_14.md`,
  `../op3_slot_u3_gauging_2026_11_13.md`, `../op3_koide_potential_2026_11_13.md`,
  `../op3_string_relaxation_backward_2026_11_12.md`.
- Volltextsuche in `notes/research`, `analysis` und `wiki` nach Potts, Kramers, selbstdual, self-dual,
  MUB, Weyl-Heisenberg und Uhrenmodell: keine einschlägige Fundstelle. Die Treffer zu „Hesse“ meinen
  die Hesse-Matrix.
- Wirkungen im Bestand mit Slotoperatoren:
  - Die Familien-U(3)-Eichung (`op3_slot_u3_gauging`) gibt eine Überlappung als Feld, aber keinen
    D-Term.
  - Der Zwei-Sonden-Verbinder T_12 ist tau-erhaltend und erzeugt F nicht (Codex).
  - Die Stringrelaxation (`op3_string_relaxation_backward`) gibt K = 2/3 nur mit abgestimmter
    Kraftfunktion und arbeitet auf Längen, nicht auf dem Slotzustand.
- **Keine vorhandene Wirkung erfüllt (N1) und (N2) zugleich.**
- QAM-Leseserver in dieser Sitzung nicht verbunden. Keine Belege oder Prämissenhashes benutzt.

## 1. Keine native Slotsymmetrie bindet die Gewichte

Die native Slotgruppe besteht aus Permutationen mit Phasen, also monomialen Matrizen.
Durchgerechnet ist die Gruppe mit sechsten Einheitswurzeln (Ordnung 1296). Konjugation mit einer
monomialen Matrix bildet Diagonalmatrizen auf Diagonalmatrizen ab. In allen 1296 Fällen geht ⟨D⟩
daher auf ⟨D⟩, nie auf ⟨τ⟩. Q und R liegen in verschiedenen Bahnen, und keine native Slotsymmetrie
kann a = b erzwingen.

Ein Tausch verlangt eine nicht monomiale Operation, etwa F (F D F† = τ). F wurde aber schon als
nicht nativ und nicht trialitätssymmetrisch ausgeschlossen (Codex, 14.11.). Bedingung (N2) bleibt
damit nur über eine Zählregel oder eine dynamische Auswahl erreichbar.

## 2. Die Paarwahl ist beliebig, nur die gleichen Gewichte zählen

Die vier zyklischen Untergruppen ⟨D⟩, ⟨τ⟩, ⟨τD⟩ und ⟨τD²⟩ der Weyl-Gruppe haben je drei
Eigenlinien, zusammen zwölf Projektoren. Sie bilden vier gegenseitig unverzerrte Basen (MUBs).
Durchsucht wurden alle Summen H = −Σ w_i P_i:

- mit w_i ∈ {0, 1}: 4095 Summen, 270 Treffer;
- mit w_i ∈ {−1, 0, 1}: 531440 Summen, 5616 Treffer.

Als Treffer zählt ein eindeutiger Grundzustand, dessen S-Bahn für einen ausgezeichneten Slot
K_orb = 2/3 gibt.

- **Alle 54 Paare** gleich gewichteter Linien aus zwei verschiedenen Untergruppen treffen. Sie geben
  den Oktanten-Bezug für genau einen Slot, mit |Bargmann-Phase| = π/4. Das Paar aus den
  Eigenwert-1-Linien von D und τ ist das Q/R-Paar von Codex.
- Grund: Zwei Linien aus verschiedenen MUBs haben stets |⟨a|b⟩|² = 1/3. Die Codex-Formel hängt nur
  von dieser Überlappung und vom Gewichtsverhältnis ab.
- Alle 0/1-Treffer sind nach Abzug vollständiger Basen (Summe = Identität) ein solches Paar. Die
  einzige Ausnahme sind 54 betragsgleiche ±-Kombinationen aller vier Untergruppen.
- Demokratische Zählregeln treffen nicht:
  - Eigenwert-1-Linien aller vier Untergruppen: K_orb = 3/5, Lücke (1+√5)/2 (numerisch 1,618034);
  - Eigenwert-1-Linien von drei Untergruppen: K_orb = 0,5902;
  - alle zwölf Linien: H ∝ I, entartet.

Das schärft die Voraussetzung. Q und R sind nicht ausgezeichnet. Gebraucht werden **zwei gleich
gewichtete Rang-eins-Terme aus zwei unverzerrten Basen**. Die Unverzerrtheit ist nativ (D und τ),
die Gleichgewichtung nicht.

## 3. Lesart: Gleichgewicht ist Selbstdualität eines Z3-Uhrenterms

Exakt gilt −J(Z + Z†) − h(X + X†) = −3J Q − 3h R + (J + h) I mit Z = D und X = τ. Die Bedingung
a = b ist also J = h, und F bildet Z auf X ab. Das ist der F-selbstduale Punkt eines Z3-Uhrenterms
auf einem Platz. Bei J = h sind die Eigenwerte −(1 + √3)J, (√3 − 1)J und 2J, der Grundzustand ist
(1 + √3, 1, 1).

**Grenze der Lesart.** In einer Z3-Potts- oder Uhrenkette ist der Kramers-Wannier-selbstduale Punkt
der kritische Punkt. Dort ist das Gleichgewicht dynamisch ausgezeichnet. Der Kopplungsterm der Kette
ist aber Z_i Z†_{i+1}, nicht das Einzelplatz-Z + Z†. Eine Kette, ein Gitter oder ein
Kritikalitätsprinzip über den Slots gibt es im Companion nicht. Die Lesart benennt also den Typ
eines möglichen Auswahlprinzips. Sie ist keine Quelle.

## Ergebnis

Im Bestand liefert keine Wirkung Q und R mit gebunden gleichen Kopplungen. Die Rückwärtssuche
zeigt dreierlei:

1. Native Slotsymmetrien können die Gleichheit nicht erzwingen (§1).
2. Die Wahl des Paars ist frei, offen ist allein die Gleichgewichtung zweier unverzerrter Terme
   (§2).
3. Die Gleichgewichtung ist dasselbe wie F-Selbstdualität (§3). Damit führt die Bezugsauswahl
   auf dieselbe fehlende Struktur wie die aktive Fourier-Route.

Das ist die **fünfte Variante mit derselben offenen Voraussetzung** (nativer Bezug bzw. F). Die
Linie hält hier an. Empfehlung: ruhen lassen, bis H100 oder H102 entschieden sind. Ein späterer
Ansatz bräuchte eine neue Struktur, etwa ein Gitter oder eine Kette über den Slots mit
Kritikalität oder eine native nicht monomiale Slotoperation. Er ist kein weiterer Gewichtsfit.

I1–I5 geprüft, kein Auslöser getroffen. OP1–OP5, C5, C6/T2 und die Guards bleiben unverändert offen.
CT-001 bis CT-003 sind unverändert.

## Nachweis

```
python notes/research/op3_action_balance_search_2026_11_14/search.py --out notes/research/op3_action_balance_search_2026_11_14/result.json
python notes/research/op3_action_balance_search_2026_11_14/extra.py   # im Ordner ausführen
```

- `search.py`: §1, §2 numerisch mit Toleranz 1e-9, §3 exakt mit sympy.
- `extra.py`: natürliche Mehrtermkandidaten, Größenprofil und Reduktion der Treffer.
- Ausgaben: `result.json`, `run/search_stdout.txt`, `run/extra_stdout.txt`.

## Nachtrag 14.11.: Durchsicht der übrigen Teilbäume (nachträglich, auf Bitte des Autors)

Durchsucht wurden alle Teile unter `sources/research/parts/` nach Fourier, modular, selbstdual, Dualität,
Chern-Simons, Wilson und Verlinde. Chern-Simons, Wilson und Verlinde kommen nicht vor. Drei Stellen waren bisher
nicht mit der Bezugsauswahl verbunden:

1. **Mischung r46/r47 (OP4), stärkster Anknüpfungspunkt.** r46 schreibt die Mischung als zirkulante
   Kopplung plus Einslot-Maske, M + δD_S. Das ist genau die Form von Codex' H, denn R ist eine
   Rang-eins-Zirkulante (das τ-Mittel, „∨-Lesart“ von r39/r46), und D_S mit |S| = 1 ist Q.
   r47 leitet die Maske aus der Chiralitätsabweichung J_II − J_I her: W_l = diag(0, 0, −3) für Leptonen,
   also ein reiner Einslot-Projektor, aber W_q = diag(0, −2, −1) für Quarks, also kein Projektor. Dass
   Koide nur für geladene Leptonen genau gilt, passt zu dieser Trennung. Das ist eine Beobachtung, kein Beleg.
   Die Kopplung ε ist in r47 ausdrücklich nicht hergeleitet. `r47_mask_check.py`, numerisch auf sechs
   Stellen:
   - additiv (r46-Form), −R + δW_l: K_orb = 2/3 bei δ = 1/3, das ist die Balance a = b;
   - in r47-Form, M + ε(W_l M + M W_l) mit M = −R: K_orb = 2/3 bei ε = 1/12, π/4, Lücke 0,8497.

   Offen ist damit die Herleitung von ε. Ergäbe sie unabhängig ε = 1/12, wäre die Bezugsauswahl an OP4
   gebunden. Ein solcher Test müsste vorab festgeschrieben werden. Der Zielwert ist jetzt bekannt, die
   Herleitung von ε könnte aber blind gegen ihn sein, wenn sie ihn nicht benutzt.
2. **Elektromagnetische Dualität (r07).** z ↦ iz ist die Dualitätsdrehung E ↦ −B, B ↦ E. Sie hat
   Ordnung vier wie F und vertauscht mit Boost und Modulgruppe. Ihre Energie (E² + B²)/2 ist
   dualitätsinvariant, also gleich gewichtet. Wären D und τ die magnetische und die elektrische
   Z3-Variable eines Slotfelds, so erzwänge Dualitätsinvarianz a = b. Ein solches Wörterbuch gibt es im
   Companion nicht.
3. **Δ(96) (r12.2/r12.3).** Die Flavourgruppe ist monomial, Phasen ±1, ±i. Nach §1 vertauscht sie Q und R
   nicht. Ihre Spalte (1/3, (2 ∓ √3)/6) enthält π/12. Mit dem Bezug ist sie nicht identisch
   (K_orb = 5/9 für einen Vektor mit p₀ = 1/3).

## Nachtrag 2 (14.11.): Vorwissen zu ε vor H105, Berichtigung von Nachtrag 1

Bei der Vorwissensprüfung für H105 kamen die Folgerunden von r47 hinzu. Sie ändern das Bild:

- **r50 (H34):** Die lineare Form M + ε(WM + MW), die in Nachtrag 1 ε = 1/12 gab, ist als Mischungsmodell
  widerlegt. Der Term ε²WCW erzeugt Massen, und die Hierarchie hält ε klein.
- **r52 (H36):** Ersetzt wurde sie durch die exakten Formen K (DCD) und S (DCD⁻¹) mit D = exp(εW).
- **r54 (H38) und r56 (H40):** Mit einem ε je Sektor passt Form S an CKM und PMNS, mit
  ε_e ∈ [0,44; 0,82] und ε_ν ∈ [0,27; 0,55]. Die Runden nennen das eine Anpassung, keine Erklärung. Die Herkunft
  von ε ist offen, und der Vergleich mit 14 Korpuswerten lag im Zufallsbereich.
- **Exakte Formen, nachgerechnet:** Mit dem Rang-eins-Zirkulanten C = R ist der linke Singulärvektor in K und
  S derselbe, nämlich D(1, 1, 1). K_orb = 2/3 gilt bei **ε* = (1/3) ln((1 + √3)/2) ≈ 0,10397**, numerisch auf
  15 Stellen gleich. Dann ist e^{−3ε*} = √3 − 1, und das Gewicht des ausgezeichneten Slots ist (3 − √3)/6.
- **Folge:** Der Wert 1/12 aus Nachtrag 1 gehört zu einer widerlegten Form. Der Wert der exakten Formen,
  0,104, liegt außerhalb des Fitbereichs von ε_e. Einschränkung: r54 benutzt volle Brannen-Zirkulanten, nicht
  den Rang-eins-Grenzfall. Der Vergleich ist daher ein Hinweis gegen die Gleichsetzung, keine Widerlegung.
  Steht damit schon fest, ohne Test.

## Nachtrag 3 (14.11.): Idee des Autors, ε mit zwei Auslesungen je nach Kopplungspartner

Frage des Autors: „was ist wenn epsilon in dem grenzfall zwei auslesungen hat, je nachdem wer es braucht oder besser,
mit wem es gerade koppelt?“ Einordnung als Erkundung, nicht blind:

- **Im Bestand schon angelegt:** r47 liest den rechtshändigen Partner im Frame T. r52 unterscheidet die
  Formen K (Partner über Zeitumkehr) und S (Partner über die Tachyon-Abbildung). Im Rang-eins-Grenzfall geben
  K und S aber **dasselbe** ε* = 0,10397 (Nachtrag 2). Die beiden vorhandenen Partnerlesarten spalten ε also
  nicht. Eine Spaltung müsste im Betrag liegen, nicht in der Form.
- **Nötiger Faktor:** Zwischen der Bezugslesart (ε* = 0,10397) und der Mischungslesart (ε_e ∈ [0,44; 0,82],
  r54) liegt ein Faktor von 4,23 bis 7,89.
- **Vorhandenes Frame-Gesetz r85.1 (H82):** Massenterme gehen mit P = a + b ein, Ableitungsterme mit
  K = a − b. Bei Materiegewichten ist P/K = γ = 1,8645. Ein Faktor γ gibt 0,194, γ² gibt 0,362; beide liegen
  außerhalb. Erst γ³ = 6,48 läge innerhalb, wofür r85 kein Gesetz hat. Mit dem vorhandenen Gesetz trägt die
  Idee also nicht. Jeder andere Faktor wäre bei dieser Bandbreite eine Auswahl im Nachhinein (vgl. r56:
  Korpuswerte treffen solche Bereiche zufällig).
- **Wenn die Idee verfolgt werden soll:** Ohne eine vorab feste Ausleseregel ist ein partnerabhängiges ε ein
  Gegenterm. Er gehört ins Gegenterm-Register (ein möglicher CT-004 „ε mit zwei Auslesungen“ mit Guards), und
  jede Folgerung erbt diese Guards. Ein Test (H105) wäre erst sinnvoll, wenn die Regel (welcher Partner, welcher
  Faktor) aus dem Bestand festgelegt ist, bevor gerechnet wird.

## Nachtrag 4 (14.11.): Idee des Autors, ε gilt in seiner jetzigen Gestalt nur in einem Frame

Frage des Autors: Gilt ε in der jetzigen Gestalt vielleicht nur in einem Frame und muss in einem anderen anders
verstanden werden? Erkundung, nicht blind.

- **Wo ε heute steht:** Die Mischungsanpassung r54 ist eine Aussage über Massenmatrizen in M, in T gleich wie
  in r52; **P ist nicht ausgewertet** (Frametabelle r54). Die Maske selbst ist T-ungerade (r47.1(b):
  TΔT⁻¹ = −Δ).
- **Strukturelle Übereinstimmung:** Die Balance a = b, die der Koide-Bezug verlangt, ist genau die Bedingung
  der Photonengewichte (r85.3: arctan(b/a) = 45°; r82/r83: Aufhebung bei Photonengewichten). Liest man
  H = −(aQ + bR) mit den Frame-Gewichten a (M) und b (T), so gilt:

  | Gewichte | a/b | K_orb |
  |---|---|---|
  | Materie (K = 1/γ, P = 1) | 1/β² = 3,3129 | 0,9545 |
  | Tachyon (vertauscht) | β² = 0,3018 | 0,5006 |
  | Photon | 1 | 2/3 exakt |

  Lesart: Der Koide-Bezug wäre eine P-Auslesung und das Mischungs-ε eine M-Auslesung. Dass beide Zahlen
  verschieden sind, wäre dann zu erwarten.
- **Erste Lücke:** Die Lesart verlangt, dass die M→T-Abbildung den D-Projektor Q auf den τ-Projektor R
  abbildet. Nach r51.1 wirkt die Tachyon-Abbildung z ↦ iz unter der Annahme r33 (C-Faktor der Dixon-Ablage
  = Amplitudenebene) als Multiplikation mit der äußeren Einheit, auf dem Slotraum also skalar. Die
  Zeitumkehr wirkt als Konjugation (D ↦ D⁻¹). Beide sind monomial (§1) und bilden Q nicht auf R ab. Unter r33
  trägt die Lesart also nicht. Sie bräuchte eine andere Lage der Frame-Ebene, die auf den Slotindex wirkt.
- **Zweite Lücke, nach dem Muster von r85.1, nicht gerechnet:** Ein T-ungerader Term geht mit a − b ein und
  verschwindet bei Photonengewichten. Die Maske wäre in P dann null.
- **Folge:** Die Idee ist der bisher sauberste Ort für die Balance, weil Photonengewichte sie ohne Wahl liefern.
  Daran hängt eine benannte Annahme (r33), keine freie Zahl. Ein Gegenterm wäre daher „Q und R sind M- und
  T-Lesart desselben Terms“, nicht „ε mit zwei Werten“.

## Nachtrag 5 (14.11.): Idee des Autors, Kreuzprodukte der Frames, ε an den Orthogonalen

Frage des Autors: Bildet man aus jeder Kombination der Frames ein Kreuzprodukt, erhält man neue, senkrechte
Frames. Kann ε an diesen Orthogonalen hängen? Erkundung, nicht blind, `frame_cross_check.py`.

- **Kreuzprodukt der Frame-Abbildungen (r51):** Gemeint sind R: z ↦ iz, T: z ↦ z̄ und J_B = R∘T auf der reellen
  Frame-Ebene. Exakt gilt [R, T]/2 = J_B, [T, J_B]/2 = −R und [J_B, R]/2 = T. Die Kreuzprodukte schließen also
  und erzeugen **keine neuen Frames**; drei ist der vollständige Satz. Die Vorzeichen und die Quadrate
  (R² = −1, T² = J_B² = +1) zeigen aber sl(2, R) bzw. so(2, 1), nicht su(2). Die drei sind daher nicht drei
  gleichwertige senkrechte Achsen, sondern eine Drehung (Tachyon) und zwei Spiegelungen.
- **Vorwissen:** Im neutralen Dixon-Teil verhinderte eine indefinite Signatur den exakten Oktanten
  (`../op3_hopf_octant_2026_11_13.md`, Punkt 3). Bei den Frame-Abbildungen ist dieselbe Sperre zu erwarten. Mit
  einer vom Frame unabhängigen imaginären Einheit i wäre −iR hermitesch, das Tripel wäre su(2), und die
  Eigenzustände der drei Frame-Abbildungen bildeten das Oktanten-Tripel (K = 2/3, π/4, Zyklus der Ordnung 3).
  Unter r33 ist i aber gerade R, und dann ist −iR = 1. **Die Sperre ist wieder die Annahme r33.**
- **Orthogonale der Frame-Gewichte (r85):** Auf den Gewichten (a, b) gilt die Form a² − b² = P·K, das Produkt
  aus Massen- und Ableitungsgewicht. Damit gilt exakt:
  - ⟨M, T⟩ = 0: Jeder Frame ist zu seinem Tachyon-Bild orthogonal.
  - ⟨M, M⟩ = 1/γ.
  - ⟨P, P⟩ = 0: Der Photon-Frame ist lichtartig, also **zu sich selbst orthogonal**.

  Hängt ε am Orthogonal des Frames, in dem gelesen wird, so wird es in M mit dem Gewicht von T gelesen und in
  P mit dem Gewicht von P selbst. Nur in P fallen Term und orthogonaler Term zusammen. Das ist genau die
  Balance a = b, also K_orb = 2/3 (Nachtrag 4) und F-Selbstdualität (§3).
- **Folge:** Die Idee präzisiert Nachtrag 4. Die Balance ist die Selbstorthogonalität des lichtartigen
  Photon-Frames, und zwar ohne Wahl. Offen bleibt dieselbe eine Stelle: ob die Frame-Ebene eine von ihr
  unabhängige komplexe Einheit hat bzw. auf den Slotindex wirkt (Annahme r33). Beide Wege zum Oktanten über die
  Frames scheitern bisher genau dort.

## Nachtrag 6 (15.11.): Idee des Autors, Levi-Civita-Symbol aus zyklisch rotierten Frame-Kreuzprodukten

Präzisierung des Autors: Das Kreuzprodukt aus (M, T, P) bilden und nur die Reihenfolge im Tupel zyklisch rotieren,
um so ein Levi-Civita-Symbol zu erhalten. Erkundung, nicht blind, `frame_levi_civita.py`.

- **Kriterium:** Ein Levi-Civita-Symbol liegt vor, wenn die Strukturkonstanten c in [X_i, X_j]/2 = c X_k unter
  zyklischer Rotation des Tupels gleich bleiben (und unter Vertauschung das Vorzeichen wechseln). Das ist genau
  der Fall einer Drehalgebra so(3) = su(2).
- **Gewichtsvektoren:** M, T und P liegen in der (a, b)-Ebene und haben Rang 2. Ein dreidimensionales
  Kreuzprodukt gibt es dort nicht. Es muss an den Frame-Abbildungen ansetzen.
- **Native Frame-Abbildungen (R, T, J_B):** Die Konstanten sind (+1, −1, +1), exakt. Die zyklische Rotation
  kippt ein Vorzeichen, und zwar an der Tachyon-Abbildung (R² = −1). Keine reelle Umskalierung ändert das
  (64 Fälle geprüft); es ist die Signatur von so(2, 1). **Kein Levi-Civita-Symbol.**
- **Mit unabhängiger Einheit i (iR statt R):** Alle drei Konstanten sind gleich (i), das Tupel ist zyklisch
  invariant, und es entsteht ein Levi-Civita-Symbol (su(2)). Dann gilt automatisch:
  - die drei Frame-Achsen sind orthogonal, die zyklische Rotation ist ein Element der Ordnung 3 um die
    Diagonale, und jede Achse liegt unter arccos(1/√3) zu ihr;
  - die Achsenzustände bilden das Oktanten-Tripel: mittlere Treue 1/2, K = 2/3, Bargmann-Phase π/4 (exakt
    nachgerechnet).

  **Ein Levi-Civita-Symbol auf den Frames wäre also genau das gesuchte Profil.**
- **Folge:** Die Idee des Autors macht die Lücke so scharf wie bisher keine andere Formulierung. Es fehlt genau ein
  Vorzeichen: das der Tachyon-Abbildung im zyklischen Kreuzprodukt. Es lässt sich nur mit einer vom Frame
  unabhängigen komplexen Einheit beheben, also an der Annahme r33.
- **Einschränkung:** Das Oktanten-Tripel wäre hier die Bahn eines Zustands über die drei Frame-Achsen. Die drei
  geladenen Leptonen sind aber alle Materie im Frame M. Ob und wie die Frame-Bahn mit den Generationen
  zusammenhängt, ist damit nicht gesagt.
