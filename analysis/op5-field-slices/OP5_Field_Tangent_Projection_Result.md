# OP5: vollständige Parametertangente des verbleibenden Feldrestes

29.10.2026. Quadratische Zweimodenfamilie, gespeicherter Stand aus OP5_Field_Residual_Diagnosis.json. Keine Modelländerung.

Alle720 reellen Ansatzparameter gegen alle8088 reellen Gleichungskomponenten an337 Trainingspunkten differenziert. PyTorch-autograd-JVP für jede Parameterspalte, vollständige dünne SVD der8088x720-Matrix. Bei hoher Matrix genügen die linken Singulärvektoren der dünnen SVD zur Bildprojektion; das Komplement r-U_r U_r^T r erfasst den gesamten verbleibenden Rest, ohne einen unvollständigen linken Kern als vollständig auszugeben. Unabhängige Richtungs-Differenzenkontrolle in OP5_Field_Tangent_Derivative_Control.json.

Absolute Restnorm über alle Trainingspunkte .01695527, entsprechend RMS .000923612. Relative SVD-Abschneidung1e-6: Rang543, korrigierbare Norm .01694359, Rest .000629351, volle Schrittweite in Parametern .0167295. Abschneidung1e-8: Rang649, Rest .000273362, Schrittnorm .708981; bei1e-10 Rang695, Rest .000224364, Schrittnorm1.79756. Starke Abhängigkeit von der Rangschwelle und große schwache Richtungen: kein zertifizierter exakter Rang und keine mathematische unvermeidliche Restuntergrenze.

Bei1e-6 erfasst die lineare Korrektur über99.8% der quadratischen Restnorm. Aber ihre volle nichtlineare Einsetzung verschlechtert Trainings-RMS auf .62443. Dämpfungsfaktor.01 verbessert ihn auf .000915242; neue512 Kontrollpunkte seed291031 verbessern sich von .000840877 auf .000833228. Faktor.1 verschlechtert bereits auf .00413. Bei den schwächer abgeschnittenen Systemen ergeben sich dieselben Warnzeichen: bessere lineare Vorhersage bedeutet nicht besseren großen nichtlinearen Schritt.

Alle getesteten Schrittweiten wurden mit neu berechneter Coframe, Originalkopplungen, Positivitätswert Q und g^{00} kontrolliert. Die dokumentierten512-Kontrollwerte bleiben regulär und g^{00}<0. Die getesteten Korrekturen sind nur Kontrollen, keine bereits akzeptierte regional genaue Lösung.

Diagnose: Die Restlage ist an diesem Feld überwiegend durch vorhandene Parameterrichtungen linear korrigierbar. Ein erheblicher Teil des bisherigen Plateaus ist somit mit nichtlinearer Schrittwahl/ill-konditionierten Richtungen vereinbar. Das beweist weder Konvergenz einer neuen Optimierung noch eine native physikalische Ursache. Der kleine projizierte Rest bleibt ansatz-, punktmengen- und abschneidungsabhängig.

Nächste sinnvolle Rechnung: gedämpftes Gauss-Newton-/Levenberg-Marquardt-Verfahren mit tatsächlicher gegen vorhergesagte Fehlerreduktion; Parameterwerte und Geometrie nach jedem akzeptierten Schritt kontrollieren. Keine volle Pseudoinversenkorrektur unbesehen übernehmen und keine neue Physik aus einem numerischen Rang ableiten.

Artefakte: OP5_Field_Tangent_Projection_Check.py/.json und OP5_Field_Tangent_Derivative_Control.py/.json; NumPy, Torch, Vorgängerdaten und bestehende Evaluatoren erforderlich. Neue endgültige Feldkoeffizienten wurden hier nicht ausgewählt. Lokal gespeichert, nicht committed; Paper-Grafik unverändert, OP5 offen.
