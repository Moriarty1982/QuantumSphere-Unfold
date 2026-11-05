# Ergebnis H75: Mit Gravitation als einziger Kopplung gibt es keine exponentielle Instabilität, aber ein Durchgehen

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H75_Gravitationskopplung.md` (Commit 6aa8477, nicht blind). Skript `k189_test_h75.py`, Ausgabe `k189_out.json`. Status: H75b und H75c bestätigt; H75a im Kern bestätigt (kein exponentielles Wachstum), in der Gradangabe widerlegt (quadratisch statt linear).**

## Ergebnis
- **a (Photon-Gewichte, ρ_A = ρ_B):** N ist nilpotent (N² = 0 exakt). Die exakte Lösung ist δ_A(t) = δ₀(1 + t²) für beide Sektoren; der Unterschied δ_A − δ_B bleibt konstant (2e-3). Die vorab angegebene Schranke „höchstens linear“ ist für die gemeinsame Mode falsch, sie wächst quadratisch. Der von `eigvals` gemeldete Exponent 3,7e-6 ist ein numerisches Artefakt der Eigenwertberechnung bei einer defekten Matrix (Störung ∝ ε_mach^{1/4}); die Trajektorie stimmt exakt mit dem Polynom überein. Kein exponentielles Wachstum.
- **b (Materie-Gewichte):** genau eine exponentielle Mode mit Rate √(1 − x) = 0,8356 (vorhergesagt 0,8356). Kontrolle mit zwei normalen Flüssigkeiten: √(1 + x) = 1,1409 (vorhergesagt 1,1409).
- **c (Bondi-Paar ±m):** Abstand und Beschleunigung exakt konstant (Abweichung 0), gemeinsame Beschleunigung −Gm/d², Impuls 0, Energie konstant (+1); nach t = 20 laufen beide mit v = −20.

## Lesart
- **Gravitation als einzige Kopplung ist viel milder als eine direkte Kopplung (H74):** Bei exakter Paarung wächst nichts exponentiell. Die Resonanz aus H74 tritt nicht auf, weil beide Sektoren im selben Feld gleich fallen.
- **Es bleibt ein Durchgehen:** Ein kleiner Unterschied der Dichten erzeugt ein Feld, in dem beide Sektoren gemeinsam immer schneller fallen (Wachstum ∝ t²). Bei Punktmassen ist das Bondis Durchgehen mit konstanter Beschleunigung. Energie und Impuls bleiben dabei erhalten; physikalisch ist es trotzdem unerwünscht.
- **Bei Materie-Gewichten** ist die Paarung gewöhnliche Jeans-Instabilität mit verminderter wirksamer Dichte ρ(1 − β²), also Strukturbildung, die langsamer ist als ohne Tachyon-Sektor.
- **Für das Modell:** Eine M–T-Paarung, die nur über die Gravitation gekoppelt ist, ist klassisch linear tragbar (keine Resonanz), mit dem Durchgehen als bekanntem Preis. Das quantenmechanische Hauptproblem solcher Modelle, der Vakuumzerfall in Paare positiver und negativer Energie über Gravitonen, ist hier nicht erfasst.
