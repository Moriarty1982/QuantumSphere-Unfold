# OP5: fünf gedämpfte Gauss-Newton-Schritte

29.10.2026. Gleiche quadratische Zweimodenfamilie, dieselben337 Trainingspunkte, Gebiet Radius .01 um (1,.6,0,0), gleiche Vergleichskopplungen und Null-Lorentz-Spinverbindung. Ausgangskoeffizienten aus OP5_Field_Residual_Diagnosis.json. Keine zusätzlichen Freiheitsgrade.

720 Parameter gegen8088 reelle Residualkomponenten mit autograd differenziert. Schritt aus SVD mit Filter sigma/(sigma²+lambda), lambda=relative_damping*sigma_max². Annahme bei tatsächlicher/vorhergesagter quadratischer Fehlerreduktion>.1 und geprüfter Coframe-Regularität, Q>1e-4 und g^{00}<-.05. Relative Dämpfung initial1e-6, nach Erfolg entsprechend angepasst. Fünf äußere Schritte, jeder akzeptiert nach eventuell erhöhtem Dämpfungsversuch. Vollständige Versuchshistorie und Koeffizienten gespeichert. Laufzeit etwa50.3 Sekunden, kein Laufzeitskalierungsversprechen.

Trainings-RMS von .000923612 auf .000429682. Gleicher1024-Punkte-Kontrollsatz seed291033 von .000865816 auf .000393676; Kontrollmaximum von .00207978 auf .000937010. Dieser Satz wurde nicht zur Residualminimierung verwendet, nahm aber an der geometrischen Annahmeprüfung teil und ist deshalb nicht vollständig unangetastete Validierung.

Frischer4096-Punkte-Satz seed291034 nach Abschluss ohne Einfluss auf Schrittannahme: RMS .000391481, Maximum .00105745. Minimales |detE|13.0943, größtes g^{00}=-.365616, Q>5.45018, kleinste Coframe-Singulärzahl .395239 und größte Konditionszahl16.4231. Größte Feldnorm4.0130. Diese Stichprobe zeigt keine singuläre Geometrie als Ursache kleiner Residuen; sie liefert keine uniformen Gebietsschranken.

Relatives Vergleichsmaß ||F||/(||kinetischer Term||+||Massenterm||): frischer RMS4.79183e-5, Maximum1.28525e-4 (rund .00479% bzw .01285%). Keine physikalische Genauigkeitsgarantie oder Fehlerschranke gegenüber einer exakten Lösung. Quadratische Restanteile A22.28%, B69.43%, C8.30%; Imaginärteil der S-Projektion unter4e-15, entsprechend erfüllter notwendiger skalarer Zustandsbedingung.

Interpretation: Kontrollierte nichtlineare Schrittwahl verbessert das vorhandene Feld deutlich. Der Rest ist damit weiterhin keine nachgewiesene physikalische Mindestabweichung. Eine Konvergenz- oder Existenzbehauptung, neue Wirkung und native OP5-Schließung folgen daraus nicht. Künftige Fortsetzung benötigt weiter unabhängige Stichproben, geometrische Margen und ein nachvollziehbares Abbruchkriterium; die Koeffizienten bleiben frei optimierte Vergleichsdaten.

Artefakte: OP5_Damped_Gauss_Newton_Check.py/.json, OP5_Gauss_Newton_Fresh_Validation.py/.json. Benötigen Torch/NumPy, vorhandene Evaluatoren und vorherige Koeffizienten. Lokaler Stand, nicht committed. Die Paper-Abbildung bleibt unverändert und zeigt weiterhin den früheren affinen Stand.
