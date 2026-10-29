# OP5: vollständige Freigabe der ersten Zustandsableitungen

29.10.2026. Numerischer punktweiser Vergleich, kein regionaler Existenzbeweis.

## Festgehalten und freigegeben

Dieselben zwei proportionalen Feldwerte wie bisher, ursprüngliche Kopplungen, Massenterm und interne Verbindung; Lorentz-Spinverbindung weiterhin null, nicht als Levi-Civita-Verbindung beansprucht. Jetzt alle 48 komplexen ersten Ableitungen der drei vierkomponentigen Spinoren frei (96 reelle Variablen). Volle Spinorgleichung: 24 reelle Komponenten. Die Coframe wird aus den jeweiligen kovarianten Ableitungen neu berechnet und invertiert. Weder E=I noch A/B-Proportionalität der Ableitungen wird erzwungen. Die resultierenden Jets beschreiben ein Verlassen der alten Familie bei denselben anfänglichen Feldwerten.

## Ergebnis

Je Punkt zwei Startwerte: ursprüngliche Ableitungen und flacher Hamilton-Vorschlag. Gedämpfter NumPy-Newton-Schritt mit Pseudoinverse, Differenzen-Jacobi-Schritt1e-5. P1: Restnormen1.62e-11 bzw1.23e-15, detE4.496 bzw4.308, inverser Metrikwert g00=-.413 bzw-7.006. P2: Restnormen3.48e-13 bzw3.26e-15, detE6.496 bzw5.071, g00=-.330 bzw-7.520. Gemeint ist jeweils g^{00}; die alten t-Schnitte sind somit im induzierten lorentzschen Vergleich raumartig.

Kontrolllauf OP5_Full_State_Jet_Control.py verwendet Differenzenschritt1e-6; alle vier Versuche erreichen ebenfalls Restnorm unter1e-9, positive Determinante und negatives g^{00}. Es ist eine numerische Konsistenzprobe, keine zertifizierte exakte Nullstelle. Die unterschiedlichen Coframes zeigen die Unterbestimmtheit; kein Auswahlprinzip oder physikalisch eindeutiger Zustand wurde gewonnen.

## Bedeutung

Der frühere Rest bei allein freier Zeitableitung hängt in diesem Vergleich wesentlich an den festgehaltenen räumlichen Jets. Nach ihrer Freigabe existieren numerisch punktweise verträgliche Zustands-/Coframe-Daten ohne zusätzliche zentrale Verbindung. Deshalb darf die zuvor für die feste Familie gefundene zentrale Krümmungsforderung nicht als universelles Hindernis gelesen werden.

Nicht gezeigt ist, dass ein über ein Gebiet definiertes Feld diese Jets und die differenzierten Gleichungen gleichzeitig erfüllt. Es wurden keine gemischten zweiten Ableitungen, Verbindungsfeldgleichungen, induzierte Levi-Civita-Spinverbindung, native Wirkung oder Einstein-Gleichungen gelöst. Die unveränderte ursprüngliche interne Verbindung kann selbst Krümmung besitzen: das Ergebnis ist kein Nachweis einer krümmungsfreien Gesamtlösung. Alte Ableitungen lassen sich nicht beibehalten; die veränderten räumlichen Jets bedeuten neue Anfangsdaten.

Nächste entscheidende Prüfung: kompatible zweite Jets bei diesem erweiterten Zustandsansatz, mit Coframe-Ableitungen aus den Feldern. Nicht jeden Punkt unabhängig als fertige Raumzeitlösung zusammensetzen. Erst danach lässt sich beurteilen, ob die Obstruktion tatsächlich verschwindet oder eine Ableitungsordnung höher wiederkehrt.

## Artefakte

OP5_Full_State_Jet_Check.py/.json und OP5_Full_State_Jet_Control.py/.json, Reproduktion durch python auf dem jeweiligen Skript. Python/NumPy/SymPy, absolute ausdrücklich angegebene Repository-Basis wie im vorigen Test. Die Solver-Startdaten und resultierenden Jets sind gespeichert; die Tests fixieren noch keine physikalische Quantenzustandsinterpretation. Lokal gespeichert, nicht committed.
