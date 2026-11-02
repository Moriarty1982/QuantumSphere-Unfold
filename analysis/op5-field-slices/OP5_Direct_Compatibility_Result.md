# OP5: direkte Lösung statt Strafterm

30.10.2026. Vergleichssystem, keine regionale Lösung.

An drei Punkten des gespeicherten gemischten Felds werden Feldwerte und zeitliche Coframe E_0 festgehalten. Alle räumlichen Jets zunächst aus dem expliziten Näherungsfeld, aber drei ausgewählte reelle Komponenten dürfen sich ändern. Für jeden Versuch werden räumliche Coframe-Spalten neu berechnet, E_0 beibehalten, inverse Coframe neu berechnet und die zeitlichen Jets durch die invertierbare eingefrorene Zeitmatrix exakt linear bestimmt. Die Differenz zwischen der so ausgelesenen Zeitcoframe und dem vorgegebenen E_0 ist die vierkomponentige Kompatibilitätsfunktion C.

Drei dominante Kombinationen von C werden mit einem3x3-Newton-System gelöst. Drei räumliche Parameter werden per unabhängiger Spaltenauswahl der anfänglichen Jacobi-Matrix gewählt (gepackte Indizes64,28,40). Auch die vierte C-Komponente wird nach jedem Schritt unabhängig kontrolliert, nicht als automatisch null vorausgesetzt. Abseits einer kompatiblen Nullstelle hat die numerische4x72-Jacobi-Matrix zunächst Rang4 mit einer kleinen vierten Singulärzahl; deshalb keine falsche universelle Rang3-Behauptung.

Ergebnis an Zentrum/Rand/Innenpunkt: volle C-Normen2.2e-15,1.1e-15,6.0e-15; vollständige Spinorgleichung4.7e-15,3.6e-15,9.7e-15. Änderungen räumlicher Jetnormen4.59e-5,6.13e-4,9.25e-5. Coframe-Determinanten13.63,13.94,13.48 und g^{00}=-.468,-.533,-.435. Die vollständige Gleichung wird im unabhängigen ursprünglichen NumPy-Residual-Evaluator mit tatsächlich zurückgelesener Coframe geprüft. Keine zusätzliche Verbindung oder Kopplung angepasst.

Wichtige Fortsetzungskontrolle: dieselben Feldwerte und reparierten Jets in das vollständige differenzierte System mit240 symmetrischen zweiten Ableitungen eingesetzt. Rang88, bei Schritten1e-4,1e-5,1e-6 stabile Restnormen .000945332, .02377108, .00948071. Ohne Zweitjetsymmetrie verbleiben bei Schritt1e-5 .000163474, .00100613, .0000745086. Damit keine Fortsetzung bis zur zweiten Ordnung gefunden. Die neuen Punktjets sind keine Ableitungen des vorherigen expliziten globalen Feldes mehr.

Insbesondere gewährleistet das Lösen der algebraischen Zustandsbedingung am Punkt nicht deren Ableitungen dg=0 nach einer Änderung räumlicher Jets. Auch Fortpflanzung der drei weiteren Bedingungen wurde nicht erzwungen. Das direkte3-Parameter-Verfahren löst deshalb den punktweisen Zwang tatsächlich, aber noch nicht das regionale Anfangswertproblem. Der weitere Test muss direkte Kompatibilität mit den differenzierten Zustandsbedingungen gemeinsam aufnehmen, statt erst nachträglich zweite Jets zu fitten.

Artefakte OP5_Direct_Compatibility_Solve.py/.json; OP5_Direct_Compatibility_Lower_Data.json; OP5_Direct_Compatibility_Second_Jet_Check.py/.json. Vorläuferdaten und bestehende Evaluatoren erforderlich. Lokal gespeichert, nicht committed; Paper-Grafik unverändert. Keine native Wirkung, Hyperbolizität oder OP5-Schließung bewiesen.
