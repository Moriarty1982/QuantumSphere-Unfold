# Ergebnis H197: Keine Symmetrie erzwingt D = B — „Down linear" ist eine empirische Auswahlregel

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H197_Erzwingt_eine_Symmetrie_D_gleich_B.md` (Commit 7d39915, vor der Rechnung;
H197a/d teils nicht blind, siehe dort). Skript `k406_test_h197.py` (`k406_out.txt`), Wolfram-Gegenprobe `k406b_out.txt`.
Python (sympy/numpy) und Wolfram (exakt) stimmen in allen symbolischen Werten überein.

Werkzeuge: Python für die Reduktionen, die Rang- und die festen-D/B-Fits und die Kontrolle; Wolfram Language exakt für die
Vakuum-Reduktion der Krümmungen und die J-Kovarianz der Ladungsformen. Qiskit nicht nötig (keine Schaltung, kein Messablauf).

**Ergebnis in einem Satz:** D = B ist von **keiner** Symmetrie des H182/F4-Rahmens erzwungen — die ladungsgerade Quelle (B, Grad 5)
und die ladungsungerade (D, Grad 4) haben unabhängige Kopplungen, die einzige von J ausgezeichnete Ladungsform (Q₀−½) liefert ein
antisymmetrisches l_k² (D/B = −1), und die Daten verlangen scharf D/B = 1,009 ± 0,001, meilenweit von jedem symmetrienahen Wert.
„Down linear" ist eine empirische Auswahlregel (das quadratische Glied lebt nur auf dem Up-Typ), die der Rahmen nicht erzeugt.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Urteil |
|---|---|---|
| H197a (nicht blind) | Ladungsgerades l_k² erscheint erst bei Potentialgrad **5** (F4-Krümmung, Koeff −30); ladungsungerades l_k² existiert schon bei Grad **4** (H186: c4/c5 = 2−l_k²/3, c7/c9 = 3/2−l_k+l_k²/6, c11 = 7/2−l_k−l_k²/6). Verschiedener Grad, verschiedene Invarianz. | bestätigt (exakt, Wolfram) |
| H197c (Rang) | Die Abbildung (g_gerade, g_ungerade) → (B, D) hat **Rang 2**: die Grad-5-gerade Quelle liefert (B,D)=(−30,0), die Grad-4-ungerade (c7/c9) (0,+⅙). **D/B ist frei.** | bestätigt |
| H197d (J-Kovarianz) | Q₀ hat auf dem Farbblock die Eigenwerte ⅓, ⅔; J: Q₀→1−Q₀. **h = Q₀−½** ist J-Eigenform (Eigenwert −1, ladungsungerade). **Q₀−⅓** und **P_up = 3(Q₀−⅓)** sind **keine** Eigenformen; J bildet P_up (Werte Up 1, Down 0) auf P_down ab. | bestätigt |
| H197b (Daten gegen feste D/B) | Fester 3-Param-Fit mit D/B ∈ {0, ⅓, −1}: χ² = 60614 / 60497 / 60311 — **alle ausgeschlossen**. Freier 4-Param-Fit: χ² = 7,91 bei D/B = 1,009. | **Befund: nein** (Symmetrie erzwingt D=B nicht) |
| H197c (Schärfe) | χ²(D/B)-Minimum 7,91 bei D/B = 1,0086; **2σ-Fenster D/B ∈ [1,0076; 1,0095]** (Breite 0,002). Die leichten, präzisen Down-Massen pinnen D/B extrem scharf. | — |
| Kontrolle | 2000 erfundene Massenpaare: fester-D/B-Fit (0, ⅓, −1) trifft in **0,0 %** mit χ²<12; auch der freie 4-Param-Fit 0,0 %. | — |

## Was die Rechnung zeigt
- **Zwei getrennte Quellen.** Der Up/Down-Split im **linearen** l_k ist billig (ladungsungerade Terme ab Grad 2–4), aber im
  **quadratischen** l_k² kommen die gerade und die ungerade Komponente aus **verschiedenen** Stellen: B aus der reinen,
  ladungsblinden F4-Invariante vom Grad 5; D aus einer ladungsungeraden (F4-brechenden) Form, die schon bei Grad 4 ein l_k² trägt.
  Zwei unabhängige Kopplungen ⇒ D/B ist ein freier Parameter, den keine Relation festnagelt (Rang 2).
- **Die Symmetrie zeigt in die falsche Richtung.** Die von J (H182) ausgezeichnete ladungsungerade Form ist genau Q₀−½: sie ist
  **rein** ungerade (J-Eigenwert −1). Ein l_k²-Term, der nur über Q₀−½ koppelt, gäbe b_up = +D, b_down = −D, also
  |b_up| = |b_down| (D/B = −1 relativ zu einem separaten geraden Term, oder B = 0). Das ist das **Gegenteil** von „Down aus":
  die Symmetrie bevorzugt die antisymmetrische Aufteilung, nicht das Abschalten einer Seite.
- **D = B ist der Up-Typ-Projektor — und der ist nicht symmetrisch.** D = B ⇔ l_k²-Koeffizient ∝ (1+s)/2 = P_up = 3(Q₀−⅓).
  P_up ist kein J-Eigenobjekt: J bildet P_up auf P_down ab, vertauscht also Up und Down. Diese Vertauschung gibt es im Farbblock
  gerade **nicht** (der Kern von H182: J erhält dort die Ladung). P_up ist damit erlaubt, aber als freie Kopplung, von keiner
  Symmetrie erzwungen.
- **Die Daten sind eindeutig und scharf.** Sie verlangen D/B = 1,009 ± 0,001. Die drei symmetrie­nahen Werte (0 ladungsblind,
  ⅓ lineare Ladung, −1 reine J-Form) liegen bei Δχ² ≈ 6·10⁴. Es gibt kein „fast": der Rahmen trifft den nötigen Wert nicht
  einmal näherungsweise.

## Lesart
- **Antwort auf die Frage des Autors:** **Nein.** Keine Symmetrie des bestehenden Rahmens erzwingt D = B. Die aus H196 abgelesene
  Beziehung D ≈ B ist ein Fit, kein Zwang.
- **Positiver Gehalt:** Der Befund ist nicht leer. Er benennt genau, **was** fehlt: die Up/Down-Asymmetrie der *Stärke* des
  quadratischen Glieds ist ein **Up-Typ-Projektor** P_up = 3(Q₀−⅓). Das ist ein konkretes Objekt. Der Rahmen erzeugt es nicht aus
  einer Symmetrie; eine Herleitung müsste P_up aus einer **neuen Eingabe** bekommen.
- **Methodischer Gewinn:** Dies war eine Richtungsprüfung (ist das Ziel D=B eine gesetzte Eingabe?) statt eines weiteren Fits. Sie
  schließt die Baustein-Suche im selben Rahmen ab: mehr Terme desselben Baukastens können D/B nur weiter frei lassen, nicht binden.

## Bilanz der Setzungen (Pflicht nach ≥ 2× „teilweise" zur selben Voraussetzung)
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H193 | getrennte Felder je HS-Stufe | — (widerlegt: stufenfeste Verhältnisse) | zurück zur gemeinsamen Form |
| H194 | H188-Form (nachträglich) | Spezifität: nur Zuordnung B, Zufalls-l 0,0 % | b/a je Sektor frei |
| H195 | — | Nenner (l_i+l_j)² (Peirce, W²-Norm); l_k² ab Grad 5 | Zähler-Koeffizienten frei |
| H196 | volle Ladungsstruktur (4 Param) | Up/Down-Ort = Vorzeichen des ladungsungeraden l_k² | Stärke D (D≈B gefittet) |
| **H197** | **nichts Neues** (nur bestehende Rechnungen zerlegt) | **D/B ist frei; kein Symmetriezwang; die nötige Kopplung ist P_up, nicht J-kovariant** | **raus aus dem Baukasten: nur eine neue Eingabe kann die Stärke binden** |

Vierter „teilweise"-Nachbar in Folge zur Quark-Koeffizienten-Frage, aber **diese** Runde beantwortet eine Ja/Nein-Frage klar (nein)
und verschiebt die offene Wahl aus dem Baukasten heraus. **Dem Autor vorzulegende Weggabelung:** Der Rahmen liefert die
Stärke-Asymmetrie (P_up) nicht. Weiter lohnt nur eine neue Eingabe — (a) eine Beziehung P_up ↔ bekannte Projektgröße (z. B. eine
Projektion im HS-Turm oder der Oktantstruktur), oder (b) Dynamik/Lauf der Kopplungen. Ein weiterer Term im selben F4/Ladungs-Baukasten
bringt nichts.

## Grenzen
Dieselbe Zerlegung wie H182/H186/H195/H196 (ein Feld, zweite Variation um das ruhende Vakuum, Krümmung/kinetische Norm). Die
ladungsungeraden Krümmungen sind aus H186 übernommen (dort über vier Vakua und Wolfram exakt). Die geprüften symmetrie­nahen D/B
sind {0, ⅓, −1} (ladungsblind, lineare Ladung, reine J-Form) plus die J-Kovarianz von P_up; eine höhere, hier nicht konstruierte
Ladungsstruktur ist nicht ausgeschlossen, müsste aber P_up erzeugen, ohne die Up↔Down-Symmetrie einzuführen, die H182 im Farbblock
verbietet. Winkel/Massen bei M_Z. Kein Guard berührt; OP3/OP4 bleiben offen. Vergeben: H197, k406. Nächste frei: H198, k406
(vor Vergabe prüfen).
