# OP1: Vorprüfung „einheitliche Flussauslesung in R“ – statt Vorab-Notiz (Erkundung, analytisch, nicht blind)

16. November 2026. Auftrag des Autors: „Vorab-Notiz aufsetzen“ für die Erkundung „Flussauslesung in R“ (eine Auslesung im Bezugsframe R; M bei
Rapidität η, T bei −η + iπ/2; Umrechnung nur über Konvention F). Beim Vorwissen zeigte sich, dass das Ergebnis der geplanten Konstruktion
**analytisch feststeht**. Nach der Regel „Nicht blind = offen sagen“ wird deshalb **keine H-Nummer** vergeben; diese Notiz hält die Vorprüfung fest.
Skript `precheck.py`, Ausgabe `run/precheck_stdout.txt`.

## Vorwissen geprüft
- v4.9.0-r61.1(b), r61.1(c): Der Hopf-Fehler war die Gleichsetzung eines R-Ergebnisses mit dem M-Versatz, nicht das Rechnen in R; γ_L ist
  frame-konsistent als Lorentzfaktor der reellen Projektionen von M und T und als Verhältnis |b_R|/|b_M|.
- v4.9.0-r63.3, r63.4: Tachyon-Boden bei η_X + iπ/2; der Boden des Spiegelframes −η hat zu M den Abstand cosh 2η = γ_L.
- v4.10.0-r10.1, r10.2: Über das lokale erste Gesetz und die Unruh-Temperatur zählen alle statischen Beobachter gleich, auch T.
- v4.10.0-r10.3: Die Zählregel ist gleichwertig mit einem frame-abhängigen Flächenquant; „a reason would have to come from the boost part of the
  frame map …, which only reparametrizes the horizon. No such reason is known.“
- **v4.10.0-r10.4(c):** „A passive, invertible change of description cannot remove spin sectors; a T reading restricted to j = ½ is either a
  restricted readout of the same state … or a selection with its own weight.“
- `../op1_u1_check_2026_11_16/`, `../op1_s1_check_2026_11_16/` (mit Literaturnachtrag): U1 = Flussauslesung längs der Normalen.

## Die Konstruktion und warum sie entschieden ist
Geplant war: eine feste Auslesung in R, der Projektor P auf die Extremzustände |j, ±j⟩ längs der Achse u (die M-Maske), angewandt auf Objekte, die
aus demselben Zustand durch Boosts entstehen, $D_M=e^{\eta K}$ und $D_T=e^{(-\eta+i\pi/2)K}$. Gezählt wird der Rang des Effekts $D^\dagger PD$ je Spin.

**Satz (Form von r10.4(c)).** Ist D invertierbar und erhält D die Spinsektoren ($[D,J^2]=0$), dann hat $D^\dagger PD$ in jedem Sektor denselben Rang
wie P. M und T zählen dann gleich, beide mit Gewicht 2 je j. Die T-Regel (nur j = ½) kann so nicht entstehen.

Nachgerechnet für j = ½ bis 5, Boost längs u und quer dazu (η = 0,6, der Wert spielt keine Rolle): Rang 2 in jedem Sektor für M und für T;
$|[D,J^2]|\le 8{,}5\cdot10^{-12}$.

Damit ist die geplante Erkundung ohne Rechnung entschieden: **Eine einheitliche Auslesung in R mit sektorerhaltenden Frame-Abbildungen gibt keine
M/T-Asymmetrie.** Das bestätigt r10.4(c) für die Flussauslesung.

## Was offen bleibt (die zwei Auswege, die der Satz lässt)
1. **Verschiedene Objekte statt verschiedener Frames.** Die Asymmetrie sitzt dann im Zustand, nicht in der Auslesung: M-Stränge sind Flusslinien,
   T-Stränge sind Querungen (r24.4). Die Auslesung in R kann einheitlich bleiben; sie sieht zwei verschiedene Objektarten. Das ist eine Aussage über
   die Physik der Stränge, nicht über den Frame.
2. **Sektormischende Boosts.** Der Satz braucht $[D,J^2]=0$. In der Lorentz-Darstellung der Spinschaum-Modelle (EPRL, Simplizitätsbedingung
   K = γL) zerlegt sich eine Lorentz-Irrep in SU(2)-Spins j, j+1, …, und Boosts mischen sie. Das wäre genau der „boost part“, den r10.3 als einzig
   möglichen Ort nennt, und er enthält γ selbst. Literatur dazu (EPRL; Bianchi, arXiv:1204.5122, lokaler Rindler-Horizont aus dem Boost-Hamiltonian)
   ist hier **nicht geprüft**.

## Folgerung
Keine Vorab-Notiz für die Konstruktion in der geplanten Form, denn ihr Ausgang steht fest (M und T zählen gleich). Ein Test ist nur für einen der zwei
Auswege sinnvoll. Weg 2 wäre der, der eine Zahl liefern könnte; er verlangt zuerst die Literaturprüfung zu EPRL und Bianchi. OP1 offen; H98, H102
unverändert; keine H-Nummer vergeben (H111 und k233 bleiben frei).

## Nachtrag (16.11.2026): Literatur zu Ausweg 2 (EPRL, Bianchi)
Auftrag des Autors: „Literatur EPRL/Bianchi“. Gelesen über alphaXiv: Engle–Livine–Pereira–Rovelli, „LQG vertex with finite Immirzi parameter“,
arXiv:0711.0146; Bianchi, „Entropy of Non-Extremal Black Holes from Loop Gravity“, arXiv:1204.5122. Skript `spectrum_order.py`, Ausgabe
`run/spectrum_order_stdout.txt`.

**1. Sektormischende Boosts gibt es.** In EPRL (Lorentz-Fall) wählen die Simplizitätsbedingungen ρ = γn und k = n/2, also die **niedrigste**
SU(2)-Darstellung in $H_{(n,\rho)}=\bigoplus_{k\ge n/2}H_k$. Die Bedingung L − K/γ ≈ 0 (bzw. K = γL bei Bianchi) gilt nur schwach, als
Matrixelemente auf dem Bild der Y-Abbildung. Ein Boost führt aus diesem Bild hinaus in die höheren k. Bianchi zeigt es direkt: Die Eigenzustände
|λ⟩ des Boost-Generators K_z sind keine Flächeneigenzustände; ein Zustand |j⟩ hat eine Verteilung über λ mit Mittel γj. Die Voraussetzung
$[D,J^2]=0$ des Satzes aus der Vorprüfung gilt für Lorentz-Boosts in γ-einfachen Darstellungen also **nicht**; Ausweg 2 ist formal offen.

**2. Aber der Boost-Weg macht γ und den Beobachter unsichtbar.** Bianchi definiert den Quanten-Rindler-Horizont über den Boost-Hamiltonoperator
$H=\sum_f\hbar K^z_f a$, mit Facettenzuständen |j⟩ = |(γ(j+1), j); j, **+j**⟩ (größte magnetische Zahl längs der Normalen). Ergebnisse: Energie
⟨H⟩ = A a/(8πG) (Frodden–Ghosh–Perez), Temperatur ℏa/2π unabhängig von j und γ, Entropie je Facette 2πγj, insgesamt **S = A/4 für jeden Wert
von γ**; die Entropiedichte hängt nicht vom Abstand des Beobachters ab. Das ist r10.1/r10.2 in kovarianter Form: Der Boost-Teil liefert keinen
frame-abhängigen Flächenquant, und γ wird durch die Entropie gar nicht festgelegt („the entropy of large black holes is independent from the
Immirzi parameter“). Der in r10.3 als einziger möglicher Ort genannte Boost-Teil gibt in der Literatur also gerade **keine** Zahl.

**3. Was das für die Zählregel und für H102 heißt.**
- Der Wert γ_M = 0,237533 ist eine Eigenschaft der **Flächen-Ensemble-Zählung** (mikrokanonisch, ABK/DL). Im kovarianten, thermischen Zugang fällt γ
  aus der Entropie heraus. Die Frage OP1 verschiebt sich damit noch einmal: nicht nur „warum U(1)“, sondern „warum zählt der Frame M mikrokanonisch
  im Flächen-Ensemble“.
- Bianchis Facettenzustände sind die Extremzustände längs der Normalen. Das stützt U1 (Achse = Normale) und U2 (Extremzustand) auch im kovarianten
  Bild, dort aber ohne Zählgewicht.
- **Neue Grunddaten-Empfindlichkeit:** EPRL weisen auf eine Ordnungsmehrdeutigkeit des Flächenspektrums hin (√(j(j+1)) oder j bzw. j + ½). Die
  DL-Zählung gibt dann γ = 0,237533 / 0,349699 / 0,220636 und die H102-Beziehung π/4 − γ/2 = 0,666632 / 0,610549 / 0,675080. H102 hängt also
  zusätzlich an der Wahl √(j(j+1)).

**4. Zirkelregeln auf Ausweg 2 angewandt.** Ein Test über sektormischende Boosts müsste γ als freie Größe führen und eine Selbstkonsistenz suchen,
die es festlegt. Bianchi zeigt, dass die naheliegende thermische Selbstkonsistenz (Clausius mit Unruh-Temperatur) γ gerade **nicht** festlegt. Ein
solcher Test bräuchte also eine zusätzliche Bedingung, die im Bestand nicht steht. Ein Test wird hier nicht angelegt.

**Folgerung.** Ausweg 2 ist formal offen (Boosts mischen Sektoren), physikalisch aber in der Literatur gerade der Weg, auf dem γ und der Beobachter
herausfallen. Der verbleibende Ausweg ist 1 (verschiedene Objekte: Flusslinien gegen Querungen). OP1 offen; H102 unverändert, mit einer weiteren
benannten Abhängigkeit (Spektrumsordnung).
