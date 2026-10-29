# OP5: richtungsabhängiger Transport und Unschärfe

29.10.2026. Begrenzte Fortsetzung des Unschärfetests; lokal gespeichert.

Für V=(1,-x/t,-y/t,-z/t) und W=(0,-xz/rho²,-yz/rho²,1) gilt exakt [V,W]=W/t. Gebiet: t!=0, rho²=x²+y²>0. Deshalb enthält der gewöhnliche Transportkommutator auch ohne Verbindungskrümmung einen Beitrag. Die bloße Nichtkommutativität dieser Richtungsableitungen ist kein Krümmungsnachweis.

Setzt man U=W/t, gilt exakt [V,U]=0. Diese Umparametrisierung ist invertierbar auf dem Gebiet; sie beseitigt keine vorhandene Krümmung: F(V,U)=F(V,W)/t. Die zunächst getestete Alternative tW kommutiert nicht; der symbolische Test hat dies erkannt und die Wahl korrigiert.

Für eine zentrale Verbindung c und D_X=X^mu(partial_mu+i c_mu) gilt [D_V,D_U]=i F(V,U). Das ist hier eine Differentialidentität, keine bereits etablierte Quantenobservable.

Eine explizite formale positive Vergleichsstruktur ist L² der Raumzeit mit Volumen 2 dtdxdydz aus der bisherigen Coframe. Für reelles c und kompakt getragene glatte Funktionen sind Pi_X=-i hbar (D_X+div(X)/2) symmetrisch. Es gilt div(V)=-3/t und div(U)=0. Symmetrie bedeutet noch keine Selbstadjungiertheit; die Zeitrichtung ist noch keine physikalische Observable auf dem Raum der Lösungen.

Unter dieser formalen Struktur folgt auf dem gemeinsamen Testbereich [Pi_V,Pi_U]=-i hbar² F(V,W)/t. Für normierte Testzustände ergibt Cauchy-Schwarz somit die bedingte Streuungsgrenze DeltaPi_V DeltaPi_U >= hbar² |<F(V,W)/t>|/2. Punktwerte aus den bisherigen vier Kompatibilitätsproben dürfen nicht als solche Erwartungswerte eingesetzt werden. Das Feld ist noch nicht als regionale Lösung bekannt.

Fortschritt: Der Beitrag allein durch wechselnde Richtungen lässt sich exakt entfernen, während der Krümmungsbeitrag erhalten bleibt. So werden Frame-Anholonomie und zentrale Krümmung mathematisch getrennt. Die Unschärfegrenze bleibt eine Folge einer gegebenen Krümmung; sie leitet deren Quelle nicht her. Die Vergleichsstruktur ist nicht aus der nativen Wirkung abgeleitet und schließt OP5 nicht.

Prüfung: python OP5_Transport_Uncertainty_Frame_Check.py; fünf exakte SymPy-Identitäten bestanden, Ergebnis in gleichnamiger JSON-Datei. Die zusätzlichen Differential-/Symmetrieformeln wurden algebraisch hergeleitet, nicht als vollständiges PDE-System ausgeführt. Kein Commit in diesem Schritt.
