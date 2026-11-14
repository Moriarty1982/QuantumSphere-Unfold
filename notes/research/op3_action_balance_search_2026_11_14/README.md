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
