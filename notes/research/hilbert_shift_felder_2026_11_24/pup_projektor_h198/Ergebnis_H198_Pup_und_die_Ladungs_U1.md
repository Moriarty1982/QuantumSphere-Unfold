# Ergebnis H198 (1a): P_up ist die chirale Projektion der Ladungs-U(1) — „Down linear" heißt „der Massen-Quintik ist holomorph"

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H198_Pup_und_die_Ladungs_U1.md` (Commit a8ac697, vor der Rechnung; H198a nicht
blind). Skript `k408_test_h198.py` (`k408_out.txt`), Wolfram-Gegenprobe `k408b_out.txt`. Python (numpy, exakte Rationalzahlen)
und Wolfram (unabhängige Oktonion-Rekonstruktion) stimmen exakt überein.

Werkzeuge: Python für die Operatoridentität und die chirale Krümmung; Wolfram Language exakt für die Oktonion-Multiplikation
L_U und die Projektor-Eigenschaften. Qiskit nicht nötig.

**Ergebnis in einem Satz:** Der Up-Typ-Projektor aus H197 ist **exakt** die chirale Projektion der Ladungs-U(1),
**P_up = ½(1 + i·L_U)** (L_U = Linksmultiplikation mit U = e₇), und „Down linear" (D = B) ist damit **äquivalent** dazu, dass
das l_k²-Massenglied **holomorph (chiral) unter der Ladung** ist. P_up ist also ein bekanntes Objekt des Projekts; die freie
Zahl D/B ist auf **eine** Symmetrieannahme (Chiralität) zurückgeführt — die der F4-Rahmen erlaubt, aber nicht erzwingt.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Urteil |
|---|---|---|
| H198a (nicht blind) | **P_up = ½(1 + i·L_U) exakt** (‖Diff‖ = 0). (i·L_U)² = 1, P_up² = P_up, P_up + P_down = 1, P_up·P_down = 0 (alle = 0). Spur P_up = 18 (halber Farbblock, der +i-Eigenraum von L_U = Ladung ⅔ = Up). | bestätigt (exakt, Wolfram) |
| H198b | Ein l_k²-Term mit Operator O gibt (b_up, b_down) = (⟨O⟩_up, ⟨O⟩_down): **O = 1** (ladungsblind) → (1, 1), D/B = 0; **O = i·L_U** (J-Form Q₀−½) → (1, −1), rein ungerade, B = 0; **O = P_up** (chiral) → (1, 0), **b_down = 0, D/B = 1**. | **teilweise** |

## Was die Rechnung zeigt
- **P_up ist nicht exotisch.** Aus H182 ist auf dem Farbblock Q₀ = ½ + (i/6)·L_U. Also Q₀−½ = (i/6)·L_U (der **Generator** der
  Ladungs-U(1)), und P_up = 3(Q₀−⅓) = **½(1 + i·L_U)** — der **Projektor** auf eine Chiralität dieser U(1). Das ist exakt, nicht
  genähert.
- **„Down linear" = Holomorphie.** Das l_k²-Glied koppelt über einen Operator O im Ladungsraum. Ist O **chiral** (nur +Chiralität,
  O ∝ P_up), so verschwindet seine Krümmung auf dem Down-Typ (P_up·Down = 0) und D = B folgt. Ist O ladungsblind (F4), gilt D = 0;
  ist O die reine J-Form, gilt B = 0 (antisymmetrisch). Nur die **chirale** Kopplung trifft das gemessene „Up quadratisch, Down
  linear".
- **Erste Deutung der Stärke-Asymmetrie.** H197 hatte die Stärke als „freie Zahl, von keiner Symmetrie erzeugt" stehen lassen.
  H198 gibt ihr einen Namen: sie ist die **Chiralität der Ladung**. Die offene Frage ist damit schärfer und kleiner: nicht mehr
  „woher die Zahl 1,009", sondern „warum ist der Massenterm chiral, während die Kinetik F4-symmetrisch (ladungsblind) ist".

## Lesart (ehrlich)
- **Hergeleitet:** die Identität P_up = ½(1 + i·L_U) (exakt) und die Äquivalenz „D = B ⇔ l_k²-Term chiral".
- **Zusätzliche Annahme (nicht erzwungen):** dass der Massen-Quintik holomorph unter der Ladungs-U(1) ist. Der F4-Rahmen lässt
  das zu, verlangt es aber nicht (H178: die Ladungs-U(1) ist nicht gefordert; die Kinetik ist ladungsblind). D = B ist damit auf
  **eine Symmetrieannahme** reduziert, nicht auf null.
- **Teilweise**, weil: P_up ist mit einem bekannten Objekt identifiziert (Gewinn), aber die Annahme „chiral" ist neu, und die
  übrigen Koeffizienten (A, B über beide Sektoren, C) bleiben frei.

## Zusammenhang mit H199 (1b)
H199 zeigt, dass D/B über 17 Dekaden nur 0,4 % läuft — D = B ist **skalenstabil**. Das passt zu H198: eine Chiralität ist ein
struktureller, skalenunabhängiger Zug, kein Laufeffekt. Die beiden Richtungen stützen sich gegenseitig.

## Grenzen
Dieselbe Zerlegung (ruhendes Vakuum, Krümmung/Norm, Farbblock). Die Operatoridentität ist exakt; die „Holomorphie des Quintik"
ist eine benannte, aber zusätzliche Annahme — H198 beweist nicht, dass sie gelten muss, sondern dass D = B genau zu ihr äquivalent
ist. Ein voller nächster Schritt müsste zeigen, **warum** der Massenterm chiral sein soll, während die Kinetik es nicht ist (etwa
aus einer chiralen/holomorphen Struktur der Feldgleichung selbst). OP3/OP4 bleiben offen; kein Guard berührt. Vergeben: H198, k408.
Nächste frei: H200, k410 (vor Vergabe prüfen).
