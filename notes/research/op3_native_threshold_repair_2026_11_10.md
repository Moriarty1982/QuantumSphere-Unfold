# OP3 und die Reparatur eines festen Zweischritt-Fensters

Analytische Erkundung vom 10. November 2026. Sie prüft die native geometrische Persistenzbedingung unabhängig von einer historischen Monte-Carlo-Stichprobe. Die bisherigen endlichen Atlas- und geometrischen Vergleichsmodelle werden nicht als native Evidenz eingesetzt.

## Festes Fenster

Die [Reparaturdefinition](../../sources/research/parts/v470/19_local_op_entry.tex#L1760) fordert nichtnegative Beträge ζ und λ. Sie setzt die geometrischen Obergrenzen auf e = ε_T^♯ − ζ und v = η_T − λ. Der [Zweischritt-Test](../../sources/research/parts/v470/19_local_op_entry.tex#L1825) verwendet beide gegebenen Zustände X₀ und X₁ und denselben Monitor T_N.

Setze A = max(T_N(X₀), T_N(X₁)) und B = |T_N(X₁) − T_N(X₀)|. Für die geometrischen Klauseln gilt genau:

```text
0 ≤ ζ ≤ ε_T^♯ − A
0 ≤ λ ≤ η_T − B
```

Die Positivitäts- und Zulässigkeitsguards für das Paket gelten zusätzlich. War eine der geometrischen Ausgangsschranken verletzt, hat das entsprechende Intervall eine negative Obergrenze. Eine reine Schwellenverschärfung kann das feste Fenster also nicht reparieren. War das Ausgangsfenster einschließlich der übrigen Guards bereits gültig, ist das Nulldatum die kleinste nichtnegative Wahl, sofern es als Datum zugelassen ist.

Das [Reparaturlemma](../../sources/research/parts/v470/19_local_op_entry.tex#L1873) setzt die Existenz eines minimalen Reparaturdatums voraus. Der [anschließende Satz](../../sources/research/parts/v470/19_local_op_entry.tex#L1887) benennt die geometrische Rekalibrierung, liefert aber keine Aktualisierung der Zustände. Die [Kristallkorrektur](../../sources/research/parts/v470/14_local_crystal.tex#L98) verlangt, dass das verstärkte Paket auf dem korrigierten Fenster besteht. In der späteren [Phasenbindung](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1045) wird eine erneute Ausrichtung des zweiten Punkts beschrieben, doch die Definition gibt nur Nachbedingungen an. Auch der [positive Hybridzeuge](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L734) ist durch positive Beiträge und einen Gewinn des Balance-Defekts charakterisiert. Diese geprüften Stellen erzeugen keinen neuen Folgezustand.

## Aktualisiertes Fenster

Die [spätere Kanalnormalisierung](../../sources/research/parts/v470/24_computational_specification.tex#L3369) ersetzt die einseitige Defektprüfung nicht durch eine Betragsprüfung. Bei der üblichen Division durch eine positive Skala bleibt das Vorzeichen erhalten. Falls die Skala zwischen Schritten wechselt, ist zur Erhaltung desselben Tests auch die Schwelle durch dieselbe jeweilige Skala zu teilen. Ein Vergleich mit unverändertem normiertem Grenzwert würde andernfalls die unnormierte Zulässigkeitsgrenze verschieben.

Die [Eintrittsdefinition](../../sources/research/parts/v470/19_local_op_entry.tex#L539) schreibt die beiden spektralen Residuen mit einseitigen Obergrenzen. Ihre expliziten Definitionen sind vorzeichenbehaftet. Damit erfüllt jedes negative Residuum die jeweilige positive Obergrenze, auch bei beliebig großem Betrag. Soll die Bedingung stattdessen Nähe zu null testen, muss ein Betragsmonitor oder eine untere Grenze ausdrücklich eingeführt werden. Beim CL-Residual entspricht das für feste Spektralparameter einer beidseitigen Schranke für δ_CL um den formalen Nullwert. Dies ist eine Spezifikationsfrage und keine Wiederbelebung des archivierten Zielwerts.

Der [Satz zum maschinellen OP-Eintritt](../../sources/research/parts/v470/19_local_op_entry.tex#L1) setzt die endliche Ausführbarkeit des Primzahlgitter-Abstiegs und die Prüfbarkeit der Eintrittsbedingungen voraus. Der Satz konstruiert keinen Abstiegsoperator. Für einen gegebenen endlichen Graphen zulässiger Übergänge kann die Mindestpersistenz rückwärts geprüft werden: B₁ enthält die Zustände, die alle Einzelbedingungen erfüllen. Bⱼ₊₁ enthält diejenigen Zustände aus B₁, die einen Übergang nach Bⱼ mit bestandener geometrischer Differenzprüfung besitzen. Ein Start in Bₘ liefert genau ein Fenster von mindestens m gültigen Zuständen einschließlich des Starts. Der Graph muss dazu zulässige Übergänge und auswertbare Monitorwerte liefern.

Die [Mindestpersistenz](../../sources/research/parts/v470/19_local_op_entry.tex#L585) verlangt mindestens m_min aufeinanderfolgende Zustände mit gültigem Triggerschema. Der geometrische Zweischritt-Test umfasst zwei Zustände und eine Differenz. Bei m_min > 2 kann ein bestandenes Paar allein die Mindestlänge nicht nachweisen. Wenn die geometrische Bedingung als Schranke pro Übergang gemeint ist, müssen die benachbarten Paare eines Fensters gemeinsam geprüft werden. Eine zusätzliche Schranke für den Gesamtweg folgt daraus nur mit akkumulierten Einzeltoleranzen, nicht mit derselben Einzeltoleranz.

Beim Paket-Guard ist zwischen der allgemeinen Zulässigkeitsmenge und ihrer sicheren Teilmenge zu unterscheiden. Der [Zweischritt-Test](../../sources/research/parts/v470/19_local_op_entry.tex#L1825) verwendet die Mitgliedschaft in der sicheren Menge. Die [Beschreibung von PF_A](../../sources/research/parts/v470/19_local_op_entry.tex#L1127) zählt bereits Randkontakt als Ausfall. Beides stimmt überein, wenn der relevante Rand zur sicheren Menge nicht gehört. Andernfalls muss die Randkonvention für einen reproduzierbaren Test explizit festgelegt werden. Das Verlassen des sicheren Bands allein belegt keinen Verlust der QAM-Schließungsklasse.

Der [explizite Schließungsdefekt](../../sources/research/parts/v470/24_computational_specification.tex#L1185) ist log δ_CL + γ₁/(4πγ_L⁵). Bei festem γ₁ und γ_L ist die Änderung zwischen zwei Schritten exakt log(δ_CL(Y)/δ_CL(X₀)). Für die im Zweischritt-Test geschriebene einseitige Schranke Δ_CL ≤ ε_CL^sharp und einen ersten Zustand mit Reserve m = ε_CL^sharp − Δ_CL(X₀) tritt eine neue Verletzung genau dann auf, wenn δ_CL(Y)/δ_CL(X₀) > exp(m). Das setzt positive Korrekturwerte voraus. Eine native Zuordnung Y ↦ δ_CL(Y) wird dadurch nicht konstruiert.

Die Variation des Cutoffs bei festen Frequenzen ist eine Modellwahl. In der historischen Photon-Frame-Definition hängen sowohl T als auch jede Frequenz an γ_L. Setzt man probeweise γ_L = g als variable positive Größe ein, lautet die endliche Summe 2g Σ sin(γ_j g^(−5/2))/γ_j. Ihre g-Ableitung enthält sowohl die Ableitung des Vorfaktors als auch einen Beitrag −5g^(−5/2) Σ cos(γ_j g^(−5/2)). Das ist eine gekoppelte Parameterempfindlichkeit, keine native Zustandsaktualisierung. Die [spätere Carrier-Analyse](../../sources/research/parts/v470/24_computational_specification.tex#L3160) begrenzt den historischen Balancezeugen auf eine sichtbare Screening-Rolle auf der carrier-stabilen Rückroute.

Für eine ausdrücklich neu definierte endliche Theta-Auslesung mit den ersten N festen Frequenzen gilt bei variablem Cutoff T: Die Ableitung der endlichen Summe ist 2 mal die Summe der N Kosinuswerte und betragsmäßig höchstens 2N. Auf einem positiven Cutoff-Intervall I ist der endliche Defekt deshalb Lipschitz mit Konstante höchstens 2N + sup_I |3/2 − 1/T − T/12 − 2β_sym² T|. Die Konstante wächst mit N. Der Befund liefert ohne gleichmäßige Restkontrolle keine Schranke für die historische unendliche Reihe und ohne eine native Abbildung X ↦ T(X) keinen OP3-Zeugen.

Der [Zweischritt-Test](../../sources/research/parts/v470/19_local_op_entry.tex#L1825) schreibt den Theta-Monitor mit einem Schrittindex. Seine [explizite Definition](../../sources/research/parts/v470/24_computational_specification.tex#L1200) verwendet dagegen den Photon-Frame-Cutoff T, das festgelegte Spektrum und die eingesetzten Parameter. Bei festen Eingaben und gemeinsamer Schwelle ist der Wert in beiden Schritten gleich. Eine ausschließlich im zweiten Schritt auftretende Theta-Verletzung braucht daher eine eigene Zustandsabhängigkeit der Eingaben oder einen neu definierten Monitor. Die spektrale Balancevermutung ist [archiviert](../../sources/research/parts/v470/23_physical_readouts.tex#L844).

Halte X₀ fest und setze t₀ = T_N(X₀). Für vorgegebene zulässige Schwellen e und v sei S die Menge der Werte T_N(Y), die über einen nativen zulässigen Hüllenübergang von X₀ erreicht werden. In S zählen nur Folgezustände Y, die auch die vorgegebenen Closure-, Theta- und Paketbedingungen erfüllen.

Wenn X₀ die übrigen Bedingungen erfüllt und v ≥ 0 ist, ist ein reparierter Folgezustand genau dann erreichbar, wenn

```text
t₀ ≤ e  und  S ∩ [t₀ − v, min(e, t₀ + v)] ≠ ∅.
```

Der Beweis ist die Umformung von T_N(Y) ≤ e und |T_N(Y) − t₀| ≤ v. Für einen nichtnegativen Monitor kann die untere Grenze zusätzlich bei null abgeschnitten werden. Liegt der aktuelle Wert t₁ oberhalb des Intervalls, muss eine Operation ihn mindestens um t₁ − min(e, t₀ + v) senken. Liegt er darunter, muss sie ihn mindestens um t₀ − v − t₁ anheben. Bei t₀ > e reicht keine Veränderung des zweiten Zustands.

Ein unveränderter Zustand Y = X₀ erfüllt zwar die geometrische Differenzschranke, falls t₀ ≤ e. Damit wäre aber nur dann ein zulässiger Ersatz konstruiert, wenn die native Übergangsfamilie diesen Schritt zulässt und er die vorgesehene Funktion des ursprünglichen Folgeschritts erfüllt. Ein beliebiger gleichklassiger Zustand zählt ebenso erst nach dem Nachweis eines passenden Hüllenübergangs. Der [OP3-Hüllensatz](../../sources/research/parts/v470/22_op_transport_arguments.tex#L491) prüft die Klassenerhaltung eines gegebenen Übergangs.

Der [Micro-Lock-Update](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1929) nennt ausdrücklich eine Zustandsänderung. Sein Eingang ist aber bereits der reparierte Zustand. Das zugehörige [HC-Menü](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1829) charakterisiert eine Klasse von Kandidaten und ihre Auswahlbedingungen. In diesem Abschnitt wird kein konkreter Operator angegeben, der aus dem durchgefallenen Fenster einen reparierten Eingang erzeugt.

Der [Phasenbindungs-Reparatursatz](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1117) setzt sowohl die geometrische Reparatur als auch ein minimales Phasenbindungsdatum voraus. Der [HC-Capture-Satz](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L2014) setzt seinerseits einen erfolgreichen Micro-Lock-Update voraus. Damit sind zwei Existenzfragen getrennt: den reparierten Eingang aus dem ursprünglichen Fenster erreichen und aus diesem Eingang einen erfolgreichen Lock erzeugen. Die zweite kann die erste nicht ersetzen.

Der nächste native Nachweis braucht eine zustandsändernde, zertifiziert erreichbare Ausprägung der Phasenbindung oder einen anderen konkreten Hüllenübergang. Ihre Auslesung muss das Intervall treffen. Der Ausschluss der reinen Schwellenreparatur gilt für das feste Fenster. Die Existenz oder Unmöglichkeit eines aktualisierten nativen Fensters und der vollständige OP3 bleiben offen.
