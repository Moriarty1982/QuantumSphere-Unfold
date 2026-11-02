# QSC: zuerst Uhren abgleichen

30.10.2026. Exakter kontrollierter Folgetest, keine native Uhrenherleitung.

Im vorherigen Ratenbeispiel entwickelt sich rho_a(t_a) mit Phase omega a t_a und rho_b(t_b) mit Phase omega b t_b, a,b>0. Gleiche Startanzeige t_a=t_b=0 allein beseitigt den Unterschied der Änderungsraten nicht.

Nach Abgleich von Nullpunkt und Gangrate definiere tau=a t_a=b t_b. Dann gilt rho_a(tau/a)=rho_b(tau/b) exakt für alle tau. Mit festen Offsets wäre tau=a t_a+delta_a=b t_b+delta_b zu verwenden, einschließlich gemeinsamer Anfangsphase. Wolfram und SymPy bestätigen die Matrizenidentität.

Damit ist der Unterschied dieses ausdrücklich konstruierten Uhr-/Ratenmodells vollständig durch Parametrisierung erklärbar. Das ist keine Lösung für beliebige gekoppelte Uhren: der Hamiltonoperator wurde gerade mit diesem Ratenfaktor definiert. Ein physikalischer Vergleich zur selben Koordinatenzeit kann weiterhin unterschiedliche lokale Phasen zeigen; die Umparametrisierung erklärt den Unterschied, beseitigt ihn nicht als Messsignal.

Auch die Formulierung als System mit versteckter Rate bleibt bei fehlender Rateninformation nicht autonom bezüglich des ursprünglichen gemeinsamen t. Zur gemeinsamen tau überzugehen benutzt die vorher zusätzlich bekannten a,b. Daraus folgt weder eine universelle neue Quantenzeit noch die Möglichkeit globaler Synchronisierung in jeder gekrümmten Raumzeit.

Orientierungstest separat unter derselben Uhr tau: E=(2,0,0), B_plus/minus=(0,+/-1,0), gemeinsamer Beobachterwechsel v(tau), v(0)=0. Die Auslesegeschwindigkeiten bleiben verschieden: Differenz diag(24/25,-24/25) mal dv/dtau. Eine gemeinsame positive Zeitumparametrisierung beseitigt diesen Richtungsunterschied bei nichtverschwindender Boostrate nicht. Hier liegt keine unterschiedliche Uhr als Ursache vor.

Folgerung: Synchronisierung zuerst ist der saubere diskriminierende Test. In diesem Beispiel verschwindet die Uhrkomponente, während Orientierungsinformation weiterhin gebraucht wird. Der Vermittler sollte die Uhrkonversion explizit führen; er muss keine zusätzliche Zeit postulieren, solange dieses einfache Modell genügt. Native Clock-/Kopplungsdaten müssen erst auf eine solche Konversion geprüft werden.

Artefakte QSC_Clock_Synchronization_Check.py/.json. Python/SymPy; Wolfram bestätigt Teilidentitäten. Lokal gespeichert, nicht committed.
