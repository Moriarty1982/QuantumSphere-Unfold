# Ergebnis H199 (1b): Der Lauf der Kopplungen erzeugt D = B nicht — D/B ist skalenstabil

**Stand:** 27.11.2026. Vorab-Notiz `Vorab_Notiz_H199_Lauf_der_Kopplungen.md` (Commit a8ac697, vor der Rechnung). Skript
`k409_test_h199.py` (`k409_out.txt`), Wolfram-Gegenprobe `k409b_out.txt` (dominanter Top-Lauf, einig mit scipy).

Werkzeuge: Python (numpy, scipy.integrate für die 1-Schleifen-SM-RGEs, Fit wie k406); Wolfram Language zur Gegenprobe des
y_t-Laufs. Qiskit nicht nötig.

**Ergebnis in einem Satz:** D/B läuft von 1,0085 (M_Z) bis 1,0123 (Planck) — **0,4 % über 17 Dekaden** — und bleibt überall
nahe 1, fern von jedem symmetrieausgezeichneten Wert (0, ⅓, −1). Der Lauf der Kopplungen ist **nicht** die Quelle von D = B.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Urteil |
|---|---|---|
| H199a (nicht blind) | 1-Schleifen-SM-RGEs (g₁,g₂,g₃ + sechs Yukawas) integriert, M_Z → 10¹⁹ GeV; y_t: 0,967 → 0,401 (Wolfram einig). Massenverhältnisse innerhalb eines Sektors bleiben bis auf den Top-Term stabil (universelle Terme Y₂, g₂, g₃ kürzen sich). | bestätigt |
| H199b | D/B(μ): M_Z 1,0085 → Planck 1,0123. Bewegung 0,0038 (**0,4 %**). Nächster Symmetriewert (⅓) bleibt 0,68 entfernt. | **Befund: nein** |

## Was die Rechnung zeigt
- **Die Verhältnisse laufen schwach.** Der dominante Lauf ist die Top-Yukawa (0,97 → 0,40 bis zur Planck-Skala), aber die
  gemessene Up/Down-Struktur sitzt in den Massen**verhältnissen**, und dort kürzen sich die universellen Beiträge (die
  Yukawa-Spur Y₂ und die Eichkopplungen g₂, g₃). Was bleibt, verschiebt D/B um nicht einmal ein halbes Prozent über die ganzen
  17 Dekaden von M_Z bis zur Planck-Skala.
- **D = B ist skalenstabil.** Es gibt keine Skala μ*, an der D/B einen einfacheren (symmetrischen) Wert erreichte; D ≈ B ist bei
  M_Z genauso wie bei 10¹⁹ GeV. Also ist D = B **kein** heruntergelaufener Rand eines Hochskalen-Zustands.

## Lesart (ehrlich)
- **Befund: nein** (wie in der Vorab-Notiz als wahrscheinlich offengelegt). Der Lauf erklärt D = B nicht.
- **Positiver Gehalt im Zusammenspiel mit H198:** Die Skalenstabilität **stützt** die H198-Deutung. Wäre D = B ein dynamischer
  Laufeffekt, müsste es mit der Skala wandern. Dass es das nicht tut, passt dazu, dass D = B ein **struktureller** Zug ist —
  die Chiralität des Massenterms unter der Ladungs-U(1) (H198), ein skalenunabhängiges Symmetriemerkmal.

## Grenzen
1-Schleifen-SM-RGEs, grobe Flavour-Schwellen, keine CKM-Mischung (für Massenverhältnisse vernachlässigbar). 2-Schleife wurde
nicht gebraucht, da die 1-Schleifen-Bewegung mit 0,4 % weit von jedem Symmetriewert endet (2-Schleife würde das nicht umkehren).
Das Vakuum und die Zuordnung Paar→Generation (Permutation B) laufen nicht. OP3/OP4 bleiben offen; kein Guard berührt. Vergeben:
H199, k409. Nächste frei: H200, k410 (vor Vergabe prüfen).
