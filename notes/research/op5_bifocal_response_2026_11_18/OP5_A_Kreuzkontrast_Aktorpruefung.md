# OP5: A-Port-Kreuzkontrast und Aktorprüfung

Erkundung im Materieframe M, gewöhnliche Optik und Elastizität. Ausgangspunkt ist die [A-Port-Auswertung](OP5_A_Port_Auswertung.md). Vom A-Phasenbudget führt die Rückwärtssuche zum gemischten Fehler aus Marker und Schaltzustand, vom lokalen Gegenhub zur Erreichbarkeit eines vorgegebenen Tensorpaars mit gemeinsamen Stellbefehlen.

## A-Port-Referenz

In der Reihenfolge Leerprobe aus/an, Marker aus/an sei \(K(z)=z_{11}z_{22}/(z_{12}z_{21})\), mit Vorzeichen \(s=(+,-,-,+)\). Die Lastgerade liefert den Interzept \(t\), der separate Direktstandard \(B\). Für einen separablen Multiplikator \(g_{ms}=a_m b_s\) gilt \(K(gz)=K(z)\) exakt pro Frequenz. Ein gemeinsamer additiver Offset kann den Kontrast verändern. Das Beispiel \((1,2,3,6)\) ergibt mit Offset \(1/10\) den Wert \(671/651\) statt \(1\).

Das Zentrum ist \(L_c=\sum_i s_i\log(\hat t_i/\hat B_i)\) auf den von der bisherigen Zellprüfung getragenen Zweigen. Unter den dortigen Nullabständen gilt
\[
 \frac{K(t)/K(B)}{K(\hat t)/K(\hat B)}
 =\frac{K(1+(t-\hat t)/\hat t)}{K(1+(B-\hat B)/\hat B)} .
\]
Für jeden relativen Radius \(r=\epsilon_t/|\hat t|\) bzw. \(r=\epsilon_B/|\hat B|\) begrenzen \(-\log(1-r)\) und \(\arcsin r\) den komplexen Logfehler und den Winkel. Die Auswertung addiert diese Terme zu \(|L_c|\) bzw. \(|\Im L_c|\). Je Größe nimmt sie das Minimum aus dieser und der bisherigen Zellhülle und addiert die Phasentransferschranke. Der bisherige Zellzweig bleibt Eingangsbedingung. Ein Hauptlogarithmus des Kreuzquotienten allein kann eine Windung der Zelllogarithmen verdecken.

Optional ersetzt ein kleinerer, unabhängig begründeter Vierzustandswert die Summe der Einzelgrenzen für denselben reinen Phasentransfer. Ein bekannter Direktpfad mit eigenen Sollwerten in allen vier Zuständen kann unter denselben Bezugs- und Lastbedingungen \(K(g)\) messen. Der Kalibriernachweis muss den signierten Phasenrest samt Drift und Transfer zur Nutzmessung abdecken. Die vier Nutzsignale allein lassen \(K(g)\) unbestimmt, weil ein beliebiger nichtseparabler Multiplikator zwischen Nutzsignal und Systemfaktor umverteilt werden kann. Eine Kalibrier-ID benennt die Quelle der Schranke. Bis zu einer eigenen Zweifrequenzkalibrierung addiert die Auswertung die Phasengrenzen beider Enden.

`python op5_a_cross_check.py --example-input` erzeugt ein synthetisches JSON-Beispiel. `python op5_a_cross_check.py --input Messung.json` verwendet das bisherige Schema und optional am jeweiligen Bandende `phase_transfer_contrast` mit `calibration_id` und `error_rad`. Dazu müssen alle vier Einzelgrenzen `extra_phase_error_rad` explizit vorliegen. Python rechnet mit Gleitkommazahlen. Ergebnisse unmittelbar an einer Schwelle erfordern eine Rundungsreserve. In den geprüften Projektpfaden lag kein als gemessen gekennzeichneter A-Port-Datensatz vor.

## Lokale Aktormessung

Je Materialprobe wird dieselbe mechanisch freie oder separat spannungskorrigierte Innenregion beobachtet. Sechs Normaldehnungen entlang \(e_1,e_2,e_3,(e_1+e_2)/\sqrt2,(e_1+e_3)/\sqrt2,(e_2+e_3)/\sqrt2\) bestimmen den Kelvin-Vektor \((\epsilon_{11},\epsilon_{22},\epsilon_{33},\sqrt2\epsilon_{12},\sqrt2\epsilon_{13},\sqrt2\epsilon_{23})\). Dessen euklidische Norm ist die Frobeniusnorm des Tensors. Wolfram ergibt für die Projektionsmatrix \(P\) den kleinsten Singulärwert \(0{,}46821319\) und den Rekonstruktionsfaktor \(\|P^{-1}\|_2=2{,}13577921\).

Pro Stellrichtung \(i\) werden symmetrische Schritte \(\pm h_i\) mit Rückkehr zur Basis gemessen. Aus der zentralen Differenz folgt die geschätzte Kelvin-Antwortspalte \(\hat m_i\). Ist der Erfassungsfehler je Projektion und Einzelmessung höchstens \(\epsilon_i\), \(\|P-\hat P\|_2\le E<\sigma_{\min}(\hat P)\) und die Norm der dritten Ableitung entlang der Stellrichtung höchstens \(L_i\), dann gilt
\[
 \|m_i-\hat m_i\|\le
 \delta_i=\frac{\sqrt6\,\epsilon_i/h_i+E\|\hat m_i\|}
                  {\sigma_{\min}(\hat P)-E}+\frac{L_i h_i^2}{6}.
\]
Der erste Summand folgt aus der inversen Projektionsabbildung und dem Messfehler der zentralen Differenz, der zweite aus dem Taylorrest beider Schritte. Abweichungen von Schrittkalibrierung, Drift oder Spannungszustand brauchen zusätzliche Hüllen, sofern sie in den Messgrenzen fehlen.

Mit \(\Delta=(\sum_i\delta_i^2)^{1/2}\) folgt \(\|M-\hat M\|_2\le\Delta\). Bei mindestens sechs Stellrichtungen sichert \(\sigma_{\min}(\hat M)>\Delta\) vollen Zeilenrang für eine Sechskomponentenprobe. Für das Komponentenpaar sind dieselben Stellbefehle in \(\hat M=(\hat M_1;\hat M_2)\) zu verwenden. Bei Gegenhub \(d_2=-d_1/c\) ist das Sollpaar \((e,-e/c)\). Ein Stellvektor \(q\) mit \(\|q\|\le Q\) hat für das nominelle Soll \(\hat e\) und Zielfehler \(\eta\) den Rest höchstens \(\|\hat Mq-\hat e\|+\Delta\|q\|+\eta\). Ein Einheitsvektor \(w\) mit
\[
 |w^\top\hat e|>Q(\|\hat M^\top w\|+\Delta)+\eta+\tau
\]
schließt das Ziel in Resttoleranz \(\tau\) für diese lineare Antwort aus. Beide Kriterien gelten direkt für das gestapelte Sollpaar. Bei endlichen Stellwegen kommt der Betrag eines separat begrenzten Nichtlinearitätsrests in beiden Schranken hinzu.

## Lauf und offene Voraussetzungen

Die [Wolfram-Rechnung](op5_a_cross_actuator.wl) kontrolliert die algebraischen Identitäten und die Projektionsmatrix exakt. Eine Quantenschaltung kommt in diesen Prüfungen nicht vor. Die [tatsächliche Ausgabe](op5_a_cross_actuator.txt) enthält außerdem synthetische Python-Prüffälle. Das Beispiel mit gemeinsamem Phasenfehler senkt die obere Schranke von \(1{,}982\cdot10^{-6}\) auf \(2{,}210\cdot10^{-7}\). Der affine Fehler in einer Zelle überschreitet weiterhin das Budget \(5\cdot10^{-7}\). Der gekrümmte Fall scheitert an der Modellprüfung.

Offen sind reale A-Referenz- und Transferwerte, lokale Antwortmatrizen einschließlich Stellweg, Nichtlinearität und Kopplung, die physische J-Ausbreitung sowie die native Metrik. OP5 bleibt offen.
