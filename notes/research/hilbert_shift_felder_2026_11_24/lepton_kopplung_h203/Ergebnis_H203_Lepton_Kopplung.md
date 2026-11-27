# Ergebnis H203 / k413 — Binden die Lepton-Massen / δ die Quark-Kopplungen?

**Datum:** 2026-11-27
**Vorab:** `Vorab_H203_Lepton_Kopplung.md` (committet vor der Rechnung)
**Skripte:** `k413_test_h203.py` (numpy, Maschinerie aus k387/H184), `k413b_kontrolle.wl` (Wolfram)
**Ausgaben:** `k413_out.txt`, `k413b_out.txt`
**Freigabe:** Autor wählte per Karte „An Lepton-Sektor / δ koppeln" (27.11., 12:07 UTC).

## Verdikt: **nein** (Kriterium K2) — der Lepton-Sektor bindet die Quark-Kopplungen nicht

In der Lesart „ein Vakuum, Sektoren schwingen" ist der Lepton-Sektor **blind** gegen die
Kopplungen, die die Quarkmassen bestimmen. Die Lepton-Massen und δ legen die Quark-Kopplungen
**nicht** fest; D/B bleibt frei. δ (das Vakuum) ist geteilt und steckt schon in den l_k, legt
aber die Kopplungsstärken nicht fest.

## (A) Kontrolle — Stationarität macht die Quarks masselos (reproduziert H184; Wolfram exakt)

Ein F₄-invariantes Potential, das W₀ stationär macht (v′(l) = (l−l₁)(l−l₂)(l−l₃)):
- **Farbfrequenzen (Quarks) = 0** (max |EV| = 1,6·10⁻¹²; Wolfram: alle drei Paare exakt 0).
- **farbloser Block:** drei massive Moden (−1,51; 1,92; 7,09) = die Lepton-Moden, plus sechs
  Nullrichtungen aus der Familien-SU(3).

Die Regel (H184, Wolfram bestätigt): Farbmoden-Frequenz² der Mode (i,j) = 2(v′(l_i)−v′(l_j))/(l_i−l_j),
null sobald W₀ stationär ist. **Die Stationarität, die die Leptonen (als massive Moden) bindet,
macht die Quarks masselos.** Quarkmassen brauchen also F₄-brechende (U-auszeichnende) Terme.

## (B) Blindheit — Kopplungen, die die Quarks ändern, aber die Leptonen nicht

Lineare Abbildungen Kopplung → zweite Variation, getrennt nach Sektor (13 Spur-Invarianten):

- Rang Kopplung → **farblose** Hesse (Leptonen): **6** von 13.
- Rang Kopplung → **Farb**-Hesse (Quarks): **3** von 13.
- Kopplungsrichtungen, die den **farblosen** Sektor völlig unberührt lassen (Hesse **und**
  Gradient = 0, also auch die Stationarität): **7**.
- Davon, die die **Farb**-(Quark-)Frequenzen ändern: **alle 7**.

Eine Beispiel-Blindrichtung (antisymmetrische W-vs-W_U-Kombination, z. B. +Tr W² − Tr W_U²,
+Tr W³ − Tr W_U³, +(Tr W)²Tr W² − (Tr W)²Tr W_U², …) lässt die farblose Hesse (7·10⁻¹⁵) und den
farblosen Gradienten (1·10⁻¹⁵) exakt unberührt, verschiebt aber die Farb-(Quark-)Frequenzen auf
{32,6; 39,1; 41,2}. **Der Lepton-Sektor sieht diese Kopplungen nicht.**

## Einordnung

- Die Quarkmassen messen in dieser Lesart die **Brechung F₄ → SU(3)_c** durch die Wahl von U
  (die U-auszeichnenden Terme), **nicht** das Leptonvakuum. Genau diese Terme sind für den
  farblosen Lepton-Sektor unsichtbar (W-vs-W_U-antisymmetrische Kombinationen heben sich dort auf).
- Daher **bindet die Lepton-Kopplung die Quark-Kopplungen nicht**. δ ist zwar geteilt (dasselbe
  Vakuum) und bestimmt die l_k-Abhängigkeit der Quark-Formel — aber die vier Kopplungsstärken
  (A, B, C, D), die H202 als frei fand, bleiben frei. Die Lepton-Kopplung ist **nicht** die
  gesuchte neue bindende Eingabe.
- Das ist ein sauberes **negatives** Resultat für die vom Autor gewählte Route. Es engt die
  verbleibenden Möglichkeiten ein: die Quark-Kopplungen sind F₄-brechende Größen, die weder der
  Grad (H201), die Symmetrie (H197), der Lauf (H199), die Holomorphie (H200), die minimale
  Invariant-Zahl (H202) noch der Lepton-Sektor (H203) festlegt.

## Werkzeuge, Bereich, Grenzen

- **Werkzeuge:** numpy (zweite Variation der 13 Spur-Invarianten auf farblosen/Farbrichtungen bei
  W₀, Rang- und Nullraum-Analyse; Maschinerie aus k387/H184) + Wolfram (H184-Regel und
  Stationarität → masselos, exakt). Qiskit nicht einschlägig.
- **Geprüfter Bereich:** die 13 Spur-Invarianten (F₄-invariant und U-abhängig) bis effektiv Grad 4
  in W; zweite Variation bei W₀ (K = ⅔, δ = 2/9).
- **Entscheidende Stelle:** 7 Kopplungsrichtungen lassen den Lepton-Sektor (Hesse + Gradient)
  exakt unberührt und ändern dennoch die Quarkfrequenzen.
- **Grenzen / Nuance:** reelle Feld-Ebene (ein Quarktyp, H184). Die Up/Down-Spaltung (C, D, und
  damit D/B exakt) braucht das komplexe H₃(ℂ⊗𝕆) (H182/H185) und ist hier nicht gerechnet. H203
  beantwortet die vorgelagerte Frage — **bindet der Lepton-Sektor die quarkbestimmenden Kopplungen
  überhaupt** — mit nein; damit erübrigt sich die komplexe Verfeinerung für diese Route.
- Keine symbolischen Nullreste; Teil A nicht blind (reproduziert H184), Teil B blind.

Nächste freie Nummern nach H203/k413: H204, k414 (vor Vergabe gegen `main` prüfen; Parallel-Thread
HS(−1) vergibt ebenfalls k-Nummern).
