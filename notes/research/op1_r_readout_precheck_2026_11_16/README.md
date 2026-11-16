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
