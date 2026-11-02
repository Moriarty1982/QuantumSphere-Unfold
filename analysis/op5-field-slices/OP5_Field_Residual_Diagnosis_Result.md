# OP5: Restattribution und Optimierungskontrolle

29.10.2026. Gleiche quadratische Zweimodenfamilie, gleiche337 Trainingspunkte, gleiche Region Radius .01. Keine neue Kopplung, Frequenz, Normierung oder Zusatzverbindung. Ausgang: OP5_Quadratic_Dense_Field_Control.json.

Am Kontrollsatz512 entfallen vor weiterer Optimierung rund11.58%,84.55%,3.87% der quadratischen Restnorm auf A,B,C. Der Imaginärteil der Ausleseprojektion Psi†(S tensor I)F liegt unter4e-15; die bereits identifizierte skalare Zustandsbedingung ist somit nicht die Ursache dieses verbleibenden Restes. Der Realteil dieser Projektion ist nicht identisch null. Daraus allein folgt keine neue unabhängige Identität.

Die Parametergradientennorm der unbestraften Trainingsverlustfunktion beträgt .03192 bei Verlust4.7184e-6. Rohgradienten sind parameterabhängig, keine physikalische Norm; die Aussage, der Solver habe bereits eine strukturelle Restgrenze erreicht, ist damit nicht begründet.

Fortsetzung mit neu initialisiertem L-BFGS-Speicher und1200 Iterationen, sonst gleiche Aufgabe: Trainings-RMS .000923612; Kontroll-RMS512 .000852458 statt zuvor .00203972, Verbesserung etwa2.39. Kontroll-Maximum .00193616. Restanteile danach A12.61%,B82.96%,C4.43%. Der überwiegende B-Rest ist eine Beschreibung dieser gewählten Basis/Familie, kein universeller physikalischer B-Sektorbefund.

Relatives Fehlermaß pro Punkt: ||F||/(||kinetischer Term||+||Massenterm||), in derselben gewöhnlichen Vergleichsnorm. Kontroll-RMS .000104381, Maximum .000234859. Das entspricht etwa .0104% RMS bzw .0235% Maximum der so definierten Termskala, nicht einer experimentellen Genauigkeit oder bewiesenen Lösungsfehlerschranke. Die Null-Lorentz-Spinverbindung bleibt eine Vergleichsannahme.

Geprüfte Coframes weiterhin invertierbar, g^{00} negativ. Ein frischer unabhängiger Satz4096 Punkte mit seed291029 samt kleinster Singulärzahl und Konditionszahl ist in OP5_Field_Residual_Fresh_Validation.json dokumentiert; Stichproben sind keine uniformen Gebietsschätzungen. Dieser Satz wurde nicht zur Optimierung verwendet.

Ergebnis: Es gibt noch Optimierungsspielraum ohne neue Ansatzfreiheitsgrade. Der vorherige Gradvergleich beweist weder ein kubisches Hindernis noch eine Konvergenzfolge. Eine exakte regionale Lösung und ein native-action-Abschluss bleiben offen. Nächste sinnvolle Verbesserung: Skalierung/Konditionierung der Parameter und vollständige Restprojektionsanalyse, statt aus einem finite-budget Plateau eine neue physikalische Obstruktion abzuleiten.

Artefakte OP5_Field_Residual_Diagnosis.py/.json und OP5_Field_Residual_Fresh_Validation.py/.json. Benötigen bestehende lokale Rechendaten und Basis wie die vorherigen Feldtests. Neue Koeffizienten gespeichert. Lokal, nicht committed; Paper-Grafik bleibt unverändert.
