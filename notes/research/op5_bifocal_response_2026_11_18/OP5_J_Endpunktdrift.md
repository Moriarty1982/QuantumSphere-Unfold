# OP5 — Endpunktdrift bei differentieller Laufzeit

20. November 2026. Analytische Erkundung im Materieframe M.

## Vorwissen geprüft

Die [doppelte Laufzeitdifferenz](OP5_J_Doppelte_Laufzeitdifferenz.md) kürzt feste Endpunktfaktoren in der Einzelpfad-Übertragung. Endpunktänderungen durch ein verändertes D-Profil benötigen dort bekannte Apparaturempfindlichkeiten. Der [longitudinale Abgleich](OP5_J_Longitudinaler_Abgleich.md) unterscheidet freie Ausbreitung von Beiträgen der geladenen Sender- und Detektorregionen. Der [Kalibrierrechner](OP5_J_Kalibrierprofile.md) setzt bereits gebildete Karten voraus. Das [Gesamtbild](../../../wiki/Gesamtbild.md) ordnet die absolute Materieauslese H96 zu. Rückwärts braucht jede J-Karte zuerst eine identifizierbare Änderung der Ausbreitungsphase bei definiertem physischen Kontrast.

## Zeitdrift und profilgebundene Endpunktantwort

Sei $s=0,1$ das D-Profil A oder B. Für einen identifizierten Einzelpfad und nichtverschwindende Übertragungsfunktionen im Frequenzfenster setze
$$
z(t,s,\omega)=\partial_\omega\arg[H_J/H_A](t,s,\omega)
 = P_0(\omega)+f(t,\omega)+s[\Delta P(\omega)+\delta(\omega)].
$$
$P_0$ ist der Grundwert, $\Delta P$ die gesuchte Laufzeitänderung entlang der Strecke, $f$ der profilunabhängige Endpunktdrift und $\delta$ die mit dem Profilwechsel gekoppelte Endpunktantwort. Die Darstellung setzt reproduzierbare Profile und eine zeitlich konstante profilgebundene Antwort innerhalb des Blocks voraus. Einschwingvorgänge und Gedächtniseffekte sind darin unberücksichtigt.

Messe A–B–B–A in gleichen Zeitabständen $h$ um die Blockmitte zu Zeiten $h(-3,-1,1,3)/2$. Mit den Gewichten $(-1,1,1,-1)/2$ ist
$$
D=\tfrac12(z_2+z_3-z_1-z_4)=\Delta P+\delta+R_f.
$$
Die Gewichte summieren sich zu null, ihr erstes Zeitmoment ist null und ihr Skalarprodukt mit dem Profilvektor $(0,1,1,0)$ ist eins. Konstante und lineare Zeitdrift fallen heraus. Für zweimal stetig differenzierbares $f$ mit $|\partial_t^2 f|\le M$ auf dem ganzen Block ist
$$
R_f=-\frac12\int_{h/2}^{3h/2} [\partial_t f(u)-\partial_t f(-u)]\,du,\qquad |R_f|\le M h^2.
$$
Die Schranke wird bei $f(t)=Mt^2/2$ erreicht. Sie gilt für Drift der Gruppenlaufzeit $z$. Bei direkter Analyse der Phase statt der Laufzeit muss für eine Laufzeitschranke die Frequenzableitung der zeitlichen Krümmung kontrolliert werden.

Direkt aus komplexen Daten kann man den Block bilden, indem man mit $Q_i=(H_J/H_A)(t_i,s_i,\omega)$ den Ausdruck $\frac12\operatorname{Im}\partial_\omega\log(Q_2Q_3/(Q_1Q_4))$ auswertet. Die logarithmische Ableitung ist lokal zweigunabhängig, solange alle vier Faktoren glatt und von null verschieden sind. Für eine absolute Phase an einer einzigen Frequenz liefert der halbierte Hauptwert des Produktarguments den Kontrast modulo $\pi$.

## Was für die Identifikation fehlt

$\Delta P$ und $\delta$ multiplizieren denselben Profilvektor. Zwei getrennte Spalten ändern den Rang des Designs daher nicht. Dieselbe Nichtidentifizierbarkeit gilt bei beliebig vielen Wiederholungen, solange alle Messungen dieselbe Kopplung an den Profilvektor behalten. Auch zwei J-Splits können eine gemeinsame profilgebundene Endpunktantwort teilen.

Ein Kontrollblock mit derselben Endpunktmodulation und unabhängig bekanntem Ausbreitungskontrast $\Delta P_c$ macht eine zusätzliche Gleichung verfügbar. Für
$$
D_c=\Delta P_c+\delta_c+R_{f,c}+\epsilon_c,\qquad
D=\Delta P+\delta+R_f+\epsilon
$$
gilt bei unabhängig belegter Übereinstimmung $|\delta-\delta_c|\le b$ und bekannten Fehlerhalbbreiten $|\epsilon|\le e$, $|\epsilon_c|\le e_c$:
$$
|(D-D_c+\Delta P_c)-\Delta P|\le b+M h^2+M_c h_c^2+e+e_c.
$$
Die Kontrolle kann insbesondere eine Anordnung mit bekanntem Nullkontrast verwenden. Die frühere Yukawa-Schranke am Endpunkt kann zu $b$ beitragen, sobald die lokalen Empfindlichkeiten und ihre Frequenzableitung kalibriert sind. Eine reine Wiederholung derselben Profiländerung liefert diese Information nicht.

## Rechenkontrollen

Wolfram Language prüft Rang drei sowohl für die Spalten Konstante, Zeit und Profil als auch nach Hinzufügen der zweiten Profilspalte. Für $f(t)=b_0+b_1t+b_2t^2/2$ gibt die symbolische Auswertung den Rest $-b_2h^2$. Der Integralvorfaktor für die allgemeine Schranke ist $h^2$.

Qiskit prüft die Phasenfassung mit einer Ein-Qubit-Zustandsvektorsimulation. Die vier kontrollierten Beiträge werden als Phasengatter $P(-\phi_1)P(\phi_2)P(\phi_3)P(-\phi_4)$ nach dem Hadamard-Gatter codiert. Aus den Pauli-Erwartungen folgt $\tfrac12\operatorname{atan2}(\langle Y\rangle,\langle X\rangle)$. Mit $h=0{,}2$, $\phi_i=3{,}11+0{,}2t_i+s_i(0{,}25+\delta)+b_2t_i^2/2$ ergibt dies

| $\delta$ (rad) | $b_2$ (rad pro Zeiteinheit²) | Phasenkontrast (rad) |
| --- | --- | --- |
| 0 | 0 | 0,250 |
| 0,013 | 0 | 0,263 |
| 0,013 | 0,4 | 0,247 |

Die Schaltung codiert vorgegebene Phasen. Die Endpunktkontrolle, physische J-Auslese, gemeinsame Messkarten und H96 bleiben offen.
