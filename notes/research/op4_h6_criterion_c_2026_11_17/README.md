# OP4, H6 Kriterium C: Hat die Vorzeichen-Symmetrie einen modellinternen Grund? (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „Ja, Vorab-Notiz“ zum Kandidaten aus `../review_discarded_ideas_2026_11_17/` (H6, Kriterium C: TM1 ⇔ die
Gruppe aus Triole und Restspiegelung enthält die vierelementige Vorzeichen-Symmetrie der Oktonionen). Skript `criterion_c.py` (nutzt k22/k23 aus
`../v4_8_0_r03_r12/llm/`), Ausgabe `run/criterion_c_stdout.txt`.

## Warum keine Vorab-Notiz H112
Beim Festlegen des Tests zeigte sich, dass beide naheliegenden Gleichsetzungen **vor der Rechnung analytisch entschieden** sind:
1. **Frame-Abbildungen:** Unter der Abbildung φ (v4.9.0-r51.1(c), r16.2(b)) geht das Feld-Dublett (E, B) auf span(1, e₇); dort wirken T, J_B, R als
   Konjugation, Tausch und L_e₇. Die Vorzeichen-Elemente halten e₇ fest, also span(1, e₇) punktweise. Sie können nicht das Bild der Frame-Abbildungen sein.
2. **Familien-su(2) (r13.4):** Die Vorzeichen-Elemente sind Automorphismen von O, die e₇ festhalten. Ihre Cayley–Dickson-Fortsetzung auf S hält e₇, e₈,
   e₁₅ fest und vertauscht deshalb mit R_e₇, R_e₈, R_e₁₅; auf jedem Dublett der Familien-su(2) wirkt sie höchstens als Skalar, nie als Pauli-Tripel.
Nach „Nicht blind = offen sagen“ ist das kein Test. Die Rechnung bestätigt beide Aussagen und bestimmt die Lage der Gruppe. H112 bleibt frei.

## Rechnung

| Prüfung | Ergebnis |
|---|---|
| Vorzeichen-Elemente sind Automorphismen von O | Abweichung 0 |
| (1) Einschränkung auf span(1, e₇) | Identität für alle vier; Frame-Abbildungen dort nicht trivial → keine Gleichsetzung |
| (2) Fortsetzung auf S | Automorphismus (0), vertauscht mit R_e₇, R_e₈, R_e₁₅ (0); e₇e₈ = +e₁₅ → kein Pauli-Tripel |
| (3) Lage | vertauscht mit L_e₇ (komplex-linear); Vorzeichenwechsel auf genau zwei der drei Linien durch e₇, (e₁,e₆), (e₂,e₅), (e₃,e₄): die Kleinsche Gruppe im Torus von Stab(e₇) = SU(3) |

## Einordnung
- **Die Vorzeichen-Symmetrie aus H6 ist die Kleinsche Gruppe im Torus von SU(3) = Stab(e₇)**, also Vorzeichenwechsel auf zwei der drei komplexen
  Linien durch e₇. In der Lesart von K18 (H6) sind diese Linien das Generationen-Triplett; in der Dixon-Lesart ist Stab(e₇) die Farbgruppe. Beide Rollen
  stehen nebeneinander und sind getrennt zu halten (r27.2(c)).
- **Strukturelle Parallele, keine Gleichsetzung:** Die Triole e₄ → e₅ → e₆ liegt mit je einer Einheit in jeder Linie durch e₇ und zyklisiert die drei
  Linien. Vierergruppe plus Dreierzyklus geben auf den Oktonionen A₄, mit Spiegelung S₄ (Ordnung 24), wie auf χ die Frame-Abbildungen (π-Drehungen um
  drei senkrechte Achsen) mit dem Generationszyklus. Dasselbe Muster liegt also auf zwei verschiedenen Räumen; eine Abbildung zwischen den drei Linien
  durch e₇ und den drei Achsen von χ gibt es im Bestand nicht (vgl. r16.5: keine mit R, T, J_B verträgliche Gleichsetzung von N mit χ).
- **Folge für die Sichtung:** Der Kandidat „H6, Kriterium C hat seit 16.11. einen modellinternen Grund“ trägt nicht. Kriterium C bleibt ohne Grund; was
  bleibt, ist die Parallele. Ein Grund entstünde erst mit einer begründeten Abbildung „Linien durch e₇ ↔ Achsen von χ“, die die Frame-Abbildungen auf die
  Vorzeichen-Elemente schickt. OP4 offen.

## Ergebnis in einem Satz
Die Vorzeichen-Symmetrie aus H6 ist die Kleinsche Gruppe im Torus von Stab(e₇); sie ist weder das Bild der Frame-Abbildungen noch ein Pauli-Tripel der
Familien-su(2) (beides analytisch, nachgerechnet), sondern trägt auf den Oktonionen dasselbe Muster (A₄, S₄) wie die Frame-Abbildungen auf χ. Kriterium C
bleibt ohne modellinternen Grund. OP4 offen.
