# OP5: native Auslesung, verborgener Zustand und Messdynamik

26. Oktober 2026. Fortsetzung von `OP5_Readout_Protocol_Energy_Result.md`.
Lokaler Forschungsstand; keine Änderung am Manuskript und keine Schließung von OP5.

## Ausgangspunkt und engeres Ergebnis

Die native Schnittstelle ist enger bestimmbar als im frei gewählten Qubitmodell:
Die projizierte Mastergleichung enthält bereits einen exakten Test dafür, wann
eine Auslesung überhaupt eine eigenständige Dynamik besitzt. Ein zweiter Test
entscheidet, ob ihr Generator als verlustbehafteter Zweig eines vollständigen
Quanteninstruments interpretiert werden kann. Keiner dieser Tests liefert von
selbst eine absolute Energiedichte oder kosmologische Konstante.

Quellen im Repository: `sources/research/parts/hc-dynamics-and-geometry.tex`,
Abschnitte zur projizierten Autonomie und Elimination des verborgenen Blocks;
`sources/research/parts/v470/10_sphaera_and_physics.tex`, geordnete
Mastergleichung, Variationsform und Closure-Funktional;
`analysis/HC_Real_Probe_Current_Closure.md` und
`analysis/HC_Null_Axis_Action_Check.md` für die Voraussetzungen an Adjungierte,
reelle Wirkung und Uhr. Die folgenden endlichdimensionalen Aussagen sind
direkte algebraische Ableitungen, keine numerischen Experimente. Für
unbeschränkte Feldoperatoren wären zusätzlich gemeinsame Definitionsbereiche
und Existenz der Dynamik nachzuweisen.

## 1. Welcher Frame wann ausliest: der native Autonomietest

Seien u der vollständige reelle Zustand, dot u = G u und r = T(t)u die
Auslesung. Für einen Rechtsinversen R von T ist u = Rr + z mit Tz = 0.
Damit gilt exakt

    dot r = (dot T + TG)Rr + (dot T + TG)z.

Eine von der verborgenen Zustandshebung unabhängige Gleichung für r existiert
genau dann, wenn

    (dot T + TG) ker T = {0}.

Der Term dot T beschreibt hier die zeitabhängige Auslesekarte. Er ist für
sich weder eine Messrückwirkung noch eine Energielieferung. Das Kriterium
verhindert, dass ein anderer Lesetakt oder eine andere Zustandshebung
versehentlich als universelle neue Dynamik ausgegeben wird.

Ein minimales Gegenbeispiel ist der reversible Oszillator

    dot x = omega r,    dot r = -omega x,    T(x,r) = r.

Die Zustände (x,r) = (1,0) und (-1,0) besitzen dieselbe momentane Auslesung,
aber entgegengesetzte erste Ableitung. Nach einer Wartezeit tau ist

    r(t+tau) = r(t) cos(omega tau) - x(t) sin(omega tau).

Aus einem einzelnen r(t) lässt sich das spätere Ergebnis nicht bestimmen.
Bei sin(omega tau)=0 verschwinden die verborgenen Beiträge stroboskopisch;
das beweist keine kontinuierliche Autonomie. Mit dot r oder einer geeigneten
zweiten Auslesung kann x für omega != 0 rekonstruiert werden. Das ist ein
konkreter Grund, zwei komplementäre Auslesungen zu erwägen: Sie können den
fehlenden Zustand identifizierbar machen. Ihre Kombination ist damit noch
kein physikalisch ausgezeichneter neutraler Frame.

## 2. Wann ein geordneter Generator einen Messzweig definiert

In einem festgelegten positiven Hilbertraum sei dot psi = G psi. Setze

    R_loss = -(G + G†),    H = (i/2)(G - G†),
    G = -i H - R_loss/2                         (hbar = 1).

Genau R_loss >= 0 garantiert eine kontraktive Norm für alle Anfangszustände.
Dann kann man beispielsweise L = sqrt(R_loss) wählen und den Generator
zu einer spurtreuen Dynamik vervollständigen:

    dot rho = -i[H,rho] + L rho L† - {L†L,rho}/2.

Der ungejumpte Zweig hat weiterhin Generator G. Seine Norm liefert eine
Überlebenswahrscheinlichkeit. Die Ergänzung ist nicht eindeutig: andere
Sprungoperatoren mit Summe L_j† L_j = R_loss haben dieselbe Verlustdynamik,
aber andere Rücksprünge und Messaufzeichnungen. Ein nativer Generator allein
bestimmt daher noch kein vollständiges Messinstrument und keinen Energiefluss.

Für eine zeitabhängige positive Normmatrix W(t) lautet der entsprechende Test

    dot W + G†W + WG <= 0.

Das folgt unmittelbar durch Ableiten von psi† W psi. Die Wahl und Bewegung
von W müssen physikalisch begründet sein; sie dürfen nicht nachträglich nur
zum Erzeugen eines gewünschten Dämpfungsergebnisses gewählt werden.

## 3. Positive Closure ist noch keine positive Verlustrate

Der native HC-Beitrag hat die geordnete Form

    G_HC = -(Gamma0)^(-1) [kappa Gamma.n + i gamma I] H_C.

Die positive Closure-Konstruktion H_C >= 0 entscheidet deshalb nicht allein
über G_HC + G_HC†. Bereits das reduzierte Produkt D = A H_C zeigt die Lücke.
Wähle im gewöhnlichen euklidischen Skalarprodukt

    A = diag(1,4),    H_C = [[1,1],[1,1]],    G = -kappa A H_C,
    kappa > 0.

Beide Faktoren sind positiv (H_C semidefinit), aber

    R_loss/kappa = A H_C + H_C A = [[2,5],[5,8]].

Seine Determinante ist -9, seine Eigenwerte sind 5 +/- sqrt(34).
Der negative Eigenwert erlaubt anfängliches Normwachstum. Dies widerlegt
die allgemeine Produktfolgerung im gewählten Skalarprodukt; es ist kein
Beweis, dass diese Matrizen der tatsächlich zulässige native Sektor sind.

Ebenso wichtig: Für dieses isolierte Produkt liefert W = A^(-1)

    -(G†W + WG) = 2 kappa H_C >= 0.

Das Gegenbeispiel beweist also keine normunabhängige Instabilität. Eine native
positive Norm könnte die Frage lösen. Für den vollständigen Generator müssen
jedoch auch Transport, Hamiltonanteil und gegebenenfalls dot W mitgeprüft
werden. Insbesondere ist das aus dem Spinorstrom kommende K0 nicht ohne
Herleitung mit A^(-1) identisch.

Eine künstliche skalare Zusatzverlustrate G -> G - alpha I würde das Beispiel
für alpha >= kappa(sqrt(34)-5)/2 kontraktiv machen. Sie verändert die
Überlebenswahrscheinlichkeit, obwohl sie aus der normalisierten bedingten
Zustandsbahn herausfällt. Das ist ein zusätzliches Modell, keine native Lösung.
Reelle Verlustverschiebung und imaginäre Energieverschiebung sind verschieden.

## 4. Was eine Uhr und ein absoluter Anteil noch benötigen

Die kanonische Zweimodenreduktion im Paper behält die verborgenen Partner a,c.
Ihre Elimination erzeugt unter positiver verborgener Hesse-Matrix eine
Trägheit DW^(-1)D. Das dortige Beispiel mit H = m I + omega sigma_y hat eine
reversible Amplituden-Winkel-Kopplung; die scheinbare Dämpfung wechselt bei
Kontraktion das Vorzeichen. Daraus folgt kein irreversibler Reservoirprozess.

Eine ausgelesene Frequenz kann eine interne Vergleichsuhr liefern, sobald
Generator, Norm und physikalische Zeiteinheit identifiziert sind. Die
Nullachsen-HC-Wirkung liefert diese Identifikation bislang nicht: Ihr
Hauptsymbol ist im untersuchten Zweig nur vom Rang eins, und Achsen- sowie
Kopplungsnormalisierung bleiben relevant.

Auch nach einer erfolgreichen Instrument-Vervollständigung bleibt die
Ersetzung H -> H + C I in der Zustandsdynamik unsichtbar. Die zusätzliche
gravitierende Volumenwirkung -integral sqrt(-g) rho_0 braucht eine eigene
Herleitung oder Bedingung. Eine Messverlustrate ist keine solche Bedingung.

## Prüfbarer nächster Übergang

Für einen ausdrücklich gewählten nativen endlichen Sektor sind gemeinsam
anzugeben: positiver Strom/Norm W, vollständiger geordneter Generator G,
Auslesekarten T(t), physikalische Zeitnormalisierung sowie instrumentelle
Rücksprünge und deren Energieaustausch. Dann lassen sich Autonomie und
Kontraktivität mit den beiden obigen Kriterien prüfen. Ohne diese Angaben
wäre jede bestimmte Messachse, Relaxationszeit oder absolute Vakuumenergie
eine zusätzliche Annahme. OP5 bleibt offen; präzisiert wurde die fehlende
Brücke zwischen nativer Gleichung und physischer Auslesedynamik.
