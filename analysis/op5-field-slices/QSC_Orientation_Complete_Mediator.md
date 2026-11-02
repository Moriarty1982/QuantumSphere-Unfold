# QSC: Folgerungen aus synchronisierten Uhren und fehlender Orientierung

30.10.2026. Konkrete lokale Rekonstruktion, keine vollständige native Dynamik.

## Fluss allein genügt nicht

E1=(1,0,0),B1=0 und E2=(0,1,0),B2=0 besitzen identische G=diag(1,0), rho und Fluss E cross B=0. Unter demselben Boost entlang x ergibt der erste Fall G'=diag(1,0), der zweite G'=diag(1,v²)/(1-v²). Deshalb genügt auch (G,Flussvektor) nicht für beliebige gerichtete Beobachterwechsel. Der gemeinsame Uhrabgleich ändert dieses Ergebnis nicht.

## Vollständige lokale Rekonstruktion

Für G=[[a,c],[c,b]], a>0 und Delta=sqrt(ab-c²)>0, definiere den kanonischen3x2-Feldvertreter

F0(G)=[[sqrt(a),c/sqrt(a)],[0,Delta/sqrt(a)],[0,0]].

Für das tatsächliche Feld F=[E|B] setze e=E/sqrt(a), q=(B-(c/a)E)/(Delta/sqrt(a)), n=e cross q und O=[e|q|n]. Dann O in SO(3) und F=O F0(G). Beweis durch Skalarprodukte und direkten Matrixeinsatz; Wolfram bestätigte F0^T F0=G, SymPy zwei exakte generische Rekonstruktionen. Damit ist (G,O) auf diesem Chart eine vollständige lokale Feldbeschreibung, keine beliebige Informationsvermehrung: drei Gramparameter plus drei Orientierungsparameter entsprechen den sechs reellen Feldkomponenten.

Wer nur rho aufbewahrt, muss außerdem TrG=2u erhalten. Dann G=2u rho. Observer, Tetrade und Uhrzuordnung sind Kontext-/Vergleichsdaten, nicht automatisch weitere Komponenten desselben Feldregisters. Bei Rangverlust oder E=0 sind andere Charts bzw. Stabilisatorfreiheiten zu behandeln. Nichtverschwindende lichtartige elektromagnetische Felder mit G=u I liegen hingegen im regulären Rang2-Bereich dieser Rekonstruktion; 'lichtartig' ist hier nicht 'Gram-Rang1'.

## Warum die Energieauslesung davon abhängt

Mit c=1, u=(E²+B²)/2, S=E cross B und der bisherigen Boostkonvention gilt

u'=gamma² [u(1+v²)-2 v dot S-(v dot E)²-(v dot B)²].

SymPy verifiziert diese Formel an zwei unabhängigen exakten Feldpaaren gegen die vollständigen Lorentz-Feldtransformationen. Sie zeigt getrennt Flussrichtung und Feldachsen. Energieänderungen des Beobachterwechsels hängen damit nicht nur von Uhrkonversion oder momentanem rho ab. Diese Formel ist eine lokale elektromagnetische Beziehung, kein QSC-Vakuum- oder Lambda-Ergebnis.

## Bedeutung für den sphärischen Träger

Das vollständige z=E+iB im gewählten C^3-Teil trägt bereits die benötigten sechs Felddaten. Die neue Konstruktion sagt daher nicht, dass O oder Dixon 'zu klein' seien. Der Verlust entsteht erst bei der Auslese z->G->rho. Der Vermittler sollte diesen Verlust vermeiden, indem er Orientierung und Skala beim Vergleich mitführt. Reelle räumliche Rotationen wirken in dieser C^3-Darstellung komplexlinear und unitär; die vollständige native Einbettung inklusive Boosts und Multiplikationsstruktur ist weiterhin zu prüfen.

Es bestehen mindestens zwei formal unterschiedliche Kugelbilder: reine Zustände auf einer Qubit-Bloch-Oberfläche und die native elektromagnetische Gram-Auslesung, bei der lichtartige Felder am Mittelpunkt rho=I/2 liegen. Sie dürfen nicht ohne explizite Abbildung gleichgesetzt werden. Eine übergeordnete Sphäre kann beide Beschreibungen tragen, muss aber ihre Typen und Skalen erhalten.

## Was tatsächlich weiter folgt

Für den Beobachterwechsel ist die Auslesung mit vollständigem Feld und Kontext eindeutig bestimmt. Die Orientierung kann nach einem Boost durch dieselbe kanonische Rekonstruktion aus dem neuen F bestimmt werden; nur G bzw rho hatte dafür nicht gereicht. Das beseitigt die dargestellte Informationslücke, leitet aber noch keine eigenständige zeitliche Feldentwicklung ab.

Der nächste native Test lautet: die bereits vorhandenen QSC-Operationen zuerst auf z bzw. den vollstaendigen Träger anwenden, dann (G,O,u) auslesen; separat prüfen, ob eine reduzierte Vermittlung denselben Schritt reproduziert. Zeitentwicklung, Beobachterwechsel und Projektion bleiben unterschiedliche Operationen. OP5-Spinorfortsetzung wird durch die lokale EM-Rekonstruktion nicht automatisch gelöst.

Artefakte QSC_Orientation_Complete_Mediator_Check.py/.json, Python/SymPy; Wolfram-Teilprüfung im Gespräch. Lokal gespeichert, nicht committed.
