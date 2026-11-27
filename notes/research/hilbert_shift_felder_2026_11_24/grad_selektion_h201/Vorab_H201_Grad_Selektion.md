# Vorab-Notiz H201 / k411 — Ist die Chiralität der Quintik eine Grad-Selektion?

**Datum:** 2026-11-27
**Strang:** Quarkmassen, Feldgleichung (Fortsetzung nach H200)
**Nummern:** Test H201, Skript k411 (vor dem Push erneut gegen `main` geprüft; Parallel-Thread HS(−1) vergibt ebenfalls k-Nummern)
**Freigabe:** Autor „ja bitte" (27.11., 11:26 UTC) — zuerst (1) Grad-Selektion der chiralen Quintik, danach (2) der 0,9-%-Rest.

## Frage

H200 ergab: die Chiralität der Ladung ist **gradselektiv** — nur der Term höchsten l_k-Grades
(l_k², „Quintik") koppelt chiral (D = B), der lineare Term nicht. H201 prüft, ob diese
Grad-Selektion ein **Strukturprinzip** ist: Folgt „nur der Top-Grad ist chiral" aus der Form des
Potentials (F4-invarianter, ladungsgerader Teil + holomorpher, chiraler Teil), oder ist D ≈ B
eine **gradübergreifende Koinzidenz** zweier unabhängiger Kopplungen?

Die saubere Grad-Selektions-Lesart würde bedeuten:
- der l_k-Term ist rein ladungsblind (C = 0, kein ladungsungerader Anteil),
- der l_k²-Term ist rein chiral (D = B),
denn ein holomorpher Zusatz allein am höchsten Feldgrad gibt einen P_up-Beitrag (gleich gerade +
ungerade) nur dort, und der ladungsblinde Rest ist überall gerade (C = 0).

## Vorwissen geprüft

- `symmetrie_db_h197/k406_test_h197.py` (H197): Grad-Leiter der **ladungsgeraden** F4-Krümmung
  (l_k² erst bei Grad 5) und der **ladungsungeraden** H186-Krümmungen (l_k² schon bei Grad 4).
  Befund: B (gerade l_k²) und D (ungerade l_k²) aus **verschiedenen Graden** ⇒ unabhängig, D/B frei.
  → Diese Maschinerie (hcomp-Leiter, odd_forms, Vakuum-Identitäten) wird wiederverwendet und auf
  den **linearen** Term erweitert (wo erscheinen A und C?).
- `chirale_feldgleichung_h200/` (H200): global holomorph verworfen; strikt D=B bei ~9σ verworfen;
  Chiralität dominant, approximativ, gradselektiv. D/B = 1,0085.
- `ladung_zaehler_h196/` (H196): 4-Param-Fit A=1,082e-3, B=3,291e-2, C=−2,224e-3, D=3,320e-2.
  **Beachte C/A ≈ −2,06**: der lineare Term ist stark ladungsabhängig, nicht blind.
- Vakuum-Identitäten: l_i+l_j = 3−l_k, l_i²+l_j² = 6−l_k², l_i·l_j = 3/2−3l_k+l_k².
- Quarkdaten (M_Z-Yukawa, k376): up, down mit σ wie in k406.

## Test

Zwei Teile am selben Datensatz (6 Massen, Zuordnung B, Nenner (l_i+l_j)²).

**(A) Strukturelle Grad-Zerlegung (teils nicht blind).** Mit der k406-Maschinerie für jeden
Feldgrad n den Beitrag zu **allen vier** Koeffizienten bestimmen:
- ladungsgerade F4-Krümmung v = xⁿ → l_k-Koeff (zu A) und l_k²-Koeff (zu B), je Grad.
- ladungsungerade H186-Krümmungen (Grad 4) → l_k-Koeff (zu C) und l_k²-Koeff (zu D).
Ablesen: bei welchem Grad erscheint jedes von {A, B, C, D} zuerst, und **teilen sich B und D je
einen Grad** (nötig, damit D = B automatisch wäre)? Dass B (Grad 5) und D (Grad 4) verschiedene
Grade haben, ist aus H197 bekannt (nicht blind); **neu** ist die Zerlegung des linearen Terms
(A, C) und die Frage, ob „Top-Grad = chiral" überhaupt eine konsistente Grad-Ordnung ergibt.

**(B) Fit-Test der sauberen Grad-Selektion (blind).** Drei geschachtelte Modelle:
1. Grad-selektiv-holomorph, 2 Param (A, B): C = 0 (linear blind), D = B (quadratisch chiral).
2. D = B, C frei, 3 Param (= H200-Modell 2).
3. frei A, B, C, D, 4 Param (= H196, Referenz).

## Entscheidungskriterium (vorab)

- **(K1) Grad-Selektion trägt**, wenn das saubere 2-Param-Modell (C = 0, D = B) die Massen
  innerhalb der Fehler trifft (χ²/dof akzeptabel, p > 0,05 bei dof = 4) **und** C = 0 mit den
  Daten verträglich ist (|C|/σ_C ≲ 2 im freien Fit).
- **(K2) Keine Grad-Selektion**, wenn C ≠ 0 scharf verlangt wird (|C|/σ_C ≫ 2) und das 2-Param-
  Modell verworfen ist, **und** B (Grad 5) und D (Grad 4) strukturell verschiedene Grade haben.
  Dann ist die Chiralität der Quintik **keine Grad-Ordnung**, sondern eine gradübergreifende
  Near-Equality (D ≈ B) zwischen einer Grad-4-ungeraden und einer Grad-5-geraden Kopplung; der
  lineare Term ist unabhängig ladungsgespalten (C ≠ 0).

**Erwartung** (aus H196, nicht Teil des blinden Teils B): C/A ≈ −2, also C deutlich ≠ 0 →
voraussichtlich **(K2)**. Dann lautet die Antwort auf (1): die „Grad-Selektion" ist kein Prinzip;
die Quintik-Chiralität ist eine isolierte Koinzidenz, und der ~0,9-%-Rest (D/B−1, Übergang zu (2))
ist der Grad-4/Grad-5-Versatz. Zusätzlich festzuhalten (nachträglich, kein Test): ob C/A einen
einfachen Wert (≈ −2?) trifft.

## Rechenwerkzeug

- sympy (symbolische Grad-Zerlegung, Vakuum-Reduktion in s, pr — wie k406) + numpy (Fits).
- Wolfram Language als unabhängige Kontrolle der Grad-Zerlegung (l_k- und l_k²-Koeffizienten je
  Grad) und der drei χ²-Minima.
- Qiskit nicht einschlägig.

## Festhalten

Werkzeugwahl, geprüfter Grad-Bereich, erste Abweichung, offene Voraussetzungen in die Ergebnis-
Notiz. Symbolische Nullreste, Rückgabewerte und Warnungen getrennt ausweisen. Der strukturelle
Teil (A) ist für B/D aus H197 bekannt (nicht blind); der lineare Teil und der Fit-Test (B) sind neu.
