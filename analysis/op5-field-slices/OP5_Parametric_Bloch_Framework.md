# OP5: lokale Lösungsschar und Bloch-Darstellung

30.10.2026. Die Familie wird als Forschungsansatz ausdrücklich parametrisch geführt; keine regionale Feldlösung behauptet.

## Lösungsschar statt Einzelwahl

Bei festen Feldwerten, zeitlicher Coframe und Vergleichskopplungen besitzt der räumliche Erstjet72 reelle Komponenten. Nach gemeinsamer Lösung der direkten zeitlichen Verträglichkeit und dg=0 hat die8x72-Jacobi-Matrix am reparierten Punkt numerisch Rang7. An allen drei Kontrollpunkten bleibt die kleinste der sieben regulären Singulärzahlen zwischen1.34 und1.66, die achte liegt bei ungefähr1e-10 (Differenzengenauigkeit).65 lokale räumliche Jetparameter sind damit im linearen Vergleich frei. Diese Zahl zählt keine65 physikalischen Freiheitsgrade: Koordinaten-/Auslesefreiheiten und weitere Fortsetzungsbedingungen sind noch enthalten.

Neue Darstellung: zerlege räumliche Jets in sieben ausgewählte abhängige Komponenten y und65 Parameter lambda; löse die sieben unabhängigen Bedingungen als y=y(lambda). Der implizite Funktionensatz motiviert eine lokale Schar, sofern die exakten Regularitäts- und Unabhängigkeitsvoraussetzungen gelten; die numerische Rangprüfung allein ist kein formaler Beweis. Alle ursprünglichen acht Bedingungen werden weiter kontrolliert. Zeitjets folgen aus der bisherigen direkten Auflösung. Die gespeicherten65 Tangentialrichtungen sind lineare Startdaten, keine65 unabhängig integrierten regionalen Lösungsfelder.

Für eine regionale Familie Psi(x;lambda) sind konstante Parameter von Funktionen lambda(x) zu trennen. Letztere erzeugen zusätzliche Kettenregelterme und müssen die symmetrische Fortsetzung erfüllen. Nicht punktweise beliebige Vertreter zusammensetzen.

## Bloch-Ball des AB-Registers

Für A,B in C^4, N=||A||²+||B||²>0, verwende
rho_AB=1/N [[A†A,B†A],[A†B,B†B]].
Dann rho=(I+r dot sigma)/2 mit
r=(2 Re(A†B),2 Im(A†B),||A||²-||B||²)/N.
Exakt gilt 1-|r|²=4 det(rho)>=0. Wolfram bestätigte die algebraische Identität. Proportionale A/B-Zustände liegen auf der Kugeloberfläche; unabhängige Spinorzustände können im Inneren liegen. Eine Beschränkung auf die Oberfläche würde die frühere Rang1-Annahme erneut einführen.

Diese Darstellung ist zunächst die positive interne Gramdarstellung; eine physikalische Teilspur setzt die entsprechende Tensorprodukt-/Messinterpretation voraus. Die volle Drei-Spezies-Familie liegt zudem nicht allein im AB-Register: C und seine Kopplungen bleiben erhalten.

Die Bloch-Koordinaten vereinfachen Normierung, AB-Kohärenz und die Diagnose des Verlusts der Proportionalität. Sie enthalten jedoch nicht die komplette Dirac-Orientierung. Exaktes Gegenbeispiel: A=cos(theta)e1,B=sin(theta)e1 und A=cos(theta)e3,B=sin(theta)e3 besitzen dieselbe rho, aber A†beta A-B†beta B=+cos(2theta) bzw -cos(2theta). Die notwendige Zustandsbedingung h(A†beta A-B†beta B)=8 kann daher aus r allein nicht berechnet werden.

## Arbeitsregel ab diesem Stand

Bloch-Koordinaten dienen als interne, geometrisch übersichtliche Parameter; Dirac-Orientierung, C-Kopplung und ein gegebenenfalls erforderlicher Spinorlift müssen mitgeführt werden. Für die Auslese kommen zusätzliche Hermitesche Registermatrizen rho^(K)_ij=Psi_j†K Psi_i hinzu. Bei K!=I sind sie im Allgemeinen keine positiven Dichteoperatoren. Eine reine Drei-Variablen-Bloch-Feldgleichung ist damit nicht geschlossen.

Nächster diskriminierender Test: die bisherigen symmetrischen Quellenbedingungen auf die65 lokalen Scharrichtungen zurückziehen; danach untersuchen, welche Richtungen Bloch-Registerdaten ändern und welche ausschließlich im Dirac-Lift liegen. So lässt sich die Lage des Hindernisses prüfen, ohne die unzulässige reine AB-Proportionalität erneut aufzuzwingen.

Artefakte OP5_Parametric_Jet_Family_Check.py/.json (inklusive Tangentialbasen), OP5_Bloch_Parametric_State_Check.py/.json. Vorläuferdaten und Evaluatoren nötig. Lokal gespeichert, nicht committed. Keine OP5-Schließung, Paper-Grafik unverändert.
