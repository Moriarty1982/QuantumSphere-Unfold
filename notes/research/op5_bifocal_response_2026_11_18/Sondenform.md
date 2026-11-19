# OP5: Welche radiale Sonde liefert die bifokale Form?

Analytische Erkundung, nicht blind, mit [vorab festgeschriebener Kontrolle](https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/9038b8b8dce2b95ee7c59a8f2e2cbd07b5bacc6f/notes/research/op5_bifocal_response_2026_11_18/Sondenform_Vorab.md). Gemeinsamer euklidischer Chart. Zwei Foki F_±=(±w,0), a>|w| und d_±=|x−F_±|. Verglichen werden gleich normierte, einzeln zugängliche Kanalantworten mit derselben radialen Funktion K. Bei tatsächlicher Überlagerung ungleich geladener Quellen ist eine Trennung und Normierung eine zusätzliche Voraussetzung.

## Exakte Formbedingung für die rohe Summe

Die Reparaturellipse ist x=(a cos t, √(a²−w²) sin t). Auf ihr gilt d_−=a+w cos t und d_+=a−w cos t. Setze S_K=K(d_−)+K(d_+). Die kleine Achse legt den einzig möglichen konstanten Wert auf der Ellipse als 2K(a) fest. Die exakte Anforderung an das Sondengesetz ist damit

    K(a+s)+K(a−s)=2K(a)   für jedes |s|≤|w|.

Bei festem a darf K einen um a ungeraden, auch nichtlinearen Anteil haben. Wird die Bedingung für jedes a in einem offenen Radienintervall und beliebig kleine nichtverschwindende w verlangt, folgt durch zweimaliges Differenzieren bei s=0, dass K″(a)=0. Dann ist K auf diesem Intervall affin. Umgekehrt liefert K(d)=A+Bd mit B≠0 überall exakt die geometrische Ellipse als Niveaukurve. Strikte Konvexität auf [a−|w|,a+|w|] schließt die Bedingung für jedes w≠0 aus, weil S_K am großen Scheitel strikt größer als an der kleinen Achse ist.

## Ergebnis für die vorhandene Yukawa-Sonde

Eine glatte Sonde mit K′(a)≠0 definiert für kleine |w| eine radiale Niveaukurve nahe dem Kreis. Setze ihren Wert am großen Scheitel x=(a,0) fest und verwende den Polarwinkel θ um die Mitte. Für einen Radius r=a+u mit u=O(w²) gilt

    S_K = 2K(a)+2K′(a)u
          + w²[(K′(a)/a) sin²θ + K″(a) cos²θ]+O(w⁴).
    D_K = K(d_−)−K(d_+) = 2w K′(a) cos θ+O(w³).

Hier und im Folgenden sei K hinreichend glatt für die angegebenen Reste. Aus dem Sollwert S_K(a,0)=2K(a)+K″(a)w²+O(w⁴) folgt die lokale Kurve

    r(θ)=a + (w²/2)[K″(a)/K′(a)−1/a] sin²θ + O(w⁴).

Die implizite Ableitung nach r ist bei w=0 gleich 2K′(a). Der dort bestimmte Zweig ist eindeutig und gerade in w. Die geometrische Reparatur hätte stattdessen u=−w² sin²θ/(2a)+O(w⁴).

Für den in [Grenze_W2.md](Grenze_W2.md) betrachteten Kernel K(d)=e^(−μd)/(4πd), μ≥0, gilt K′<0 und K″>0. Der Faktor der radialen Formänderung relativ zum geometrischen Soll ist

    1−a K″(a)/K′(a) = μa+2+1/(1+μa) ≥ 3.

Die rohe Yukawa-Summe liefert somit eine andere Niveaukurve, obwohl ihre Differenz einen signierten Dipol liefert. Die exakte Konvexitätsprüfung gilt auch für getrennte Foki außerhalb der Entwicklung um w=0. Im Coulomb-Grenzfall μ=0 schneidet die gleichwertige Kurve die kleine Achse bei b²=a²−3w²+w⁴/a², sofern dieser Wert positiv und a>|w| ist. Das folgt aus 2/√(b²+w²)=1/(a+w)+1/(a−w). Der geometrische Schnitt wäre b²=a²−w².

## Getrennte Signale als Auslese

Sind beide Werte Y_±=K(d_±) separat kalibriert verfügbar und ist K auf dem relevanten Intervall invertierbar, gilt punktweise

    S = K⁻¹(Y_−)+K⁻¹(Y_+),    D = K⁻¹(Y_−)−K⁻¹(Y_+).

Damit kann im gemeinsamen Chart der vorhandene Distanzmonitor S=2a und die signierte Größe D ausgelesen werden. Äquivalent genügen getrennt gemessene rohe Summe und Differenz, weil sich daraus Y_± zurückgewinnen lassen. Für die lokale geometrische Rückgewinnung von x=(x₁,x₂) ist der Jacobi der beiden Distanzwerte von Betrag |2w x₂|/(d_−d_+). Der Chart ist außerhalb der Fokusachse bei w≠0 lokal rekonstruierbar. Global bleibt die Spiegelung x₂↦−x₂, und am Kreisgrenzfall w=0 fallen die beiden geometrischen Richtungen zusammen.

Die [symbolische Kontrolle](sondenform_kontrolle.py) prüft die ungeraden und geraden Koeffizienten, die affine Kontrolle, den Yukawa-Faktor, den exakten Coulomb-Schnitt und den Jacobi. Sie speist kein mechanisches Gesetz ein. W2 enthält laut [Quellenabgleich](Grenze_W2.md) keine solche lineare neutrale Yukawa-Sonde. OP2 liefert im vorhandenen Stand einen phasensensitiven Kreuzterm und keine zwei unabhängig kalibrierten Entfernungssignale. Eine physikalische Formantwort bräuchte eine Wirkung, die den ausgelesenen Monitor in die Randgleichung einsetzt und die absolute Orientierung und Quellnormierung liefert. Der Ausleseschritt selbst bestimmt weder Rückstellenergie noch Zeitentwicklung. I3 bleibt als weitergehende Lesart an eine eigenständige Überschussdynamik gebunden. OP5 und H96 bleiben offen.
