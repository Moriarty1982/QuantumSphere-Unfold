# OP5: weitere fünf gedämpfte Feldkorrekturen

29.10.2026. Vorherige Forschung bis zum ersten Gauss-Newton-Block als91d60c6 auf main committed; kein Push in diesem Schritt beauftragt. Diese Fortsetzung entstand danach und ist lokal.

Unverändert: quadratische Zweimodenfamilie mit720 reellen Parametern,337 Trainingspunkte, Region Radius .01, Vergleichskopplungen und Null-Lorentz-Spinverbindung. Start aus OP5_Damped_Gauss_Newton_Check.json. Gleiche gedämpfte SVD-Korrektur und Kontrolle tatsächlicher gegen vorhergesagte Verlustreduktion. Fünf weitere äußere Schritte angenommen; Laufzeit etwa56.2 Sekunden. Kontrollsatz1024, seed291035, nur für geometrische Schrittannahme sowie Berichterstattung verwendet.

Trainings-RMS von .000429682 auf .000214427. Derselbe1024-Kontrollsatz von .000389358 auf .000173307, Kontrollmaximum .000392795. Ein angenommener Zwischenschritt verbessert den Trainingsfehler, erhöht aber den Kontroll-RMS geringfügig; dessen Monotonie wird nicht behauptet. Gesamtergebnis verbessert beide deutlich.

Frischer unangetasteter4096-Satz seed291036: RMS .000171868, Maximum .000579191. Relatives Maß ||F||/(||kinetischer Term||+||Massenterm||): RMS2.10357e-5 und Maximum7.15925e-5. Keine physikalische Fehlerschranke. Minimales |detE|13.1338, größtes g^{00}=-.383001, Q>5.4498, kleinste Coframe-Singulärzahl .403747, größte Konditionszahl16.0528, maximale Feldnorm4.01190. Keine singuläre Geometrie im Prüfsatz.

Quadratische Restanteile auf dem frischen Satz: A41.37%,B38.60%,C20.03%. Der frühere überwiegende B-Anteil ist damit kein beständiger Sektorengpass. Imaginäre S-Projektion unter4.1e-15. Notwendige skalare Zustandsbedingung weiter erfüllt.

Bewertung: Fortgesetzter Genauigkeitsgewinn ohne neue Ansatzfreiheiten. Kein Beweis für Erreichbarkeit von Nullrest oder eine regionale exakte Lösung; nach wie vor finite Parametrisierung und endliche Stichproben. Die bestehende Paper-Abbildung und native physikalische Zuordnungen bleiben unverändert. Eine numerische Existenz-/Stabilitätszertifizierung ist offen.

Artefakte: OP5_Gauss_Newton_Continuation_Check.py/.json sowie OP5_Gauss_Newton_Continuation_Validation.py/.json. Reproduktion mit python im lokalen Forschungsordner benötigt bisherige Skripte/Koeffizienten, Torch/NumPy und die referenzierte Repository-Basis. Neue Koeffizienten lokal gespeichert, nicht committed.
