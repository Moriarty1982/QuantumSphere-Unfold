# OP5: transversale Fixierung der zeitlichen Coframe

29.10.2026. Linearisierte punktweise Diagnose am gespeicherten gemischten Feld, keine globale Eichfixierung.

Feste Feldwerte und räumliche Jets aus OP5_Peak_Mixed_Check.json; volle zeitliche Jacobi-Matrix J=dF/d(partial_t Psi) einschließlich Coframe-Rückwirkung. 24 reelle zeitliche Variablen. Drei Punkte: Zentrum, früherer kritischer Rasterrand (.99,.59,.01,-.01), innerer Punkt (1.005,.605,-.005,.005). Drei zentrale Differenzschritte1e-4,1e-5,1e-6, relative Rangschwelle1e-8. Die zugrunde liegenden ersten Jets werden aus der expliziten Feldfunktion differenziert.

Definiere A=dE_0/d(partial_t Psi), eine reelle4x24-Matrix. Sei B die24x4-Matrix mit den vier reell gepackten kovarianten Jets D_nu Psi als Spalten. Exakt folgt AB=E aus der Cross-Auslese. Bei invertierbarem E hat B Rang4 und A Rang4; keine numerische Zufallskoinzidenz. Der volle kinetische Ausdruck bleibt bei den entsprechenden punktweisen Coframe-/Jet-Scherungen unverändert, weshalb JB=0.

Damit ist P=I-B E^{-1} A ein expliziter Projektor: P²=P, AP=0, PB=0, Rang20. Er entfernt genau die vier bekannten punktweisen Scherrichtungen und wählt A delta(partial_t Psi)=0, also konstante zeitliche Coframe bei linearen Änderungen. Projektoridentitäten an allen drei Punkten numerisch unter1e-9 kontrolliert; AB-E unter2e-15.

Ergebnisse an allen drei Punkten und Schrittweiten: RangJ20; Rang des auf ker(A) eingeschränkten24x20-Operators20; Rang der gestapelten Matrix [J;A]24. Kleinste Singulärzahl des eingeschränkten Operators .1587 bis.1873, Konditionszahl15.2 bis17.3 in den verwendeten euklidischen Normen. JB relative Abweichung ungefähr1e-11 bei Schritt1e-5. Die Fixierung beseitigt somit die vier beobachteten Nullrichtungen im getesteten linearen Problem.

Wesentliche Grenze: Der reduzierte Operator besitzt24 Gleichungszeilen gegen20 freie Zeitrichtungen. Voller Spaltenrang bedeutet Eindeutigkeit einer linearen Korrektur, sofern die Quelle im Bild liegt; es garantiert keine Lösung für jede Quelle. Vier linke Verträglichkeitsbedingungen sind weiterhin zu behandeln. Die bereits bekannte skalare Zustandsbedingung ist nicht automatisch die gesamte Menge dieser Bedingungen.

Ebenso ergibt die punktweise Scherfreiheit noch keinen Beweis für eine regionale Koordinaten-/Eichsymmetrie. Ein vorgegebenes E_0(x) muss mit den restlichen Coframe-Komponenten, den integrablen Jets und den transportierten Hintergrundkopplungen zusammenpassen. Die Annahme, E_0 überall konstant zu setzen, wurde nicht getroffen. Eine festgehaltene Vergleichsverbindung ist nicht ohne Weiteres unter beliebigen aktiven Änderungen invariant.

Folge: Die vier Nullrichtungen erfordern an diesem Punkt keine vier neuen physikalischen Felder; sie besitzen eine explizite algebraische transversale Fixierung. Nächster mathematischer Schritt ist die vollständige linke Kompatibilitätsanalyse der reduzierten Evolution samt Fortpflanzung, danach erst eine regionale Entwicklung. Keine Hyperbolizität oder regionale Lösung aus invertierbarer eingefrorener Dirac-Matrix ableiten.

Artefakte OP5_Temporal_Coframe_Gauge_Check.py/.json, Python/Torch/NumPy und Vorläuferdaten erforderlich. Lokal gespeichert, nicht committed; native Wirkung und OP5-Schließung offen.
