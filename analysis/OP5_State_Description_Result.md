# OP5: Audit der proportionalen Zustandsbeschreibung

29.10.2026. Begrenzter Test der bestehenden Vergleichsdynamik, keine vollständige native Zustandsraumherleitung.

## Herkunft der Einschränkungen

Die Familie A=cos(theta)u, B=sin(theta)u, C=w ist ein Vergleichsansatz. Die zuvor geprüfte native Wirkung hat eigenständige Komponenten und Kopplungen zum Querkanal; aus ihren Blockstrukturen folgt keine allgemeine A/B-Proportionalität. Grundlage: analysis/OP5_Native_Action_Closure_Penalty_Audit.md und analysis/OP5_AB_Proportional_Dynamics_Result.md. Die Aussage ist auf diese untersuchten Darstellungen beschränkt, kein Volltextbeweis über jede Manuskriptfassung.

Die Proportionalitätsforderung ist invariant unter gemeinsamem invertierbarem Spinorbasiswechsel. Ihre Verletzung lässt sich deshalb nicht durch einen solchen passiven Framewechsel beseitigen. Bei aktivem Mischen mit C oder Änderung der Auslesung wird dagegen die Bedeutung des ausgewählten AB-Systems verändert.

## Direkter Dynamiktest

Beibehalten: ursprüngliche flache Vergleichsdynamik, räumliche Anfangsableitungen, Kopplungen, N=16 und die zwei alten Punkte. Keine neu angepasste Verbindung. Die Hamilton-Gleichung bestimmt den transversalen Zeitvektor b=c dotB-d dotA=h beta u+i(dp-cq)alpha_s w. Komplexe Proportionalität erfordert b in span_C(u).

Der orthogonale Rest b_perp=b-u(u†b)/(u†u) besitzt quadratische Norm 32.6666666667 an P1 und 42.1684210526 an P2. Relativ zu ||u||² sind dies 4.0833333333 und 5.2710526316. Reproduktion des früheren Gates aus direkter komplexer Projektion; symbolisch aufgebaute Eingaben mit 30 Stellen, anschließende NumPy-Arithmetik. Keine numerische Rangentscheidung erforderlich.

Folge: Die vorgegebenen Anfangsdaten verlassen unter dieser Dynamik sofort die komplex-proportionale AB-Familie. Dies beweist nicht, dass die volle native Dynamik dieselbe Eigenschaft hat. Es zeigt, dass die späteren Verbindungsfits unter einer zusätzlichen, dynamisch nicht erhaltenen Vergleichsbeschränkung erfolgten. Ob die damit berechnete zentrale Krümmung ohne diese Beschränkung fortbesteht, ist neu zu prüfen.

## Geöffnete Zustandsrichtung

Schreibe lokal A=c u-d eta, B=d u+c eta. Bei eta=0 gilt c dotB-d dotA=dot(theta)u+dot(eta). Eine unabhängige vierkomponentige komplexe eta kann den bisherigen transversalen Rest aufnehmen; das ist eine Parametrisierung der durch die Ausgangsdynamik vorgeschriebenen Tangente, kein neuer Potentialfit. Frei gewählte eta löst noch nicht die übrigen Gleichungen oder die geometrische Rückwirkung.

Die Beschränkung eta=0 zwingt den AB-Komponentenblock auf Rang1. Das exakte Zweikomponentenbeispiel A=c e1-d epsilon e2, B=d e1+c epsilon e2 hat Minor epsilon. Sein normierter formaler reduzierter Dichteoperator hat Reinheit (1+epsilon^4)/(1+epsilon²)^2 <1 für epsilon!=0. Damit ist Rangwachstum bereits ohne neue interne Sektoren möglich.

Wichtig: Die Matrixstruktur allein begründet keine physikalische Verschränkung. Dafür fehlen die Bedeutung des Tensorproduktes, der physikalische Zustandsraum und die Messalgebra. Eine klassische Feldkonfiguration ist nicht allein durch Umbenennung ein quantenmechanischer Vielteilchenzustand. Bedingung auf eine Uhranzeige und partieller Trace sind getrennte Operationen.

## Konsequenz für das weitere Programm

Vorrang: unabhängige A,B,C-Felder in der bestehenden Dynamik und Auslese gemeinsam zulassen; insbesondere sämtliche eta-Beiträge zur Coframe und ihren Ableitungen mitführen. Dann erneut testen, ob eine zentrale Krümmung erzwungen bleibt. Erst nach dieser Trennung ist eine Interpretation der Restbedingung als fundamentale Unschärfe oder neues Feld belastbar.

Die bisherigen negativen Resultate bleiben für ihre festgehaltenen Familien gültig. Eine regionale unabhängige Spinorlösung, positive Quantenzustandsstruktur, interne Uhr und native OP5-Schließung sind nicht bewiesen.

Dateien: OP5_State_Description_Check.py/.json. Ausführen mit python OP5_State_Description_Check.py; benötigt die im Skript ausdrücklich referenzierte Repository-Basis, NumPy und SymPy. Lokaler Arbeitsstand, nicht committed.
