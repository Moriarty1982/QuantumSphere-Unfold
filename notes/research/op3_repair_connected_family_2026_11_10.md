# OP3: Welche Übergangsfamilie könnte das Reparaturintervall treffen?

Analytische Erkundung im Anschluss an [die Schwellenprüfung](op3_native_threshold_repair_2026_11_10.md). Der erste Zustand bleibt fest. Das dort abgeleitete zulässige Intervall sei [L,U], mit L ≤ U.

Sei A die Menge der Parameter einer konkreten Übergangsfamilie, für die der Folgeschritt nativ erreichbar ist und Closure, Theta, Paketbedingungen und die Funktion des ursprünglichen Folgeschritts erfüllt. Die beiden geometrischen Monitorgrenzen werden bei der Bildung von A ausgespart. Sei t(a) der Monitor des Folgezustands.

Auf jeder zusammenhängenden Teilmenge C von A, auf der t stetig ist, bildet t(C) ein Intervall. Finden sich a,b in demselben C mit t(a) ≤ U und t(b) ≥ L, dann trifft t(C) das Reparaturintervall. Liegt einer der Werte bereits darin, ist er der Zeuge. Andernfalls liegen die Werte auf verschiedenen Seiten und die Stetigkeit liefert einen Zwischenwert. Die Aussage setzt wie zuvor voraus, dass der feste erste Zustand alle Bedingungen erfüllt.

Ein Einschluss durch zwei Werte aus verschiedenen zulässigen Komponenten reicht dagegen nicht. Beispiel: A = [0,1] ∪ [2,3], t(a) = a, Zielintervall [1,2; 1,8]. Beide Seiten sind erreichbar, aber kein Wert dazwischen. Auch Infimum und Supremum allein können einen Treffer am Rand vortäuschen, wenn der Grenzwert nicht erreicht wird.

Für die Phasenbindung lautet die nächste Quellenfrage damit konkret: Gibt es eine parametrisierte native Familie, auf der die nichtgeometrischen Guards beim Variieren erhalten bleiben? Erst innerhalb einer solchen Familie kann ein Phasenscan mit zwei einschließenden Werten einen Existenznachweis liefern. Für die bisher geprüfte Definition mit Nachbedingungen liegt diese Familie noch nicht vor. OP3 bleibt offen.

## Lokaler Test auf Beweglichkeit bei exakter Phasenbindung

Für eine glatte native Familie X(a) auf einer offenen Parameterkarte fasse F(a) = 0 die aktiven Gleichheitsbedingungen zusammen. Dazu gehört die Phasenbindung, sofern sie durch glatte Gleichungen beschrieben wird. Falls der protokollierte Defekt ein Betrag ist, braucht man dafür eine glatte zugrunde liegende Residualgleichung oder eine andere reguläre Beschreibung seiner Nullmenge. Die übrigen Ungleichungen seien am Ausgangspunkt a* strikt erfüllt.

Hat F lokal konstanten Rang, ist die Nullmenge nahe a* eine Untermannigfaltigkeit mit Tangentialraum ker DF(a*). Für den geometrischen Monitor t gibt es genau dann eine Änderung erster Ordnung entlang einer glatten zulässigen Kurve durch a*, wenn Dt(a*) auf ker DF(a*) nicht identisch null ist. Äquivalent erhöht die zusätzliche Monitorzeile den Rang der Jacobi-Matrix um eins. Dann sind Monitorwerte auf beiden Seiten von t(a*) lokal erreichbar. Das liefert nur einen lokalen Wertebereich. Für ein weiter entferntes Reparaturintervall braucht es eine Fortsetzung oder eine quantitative Schranke.

Hat DF vollen Spaltenrang, ist der gebundene Punkt lokal isoliert. Ein einzelner regulärer Phasenparameter mit einer Gleichung und von null verschiedener Ableitung fällt darunter. Bei einem verbleibenden Tangentialraum und verschwindender Monitorableitung ist nur eine Änderung erster Ordnung ausgeschlossen.

Die [Definition der Phasenbindung](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1045) fordert exaktes Verschwinden des Defekts. Sie gibt weder die native Parameterkarte noch die Residualabbildung an, auf der sich der Rang bestimmen ließe. Für den nächsten Quellenabgleich werden damit zwei konkrete Daten benötigt: eine Zustandsabbildung und eine reguläre Gleichungsbeschreibung der aktiven Guards. OP3 bleibt offen.

## Was das endliche HC-Menü leisten kann

Die [Definition des lokalen HC](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1163) gibt den Typ der gesuchten Abbildung an: Der erste Zustand bleibt fest, der bereits reparierte zweite wird ersetzt. Die anschließende Zulässigkeitsdefinition verlangt strikten Rückgang des Phasenfehlers, kontrollierte Closure und keinen Anstieg des Carry-Defekts. Das Bombe-Menü enthält endlich viele Kandidaten und filtert sie nach Zulässigkeit. Die geprüften Definitionen liefern keinen konkreten Kandidaten als Formel.

Für ein festes Eingangsfenster hat das Menü höchstens so viele Ausgänge wie Kandidaten. Stetigkeit zwischen zwei ihrer Monitorwerte folgt daraus nicht. Auch Iteration würde einen zusätzlichen Nachweis erfordern: Selbst bei erhaltener Zulässigkeit und exakter Halbierung eines positiven Phasenfehlers in jedem Schritt bleibt dieser nach jeder endlichen Zahl von Schritten positiv. Ein exakter Lock braucht einen erreichbaren Nullschritt oder, wenn ein Grenzübergang zugelassen ist, Konvergenz der Zustände und Zulässigkeit des Grenzzustands. Ein bloßer Rückgang des Defekts beweist keines von beidem.

Damit sind zwei konkrete Prüfwege getrennt. Für ein tatsächlich auswertbares endliches Menü genügt die direkte Suche nach einem zulässigen Ausgang mit Phasenfehler null und Monitor im Reparaturintervall. Für einen Zwischenwertnachweis braucht es eine eigene kontinuierliche native Familie. Zudem arbeitet der hier definierte HC auf einem bereits reparierten Eingang. Die Quellenstelle löst die vorgelagerte geometrische Reparatur nicht.

## Nullschritt aus einem vorzeichenbehafteten Phasenresiduum

Der [Micro-Lock-Update](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L1929) setzt einen HC-Kandidaten voraus, der auf dem reparierten Eingang wirkt. Die Erfolgsdefinition fordert verschwindendes Phasenleck. Ein Vorzeichen für die zugrunde liegende Abweichung ist dort nicht angegeben.

Für den Lock-Schritt lässt sich der bisherige Zwischenwerttest umkehren: Hält eine konkrete kontinuierliche Familie das geometrische Reparaturintervall, den Lock-Korridor und alle übrigen Guards ein, genügt auf dieser Familie ein stetiges reelles Residuum r, dessen Nullmenge genau dem verschwindenden Phasenleck entspricht. Zwei Werte r(a) < 0 < r(b) auf einem zusammenhängenden zulässigen Parameterintervall erzwingen dann einen exakten Lock. Ein nichtnegatives Leckmaß liefert diesen Vorzeichentest nicht. Für eine Kreisphase wäre eine konsistente lokale Winkelkarte nötig. Bei mehreren unabhängigen Phasengleichungen reicht der skalare Test nicht aus.

Die Quellenstelle liefert weder eine solche HC-Familie noch ein vorzeichenbehaftetes Residuum. Das Kriterium gilt ab dem bereits reparierten Eingang. OP3 bleibt offen.

## Der Schalenquotient als vorzeichenbehaftete Diagnose

Im historischen Antiphasenkorridor |ζ_sh + 1| ≤ ρ < 1 gilt Re ζ_sh < 0. Damit ist Im ζ_sh ein stetiges vorzeichenbehaftetes Residuum für die Antiphase des sichtbaren Quotienten. Seine Nullmenge im Korridor ist genau die negative reelle Achse. Für einen stetigen zulässigen Übergang mit Vorzeichenwechsel folgt daher ein exakter Antiphasentreffer. Der Betrag des Quotienten muss dort nicht eins sein.

Der [Transporttext](../../sources/research/parts/v470/22_op_transport_arguments.tex#L677) führt diesen Quotienten als sichtbare Diagnose. Der [Vorbefund](qam_r27_richtungsreadout_2026_11_07.md#quellenabgleich-zur-nativen-phasenbindung) trennt seine Phase von der Phase der elektromagnetischen Invariante. Für den Micro-Lock wäre zusätzlich zu zeigen, dass ein negativer reeller Quotient innerhalb des zulässigen Korridors verschwindendes Phasenleck impliziert. Der Korridor allein impliziert weder diese Brücke noch die Erreichbarkeit beider Vorzeichen. OP3 bleibt offen.

## Wann der historische Fehlerterm einen Vorzeichenwechsel zertifiziert

Der [historische Antiphasensatz](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6244) begrenzt Abstände und lässt damit auch einen konstanten Quotienten −1 + iρ/2 zu, wenn 0 < ρ < 1. Aus der Korridorschranke allein folgt kein Vorzeichenwechsel.

Die ungekürzte Formel im Beweis gibt jedoch einen Test. Setze q = Im[(A_sh ε_conj + Δ_AB b_sh)/Γ_ph] und d = |ζ_sh − ζ_Γ|. Dann liegt Im ζ_sh im Intervall [q − d, q + d]. Ein Anfangspunkt mit q < −d und ein Endpunkt mit q > d erzwingen entgegengesetzte Vorzeichen trotz der Abweichung zwischen beiden Quotienten. Für einen stetigen zulässigen Weg im Korridor folgt dann sichtbare Antiphase. Der historische Betragstest verwirft gerade die Vorzeicheninformation, die hierfür benötigt wird.

Die geprüfte Stelle garantiert keine solchen Punkte. Für die weitere Quellensuche ist der konkrete Ausdruck q entscheidend, besonders ob der Konjugations- oder A/B-Fehler ihn bei zulässiger Variation durch null treibt. Die Verbindung zum exakten Micro-Lock bleibt separat offen.

## Welche der beiden Fehlerquellen die Phase drehen kann

Aus Γ_ph = A_sh a_sh ≠ 0 und b_sh = −a_sh + ε_conj folgt für die Faktoren R = B_sh/A_sh und E = ε_conj/a_sh exakt ζ_Γ = R(E − 1). Der [historische Beweis](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6146) lässt sich damit nach Phasenwirkung aufteilen:

- Bei exakter Konjugation (E = 0) ist Im ζ_Γ = −Im R. Eine rein reelle A/B-Abweichung kann allein keinen Vorzeichenwechsel erzeugen.
- Bei exaktem Transportgleichgewicht (R = 1) ist Im ζ_Γ = Im E. Ein Vorzeichenwechsel müsste dann aus der normierten Konjugationsabweichung stammen.
- Ist R durchgehend reell und positiv, gilt Im ζ_Γ = R Im E. Eine Variation seiner Stärke kann einen Wechsel des Vorzeichens von E nicht ersetzen.

Diese Aussagen betreffen den linearen Quotienten ζ_Γ. Für den sichtbaren Quotienten muss der jeweilige Imaginärteil weiterhin die Quotientenabweichung übertreffen. Die Definition von Δ_AB als Differenz liefert keine native Variation von Im R, und die Definition des Konjugationsdefekts liefert keine Variation von Im E. Für die Fortsetzung ist deshalb zuerst der Wertebereich dieser normierten Größen auf einer konkreten Transportroute zu bestimmen.

## Variation der Schalenkoordinate bei festem Hintergrund

Der historische Text führt A_sh und B_sh als erste Antwortkoeffizienten in θ. Die geprüfte Definition typisiert ihr Verhältnis weder ausdrücklich als positiv reell noch liefert sie eine native komplexe Variation. Bei festem θ hängt der lineare Quotient ζ_Γ überhaupt nicht von der kleinen Schalenkoordinate ξ ab.

Aus den [beiden Entwicklungen](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6034) folgt mehr: Falls die sichtbaren Koordinaten bei festem θ Entwicklungen p = P ξ + p₂ ξ² + o(ξ²) und e = Q ξ + e₂ ξ² + o(ξ²) entlang reeller ξ besitzen, mit P ≠ 0, dann setzt sich e/p stetig nach ξ = 0 fort. Sein Wert dort ist Q/P und seine Ableitung ist (P e₂ − Q p₂)/P². Bei Im(Q/P) ≠ 0 ist das Vorzeichen auf beiden Seiten nahe null gleich. Bei reellem Q/P und nichtverschwindendem Imaginärteil der Ableitung sind die Vorzeichen auf beiden Seiten verschieden. Der dazwischenliegende Nullpunkt der fortgesetzten Diagnose kann aber bei ξ = 0 liegen, wo der ursprüngliche Quotient 0/0 ist. Das Modell e = (−1 + iξ)p mit p = ξ zeigt diese Lücke exakt.

Ein Scan von ±ξ bei festem θ liefert deshalb selbst mit einem Vorzeichenwechsel keinen regulären Antiphasenzeugen, solange der Weg durch die ausgeschlossene Nullschale geht. Für einen Nachweis muss der Quotient entlang des gesamten zulässigen Weges definiert bleiben. OP3 bleibt offen.

## Antiphasentreffer bei von null verschiedener Schalenkoordinate

Die Nullschale lässt sich in einer bedingten lokalen Konstruktion umgehen. Seien p(θ,ξ) und e(θ,ξ) gemeinsam C² und verschwinden beide bei ξ = 0. Setze P(θ) = ∂ξp(θ,0) und Q(θ) = ∂ξe(θ,0). Durch Ausklammern von ξ mittels der Integralform des Taylorrests entsteht nahe P(θ₀) ≠ 0 ein gemeinsam C¹ fortgesetzter Quotient Z mit Z(θ,0) = Q(θ)/P(θ).

Sei Z(θ₀,0) reell negativ und ∂θ Im(Q/P)(θ₀) ≠ 0. Der implizite Funktionensatz liefert dann eine lokale Kurve θ(ξ), auf der Im Z = 0. Der Realteil bleibt negativ. Für genügend kleine ξ ≠ 0 gilt p ≠ 0, sodass diese Kurve echte Treffer des sichtbaren Quotienten enthält. Die Steigung ist θ'(0) = −∂ξ Im Z / ∂θ Im Z am Ausgangspunkt. Damit lässt sich der erste Einfluss der höheren Schalenterme durch eine Verschiebung des Hintergrundparameters ausgleichen.

Die historische Entwicklung am festen Hintergrund allein liefert weder die gemeinsame Regularität noch eine transversale Nullstelle in θ. Die Kurve zählt für OP3 außerdem erst, wenn sie innerhalb der nativen zulässigen Zustände realisiert wird und der sichtbare Treffer das Phasenleck schließt. OP3 bleibt offen.

## Exakte lineare Balance auf einer ganzen Route

Die [historische Folgerung](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6190) setzt exakte Konjugation und exakte A/B-Balance voraus. Gelten beide auf einer ganzen θ-Familie, ist Q/P dort konstant −1. Diese Familie liefert daher keine transversale Nullstelle des linearen Quotienten. Exaktheit nur an einem Punkt schließt eine solche Nullstelle dagegen nicht aus.

Auf einer durchgehend balancierten Familie entscheidet stattdessen der quadratische Rest. Bei den oben beschriebenen Entwicklungen gilt gleichmäßig auf einem kompakten θ-Intervall mit von null getrenntem P, sofern die Taylorreste gleichmäßig sind,

    Im Z(θ,ξ) = ξ Im[(e₂(θ) + p₂(θ))/P(θ)] + o(|ξ|).

Für festes hinreichend kleines ξ ≠ 0 genügen zwei Endpunkte mit strikt entgegengesetzten Vorzeichen dieses normierten quadratischen Koeffizienten. Bleibt der ganze θ-Weg zulässig und der Quotient stetig, liegt dazwischen ein sichtbarer Antiphasentreffer. Hat der Koeffizient auf dem ganzen Intervall ein einheitliches, von null getrenntes Vorzeichen, ist ein solcher Treffer dort für hinreichend kleine ξ ≠ 0 ausgeschlossen.

Die historische Folgerung legt die quadratischen Koeffizienten nicht fest. Ein generischer erster Ordnungsrest reicht für die Vorzeichenprüfung nicht. OP3 bleibt offen.

## Exakte Reduktion auf die Summe der Auslesereste

Die [Ein-Schalen-Koordinatenregel](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6006) gibt nur eine gemeinsame Betragsschranke für r_δ und r_η. Auch die [quadratische Trunkierung](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6467) liefert keinen signierten Koeffizienten.

Bei A_sh = B_sh ≠ 0 und b_sh = −a_sh kürzen sich die Transportkoeffizienten aus dem sichtbaren Quotienten. Für δ_obs ≠ 0 gilt exakt

    ζ_sh + 1 = (r_δ + r_η)/δ_obs.

Die sichtbare Antiphase im Korridor ist damit äquivalent zu Im[(r_δ + r_η) conj(δ_obs)] = 0. Falls die Reste quadratische Koeffizienten d₂ und h₂ besitzen, ist der gesuchte normierte Koeffizient (d₂ + h₂)/a_sh. Eine exakte Spiegelung η_exp = −δ_obs würde alle Ordnungen aufheben. Die geprüfte historische Konjugationsregel verbindet die linearen Koeffizienten; sie erzwingt keine solche Spiegelung der vollen Auslesungen.

Die Betragsschranke ist mit r_η = −r_δ ebenso vereinbar wie mit r_δ = 0 und r_η = ±i c a_sh ξ² für hinreichend kleines c > 0. Sie entscheidet somit weder Vorzeichen noch exakte Antiphase. Der nächste Quellencheck muss eine Symmetrie oder Formel für die vollen Auslesungen finden. OP3 bleibt offen.

## Fixierte Tangente und fixierte Schale

Die [historische Definition](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6108) wendet die Involution auf die Schalentangente an. Eine hinreichende nichtlineare Ergänzung wäre eine Involution R auf den vollen Zuständen und die Ausleseregel η(X) = −δ(RX). Auf einem Weg aus Fixpunkten von R ergäbe das bei A/B-Balance und δ ≠ 0 exakt ζ_sh = −1.

Eine fixierte Tangente allein genügt selbst mit dieser Ausleseregel nicht. Als analytisches Gegenmodell setze R(x,y) = (x,−y), X(ξ) = (ξ,ξ²) und δ(x,y) = x + iy. Dann ist X'(0) = (1,0) fixiert, aber η(X(ξ)) = −ξ + iξ² und δ(X(ξ)) = ξ + iξ². Ihre Summe ist 2iξ², und für reelle ξ ≠ 0 ist Im(η/δ) = 2ξ/(1+ξ²) ≠ 0. Der Queranteil des Weges beginnt erst in zweiter Ordnung und genügt, um die sichtbare Antiphase zu verhindern.

Die geprüfte Definition liefert weder die vollständige Ausleseregel noch einen nativ erreichbaren Weg in der Fixpunktmenge. Der nächste konkrete Test ist daher, ob der Hüllentransport mit einer Zustandsinvolution vertauscht und einen geeigneten Fixpunkt als Eingang besitzt. OP3 bleibt offen.

## Vom gruppierten Transport zur sichtbaren Schale

Das [Stabilitätskriterium in Teil 09](../../sources/research/parts/v470/09_preclosure_memory.tex#L70) fordert auf dem aktiven gruppierten Zweig [M,J] = 0 und verschwindende HC-Leckage. Es liefert dort eine bedingte Fixpunkterhaltung: Aus Jx = x folgt JMx = Mx. Die historische Schaleninvolution ist als Nachfolgerin der Umkehrwalze bezeichnet. Für einen konkreten Übergang auf der sichtbaren Schale braucht es dazu eine Abbildung π vom gruppierten Zustand zur Schale mit πJ = R_shπ.

Ist π vorhanden, reicht ein gruppierter Fixpunkt für einen sichtbaren Fixpunkt, denn R_shπ(Mx) = π(JMx) = π(Mx). Soll M zusätzlich eine eigenständige Schalenabbildung induzieren, ist auf dem betrachteten Bereich die Faserbedingung nötig und hinreichend: π(x)=π(y) impliziert π(Mx)=π(My). Andernfalls können zwei gruppierte Repräsentanten desselben sichtbaren Zustands unterschiedliche sichtbare Folgezustände liefern.

Die geprüfte Passage formuliert die Bedingungen auf der gruppierten OP1/OP5-Schicht. Für OP3 bleiben die konkrete kompatible Schalenabbildung, der admissible Fixpunkteingang und die vollständige Spiegelregel zu prüfen.

## Test für eine lineare sichtbare Auslesung

Für eine lineare Schalenabbildung L und einen linearen gruppierten Transport M ist die Faserbedingung äquivalent zu M(ker L) ⊆ ker L. Denn zwei Zustände mit gleicher Auslesung unterscheiden sich genau um einen Vektor aus ker L. Für eine skalare nichtverschwindende Auslesung ℓ ist das äquivalent zu ℓM = μℓ. Eine einzelne sichtbare Koordinate ist somit genau dann autonom, wenn ihre Auslesung ein linker Eigenvektor des Transports ist.

Die in Teil 09 beschriebene J-Sektorerhaltung reicht dafür allein nicht. Ein zweidimensionaler gerader Sektor mit J = I, M = diag(1,2) und ℓ(x,y) = x+y erfüllt die Sektorerhaltung. Die Zustände (1,0) und (0,1) haben denselben sichtbaren Wert 1, danach aber die Werte 1 und 2. Der verborgene Unterschied liegt vollständig im geraden Sektor.

Für einen konkreten linearen Kandidaten kann man deshalb direkt ℓM auf ker ℓ prüfen. Bei einem Treffer lässt sich die sichtbare Dynamik durch μ angeben. Bei einem Fehlschlag braucht die sichtbare Dynamik weitere Koordinaten oder einen ausgezeichneten Lift. Teil 09 identifiziert den OP3-Schalenfunktional auf dem gruppierten Träger nicht. OP3 bleibt offen.

## Kleinste lineare Ergänzung der Schalenablesung

Auf einem endlichdimensionalen linearen Träger mit festem Transport M lässt sich aus einem gegebenen Schalenfunktional ℓ die kleinste autonome lineare Auslesung konstruieren. Bilde den Zeilenraum W = span{ℓ, ℓM, ℓM², …}. Sobald eine neue Zeile im bisherigen Spann liegt, bleibt der Raum unter Rechtsmultiplikation mit M invariant. Für r = dim W genügen daher die ersten r Zeilen.

Der ergänzte sichtbare Zustand ist (ℓx, ℓMx, …, ℓM^(r−1)x). Sein Update verschiebt die Einträge und berechnet den letzten aus der linearen Abhängigkeit der nächsten Zeile. Jede autonome lineare Auslesung, aus der sich ℓ linear zurückgewinnen lässt, muss alle diese Zeilen enthalten. Die Konstruktion gibt deshalb die minimale Zahl zusätzlicher linearer Koordinaten r−1. Äquivalent sind zwei gruppierte Zustände für diese Auslesung genau dann gleich, wenn ihre skalaren Auslesungen nach allen Iterationen übereinstimmen.

Das ist eine bedingte Konstruktion für einen festen linearen Transport. Sie identifiziert weder das historische OP3-Funktional noch zeigt sie, dass die ergänzten Koordinaten den geometrischen Monitor und die Phasenbedingungen bestimmen. Für ein konkretes M und ℓ kann man danach prüfen, ob diese weiteren Auslesungen auf den Fasern konstant sind. OP3 bleibt offen.

## Was die historischen Antwortkoeffizienten über den Transport verraten

Die historische Definition gibt ℓ_sh als Element des Dualraums der sichtbaren Schalentangente vor. Sie bestimmt im betrachteten Fixpunktfall nur seine Auswertung auf u_sh. Selbst wenn man einen Lift v von u_sh auf den gruppierten Träger und einen Transport M voraussetzt, reicht die Auswertung ℓ(v) nicht für den Eigenvektortest.

Gegenmodell: M = diag(1,2), v = (1,0), ℓ₁(x,y)=x und ℓ₂(x,y)=x+y. Beide Auslesungen ergeben auf v denselben Koeffizienten 1 und auf der gesamten Bahn von v dieselben Werte. Dennoch ist nur ℓ₁ eine linke Eigenform. Die kleinste autonome Ergänzung hat für ℓ₁ Rang eins und für ℓ₂ Rang zwei. Das trennt die Auswertung auf einer einzigen Bahn von der Prüfung auf einem größeren Zustandsraum.

Allgemein reichen die Werte auf v, Mv, … zur eindeutigen Rekonstruktion einer linearen Auslesung genau auf deren Spann. Auf dem ganzen Träger reichen sie genau dann, wenn diese Bahnvektoren ihn aufspannen. Ist nur die Autonomie auf dem tatsächlich zulässigen Träger gefragt, muss dieser Träger zuerst festgelegt werden. Die historische Schalentangente allein entscheidet die Frage nicht. OP3 bleibt offen.

## Ist die historische Schale auf eine Bahn beschränkt?

Der [historische Aufbau](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L5367) unterscheidet den gruppierten Zweig U, die Leckageebene W und die nachgelagerte Beobachterschale. Das Verschwinden der gruppierten Leckage auf W ist eine Voraussetzung für die Reduktion des sichtbaren Restes auf eine skalare Beobachtergröße. Daraus folgt keine Darstellung der Beobachterschale als Bahn eines gruppierten Startvektors. Auch die [Ein-Schalen-Koordinatenregel](../../sources/historical/01_historical_core_snapshot/05_appendices_and_computational_completeness.tex#L6006) parametrisiert Auslesungen, ohne ein Update dieser Koordinate zu definieren.

Selbst auf einer einzigen Bahn x_n = M^n v kann eine skalare Auslesung als Zustand scheitern: Eine autonome Abbildung auf den beobachteten Werten existiert genau dann, wenn jeder wiederholte Wert denselben Nachfolger hat. Beispiel M(x,y)=(y,x+y), v=(1,1), ℓ(x,y)=x. Die Bahn beginnt sichtbar mit 1,1,2. Der Wert 1 hat zwei verschiedene Nachfolger. Damit kann auch die Beschränkung auf eine Bahn fehlende Zustandsinformation nicht generell ersetzen.

Für die historische Route wäre als Nächstes eine ausdrücklich zeitlich geordnete Schalenfolge samt Folgeregel zu suchen. Ohne sie lässt sich weder der Test auf wiederholte Werte noch die native Erreichbarkeit des Micro-Locks auswerten. OP3 bleibt offen.

## OP3-Verfeinerung am Basispunkt und wiederholter Übergang

Der [OP3-Hüllensatz](../../sources/research/parts/v470/22_op_transport_arguments.tex#L491) gibt eine Familie von Abbildungen T_(r,s) auf dem Träger an. Die Zulässigkeitsdefinition prüft jede Verfeinerung am selben Basisträger c₃. Das liefert eine parametrisierte Menge zulässiger Endpunkte, aber aus dem Test am Basispunkt folgt keine Zulässigkeit einer Komposition.

Gegenmodell: Die Closure-Klasse sei {0,1} im Zustandsraum {0,1,2}, mit Basispunkt 0. Eine Abbildung T mit T(0)=1 und T(1)=2 besteht den Test am Basispunkt. Bei Wiederholung verlässt sie die Klasse. Das Gegenmodell betrifft nur die logische Reichweite des Basispunkttests.

Für ein wiederholbares Update reicht es, die Closure-Erhaltung auf allen aus c₃ tatsächlich erreichbaren Zwischenzuständen nachzuweisen. Ein stärkerer, direkt prüfbarer Nachweis wäre, dass jede verwendete Verfeinerung die ganze betrachtete Closure-Klasse in sich abbildet. Für einen einzelnen Micro-Lock-Schritt ab einem bereits reparierten Eingang genügt stattdessen ein zertifizierter Übergang genau von diesem Eingang mit den zusätzlichen Phasen- und Geometrieguards. OP3 bleibt offen.

## Relativer Übergang zwischen zwei zertifizierten Endpunkten

Sind T_a und T_b am selben Basisträger c₃ zulässig, sei x_a=T_a(c₃) und x_b=T_b(c₃). Falls T_a auf einem geeigneten Bereich invertierbar ist, bildet T_b ∘ T_a⁻¹ den Zustand x_a auf x_b ab und erhält an diesem Eingang die Closure-Klasse. Das folgt aus der Gleichheit der beiden Endpunktklassen, auch wenn die einzelnen Abbildungen die Klasse auf anderen Eingängen nicht erhalten.

Für einen nativen Reparaturschritt muss die Route aber die Umkehrung von T_a und die anschließende Komposition erlauben oder den relativen Übergang direkt realisieren. Eine mathematische Umkehrabbildung allein zertifiziert keine zulässige Rückroute. Außerdem müssen die Phasen- und Geometrieguards für den beabsichtigten Schritt gesondert gelten. Die [geprüfte Definition](../../sources/research/parts/v470/22_op_transport_arguments.tex#L502) gibt keine Invertierbarkeit oder zulässige Rückroute für T_(r,s) an. OP3 bleibt offen.

## Relativer Übergang ohne Invertierbarkeit

Auf einem festgelegten Bereich D von Basisträgern existiert eine eindeutige Abbildung H auf T_a(D) mit H(T_a(x)) = T_b(x) für alle x in D genau dann, wenn T_a(x)=T_a(y) stets T_b(x)=T_b(y) impliziert. Notwendigkeit folgt durch Anwenden von H. Für die Umkehrung definiert man H auf jedem Bildpunkt durch den gemeinsamen T_b-Wert seiner Urbilder. Damit darf T_a Information verlieren, sofern T_b genau diese Information nicht benötigt.

Auf einem einzelnen Basisträger ist diese Bedingung automatisch erfüllt und liefert lediglich eine Zuordnung der beiden Endpunkte. Für einen aus dem reparierten Zustand berechenbaren Schritt muss D die relevanten Basisträger umfassen. Sind T_a und T_b dort jeweils klassenbewahrend, erbt H die Closure-Erhaltung auf T_a(D). Native Realisierbarkeit und die übrigen Guards folgen daraus separat zu prüfen.

Der [OP3-Hüllensatz](../../sources/research/parts/v470/22_op_transport_arguments.tex#L526) behandelt Inverse-Shell-Verhalten als Diagnose. Diese Passage spezifiziert keinen inversen oder relativen Übergang. Der nächste Test für konkrete Kandidaten ist, zwei durch T_a ununterscheidbare Basisträger zu suchen und ihre T_b-Ausgänge zu vergleichen. OP3 bleibt offen.

## Wieviel Information bei einer linearen Reparatur fehlt

Die gezielte Suche nach Schalenverfeinerungen in den Forschungsnotizen führt zum Richtungsreadout-Vorbefund, der die native Klassenerhaltung von einem konstruierten Pfad trennt. Sie hat keinen auswertbaren nativen Kandidaten für das Paar aus Reparatur und Zielabbildung geliefert.

Für lineare Kandidaten A (Reparatur) und B (Ziel) auf demselben endlichdimensionalen linearen Träger lässt sich der Informationsverlust genau eingrenzen. Alle Basisträger, die denselben reparierten Zustand wie x ergeben, liegen in x + ker A. Ihre Zielwerte bilden Bx + B(ker A). Damit ist d = dim B(ker A) die Zahl zusätzlich benötigter linearer Skalare. Sie entspricht Rang der gestapelten Abbildung (A,B) minus Rang A.

Zur Notwendigkeit muss eine Zusatzablesung auf ker A mindestens Rang d haben, sonst identifiziert sie zwei Zustände mit verschiedenen Zielwerten. Zur Hinlänglichkeit wähle eine lineare Projektion vom Zielraum auf B(ker A) und speichere die Koordinaten des projizierten Zielwertes. Zusammen mit A unterscheiden diese d Skalare alle relevanten Zielwerte. Das beschreibt eine minimale Ergänzung auf dem vollen linearen Träger. Auf einer eingeschränkten nichtlinearen zulässigen Menge muss man stattdessen die tatsächlich auftretenden Fasern prüfen.

Damit kann ein konkreter Kandidat entweder einen eindeutigen relativen Schritt liefern (d=0) oder genau benennen, welche verborgenen Richtungen ihn verhindern (d>0). Die Konstruktion selbst liefert weder die nativen Abbildungen noch die Micro-Lock-Guards. OP3 bleibt offen.

## Auswertung am vorhandenen Paritäts-Vergleichsmodell

Im [Paritäts-Vergleichsmodell](op3_parity_distortion_exploration.py) wirkt die lineare Erweiterung R_b(x,y)=(-x+b y,y) auf der sichtbaren Achse stets als x ↦ −x. Setze für den Informationsverlusttest A(x,y)=x und B_b(x,y)=−x+b y als sichtbaren Zielwert. Auf ker A gilt B_b(0,y)=b y. Damit ist der Zusatzrang exakt null für b=0 und eins für b≠0. Bei b≠0 haben (x,0) und (x,1) denselben Eingangswert, aber Zielwerte mit Differenz b.

Die Einschränkung auf y=0 macht den sichtbaren Schritt für jedes b eindeutig. Sie verdeckt dabei die Ableitung quer zur Achse, die im Vergleichsmodell die Verzerrung bestimmt. Das ist ein konkretes Beispiel, in dem autonome sichtbare Dynamik auf der gewählten Bahn und geometrische Kontrolle in ihrer Umgebung getrennt nachgewiesen werden müssen. A ist hier die gewählte Auslesung und keine native OP3-Reparatur. OP3 bleibt offen.

## Was zwei sichtbare Messungen rekonstruieren

Für R_b(x,y)=(-x+b y,y) sei b bekannt. Zwei aufeinanderfolgende sichtbare Werte x₀ und x₁ liefern bei b≠0 genau y=(x₀+x₁)/b. Der Rang der beiden Messzeilen (1,0) und (−1,b) ist zwei. Bei Messfehlern von jeweils höchstens ε beträgt der Fehler der rekonstruierten Querkoordinate höchstens 2ε/|b|. Nahe b=0 wird die Rekonstruktion entsprechend empfindlich.

Ist b unbekannt, liefern die Werte nur das Produkt b y. Weil R_b² die Identität ist, wechseln alle weiteren sichtbaren Werte zwischen x₀ und x₁. Selbst eine vollständige Folge bestimmt b und y daher nicht getrennt. Beispielsweise liefern (b,y)=(1,1) und (1/2,2) bei gleichem x₀ dieselbe Folge. Sie liegen für die Verzerrungsgrenze K≤2 auf verschiedenen Seiten: Das Modellkriterium lautet b²≤1/2. Ein unabhängig bekannter Querwert y≠0 würde diese Mehrdeutigkeit auflösen. Dieser Befund gilt für das Paritäts-Vergleichsmodell und lässt OP3 offen.

## Kalibrierung durch eine bekannte Querverschiebung

Im linearen Paritätsmodell genügen zwei Messpaare, wenn zwischen ihnen eine bekannte Querverschiebung h ≠ 0 möglich ist und b gleich bleibt. Die Summen der sichtbaren Eingangswerte und Folgemessungen lauten s₀=by und s₁=b(y+h). Daher ist b=(s₁−s₀)/h unabhängig vom unbekannten y. Haben alle vier Einzelwerte Fehler von höchstens ε, liegt b im Intervall um den Schätzwert mit Radius 4ε/|h|. Für K≤2 ist die Entscheidung gesichert, sobald dieses Intervall vollständig innerhalb oder vollständig außerhalb von [−1/√2,1/√2] liegt.

Die bekannte Querverschiebung ist eine zusätzliche Eingriffsmöglichkeit im Vergleichsmodell. Für einen nativen OP3-Test wäre zu zeigen, welche zulässige Operation eine kalibrierte Querverschiebung erzeugt und dabei den untersuchten Transport unverändert lässt. OP3 bleibt offen.

## Vierteldrehung als Alternative zur kalibrierten Translation

[Teil 09](../../sources/research/parts/v470/09_preclosure_memory.tex#L494) definiert eine Vierteldrehung J_W auf der komplementären Leckageebene. Sie dreht die Ausgaberichtungen zweier gruppierter Leckageproben. Die Passage gibt keine Operation an, mit der sich der verborgene Eingang eines OP3-Folgeschritts kontrolliert drehen lässt.

Als Vergleichsrechnung erweitere die Scherung auf einen linearen Funktionalwert b·y in einer orthonormalen Querebene. Könnte man bei festem b zusätzlich y durch J_W y ersetzen, lieferten die beiden sichtbaren Summen s=b·y und t=b·J_W y exakt s²+t²=||b||²||y||². Bei unabhängig bekanntem ||y||>0 wäre damit die Scherungsnorm bestimmt, auch ohne Kenntnis der Richtung von y. Für den euklidischen Spiegelblock R(x,y)=(-x+b·y,y) liegt die einzige nichttriviale Verzerrung in der von der sichtbaren Achse und b aufgespannten Ebene. Daher gilt wie im zweidimensionalen Modell K≤2 genau für ||b||²≤1/2.

Ohne bekannte Norm bleibt die Skalierung (b,y) ↦ (c b,y/c) für c>0 unsichtbar. Auch weitere bekannte Drehungen lösen diese Mehrdeutigkeit nicht. Der Quellenbefund stellt eine Drehung auf der Ausgabeseite bereit. Ein nativer kalibrierter Eingangseingriff für OP3 bleibt offen.

## Kann die Vierteldrehung auf den Eingang zurückgezogen werden?

Für eine lineare Leckageabbildung K: V → W und die Vierteldrehung J_W auf der reellen Ebene W kann es eine lineare Eingangsoperation U mit KU = J_W K nur geben, wenn im K unter J_W invariant ist. Denn die linke Seite liegt stets in im K. Umgekehrt genügt diese Invarianz für eine lineare Lösung: Auf einem Komplement von ker K zieht man J_W über die Einschränkung von K zurück. Auf ker K kann U etwa als Identität gewählt werden.

Auf einer reellen Vierteldrehungsebene ist keine Gerade invariant. Für eine nichtverschwindende Leckage ist daher Rang zwei nötig. In [Teil 09](../../sources/research/parts/v470/09_preclosure_memory.tex#L473) hat die Ausgabe der einzelnen Parallelprobe nur eine Richtung. Ihre Vierteldrehung erzeugt die Partnerprobe durch Änderung der Abbildung. Sie kann nicht als Eingangsoperation derselben Probe dargestellt werden. Erst eine feste Abbildung mit beiden unabhängigen Ausgaberichtungen würde den algebraischen Rangtest bestehen. Die Zulässigkeit des zurückgezogenen Eingriffs für OP3 wäre dann separat zu prüfen.

Für die historische **gepaarte** Parallelprobe ist dagegen der projizierte Vorwärtsblock K=(I−C)K_parallel auf span(u₁,u₂) vom Rang zwei. Er bildet die beiden Eingangsrichtungen auf w₁ und w₂ ab, bis auf die gemeinsame Vorzeichenkonvention des Austauschoperators. Der Rückzug U=K⁻¹J_W K ist hier die entsprechende Vierteldrehung der admissiblen Eingangsebene. Die Rang-eins-Sperre betrifft nur eine einzelne elementare Austauschrichtung. Die Identität gilt für den projizierten Vorwärtsblock; sie macht keine Aussage über die Rückwärtskomponente des vollen Austauschoperators oder über die native Realisierbarkeit als OP3-Eingriff.

## Vierteldrehung auf beiden Sektoren des Austauschoperators

In den historischen Basen der gepaarten Parallelprobe ist der volle Austausch K(u,w)=(w,u). Schreibe J₂ für die Vierteldrehung in den jeweiligen Koordinaten. Die einseitige Drehung D(u,w)=(J₂u,w) vertauscht nicht mit K: KD(u,w)=(w,J₂u), während DK(u,w)=(J₂w,u). Die gekoppelte Drehung S(u,w)=(J₂u,J₂w) vertauscht dagegen exakt mit K. Unter blockdiagonalen Eingriffen mit vorgegebener Eingangsdrehung J₂ ist die gleiche Drehung im zweiten Sektor durch die Vertauschungsforderung eindeutig erzwungen.

S ist orthogonal und erhält die geraden und ungeraden Sektoren. Für ein reines Eingangssignal (u,0) stimmt ihre Wirkung zunächst mit der einseitigen Drehung überein. Auf gemischten Zuständen ist die gekoppelte Drehung die Symmetrie des vollen Austauschoperators. Ob sie auch den tatsächlichen Millennium-Transport, die Closure-Klasse und den OP3-Monitor erhält, folgt aus dieser Rechnung am historischen Probeoperator nicht.

## Blocktest am gruppierten Millennium-Transport

Auf der gepaarten Vier-Ebene sei M sektortreu und lasse die Ebene invariant. Dann hat M die Blöcke P und Q auf der geraden und der ungeraden Ebene. Für S=diag(J₂,J₂) gilt [M,S]=0 genau dann, wenn beide Blöcke die Form aI+bJ₂ haben. Für einen reellen 2×2-Block sind dafür gleiche Diagonaleinträge und entgegengesetzte Nebendiagonaleinträge nötig und hinreichend.

Das [historische Kommutatorkriterium](../../sources/research/parts/v470/09_preclosure_memory.tex#L70) für die Umkehrwalze J prüft lediglich die Sektortreue. Das Gegenmodell M=diag(1,2,1,2) vertauscht mit J=diag(I₂,−I₂) und hat keine HC-Leckage. Es vertauscht sogar mit dem gepaarten Austausch, aber nicht mit S. Auf der ersten Basisrichtung der geraden Ebene unterscheiden sich MS und SM um eine Einheit in der zweiten Basisrichtung. Damit reichen Umkehrwalzenverträglichkeit und die Symmetrie des Probeoperators zusammen nicht aus.

Für die tatsächliche Route braucht es die eingeschränkten Transportblöcke oder einen unabhängigen Rotationsinvarianznachweis. Invarianz der Vier-Ebene, Closure und Geometriemonitor bleiben gesondert zu prüfen. OP3 bleibt offen.

## Kann eine einzelne Messrichtung die Drehsymmetrie ersetzen?

Für einen reellen 2×2-Transportblock P und J₂=[[0,−1],[1,0]] hat der Kommutator PJ₂−J₂P die Form [[s,t],[t,−s]], wobei s=P₁₂+P₂₁ und t=P₂₂−P₁₁. Sein Quadrat ist (s²+t²)I. Damit ist der Fehler ||PJ₂u−J₂Pu|| auf jedem Einheitsvektor gleich √(s²+t²). Ein einziger nichtnulliger Eingangsvektor, auf dem beide vollständigen Vektorausgaben gleich sind, zertifiziert daher die Symmetrie des ganzen Blocks. Bei gebrochener Symmetrie gibt es keine einzelne fehlerfreie Richtung im vollständigen Block.

Eine skalare Messung kann den Fehler dagegen verbergen. Für P=diag(1,2) und u=(1,0) liegt der Fehler in der zweiten Koordinate; die erste Koordinate meldet null. Zwei unabhängige skalare Auslesungen oder eine vollständige Vektorausgabe reichen für den Test auf einem bekannten Nichtnullvektor. Der Befund setzt die Invarianz der betrachteten Ebene voraus und zertifiziert keinen nativen OP3-Übergang. OP3 bleibt offen.

## Vierteldrehungstest mit einer skalaren Auslesung

Setze D=PJ₂−J₂P. Aus J₂²=−I folgt DJ₂=−J₂D. Sei ℓ eine bekannte, nichtverschwindende reelle lineare Auslesung auf der invarianten euklidischen Ebene und u ein Nichtnullvektor. Die beiden skalaren Kommutatorwerte c₀=ℓDu und c₁=ℓDJ₂u=−ℓJ₂Du messen Du in zwei orthogonalen Richtungen. Damit gilt exakt

    ||D|| = sqrt(c₀²+c₁²)/(||ℓ|| ||u||).

Bei Fehlergrenzen ε je Kommutatorwert liegt der wahre Normwert höchstens sqrt(2) ε/(||ℓ|| ||u||) vom Schätzwert entfernt. Der Test setzt voraus, dass beide Reihenfolgen von Drehung und Transport sowie beide Eingänge tatsächlich verfügbar sind. Er identifiziert den Symmetriefehler eines festen Blocks. Er konstruiert weder die native Drehoperation noch die für OP3 nötigen Übergänge.

## Reine Eingangsdrehung und Identifikation des Transportblocks

Messungen mit derselben skalaren Auslesung ℓ an u und J₂u bestimmen bei einem festen linearen Block P genau die Zeile ℓP, da diese Eingänge eine Basis bilden. Beliebig viele weitere Eingangsdrehungen fügen dazu keine Information hinzu. Für ℓ=(1,0) liefern P=I und P=diag(1,2) dieselbe skalare Ausgabe für jeden Eingang. Nur der erste Block vertauscht mit J₂. Deshalb muss für den Vierteldrehungstest die zweite Ausgaberichtung entweder gemessen oder aus einer unabhängigen Transportidentität bestimmt werden.

Die [Leseregel der Runden r75/r76](v4_10_0_r76/README.md) identifiziert den historischen Namen Millennium-Matrix mit der Kompensatormatrix M₁₆. Das legt die Bezeichnung des gesuchten Operators fest. Für den Test fehlen weiterhin die Einbettung der historischen Paarbasis und ihre Ausgabekoordinaten unter M₁₆. OP3 bleibt offen.

## Abgleich mit der konkreten Dublett-Restriktion

[Runde r05](v4_9_0_r01_r16/rounds/v490_r05_round.tex#L35) gibt den Portblock M=λ₊C+λ₋(I−C) an. Auf dem reellen Portdublett hat jeder J-Sektor Dimension eins. Das historische Paar (u₁,u₂) beziehungsweise (w₁,w₂) kann daher nicht allein in diesem Dublett liegen. Eine Vierteldrehung in der Portebene vertauscht mit dem diagonalen Portblock genau für λ₊=λ₋ und verbindet dabei die beiden J-Sektoren.

Eine andere, bedingte Einbettung nutzt eine gemeinsame zweidimensionale räumliche Ebene V in beiden Ports. Falls der Transport dort als diag(λ₊I_V,λ₋I_V) wirkt, vertauscht er für beliebige Portgewichte mit der gekoppelten räumlichen Vierteldrehung. Das benennt die zusätzlich benötigte Struktur. Runde r05 realisiert den Kompensatoranteil auf dem Dublett; sie identifiziert diese räumliche Paarbasis nicht mit der historischen OP3-Probe im vollständigen M₁₆. OP3 bleibt offen.

## Räumliche Achsensymmetrie als hinreichender Nachweis

Im räumlich erweiterten Vergleichsträger bestehe jeder Port aus R³. Sei n eine gemeinsame Einheitsachse und S die Vierteldrehung um n, die in beiden Ports gleich wirkt. Falls der Transport sowohl die Portaufteilung erhält als auch mit S vertauscht, erhält er in jedem Port automatisch die Achse und ihre senkrechte Ebene. Die Achse ist ker(S−I), die Ebene ker(S²+I). Beide Kerne bleiben unter jedem mit S vertauschenden Transport invariant.

Auf jeder Querfläche hat der Block dann die Form aI+bJ₂. Die für den bisherigen Test benötigte gekoppelte Vierteldrehung wäre also durch eine einzige gemeinsame räumliche Symmetrie gesichert. Falls der Block zusätzlich selbstadjungiert ist, verschwindet b, und die Querfläche wird isotrop gewichtet.

Die räumlichen Rotationen in [r05](v4_9_0_r01_r16/rounds/v490_r05_round.tex#L35) sind mit der Portaufteilung verträglich. Daraus allein folgt nicht, dass der konkrete OP3-Transport mit einer bestimmten räumlichen Vierteldrehung vertauscht. Die verbleibende Quellenfrage lautet, ob der relevante Zustand und die Transportregel eine gemeinsame feste Achse haben und unter der Vierteldrehung invariant sind. OP3 bleibt offen.

## Gemeinsame Drehachse am konkreten Feldzustand

Im räumlichen Vergleichsträger seien E und B reelle Vektoren desselben Frames. Eine räumliche Vierteldrehung fixiert genau ihre Achse. Sie fixiert den geordneten Zustand (E,B) daher genau dann, wenn beide Vektoren auf dieser Achse liegen. Für E×B≠0 gibt es keine solche gemeinsame Achse. Der Wechsel zu den beiden linearen Portkombinationen ändert das nicht, da der Portwechsel invertierbar ist und deshalb denselben räumlichen Spann erhält.

Sei F eine differenzierbare rotationsäquivariante Zustandsregel, also F(SX)=SF(X). Ableiten ergibt DF(SX)S=S DF(X). Erst wenn SX=X gilt, folgt daraus die Vierteldrehungssymmetrie des lokalen Transportblocks DF(X). Bei nichtkollinearem E und B verknüpft dieselbe Gleichung zwei verschiedene Hintergrundzustände. Eine zufällige Symmetrie des Blocks am einzelnen Hintergrund bleibt möglich und braucht einen eigenen Nachweis.

Das liefert einen vorgeschalteten Test für den bisherigen OP3-Kandidaten: Kollinearität im gewählten Frame und die Fixierung aller weiteren Hintergrunddaten prüfen. Die Rechnung betrifft eine äquivariante Vergleichsroute. Sie identifiziert DF nicht mit M₁₆ und setzt keinen Framewechsel voraus. OP3 bleibt offen.

## Messbarkeit am rotationsfixierten Hintergrund

Fixiert die Vierteldrehung S den Hintergrund X und ist eine skalare Auslesung f unter S invariant, dann gilt Df(X)S=Df(X). Auf der Querebene gilt S²=−I, also verschwindet Df(X) dort. Eine reine Querverschiebung verändert diese Auslesung am fixierten Hintergrund erst ab zweiter Ordnung, sofern f zweimal differenzierbar ist. Bei einer S-äquivarianten Zustandsregel F ist auch f∘F invariant. Für zwei durch S verbundene Eingänge stimmen die skalaren Folgemessungen dann exakt überein.

Damit kann derselbe Symmetrieansatz, der die Vierteldrehung des Transports sichert, die dafür geplante Messung unempfindlich machen. Die Kalibrierung braucht eine richtungsempfindliche Auslesung oder eine mitgeführte Referenz, deren Transformation separat festgelegt ist. Das gilt bedingt für den rotationsfixierten Vergleichshintergrund. Ob der native OP3-Monitor diese Invarianz besitzt, wurde hier nicht nachgewiesen. OP3 bleibt offen.

## Richtungsinformation aus zwei Querabweichungen

Am rotationsfixierten Hintergrund verschwindet die lineare Antwort einer invarianten skalaren Auslesung auf Querabweichungen. Sind zwei Quervektoren u und w verfügbar und wirkt dieselbe Vierteldrehung auf beide, darf ihr quadratischer Taylorterm dennoch relative Richtungsinformation enthalten. Die reinen Quadratterme sind Vielfache von ||u||² und ||w||². Der gemischte Block vertauscht mit J₂ und hat deshalb die Form aI+bJ₂. Der gemischte Term lautet somit a u·w + b u·J₂w, bei entsprechender Wahl der Koeffizienten.

Gemeinsames Drehen von u und w lässt beide Terme invariant. Dreht man nur w, werden die beiden gemischten Auslesungen (u·w, u·J₂w) zu (u·J₂w, −u·w). Gemischte Differenzen aus den vier Eingaben (0,0), (u,0), (0,w) und (u,w) isolieren den Kopplungsterm in zweiter Ordnung. Zusätzliche Spiegelinvarianz würde den orientierten Term b ausschließen.

Damit kann ein zweiter Port als Richtungsreferenz dienen, sofern er unabhängig präparierbar ist und ein gemischter Term vorhanden ist. Die Rechnung ist ein bedingter lokaler Test für eine glatte Auslesung. Für den nativen OP3-Monitor sind weder dieser gemischte Block noch eine zulässige einseitige Variation nachgewiesen.

## Konkreter Test an der Feldinvariante

Der [Richtungsreadout-Vorbefund](qam_r27_richtungsreadout_2026_11_07.md#quellenabgleich-zur-nativen-phasenbindung) verwendet die Feldinvariante s=A·D+i(||A||²−||D||²)/2 für die Ports A=E+B und D=E−B im selben Frame. Der gemischte Term ist das Skalarprodukt. Für festes A und eine Drehung D(φ) in einer Querfläche ist der Imaginärteil konstant, während der Realteil sinusförmig variiert. Zwei um eine Vierteldrehung versetzte Werte des Realteils geben die beiden relativen Richtungskomponenten.

Damit gilt für diese Invariante: Bei ungleichen Portnormen kann eine reine Portdrehung s nie auf die negative reelle Achse bringen. Bei gleichen Portnormen ist s für alle Winkel reell. Negative Werte sind bei nichtverschwindendem Skalarproduktamplitudenanteil erreichbar, aber ein transversaler Durchgang durch die negative reelle Achse ist ausgeschlossen. Die reine Winkelvariation liefert also relative Richtungsinformation und genügt zugleich nicht für den zuvor gesuchten transversalen Antiphasentreffer. Dafür wäre eine unabhängig zulässige Änderung der Normdifferenz bei negativem Realteil zu prüfen.

Diese Aussage gilt für s. Die Identifikation mit dem sichtbaren Schalenquotienten oder dem Micro-Lock-Residuum bleibt offen.

## Reziproke Portgewichtung erzeugt einen transversalen Treffer

Die [r05-Portrestriktion](v4_9_0_r01_r16/rounds/v490_r05_round.tex#L35) liefert die Familie mit Gewichten e^t und e^(−t). Auf die reellen Ports A,D im selben Frame angewandt ergibt sie

    s(t) = A·D + i(e^(2t)||A||² − e^(−2t)||D||²)/2.

Für A·D<0 sind beide Ports von null verschieden. Der Realteil bleibt negativ und der Imaginärteil verschwindet eindeutig bei t* = (1/2) log(||D||/||A||). Seine Ableitung dort ist 2||A||||D||>0. Der Treffer ist transversal und läuft nicht durch s=0. Beispiel A=(1,0,0), D=(−2,0,0): t*=(log 2)/2 und s(t*)=−2. Bei einem vorgeschriebenen Parameterintervall ist zusätzlich t* ∈ I zu prüfen.

Damit liefert die r05-Familie für negative Anfangswerte von A·D den zuvor fehlenden Vorzeichenwechsel auf der Ebene der Feldinvariante. Die freie Wahl von t für einen nativen OP3-Übergang, die Closure- und Geometrieguards sowie die Brücke von s zum sichtbaren Quotienten und zum Phasenleck bleiben nachzuweisen.

## Exakter Verzerrungspreis der Portbalance

Unter (A,D) ↦ (e^t A,e^(−t)D) bleiben Skalarprodukt und Kreuzprodukt der beiden Ports erhalten. Da E×B = −(A×D)/2, bleibt auch der Feldfluss im gewählten Frame unverändert. Der Treffer macht E·B = 0, kann aber einen vorhandenen Fluss nicht entfernen. Die Feldnormsumme ||E||²+||B||² = (e^(2t)||A||²+e^(−2t)||D||²)/2 erreicht am selben t* ihr eindeutiges Minimum ||A||||D||.

In der euklidischen Portmetrik hat die Gewichtung die Singularwerte e^t und e^(−t). Ihre Verzerrung, als Verhältnis größter zu kleinster Singularzahl, beträgt am Treffer exakt max(||A||/||D||,||D||/||A||). Für eine gewählte Vergleichsgrenze K_max ≥ 1 ist der Treffer daher genau dann innerhalb dieses Budgets, wenn das anfängliche Portnormverhältnis in [1/K_max,K_max] liegt. Beispiel: A=(1,0,0), D=(−2,0,0) trifft K_max=2 genau am Rand.

Diese Verzerrung gehört zur euklidischen Portgewichtung und ist nicht mit dem historischen T_N identifiziert. Die Erhaltung von Realteil und Fluss beweist ebenfalls keine Erhaltung der nativen Closure-Klasse. OP3 bleibt offen.

## Teilung in kleine Schritte und untere Verzerrungsgrenze

Die Portgewichtungen M(t)=diag(e^t I,e^(−t)I) erfüllen M(t₂)M(t₁)=M(t₁+t₂). Für n gleich große Schritte zum Treffer t* ist die Verzerrung je Schritt exp(2|t*|/n), während die Gesamtverzerrung unverändert exp(2|t*|) beträgt. Bei einer reinen Schrittgrenze κ>1 genügen für t*≠0 genau ceil(2|t*|/log κ) Schritte. Die Untergrenze folgt aus der Dreiecksungleichung für die Summe der Schrittparameter und wird durch gleich große Schritte erreicht. Für κ=1 ist nur t*=0 erreichbar. Eine Schranke auf die Verzerrung relativ zum Anfangszustand bleibt durch Unterteilung unverändert.

Der Gesamtpreis ist sogar optimal unter allen invertierbaren linearen Abbildungen, die die beiden anfänglichen Portvektoren im direkten Summenraum auf gleiche Norm bringen. Sind ihre Ausgangsnormen a und d, muss das Verhältnis der Streckungen auf ihren normierten Richtungen d/a sein. Jede Streckung liegt zwischen kleinster und größter Singularzahl. Daher ist K ≥ max(a/d,d/a), und die reziproke Gewichtung erreicht diese Schranke.

Für OP3 sind Schrittgrenze und absolute geometrische Schranke getrennt zu prüfen. Diese Rechnung verwendet die euklidische Portmetrik und liefert keine Identifikation mit T_N oder eine native Zulässigkeit der Teilschritte.

## Was Unterteilung im historischen Zweischritt-Test ändern kann

Der [Zweischritt-Test](../../sources/research/parts/v470/19_local_op_entry.tex#L1825) enthält zwei verschiedene geometrische Bedingungen: eine Obergrenze e für T_N an jedem Zustand und eine Grenze v für die Differenz zwischen benachbarten Zuständen. Unterteilung kann nur die zweite Bedingung entschärfen. Ein Endzustand mit T_N>e bleibt ausgeschlossen. Soll der ursprüngliche Anfang mit dem Endzustand weiterhin unmittelbar das zu prüfende Fenster bilden, bleibt auch dessen Differenz unverändert.

Bedingter Vergleich: Auf einer stetigen Route mit monotonem Monitor g und g≤e kann man bei festem v>0 Zwischenzustände in gleich großen Monitorabständen wählen. Für einen nichttrivialen Monitorunterschied Δ genügen genau ceil(Δ/v) Schritte, sofern jede solche Teilstrecke als Übergang zulässig ist. Die Untergrenze folgt aus der Dreiecksungleichung, die Erreichbarkeit aus Stetigkeit und Monotonie. Für den gewählten Port-Vergleichsmonitor g(t)=log K(M(t))=2|t| entlang der Route ab t=0 ist Δ=2|t*|. Das ist ein Vergleichsmonitor, keine Formel für T_N. Auch Closure, Theta und Paketzulässigkeit sind an den Zwischenzuständen separat zu prüfen. OP3 bleibt offen.

## Welchen ebenen Chart die Portgewichtung braucht

[Teil 19](../../sources/research/parts/v470/19_local_op_entry.tex#L843) führt T_N als lokales Monte-Carlo-Surrogat auf dem Maschinenzustand ein. Die geprüfte Definition des Persistenzstroms nennt keine Abbildung vom Portzustand zum gesampelten ebenen Chart.

Bedingter Chart-Test: Identifiziert ein euklidischer Chart seine reelle und imaginäre Achse mit je einer orthonormalen Richtung aus verschiedenen Ports, dann wirkt die Portgewichtung dort als z ↦ cosh(t)z+sinh(t)conj(z). Der Beltrami-Koeffizient ist μ=tanh(t) und die ebene Dilatation ist (1+|μ|)/(1−|μ|)=exp(2|t|). Liegen dagegen beide Chartachsen im selben Port, wirkt dieselbe Gewichtung als gleichförmige Skalierung und liefert μ=0. Damit ist selbst die lokale Dilatation ohne Festlegung des Charts nicht aus den Portgewichten allein bestimmbar. Für einen Monte-Carlo-Wert braucht es zusätzlich die Stichproben- und Aggregationsregel. OP3 bleibt offen.

## Stichprobenabhängigkeit im Zwei-Chart-Vergleich

Die gezielte Suche nach einer Monte-Carlo-Beltrami-Regel hat für den historischen OP3-Monitor keine auswertbare Chart- und Aggregationsvorschrift ergeben. Im expliziten Vergleich mit Ein-Port-Charts (Dilatation 1) und gemischten Charts (Dilatation K) lässt sich die Auswirkung dieser Lücke quantifizieren.

Sind m von N Stichproben gemischt, ist die mittlere Dilatation 1+(m/N)(K−1). Das Stichprobenmaximum ist dagegen schon für m≥1 gleich K. Bei unabhängiger Ziehung und Wahrscheinlichkeit p für einen gemischten Chart übersieht das Maximum die volle Verzerrung mit Wahrscheinlichkeit (1−p)^N, sofern K>1. Für bekannte 0<p<1 und gewünschte Fehlwahrscheinlichkeit α genügt N≥ceil(log α/log(1−p)). Ohne positive Untergrenze für p kann keine feste Stichprobengröße diese Garantie gleichmäßig liefern. Der Vergleich setzt nur diese zwei Charttypen voraus und identifiziert keine der Aggregationen mit T_N. OP3 bleibt offen.

## 11. November: Welche Invariante die Portbalance verändert

Fokussierte algebraische Selbstprüfung der Portroute, nicht blind. Geprüfter Anspruch: Für beliebige reelle Ports A,D desselben Frames mit c=A·D<0 erreicht die reziproke Gewichtung eine negative reelle Feldinvariante. Quelle der Route ist r05; die Verbindung zur nativen Closure-Klasse wurde bisher ausdrücklich offengelassen.

Setze a=||A||, d=||D|| und h(t)=(e^(2t)a²−e^(−2t)d²)/2. Dann s(t)=c+i h(t), also |s(t)|²=c²+h(t)². Am eindeutigen Treffer gilt h(t*)=0 und |s(t*)|=|c|. Falls die anfänglichen Portnormen verschieden sind, ist |s(t*)| strikt kleiner als |s(0)|. Zugleich bleibt der Feldfluss erhalten und die Feldnormsumme sinkt auf ad. Die Route verändert daher mehr als die Phase von s.

Ein konkreter bedingter Ausschluss folgt: Verlangt die betrachtete native Route Erhaltung von |s|, ist dieser Portbalance-Treffer bei ungleichen Anfangsnormen unzulässig. Für eine Route mit erhaltener komplexer Invariante s gilt das erst recht. Bei gleichen Anfangsnormen ist t*=0 und die negative reelle Achse bereits erreicht. Daraus folgt kein allgemeiner Ausschluss von OP3-Reparaturen, da noch nicht nachgewiesen ist, welche Invarianten K_ncl für diesen Zustand festhält.

Diese Frage liegt vor weiteren Sampling-Optimierungen: Welche Äquivalenz der Träger wird benötigt, und erhält sie |s|? Der [Rückwärtsbefund zur Grundidee](qsc_back_to_basic_idea_2026_11_06.md#5-davor-dasselbe-objekt-wurde-mit-verschiedenen-äquivalenzen-verbunden) trennt gemeinsamen Träger, gleichen physikalischen Zustand, aktive Operation und reduzierte Auslesung. Die Portroute liefert einen algebraischen aktiven Übergang; ihre native Zulassung muss anhand dieser Unterscheidung geprüft werden.

## 11. November: Die Closure-Klasse legt |s| an der geprüften Stelle nicht fest

Die [Definition in Teil 22](../../sources/research/parts/v470/22_op_transport_arguments.tex#L41) führt K_ncl als Quotient nach HC-kompensiertem Transport, zulässigem Framewechsel und zulässiger Verfeinerung desselben Closure-Modus ein. Die anschließenden Annahmen fordern Klassenerhaltung und eine durch die Klasse faktorisierende sichtbare Invariante I. Sie identifizieren diese Invariante weder mit s noch mit |s|. Die Gleichung der Klassen ist daher an dieser Stelle kein auswertbarer Feldtest für die Portbalance.

Zwei einfache Quotienten auf dem betrachteten Feldbereich zeigen die verbleibende Unbestimmtheit. Eine Klasse nach gleichem Re s würde die reziproke Portgewichtung erhalten. Eine Klasse nach dem Paar (Re s, |s|) würde sie bei ungleichen Portnormen verwerfen. Beide erlauben die Faktorisierung einer sichtbaren Auslesung Re s über die Klasse. Dies sind Gegenmodelle zur Ableitbarkeit aus dieser Faktorisierung, keine vorgeschlagenen Definitionen der nativen Klasse. Die sonstigen Closure-Annahmen würden außerdem eine jeweils dazu kompatible Route verlangen.

Ein positiver Anschluss wäre eine unabhängige Festlegung der zulässigen erzeugenden Operationen der Äquivalenzrelation oder ein vollständiger Feldinvariantensatz. Erst daraus kann man entscheiden, ob die Portgewichtung die Klasse erhält. Die r05-Portverträglichkeit allein liefert diesen Nachweis nicht. Der vorige Ausschluss unter Erhaltung von |s| bleibt bedingt; eine solche Erhaltung konnte aus der geprüften Definition nicht abgeleitet werden. OP3 bleibt offen.

## 11. November: Die Relation wird im Quelltext als Eingabe verlangt

Die Suche nach dem exakten Symbol der nativen Äquivalenzrelation in den modularen Forschungsquellen findet den Quotienten und seine Invariantenfaktorisierung in Teil 22. Der historische kodierte Spiegel in Teil 07 beschreibt die Bedeutung der Relation und verlangt die Äquivalenzaxiome, gibt dort aber keine konkrete Feldoperation als Generator an.

Die spätere [Aktivierungsgrenze](../../sources/research/parts/koide-and-kernel.tex#L263) verlangt ausdrücklich ein vorgegebenes Fragment, eine Closure-Äquivalenz und kompatible Auslesungen und Routen. Sie hält die native globale Identifikation offen. Der Abgleich betrifft Manuskriptdefinitionen; gespeicherte MMA-Zertifikate wurden in diesem Schritt nicht überprüft.

Für die Portbalance ergibt sich somit ein klar abgegrenzter Arbeitsauftrag: Auf einem unabhängig festgelegten Feldfragment muss die Äquivalenz vor Zulassung des Kandidaten bestimmt sein. Definiert man sie erst als von der Portbalance erzeugte Relation, wird deren Klassenerhaltung tautologisch und liefert keine unabhängige Prüfung des OP3-Anspruchs. Ein möglicher Test braucht daher zuerst eine unabhängig begründete Closure-Auslesung und muss anschließend deren Wert vor und nach dem Portschritt vergleichen. Die vorliegenden Antiphasenformeln bleiben bedingte Kandidaten. OP3 bleibt offen.

## 11. November: Zwei vorhandene Operationsklassen im direkten Vergleich

Die [Feldlesart](qsc_back_to_basic_idea_2026_11_06.md#5-davor-dasselbe-objekt-wurde-mit-verschiedenen-äquivalenzen-verbunden) gibt unabhängige Erhaltungsaussagen: Gewöhnliche Lorentz-Transformationen erhalten s, Dualitätsdrehungen z ↦ e^(iα)z erhalten |s| und bilden s auf e^(2iα)s ab.

Für s≠0 erreicht eine Dualitätsdrehung die negative reelle Achse bei α=(π−arg s)/2 modulo π. Das ist ein exakt lösbarer, betragerhaltender Antiphasenkandidat. Eine Lorentz-Transformation allein erreicht dieses Ziel nur, wenn s bereits negativ reell ist. Eine reine Dualitätsdrehung ist unter der r05-Bedingung T4 dagegen nur bei α=0 modulo π zugelassen; diese Fälle lassen s selbst unverändert. Damit schließt T4 jeden nichttrivialen Phasenreparaturschritt durch reine Dualität aus.

Die Portbalance besteht T4 auf dem Dublett, verändert bei ungleichen Portnormen aber |s|. Dualität erhält |s|, verletzt bei nichttrivialer Phasenänderung aber T4. Würde ein nativer Kandidat beides verlangen, wären diese beiden Ein-Parameter-Routen als Reparatur gescheitert. Ob diese beiden Forderungen gemeinsam zum nativen OP3-Problem gehören, bleibt gesondert zu belegen. Zusammengesetzte oder allgemeinere aktive Übergänge sind durch diesen Vergleich nicht untersucht. OP3 bleibt offen.

## 11. November: Vollständiger Test für reelle skalare T4-Portblöcke

Betrachtet werden die reellen T4-Blöcke aus r05, die auf die Ports als A' = λ₊A und D' = λ₋D wirken. Gefordert sei zusätzlich |s'|=|s| für **alle** reellen Eingangsfelder. Mit a=||A||, d=||D||, c=A·D gilt

    |s'|² = λ₊²λ₋²c² + (λ₊²a²−λ₋²d²)²/4.

Setzt man D=0, folgt λ₊⁴=1; aus A=0 folgt λ₋⁴=1. Für reelle Gewichte bleiben damit nur λ₊,λ₋ ∈ {−1,1}. Alle vier Vorzeichenkombinationen erhalten tatsächlich |s|. Bei gleichem Vorzeichen gilt s'=s, bei entgegengesetztem s'=−conj(s). Insbesondere bleibt Im s in allen vier Fällen unverändert.

Folge: Kein reeller skalarer T4-Portblock, der |s| auf dem ganzen Feldträger erhält, kann einen Zustand mit Im s≠0 auf die negative reelle Achse bringen. In der stetigen Komponente der Identität bleiben nur die unveränderten Portgewichte; eine gemeinsame räumliche Rotation verändert s ebenfalls nicht. Die Aussage klassifiziert diese ganze Blockfamilie und ersetzt für sie weitere Parameterscans.

Die globale Erhaltungsforderung ist stärker als Erhaltung am einzelnen Eingang. Auch unabhängige räumliche Portabbildungen, zustandsabhängige oder nichtlineare Operationen sind hier nicht klassifiziert. Zudem bleibt zu belegen, ob OP3 überhaupt globale |s|-Erhaltung und T4 gemeinsam verlangt. OP3 bleibt offen.

## 11. November: Erweiterung auf unabhängige räumliche Portblöcke

Seien A'=PA und D'=QD mit reellen 3×3-Matrizen P,Q. Dies ist die allgemeine reelle blockdiagonale Form bezüglich der beiden J-Ports. Gefordert sei |s'|=|s| für alle reellen A,D im selben Frame.

Aus D=0 folgt ||PA||=||A|| für alle A, also PᵀP=I. Analog ist Q orthogonal. Der Normdifferenzterm von Im s bleibt damit unverändert. Die verbleibende Erhaltungsbedingung ist (AᵀPᵀQD)²=(AᵀD)² für alle A,D. Setzt man H=PᵀQ, so erzwingt sie für jedes feste D, dass HD=±D. Eine lineare Abbildung mit dieser Eigenschaft auf allen Vektoren ist H=I oder H=−I: Verschiedene Vorzeichen auf zwei unabhängigen Vektoren widersprächen der Eigenschaft an ihrer Summe. Somit Q=±P.

Das sind genau die möglichen Blöcke: gemeinsame orthogonale räumliche Abbildung beider Ports, optional mit zusätzlichem Vorzeichen eines Ports. Wieder gilt s'=s oder s'=−conj(s), und Im s bleibt unverändert. Die vorherige Sperre für eine nichtreelle Feldphase erfasst damit alle reellen linearen T4-Abbildungen auf diesem direkten Portträger mit globaler |s|-Erhaltung. Ihre stetige Identitätskomponente besteht aus gemeinsamen eigentlichen räumlichen Rotationen.

Nichtlineare und eingangsspezifisch erhaltende Regeln sowie die Identifikation dieses Trägers mit dem vollständigen nativen M₁₆ bleiben offen. Die Klassifikation setzt keine native Closure-Relation fest.

## 11. November: Eingangsspezifische reelle skalare Portgewichte

Die globale Erhaltungsforderung lässt sich für die skalare Portfamilie abschwächen. Sei ein einzelnes Eingangspaar A,D gegeben mit s=c+ih und h≠0. Erlaubt seien beliebige reelle Gewichte α,β, auch zustandsabhängig gewählt. Dann ist

    s' = αβ c + i(α²||A||²−β²||D||²)/2.

Für einen negativen reellen Zielwert sind αβc<0 und α²||A||²=β²||D||² nötig. Insbesondere müssen beide Ports nichtnull sein. Setze die gemeinsame quadratische Zielnorm gleich k>0. Dann |αβ|=k/(||A||||D||). Die zusätzliche Forderung |s'|=|s| ergibt k=|s| ||A||||D||/|c|, sofern c≠0. Damit existieren für c≠0 eingangsspezifische, betragerhaltende Antiphasengewichte. Die Vorzeichen können αβc negativ machen.

Für c<0 lassen sich beide Gewichte positiv wählen. Sie sind eine reziproke Balance bis zum Phasentreffer, gefolgt von gemeinsamer Skalierung mit Faktor sqrt(|s|/|c|). Diese Skalierung gleicht den Betrag aus. Für c=0 bleibt der Realteil unter jeder skalaren Gewichtung null; ein negativer reeller Zielwert ist unmöglich.

Die Operation widerlegt keinen globalen Ausschluss: Ihre Matrix hängt vom Eingang ab und erhält |s| dort. Wird sie als nichtlineare Zustandsregel verstanden, folgt aus dem portdiagonalen Ansatz allein keine vollständige T4- oder J-Äquivarianz der Regel. Native Closure, Regularität und geometrische Zulässigkeit bleiben zu prüfen. OP3 bleibt offen.

## 11. November: Umkehrwalze und einheitliches Antiphasenziel

Auf dem r05-Dublett vertauscht J die reellen Felder E und B. Daher gilt in den Ports J(A,D)=(A,−D) und für die Feldinvariante s(JX)=−conj(s(X)). Die negative reelle Achse wird auf die positive reelle Achse abgebildet.

Betrachte eine J-invariante Menge nichtnullartiger Eingänge und eine zustandsabhängige Regel F mit F(JX)=JF(X). Würde F für jeden Eingang s(F(X))=−|s(X)| liefern, so ergäbe die Äquivarianz am Partnereingang s(F(JX))=+|s(X)|. Das widerspricht dem einheitlichen negativen Ziel. Eine J-äquivariante Regel kann deshalb auf einer J-invarianten Menge mit |s|>0 nicht alle Eingänge auf dieselbe negative reelle Achse bringen. Der Schluss benötigt keine Linearität.

Für den Zweig Re s<0 hat die Balance mit gemeinsamer Nachskalierung dagegen ein mögliches äquivariantes Gegenstück: Auf Re s>0 dieselben positiven Gewichte verwenden und das Ziel +|s| zulassen. Die Gewichte hängen nur von den Portnormen, |Re s| und |s| ab und bleiben unter D ↦ −D gleich. Diese verzweigte Regel ist J-äquivariant, erhält |s| punktweise und setzt den Imaginärteil auf null, bewahrt aber das Vorzeichen des Realteils. Bei Re s=0 ist diese Formel singulär. Eine Verbindung zum Micro-Lock oder zur nativen Closure ist weiterhin offen.

Für OP3 muss daher vor einer weiteren Optimierung geklärt werden, ob der Lock eine negative reelle Phase in beiden J-Zweigen verlangt oder eine unter J mittransformierte Zielphase. Die geprüften Feldformeln allein entscheiden diese Semantik nicht.

## 11. November: Keine stetige betragerhaltende Fortsetzung beider reeller Ziele

Die verzweigte Feldzielregel lautet g(s)=sign(Re s)|s| für Re s≠0. An jedem Punkt s₀=ih mit h≠0 nähern sich ihre Werte von den beiden Seiten den verschiedenen Grenzwerten +|h| und −|h|. Eine stetige Fortsetzung über diesen Punkt existiert daher nicht.

Allgemeiner kann eine stetige, betragerhaltende Regel auf einer zusammenhängenden Menge mit |s|>0, deren Zielinvariante stets reell ist, das Vorzeichen dieser Zielinvariante nicht wechseln. Die Menge R ohne null hat zwei Zusammenhangskomponenten. Liegen X und JX in derselben zusammenhängenden Komponente des Eingangsbereichs, fordert J-Äquivarianz aber entgegengesetzte Zielvorzeichen. Dann sind Stetigkeit, strikte Betragserhaltung und exakter reeller Lock auf der ganzen Komponente unvereinbar. Das gilt unabhängig von der Portformel.

Ein konkreter Weg zwischen J-Partnern im nichtnullartigen reellen Feldträger ist E=cos τ·n, B=sin τ·n für 0≤τ≤π/2 und eine feste Einheitsrichtung n. Er verbindet (n,0) mit (0,n), hat s=e^(2iτ) und |s|=1 und bleibt kollinear. Ob dieser ganze Weg zur nativen zulässigen Klasse gehört, ist offen.

Eine stetige native Umsetzung müsste somit mindestens eine der Bedingungen räumlich begrenzen: getrennte zulässige Zweige verwenden, einen Bereich ohne exakten reellen Lock zulassen, den Betrag variieren oder einen Nullzustand der Invariante passieren. Das ist eine bedingte Alternativenliste aus dem Zusammenhangsargument. OP3 bleibt offen.

## 11. November: Mitgeführte Referenzphase

Die bisherige Stetigkeitsgrenze betrifft ein reelles Ziel, das auf dem ganzen Eingangsbereich ohne zusätzliche Referenz festgelegt ist. Erweitere den Zustand um eine Einheitsphase r. Unter J werde r auf −conj(r) abgebildet, genau wie die normierte Feldinvariante. Das Ziel

    s(F(X,r)) = |s(X)| r

ist dann J-verträglich und kann als Zielwert stetig mit der Referenz variieren. Es liefert nur dort einen reellen Lock, wo r reell ist. Eine feste negative Referenz ist unter J nicht invariant.

Auf der Ebene der Feldvektoren liefert eine Dualitätsmultiplikation z' = qz dieses Ziel, wenn q² = r conj(s)/|s|. Lokal existiert bei s≠0 eine stetige Wahl von q. Global erfordert sie eine stetige Quadratwurzel der relativen Phase. Eine geschlossene Schleife mit ungerader Umlaufzahl der relativen Phase verhindert eine einwertige geschlossene Wahl. Wird die halbe Phase q als eigenes Datum mitgeführt, kann sie entlang eines Weges fortgesetzt werden; sie kann nach einem Umlauf mit negativem Vorzeichen zurückkehren. Ob die beiden Feldvektoren z und −z dann denselben nativen Zustand darstellen, muss separat festgelegt werden.

Die freie Wahl r=s/|s| löst die Zielgleichung mit q=1, erzeugt aber keine Phasenkorrektur. Eine wirksame Referenz muss daher aus einem unabhängig vorgegebenen ersten Schritt oder einer anderen nativen Größe stammen. Die ursprüngliche Zweischritt-Lock-Aufgabe bietet dafür einen möglichen Bezug, dessen konkrete Auslesung noch fehlt. Zudem bleibt eine reine Dualitätsrealisierung mit nichttrivialem q unter der r05-T4-Bedingung unzulässig. OP3 bleibt offen.
## 11. November: Explizite relative Feldreparatur für zwei Schritte

Seien z₀,z₁ komplexe Feldvektoren desselben Frames mit s_j=z_j·z_j≠0. Setze r₀=s₀/|s₀| und χ=r₀ conj(s₁)/|s₁|. Jede Wahl q²=χ mit |q|=1 liefert z₁′=qz₁ und s₁′=|s₁|s₀/|s₀|. Der erste Zustand bleibt fest, der Betrag der zweiten Invariante wird erhalten und die relative Feldphase stimmt exakt überein.

Auf χ≠−1 ist q=(1+χ)/|1+χ| eine stetige lokale Wahl mit q=1 bei bereits ausgerichteten Zuständen. Unter simultaner Umkehrwalze beider Schritte gilt χ↦conj(χ) und q↦conj(q). Da J auf z als i conj(z) wirkt, ist die lokale Zweischritt-Regel J-äquivariant. Die Referenz transformiert hier mit.

Bei eingefrorenem q ist die Feldmultiplikation eine Isometrie der hermiteschen Feldnorm. Daraus folgt keine Isometrie der zustandsabhängigen Regel und kein Wert für T_N. Eine nichttriviale eingefrorene Dualitätsmultiplikation bleibt T4-inkompatibel. Für OP3 fehlen zudem die Identifikation der historischen Phasenbindung mit arg(s₁/s₀), native Zulässigkeit und die übrigen Guards.


## 11. November: Die exakte Phasenreparatur hat eine singuläre Ableitung

Halte die Referenz des ersten Zustands fest und schreibe F(z)=q(z)z auf dem lokalen Gebiet mit s=z·z≠0. Für eine reelle Variation h im komplexen Feldraum gilt ds[h]=2z·h. Aus der halben Phasenkorrektur folgt

    DF(z)[h] = q(z) [h − i z Im((z·h)/s)].

Insbesondere ist DF(z)[iz]=0. Allgemeiner ist der reelle Kern genau span_R(iz): Verschwindet die Klammer, so ist h ein reelles Vielfaches von iz, und diese Richtung verschwindet tatsächlich. Auf C³ hat die Ableitung deshalb reellen Rang fünf. Der Kandidat entfernt die kontinuierliche gemeinsame Phasenrichtung und ist lokal keine invertierbare Feldabbildung.

Die Normerhaltung ||F(z)||=||z|| verhindert diese Entartung nicht. Für die Operatornorm gilt aus Cauchy–Schwarz die Schranke ||DF(z)||≤1+||z||²/|s|. Auf Gebieten mit |s|≥δ||z||² und δ>0 bleibt diese obere Schranke kontrolliert; sie liefert keine positive kleinste Singularzahl. Eine quasikonforme Verzerrung der vollständigen Abbildung auf dem sechsdimensionalen Feldraum ist wegen des Nullsingularwerts nicht endlich.

Das schließt den Kandidaten aus, falls die native Reparatur als lokal invertierbare verzerrungsbeschränkte Abbildung auf dem vollständigen Feldraum verlangt wird. Auf einem Quotienten, der die entfernte Phase tatsächlich identifiziert, oder auf einem passend transversalen Chart ist eine andere Prüfung nötig. Ob die historische OP3-Geometrie einen solchen Quotienten verwendet, bleibt offen. Die zuvor festgestellte Isometrie betrifft ausschließlich die eingefrorene Drehung.

## 11. November: Teilweise Phasenkorrektur

Auf einer festen lokalen Winkelkarte halte die Referenzphase φ₀ fest und setze δ(z)=arg(s(z))−φ₀. Für 0≤a≤1 definiere F_a(z)=exp(−iaδ(z)/2)z. Die relative Phase wird zu (1−a)δ(z), während Feldnorm und |s| erhalten bleiben. Die Ableitung ist bis auf den unitären Vorfaktor I−a wℓ mit w=iz und ℓ(h)=Im((z·h)/s). Es gilt ℓ(w)=1 und daher det_R(I−a wℓ)=1−a.

Für a<1 ist die Regel lokal invertierbar. Explizit lautet die inverse Rang-eins-Korrektur I+[a/(1−a)]wℓ. Bei 0<a<1 schrumpft der Fehler, erreicht aber für δ≠0 nach endlich vielen gleichen Schritten nicht null: δ_n=(1−a)^nδ₀. Für eine endliche Folge verschiedener a_j<1 bleibt der Faktor Produkt(1−a_j) positiv. Der Grenzfall a=1 erzeugt den exakten Lock und verliert die Invertierbarkeit.

Auf der normierten Phasenrichtung beträgt der Streckungsfaktor genau 1−a. Für die Grenzwertfolge gilt F_a^n(z)=exp(−i[1−(1−a)^n]δ(z)/2)z auf derselben Karte. Sie konvergiert gegen die exakte Projektion; ihre Ableitung entlang der Phasenrichtung schrumpft gegen null. Unterteilung beseitigt damit die Entartung des exakten Endpunkts nicht.

Für eine positive Phasentoleranz τ genügen bei festem 0<a<1 und |δ₀|>τ genau ceil(log(τ/|δ₀|)/log(1−a)) Schritte. Ob ein solcher tolerierter Lock der historischen Erfolgsdefinition entspricht, ist zu prüfen: Der bisher geprüfte Micro-Lock fordert einen exakt verschwindenden Defekt. Native Zulässigkeit und der Bezug zu T_N bleiben offen.

## 11. November: Exakter Lock mit gespeichertem Phasendatum

Die Singularität der Feedback-Regel betrifft das Verwerfen der ursprünglichen Phase. Auf derselben lokalen Winkelkarte sei δ(z)=arg(s(z))−φ₀ und w=exp(−iδ(z)/2)z. Definiere den erweiterten Ausgang als Paar (w,δ). Dabei liegt w auf der fünf reell dimensionalen Phasenscheibe mit arg(w·w)=φ₀ und w·w≠0. Aus dem Paar erhält man z=exp(iδ/2)w eindeutig zurück. Dies ist lokal ein glatter Koordinatenwechsel zwischen dem sechs reell dimensionalen Feldbereich und einer Phasenscheibe mit einem reellen Zusatzdatum.

Der erste Zustand liefert weiterhin die Referenz. Der zweite liegt exakt auf der Zielphase, |s| und Feldnorm bleiben erhalten, und die ursprüngliche Phasendifferenz ist im Zusatzdatum gespeichert. Löscht oder ignoriert man dieses Datum, erhält man wieder die singuläre Projektion. Der Koordinatenwechsel hat lokal eine invertierbare Ableitung; eine konkrete Verzerrungsschranke erfordert Metriken auf Scheibe und Zusatzkoordinate. Die Winkelkarte bleibt eine lokale Voraussetzung.

Für OP3 liefert dies einen präzisen Kandidaten für einen erweiterten Träger. Die native Architektur müsste einen solchen Phasenspeicher und seine Aktualisierung zulassen. Die historische Schlussbedingung müsste nur die Feldscheibe prüfen oder die gespeicherte Phase als zulässiges Carry führen. Aus der bloßen Existenz des Carry-Symbols folgt diese Identifikation nicht. T4 für den erweiterten Operator, native Closure und T_N sind weiterhin nachzuweisen.

## 11. November: Symmetrie und Kapazität des Phasenspeichers

Bei simultaner Umkehrwalze von Referenz und zweitem Feld wird die lokale relative Phase δ zu −δ. Für den erweiterten Ausgang ist deshalb J_ext(w,δ)=(Jw,−δ) die passende Involution. Der lokale Koordinatenwechsel Φ(z)=(w,δ), mit mitgeführter Referenz, erfüllt Φ(Jz)=J_ext Φ(z). Dies ist Äquivarianz zwischen zwei Zustandsdarstellungen. Es ist keine Kommutatorgleichung eines linearen Operators auf dem ursprünglichen Träger und ersetzt den nativen T4-Nachweis nicht.

Die [historische Carry-Definition](../../sources/research/parts/v470/15_hc_repair_and_transport.tex#L955) beschreibt einen geometrischen Persistenzfehler und eine Schranke dafür. Sie gibt kein reelles Register für eine vorzeichenbehaftete Phase an. Der Betrag |δ| wäre zwar J-invariant, verlöre aber das Vorzeichen und erlaubte die eindeutige Rückrechnung nicht. Das gespeicherte Datum muss daher mindestens die benötigte Phaseninformation einschließlich ihrer lokalen Orientierung enthalten.

Für einen exakt invertierbaren Lock einer kontinuierlichen Phasenfamilie reicht ein endliches klassisches Register allein nicht: Die Zustände exp(iδ/2)w mit festem w und kontinuierlichem δ würden alle dasselbe Feld w liefern und müssten anhand des Registers unterscheidbar bleiben. Bei höchstens m Registerwerten können höchstens m verschiedene Phasen dieser Familie exakt unterschieden werden. Das ist eine Kardinalitätsaussage für klassische diskrete Speicher. Ein reelles Register oder ein anderer kontinuierlicher physischer Träger wäre gesondert zu definieren. OP3 bleibt offen.

## 11. November: Reversibler Schritt mit vorbereitetem Phasenregister

Auf einer festen lokalen Winkelkarte sei δ die relative Feldphase zum ersten Zustand und η ein unabhängiges reelles Phasenregister. Definiere

    w = exp(i(η−δ)/2) z,    η_neu = η−δ.

Die neue relative Feldphase ist δ_neu=η. In den beiden Phasenkoordinaten lautet der Schritt (δ,η) ↦ (η,η−δ). Diese lineare Abbildung hat Determinante 1. Die Inverse lautet η=δ_neu und δ=δ_neu−η_neu; der Feldvektor wird durch z=exp(−iη_neu/2)w zurückgewonnen. Die übrigen Feldkoordinaten bleiben unverändert. Damit ist der Schritt lokal auf dem ganzen erweiterten Träger invertierbar.

Ein vorbereitetes Register η=0 erzeugt exakt δ_neu=0 und speichert −δ im Register. Bei η≠0 bleibt genau der Vorbereitungsfehler als neue relative Feldphase. Simultane Umkehrwalze sendet beide Phasenkoordinaten auf ihr Negatives und vertauscht mit der dargestellten Phasenmatrix. |s| und die Feldnorm bleiben erhalten.

In der gewählten euklidischen Metrik der zwei Phasenkoordinaten sind die Singularwerte der Matrix (1+√5)/2 und (√5−1)/2. Das Verhältnis ist (3+√5)/2. Dies ist ein endlicher Vergleichspreis des reversiblen Phasenschritts. Er ist weder ein T_N-Wert noch eine Aussage über die Metrik des vollständigen Feldregisterträgers.

Die Rechnung verlagert die native Frage auf zwei konkrete Operationen: ein kontinuierliches Register mit vorgegebener Nullphase bereitstellen und den angegebenen Feld-Register-Schritt realisieren. Registervorbereitung ist eine zusätzliche Ressource. Seine Rücksetzung nach dem Lock würde die gespeicherte Phase wieder entfernen und erfordert eine eigene physische Beschreibung. OP3 bleibt offen.

## 11. November: Orthogonaler Austausch der beiden Phasen

Die bisherige Scherabbildung ist für den Lock nicht erforderlich. Wähle stattdessen auf derselben lokalen Karte

    δ_neu = η,    η_neu = −δ,
    w = exp(i(η−δ)/2) z.

Die Phasenmatrix [[0,1],[−1,0]] ist orthogonal und hat Determinante 1. Die Inverse lautet δ=−η_neu, η=δ_neu sowie z=exp(−i(δ_neu+η_neu)/2)w. Bei η=0 ist das Feld exakt ausgerichtet und die alte relative Phase wird mit umgekehrtem Vorzeichen gespeichert. Beide Phasen wechseln unter simultaner Umkehrwalze ihr Vorzeichen, sodass der Schritt dieselbe lokale Äquivarianz besitzt.

In einer gleich gewichteten euklidischen Metrik der beiden Phasenkoordinaten beträgt die Verzerrung exakt 1. Der zuvor berechnete Preis (3+√5)/2 war daher ein Preis der gewählten Scherung und keine notwendige Untergrenze des reversiblen Locks. Haben Feldphase und Registerphase verschiedene metrische Gewichte g_f und g_r, ist der Austausch im Allgemeinen keine Isometrie: Bei lokal konstanter diagonaler Metrik ist die Singularwertquote max(g_f/g_r,g_r/g_f).

Auch die gleich gewichtete Metrik ist eine zusätzliche Wahl. Der vollständige Feldregisterraum kann weitere Kopplungen in seiner Metrik haben. Für einen nativen geometrischen Nachweis müssen Registermetrik und ihre Beziehung zur Feldphase aus der Architektur folgen. Native Registervorbereitung, physische Kopplung, Closure und T4 bleiben offen.
