# Vorab-Notiz H200 / k410 — Ist die Feldgleichung holomorph (chiral) unter der Ladung?

**Datum:** 2026-11-27
**Strang:** Quarkmassen, Feldgleichung (Fortsetzung nach H198/H199)
**Nummern:** Test H200, Skript k410 (vor dem Push erneut gegen `main` geprüft; der Parallel-Thread HS(−1) vergibt ebenfalls k-Nummern)

## Ausgangslage

H198 (k408) hat den Up-Typ-Projektor exakt bestimmt:

    P_up = ½(1 + i·L_U),   L_U = Linksmultiplikation mit U = e₇

Das ist der Projektor auf den +i-Eigenraum von L_U, also **eine Chiralität der Ladungs-U(1)**.
„Down linear" (D = B im Massenmodell) ist gleichbedeutend damit, dass das l_k²-Massenglied
**holomorph/chiral** unter der Ladung ankoppelt: nur die Up-Chiralität trägt, b_down = 0.

H199 (k409) hat gezeigt: D = B ist skalenstabil (0,4 % Lauf über 17 Dekaden), also **kein**
Laufeffekt — das stützt die strukturelle (chirale) Lesart statt einer dynamischen.

Offene, geschärfte Frage nach H198/H199: **Warum ist der Massenterm chiral, während die
Kinetik F4-symmetrisch (ladungsblind) ist?** Kandidat aus der Memo: eine chirale/holomorphe
Struktur der Feldgleichung selbst.

Diese Notiz prüft diesen Kandidaten direkt.

## Vorwissen geprüft

- `ladung_h182/` (H182): Q₀ = ½ + (i/6)·L_U; Q₀ − ½ = (i/6)L_U ist die einzige J-ungerade
  hermitesche Ladungsform. J: Q₀ → 1 − Q₀ (Up ↔ Down).
- `pup_projektor_h198/` (H198): P_up = ½(1 + iL_U) exakt; Rang 18 von 36; (iL_U)² = 1.
  Kopplungsmuster für den l_k²-Operator O: O = 1 (ladungsblind) → D/B = 0; O = iL_U (J-Form)
  → reines Ungerade, B = 0 → D/B = −∞; O = P_up (chiral) → b_down = 0 → D/B = +1.
- `lauf_kopplungen_h199/` (H199): D/B läuft 1,0085 → 1,0123 (0,4 %) M_Z→Planck; kein Laufeffekt.
- `symmetrie_db_h197/` (H197): keine Symmetrie erzwingt D = B; Daten verlangen scharf
  D/B = 1,009 ± 0,001 (2σ-Fenster [1,0076; 1,0095], Breite 0,0019); Symmetriewerte {0, ⅓, −1}
  bei Δχ² ≈ 6·10⁴. B (ladungsgerades l_k²) braucht F4-Invariante Grad 5; D (ladungsungerades
  l_k²) existiert schon bei Grad 4 → unabhängige Kopplungen, D/B frei.
- `ladung_zaehler_h196/` (H196): Modell m_s(k) = [A·l_k + B·l_k² + s·(C·l_k + D·l_k²)]/(l_i+l_j)²,
  s = +1 (Up), s = −1 (Down). 4-Param-Fit χ² = 7,9; b_up = B+D stark, b_down = B−D ≈ 0.
- `feldgleichung_form_h195/` (H195): Nenner (l_i+l_j)² hergeleitet; Zähler frei.
- Vakuum-Identitäten: l_i+l_j = 3−l_k, l_i²+l_j² = 6−l_k², l_i·l_j = 3/2−3l_k+l_k².
- Quarkdaten (M_Z-Yukawa, k376): up = [7,04e-6; 3,56e-3; 0,967], σ = [0,15e-6; 0,06e-3; 0,004];
  down = [1,54e-5; 3,06e-4; 1,630e-2], σ = [0,02e-5; 0,04e-4; 0,009e-2]. Zuordnung B
  (Paar-Permutation [2,1,0]).

## Begriff: holomorph/chiral unter der Ladung

Der Zähler des Massenterms ist ein Polynom im Ladungsoperator, der auf den Off-Diagonal-Mode
(Quark) wirkt. Jedes Monom l_k^n koppelt über einen Operator O auf dem Farbblock:

- **ladungsblind:** O ∝ 1 → gleicher Beitrag für Up (s=+1) und Down (s=−1) → gerade Kopplung.
- **chiral/holomorph:** O ∝ P_up → wirkt nur auf die Up-Chiralität → für Down (s=−1) null.
  Eine *holomorphe* Potentialfunktion V(Φ) hängt nur von Φ (dem +i-Eigenmode, der Up-Chiralität)
  ab, nicht von Φ̄; jeder ihrer Terme ist dann ∝ P_up.

Zuordnung zum Massenmodell (pro Monom, Koeffizient gerade/ungerade):

- l_k-Term: a_up = A+C, a_down = A−C.
- l_k²-Term: b_up = B+D, b_down = B−D.

Wäre **die ganze** Feldgleichung holomorph (Zähler vollständig aus P_up gebaut), dann sind
*beide* Terme chiral: a_down = 0 **und** b_down = 0 → der Zähler des Down-Massenterms
verschwindet identisch → **Down-Quarks masselos**.

## Hypothese

H200: Die Feldgleichung ist **nicht** global holomorph. Chiralität ist **gradselektiv** —
nur der Term höchsten Grades (l_k², Quintik) koppelt chiral (∝ P_up, b_down ≈ 0), der lineare
Term bleibt ladungsblind (a_down ≠ 0). Zusätzlich ist selbst die Quintik nur chiral-*dominant*,
nicht exakt chiral, weil die Daten D/B = 1,009 ≠ 1 verlangen.

## Test und Entscheidungskriterium

Drei Modelle werden am selben Quarkdatensatz (6 Massen, Zuordnung B, Nenner (l_i+l_j)²) gefittet
und per χ² verglichen. Alle Rechnungen mit Peirce/Vakuum-Reduktion in elementar-symmetrischen
Variablen (s = l_i+l_j, pr = l_i·l_j), um den bekannten Reduktionsfehler aus H197 zu vermeiden.

1. **Voll holomorph (1 Arm, *nicht blind*):** Zähler = Chiralprojektor auf *jeden* Term, d. h.
   a_down = 0 und b_down = 0. Analytisch steht fest: Down-Massen aus dem Zähler = 0.
   → Erwartung: χ² katastrophal (Down-Massen können nicht reproduziert werden). **Dieser Arm ist
   nicht blind** (analytisch fixiert); er wird als Kontrolle mitgerechnet, nicht als Vorhersage.

2. **Gradselektiv-chiral (strikt, 3 Param A, C, B=D):** linearer Term ladungsblind+ungerade
   (A, C frei), l_k²-Term strikt chiral (D = B, 1 Kopplung). Fit → χ²₃.

3. **Voll (4 Param, Referenz = H196):** A, B, C, D frei. Fit → χ²₄.

**Kriterium (vorab festgelegt):**

- (K1) **Voll holomorph verworfen**, wenn χ²(Modell 1) ≫ χ²₄ und die Down-Massen nicht
  innerhalb 5σ getroffen werden. (Nicht-blinder Kontrollarm.)
- (K2) **Gradselektive Chiralität trägt**, wenn das strikte D=B-Modell (3 Param) die Massen
  innerhalb der Fehler trifft: χ²₃/dof akzeptabel (p > 0,05 bei dof = 6−3 = 3) **und** der
  verbleibende Abstand D/B − 1 im RG-Budget aus H199 liegt (≤ 0,4 %).
- (K3) **Chiralität nur approximativ**, wenn D = B von den Daten verworfen wird (χ²₃ − χ²₄ groß,
  D/B = 1,009 bei vielen σ) bzw. der Rest D/B − 1 ≈ 0,9 % das RG-Budget (0,4 %) übersteigt.

Erwartung (aus H197, nicht Teil des blinden Tests): D/B = 1,009 ± 0,001 ist 9σ von 1 entfernt,
also dürfte **(K3)** eintreten → Verdikt voraussichtlich **teilweise**: globale Holomorphie
sauber verworfen, Muster (b_down ≈ 0, Up quadratisch-dominant) durch die chirale Lesart erklärt,
aber strikte Chiralität bei ~9σ ausgeschlossen und der ~0,9-%-Rest über dem RG-Budget. Die
geschärfte offene Frage wäre dann: **was zeichnet gerade die Quintik für die Chiralität aus,
und woher kommt der ~0,9-%-ladungsblinde Beimischungsanteil?**

## Rechenwerkzeug

- Python/numpy für Operatorbau (Farbblock, L_U, P_up) und die χ²-Fits — wie k408/k409.
- Wolfram Language als unabhängige Kontrolle für (a) die holomorph⇒Down-masselos-Identität
  (symbolisch: P_up angewandt auf s=−1 gibt 0) und (b) die χ²-Minima der drei Modelle.
- Qiskit nicht einschlägig (keine Schaltung/Messung).

## Festhalten

Werkzeugwahl, geprüfter Bereich, erste Abweichung und offene Voraussetzungen kommen in die
Ergebnis-Notiz. Symbolische Nullreste, Rückgabewerte und Warnungen werden getrennt ausgewiesen.
