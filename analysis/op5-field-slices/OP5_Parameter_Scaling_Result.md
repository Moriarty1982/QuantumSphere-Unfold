# OP5: Kontrollversuch zur Parameterskalierung

29.10.2026. Gleiche quadratische Feldfamilie, gleiche337 Trainingspunkte, ursprüngliches Gebiet Radius .01 und gleiche Kopplungen. Beide Zweige starten aus den Koeffizienten von OP5_Field_Residual_Diagnosis.json. Neue4096 Kontrollpunkte mit seed291030 werden nicht angepasst.

Unskalierter Kontrollzweig versus Gradskalierung der Parameter (konstant1, linear.01, quadratisch.0001), mit identischer Zielfunktion und L-BFGS-Einstellungen. Die Skalierung ist invertierbar und ändert die erlaubten Feldfunktionen nicht. Beide Läufe haben max_iter1200, erreichten aber1501 Closure-Aufrufe: das Standard-Funktionsauswertungslimit ist ebenfalls aktiv. Eine vollständige Ausschöpfung aller1200 Iterationen wurde nicht protokolliert und wird nicht behauptet.

Unskaliert: Trainings-RMS .000920288, frischer Kontroll-RMS .000845340, Maximum .00242708. Gradskaliert: Trainings-RMS .000923305, Kontroll-RMS .000847783, Maximum .00242832. Auf demselben Kontrollsatz liegen die beiden Fehler somit praktisch gleich. Die konkret getestete Gradskalierung bringt keinen Vorteil; sie ist keine vollständige Untersuchung aller möglichen Vorkonditionierungen.

Gegenüber dem vorangehenden Trainings-RMS .000923612 verbessert sich der unveränderte Kontrollzweig nur gering. Der Vergleich von Kontroll-RMS auf unterschiedlichen Punktmengen ist keine exakte Fortschrittsmessung; der direkte Vergleich der zwei jetzigen Zweige verwendet denselben neuen Satz.

An allen geprüften Punkten bleibt g^{00}<0 und die Coframe invertierbar (kleinstes |detE| auf Kontrollen etwa13.0231). Keine Uniformgarantie, keine physikalische Genauigkeitszusage, keine exakte regionale Lösung.

Ergebnis: Die einfache Gradskalierung liefert keinen Beleg für die zuvor vermutete Konditionierungsverbesserung. Ein erneutes Plateau ist weiterhin keine mathematische Restuntergrenze. Vor weiteren blind verlängerten Optimierungen sind Liniensuch-/Gradientendiagnose und eine vollständige Tangentialprojektion des Restes sinnvoll. Insbesondere muss ein solches Projektionssystem alle verbliebenen Parameterfreiheiten eliminieren, bevor ein unvermeidlicher Quellterm identifiziert wird.

Artefakte: OP5_Parameter_Scaling_Check.py/.json. Python/Torch/NumPy/SymPy, gespeicherte vorherige Feldkoeffizienten und bestehende Evaluatoren erforderlich. Lokal gespeichert, nicht committed. Paper-Grafik unverändert, OP5 offen.
