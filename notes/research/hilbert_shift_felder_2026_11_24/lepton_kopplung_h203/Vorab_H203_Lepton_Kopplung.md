# Vorab-Notiz H203 / k413 — Legen die Lepton-Massen / δ die Quark-Kopplungen fest?

**Datum:** 2026-11-27
**Strang:** Quarkmassen, Feldgleichung (neue Eingabe nach H202)
**Nummern:** Test H203, Skript k413 (vor Push gegen `main` geprüft; Parallel-Thread HS(−1) vergibt ebenfalls k-Nummern)
**Freigabe:** Autor wählte per Karte „An Lepton-Sektor / δ koppeln" (27.11., 12:07 UTC).

## Frage

H202 zeigte: die vier Quark-Kopplungen (A, B, C, D) sind im bisherigen Rahmen frei. Die vom
Autor gewählte neue Eingabe: Binden die **Lepton-Massen** (und δ = 2/9) diese Kopplungen? In der
vom Autor nach H183 gewählten Lesart **„ein Vakuum, Sektoren schwingen"** (H184) sind Lepton- und
Quarkmassen **Krümmungen desselben Potentials** um dasselbe Vakuum W₀:

- **Lepton-Moden** = die farblosen Richtungen (9 Stück; davon die drei massiven = die Leptonen).
- **Quark-Moden** = die 18 Farbrichtungen (Frequenzquadrate mit Vielfachheit 6 = Farbtriplett).

Wenn die drei Lepton-Massen + die Vakuum-Stationarität die Kopplungen des Potentials festlegen,
wären die Quarkfrequenzen (und das Verhältnis, das D/B entspricht) **vorhergesagt**.

## Vorwissen geprüft

- `feldgleichung_h183/` (H183): Lepton- und Quarkzustand nicht zugleich Vakua eines Grad-4-
  Potentials; Autor wählte „ein Vakuum, Sektoren schwingen".
- `schwingungen_h184/k387_test_h184.py` (H184): **Regel (Wolfram exakt):** für ein F₄-invariantes
  Potential Σ v(l_k) ist das Farbmoden-Frequenzquadrat der Mode (i,j) = 2(v′(l_i)−v′(l_j))/(l_i−l_j);
  ist W₀ stationär (v′(l_k) = 0), sind **alle Farbschwingungen masselos** (Bahn von W₀ unter F₄).
  Folge: Quark-(Farb-)Frequenzen kommen allein aus **U-auszeichnenden** (F₄-brechenden) Termen
  (Tr W²∘W_U², Tr W²·Tr W_U²). Maschinerie (toW/fromW, hess_all auf colidx/sngidx, 13 Spur-
  Invarianten, W0) wird wiederverwendet.
- `rest_frei_h202/`, `grad_selektion_h201/`, `ladung_h182/`, `updown_h185/`: Quark-Massenmodell
  A,B,C,D; C,D (Up/Down-Spaltung) aus der ladungsungeraden Form, nur im Farbblock (H182).
- Lepton-/Vakuum-Eigenwerte l = [0,04035; 0,580212; 2,379438] (K = ⅔, δ = 2/9).

## Test

Alles mit der k387-Maschinerie (zweite Variation der 13 Spur-Invarianten auf farblosen und
Farbrichtungen bei W₀), numpy; Wolfram zur Kontrolle der Regel und des Rangs.

**(A) Kontrolle (nicht blind, reproduziert H184).** F₄-invariantes stationäres Potential
(v′ = (l−l₁)(l−l₂)(l−l₃)): Farbfrequenzen = 0 (masselos), farbloser Block drei massive Moden
(die Lepton-Massen). Bestätigt, dass die F₄-invariante, lepton-bindende Stationarität die Quarks
masselos lässt.

**(B) Rang/Blindheit (blind).** Baue die lineare Abbildung (Kopplungen der 13 Invarianten) →
(farblose Hesse-Matrix = Lepton-Sektor) und → (Farb-Hesse-Matrix = Quark-Sektor). Bestimme:
1. Welche Kopplungen ändern die **Quark**-(Farb-)Frequenzen (Rang der Farb-Abbildung)?
2. Sind die Lepton-Massen (farblose massive Moden) bei fester Vakuum-Stationarität **blind**
   gegen diese Kopplungen? Konkret: Gibt es eine Kopplungsrichtung, die die Farb-(Quark-)
   Frequenzen ändert, aber die farblosen Lepton-Massen und die Stationarität **nicht**?

## Entscheidungskriterium (vorab)

- **(K1) Lepton-Sektor bindet die Quarks**, wenn jede Kopplungsrichtung, die die Quark-
  Frequenzen ändert, auch die Lepton-Massen ändert (keine blinde Richtung) — dann legen die drei
  Lepton-Massen + δ die Quarkfrequenzen fest, und das Verhältnis (↔ D/B) ist eine **Vorhersage**.
- **(K2) Lepton-Sektor bindet die Quarks nicht**, wenn es eine Kopplungsrichtung gibt, die die
  Quark-Frequenzen ändert, aber Lepton-Massen und Stationarität fest lässt. Dann sind die Quark-
  Kopplungen (F₄-brechende U-Terme) **unabhängig** vom Lepton-Sektor; δ (Vakuum) ist geteilt und
  steckt schon in l_k, legt aber die Kopplungsstärken nicht fest.

**Erwartung** (aus H184, nicht blind für Teil A): voraussichtlich **(K2)** — die Quarks sitzen in
den F₄-brechenden U-Termen, die der farblose Lepton-Sektor über die Stationarität nicht bindet.
Dann ist die Antwort auf die Lepton-Kopplung **nein** (mit der Nuance: δ ist geteilt, aber schon
genutzt). Das wäre eine klare Grenze: der Lepton-Sektor liefert nicht die neue bindende Eingabe.

## Grenze / Nuance

Diese Rechnung läuft auf der **reellen** Feld-Ebene (ein Quarktyp, H184); die Up/Down-Spaltung
(C, D, hence D/B exakt) braucht das komplexe H₃(ℂ⊗𝕆) (H182/H185) und ist hier nicht voll gerechnet.
H203 beantwortet daher präzise: **bindet der Lepton-Sektor die quarkbestimmenden Kopplungen
überhaupt** (die Stärke der U-Terme). Trägt das nicht, erübrigt sich die komplexe Verfeinerung.

## Rechenwerkzeug

- numpy (zweite Variation aus k387, Rang-/Blindheits-Analyse). Wolfram zur Kontrolle der H184-Regel
  und des Rangs. Qiskit nicht einschlägig.

## Festhalten

Werkzeugwahl, geprüfter Bereich, erste Abweichung, offene Voraussetzungen in die Ergebnis-Notiz.
Teil A nicht blind (reproduziert H184), Teil B blind.
