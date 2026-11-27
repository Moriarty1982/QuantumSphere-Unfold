# Ergebnis H202 / k412 — Folgt der ~0,9-%-Rest (D/B−1) aus den Invariant-Koeffizienten, oder ist er frei?

**Datum:** 2026-11-27
**Vorab:** `Vorab_H202_Rest_frei.md` (committet vor der Rechnung)
**Skripte:** `k412_test_h202.py` (numpy), `k412b_kontrolle.wl` (Wolfram, unabhängig)
**Ausgaben:** `k412_out.txt`, `k412b_out.txt`
**Freigabe:** Autor „ja bitte" (27.11., 11:26 UTC) für (1) und (2).

## Verdikt: **D/B ist frei** (Kriterium K2) — der ~0,9-%-Rest ist ein Eingabewert

Weder Grad (H201), Symmetrie (H197), Holomorphie (H200) noch die minimale Invariant-Zahl (H202)
legen D/B fest. Alle Bausteine sind identifiziert, aber die Kopplungen sind frei. Damit ist der
chirale/holomorphe Strang **durchgerechnet und abgeschlossen**; ein weiterer Schritt im selben
Rahmen bringt nichts Neues.

## (A) Rang der Abbildung (sympy/numpy und Wolfram exakt einig)

Die Strukturmatrix (A, B, C, D) × 8 Kopplungen (gerade F4-Invarianten g₃…g₆, ungerade H186-Formen):
- **Rang = 4.** Gerade Kopplungen betreffen nur (A, B), ungerade nur (C, D) → Blöcke 2 + 2.
- Rang (A,B)-Block = 2, Rang (C,D)-Block = 2.

→ Alle vier effektiven Koeffizienten sind **unabhängig** einstellbar, also auch D/B. (Für den
l_k²-Block allein war das schon H197; neu ist der volle Satz inkl. linearem Term — nicht blind.)

## (B) Minimale Invariant-Basis (blind)

Bester χ² je Kopplungszahl (Fit aller sechs Massen, Zuordnung B, Nenner (l_i+l_j)²):

| Kopplungen | bestes χ² | dof | p | Basis |
|---|---|---|---|---|
| 2 | 39 895 | 4 | 0 | (g₆, c4/c5) |
| 3 | 8 312 | 3 | 0 | (g₃, g₆, c4/c5) |
| **4** | **7,91** | 2 | 0,019 | (g₃, g₆, c2, c7/c9) |

Jede Basis mit ≤ 3 Kopplungen ist **verworfen** (χ² ≥ 8 312). Erst 4 Kopplungen treffen die Massen
(χ² = 7,91, reproduziert A = 1,082e-3, B = 3,291e-2, C = −2,224e-3, D = 3,320e-2, D/B = 1,0085).
**Minimal nötig: 2 gerade (für A, B) + 2 ungerade (für C, D) = 4 Kopplungen = 4 Koeffizienten.**
Grund: der l_k²-gerade Anteil B verschwindet bei Grad 4 und braucht die Grad-5-Kopplung separat,
und keine einzelne ungerade Form trifft D/C = −14,9 (c7/c9 gäbe −1/6, c11 gäbe +1/6).

## Einordnung — Abschluss des chiralen Strangs und Weggabelung

Der ganze Strang H195–H202 zum Quark-Massenursprung lässt sich jetzt so zusammenfassen:

- **Nenner** (l_i+l_j)² hergeleitet (H195, Peirce/W²-Norm).
- **Funktionsform** (l_k, l_k²) und **Zuordnung B** gesetzt (H188/H194).
- **Up/Down-Ort** = Ladungsvorzeichen (H196); **P_up = ½(1+iL_U)** = Chiralität der Ladung (H198).
- **Keine** Symmetrie (H197), **kein** Laufeffekt (H199), **keine** globale Holomorphie (H200),
  **keine** Grad-Ordnung (H201), **keine** minimale Invariant-Zahl (H202) legt D/B fest.
- Die vier Koeffizienten A, B, C, D (und damit alle sechs Quarkmassen) sind **freie Kopplungen**
  von vier Invarianten: zwei geraden (Grad 3 und 5) und zwei ungeraden (Grad-4-H186-Formen). Die
  Strukturkoeffizienten sind exakte Rationale; die Kopplungsstärken sind Eingaben.

**Konsequenz:** In diesem Rahmen (F4 + Ladung + dieses Vakuum + diese Invarianten) ist die
Quark-Massenhierarchie **nicht herleitbar** — sie steckt in vier freien Kopplungen. Ein nächster
Schritt braucht eine **neue Eingabe**, ein Prinzip, das die Kopplungen bindet. Mögliche Routen (dem
Autor als Weggabelung vorgelegt, nicht gerechnet):
1. **Kopplung an den Lepton-Sektor:** dieselben Invarianten wirken auf die Diagonalmoden; wenn die
   Leptonmassen (oder δ = 2/9) die Kopplungen g, h festlegen, würde D/B zur Vorhersage.
2. **Ein Elter-Objekt:** B und D als Zweige einer einzigen höheren F4-Darstellung, deren Verzweigung
   das Verhältnis bindet.
3. **Der Strang ruht** (wie bei β_sym nach 37 Versuchen), bis eine neue Idee kommt.

## Werkzeuge, Bereich, Grenzen

- **Werkzeuge:** numpy (Rang; erschöpfende χ²-Enumeration der ≤ 4-Kopplungs-Basen) + Wolfram
  (Rang-Kontrolle, exakt gleich). Qiskit nicht einschlägig.
- **Geprüfter Bereich:** acht Kopplungen (vier gerade Grad 3–6, vier ungerade H186-Formen Grad 4),
  alle Teilmengen bis Größe 4, fester M_Z-Datensatz, Zuordnung B.
- **Erste/entscheidende Abweichung:** beste ≤ 3-Basis χ² = 8 312 gegen 7,91 bei vier Kopplungen.
- **Grenzen / offene Voraussetzungen:** Invariant-Basis = die bisher identifizierten Bausteine
  (H186/H201); ein noch unbekannter Baustein könnte die Zahl senken. Der Test zeigt Freiheit in der
  bekannten Basis, nicht Unmöglichkeit in jeder denkbaren. Rang-Teil nicht blind, Basis-Test blind.
- Keine symbolischen Nullreste (exakte rationale Matrix); Wolfram-„undefined"-Warnung kosmetisch.

Nächste freie Nummern nach H202/k412: H203, k413 (vor Vergabe gegen `main` prüfen; Parallel-Thread
HS(−1) vergibt ebenfalls k-Nummern).
