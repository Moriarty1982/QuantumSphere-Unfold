# Ergebnis H50: Greift Ω über die ϑ-Richtung auf Ψ zurück?

Vorab-Notiz: `Vorab_Notiz_H50_Omega_Psi_Kopplung.md`, lokaler Commit ea36f39 (2. November 2026, 20:51 UTC), vor der
Rechnung. Rechnung: `k135_test_h50.py` mit dem Reihenauswerter `tps.py`. Die Jacobi-Matrix wurde mit einer
Fünfpunkt-Differenz (Schritt 1e-3) bestimmt. Ein erster Lauf mit Zweipunkt-Differenz war für den Grad-4-Rang zu
ungenau (keine Lücke) und wurde vor der Bewertung verworfen.

## Gültigkeit

- **Grad-4-Symbol:** Rang 528, Linkskern 112, Lücke 1,1e-3 | 4,2e-10. Das sind dieselben Zahlen wie beim anderen Modell
  (`precision-fourth-elimination-result.json`).
- **Ω eindeutig:** Nach Abzug der Konsequenzen niederer Ordnung hat der Gradientenraum Rang 1 (2,7 gegen 3e-7).
- **Ω passt zu θ:** Der Grad-3-Anteil von dΩ⊥ ist modulo der Grad-3-Symbolzeilen θ (Rest 2,2e-9, ohne θ 0,27).
- **Kontrollen schlagen an:** max_f r = 0,044 für ∂_t, 0,11 für ∂_x und 0,11 für ∂_y.
- **Nebenbefund:** Der 70-stellige Keim erfüllt R = (F, G, dg) in allen Taylor-Koeffizienten bis Grad 3 auf
  ≤ 2,4e-12 (float64). Damit ist auch der G-Teil unabhängig geprüft.

## Ergebnis: widerlegt (erste Klasse bis Ordnung 3)

max_f r(f, ϑ) = 1,5e-10 über alle 35 Monome f bis Grad 3. Es gibt also keine Kopplung zwischen Ω und der ϑ-Richtung.

Zusatzmessung (nach dem Kriterium, Teil der Deutung): Die ϑ-Verschiebungen f·c^μ∂_μΨ verletzen die Gleichungen
niederer Ordnung nicht, |A_low v|/(|A_low||v|) ≤ 3,4e-13 für jedes f bis Grad 3. Die Kontrollrichtungen liegen bei
6e-4 bis 2e-2.

## Erklärung: Die ϑ-Freiheit ist eine exakte Eichsymmetrie

Das Vergleichsmodell ist diffeomorphismenkovariant, weil die Geometrie aus Ψ selbst gebaut wird. Nur die
Hintergrundgrößen A und h brechen das. Beide sind unter jedem Diffeo entlang f·∂_ϑ invariant, mit beliebigem f:

- **h** hängt nur von t und r ab, also ist L_{f∂ϑ}h = 0.
- **A** ist die Verbindung A = M(t) dφ, wobei ρ·G(t, ρ) nicht von ρ abhängt. Mit c ⌟ A = 0 und dA = M′(t) dt∧dφ ergibt
  sich L_{fc}A = f c⌟dA + d(f c⌟A) = 0, weil c keine t- und φ-Komponente hat. Symbolisch geprüft: L_cA = 0.

Die freie Funktion ist also eine echte Eichfreiheit: Der Hintergrund kennt t, r und φ, aber nicht ϑ. Ω ist eichinvariant.
Das erklärt sowohl die Blindheit im Symbol als auch dieses Ergebnis.

Die Ebenen-Richtung c₀ (h-erhaltend in t, r) ist nur teilweise frei: L_{fc₀}A = f·c₀^t·M′(t) dφ ≠ 0. Das passt zur
Entartung nur auf den Ebenen Π₀ und Π₁.

## Korrektur früherer Aussagen

Die Annahme „der Bruch c·∇G ∝ z/ρ² bricht die ϑ-Freiheit“ (Gespräch und Vorab-Notiz H49) war falsch. Betrachtet wurde
dort nur der kartesische Koeffizient, nicht die Lie-Ableitung der 1-Form. Die Widerlegung von H49 passt zur exakten
Symmetrie.

## Folgerung

Eine Eichbedingung für ϑ ist zulässig, und vor der Involutivitätsprüfung ist sie nötig.
