# OP5: relativer Verbindungskanal und lokale Sektoren
28.10.2026. Fortsetzung der Phasenintegrabilität. Vergleichsmodell; kein OP5-Abschluss.

Die lokale Phasenreparatur lässt sich am gleichen Feldwert als zusätzliche interne Verbindung B_mu=diag(-d/c,c/d,0) l_mu darstellen. Bei D=partial+iA reproduziert iB Psi genau die zuvor eingesetzten Phasenjets. Ihr reeller Coframe-Beitrag verschwindet am proportionalen Startwert.

Mit P_AB=diag(1,1,0), Z_AB=diag(1,-1,0) gilt:
Z_theta=[(c/d-d/c)/2]P_AB-[(c/d+d/c)/2]Z_AB,
Z_AB=-i[S,Y], P_AB=4S².
Damit ist der Operator in der assoziativen Algebra vorhandener Matrizen darstellbar. Das begründet weder seine Zulässigkeit als Lie-Algebra-Generator noch seine Stärke oder Bewegungsgleichung. Native Auditnotizen enthalten einen internen Verbindungsplatz, aber keine fertige Herleitung dieser Komponente.

Die Originalverbindung A_mu=s_mu G hat verschwindende gegenseitige Kommutatoren; ihre Ableitungen bleiben in der gewählten Darstellung offdiagonal. Die zusätzlich benötigte diagonale Verbindung ist darin nicht vorhanden. Nichtgeschlossenheit der Phasen-Einform bedeutet, dass die neue diagonale Verbindung für sich nicht bloß ein skalarer Phasengradient ist. Diagonal/offdiagonal ist basisabhängig und beweist keine globale Eichinequivalenz. Der Massenterm hY tensor beta wird nicht zur Zeitverbindung umgedeutet.

## Spurfreie Gegenprobe
Die exakt C unverändert lassende Matrix Z_theta hat im Allgemeinen nichtverschwindende Spur. Zhat=Z_theta-Tr(Z_theta)I/3 ist eine mögliche spurfreie Alternative. Sie erhält die transversale A/B-Reparatur und die reelle Coframe, verändert jedoch gemeinsame A/B- und C-Gleichungen.

Quadratische vollständige Restnormen:
- Original: P1 102.27778; P2 157.36176.
- Zusätzlicher diagonaler Kanal: P1 69.61111; P2 113.99334.
- Spurfreie Alternative: P1 128.72222; P2 206.90562.

Die C-Restnorm wächst bei der spurfreien Alternative auf 11.0955 bzw. 14.0162. Eine algebraisch erlaubte Form liefert also nicht automatisch die richtige Gesamtdynamik. Beide Varianten sind gefittete Vergleichserweiterungen, keine hergeleiteten Feldlösungen.

## Präzisierung zur Idee unzerlegbarer Teilbereiche
Die frühere Kommutantenprüfung enthielt ausdrücklich den Ausleseoperator S. Ohne diese Zusatzforderung hat die eingefrorene dynamische Familie eine weitere Struktur:
R=I-2G²/(p²+q²), J=R tensor gamma5.
Für p²+q² ungleich null gilt exakt R²=I, [R,G]=0 und {R,Y}=0. Deshalb kommutiert J mit den eingefrorenen Matrizen I tensor alpha_i, G tensor alpha_s und Y tensor beta. J²=I liefert zwei punktweise Projektoren (I±J)/2, jeweils Rang sechs.

Diese unabhängige algebraische Beobachtung wurde lokal mit SymPy überprüft. S kommutiert im Allgemeinen nicht mit J. Außerdem ist J ortsabhängig: Der vollständige Differentialoperator erzeugt Ableitungen von J. Deshalb ist die punktweise Zerlegung noch keine erhaltene globale dynamische Sektoraufteilung. Die zusätzliche diagonale Verbindung muss ebenfalls gegen diese Projektoren geprüft werden. Die Blöcke sind nicht bereits als ihrerseits irreduzibel nachgewiesen.

Das ist ein konkreter Ansatz zur Nutzeridee nicht weiter teilbarer Teilbereiche, aber kein Primzahlgesetz, kein Beweis elementarer Teilchen und keine neue physikalische Konstante.

Nächster Schritt: kovarianten Transport der Projektoren prüfen, statt weitere Potentialkoeffizienten nur an Restgleichungen anzupassen. Eine vorhandene Verbindung könnte die lokale Zerlegung transportieren; ob sie dies tatsächlich tut und mit der Auslese vereinbar ist, bleibt offen.

Dateien: OP5_Relative_Connection_Channel_Check.py/.json (exakte Matrixidentitäten), OP5_Relative_Connection_Residual_Check.py/.json (vollständige Vergleichsreste). Lokal gespeichert, nicht committed.
