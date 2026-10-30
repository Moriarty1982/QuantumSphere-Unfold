# QSC: Einbettung, Transformationsstruktur und verschiedene Uhren

30.10.2026. Begrenzte Architekturprüfung, keine Vereinheitlichungsbehauptung.

## Oktaventräger

Nach Wahl einer imaginären Einheit I in O existiert eine reelle Zerlegung O=C_I plus C_I-perp, wobei der sechsdimensionale reelle Komplementraum als C^3 beschrieben werden kann. Damit lässt sich das native z=E+iB in einem gewählten sechsreellen Register repräsentieren. Basiswahl und Multiplikationswörterbuch sind zusätzliche Daten; die Zuordnung ist keine automatisch kanonische Einbettung sämtlicher Raumzeit-/Beobachterdaten in ein einzelnes Oktavenelement. Die Dixon-Träger C tensor H tensor O der Quelle besitzen zudem weitere Faktoren; sie sollten nicht stillschweigend auf ein O reduziert werden.

Strukturerhaltungstest: E=(0,1,0),B=0 unter einem Boost entlang x liefert E'=(0,gamma,0),B'=(0,0,-gamma v). E'^2-B'^2=1, aber E'^2+B'^2=(1+v²)/(1-v²). Das bisherige positive euklidische Registermaß ändert sich. Reelle Oktavenautomorphismen erhalten die positive Oktavennorm. Daher kann diese konkrete lineare Feldwirkung im normidentischen Register nicht einfach als reeller O-Automorphismus identifiziert werden. Die Aussage schließt komplexifizierte Träger, andere Aktionen oder zusätzliche Skalendaten nicht aus.

Eine Datenaufnahme in der Sphäre und eine physikalisch korrekte Aktions-/Ausleseabbildung sind getrennte Prüfpflichten. Die vorhandene komplexe/biquaternionische Struktur könnte den Lorentzteil tragen, während O andere Struktur organisiert; dies ist anhand des nativen Operatorwörterbuchs festzulegen, nicht aus Dimensionen allein zu folgern.

## Quellen zur Zeit

sources/research/parts/v470/10_sphaera_and_physics.tex, sec:lorentz und thm:entanglement-shared-time, verwenden tau_n²=|q_n|² und dessen J-Invarianz. Der angegebene Beweis zeigt die Erhaltung des quadratischen Ausdrucks unter der bezeichneten Involution. Das allein identifiziert noch keine vollständige physikalische Uhr, keine allgemeine Zeitentwicklungsgruppe und kein notwendiges/hinreichendes Verschränkungskriterium. Der Legacy-/Statuskontext ist zu beachten.

analysis/OP5_Readout_Order_Timing.md unterscheidet bereits passive Beschreibung, aktive Messkopplung und selektive Auslesung. Die neue Uhrzuordnung muss diese Rollen ebenfalls erhalten.

## Drei Zeitgrößen, nicht vorschnell eine Identifikation

1. Koordinatenparameter t zur Beschreibung eines Feldes.
2. Eigenzeit tau entlang einer gewählten zeitartigen Beobachter-/Materieweltlinie, aus der Metrik bestimmt.
3. Interne Uhranzeige T als Zustandsvariable eines Teilsystems, mit bedingter Auslesung des anderen.

Quantenregime und massiver Beobachter müssen nicht denselben Uhrparameter direkt verwenden. Eine konkrete Zuordnung ist jedoch nötig. Als einfaches kontrolliertes Beispiel gilt fuer psi(tau)=exp(-i omega tau) die Gleichung d psi/dt=-i omega (d tau/dt)psi. Unterschiedliche Raten koennen so aus der Uhrabbildung entstehen, ohne sofort eine zweite fundamentale Zeit zu postulieren. Bei nichttrivialen Beobachterwechseln, Kopplungen oder zeitabhaengigen Basen sind deren weitere Terme zu behalten.

Massive Quantensysteme sind ebenfalls moeglich; die Trennung 'Quanten = keine Masse' ist daher keine zulaessige allgemeine Zustandsaufteilung. Lichtartige Kurven haben keine nichtverschwindende Eigenzeit als mitlaufende Uhr; daraus folgt nicht das Fehlen von Koordinatenentwicklung oder Feldphase. Die Uhrinterpretation muss fuer den jeweiligen Sektor angegeben werden.

## Exakte kleine Gegenpruefung

Zwei anfaenglich ungekoppelte reine Qubits bleiben unter U1(tau) tensor U2(tau) ein Produktzustand, auch wenn sie dieselbe Uhr tau verwenden. Der Determinantentest der2x2-Amplitudenmatrix ergibt exakt0. Gemeinsame Uhr oder gemeinsame Herkunft allein ist deshalb kein allgemeines Verschränkungskriterium. Ein zusaetzlicher nichtseparabler Kopplungs-/Zustandsnachweis waere noetig; die QSC-Spezialdefinition kann nicht stillschweigend als allgemeiner Quantensatz verwendet werden.

## Erweiterte Vermittlungsdaten

Der Vermittler soll neben vollstaendigem Feld, Orientierung, Metrik und Beobachter auch eine Uhrzuordnung tragen: gewaehlte Weltlinie, tau(t), gegebenenfalls interner Uhrzustand und bedingte Auslese. Diese Daten duerfen ueber das Trägerfeld oder weitere Register organisiert werden. Die beiden dynamischen Auslesediagramme muessen dann mit den entsprechenden Zeitparametrisierungen geprueft werden; eine Beobachtertransformation allein wird weiterhin nicht zu einer unitaeren Quanten-Zeitentwicklung erklaert.

Prioritaet: einen nativen einfachen Clock-/Spinorblock samt positivem Adjungierten und Geltungsbereich identifizieren; zwei explizite Zustaende mit gleicher reduzierter Auslesung aber verschiedenen versteckten Uhr-/Orientierungsdaten auf ihre Auslesegeschwindigkeit vergleichen. Nur bei gleicher Geschwindigkeit ist autonome reduzierte Dynamik moeglich. Andernfalls muss der Vermittler weitere Daten oder eine Erinnerungsgleichung behalten. Keine neue universelle Zeit behauptet.

Wolfram bestaetigte Invariante, positive Normaenderung und Kettenregel; SymPy bestaetigte diese und den Produktzustands-Gegencheck. Artefakte QSC_Octonion_Clock_Bridge_Check.py/.json. Lokal gespeichert, nicht committed. Keine native gemeinsame Wirkung oder OP5-Schliessung hergeleitet.
