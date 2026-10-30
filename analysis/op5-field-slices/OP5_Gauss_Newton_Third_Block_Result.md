# OP5: dritter Korrekturblock und Randprüfung

29.10.2026. Weitere fünf akzeptierte gedämpfte Gauss-Newton-Schritte aus dem gespeicherten zweiten Block. Unverändert720 Parameter,337 Trainingspunkte, quadratische Zweimodenfamilie und Hyperwürfel Radius .01 um (1,.6,0,0). Vergleichskopplungen, Zustandsnormalisierung und Null-Lorentz-Spinverbindung unverändert.

Trainings-RMS von .000214427 auf .000171634. Neuer1024-Satz seed291037, bei der Schrittannahme nur für Geometrie verwendet: finaler RMS .000129803. Kein exakter Nullrest und keine Konvergenzzusage.

Unangetastete abschließende Prüfung: vollständiges5^4-Gitter mit625 Punkten, darunter544 Randpunkte. Die81 ursprünglichen Gittertrainingspunkte sind enthalten; dieser Satz ist deshalb nicht vollständig unabhängig. Die256 zufälligen Trainingspunkte werden nicht absichtlich aufgenommen. Zusätzlich4096 frische Zufallspunkte mit seed291038, nicht zur Schrittannahme verwendet.

Neues Feld: Raster-RMS .000200607, Rand-RMS .000212274, Maximum .000637463 bei (.99,.59,.01,-.01). Frischer4096-Satz: RMS .000130310, Maximum .000471026. Rand und gleichverteilte Innenpunkte haben unterschiedliche Verteilungen; ihre RMS-Werte sind keine direkt identischen Normen. Der relative Rest gegenüber kinetischem plus Massenterm liegt auf dem Raster bei2.45748e-5 RMS, im Zufallssatz bei1.59548e-5. Keine physikalische Fehlerschranke.

Auf sämtlichen geprüften Rasterpunkten minimale |detE|12.9674, größtes g^{00}=-.386842, kleinste Coframe-Singulärzahl .400270, größte Konditionszahl16.1902. Keine beobachtete Singularität oder Verlust raumartiger t-Schnitte.

Kontrollvergleich des vorherigen Feldes auf genau denselben Raster-/Zufallspunkten gespeichert in OP5_Third_Block_Previous_Field_Control.json. So kann Fortschritt unabhängig von wechselnder Stichprobenwahl bewertet werden. Randfehler sind der nächste vorrangige Anpassungstest: mehr Randpunkte bei gleicher Region, zusätzlich unangetastete Randkontrollen; nicht stillschweigend das Gebiet verkleinern.

Artefakte: OP5_Gauss_Newton_Third_Block_Check.py/.json, OP5_Third_Block_Grid_Validation.py/.json, OP5_Third_Block_Previous_Field_Control.py/.json. Voraussetzungen wie vorherige Feldrechnungen. Lokal gespeichert, nicht committed. Bestehende Paper-Grafik zeigt weiterhin den ursprünglichen affinen Stand. OP5 offen.
