# OP5 – Was der Rücklauf über den Einwegfehler bestimmt

21. November 2026. Analytische Erkundung im Materieframe M. Die [gekreuzte Schaltkontrolle](OP5_J_Gekreuzte_Schaltkontrolle.md) lässt für die gemischte komplexe Abweichung zwischen Signal- und Kontrollpfad $5\cdot10^{-7}$ im Loggewinn. Hier wird geprüft, wann ein Rücklauf diesen Beitrag einschränkt. Die [Einkanalreferenz](OP5_J_Einkanal_Nullreferenz.md) legt die kohärenten Referenzebenen und das Budget fest. Der [Anschlussvergleich](OP5_J_HCl_Anschlusskondition.md) liefert die separate Zweikanalbedingung. Im [Gesamtbild](../../../wiki/Gesamtbild.md) ist dies eine Frage der lokalen Auslese. I3 benötigt eine eigenständige kosmologische Bestandsdynamik.

## Was das Echo identifiziert

Für die vier Marker-/Schalterzustände seien $F_{ms}$ und $B_{ms}$ die für den Abgleich relevanten komplexen Einwegfaktoren in Hin- und Rückrichtung. Gemeint sind Faktoren der Anschlussabweichung zwischen Signal und Kontrolle, nach unabhängig bekannter Normalisierung der eigentlichen Durchgänge. Ein einzelner isolierter Rücklauf sei $E_{ms}=F_{ms}B_{ms}\rho_{ms}$, mit bekannter komplexer Reflexion $\rho_{ms}$ an der Gegenebene. Mehrfachreflexionen, andere Echoanteile und Modenumwandlung müssen für dieses skalare Produktmodell getrennt oder über einen Fehlerrest erfasst werden.

Mit $C(X)=X_{11}X_{00}/(X_{10}X_{01})$ gilt
$$
C(E/\rho)=C(F)C(B).
$$
Die Transformation $(F_{ms},B_{ms})\mapsto(\lambda_{ms}F_{ms}, B_{ms}/\lambda_{ms})$ hält jedes Echo fest und ändert $C(F)$ beliebig. Eine Echo-Messung allein bestimmt den Einwegfehler daher auch bei idealer Präzision nur mit einer Zusatzbedingung.

Auf kohärent verfolgten, zueinander passenden Logzweigen gilt
$$
2\log C(F)=\log C(E/\rho)+\log[C(F)/C(B)] .
$$
Ein Betrag $b_{\rm echo}$ für den normalisierten komplexen Log-Kreuzquotienten muss Messfehler, Spiegelzustände und verbleibende Mehrfachpfade einschließen. Eine unabhängige Schranke $b_{\rm asy}$ für den gemischten Richtungsunterschied genügt zusammen mit
$$
b_{\rm echo}+b_{\rm asy}\le10^{-6}.
$$
So bleibt $|\log C(F)|\le5\cdot10^{-7}$ pro Bandende. Beispielsweise sind $4\cdot10^{-7}$ für Echo und $6\cdot10^{-7}$ für Richtungsunterschied gemeinsam hinreichend. Wird eine kompensierte Echo-Schätzung verwendet, gilt dieselbe Schranke für den entsprechenden Schätzfehler im Einwegfaktor.

Es genügt Reziprozität des **gemischten Richtungsfaktors** $C(F)/C(B)=1$. Feste Asymmetrien eines Körpers oder reine Schaltasymmetrien können sich im Kreuzquotienten schon kürzen. Eine pauschale Annahme eines passiven Aufbaus liefert diese Gleichheit nicht. Eine Reziprozitätsaussage muss die konkreten Portmoden, Referenzebenen, Schaltzustände und die tatsächlich vom Kontrollton gesehenen Faktoren abdecken. Ohne diese Absicherung braucht es einen unabhängig bekannten Einwegdurchgang oder einen von beiden Seiten kalibrierten Vergleich.

## Was die Parallelspuren einschränken

- **Freie J-Ausbreitung.** Die lokale HCl-Linie bei $0{,}360329$ eV liefert im Vergleichsmodell eine Anschlussrichtung. Ein massiver freier J-Kanal ist dort nur oberhalb seiner Ruheenergie offen. Der für die 100-MHz-Toleranzrechnung eingesetzte Wert von rund $0{,}00510$ eV wurde zur Phasenanpassung gewählt. Für ein in der Nähe seiner Schwelle liegendes oder geschlossenes J muss die Zweikanalschranke neu gerechnet werden. Eine freie kohärente Laufphase über mehrere bekannte Streckenlängen und Frequenzen ist der nächste unterscheidende Test, mit separat abgeglichenen Anschlussphasen und Kontrolle evaneszenter Anteile. Der frühere nominelle MeV-Bereich des Stückelberg-Vergleichs käme bei dieser optischen Energie für dieselbe massive Mode nicht infrage. Ein optischer A‑Durchgang kann unabhängig davon geprüft werden. Seine Reziprozität liefert keine Ausbreitungsbedingung für J. [Vektoranschluss](OP5_J_HCl_Vektoranschluss.md) · [J-Modellphase](OP5_J_Ruecklauf_Toleranzen.md)
- **Native Kopplung.** Die modellierten Quantitäten eines gerichteten massiven Vermittlers und die materielle Higgsquelle liefern bedingte Vorhersagen. Ein A‑Kontrollton bestimmt weder den nativen Kopplungskoeffizienten noch eine mögliche Wirkung des Schalters auf den J‑Kanal. Ein gemeinsamer skalarer Maxwell-Vorfaktor erzeugt im geprüften masselosen Vergleich keine führende zusätzliche Laufphase; der Tensorvergleich mit unterschiedlichen elektrischen und magnetischen Beiträgen kann eine Laufphase erzeugen, setzt seine Stärke aber ein. Für die native Suche ist damit ein aus der Wirkung abgeleiteter Differenzoperator für J und A gesucht. [Wellenvergleich](OP5_J_Wellenauslese.md) · [Tensorvergleich](OP5_J_Tensorkopplung.md) Ein J‑abhängiges Signal darf im Kontrollvergleich nur dann als gemeinsamer Anschlussfaktor behandelt werden, wenn diese Zuordnung aus der Wirkung oder einem unabhängigen Kalibrierdurchgang folgt.
- **HCl/H.** Schon ohne Übersprechen gilt für die kleinste Singulärzahl eines Endes $\sigma_{\min}\le a\sqrt{1-|v_H^\dagger v_C|^2}$. Im schwachen illustrativen Kopplungsfall ist der geometrische Faktor rund $0{,}00254$. Eine stärkere HCl-Resonanz allein hebt diese Grenze bei festem H-Port nicht an. Damit sind ein guter A‑Monitor und eine gut konditionierte Zweikanalrekonstruktion eigenständige Prüfungen.

Wolfram bestätigt die Produktidentität, die Freiheit der ungemessenen Einwegfaktoren und den reziproken Grenzfall exakt. Die Auswertung benötigt klassische komplexe Übertragungskoeffizienten. Ein gemessener Abgleich der A‑Ports, freie J‑Ausbreitung, native Kopplung und H96 bleiben offen.

[Wolfram-Skript](op5_j_einweg_ruecklauf.wl) · [Tatsächliche Ausgabe](op5_j_einweg_ruecklauf.txt) · [Laufmanifest](op5_j_einweg_ruecklauf.json)
