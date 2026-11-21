# OP5 – Gekreuzte Schaltkontrolle für die A-Referenz

21. November 2026. Analytische Erkundung im Materieframe M. Ein Vier-Zustands-Vergleich soll den komplexen Schaltfehler der Einkanalreferenz an beiden Enden des illustrativen 100-MHz-Bands bestimmen. Die Rechnung gibt an, welcher Fehler dafür unabhängig gemessen werden muss.

## Vorwissen geprüft

Die [Einkanal-Nullreferenz](OP5_J_Einkanal_Nullreferenz.md) kürzt gemeinsame Anschlussfaktoren und affine zeitliche Drift des komplexen Loggewinns. Sie lässt den schaltabhängigen Gewinn als eigenständigen Fehler. Der [Matrix-Nullpfad](OP5_J_Nullpfad_Abgleich.md) begründet die Referenz im gleichen kohärenten Zweig. Die [Diagonalreferenz](OP5_J_Diagonalreferenz.md) trägt die verbleibende Kalibrierreserve. Im [Gesamtbild](../../../wiki/Gesamtbild.md) gehört der Vergleich zur lokalen Auslese. I3 braucht eine eigenständige kosmologische Bestandsdynamik.

## Vier Zustände und der verbleibende Produktfaktor

Sei $m=0$ ein Leerkörper und $m=1$ der Marker. $s=0,1$ bezeichnet die beiden Schaltstellungen. Alle komplexen Signale seien von null verschieden und an denselben Referenzebenen definiert. Der saubere A-Port-Quotient des Markers sei $q$, nach Aufteilung der bekannten Referenzübertragungen. Insbesondere muss die Nullstellung des Markers an der vorgesehenen Feldreferenz unabhängig verankert sein. Ein bekannter nichttrivialer Schaltkontrast des Leerkörpers ist vor der folgenden Rechnung zu dekonvolvieren. Unsicherheiten dabei gehen in die Fehlergrenze ein.

Bei festem Zeitpunkt schreibe das normierte Signal als
$$
Y_{ms}=H\,a_m b_s\,w_{ms}\,q^{ms},
$$
mit gemeinsamem komplexem Gain $H$, einem reinen Körperfaktor $a_m$, einem reinen Schaltfaktor $b_s$ und dem verbleibenden Zustandsterm $w_{ms}$. Der Kreuzquotient
$$
C(Y)=\frac{Y_{11}Y_{00}}{Y_{10}Y_{01}}=q\,C(w)
$$
kürzt $H$, $a_m$ und $b_s$ exakt. Ein Leerkörper mit derselben festen Übertragung in beiden Schaltzuständen darf daher eine andere feste Übertragung als der Marker haben. Das Verhältnis $C(w)$ misst die Änderung des Schaltgewinns zwischen Leerkörper und Marker. Jede Ersetzung $(q,w_{11})\mapsto(\lambda q,w_{11}/\lambda)$ mit $\lambda\ne0$ lässt alle vier Rohsignale identisch. Auch beliebig genaue Wiederholungen derselben Zustände trennen die Wechselwirkung dann erst mit einer zusätzlichen Referenz.

## Unabhängiger Kontrolltransfer

Ein möglicher zusätzlicher Messkanal ist ein kohärenter Kontrollton in denselben vier Zuständen. Nach Division durch seine unabhängig bekannte Übertragung $B_{ms}$ sei $Z_{ms}/B_{ms}=H_Z a'_m b'_s v_{ms}$. Bei identischen Messzeitpunkten bilde den zustandsweisen Quotienten
$$
X_{ms}=\frac{Y_{ms}}{Z_{ms}/B_{ms}}.
$$
Im stationären Fall ergibt sich $C(X)=q\,\Gamma$ mit $\Gamma=C(w)/C(v)$. Der Kontrollton braucht eine bekannte eigene Übertragung und einen geprüften Abgleich der Zustandseinflüsse. Eine hinreichende Bedingung ist $|\log\Gamma|\le d_\Gamma$ auf dem Zweig bei eins. Faktoren im Monitormissverhältnis, die nur vom Körper oder nur vom Schaltzustand abhängen, bleiben unschädlich. Gemessen oder unabhängig begrenzt werden muss die gemischte Änderung des komplexen Anschlussgewinns. Dazu müsste eine bekannte kohärente Übertragung unter beiden Körpern und beiden Schaltstellungen eingespeist werden, mit Bezug auf die durch den Schalter beeinflussten Anschlussabschnitte. Ein bloßer Bypass mit unbekanntem eigenem Wechselwirkungsrest liefert keinen Nachweis für $d_\Gamma$.

## Zeitliche Staffelung

Bei zeitversetzten Zuständen sei $g(t)=\log[H(t)/H_Z(t)]$ der stetig verfolgte differentielle Loggewinn. Die zustandsspezifischen Faktoren müssen für die Zeit der Sequenz stabil genug sein. Weitere zustandsabhängige Zeitänderungen gehören zum gemischten Rest oder zu einem gesondert begrenzten Modellrest. Beobachten Signal und Kontrollton denselben Gain am selben Zeitpunkt, kann die Differenz $g$ konstant sein.

Vier äquidistante Zeitpunkte mit Abstand $\Delta$ und Reihenfolge $00,01,10,11$ liefern Gewichte $(1,-1,-1,1)$. Der gemeinsame Driftterm ist $(1-E_\Delta)(1-E_{2\Delta})g(t)$, wobei $E_\tau$ um $\tau$ verschiebt. Bei $\sup|g''|\le K_2$ folgt durch zweimalige Integration der Ableitungen die Schranke $2K_2\Delta^2$. Affine Drift fällt exakt heraus. Der Kreuzquotient selbst kann direkt aus den komplexen Messwerten gebildet werden.

Acht äquidistante Zeitpunkte in der Reihenfolge $00,01,10,11,01,00,11,10$ erfassen jeden Zustand zweimal. Der Mittelwert der beiden Log-Kreuzquotienten hat Gewichte $(1,-1,-1,1,-1,1,1,-1)/2$. Damit bleibt der Driftterm $(1-E_\Delta)(1-E_{2\Delta})(1-E_{4\Delta})g(t)/2$. Bei $\sup|g'''|\le K_3$ folgt durch dreimalige Integration $4K_3\Delta^3$. Auch ein quadratischer gemeinsamer Loggewinn fällt exakt heraus. Für das geometrische Mittel der beiden Kreuzquotienten muss die relative Phase zwischen den Blöcken eindeutig festliegen. Der Phasenmonitor oder eine unabhängige Schranke aus der vorigen Einkanalrechnung liefert diese Information.

## Fehlerbudget je Bandende

Für die relativen komplexen Messfehler jedes Signal- und Monitorwerts gelte $|\epsilon|\le e<1$. Beide Messfolgen haben Summe vier der absoluten Kreuzgewichte. Damit ist der Beitrag der acht beziehungsweise sechzehn relativen Messwerte zu $|\log(\widehat q/q)|$ höchstens $-8\log(1-e)$. Dies ist eine deterministische Schranke. Absolute Gerätefehler müssen jeweils auf die tatsächlich verfügbare Signalamplitude bezogen werden. Mit Driftgrenze $B_{\rm Drift}$ folgt
$$
|\widehat q-q|\le |q|\left[\exp\bigl(d_\Gamma+B_{\rm Drift}-8\log(1-e)\bigr)-1\right].
$$

Übernehme die bisherige illustrative Aufteilung. Die Projektion bleibt auf $2\cdot10^{-6}$ begrenzt, sodass $|q|\le1+2\cdot10^{-6}$ für den passiven Marker. Für Schaltkontrolle, Drift und Messfehler zusammen stehen $2\cdot10^{-6}$ zur Verfügung. Bei $e\le10^{-7}$ pro Signal- und Monitorwert sowie $d_\Gamma\le5\cdot10^{-7}$ bleiben rund $7{,}00\cdot10^{-7}$ im differentiellen Loggewinn. Für $\Delta=0{,}25$ s genügen folgende separat an beiden Bandenden belegte Grenzen.

| Sequenz | Hinreichende Ableitungsgrenze |
| --- | ---: |
| Vier Zustände | $K_2\le 5{,}59\cdot10^{-6}\ {\rm s}^{-2}$ |
| Acht Zustände | $K_3\le 1{,}119\cdot10^{-5}\ {\rm s}^{-3}$ |

Unter dieser Aufteilung bleiben $5{,}96\cdot10^{-7}$ für übrige Beiträge. Die Grenzen sind Anforderungen an eine noch zu vermessende Referenz. Der A-Kontrollton bestimmt die HCl/H-Zweikanal-Singulärzahl nicht. Freie J-Ausbreitung, native Kopplung und H96 bleiben offen.

## Rechenkontrolle

Wolfram prüfte die beiden Quotientenidentitäten, die Unbestimmtheit ohne unabhängige Referenz und beide Differenzenpolynome exakt. Beide gerundeten Ableitungsgrenzen erfüllen die nichtlineare Fehlerhülle. Qiskit wurde erwogen. Die Rechnung benötigt klassische komplexe Transferkoeffizienten und keine Quantenschaltung.

[Wolfram-Skript](op5_j_gekreuzte_schaltkontrolle.wl) · [Tatsächliche Ausgabe](op5_j_gekreuzte_schaltkontrolle.txt) · [Laufmanifest](op5_j_gekreuzte_schaltkontrolle.json)
