# Ergebnis H168: Die Sektoren unterscheiden sich durch die Ladungsmischung (0 neutral, 1 geladen) und teilen einen Versatz; eine gemeinsame feste Skala scheidet als Quelle aus

**26.11.2026. Vorab-Notiz `Vorab_Notiz_H168_Skala_und_Sektoren.md` (Commit 27d4e39; a, b, c nicht blind, d und e blind). Skripte `k363_test_h168.py`
(`k363_out.txt`), `k363b_gegenprobe.wl` (`k363b_out.txt`, Wolfram). Status: H168a bestätigt mit einer Berichtigung; H168b, c bestätigt (nicht blind);
H168d, e bestätigt (blind).**

Anlass: Autor, 26.11.2026: „prüfe ob die skale mit den sektoren zusammenhängt, es könnte nämlich beides sein.“ „Sektoren“ ist hier als Fermionsektor gelesen
(geladene Leptonen, Neutrinos). Gesetzt wie in H167: Postulat J, K = ⅔ in beiden Sektoren, Brannen-Form auch für Neutrinos (wie H99), c = 1 für den geladenen
Sektor. Werkzeuge: Python, Wolfram unabhängig; alle gemeinsamen Zahlen stimmen überein. Eine erste Wolfram-Fassung hatte einen Sortierfehler (in `k363b_out.txt`
offengelegt). Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H168a | c = 0: Minima χ + kπ/2 gefaltet 0, π/6, π/3; c = 1: π/12, π/4. π/6 − π/12 = π/12 | symbolisch | **bestätigt** (nicht blind); Berichtigung: die Vorab-Notiz nannte für c = 0 nur 0 und π/6 |
| H168b | δ_e = π/12 − x, δ_ν(H99) = π/6 − x mit x = 0,0395773407; Differenz 0; als Mischung c_e = 0,9238205, c_ν = −0,0395980 | Identität 10⁻¹² | **bestätigt** (nicht blind) |
| H168c | R_obs = 0,030016 ± 0,000457; R(π/6) = 0,040721 (+23,4σ); R(π/6 − x) = 0,030839 (+1,80σ); (Σ√m_ν/Σ√m_ℓ)² = 3,2·10⁻¹¹, also x_ν = 1,2·10⁻¹² bei gemeinsamem Λ | > 5σ | **bestätigt** (nicht blind) |
| H168d | Von acht Kandidaten liegt nur π/6 − x innerhalb 3σ; die anderen zwischen 50σ und 535σ. Daten verlangen x_ν = 0,04336 ± 0,00213 gegen x = 0,03958 (−1,78σ) | genau einer | **bestätigt** |
| H168e | 360 Vergleiche, 0 Treffer; nächster γ_M/6 gegen tan x (2,3·10⁻⁴) und γ_M/2 gegen 3x (2,9·10⁻⁴, das ist H102) | kein Treffer vorhergesagt | **bestätigt** |

## Lesart
- **Was die Sektoren unterscheidet.** Mit einem einzigen Term je Sektor, dem Spin-1-Term, hängt die Lage des Minimums nur an der Ladungsmischung c. Für c = 0
  liegt es bei π/6 (bzw. 0 und π/3 beim anderen Vorzeichen), für c = 1 bei π/12 und π/4. Der Abstand π/6 − π/12 = π/12 ist genau die Verschiebung zwischen
  Neutrino- und Lepton-Phase aus H99, für die es bisher keine Herleitung gab. Lesart: neutral heißt c = 0, geladen heißt c = 1.
- **Was die Sektoren teilen.** Beide liegen um denselben Betrag x = 0,0396 unter ihrem Minimum. Die Neutrino-Daten verlangen x_ν = 0,0434 ± 0,0021, also x
  innerhalb 1,8σ (das ist H99 in anderer Form, keine neue Bestätigung).
- **Zur Frage nach der Skala.** Die Massenskalen der beiden Sektoren unterscheiden sich so stark, dass ein Term sechster Ordnung mit gemeinsamem Λ den
  Neutrinosektor gar nicht verschiebt: x_ν wäre 10⁻¹², und R = 0,0407 liegt 23σ neben den Daten. Der Versatz kommt also nicht aus einer festen gemeinsamen Skala.
  Es bleiben zwei Möglichkeiten, und sie sind gleichwertig: Der Versatz ist eine dimensionslose Zahl (Konjugationsterm oder ein gemeinsamer Drehwinkel der
  Mischung), oder die Skala hängt am Sektor, Λ_s ∝ v_s. Im zweiten Fall ist β₃v_s²/Λ_s² in beiden Sektoren gleich, also wieder eine dimensionslose Zahl.
  „Beides“ trifft in diesem Sinn zu: Eine Skala kann beteiligt sein, aber nur als Sektorskala, und für die Phase zählt allein das Verhältnis.
- **Ein Hinweis auf skalenfrei.** Die Phase und der Versatz sind in beiden Sektoren dieselben Zahlen, obwohl die Massen um elf Größenordnungen auseinanderliegen.
  Das ist das Verhalten einer skalenfreien Größe. Es ist ein Hinweis, kein Beweis, und es hängt an H99.

## Nachträglich (nicht in der Vorab-Notiz)
- Für c = 0 und das Vorzeichen, das π/6 gibt, sind beide Minima gleichwertig; der neutrale Sektor braucht keine Zweigwahl. Für c = 1 gibt es bei jedem
  Vorzeichen zwei verschiedene Zweige (π/12 und π/4), und erst Ordnung 6 wählt (H167). Die Zweigwahl ist also nur im geladenen Sektor nötig.
- Im Neutrinosektor ist die leichteste Wurzel negativ (−0,196), wie in H99. Massen bei π/6 − x: 0,38; 8,81; 50,11 meV.
- Der Konjugationsterm aus H167 kann den gemeinsamen Versatz nicht liefern: Für c = 0 ist er dieselbe Funktion wie der Spin-1-Term und verschiebt nichts.
  Der gemeinsame Versatz passt besser zu einem gemeinsamen Drehwinkel der Mischung (χ → χ − x in beiden Sektoren). Das war nicht Gegenstand eines Kriteriums.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H167 | Skala, J, c = 1 | Oktant; Phase aus dimensionslosen Termen | warum c = 1; ein kleines Verhältnis |
| H168 | dazu: Brannen-Form für Neutrinos, c = 0 neutral | π/12 zwischen den Sektoren; Versatz nicht aus fester gemeinsamer Skala | ein gemeinsamer Versatz x = 0,0396 (dimensionslos); warum c = 0 und 1 |

Die offene Wahl ist jetzt eine einzige Zahl für beide Sektoren. Geprüft: x ist aus Messgrößen bestimmt (m_μ/m_e); die Zuordnung c = 0 und 1 ist eine Lesart.

## Grenzen
- Alles steht unter H99 (Brannen-Form mit K = ⅔ für Neutrinos; heute +1,8σ, JUNO an der 2σ-Grenze). Fällt H99, fallen b, c und d.
- Quarks nicht gerechnet (H1: δ = 2/9 gilt dort nicht). Nur der Zirkulantensektor, Baumniveau.
- „Sektor“ als Frame (H144) ist nicht geprüft.
- Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Keine neue Datenvorhersage.
- Vergeben: H168, k363. Nächste frei: H169, k364.
