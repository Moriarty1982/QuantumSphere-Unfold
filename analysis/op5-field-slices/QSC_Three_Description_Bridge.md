# QSC: drei Beschreibungen und erster Vermittlungstest

30.10.2026. Forschungsdefinition und begrenztes überprüftes Beispiel; keine vollständige Quanten/ART-Vereinheitlichung.

## Rolle der QAM

Die QAM trennt Definitionen, Zustände, Abbildungen, Geltungsbereiche, Nachweise und offene Verpflichtungen. Ein nicht als bewiesen geführter Übergang ist nicht deshalb falsch; er bleibt eine zu untersuchende Behauptung. Ebenso beweist ein erfolgreicher Score-Test noch nicht die behauptete physikalische Übertragung. analysis/OP5_QAM_Zustand_Operator.md fordert bereits eine native Abbildung F:A->A und ausdrücklich nachzuweisende Verträglichkeit R(Fx)=T R(x) sowie echte Guard-Erhaltung. Die folgende Konstruktion bearbeitet genau eine solche Vermittlungsfrage, ohne den offenen Gesamtstatus als Gegenargument zu verwenden.

## Zielarchitektur

Ein gemeinsamer Träger C (möglicherweise mit den vorhandenen komplex/quaternionisch/oktonionischen Strata), ein Quantenbeschreibungsraum Q, ein relativistischer Beschreibungsraum R und eine explizite gemeinsame Vermittlungsstruktur M. Eine vollständige ART-Konfiguration enthält insbesondere Raumzeit, Lorentzmetrik, Verbindung/Materie und zulässige Daten; sie ist keine einzelne2-Kugel. Eine vollständige Quantenbeschreibung verlangt Zustandsraum, Observablen und Dynamik; ein einzelnes Qubit ist nur ein begrenzter Teilbereich.

Erforderliche Abbildungen pi_Q:C->Q, pi_R:C->R und m_Q:Q->M, m_R:R->M müssen den jeweils angegebenen Definitionsbereich tragen. Für denselben zulässigen c ist m_Q(pi_Q(c))=m_R(pi_R(c)) zu prüfen, nicht durch Paarbildung als erfüllt zu deklarieren. Bei gemeinsamer Dynamik U_C und V_Q,V_R kommen pi_Q U_C=V_Q pi_Q und pi_R U_C=V_R pi_R hinzu. Falls Zeit relational definiert wird, sind Uhr und Parametrisierung Teil der Daten. Ein gemeinsamer Vermittler ist nicht automatisch invariant unter voneinander unabhängig gewählten Transformationen.

## Konkret geprüfter lokaler Anfang

M=H_2^+\{0}: nichtverschwindende positive semidefinite hermitesche2x2-Matrizen. Für die Quanten-Seite zunächst erweiterte Zustände (w,rho), w>0, rho>=0, Tr(rho)=1, mit X=w rho. w ist hier eine zusätzliche Vergleichsskala, nicht ohne Weiteres eine Wahrscheinlichkeit. Für die relativistische Seite zunächst ein zukünftiger kausaler Tangentialvektor (u,x,y,z), ohne Nullvektor, in einer gewählten lokalen Spinor-/Lorentzbasis, mit X=u I+x sigma_x+y sigma_y+z sigma_z. Beide sind unterschiedliche Deutungen desselben Matrixobjekts, noch keine vollständigen physikalischen Zustandsräume.

det X=u²-x²-y²-z², Tr X=2u. Der relativistische Ausdruck verwendet die entsprechend positive Zeitnormkonvention; die Raumzeitmetrik kann unabhängig in der bisherigen(-+++)Konvention notiert werden. Aus X folgt rho=X/Tr X. Wer nur rho aufbewahrt, verliert die Skala u. Das gemeinsame Matrixobjekt ist daher informativer als eine einzelne normierte Bloch-Kugel.

Für B in SL(2,C) wirkt X->B X B†. det X und Rang bleiben erhalten. Auf normierten Zuständen induziert dies rho->B rho B†/Tr(B rho B†), auf der Skala w->w Tr(B rho B†). Der entsprechende Normalisierungs-/Transformationsvergleich kommutiert exakt. SU(2)-Rotationen erhalten zusätzlich Tr X und Reinheit; allgemeine Boosts tun das nicht.

Expliziter Boost B=diag(exp(eta/2),exp(-eta/2)): u'=u cosh eta+z sinh eta, z'=z cosh eta+u sinh eta, x'=x,y'=y. Wolfram bestätigte Determinante und Zeitkomponente sowie das normierte z-Verhältnis. SymPy bestätigt unabhängig das kommutierende Normalisierungsdiagramm.

## Trennscharfer Befund

Starte mit rho=I/2. Nach dem normierten Boost ist der Bloch-Vektor (0,0,tanh eta), Reinheit (1+tanh² eta)/2; bei eta=1 etwa.790 statt.5. Damit kann derselbe Boost nicht als gewöhnliche unitäre Evolution desselben Qubits interpretiert werden, weil unitäre Konjugation die Eigenwerte/Reinheit erhält. Die Matrixvermittlung funktioniert algebraisch, die behauptete physikalische Identifikation der Dynamiken braucht weitere Daten.

Ein normierter nichtunitärer Filter oder eine geänderte Beobachter-/Zustandsextraktion wären mögliche Interpretationen, keine bereits bewiesenen Lösungen. Ein physikalischer Filter muss seinerseits die Voraussetzungen eines Quanteninstruments erfüllen. Weder gemischter Zustand gleich Masse noch reiner Zustand gleich physikalisches Photon wird behauptet.

## Einordnung in die oktonionische Sphäre

Das Beispiel nutzt einen gewählten assoziativen komplexen Teilbereich. Seine Einbettung in den tatsächlichen oktonionischen Träger und die Erhaltung der benötigten Operationen sind noch anzugeben. Genügend Komponenten oder eine mengentheoretische Codierung liefern diese Strukturerhaltung nicht automatisch. Umgekehrt ist ihr offener Nachweis kein Beleg gegen die Möglichkeit.

Priorität: die ursprüngliche QSC-Dynamik auf diesem gemeinsamen Teilbereich identifizieren und prüfen, ob sie eine Beobachtertransformation, Zustandsentwicklung oder bedingte Auslesung darstellen soll. Erst danach lässt sich eine nicht nur formal gewählte dritte Vermittlungssphäre physikalisch begründen. Der Boost-Test zeigt konkret, welche vorschnelle Gleichsetzung vermieden werden muss.

Artefakte QSC_Three_Description_Bridge_Check.py/.json. Python/SymPy; Wolfram-Teilprüfungen im Gespräch. Lokal gespeichert, nicht committed. Kein neuer Beweisstatus des gesamten QSC oder OP5 gesetzt.
