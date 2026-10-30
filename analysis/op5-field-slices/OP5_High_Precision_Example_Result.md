# OP5: exemplarischer Präzisionstest der direkten Punktlösung

30.10.2026. mpmath1.3.0,30/50/80 Dezimalstellen, Zentrum (1,.6,0,0). Vollständige komplexe Matrixrechnung des bisherigen Vergleichssystems, keine regionale PDE-Lösung.

Eingaben: gespeicherte Feldwerte und bereits reparierte Jets von OP5_Direct_Compatibility_Solve.json werden als endliche Dezimalzahlen eingelesen. Sie besitzen damit nicht plötzlich80 Stellen ursprünglicher physikalischer Information. Hintergrundkopplungen werden am Zentrum aus rationalen Zahlen und hochpräzisen Wurzeln/Trigonometrie neu aufgebaut; keine NumPy-Matrizen im eigentlichen Präzisionslauf. Zwei Varianten derselben Punktaufgabe:

1. Gerundete Feldwerte unverändert. Deren notwendige skalare Zustandsbedingung hat einen Defekt etwa1.00445e-15. Drei räumliche Parameter und die Zeitgleichung werden höherpräzise gelöst; die vierte Bedingung wird unabhängig geprüft.
2. Dieselben gespeicherten Feldwerte werden mit einem gemeinsamen positiven Faktor in jeder Präzision neu auf h Psi†ZbetaPsi=8 normiert. Das ist eine explizite winzige Änderung der Feldwerte und beseitigt den bekannten Eingabedefekt; keine nachträgliche Löschung des Ausgaberestes. Die gespeicherten ursprünglichen Ansatzkoeffizienten wurden hier nicht vollständig höherpräzise neu evaluiert. Alle drei räumlichen Parameter werden anschließend neu gelöst und die Zeitcoframe neu rückgelesen.

Vollständige Restnormen:

| Dezimalstellen | gerundete Feldwerte beibehalten | Zustandsnormierung höherpräzise erfüllt |
|---|---:|---:|
|30|2.88760698288e-15|2.30434438938e-30|
|50|2.88760698288e-15|6.01399881244e-50|
|80|2.88760698288e-15|4.54005676473e-80|

Die Norm der vier Verträglichkeitskomponenten verhält sich entsprechend. mp.findroot löst nur drei ausgewählte Komponenten mit tol10^-(dps-8); die nicht gelöste vierte sowie der vollständige Residualoperator mit tatsächlich ausgelesener Coframe werden danach geprüft. Assertions bestätigen die erwartete Präzisionsskalierung und den erhaltenen Rundungseingabe-Kontrollrest.

Interpretation: Im Beispiel ist10^-14 bis10^-16 keine eigenständige physikalische Schwelle. Zwei numerische Effekte lassen sich unterscheiden: arithmetische Rundung im Löser und bereits eingefrorene ungenaue Zustandsdaten. Höhere Rechenpräzision allein entfernt Letzteres nicht. Mit präzisionsgerecht erfüllter notwendiger Eingabebedingung sinkt der Rest bis in den jeweiligen Rundungsbereich. Die kleinen Werte sind keine experimentelle Genauigkeit oder mathematische Existenzzertifizierung.

Der Test rehabilitiert insbesondere nicht die regionalen Fortsetzungen: Deren deutlich größere Restnormen wurden hier nicht höherpräzise geprüft oder beseitigt. Nur die direkte algebraische Punktlösung ist untersucht.

Artefakte OP5_High_Precision_Example.py/.json/.log, mpmath/SymPy und gespeicherte Ausgangsdaten nötig. Aufruf python OP5_High_Precision_Example.py. Lokal gespeichert, nicht committed.
