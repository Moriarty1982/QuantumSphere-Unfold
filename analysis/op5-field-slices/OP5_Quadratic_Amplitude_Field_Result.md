# OP5: quadratische Modenamplituden bei fester Gebietsgröße

29.10.2026. Ansatzvergleich, keine exakte regionale Lösung.

Gleiches Gebiet um (1,.6,0,0), Radius .01, gleiche zwei Frequenzen und Vergleichskopplungen, gleiche Normalisierung zur Erfüllung der notwendigen Zustandsbedingung. Statt fünf affiner Basisfunktionen jetzt15 Monome bis Grad2 einschließlich aller sechs gemischten quadratischen Terme. Zwei Moden, drei vierkomponentige komplexe Spinoren. Initialisierung aus dem gespeicherten affinen Feld; quadratische Koeffizienten zunächst0. Feldwerte frei, keine Erhaltung alter Anfangsdaten beansprucht. Null-Lorentz-Spinverbindung unverändert wie im Vergleich.

81 Trainingspunkte im vollständigen3^4-Gitter mit Abweichungen -.01,0,.01. 128 unabhängige gleichverteilte Kontrollpunkte im selben Hyperwürfel, NumPy seed291026. L-BFGS400 Iterationen, kausale Strafe wie im Vorgänger. Keine Verkleinerung des Gebiets.

Quadratisches Feld: Trainings-RMS .00415969, Kontroll-RMS .00297106, Kontroll-Maximum .00490620. Kontroll-Minimum |detE|11.3140, größtes g^{00}=-.40034, Q>5.4698. Positives Q lässt die Zustandsnormalisierung regulär. Damit bleibt an den geprüften Punkten die Geometrie invertierbar und t raumartig geschnitten.

Fairer Kontrolllauf: vorhandenes affines Feld ebenfalls400 Iterationen auf denselben81 Punkten nachoptimiert, dieselben128 Kontrollpunkte. Trainings-RMS .01830695, Kontroll-RMS .01151736, Kontroll-Maximum .0229870. Quadratische Familie ist in diesem Optimierungsvergleich am Kontroll-RMS rund3.88-mal genauer. Gleiche Iterationsgrenze ist keine Garantie globaler Minima oder exakt gleicher Rechenzeit. Unterschiedliche gefundene Geometrien sind erlaubt; der Fit ist unterbestimmt.

Ein zweiter Kontrollsatz mit128 Punkten und seed291027 sowie unabhängige finite Differenzen der Feldfunktion und vorhandener NumPy-Residualauswertung sind separat in OP5_Quadratic_Field_Validation.json dokumentiert. Kein Vergleich der unterschiedlichen Punktmengen als exakte gleiche Norm. Die Amplituden-/Normalisierungsableitung enthält auch alle gemischten Monome.

Bewertung: Reproduzierbarer Hinweis, dass ein Teil des Restes an der eingeschränkten Amplitudenfamilie liegt. Eine Konvergenzreihe, uniforme Fehlerkontrolle, native Wirkungs-/Einstein-Gleichung und regionale exakte Lösung fehlen. Kein Schluss auf eine physikalische Naturkonstante oder OP5-Schließung. Die bisherigen Paper-Abbildungen zeigen weiterhin das ältere affine Feld und wurden nicht stillschweigend ersetzt.

Artefakte: OP5_Quadratic_Amplitude_Field_Check.py/.json, OP5_Affine_Dense_Field_Control.py/.json, OP5_Quadratic_Field_Validation.py/.json. Ausführen mit python im lokalen Forschungsordner; Torch/NumPy/SymPy, Vorgängerdaten und Repository-Basis erforderlich. Lokal gespeichert, nicht committed.
