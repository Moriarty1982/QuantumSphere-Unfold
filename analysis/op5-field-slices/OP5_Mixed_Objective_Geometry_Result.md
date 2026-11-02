# OP5: gemischte Gewichtung und vollständiger zeitlicher Hauptteil

29.10.2026. Vergleichsmodell, kein nativer physikalischer Abschluss.

## Geometrie zuerst

4096 gemeinsame Punkte seed291047: Ausgangs-, Mittelwert- und Spitzenfeld besitzen überall geprüfte Lorentz-Signatur (-+++), g^{00}<-.40 ungefähr, kleinste Coframe-Singulärzahl>.400 und größte Konditionszahl<16.2. Der eingefrorene Dirac-Zeithauptteil P0=E^{-1}[0,a]K^a hat kleinsten absoluten Eigenwert>.148 und Konditionszahl<18.7. Diese regulären Stichproben sind kein Beweis der Wohldefiniertheit der vollständigen nichtlinearen Evolution.

Der vollständige zeitliche Hauptteil muss auch die Ableitungsabhängigkeit der ausgelesenen Coframe berücksichtigen. Am Zentrum des Mittelwertfelds ergibt die24x24-Jacobi-Matrix nach den24 reellen zeitlichen Spinorableitungen Rang20 bei relativer Schwelle1e-8. Drei Differenzenschritte1e-4,1e-5,1e-6 bestätigen vier kleine Singulärwerte. Der eingefrorene Dirac-Hauptteil und diese volle Matrix sind verschiedene Objekte.

Algebraischer Grund: Bei festen Feldwerten und kovarianten Jets D_mu Psi lässt sich D_0 Psi durch D_0 Psi+sum_nu a_nu D_nu Psi ersetzen, gleichzeitig E_0 durch E_0+sum_nu a_nu E_nu. Bei invertierbarer entsprechender Spaltentransformation kompensiert die inverse Coframe die Jetänderung exakt. Der kontrahierte kinetische Term bleibt unverändert, ebenso der festgehaltene Massenterm. Vier reelle Richtungen sind daher am Punkt unsichtbar. Für0.1-mal jede kovariante Jetspalte wurde die endliche Invarianz direkt geprüft.

Diese punktweise algebraische Freiheit ist nicht automatisch eine globale Eichsymmetrie: Transformierte Jets müssen über ein Gebiet integrierbar sein, und die festgehaltenen Hintergrundkopplungen müssen korrekt transportiert werden. Es folgt auch nicht, dass beliebige vier Zusatzbedingungen eine wohldefinierte Evolution erzeugen. Eine begründete Auslese-/Koordinatenfestlegung und reduzierte Hauptteilanalyse sind die nächste strukturelle Aufgabe.

## Gemischter Optimierungstest

Gleicher Ausgangspunkt, dieselben401 Trainingspunkte und drei äußere Schritte wie Mittelwert-/Spitzentest. Gemischtes IRLS-Gewicht w²=.75+.25*||F_point||²/mean(||F_point||²). Gewichte pro äußerem Schritt fest; dies ist eine Mischung von lokalen quadratischen Surrogaten, keine exakt gelöste Maximumsnorm. Alte Kopplungen und Region unverändert.

Identische abschließende Prüfmengen seed291046:1024 Randpunkte und4096 Innenpunkte. Rand-RMS/Maximum: Mittelwert .000156881/.000411706; starke Spitzengewichtung .000174291/.000321192; Mischung .000158096/.000341700. Die Mischung senkt das beobachtete Maximum gegenüber Mittelwert um17%, bei nur.8% höherem Rand-RMS. Innen-RMS/Maximum: Mittelwert .000109764/.000332919, Mischung .000116939/.000316592. Somit kein Kandidat, der beide Fehlermaße überall verbessert.

Fazit: Die Mischung liefert einen brauchbaren numerischen Kompromiss, keine exakte Feldlösung. Geometrische Regularität ist vorhanden, aber die vollständige Evolutionsmatrix hat zusätzliche punktweise Freiheiten. Vor immer weiteren Optimierungsschritten ist eine strukturelle Fixierung dieser Freiheiten und Fortsetzungsprüfung begründet. Keine neue physikalische Konstante, keine native Wirkung oder OP5-Schließung hergeleitet.

Artefakte OP5_Mixed_Objective_Geometry_Check.py/.json; OP5_Full_Time_Symbol_Check.py/.json; OP5_Time_Shear_Invariance_Check.py/.json; OP5_Peak_Mixed_Check.py/.json; OP5_Peak_Mixed_Validation.py/.json. Vorläuferdaten/Evaluatoren erforderlich. Lokal gesichert, nicht committed; Paper-Grafik unverändert.
