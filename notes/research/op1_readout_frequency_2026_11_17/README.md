# OP1: Mit welcher Frequenz liest M aus? (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „weiter“, nach `../op1_flux_lines_2026_11_17/` (Nachtrag: Die Breite von M setzt eine Frequenz voraus; gesucht ist
die Frequenz, mit der M ausliest). Literatur zuerst, dann eine kurze Rechnung. Skript `qnm_rules.py`, Ausgabe `run/qnm_rules_stdout.txt`. Nicht blind:
Zählgewichte und γ-Werte sind bekannt, die Rechnung ist elementar. Keine H-Nummer.

## Vorwissen geprüft
- Bestand: r17.1 (Photonuhr; Gleichsetzung von Uhr- und Feldfrequenz vom Quelltext abgelehnt, v4.9.0-r12), r17.4 (Barbero-Verbindung als Punkt
  des Dubletts (A₊, A₋): reelles γ auf dem Äquator, γ = ±i an den Polen), r16.8 (zeitharmonische Felder).
- `predictions/Vorab_Notiz_H104_Zaehlregel_Flaechenspektren.md`: (L, A, 2) gibt γ = ln 3/π = 0,3497 (linear, alle Spins, Gewicht 2). Den Bezug
  zu den Quasinormalmoden hatte das Repo nicht (Suche nach „quasinormal“, „Dreyer“: keine Fundstelle vor dieser Notiz).
- r28.3: Mit j statt √(j(j+1)) gibt die Gewicht-2-Regel 0,3497.

## Literatur
- **Dreyer** ([gr-qc/0211076](https://arxiv.org/abs/gr-qc/0211076)): Bohr-Korrespondenz mit der Quasinormal-Frequenz ω = ln 3/(8πM) (Hod; analytisch
  Motl) gibt das Flächenquant ΔA = 4 ln 3; mit Standardspektrum und 2j + 1 Zuständen folgt j_min = 1 und γ = ln 3/(2π√2) = 0,1236 (SO(3) statt SU(2)).
- **Corichi** ([gr-qc/0212126](https://arxiv.org/abs/gr-qc/0212126)): j_min = 1 aus Fermionzahl-Erhaltung, SU(2) bleibt; derselbe Wert 0,1236.
- **Polychronakos** ([hep-th/0304135](https://arxiv.org/abs/hep-th/0304135)): Ein äquidistantes Spektrum versöhnt Quasinormalmoden und
  Bekenstein–Hawking, mit Entartung n + 1 (Kondensat aus Spin 1) oder 2n + 1 (nur ganze Spins, unterscheidbare Kanten). Gewicht 2 kommt dort nicht vor.
- **Frodden–Geiller–Noui–Perez** ([1212.4060](https://arxiv.org/abs/1212.4060)): Mit γ = ±i (selbstduale Ashtekar-Variablen) und der Fortsetzung
  j → is − ½ (Hauptserie von SU(1,1)) ergibt sich S = A/4 ohne Festlegung von γ; ein makroskopischer Zustand verlangt die Hawking-Temperatur.
  Im Bild von r17.4 sind γ = ±i die Pole des Dubletts, also die Lage der Ports.

## Rechnung

| Spektrum | Regel | γ | kleinstes Flächenquant 8πγ a(½) |
|---|---|---|---|
| √(j(j+1)) | M (alle j, Gewicht 2) | 0,237533 | 5,170 |
| √(j(j+1)) | P (alle j, 2j + 1) | 0,274067 | 5,965 |
| √(j(j+1)) | T (nur j = ½, Gewicht 2) | 0,127384 | 2,773 = 4 ln 2 |
| linear j | **M (alle j, Gewicht 2)** | **0,349699 = ln 3/π** | **4,394 = 4 ln 3** |
| linear j | P (alle j, 2j + 1) | 0,390868 | 4,912 |
| linear j | T (nur j = ½, Gewicht 2) | 0,220636 = ln 2/π | 2,773 = 4 ln 2 |

Quasinormal-Quant nach Dreyer: ΔA = 4 ln 3 = 4,394.

1. **Nur die Regel von M mit linearem Spektrum trifft das Quasinormal-Quant.** Mit a(j) = j ist die Zählgleichung eine geometrische Reihe,
   Σ_{n≥1} 2xⁿ = 1 mit x = e^{−πγ}, also x = ⅓ und γ = ln 3/π; der kleinste Schritt (Δj = ½) hat die Fläche 8π·γ·½ = 4 ln 3, genau Dreyers ΔA.
   Die Bohr-Frequenz dieses Schritts ist damit die Quasinormal-Frequenz ln 3/(8πM). In der Sprache von Polychronakos (unterscheidbare Kanten,
   Z₁ = 1): Entartung 2 je Kante, Fläche n·4 ln 3 (n = 2j ≥ 1), β_c = ¼, also Bekenstein–Hawking und Quasinormal-Quant zugleich, ohne SO(3) und ohne
   j_min = 1. Diese Kombination steht in keiner der gelesenen Arbeiten; ob sie anderswo steht, ist nicht geprüft.
2. **Mit dem Spektrum √(j(j+1)) des Bestands passt keine Regel.** M hat das kleinste Quant 5,170, P 5,965; beide weichen vom Quasinormal-Quant ab.
   T trifft in beiden Spektren 4 ln 2, das Bit-Quant von Bekenstein; das ist die bekannte ABK-Lesart, keine Quasinormal-Frequenz.
3. **Preis.** Mit linearem Spektrum wird γ_L = γ_M/γ_T = log₂ 3 = 1,585 (exakt) und β² = Ω_M = 0,226 statt 0,302. Das widerspricht den Fenstern von
   H98 (Ω_M, m_W) und dem Leptonfenster; die Datenpaarung des Bestands verlangt √(j(j+1)).

## Einordnung
- **Antwort auf die Frage (Lesart):** Die einzige Frequenz, die die Literatur einem Horizont ohne Zusatzannahme zuordnet, ist die asymptotische
  Quasinormal-Frequenz. Sie passt genau zur Gewicht-2-Regel von M, aber nur mit äquidistantem Spektrum. Das ist eine Gabel: Liest M mit der
  Quasinormal-Frequenz aus, dann ist das Flächenspektrum linear, und die Datenpaarung von H98 (γ_L = 1,8647) fällt; hält man an √(j(j+1)) fest, hat
  M keine Quasinormal-Frequenz.
- **Zweiter Kandidat:** Die Hawking-Temperatur bei γ = ±i (FGNP). Sie gehört zu den Polen des Dubletts (A₊, A₋), also zur Lage der Ports, und gibt
  keine Zahl für γ, weil γ dort nicht festgelegt wird. Die Breite von M liegt zwischen Äquator (reelles γ) und Pol (γ = ±i).
- **Bezug zu `../op1_flux_lines_2026_11_17/`:** Quasinormalmoden sind gedämpfte, zeitharmonische Felder mit komplexer Frequenz; sie haben
  relative Phasen und damit eine Breite ungleich null. Sie sind also der Art nach der Feldtyp, den die Breite von M verlangt.
- Nicht blind, keine H-Nummer. Ein Test wäre nur sinnvoll, wenn ein Datum das Flächenspektrum unabhängig entscheidet; im Bestand ist es gesetzt.
  OP1 offen.

## Ergebnis in einem Satz
Die Quasinormal-Frequenz ist genau die Übergangsfrequenz der Gewicht-2-Regel von M, aber nur bei linearem Flächenspektrum (γ = ln 3/π, Schritt
4 ln 3); mit dem Spektrum √(j(j+1)) des Bestands und seiner Datenpaarung passt sie nicht. OP1 offen.
