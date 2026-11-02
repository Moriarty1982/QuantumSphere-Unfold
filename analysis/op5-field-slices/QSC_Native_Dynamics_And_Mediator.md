# QSC: native Rollen von Frame, Readout und Dynamik

30.10.2026. Quellenabgleich und exakter begrenzter Vermittlungstest.

## Keine einheitliche Bedeutung aller Transformationen

Die Quelle sources/research/parts/v490-post-release-layers.tex, r04.1/r04.2, realifiziert z=E+iB als F=[E|B] und bildet G=F^T F, rho=G/Tr G. Der Gram-Schritt ist eine verlustbehaftete Auslesung, keine invertierbare Beschreibung des ganzen Feldes. r17 definiert den Zustand explizit relativ zum Beobachterversatz gegen den E-parallel-B-Frame. Änderungen seiner Eigenwerte unter Boost sind deshalb nicht ohne Weiteres eine zeitliche Entwicklung eines autonomen Quantenregisters.

sources/research/parts/v470/10_sphaera_and_physics.tex, thm:unitary-equiv, enthält eine strukturelle unitäre Äquivalenzbehauptung, deren Statusnote offen ist. Eine solche Darstellungsäquivalenz ist selbst bei Nachweis nicht automatisch ein Zeitentwicklungsoperator. Kaskade/Projektor/Compensator sind weitere Operationstypen und dürfen nicht gleichgesetzt werden.

Die physikalische Feldgleichung und der formale Zeitgenerator verlangen eigene Träger, Adjungierte, Definitionsbereiche und Hintergrundgleichungen. Siehe analysis/HC_Projected_Residual_Dynamics.md. Damit ist die Frage nach einer einzigen 'ursprünglichen Dynamik' noch zu grob: der betreffende Übergang muss erst als Frame-, Auslese-, Projektions- oder Zeitschritt typisiert werden.

## Konkreter Test des nativen Gram-Readouts

Nimm zwei Felder E1=(1,0,0),B1=0 und E2=(0,1,0),B2=0. Beide besitzen G=diag(1,0), dieselbe normierte rho, dieselbe Energie und dieselben Lorentz-Invarianten E²-B²=1 und E dot B=0.

Unter demselben Lorentzboost entlang x mit Geschwindigkeit v bleibt das erste Feld rein parallel; sein Zustand bleibt diag(1,0). Für das zweite gilt E2'=gamma(0,1,0), B2'=gamma(0,0,-v), also rho2'=diag(1/(1+v²),v²/(1+v²)). Bei v=3/5 ist dies diag(25/34,9/34). Wolfram und SymPy bestätigen die Formeln exakt.

Ein einziger Boostoperator auf dem reduzierten rho allein kann daher nicht beide erlaubten Fälle abbilden. Auch die zusätzliche Energie oder nur die beiden Lorentz-Invarianten unterscheiden diese Eingaben nicht. Es fehlt die räumliche Orientierung relativ zum Beobachter. Diese Informationsgrenze passt zur bereits bestehenden Analyse analysis/OP5_Realification_And_Gram_Boundary.md; sie wird hier auf die Vermittlungsfrage angewandt, nicht als neue allgemeine Entdeckung beansprucht.

## Verbesserte erste Vermittlungsstruktur

Für diesen elektromagnetischen Teilbereich sollte der Vermittler mindestens das vollständige Feld als geometrisches Objekt mitsamt Beobachter-/Rahmenbezug tragen. Lokal geeignet: Faraday-Zweiform F_ab, Lorentzmetrik, Orientierung und ein normierter zeitartiger Beobachter u (plus Tetrade, falls konkrete Komponenten benötigt werden). Daraus folgen elektrische und magnetische Felder relativ zu u und der native Gram-Diskus. Das Tensorobjekt kann unabhängig von Komponentenwahl beschrieben werden; seine Komponenten transformieren kovariant. Dies ist ein präziser Sinn eines gemeinsamen Vermittlers, ohne alle Auslesewerte für jeden Beobachter gleichsetzen zu müssen.

Ein nur skalarer invariant formulierter Vermittler ist schwächer: Er kann E²-B² und E dot B erhalten, aber nicht die vollständige beobachterabhängige Auslesung oder ihre autonome Entwicklung bestimmen. 'Invariant' muss deshalb entweder eine Menge gemeinsam erhaltener Größen oder die koordinatenunabhängige geometrische Objektbedeutung meinen; diese Forderungen sind verschieden.

Der vollständige Feldträger hat genug Daten, um den beobachterabhängigen Gram-Schritt eindeutig zu berechnen. Das ist jedoch noch keine vollständige Quantenzustandsabbildung: der native reale Gramdiskus ist nur eine Teilbeschreibung. Ebenso ist ein Faraday-Feld mit gegebener Lorentzmetrik noch keine Lösung der ART oder einer gemeinsamen QSC-Wirkung. Die konkrete Einbettung in den oktonionischen Gesamtträger und die Nichtassoziativitäts-/Strukturerhaltungsfragen bleiben zu prüfen.

## Nächster belastbarer Schritt

Zuerst die gemeinsame Transformation auf vollständigem Feld und Beobachter festlegen, dann die zwei Auslesungen daraus vergleichen. Für zeitliche Dynamik ist separat die Faserverträglichkeit nötig: vollständige Zustände mit gleichem Readout müssen gleiche Readout-Zeitänderung haben, falls eine autonome reduzierte Gleichung beansprucht wird. Wenn das nicht gilt, muss der Vermittler verborgene Daten/Erinnerung mitführen. Das ist eine konkrete QAM-Prüfpflicht und kein Grund, die übergeordnete Sphärenidee zu verwerfen.

Artefakte QSC_Native_Readout_Dynamics_Check.py/.json. Quellen wie oben; lokale Ergebnisse, nicht committed. Keine native Operatoridentifikation, universelle Sphäreneinbettung oder OP5-Schließung behauptet.
