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
