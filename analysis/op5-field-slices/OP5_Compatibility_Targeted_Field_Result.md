# OP5: gezielte zeitliche Kompatibilität im Feldansatz

29.10.2026. Unveränderte quadratische Familie und Region, tatsächliche401 Trainingspunkte (337 bisherige und64 gleichmäßig über8 Flächen verteilte Punkte). Gemeinsamer Ausgang OP5_Peak_Mixed_Check.json. Notwendige skalare Zustandsbedingung bleibt durch Normierung erfüllt.

Aus der exakten Formel L=A H^{-1} wird die orthogonale linke Restkomponente p=L^T(LL^T)^{-1}LF berechnet. Reell gepackt hat L vier Zeilen; die bereits erfüllte skalare Kombination wird nicht als neue Bedingung gezählt. Die Projektionsnorm berücksichtigt die willkürliche Zeilenbasis, anders als eine unnormierte Summe von vier Bedingungswerten. Sie ist ein Maß für drei verbleibende Kompatibilitätskombinationen dieses Kandidaten. Keine neue physikalische Gleichung.

Zwei L-BFGS-Läufe ab demselben Feld: Mittelwert von ||F||² versus ||F||²+4||p||², gleiche maximal400 Iterationen. Tatsächlich nur20 bzw24 Closure-Aufrufe bis zur internen Beendigung; keine vollständige Ausschöpfung behauptet. Die Coframe-Rückwirkung und Feldabhängigkeit der Projektion werden im Gradienten mitgeführt. Geometriestrafen unverändert.

Unangetastete1024 Innenkontrollpunkte seed291048: Ausgang voller RMS .000117144, Kompatibilitäts-RMS .0000545424. Nach normaler Fortsetzung .000111100 bzw .0000542728; nach gezielter Gewichtung .000110943 bzw .0000539296. Die gezielte Variante verbessert die Kompatibilitätskomponente gegenüber der normalen nur um etwa.6%, den vollständigen RMS um etwa.14%. Kontrollmaxima .000276149 versus .000276416: kein Vorteil bei den Maxima.

Alle geprüften Coframes regulär und g^{00}<0. Die zusätzliche Gewichtung allein löst die drei Bedingungen somit nicht. Insbesondere ist dies kein Beleg, dass sie exakt kompatibel oder grundsätzlich unvereinbar sind. Das frühe Optimierungsende ist eine konkrete numerische Einschränkung dieses Versuchs.

Konsequenz: Die Bedingungen sind nun explizit berechenbar, differenzierbar und auf dem gemeinsamen Feld ausgewertet. Eine stärker gewichtete Strafe beseitigt sie nicht automatisch. Für wirkliche Zwangserfüllung ist ein Verfahren mit direkt gelösten Kompatibilitätsgleichungen bzw. einer begründeten Zustandsparametrisierung zu untersuchen; die verbleibende regionale Fortpflanzung darf nicht aus einem kleineren Strafterm abgeleitet werden.

Artefakte OP5_Compatibility_Targeted_Field_Check.py/.json, benötigen gespeicherte Vorläuferfelder und Torch/NumPy-Evaluator. Beide Koeffizientensätze separat gesichert. Lokal gespeichert, nicht committed; Paper-Grafik unverändert, OP5 offen.
