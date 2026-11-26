# Ergebnis H183: Leptonen und Quarks sind nicht zugleich stabile Lösungen einer Feldgleichung mit Potential bis Grad 4

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H183_Sektoren_als_Vakua_einer_Feldgleichung.md` (Commit a009664, vor der Rechnung). Skripte
`k386_test_h183.py` (`k386_out.txt`) und `k386b_gegenprobe.wl` (`k386b_out.txt`).

Werkzeuge: Python (numpy, scipy, cvxpy mit SCS) für die Invarianten (wie k385), Gradient und zweite Variation exakt aus den Polynomen und das
konvexe Programm (semidefinit, linear in den Koeffizienten; damit ist „nicht lösbar“ eine Aussage über **alle** Koeffizienten, nicht über eine Suche).
Wolfram Language exakt für eine reelle Unterfamilie, in der sich der Widerspruch von Hand ablesen lässt (Reduce: False). Qiskit nicht eingesetzt
(keine Schaltung, kein Messablauf).

**Ergebnis in einem Satz:** Jeder der drei Zustände (Leptonen bei 45°, Down, Up) ist für sich eine stabile statische Lösung, Down und Up auch
gemeinsam, aber der Leptonzustand und ein Quarkzustand sind in keinem invarianten Potential bis Grad 4 zugleich stabil, für keinen Winkel und
unabhängig davon, ob die Norm fest ist.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H183a | t* (größter erreichbarer kleinster Eigenwert): L 1,689; D 0,483; Up 0,440; D + Up 0,135; **L + D 0; L + Up 0; L + D + Up 0** | t* > 0 | **widerlegt** |
| H183b | kein gemeinsamer lösbarer Bereich | – | entfällt in der vorab geschriebenen Form |
| H183c | Stationarität an L, D, Up lässt 31 von 40 Koeffizienten frei | Bericht | – |
| Phasenfassung | L 0,415; D + Up 0,117; L + D + Up 0 | Bericht | dasselbe Bild |

Kontrollen: Tensoren gegen die Monomdarstellung 3·10⁻¹⁴; Nullrichtungen wie aus der Symmetrie erwartet (L: 0; D, Up: 5 aus SU(3) → SU(2)).

## Woran es liegt (nachträglich, Erkundung; Wolfram exakt)
In der reellen Unterfamilie (x₀, x_U, r = |c|) hat jedes invariante Potential bis Grad 4 die Form
V = a₁(x₀² + x_U²) + a₂r² + b₁(x₀² + x_U²)² + b₂x₀²x_U² + b₃r²(x₀² + x_U²) + b₄r⁴. Auf der Kugel:
- Leptonzustand, Krümmung in der Leptonebene: −2b₂. Stabil verlangt **b₂ < 0** (das ist κ < 0 aus H178, das offene Vorzeichen 2a − b aus H149).
- Quarkzustand cos θ·1 + sin θ·n, Krümmung in Richtung U: 2b₂cos²θ. Stabil verlangt **b₂ > 0**.
Der Term, der 45° bei den Leptonen zum Minimum macht, lässt jeden Quarkzustand in die Richtung U wegkippen. Reduce über alle Koeffizienten und
0 < θ < π/2: False.
- Variante mit dem farblosen Anteil des Quarks bei 45° (D′ = cos θ(1 + U)/√2 + sin θ·n): Krümmung von D′ entlang θ ist (4b₁ + b₂ − 4b₃ + 4b₄)sin²2θ/2,
  die des Leptonzustands in Richtung Farbe ist −(4b₁ + b₂ − 4b₃ + 4b₄)sin²θ. Entgegengesetzte Vorzeichen, also ebenfalls nicht lösbar (Python
  im vollen Raum: 0). Grund: Entlang des Farbanteils ist V dort quadratisch und hat nur ein Minimum.
- Winkel: Für θ = 10° bis 80° und beide Ladungen dasselbe (t* = 0).
- Freie Norm (Zustände r·x mit r_D, r_U zwischen 0,5 und 2, voller Gradient null): L + D und L + D + Up bleiben bei 0; D + Up ist lösbar.
Die Skala zu setzen ist also nicht die Ursache.

## Was geht (nachträglich, Erkundung)
- **Down und Up gemeinsam** (32 freie Koeffizienten). Im lösbaren Bereich erzwungen: A < 0, B > 0 (wie in k378) und **V_L(45°) − V_L(0°) > 0**:
  Wo die Quarkzustände stabil sind, ist 45° in der Leptonebene kein Minimum. C und D (ladungsungerade Anteile) haben freies Vorzeichen.
- **Ein Vakuum, die anderen Sektoren als Schwingungen.** Um den Leptonzustand zerfallen die 15 Schwingungsrichtungen für ein allgemeines Potential
  in Gruppen mit den Vielfachheiten 6, 6, 1, 1, 1: zwei Farbgruppen (Ladung ⅓ und ⅔, je drei komplexe Richtungen) mit je eigenem Frequenzquadrat
  und drei farblose. Die zweite Variation hat dort 8 unabhängige Koeffizienten. Das Muster „zwei Quarktypen mit verschiedener Masse, Farbe
  entartet“ kommt also auch ohne eigene Quarkvakua heraus; es ist die Aussage von H182 (ladungsungerade Form nur im Farbblock) in anderer Gestalt.

## Lesart
- **Was das für H178, k378 und H182 heißt.** Dort war je Sektor ein Feld vorgegebener Art betrachtet und nur der Winkel variiert, mit **einem**
  Potential für alle. Das trägt nicht als Feldgleichung eines Feldes: Die drei Winkel können nicht alle stabile Lösungen desselben Potentials sein.
  Die Aussagen zur Symmetrie (welche Terme J erlaubt, H178a, b; H182a, c) bleiben; die Lesart „gemeinsames Potential, drei Vakua“ ist zurückgenommen.
- **Das offene Vorzeichen.** Der Autor hatte vermutet, die offenen Vorzeichen folgten aus der Feldgleichung. Hier folgt eines: Das Vorzeichen von
  b₂ (κ, 2a − b) ist durch die Wahl des Vakuums festgelegt. Leptonvakuum: b₂ < 0. Quarkvakuum: b₂ > 0. Beides zugleich gibt es nicht.
- **Weggabelung (für den Autor):**
  (1) **Ein Vakuum, Sektoren als Schwingungen.** Das Vakuum ist der farblose Zustand bei 45°; Quarks und Leptonen sind Anregungen. Dann sind K und θ
  je Sektor keine Vakuumwinkel, sondern müssen aus der Generationenstruktur der Anregungen kommen (drei Felder, Albert-Algebra, H156 bis H158).
  (2) **Getrennte Felder je Sektor**, jedes mit eigenem Potential. Dann gibt es keine gemeinsamen Koeffizienten mehr, und die Zahl der freien Größen
  wächst; eine Beziehung zwischen den Sektoren müsste von außen kommen.
  (3) **Höherer Grad** (ab 6 ist V entlang des Farbanteils kubisch und kann zwei Minima haben). Nicht gerechnet; bringt weitere freie Koeffizienten.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H178 | ein Potential für alle Sektoren; Art des Feldes je Sektor | J legt 45° nur farblos fest | A/B je Quarktyp |
| H182 | Feld in ℂ ⊗ 𝕆; Quarkfeld als Ladungs-Eigenzustand | ladungsungerade Form nur im Farbblock | Stärke C/B |
| H183 | ein Feld, feste Norm (auch frei geprüft), Grad ≤ 4, statisch und homogen | Lepton- und Quarkzustand nicht zugleich stabil; Vorzeichen von b₂ hängt am Vakuum | welche Lesart: ein Vakuum mit Schwingungen, getrennte Felder oder höherer Grad |

Prüfung nach der Regel „Bilanz der Setzungen“ (vierter Schritt zur selben Voraussetzung): Die stillschweigend gewählte Weggabelung seit H178 war,
jeden Sektor als eigenen stationären Zustand **eines** Potentials zu lesen. Sie ist hiermit geprüft und trägt nicht. Sie wird dem Autor vorgelegt.

## Grenzen
Grad ≤ 4; statische homogene Lösungen (Ableitungsterme K₁ bis K₃ aus k290 und zeitabhängige Lösungen wie ψ̇ = ωuψ sind nicht einbezogen und könnten
das Bild ändern); lokale Stabilität; ein Feld ohne Generationenindex; Winkel bei M_Z (das Ergebnis hängt nicht vom Winkel ab). Symmetrie wie in H182
(J und Konjugation komplex-linear). Keine Übertragung in den Materie-Frame nötig (keine Aussage über Messwerte). Kein Vorzeichen gesetzt. Kein Guard
berührt; OP3 und OP4 offen. Vergeben: H183, k386. Nächste frei: H184, k387 (vor Vergabe prüfen).
