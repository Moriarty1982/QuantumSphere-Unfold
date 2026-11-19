# OP5: Anomaliefreie Erweiterung und Beta-Zerfall des Sechserkandidaten

19. November 2026. Analytische Erkundung in M. Die [Coulomb-Induktion](OP5_Sechserbindung.md) setzt einen stabilen $udd$-Kern voraus. Die [Ladungsrechnung](OP5_Paarstabilitaet.md) lässt die gemeinsame Eichung von J und schwachem $SU(2)$ offen. Hier wird eine konkrete zusätzliche Feldliste als Existenzbeispiel geprüft und anschließend die Stabilität des Kerns gegen die damit zugängliche schwache Umwandlung. Für [H96](../predictions/Vorab_Notiz_H96_Omega_M_beta2.md) wird kein Datenvergleich vorgenommen.

## Ein gemeinsamer Eichsektor mit unveränderten J-Ladungen

Wähle die Produktgruppe $SU(3)_c\times SU(2)_L\times U(1)_Y\times U(1)_J$. Füge pro ursprünglicher Dirac-Generation mit $\nu_R$ eine zweite Generation hinzu. Sie bekommt exakt dieselben Farbdarstellungen, schwachen Darstellungen und Hyperladungen, aber alle J-Ladungen mit umgekehrtem Vorzeichen. Der Higgs bleibt unter J neutral. Die Yukawa-Kopplungen innerhalb beider Generationen sind J-invariant und können verschiedene Massen liefern, ohne J durch den Higgs-Vakuumwert zu brechen. Für die betrachtete Dirac-Variante wählen wir keine Majorana-Terme, auch keinen durch J allein erlaubten generationsübergreifenden Singulett-Term $\nu^c\nu'{}^c$. Ein auferlegtes gemeinsames $B-L$ verbietet diesen Term.

Im linkshändigen Weyl-Schema sind die Gewichte der ursprünglichen Generation:

| Feld | Farbdarstellung | $SU(2)$ | Multiplizität | $6Y$ | J |
| --- | --- | --- | ---: | ---: | ---: |
| $Q$ | $\mathbf 3$ | $\mathbf 2$ | 6 | 1 | 1 |
| $u^c$ | $\bar{\mathbf 3}$ | $\mathbf 1$ | 3 | -4 | -1 |
| $d^c$ | $\bar{\mathbf 3}$ | $\mathbf 1$ | 3 | 2 | -1 |
| $L$ | $\mathbf 1$ | $\mathbf 2$ | 2 | -3 | 1 |
| $e^c$ | $\mathbf 1$ | $\mathbf 1$ | 1 | 6 | -1 |
| $\nu^c$ | $\mathbf 1$ | $\mathbf 1$ | 1 | 0 | -1 |

Die Konvention ist $Q_{\rm em}=T_3+Y$. Mit $T(\mathbf 2)=T(\mathbf 3)=1/2$ lauten die J-haltigen Spuren:

| Anomaliekoeffizient | Ursprünglich | Zusatz | Summe |
| --- | ---: | ---: | ---: |
| $SU(2)^2J$ | 2 | -2 | 0 |
| $SU(3)^2J$ | 0 | 0 | 0 |
| $Y^2J$ | -2 | 2 | 0 |
| $YJ^2$ | 0 | 0 | 0 |
| $J^3$ | 0 | 0 | 0 |
| Gravitation–J | 0 | 0 | 0 |

Die vier abelschen und gravitativen Spuren wurden direkt mit ganzzahligen Gewichten $6Y$ und den Multiplizitäten kontrolliert. Nur bei $(6Y)^2J$ sind die Einzelwerte ungleich null, nämlich $-72$ und $+72$. Die reinen Standardmodell-Anomalien verschwinden pro Generation. Die globale $SU(2)$-Anomalie greift hier nicht: Pro ursprünglicher Generation mit Zusatz gibt es acht fundamentale Weyl-Dubletts einschließlich Farbmultiplizität. Damit ist die geprüfte Eichanomalie mit unveränderten ursprünglichen J-Ladungen aufhebbar, allerdings durch zusätzliche chirale Materie. Massen, phänomenologische Verträglichkeit und Einbau in W2 sind damit offen. [Anomaliekonventionen und globale SU(2)-Anomalie](https://davidtong.org/pdfs/teaching/standard-model/standardmodel4.pdf)

## Der ursprüngliche Kern darf beta-zerfallen

Mit geladenem schwachem Strom wird im ursprünglichen Sektor aus $udd$ ein $uud$-Kern. Der bekannte Prozess $n\to p+e^-+\bar\nu_e$ erhält J, elektrische Ladung und $B-L$. Dieselben Bilanzen gelten mit drei zunächst gebundenen $\bar\nu_e$:
$$
(n+3\bar\nu_e)_{\rm geb}\longrightarrow p+e^-+4\bar\nu_e ,
\qquad Q_J:0=3+1-4,\qquad Q_{\rm em}:0=1-1,\qquad B-L:4=1-1+4 .
$$
Als kinematische Referenz verwende die gewöhnlichen gemessenen Nukleon- und Elektronenmassen und eine leichte Dirac-Neutrinomasse $m$. Die zusätzliche J-Dynamik könnte die Massen ändern. Mit diesen Eingaben ist der freie Energieüberschuss $\Delta_{\rm free}=M_n-M_p-m_e-m$ annähernd $0{,}782\,{\rm MeV}$. Für den Übergang vom gebundenen Anfangszustand zu vollständig getrennten Endteilchen ist der Energieüberschuss $\Delta_{\rm free}-B_n$, wobei $B_n=-E_3>0$ die gesamte Bindungsenergie der drei Antineutrinos bezeichnet. Würden sich Endteilchen binden, könnten zusätzliche niedrigere Schwellen existieren. Die gewöhnliche freie Massendifferenz ist eine Eingabe für den Vergleich. [GSI-Vorlesung, Abschnitt zum Neutron-Beta-Zerfall](https://web-docs.gsi.de/~wolle/TELEKOLLEG/KERN/LECTURE/Fraser/L1.pdf)

## Obergrenze der Bindungsenergie

Abtrennen der Schwerpunktbewegung bei Gesamtimpuls null und Wahl der drei Koordinaten relativ zum Kern liefert die Summe der kinetischen Terme $\sum_i p_i^2/(2m)$ und den nichtnegativen Rückstoßterm $(\sum_i p_i)^2/(2M_n)$. Auch die Coulomb-Abstoßung zwischen den Antineutrinos ist nichtnegativ. Weglassen dieser beiden Terme gibt eine untere Schranke für $E_3$. Übrig bleiben drei Spin-½-Fermionen im Einteilchenpotential $-3A/r$, $A=g_J^2/(4\pi)$. Nach dem Pauli-Prinzip belegen zwei Fermionen den ersten und das dritte den zweiten Hauptenergiewert. Damit gilt
$$
E_3\ \ge\ -\frac{9}{2}mA^2\left(2+\frac14\right),\qquad
B_n\ \le\ \frac{81}{8}mA^2 .
$$
Zusammen mit der [Induktion](OP5_Sechserbindung.md) gilt $0<B_n\le81mA^2/8$. Eine hinreichende Bedingung für den offenen Beta-Zerfall zu vollständig getrennten Endteilchen ist also
$$
\Delta_{\rm free}>\frac{81}{8}mA^2 .
$$
Bei sub-eV-Neutrinomassen und schwacher Kopplung im nichtrelativistischen Modell liegt die obere Schranke weit unter dem gewöhnlichen Neutron-Energieüberschuss. Für eine andere Masseneingabe muss die Ungleichung geprüft werden. Die Rechnung weist einen schwachen Prozess mit offener kinematischer Schwelle nach. Eine Zerfallsrate erfordert das hadronische Matrixelement, die gebundenen und gestreuten Leptonwellenfunktionen und die Antisymmetrisierung der vier Antineutrinos im Endzustand. Damit bleibt die Lebensdauer offen. Auch die Bildung einer Population und H96 bleiben offen.
