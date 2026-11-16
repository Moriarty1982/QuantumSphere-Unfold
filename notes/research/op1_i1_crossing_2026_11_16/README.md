# OP1 mit I1: Guard „T = String-Sektor“ rückwärts geprüft; Ersatz „T zählt Querungen“

16. November 2026, Claude Opus 5.5. **Erkundung (Lesart), nicht blind, ohne Rechnung und ohne Kriterium.** Auftrag des Autors:
„I1 verfolgen“, nach der Rückwärtssuche zu (S2) (`../op1_statistics_backward_2026_11_16/README.md`), die I1 als Ausweg vorgelegt hat.
Auslöser I1-3 ist getroffen. Keine H-Nummer, kein CT-Eintrag; das Register CT-004 wird nicht geändert. OP1 bleibt offen.

## Ausgangslage
Die I1-Lesart vom 15.11. (`../op1_i1_string_endpoints_2026_11_15/README.md`, Kandidat C3) sagt: T zählt Endpunkte einzelner offener
Strings; ein Endpunkt trägt die Fundamentaldarstellung, also j = ½ mit Gewicht 2. Damit wird (S2) überflüssig: j = ½ folgt aus der
Einzahl, nicht aus fermionischem Austausch. Die Lesart braucht aber Guard 1 von CT-004, **„T = String-Sektor“**, und der hat nach der
Berichtigung vom 15.11. keine Stütze im Bestand. Hier wird geprüft, ob es eine gibt oder einen Ersatz.

## Notwendige Bedingungen für einen Ersatz von Guard 1
- **(G1)** Was T an einer Punktierung zählt, muss einzeln auftreten: genau ein Strang je Punktierung.
- **(G2)** Das muss eine Eigenschaft des Tachyon-Frames sein, nicht beider Frames.
- **(G3)** Es darf nicht auf eine Statistik je Frame zurückgreifen, denn die ist aus der Frame- und Portstruktur nicht begründbar
  (Rückwärtssuche zu (S2)).

## Kandidaten
### K1: T11 (`thm:string-lqg-duality`) über die Ports
T11 ordnet zu: C = ½(1 + J) „symmetrisch, bosonisch – Stringtheorie“, A = ½(1 − J) „antisymmetrisch, fermionisch – LQG“. Welchen Port
liest welcher Frame? Dafür gibt es nach v4.10.0-r20.4(a) zwei Port-Begriffe:
- **Scheiben-Ports** (C5-Lesart, r04–r28): Die Tachyon-Abbildung vertauscht sie (r28). M liest C, T liest A. Nach T11 läse M dann den
  **String-Sektor** und T den **LQG-Sektor**: genau das Gegenteil von Guard 1.
- **Algebraische Ports** (r42/r51, Helizitätsachse): Die Tachyon-Abbildung lässt sie fest. M und T läsen denselben Port; T11 trennt
  die Frames dann gar nicht.

**Urteil:** T11 stützt Guard 1 in keiner Lesart, mit den Scheiben-Ports widerspricht es ihm. Das ist ein neuer Befund; er verschärft die
Berichtigung zu CT-004 vom 15.11.

### K2: der Name γ_string
γ_string heißt im Companion „string coupling“ (Nomenklatur v470/08). Der Wert ln 2/(π√3) ist aber die ABCK-Zählung der
Schleifenquantengravitation mit nur j = ½ (v4.9.0-r63); v4.8.0-r03 F11 nennt die Stringkopplung nur dem Namen nach. **Urteil:** keine
Stütze.

### K3: T ist der Kanal, der den Horizont quert
Der Bestand hat eine Stelle, an der der Tachyon-Frame eine eigene Rolle zwischen zwei getrennten Bereichen spielt:
- `thm:core`: Der Kern eines Schwarzen Lochs erreicht das Außen nur über einen Kanal, die Tunnelung durch den Horizont, und zwar als
  Tachyon („the only open channel“).
- `thm:hawking-triolic` mit dem Statusvermerk aus v4.9.0-r64(e): Der Tachyon fällt ein; γ_string ist nach der Zähl-Lesart (r63) die
  Zählung **des einfallenden Tachyons**.
- v4.9.0-r63.3: Ein Tachyon, der Energie verliert, läuft auf einen **einzigen** Boden zu.
- CT-002: „eine Querung“; Erkundung `../op3_i1_string_bridge_2026_11_14.md`: ein String zur Punktierung.

Gelesen mit I1: Die Brücke zwischen den getrennten Systemen ist das, was den Horizont quert, und das ist im Bestand der Tachyon. Eine
Punktierung des Tachyon-Frames ist dann eine **Querung**. Ist eine Querung ein einzelnes Quant von χ (Setzung S1 aus r17.5), trägt sie
genau einen Strang, also j = ½ mit Gewicht 2.
- (G1) erfüllt: eine Querung, ein Strang.
- (G2) erfüllt: Querungen gehören zum Tachyon (`thm:core`, r64(e)); M bleibt außen und zählt Kanten des Spin-Netzwerks mit beliebigem j.
- (G3) erfüllt: Es wird nichts ausgetauscht; j = ½ folgt aus der Einzahl.

**Urteil:** K3 ersetzt Guard 1 („T = String-Sektor“) durch **„T zählt Querungen des Horizonts, eine Querung trägt einen Strang“**. Die
Stütze sind `thm:core`, die Typisierung r64(e) und r63.3, nicht T11. Der String aus I1 ist in dieser Lesart kein eigener Sektor, sondern
die Weltlinie der Querung.

## Was sich damit ändert
| Setzung | vorher (I1, 15.11.) | nach K3 |
|---|---|---|
| Guard 1 von CT-004 | T = String-Sektor (ohne Stütze) | T zählt Querungen; Stütze `thm:core`, r64(e), r63.3 |
| (S2) Statistik je Frame | nötig, nicht begründbar | nicht nötig |
| (S1) Strang = Quant von χ | nötig | weiter nötig (eine Querung = ein Quant) |
| Chan–Paton | nötig | ersetzt durch (S1) |
| (S3) M nur ausgerichtete Bündel | nötig | weiter nötig; Lesart über strangweise Ports (Rückwärtssuche zu (S2), Ergebnis 3) |
| Spektrum a(j) = √(j(j+1)) | fest (H104) | unverändert fest |

Die „eine Querung“ von CT-002, der eine Kern aus OP3 und die Zählung in T fallen weiterhin auf dieselbe Stelle; jetzt mit einem Grund
im Bestand dafür, warum es gerade der Tachyon-Frame ist.

## Grenzen
- **Lesart, keine Herleitung.** `thm:core` ist eine Erzählung des Hauptkorpus ohne eigenen Statusvermerk; r64(e) ist eine
  Typisierung, kein Beweis.
- (S1) und (S3) bleiben gesetzt; die Sonderstellung des Paares hängt weiter am festen Flächenspektrum (H104).
- Warum M dieselben Punktierungen als Kanten mit beliebigem j zählt, also warum der Materie-Frame nicht auch Querungen sieht, ist nur
  durch „M bleibt außen“ gelesen, nicht gezeigt.
- **Kein Test.** Die Lesart reproduziert das Paar aus H98. Ein Test bräuchte eine Folge der Querungs-Lesart, die nicht γ_L ist, etwa für
  die Zahl der T-Punktierungen eines Horizonts im Verhältnis zu seiner Hawking-Rate. Eine solche Folge ist hier nicht abgeleitet.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
