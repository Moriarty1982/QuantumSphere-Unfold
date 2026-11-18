# OP5: Breitbandige Sperre durch Auswahl der offenen Kanäle

Analytische Erkundung nach [Vorab-Notiz](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/b3b35a14afabdc46fee7ba3cc1a28ddbd3990a22/notes/research/op5_bifocal_response_2026_11_18/Kanalauswahl_Vorab.md). Die zwei Kanalindizes der folgenden Modelle sind interne Zustände in einem gemeinsamen Raumsystem. Eine Identifikation mit den Frames M/T ist keine Eingabe.

## Endlicher Abschnitt bei beidseitig offenen Kanälen

Betrachte einen statischen Dirac-Abschnitt mit n vollständig offenen, stromnormierten Kanälen in beiden Leitungen. Im endlichen Übergangsbereich sei die Koeffizientenmatrix der linearen Gleichung erster Ordnung beschränkt und stromerhaltend. Es gibt im betrachteten Kanalraum keine weiteren geschlossenen Freiheitsgrade. Die Transfermatrix M ist endlich und erfüllt M†ΣM=Σ mit Σ=diag(Iₙ,−Iₙ).

Schreibe M in Blöcken A,B,C,D gemäß (b_rechts⁺,b_rechts⁻)=M(a_links⁺,a_links⁻). Die Flusserhaltung liefert D†D=I+B†B und A†A=I+C†C. Beide Diagonalblöcke sind invertierbar. Bei Einfall von links und b_rechts⁻=0 ist die Transmissionsmatrix t=A−BD⁻¹C. Der obere linke Block von M⁻¹ ist zugleich t⁻¹ und A†, denn M⁻¹=ΣM†Σ. Also gilt t=(A†)⁻¹. Jede von null verschiedene einlaufende Kombination trägt rechts einen positiven propagierenden Fluss. Beliebige endliche kohärente Mischung innerhalb dieses rein offenen Systems erzeugt keine vollständige Sperre auch nur eines einlaufenden Vektors. Die Voraussetzung, dass der Transferraum nur beidseitig offene Kanäle enthält, schließt die diskrete Seitenmode aus Interferenz.md ausdrücklich aus.

## Exakte Sperre bei verschiedenen offenen Sektoren

Seien Π±=(I±τ₃)/2 zwei interne orthogonale Projektoren und σ_i die Dirac-Matrizen. In Einheiten ħ=c=1 sei

    H = −iσ₂⊗I ∂ₓ + σ₁⊗m₀[f(x)Π₊ + (1−f(x))Π₋],   m₀>0.

Setze f=0 weit links, f=1 weit rechts und dazwischen irgendein beschränktes reelles Profil. H kommutiert überall mit I⊗τ₃. Für 0<E<m₀ ist links nur Π₊ propagierend (massefrei), rechts nur Π₋ (massefrei). Das von links einlaufende Π₊-Signal bleibt in Π₊ und besitzt rechts nur einen abklingenden Anteil. Der normale Strom dieses Anteils ist konstant und geht gegen null, daher ist er null. Es folgt T(E)=0 und vollständige Reflexion im ganzen Intervall. Für Einfall von rechts gilt derselbe Schluss mit vertauschten Sektoren. Beide Leitungen tragen in diesem Intervall für sich genommen propagierende Zustände. Die Sperre gilt für alle Übergangsprofile mit dieser Symmetrie und denselben asymptotischen Lücken.

## Abgleich mit W2 und dem Randdipol

Der gemeinsame Kommutant als Auswahltest wurde schon in analysis/OP5_Dynamics_And_Symmetry_Selection.md formuliert. Hier kommen zwei konkrete Anforderungen an den Transport hinzu: Er braucht einen erhaltenen Projektor und eine räumliche Karte, die auf den beiden Seiten verschiedene offene Spektralsektoren ausweist. Eine gemeinsame Ladung X kann die Projektoren nach ihren Eigenwerten schützen, sofern die effektive Einteilchendynamik mit X kommutiert. Innerhalb eines Eigenraums, in dem X=qI wirkt, erlaubt die Ladung allein aber auch einen Mischterm proportional zu τ₁. Das Beispiel behauptet nicht, dass ein solcher Term auch unter den übrigen W2-Symmetrien erlaubt wäre.

Die klassische W2-Dirac-Lesart liefert X=3(B−L). Der im Bestand geprüfte M→T-Wechsel R kommutiert mit X und bewahrt damit gerade dessen Ladungssektoren. Er liefert keine einander ausschließenden asymptotischen Kanäle und keine räumliche Grenzfläche. Auch die Gegenphasensymmetrie im Paarmodell erhält eine modellierte Differenz, legt aber bisher keine W2-Leitungsspektren fest. Die breitbandige Sperre ist damit ein analytischer Modellbefund. Ihre physikalische Abbildung, die Herstellung des Überschusses und H96 bleiben offen. Für die als I3 zurückgestellte Lesart könnte erst eine unabhängig begründete Überschussdynamik als Ausgangspunkt für die Λ-Auslese dienen.
