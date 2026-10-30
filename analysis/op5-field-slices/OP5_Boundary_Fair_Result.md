# OP5: korrigierter Vergleich gleichmäßiger Randabdeckung

29.10.2026. Wichtige Implementierungskorrektur: Die vorherige Randrechnung änderte eine lokale Punktvariable, nicht den globalen Punktdatensatz der wiederverwendeten Residualfunktion. Die gespeicherten Kontrollfehler bleiben gültig, aber die behauptete Randanpassung wurde damals nicht ausgeführt. OP5_Boundary_Refinement_Result.md trägt eine entsprechende Korrektur. Der erste identische Zweigvergleich deckte den Fehler auf; das identische Ergebnis wird nicht als physikalischer Befund verwendet.

Korrigierter Versuch: Beide Zweige starten aus demselben Feld OP5_Boundary_Refinement_Check.json, gleiche Region und quadratische Familie. Drei äußere gedämpfte Gauss-Newton-Schritte je Zweig. Kontrolle337 bisherige Punkte; Randzweig401 verschiedene Punkte mit64 neuen Punkten, genau8 je der8 Flächen, seed291043, keine Eckpunktdopplung. Der korrigierte Residualdatensatz ist tatsächlich erweitert:401 Punkte und9624 reelle Residualkomponenten, durch ausführbare Größenkontrolle bestätigt. Gleich viele äußere Schritte sind nicht exakt gleiche Rechenzeit.

Gemeinsame abschließende unangetastete Prüfmenge seed291044:1024 gleichmäßig über8 Flächen verteilte Randpunkte und4096 Innenpunkte. Ausgangs-RMS Rand .000168682, innen .000120901.

Nach Kontrolle auf alter Punktmenge: Rand-RMS .000161141, Maximum .000431718; innen RMS .000115420, Maximum .000320051. Nach echter Randanpassung: Rand-RMS .000160191, Maximum .000450631; innen RMS .000114737, Maximum .000323534. Die Mittelwerte verbessern sich gegenüber dem Kontrollzweig um ungefähr .6%, die Maximalwerte werden hingegen etwas schlechter.

Damit ist ein klarer Vorteil der Randgewichtung bei diesem Budget nicht belegt. Die einfache geringe Ergänzung neuer Randpunkte ist kein verlässlicher Weg zu besserem maximalem Fehler. Stichproben-Coframes bleiben invertierbar und g^{00}<0. Keine uniforme Gebietsgarantie, kein exakter Lösungs- oder native-action-Nachweis.

Nächste entscheidende Wahl: Wenn maximale Fehler das Ziel sind, wäre eine gezielte Anpassung an Fehlermaxima bzw. eine kontrollierte Maximumsnorm zu testen, statt den bisherigen quadratischen Mittelwert als einziges Kriterium zu benutzen. Ein solcher Zielfunktionswechsel ist offen auszuweisen und mit derselben unabhängigen Prüfmenge zu vergleichen.

Artefakte: OP5_Boundary_Fair_Interior_Control.py/.json, korrigiertes OP5_Boundary_Fair_Balanced_Check.py/.json und OP5_Boundary_Fair_Validation.py/.json. Lokale Vorläuferdaten und Evaluatoren erforderlich. Ergebnisse lokal gespeichert, nicht committed. Die ältere Paper-Grafik wurde nicht geändert.
