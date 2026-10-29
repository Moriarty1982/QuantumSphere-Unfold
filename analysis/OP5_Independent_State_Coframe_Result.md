# Unabhängige Zustandsableitungen mit geometrischer Rückwirkung

29.10.2026. Begrenzter numerischer Versuch; OP5 offen.

Vertrag: ursprüngliche proportionale Feldwerte an den zwei bisherigen Punkten, ursprüngliche räumliche Ableitungen und Kopplungen; sämtliche zwölf komplexen zeitlichen Feldableitungen frei. Die zeitliche Proportionalität wird nicht erzwungen. Coframe E_a_mu=Re(Psi†(S tensor K_a)D_mu Psi) wird bei jedem Versuch neu berechnet, ihre Inverse im kinetischen Operator verwendet. Massenterm unverändert. Lorentz-Spinverbindung bleibt null wie im bisherigen Vergleich, nicht als Levi-Civita-Verbindung behauptet. Keine zusätzliche interne Verbindung.

Verfahren: reelles System mit 24 Variablen und 24 Residualkomponenten. Finite-Differenzen-Jacobi mit Schritt1e-5, NumPy-Pseudoinverse rcond1e-11 und gedämpfte Schritte. Je zwei Startwerte: alte zeitliche Ableitungen sowie Vorschlag der ursprünglichen flachen Hamilton-Gleichung. SciPy nicht verfügbar, daher kleiner expliziter NumPy-Newton-Solver im Skript. Keine globale oder zertifizierte Nichtexistenzaussage.

Vollständige Residualnorm fällt an P1 von10.11325 auf1.76777, an P2 von12.54439 auf1.97634. Beide Startwerte erreichen jeweils ähnliche Restnormen, aber unterschiedliche Coframes. Determinanten etwa1 bis1.041 bzw1 bis1.031; g_inverse_00 negativ, ungefähr -1 bis-.923 bzw-1 bis-.941. Die Versuche verbessern die volle Gleichung stark, erreichen aber keine Nullstelle.

Damit reicht das Freigeben unabhängiger Zeitrichtungen an diesen festgehaltenen räumlichen Anfangsdaten im getesteten Solver nicht zur Lösung. Das ist kein Beweis, dass unabhängige Zustandsfelder insgesamt scheitern: die räumlichen Jets bleiben aus der alten eingeschränkten Familie übernommen. Außerdem ist die vorgegebene Coframe-Auslese selbst eine zusätzliche Bedingung. Die frühere zentrale Krümmungsforderung wurde hier nicht erneut als notwendige Bedingung hergeleitet und darf nicht als bestätigt gelten.

Nächste trennscharfe Frage: Welche algebraische Projektion erzwingt den verbleibenden Rest, und hängt sie an den eingefrorenen räumlichen Jets oder am gleichen Auslese-/Bewegungsgesetz? Vor weiterer Parameterfreigabe ist der Rest zu attribuieren. Zweiter unabhängiger Solver und Variation der Differenzenschritte fehlen noch.

Reproduktion: python OP5_Independent_State_Coframe_Check.py; NumPy, SymPy und ausdrücklich referenzierte Repository-Basis nötig. Vollständige Werte, Ableitungen und Coframes in gleichnamiger JSON-Datei. Lokaler Arbeitsstand, nicht committed. Kein physikalischer Quantenzustandsraum oder regionale PDE-Lösung nachgewiesen.
