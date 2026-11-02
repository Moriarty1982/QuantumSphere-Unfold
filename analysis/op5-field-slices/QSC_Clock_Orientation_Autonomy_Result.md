# QSC: gleiche Auslesung, unterschiedliche weitere Auslesegeschwindigkeit

30.10.2026. Zwei exakte begrenzte Tests, Wolfram und SymPy gegengeprüft. Keine native gemeinsame Wirkung hergeleitet.

## Allgemeines Kriterium

Für vollständigen Zustand c, Dynamik X(c) und reduzierte Auslesung pi ist eine autonome reduzierte Dynamik Y nur möglich, wenn Dpi_c X(c) für sämtliche zulässigen c mit demselben pi(c) übereinstimmt. Die Gleichheit der momentan ausgelesenen Zustände reicht nicht. Dieses Faserverträglichkeitskriterium ist bereits in analysis/HC_Projected_Residual_Dynamics.md linear konkretisiert; hier werden Uhr- und Orientierungsdaten isoliert.

## Kontrolliertes Uhr-/Ratenbeispiel

Gemeinsamer vollständiger Träger C²_rate tensor C²_system, gemeinsamer Hamiltonoperator H=diag(a,b) tensor omega sigma_z/2. Zwei vollständige Anfangszustände |0><0| tensor rho und |1><1| tensor rho mit rho=(I+sigma_x)/2 liefern dieselbe reduzierte Systemauslesung. Unter derselben vollständigen Dynamik sind jedoch dot rho_0=-i a omega[sigma_z,rho]/2 und dot rho_1=-i b omega[sigma_z,rho]/2. Für a!=b,omega!=0 verschieden.

Es werden nicht zwei frei gewechselte Hamiltonoperatoren als eine Theorie ausgegeben: H ist in beiden Fällen derselbe, die verborgene Ratenkomponente unterscheidet sich. Die Interpretation dieser Komponente als physikalische Uhr ist eine deklarierte Vergleichsannahme; keine native QSC-Uhr oder Page-Wootters-Zwangsbedingung daraus abgeleitet. Gemeinsame Parametrisierung tau_a=a t,tau_b=b t erklärt den begrenzten Test. Der reduzierte Zustand allein enthält die Rate nicht.

## Native Gram-Auslesung: exakte Geschwindigkeit des Beobachterwechsels

Nimm die bereits dokumentierten Felder E=(2,0,0), B_plus=(0,1,0), B_minus=(0,-1,0). Beide haben G=diag(4,1), rho=diag(4/5,1/5), gleiche Energie und Invarianten E²-B²=3,E dot B=0. Die Orientierungsinformation bzw Richtung des Poyntingvektors unterscheidet sie.

Gemeinsamer Boost entlang z mit v(t), v(0)=0. Der gemeinsame gamma²-Faktor fällt aus der normierten Gram-Auslesung heraus. Es gelten G_plus proportional diag((2-v)^2,(1-2v)^2), G_minus proportional diag((2+v)^2,(1+2v)^2).

Somit d rho_plus/dv|0=diag(12/25,-12/25) und d rho_minus/dv|0=-d rho_plus/dv|0. Für dot v(0)!=0 haben identische anfängliche Zustandsdiskus-Auslesungen entgegengesetzte Auslesegeschwindigkeiten. Es handelt sich um dieselbe vorgegebene Änderung des Beobachterbezugs, nicht die freie zeitliche Entwicklung eines isolierten Qubits. Wolfram und SymPy bestätigen beide Matrizen exakt.

## Konsequenz für die Vermittlungssphäre

Die reduzierte Gram-/Bloch-Auslesung ist für diese zugelassenen Daten nicht autonom unter allgemeinen gerichteten Beobachterwechseln. Uhr-/Rateninformation kann eine weitere Nichtautonomie verursachen. Der Vermittler muss relevante Orientierungs-, Beobachter- und Uhrdaten mitführen oder die reduzierte Gleichung explizit von ihnen abhängig machen; alternativ wären eingeschränkte Zustandsklassen oder Gedächtnisterme zu begründen.

Das ist eine Anforderung an die Zustandsbeschreibung, keine Widerlegung des gemeinsamen oktonionischen Trägers. Eine eigene autonome 'Quantenzeit' folgt ebenfalls nicht. Der native Operator muss erst auf dem vollständigen, getypten Vermittlungspaket ausgewertet werden. Die QAM sollte genau diesen Unterschied zwischen Momentanauslesung, gemeinsamem Zustand und dynamisch geschlossenem Zustand als Prüfpflicht erhalten.

Nächster belastbarer Test: konkrete Auswahl des minimalen nativen Vermittlungspakets und erneute Faserverträglichkeitsprüfung; zusätzliche Daten nicht bloß benennen, sondern aus der vorhandenen Struktur eindeutig auslesen und transportieren.

Artefakte QSC_Clock_Orientation_Autonomy_Check.py/.json, Python/SymPy. Wolfram-Teilrechnungen symbolisch bestätigt. Lokal gespeichert, nicht committed.
